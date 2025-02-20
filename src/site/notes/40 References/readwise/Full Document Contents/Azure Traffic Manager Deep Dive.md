---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-traffic-manager-deep-dive/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/PfZPuBt50ps/maxresdefault.jpg)

hey everyone in this video I want to talk about Azure traffic manager now you might be thinking John you've already done a video on Azure traffic manager and yes I have but I did that video a really really long time ago so long ago I even had a tiny tiny amount of hair so clearly it's probably time to have something a little bit more recent and not just rely on that so my goal is to create an updated 

version of the traffic manager solution now why do we have this solution at all now we also about resiliency we talk about scaling based on requirements and if I think about resiliency if I think about performance the way we do that typically is imagine I have some kind of service so I have some service that I have running and in Azure world what I would do for resiliency is well I have 

multiple instances both for resilience and performance and I would spread them over constructs such as availability zones so hey I'd make sure my services in AZ one and az2 and az3 but this is all living within a certain region and that region itself could have a problem so we also always thinking about well I'm going to have another instance of my service once again spread over availability zones in a different region 

so region two and so on so I have multiple instances of my service now the other benefit and the requirement we have around using multiple regions is remember a region is a certain Geographic space so remember the certain two millisecond latency envelope and my client population may be scattered all throughout the US throughout Europe throughout the entire world and in today's world if performance is 

poor we consider it broken so the other reason we have instances of services in multiple locations be it in Azure regions or other constructs on premises is there closer to the user so if I'm sitting over here near region one hey I'll talk to region one my latency will be fairly small if I'm sitting over here hey I'll talk to the region closest to me so again my latency will be low my performance will be good so we have these multiple instances of 

regions of our service so we get resiliency from a particular failure blast radius but also so clients can talk to One closest to them to get great performance but the issue with this is that why have my client so if these are all my instances of my services over here what I then have is my client so my client is sitting over here for example 

and I don't want to have to know well if I'm in Europe I should use this DNS name if I'm in the US I should use a different DNS name what I want is a single endpoint that I will communicate to so that's the whole goal of when we think about these Global Services is I want to be able to provide a single point for this to communicate with now there are numerous solutions to 

solve this if I was to think for example we talk about layer 7 so it's HTTP it understands the application protocol there are things like Azure front door so as your front door is fantastic for those HTTP https HP 2 workloads because it has any cast IPS that are through the entire Global Microsoft network it uses split TCP so that my TCP session is terminated close to me my 

TLS session is terminated close to me at the closest pop and then it goes on its backend Network to go and get the data it can do caching because it's layer 7. it's intelligent it can do TLS offload and certain types of affinity so fantastic for that if it's layer 4 there's things like the Azure Global load balancer which again is an anycast IP so it's a global Service and then it can redirect to Regional standard load balances 

but what if my requirement doesn't fit in those buckets what works for anything what works for anything is good old DNS I give it a fully qualified domain name and it returns an IP and so our DNS solution is the topic of this talk Azure traffic manager 

so the whole goal is with DNS it's going to return to me either a name of a DNS record or even an IP address so it might be a c name it returns to me or it could be an a quadruple a if it's IPv6 record that I should then go and talk to now a key point when I think about Azure traffic manager it is a global Service and remember this is basically our entry point to get to all of our other 

Regional Services beer in Azure be it in other clouds be on premises it doesn't care but that means it needs to be Rock Solid and so there's a huge amount of work some of which I can't talk about within the DNS Services of Microsoft to just make that serving plane so resilient this needs to be a dial tone service I just need this to always be available because this is our doorway before I can start talking to anything 

else so there's a huge amount of work going on here now remember for me as the developer maybe of my client application there are still things I can do I can do things from my most critical applications such as hey when I go and make this request by my DNS resolver to find who I need to talk to I could add in things like well I'm going to Cache the last response it actually gave me so in the case there was some Global issue 

I still had the last response that I got and I could go and then talk directly so things I can architecturally do to add even more resilience in the extremely rare scenario that there is some Global DNS problem so it's not like hey there's nothing I can do at all now the way this is going to work is traffic manager is not a a regular static DNS zone so if I was to think about my traffic manager 

solution then we have there's going to be this Dot traffic manager .net and what we will get is for a particular profile so what happens here is we create a traffic manager profile now a profile is a certain set of configuration so that profile has a 

