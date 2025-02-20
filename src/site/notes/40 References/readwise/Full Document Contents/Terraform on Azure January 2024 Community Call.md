---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-on-azure-january-2024-community-call/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/WooYGjmJuaA/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGFkgZShlMA8=&rs=AOn4CLBmIgU5D9G8dvbnySjrDPPhu2WhoA)

all right well welcome everybody to the January uh terraform and Azure Community call it's our first call of the new year uh as usual if it's your first time we just like to go over this it's nothing crazy here but just make sure to please be respectful uh be a nice person and we will really enjoy your company as long as we all treat each other with respect and uh yeah now first thing I guess point zero 

is Happy New Year everybody uh this is our second full year of the terraform and Azure community so it's really been great to uh get to know everyone and continue to have these Community calls and see people come out um hopefully this year is just more terraforming U more learning and we have a lot of new faces uh these Community calls when we first started them uh we were in 

maybe like the attendance numbers of like 15 to 20 now we're at almost 100 so that's that's really awesome to see and really thank everyone for spreading the word and also just for coming through so let's hope for uh even more U members of the community and uh let's hope that we all continue to grow together uh in our terraform and Azure world and development so as always 

I always like to start with uh the overview uh just to really give the rundown especially for the first timers uh myself and uh some of the there's Mark gray who will sometimes be on here uh the two of us are from a team in Microsoft called the Azure deployments team our real goal is to make sure that Azure is the uh choice for all developers it folks devops Engineers Cloud Architects and really our hope is that we can meet you where you're at 

with a frictionless and really first class experience uh developing on Azure using your tool of choice so our team manages arm templates we manage bicep and we manage terraform and actually we all three of us are on the same page in terms of those product teams uh that we believe that choosing a tool is a bit like going to an ice cream shop just because you like chocolate doesn't mean that you shouldn't have a good chocolate when you're at the ice cream shop and 

just because you like strawberry doesn't mean you can't enjoy a good strawberry uh so whatever your flavor is that you prefer uh our team is really making sure that we support that uh and why Community why did we start this whole thing well there's a number of components uh we always are valuing your feedback and we want to take your feedback through these Community calls and also through conversations uh with all of you and we also want you to feel like you're contributing to the Improvement of your experience uh we found that a huge help for people is 

when they're able to voice their opinion to us and we actually are able to take that and address it and before they felt like oh where is Microsoft and all this are we really caring are we involved uh there's also the importance of getting to talk uh about what you care about there is right there a link uh that you can click uh if you can't click it it's aka.ms a tfcc speakers we welcome uh different Community call speakers and we 

are trying as often as we can to talk as little as possible uh and this community call hopefully will be more of that um and we also want all of you to be up to date with what we have coming down the pipeline so I know that a lot of you have joined this community call but we actually do a lot outside of the community as well here's just a list of this some of the things that we're doing uh if you joined the community already great if you haven't please please make sure to fill 

out that form um and you can also join our slack uh the slack is great and we have some really cool people uh I'll just call out Mark tenderholt aure terraformer uh as some of you may know him as a person who not only has his video on but also is very active uh on the slack and helping people out so join and you can interact with people uh like him there's some other really cool people on the slack who um are there and 

we always try to check that uh every day or two and make sure that we also get to your issues uh again if you want to present at a community call follow that form we do have a blog post uh that we try to update uh we originally called it a bu monthly update we are still attempting to do a bonly update but if you've been keeping track uh we haven't had one since August which goes to show that the holidays are truly a sle uh for getting some things out um we are working on 

that though and we're going to try to get it out very very soon apologies to anyone who's been waiting for it and then we have a YouTube channel uh we have videos in there including one for Azure export for terraform uh we also record the community calls and upload them onto that channel so make sure to follow And subscribe there so that you can uh watch the recordings or any other new video content that comes out and then uh Twitter or X U just go ahead and follow Azure terraform there and you can 

uh learn more about us uh so one last thing um we are actually beginning another round of user research uh and all of you if you're joining this call are users so we want to make sure to get your feedback specifically on the aapi provider if you are using aapi or interested in using aapi uh make sure to scan that QR code and we'll schedule uh some time hopefully with at least a good portion of all of you to talk talk about the a 

API provider we have some I guess I can say in this little Community call we have some new things that we're trying out and we want to definitely get your feedback to make sure that it works for what you're hoping uh to accomplish so give that a scan uh fill out the form and we will uh go ahead and make sure to get in touch with you and that wraps it up for me uh I'm going to hand it over to Jeff uh Jeff why don't you go ahead and introduce yourself and I'll let you take over from 

here sorry stepen can you hear me yep sorry I'm having some I was just having some audio device issues uh okay cool um so are we often running or 

I think so why don't you go ahead and uh start the deck um let me not yeah I should be able to yeah that's cool okay sounds good all right excellent thank you Stephen and uh thank you Mark uh for letting us do this um so my name's Jeff aen um co-founder of the project Karen rimmer is online as well he do some 

demoing um a little bit later um so we first met Mark uh through a another Microsoft colleague uh probably about um six seven months ago maybe might even been a touch more um and uh we we started an open source project called stql uh probably about uh close to two 

years ago um so we myself and kieren and um the other uh co-founder that's involved we're all uh data people I guess from way back as you can probably tell from the gry Harris um and uh but we are also uh spent so the last you know um decade and a bit U living in the cloud engineering 

World um in projects across all three hyperscalers and then a bunch of all cloud and SAS Solutions as well um and we saw as we were starting to get involved in projects and we were starting to get asked to um you know to provide different attestations and um control States for uh for different um Cloud 

