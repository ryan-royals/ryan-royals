---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/data-sources-are-evil/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/l8k_cOHep28/maxresdefault.jpg)

hi in this video I'm going to try and convince you that data sources are [Music] [Applause] evil now of course not all data sources are evil I'm talking from the the perspective of a module author especially one that's developing quite a low-level building block type of module such as the ones we have in Azure verified modules in fact the example today has come from some lessons learned from the ash of verif 5 modules project 

so let's start with a look into why data sources are evil from the perspective of a moduled author and then move on to some of the lessons on how an alternative approaches let's dive in let's demonstrate why data sources are evil hopefully by the end of this you will agree with me so we have a terraform data resource what that is doing is providing some dependencies for for the data source so what the first input to the terap dat is the RG name 

data sources are evil cool and we've also got something else that we don't care about so part of that dependency that isn't really person to us and I'll explain what that's for later so this is quite common some people have inputs to data sources that are variables or the results of other things in the dependency graph so let's just put the data source for that Resource Group now um but crucially we're going to make it 

dependent on the output of that so that's we're creating a dependency on a computed value for that resource again very common this will work let's now add a resource now what's quite a simple resource that we can create so if I go resource um Azure RM user assigned identity something like that demo um I'm going to put evil data 

sources much more fun um name something like evil data sources that's fine location now this is going to be the location of the resource Group um Resource Group name is also going to be that so really really simple you'd expect that to work so we init oops ter init that N I can't spell there you go right plan 

uh I always do this think I'd learned by now didn't you I literally just created this for this demo there you go um now I should mention that I have actually pre-created this resource scoup so uh if I bring up this window here oh no I've lost it now I put it in another terminal window I've just pre created the resource Group with um a group create so that does exist you can see that we're just going to read in the 

data source and then it's going to create the resource based on that okay so this is this is going to work I suspect uh hopefully it won't take very long it's created the terraform data resource it's now reading the resource Group and it's done it hooray what's the problem this is the problem whatever dude I'm going to change something that actually has got nothing 

to do with any of these resources however terraform doesn't know that so what happens here is this ah I I was worried that I was worried that it was going to work but actually I just needed to scroll up here we go atrm user assigned identity evil data sources must be replaced why nothing's changed that we care about well 

the reason is because the location is now known after apply now the reason is is because the dependency changed and this data source is dependent on this dependency because we've referenced it here now terraform is not clever enough to know that actually this thing is the only thing that's changed and as such the result and output is going to be consistent right with the resource Group name terraform is not clever enough to know that so what it does is because we're 

using the outputs so of this resource so I something that's been computed so not known till after apply it marks every single dependency in the chain is not known till after apply and your resource will end up being recreated so how do you fix this well don't use data sources what I really mean by that is remove as many dependencies from your chain as possible terraform is really really good at making implicit dependencies between things just by the 

way you can do this but just because you can put a dependency in there does not mean that you should and I think that's the key message just because you can create a dependency does not mean that you should now in that last clip I was being a little unfair to terraform it actually has no knowledge on what the provider is doing with inputs related to outputs all it knows is that some of the inputs to the resource was changing and that means the computed output 

may also change it doesn't know that it will it doesn't know that it won't the problem here is that you've created a dependency to everything following on from that is then not known till after apply and then you get into the problem that we we just experienced so what lessons can we take here as a module author if you want to make your modules robust when you have dependencies take in those dependencies using the simplest form possible as an example if you need a location just take the location as a 

string don't try and be clever and infer it from the resource Group that the caller provided if they want to use a data source to do that they can do that outside of the module because then they have the choice about whether to take the risk of the you know the scenario happening where stuff might get accidentally recreated then they have that choice if you put it inside your module they have no choice and they're affected by it no matter what if you have a dependency on another resource take that in as a resource ID 

it's the simplest way of doing it they are predictable you can use regular Expressions to understand if uh to create validation rules rather to understand if the resource ID is correct so you can then present a sensible error message to the caller of your module really early on and using a simple uh using a simple split function then you can take out the bits of that resource ID that you're that are important to you it's a nice standard way of sharing data between um modules so you might not be 

that good at regular expressions and I I completely hear you they're a bit of a pain so let's have a look at some examples of how we can use a bit of AI to help us create this so if we uh look at this window here you can see that I've got a variable for as an example storage account resource ID now if I just type validation that's going to come up with a suggestion now that isn't particularly good right if you look at that regular expression it's saying and it's saying any one or more of any character Then followed by storage accounts and a slash and then some more stuff afterwards 

which is pretty rubbish so what I suggest we do bring up co-pilot chat and you can see I've asked this question before um I'm going to ask it again though uh because it's now got the context of the correct variable name in there so o it did not work should we do that again yeah okay transient error so it's now saying yeah you can add a validation Rule and it's going to 

say there you go so if we just scroll okay this is much better regular expression it's saying the beginning of the string then it's got to be/ subscriptions then it's got to be a valid guid which is done for us then resource groups then any character apart from a slash then provider storage da da d d d d da right that's a much better regular expression that you can use um and I think if I just click that button it'll add it for me there there you go so you don't have to be a genius um of course you may want test this and 

check that it's right but you know just eyeballing it that looks pretty good to me um and that's how you can use regular Expressions to validate that your input variables are sound and also take dependencies in in the simplest way possible so I hope that was useful if you did find this video um useful please give us a like comment subscribe that would all be much appreciated we are going to be making this recommendation to AVM module authors so you might find 

that data sources for resource groups get removed from your resource modules that you've been using um we apologize I know this might be a breaking change because we might have to make the location uh variable mandatory now we were trying to make it easy for people but it just turns out actually it caused more problems than it appears to solve so it's all part of the learning process um I hope you can bear with us where we make these changes and this is just another reason why we're not quite at V1 at these modules yet we're still going to come up against these things every now and again so yeah let me know uh via 

my feedback via feedback in the comments or drop me a message on LinkedIn if you've got anything that you want to discuss in private but yeah thanks again for watching and see you next time