certain name and maybe it's easy to show one quickly so if we jump over if I go and look at the portal you can see I've got a whole bunch of different profiles here and the reason I've got multiple profiles is there's different routing options that I have we can see over here routing methods which I'm going to go through but I wanted to create one of each but the whole point is each of these are a profile so you can see here this is a 

particular traffic manager profile and the key point is it has its own name so in this case this is HTTP savotek so the key part here is it's going to be savotek then it's always dot trafficmanager.net so that is the name and I could go and use that traffic manager name if I jump over here and I'm going to my service so we give it savotek dot trafficmanager.net now 

the records behind it is not actually anything serving trafficmanager.net but that's the point that it's redirecting it's bringing me other records so I have this concept of a profile and it has its own name and what's Happening Here is this profile it has a set of back ends so what I've configured here is a whole set of different back ends 

that it can respond with so there's its own back end and there's other configurations we have now one key point and I guess I should cover this straight away I am not going to publicly want to use something.trafficmanager.net there's no scenario if it's client visible that I want to expose that now remember what is DNS the whole point of DNS is I 

as a client let's actually come over here a little bit so when I as a client I'm trying to get to something I want to talk to a certain service so there's a whole set of different components involved with that now the first thing that really happens here is I make a query so I make a query for a record so let's say it's that bad father I'm just going to write BF Dot Savo Tech 

.com because I want it to be a friendly name that I want to be visible I don't want trafficmaster.net so I've got this record in my custom vanity domain it's the domain I want to be publicly visible now what happens is I send that request to my DNS resolver and my DNS resolver now recursively it goes and gets redirected to different servers is going to look that up and so what's happening is I have a zone for 

savotep.com and what I would add in here is I add something called a c name record so a cname record references another record in another Zone typically but it could be a record in My Own Zone so in this case I've created a record called BF so it would be bf.savletech.com and it points to 

the record I created in traffic manager savotek.t traffic manager.net and we can see this so if we jump back over so remember this record in my traffic manager was savvaltech.trafficmanage.net if I go and look at my saviletech.com zone so this is hosted in Microsoft 365 and this is the authoritative zone for savotek.com we can see down here well I added a 

cname record for the name bad father that actually returns savvotech.trafficmanager.net so that's what will enable me to just type in hey badfather.savotech.com and it will respond to that site and we can see this happening so if we make this a bit bigger if I do a name server lookup 

bad father.savletech.com you can see the entire flow happening so what we can see here is well I typed in my request that cname record I created referred me to the traffic manager name and then what's happening in this particular traffic manager it can return a number of app service websites so in this case it returned this one because it was closest to me because I'm using performance which then actually resolves 

to this particular host which eventually then returns this particular IP address so you can see that complete flow actually happening within there so if we was to finish that off just for your understanding so the point here is then that hey I query my DNS was over for badfiver.savletech.com it would then query that authoritative 

zone for cybertech.com it will then return me a reference over to here now this can return different things because remember I said there's different types of back ends well I can have back ends that are typically other DNS names so if it's another DNS name what it would actually return is a cname record to them what is the final service so it's then going to go and look up something else 

if C name but if it was actually an IP address and it would just return me an A or a quadruple a if it's IPv6 record and at that point whether it had to do another hop over there to resolve another name the client gets that response that I showed you so it hey gets a list of all the aliases but eventually it gets an IP address and then the client which just talks directly so these are my services over here 

it just goes and talks direct it's not the traffic the data plane does not flow through traffic manager at all it's just traffic manager is getting it the thing the IP address the DNS name that it should talk to for its ongoing service requirements so that's the whole point around what is happening here so traffic manager has no ongoing implication as part of the data flow it's only doing it 

to go and find hey look who I should talk to and when we think about the things that traffic manager can do primarily some of its routing methods can be based on well my proximity to the possible targets a big one is called performance it is primarily considering the latency map of my DNS resolver because it's my DNS resolver that traffic manager is 

seeing the request from the client is talking to its local DNS resolver but he's not talking to me directly so when I have to make my decisions I'm really considering the latency between the DNS resolver who is talking to trafficmaster.net now there are some extensions where the client subnet address can also be passed to the DNS server so if that is provided by 

your DNS resolver then that client subnet information can be considered as part of its decision around which back end it will actually send you to but primarily hey it's focused on the DNS resolver so you want your clients really to be using a DNS resolver that is geographically similar to them which will typically commonly be the case okay so I talked about these different types of back ends that 

