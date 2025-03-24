---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/building-terraform-providers-part-1-setting-up-your-environment/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/0Smlan-qBJA/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGFIgLyh_MA8=&rs=AOn4CLAG8Ba466ZnxclVmHChsvkkzC6b5g)

well hello this is supposed to be live it's live I it looks live to me let's out in a couple of minutes when uh YouTube tells us that we're not really live yeah anyway welcome hello Melissa how 

you doing hello I am doing great I'm excited to be here today and to learn about terraform and go although we may not get to terraform today so this is the intro to the intro yeah that's absolutely true so what do we want to do and I think this is kind of an important thing but you have a project and what is your project so I like to Tinker with robots and I am working on a maybe demo for Hashi comp 

that involves robotss and right now um other members of the team kareim and Bruno are also working on this project with me as well as you but I've got this little robot and I would like to make it work to navigate a course that is still to be built but we we can learn a lot just getting the robot to move it all and I thought maybe since we have multiple of these robots careform provider might come in handy that 

different robots too way so of course like not all robots can be the same but the one we're working with today is the um white one I showed first nice I think the sounds sounds pretty good so what we're going to do or what we're going to attempt to do is we're going to build a terraform provider a custom terraform provider and in this series we're going to teach you how to do that but also we appreciate that a lot of folks don't necessarily program go so let's let's 

dig into this very very quickly into this well what is a a terraform provider so I'm going to show you some example code of a terraform provider and it looks like this now you're probably looking at this and thinking oh dear what have I let myself into but we we're gonna kind of yeah we're gonna kind of look at this so a terraform provider works like this so you if anybody's never built a terraform provider but they' used teror 

form they're probably used to seeing something like this which is in its absolute simplest kind of setup a very very basic resource now the the way that terraform works is under the hood when you run the the terraform binary it will attempt to load a plug-in which which can understand what this resource is it can understand the properties of the resource and it can then translate that into API calls and 

the way that it does the translation is you build a a plugin now the the plugins are all kind of Standalone that they're not distributed with terraform they're distributed in in the registry but predominantly you've got to use go as as a programming language for this and and when I've taught plug-in development before a lot of people kind of come unstuck on this now do you have any idea on how to program go 

not really um I'm classically trained in in development but I haven't really touched it for a while I'd say I learned C and C++ Java uh Python and stuff along the way there were there were like 10 to 20 other languages that they forced down us uh at University but that was quite a while ago so I hear that go is similar to C so I'm not completely going to be lost and generally if you're fluent in a language you can pick it up within a few days 

but no this is brand brand new to me brand new to me and I think that's a cool thing and and I think you're absolutely right and one of the beauties of go as a language is that I do think it is quite easy to to pick up so a lot of folks hit this terraform provider thing and they're like well how do I you mean I got to learn program and go it's not that bad we are going to cover everything we're gonna cover the the sort of the absolute basics of of Provider composition we're going to cover the the kind of the the elements 

of how you you write you kind of write your own provider so this is a a resource here um and all of the detail inside of there and looking at data sources and and and and all of the different bits and pieces on how you can kind of write custom um diffs and and and all sorts of stuff like that and we'll do that over a series of weeks and this today what we're going to kind of I don't think we'll get to any of this but we're going to run through some go so I'm going to teach you how to program go well I'm going to teach we're going to 

set up your environment first and then we're going to to to to program sun go I I have a bit of unfortunate news for you in that we're being asked by Tracy for an intro to who you are now I know Tracy knows you but the rest of the streamers may not can you help us out is is this because I've had a haircut Maybe 

all right I am Eric V and I am a at happy that is uh that's not true at all I'm I'm um I'm I'm Nick Jackson I'm a developer advoc hash Corp I've been working here for about what like seven years or something now and yeah i' I've been programming go for a while um probably I I don't know like I I'm I'm really terrible at kind of doing the the 

maths on these things but like 7 years plus maybe 2 years plus maybe 3 years I don't know like for for a while so since go was in it sort of infancy at least 10 years I am not an expert in in programming go and I I would never profess to be I am dangerous enough to be able to do stuff and and I think that's the thing that I love about go and that that with a little bit of knowledge you can you can do dangerous things and and 

that's exactly what we're going to try to do here so I mean dangerous things love it yeah right um so yeah let's Jump On In I think I think this sounds good to me um all right and and well this is going to be great so first things first so what as I said what we're going to do to just to recap we we kind of want to go through this we're going to try and do this convers style we're going to kind 

of do a little bit of teaching hopefully you'll learn a lot and and if folks have questions as we're going through this please throw them in the chat I will do my very best to to kind of keep my eye on those things but I think we're going to be fine and and if anybody wants to troll Us in the in the chat then you know feel free I'm I'm I'm I'm I'm absolutely fine with that as well but we do we do have our bear with me Community guidelines 

tldr be an awesome person welcoming professional and just just be awesome so any questions you have feel free get them in the chat answer them we'll we'll we'll do our very best to to kind of run through these things are you good to go Melissa are you are you feeling confident are you ready I am ready I'm not feeling confident but I'm confident that you are with me and you will help me so okay is going to be fine now first thing first do you want to do you want 

to do you want to share your screen because we're we're going to have to I've got everything running on my computer are you I think I can share my screen we will uh we will get there right let's see here entire screen let's go literally no pun pun intended that I will I will bump off the screen streamyard screen so that I don't give everybody the Eternal screen of death 

