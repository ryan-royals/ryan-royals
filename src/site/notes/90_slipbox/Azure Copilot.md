---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Copilot.md","permalink":"/slipbox-notes/azure-copilot/","tags":["notes"],"created":"2023-12-05","updated":"2025-11-28"}
---

Azure Copliot is powered by LLM, to send your prompt and context to the LLM and uses data sources such as Microsoft Docs, Azure Resource Manager, Azure Resource Graph to create a Retrieval Augmented Generation response.  
The LLM does not have access to ARM, and is filtered through Azure Copilot, which prevents it from going rogue on your data.

Azure Copilot runs on a On-behalf-of flow, meaning it runs as your user, and does not run as a Service Principal.

A powerful part of this that is not clear from the start, but if you are using [[90_slipbox/Azure Arc\|Azure Arc]], Azure Copilot can also manage your on prem resources.

When interacting with it, you generate scripts using the tool that you can run using a run button, but it wont take the action itself.