are supported and there are three types there's external Azure services and nested so let's actually go and dive in a little bit to these different types of back ends that we can actually use now they should be public and this is a key point this is a public service whatever it points to should be other public services other public Azure Services of a public IP addresses other 

public DNS names it's not used for private services and I can mix them within a single profile so I can have a profile that links to some Azure Services it could link to some on-prem things via Republic IP or DNS name in my assign that links to another traffic manager profile so the first option is where we can integrate with Azure services so in terms of my types of backends I can have let's just 

move this over give myself a little bit more space so we move this over to here so the first type of option I have is hey it could be Azure services so this right here azure now specifically when we talk about Azure Services it's probably easier to go and see this if we go and look at what I could actually add here 

if I go and look at what are my possible endpoints that are available to me and if I do add well firstly we see the three types so there's Azure endpoints external endpoints and nested endpoints so if I select azure this is what I can Target a cloud service which hopefully you're not really using cloud services anymore but there was some extended arm support added but 

those were really the original type of service app services now if I use app service it's really important that it is standard SKU or above it will not work with the free or the more basic excuse it has to be standard or the redirection does not work correctly if I'm using multiple slots or I can use app service slots slots enabled me to have different versions like a uat a blue green whatever I might want so I 

can Target a particular slot or it can even be just an Azure public IP address now I can pick any of these if I do app service it will show me what app Services I could possibly use now I cannot use the same service within the same profile more than once so I'm already using both of these in the profile my East us and my West us so if I try and select this it's going to error you're already 

using this target within this profile so I have those options for my different types of azure service it would show me public IP addresses that I could use it would just be a list of the ones I could use and I could select notice it's ipv4 and IPv6 so I do have those options so that's one option and obviously as you just saw well I can also do external now if it's external all I'm typing in is either an ipv4 

an IPv6 or a fully qualified domain name I think I went and created a different one was it Priority maybe I added because a key Point here is if I use external so yes I did an IP here so if I look at my endpoints I added an IP address and in this case it's just a particular 

ipv4 address just enter that in great I cannot mix different types of external within the same profile so what I mean by that if I now tried to add a fully acquired qualified domain name is complaining you cannot have different types of domain name ipv4 address 

if I try to type in an IPv6 if I did f06 I'm going to do that and do add it looks like it's working but it's going to fail it won't actually add it because once again so fail to save it you cannot mix targets so I cannot mix ipv4 and IPv6 so the key Point here is telling me 

that for my back ends so Azure Services one but I can also just have public endpoints so I can have another type which is just some type of public endpoint and there's public endpoints great they can be ipv4 or IPv6 or a fully qualified domain name 

but it's per profile I cannot mix them now there's a exception to that and I guess we'll draw a little star there and the story is set for the multi-value which we're going to come back to but with multi-value it just returns a whole set of Records 

I can mix ipv4 and IPv6 in a multi-value type of routing but ordinarily as you saw you cannot so I would be all ipv4 externals or all IPv6 externals or all fully qualified domain names because it comes down to the type of record it has to return it returns a cname or an a record or a quadruple a record Well normally I don't want to be switching between that now I can still mix ipv4 with Azure services or IPv6 with 

Azure Services I can still mix all of those things together generally I prefer to use a fully qualified domain name just because it gives me more flexibility on the back end that hey IP addresses could change what's actually providing that service I don't have to go and add and update my endpoint so as much as you can try and avoid putting in specific ipv4 and IPv6 I really would rather put in DNS names which 

becomes that c name to what actual service is providing it that would probably update more quickly so try and avoid these as much as you can but sometimes hey it's going to be required and then my other option is I Nest them so my other option right here is absolutely we have this option of nested 

and when I do nested I can configure a minimum number of endpoints for it to be considered healthy and of course if it's nested what it's basically pointing to is I have another profile so I have a completely different profile up here profile two and this nested one is just pointing to it 

and that profile too would have its own sets of back ends and that can be really useful so the ability to have as one of the back ends another traffic manager profile is it starts to give me a lot of flexibility and how I can handle the routing I might have a primary routing method I want to use for how do I pick which back end but then hey there were certain 