all right I assume we're starting with go we are so the first thing we're going to have to do is we need to install go so if you um go over to go dodev let me look at that and could you could you zoom me up about uh four clicks on command plus about 200 would be perfect thank you so much so we 

um so you need to install go so go uh is has a as a kind of an introduction um it it has a a distribution for pretty much anything that's relevant in today you can uh install it for for Mac Linux Windows like all sorts I think there's even an install for IBM Model Z mainframes like it literally will will install like anywhere which is which is awesome right the the nice thing about that is I use 

my most of the day I use kind of Windows I um specifically when doing streaming and stuff like that you're obviously using a Mac so yes we we can actually we're fine with this we will be able to share code and we'll be able to collaborate and and and do that and actually even do cross compilation which which is one of the beauties of the language so the first step is to to basically just download things and install things so the um are you on one of the M1 Macs or um 

this is an iMac I don't think so so I think we should be you're on one of the the intels Intel Max perfect okay so first things first um could you install there the the package so if you install the package well if you if you click on that we'll we'll set you through this and um and we'll we'll walk you through that all right it is here awesome so the there's a number of different ways to to 

kind of in for the installer uh if you're installing on a Mac I I find that the package installer is is is the best it um it'll kind of set everything up and it'll sort of put put everything where it needs to to kind of go if if you're using uh Linux or if using Windows there's there's an executable installer uh for Linux um package managers like you know you can use packet managers but uh I think if you use brew as well you can install go with Brew I'm not sure about apt I generally 

just um download the package and install because I I don't necessarily want things to be continually changing uh I think this is kind of the key thing that sort of like the language changes I tend to make those decisions on when I want to upgrade to the next version of the language myself rather than when the latest version gets pushed there's there's a debate we can have on that whether that's the right or the wrong approach but that's what works for me so we we'll kind of we'll leave that up to 

you however you do that so if you double click that and get that installed all right go through those Everybody Must Have go yeah I think this is fine type your password uh that that isn't starred there we can see that on the internet well if that's the case then then you've got me I'm pretty sure that's not the 

case so so the installer is going through and it's setting that up and um it'll just take a couple of minutes so if you're using um an M1 based Mac then you would obviously you download the the Arm based installer Windows you can install the the axi also if you're using wsl2 or something like that inside of windows then you can use the the Linux packages and and yeah if if you're running this on an IB Model Z then well 

there is a yeah yeah I think you got to pull a fork but so we're we're just waiting for for that to finish um it's taking a minute it'll be fine yeah all right look at that we're done sure all right perfect so now that's installed so let's uh can you open up a terminal let's just check that that is 

is oh hey got some yeah let's go and uh you well let's just try this I think you might have to open up a brand new terminal because I'm not sure the path's updated but if just type go space version uh okay yeah so yeah open up a new a new terminal window and it'll um okay those variables for the paths and stuff 

yep there we go new terminal where did you go terminal not there let's see command space and then terminal is I I'm I'm I'm horrible Mac User I genuinely Uh I that is atrocious so we're going to fix that right now yeah maybe five or 

six clicks on that one better uh yeah a couple more couple more please yeah that'll be perfect now so let's just try that again Go version all right that so so this is good so we're Step One is done we have we have go go installed now whilst we could build uh everything we can use just some like a text editor really I 

mean you don't even have to use anything like Vim or or or something like that we we'll probably use vs code I I quite like vs code because of the collaboration and we'll kind of set that up because I think that's an important part of of kind of learning something as well being able to have that sort of collaboration is is useful um we we could use Vim but then we we we'll probably have to have an entire episode on on how to exit Vim I actually know them well enough so it 

would not take me an entire episode for what is Works to learn how to exit I I I I I lie not that I swear there are servers out there on the internet from years and years and years ago which still have Vim sessions of buying open one because I I genuinely did not know how to how to uh to to use this thing all right but we're good so the next step is we want to install Visual Studio code and um you know whether you Visual Studio code or jet brains 

actually is is great and has a has a great um collaboration environment as well in there uh or or if you just want to use Vim you know you can use Vim the you can run the language Sero in in almost anything now like I think this is a good tool it's a free tool it's uh it it's it's very well supported with the community so I'm I'm kind of this is what we we can use so if you download that and we'll get that installed and then we'll install a a couple of extensions as well all right that sounds 

good I might already have it installed but I'm sure it needs to be updated because it's been a while I think the last time I installed it was actually in support of the Hashi Craft demo for a long gone Hashi comp um oh but I mean that was a that was that was a while yeah okay okay so assume we just gonna unzip 

all this good stuff yeah figure out I think it is I'm just look at my on a different screen which is I can see I think you can just drag that into your applications folder yeah and oh Visual Studio code is already in use what oh you already got it opened where uh so 

man oh sure not oh there we go well I mean if it's up that didn't quit it so there we go all right awesome get it [Music] updated all right yes so this is all installed so in the next step if you can just maximize that for me and again can we to the uh yes 

perfect uh if you go over to the the the left hand side you see the the the Rubik Cube with The the missing the missing block yeah so what we we're going to install is the the go extension so if you just type go in there and then that will it's from the official go team so it's just the top one there if you can hit install on there and what this is going to do is this is going to enable the language server to enable sing like 

