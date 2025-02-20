---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/dry-vs-wet-in-terraform-when-elegance-makes-your-code-a-mess/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/dwQRv9Vh6Kk/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGFggZShbMA8=&rs=AOn4CLCGlvUnZBQb4y1jn0CO8U2JIfaTxw)

hello and welcome back to the Azure terraformer today I have a code review from one of my code ninjas Abdul the way these code reviews work is basically if you want me to review your code all you have to do is open a PR on GitHub and assign it to me it might help to ping me on Discord to let me know that it's in my Hopper but that's pretty much all that you got to do now if you are part of the code ninja program you get priority access to my code reviews which means you go to the front of the line so 

if you'd like to have these old eyes looking at your terraform code doesn't even have to be Azure terraform code but I mean that is kind of the name of the channel here but I've done code reviews on this channel for terraform providers I haven't even looked at i' I've never even used them before right the same principles of module design apply no matter what platform that you're targeting now of course there may be certain provider specific nuances that 

you might want to be aware of or platform specific idiosyncrasies which are always helpful but I'll do what I can I've got quite a bit of experience under on my belt with Azure AWS and gcp so if you throw anything my way within either of those wheelhouses I think we'll be all right but of course my favorite cloud is azure so there's always going to be a special place in my heart for Azure terraformer code so anyways uh if you're interested in that smash that join button and hop on the 

Azure terraformer Train by joining as a code ninja um you'll get access to our Dojo within the Azure terraformer Discord um where we can work more closely together um and of course you'll get Priority Access to these uh code reviews in the future so check that out anyways let's get down to what Abdul's working on here so here's the pull request he says I hope you're doing well when you have some time could you please review this code oh he's so polite Abdul 

that guy what a what a great guy I've been working on it and provide any feedback or Improvement specifically I'm trying to use the four each indexes in terraform I'm dealing with a scenario where the relationship between scope identity and role is many to many and I'm struggling to figure out the best candidate for the for each index I need to ensure the index remains unique across different assignments and doesn't result in duplicates H interesting 

any insights or suggestions would be greatly appreciated thanks in advance for your help Abdul Abdul what a polite guy G whiz like if if I were to get poll requests that have that kind of a description uh every day I would die a happy man let me tell you like how sweet is that um anyways so yeah let's get started here um let me pop over into the files changed here and let's go go take 

a look okay so first of all I'm seeing some some dirty here I got a lock file I don't like this here we go so so we definitely want to have lock files added to the git ignore um there is a kind of standard git ignore that I use um which you know you want to hit anything that's got a do you know basically star star sl. terraform star so that's going to catch any of these 

like wacky lock files or anything like that um you want to capture starstar sl. terraform slashstar so basically anything in that hidden terraform directory you don't want to check that in as well um so yeah def get G ignore etiquette is a thing folks you got to make sure um you set up your G ignore files properly um the yeah not bad not 

bad I mean he actually wrote pretty decent documentation um doesn't even it looks like it's handcrafted like he's not even using um terraformed doxs you know um I I I got to I got to give him props for that like uh props yeah so you definitely want to you know use terraform docks to generate the boiler plate like may maybe he did but 

this this this does not look like terraform docs output to me um of course it is highly customizable so it's I guess it's possible but this definitely does not smell like uh you know like like regular um output you know um it just feels kind of handcrafted now I'm I'm pausing because it you know he has like these requirements which 

almost I almost never see anybody like hand that hand rolls their own documentation I I almost this this is one of those things that people always admit right is like the provider and terraform versions right um I love that he's using terraform 1.9 that's my favorite version uh because it has the input variable validation oh my gosh it's an amazing thing oh and he's on 4.0 that's awesome so sick um way to go okay uh I'm I'm I'm done I'm done looking to read me so we 

have this custom roll definition thing in here um which so this looks like a very generic module we got looks like a lot of um basically this this is what I would consider like a pass through right like I'm I like when you see a resource and every single attribute is VAR Bar Bar Bar Bar Bar like basically it's like okay we we we are pretty much just doing a pass 

through wrapper um the question is are we adding any value right um are we adding constraints that the resource by itself doesn't have like right off the bat you can see here we're locking this to um I why would we even pass in a single scope um actually you know probably going to have to go rtfm on this roll 