circumstances that I want to then have some different Logic for a certain set of back ends well those back ends I put in its own profile and then I reference that profile via nested as part of a parent profile so I it gives me a huge amount of flexibility to actually do this and we can see this if we jump over again if I go and look let's close this one down 

if I just go back again to my main and I go to endpoints I just do add and I select nested all I'm going to do here is Select one of those other profiles I want to include priority notice it's asking me for a minimum child endpoints so what this is saying is ordinarily there's a certain amount of Health probing going on which we're going to talk about 

so as part of these checks it's going to go and check well is it healthy because only if it's healthy do I want to send people there well in this case to check on if a nested is healthy how many of its back ends that it's checking are healthy has to be healthy for it to be considered a viable Target that it wants to return to the requesting DNS resolver so one is the minimum it has to have at least one healthy back end of its own but maybe I say two or three I can configure what I 

want to consider healthy so I have that flexibility um one of the places you're always going to see nested is if I use routing based on particular geographies because I can only have one endpoint for each geography which in itself means there's no resilience there so what's really nice is I could create a profile that maybe uses some other routing method maybe it's priority or weighted we're going to 

talk about all of these which have a set of different back ends for example North America and then I have my overall Geographic profile that says hey well this is North America because you can only have one endpoint for a particular geography but then it's pointing to another profile that has a whole set of different backends that that's a way I can use that more powerful combination but to still give me the resiliency I actually want now I mentioned Health probes so one of the things we obviously want 

to check is if I've got a whole set of different possible back ends I can send things to well I don't want to send it to one that's not healthy and so what we absolutely have is the concept of Health probes so I'll use a light friendly Green for health probes so part of the profile is we can configure Health probing now 

as part of this I can configure well what's the protocol that I'm going to use to go and check so is that HTTP is it https is it TCP um what is the port that I'm going to go and check for what is the path so we'll say the three p's and there are other things I can configure as well so these are basically going these Health probes are going to go and Fire and check all of the different back ends to see well are you healthy or not 

so once again if we go and look this is part of each profile I can go and look at my configuration and now I have the endpoint monitoring settings so here I was doing https but we can see I can also pick from HTTP https or TCP the port the path if there's any custom header settings I want but also I can have things like extended code ranges for checking I can have a probing interval 

how many failures will I tolerate before I consider it bad what is the timeout of my probe so I can do a lot of configuration in this and remember the key point is I want to pick a health probe that actually truly indicates is that back end healthy or not so I could have a maybe it's some sort of component running on these back ends that has its own specific path like I don't just want to check is the website there maybe maybe that's pretty useless maybe the website is there but what's 

internally running the app and providing other content is down so I could configure a path to maybe some sub component that proves the actual engine is running and processing I'm expecting a certain return code from that so my health probing is really accurate now there may be some circumstances where I don't want the health probing I want to just always return back ends and so I can actually override and say look I don't want you to do the 

health probing so if I look at a particular back end if I look at my endpoints and I just pick one of them we have the concept of this health check and by default it is enabled however I can always select always serve traffic and this turns off the health program it will just always return this as a viable option doesn't mean it will 

actually return This Record but it means it is a viable option to be returned so I might do this in circumstances where the health probing cannot adequately ascertain is it truly available and what I maybe do is I've got my own logical processing running that is doing the health checking and then via API via arm it's updating the back ends whether or not it should send traffic to that back end or not so if I 

want to I can configure particular backends to always be served which says I don't care about health probing always serve me as a possibility again it doesn't mean it will be returned as the ultimate answer it just means depending on the routing logic I'm using it will be a possible viable option that can be returned if it's the most suitable in some way so we have that available so then how do we distribute the traffic 

I have multiple back ends how do I know which one we should actually return so we have all these possible backends available to us and I need to pick what is the right one to return for any particular circumstance so what we have is routing methods I'm going to do routing method because a 

particular profile can only have one unless I'm doing that clever nesting where obviously that profile has its particular routing method and then it's being called by another profile which has its particular method now potentially you can change the method of a profile but what you're going to see as I go through this is there's particular configurations that the back ends have depending on what is my routing method and if I try and change it unless I've 

added the right data it's going to say hey you're missing the data on the endpoint so typically we're just going to create it of a particular routing method and you may have even noticed something when I was playing around with some of the back ends you might have seen or hate wanted a priority or it wanted a region well what it's going to ask me for is depending on the routing method but we'll come back to that so what are my routing methods so I have priority 