providers uh we found that there was no real good way to collect all this information um and to be able to display it and and analyze it um and we sort of thought well why why don't we just use SQL for this and this then became okay well hold on why don't we just use a SE why don't we just use sqls of DSL to do a lot of things that are sort of uh whether it's um you provisioning provisioning um 

ssops uh cspm Etc so this is sort of where where the Genesis for stql came up with so this is a unified analytics and um xops um provisioning de-provisioning uh framework using SQL um so we we're saying here multicloud visibility Automation and operations uh so we'll go more in into what what this product what this project 

is um so we it's an intelligent API client um so it it actually allows us to uh interrogate providers uh open API um inter open API specifications that's essentially our provider interface um so we don't we don't build off of sdks or or anything like that we actually uh take the uh providers open apis spec 

which I'll talk a little bit more about especially with that with respect to Azure um and we map out routes uh SQL routes and SQL methods from that specification um so we have a a a hierarchy provider service resource if you think of your your standard database hary you know You' got database schema table database schema view uh it's very similar in terms terms of the the way we 

look at things we we essentially look at um Cloud providers as data sources um which again you can you can interact with as far as mutating data creating uh Services changing the state of services as well as uh quering the state of them uh so provider service resource the provider would be Azure service would be compute resource would be virtual machines as an example uh then all the methods that we use are are going to be 

SQL methods select insert delete um update uh and then where we can't map a crud method we use exec so things like starting a VM stopping a VM uh attaching a Nick detaching a Nick Etc uh and then every res every resource has Fields um and again these are fields that we get from the open API specification um so we support all the the relational algebra um so that's all 

the set based operations your joins your unions um and we could do some pretty cool things uh as far as that goes we we've essentially built a SQL parer um a full a fully fledged SQL p parer and you know pluggable backends and we'll show some examples of this so what can you use it for uh reporting and Analysis uh so we we do a lot of Consulting work um and we've actually done several 

audits for clients where they've asked they've they've had multicloud Estates or they've had sort of uh complex spraing Estates that had different SAS Solutions involved and we've done uh audits uh where we've generated reports for people in terms of um their Cloud inventory um cspm Cloud uh security posture management that's a uh a really common one um we've worked in a lot of Highly 

regulated Industries um that have a lot of strict controls around the use of public Cloud um so we're but by the way we're both from Australia so um yeah so we're ding in from Australia but yeah we've we've worked on uh projects that uh that have um required you know control um control State at stations and so forth and that this is a use for that uh 

user access management entitlements this is an interesting one uh and we've gotten involved with this in a few different places where people use an IDP like Azure ad like OCTA like for rock like Ping uh what have you and then they'll have a resource provider that could be uh could be Azure could be um OCTA could be GitHub could be be 

whatever um and it's it's sort of difficult to get a list of identities uh the properties for those identities and then what they're entitled to within the estate across all the resource providers and because of because of our ability to join things uh we can actually give these entitlements reports for across all the resource providers that we've got coverage for uh so also things like fops you know which is a big thing um you know a lot of times people have 

spraing Estates and as much as we'd like them to uh to drive everything through one channel which might be terraform um oftentimes we'll have uh we'll have states where oh how did that get there I didn't know that v-net was there where' that come from yeah people people click offs things uh people use CIS and sdks and cdks and um other methods so you end up with you know in the Enterprise you end up with a lot of 

uh spraing Estates so being able to to do some reporting around that and then also within the the IAC devops cops side of things uh we can use we can provision things um so we can provision things using insert statements um we can also do uh you know essentially multicloud provisioning so we can provision identities and then provision applications or uh resource within the same batch uh life cycle Ops 

you know starting stopping attaching detaching uh and so forth uh as well as IC validation this is an interesting one uh so if I have a terraform routine uh we've got some different methods where we can actually go and do some uh some validation that could be for uh compliance or it could be for just uh verification so there's a a method we've got called stq assert which is in our giab action I'll talk a bit more about that later but I'll keep going on um so 

essentially stackl is a self-contained Dev tool um where we can operate Standalone uh we can also operate with a um an external backend database um we have a provider registry which I'll talk about more in a second which is essentially similar to terraform registry this is where we get all of our providers AWS aure Google digital ocean OCTA GitHub you 

know can go on and on um and then we we query the cloud providers um so it's it's relatively simple uh but there's sort of a lot of sophistication inside the the project itself so our provider registry so this is essentially our plugins so our providers uh in like I said instead of them being SDK based they are uh open API based open API 3 based so there are 

open API specifications with some uh syntactic sugar or some extensions um but they're legal open API documents um so this is where we and I I'll show some examples uh so essentially we map out the routes to operations so we say that a select operation for this resource will point you into this particular uh operation ID within the 

specification uh and that can be overloaded as well so for instance you you know Azure has a lot of methods of um you know get something and then there's get by subscription get by Resource Group um so all those things would be the same resource um and the method signature would just route to the appropriate operation so if you said select XXX where uh from 

resource where subscription ID equals something um and Resource Group is equals something we would pick the appropriate uh route or the appropriate operation to map that to um so I'm not sure can I share my screen as well here um Stephen yeah go ahead and share your screen it looks like it's blocked yeah it's great out give me a second let's fix that uh hey Steen it's it's Kieran here as well 

I'm in the same situation I have no way of all the login flows are blocked for me so I've had to join as a guest and I'm totally gr out from present to yeah let me uh fix that real quick give me a sec guys I'll keep I'll keep going in the meantime uh okay so how do we get it um so you download it from the website uh we've got yeah we've got Brew install we've got Cho installed we've got um we've got pip install we've got 

