---
{"dg-publish":true,"permalink":"/90-slipbox/get-started-with-ai-on-azure/","tags":["notes"]}
---


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


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/azure-machine-learning/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





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


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/azure-anomaly-detector/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





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


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/computer-vision-services-in-azure/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





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


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/natural-language-processing-resources-in-microsoft-azure/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





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


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/azure-cognitive-search/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





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