roll definition here just to see what this scope thing is I I think that scope would be a single string so I'm not even sure why it would uh so there's an assignable Scopes which is an array uh that's interesting so oh yeah here we go so scope yeah so the scope is a single attribute um which is what he's doing here um I'm not sure ah so assignable Scopes is an array and it looks like 

maybe the idea was like we would eventually support this assignable scope oh I see what's I would see what's happening here so he is passing in this assignable Scopes but he's just taking index zero and dropping it into the scope now is is that even how it's supposed to work right [Music] um the scope at which the role definition applies to 

okay so you could pass in like a specific subscription okay so a a role definition in Azure is basically like a template for permissions that you would like to create role assignments with right so if you want to have a custom set of permissions you know to dictate what users can can't do you create a role 

definition and then when you want to link that to identities you create a role assignment so it looks like this scope here is basically saying um all right I want this role definition to be accessible within the following scope like I I guess we could set this at I mean potentially Management Group level yep we got man we could set it at a management group or at a subscription level and presumably that would mean that the role definition is not even going to show up as as an option um if 

you're not in the subscription or if you're not if you're in a if you're in a subscription that's not in this Management Group right um it is recommended to use the first entry of the signable Scopes and changing this forces a new resource to be created okay so that kind of coincides with the logic that we're seeing here so the recommendation is you pass in this collection of assignable Scopes and you take the first index here 

okay yeah makes sense um so in that sense this logic even though it's very kind of seem seemingly redundant right I mean he is adding a little bit of value in that that that that that uh recommended approach is basically you're he's forcing you to do that which I like I like that a lot 

so at first blush this just appeared like a resource wrapper module but this is adding some value albeit meager value um but still some value so I do like that um now the question you know this begs the question is this value right enough to justify creating a module for this right cuz I mean you look at this there's not a lot going on 

in this module like it's it's essentially a resource rapper so I don't know I'm kind of I'm kind of airing I'm kind I'm kind of w wafering I think we'll get into this but you know um let let me just leave some comments here so yeah I mean the main benefit of this is that um he does simplify the interface of the module the module has a simpler interface you don't have to pass 

a scope and an assignable Scopes um you pass in the assignable Scopes and you know he does the work of figuring all the stuff out for you so you know I'm torn I'm torn I'm absolutely torn um I I do want to point out so at this point I could go either way right I mean uh I'm I'm I'm definitely leaning towards no module but 

I'm I'm I'm just going to put this in the parking lot and I'll revisit this later um okay that's fine this so if he's presumably if he's going to do the module that's fine um he's presumably doing 1.9 um because uh let me just shut down like some of these files that I've already looked at I I don't need to see this I don't need to see this um 

and I don't you see this so presumably he's actually using 1.9 not sure if he is so Ro definition it so his module does add some additional value in terms of the input validation okay not not sure if the resource doesn't do that but we'll see um might be valuable I I I don't like how the names are completely redundant like why do we 

have Ro definition uh naming I'm just going to call this like a naming nit so in in this type of situation I I typically recommend like don't be Captain redundant right um if the name of the module is custom roll definition module then when I instantiate this thing I know it's a role definition right which means all of the input variables don't need to have the 

Redundant prefix of Ro definition the mere fact that that attribute this name attribute is being set on a module block that is a source which has a source of custom Ro definition implies that the name is the name of the role definition right that's implicit so I don't need to do that um and I would probably repeat that everywhere here right 

um yeah so this is this is a 1.9 Nick right and I don't think there's definitive guidance on this yet but like if you're already using 1.9 like why hardcode nasty regular Expressions inside of this condition statement when you could just as easily declare a local and have it very easy to spot right so that would be 

my recommendation I'm still evolving my my viewpoint on this so I could be convinced otherwise however for me this is a more of a readability thing right um just just look at this right like is that easy to read like looking at this regx string that's embedded in a can regx like uh nested you know function uh expression not super easy to read if 

you're if we're really being honest with each other right so let me let me type this up yeah so my current thinking is for common validation variables or expressions or logic I that I only use in validation blocks if I'm drawing a dependency on the 1.9 

on on terraform 1.9.0 then I should just go all the way and like use it right which means I can stop doing kind of painful things like creating ridiculously nasty um condition Expressions right because I can now store parts of that expression in in a different location right now this is a this is a kind of this is 