so each back end will have a priority between one and a thousand and in this case the lower the number the higher its priority the same with a priority one that's going to be served first if it was not available because the health Pro being I said hey it's unhealthy then it would return the next highest priority so number two was three or four so I would use this when I really had a primary back end and only if it wasn't available 

would I want to return a different one I can do weighted and once again it's between one and a thousand but this time the higher the number the greater the probability it will be returned so each back end will have a weight and in this case the higher the weight the greater the probability so if I had two back ends one with a weight of 100 

one with a weight of 200 the one with 200 will have twice the probability of being returned so here I would use if I had multiple back ends if multiple are healthy well maybe one of them has more resources than another deployment so I want it to get the preference but I still want some traffic to go to another one maybe to make sure it is healthy so I can keep testing it so I would know maybe I'm doing it as part of a move over and start switching 

a flow of traffic so moving percentages over so waiting lets me control that and we also have performance now performance is one of the most common ones because what this is basically saying is closest so this is where it's looking at well what's the latency map between the DNS resolver or if it is passing the information the 

client information to order the possible backend targets now latency map is based on the Azure regions obviously if it's an Azure service it knows the regional ready if not well I have to tell it which region is this particular thing closest to we're going to come back to that then we have Geographic so each back end will be assigned a particular geography this is really 

useful if I have certain data sovereignty or regulatory requirements that I need to make sure is only used when I'm coming from that particular location and again this is where a particular backend can only have a geography assigned once so if I'm us I can't assign us to multiple back ends to give it resiliency so what I would have to do is I would create a different profile with all of the possible backends for the US and 

then on the nested backend entry that I would configure with us because I couldn't give this one us as well it will error out I'm going to go back and look at the details of all these I could do multi-value it's a multi-value is all of these other ones return a back end it gives me a back end that the client should then go and talk to multi-value does not multi-value returns all of the 

possible back ends and then that's the client make the decision on which one it's going to actually go and talk to but again it has to only be these external ipv4 or IPv6 so that's kind of a big deal we'll come back to that again and then I can do subnet and subnet is based on it's going to map a set of end user IP address ranges to a particular endpoint 

so when a request is received he's going to look at the endpoint return to be the one that's mapped to a particular set of suicide P addresses I've configured so hey this public Source IP address range this cider range if it's within this range it goes to this back end um this other set of public IPS goes to another back end so it's just an option we have available now because of this because of all these different options as I'm kind of getting 

to here there are certain properties I would have to set for the back ends to work so priority I talked about you have to set a priority for weighted you have to set a weight and we can see these and this is why I created different profiles so if I close this down if I go and look at priority when I go and add a back end endpoint it's going to make me enter a priority 

again between one and a thousand and it's recommended number two because the one I added already was number one if I did weighted is going to make me enter a weight to notice there's a different additional attribute required on the endpoints depending on what is that traffic manager profile if I do performance 

this one is interesting if I add a performance endpoint if it's an Azure resource notice it's not asking me for anything particular about a location because it doesn't need to because an Azure resource lives in a particular region but if I select anything else if I select external notice it's asking me for a location 

or if I select nested it's asking me for a location and these locations if you look at them are the names of azure regions because What's Happening Here is it knows okay what is the latency heat map for all the different Azure regions but it doesn't know the location and the latency heat map of some random ipv4 

address or what my nested profile seems to be and so if I do performance what I have to add here is a region so I have to configure them with a region that represents who they are closest to or at least what I want them to represent so I have to configure that region public endpoints and nested I do not have to configure it 

for Azure Services because we already has a region because it's an Azure service so I don't have to configure it for Azure Services because the region is just implicit it's the reason we're set when I created the resource but if I want to use an external if I want to use a nested performance is all based on hey what is the latency heat map what's closest to you requesting it it 

only knows its latency heat map to the Azure regions and so if it's something that's not an Azure service I'm going to say hey well this public endpoint and you know Hey look it's physically located in Seattle well then hey I'm going to pick a region of West us2 or something whichever one is closest to it if it was in England okay I'll set a region of UK so I would pick the location to be the Azure region closest 

to this or again the one I want to serve the traffic that would be considered closest to that particular request with Geographic I have to set the Geo now there's different levels that that geography can be configured on so if I jump over let's close that one down and we'll go to our Geo 

