---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/a-walkthrough-of-azure-copilot-what-it-is-how-it-works/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/-qZZnwgb2ss/maxresdefault.jpg)

hey everyone in this video I want to talk about Azure co-pilot this is starting to roll out as we speak today you have to go and request to sign up but I wanted to go through exactly how this technology is working because I always think if we understand how something works it gives us the confidence the trust to actually start adopting and leveraging the technology now when you hear about the C 

Pilots you always hear it talked about with generative Ai and large language models the ability to interact with natural language and that model is going to predict the next word and the next word and the next word to an end of sequence a response and it's a very natural interactive type experience and obviously they're bringing these to more and more Technologies so I wanted to talk a little bit about well how do these actually work work and then how do they 

work with our data in the context of azure so if we take a step back if we remember that this model we use is gp4 and so the GPT 4 comes from open AI so you have open Ai and what they do is they have huge amounts of data that they use for training and really the whole point is 

you have this large um neural network of parameters and the training essentially works out well what are the optimal weights and biases that will make it fit the training data which is this huge amount of knowledge that is takes a huge amount of time it takes a huge amount of GPU and computational power but once that training has been completed by tuning all of the parameters is available you 

get your large language model that then you can use to feed in a prompt the information I give it and it does an inference it does that prediction of the most probable next token the next token next token i r response and so we're talking about this GPT 4 at time of recording is the most powerful model from open AI over time they obviously release newer ones I'm overtime 

Microsoft will adopt newer ones but open AI trained that model and I can think that all lives in the open AI space so then if we think of a boundary now we have Microsoft Microsoft are not using the open AI instance of the running model that is used for open AI Services what they do is they take a copy so Microsoft 

have multiple copies if you think there's there Microsoft 365 there's Dynamics 365 there's Azure open AI Services as aure co-pilot they take a copy of that large language model which once trained is read only at this point I'm not adding new knowledge into it it has been trained on that huge amount of knowledge that enables it to have those interactions but it's Now set in stone 

it's not modifying Its Behavior and that really is actually a key point so Microsoft do not fine tune these models there are ways to adapt behavior of maybe the types of interactions you have with it this is just the regular gp4 large language model they're not tuning it they're not changing things all of the interactions come from really a lot of work with the prompt The Prompt engineer hearing I.E what we give it for its 

input and then adding extra information you'll hear about this retrieval augmented uh generation rag which is all about how can I give it more information so it can create these great experiences for us and that's exactly what's happening so the model is just the regular model and then it's how we interact with it that actually gives us that great experience so how then if this is the 

case does it get information on our knowledge on our Azure subscriptions on the Microsoft documentation and that's what I want to walk through um to give you that idea the whole point is it's its ability to go and Via this Azure co-pilot which is the orchestrator go and talk to other things and I did videos specifically on retrieval augmented generation and vectors and embeddings I did a whole 

module on generative AI I think it's something everyone should understand in this day and age this is going to become more and more common pace so if you understand those Concepts I think it will really help you out so if you have a little bit of spare time I would highly recommend going and watching those but let's think about just walk through what happens in an interaction with aure co-pilot so I am the user so I'm my 

user and I'm interacting with the Azure portal now in my interaction with the Azure portal I'm on a certain page on a certain resource so there's a certain context with what I'm doing in the Azure portal at any particular moment in time and then I bring up the copilot option and I I ask it something so I'm 

asking it I'm giving it a prompt so at this point I have a prompt that I'm typing my question um what manage diss am I not using what's my most expensive resource how can I make this VM more highly available are there any outages affecting me right now hey help me create a manifest to deploy a kubernetes service whatever it is that prompt and my current 

context is sent to the Azure co-pilot now at this point that alone if I just sent it to the large language model so say this is step one would not be that useful there's not enough information remember all it's been trained on was that initial data which was not Azure specific in any way it has no knowledge to anything I have it needs some more useful information 

so where is that more useful information well I could think about well obviously we have things like the Microsoft docs which are changed very frequently and updated with new capabilities so yes the Azure copilot can go and interact with those then also remember there's the Azure resource manager that is the control plane for everything we do in Azure that is our entry point 

so through that I have things like the Azure resource graph which enables me to query information about anything in aure there's things like cost management there's the Health Service Health um support capabilities and then I'll talk more about this but then there's also in this case some specific sets of skills and fun functionality that are being exposed 

with the co-pilot because if if I think about it for a second Azure resource manager can hook in and do anything in Azure however realize some of those things it could do are very powerful if I have the permissions delete resources modify them and it's a bit different from say I office with office if I went and updated a slide with Cod pilot and I didn't like it I can do control Z and I'll undo it well it's not the same with these real 