auto complete and um inspection and also some of the the the varying tools uh I don't think we want to do that right now so just kind of Hit the the little Xbox there but uh okay and and yeah so this is going to be be essential we'll we'll also actually we might as well install the um the terraform extension whilst we are here so that's the terraform extension from 

hash cob and that that again enables things like language server integration syntax highlighting and all sorts of stuff like that uh I assume it's this one yeah yeah yeah the community one's dope as well like this uh but this is the the official one which includes the language server and the language server actually works with the plugin so to to be able to get um you know property help and and auto completion you can actually get that from Custom plugins as well which is going to be nice later 

on all right so we are good so we have our development environment set up and this is all we're going to need for the moment to to to kind of um start building the Tero provider but I think the the key thing is that like we kind of explaining earlier on the terone providers are built using go so let's teach you some some go so where do you start when you you you want to learn go now there are excellent books 

out there and um Bill Kennedy and and book and Bill Kennedy also has an amazing course on on go and and their their YouTube channel for art and Labs which I I I heartly recommend you you subscribe to but the the go kind of tutorial which is on the the go.d website is is actually really good at introducing to the basics of syntax and some of the things that you will you'll 

come across and I will you know I'm going to make a little I'll make a little bet that if we go through the go tutorial and we get everything working in here then that will be almost all the information that you need to actually build your own terraform providers and and we can do that okay in in about I don't know what is it like a 17 slides or something so uh go.d let me I've got link here for any folks that want to play 

along but we we have the tour so if you go to tour of go and that's that's it and if you can I can read that but maybe we go up one one one size for the for the folks at home just in case all right all right 

brilliant so the we we can kind of let's let's skip through the the first few few steps here so what you want to do is you want to skip through until you get to to packages and then we'll kind of start digging into this okay go playground next lesson all right Packaging C perfect right 

now so in go you you build everything as is a package now a a package is something which is is kind of well you can have external packages so things that you import but you can also have packages which are local which are basically just another folder inside of your your your source code so package main here yeah well yeah 

package main is a special package so package main is is the entry point so what what what you have here is package Main and then uh Let's ignore the the import for now but then you see Funk main so Funk main is the the entry point for the application so when an application starts it will run the code inside of funk main so if you do if you had this in a file called packages. go and then you did g run packages. go go 

would look for the main package which it would find here and it'll then execute the main function now what it's doing is it's going to print line my favorite number is blah so print line is a function on the format package so a separate separate package and yeah that's right so you see that there 

you've got import format and we've also got import math Rand now which is where I assume this guy comes in here that's right yeah now both both both of these here are standard packages so that they're part of the the standard Library if it was a a kind of an external package it's generally going to be prefixed with a VCS so you're going to see it as like gitlab.com or or github.com or something along those lines if it's a a kind of 

um a local package again you will you'll see that with the the name of your whatever your your kind of your your module is and we we'll kind of dig into that later but we'll we'll kind of look at that so for now that funk main we're going to format. print line and format. print line takes a number of arguments so in go the the kind of the types of this is is is named it would be 

classified as veric in in that it is a number n number of arguments and we can specify and it'll basically just print each of those onto a line and separated by space so it'll do my favorite number space and then it's going to do a a random number so uh actually an integer so int n it's going to do a random number between zero and 10 so if you you can actually hit the 

run the Run button down the bottom there and we'll see there it printed out so it's it's printed out for you my random uh my favorite number is one now if you if you run that again you will see they three yeah and and if you keep pressing it it will keep generating random numbers and keep printing printing stuff out so in the basics that is it's not the most simple go program that 

you could have written like absolutely hello world is that thing but this is more useful example it shows you how to introduce packages and things next let's let's let's look at where we where we are next okay we're going to Imports right so we I kind of jumped ahead of myself previously but you can kind of see here that the if you don't import things like format go will will kind of complain 

now the the the the sort of the the IDE setup so what you set up in terms of uh the the extension inside of vs code and in exactly the same way as if you're using as say any of the the the Integrations for Vim or emac or or um uh jet brains intell inell I can't remember what it's called the the go go ID from from intell when generally when you press 

control save it will automatically import that um but but they have to be imported so any package that you use you have to import and you only when you're referencing a package you always goand yes thank you so much um you only kind of use the the final sort of suffix there so you you wouldn't kind of reference Inn which is a a function inside of the 

the Rand package by using math. Rand you just use the the last one so it uses Rand so let's let's let's go on to the the next the next step here exported names right so this is um generally kind of what we were just kind of talking about so we we we kind 

of the the name of the package as it's exported is is referenced at the top of package main now you can override this so for example say I have a math Rand and I also have you've got your own random package which is in your own Library Melissa then you you have a clash you can't use both of those at once so what you need to do is you need to to kind of override the name and so for example if you just type on line five uh if you 

just call it uh type before the the first speech mark there R&D oh sorry um so it's uh it would be R&D space speechmark math Rand so like that uh yeah slash r n d that's it oh so you don't need the the first speech mark there either right so what you've just 

done there is you've just changed the name of the the import path so we instead of doing um rand. Inn oh sorry uh I've gone ahead of myself here so can you change math. Pi here go down there and if you change this to to now 

