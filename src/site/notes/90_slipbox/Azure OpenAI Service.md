---
{"dg-publish":true,"permalink":"/90-slipbox/azure-open-ai-service/","tags":["notes"],"created":"2025-06-11T10:28:47.771+09:30","updated":"2026-06-11T09:30:38.361+09:30","dg-note-properties":{"aliases":null,"created":"2025-01-20","modified":"2026-06-11","references":["https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/understand-embeddings"],"related":["[[Azure]]"],"tags":"notes"}}
---


Created in partnership with Microsoft and [[90_slipbox/companies/OpenAI\|OpenAI]], a service is supplied to provide 4 key components:

- Pre trained generative AI models
- customization capabilities to fine tune the AI
- Built in tools to detect and mitigate harmful use cases
- Enterprise grade security with RBAC and private networks.

## How to Use

As of the MS Learn document, you need to apply for access to the service. Once created, you can interact with REST APIs, Python SDK, or the web base interface in the Azure OpenAI Studio

The main family of offers are:

- GPT-4
- GPT-3
- Codex
- Embeddings
- Dall-e

Testing the model is done within a Playground, which allows you to send prompts.

## SKUs

**Global Standard** - Consumption based Shared Model, surfaced globally  
**Standard** - Consumption based Shared model, surfaced in a specific region  
**Provision Managed** - Reserved Isolated model, surfaced in a specific region

## Models

### Completions

Completions (Also Chat Completions) are predictive modes that you pass a message in, and you get a conversational response. This is your typical experience with models such as GPT3.5 and GPT4

### Embeddings

Embeddings are trained to give a [[Data Vector\|Data Vector]] response, which is used to create searchable content to find a specific document that is most like the input.  
This involves the processing of data using something like [[90_slipbox/Azure Data Factory\|Azure Data Factory]]  

![[Data Vector\|Data Vector]]
