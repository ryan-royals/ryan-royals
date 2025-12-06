---
{"dg-publish":true,"dg-path":"Slipbox Notes/Managed Identity can not add members to a Group it is the owner of.md","permalink":"/slipbox-notes/managed-identity-can-not-add-members-to-a-group-it-is-the-owner-of/","tags":["notes"],"created":"2025-12-04","updated":"2025-12-04"}
---

When using Terraform's [[90_slipbox/AzureAD Provider\|AzureAD Provider]] `azuread_group_member` resource to add managed identities to Azure AD groups, you may encounter a 403 Authorization_RequestDenied error even when the principal running Terraform is an owner of the target group.

``` bash
Error: Retrieving member "<member-id>" for group with object ID: "<group-id>"

unexpected status 403 (403 Forbidden) with error:
Authorization_RequestDenied: Insufficient privileges to complete the operation.
```

## Why This Happens

The `azuread_group_member` resource calls the Microsoft Graph API to manage group memberships. When adding [[Azure User Assigned Managed Identity\|Azure User Assigned Managed Identity]]'s (or service principals) to groups, the API requires additional permissions beyond group ownership:

- **Group ownership** is sufficient for adding regular users
- **Adding managed identities/service principals** requires the ability to read Application objects, which needs explicit Graph API permissions

This is not shown in the provider docs: <https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/group_member#api-permissions>

## Resolution

The managed identity or service principal running Terraform needs these Microsoft Graph **Application permissions**:

1. **`Application.Read.All`** - Required to read service principal/managed identity objects
2. **`Directory.Read.All`** - Required for directory read operations

These permissions are not Entra Roles, but are on the API side (Think Management plane vs Data plane in Azure)

### Script Example

