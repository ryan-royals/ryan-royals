---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/using-the-well-architected-framework/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/vTjasx3ahjM/maxresdefault.jpg)

hey everyone in this video I want to explore the very recently refreshed well architected framework now before I talk about the well architected framework if we just take a step back I as an organization want to start leveraging the cloud now I'm going to talk about Azure specifically but as we'll see most of what we're talking about these principles actually apply to any cloud and also on premises to a great deal but 

it is focused around Azure when I talk about some of the examples now as an organization I want to adopt the cloud there's a certain set of governance and consideration and finops and identity lots of things I think about just adopting the cloud in general and I did a video a few weeks ago on adopting a which aligns very closely 

with Microsoft's Cloud adoption framework so I can think of the cloud adoption framework as being focused on the big organization level considerations and planning that I think about for adopting the cloud in general what are the the big picture things that I have to consider and then once I've got my organization 

governance my models in place then I have to think about well every individual workload so under my organization I'll have n number of workloads now it can actually get fairly tricky when we think about well what exactly is a workload in this context and I can really think of a workload as it's some collection of resources hey 

there might be different entry points there's going to be maybe some compute things there's going to be some data storage it could actually consist of multiple applications as we think of them as individual small areas there's going to be things maybe it goes and talks to but there's going to be obviously development processes that goes into a workload there's going to be certain governance certain identity certain monitoring 

aspects to it but I think of it as a business function a particular business workload so ultimately it's going to achieve some complete unit of work for the business so it's very typically going to align with a certain business team a certain Department maybe some organizational construct and that's what we're focusing on when we think about the well architected framework that we're going to consider it's about how do we 

architect this particular business function and what are the specific considerations we're going to apply per workload so if the calf was hey the whole organization now for every single workload that business function that business unit of work that we have in our organization what are the considerations we need to apply to that and so that's what a workload is 

well the guidance as I've already alluded to is WF and W I'm actually going to spell this I want to emphasize a certain point so this is the well architected framework and I'm really emphasizing the word architected for a reason 

because it is focused on the architecture now if you've used WFT before it has gone through a huge overhaul we actually jump over super quickly if we go and look at the documentation basically it is completely been restructured it is focused on architecture so just like I said well the cloud adoption framework it's not really Azure specific for the most part it's fantastic guidance for the whole organization 

is the same for the well architected framework they've really shifted it to being focused on what are the architecture principles we consider and then it brings in specific Azure Technologies all the way at the end whereas before some of the guidance was hidden behind Azure Technologies so WF is very different from the calf CF think of it as that organization Enterprise grade framework for the entire Enterprise to adopt the cloud WF is the 

best practice around the architectures so WF is driving a methodical framework to get the right designs for your workload and a key Point here and you can kind of think of it this way it is very much about well architected it is not about well implemented that is outside of the scope 

of the WFT now obviously Microsoft has things to help you on the well implemented side so if I want help around that well there's obviously things like the architecture Center there are things like Landing zones and obviously there's the product docks so there are things to help you with the implemented but I really want 

to stress Waf is about the well architected framework it is not concerns with the implementation but there are other things you could go and look at if you want help there there are service guides that help some aspects of specific Azure Technologies um but again focuses on the architecture part of what we want to do so what is the wff it's broken down into particular areas that follow really 

a logical mindset in how I would think about architecting a solution and the key areas of considerations when I architect something so I could start off with thinking well it starts off with pillars because if you think about architect in a solution hey I think about well it's resiliency I think about security I think about hey optimizing my 

cost I would think about efficiency of what I do um operational excellence around those things well they're the pillars that we're going to have have with the well architected framework so we can break it down into reliability which obviously super important we can think of it as security there's cost optimization 

then I can think about there's operational excellence and then there's performance efficiency performance efficiency 

so much to write so they're the core pillars that we think about when we're architecting something I'm always thinking of those things hey I'm architecting my solution okay how do I make sure it's reliable it's resilient to different problems um okay well what Solutions do I need to improve my security how do I make it efficient in what I'm doing and how to optimize my costs and so for each of the these pillars there are major sections to this 

so it starts off with the idea and again these these go across all of these so I can think about well there are design principles so for each of these we have design principles and really each of these design principles has some goal that it's trying to drive us 