and look at our endpoints again now notice I've added one already and you'll see in this case I just added it for North America but I could add additional ones so I can pick the regional grouping and notice the first level is fairly generic I could do all like the entire world to create a catch-all which would be really useful and then one of these more specific things now I could not just select North America 

if I try to save this it didn't do anything because it already had North America let's actually go and add a second one it's more useful and in my regional grouping I'm going to pick North America again and I'll give it a test and we'll just pick something like a different one 

notice it's unhappy it's saying hey look you have to pick a country and it's saying I have to pick a country this time because I've already added an endpoint with North America up here so I can't add a second endpoint for the exact same geography I have to go more specific this time and I can be super specific I can go all the way down to if I wanted to and this is now optional if I could go and pick it for a certain state so there's different levels but I cannot 

have the exact same level of geography for more than one endpoint this is why if I wanted to just have North America with a bunch of different endpoints I would create a different endpoint remember so I'd create one profile for North America with all of its possible back ends maybe it's using performance or priority or weighted and then that profile I would add as a nested profile and I would give that the 

North America Geo so that's why we think about combining those things together but the geographic is hey I add a geography for each endpoint and we saw those different levels of how specific it is depending on how I want to match those multi-value as we said now remember multi-value can only be let's do something actually in red there we go so multi-value can only be 

that cannot add Azure Services I cannot add nested I cannot add fqdns but it can be a mix so in this case it's ipv4 and or IPv6 I can have a mix of those returns so this is the only one that lets me mix ipv4 and IPv6 in the same profile but it can only be these external public endpoints so 

that's really the key part of those and then subnet I'm just adding cider ranges so for subnet over here what I'm actually adding is cider so I go in and I add a bunch of ranges so again if we jump over here and we look at subnet when I add one what it's asking me for 

over here as you can see is the sidear range so I have to add in either particular IPS or the range so I can do the sidear format here or I can just enter a range of ips so it's coming from those that would get mapped to this particular endpoint I am adding and that's really the key point and I guess really I noticed I wrote 

public endpoint I guess I really should call that if I want to be um accurate I should really call that external just to get the nomenclature right so we write external but my point was I wanted to stress the point that it was a public has to be publicly facing but I should use the right name external there so those are the configurations so it brings all of that together and so I can think about that 

this will work for anything it really is using that that DNS service but it is a DNS service it's not adding any application Level intelligence it's not doing TLS offload it's not doing any type of sticky Affinity or something it's returning a record each time it's just giving me either a cname record back that I then go and look up or if it turned out it was an external endpoint or a public IP 

it's returning me an A or a 4A record if it was IPv6 that the client then goes and directly is talked to but it is adding no other richness beyond that but I think these routing methods are super powerful when I think about how it knows which one is the best one to go and talk to now if you're unsure of which one like I thought that three Global Services here I did a separate video where I talked about picking the right service but 

additionally Microsoft actually makes it fairly nice for you so if I just go and search for load balances overview well notice it actually starts off with hey does your application so it has a help you choose and it was one of the menu options as well so I'll say well no it doesn't is it public facing yes it is is it in multiple regions yes it is does your application require a static 

IP address I'll say sure so it's saying hey there's an Azure load balancer is an option there and it gives you a summary of the business needs but what I can also do is service comparison and this is where I could see those three possible options for Global remember load balancer can actually be Regional or global and then you can scroll down and it tells you well okay what are the 

different routing policies available so hey the traffic manager has a lot of flexibility it can be all these different types but the key Point here is that traffic manager is any Azure front door are only these load balancer is only those so that's going to be one of the big decisions you can make there but then traffic manager adds no other features like it's all just blank because it's just DNS it can't do all of the fancy 

other stuff because I mean that's just not the level it's working at and you probably wouldn't want it to anyway in terms of the metrics available to me so that it's fairly basic because again it's just a DNS service there are two metrics so I could go and look at the endpoint status one means it's of a up zero means it's down so all of mine have been up I could split this so if I apply 

splitting Supply splitting is up here I could then split it based on the endpoint name and then what I will see is a value for each of my two back ends and they've both been up which is great but I can go and see that detail my other option I don't mean to do that my other option I can do is queries by endpoint returned and it's just showing me the amount of queries I'm running against a particular 

