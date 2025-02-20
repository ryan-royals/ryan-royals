---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-virtual-wan-overview/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/f-GyAURZWzg/maxresdefault.jpg)

hey everyone welcome to another 360 in 360. and for this one i actually want to talk about azure virtual one but a lot of people request look what exactly is this thing and i can really think about forgetting about anything in azure for a second if i'm an organization i might have multiple locations i can think about i have some really big locations maybe that's a great big data center maybe it's a big user population i might 

have multiples of these and then i might think about well i have maybe branch locations so i have these kind of smaller branch locations in kind of different areas maybe i even have individuals in the past this was maybe kind of those road warrior type people that are constantly out on the road today it might be more people just working from home so i have these different types of 

users different types of user populations and as an organization well i want to connect these things together but i also want to give them maybe connectivity to the internet and so historically our solution would be well maybe it's a an mpls so i can think about kind of i have this mpls network that these major locations are connected to so that's 

basically private connectivity and it's kind of a 2.5 layer labeling the packets and gives me this connectivity now for those branch locations well i have to do something else maybe for example i run a vpn service at one or multiple locations and they would kind of connect in by a vpn this would be a site-to-site vpn connection 

so i'm connecting that ip space to this ip space then these are connected for the individual users well via a point to site they would then get that connectivity as well but i'm having to kind of host that vpn connection again these are over the internet so i'm using that internet cloud and i have also this kind of dedicated connectivity and then if you throw in the cloud so i can think about 

well okay so now i've got kind of let's say i've got different azure regions where say we're using two azure regions and they're obviously connected on that great big azure network it's kind of one of the biggest in the world and i want to extend out to that now there's different ways we could do that that could be kind of a site to site i could do a vpn connection to gateways in azure we can imagine i've got kind of v-nets up in azure that i have resources 

running in maybe a music express route now there's obviously going to be places where this microsoft network is extended out into carrier neutral facilities they're called meet me's for express wrap purposes maybe that actually becomes a node off of the mpls so the mpls now can actually go and connect up into that meet me and extend the connectivity maybe i have a dedicated kind of connection um an actual line not an mpls just a 

private connection why would meet me as well so there's different types of connectivity i could kind of have there to enable me to kind of stretch those environments so i have those kind of different options but i'm managing all of that i have to enable those types of peering if these v-nets want to talk to each other well there's yet again more connectivity i have to consider and transit routing there's a whole bunch of complexity to 

this now this mpls you've probably heard of sd1 more more companies are looking at this sd1 type solution and it's designed around the idea of having this kind of central policy routing engine that will automatically go and populate appliances at my different locations and provide the connectivity very often the way it actually does that is is actually kind of 

over the internet so i can think about well there's the kind of internet cloud as well but sd1 could also use things like mpls but in the sd1 world well hey look we we all have these kind of appliances at the various locations and by the internet we have these encrypted tunnels that create this kind of mesh connection up through everything so this sd-wan is gaining more and more popularity 

but i'm relying on the internet here i'm relying on the carrier and the quality of that connectivity between them so where exactly is this azure virtual one playing and we can really take this exact same picture here and we're just kind of transpose it over to a clean canvas so we'll draw those same hey i've got these two 

major locations again i could have many many more and we'll think about well i have those same smaller branch locations and we've got those individual machines spreading different places those same kind of combinations of connectivity requirements and then we have the same cloud so we have the idea that hey yeah there's there's azure regions and there's regions all throughout the world 

and once again the important point here is those regions are connected to this massive microsoft backbone network now that microsoft backbone network yes it connects to regions together and i previously drew all the meet me locations where i can have things like express route but there are many many other network edge locations i can think about there were all these network edge kind of points of presence 

locations and what these are used for is these are all kind of those carrier neutral facilities where you can go and connect to all the different kind of connectivity vendors of the world the att's the verizons the t-mobiles the carriers you name it they have these almost direct connectivity to as many providers as possible that enables hey if i'm using x service provider hopefully i don't have to then go via another service provider to quickly get 

onto that azure backbone the microsoft backbone network want to be able to get onto it as quick as possible so the point of the the azure virtual one i just call it v1 going forwards is we want to leverage this if i'm going to this sd-wan methodology well who better than to leverage that backbone network so what we're going to do is we're actually going to create i'm just going to change the color a little bit for a 

second we're going to create a virtual wan instance typically we're only ever going to want one virtual one a virtual one is kind of like a security delineation if i had another virtual one instance that would be completely separate in terms of connectivity from any other v1 instance so i'm pretty going to have one and the way this manifests itself is i create hubs and i create hubs in regions where i 

want connectivity i have locations there maybe i have a big user population there so i'm going to put a hub where i want to provide connectivity so let's say hey i'm going to create a hub here in this region i'm going to create a hub over in this region as well now the hub is a virtual network and it's obviously certain types of gateways and connectivity and routers but you don't see that you do not see 

the virtual network you can't put things in the virtual network it's managed what i see is the hub resource so i say hey i want to deploy hubs to these regions the hub is deployed then it's providing me that that connectivity now the whole point is this is managed i'm not having to do anything now there are two different skews of the azure virtual one i can think about there's basic 