packages in npn npm um so again if you wanted to use whatever method with these are essentially wrappers we've got um so we've got uh wrappers in Python and and node uh as well as just a straight CLI uh We've also got Docker images that that are built uh with stacko in them we've actually got a stack server image that's sort of pushed up to to Docker as well uh we have action in the GitHub Marketplace um so setup stackl is very 

similar to setup terraform uh but we also have uh one called Stu exec and one called stacu assert um so the stack assert one is where I can actually go and uh run queries and look for expected results uh or expected um expected um row counts so like you know I'll show some examples of this letter if I can get the sharings of stuff uh 

going okay how can I use it so uh we've got an interactive command Shell stackl Shell yeah we'll show some examples of this stuff uh we've got stackl exec which I can use in batches like I can use that through GitHub actions or you know any sort of CI routine uh we also have a server that we can run so we can run a uh postris wi protocol server we're not it is not doesn't mean we are 

postris uh but we can we can essentially emulate a postris server um and you can then connect to this with psql or you can connect to it with psychop PG or um any of the post postre protocol clients um we also have the get up actions I mentioned uh which I can use this within pipelines natively you can use this from jupyter notebooks you can use this from powerbi um you can use this from you all your other bi tools because again we've 

got uh we can sort of look to tools like we are a data like we're a normal database even though we're we're actually not um so that's pretty cool uh okay so just before we get in the demo uh there's one other thing if if I can share here uh stepen did you were you able to see if you could share yeah so you you are a presenter I'm not 

sure why it's not letting you share your screen okay maybe because you're sharing maybe I don't know is it maybe let me see if this works let's see if I stop sharing real quick how's that going H still great out only meeting organizers and presenters can share here you are a 

presenter okay that's interesting um so okay so on my thing it says meeting guest interesting so when I look at the attendees it says meeting guest there's no way to like Elevate me in the in the meeting is there uh I think there's a unique link that you would have to join through cuz I don't have an option here that lets you suddenly share your screen right let's see um so yeah I joined the event using 

the link that you gave me okay let's see if this works hold on did that work try sharing something now yes yes yes yes yes perfect awesome awesome awesome hey hey Steve sorry didn't interject could you try the same for myself as well because I'm in exactly the same situation I've been over try so we so we gave I guess they must have done change with teams over the New Year where 

adding you as a presenter is not the same as making you a presenter in the call itself but now we're good so I'll leave it to you sorry for the difficulties everyone no no no it's all it's all good Stephen so uh so just could quickly show that this is our provider registry um and I'll talk about how how we sort of curate things to get in here but essentially uh if we look at our providers um these are our our providers ERS uh if I look at something like 

Azure um and I go into here um you know our providers are essentially just open API documents um but if I go down uh there'll be a components exal resources in here uh somewhere there it is uh which is is what Maps the operations um and if we go down a little bit further there's going to be SQL verbs um so I see select insert update 

delete and they map to an operation uh or to a method and then the method maps to an operation uh and we can also route to um what the appropriate information within the the response is so if you see here like this object key uh we can drill into a a response body and get a particular um a particular field back that's of interest um so and we show a little bit more when we demo stuff but essentially that that is that's the 

plugin so instead of it being code based instead of it being goang based uh it's essentially um the providers are documents and that includes we can embed views in these documents um so that you can have predefined views that can actually simplify uh the output schema for things I'll just quickly talk about the aure provider generation process uh because this is probably of specific interest to you guys um so we have this project 

called stq as your open AP so as you know Azure doesn't uh publish a direct open API schema um you have to use autor rest uh to actually generate um the way same way you generate um you know python Powershell Etc uh sdks so we use uh autor rest um and the Azure rest API specs which 

are Json schemas to generate open API schemas for every service in Azure um so like every every service in Azure and what we've done is we've broken them into this is in our Dev registry we we have got a new provider for Azure coming out very soon but we've we've divided them to as your as your extras as your eyes v as your stack so as your eyes V is like all your um you know data dog and data bricks and um New Relic and so 

forth uh and then um Azure stack is is is everything related to Azure stack um and uh Azure extras is pretty much everything that's sort of non-core and we had to make some sort of judgment calls but aure is sort of all the core Services you know compute storage Cosmos DB um you cognitive Services Etc uh but to get there uh we have we we 

have this project called sto as your open API um where we can actually generate this this sort of a bunch of information you I'll send out all these links afterwards but we end up with a uh a tagged uh specification so we end up with an open API specification for Azure for every one of the services I think these are actually I think we actually push these ones in uh we don't no um but that that's essentially how we get these aure 

specs um and then we have another project uh which is called open API source which we use to actually add that xdq resources bit so that's sort of how we get there it's it's an interesting process but we've got it down to uh it's all automated and like I said with within uh I've generated another the latest as your provider which covers every every single service that uh that Azure has some of them 

might be deprecated by the way too um and it it you know we we can smash that out in a matter of um you know less than a day including all of our tests um so it's pretty cool so anyway look what I'm going to do is I'm going to stop sharing and I'm going to pass the Baton over to Kieran uh take over and show some other stuff 

yeah thank you very thank you very much Jeff um okay guys let me just share my entire screen this is a I spent sorry I spent the first um probably 20 minutes coming and then going back out because I couldn't see the Shar icon so I thought if I log in and do everything I'll be able to share but didn't work so thanks Steve um okay I'm going to share my whole screen here we go entire screen here we go yep Bea okay you're gonna see some yuck stuff first but I'll just go 

