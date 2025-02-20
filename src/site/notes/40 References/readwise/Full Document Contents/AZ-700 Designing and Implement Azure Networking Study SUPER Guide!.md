---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/az-700-designing-and-implement-azure-networking-study-super-guide/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/nVZYDhB_M64/maxresdefault.jpg)

hey everyone in this video I want to provide how to study for and a study cram for the new A700 the designing and implementing Azure networking Solutions exam and certification I took the beta of the exam this week to get an idea of what was involved and really I spent the last seven days just preparing for this video it's probably the most amount of work I've ever put into one single video um I hope it turns out useful as always if 

this is useful a like subscribe comment and share is appreciated and hit that Bell icon to get notified of new content now when I think about preparing for this I definitely do want to get some Hands-On and the good thing is for the networking for the most part is not really expensive resources networks are free there are some elements I might want to spin up to see them and experiment then I could delete them pretty quickly to start off head over to the A700 page 

so this page will give me the instructions well how do I actually go ahead and schedule the exam it has the skills measured you want to be able to look at this skills outline and basically be a to put a tick next to every single one of these to say yes I understand those Concepts I feel pretty good I can answer questions around them now it is a pretty broad exam I mean there's a lot of content covered in here so I don't have to be a 

super deep dive expert in any one area I just need to really understand how do these things fit together and what is their function in an overall solution now the other thing that's really good here is they do now have they didn't have this when I took the exam but I did kind of quickly run through it just to see what was in it they now have a free learning path and again that's going to cover most of the content now what they've done in this learning path is they've essentially 

taken the Microsoft documentation and cut and pasted it into this learning path so instead of you having to go and search for the Microsoft docs for the right content that's what the learning path really is there's a few questions s clarify your learning but for the most part it's the Microsoft documentation which I think is a pretty good thing the documentation is good now for the content I've created in the past I've created a special A700 playlist once I finished in this video 

I'll put this at the top of that so you can actually go and see that and what I've done is over the years I've created a whole bunch of content around all the different areas so I have videos around the networking and then all of the different topics that are basically in the exam I've already got videos about them I'm not going to keep referencing these throughout this session you can just go and check out this playlist you can go and look at those YouTube only allows me to add I think five kind of of 

cards in the top Corner that link to particular videos so I'll Target some of the primary ones but obviously I can't link to all of them I've got too many videos but go and make sure you check out the playlist it's in the description this video will be part of it and review that content so look at the Microsoft learn material watch this study cram and then ideally go through the various videos I have no advertising on my channel I make no money from this this is me trying to help out so you're not going to get interrupted or bombarded with other stuff now in terms of the 

actual exam it was 2 hours I had 59 questions there were a couple of case studies at the start remember the case study is hey here's the scenario multiple Pages maybe where we are today business requirements technical requirements and then those same artifacts are used to answer a number of questions I think I had one case study that was four questions one case study that was seven questions so that makes up a chunk of that total 59 questions 

questions then the rest of them some of the questions where it has a certain kind of scenario and then it's a does this solution meet the requirement and it will have exactly the same thing three or four times it just changes how they would solve it and you can't go back so it's asking you hey we would do this does this solve it and then once you've selected that and move on I can't go back because the next answer maybe would give you a hint and change your previous answer and then there's just a whole bunch of regular questions hey 

what would I use um which steps would be required put these steps in the right sequence it's those types of questions so that's the exam 2 hours 59 questions I had plenty of time I think I did it in sub hour obviously in the beta you don't get your result yet but it really wasn't that bad in terms of the content there was nothing super deep that I thought was ridiculous it it it kind of was logical um for the most part okay so have that cup of coffee or 

whatever your beverage is and let's actually get down and start thinking about the actual review of all the content now I'm going to go pretty quick I have to I'm covering a huge number of things so the first part I want to kind of dive into just the basics and when I think about the basics obviously we're going to start out with a virtual Network so we have this concept of this virtual Network and I can have multiple virtual 

networks I'm not bound to just one or anything like that and a key point a virtual network is it exists within a certain subscription and a certain region I.E if I have multiple subscriptions one virtual Network cannot 

span that if I'm deploying to East us and West us I would need a virtual Network in each of those so a virtual Network exists within a specific region within a specific subscription it cannot span regions it cannot span subscriptions so that's really kind of a a key point now it is a regional construct I.E exists in the region if I'm in a region of supports availability zones those are distinct data centers with independent calling power 

Communications in your subscription typically you would see three availability zones my virtual Network spans all of them so even though there might be like three availability zones my virtual network is not pinned to a certain availability Zone it is still a regional resource and then what happens with the virtual network is I put resources into it virtual machines AKs environments app service is many other types of resource 

that we will actually explore now my virtual network is a layer three construct essentially it understands IP it's not Layer Two there is no concept of VLS in an Azure virtual Network to maybe segment traffic and there are other constructs I use for kind of micro segmentation so because this IP most of the time we're really dealing with kind of of 

TCP and UDP and there's icmp I can do Echo requests within there as well I cannot do broadcast I cannot do multicast I cannot cannot do GRE encapsulation this is all software defined networking Azure is using those things itself so I'm really thinking about hey layer 3 IP TCP UDP and what I'm going to have is this virtual network is is really defined as 

one or more private IP blocks now I'm saying private IP I.E the RFC 1918 the 10 dot uh 1726 192 168 those IP ranges but they don't have to be if I have some public IP block I can bring those to Azure but they are still going to be considered private IPS I.E they will not be accessible from the internet there so 

when I think about what is the virtual Network I'm going to add one or more so I can have multiple blocks I'm going to have ipv4 cider ranges remember cider range is that kind of 10. 1.0.0 16 I have other videos on IP Basics if you're not sure what kind of CER ranges is and again I can use the RFC 1918 um and others I don't I'm notri red 

to those so I'm going to add one or more ipv4 now optionally but I don't have to I can add zero or more IP V6 it is always dual stack I cannot do only IPv6 but I can optionally add IPv6 if I actually want to add it to there now if I add IPv6 to the virtual Network at least one subnet has to have an ipv range as well but they don't all 

have to have it which brings me on to So within the virtual Network just like a real Network I divide it into subnets so I can absolutely think about well within this I'll create multiple subnets and essentially what happens is those subnets are a segment of the IP space so I might have kind of subnet one subnet 2 and I can give them names 

don't have to be called subnet one and two I can give them proper names and so these subnets are they have a portion of ipv4 side range this has an ipv4 side range and again optionally if I gave the virtual Network an IPv6 they can optionally have an IPv6 which will always be sl64 so because of the way some equipment works with IPv6 and because of the how huge the address space is is um 

I'll always have a slat 64 if it's IPv6 for the regular subnets I can pick the subnet size and once again notice subnets are spanning the availability zones as well subnets are not pinned to a particular availability Zone they are Regional as well so it's another important point to realize these IP ranges of the subnets have to come from the IP range of the virtual Network they cannot overlap and 

when I'm picking my IP ranges even with other virtual networks with my on premises networks I don't want them to overlap if they overlap well for normal kind of communications it won't work I won't be able to connect those networks together unless I do some kind of network address translation which is generally pretty cumbersome so I need unique side arranges for each of these kind of constructs and we can see this if I jump over to the port portal kind of super 

quickly if I look at my virtual networks for example I have a whole bunch of different virtual networks but you'll see the address space I have here but notice I can add additional ones see yes I have this address space when I created it I did a slash6 but I could add additional ranges now if I wanted to I could add IPv6 address rang to that 

and then I have subnets which are a portion of that space and notice I'm doing some sl24 some sl28 the smallest is /29 you can kind of see that right here now notice that /29 gives me three usable IP addresses and you might say well that's kind of strange um a29 should actually give me more IP addresses than three and that's that's empty now the reason for that is just 

ordinarily with TCP if we think about Let's Pretend This is a sl24 so it's very easy on the host side it's 0 through 255 well always we always lose kind of the do0 and the 255 because the0 is kind of the network address we generally don't give that to anything and the 255 is kind of that 

network broadcast so we can't use that either but then what happens is azure takes the first usable address as kind of this default gateway and then it uses the next two for DNS purposes so you can see I always lose five IP addresses from whatever 

range I create which means the smallest is a slash 29 which equals 3 usable so that's kind of the point on that so there're the basics around kind of that virtual Network and again if I have IPv6 on the virtual Network I have to have at least one subnet and then I resources into these subnets whether 

it's a VM or AKs or app services or firewalls or NVA doesn't matter what it is there's some resource which will VI a Nick and the Azure resource manager network interface is a resource as well it will get linked to a certain subnet and it will get its address through DHCP so the Azure fabric provides that DHCP service it's always going to use that except in some very fiddly which 

you don't really need to know if I have multiple IPS on a single configuration I might have to do some static config but it's going to get that IP now these are all private remember these are all kind of private IP addresses those IP addresses as Dynamic normally I.E hey I need an IP address well here it is if I deprovision that resource I I stop paying for it well the next time I start that VM up or whatever that is I'm might get a different IP 

address I can also say hey I want it to be static so that's kind of like a DHCP reservation so when I restart my resource I would still get the same IP address even though I was deallocated and that's done on kind of the per resource level see if I was to quickly look at like a virtual machine I look at its network configuration I can see it has a network interface card and I can see on that network interface we have IP configurations and with in there I've 

got this ip config and this IP config we can see is static assignment and that's kind of the key point and I've given it the particular IP address I want it to always get so if I had resources in Azure that always need the same IP address maybe it's a SQL server or a domain controller I can absolutely make that happen so that's kind of the the fundamentals when I think about okay just the virtual Network so make sure 

you don't have overlapping IP ranges you can add ranges I can resize things if they're empty so I can resize but I have to empty it first so ideally get your planning done the right way so that's all private IPS okay well that's great then we can think about kind of public IPS I cannot bring my own 

IPS to AIA if I own a block of public IPS I can't use them as public IPS in AIA AIA has its own public IPS that are Regional so I can think about hey I have kind of a certain region in Asia could be like East us or east Us 2 or west us whatever when I create a public IP it exists in that region I can't move it to another region I have to create a new public IP Now by default it's kind of an interesting Point resources in 

azzure can get to the internet I don't have to do anything special I can do an outbound connection and I can get the state for the response back to me I don't have to do anything special the exact mechanism varies depending on hey does a resource have its own public IP is it behind a low balance that has a public IP depends on the config but fundamentally they can all get outbound to the internet and get the response back but what about if I want to offer services to the internet I 

actually maybe want to make a web server available so I think again okay well remember I have that virtual Network and remember that virtual network has that private IP space and then within there I have a certain subnet and we'll just say I have some kind of resource could be a VM with a Nick attached really doesn't matter so that has a private 

IP that private IP is from the IP range of the subnet it is in it can do outbound can't receive so what I have to do is I have to create a public IP this is a resource in aure now there's actually two SKS for a public IP so I can think about well there's a basic skew 

and then from the basic we can also build on there is a standard skew so have two different types now that basic skew you get a certain amount free uh this can be dynamic or static I again if I kind of stop using it and then start using it again I might get a different public IP it is open by default 

all it's just going to let everything kind of come in there is no availability Zone support what that means is if I was kind of having certain resources I can't make that resilient against maybe a data center failure or make it resilient across different zones or pin it to a certain Zone it has no concept of that then we have standard standard is static only it is locked down 

