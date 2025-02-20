---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/accelerate-scale-with-azure-open-ai-service-provisioned-offering/","tags":["rw/articles"]}
---

![rw-book-cover](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/06/microsoft_logo-300x300.webp)

In today’s fast-evolving digital landscape, enterprises need more than just powerful AI models—they need AI solutions that are adaptable, reliable, and scalable. With upcoming availability of Data Zones and new enhancements to Provisioned offering in [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/), we are taking a big step forward in making AI broadly available and also enterprise-ready. These features represent a fundamental shift in how organizations can deploy, manage, and optimize generative AI models.

![A person sitting at a table looking at a laptop.](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/05/CLO22_RemoteHome_043.jpg) 

#### Azure OpenAI Service

Build your own copilot and generative AI applications.

[Find your AI solution](https://azure.microsoft.com/en-us/products/ai-services/openai-service/) 

With the launch of Azure OpenAI Service Data Zones in the European Union and the United States, enterprises can now scale their AI workloads with even greater ease while maintaining compliance with regional data residency requirements. Historically, variances in model-region availability forced customers to manage multiple resources, often slowing down development and complicating operations. Azure OpenAI Service Data Zones can remove that friction by offering flexible, multi-regional data processing while ensuring data is processed and stored within the selected data boundary.

This is a compliance win which also allows businesses to seamlessly scale their AI operations across regions, optimizing for both performance and reliability without having to navigate the complexities of managing traffic across disparate systems.

Leya, a tech startup building genAI platform for legal professionals, has been exploring Data Zones deployment option.

> 
> *“Azure OpenAI Service Data Zones deployment option offers Leya a cost-efficient way to securely scale AI applications to thousands of lawyers, ensuring compliance and top performance. It helps us achieve better customer quality and control, with rapid access to the latest Azure OpenAI innovations.*“*—Sigge Labor, CTO, Leya*
> 
> 
> 

Data Zones will be available for both Standard (PayGo) and Provisioned offerings, starting this week on November 1, 2024.

![graphical user interface, text, application, chat or text message](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2024/10/Picture1-5.webp)
#### Industry leading performance

Enterprises depend on predictability, especially when deploying mission-critical applications. That’s why we’re introducing a 99% latency service level agreement for token generation. This latency SLA ensures that tokens are generated at a faster and more consistent speeds, especially at high volumes

The Provisioned offer provides predictable performance for your application. Whether you’re in e-commerce, healthcare, or financial services, the ability to depend on low-latency and high-reliability AI infrastructure translates directly to better customer experiences and more efficient operations.

#### Lowering the cost of getting started

To make it easier to test, scale, and manage, we are reducing hourly pricing for Provisioned Global and Provisioned Data Zone deployments starting November 1, 2024. This reduction in cost ensures that our customers can benefit from these new features without the burden of high expenses. Provisioned offering continues to offer discounts for monthly and annual commitments.

|  |  |  |  |
| --- | --- | --- | --- |
| **Deployment option** | **Hourly PTU** | **One month reservation per PTU** | **One year reservation per PTU** |
| **Provisioned Global** | Current: $2.00 per hour November 1, 2024: $1.00 per hour | $260 per month   | $221 per month |
| **Provisioned Data ZoneNew** | November 1, 2024: $1.10 per hour   | $260 per month | $221 per month |

We are also reducing deployment minimum entry points for Provisioned Global deployment by 70% and scaling increments by up to 90%, lowering the barrier for businesses to get started with Provisioned offering earlier in their development lifecycle.

#### Deployment quantity minimums and increments for Provisioned offering

|  |  |  |  |
| --- | --- | --- | --- |
| Model | Global | Data Zone **New** | Regional |
| **GPT-4o** | Min: ~~50~~ 15 Increment ~~50~~ 5 | Min: 15 Increment 5 | Min: 50 Increment 50 |
| **GPT-4o-mini** | Min: ~~25~~ 15 Increment: ~~25~~ 5 | Min: 15 Increment 5 | Min: 25 Increment: 25 |

For developers and IT teams, this means faster time-to-deployment and less friction when transitioning from Standard to Provisioned offering. As businesses grow, these simple transitions become vital to maintaining agility while scaling AI applications globally.

#### Efficiency through caching: A game-changer for high-volume applications

Another new feature is Prompt Caching, which offers cheaper and faster inference for repetitive API requests. Cached tokens are 50% off for Standard. For applications that frequently send the same system prompts and instructions, this improvement provides a significant cost and performance advantage.

By caching prompts, organizations can maximize their throughput without needing to reprocess identical requests repeatedly, all while reducing costs. This is particularly beneficial for high-traffic environments, where even slight performance boosts can translate into tangible business gains.

#### A new era of model flexibility and performance

One of the key benefits of the Provisioned offering is that it is flexible, with one simple hourly, monthly, and yearly price that applies to all available models. We’ve also heard your feedback that it is difficult to understand how many tokens per minute (TPM) you get for each model on Provisioned deployments. We now provide a simplified view of the number of input and output tokens per minute for each Provisioned deployment. Customers no longer need to rely on detailed conversion tables or calculators. 

We are maintaining the flexibility that customers love with the Provisioned offering. With monthly and annual commitments you can still change the model and version—like GPT-4o and GPT-4o-mini—within the reservation period without losing any discount. This agility allows businesses to experiment, iterate, and evolve their AI deployments without incurring unnecessary costs or having to restructure their infrastructure.

#### Enterprise readiness in action

Azure OpenAI’s continuous innovations aren’t just theoretical; they’re already delivering results in various industries. For instance, companies like [AT&T](https://customers.microsoft.com/en-us/story/1637511309136244127-att-telecommunications-azure-openai-service), [H&R Block](https://customers.microsoft.com/en-us/story/1771647415089854527-hrblock-azure-ai-studio-professional-services-en-united-states), [Mercedes](https://www.youtube.com/watch?v=ocxnhqZuS8w), and more are using [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/) not just as a tool, but as a transformational asset that reshapes how they operate and engage with customers.

#### Beyond models: The enterprise-grade promise

It’s clear that the future of AI is about much more than just offering the latest models. While powerful models like GPT-4o and GPT-4o-mini provide the foundation, it’s the supporting infrastructure—such as Provisioned offering, Data Zones deployment option, SLAs, caching, and simplified deployment flows—that truly make Azure OpenAI Service enterprise-ready.

Microsoft’s vision is to provide not only cutting-edge AI models but also the enterprise-grade tools and support that allow businesses to scale these models confidently, securely, and cost-effectively. From enabling low-latency, high-reliability deployments to offering flexible and simplified infrastructure, Azure OpenAI Service empowers enterprises to fully embrace the future of AI-driven innovation.

#### Get started today

As the AI landscape continues to evolve, the need for scalable, flexible, and reliable AI solutions becomes even more critical for enterprise success. With the latest enhancements to Azure OpenAI Service, Microsoft is delivering on that promise—giving customers not just access to world-class AI models, but the tools and infrastructure to operationalize them at scale.

Now is the time for businesses to unlock the full potential of generative AI with Azure, moving beyond experimentation into real-world, enterprise-grade applications that drive measurable outcomes. Whether you’re scaling a virtual assistant, developing real-time voice applications, or transforming customer service with AI, Azure OpenAI Service provides the enterprise-ready platform you need to innovate and grow.

[Start today with Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service/)

The post [Accelerate scale with Azure OpenAI Service Provisioned offering](https://azure.microsoft.com/en-us/blog/accelerate-scale-with-azure-openai-service-provisioned-offering/) appeared first on [Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog).