resources and so what Microsoft being very careful about is when it's exposing functionality that can actually modify or delete things they want to make sure the right guard rails are in place the right checks the right confirmations are in place so we don't do harm through these natural language interactions so the whole point that these are put in all of the right guard rails 

confirmations etc etc around anything it may be interacting with so it's just a really important point with what we want to do okay so there's all this information available to us so this is the point of the co-pilot so one of the things the co-pilot is doing it's the orchestrator for our AI interactions so I give it a prompt and some basic context it looks at this and then it works out what other 

information may be required so it can then send to these some questions it might be run a resource graph query and give me some information on cost management give me information from the docs whatever it is it gets a response back with additional data and this is that retrieval augmented generation we're getting additional information we're 

going to give to the prompt so this data is now used for grounding the request I'm going to make the prompt I'm grounding it in this additional data it can go and get the co-pilot will now also modify the prompt it will create something called a meta prompt so now it can actually go and ask the large language model hey here's the meta prompt so it can add in extra 

specifications to what is being sent it could also describe hey here's what I want you to do here's some information so it's also going to add all that information that we got but it can also describe functions by the way um I have the ability to call these functions if you need more information so what might happen is this will then generate the response 

but sometimes it may actually respond with a plan and the plan is hey I want you to run these things for me so there'll be a few iterations of this inference these responses to make sure it gets the right information and then this can tidy up when it finally does get a response and great it can go and send it back and I get this nice response to the user and 

they're all happy and delighted about what they're seeing um and so that is fundamentally how it's working now the key part you see in this what we don't have is the large language model has no direct access to anything of yours it cannot go and hook into Azure resource manager manager or anything else it is a readon model we 

fixed neurons and the parameters all it can do is act on the data it's given and give a response if it needs more data hey I ask it what are my um unused managed discs and how much is it costing me well it might initially get sent a resource graph query maybe of how here's my manage discs that are not connected to a VM but then it's going to say hey I 

need you to run a query against cost management to get me the pricing for these resources so then this would go and do some more retrieve log man generation send a prompt back with the history of the previous and now the cost information so now it can go and give her response and oh it's costing me this much and then it can go and send it back so it always has to go via the co-pilot the orchestrator and so you'll sometimes see iterations because it wants to go and get more data but it has no access 

whatsoever it has to go through the co-pilot that can enforce all those responsible AI principles and everything else that brings us on to an important point then because one of the things people always get scared about is well okay well what do the co-pilot nager enable the user to do that maybe they couldn't do before so let's focus on this side of the interaction with the co-pilot talking to different things here and really the most important thing to 

consider is remember the user has a certain set of roles the role-based access control on the Azure resources the Azure co-pilot when it talks is not running as its own service principle with complete permissions everything the co-pilot does is what we call it on behalf of flow I.E it can only act on what the user can 

act as what the user can see it can see if the user can't see it it can't see it so it is acting on behalf of the user for all of the interactions with the Azure resource manager if I don't have permission to run this Azure resource graph query against those resources nor can this if I don't have the permission to see that resource or modify that resource nor can this it cannot do anything the user can 

do and the key point is we're going via arm and remember what does arm do arm is our control plane and arm is what well it enforces any policy so we're not bypassing any policy any guard rails we have configured arm is what enforces Ro based access control so I can't bypass any permissions that are set are is what 

enforces budgets co-pilot cannot do anything you couldn't do already through the portal I honestly think of it a little bit the old argument used to hear with Powershell when Powershell first came about everyone freaked out so oh no you must disable Powershell people are going to wreck havoc Powershell didn't let you do anything you couldn't have already done another way it may have made it more efficient but it wasn't bypassing 

anything it was just another way of doing things this is exactly the same co-pilot makes us more efficient it helps us if we're not sure how to do something it will suggest next paths it can help us do certain activities but it can't do anything that I couldn't already do if I found my way around the portal if I worked out a script it's just it would take me a lot longer so it is enforc it can only do what I can do it's 

still going through the regular apis so it only has my level of access that's really the most important thing so it is only my access it's not a back door it's not going to do anything else one of the nice things here if we think about it for a second then because we are just using arm well there are remember all those other resources I may 

have so I may have resources on premises server operating systems whatever it may be so now if I Arc enable them what does Arc do Arc extends the Azure control plane to other resources and also lets me apply certain Azure skills and capabilities to those resources well if the control plane is extended and knows about it technically the co-pilot can hook in so if I run an 

Azure resource graph query for example through co-pilot for its interactions it would know about my arc enabled resources as well so it's actually really nice that it's it's not recreating the wheel or doing anything special there I'm going to be able to take advantage of all those things as well so hopefully that helps clear up a big element of well is it safe to use um is it going to Havoc it can only do what the user can 