r&d. inn1 I think that's supposed to be caps isn't it yes that's correct and then if you run this so this this works right so what we've just done is we've just renamed an import and and you will see this in go code but that's that's ultimately what what's going on so let's just refresh your browser let's go back to the to the 

exercise and then let's kind of explain a very core concept of goal which which I think trips a lot of people up who are not necessarily used to it as as a language and um is it not gonna do it reset here we go oh there we go okay the other reset yes right so let's let's just run this it's goingon to break doesn't work exactly right so the the reason that it 

doesn't work is because if you look there we've got math.pi now math. Pi Pi is is lower lowercase so go uses convention so in a in a lot of languages you will have the concept of private and public for for example in Java you've got private classes you've got public classes generally a private class can't be consumed outside of the particular package and that you do that by denoting 

a class with the a specific instruction I to say the generally the keyword private now in go go does away with any of that you you won't find any of those types of complex object orientis what go does is it uses convention anything a function which is defined with which starts with an uppercase letter is classified as exported and 

that means it can be consumed outside of the package anything that is defined with lowercase is not exported and that means that it can't be consumed now so that's not just functions that are that is also variables constants um interfaces like pretty much everything when we get on the struts you'll see it's kind of there as well but just remember that that convention is um uppercase exported lower case not 

exported so we're good there right let's move on moving on okay functions right so so here we have a function def uh definition now a a function in go is something which is Standalone it's not attached to a a strut or an an object I 

suppose that would be a method and we will get under that confusing which is definitely confusing part number two for anybody who's never programmed go but a function has a number of different parameters and you define it like it so we have here a function called add the convention is that you have the parameter name so we have a parameter called X the parameter type this is an INT or an integer and parameter y now whenever you 

see INT in go int is is basically an alias for either int32 or int64 it depends on what the what your processor architecture is most people are dealing with 64 bit processes these days but you know not always the case if you're using an older Raspberry Pi or something like that it's definitely 32-bit but for for kind of convenience go also has this Alias which which basically defines int to be whatever the 

the kind of the architecture of the machine that's compiling the Cod is that's pretty cool yeah it it just kind of makes Mo for most part you can kind of forget about it you you don't necessarily need to to kind of worry about um the the specifics for the most part now calling a function again you can see that here in line 10 so we're just calling add uh we're going to add the the sort of the the answer to the life of universe and everything to to the 

unluckiest number in the in the world and uh if you hit run there you'll you'll kind of see the answer so the way that that works is if we kind of Trace that back add 42 to 13 you can see there on line six we are returning X+ y now the return type in go has to be explicitly typed and you can see there on line five at the very end of the bracket we have we have int so 

we're returning a type integer and that's that's that's a basic function like when we get into the the terraform provider you you'll see a lot of this um but it's it's pretty straightforward uh let's let's let's have a look at the the next example here more functions all righty so okay so this is just a syntactic sugar so the difference 

between this example and the previous example is that on the previous example we had X space int y space int now in in go it it allows you to kind of do some syntactic sugar so if the parameters are the same in a kind of a chain you only need to define the last the last instance so you know here we we've got X comma Y in that that means that both X and Y our integers if if x was a string obviously we couldn't write 

a so we'd have to explicitly write X string y int but it it's just a a nice bit of um syntactic sugar so the the next let's a look at the the next example because I think this is is is one of my one of my favorite features of um of GH so go has the the concept of 

multiple return parameters now not a lot of kind of languages uh enable you allow you to do this like a lot of the time that if you want to kind of return multiple sort of um M multiple instances of something from a function you've got to kind of encapsulate it in a in a structure with with go you you don't have to do that you can Define that a function or a method indeed can can return 

multiple uh multiple parameters so here we we've got this swap function and the swap function is going to take two strings X and Y and it is going to return those strings in the opposite order this is a a really common pattern in go most of the time when you see this pattern I mean I think you will see multiple returns but one of the the most common patterns you will see abs absolutely everywhere is the the convention go 

where you will have a return a thing comma error and we we'll see that a lot when we're building the terraform provider but it's is sort of very conven it's a sort of very go standard idiom which actually right enables you to write really good kind of code if if you kind of do all of that error checking all the way down the line it kind of forces you into a mentality in a pattern which I actually quite like I really hated the first time I did it but I actually quite like it after 10 years 

[Laughter] so all right we are getting there so next named return values like I'm on the fence I did not know that uh shantu I'm neither a pearl or a python programmer but uh I definitely appreciate this as a pattern I'm kind of 

um from a c c Java um yeah I I appreciate this right so what what you can actually kind of um do also is Define named return parameters and I'm not 100% certain I like doing this I think it's it's useful in the sense that sometimes you want to kind of give 

a hint to the the consumer of your function what you are returning like what the thing does but the the kind of the naked return here I I always find a little bit um awkward to read now what what we're doing here is if you look at line five you see you have X comma Y and in so we could have written this which 

would have just been Funk split sum int Open Bracket int comma int but instead what we're doing is we're we're defining these named return parameters X and Y now the difference is if you look down there on line eight we're not returning anything now that's because we are setting the named return parameters on line six and seven so if we do a little if you run this 

you'll see see this working so we should get the uh the answers there okay now delete line seven and I've never done this in a while but I'm I'm hoping that my knowledge is good enough that this should give you an error it doesn't all right that's even worse [Laughter] so you've got a named parameter you 