now if i'm using basic that is just site-to-site vpn so think about here well yep it's going to give me that site to site connectivity and so hey these branch locations for example yes over the internet they're going to get to whatever network edges as close to them as possible so it's going to quickly kind of like hot potato uh from the vendors perspective they're going to get it off and onto the azure network hot potato as quickly as possible then 

we try to keep it as long as we can so we're kind of cold potato we want to keep it on our network until we have to offload it to someone else so absolutely hey yeah i can i can site to site vpn in and connect to that hub this is a kind of site to site as would this one go to its closest network edge location and then they can talk to each other so that would give me connectivity between different sites it would also give me connectivity if i 

also had maybe v-necks here so i had a v-net maybe i had multiple v-necks i can peer them to that managed virtual network so now they could get to resources in those virtual network but it's not doing any transit what i mean is these v-nets yes could talk to these resources those v-nets cannot talk to each other so the basic skew is not providing any transit between virtual networks and 

it's only the site-to-site vpn now you may ask yourself okay well why would i bother with virtual wan then i can just deploy a site-to-site vpn gateway in a virtual network you can but i think it maxes out as saying like 30 tunnels or 15 active active connections the azure virtual one scales up to 2 000 tunnels or a thousand active active connections so the scale 

was just way way higher than i could do with a regular site-to-site vpn gateway that i could create so that the mass difference in the scale but then what we really move on to is then there's the standard sku and what the standard sku adds is well again we kind of talked about what we have this site to site and obviously you still have that with standard standard is basic and then 

other stuff but standard then adds point to site so hey great um i could now have those users kind of connecting to their closest point of presence and get to the point of sight so these could now connect in but it also adds express route so i'm just going to do xr so now this location for example 

hey maybe there's actually i could think about well yeah there's uh there's a meet me location and i've extended my connectivity out to that so great i shall pick this one so i've extended my network so i'm now using express route so i could have an express route connection up into here to add into that hub this one oh yeah it's doing express route up into here as well now today 

this express route connection this is premium and i have this thing called global reach i'll talk more about that in a second but i can have all of those different things as part of my configuration now so that's what standard gives me standard is also giving me transit between the v-nets so those v-nets that typically couldn't 

talk to each other with standard they now can talk to each other they're going to have that capability to automatically have that transit so i can have v-nets all over the place that connected to the hub the v-nets can talk to each other i could actually have v-nets over here because the point of this is what it's going to give me is these hubs with standard well 

they essentially connect to each other over that network and what it's going to give me is this any to any capability so this major location here well it's going up vine express route gateway and then kind of bounces via the site-to-site gateway and can go and get to that location this machine that's 

connected in when it bounces by its gateway could get to any location this site over here can go and get to this v-net because that v-net is connected to that that v-neck can go over to that v-net it's any to any i'm not going to draw all the lines in but any connection be it point to site site to site express route can talk to any other connection can talk to any v-net there's one slightly different path 

i'm drawing all of these bouncing via the hub bouncing via those gateways the express route the site the site the point the site if these are both express rail and i drew this kind of global reach it's inefficient to make them go via the gateway express route global reach enables connectivity just on the raw backbone between different express route circuits so if i have different express route 

circuits connected by a azure virtual wan when they talk to each other they actually won't go via the hub and actually take a more efficient path they will get onto the backbone but then just go straight down so express route to express route while still managed by the azure virtual one in terms of that connectivity they're not going to bounce by the hub it is totally inefficient it doesn't buy me anything they are going to bounce using global 

reach and i'm drawing all of these connections in there are appliances there's a huge slew of different partners that provide appliances that i can put down in my location that will go and integrate with azure virtual web i drew express rail and point to site and site the site as these kind of routing mechanisms within the hub well there are actually now third parties that can actually drop 

nvas into that hub from the marketplace like barracuda has one and then maybe it has a barracuda location over here running a certain type of appliance that can go and connect in and manage that connectivity as well so it is extensible so yes there's there's appliances that i can put in locations that will make it easy to connect to azure virtual wan but now vendors can even put their own appliances up in the hub to maybe use a different 

type of vpn technology or whatever it is also express route if i want to it can do an encryption over that express route it will actually create kind of uh there's a network here it will create a ipsec encrypted tunnel over the express route into the hub so i can even do encryption over express route if i wanted to so there's a huge amount of capability there but it's really just about providing me 

this great connectivity on my environment using that azure backbone and i really pay for it's build on an hourly based on the connection and kind of that that scale unit it requires you can go and look at the pricing page to kind of walk through how i pay for the service i can make these secure so i can have a secured hub what it essentially does if it's a secured hub is it puts azure firewall kind of in here 

and i can pick it on a per hub basis and obviously gives me that in heart security um through the azure firewall so that's it kind of in a nutshell it's designed to really provide that huge scale connectivity between all of the different locations i might have and all of my azure resources it's providing that transit and for any v-nets i have so i hope that was useful if it was and as always please like comment share 

subscribe and until the next video take care you