down by default and we'll see we talk about something called network security groups later on so here I would use an NSG to allow things here I would have to use an NSG to actually lock that thing down and it has a support and what you'll find is there are a lot of services that require a standard skew public IP and if I have certain types of resource like low balancer we'll talk about later on the 

skews have to match so if I have a basic low balancer I have to use a basic public IP I use a standard load balancer I have to use a standard public IP so they kind of go hand inand so we have these two different SKS available to us and then what I essentially do is I I have to use that public IP now yes technically I could link that public IP to a particular resource that then 

becomes kind of this instance level so it's just the the resource doesn't really know it has a public IP or it's converted by the fabric but it links directly into that resource but most of the time if we're doing this kind of public IP it's because I'm offering a service to something so I want it to be resilient I want it scalable so generally this is not kind of the thing we want to do instead we would have some kind of low balancing solution now 

depending on what we're doing here this might be a layer four I like TCP UDP might be layer seven like HTTP https http2 we'll talk about that and this low balance would link to a whole bunch of different resources and I would link the public IP as the front end configuration of that and that's is generally kind of what we'll typically do with public IPS public I used by a whole bunch of things VPN gateways um firewall solution they they're massively 

used now the other thing I can do is a public IP is a a single IP address what about if I know I'm going to need multiple public IPS and really I want them to be contiguous one after the other so the other thing I can actually create is a public IP prefix so public IP prefix is that contiguous block that I kind of get in advance and then I 

can use them from that block some resources I can just assign the prefix too like a that Gateway I can give it a prefix and it will kind of go through the IPS and use them as I need to so this is a contiguous block of public IPS so that's how I can think about those so two different skews that's how I can then obviously offer things from the 

internet to actually get to certain services and likewise if I have a public IP I might then use it for the outbound as well there were services like Azure firewall and that Gateway that would actually use it to snap traffic on the outbound and we're going to talk about those later on so don't worry about that just yet okay so that's all well and good um we have this virtual Network we have public IP and I said the virtual network was bound 

within a region and a certain subscription so what about if I have multiple regions what about if I have multiple subscriptions what about just if hey I need different virtual networks for different regions well I can peer them so what we can actually do now is well I can do peering so I can absolutely imagine the idea that okay I 

have vet one and vnet one is a certain IP address bace let's say this is 10.0.0 sl16 so that's kind of the important those first two blocks and then let's say we have two other virtual networks for the time being I've got a v-net over here call this v-net 2 and I have another one over 

here the net three and remember if I want to connect them they have to be unique IP ranges so we'll say this one is 10.1 that's 16 so it's those bits that are important and we'll say 10.2 so those are the important parts so because they're unique ranges um yes I can connect those and what we might say is well let's say 

this is kind of region one I that could be West us and this one happens to be in region two maybe that's East us doesn't has really no bearing so what I can do from here is I can peer them together so on the Azure backbone Say Hey I want a connection between these v-ets now before this we'd have to do like a 

sight to sight VPN then we were restricted to the speed of the VPN Gateway VMS couldn't operate their native capability we lost stuff with that with puring I don't have any of those problems it's using the native Azure backbone so because these are in the same region this is just vet puring because these are in different regions well this is 

global v-net puring but it doesn't really change very much it's going to kind of work the same way now I cannot peer across clouds and what I mean by that is there's more than one Azure Cloud there's the commercial Cloud that most of us are using then there are sovereign clouds China us gov Germany I cannot PE vets from example commercial to China or to us gov I can only peer within the same cloud now a peer is actually created in each 

direction there's a bit of permissioning I need to actually peer to a v-net there's permissions I need to establish the v-net outbound my deep dive video on that I've actually got one on kind of peering overview of v-net peering I go into exactly what those permissions are so I'm not going to cover that here but there are permissions I need to do if it's different subscriptions I have to kind of authorize that Pier to actually complete but essentially it's made up of 

um two peering connections once I do those peerings there are some kind of special tags in Virtual networks one of them is called virtual Network and I might think virtual network is the IP space of my virtual Network it really isn't virtual network is the known IP space so when I PE virtual Network now includes the networks I have connected to so if I've peered to these two v-ets virtual 

Network the tag which we're going to talk about now includes 10.16 and 10.26 as well that's important when we think about certain rules because if I'm using virtual Network it now applies to these as well so important point so IP space cannot overlap cannot peer if the IP space 

overlaps another important Point Let's imagine this is a hub and these are spokes so this spoke has peered to the hub this spoke has peered to the hub can they talk to each other no it is not transitive those not talk if I want them 

to be able to talk I would have to add a pi between these two I.E I have to create a mesh Network you alternative to that is root via the Hub what I mean is there were certain appliances I could put in this Hub right here that would then enable it to be the next hop and could 

route on their behalf so there are ways to do that for example um let's think about this a second I could have something like in here I could have Azure firewall or just some kind of network virtual Appliance and then I could you tell these hey use this Appliance to actually get to each each other so the way I would do that is I 

could use something called userdefined routing and say hey if you want to get over to there go that way and I would do the same to get back again so there there are ways to do that now also consider within this Hub I probably have connectivity I probably have kind of a Gateway subnet 

and I have some Gateway devices this could be um sight to site VPN it could be express route and we're going to talk about what exactly those are so these are kind of these maybe it's active passive if it's VPN or it could be active active Express R is always active active but I have these devices that have kind of 

connectivity to my kind of on premises networks out there now what if I want these spokes to be able to use that connectivity via this Hub and I can absolutely turn that on so there's a configuration I can actually do so I remember I said there's kind of two peerings two kind of directions on this so what I'm going to do is on this side of the pier there's flag I can do that actually lets me say 

hey allow Gateway Transit IE let them use my gateways and then on this side I'm going to say use remote Gateway so that's on this side of the connection so allow Gateway Transit on the Hub side let them use my Gateway send the bgp routes through use the 

remote Gateway hey on these connections let's actually use that and if we go and look super quick if I was to go and just look at a virtual Network so I'll look at my Hub so on my Hub if I looked at the peerings so this is from me to let's say East USS what I would make sure is use this virt networks that would be the setting I would need to make sure I have 

turned on so that in the poers Shell would be allow Gateway Transit and then on the peering of the spoke if I looked at its connection what I would need to make do and I can't do that because I've not got it turned on on the other connection I would do use remote virtual networks Gateway so that would then let those spokes actually go get the routes 

advertised via bgp of that connection and then use it so the spokes would now be able to get to these whatever that on Prem is on the other side of that VPN or that express route because they're going to use the gateways of that I can only use one Pier remote Gateway I could not have another Hub and use that remote Gateway as well it's a one only one of them can be selected to actually do that and if I have Gateway in my local v-net I can't 

use a remote Gateway I'm only ever going to use my own now there was actually another setting and it was allow forwarded traffic and that's kind of important if I do have some kind of network virtual Appliance in the hub and I want traffic to be able to flow via it because this has to basically accept traffic from here via this connection so there was that option on the peering as well and it was this setting here allow 

forwarded traffic from remote virtual Network so that would say hey I'm going to let that Hub Network send me traffic from someone else I.E it can act as that kind of f so I mentioned something about kind of some special routing if I actually wanted to do this I said this userdefined UDR thing and if you think about it by default a virtual network has a set of routes there are routes it knows just 

because of its IP space the rest of the RFC address space is kind of black hold it knows everything else to go out to the internet and I can see those if I go and look at a network interface card so if I just go and pick any kind of virtual machine in my environment and if I go and look at its networking and look at its network interface card so I'm selecting its Nick we have this effective routes 

option down here at the bottom and these two are actually both super useful effective routes to see the routes it knows and effective security rules when I start doing things like nsgs network security groups to see what rules are impacting it but if I look at the effective routes we'll see a whole bunch of different routes now there are some that just built in and then there are other things that will get added when I have things like a VPN connection or an express route well there will be other routes 

added for the address space on the other end of that connection so we can see here well there's a default route for my local v-net kind of see that for there's a default route 00000000 goes to the internet and then there's a whole bunch of Ones Will black hole the rest of kind of the RFC space there's different rules about that over here then there are some other 

special ones around sort of the Azure itself and that's actually an important point I said you can kind of use pretty much any set of IP addresses you want there are actually a set of Ip ranges you cannot use so I said sure use RFC you can use other address spaces but you cannot use these ones I said you can't use multicast or broadcast but it also blocks off uh some other IP addresses because they're just not allowed as part 

of azure so are other ranges you can't use but I have these default routes and again other things will get added into them like I've added peering well now it knows there are these other IP spaces over here that are used for peering there are other ones about certain service endpoints and I'll talk more about that later on there are private endpoints points added in I would see things for virtual appliances 

I would see things for gateways there's this whole bunch of default RS that kind of just exist within the virtual Network that get populated to the network interface cards themselves but I may want to change that I may want to add additional routing and for good cause maybe I've got like Network virtual appliances I want to change the type of traffic I'm actually doing and sending over these things so I can create route tables so I 

can think about okay I can create this rout table and we think of this as this userdefined routing and a route table is really just a set of routes the routes I'm going to Define now in this case I might say look I want to define a route how to get to that spoke over there now that particular NVA it would have a certain 

IP address um maybe it actually has an IP address of 10.0 dot I don't know um 1.4 that's the IP address of that Azure fiable over there so I want to say look to get to this address space over here so to get to 10.2 my next hop is a virtual Appliance 

and its IP address is 10.0.1 do4 this is remember a software defined networking my next hop doesn't have to be an IP address on my local subnet it can be an IP address actually on a different subnet even a different network it's not like traditional networking how we used to think of it bits of copper wire and actual physical connections so I create this route table if I had Z 0/0 I'm setting a default route I send everything to this virtual 

Appliance and I could do that and then what I do is within here I have subnets so I have a certain subnet I link the route table oh let's change that color I link it the route table has to be in the same region as the virtual Network when I create those things things and then I would do exactly the same on the other side I would have a route table here as 

well this one would say hey to get to 10. 1.0.0 I would go to that same virtual Appliance and I would link it to the subnets I wanted to go here so what I've essentially done now is through that I've configured hey you can now get to each other via that virtual Appliance I've added my own userdefined 

routing to change the default Behavior so I'm linking it I want to make sure it's symmetrical I want to make sure it flows in the same direction especially this is kind of a stateful firewall or virtual Appliance it needs to see the traffic going in both directions and again remember I could look at those effective routes as I was showing here to actually see what is happening so if I kind of looked at this and actually if we look at a different virtual 

machine so if I look at my West Central and it has its networking and it has the network interface and look at its effective routes this actually is using my Azure firewall so what I did for this one is I added a default route I want everything to go via a particular Azure Fireball I have defined so here you can see this user defined route here so I'm overriding the regular 

0000 I'm sending it to my virtual Appliance so that means hey everything go via this particular one now I also have another VM in the v-net I wanted to talk to it also has a route table but it only sends traffic through that's destined for the subnet of that West Central us so it's using the same Appliance in that same Hub virtual 

Network and I go into detail on this in my Azure traffic uh my Azure firewall video so not going to Deep dive here but the point is I Define these various routes I want and then take effect on the various devices that I actually have in the environment and there's a bit of work it has to do is go and work out the effective RS but it's going through and all I'm going to see is a slash6 userdefined rout that's actually applying on this network interface card 