to so there's design principles each design principle has a goal and then there's a set of approaches and benefits from them so if we go and look at the documentation we can see we start off in this section of pillars and we can see those five pillars that I drew out now let's just go and look at reliability here we can see those four sections that I mentioned and we're 

really starting off here with design principles if I was to go and look at this well reliability well we think of business requirements resilience recovery operations keeping it simple so often we can really trip ourselves up by making things overly complex and the more complex we make something well it actually decreases our resiliency our reliability and then we can see for each of 

these what are the approaches what are the benefits of going through designing for resilience distinguish components that are on the critical path identify potential failure points so I would go through and look at these understand what is it looking at and then what is the benefit to those and we'll see the same things for every single pillar cost optimization develop a cost model have an effective but flexible 

accounting model so these are all things that are going to drive me to design with the right considerations for each of those pillars in mind so this is the goal so I would go through these hopefully over time I'll I'll get more familiar with them and this will drive a lot of my core design now the next thing it has is because obviously there's a huge amount of that that then it has 

checklists now each of the checklists actually drive us to specific recommendations and those recommendations also have certain goals they're trying to drive us to and once again let's just go and look at that now if I was to go and look at my checklist it has a particular code and it has a particular 

recommendation and for each of those checklist codes I can select it and then I see specific detail around it how I can actually be successful in making this happen so it's really walking me through great amounts of information to help me be successful through this so I would go through the checklist and think about hey have I considered this have I read those detail to help drive that to be successful for 

my particular workload now the next section I think is amazing uh I think maybe this is actually one of my favorite things and it's tradeoffs and this is to me very very realistic because if you look at those pillars for a second they're not all loving of each 

other and hey we have a common goal and hey no issues whatsoever there are definite tradeoffs between these I always think of it for a second if we take out technology if you you've probably seen the whole thing hey you can have it done right you can have it done fast you can have it done cheap and the key point is you can pick two 

I have to compromise on something hey I can have it done right and fast it's not going to be cheap I can have it done right and cheap it's not going to be fast hey I can have it fast and cheap well it's not going to be right when I look at the pillars some of these things do often conflict and there are some really obvious ones now this is just an example this is not um full detail by any means at all but just one of the biggest examples of 

an EG you're ever going to see is when I think of cost optimization and then I think about the reliability generally speaking these are opposing goals uh cost optimization I want to reduce my spend Rel I ability often means increasing the spend I need 

additional instances of something I need them in multiple regions I need maybe some caching there there's things that I'm going to do that generally to improve my reliability there are sometimes I don't hey if I have workloads just sitting in a region level deployment and I can switch it to an AZ deployment doesn't actually cost me more but I've increased my reliability without impacting my cost but very often um they do have some 

opposition to it security hey I want to reduce cost I'm going to turn off a certain amount of logging I'm going to turn off these products well now I've reduced my security I can think of performance efficiency would actually be an interesting one performance because there might be actually a certain amount of commonality between these to a certain extent um and performance and reliability there'd be some 

considerations um hey if I want to increase my reliability I might have the now spread over different regions well does that add some latency to me if I want to be performance efficiency and I start Auto scaling well hey if there's a spike in traffic Auto scaling takes a littleit bit of time does that impact my reliability in some way but all of the pillars all interact in some way and so that's what this does so if I go and 

look let's start off with reliability I can look at tradeoffs and it has the tradeoffs against the other four pillars so I can go and understand so I could jump to cost optimization well increas increased implementation redundancy or waste hey I need resiliency I need redundancy well that's going to cost me more money and I can go through and see what those considerations are I can see them against operational excellence 

performance efficiency and of course security was at the top I could go and look at Cost optimization what are the trade-offs here I can reduce resiliency so we can really just go through and this to me is fantastic because generally there's always going to be some balance and the tradeoffs help me see what those tradeoffs what those compromises really may be and let me 

decide okay where is the right balance in that what is most important to me and I I guess I'll come back and I'll talk about this more but this is something most customers do a very poor job of most customers for example will be up and running and then they have a certain initiative hey we want to reduce cost so they send out an email saying reduced cost well they don't balance that with 