over this uh okay cool so uh I'm just going to go um yeah uh we'll just go go for bro here so please interject if stuff just isn't working I can't hear anything right now so assuming that means we're working so um yeah so sweet all all I'm going to demo is just like bootstrap stql server with um with terraform because this I fig this is a terraform group so just go for that if that doesn't work there's one I bed to home earlier which will work 

subject to me doing a little bit of fiddling around so um just uh this is just based purely on the um the Microsoft um you know demo um container Microsoft container instance uh um terraform thing so I've just got a this is just a b 64 encoded um uh certificate you know public whatever certificate um for our um for our uh um for my client my U for my um just for some open SSL 

stuff I've generated so that we can log in to um stql over post wi protocol using Mutual TLS so all going well um now I should be able to just uh my memory not being great this I need to copy and paste whoops have to copy and past Yep this one right here so ter oh well yep I'm just going to have to run that and remember terraform 

apply okay so let's just see if this does work I figure you know let's go for it so just going to create a terraform container instance um it's that UNS un sophisticated I haven't done anything to make this um persistent or bulletproof or anything like that so what this is doing is just creating one with some secret environment variables that're going enable us to talk to various providers I think we'll just keep it um on the straight and narrow if everything works we'll just do a quick query 

against Amazon to prove that we can do this stuff and then that there'll be enough so just creating terraform um sorry just creating a a container instance running stack ql it's just going to spit out um the certificate that I need to include in my local service certificate sorry that I need to include it hey including my local um set up for that to work so I think it is uh let me just let me just go over 

[Music] here okay this is the one okay je my Resource Group K here I'll just call it yep I've got a resource Group that's been created as part of this and I've got [Music] uh got 

a okay okay cool that's easy so then I've got I've got a container instance name a container group name whatever it's called so we say this one so all I want all I'm doing here is I just want to say the startup log it's screwed as that it's in inside the startup log it's going to spit out this uh encoded um this encoded thing here so it's now just a case 

of today the day that everything just whoops everything decides to not work I can't I can't tab between different uh this one here okay so this is all again this is not um private key stuff this is just certificates uh this should give me so now I'll do this this is just some shell script mate seriously 

uh I will run this script it will spit out a connection string for me plus or minus one of the things I need sweet so now I just have to run this I just need to replace one part so this is all just operating on exactly that stuff I just set up with terraform whoops don't want that not now um I just need my fully qualified domain name which was spit out on the terraform 

create and I should be able to just straight up connect to this baby uh if this doesn't work we'll go for the uh we'll go for the backup that I cooked at home earlier cool so here we [Music] go huh all right let's go straight for the one that I back to home Famer I've done something wrong with the um with the setup 

here so that's nazy demo won't work this guy over here I've got one that I backed to home earlier so it's called um slightly different have to run this again so run that again this one's called uh the um prequel you know the fully qualified the main name is a little different oh whoops cpes wouldn't you know it very think I think somebody uh said uh swap one for two or something like 

that I'm not sure if it's in the host name maybe no so that one that one's done it's um someone said that oh yeah yeah oh yeah I see I see me uh yeah okay oh yeah okay this will be yeah give me one second oh I'll just try and join the one I backed I know what you mean and you stuff that up it's 

too late uh just go here yeah uh oh man um Ian I could probably show some other quick stuff just while you're doing that yeah cool do that yeah so uh so what what kieran's trying to show is um so this this is uh we talked about stackl server so we're just building a server in a container instance that that that's um that's listening uh on the 

post protocol which then you could connect to like a bi tool or anything like that but I'll just quickly show you some other quick sort of context while Kieran sort of getting that stuff uh together uh so I'm assuming everyone can see my screen yeah um so I mentioned that we've got um we've got a uh a command shell like an interactive command shell as well as the you know uh the server stuff and uh the exec stuff but so I've just opened a 

command I've downloaded stack binary into uh aure Cloud shell um and I've just run up the stacu interactive command shell um I've got some creds in here for uh for uh AWS as far as as well as for um obviously Azure I'm Mo to Azure so we have the providers I mentioned you show providers if I wanted to say uh say 

registry registry list these are all the providers we've got in the public registry uh as a matter of fact I'm connected to the dev registry so we've got things like Cloud Player digital ocean obviously all the hyperscalers here AWS has your so if I wanted to pull something like let's say I wanted to pull uh data dog I would say redry pole uh data dog um not data dog just as an example 

uh and then if I say show providers I can see now that I've got the data dog provider installed so that's how we get the plugins installed um that's essentially those provider registry that we talk about so then sorry I'm back can everyone hear me yep can hear me yeah yeah you're you're good yep good yeah so um so I 

mentioned about the hary so if I say show uh services in Azure uh this shows me all the services in Azure I can say you know like uh container let's say and I can see all the services that are you know like container um and then I could say something like uh I don't know does any have a favorite service something they want to look at any 

ideas make this interactive my vote's AKs AKs all right okay so I'll say uh let's say AKs right so there's oh so hybrid AKs there should be AKs one as well uh I think because I've got the actually hold on let me do this uh registry pull measure 

again yeah that's better uh there should be an AKs service yeah okay I'm not sure there's a new there's a new provider that um that let me do this let me get out here and let me say 

okay show services and Azure like G is it is it querying based on like the resource type because if it's like the oh no this is correct this is correct it's it's this is correct I just had the wrong provider on I had the okay previous generation provider so you can 

see there's an AKs Service uh I could also say you know uh where U name is equal AKs okay so there's the AKs service so now I can say show uh resources in AKs sorry a Azure AKs and there's all your resources in Azure AKs uh so I've got agent pools manage clusters I don't know do you want to 