haven't set one of the values there and it it's just returned you the default for which for an inur is is uh is zero and go I don't specifically like using naked returns I [Music] um you you do see them there are uses there's kind of definitely a purpose for it but I I like doing things explicitly but if you ever see this this is what you can do let's let's let's let's move along I assume here you could do 

like or something like that yeah 100% yeah if you hit run there that should that'll work yeah it doesn't um it doesn't mind if you use named named parameters you can you can still uh you can you can still use you don't have to use a naked return you can actually do um explicit like I I think it it is fine line right like I I think helping people to to kind of 

understand what your function is is doing what it's returning when it just has int it's like what int um yeah because there's no name for the thing that's being returned but actually we'll we'll kind of see when we look at comments and stuff like that that that we can kind of solve a lot of these problems just by writing good inline documentation for stuff and and all of that gets picked up by the the um the language server so we we're generally going to be 

okay okay variables variables now so variables are you can Define them in in a in in a couple of different ways the the kind of this you can be sort of specifying here we're specifying VAR so VAR is a keyword which which enables you to Define a variable or variables as you will see on line five we've got three different variables 

there C Python and Java now the type of those are all booleans so we we've defined three variables all of type Boolean and we we haven't set a value of those but because a um a Bool is is a value type so it it must have an initial value it's it's going to be defined in all of those up initially to to be false uh 

which is the default value for bu now on line8 again you can see there that we are defining v i in so you you can define a variable outside of an application uh outside of a block so for example outside of a function my bad line five that is global to the package and that's an important concept Global to the package not the 

file and on line eight we're defining something which is local to the function so you couldn't use I outside of funk main now if you if you run that it's it's going to kind of give you the the initial values which will be um zero false false false yep and and that's kind of how you set that up let's um let's go on to 

the the next example and we'll we'll kind of see how you can set those with with some initial values so very very similar to to what you we we kind of saw earlier on now we're we're defining two variables I and J the type is in integer but now we're setting the values and we we're using this convenience where we can set the value and we're going to set it to 1 comma 2 so we're going to set I to 1 and 

J to 2 and then on line eight what you can see is variable now we don't have the type here but you see that we're setting Java sorry where with C python Java we're going to set C to True python to false booleans and we're going set Java to no 

exclamation mark what that will actually do under the under the the sort of the hood is it will create three variables python C and Java C and python will be Boolean and Java will be a string because the the compiler has has inferred based on what the value it's going to be set the the kind of the type you don't have to explicitly Define the the type of a of a of a variable it's it's optional in some 

instances it's useful but generally in go whenever you're kind of creating a variable and you're assigning it a value most of the time I would say 99% of the time you will see that the the actual type is is emitted because the the type is defined through inference of when the compiler kind of assigns it and there we go but you know everything works so print line will will actually take any it'll attempt to to 

print anything which is um stringle short variable definitions I think you you kind of see these more often then then you will see the VAR keyword so for example we've there on line on line six we have VAR IJ int1 two we could actually drop the int from this but um what 

uh what we could also have done is we we could have written this as I colon equals 1 J colon equals 2 and they would have to be on separate lines now the the kind of the colon equals is a specific operator you'll find in go which assigns a value but it also creates an instance of the variable so you can kind of think of the colon as replacement for the keyword VAR this this kind of line seven syntax 

is is what you will see uh a lot of the time and again they're on line line eight there you know the the compiler is smart enough to to understand that that when it creates a type of variable it can do so by the initial value that's insigned like it's a I think it makes it very nice and and kind of easy to to read let's let's 

uh have a look at this so we're we're getting there and literally I promise you this this stuff here that we're learning is going to be enough to build that terraform provider for that robot in the next the next episode okay it'll be easy okay types so you've got uh a number of different 

types here so they're Boolean obviously is a is a primitive um true or false you have uh uint 64 so that's a 64bit unsigned integer so a value between zero and uh whatever the the max size of uh a 64-bit Inger is which I'm not trying to do that in my head um and then of course uh complex which is a a type which I think is very specific to to go but it 

allows you to handle like really really big numbers so which kind of go beyond and when you're dealing with complex types it's it's not a primitive it's it's it's a it's kind of a an object more so so let's let's run that code and let's let's just have a look at this okay okay so you can you can kind of see um the the kind of the complex 

type because it's a it's a it's I would say like an object as such it's its representation is is string based so it's it's representing that there is uh what does it say uh 2 + 3 I uh okay yeah so it's resolving that you don't find complex types used very often they when you do need them as I say they're they're there but more 

often than not what you're dealing with are things like bites um strings the two are different uh but but sort of castable convertible between booleans integers unsigned integers and and things like that most of the time as well you don't necessarily have to kind of explaining earlier you don't really need to worry too much about whether something is uh a 64-bit or a 32-bit that there are 

sort of definitive reasons why you sometimes you do need to care but um I think for what we're doing we we might need to care I think it depends on on um on on how the the package that enables us to communicate the robot but we most of the time int you in stuff like that okay I assume this here is just a shortcut for the type of this variable 

that's correct yeah so um yeah yeah so string formatting so I didn't explain this so um before we were using format. print Line Print line basically just attempts to convert anything that you put any any parameter you put into the print line function to a string and then will'll just print print the concatenation of that print f is the same as is is like um you know the print sort of the the S 

