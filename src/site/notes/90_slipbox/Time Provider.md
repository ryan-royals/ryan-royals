---
{"dg-publish":true,"dg-path":"Slipbox Notes/Time Provider.md","permalink":"/slipbox-notes/time-provider/","tags":["notes"],"created":"2023-12-08","updated":"2025-11-28"}
---


The Time Provider is mostly used to add Sleep steps between operations, to not cause over run on API calls, and let resources deploy.  
Found that the `Triggers` style of adding sleep does not actually cause the operation to wait when chaining the trigger to the resource failing to wait.