pick one to drill into we can say clusters here so manage clusters I go and do this I'm back by the way Jeff I can I can actually connect just finished your I'll finish I'll finish off this but again I've got a resource so I can say Okay describe uh we'll say describe extended um and 

paste describe yeah okay so there's uh there's the fields here um so again this is this comes directly from the specification there's a response body all the gold is in properties uh and I'll show you you can get that stuff out so as a matter of fact I've got here some ones I pre-baked 

earlier uh so I'll just quickly run this query and then it'll get out um so here I'm going to run this is this is not AKs this is just uh virtual machines um but you can see how like there's a properties object properties object has all the gold in it um so I'm just going to run this query which is going to say get me the ID name location and VM size for all the virtual machines and you you can see I've got an in Clause so I've got a a I've got five resource 

groups the beauty of this is we will query all of those asynchronously and bring all the results back uh at the same time so it's intelligent enough to say all right that's actually five different queries um but what I'm going to do is I'm going to make it look like one query I'm going to run them all asynchronously and bring them back and you can see here we're bringing back all of our inventory across all of our resource groups in that list uh in one operation uh and the other thing that's 

cool is because uh because we are um I've got AWS uh creds here again I'm in cloudshell and oops oh yeah I got to do registry poll AWS um I can run a query from yeah I can query my AWS estate from here I can query Google from here query octave from here uh again I haven't installed any 

sdks I haven't installed any all I've done is just say registry pool AWS um had my AWS creds so we use a lot of the our our off is is modeled off of terraform so all the variables and all the terraform off uh you know will work for stackl um that's intentional um but yeah you can see here that that you know we can we can do quite a bit in terms of ad hoc querying so what I'm going to do is I'm going to hand it back to Kieran to 

continue on here yep thanks mate I'm just going to share the entire screen and let's go and uh Daren while you're talking if Jeff you could just help answer some of those questions in the chat for everyone or actually we can just do a Q&A after everybody or all the demos are done so that while we're going yeah cool cool thanks 

guys so um yep okay so I'm just going to go with the with the prebate one I'm not uh if time any I can have a look at the other one because I've actually included secrets for the providers but uh here we go all right so that was a nice illustration before that if we don't have the service certificates all present correct then we don't get to join so now we're joined uh we're just in here I mean some of this you know you're not seeing quite the perfectly Polished everything you like like to see with a actual postgress instance but we can see that we actually do have TLS 

correctly set up here because all credentials are present and correct on both sides now um because we're using container instance what happened before with my preb version was the container just restarted and so generated a new a new server certificate which I didn't have so therefore the one I was using was wrong and we were locked out so that's that's kind of in a way it's nice but just an illustration of um of this how how this demo actually so I'm in here so there shouldn't be any providers so um Jeff probably talked through that 

we actually use um we have this show providers command oh there is one oh wait there is one maybe I pull it for let me just um let me just uh pull another one so I can just do all the commands that even post doesn't support we can still do easily enough over the wire protocol uh let's just pull down the Google provider we should be able to see that okay okay so then if I do again show 

providers I should see that I now have Google and Amazon present no worries so in this particular container instance I've only just included um some um uh credentials only for um for Amazon and that's done like Jeff was just alluding to just purely purely using um like those environment variables that Amazon likes you to use for your CLI and also terraform users as well um we're doing this so intentionally like Jeff said so I just have one nice little prean query 

I'm just going to look at all the um Amazon virtual machines which are you know full disclosure we've created these using our startup credits with um with Amazon and played around with to set things up so I should see a bunch of um um virtual machines ec2 instances sitting in this there we go back so I like Jeff was saying that's just um that's running in in real time uh just using the um the rest API from Amazon which is old school so um you know all 

these different um all these different interfaces have their own uh have their own eccentricities I don't have Google credentials um so I can't issue a query against Google um do we want to get adventurers Jeff and um I can try and um I can try and join my other container instance and uh and then um bang bang a few queries against Google or do you want to just do you want to no it's up it's up to you it's up to you okay give me give me me give me yeah let's just 

give me two minutes guys so I'll demonstrate what I was trying to demonstrate before and if it doesn't I can answer I can answer questions while we're while we're doing this as well too by the way so I've just I've just going through the list here uh so um yeah so there was a lot of services mentioned we've got coverage for all those um does the query run against state or am MOD understanding so it does not run against State these are live queries they're hitting the apis directly um so they are querying the 

estate directly so they're not these aren't State Fall type things so um we're quering the the current uh environment um is it using the arm resource type name convention Okay so we've modeled this directly after uh the arm resource manager so we generate um we generate the the provider 

as I mentioned off autor rest and as your uh rest API specs uh all the control plane is covered so everything I've showed you is all the control plan it's all the resource manager uh we have started to build some data plane services so we are starting to build a as your container registry data plane service which essentially means you can query your container registry with your endpoint um but the rest of them are all sort of arm um resource manager based uh 

what's purposes stack is it just a query so predominantly we're showing queries here we can do a lot of other stuff so we can scaffold an entire environment uh using stackl and we've done that before um so it's a it is a unified analytics and IAC tool so um you know we can use it as a complement to terraform or you can actually use it to uh provis Vision things much like you would do with the cdk so much like people are doing things 

like pulam or other cdk variants where they allow you to have you know python or typescript or JavaScript we're essentially in ssql SDK uh for all the cloud providers so again you can mutate you can query uh I'm just going to rip through these things uh terraform um yeah so the the naming convention yeah we've tried to keep as pure to the open to the rest to the Azure API spec as possible um so uh 