when this wakes up um it would show that to me but honestly I don't want to sit here waiting for this if I go and look at the route tables themselves the whole point is this was the one it had and we can see here this is what you would have seen 10.36 goes to that same virtual Appliance I can just add multiple routes so I give it a name the prefix and then what is the type of hop is it a virtual 

Appliance is it to the internet is it overriding the default virtual networks is it a virtual Network Gateway like sites like VPN or express route so I can add multiple routes and then I link it to one or more subnets but again I can only link it to v-ets in the same region as the route table so I'm doing things across multiple regions I'll need a route table for each of those so that's kind of a key point in how those things 

really all fit together so that's one element when I think about hey I'm connecting things together I also talked as well about hey if I want to get to the internet well there's this public IP if I have one if the low balance one behind has a public IP I'll use it but I may want more control now there are mechanisms I can do gure firewall um through the lad balancer but it's 

actually a dedicated service so there actually something so that was kind of the peering there actually something called natat Gateway so with Nat Gateway we'll use a color I haven't used that so that Gateway as the name suggests this is focused just on the outbound knat connectivity so what I do is I create this knack way and what I do is I have public 

IPS or prefixes that I attach to this that is basically focusing and listening on these have to be standard skew remember I talked before about different skews some Services require a certain one has to be standard skew and then what I'm doing is from that n Gateway once again I link it so I go and Link it to 

particular subnets again in the same region as the that Gateway instance so what happens is now they outbound traffic to the internet will go via the N Gateway and the that Gateway performs that snat Source Network address translation it's super super efficient um normally we might struggle with pull exhaustion the whole point of snap is I have this private IP range they're not 

usable on the internet so these devices essentially use a port per unique session TCP or UDP when if I have tons of people connecting there's only so many ports per IP address so I can run out so by giving it a prefix or multiple public IPS it lets it scale even better I think it's 16 IPS but you should check that number that's kind of in the top of my head I'm thinking 16 but could be wrong but and that's in total so if I had a prefix of eight that 

counts out of those 16 that I can do it's standard skew and it's also ipv4 only I cannot do IPv6 on this each public IP is 64,000 concurrent connections so times that by 16 that's that's a lot of connections through one that Gateway it can be pinned to a certain zone so it can be zonal or Regional but it cannot be Zone 

redundant so those are the two options I can pin it to a zone or it can just be deployed to the region it works with things like standard low balancer it actually does not work with basic resources so if I try and pin it to a subnet with basic IP public IPS or public low balances it will not work it'll actually complain it won't let me link it but then any traffic I'm doing out B will go via this knat Gateway now it is intelligent if I had services that had 

maybe a low balancer and it had requests coming in so we think about this picture over here if things were coming in to low balancer the responses would still be sent out via the low balancer but net new outbound connections to the internet would go via the nap Gateway so it is intelligent it's not going to break flows by coming from different IP addresses it will work with the other things you actually have okay 

so next public IPS public IP outbound all good things and again that Gateway is super simple to actually deploy the next big thing we typically have is uh DNS by default the virtual machines that I have or any resources in a v-net are using Azure DNS so if I go back again DNS if I have that virtual 

Network as part of the virtual network configuration there's actually the ability to Define my DNS Now by default it will use Azure DNS or I can use custom I I have a choice for that now the default Azure DNS will provide me name resolution for the resources in the same virtual network but if I'm going 

across virtual networks I won't get any kind of consistent name resolution I can also Define custom DNS at a per Nick level if I need to overwrite it just for a couple of virtual machines now the way this really works behind the scenes is hey we have these resources that get defined and the way its DNS works is there's a special IP address so there's this 

168 63129 129 oh terrible writing 1296 that is always the IP address for azure's DNS so this is the Azure DNS end point that's where I go for anything that is is azure DNS so that would be if it's going off and then quering s on the 

internet it would be saying if it's going internally now what if I want a custom name I want different names internally but I want them to work across different zones now I could have my own DNS servers I could have active directory DNS servers I could have some custom Linux thing but I want it to just be a native part of the platform so what I can actually do is I can create Azure private d s zones so I create this 

Azure private DNS zone now that is a certain name that is whatever I'm going to have name.om or whatever I want it's it's a certain name for that zone now within this this Azure private DNS I SP a whole range of of different types of Records so I can have things like a records C Name Records um text 

records pointer records MX records um SRV s SOA there's a whole bunch of different types of Records I can have within that and I can manually add those or I can actually have kind of this Auto creation of those now the way that 

auto actually works is I have my virtual Network I actually have multiple virtual networks but I link the virtual Network to Azure private DNS zones and there's two different modes for those links each virtual Network can link to one only one aure private DNS Zone for 

registration only one now I might have other Azure private DNS zones name two bob.com I can also link to those for resolution I.E I can go and look up records I can link to up to a th000 for resolution purposes so I can 

link to one Azure private DNS for the resources that get created um VMS AKs worker noes virtual machine scale set SQL managed uh instance it will register those names into that zone so get vm1 name.com vm2 name.com and obviously I would also use that for resolution as well I want to be able to look things up as well and then if I have other zones name two name three I can link to those 

but only for resolution my resources will not create records and this makes sense I'm not going to create vm1 into eight different zones so I can link to one for registration a thousand for actual resolution purposes so now I could look up hey www.am to.com or whatever that might be now those zones themselves so each of these zones now firstly these are global 

resources I can use them across different regions and for each Zone it supports 100 vets that are doing registration to it and it supports a th000 vets for resolution which again makes sense I might have five different v-ets I want them all to 

maybe register the same name.com and they can go and look across so a single zone can have multiple virtual networks um registering records into it and up to a th resolving from it but a particular v-net can only register records into one but it can use a th000 for actual resolution so hopefully that makes sense and this when I use Azure DNS it's using that for the actual lookups so that's 

how I'm actually resolving it's using that 16863 1296 this will only work in Azure so one of the things you'll sometimes see is if I'm on Prem and I want to use Azure private DNS I can't this HP address will not work I would have to have some kind of DNS f as a VM that it talks to its private IP and then it goes and talks that VM and Azure goes and talks to this now I can also have that's private DNS I 

can also have Azure public DNS zones now obviously for a public DNS Zone these are all going to be manually added I'm not Auto registering anything to these this is really host records or IPv6 host records and aliases once again it's going to be a certain 

name whatever that might be name. and I have to be orative fortive probably spell that wrong I have to be authorative for that zone to be able to make that on the public um it has to actually point to Azure DNS for that to actually work but then that end point will resolve to those as well so I can use those from my res sources internally so if I want something to be accessible from the public internet I create an Azure public 

DNS Zone but I have to prove I own that name there are records you create like a text record that proves I own that and they'll go and check howy you did create that text record that means you have access to create records in it so okay we we'll go and move it to here obviously private DNS zones I can use whatever names I want it doesn't care because it's only usable from within that virtual Network itself so that's how I can use kind of the DNS things so these are all really right now 

all about just stuff in Azure itself what about hybrid connectivity hey I want to get to other things so there's many different types of hybrid connectivity technically from on Prem I could connect to things via an internet connection I could expose it to the internet but that's generally pretty terrible I don't want to expose things to the internet so instead remember those private IP addresses of our 

resources I want to be a to get to those private IP addresses which means connecting my virtual Network to my data center or maybe some virtual Network on another cloud and the way we think about starting with this is kind of a VPN a virtual private Network so straight away I'm going to think once again we was going to start with this virtual Network then everything we do I'm going to start with a virtual 

Network have to drink them thirsty this is going to be a super long session probably see me drink quite a few times so I have this virtual private Network now remember always I don't want to overlap the IP ranges this vet has a certain IP range and the first thing I have to do is I create a Gateway subnet now I get to name it 

um and what actually happens is it's going to create this for me it's going to use kind of an IP range now the minimum is a slash 29 the recommended is a sl27 and the reason the 27 is recommended and sorry it's not you get to name it you you can pick the IP range it's going to use is if I only use sight site VPN /29 is fine if I only use express route 

Gateway /29 is fine if I choose later on to coexist and I want VPN and express R I need the slash 27 and it I remember I can't resize there's things in it already so unless you're really really short of Ip ranges do that one do the sl27 but if you saw kind maybe a question it's like hey you've got a /29 um V and you're going to add express route it's not going to work you're going to have to delete the Gateway make 

it at sl27 add the Gateway back then add the express rout so that's going to kind of be a key thing now there's actually two types of VPN Gateway so what's happening is my Gateway is going to deploy into here so into that v-net I'm going to kind of get these gateways and there's two types now there's actually a huge number of SKS massive number of different SKS that really relate to kind 

of the generation there's a V1 and the V2 there's even a basic and it's really about the speed how fast they're going to go but we can really break this down into the basic skew which is really kind of this Legacy again I'm going to do the frowny face um I I really don't want to be using that and then we kind of have everything else these kind of gen one and gen two and 

they're the ones we we kind of want to use and the reason is this is super restricted so this is something we call a policy based you'll also hear this called Static and the way this basically works is it can only have one tunnel I a connection to One Network um it cannot coexist with express 

route it cannot do point to sight VPN and the way these work is essentially it encrypts the traffic first then sends it to the tunnel which has kind of an arle of which IP address is it allows so we doing that encryption first I can only have one tunnel whereas all of the others are route 

based I.E Dynamic and what that means I can have n number of tunnels because what it's basically doing is it sends it directs the traffic to a tunnel and then encrypts so I can have different kind of encryption depending on the tunnel I'm sending to so it gives me that flexibility of multiple tunnels I can have both express route coexist I can also have point to site 

VPN if I want it um so it's just kind of this richer option it supports things like I can do bgp optionally and I can do active active configurations as well if I want to so it deploys these multiple gateways they can actually both be active and both establish tunnels to give me kind of that better resiliency if there's actually a problem now there are massive 

number of SKS if we jump over quickly so here we can see hey this gen one we have basic this one so it doesn't support bgp it's not Zone redundant it says Max 10 but that's only Max 10 if it's running in a um Dynamic mode so it does support that as well but it's actually the only one that supports static then there's this whole bunch of VPN gateway 1 2 3 AZ versions 

then there's Gen 2 versions and you can see things like the number of tunnels vary point to sight sight to sight if it's bgp zones the speed um varies kind of greatly you can kind of see the different speeds now this is the total speed it supports across all of the different tunnels what we find is actual for an individual tunnel it's kind of this 1 gbit per 

second because it goes through a single core so no matter yes I can have multiple these get bigger so I can support more tunnels but the actual a particular tunnel is still 1 gabit per second because it goes through a single core and that kind of maxes out a single core so I can think about okay so got different gateways actually if I go back to that document for a second it does kind of go through different requirements talks about the encryptions 

it can use feature sets so remember the basic skew can do route based and policy based remember that policy based is is kind of stressing one connection and then everything else they're only route based so it does kind of talk about those differences between them I cannot convert from a basic skew 

to one of the other SKS I basically have to delete the basic and then recreate it the others for the most part I can kind of convert between them so how how am I using these so I create the Gateway so I create as a resource the VPN Gateway resource that's kind of Step number one well then what happens is if you think about it I have my on premises and this is a certain IP space 

so I have some side arranged that represents the IP space on Prem let's say side of one and this is obviously an IP range up here let's say this is side of two and then I'm going to have Gateway devices so I have kind of a Gateway here maybe I have two so what I have to do is I then create um what is kind of called this local network Gateway so local network 

