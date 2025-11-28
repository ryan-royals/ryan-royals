---
{"dg-publish":true,"permalink":"/90-slipbox/azure-open-ai-service/","tags":["notes"]}
---

Created in partnership with Microsoft and [[90_slipbox/OpenAI\|OpenAI]], a service is supplied to provide 4 key components:

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

Embeddings are trained to give a [[90_slipbox/Data Vector\|Data Vector]] response, which is used to create searchable content to find a specific document that is most like the input.  
This involves the processing of data using something like [[90_slipbox/Azure Data Factory\|Azure Data Factory]]  


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/data-vector/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





Vectors are similar to a GUID for the data, that measure the data in 3d space so you can compare them.  
Convert content to maths, so you can compare the maths to find what you are looking for  
Each Embedding is a vector of floating point numbers, and the distance between two embeddings in the vector space is correlated with semantic similarity between two inputs in the original format.


</div></div>