hey but make sure your application still has the resiliency to meet its service level agreements it's recovery time recovery Point objectives make sure we are not compromising on the levels of security required for this criticality of workload and so if you just say reduce cost without balancing it without considering the tradeoffs then you end up with those workload owners they're being measured on reduced cost that's all they hear that's all they focus on 

and then you jeopardize the other things so if I was going to send out Communications as a company I would actually go and look at the tradeoffs and think okay if I message this what's the potential risk to the behavior of the organization and what could I maybe add to them messaging to make sure I don't introduce that sort of problem so I think that is so important and then I can think about 

recommendations and the recommendations are really patterns and these are not Azure specific a lot of these are just industry standards so if we go and take a quick look and look at recommendations these will look very very familiar this is nothing aure specific these are all just standard 

patterns that we use circuit breaker claim check compensating transactions um you'll probably see bulkhead right so these are just things that I can leverage to help me be successful in those so I would really walk through and understand these as part of my architecture so those are all focused on the 

pillars for any workload so I would go and look at these now the next thing it has is it has the concept of particular workloads now this won't apply to every workload because these workloads are based on specific classifications 

and then if you do fall in one of those specific classifications well then it has guidance so I could think of Mission critical uh Telco grade and it's going to give some other things that I would consider if I'm architecting an application a workload that falls within those so we can go and see so now I'm out of the pillar section and now I'm looking at the work load section and 

then it's got these additional sets of guidance if my workload falls into one of these so hey Mission critical well then there's a whole set of additional design methodology design principles patterns that can help me design a mission critical workload and so once again all of this is really technology agnostic none of this is azure specific so and then and only 

then really the next point is service guides so this would be hey I've gone through all these principles I have decided which particular Technologies I want to use and then the service guides are focused on Azure specific um sets of guidance so it would once 

again it breaks it down by the pillar and it's going to give me checklists for that particular service and it's also then going to give me particular recommendations so it's been completely agnostic up until this point I've not talked about Azure there's nothing in there but it's at the end when I've done all of these things only now do we 

actually go and hey what do I actually do for this service so we're not in Pillars we've done the workloads and now we can look at the service guides so here I could go and pick okay yeah well I'm going to use AKs okay so what are some key things around each pillar that apply to Azure kuat service so from reliability perspective where there's a checklist okay so I want to use availability zones 

that makes a lot of sense make sure I've got enough IP space okay container insights to get alerting my architectures separating out workloads into a user node pool us AKs uptime SLA so I pick the right AKs cluster skew and then you have particular AKs recommendations and then it goes into W for security what should I do what would I do for cost 

optimization so it gives you additional detail for every single one of those so you can really see how it's progressing at a very logical way to get you the information you need and someone explain this to me if you put this in terms of for example a a vehicle so you could think of it as well the pillars would be things like the power train the electrical system the 

fuel system the interior the safety considerations I could think of the workloads as a motorcycle a emergency service vehicle and then service guides could be well it's a specific Azure shocks Azure battery that's how I can think about how these play together in the sum solution so hope this makes sense of what it 

is but the next question is generally going to be well okay great there seems a lot there how like how do I actually start using this thing so what's the how the guidance would be okay I'm starting out you're going to start with the pillars I'm going to go through the pillars at 

the core level I'm defining my workload I want to understand for that workload what are the specific considerations against each of those pillars I would then say once I've gone through that exercise potentially does my particular workload fit within one of the classifications that exists in the workload setion is it Mission critical is it Telco grade is it 

Oracle if it does then I would feed in and read through the workload specific pieces of guidance to enhance those considerations I've done and then for each of the Azure Services I'm using I would then go and look at the service guides for additional help in making sure I'm then getting more 

detailed guidance for all of the things I need to do the next question becomes okay well when when do I do these things and it's not a a one-time thing obviously when I'm doing the architect I'm going to do it at the architecture 

phase that's just very very logical but this is not a I do it once and then I leave it I really want to think about the idea of continuous Improvement if you think of your applications life cycle well I could pick key points maybe it's when I actually have some update to the 

workload that would be a good time to hey I'm making an enhancement I'm making a change let's re-evaluate have things changed from guidance are there new features that could improve some aspect of what I'm doing or maybe it's just on some time interval I want to go and re-evaluate what I'm doing because every time we change an application we're going to go through a design process you'll have 