Gateway is created in AIA and it represents kind of the public so these each have a public IP now I might not have two I might just have one public IP 2 so I'd create it i' say okay well this is public ip1 and it's cider one now if it's bgp then there's other things I can do as part of that address 

config if I was going active active I'd create a second one of these for public ip2 and it would just be the same side of range so this defines my on Prem connectivity and then the next thing I have to do out of here is a VPN connection which is from the the gate I create a VPN connection which links to a certain local network 

Gateway up here I have a public IP now if I selected as part of the creation to make this active active I'll have two public IPS so this would be public IPS if it's active active and then I really control what that configuration actually looks like like because there are a number of high availability configurations I might for example say 

um hey I'm going to connect from both of these to the Gateway I might do that so I've got resiliency if one of these fails or I might just have one but I'm active active here so I connect one of them pretend that isn't there to both so maybe I do that or maybe I'm active active on both 

sides so I have that so different configurations I can perform but but I have that capability it's all documented uh the learning material goes into detail on all of these but essentially remember you are going by these Gateway devices each tunnel is really 1 gbit per second per tunnel so yes these might support 10 gbits per second as a 

Gateway but an individual tunnel is still kind of limited to that number I wouldn't use this to connect different v-ets together remember because I'm going limited by that tunnel speed when I'm linking virtual networks together use the peering this is a much better Superior speed option for that okay so that's I'm connecting my on Prem 

to Azure and it's actually now that they're connected Azure is an extension on my onpro network now from here I can go and get to the private IPS of any resource here and if I've do the networking correctly kind of peered networks as well it's just an extension of the network likewise things here all the peered networks from using the remote Gateway allow Gateway Transit can get to things on premises what about if I just have some individual 

machine contractors remote workers they want to be a to get in well I can also and it's really going by these public IPS I can enable point to site VPN as well only remember on the route based SKS but I can go and turn that on so that's giving me the ability for individual machines to actually go and connect to that virtual Network so it's going to create a tunnel that there's actually three different types available to me there's kind of this 

open VPN now this is establishing an outbound kind of TLS so it's using 443 that should work really from anywhere and this really works for kind of all clients this could be iOS Android Windows Mac Linux that's generally kind of the preferred thing you're going to use there's also there's 

sstp once again that's kind of the TLs 443 but that's Windows only and then the third one is this Ike V2 and that's kind of Mac one of the great things about this so all of these can use things like Sur based or authentication um they can integrate with ad so if I had my regular kind of active 

directory so i' got my regular a they can integrate but the way they integrate is I have to deploy radius so I have to have a radius server that talks to my ad so then these can kind of go and query us the radius if I have Azure ad so I'll think about hey um this is for the open vdn openvpn only so I have kind of azure 

ad this can use that so I can actually one of the nice things and then things like conditional access um MFA can all come into play now the only thing to use the open vdm with Azure ad you have to add an Enterprise app application to my Azure ad as part of the setup you'll go to a special URL and I have to consent and 

say yes when I do that consent it will add in an Enterprise app so if you see hey hey you want to add open VPN what do I have to do is adding an Enterprise app to azid to actually make that work hey I want to hook into active directory hey I need a radius server um if your IP address space changes of what you're connecting to for the open VPN and the sstp sorry for the openvpn and Ike it 

would just detect it but I I will have to reconnect for the sstp I have to redownload the configuration to actually make it take effective to learn about those new routes so that's where I can actually think but now I've got this kind of complete connection remember a key thing though those connections right here they are all over the 

Internet so it's all going over the Internet latency I don't know might be taking a different path different noisy neighbors people conflicting with me so that will potentially vary pretty massively over time and I may not like that now they've encrypted I'm not super concerned about the security side of it but maybe I want a more dedicated kind of private connection just for me me so how do I I think about that so that's when we get to express route so I'm going to keep 

drinking so express route is all about a private connection say's scroll over plenty of space good all right so let's talk about express route so I think of Microsoft Microsoft has this 

massive Global one it spans the world it's one of the biggest networks you can actually see it so if I go and look there's a way you can go and explore so this is kind of a picture of the Azure Global infrastructure and you can see all these little kind of connections all of these Microsoft has all this connectivity all these little lines that's 

connectivity all throughout the world so there this massive backbone Network and those blue circles are Azure regions that I kind of talked about so have all these different regions all throughout the world South Central day sport availability zones got all those things I can see kind of a basic map view as well so regions all throughout the world massive set of infrastructure now the way this actually works is there's this massive Microsoft 

backbone fantastic and I talked about regions so I can think okay well I'll draw this great big region I have a certain region so this is hey I got region one really doesn't matter and the way this works behind the scenes is there are these kind of regional Network gateways in each region that go and actually 

connect to that Microsoft backbone Network that's what actually gives it that connectivity now in addition to connecting and again there's many many other regions so there's like other regions region two three Etc lots of regions they all connect as well redundant connections but there's other kind of points of presence so there's also these kind of points of presence on the edge there's a certain pop and maybe I go and 

connect to some internet service provider could be an AT&T a Verizon whatever that is that's how we get to the internet and Internet is just a whole bunch of different connected networks and these kind of meet these carrier neutral facilities now in addition to those kind of points of presence that Microsoft backbone Network also expands into these peering points so we actually have these carrier 

neutral facilities so we kind of call these meat Mees and peering points same thing and what happens here is that Microsoft n network once again expands into a whole array of routers I'm just join two there's this whole Microsoft Enterprise Edge actually that facility so what we can do is customers 

I can think about hey I kind of got my customer Network so I'll kind of draw that down here so this is my customer now that customer might be at a Colo in which case they're in kind of the same building I'm drawing it as hey they have their kind of customer Edge routers and those customer Edge routers Connect into this kind of meet me facility could be an NLS so it's kind of more it's a cloud but 

it's this layer 3 Ms tagged but it's still basically going to end up as that ISP is essentially going to have a set of routers so they have kind of this provider Edge customer facing to connect to the customer and then what will actually happen here is that that provider has an MS Enterprise Edge 

facing so those connections get connected through and then it does a cross connect to Azure so I'm going to do this as a magical color just to kind of show magic then we get this at this point what have you done you've connected the customer Network to that Microsoft backbone Network so that's kind of the key point and again I've drawn it as this direct Layer Two connection doesn't have to be there's many different ways this can actually work there's different models could be 

an NLS that it can even be um express route direct so express route direct essentially the customer has their own routers in here they're not using a provider and the customer Maps their routers directly into the Microsoft Enterprise Edge so if I'm a really big customer I can get these 10 or 100 GB per second direct Port connections and then I create circuits on top of those now these meet me locations there's a whole bunch of them so if I jump over I can kind of see 

halock for Amsterdam Amsterdam 2 there's different addresses and there's different service providers that operate out of these so lots of different locations different providers shows me kind of the different speeds they're supporting You' also see this local Azure region for some of them not all of them some of them it doesn't apply to and I'm going to explain what that means in a second but basically for all of the 

models I'm using a certain provider Microsoft does not provide Last Mile Microsoft do not provide the connection from your location to its Enterprise Edge you're using someone to do that either that's a service provider or you have got your routers in this facility and you're using Express right direct so you can do that it's always a pair it's always redundant it's always active active so there's always two connections between you and 

that's kind of an important point because I buy a circuit even if I'm doing direct I buy a port I create circuits on it so I create kind of this Express rout circuit and that Express out circuit is a certain speed so I buy a 10 let's say 100 megabit per second circuit with actually 100 megabit per second circuits so in if everything's happy and working I'll get double the through p and it's full duplex so it's 100 in each Direction on each connection 

so I actually get a much bigger throughput that I might otherwise think I have now that's great I've connected my network to Microsoft backbone Network fantastic what can I do absolutely nothing um because nothing's been advertised I've just connected networks together but there's no routes being advertised to say hey you can get to this v-net or these Microsoft Services because there's actually two 

different types of service I can use two types of peering once I have this connectivity there's something called private peering and Microsoft peering so private peering is hey I have don't do that color let's get that back out I have a certain virtual Network remember that virtual network is a certain kind of Ip space within there 

and I want to connect that virtual Network to my on premises IP space so that would be private peering Microsoft peing would be hey there's other types of service in AIA there's maybe storage accounts there's even things like Microsoft 365 there's seal there's all these different things I want to use those but those don't live in a v-net but I want to be able to get those advertised as well so let's start with private 

peering so if I think about private peering I have my virtual Network so the first thing I have remember I need that Gateway so I have my Gateway subnet and it's going to deploy express route gateways so these are different from the VPN type they can coexist express route will always take preference I need that sl27 if I want 

VPN and express route you can actually do a VPN over express route if I want it encrypted end to end I can do that because this is a private connection there's no encryption on here so if I actually want it encrypted I could do IP sec I could do a VPN over it I do have those options but this is not an encrypted connection but I get some number of gateways we don't really see all care about the exact number there are different SKS so if I look at the express re 

gateways I can see hey standard skew high performance Ultra performance and then there's a maximum number of circuit connections so depending on the skew of the Gateway I can depend to multiple express route circuits so remember a circuit is really tied to a certain meet me I might connect to different ones maybe for redundancy for various purposes I can actually connect to more than one circuit from a particular um Gateway skew so there are those different ones 

available there's different speeds so we can see the maximum megabytes per second of the different gateways while it can actually support talks about the Gateway subnet as well so we have these documentation but some of them are AZ understanding um some of them are not so I have that choice if it's understands azs it can be zonal I pinned to particular a or it can be Zone redundant multiple v-ets can connect to 

the same circuit so I create a circuit I create authorizations that let gateways connect to the Circuit so if I had a circuit I could have this v-net connected to it and that v-net and that v-net they would actually then be able to talk to each other so if I had another virtual Network connecting to the same express route circuit doing private peering they could talk to each other but the traffic would flow bya the meet me so even if there was another v-net sitting here so this is kind of 

vet 2 and it was connected to the same circuit the traffic would do this so if this meet me was 50 mil away from the data center was going to add significant latency so I wouldn't do that I wouldn't connect them using that I would use peing to kind of remember that key kind of point but once I had this gate way essentially what I'm doing is I establish private peering so I'm 

actually going to go and say hey from here for all of these connections that is private peering and what happens is the address space of kind of this this side arranged down here gets advertised up to the v-net so will have in its routing table effective routes hey to get to side of two go the next hop and that's actually 

an interesting thing about the next hop inbound traffic flows via the Gateway that is true but outbound does not outbound goes to the MS it's pretty more detailed than you need to know for the exam but outbound does not go VI the Gateway the next hop will be the M inbound goes by the gateways so that's kind of a a key point for that 

um there are different things I can actually do there's something called fast path so this inbound connection if I turn on fast path then the inbound does not go by the Gateway fast path will go directly to the resources does some magic there are things it doesn't support So if I do fast path for example if I jump over here it can't have userdefined routes on 

the Gateway cuz it doesn't go VI the Gateway I can't do connect to things that appeared I can't talk to basic low balancers and I can't talk to private link so that's just kind of an important point to understand that hey the way the traffic flows is inbound is normally by the gateways but if I turn on fast path then it does not then there's some limitations I still need gateways I it have to do that bgp route propagation and it actually has to be the highest skew it's like the the ultra or the ERG 