we have our resource names don't come from so whereas terraform can sort of uh you know come up with some pre-form names and things like that we we essentially inherit a lot of our names directly from the API specs um and we try to be as as true to the API as possible uh do you ever run into throttling by arm or AWS management apis so uh there are some things that are 

rate limited uh but most of the queries that we do rate limiting isn't an issue and we've also built a lot of uh backend magic for pagination and and those sort of things as well uh um okay yeah some other things here followup so other clouds the resource schema would conform to whatever platform correct yeah there is no custom schema to learn that's correct so the schemas um the schemas are come from the 

open API specifications for the different providers and in the case where they don't publish one we can derive one through the ways that I talked about um so again the the taxonomy is the same it's just a question of you know like Google of different names for VMS than um than than as your will and so forth sorry uh Kieran I'm gonna hand back to you yeah yeah it's okay so we've got a happy story over here guys so after my earlier 

on bungle I don't know if you've watch but it's just been pretty raw stuff so didn't rehearse any of this but I thought it's worth it's worth a shot I'll just try and be natural and we'll do it so I'll just replay what what we've done here so um I'll just download because now I've started another instance number two and thank you for the kind s pointing out that I didn't have my op SSL config file with the correct server name hence we couldn't log in and further evidence that mitual TLS setup actually works um so then all 

it's it's just like I got no idea what I'm going to query now because I can't you know my memory I'm 45 years old and I never had a great memory when I was in my 20 so I just I just come in here and I I just I know that I remembered you I'll be honest that there is an endpoint sorry we do have a resource called google. compute. instances so I want to see how the hell do I quer it I'm just like oh there's one method here aggregated list which equates to a SQL verb of Select which is what I want to show you guys and hopefully 

impress um and there's one required parameter which is project so I remember we've got a project uh I remember that we also do have um I mean we do have a project called stat demo and I have a service account um shared I'm mounted to I'm not mounted to but I have a service account in a secret environment very well on this container instance so I can probably talk to it I just look at a couple of things here and going okay this is easy I'll just the ID and name from all the um computer instances in my testing 

project and lo and behold yeah I get them back so I think uh we I mean I've just recapitulated the Amazon query I ran before on the other um container instance should work it does uh yep so that one's fine so I've talked to I can talk to Google I can talk to Amazon uh now this is just bleding Edge stuff I didn't use your like you know work identity um um you know object whatever it might be I haven't attached that to 

The Container but I have put in some um Azure uh some Azure environment variables into this container as well so let's just see if I can actually also talk to aure strange as it sounds um you know I haven't even tried talking to um to the to the hosting provider yet so uh let me just see show Services first of all first of all registry we try talk to Microsoft a okay 

um so uh show services in I just want to see I can't remember again what we've got there so wow uh so then there's a lot there so I'll just say show services in as you like and just usual SQL type um whatever you call it matching language hopefully we have something that looks like compute okay right cool 

there's a compute [Music] so I got to spell it right or else not going to work is it so resources is your Compu okay uh so we got virtual machines so I'm going to say show methods in is . compute. virtual machines and see what we got and we'll just try and see that and then I'll be 

done after that um so this is with the latest provider Jeff was just talking about okay uh so I've got one where I can list just by subscription ID so let me virtu machines some describe I'm going to describe this we'll give this one sh then we're out uh okay cool I'm just going to select ID 

and name again let's try that give me one second I'll have to just copy paste my subscription ID [Music] uh subscription ID now I'm going to have to click across to my a console I think I've got one 

open oh God damn it um I do have do have hopefully the subscription ID in here somewhere no give me one second one second I'll just go through the pain go in sign in and we can gra we can just copy paste the subscription ID uh here somewhere cool copy there we go bang 

okay um cool here we go the Moment of Truth can I talk to as your as well as Microsoft sorry as well as um Amazon and Google yep bang There we are so that that name's a bit ugly so we probably use one of our Rex functions um let's uh oh let's let's try let's just try one live I promise this will be the last thing we'll just try and pretty this up so 

um select let's use one of these we just co-opted a bunch of um a bunch of um a bunch of the SQL light and all postgress um so hopefully yeah hopefully this will do it and then uh uh whoops it should be split part name that's IDE y y Al is as pretty OD okay hopefully we get a nice pretty 

looking output now yeah okay so now I'm just you know have I done that right oh yeah they're cl to the same thing so yeah so that that's basically it like if I wanted to be if I was if I wanted to be real sck what we can like Jeff alluded to we can do views and all sorts of stuff and materialized views but because these containers were FAL I thought let's not take the risk I can talk to all three we can run queries that would actually um join uh 

information from all three different providers but that's effectively all I wanted to show today so I'll hand back to Jeff now thanks for tolerating my bungling we got there in the end thanks very much all good yeah so um all right I'm just going to quickly wrap this because I know we're sort of at the end here uh so um let's just do this uh okay so um so where we're at again we've got coverage for multiple different 

providers uh I'll send it send around this pack and some links afterwards um the get up action stuff I'll just quickly uh within five seconds go through that uh so this is where we're using this alongside terraform uh so we're using this stacu assert uh method um and I've baked in some queries in this particular repo where I'm saying check instances check terraform instances run compliance checks so 

essentially this is I think this examples Google we're looking to say is is there buckets that are publicly uh where have an enforced public uh access prevention um and then what we can do is we can bake that into um to a CI workflow here where like if you come down here I've got um I've got a terraform and it Terr validated Terr plan uh and apply and then I run a compliance check using the 

