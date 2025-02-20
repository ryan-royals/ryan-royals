---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-functions-overview/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/open-graph-image_LeISKTK.png)

Choose a programming language 

 C# Java JavaScript PowerShell Python 

#### In this article

1. [Scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp#scenarios)
2. [Development lifecycle](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp#development-lifecycle)
3. [Hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp#hosting-options)
4. [Next Steps](https://learn.microsoft.com/en-us/azure/azure-functions/functions-overview?pivots=programming-language-csharp#next-steps)

Azure Functions is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running.

You focus on the code that matters most to you, in the most productive language for you, and Azure Functions handles the rest.

For the best experience with the Functions documentation, choose your preferred development language from the list of native Functions languages at the top of the article.

#### Scenarios

Functions provides a comprehensive set of event-driven [triggers and bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings) that connect your functions to other services without having to write extra code.

The following are a common, *but by no means exhaustive*, set of integrated scenarios that feature Functions.

| If you want to... | then... |
| --- | --- |
| [Process file uploads](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#process-file-uploads) | Run code when a file is uploaded or changed in blob storage. |
| [Process data in real time](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#real-time-stream-and-event-processing) | Capture and transform data from event and IoT source streams on the way to storage. |
| [Infer on data models](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#machine-learning-and-ai) | Pull text from a queue and present it to various AI services for analysis and classification. |
| [Run scheduled task](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#run-scheduled-tasks) | Execute data clean-up code on pre-defined timed intervals. |
| [Build a scalable web API](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#build-a-scalable-web-api) | Implement a set of REST endpoints for your web applications using HTTP triggers. |
| [Build a serverless workflow](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#build-a-serverless-workflow) | Create an event-driven workflow from a series of functions using Durable Functions. |
| [Respond to database changes](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#respond-to-database-changes) | Run custom logic when a document is created or updated in [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction). |
| [Create reliable message systems](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios#create-reliable-message-systems) | Process message queues using Queue Storage, Service Bus, or Event Hubs. |

These scenarios allow you to build event-driven systems using modern architectural patterns. For more information, see [Azure Functions Scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios).

#### Development lifecycle

With Functions, you write your function code in your preferred language using your favorite development tools and then deploy your code to the Azure cloud. Functions provides native support for developing in [C#, Java, JavaScript, PowerShell, Python](https://learn.microsoft.com/en-us/azure/azure-functions/supported-languages), plus the ability to use [more languages](https://learn.microsoft.com/en-us/azure/azure-functions/functions-custom-handlers), such as Rust and Go.

Functions integrates directly with Visual Studio, Visual Studio Code, Maven, and other popular development tools to enable seamless debugging and [deployments](https://learn.microsoft.com/en-us/azure/azure-functions/functions-deployment-technologies).

Functions also integrates with Azure Monitor and Azure Application Insights to provide comprehensive runtime telemetry and analysis of your [functions in the cloud](https://learn.microsoft.com/en-us/azure/azure-functions/functions-monitoring).

#### Hosting options

Functions provides a variety [hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scale#overview-of-plans) for your business needs and application workload. [Event-driven scaling hosting options](https://learn.microsoft.com/en-us/azure/azure-functions/event-driven-scaling) range from fully serverless, where you only pay for execution time (Consumption plan), to always warm instances kept ready for fastest response times (Premium plan).

When you have excess App Service hosting resources, you can host your functions in an existing App Service plan. This kind of Dedicated hosting plan is also a good choice when you need predictable scaling behaviors and costs from your functions.

If you want complete control over your functions runtime environment and dependencies, you can even deploy your functions in containers that you can fully customize. Your custom containers can be hosted by Functions, deployed as part of a microservices architecture in Azure Container Apps, or even self-hosted in Kubernetes.

#### Next Steps

[Azure Functions Scenarios](https://learn.microsoft.com/en-us/azure/azure-functions/functions-scenarios) [Get started through lessons, samples, and interactive tutorials](https://learn.microsoft.com/en-us/azure/azure-functions/functions-get-started)
