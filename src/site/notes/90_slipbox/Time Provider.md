---
{"dg-publish":true,"permalink":"/90-slipbox/time-provider/","tags":["notes"]}
---


The Time Provider is mostly used to add Sleep steps between operations, to not cause over run on API calls, and let resources deploy.  
Found that the `Triggers` style of adding sleep does not actually cause the operation to wait when chaining the trigger to the resource failing to wait.