already do it's just making me more efficient it will help me along the way now I don't want to do a big demo of Code Pilot there's been great sessions and great things done already but I guess in case you've not seeing it I'll show a couple of quick things and maybe just have a little bit of fun now again today you have to on board and there are certain requirements around it but once you are on boarded you'll see your little co-pilot uh up here 

and there were limitations and I'll talk a bit more about that to how many chats you can have a day and how many interactions per checks obviously this is all using um resources so you obviously have to be careful with this but it's asking me hey how can I help I mean what's the most powerful thing we might ever want to do can you change the theme to Black and then you can see it sort of thinking about things so this may actually oh and then it's 

done I'll just stop that see you saw it go through his interaction so that may have actually been going back and forth a couple of times to say hey what should I do what the documentation okay what's the API call but we saw that in action to complete the thing I was trying to do um I never even actually tried this can you set it back again not even sure if that will work I've never actually tried typing that 

but it does so notice that that's really cool so it changed it back to blue because it has the context so one of the things that happens here is when it has these interactions and we talked about there's a certain number of chats it allows when it sends this meta prompt it also sends it the history of the previous interactions so it has a larger context to make it a lot more natural interaction if it wasn't doing that when I said change it back be like change what are you talking about back to what 

it has the context so that's actually a really nice feature here okay so what else could we do um so it can generate CLI scripts um can you create a script to start all VMS with an owner of John savle so now it can go away it can look at document ation it can go and understand okay what 

does an owner of John savle mean and it can go and create a script and notice it's doing that determining what to do a couple of times it might be bouncing back and forth to the large language model back and forth the orchestrator is going to go and talk to the arm it might be looking at the documentation to work out so notice here it's giving me my answer okay one option is a VM query tags owner John 

savl and then I could start those IDs so it's helping me do that task and one of the nice things you're actually seeing here is it does have the Run button so if I do the run button it will open up a cloud shell and I could copy the code and just execute it so it makes it very easy to interact and it understands the monitor information it understands kql which is used to things like log analytics and ACC course the resource graph it understands yaml for 

AKs manifests um list all my unused public IPS so here would have to go and look at the Azure resource graph once it's worked out what is the right kql to ascertain what is the query to find what is an unused IP 

so see it's so looking at resources where it contains public IP address and is empty properties is IP so it's working out what is the query so it's looking for this is empty and then it will go run it for me and now it's going found okay I've got an empty public IP address and notice it's then giving me suggestions we'll delete them um maybe assign it and I could do 

the same thing with uh discs show me all of my unused discs then what's the cost of the discs how could I delete them I could ask it to summarize my cost for the last three months and one of the great things actually just look up the documentation um because as we go through it has these enhanced scenarios so if we look at the documentation it gives a whole bunch of prompt you could try and it notice here 

it's doing a much more complicated kql query it can help you deploy VMS more effectively and this is actually a really nice one so remember I talked about the idea of the context so imagine I'm just creating a VM let's create a new virtual machine and let's say I just select a region and maybe I'm like well you I'm not sure exactly what to do so I might 

say how can I make this VM more resilient and while it's doing this this is what I was talking about so today and this may or may not change I can have 10 requests per chat and I think it's five chats per 24-hour period so it's not like I can just do an infinite number so notice it's saying look I can help in a number of ways multis zonal VM scale 

sets public IP and it's saying hey do you want me to help you select multiple zones so if I select this notice what it just did it automatically went in and set me to two zones which now means it created two VMS and then it's going to guide me it's like hey do you want me to help you add a load balancer to your solution so it's going to walk me through that complete process of helping 

me and this is it its whole point of what it's trying to do but I'm just going to cancel that out okay so what else could it do um how can I make my storage accounts more secure and once again it does this really nice interaction now I have lots of storage accounts so one of the things it's going to do look you open up the page and it's like select one which 

storage account do you want me to go and look at for you so I'll say okay I'll pick that one do you want me to run a security check on that account yes please and then it will go and do an analysis based on its best practices based on its knowledge based on the skills that remember those different product groups may have created that can be the most benefit that has the right guard rail on it and it can come back and guide me and 

it's the fact that you have these skills you're going to see different levels of interaction with different Services they're going to grow over time but it's all being done with safety in mind to make sure hey we something doesn't happen that we don't want to do and that's giving me a bunch of recommendations hey look oh it doesn't require secure transfer oh it's not using private end points allows Anonymous blob access so a whole bunch of great things and then again it gives me some recommended next steps well okay 