Gateway 3 a so I still need the Gateway and I still need the top tier but outbound never goes by the Gateway doesn't need to it just goes straight to the m there are different speeds uh about express route so when I when I buy a circuit I mean there are certain limits I'm going to talk about premium in a second but it tells about number of circuits I can have so the number of virtual networks that can connect to a circuit for the standard skew is 

basically always 10 so 10 different v-ets can connect to the same skew regardless of kind of the circuit size we can see over here if I add premium well I can add more v-ets to the same circuit as kind of it gets faster this bigger connection so there are some differences that kind of creep in between standard and premium and again I'm talk about those uh in a second what 

standard and premium differ by so was Private peering so private peering hey I'm connecting IP space to IP space of a virtual Network then what we also have is kind of this idea of Microsoft peering so Microsoft peing are those other services that don't exist in a v-net now ordinarily these Services advertise these public IP addresses out 

to the internet and I connect via those public IPS but maybe I want to actually connect to them via this private connection now when I turn on I can have both Microsoft peering and private peering on the same circuit my provider May charge me separately that's down to the provider so I turn off Microsoft peering and I get nothing nothing happens because by default it's not advertising 

any routes by a bgp to say hey take this path instead of your path via the Internet so what I have to actually create is a route filter and then I kind of link that to the Microsoft peering and that says well hey via bgp now we're going to advertise these services to come in Via this connection 

so if I jump over super quick if I look at my over here so if I look at my route filters so i' create a r filter and what it's going to do if I manage the rules I select the service communities I exchange SharePoint online azure D all the different regions and then particular services within a particular region so I can say 

hey I just want these routes advertised through my Microsoft peering so only these things that I have selected would go via my express route connection so that's really kind of a key point about that that's really all there is to it now I I do have to do a few different things for all of these puring connect s obviously if you notice there the Microsoft Edge side and the provider Edge side want need IP addresses if it's 

private IP sorry private peering I can give it private IPS um 230s or 1/29 customer always gets the first usable IP the MSE uses the other one I can use public IPS kind of a waste if it's Microsoft peering again I need 230s or a 29 but they have to be public IPS that I have to actually use for that connectivity also if Microsoft peing 

because it's all public IP space I have to knat the traffic so when I tell it an IP space I'm advertising over Microsoft peering it's only going to be my gat servers here which are separate IPS that's going to knat the traffic from that private side of topace over that connection so I can actually get to it but I talked about kind of premium express route premium before so what what does that mean so 

ordinarily we have Express R standard and I can actually think standard covers everything in a certain geopolitical boundary because I'm connecting to the Microsoft backbone network but I can only connect to things in the same geopolitical boundary now these are documented if I look at the express rout regions it tells me at the top the 

geopolitical region so North America for example are all of these regions so if I have a regular express route circuit to a meet me in North America I can connect to all of these regions but only those regions if I turn on premium so if I go premium let's pick a different color we do gold there we go if I do 

premium it is now global I can connect to any region on the Microsoft backbone Network so that's really the big difference between them now there are some other differences um with the premium skew I can advertise more routs I think it's 10 000 RS instead of 4,000 routs I can if I get Microsoft buy in connect to Microsoft 365 Services over that as well 

so there are some differences between the SKS let's look at the pricing details quickly this might spell it out so notice you can add on the premium kind of price added onto the cost of the standard price if I want that trying to see if it tells me what premium is so Express about documentation tells me what premium is um where's it 

gone but it's basically that I don't know if I'm going to find it quickly but that that's the key Point behind premium is let's see if the fact has it premium here we go yeah so increased route limits so it's 4,000 10,000 remember that increased number of v-ets can connect based on the speed connecting to Microsoft 365 services and Global connectivity so those are the things I said so thank goodness I didn't 

get that wrong um but that that's what I would actually kind of use that for now when I'm looking at the pricing an interesting thing is in Azure you don't pay for Ingress so data coming into aure I never pay for it but I pay for egress it's going out to the internet out to another a region I pay for egress from AIA an express route is no different there's actually two different 

SKS there actually three so there's a a meted plan for express route where I pay for the egress and that's normally the right one for most customers so if I look at the metered plan you can see the meter plan let's just say 100 megabits per second okay so it's 80 why is it P you must detect my accent some new Advanced thing there's $110 per month but I then don't have any outbound data included so I pay for the outbound 

data and it's telling me based on the zones so different regions like North America is Zone one um that tells me what zone 2 3 4 is later on there's also an unmated plan but for the unmeer plan notice the price is significantly higher so it's $575 instead of the 110 so I'm paying more but I don't pay 

for the egress typically you wouldn't do the unmetered unless you were constantly using I think it's 60% or more of the constant egress speed it just doesn't work out um optimal for you then is also noticed here in this unmetered something called a local circuit now notice the local is significantly cheaper than the 

standard so what is local now remember when I talked about the different locations if I jump back to this document by location when we looked at this document it actually had this concept of a local azure for some of them not all of them noce Atlanta doesn't have one but if I scroll 

down for example um like San Antonio is local to South Central us I that meet me is super close to a certain region so what the local skew lets me do is if I use the local skew I can only connect to the aure region that is local to the meet me I can't connect to the others but I don't pay for egress so kind of the big Point 

here is that local skew if I just need to do a huge amount of agress but it my region is local to the meet me per that chart it's a lot cheaper so if I have that requirement hey use the local skew so the local skew kind of a key Point kind of draw this out so local only 

region so that's kind of an important thing so there is the local skew but I can only use the region local to meet me per that chart that's kind of a key Point um a few other little things so I talked before about kind of bgp I talked about bgp is used I have this redundant pair this active active if there is a failure it uses bgp to detect that and do the fail over well that bgp could be 

fairly slight could take many minutes to fail over so there actually something I can do B FD so this is basically I think it's almost like a subc so what BFD is actually going to do is this bir directional 4D detection it's going to enable much faster link fail over so I can turn that on typically subc there's a failure it's 

going to detect that another thing you might want to do is remember this is not encrypted I talked about this is not an encrypted connection it's a private connection but it's not encrypted now remember I talked about instead of just buying circuits if I'm like big into this I might buy kind of express route direct so express route Direct there is no service provider at that 

meet me it essentially becomes so this is the meet me still you can think about well I still have that Microsoft Enterprise Edge routers but now it's really the customer Edge we have these customer Edge routers and then I have that pair of connections between them so this is only for Express R direct it's just me I'm owning the ports so if I want to encrypt it there is actually something I can 

do called MACC so what Mac SEC is not endtoend encryption but it's going to encrypt between the two routers the customer router and the Microsoft Enterprise Edge routers so basically the air of the meet me location so it's traveling over that cuz obvious there cables going that traffic would be encrypted between the two routers again not end to end but in the air of that meet me I can use 

maxc to do that encryption and as mentioned already I could do a sight sight VPN over express route so if I have private peering if you think about I got the routers used for express route I could also have kind of the VPN gateways behind this and Above This and so over the private peering I could establish a sight to site VPN as well so that that is actually possible remember you can 

have multiple circuits and you probably would so if I had multiple locations geographically distributed I might have let's say Dallas and London let's say I had that for example well if I had that kind of Dallas London idea so let's say hey this was a a global region and let's say hey I had another data center here and I had another meet me location here not going to draw different connections well this would make sense 

cuz think latency I wouldn't want to from London talk to my London Azure region by going over my private connection up here back over the Atlantic twice that would be terrible so I'll add kind of a local meet me but now imagine a scenario well hey this is let's say this is Dallas this is London I would actually like these to 

talk via my Express Round connections because got this Microsoft backbone Network well I can actually do that so what we have is there's actually a feature called express route Global reach and I I can turn that on and what that's going to do is essentially over that Microsoft backbone 

Network it's going to connect my offices to each other so that's what express route Global reach does it gives me that connection to actually go and leverage that capability use that existing now maybe it's a backup connection it's not my primary one I'm using it as a backup or maybe that that here how I connect them together so that's hybrid connectivity sight site VPN Point site VPN express 

route with Express rout I don't only have to do private peering I can kind of that Microsoft peering as well there's a lot of management involved in those things if I have express route and I have VPN maybe I'm doing all these different peerings I have all these different things that maybe I have to manage there's actually quite a lot of work I'm doing there so there is another service that kind of takes a lot of that work away from me 

and that service is azure virtual one so we hear a lot about SD W today and hey this new world of just using the internet connection so instead of me having to worry about these peerings and these vpns and these Express routes well if I think about a certain 

region I can just create an instance of azure virtual one now what it's doing behind the scenes is it does create a managed v-net but I don't have really any direct access to that managed v-net it's just there but what I can then do is if I have kind of other v-ets I have I essentially can add them it's 

going to PE them so I I can kind of do this there were two skews so I actually I should kind of stress that point there's a basic so if I have the basic skew I can do those connections but it only supports sight to sight VPN so if I had a location it supports connecting 

it but that's just me getting to the v-net and I could have multiple locations and it would kind of connect those things together then there's also do another color going to run out colors today I think for sure um we'll pick that color no it's too similar that's a bad idea we'll pick gold again there's also a standard skew so in addition to kind of the sight to sight VPN it also supports express 

route and it supports point to site and it kind of supports this vnet transitive and it supports kind of multihub routing because I may have another region so then that other region I have another V1 over here it will now let me kind of connect them and it has connections and everything would route together these v-ets can now talk to each 

other I could add another location with an express route they can talk they can talk they can talk I can have my kind of point to site it's kind of now enabling this full connectivity between it now if I don't want this kind of any to any configuration I can add custom route tables to restrict the flow so if I 

don't want this any to any I can absolutely use a custom R table for v-ets so I can link it to these say hey I actually don't want you to talk so I can restrict that if I want to so that's kind of a cool thing I can do there's even third party NV um Network virtual appliances I can actually install into the manag v-net maybe I've got like a barracuda and then my branch office is maybe connecting via Barracuda gateways 

locally into this Barracuda NVA that I've got in that managed v-net so I can absolutely do that as well okay so lots of different things I'm trying to get my bearings a little bit so that was all about kind of connectivity hybrid connectivity making all those things work now what I want to actually talk about is I kind of alluded to a load 

balancer long long ago many many hours ago I talked about this load balancer there's actually different low balancer Solutions available to us and it depends on my requirement again I've got a whole video about picking the right one because if I think about hey I have these public IP spaces public IP addresses or maybe internal I want to make Services highly available so how do I actually do that there are many many different 

options when I think about low balances in AIA a little dot here I want to draw it high away from everything else because if I think about the different types of services we might have well there's different requirements think of load balancers what do we have well I might 

have services at a global level and I have services at a regional level I within a certain region and then quite separate from that I have some services that operate at layer seven so things like HTTP https HTP 2 and I things that operate at layer four I TCP UDP so depending on what I'm doing and 

what I need I'm going to have different solutions that I actually want to use for this watch the video there's there's a lot of detail around this now a key Point here is I'll often combine Solutions So within a certain region I'm going to use one of these then if I'm deployed to multiple regions I'll probably have Global Services that point to the regionally highly resilient 

Services let's start with the bottom layer for regional so what is my solution here so my solution here is the Azure load balancer this is actually kind of a very simple service when you think about what it's doing it's layer four so with layer four what that really means is I'm focusing on these kind of five tupal and 