print functions that you'll find in in a lot of languages it's it's where you're you're very specific so here obviously it it will not automatically add the spaces we we have to Define what the the type is to to be able to print the value out there and uh if you look at the very end we're using uh sln because we need to add the um the return control character otherwise we wouldn't get a carriage return in our in our 

console now there are a couple of um special kind of types there t obviously will will give you the the type um V is just the value you could be explicit there you could say s for a string um D for integers it it's um and then obviously you can also do stuff in there where you can actually do things like padding and stuff like that so it 

um it's something very useful for kind of we use quite a bit for for debugging but like string concatenation and stuff like that as well you'll find that folk use format. S printf which which is a a function which returns a string rather than writing it to to standard out no no next one yeah let's have a look what do we got zero values woohoo okay so 

zero values now zero values for for Primitives you can see there zero for for anything that's a a number uh you you have false for Boolean you have empty string for for a string if you have a complex object if it is a a value and not a reference to a con complex object then it will be just a an empty strut 

which we'll we'll kind of get to in a moment reference types so we will allow things like nil but by default you if you define an integer as as just VAR I in it's not nil even though you haven't assigned a value because it's a primitive value type it will be assigned whatever the default is for that and and in an instance of an iner it's 

cool is this clear as mud I think it's more clear it's not too bad right maybe maybe let's ask folks in chat just in case I I do have enough background to understand a lot of this stuff so yeah okay so chat is this clear as mud they've all gone to sleep they're literally like okay that's fine let's 

move on then we don't we don't want to know about how to program go but you will need it you will I trust me all right type conversions right so a lot of the time you can you can sort of convert types now it it kind of there there's kind of safe type conversions and there's kind of like the ability um what is the the word Nick used for 

double quotes I don't did I say speech marks yes yeah okay yeah sorry sorry about that uh shantu is is just my um my my my terrible briish but your britishness is just fine you you can you can kind of convert sort of types so things like a um you know a 64-bit integer can be converted into a 32-bit integer you could convert a float 

into an integer uh and and along with all of that you will lose Precision um obviously if you convert a 32-bit integer a 64-bit integer you you don't lose any Precision because you you know the the value of the max value of inder 64 is larger than 32 but um you you kind of generally do it like this so you for example here on uh if we look at line 11 Alo line 10 so what line 10 is doing 

is it is giving us the the square root of um uh 3 \* 3 + 4 \* 4 and the value of that is going to be float to a 64-bit floating Point number right now what we can do is we we can actually convert that into an integer because sometimes we we do 

want to drop the Precision we just you know we're not we don't care or we we want to kind of do mathematical operation on on a different type and the way that that the example on line 11 is showing us is that we are converting that to an unsigned integer and the way that you do that is by using the the name of the type in this instance uint and then Open Bracket with the value F which is a floating 

point and that will create a new integer 32 but casting the float 64 into it so if you if you run that you will see what do we see yeah I snuck the F in oh okay yeah yeah but but it um I mean if you changed uh can we change this 

uh yeah like the the casting will work with with with differ Precision but it's not always possible to do large scale type conversions and and actually doing type conversion like this can be can be unsafe there are better ways of of doing it but it's kind of a as a basic instruction when you see something like this this is what you're getting now type inference we kind of uh we we 

discussed this earlier on and um basically in in in go oh if you go on to the next slide there sorry yes what if you sort of do this in in go then the we can either Define something explicitly so we can say I is an integer um but then you have type inference so if you if you're assigning something to a variable goes compiler 

will figure out what that variable needs to be you don't have to kind of explicitly kind of state what what it is and that's kind of nice because it it it sort of keeps the code clean you don't have to kind of have all of these these types U throughout your your code there you can kind of see there some some of the examples but um I I do love the fact that do do folks on chat know where the why the number 42 is so 

popular like is did did hitch is gu to the Galaxy is that is that a is that a thing that is crossed the channel they made a they made a Hood movie of this right there there was a Hollywood movie I have the book on my bookshelf um this just off camera over here so so I I think it's part of nerd pop culture now but that could be my own bias I um I grew up with with hitchhikers because I was I'm just 

old enough to remember the I didn't listen to the radio place because we had television you know we were we were modern in my household but I did watch the the first series um of of hitchhikers the BBC based series uh which was on on on television and well not just more than once I watched that several times CU my dad was was also a massive fan okay moving on right oh I'm going to 

pull my cable out so yeah we've discussed type inference yeah we now know that 42 is uh the the and now on a on a side note of this so deep thought right which which obviously spent a long time is deep thought like some some kind of uh Prof is is it like a is it is is 

this AI before we knew what AI is is is was this predicting the future before the future I I I I don't even want to go into this let's move along constant yes all right now so a constant is is kind of what it says it's something that you can assign but you then you can't change the the the value no I am just uh naturally broken um bco 

uh it's something you can't change the value of so Pi is is obviously a constant there's obviously the two decimal places version of of Pi here but for example if you if you try to kind of set the the value of a a constant after you've declared it the the compiler will will break so if you if you kind of run the code there you you kind see those those kind of constants very similar conceptually to a variable in terms of the type inference 

and the the ways you can kind of declare them with without the the types there and use the uh you do have to use the const keyword though so this this works but then if you let's say on line after line 12 let's just add another line and let's try and do truth equals false and then run that and then the compiler 