endpoint again mine is not very big in this environment because it's not doing very much but that is available to me you can also turn on this concept of traffic View so a traffic View and mine may not even have enough data right now but if I enable it it needs 24 hours to bake yeah I've not given it enough time but basically what it would show you is information on where the user DNS 

resolvers are the volume of traffic the representative latency and the different traffic patterns so you'd see all of that data you also see this real user measurements thing now I'm not using that at all what we'll use a measurements lets me do is now I have to pay for this but in my client code um I could actually add a bit of script that they give me and what it would do is it would try and download a single 

Pixel from all the different Azure regions and then feed back that latency information to Azure which can then influence its routing methods that use that latency for example Performance will be a big one there so instead of it just using its more generic information on what its season understands well now I can feed information in Telemetry because hey my client's trying to download this single Pixel from all these different regions and then give that back into azure 

but that is telemetry Azure has to process accept and do with so that there is a price for that but hey I if I want to have more um feedback into that decision making I can absolutely use that option and so I could generate a key I would then take the JavaScript it gives me and I can then start feeding some intelligence uh into that for the pricing information 

so we look at the pricing I mean it's cheap so for the first billion DNS queries uh it's for so per million it's 54 cents so it's not a lot of money there's obviously the health checks there's a certain cost per month and there's fast interval health checks the real user measurements there's some special things about how this is working and I think they're 

rolling some of this out traffic view so to get those data points processed is two dollars per million data points processed so there are some costs around that now obviously is DNS it's one of the big things DNS has is as part of the configuration you will configure a time to live so A Time To Live is all about well hey when it returns This Record the client cashes it for a period of 

time that it considers it accurate for and only once that time to leave is expired will it then try and go back and get an updated result unless I sort of flush out my DNS cache now obviously that means the smaller that time to live the faster it will react if now maybe it was healthier now it's not healthy to go and get an updated record but it also means it will be querying more 

frequently which means I'll pay more money so the balance between well how forgiving do I want to be if something has failed and now I need it to return a new one and go back and get a different address compared to if I set the time to live too small it's going to be hammering it which yes it's very cheap was it 50 cents or something per million but if a client was checking every minute for example and there's millions of clients well that price is going to start to step up so there's a balance when I think about a time to 

live between responsiveness to a back end failing now remember my back end should still have their own resilience it's not just like oh there's some single thing for example in Azure or these would be a regional load balancer be at Gateway or a low balancer and then multiple instances behind it so if a just a server failed or an app crashed or an OS crashed or even a data set that failed it's still running so 

this the back end it redirected me to is still healthy and it's fine I'm really talking about hey an entire region has failed so there's a balance of responsiveness there but that's something to consider if my time flip is too big if there was one that was taken out of the rotation is going to keep using it for a period of time which is why if you have some planned retirement or maintenance I would remove or disable the back end ahead of time so that it will stop being 

sent essentially you're draining it as a Target once that time delivers expired and no one would point to it anymore then I can go and do whatever maintenance I want on that so just think in mind there is that that balance to think about and then if you have other questions the documentation is fantastic and I recommend go and read the FAQ document it's huge it talks about implications of geography and is it how accurate that geography is 

if I'm linking it to there so if you have questions about traffic manager I mean seriously go and read the FAQ dot because it's really powerful and it will probably answer any of the questions you have so definitely go and check those things out check out the other docs it has all these step by steps notice as I mentioned an endpoint can be disabled so if I did have that planned maintenance that I have going on in an hour's time hey go and set it to disabled 

wait for that time to live to expire whatever is configured for the profile and then I could go and take it out rotation and most likely what I would actually do is hopefully you've got some pipelines so in my pipeline if I knew I was going to take out a huge Target it automatically via the API since it's disabled weights does the deployment brings it back in now normally we shouldn't impact availability because we're within a location do a staged 

rollout so the service is still running but if that wasn't available for some reason I can build that in and I can disable it um and that was it so I really hope this was useful it's a phenomenally powerful service and it really is kind of you think as a dial tone now the resiliency they're building into the Azure DNS because it's so fundamental if DNS doesn't work nothing works so yes I can build in some logic and clients to Cache things and for real 

Mission critical apps but they're doing huge work here and they're very very powerful routing methods available to me combining them in that nested pattern gives me even more flexibility but yeah just to understand how the things are working understand the types of resource and you can get a really powerful global entry point to your public facing services until next video take care
