---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/how-does-c4-and-plant-uml-help/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/max/823/0*7U-t7tz6CHz11Kt1)

**Author:** Mstislav Kazakov, Head of Python Practice at [Usetech](https://usetech.com/).

In this article, I’ll explain the nuances of working with PlantUML and C4 model. All the information is a distillation of our daily experience.

### **What problems do we solve?**

If there are no accepted standards for drawing diagrams in the team, then when it’s necessary to graphically represent certain nuances of the system. We draw diagrams ad hoc, without considering any design standards, generally accepted notations.

As a result, during the life of the project, we have piled up images with different figures, with different arrows, all in different colors. As the cherry on the cake — a legend for all this artwork, in most cases, doesn’t exist.

Let us clearly articulate the resulting problems:

**1.** The connections between the elements are often ambiguous;  

**2.** The meanings and purposes of the elements are ambiguous. When discussing architecture, you probably used words like component, module, subsystem, system, and everyone probably meant something different;  

**3.** Too much or too little detail in your diagram;  

**4.** Levels of abstraction are mixed up;  

**5.** Often, no context is provided.

These issues lead to the fact that only the people who were involved in drawing the diagrams have an understanding, and that understanding exists for a fairly short period of time, because due to the lack of standard and legend it is not always possible to remember what you meant a month ago under, for example, the red square.

In addition, the modification of drawn diagrams, which are usually saved as images, is actually impossible because of the lack of sources or, even if they are available, the constant change of tools.

### **How does C4 and PlantUML help?**

C4 offers us a preconceived and very limited number of abstractions. This allows the entire team to use single abstractions, and at the expense of a few of them, reduce the cognitive load. In this article, I will not look at all abstractions, but only boundaries, systems, containers, personas, and relationships.

So how does PlantUML help us? With it, you don’t have to think about how to design your diagram. We’re engineers, not artists, after all.

You don’t need to have heavy, complex design and rendering tools — many development environments already support PlantUML, so you as a developer probably won’t even have to install and learn a new tool. In addition, there are many online editors, and in a pinch you can always get the PlantUML server at your company or computer with one command and docker.

A big plus of PlantUML is that it is plain text, and therefore the versioning of your diagrams is done with Git or any other version control system.

### **What is architecture?**

To be on the same page, I want to clarify how I interpret the concept of architecture in this article.

Firstly, these are important things. You have to understand what the important things are and convince the people around you that they are important. In addition to that, they will be difficult to change in the future, and therefore they must be taken early in the development of the solution.

Speaking of architecture, it is worth noting that as an architect, you have to be good at structuring information. For example, make one simple model out of 40 pages of documentation.

### **What is PlantUML?**

![](https://miro.medium.com/max/700/0*7U-t7tz6CHz11Kt1)
PlantUML is a language, a tool that allows you to create diagrams using a text description. This text description can be rendered with many tools.

### **Benefits of PlantUML**

As I wrote earlier, PlantUML makes it easy to support diagrams — it’s a simple, free tool, open source and cross-platform.

PlantUML has a low entry threshold, and it allows all team members such as analysts, developers, QA to draw sequence diagrams, activity diagrams, and other commonly known diagrams. The whole team takes part in the drawing using a single tool, without wasting time discussing and arguing about the design and notation used.

The implementation of PlantUML allows you to see the evolution of a particular architectural solution and versioning, because PlantUML, as I said before, is a trivial plain text document.

PlantUML allows you to render a PlantUML document without having to go through the extra step of exporting the image to Confluence, GitLab, Sphinx, because most systems support PlantUML rendering with minimal configuration. This prevents an inconsistency between images in your knowledge base and PlantUML source code in your repository.

Now let’s talk about C4.

### **C4 model**

![](https://miro.medium.com/max/700/0*IKvNK9WTvF6WKObu)
The C4 model was developed by Simon Brown, inspired by the 4+1 architecture representation model and UML. He pointed out that notation is secondary, abstractions are primary. It doesn’t matter what images you draw, as long as you operate on the same abstractions.

Simon Brown himself suggested 4 levels of abstraction: systems, containers, components, and code. I propose to consider only the systems and containers level.

It’s important to clarify that the name “containers” came about before Docker became popular. So when we say “containers” we don’t mean Docker, we mean some abstraction behind which could be a database, a data bus, a script. Something that is part of the system. In fact, a container can also be a Docker container.

It’s also important to understand that C4 isn’t directly related to PlantUML. PlantUML is just a tool that allows us to create‌ C4 diagrams.

You can even use Paint to operate with the abstractions and design proposed, but then you lose the pluses of plain text.

### **The C4 model: Systems**

Let’s talk about systems in C4.

Looking at a diagram that consists only of systems and personas will allow you to see the system on a smaller scale and how it fits into the surrounding environment.

A systems-level diagram answers **the following questions**:

**1.** What kind of system are we developing?  

**2.** Who uses the system?  

**3.** How does it fit into the current environment?

The primary focus at this level should be on actors and on systems, not on technology, protocols, and other low-level details.

A systems-level diagram allows you to:

**1.** See which system is being added to the current environment;  

**2.** Show it to colleagues with less technical immersion, without fear of misunderstanding;  

**3.** Understand who you probably need to go talk to in order to negotiate cross-system interactions.

The image below is a diagram. Let’s look at it and imagine we were developing a system that:

**1.** Has a web interface with a list of messages and the ability to send a response to them;  

**2.** This system is able to publish the responses sent to Facebook and Twitter;  

**3.** At the moment, we see that there is only one person who works with the system — the operator. The gray color indicates external systems, blue — our system.

![](https://miro.medium.com/max/430/0*CAltqf07Qv2ctuzJ)
### **The C4 model: Systems #2**

However, the publishing system is so well-designed that some external systems like, for example, AMO CRM, wants to connect to us and use as a message delivery system. At the moment, AMO CRM only knows how to publish responses to email, but wants to be able to publish responses to Facebook and Twitter. Let’s see how it looks now, let’s draw it next to our system (in the image below).

![](https://miro.medium.com/max/526/0*1Nf6Fn0hDKwSgizi)
### **The C4 model: Systems #3**

The second actor has been added — the AMO CRM operator. Now let’s connect our system and AMO CRM.

![](https://miro.medium.com/max/653/0*PFpzouobvnj_prc3)
In the end, we see some pretty obvious things, but it can lead to useful insights. For example, our project manager, looking at the diagram, might realize that we can try to take away their email messaging if we teach our message processing system to do it better.

Let’s go ahead and give this diagram to the architects, to the developers, to go into more detail. But first, let’s talk about containers and the relationships/interactions between them.

### **C4 model: Containers**

Containers represent a kind of application, a data repository. By data repository you can mean a file, a file system or a database, etc. It’s customary for a container to:

**1.** Give an understandable name;  

**2.** Specify a common list of technologies used. For example, for the software you are developing, you can specify a name, a language version, and a basic framework;  

**3.** You should give a brief description of the container and describe its primary responsibility.

A container diagram allows you to answer the following questions:

**1.** What technology is used in the system?  

**2.** How are responsibilities distributed in the system?  

**3.** How and which containers interact with each other?

It is common to specify for relationships between elements:

**1.** The purpose of the communication — writes, reads, sends, creates, receives — it all depends on the context;  

**2.** The protocol, the mechanism of the communication: HTTP, AMQP, Kafka, REST API, SOAP, etc.  

**3.** Communication style if necessary: synchronous, asynchronous, batch, i.e. when we send many objects at once;

In some situations, we can specify a port if this seems important.

A less obvious detail is the direction of communication, i.e. in which direction you point the arrow. Many people get confused here because, for example, in the HTTP protocol every requester implies a response, so the connection should be bidirectional, but that’s not true.

We are interested in the question: who is the initiator of the request, and who is the recipient? So the arrow comes from the one who sends the request.

So, back to the design. Earlier we wanted to give the diagram to the architects, to the developers, to think through the details.

What will they need to do? First, reveal the details of the message handling system. Second, add technical nuance to the relationship between the AMO CRM and the message processing system.

**Technical nuances of the system under discussion**

I’ll briefly tell you the technical nuances of the system:

— All posts that need to be published are saved in Kafka;

— For each social network has its own topic;

— From the relevant topics are read containers engaged in the publication;

— Since we don’t have an external API — note the connection between the operator and the feedback form. It says that the internal API is used, and it’s too early to design an external API (because we are solving one specific problem and generally experimenting). We make the PoC for integration with AMO CRM as simple as possible: we create an adapter for requests from AMO CRM, convert the input data into the format we need and simply write to the appropriate Kafka topic;

— We’ve uncovered the nuances of Facebook and Twitter;

— We’ve indicated which protocol is used for the interaction between the AMO CRM and the message processing system.

### **The C4 model: Containers #2**

![](https://miro.medium.com/max/700/0*_YYXnA0ck77NHzVc)
Now moving on to the nuances of the chart itself:

— First — boundaries appeared. In particular, we see the boundaries (dashed lines) in 3 systems — the message processing system, Facebook and Twitter. Thus, we show that we went deeper into the system, i.e. increased the scale;

— Containers within the message processing system have information about the selected technologies;

— Links between containers have appeared protocols and nuances of interaction (an example with the internal REST API);

— Some containers within the messaging system I marked in gray, that is, they’re supposedly external containers. I did this to make it clear at first glance which container is being added, which containers are being modified, and which containers remain untouched. In our case, only one container is being added — the adapter.

Now, I propose to take apart the source code of this diagram

### **C4 + PlantUML: The Basics**

```
1 @startuml  
2 !include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Container.puml  
3  
4 skinparam wrapWidth 300  
5 LAYOUT_WITH_LEGEND()  
6 LAYOUT_LANDSCAPE()  
7   
8 title  
9 <b>FeedbackPublicationArch-simple v2022.11.02</b>  
10<i>Feedback system: publication</i>  
11 end title  
12   
13 System_Boundary(facebook, "Facebook") {  
14   System_Ext(facebook_api, "Internal API")  
15 }  
16   
17 System_Boundary(twitter, "Twitter") {  
18   System_Ext(twitter_api, "Mobile Interface")  
19 }  
20   
21 Person(operator, "Operator")  
22   
23 System_Boundary(message_processing_system, "Message processing system") {  
24  Container(amo_adapter, "AMO CRM Adapter", "Python 3.10, FastAPI", "Receive data for publication from AMO CRM and push it into message queue")  
25  Container(feedback, "Feedback system form", "Python 3.8, Django 3, React", "Create responses, push responses into message queue")  
26  SystemQueue(response_queue, "Kafka", "Publication responses")  
27  Container(fb_publsher, "FB Publisher", "Python", "Publish responses on Facebook")  
28  Container(tw_publsher, "TW Publisher", "Java, Selenium", "Publish responses on Twitter")  
29   
30  Rel(feedback, response_queue, "Produce", "kafka")  
31  Rel(amo_adapter, response_queue, "Produce", "kafka")  
32  Rel(fb_publsher, response_queue, "Consume", "kafka")  
33  Rel(tw_publsher, response_queue, "Consume", "kafka")  
34  Rel(operator, feedback, "Response to publication", "Internal REST API")  
35 }  
36   
37 System_Ext(amo, "AMO CRM", "Browse income messages, send responses")  
38 System_Ext(email, "Email")  
39 Person_Ext(amo_operator, "AMO CRM operator")  
40   
41 Rel(amo_operator, amo, "Response to income messages")  
42 Rel(amo, email, "Send response to email")  
43 Rel_U(amo, amo_adapter, "Send response on Facebook and Twitter")  
44   
45 Rel_L(fb_publsher, facebook_api, "Publication", "HTTP")  
46 Rel_L(tw_publsher, twitter_api, "Publication", "HTTP")  
47 @enduml
```

**1.** Let’s start with the first and last line. This is how any PlantUML diagram starts and ends.

**2.** Earlier, I wrote that PlantUML is not directly related to C4, but only allows you to write code that is rendered into a C4 diagram. But in fact, I lied a little bit. Out of the box we won’t draw a C4 diagram, but by plugging in a file that defines procedures that render the corresponding elements, we can use them to render a C4 diagram. You can see the connection of the file on the second line. You can also connect local files, i.e. access to the Internet is not necessary for drawing C4 diagrams.

**3.** Look at lines 8 to 11. I find it necessary to give the diagram an alias, version the diagram with CalVer, and give a human name or a short description. This helps in communication, in organizing the knowledge base: you get to refer to a more or less unique diagram name (alias).

**4.** Let’s break down boundaries, systems, and external systems.

**4.1.** You can see how to create a boundary from lines 13 to 15. The procedure System\_Boundary is called, the first parameter is an alias, the second is a human-readable name of the boundary. After the curly brackets we have the definition of containers or systems inside the boundary. Just in case, let me remind you that borders are dotted lines;

**4.2.** On line 14, you see a call to the procedure System\_Ext. The parameters are the same as those of the System procedure — alias, name. As a result, you see a gray rectangle that implies an external system. To define a non-external system, i.e. to make it blue, just remove the \_Ext postfix.

**5.** Now let’s talk about containers. Containers can also be external — here it’s simple — similar postfix “\_Ext”. Containers can represent the database, the Message Queue (look at line 26 — Kafka is depicted as a queue), or they can just be rectangles (eg line 24).

The Container procedure (and similar ones) take the following parameters: alias, human-readable name, technology, container description.

**6.** Relations. Links are defined by the procedure Rel. It takes the initiator, the recipient, the description of the link, the protocol. Look at line 30.

Links within system boundaries are defined within boundaries. Inter-system links are defined outside the boundaries. For example, look at line 40. You may have noticed that I didn’t specify a protocol. That’s because I’ve drawn big strokes on the interaction of external systems, and I don’t need to know what protocol the interaction is using.

### **C4 + PlantUML: making it presentable**

Now let’s talk about the big pain: trying to make diagrams more or less presentable. Why is this a pain? Because with a relatively large number of containers, systems, and relationships, the positioning of elements can be rather unobvious.

**1. skinparam wrapWidth 300**

![](https://miro.medium.com/max/333/0*uEcRvS7HbD9YwJGg)
![](https://miro.medium.com/max/491/0*5kRlkThXKF5sqSNq)
Let’s start by increasing the allowable size of the text to be displayed without wrap. To do this, add the line `skinparam wrapWidth 300`. You can see the difference in the image in point 1.

**2. LAYOUT\_WITH\_LEGEND()**

![](https://miro.medium.com/max/300/0*NucjULxLGmYgx6Mm)
In the next step, I propose to turn on the legend, which by default will be displayed in the bottom right corner. This will remove unnecessary `container` type text from the rendered elements, thereby saving space on the diagram.

### **C4 + PlantUML: making it presentable #2**

![](https://miro.medium.com/max/700/0*xQ3tDfGsw65uBb2Z)
In the image, you can see that the procedure Rel\_U is used instead of Rel, but it takes the same parameters as Rel.

Rel\_U(amo, amo\_adapter, “Send response on Facebook and Twitter”)

U stands for Up. Similarly, there are postfixes L, R and D (left, right, and down). In our case, Rel Up says that the communication between AMO CRM and the AMO CRM adapter should be from top to bottom.

In the first diagram you see the use of Rel\_Up and AMO CRM (located at the top), and on the second you see the use of the normal Rel. Without Rel Up, the diagram is longer.

![](https://miro.medium.com/max/700/0*CKURzWvrzeZg2AKW)
Unfortunately, this kind of positioning doesn’t always work. If it didn’t work with one container or system, try positioning others. Look for the best options. Changing literally one letter in one relationship can completely flip your diagram in both good and bad ways.

### **C4 + PlantUML: making it presentable #3**

There are also procedures for changing the drawing direction. Let’s look at them.

**LAYOUT\_LANDSCAPE()**

![](https://miro.medium.com/max/700/0*I_-lzmWNlHYo1TKN)
On the first, you see the diagram after the LAYOUT\_LANDSCAPE() procedure is called, i.e. it is drawn from first to second.

**LAYOUT\_TOP\_DOWN()**

![](https://miro.medium.com/max/700/0*Z5KDJA1gX8vXfPCu)
On the second, you see the diagram after the LAYOUT\_TOP\_DOWN() procedure is called, i.e., it is drawn from top to bottom. Top-down drawing is enabled by default.

What you see doesn’t mean that drawing from first to second is always better. It’s just that it’s better for the current diagram.

### **C4 + PlantUML: making it presentable #4**

Let’s look at the shape of the links. Earlier, you saw the default form of links: in this case, link forms can be rounded off as needed.

**skinparam linetype ortho**

![](https://miro.medium.com/max/700/0*dT832Ve5dax3PezA)
If you set the line type to ortho, the links will be as straight as possible with as few corners as possible.

At first glance it looks pretty good, but I’ve noticed that with this style of links, the position of the descriptions becomes unobvious, and sometimes it’s hard to understand which link belongs to which description.

**skinparam linetype polyline**

![](https://miro.medium.com/max/700/0*MaGfHkgS4tprIP9X)
With polyline, there are far fewer problems with the position of the link description.

An important clarification: I purposely use the top-down drawing, because it looks worse for this diagram, and the differences in arrow style are much more noticeable on bad cases.

That’s where I’d like to end about beauty. However, there are still many possibilities to change the legend, re-color the links, containers, add icons for containers and so on, but that’s not too critical.

Also keep in mind that under the hood of PlantUML uses a utility package for graph visualization — graphviz and various display settings you can find out by reading the documentation for this particular package.

To summarize, this is most of what you might need in your work. Of course, there are still quite a few other details and features, but even with the knowledge you already have, you can cover most of your tasks.