a line that I that I have to that I often have to walk right it's a judgment call right when should I hardcode something in line versus when should I bust it out as a local and put it in a separate file right because you'll see me do this um and make this recommendation on my channel a lot I'll be like no no no no no don't everything doesn't need to be a local you know cuz cuz now you're just kind of like indirecting everywhere right and as a developer as the as as a future author 

right I have to go look at your code and I can't just like look at look at one line and know what it does now I have to go look at that line and then go find every L single local wherever the hell it is in your in your source code in order to like do the math in my head that sucks right so you definitely have to walk a line about how much in Direction you want to do but I think in this case um it def the the benefit of getting this nasty regular expression 

out of this nested function Block in this conditional statement outweighs you know the potential complexity of indirection because number one it's a single variable it's it's a regular expression regular two regular expressions are already nasty as you know AF right so like the any anytime you want somebody to go look at a regular expression make sure that's all that they're looking looking at because 

their mind will explode okay so that that that would be my recommendation here reasoning there we go okay I I think you know the same feedback for all of these things the assignable SC so the prefix is always going to be the same I'm not going to repeat myself um yeah I guess you always have to have at least one makes sense so now 

this okay so his permissions block notice we have we're making good use of an object with optionals right um that uh that default to empty strings so basically we're we're going to default empty strings um if we don't specify this which I like that so that means I can create a permissions object I can have only action on it or I can only 

have not actions on it or you know yada yada y you know keep going right so this allows me to kind of random access which attributes on this object that I want to set I think this is an excellent use of uh you know an object so I I'm in full support of this now the validation um what are we doing here so we're saying if the length of my actions is greater 

than zero or the length of my data actions is greater than zero okay so I'm basically saying I have to at least have a data action or I have to have um a action okay that's fine that's fine I like it I I'm I'm just going to say I I'll give positive feedback here right nice use of optional I like 

it good job and then what do we got here we got um good good logic good logic I like it it's minimize that 

okay so now this now we're getting into the actual stuff that he's working on oh boy wow this is like getting a little a little wild and crazy um very interesting um what are we doing here so we have some data sources so our back custom rolls roll definition Azure rback custom roles 

that's the name of the object so we're we're referencing Ro definition and we're referencing this local so custom roll resource lock administrator I don't know what this is but we're getting a reference to this 

thing this thing has to exist already 

yeah now my the okay I'm I just now figured out what's going on here it's it's a lot more complex than it really needs to be um and that's because he's using an an unstable um iterator okay he's actually building a map um in line on the for each meta argument which sent my brain into a tizzy let me 

tell you okay you probably saw that okay so I would I would highly recommend using stable iterator references essentially do not hardcode for expressions on The Meta 

argument itself count or for each create a local and reference it often times you need to reuse the local on multiple resource ource data 

source blocks anyway does that make sense right so so basically what I'm what I'm saying is he is right here he is dynamically creating a map so that he can do a for each and he's just getting the name uh basically he has a list of names he's turning it into a map to make it a 

little bit more stable but he is doing an inline for expression to generate the map what all I'm saying is okay you want to use four each that's cool you want to use a list because it's less for boast than a map that's also cool but don't use an an an embedded expression an embedded an embedded four expression just create a local that encapsulate that for expression and say 

you know I don't know role Maps or something like that like he could literally do it on line eight here you know or line line nine right after line eight right yeah I mean that that that pretty much takes care of it I think I'm going to have to leave this open so now let's see if this pattern continues so we're in a different so this is a different data source okay so we're on arbac 

identities I think we just got arbac custom roles so we got 80 groups and so these look like display names Azure owner Azure reader and then we got service principles these look like these look like well-known service principles that he's that he has and then he's got Azure ad users okay okay okay so we are 

bifurcating um based on the identity type that we're using here um which I and I'm I'm I'm jumping ahead but like this this local is going to be used to iterate over the ad the corresponding Azure ad resource or data source right so go get me the groups you know for these groups go give me the service principles for these service principles right yada yada yada okay I I get that I don't 

see the corresponding user equivalent may maybe he just decided not to do that is this being used maybe not in this file Okay so we're we're trying to get you know a these data sources together 

okay so now we have these Management Group which I don't like what is so Azure and management groups okay so we're getting for each two set like these management groups and each. value I mean this is okay to me right I mean that that's not as bad as an as like an inline for expression so I'm okay with with that um it's interesting he's using two 

set here and a four expression previously so um I'm not sure why why he's going with this approach versus the inline four expression over here um I'll ask that question why are you doing two set here then you are using in line for 

