---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/troublesome-tuples-and-how-to-compare-collection-values/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/HS8c33raZ1U/maxresdefault.jpg)

I've got a little brain teaser for you today do we think that this output will be true or false have you got it yet find out in a [Music] [Applause] minute welcome back today we're going to be talking about the type system in terraform if you hadn't already guessed by the intro this all started a discussion in 

the Asher verified modules project and there was a thread posted on one of the internal teams channels from John and then a few people chipped in say thanks to Jared Jason and Cesar for their inputs to this and it uncovered some really really useful things and really interesting things as well which we're going to talk about today things like the default types that terraform uses for literals in the code and the best way to you use conditions for collection values so we're going to have a bit of a gold rule thing again 

later later on when we find out a little bit more about it so stick around for that I love how the as verified modules project is bringing like-minded people together and uncovering these idiosyncrasies in terraform and we all working together to kind of create a better terraform environment so yeah I really love the project and thanks to everyone for their commitment and inputs we're going to look at some real world applications to this as well it's not all Theory so back to the original point of constructing a request body using merge 

on objects um how do how do we do that effectively when talking about collection values such as lists sets that sort of thing so back to that question let's see what the answer is and why hi here we are again in Visual Studio code where we're going to answer that question is our list string equal to empty list Okay so we've also I've also added didn't list any in here for reasons that 

I'll come on to you later so good old terminal terone plan what do we think apparently it's not an empty list why the hell is that um so this confused me a little bit as well and it was thanks to Jared's kind of intuition on on the thread I was just been talking about where he pointed out that actually behind the scenes we're talking about types here 

here so to add a bit more detail in here let's look at the type of list string and that is an explicit list string and the default is that but when we compare list string to that we get false why is that so let's just have a look at terraform console I think the first thing to do is use the type function uh bar. list string 

that is a list of string as you'd expect okay so what about if I go type of an empty list ah so that's a tuple or Tuple I never know how to say that word but anyway it's not the same type so you can't compare those two things so technically in a type in a strongly typed programming language those two things are not the same so I'm sure if you used python or something that you know JavaScript or something that didn't really care it 

would be happy with that but we're using terraform is ultimately type based so when we compare var. list string to that we get false okay so how can we fix that if I go like that does that work it's also false that's really confusing so why is that why is that false first of all to find the answer to that we have to look at the type of to 

of that uh value to list and that uh I've got that wrong there you go and the issue is that when we're using uh literals and stuff like this it automatically assigns the type Dynamic to the value to the members of that collection and a and a list of dynamic is not the same as a list of strings this is really interesting because terraform has a strongly typed variable 

system for its input so you can say this is a list of objects with this exact schema and be really really confident about that as soon as you break into using locals or literals in your code you have much much less control over what the type system is and therefore you cannot compare them with the equals equals just doesn't work you can't be absolutely sure that it's going to give you the result you want with string value vales well not just strings with 

atomic values so number string bull that kind of thing you can do that because there's not really uh there's not any ambiguity into the type so again if we if we get a ter from console if I go type and I put empty string it's going to say string right it's going to say string so um interesting what happens if I put type null oops Dynamic okay there you go um so 

for for Atomic values for primitive types whatever you want to call them you can make the com you can make the comparison so you can use the equals equals so how do we do it with collection values well with collection values what we've got to do is we've got to use the length function um we've got to go if we wanted to say is it empty or not got to do that and that will work if 

it's a tuple if it's a list if it's um a list of any type okay so let's have a look at that now let's exit my telephone console go telephone plan is empty list is true okay so let's just uh that works with list of any right that that's also going to be fine as as would expect so we change that to is empty list which terone plan that is also true so let's 

just try some other types uh variable um empty map um type is map uh for any doesn't really matter and the default is empty okay bar empty map you go let's see I mean technically I need to rename the variable rename the output cuz it's empty list but hey it's still true I'm 

just going to call it is empty just to avoid confusion so let's talk a little bit about two PS now this is a definition of one I've got a variable of a twole which is a value with a string a string and a bull okay and that can be that can be null so if I go terraform plan that's fine it understands it terraform console I go v.2 uh it says it's null okay if I go type of of bar. tle it should give me 

it's a tuple with those values okay so tle can be null that's fine can we have a two pool to be empty let's have a look no we can't the default value is not compatible with the variable's type constraint okay so can we have null null and null that's the default value yes we 

can okay so now it's got our T value so important lesson ts are not like lists in that they can be empty they are either null or they are values of the type specified in the Tuple schema so that's okay we can we can do that so let's go back and put this back to some values so let's say that's a string that's a string and that's a bull so let's have a look at that so A B and false is our Tuple value so let's see 

what happens when we go back in here so that's a valid value so r. Tuple is a and false can we convert that to a list let's have a look yes we can but look what it's done it has changed the Boolean to a string because we all members all collections all values in a collection of a list have to be of the same type in a tupol you can have basically any type you like 