you see these five TS a lot you think about kind of the source IP and Port you think about the destination IP and port and the protocol that's really what we understand for this so I have this load balancer so kind of draw this big symbol and the whole point of what this 

has is there's actually front ends now this front end is obviously an IP address now there's two types of low balancer I can either be internal or external I cannot mix them I can have multiple front end configurations but I cannot mix them so I'm either everything is an internal front end or everything is an external front end I can't mix them so I have a front end IP address 

and then what's happening is that traffic is coming into the load balancer and I have a number of rules and those rules are really deciding how do I distribute the traffic now for this there's actually a number of different SKS and that that really dictates what I can do for some of these kind of traffics and what I can support on the other end so there's two 

SKS there is a basic skew so the basic skew everything has to be in one availability set so I can have up to 300 in the back ends but they're all from the same availability set or the same VM scale set this is free but it means there is no SLA so there's no service level agreement for free there is no availability 

Zone support uh and also it's open by default which is very similar to the the free public IP or the basic public IP and remember I have to use these together so if it is exterior if it's basic low balancer I have use a basic public IP or there's 

standard so I could use that with a standard um public IP so this there's a there's a cost for this but it means I get an SLA I can actually support a thousand back end in the same v-net doesn't have to be the same VM scale set the same availability set does doesn't care so it's a thousand instances about that it supports azs so it be Zone redundant or zonal I 

pined to a particular one and it's locked down by default so I have to open things up and also it can point to either network interface cards or IP addresses some resources don't have a Nick if I think about pods in AKs they don't have their own Nick so the idea of being out to use an IP address can actually be very powerful I can give me have more support support 

containers but they must be in the same v-net as the load balancer so I do get those different skews so we have this front end IP address we have the low balancer itself and then we have backend pulls which are made up of resources again from either the same virtual Network or the same availability set if it's basic Etc and it kind of distributes um to those via the rules 

there were also Health probes going on so the health probe I specify as part of this to say how do I know if a particular member of the pool is healthy if it's not healthy I don't want to send the traffic to it so that's really an important thing I want to have now there are different rules available as part of the load balancer so a key one is a load balancing rule so this is kind of this hash based distribution so for these kind of source 

IP port destination IP port protocol creates a hash to then send it on so based on these protocol PS it sends it to a particular backend member I can pick a certain stickiness so by default is kind of the five tupal but I can also specify a three or two Tuple so three tup takes out the pull so as long as the source IP and the destination IP and the protocol is the same you always go to the same backend member 2 two pool is 

just source and destination IP so even the protocol can change it will go to the same backend member so I can kind of pick that stickiness I actually want there's also um natat rules so a n rule is hey I don't want to distribute the traffic over multiple members I want it to go to a particular VM and Port so hey it comes in to this IP and this port or we send it maybe it's for an RDP connection although want to be careful 

about RDP to the internet if it's standard I can also do outbound and this is really about outbound net rules and actually con figuring this is snap basically so I can figure how I do outbound if it's that kind of exterior IP one of the configurations I can do is these rules this low balancing rule there's a there's a finite number 

of rules I can actually have so something I can do on standard is I can do something called ha PS so if I turn on ha PS that standard only I don't create individual rules for ports anymore it just will evenly distribute all of the flows this would be super useful if these were like Network virtual appliances and I'm covering a whole bunch of ports and protocols I don't want to do individual rules so if I turn 

on ha ports it will just distribute the flows over the backend Port members I don't have to now do individual rules and I can't do individual rules so ha ports just does all flows I can also turn on something called floating IP and what basically that means is I send 

the front end IP to the back end ordinarily what the back ends pull c as the destination is themselves it gets Rewritten by the virtual switch to say even though it was sent to this front end IP they don't see the front end IP they think they are the target sometimes I don't want to do that so what I can do is if I turn on floating IP what they see as the destination is the um front end IP address I have to do a bit of 

Wizardry inside the VMS maybe add a loot back adapter for that IP so it makes sense to it but I can actually turn that on I can configure that if I want to so that's really the low balancer so the low balancer is really all about hey layer four I can create rules I guess we can see one of these super super quick see if I jump over to my low balancer and and I should actually stress think 

when I talk about low balancers there is a help me choose it can answer you questions and there's actually a service comparison this is super useful and it tells you hey look for the lad balancer it's TCP UDP it can do private load balancing it's not Global it's using that round Robbin based on the hash and it's Azure re sources only so it's a really useful thing if I look at my low balances basically what you're just going to add in is hey I can have my 

back end pulls the members I'm sending to and then I can have rules hey lot TCP on this IP coming in going to this port send it so Hey look it's coming in ipv4 going to this particular front end IP on the low balancer it's it's TCP it's coming in to P 80 I want to send it to P 80 on these backend VMS and this is 

the health prob I'm going to use to see if they're healthy I can pick additional session persistence so this comes down to the two pools so hey um normally it's five tle with none but I could also say hey do do two twole client IP or three client IP and protocol I can turn on that floating IP that I talked about so it would see in the front end IP address and there's also some outbound snap rules as well there and also can 

also see inbound that to map particular port and IP to a particular VM and I can do outbound rules as well so that's ler four okay what about Regional So within a region layer seven well that is going to be app Gateway so Gateway is another service we 

have again it's regional HTTP htps http2 it is a layer 7 device now because it's layer 7 it understands a whole bunch of layer seven things I can do things like URL based routing uh I can do redirection redirect HTTP to https redirect this site to another site I can do SSL offload it can actually go and do that decryption and then send it unencrypted to the back end or it could even reencrypt it and send it on um I 

can rewrite the entire URL I can rewrite the request I can do cookie based Affinity there's a whole bunch of cool things I can do with this there's also a web application firewall so what I can optionally turn on is the first part is this web application firewall component to protect me from these standard types of open web application security project core rule set CRS to give me that 

initial protection and then what happens is this app Gateway actually deploys into my virtual Network so it deploys into a v-net and what I'm actually going to have here is very similar initially is I'm going to have these front end IPS so I have a front end IP now the front end IP it always has a public it's listening 

on optionally I can also have a private I cannot do private only uh what I can do is lock down the public so it's really not being used for anything but I can't not have it now once I have the front end IP what I actually create are listeners so a listener is kind of listening on a particular IP and kind of a particular 

Port is how that's working now at this point I can also tie into other things like I could do things like SSL offload at this point through ports I can hook into various certificates um as part of that configuration but for the listener there's two types so there's basic so basic is basically basically 

everything goes to this particular rule anything that it's listening on in this port no matter what the fqdn is going to go to that rule there's also something called multisite and what I can do with a multi site is I can have multiple listeners on the same port on the same IP which normally wouldn't work so what this is actually doing this is actually looking at kind of the fully qualified domain 

name I the domain that's coming in and I can do World cards I can do various characters in there to send that to a different rule so the same port same IP I can actually use different rules so hey this is going to starav tech.com go to this rule to go to this back end set oh if it's star do I don't know sacom whatever net go to these other ones so I 

I can use these different things so this uses rules and and kind of just like the other thing there's a basic rule where with the basic rule it just kind of says hey um you just go over here send this to to everything I kind of have so it's Port go over here I can also do a path-based 

routing so if path based hey if it's slash blog go to this set because what I'm going to have on the other end of this are various backend pools again so if it's path based One path could go there one path could go somewhere else I can also do various types of rewrite 

within here so I can rewrite the URL I can rewrite the request I can rewrite the header there's a whole bunch of different things I can do to actually change what's within there in terms of the services in this backend poll it's actually a lot more flexible so so the services in that backend pole can yes they can be things in aure but they could also be things on 

premises it actually doesn't really care as long as there's connectivity to them sites like VPN or express route these could be kind of on Prem as well via kind of that sight to site VPN express route um other things as well it really wouldn't matter to it um as part of that rule as well there's a whole bunch of kind of HTTP settings that I can 

configure and that's things like um Affinity so hey those cookie based the session Affinity if I'm going to do maybe re-encryption I can configure all of those things on there so I have those different options again there are different SKS available for this um I think there's Auto scale in the standard skew there's Zone redundancy 

zonal but again it exists in a single region these are all regional resources and again the Azure site it's kind of cool if I go and look at the service comparison shows me okay well app Gateway okay yeah HTTP https http2 private round robin azzure non on Azure Cloud on Prem and all these kind of nice features like session Affinity host and path based routing TLS offload okay WF 

nsgs NSG cuz it lives in the virtual Network so I can use that and that optional web application firewall so it does a whole bunch of different things it has the same Health probes so we can go and check is the backend pool member actually there and I can use it so it gives me those capabilities okay so now let's kind of move on to the next kind of level of service so those were Regional what about global so let's think layer 4 

first now what I would say is for layer 4 Global there is actually Global a a low balancer but this time it's in preview so it's not in the exam but what that Global does is it actually has an anycast address that can point to Regional azuro balances but again that's not going to be in the exam but there is a video in the playlist if you interested on that so solution we really have now for Global balancing that's not HTTP well that's going to be Azure 

traffic manager and it's really a pretty simple service because it's DNS that's that's how it's working behind the scenes so the way this is really going to work is I create a track traffic manager name so let's just say this is I don't know Sav web do and it's going to be 

traffic manager.net now that's resolvable across the kind of the whole Azure DNS service now I don't want to point people to that so on my domain servers I might create a www. saav tech which is a c name record and Alias that actually points to that now what traffic 

manager does is on the back end of this I can have a whole bunch of different resources I might have in these Azure regions over here um it can even support things that aren't in Azure so maybe it's some location over here and it has them as possible resolutions I can even use addresses fully qualified domain names as part of that and the way it's really going to work is hey I'm I'm kind of sitting here on my 

machine and I say hey www.s tech.com and I question that to my local DNS server who then goes off and does a whole bunch of recursive resolution so they resolve that for me so that goes up to traffic manager Now traffic manager has a whole bunch of different methods it can use to actually 

distribute the common load balancing one you're going to use is performance so what performance does based on the latency of my DNS server to the possible targets it will resolve to the one closest to me IE it would give me kind of that one the one that is closest to me now as the targets it can actually be these Azure end points so it could be 

Azure end points um it can also be external so that could be a fully qualified domain name an IP address or it can actually be nested so this could actually be kind of another traffic manager profile which is one of those things so performance is the most common hey redirect me to the one that's 

closest to me there are others so if we look at the documentation we can see there's priority have one as the primary service endpoint but go to others if it's not available because again we have health probing on this thing weighted send 50% to this end point 20% to another performance obviously the one send me to the closest one Geographic send me to the one based on different geographies so I have these different end points these end points 

are for North America these are for this country multivalue hey instead of returning one return all of the possible ipv4 IPv6 addresses then the client can pick which ones it wants to use or subnet hey map these IP ranges to Pacific end points and the documentation goes through kind of how all of those works there's these different things available that I can leverage key point though is DNS so I do 

as part of my configuration have to consider what the time to live with the record is so if one of these goes away if the time to deler the record is 5 minutes it's not going to go and recheck and get resolved to something different for 5 minutes so I always have to consider that for my layer seven solution it's Azure front 

door now aure front door is really focused around the idea that once again there's this massive Microsoft backbone Network and what I can think about having is remember we have all these different regions and most likely our kind of got my app Gateway in this region offering a service I've got another region with kind of my app 