expressions for groups and SPS azureum subscriptions okay so now roll assignment definitions oh boy 

oh boy so we're trying to create Ro assignment definitions roll assignments for the management groups these locals are used by the Azure rback roll assignments. TF Azure rback roll 

I'm very confused by these oh mod mod rback R assign this naming convention is a little foreign to me like I don't know if I like prefixing data in locals and mod you know I don't it it just seems confusing to me I've never seen this before um of course I've seen people use locals um but like I don't know it seems 

like I'm not I'm not sure what to call it but like unnecessarily tied to the typing the type of blocks right you see a lot of people like organize their code based off of the functionality right like identity stuff goes into one thing like scope stuff goes into scope stuff Management Group stuff goes into Management Group stuff but like prefix it with like the either the the sole or 

dominant block type seems a little bit much to me um not a big fan also in introducing a prefix like this makes makes it hard to read because now we got this nice consistent naming Convention of A- arback is Jagged right like I can't I can't it was even hard for me as my eyes wandered across this 

vertical space to like key in on like this mod ASU rback roll assignments because like I was looking for auu rback but like it it kind of bounces back and forth horizontally so have having if you're going to have prefixes like that you know try and keep them with consistent like lengths like he's done with A- rback right that is a consistent length you will not get 

Jagged uh like I guess ordered F lists of files here right um some something to think about so we're basic looks like we're like defining the the blocks as locals and then we're probably going to iterate over this when we go create rooll assignments I'm guessing yeah so um definitely remove orphan 

code I'm going to minimiz yeah more orphan code Okay C so this is my module so I'm referencing my local module for my custom roll definition and I'm setting the 

Scopes so the scope is going to my management so I have to access oh that's fun so I have to access the data. aurm Management Group mg using this key otive does that so does that map to any of these like Keys 

here oh oh it's probably up in the management groups oh yeah here we go so we have this well oh yeah yeah so we're this so this is our data source for our Management Group so here's like uh I would expect oinv to be in there what where is it where the hell is that Azure RM Management Group mg m G ventive like where is 

that that that that must be a key somewhere yeah something's jacked up here like I'm not sure I guess shouldn't shouldn't this have it appears to be 

referenced explicitly yeah H interesting seems kind of jacked up okay so I'm down to my modu so we have all these 

locals I'm I'm down to my modules let's see let's see what's going on this is all just boilerplate I I don't really need to look at that boiler plate okay I don't need to look at that so remove orphan code don't like orphan code I don't want to look at it it's a waste of my time okay so now we have mg assignments so here he is 

trying to for each again using like a avoid using un unstable um iterator references IE a nested for expression it's not so great so cuz the key right the key presumably is going to going to have to match 

something so what are what are we iterating over we're iterating over our local collection and we want to create the I and the assignment so what what is the I so that's the index so we have an index 0 1 2 3 and then the assignment object 

itself yeah not sure why we would do that I I don't know what this is is this is it is this like a so this is somebody else's module I have to go look at this now I don't know whose module this is 

browse modules presumably this is what oh see we're hitting we're hitting my 

we're hitting my knowledge of hcp cloud so this must be some private module that he has um Cloud monkey you know I love it Cloud so this is some private module um I presume this is some private module repository in your hcp Cloud okay and now what we're doing so I don't know 

what this role is I mean okay it's a role assignment so presumably right I know what a role assignment does right like a roll assignment has a scope and a principle right a name and an ID like uh let's let's let's go roll assignment okay 

so I mean this is this is what we're looking at right now clearly we're doing a a custom roll assignment okay so this appears let me cancel this so this thing appears to be doing this module appears to be creating [Music] 

roll that you created yeah and I I think that's what's happening here so the role definition ID each roll definition type so if if it's if the roll 

definition type is custom roll then get the role definition ID if not use null if the RO definition type is a built-in roll then use the name okay and so presumably on mg roll assignments I got to go look at that mg roll assignments uh sometimes I'm going to use the built-in roll okay and a name built-in roll name okay built-in 

built-in built-in they're all builtin okay they're all built in but presumably he's going to want to do both built in and custom rooll definitions that's what I'm guessing is about to go happen right may maybe that's what maybe that's what he's trying to show here right 

so he's trying to create a custom roll resource lock so this is a custom roll definition with the scope of some Management Group and blah blah blah blah these are the actions okay so presumably you want to create many custom roll definitions 