in whatever order but the tupol has to be that or nothing you can't just add stuff on so list and tups are somewhat interchangeable as long as there is an implicit type conversion between the tup schema and The List member that Mak sense it's a bit complicated but let's show you you an example now of something where that doesn't work and because terraform can't convert implicitly the the me MERS of the twool right so I'm going to comment 

that out and I'm Al and then I'm going to exit this and I'm going to delete this because I've got my other complex variable here which is a little bit more complicated and this is really important because terraform seems to assign the Tuple type to things if it hasn't got anything else so I've got a a variable Tuple two and it's a it's a tuple and the first value in the tupo is an object with a F object where the value of Fizz 

is a string yeah so we've got object we got Fu equals object we got Fizz equals string and then next in the two pool is another object and bar equals number so here is oops I to delete that here is a default value for that t so you should be able to see that we've got F object Fizz string equal a then we've got another one with baral 4 42 okay so it's 

a pretty complic complex data structure uh so let's have a look at that well it's happy with it and I can go v.2 P two and yeah that gives me that can I convert that to a list let's have a look no it can't because this Eric happens a lot and actually is one of the issues that's been raised on um the Azure the Azure regions module 

that I maintained by by the Azure terraform himself Mark inal and we got this error because um it cannot convert a tupo to a list of any single type that means that what it's saying is it can't this and this have to be the same type for it to be valid list and they can't be implicitly converted in a way that satisfies that so you do watch out for that Golden Rule I guess is to try and add two list two set two map type 

functions inside your locals to try and be as explicit as you can with the types that terraform is using because otherwise you might run into this stuff behind the scenes so I promised you a real world example this is simulating what you might do if you're using aapi and constructing the properties bag for a resource in this scenario I've got a notional variable called extensions which which is a list of string I then 

have my properties which I'm I'd normally be sending to the resource um and I'm using a merge function so these are the standard properties that I want to always put in and this is an optional property uh where I'm saying if our extensions is equal to an empty list even though we know that's now that's not an empty list that's a tupo then put null I don't want you to include it however if if it's not then add this extra add this extra a bit in so what I 

what I want is for it not to include this baz attribute at all when I when in this configuration when that is empty however as we know it's going to and you can see I've just uh run a terraform Plan before so if I just do a terraform plan again it's actually included that and I don't want it to and that actually can be problematic when you're dealing with data um there is a very real difference between null uh there can be a real difference between null and an empty um list or an empty yeah this 

would be in Jon an empty list so what can we do to fix that and this is really really interesting because actually it works fine one way around um but what we should do as we know we should use the length function so in here we should but length of our extensions is not equal to or if it does equal zero oops then we want null if not do that so 

that subtle change means that we don't get it and that's correctly done the output because it's excluded that so let's just test that the other way so let's just put a value in there um and run that again and you can see that it now correctly constructs the output because we have used the correct logic and we've obeyed the Golden Rule which is if we've got collection values and we want to use conditions on them 

then use length hopefully that kind of solidifies in a more real way uh how you might use this in the real world when writing your modules now let's wrap this up so let's wrap up what I think has been a really really interesting Journey Through the terraform type system let's summarize some of the key takeaways the first is if you need to find out if a collection value is empty or not do not use the literal empty list 

or empty set denomination because behind the scenes terraform will think that that is a tle it's also doesn't you're not able to specify the type of the element of that list so if you try and compare a a list of string variable and you want to see if it's empty or not if you just put even if you put two list function and then put the empty list you'll be comparing a list of strings to listed Dynamics and that will always say false the go rule is to use the length L function as 

pointed out by Jared internally on our chat so thanks for that the next one is two pools converting into lists so we've learned that two pools can be either be null or they have to have a value you can't just they're not like lists in that you can just find out how um you can't just add values onto the end they they're a specific fixed structure now they can be converted into lists where you can do list type operations on them such as add 

another member but they can only be converted to lists if there is if there's an implicit type conversion available for each member of the Tuple now I showed you an example where a simple example where that's fine you can convert a bull to a string and therefore it could convert um a tupo with non-matching types to a list with matching types because of the implicit conversion so instead of the Boolean 

value false we got a string that said false however that only gets you so far because as soon as you get into more complex data structures it's likely that you'll hit up against this situation where terraform is unable to perform that implicit type conversion and then you'll get the error that's unable to convert into a single type so again the guidance that I can give you is wherever possible in your terraform code use the two list two set whatever functions to try and steer 

terraform down the road of creating the right type behind the scenes in the first place do that as early as possible to avoid the errors that you've seen today so one of the things that is not is not in terraform at the moment but I think would be really cool is type assertions for locals so this I don't know if anyone else thinks this is a good idea let me know in the comments below if you think this is useful but if we look here if we have a local at the moment you can say my 

local equals what we think is an empty list but it's not actually it's a twole so what would be cool is if we used a type system like maybe they're using go and you could put my local Dot and then you could say list string that would enable you to tell terraform specifically what type this local had and therefore would make your life a lot easier I would love to have this feature in terraform if you think 

it's interesting too let me know as always um please give us a like and a subscribe if you like the content and want to support what I do love to hear what you have to say in the discussion below take care and I will see you next time
