---
{"dg-publish":true,"dg-path":"Blog Posts/How I take Notes.md","permalink":"/blog-posts/how-i-take-notes/","tags":["blogs"],"created":"2025-06-11","updated":"2025-11-27"}
---

This vault serves as my **Digital Garden** and **Personal Knowledge Management System**. Each file represents a distinct object with specific purposes, relationships, and metadata. The system is designed around the principle that **everything is connected** and **context is king**.

> [!note]  
> Mostly based on <https://stephango.com/vault>

## Vault Structure

### Files as Objects

An Object is a semi rigid template of a file that has known quantity frontmatter and content that makes it discoverable and predictable on what the file will contain.

- Each file typically has **only 1 tag** in the frontmatter, defining the type of Object it is
- Tags represent object types, not content topics

#### Object Types

| Tag               | Description                                                                      |
| ----------------- | -------------------------------------------------------------------------------- |
| `#accommodations` | Accommodation reviews of places I have stayed before                             |
| `#assets`         | Items I own, with historic information around it.                                |
| `#boardgames`     | Board game Reviews and notes for things like 'Saves'                             |
| `#books`          | Book notes and reviews. Probably to be archived.                                 |
| `#companies`      | Metadata MOC for Companies I have worked with.                                   |
| `#daily`          | Daily Notes, the backbone of the vault and where ideas start.                    |
| `#events`         | Metadata MOC for events I have attended.                                         |
| `#meetings`       | Meeting notes that link dates, projects, people etc.                             |
| `#notes`          | My catchall Object type that has technical documentation, more complex thoughts. |
| `#people`         | Metadata MOC for People I have worked with.                                      |
| `#projects`       | Metadata MOC for Projects I have worked on, either Work or Personal              |
| `#recipes`        | My own little recipe book.                                                       |
| `#restaurants`    | Restaurant reviews for places I have eaten.                                      |
| `#trips`          | Diary of my trips.                                                               |
| `#workbooks`      | Technical problem-solving journals as a place to think.                          |

### Template System

Each object type has a corresponding template in the `00_templates/` folder that defines its structure and required frontmatter. Templates ensure consistency and provide a starting point for new files.

- Templates define required frontmatter fields for each object type
- Template names follow the pattern: `[object type] template.md`

### Frontmatter System

Different object types require specific frontmatter fields to maintain consistency and enable proper linking.  
Fields are shared across different Object types to enable auto fill

#### Frontmatter Fields

| Field      | Definition                                                                                                  |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| tags       | A key field that defines the Object Type via tags                                                           |
| related    | A list of wiki-links for related Notes.                                                                     |
| references | A list of external links (typically webpages)                                                               |
| people     | A list of People that attended the meeting, worked on the project. <br>Only for linking to `people` objects |
| orgs       | A list of wiki-links for related Companies.<br>Only for linking to `companies` objects.                     |
| rating     | A numerical rating out of 10, usually used as a review.                                                     |
| author     | A list of Authors for the source material (Book Author for example)                                         |
| location   | A list of addresses, used for noting event location or accommodation location                               |
| start      | A date field showing the start of the project, when the trip started, when the event started.               |
| end        | A date field showing the end of the project, when the trip ended, when the event ended.                     |
| pronouns   | A list of the pronouns for the person                                                                       |
| role       | A job definition for the person                                                                             |
| type       | A text field used to show if the topic is Work (Arkahna) or Personal                                        |
| status     | A text field used to show if the project or workbook is Ongoing or archived                                 |

> [!note]  
> Don't use the `people` field on the companies object, instead it is inferred by the `people` object and its `orgs` field.  
> This is to reduce maintenance burden.

### Links as Relationships

Links are used to connect ideas and topics together, appearing either in the frontmatter or the body of the content.  
This is a big part of how Obsidian works, where it shows Backlinks, Outgoing Links, and the visual element in the Local Graph and Full Graph view.

Typically Frontmatter `related` links are used when this Note is a direct child (A Meeting about a Project), where as in body links are used when discussing a topic in a non directly related note. (Azure Firewall note linking to OSI Network model in body).  
This is not a hard requirement, but is used to keep Note readable without forcing a in body link. Downstream it does not typically matter if the link is in frontmatter, or in body.

#### Link Types

##### `[[Page Links]]` - Conceptual Relationship

- `[[Project Name]]` - Links to related projects
- `[[Person Name]]` - Links to people involved
- `[[Technology Name]]` - Links to technologies/concepts

##### Frontmatter Relationships - Parent / Child / Direct Relationship

```yaml
people:
  - "[[Person Name]]"
  - "[[Another Person]]"
orgs:
  - "[[Company Name]]"
related:
  - "[[Related Project]]"
  - "[[Technology Name]]"
```

