---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/boost-processing-performance-by-combining-ai-models/","tags":["rw/articles"]}
---

![rw-book-cover](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/06/microsoft_logo-300x300.webp)

Leveraging the strengths of different AI models and bringing them together into a single application can be a great strategy to help you meet your performance objectives. This approach harnesses the power of multiple AI systems to improve accuracy and reliability in complex scenarios.

In the Microsoft model catalog, there are more than 1,800 AI models available. Even more models and services are available viaAzure OpenAI Service and Azure AI Foundry, so you can find the right models to build your optimal AI solution. 

![background pattern](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/10/Azure_Hero_Cylinder_Blue_GreenGrad-1024x575.webp) 

#### Azure OpenAI Service

Customize various models for your specific use cases.

[Try it out.](https://azure.microsoft.com/en-us/products/ai-services/openai-service/) 

Let’s look at how a multiple model approach works and explore some scenarios where companies successfully implemented this approach to increase performance and reduce costs.

#### How the multiple model approach works

The multiple model approach involves combining different AI models to solve complex tasks more effectively. Models are trained for different tasks or aspects of a problem, such as language understanding, image recognition, or data analysis. Models can work in parallel and process different parts of the input data simultaneously, route to relevant models, or be used in different ways in an application.

Let’s suppose you want to pair a fine-tuned vision model with a large language model to perform several complex imaging classification tasks in conjunction with natural language queries. Or maybe you have a small model fine-tuned to generate SQL queries on your database schema, and you’d like to pair it with a larger model for more general-purpose tasks such as information retrieval and research assistance. In both of these cases, the multiple model approach could offer you the adaptability to build a comprehensive AI solution that fits your organization’s particular requirements.

##### Before implementing a multiple model strategy

First, identify and understand the outcome you want to achieve, as this is key to selecting and deploying the right AI models. In addition, each model has its own set of merits and challenges to consider in order to ensure you choose the right ones for your goals. There are several items to consider before implementing a multiple model strategy, including:

* The intended purpose of the models.
* The application’s requirements around model size.
* Training and management of specialized models.
* The varying degrees of accuracy needed.
* Governance of the application and models.
* Security and bias of potential models.
* Cost of models and expected cost at scale.
* The right programming language (check [DevQualityEval](https://github.com/symflower/eval-dev-quality) for current information on the best languages to use with specific models).

The weight you give to each criterion will depend on factors such as your objectives, tech stack, resources, and other variables specific to your organization.

Let’s look at some scenarios as well as a few customers who have implemented multiple models into their workflows.

Multiple model implementations

[Create a private virtual network in the cloud with your Azure free account](https://azure.microsoft.com/en-us/free/virtual-network/search/?ef_id=_k_b95503a83b5a11f0161364d4342f531d_k_&OCID=AIDcmm5edswduu_SEM__k_b95503a83b5a11f0161364d4342f531d_k_&msclkid=b95503a83b5a11f0161364d4342f531d)

#### Scenario 1: Routing

Routing is when AI and machine learning technologies optimize the most efficient paths for use cases such as call centers, logistics, and more. Here are a few examples:

##### Multimodal routing for diverse data processing

One innovative application of multiple model processing is to route tasks simultaneously through different multimodal models that specialize in processing specific data types such as text, images, sound, and video. For example, you can use a combination of a smaller model like GPT-3.5 turbo, with a multimodal large language model like [GPT-4o](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#gpt-4o-and-gpt-4-turbo), depending on the modality. This routing allows an application to process multiple modalities by directing each type of data to the model best suited for it, thus enhancing the system’s overall performance and versatility.

##### Expert routing for specialized domains

Another example is expert routing, where prompts are directed to specialized models, or “experts,” based on the specific area or field referenced in the task. By implementing expert routing, companies ensure that different types of user queries are handled by the most suitable AI model or service. For instance, technical support questions might be directed to a model trained on technical documentation and support tickets, while general information requests might be handled by a more general-purpose language model.

 Expert routing can be particularly useful in fields such as medicine, where different models can be fine-tuned to handle particular topics or images. Instead of relying on a single large model, multiple smaller models such as [Phi-3.5-mini-instruct](https://ai.azure.com/explore/models/Phi-3.5-mini-instruct/version/6/registry/azureml?tid=72f988bf-86f1-41af-91ab-2d7cd011db47) and [Phi-3.5-vision-instruct](https://ai.azure.com/explore/models/Phi-3.5-vision-instruct/version/2/registry/azureml?tid=72f988bf-86f1-41af-91ab-2d7cd011db47) might be used—each optimized for a defined area like chat or vision, so that each query is handled by the most appropriate expert model, thereby enhancing the precision and relevance of the model’s output. This approach can improve response accuracy and reduce costs associated with fine-tuning large models.

##### **Auto manufacturer**

One example of this type of routing comes from a large auto manufacturer. They implemented a Phi model to process most basic tasks quickly while simultaneously routing more complicated tasks to a large language model like [GPT-4o](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#gpt-4o-and-gpt-4-turbo). The Phi-3 offline model quickly handles most of the data processing locally, while the GPT online model provides the processing power for larger, more complex queries. This combination helps take advantage of the cost-effective capabilities of Phi-3, while ensuring that more complex, business-critical queries are processed effectively.

##### **Sage**

Another example demonstrates how industry-specific use cases can benefit from expert routing. Sage, a leader in accounting, finance, human resources, and payroll technology for small and medium-sized businesses (SMBs), wanted to help their customers discover efficiencies in accounting processes and boost productivity through AI-powered services that could automate routine tasks and provide real-time insights.

Recently, Sage deployed Mistral, a commercially available large language model, and fine-tuned it with accounting-specific data to address gaps in the GPT-4 model used for their Sage Copilot. This fine-tuning allowed Mistral to better understand and respond to accounting-related queries so it could categorize user questions more effectively and then route them to the appropriate agents or deterministic systems. For instance, while the out-of-the-box Mistral large language model might struggle with a cash-flow forecasting question, the fine-tuned version could accurately direct the query through both Sage-specific and domain-specific data, ensuring a precise and relevant response for the user.

#### Scenario 2: Online and offline use

Online and offline scenarios allow for the dual benefits of storing and processing information locally with an offline AI model, as well as using an online AI model to access globally available data. In this setup, an organization could run a local model for specific tasks on devices (such as a customer service chatbot), while still having access to an online model that could provide data within a broader context.

##### Hybrid model deployment for healthcare diagnostics

In the healthcare sector, AI models could be deployed in a hybrid manner to provide both online and offline capabilities. In one example, a hospital could use an offline AI model to handle initial diagnostics and data processing locally in IoT devices. Simultaneously, an online AI model could be employed to access the latest medical research from cloud-based databases and medical journals. While the offline model processes patient information locally, the online model provides globally available medical data. This online and offline combination helps ensure that staff can effectively conduct their patient assessments while still benefiting from access to the latest advancements in medical research.

##### Smart-home systems with local and cloud AI

In smart-home systems, multiple AI models can be used to manage both online and offline tasks. An offline AI model can be embedded within the home network to control basic functions such as lighting, temperature, and security systems, enabling a quicker response and allowing essential services to operate even during internet outages. Meanwhile, an online AI model can be used for tasks that require access to cloud-based services for updates and advanced processing, such as voice recognition and smart-device integration. This dual approach allows smart home systems to maintain basic operations independently while leveraging cloud capabilities for enhanced features and updates.

#### Scenario 3: Combining task-specific and larger models

Companies looking to optimize cost savings could consider combining a [small but powerful](https://news.microsoft.com/source/features/ai/the-phi-3-small-language-models-with-big-potential/) task-specific SLM like [Phi-3](https://azure.microsoft.com/en-us/products/phi/) with a robust large language model. One way this could work is by deploying Phi-3—one of [Microsoft’s family of powerful, small language models](https://azure.microsoft.com/en-us/products/phi/) with groundbreaking performance at low cost and low latency—in edge computing scenarios or applications with stricter latency requirements, together with the processing power of a larger model like GPT.

Additionally, Phi-3 could serve as an initial filter or triage system, handling straightforward queries and only escalating more nuanced or challenging requests to GPT models. This tiered approach helps to optimize workflow efficiency and reduce unnecessary use of more expensive models.

By thoughtfully building a setup of complementary small and large models, businesses can potentially achieve cost-effective performance tailored to their specific use cases.

##### **Capacity**

Capacity’s [AI-powered Answer Engine](https://www.microsoft.com/en/customers/story/1700954751530838723-lucy-azure-united-states)® retrieves exact answers for users in seconds. By leveraging cutting-edge AI technologies, Capacity gives organizations a personalized AI research assistant that can seamlessly scale across all teams and departments. They needed a way to help unify diverse datasets and make information more easily accessible and understandable for their customers. By leveraging Phi, Capacity was able to provide enterprises with an effective AI knowledge-management solution that enhances information accessibility, security, and operational efficiency, saving customers time and hassle. Following the successful implementation of Phi-3-Medium, Capacity is now eagerly testing the Phi-3.5-MOE model for use in production.

Phi Open Models

[Smaller, less compute-intensive models for generative AI solutions.](https://azure.microsoft.com/en-us/products/phi/)

#### Our commitment to Trustworthy AI

Organizations across industries are leveraging Azure AI and Copilot capabilities to drive growth, increase productivity, and create value-added experiences.

We’re committed to helping organizations use and build [AI that is trustworthy](https://blogs.microsoft.com/blog/2024/09/24/microsoft-trustworthy-ai-unlocking-human-potential-starts-with-trust/), meaning it is secure, private, and safe. We bring best practices and learnings from decades of researching and building AI products at scale to provide industry-leading commitments and capabilities that span our three pillars of security, privacy, and safety. Trustworthy AI is only possible when you combine our commitments, such as our Secure Future Initiative and our Responsible AI principles, with our product capabilities to unlock AI transformation with confidence. 

#### Get started with Azure AI Foundry

To learn more about enhancing the reliability, security, and performance of your cloud and AI investments, explore the additional resources below.

* Find the ideal AI model at [Azure AI Foundry](https://ai.azure.com/).

* Learn more about [Azure OpenAI Service models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models?tabs=python-secure%2Cglobal-standard%2Cstandard-chat-completions).

* Read about [Phi-3-mini](https://export.arxiv.org/abs/2404.14219), which performs better than some models twice its size.

[Build custom generative AI solutions with Azure OpenAI.](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)

The post [Boost processing performance by combining AI models](https://azure.microsoft.com/en-us/blog/boost-processing-performance-by-combining-ai-models/) appeared first on [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog).