Gateway offering it from here as well uh maybe there's even some on premises region that's offering the service over here and I talked about before also hanging off this network of a whole Bo bunch of points of presence different locations that Network expands to Microsoft Ed it for the content delivery Network work so what Azure front door does is essentially it adds an any 

cost IP which means that IP address is available at all of the different points of presence that is supported by here now additionally I can turn on web application firewall to kind of be in front of all of those to again give me that protection from the thing and then it has a number of possible backend targets as part of that Azure front door profile and now this is only again for 

HTTP htps https 2 is it's again that is that layer seven so now what happens is me as the user let's say I'm here I want to go to the service so I go to this anycast IP so I'm going to go to the one that is closest to me now so that's any cast but then what it does is something called split TCP because ordinally what happens is it would then redirect me to the backend 

service there's a whole bunch of things that happen I have to establish a TCP connection then I have to establish a TLS connection it does all this to the local point of presentence so it's much much faster in terms of that actual connection it can do things like SSL offload so at this point I can do SSL offload it's going to actually improve the overall 

performance and then I make a request hey I want this block of data at that point it will go and take the request and get the data it will go and do the request it will get the response for much bigger chunk of data I can do caching so then the next person we get a better performance and then it serves up portions of the data so aure front door is really going to improve the performance for multiple reasons yes it 

does some caching yes it's going to redirect me to the one closest that's available again it's doing the health probing to check it's there but all the TCP establishment the TLs establishment happens close to me not going to the back end then it gets big chunks of data and serves that up so I can really focus a whole bunch buch of different things if it's a back end if it has a public IP if it has a resolvable DNS name I can use it with this capability now what's coming out is kind 

of these V2 world of azure front door now if I actually look at this for a second now this is preview right now but they're basically going to add some additional features and what they're doing is they're really combining Azure front door with we application firewall and the Azure content delivery Network that CDN is kind of super useful for static for non-changing Content so they're merging all of these things in together and what's really happening is 

that premium skew you can see hey look private link support so I can now redirect to resources via a private endpoint that we're going to talk about has things like fre intelligence bot protection all of those kind of WFT capabilities so you can kind of go through here make sure you got a basic understanding of the Fe of it but the V2 really merging all these various things in together so up until this point we've 

really been focusing on making things available hybrid connectivity now let's think about the opposite side of this picture I don't want to make things available anymore I actually want to think about maybe locking things down so the whole idea of hey this great connectivity if you can talk to each other fantastic maybe I don't want to do that or I want that but now I need to actually control and start restricting things down now Azure 

security Center is a great starting point Azure security Center has based on Azure policy some default things it can actually leverage to advise on hey locking things down using these capes abilities hey I should have an actra firewall there are things I can do for protecting those public IPS there's a standard distributed denial of service that's just inherent but it's really designed for massive scale there's also a paid for version so there's a standard offering what the 

standard distributed denal of service protection does is I apply it to a v-net all of the public IPS associated with services in the v-net and now uses things like machine learning to actually tune to what is historically seen on that gives me more control reporting hey I'm going to start preventing these denal service taxt a lot earlier because I've learned what is common for this particular service so Distributing of service there's a standard offering gives me machine 

learning base protection more reporting more control but now I really want to think about really controlling things so I have my virtual Network so I have my v-net and remember the whole point of this is I might have local multiple subnets in that 

v-net so I've got kind of subnet one 2 3 and ordinarily everything can talk to everything I can talk to peered networks Express rout connected networks if I if I don't do anything else so I want to think about controlling that so the way we do that is we create something called a network security group and just like many other things we've seen we have 

both the idea of inbound and the idea of outbound and we create rules now these rules are really all based around that same kind of five Tuple idea we're very big on kind of maybe a cider range and IP range but there's also these things called service tags which I want to talk about a super important point though 

about network security groups this is not an edge device it's not a appliance sitting at the edge of my Subnet protecting traffic if I think about a virtual machine the virtual machine attaches to a network interface card it is here that the NSG is enforced and why that matters is it means it doesn't matter if I apply the 

NSG at the subnet which is how I normally am going to do it so what I'm going to do is I'm going to link this to a subnet it still applies to VMS in the same subnet it's just for management I apply it to the subnet but I can also link it there as well it's just that gets very hard to manage so we tend we' rather not do that most of the time we'll link it at the subnet so it's easier to manage but we can because it 

actually is applied in the virtual filtering platform of the switch that makes all of this actually happens so I link this into the Nick it's in force there ideally I link it into the subnet is these whole bunch of rules so it applies regardless of even if they're in the same subnet now it's created within a region so I have to apply it to a v-net in the same region and I create these rules now 

there are a number of them built in so if I jump over I'm getting a whole bunch of different tabs let's close some of these down so if I go and look at my network security groups there are certain rules built in so if I just go and look at really doesn't matter I can see the inbound rules now notice there are these three rules by default this is inbound to the VM where it has this linked and it's got this 

special name here called virtual Network so anything from the virtual Network to the virtual network is allowed on any port any protocol and remember what I said the virtual network is the known connected IP space so if I have a virtual Network trying to find a big picture of one and I've 

peered it to different networks and I've done sight to sight VPN or Andor Express ra and other things all of those connected things are virtual Network that's an important point it's a known connected IP space so that default rule that we see there is any of the connected IP space can all talk to each other completely unrestricted so that's kind of a default rule that's there inbound then it also always allows the 

Azure low balancers to talk to it so it can do Health probing everything else is denied so that's coming in outbound rules the stuff going out of the neck it says hey look again everything within the v-net is allowed everything out to the internet is allowed and this is stateful so the response will be allowed back as well everything else is denied 

so what the basic rules basically let you do is to say hey anything within the v-net in and out I can go out to the internet nothing else can come into me except the low balancer for probing purposes and then what I would do is I would add additional rules so The Source again can be IP addresses or this weird service tag thing I pick the port is coming from destination again could be IP 

addresses or can go to kind of this virtual Network it's an inbound rule if it was an outbound Rule The Source can be IP addresses or the virtual network but now the destination can be a service tag so I talked about the virtual network is a service tag already there's a massive number of them and think of a service tag as really just representing different Azure Services I talked before 

that really the Azure Services can't remember where it was on this board anymore I think it was when we talked about mic oft peering are really just a bunch of public IP addresses that it advertises out to the internet a huge number of public IP addresses or maybe in my rule I want to allow it access just to storage in South Central us there is a CSV file I could go and get but I don't want to have to have a load of IP addresses that update periodically in my network security 

group rule so a service tag is basically the IP ciders per service and often it's service- region so they've created these so in my rule I don't have to say this IP this IP this IP this IP for storage in South Central instead what I can very nicely do is hey yeah look there's service tags 

for look at all of the Azure Services storage there it is and I can use this only for outbound because storage doesn't establish connections into a virtual Network whereas something like service fabric well that does in and out so it tells me which direction that service tag is usable so now in my outbound security rule I could say hey I want to allow access to now it says 

internet everything that is not my virtual Network which is the known connected IP space I could say kind of the standard Global things so I could say okay all these Services I could say storage or I could say storage. just South Central us so I could pick of a particular one and just allow connectivity to that it knows it's custom service and I can here have a a 

certain Port I want to use if it was certain type of service within the storage account maybe SMB I would pick a certain one I can pick the protocols so I create the rules to basically specify the types of connectivity I want so yes I can use side side arranges because that would be super useful the side arrange if what I want to do maybe is say look subnet one is maybe my DMZ so I'm going to allow in from kind of the 

internet 443 but I would block that to all of my others and that would be the default anyway then maybe I'm going to allow these to talk and these to talk by doing the different side arranges in my rules of each of these subnets but I don't want this to be able to talk so I could control all of that just by creating these as the NSG rules and then I would link it to each of those different subnets so 

the the NSG is all about howy I create the rules realize I have to link it to the subnet for it take effect it processes the rules now the other thing I can do is on this Nick I can actually tag it so we have these things called application Security Group which is really just a tag that's all this thing is and then in my rules in addition to side and service I can put in a tag so if I look at the virtual 

machine what I can do is firstly I can create these application security groups which are nothing but tags so I've got one called quarantine SQL VM SQL VM web VM I have two because they are Regional I can only use the app Security Group in the same region that it is created then what I could do on a particular resource if I go and look at my virtual machines let's look at my uh domain 

controller and look at the networking over here if I look down here we have this application Security Group tab if I select it I can configure app security groups from the same region that's why there's only one web VM so I could add that tag to this network interface card for this virtual machine then it doesn't matter about the SAR ranges then in my network security 

groups instead of having to worry about what IP range it's in I could absolutely as part of my rule say for things like okay so for my inbound rule is that my self Central make sure so make sure it's the same region in here for example now I could add a rule instead of woring about the side out range I'll say hey look I want to allow my web 

VM to be able to talk to my SQL VMS and I would put in the right port for SQL was it 1433 not 100% sure um but I can specify that instead so now it doesn't matter where it exists it's just based on that tagging I'm actually doing on the Nick itself so application security groups are actually super super powerful then I can think well okay 

that's controlling things so that's fantastic I really want to make sure I'm doing that but now I might think about controlling connectivity because there other types of service imagine for example I had kind of a storage account so I had storage account one and maybe there's a storage count two remember these have their own kind of f walls as part of them as well maybe I want to restrict the storage account 

to only allow this v-net in but I can't do that because this is a private IP space it would be meaningless to that firewall so what I can actually do is I can create something called a service endpoint so what service endpoints let me do so I can add a service endpoint for 

storage in South Central us that is really two things firstly it now gives me a better route to all of the storage accounts that are in South Central us so there's there's a a preferred optimized route it also now makes subnet 3 in this v-net let vnnet one a known entity to 

firewalls that are in the storage account of South Central us so in this particular one I could actually now say hey yes I'm going to allow vet one subnet 3 that's allowed to pass through so now this can actually talk to that particular instance cuz I allowed it on its firewall so that's what service endpoints do so I can go in on a virtual Network I can select the services I want 

a service endpoint for gives me an optimized route and I'll see that in the effective route table and I showed you those earlier you might have noticed there was a whole bunch of IP addresses well those same service tags represent the IP addresses of the service it now has an optimized route it knows to use the service endpoint route and it's now a known entity I can enable it on the firewall itself to just let that through so that's making it 

known maybe though I don't want any public connectivity now that service endpoint is only usable from that subnet I can't go and access that from an express route a sight site VPN or anything else so the other thing I can do is say hey I have another let's say storage account five I can add something called a private 

endpoint a private endpoint is an IP address from the network it's going to get it from whatever the side of range is that represents that particular instance of that service in this case storage count five so now that there's no public connectivity to it I can get to it through this private endpoint now it's just an IP address so any network peered to this v-net can use that address any sites like VPN or 

express route can get to now this storage account through that private endpoint now there's also some special DNS required and I'll talk about that in a second but I do have to be able to resolve the name to this private IP instead of all the public ones it it's still going to spit out there they just won't be usable now that's if it's a standard built-in kind of pad service to Azure nearly all of them support private endpoints today what about if I had my 

own custom service so I have some kind of resource what I have to do I have to put them behind a standard internal low balancer and then I add the private link service in front of that and then this can have private end points that 

point to that and I can have multiple private end points to different things this is all flowing in kind of this direction this is getting me to a service it's getting me to the storage account to the SQL to these things that kind of distribute so if I wanted to add my own service via private endpoint I have to have a standard internal low balancer I have to add the private link service to that which does the Gat which means these could actually be in a v-net and they could have overlapping IP space 