what are private endpoints how can I enable them how do I enable secure transfer so it's constantly guiding me through maybe right now um are there any Azure problems impacting me so then it can go and hook into service health and let me know are there any active incidents going on that might be impacting any of my resources are subscriptions no there's 

not I'm healthy and all good to go so it's constantly helping me do the things that I'm trying to do and once again if we look at the doc so I'm not going to go through all of these but for example like Kuban 8s it will help create a manifest file it's just quicker than me typing it in but hey you ask it what you want it to do and it will go and create it for you it can again generate the CLI scripts 

and there's examples of here we saw that as well um optimize code so I it can help me do what I'm doing things like Cosmos DB currently hooking directly in Cosmos DB um actually with its interaction so if I look at data Explorer you'll see it has its own direct hooking to query with copilot so you can use natural Lang language to interact with it but 

different services are hooking at different levels but for all of these Services they're following the same principles it's using the same pattern of it can only do what you can do everything about arm the policy the arback the budget is informed if there's any risk hey these skills have the right guard rails to prompt you and guide you it's like all the co-pilots is there to help you do your job is there to help me be more 

effective um but as you saw today there are some limits around the number of interactions per chat number of chats I can have because that llm it takes a huge amount of time as I talked about to do the training but it also requires a huge amount of GPU and power to do the inferencing so there there's there's Protections in place to make sure it really doesn't get out of hand now there 

is no pricing details right now I don't know if there will be pricing I don't know what that pricing will be no idea but that will come over time as it moves out of these private previews and obviously when it's GA they'll announce whatever the pricing model will be now I did want to discuss two things that I've already seen come up one is can I limit which subscription ions can use as a co-pilot because today you 

enable it at a tenant level and then all of the subscriptions that trust that tenant get it and the answer is no you can't because remember the portal if you look at the portal This Is Not subscription specific within the portal this this bar at the top is just the Azure portal and then yes I can granular select a certain subscription but the portal is multi subscription so there is no concept of turning the co-pilot on or off at a subscription level you you don't you 

don't do that the next thing that comes up is well okay well I want to stop co-pilot being able to make any changes I'm a big infrastructure's code shop I want to make sure people don't start using co-pilot to change things and to that I would say again co-pilot can only do what the user can do and it can only do what the user can already do in the portal so if I'm a big infrastructur as code organization and I want everything 

done infrastructur as code well today the users could change things in the portal anyway the co-pilot is just another method of interacting with that if I want to make sure my users don't change things in the portal well then I should really be thinking about what are the permissions I'm giving the user so maybe the user ordinarily only has a read permission so they can go into the portal they can 

look at the resources look at the insights look at the monitoring but they don't change anything think zero trust think least privilege they shouldn't have standing permissions anyway and then the right way to do the things would be well hey I can have my write my infrastructur as code which I then commit to my repo when I do that commit hey it can trigger my cicd 

Pipeline and that pipeline runs a certain service principle and that service principle is the one that maybe has contributor it is the one that then has the ability to go and deploy the user can't anyway so if the user had the right per missions co-pilot won't be able to go 

and change anything to help the user because the user doesn't have the right permission to anyway so if I'm big into infrastructure's code I don't want the portal use I don't want Cod pilot to change stuff they shouldn't be a to do it anyway there's nothing special about Cod pilot the user should be restricted and sure I totally get it if there's exceptional circumstances well that's when we use things like pin so I could always have the ability that they can get contributor if they Pim up for a Time limited window in an 

exceptional circumstances you can still do that but my normal day today hey the user shouldn't have contributor just sitting around anyway which means when they're using Cod pilot or the portal or the CLI or anything else they can just view they can't change the things if you want to disable click Ops don't let them have the permissions the pipeline should have the permissions that goes through the right approvals and the guard rails the to check those things so maybe a longer answer but no I can't stop 

copilot changing things because it's kind of pointless anyway because they would just change things through the portal if I don't want that behavior to happen I need to set my permissions correctly and that's the key point so I hope that answers the questions about it the whole point is that the co-pilot is only doing what the user has the permissions to do 

it's still going through all of the same API so all of my normal policy and allback and budgets will apply for anything beyond the more General resource graph cost management Health there are special skills that have additional guard rails where I might want to double check where I might advise differently but we saw there's some great interactions with the context around hey the VMS um the storage accounts the C cosmas AKs it's there to help me do the job 

nothing I am doing is used to train the model the train model is readon it's a copy from open AI it runs in the Microsoft security and Regulatory and Trust boundaries it has zero access to anything everything it wants to do it has to ask the Azure Cod pilot which goes and gets the data runs the make sure we got the good responsible AI principles applying it's running as the user so it can only do what the user 

could do anyway and ultimately it just helps me do my job better and that's the point so as always I hope this was useful and until next video take care