stul assert and this this should actually fail um so I'm saying run that query your expected row count is zero if you get anything else than zero uh um the workflow fails so just some ones that I baked earlier here just you can to show an example um so we can look here and we can say that actually that's expired because I haven't run for a while but essentially yeah like we can run things within uh an actions workflow uh to do 

some compliance and validation um again using this as a compliment ter form okay uh what's next uh we're doing more and more providers we've got a new version of azure that's coming out uh within the next couple days um that's in our Dev registry at the moment uh we're also doing a bunch more work around um uh prepared state ments complex SQL uh we we started a bunch of work around asset and 

transactions where we can actually have a transaction block could potentially span multiple clouds uh including rollback support graph graphql grpc Proto buff okay uh so what you can do uh first of all um you know you can star us that would be awesome um and you know give us your report uh we've got a whole stack of stuff on GitHub um which I'll send around links 

to everything uh here we're looking for queries and use cases you know could be single Cloud could be multicloud um we want you know we want more you more more queries more use cases again we can we've got a A View mechanism where we can actually incorporate um views into our providers so we've got a mechanism that people can contribute those uh things um it'd be really good 

to get some Azure feedback uh from you guys in terms of uh what what you think we've done well with the Azure provider and what's missing where the gaps are uh that would be really good um yeah so I think that's that's pretty much it um so look um I apologies for going minutes over um but yeah stepen I'll I'll hand back to you I think I've answered most the questions in the chat 

as well um so yeah hopefully we we've covered everything off and and I can send the follow-up information to Stephen to to share and happy to answer any questions we've got no time commitments I know you guys might uh we can stick around as long as as you want um so yeah far away if you if you do have questions awesome really appreciate uh the stack ql folks uh as hopefully you've seen uh we really wanted to bring 

in these guys because we think that this can supplement your Cloud native workflows or anything that you're kind of doing multicloud related uh it's not explicitly like a terraform provider um but it is something that we think could be useful uh so glad that they got a chance to kind of show that and hopefully um that was helpful for all of you yeah thanks a lot guys it's uh it's really I'm going to Echo some of my comments in chat but it's uh I think 

your tool is like a perfect tool to literally strap co-pilot on top of um you should check out like custom jet chat gpts because they do have open aai actions like if you use the open AI spec that could jump into your remote service which might uh strap a chat interface on this and it I don't know it could open a lot of more doors so just yeah I've actually I've looked at um so one of the things we've got is we're part because we're part of the we we're part of a 

accelerator and with that we got we got a whole stack of credits like we literally are sitting on like $150,000 worth of azure credits and then we've got a bunch of open open AI credits and um so forth and uh so we we started to look a little bit at at open API open AI sorry open AI um and it's a relatively straightforward provider to to build uh but again it's it's sort of uh you know you would have to sort of Coach it to 

get the responses that you want in terms of tabular responses um instead of you know textual uh chat type responses but it's something that we're looking at what we did think of doing and this is sort of what we're looking at in terms of using uh say you know chat GPT or or those sort of tools probably probably that one because we've got you open AI credits but is things like uh respond um interpretation uh and again I'm staggered that terraform is not doing 

this already where they'll send you back the you know 403 or 401 or you know whatever response uh code and and message which is going to be directly from the provider whereas oftentimes what I want is just tell me what's wrong um and you know I could take the same response and say you know I'm doing terraform apply I'm getting and I give it to cat GPT oh right okay what you need to do is do this this and this and this like well okay what in interform just tell me that so um so 

it's like we're looking to sort of build stuff like that in the core where it's like instead of just sending people back a native HTTP response uh status message you know uh is can we put that in in plain English and say okay right what you've done here is you've you've tried to create this without that um and so that's sort of where we're looking to probably incorporate like the the AI 

type stuff a little bit but again we use this stuff so what's pretty cool uh in the latest build of chat GPT so the the latest release cck GPT plus I can't remember what month it is is that it knows about STL um because it's cwed and it understands it you can actually ask it to generate you a stu query to query you know as your VM in es and it will give you a proper stackl um grammar um so yeah and you can just ask 

it you on the latest build of chat GPT so it's it can actually help you write queries and and do things like that um but the queries themselves are pretty intuitive and you know where where there is complexity because obviously the Json response bodies can get quite gnarly you know that like it's you know again in aure you bury All the Gold in prop in a properties object um but we have a lot of we have a 

lot of like like Karen said we we expose all the built-in functions or most of the built-in functions from you know sqlite and uh postris within our grammar so you can lift stuff up so I can use like Json extract I think I showed some examples in the the previous uh thing where I can I can lift things I can pull things out of an object I can also do things like uh if you've got um arrays 

you we've got um the table valued functions where we can turn an array into into rows um this is really common with a lot of the IM type responses so we can do all kinds of cool stuff um with that to sort of again get you to a simplified output um for reporting or analysis um and that's just part you know of all the stuff we've sort of baked into it yeah yeah I guess I guess I was thinking more of like you like 

because you can go to chat GPT and be like hey write a t-sql query for this business case right yeah since it since chat GPT knows about you know your SQL language right you could potentially say hey within this context you know um tell me tell me how many virtual machines you know are oversized over provisioned or something like that or you know don't have tags or something like that and then you mean within to to actually run the query for 

you is that what you mean to actually run the query right so but that would require like integrate like there's different ways you could implement this right but I mean the most basic is a custom chat GPT that has open AI actions that could invoke your like you'd have to do some kind of thing on the back end like to register like the Azure subscriptions and the AWS accounts and stuff but like the issue yeah yeah exactly so there'd be there'd have to be some sort of out of bound off unless you just go full 