this actually does the thatting and then I project a private endpoint into that particular subnet which again is kind of usable everywhere now the DNS has to work now by default it can work with an Azure private DNS Zone it will create it for me and Link it to the v-net but what we'll see is there's a whole bunch of new privat link dot domains so we'll see hey for let's see SQL instead of just being database. 

windows.net now it's privat link. database. windows.net and what happens is an alias is now created so the things in database. windows.net now actually resolved to the privat link. database. windows.net uh I can show you this so if if I open up a so I've got one of these if I look at my private link quickly I've actually got a couple but I created some private endpoints to 

storage account so I've got a blob private link resource a files private link resource Cloud endpoint Etc so what happens is ordinarily if I look at my storage accounts for a second if I can find storage which maybe I've removed from my menu so just type in storage I created one with private links so I've got this private link 

demo and what we can see is on this I have a whole bunch of those private end points I've added but what I'm looking for oh is this networking there's those fiable things I could add if I had the thing things but I've got my private endpoint connections and you can see I've added two and normally the name for this 

service if I actually go through if I look at my endpoints well my name would be this sa privat link. blob. core. windows.net I'm kind of looking here but if I actually open up terminal for a second and if I do an NS look up on that what we'll see is because there is 

a private link let's get rid of the HTTP part don't want that it now actually has an alias over here and that will actually resolve if I'm on a v-net that can resolve that DNS record to the private IP now this is just a public one soz I'm not on a Network that has that DNS but it would actually resolve to the private IP instead and then I could get to the service so that's what's kind of 

happening there's a whole set of special DNS happening behind the scenes as well that I actually need to manage app service also supports these um when I think about app service it's a little bit special just in terms of kind of the Zone it's going to use but once again you're going to see it go ahead and in the DNS we'll see hey look we have a c name for privat link. azurewebsites.net so we will get that 

over there but if we think about remember that the DNS is kind of a key thing because it has to be able to resolve that so if I'm very simple just in the v-net it will create an Azure private DNS Zone it will create the private link. blob. core. windows.net whatever that is and it will use it for resolution and I'm good if I'm trying to use it for on premises I either have to create a privat link. blob. windows.net 

and add in the IP never ever add for the non-private link your block access to all of the other services that are blob not a good thing or I could add kind of a DNS resolver I go into that in detail but DNS is super important I have to be able to resolve to the private link Alias to be able to get to the service now let's talk about app service for a moment so app service remember I create an aure app 

service plan and then that can have multiple apps inside it now each app can push a private endpoint so each individual app would have its own private endpoint but that's all about getting to the app what about if I want the app to get 

to things in the virtual Network say there three options for that the maybe the superior one is something called Regional v-net integration so if Regional Vena integration at the app service plan not per app so you have this Regional vnet integration it basically takes over a subnet and IT projects these Phantom 

network interfaces into it through which it can go and get to things it has to be in this the v-net has to be in the same region as the app service plan hence Regional but it can then go and get to things on kind of any connected Network peer networks express route that gives me access to any think if that is not an option uh another model I can do is it can establish a point to site VPN connection out to obviously some 

Gateway that could be in other regions at that point but it doesn't work with resources like service endpoints or connected over express route it's really just that I guess there is a third option there's something called hybrid connections and that's really using things like Azure relay that I might use on premises it establishes an outbound connection to the relay service and now it can get to 

anything on that Network so I could use that for like on premises connectivity as well so these things the regional vet integration the Gateway is the Gateway required I think it's called Gateway required integration or the hybrid connectivity enable the apps to get out to whatever that is connected to so that's kind of a a key point about 

that okay coming up to the end um one more really big service so that's nsgs the next kind of thing I can think about from locking things down is azure firewall now I drew a picture this kind of already this way way back my board's getting so big now it's going to start crashing I'm sure I deploy this into its own subnet Azure fiable subnet um it has 

to be I think it's a sl26 minimum and I just use userdefined routing to send traffic to it could be 000000 for everything to go VI it I could send particular things but the whole point is I'm going to use route tables and use Define routing to send things to my Azure firewall it has public IPS so it can also get out to the internet it can snap the traffic for me um it's very good at East West traffic 

kind of management it can accept inbound as well it's not as good as say as like app Gateway but I I can do that so remember the whole point of a a firewall then is yes I have my virtual Network I'm going to create this Azure fball subnet that only it can use nothing else can deploy into that it's 

going to be this sl26 minimum and into that it's deploying its appliances so it's creating these multiple appliances and the primary thing it's going to do initially is it's going to be this internal IP that's kind of balancing between those and that's the important part because all the other subnets are going to UDR to Route traffic kind of through that it can be peered as well I could 

have another v-net multiple peered and it can use that internal IP as its next hop as well I can do all of those things and the key part what I'm going to with Azure Fireball there there's two SKS so I can think about there's a standard skew and there's a premium skew so the premium skew literally just come out I literally just released an 85 minute deep dive video on this there's a whole bunch of features I am not going to go into them but understand sort of the 

things it can do it's built in ha availability Zone support all these different types of filtering and monitoring premium primarily adds really I think about is three key features I can do TLS inspection I have this ID PS intrusion detection and prevention system so I'm looking for particular types of headers um things in the header but it's not really stateful and I can do URL 

filtering so instead of looking at just at the fully qualified domain name I can look at the path as well and I can use that path as part of web categories web categories is a standard feature but with premium I add that ability to use the path as part of the category a news site a search site etc etc so premium I'm really adding that kind of TLS inspection and watch my 85 minute deep dive if you want to know all about these things um I have the idps and URL 

filtering so remember URL is fully qualified domain name plus the path and kind of HTTP etc etc and what I do is I this is really getting I think upset the size of this whiteboard at this if this crashes it's not my fault someone else's fault what I do is I create a policy now there are classic rules that I apply directly but we try and stay away from that now the premium can only use policies so I create a policy I can 

link one policy to a particular instance of azure firewall and then I have rules and there's really three types of rule there are net rules n rule is all about hey I've got this inbound traffic coming in to one of those public IPS it has I want to do dap and I'll show these in a second but it's basically hey coming into this port and this public IP send it to this backend 

member very very simple I can do Network rules so Network rules we really think about as layer four so hey TCP UDP is kind of those five TS again sour side P IP groups which are just groups of ips I Define in Azure um ports I can obviously use the CER ranges I can use the service tags again 

those service tags we used in the nsgs this about allowing disallowing those types then there are application rules so application rules as you're going to guess is more about layer seven so here I can still control hey who it's coming from who is the source but now I can control it based on hey what's the fully qualified domain name what's the fully qualified domain name tag a fully qualified domain name 

tag are just well-known Ms services that they are defining that may be used different fully qualified domains Windows update Windows Diagnostics they create those for you if it's premium we use gold again for premium um based on the URL and then I can also do it on kind of these web categories but then once again with 

premium I can also include the URL to help distinguish that whereas the regular standard is really just that fully qualified domain name so I have those different things I can actually do let show it to you quickly so if I jump over to my Azure firewall super super close all these down again to my Azure firewall here basically I don't 

configure anything here this is premium so I can't do classic rules all I can really do is link a policy one policy and then in the policy that's where I can Define the DAP rules which say about inbound say coming from these places which home Bas is an IP group go into this port on this protocol redirect me to sorry when it's going to this public IP on the Azure firewall over here so going to this 

public IP on this protocol this port from this IP Group which is a bunch of ips I want to send it to this private IP on this port so it's just sending to some backend member a Network rule well hey again who it's coming from so I created an IP group of the IP spaces of my v-ets and in this example I said hey from the IP space on 3389 if it's TCP 

going to the same group of ips allow the traffic a very simple Port protocol destination allow and then app rules these are the Richer things here I'm saying things like hey based on let's look at one of these coming from a certain IP range this is my West Central v-net I've done a rule based on web 

categories and because I've got premium and I've got TLS inspection even if the URL changes I'm giving it access to these types of sites this is a continuous daily updated feed coming in for this but there are also rules where I could do based on fully qualified domain name tags so these are the popular services that Microsoft have defined I could also do it based on the URL I can have those as well and if I looked at the network 

rules let's look at one of these quick you could see I could also have service tags those same service tags I could use as well because that's really a layer four type thing it's okay to have those and then again TLS inspection threat intelligence those looking at all the different signals there's a mass of different signatures it's using to kind of Leverage those malicious IP addresses sorry I'm talking about idps are the signatures idps all 

those signatures about detecting hey these types of malicious um types of things in the header I can really control and lock those things out so really powerful capabilities I'd often use it with I'll still use nsgs for some of that micro segmentation I can use this kind of that layer seven is extremely powerful saying I cannot do with nsgs and then really the final thing is 

understand the monitoring um there's Network insites there's a whole bunch of different things that I can leverage um to understand this connection monitoring I can have agents deployed and do rules to go and check there if you go through that learning it it goes through all the different resource sources a really powerful one is Network Watcher so Network Watcher gives me insights into a lot of that traffic and when I talked about these nsgs one of the things I can actually turn on is something called 

NSG flow logs and I can kind of turn that on and these go to a storage account and then optionally I can kind of send it to a log analytics workspace and then with if they go there I can do something called traffic analytics and traffic analytics gives me this visual kind of 

goal showing me most common people talking hey malicious traffic I can see the most um all huge amounts of detail through that but I have to kind of go and turn that on so I have to have nsgs and then I can use all of this is kind of part of this network Watcher component it's a network watcher is very powerful opens up a huge set of functionality but really getting the flow log is not the data but it's hey it's from this source to this 

destination these flows it's capturing that data and then I can do this traffic analytics which is part of the network Watcher if we go and look at Network Watcher just to give you a really quick idea of some of the functionality so I've got my network Watcher and you can see hey look I can look at the topology I've got connection monitoring where I have those agents I can see is the connectivity working is it failing I can validate things like IP flow NSG Diagnostics work out what is 

the next hop what are the effective security rules and I kind of showed you the effective routing you can look at the effective security rules I can see that on the Nick as well um I can capture packets I can turn this on on a per VM basis if I'm doing like some deep troubleshooting I can turn on the NSG flow logs to actually go and capture those and then from that once I've got those I can do traffic analytics that then gives me this fantastic kind of visual view of hey these are the most 

common things talking I can do it via a map I have things like Network insights see lad bers there's just a massive things go and look at these understand kind of the key things you might use to troubleshoot but super super powerful um just so much to cover but this is kind of where we are I don't think I can zoom out anymore I think if I can fit oh there go there we go we fit it all on the board so this is what we 

covered um obviously a huge amount of stuff it's done that weird browser thing there we go um I hope this was useful go through the docs see the learning again my playlist I go through really all of these things in detail now there might be I don't know how many hours of content is there maybe that would be eight hours of your life um but I think it will help you but this was kind of the summary maybe watch 

this before you start learning to put everything in a picture then you might link it together as you go deeper dive I would definitely maybe watch it I don't know how long I've been recording for 3 hours now my voice says 3 hours uh I it just before to cram some last minute knowledge in but super good luck don't worry if you don't pass everyone fails things sometimes it'll tell you at the end where you did kind of weaker go and redouble your efforts and you will definitely pass next time believe in you but uh please please this 

was so much work really would appreciate if you would subscribe definitely like and uh until next time take care for