## Workflows & Best Practices

### Daily Notes Workflow

Daily notes are mostly used for their Bases to quickly see meta data about that day (Notes made, Notes changed, meetings had), but sometimes I put little bits of information in there. I typically find that my note taking style is not time boxed, and I prefer to have a long running Workbook or Project, over little bits of scattered information in daily notes (Not to say I dont like little fleeting notes, but they have the context of not being buried under a date).

### Slipbox Notes Workflow

**Inbox → Processing → Organization:**

1. **Capture** - New content starts in `99_inbox/` or daily notes
2. **Process** - Review and add proper frontmatter/tags
3. **Connect** - Add relevant links and relationships
4. **Store** - Move to the slipbox when ready for long term storage.

#### Deciding on Making a New Note or Updating a Current Note

If the content topic is strongly related to an existing Note, updating a Note should be the priority  
 *Add a new heading to the `[[Azure Kubernetes Services]]` note, not create a `[[Azure Kubernetes Services Pricing]]` note*
 
 If the content is a brand new Topic, create a new Note.  
*There are no notes on the topic of Azure Files so I'll make the `[[Azure Files]]` note*

If the content is linking two topics together, create a new Note that links to both.  
*I'll make a `[[AKS requires that Azure NFS File Shares have Secure Transfer Disabled]]` note and link both `[[Azure Kubernetes Services]]` and `[[Azure Files]]` as in future I can look in either and see a backlink to this information.*

#### Creating New Notes

1. Use Obsidian's template plugin or copy from `00_templates/` folder
2. Ensure the correct tag is applied to match the object type
3. Fill in required frontmatter fields according to the template

#### File Naming Conventions

Consistent naming patterns enable predictable organization and easy discovery:

**Daily Notes**: `YYYY-MM-DD.md`
- Example: `2025-07-29.md`
- Always use ISO date format for chronological sorting

**Meeting Notes**: `YYYY-MM-DD [Meeting Description].md`  
- Example: `2025-07-29 Contoso Standup.md`
- Date prefix enables chronological grouping
- Descriptive suffix for context

**Technical Notes**: `[Descriptive Name].md`
- Example: `Azure Application Gateway.md`
- Use clear, searchable terms
- Avoid abbreviations unless widely known

**People/Companies**: `[Full Name/Company Name].md`
- Example: `John Smith.md`, `Contoso.md`
- Use official or commonly known names

#### Linking Strategy

- **Daily notes** should **not be** directly linked, but instead the dated front matter fields offer the context.
- **Meeting notes** should link to attendees, companies, related projects
- **Technical notes** should link to related technologies, projects, people
- Use **embedded content** (`![[]]`) sparingly - mainly for pulling meeting content into project notes
- **Context is king** - every file should be discoverable through multiple paths
- **Link early and often** - create connections as you write
- **Use frontmatter** for structured relationships (people, orgs, projects)
- **Use inline links** for conceptual connections and references

#### Content Style Guide

- Content should be concise in nature, as this system is for Notes not Novels.
- Headings are used liberally to make content easily parse-able.
- Footnotes are to be used when referencing external content (webpages), otherwise WikiLinks are to be used for internal content and external content.

## Obsidian-Specific Features

### Search & Discovery Patterns

- Use **tag searches** to find all instances of an object type
- Use **link mentions** to find related but unlinked content  
- Use **graph view** to discover unexpected connections
- Use **backlinks panel** to see all references to current note
- Use **bases** to create tables to query for content in a repeatable way

## Maintenance Guidelines

### Periodic Vault Maintenance

**Weekly Review:**
- Process files in `99_inbox/` folder - add proper frontmatter and move to appropriate organized folders
- Review recent daily notes for orphaned links or incomplete connections  
- Check for duplicate or similar files that could be consolidated

**Monthly Cleanup:**
- Review and archive outdated object types
- Update project status and close completed initiatives
- Consolidate related technical notes where appropriate

### The "Campsite Rule"

Borrowed from [[90_slipbox/Building a Second Brain\|Building a Second Brain]], follow the **Campsite Rule**: *"If you touch a note, leave it better than you found it."*

This means:
- Add missing frontmatter when you encounter it
- Create links to related content you discover
- Fix broken or outdated links
- Add context or clarification to incomplete notes

### Quality Standards

- **Every file should have proper frontmatter** with at least its object type tag
- **Orphaned files** (no incoming or outgoing links) should be rare - create connections
- **Broken links** should be fixed or removed promptly
- **File names should be descriptive** and follow established conventions

This maintenance approach keeps the vault healthy and ensures the knowledge graph remains useful and discoverable.