should should complain there okay so can't assign truth because it's it's it's a you know it's a constant which is is uh a good thing right so very useful to to kind of have those and you will see them and again constant with the uppercase Pi is exportable so you can have constants which are local to the package and which which are Al exported next things 

next okay next things next numeric constants okay now what is this telling us here highper Precision values untyped constants takes the type needed by its context Ty try printing okay let's let's print this let's see what it see what it 

does weird Okay so we've printed a large value so the the key thing here when we're looking at is if you look at um8 it's um it's basically bit shifting um it's it's a useful thing to to kind of see you will you will kind of see this when when there's kind of a lot of very sort of low-level protocol type stuff where 

where people are actually manipulating the the the individual bits on a bite or or kind of a number of bites um we probably won't see it in the terraform provider so we can we can probably just move along there and file that under something that we might need to come back to if we ever see that that sort of syntax before again cool all right congratulations yay we made it through 

the initial tour okay we are getting there so let's let's kind of um kind of continue a little bit so in in kind of summing up like for anybody who's joining what we're we've done is we we've kind of just went through some of the basics of go because if you're going to be building a terraform provider the the kind of the core thing about that is you're going to have to 

program the the provider using the go programming language if you are not conversent in that language then we're kind of just running through this this very initial step of of teaching Melissa syntax around go so that then we can dig in and write our first application and go so loops are something which you will use all over the place time and time again and and let's have a look at the 

syntax here so what we have here is a a four Loop um oh sorry if you just press the the next next button uh you want to be on uh let me probably uh I'm gonna send you Loops here we go that's right yeah okay so line seven what line seven is is showing you here is a a loop so 

you have I colon equals zero so that is what does that starting point right setting the integer I to zero and making that your starting point exactly yeah that's right yeah now four Loops are kind of a bit of a a weird one in go because there's um you'll see a couple of different variations of the Sy tax here but that's exactly there so then you you see the colon what the colon is 

is kind of like separating that and then we've got obviously is I less than 10 so we have the condition by which the loop will will operate yeah yeah and then uh the very end what we have is we're basically incrementing the value of I on every loop with with Plus+ which again is just a a go convention to take the value and add one to it we 

could have explicitly kind of said IAL i+ 1 we could have said IAL i+ 2 etc etc yeah but that's that's what's um going on there and then what we're doing is we are going to increment the value of sum so we're doing plus equals so we're we're taking the value of sum and we are assigning and adding I to it and then we're just going to print the final value so if you if 

you run that we'll we'll kind of see the output there you see that right now if you let's let you do a little exercise here actually for every iteration of the loop let's print the value of I oh the value of I yeah so every every 

time we we we do a loop yeah let's let's just print I yeah perfect oops there we go and then if we run that we'll we'll obviously see okay the the individual values of I and then of course sum which is all those numbers right brilliant we will move on now for 

continued well let's run this and you'll see you'll see what's going on here okay okay so what we what we're doing is we are um basically we we've just got a a sort of a continually sort of evaluating evaluating Loop and this will exit sorry it will only evaluate when sum is less than a thousand now the the 

reason that you're kind of seeing the value of some there is 1024 is because at some point through this Loop the value of sum exceeds a th you know it doesn't immediately terminate you can't you can't figure that out but but that's what we're doing I would be honest with you I very very very rarely for Loop that you don't you don't see that very often but again it can be done so this is this is 

an important sort of learning but we can we can move on here okay okay this this I think catches a lot of new go programmers out they they're like okay great I understand for Loops I can Loop incrementing a value that is all perfect how do I do while well technically you four go doesn't have 

the doesn't have while as as a yes you can do it but you see you just use this different syntax so all that's happening here is you're saying for Su is less than than a thousand grammatically that that genuinely hurts my brain when I think about it and and um Rob Rob Pike um I want to have words with you about this 

but but it actually makes sense like you know you got to think about a lot of the things here there we've got a little bit of slightly different syntax but the the cognitive overed we we've got less things to learn there are less uh keywords to to be able to learn and that's kind of one of the core premises of of a lot of things that you do and go it it is intended to kind of fit into a small brain like mine there's there's not a massive overload of syntax 

or keywords or things like that it it's it's as simple as it can be to get the job done and I appreciate that a great deal so what we're seeing here is if we want to do while well we're just doing a for Loop but we we drop the initial assignment and we we drop the incrementer and all we're doing is a um sort of a value comparison so this will run for as long as some is less than a thousand and we can see there so exact 

you know very similar to what you we saw on the previous one but just simply yeah this uh next example is something you do see quite often so this this is basically an infinite Loop and uh if you run this it well it will eventually just time out um we're probably just this is probably used in 

some like people clicking on this it's it it'll just be probably Bitcoin mining in the background or generating entropy or something I don't know but but that would obviously if you were running that on your local computer run forever until something crash you switch your computer off or or whatever there is a way to kind of get around that you do the syntax a lot and uh the reason for that is that sometimes you want a control Loop which executes 

forever unless there's a specific condition of which you want to sort of a complex condition where you want to exit a uh exit the loop and does it does the example show you this we'll come back to it yeah but but basically what we could do is we could just put a break in there and then break would would exit the uh would exit the loop so we could haven't if you click on the next right so 

