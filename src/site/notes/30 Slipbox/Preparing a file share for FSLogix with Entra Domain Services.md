---
{"dg-publish":true,"dg-path":"Preparing a file share for FSLogix with Entra Domain Services.md","permalink":"/preparing-a-file-share-for-fs-logix-with-entra-domain-services/","tags":["notes"]}
---


When first setting up a file share for AVD, you will need to manually edit the NTFS files from a Windows machine that has access to the file share. This is because the NTFS permissions are not set correctly when the file share is created. The following steps will need to be taken:

```pwsh
cmd.exe /C "cmdkey /add:`"<storage account name>.file.core.windows.net`" /user:`"Azure\<storage account name>`" /pass:`"<storage account key>`""
net use y: \\<storage account name>.file.core.windows.net\<share name> /persistent:yes
icacls Y: /grant "oqea.com:All AVD Users(M)"
icacls Y: /grant "Creator Owner:(OI)(CI)(IO)(M)"
icacls Y: /remove "Authenticated Users"
icacls Y: /remove "Builtin\Users"
```

Whatever group you define in the `icacls` command also needs `Storage File Data SMB Share Contributor` on the storage account.

On the Host Pool VM you are connecting from, you need to modify the registry to tell FSLogix what to use.

```pwsh
$regPath = "HKLM:\SOFTWARE\FSLogix\profiles"
New-ItemProperty -Path $regPath -Name Enabled -PropertyType DWORD -Value 1 -Force
New-ItemProperty -Path $regPath -Name VHDLocations -PropertyType MultiString -Value \\<storage account name>.file.core.windows.net\<share name> -Force
```
