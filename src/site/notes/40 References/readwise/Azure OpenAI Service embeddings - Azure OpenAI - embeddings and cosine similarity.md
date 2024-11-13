---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-open-ai-service-embeddings-azure-open-ai-embeddings-and-cosine-similarity/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Summary

Learn more about how the Azure OpenAI embeddings API uses cosine similarity for document search and to measure similarity between texts.

## Highlights

An embedding is a special format of data representation that machine learning models and algorithms can easily use. The embedding is an information dense representation of the semantic meaning of a piece of text. Each embedding is a vector of floating-point numbers, such that the distance between two embeddings in the vector space is correlated with semantic similarity between two inputs in the original format. For example, if two texts are similar, then their vector representations should also be similar. Embeddings power vector similarity search in Azure Databases such as [Azure Cosmos DB for MongoDB vCore](https://learn.microsoft.com/en-us/azure/cosmos-db/mongodb/vcore/vector-search). ([View Highlight] (https://read.readwise.io/read/01hghmhfgexhbcrpd0p7vrr9z3))


Different Azure OpenAI embedding models are created to be good at a particular task:
• **Similarity embeddings** are good at capturing semantic similarity between two or more pieces of text.
• **Text search embeddings** help measure whether long documents are relevant to a short query.
• **Code search embeddings** are useful for embedding code snippets and embedding natural language search queries. ([View Highlight] (https://read.readwise.io/read/01hghmj17m72fsevjq74266gd4))