decisions use the W then and again I would really stress I'm not going to write it on the board but if I was going to do some Broad company initiative I would go and look at the W particularly the tradeoff sections and be like hey I'm about to communicate this um should I maybe add in some hey make sure you also consider XYZ to make sure I I don't break what I'm actually intending to do and 

compromise some other element now you might think well okay that's the how and the when I guess the next logical thing would really be The Who and I I think this is anyone uh obviously The Architects obviously The Architects the people responsible for architecting that work clod they're going to use this but it 

might be a central team in your organization where I have a central Cloud governance team a cloud architecture team and maybe they do a review and they add questions because maybe just realistically I got thousands of app teams I'm not going to be able to get them to go through this I just can't I'm not I know the limitations of the teams they're not going to do the great job so maybe I bring this into a central architect team who go through the review and they help validate this it's for anyone who wants to 

improve the workload so yes it's the architex but honestly it could be anyone else it it's any people that are involved and want to help improve now one of the challenging things quite honestly that there is a huge amount to that and so how do I know how I'm doing against the well architected framework how do I know if I'm getting better how do I know if I'm 

missing things and so one of the great things we can leverage we use our our sparkly pen here is we do have the idea of Assessments and that assessment is going to give me a score so how am I doing and it's also going to give me a report and that report will have very 

actionable guidance things specifically I can do now I can run this at any time if it's an existing app Brownfield I can run it if it's a new app hey so I'll run it so I'll run it for kind of that idea of the first time and we can see this so if we actually jump over so I can go to the assessments and I can start an assessment now when I 

start the assessment I can actually link it to a subscription because one of the things it can do is it ties in very closely with Azure advisor Azure advisor remember gives great information about all these various areas so I could actually go and import all the Azure advisor recommendations to help populate some of this data so we're constantly enhancing the Azure advisor as well which has recommendation around these pillar 

areas but I can just start I can pick is it some specific type of workload I'm just going to say it's a core and then I can pick which pillars I want to evaluate now ideally you do all of them but maybe you're responsible for one aspect of it maybe you're just trying to focus on one area of the design whatever that is you go through and you'll notice it adds basically question areas that will then 

guide me through how I'm thinking about this I can add notes but I would go and fill this out that's really the key point of all of this let's go back so if I go back to my architector well architected framework so at the end you would get a score and you would get particular guidance from that the next thing you can think about is okay I've gone through that it's going to give me guidance of things I 

can go and focus on it's now been six months or whatever it is I've made some changes how am I doing so the really nice thing I can do here is I can add to my existing report a new Milestone so I don't have to do a brand new report I have to delete it I go into my existing one add a milestone give it some name and what that's going to enable me to do is kind of track my 

progress ideally my score goes up and my list of recommendations and things I have to do in the report goes down so I'm making progress towards a a better and better architected a well architected workload and so here I would just go into it so okay it's been six months I can go and look one I've completed and here it's going to give me the 

option of adding a new Milestone and that will prepopulate it with all my previous answers I can give it a milestone name hey six month a date completed review with this enhancement whatever that is and I would just start it again but it will be prepopulated with the answers I already gave and I can export this as well so I can export so then make it easier to go and track that and do whatever I need to 

do and so that's the whole point the assessment helps measure how I'm doing what I'm doing against where I might need to focus on if I'm not really sure but that is the well architectured framework it's structured on a per workload basis to help me architect it in the best possible way understanding what are the core pillars that that I want to think about for my application design principles 

that I leverage as part of the architecture then I can go and use the checklist to check okay have I thought about these particular things are there tradeoffs that I need to consider particular recommendations to achieve certain things do I fit into a certain classification if there are there might be additional sets of guidance hey I've done my architecture I have the particular Azure Services what some of the checklist and recommend on a per service level and then once I've done that I can 

help measure my progress using the assessments hey I can do an initial assessment then I can create a new Milestone at key points in the life cycle of that workflow to really track my progress and again don't think of it as only I use it by the architecture team other people can benefit and if I am someone from that larger organization about to do some big communication about an initiative I would especially go and 

look at those tradeoffs and make sure I'm not communicating saying that I don't mean to communicate that's going to jeopardize some other area and so I want to call out to make sure that doesn't happen so that's the WAFF as always I hope this was useful until next video take care