okay yeah so I think I think I get I I probably should go review what he said again so actually it looks like the orphan code that I ignored I don't know I I'm I'm I'm uncertain if he wants me to look at the this commented out code cuz it really seems like it this is all stemming from either using built-in or custom 

rooll definitions at the Management Group level because I'm only seeing a rooll assignment at the Management Group level that's that's what this is right we're creating role assignments at the Management Group level and we are basically the indexer I is going to be a number it's going to be the integer of that item's index within 

that list uh you know which is mg roll assignments right so it seems like he's trying to merge two lists together that are heterogeneous right one of those lists is going to be currently it's just a bunch of built-in it's just a bunch of built-in rol and then presumably another list is 

going to be a bunch of custom roles and he wants to kind of zip those all together and just have one iteration across these mg assignments yeah but he wants to have a unique index 

yeah it's hard to say like what I mean a roll assignment the primary key of A rooll assignment is a combination of the scope the role definition name and the principle 

that's it now I think what he's trying to do is he doesn't want to accidentally create duplicate rooll assignments within the same scope for the same user for the same I'm sorry for the same identity you know here's the principle for the same 

scope with the same rooll definition now in this case it's it's like a built-in roll right so I think the easiest thing to do and and this is going to take probably some pretty pretty nasty refactoring [Music] um I I uh yeah I I think what he should do is I would I would 

split um first of all like what is the point of iterating off of this collection I mean does it does it make you feel better that you're iterating over a hardcoded collection of 

objects right do you see what's happening here like he's going through all this work to try and make some fancy iteration right but he's essentially in this file he's essentially hardcoded the the the structure of the role assignments so like why even iterate if if you're okay with having a 

block that's an object in an array then why aren't you okay with a block that is your module that just is a single instance of your module that and you legitimately just pass in these values like what what's the difference okay that would be that would be one thing that I would say 

um is is like a critique of the design like why why make it complex so basically what I'm saying is iteration on top of on top top of that point right of like if we're if 

we're let me save this if we're if we're hardcoding it here right like we're literally hardcoding the objects here I mean I I could do a search and replace and replace every curly with a module definition okay now there's really no difference uh between constructing hardcoded objects and constructing hardcoded module blocks and 

then at all other other than the hardcoded module blocks is easier to read easier to maintain but less elegant so maybe as developers like we feel like like we're lesser of a developer because we go the easy way and it it doesn't feel dry enough right but we got to remember in 

infrastructures code we got to optimize for readability maintainability right flexibility like being able to change things without having everything tightly coupled together so if you're trying to couple things together for the sole purpose of iterating in an elegant fashion just so you can patch yourself on the back and say wow I I that is isn't that slick I use that iterator I I I don't copy pasta 

you are copying pasta right it it it almost feels like we're we're at the HCL Olympics right and and it's really just about proving how awesome we are at HCL rather than like maintaining the infrastructures code or or rather than like creating highly maintainable highly readable like infrastructures code so that's my take right now and could we come up with a way to 

iterate yeah yeah I I think I think I think we could but my recommendation is to like get that out of your head like don't even iterate right you're you're not iterating you you are unless unless what he's trying to tell me is like I want to eventually remove this object block yeah unless he says Mark I want to 

eventually remove this hard-coded object block object array and and iterate in some other way right and dynamically create the objects based on role definitions which I don't think I I think what he really wants to do is he has some built-in roles and he wants to be able to have flexibility to assign built-in roles to certain management groups to certain 

identities within certain management groups and he wants to be able to assign certain custom rooll definitions to certain identities within the context of certain management groups I I don't think you need to go through an iteration process to get that done I think I think the iteration process is actually hurting you # unpopular opinion I guess we'll find out anyways um I think that's it I think 

that's it for me um that that wraps up this code review um what do you think do do you agree with my take on um you know this where where are we on this uh this uh essentially logic this is this code is logically equivalent with just a bunch of module blocks for roll assignments right so like why go through the hassle of constructing these hardcoded object 

blocks why not just create individual module blocks and and move on with life that's my take what do you think let me know in the comments below am am I stupid am I a genius am I somewhere in between let me know um keeping it like keeping it simple stupid that's my motto you know um interesting take let's uh you know we we'll see what Abdul has to say about my response here 

um and uh yeah let me know what you think in the comments below anyways that's it uh for this code review this is the Azure terraformer signing off [Music]