```bash
#!/bin/bash

# Script to grant Microsoft Graph API permissions to a managed identity
# Required permissions:
#   - Application.Read.All (to read service principals/managed identities)
#   - Directory.Read.All (to read directory objects)
#
# These permissions are needed when Terraform adds managed identities to Azure AD groups
# via the azuread_group_member resource, even when the caller is a group owner.
#
# Usage:
#   ./grant-graph-permissions.sh <managed-identity-name-or-object-id>
#
# Example:
#   ./grant-graph-permissions.sh "infra-pipeline"
#   ./grant-graph-permissions.sh "12345678-1234-1234-1234-123456789abc"

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if identity parameter provided
if [ $# -eq 0 ]; then
    echo -e "${RED}Error: Managed identity name or object ID required${NC}"
    echo "Usage: $0 <managed-identity-name-or-object-id>"
    exit 1
fi

IDENTITY_INPUT="$1"

echo -e "${GREEN}Starting Microsoft Graph permissions grant process...${NC}"
echo ""

# Step 1: Find the managed identity
echo "Step 1: Looking up managed identity..."
IDENTITY_OBJECT_ID=""

# Try as object ID first (if it looks like a GUID)
if [[ "$IDENTITY_INPUT" =~ ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ \| "$IDENTITY_INPUT" =~ ^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$ ]]; then
    echo "  Input looks like an object ID, verifying..."
    if az ad sp show --id "$IDENTITY_INPUT" &>/dev/null; then
        IDENTITY_OBJECT_ID="$IDENTITY_INPUT"
        IDENTITY_NAME=$(az ad sp show --id "$IDENTITY_OBJECT_ID" --query displayName -o tsv)
        echo -e "  ${GREEN}✓${NC} Found identity: $IDENTITY_NAME"
    fi
fi

# If not found, try as display name
if [ -z "$IDENTITY_OBJECT_ID" ]; then
    echo "  Searching by display name: $IDENTITY_INPUT"
    IDENTITY_OBJECT_ID=$(az ad sp list --display-name "$IDENTITY_INPUT" --query "[0].id" -o tsv)

    if [ -z "$IDENTITY_OBJECT_ID" ] || [ "$IDENTITY_OBJECT_ID" = "null" ]; then
        echo -e "${RED}Error: Could not find managed identity '$IDENTITY_INPUT'${NC}"
        echo ""
        echo "Tips:"
        echo "  - Verify the identity name is correct"
        echo "  - Check if you're logged into the correct Azure tenant"
        echo "  - Try using the Object ID instead of the display name"
        exit 1
    fi
    IDENTITY_NAME="$IDENTITY_INPUT"
    echo -e "  ${GREEN}✓${NC} Found identity: $IDENTITY_NAME"
fi

echo "  Object ID: $IDENTITY_OBJECT_ID"
echo ""

# Step 2: Get Microsoft Graph Service Principal
echo "Step 2: Getting Microsoft Graph service principal..."
GRAPH_APP_ID="00000003-0000-0000-c000-000000000000"
GRAPH_SP_ID=$(az ad sp show --id "$GRAPH_APP_ID" --query id -o tsv)

if [ -z "$GRAPH_SP_ID" ]; then
    echo -e "${RED}Error: Could not find Microsoft Graph service principal${NC}"
    exit 1
fi

echo -e "  ${GREEN}✓${NC} Graph Service Principal ID: $GRAPH_SP_ID"
echo ""

# Step 3: Get permission IDs
echo "Step 3: Looking up permission IDs..."

# Application.Read.All
APP_READ_ALL_ID=$(az ad sp show --id "$GRAPH_APP_ID" \
    --query "appRoles[?value=='Application.Read.All'].id | [0]" -o tsv)

if [ -z "$APP_READ_ALL_ID" ] || [ "$APP_READ_ALL_ID" = "null" ]; then
    echo -e "${RED}Error: Could not find Application.Read.All permission${NC}"
    exit 1
fi
echo -e "  ${GREEN}✓${NC} Application.Read.All: $APP_READ_ALL_ID"

# Directory.Read.All
DIR_READ_ALL_ID=$(az ad sp show --id "$GRAPH_APP_ID" \
    --query "appRoles[?value=='Directory.Read.All'].id | [0]" -o tsv)

if [ -z "$DIR_READ_ALL_ID" ] || [ "$DIR_READ_ALL_ID" = "null" ]; then
    echo -e "${RED}Error: Could not find Directory.Read.All permission${NC}"
    exit 1
fi
echo -e "  ${GREEN}✓${NC} Directory.Read.All: $DIR_READ_ALL_ID"
echo ""

# Function to grant permission
grant_permission() {
    local PERMISSION_NAME=$1
    local PERMISSION_ID=$2

    echo "  Checking if $PERMISSION_NAME is already granted..."

    # Check if permission already exists
    EXISTING=$(az rest --method GET \
        --uri "https://graph.microsoft.com/v1.0/servicePrincipals/$IDENTITY_OBJECT_ID/appRoleAssignments" \
        --query "value[?appRoleId=='$PERMISSION_ID'].id | [0]" -o tsv 2>/dev/null || echo "")

    if [ -n "$EXISTING" ] && [ "$EXISTING" != "null" ]; then
        echo -e "  ${YELLOW}⊙${NC} $PERMISSION_NAME is already granted (skipping)"
        return 0
    fi

    echo "  Granting $PERMISSION_NAME..."

    az rest --method POST \
        --uri "https://graph.microsoft.com/v1.0/servicePrincipals/$IDENTITY_OBJECT_ID/appRoleAssignments" \
        --headers "Content-Type=application/json" \
        --body "{
            \"principalId\": \"$IDENTITY_OBJECT_ID\",
            \"resourceId\": \"$GRAPH_SP_ID\",
            \"appRoleId\": \"$PERMISSION_ID\"
        }" >/dev/null

    echo -e "  ${GREEN}✓${NC} Successfully granted $PERMISSION_NAME"
}

# Step 4: Grant permissions
echo "Step 4: Granting permissions..."
grant_permission "Application.Read.All" "$APP_READ_ALL_ID"
grant_permission "Directory.Read.All" "$DIR_READ_ALL_ID"
echo ""

# Step 5: Verify
echo "Step 5: Verifying permissions..."
GRANTED_PERMS=$(az rest --method GET \
    --uri "https://graph.microsoft.com/v1.0/servicePrincipals/$IDENTITY_OBJECT_ID/appRoleAssignments" \
    --query "value[?resourceId=='$GRAPH_SP_ID'].{role:appRoleId}" -o tsv)

if echo "$GRANTED_PERMS" | grep -q "$APP_READ_ALL_ID" && echo "$GRANTED_PERMS" | grep -q "$DIR_READ_ALL_ID"; then
    echo -e "${GREEN}✓${NC} All permissions successfully granted and verified!"
else
    echo -e "${YELLOW}⚠${NC} Permissions granted but verification incomplete. Please check manually."
fi
echo ""

echo -e "${GREEN}=== Completed ===${NC}"
echo "Identity: $IDENTITY_NAME"
echo "Object ID: $IDENTITY_OBJECT_ID"
echo ""
echo "Granted permissions:"
echo "  • Application.Read.All"
echo "  • Directory.Read.All"
echo ""