boore co-pilot and build your own co-pilot um but that would be kind of the North Star in my mind is like um use chat GPT to generate the SQL then execute it in my environment and then respond back the results across Azure and AWS and and all the things right that would be you you kind of built the engine right but like um to really scale to like um I think a broader audience right of operators right people that aren't necessarily Hands-On Tech um that 

I mean you it would open so many so many Avenues to use cases yeah that's that's that's a pretty cool idea um I think we've we've we've sort of looked at we've built some higher order stuff like we've actually got and like we could literally sit sit here two hours and show you everything we've done uh and still probably not have enough time but we've we've actually built some other stuff that's we've built like order products we've got a an a monitor product uh with which build a prototype on we've actually built it for GitHub um 

as like a open source monitor sort of thing and we use materialized views and and then send slack and Discord messages to say yeah yep U Mark has just starred the ripo or you know uh Steven's just you know followed the org or anything like that and so we we've sort of built these things where they're not necessarily you don't have to be a SQL operator to use them you know you can you can actually um you you can you can use them without knowing SQL but and and 

also things like you know whether it's select bot or or anything like that where uh similar sort of concept to what you talk about the copal it is ask a natural language question which gets translated into a query um and it could even be complex like you know how many VMS do I have across uh Google Azure and and AWS just give me a rough count yeah and it's like as long as it knows uh as long as it knows some entry points so 

like your subscription uh your res your subscription your um you know potentially if you've got Google Google's very hierarchical in terms of projects and folders things like that but assuming you you're at the sort of org level uh and and likewise with AWS if if You' got your creds so so sort of things like that I think yeah it's like how can we make it a little bit more um non-sql friendly but again it's you we're hardcore SQL guys like we've 

been I've been you know I I literally started SQL server in uh 6.5 you know in in the um in the late 90s that that was my indoctrination to to databases and SQL and I've just been a sequel fanatic ever since and that's why when we're we're asked to run all these reports and we're having to run all this CLI stuff and you run this clii for this and run this clii for this and 

then do this and it's like why can't we just use SQL for this stuff yeah know it's all data um and that's that was sort of you know like so we we we don't want a shy away like We want more SQL because we're just you know Fanatics right um yeah yeah I mean expert users dropping a sequel you know people that just want to you know talk to Alexa and ask it what ask her what time it is and stuff like that then you're like what am I spending on you know Azure VMS or what 

I'm you know uh what are my high list me off the most expensive resource groups that I have you know let me know um just silly questions like that um for somebody to probe their environment where that that would reduce you know the time that would take for somebody to go actually look that stuff up you know that yeah yeah it's I'm going to jump in real quick sorry guys I have a meeting I need to run to but I'm going to leave this open for 

yall I'm not going to end it for everyone so I trust you guys can behave like adults and leave once the time comes um but one thing I'll say Jeff Karen if people want to contact you how should they contact you for questions um and I won't even stay around for the answer but yeah so what what what I'll do is I'll send you I'll send you Stephen I'll send you some information and then you can distribute it yeah sounds good cool yeah thanks mate okay all right I I gotta drop two but yeah 

cool stuff just yeah look I really appreciate appreciate everyone's time yeah and like I said we're happy to stick around and ask answer more questions there's a really interesting one about um non-ga features in Azure uh and azed API so we've looked a bit at the AZ API terraform provider um so yeah you could use this as a comp ment to help you develop asure API um or as at API routines a sorry uh 

yeah a API sorry I'm bilingual here um so yeah you could you could query essentially we are a direct representation of the API so if you want to know Fields uh and you want to know response bodies uh you can get that stuff directly from us and then you know go ahead and model your um asure uh API uh terraform routines uh that's a that's actually good potential use case as a complement yeah so again this is 

just a Dev tool um I can install it right along terraform right alongside terraform essentially using the same off as terraform uh run queries you know um as a complement so yeah so is there any anyone else have any other other sort of questions that that they wanted to ask thoughts comments 

anything there was something in the chat about using this as a replacement for terraform um I don't know if you already addressed that mate because I dropped in and out a couple of times trying to get the scen yeah I S I sort of I I responded I said look it can be a compliment to terraform but you could also do imperative I just like the cdks do like your pamies and your CD do um you know we would cover all the routes so again it's a Swiss army knife 

you know we we see it probably more as a complement to terraform like something I can use with terraform but you know if I needed to do simple scaffolding stuff that it was easier to do imperative imperatively yeah yeah I think I think from the the technial standpoint just the long form answer is that like we don't you know we don't really want to compete you know in that space but we do have um strategy for um full life cycle management of multic cloud resources 

using SQL but it's a bit of a it's a bit of a process so the the process is that we're going to implement Aries uh treating for those um SQL people that um people that are interested in um transactions and roll back it's like the canonical um algorithm for like recovery and isolation um in transactions and so we just effectively treat all of the cloud providers that we talked to as somewhat unreliable um hard Diss and 

then do do our transaction semantics on top of that uh eventually um we'd have to then build that first and then from there some some um ability to to maintain um to maintain the the history of those transactions themselves and uh do full life cycle management so that's probably 12 to 24 months away but something we're shooting for but um take some time yep cool anyone else have any any other 

questions someone ask anything else I I'll like I said I'll send around to Stephen um you know the pack that we've done and some of the links and things like that and how if you want to contact us how you contact us um we would love to work closer with Microsoft um we've um yeah we we need probably um I guess some feedback and 

things like that in terms of especially with our uh new provider that's about to be released so yeah um okay cool uh so look if there's no other questions we can probably uh drop off and I'll send details to how you can get in touch but I really appreciate everyone's time and thank you very much and enjoy the rest of your day thanks everyone bye
