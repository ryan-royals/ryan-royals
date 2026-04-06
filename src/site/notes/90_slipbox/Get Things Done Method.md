---
{"dg-publish":true,"permalink":"/90-slipbox/get-things-done-method/","tags":["notes"],"created":"2023-07-24","updated":"2026-03-03","dg-note-properties":{"created":"2023-07-24","modified":"2026-03-03","tags":"notes","references":["https://obsidian.rocks/obsidian-and-gtd/","https://todoist.com/productivity-methods/getting-things-done","https://www.zenflowchart.com/guides/gtd-flowchart"],"related":["[[Note Taking and Productivity]]"]}}
---


```mermaid
flowchart TD

INPUTS --> 00["Define the Task"] --> 01["Is it actionable?"]
01 --Yes--> 11["Is it less than 2 minutes?"]
11 --Yes--> 99["Do It!"]
11 --No--> 21["Can it be Delegated?"]
21 --Yes--> 98["Delegate it"]
21 --No--> 97["Defer It"] --> 89["Later"] & 88["Next"] & 87["Scheduled"]

01 --No--> 79["Trash it"] & 78["Someday / Maybe"]

```

[^1]

Get things Done is a simple system for managing work. There is a famous book the defines the process in great detail, but in system is effectively a re occurring task to check your backlog, and a flowchart for handling tasks themselves.

It aggressively actions items, schedules them for when they are due, or trashes it.

The system also offers a way to manage reference materials, agendas for meetings, and task for context (At Computer, At Home).

[^1]: [Getting Things Done (GTD) Flowchart A Complete Guide](https://www.zenflowchart.com/guides/gtd-flowchart)
