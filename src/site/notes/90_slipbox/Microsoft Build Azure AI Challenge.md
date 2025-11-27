---
{"dg-publish":true,"dg-path":"Slipbox Notes/Microsoft Build Azure AI Challenge.md","permalink":"/slipbox-notes/microsoft-build-azure-ai-challenge/","tags":["projects"],"created":"2023-05-26","updated":"2025-11-28"}
---


## Microsoft Build Azure AI Challenge

### Overview

Learn and develop generative AI models with deep understanding of language and code using the newest technology for a variety of use case.

### Learn Modules

#### Get Started with AI on Azure


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/get-started-with-ai-on-azure/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





## Get Started with AI on Azure

### Overview

Ai can be used to build solutions that seemed like science fiction a short time ago, enable clever apps for everyone.

#### Introduction to AI

Some key workloads for AI include:

- Machine learning: The model learns and draws conclusions over time
- Anomaly detection: The capability to detect errors or unusual activity in a system.
- Computer Vision: See images and videos.
- Natural Language Processing: Responds and interprets language like a Human, not a robot.
- Knowledge mining: The Ability to extract information for large unstructured data sources.

#### Understand Machine Learning

Machine learning is to teach the AI how to identify data within the dataset. An example is Botanist adding flowers to a data set, and the AI learning how to identify these flowers in the future.

##### Machine Learning in Microsoft Azure


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/azure-machine-learning/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





Azure Machine Learning is a cloud-based platform for creating, managing, and publishing machine learning models. It has the following capability:

- Automated machine learning - This feature enables non experts to quickly create an effective machine learning model from data.
- Azure Machine Learning Designer - A graphical interface enabling no-code development of machine learning solutions.
- Data and compute management - Cloud-based data storage and compute resources that professional data scientists can use to run data experiment code at scale
- Pipelines - Data scientists, software engineers, and IT operations professionals can define pipelines to orchestrate model training, deployment, and management tasks.

## Automated ML

Automated Machine Learning automatically tries multiple pre-processing techniques and model-training algorithms in parallel. Automated machine learning allows you to train models without extensive data science or programming knowledge. For people with a data science or programming background. it provides a way to save time and resources by automating algorithm selection and hyperparameter tuning.

In Azure Machine Learning, operations that you run are called *jobs*. The job configuration provides the information needed to specify your training script, compute target, and Azure ML environment in your run configuration and run a training job.

## Azure Machine Learning Studio

Azure Machine Learning Studio is a web portal for machine learning solutions in Azure. It includes a wide range of features and capabilities that help data scientists prepare data, train models, publish predictive services, and monitor their usage.

AMLS is used to manage the compute used by Azure Machine Learning, to which there are 4 kinds of compute you can create.

**Compute Instances**: Development workstations that data scientists can use to work with data and models.  
**Compute Clusters**: Scalable clusters of virtual machines for on-demand processing of experiment code.  
**Inference Clusters**: Deployment targets for predictive services that use your trained models.  
**Attached Compute**: Links to existing Azure compute resources, such as Virtual Machines or Azure Databricks clusters.


</div></div>
]

#### Anomaly Detection

This capability is used in software systems to identify things that are irregular. It is used for something like watching credit card transactions to identify something that looks like fraud.

##### Anomaly Detection in Microsoft Azure


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/azure-anomaly-detector/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





An API that develops can use to create anomaly detection solutions.

Links: [[90_slipbox/Azure Machine Learning\|Azure Machine Learning]]  


</div></div>


#### Understand Computer Vision

Computer vision gives an AI the power to process visual elements.  
Some common cv tasks are:

- Image classification.
- Object detection.
- Semantic Segmentation.
- Image Analysis.
- Face detection, analysis, and recognition.
- Optical Character recognition.

##### Computer Vision Services in Microsoft Azure


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/computer-vision-services-in-azure/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





Azure has a collection of services to create a full features Computer Vision suite.

## Azure Computer Vision

Used to analyse images and video, extract description, tags, objects, and text.

## Azure Custom Vision

Used to train custom image classification and object detection modules using your own images

## Azure Face

Used to build face detection and facial recognition solutions.

## Azure Form Recognizer

Used to extract information from scanned forms and invoices


</div></div>


#### Understand Natural Language Processing

NLP is the area of AI that focuses on written and spoken language. NLP enables software to:

- Analyse and interpret text in documents, email messages, and other sources.
- Interpret spoken language, and synthesize speech responses.
- automatically translate spoken or written phrases between languages.
- Interpret command and determine appropriate actions.

##### Natural Language Processing Resources in Microsoft Azure


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/natural-language-processing-resources-in-microsoft-azure/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





In Azure, the following cognitive services are used to build natural language processing solutions:

## Azure Language

Used to access features for understanding and analysing text, training language models that can understand spoken or text-based commands, and building intelligent applications.

## Azure Translator

Used to translate between over 60 different languages  

## Azure Speech

Used to recognize and syntherize speech, and to translate spoken languages  

## Azure Bot

Provides a conversation AI, the capability of a software "Agent" to participate in a conversation. Developers can use the Bot Framework to create a botand maangi it with Azure Bot Service, integrating back-end services like [[90_slipbox/Natural language processing resources in Microsoft Azure\|Natural language processing resources in Microsoft Azure]], and connecting to channels for web chat, email, [[Microsoft Teams\|Microsoft Teams]], and others.


</div></div>


#### Understand Knowledge Mining

Knowledge mining is the term used to describe solutions that involve extracting informationo from large volumes of often unstructuted data to create a searchable knowledge store.

##### Knowledge Mining in Microsoft Azure


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/slipbox-notes/azure-cognitive-search/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





Azure Cognitive search is a private, enterprise search solution that has tools for building indexes. The indexes can then be used for internal only use , or to enable searchable content on public facing internet assets.


</div></div>


#### Challenges and Risks with AI

Ai is a powerful tool that can be used to great effect to benefit the world, however it can be subject to many risks including:

- Bias can affect results
- Errors may cause harm
- Data could be exposed
- Solutions may not work for everyone
- Users must trust a complex system
- Who's liable for AI-driven decisions?

#### Understand Responsible AI

Microsoft is guided by a set of six principals to ensure that AI provide the best solution they can without unintended negative consequences:

##### Fairness

AI systems should treat all people fairly. An example would be an AI deciding on loan approvals should not include bias for gender, ethnicity or other factors.

##### Reliability and Safety

AI systems should perform reliably and safely. An example is with autonomous vehicles.

##### Privacy and Security

AI systems should be secure and respect privacy.

##### Inclusiveness

AI systems should empower everyone and engage people, regardless of physical ability, gender, sexual orientation, ethnicity or other social factors.

##### Transparency

AI systems should be understandable, and users should be made aware of the purpose of the system, how it works, and what limitations may be expected.

##### Accountability

People should be accountable for AI systems, and should always fit ethical and legal standards.

Links: [[90_slipbox/Microsoft Build Azure AI Challenge\|Microsoft Build Azure AI Challenge]]  
Reference: [Get started with AI on Azure - Training | Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/get-started-ai-fundamentals/?WT.mc_id=cloudskillschallenge_12f32cf8-2cd8-42e1-97dd-001b4a042766)


</div></div>


#### Introduction to Azure OpenAI Service


<div class="transclusion internal-embed is-loaded"><div class="markdown-embed">





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


</div></div>


#### Use Automated Machine Learning in Azure Machine Learning

![[Use Automated Machine Learning in Azure Machine Learning\|Use Automated Machine Learning in Azure Machine Learning]]
