---
{"dg-publish":true,"dg-path":"Slipbox Notes/Introduction to Azure OpenAI Service.md","permalink":"/slipbox-notes/introduction-to-azure-open-ai-service/","tags":["notes"],"created":"2023-05-29","updated":"2025-11-28"}
---


## Introduction to Azure OpenAI Service

### Overview

Learn Objectives:

- Describe Azure OpenAI workloads and access to Azure OpenAI Service
- Understand generative AI models
- Understand Azure OpenAI's language, code, and image capabilities
- Understand Azure OpenAI's responsible AI practices and limited access policies.

### Introduction

There are several categories of capabilities found in OpenAI AI models, three of these include:

| Capability                    | Examples                                                                                                                            |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| *Generating natural language* | Such as: summarizing complex text for different reading levels, suggesting alternative wording for sentences, *and much more*       |
| *Generating code*             | Such as: translating code from one programming language into another, identifying and troubleshooting bugs in code, *and much more* |
| *Generating images*           | Such as: generating images for publications from text descriptions *and much more*                                                  |

### What is Generative AI

Where OpenAI models fit into AI landscape:

- Artificial Intelligence - Imitate human behaviour by learning and executing tasks without direct oversight
- Machine learning - Extrapolate on data sets and make assumptions
- Deep learning - Use layers of algorithms to form a artificial neural network
- Generative AI - Produce new content based on the input.

### Describe Azure OpenAI


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/azure-open-ai-service/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">




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


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/data-vector/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





Vectors are similar to a GUID for the data, that measure the data in 3d space so you can compare them.  
Convert content to maths, so you can compare the maths to find what you are looking for  
Each Embedding is a vector of floating point numbers, and the distance between two embeddings in the vector space is correlated with semantic similarity between two inputs in the original format.


</div></div>



</div></div>


### Understand OpenAI's Natural Language Capabilities

Generative pre-trained transformer (GPT) models are excellent at understanding and creating natural language.

#### Example

```
Write a recipe based on these ingredients and instructions:

Fruit Pie

Ingredients:
Strawberries
Blueberries
Flour
Eggs
Milk
```

Here's an example of the OpenAI API generated response:

```
Instructions:

1. Preheat your oven to 350 degrees Fahrenheit.

2. In a medium bowl, mix together 1 cup of flour and 1 egg until it forms a dough.

3. Grease a 9-inch pie dish with butter or non-stick cooking spray.

4. Roll out the dough and place it in the pie dish.

5. In a separate bowl, mix together 1 cup of strawberries, 1 cup of blueberries, and 1 cup of milk.

6. Pour the fruit mixture into the pie dish.

7. Bake
```

### Understand OpenAI Code Generation Capabilities

Codex models are used to be proficient in over a dozen languages, such as C#, JavaScript, Perl, PHP and Python.  
Codex is based off of GPT-3

#### Example

```
# Python 3
def mult_numbers(a, b):
  return a * b

# Unit test
def
```

Codex builds out unit tests for our function:

```
# Python 3
def mult_numbers(a, b):
  return a * b

# Unit test
def test_mult_numbers():
  assert mult_numbers(3, 4) == 12
  assert mult_numbers(0, 10) == 0
  assert mult_numbers(4, 0) == 0

# Unit test
def test_mult_numbers_negative():
  assert mult_numbers(-1, 10) == -10
```

### Understand OpenAI's Image Generation Capabilities

Image Generation models can take a prompt, a base image, or both and create something new.

The key use cases are Create a Image, Edit an Image, Image variations.

### Describe Azure OpenAI's Access and Responsible AI Policies

Usage of Azure OpenAI should follow the six Microsoft [AI principles](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai):

- **Fairness**: Al systems shouldn't make decisions that discriminate against or support bias of a group or individual.
- **Reliability and Safety**: Al systems should respond safely to new situations and potential manipulation.
- **Privacy and Security**: Al systems should be secure and respect data privacy.
- **Inclusiveness**: Al systems should empower everyone and engage people.
- **Accountability**: People must be accountable for how Al systems operate.
- **Transparency**: AI systems should have explanations so users can understand how they're built and used.