conditionals so we we we can write a a conditional like this um uh absolutely right there there is no um there's no repeat until uh you um shantanu it it is all just done with with the four Loops so there's there very very simpli uh simp simplistic around that that perspective so we got a function here square root and we we have an if statement folks who 

are used to a lot of language you're probably wondering well where's the parenthesis go go doesn't doesn't use parentheses so we we have if x is less than zero then return square root of of minus X um and then obviously otherwise we're just going to return the the square root this this conven is really important because go does support else so folks who are used 

to other languages will be thinking well what about else I would say that the go idiom is always to try and avoid using else where possible so you would you'll always see go which which kind of has this this um conditional so if and if you can kind of need to stop flow you generally will see this sort of return syntax like else 

is is obviously useful but but more often than not you you kind of I think the idiom is to try and avoid using elsewhere possible to create code which is a little bit less uh mentally taxing to to read uh and and it does do that you know it is a good a good thing but uh if you if you want to run that there you will see those values and there we go so that is as 

simple as that now actually challenge for you mhm let's cast let's convert the first instance of square < tk2 uh let's let's not do that because I've just realized it's not returning a float it's returning a string so we'll uh we'll just kind of go on sorry okay 

um now if with a with a short statement yes so what your what you can see here on line nine is is actually quite a nice piece of syntax so what we're what we're doing is we we can have the the assignment of of a variable and the the calculation of a value in this we're getting the the power of x to n we're assigning that to the value V 

creating a new variable and then we can actually do the comparison V is less than whatever limb is so that that's kind of allowed us to condense into one um it's it's allowed us to condense two lines in into one and again you you can of see this quite often it is quite useful I think one of the the 

very useful areas of this is when you're looking at things like you want to call a function which would return an error and then if the error is present you can actually just return that error or you can kind of do your your error handling immediately and this this kind of syntactic sugar allows you to do that it's quite nice now you can kind of see in the next example we we see else there so else is is 

present um if you bounce on exactly the same way as you would you would expect it I think this is pretty much the same as is almost um every language you can combine the the sort of um the short form as well so we we've got you don't you don't have to use else like this you could just use else as is basic conditional I could just say if V is less than limb and then defining V in a separate line but you 

can have that there so the um else is is present now we have what's what is the exercise here so exercise loop loop let's Implement a square root function given a number X we want to find the number Z which is which Z 2 is most nearly 

X okay so computers typically blah blah blah adjustment makes the guess better implement the square root function provid [Music] 

repeat the calculation 10 times and print Zed along the way the value stopped changing uh okay than am I being thick here I think I am I'm um you you go ahead because I'm I'm 

still the decoding these uh instructions okay oh wait no I just said one and then um all 

right okay see L the next yeah I need to look at my other screen this one's a little bit too short and 

then yeah get the syntax wrong here but we'll see yeah yeah I I don't understand what it's trying to 

do so square root of x using a loop start with some guess [Music] Z okay so I'm guessing it wants to us to this even though it's awful yeah it manually wants to to kind of implement a square root function so it's um it's basically the um using 

a a gas and a Gess and check based approach so it's going to just iterate through every possible permutation until it gets to [Music] the let's see what we got see what we get oh 

yep so what we have there is a a function now because you've defined uh float 64 which is at the very end right you've always got a return got return yeah okay so you just return Z there or you could yeah undin Z okay uh and that is because so 

what you if you look there you've got line nine yeah uh oh sorry if you look at your Loop so you see there you in your Loop you have uh you're you're defining on line 8 Z colon equals one yeah now there again is something which which catches a lot on you go program is out when you define a variable in this instance Z that is 

scoped to the for Loop so you can only use Z there inside of the for Loop it it doesn't exist outside of the loop uh the same applies for the if statements that we were just looking at so the the kind of that that single line if statement it's uh it's exactly the same thing so you you um yeah you can't you can't turn Z there but I mean if you just want to test it you yeah you can Define Z up 

here so this should be a SLE I guess yeah so what you you have to do is you um on line nine you can actually assign it so you could at the very beginning you can do Zed equals one oh I thought we said we wanted it outside of the yes you where you're you're assigning it sorry you're instantiating outside on line eight but um okay you can still set the value just drop the colon and then semicolon in 

there yeah if you click the syntax off button at the top there as well it will um it will enable syntax highlighting for you okay just make it a little bit clearer to read I just not okay so you see there then the you've 

written the for Loop we we can kind of write the um the the outputs there um what does it want to do next change the loop to stop once the value has stopped changing or only changes by a small amount you know what let's just move on I am um actually is it okay if we break 

here and and return for next time it is indeed I think we we've kind of covered a lot of the um a lot of the basics anyway there so we we're kind of next time what we can actually start doing is is is digging in to building the terraform provider this episode has literally been about setting up the U the environment uh for some of you folks I'm I'm pretty sure that this is kind of well I know how to do this uh one of the things that I say I found quite quite a 

lot when when teaching people how to build tone providers is that that the barrier can actually be the go programming language that folks are Java Dev P python developers are not necessarily from from go of background which is why we're starting at the at the very beginning but next time we'll we will kind of continue and we'll we'll dig in I hope you learn I've definitely learn definitely did well thank you Nick thank you and 

thank you all for for watching and and uh check back and we'll continue this again soon all right see you later bye
