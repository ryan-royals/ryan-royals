---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/git-hub-at-at-ride-along-automate-the-automation-with-terraform-deep-dive/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/LfTQP5S1cnE/maxresdefault.jpg)

hello and welcome back to Azure terraformer I've been working on my terraform ATS quite a lot both the Azure devops Edition and the GitHub actions Edition and while I have been making announcements I haven't really dedicated a lot of video content to these new changes that I made now most of the changes are really not to the structural components of the atat themselves but to the samples that will help you get off the ground running with these at-ats and 

in case you're wondering what the heck an atat is it's a special type of module called automate the automation with terraform at at the W silent these modules distill a common practice uh that I use when setting up Azure devops and GitHub projects and pipelines that automate terraform so basically inside of an atat module you 

get a fully working Azure terraform solution with full backend state with full automation using either Azure devops pipelines or GitHub actions so I'm going to dig into that today but before I get into that I wanted to thank two new members yes we have two new official Azure terraformers we have Andrew Webster and Steven Carlson thank you guys so much not only is Steven Carlson an official azure terraformer he 

is also part of an Elite Squad of azure terraformer code ninjas which have exclusive access to Yours Truly through our dojo in the Azure terraformer Discord server so Andrew Webster Steven Carlson come on down join the Azure terraform Discord send me a DM and I will put you in the appropriate role and we can start collaborating more closely together there's quite a few folks on the Azure terraformer Discord asking lots of different questions and even some of you wonderful Azure ter performers out there are even answering 

some of the questions so I don't have to it's a wonderful thing besides I don't know everything so it's great that we have a lot more Community engagement and folks that know stuff that I don't know answering these questions so a big shout out to Rod Stewart longtime longtime audience member really appreciate what you do Rod but I just wanted to thank you Andrew Webster and stepen Carlson for supporting the channel in this way and stepen Carlson really look forward to working a lot closer with you on your terraform projects through the Azure 

terraformer code ninja Dojo if you are interested in officially announcing to the world your status as an official as your terraformer please click that join button down there and join the channel it really helps out a lot and what better way to announce to the world that you are an Azure terraformer there are other membership options such as what Steven Carlson signed up for which is the code ninja Squad 

which grants you exclusive access to my code reviews where I can provide more Hands-On mentorship in your software development journey and then there's also my inner circle which will get you access to me for 1 hour a month to talk about whatever you want to talk about we could sit and play majang if you wanted or tic-tac-toe or we could talk about terraform Cloud architecture software development you know whatever but I do know a lot about classical music so so if you want to 

pick my brain about that that's always on the table anyways that's it again thank you to my new members Andrew Webster and Steven Carlson really appreciate your support without further Ado let's drop into code and let's look at the terraform atat GitHub Edition so here is the sample this is this is probably the sample that you want to look at it's the application environment this is what's going to set up a typical Azure project that's going to provision 

and application to a resource Group and if you look at Main we see that we have the module declared here and it's using a relative path now when you go reference this module yourself if you clone the repo and you want to use the sample locally like I am then this is going to work fine for you and it's going to pull whatever the whatever version you cloned off of the repo um however if you want to reference the module over the Internet through the registry um the relative path goes away 

and you're going to use something that looks like this so the trick of converting the relative path in here is you go grab the version out in the repo um you the source is going to be uh based on the name space within the official terraform registry so um my my username out there Marti the uh module library and then the provider um make up 

essentially the namespace now I I typically set up multiple multimodule repos and in order to reference one of the modules within my repo you need to do a slash slash and then the path to the module so that's basically what we're going to change here and then you need to leave the version there to to pick the specific version and then you can reference you can reference the module just like that 

so um that's that's how you reference the remote module if you don't want to go through the hassle of cloning the repo I'll leave that in there just uh just for Giggles so anyways what is this sample actually doing so I spent uh I spent some time you know setting up this sample to basically make this thing as TurnKey as possible um so if we look at the variables what are we what are we taking here um and I'm going to I'm just just going to diagram this here over on 

the side so we're going to take we're going to take a name um we're going to take a uh commit user which is basically who you are on GitHub because as you know the GitHub ter the terraform atat GitHub Edition is going to be checking in code to GitHub for you right um so it needs to know who you are 

in order to do that so these These are the three input parameters um the name this is uh you know so if we go look at my TFR actually my tfrs are going to be right here and and actually I think I think my debug. sh script is going to be setting the name the name is essentially going to be the repo right the commit user is who you are and then the environments is actually a map um with an environment name name in this case um I'm just setting up two two 

environments uh Dev and prod and you can go set up as many environments as you want however you want them to be set up and this is essentially the subscription ID for the dev subscription so the GitHub atat um just like the Azure devops atat um a key a key feature of that of it is that it is multi subscription and so so I can throw this on here um and I am uh 

going to provision a terraform project that can deploy to one or more subscriptions so we have that subscription isolation um commit user that's just going to be me you know who is that me your GitHub user who's going to get credit for all the commits that terraform is going to do for you uh this is a great way to hack GitHub by the way uh if you if you 

want to go do uh if you want to go get some quick commit history um using using terraform to automate GitHub uh it it's it's going to pump out a lot of commits for you so um I think I'm going to be setting up my lot the live uh VW uh so I have this is going to be the name of my repo um I'm basically setting up a a GitHub repository where I can manage my virtual Wan and I'm using the live prefix for a um basically an 

environment that is going to actively manage resources in Azure um it's just one of those convention things okay so the these are the inputs to the sample we'll call this the application environment sample okay and it keeps capitalizing things which is very Troublesome so that that's this this is where the S the boundary of the sample 

is uh is right here okay these are all inputs to this sample so now inside the sample what are we doing so first of all we are provisioning our multi-stage repo so this is our multi our terraform we'll call this our terraform multi stage repo module that's kind of hard to read when when you shout 

can't spell multi-stage repository how about that so that's uh that's kind of the big deal like this this is this is the the the terraform atat that's that's what this thing is so I'm going to I'm going to highlight that in blue yeah in in honor of ter in honor of azure there we go we go Blue bluish it's 

kind of purpley but it's it's that's blue that's blue now this module needs some inputs okay and so if we look at what this module needs this module needs an application name this module needs um a name which is really going to be for the repository so the application name is the name of the unique identifier for the 

application or service that you're going to manage the infrastructure with and the release Pipeline with um that could be distinct or should be somewhat related to the name of the repository right so if my in in this example my my name is probably going to be something like uh my core Network or something like that you know so this is like my virtu my virtual Wan right it's going to be my core Network and my my repo is is 

going to be the actual live uh VW or something like that you know it might be live core Network or something like that but basically this is the repository name this is the application name um as it as it manifests itself in the terraform back end um and all the things right so these are um these are the inputs here the next the next one of course we need we need our commit 

user because the GitHub edition of the atat is of course um going to be doing the operations on uh on GitHub and then we have our environments and our environments is a this is It's that map of uh of azure subscriptions right so that's that's what we're doing there okay um now uh uh basically what when 

when you set up this application environment sample you know there's going to be some mapping going on right there's some direct mapping um we can see you know that we just Cur blanch we take the VAR name and the VAR commit user so right off the bat VAR name and VAR commit user are going directly into our GitHub atat okay um that like no nothing fancy going on here now what is fancy is we're actually our environments 

are actually com coming from a local environments we'll call this extended environments um and we construct this local through some through some skull duggery okay so if I scroll over here we're we're going to we're inside the application environment sample so we're we're going to be looking at how we how we prepare ourselves for the 

GitHub atat okay so I'm going to try and try and make some space for myself over here so how do we get um the the extended environments well first of all the extended environments um is using the the variable environments right so it's not like this is a vacuum um let me get rid of this it it it's not like the environments just magically happen um we we are taking some input from um 

our variable right um it's just we need we need more stuff than what the input variable uh has on it right and so we'll we'll look into we'll look into what that means so what else needs to go into our environment well if you see here we have this module um so for each environment we need to have a tenant ID client 

ID um and a service principal client secret um and then we also need a backends or a back end excuse me um so um you can kind of so basically each environment each subscription needs um let's just call it an an Azure credential okay and then it needs a backend right so that that that's essentially what we're doing to construct this like 

uh local extended environments object um inside this sample okay uh so that that's what's happening okay so now the Azure credential how do we get this Azure credential where this Azure credential is actually coming from this module called well we'll just call this the mo the service principle module service principle module okay um and the service principal module we 

actually have two of them um we have we have one for shocker we have one for Dev and then we have another for uh prod and we're using the key you know and a map of these to to select the correct one so basically these these extended environments um are going to allow us to support Dev both Dev and prod okay and then backends um you know 

it's kind of the same thing we've got you know this local backends uh collection which is being which is uh we're using the key um to grab the back to to grab the um to grab the back end let's just let's just it's kind of the same fashion right we we have we're going to have a Dev back end for our Dev subscription and then we're going to have a prod back end uh for our prod subscription um and so basically this is how we're 

constructing um the environments so um for so all you have to do to use this module is pass in the uh the name of the environment Dev the subscription ID for that environment um and do that for all the environments you have Dev prod each have a unique subscription ID and this sample is going to construct and your credential and a backend for 

you on your behalf right so let's go look at how that happens so if we go look at the service principle um that's under identity what we're doing is we're actually constructing this module and this is from my module Library um it's uh it's actually my Azure ad um sorry the entra my entra ID module Library um and it I just provision a simple service principle right uh and so that is that's how that's 

happening so we'll call this the um Azure ad service principle uh this is Marti service principle module um and and that's basically um that's basically going to generate you an application um inside there what what what is it going to do it's going to create an aad 

application it's going to create an aad service principle and then it's going to create an aad service principle password okay um and the password is your client secret okay so all three of these things combined right is going to produce a uh like the the credential that we use to access this service uh uh the subscription now the last thing that we 

need to do is we need to Grant this um service principal um access to our Azure subscription right so we need a role assignment okay that's going to connect this particular uh this particular service principle to the to the specified 

subscription so if it's the dev subscription we're going to create a service principle that has access to the dev subscription if it's the prod subscription we're going to create a service principle that has has access to the prod subscription this keeps access identity and access control isolated for each of the subscriptions right which is a very good thing kind of least uh least privilege kind of thing going on here right um so we don't have one service principle that has access to all of our 

subscriptions um we are creating a little bit of a security blast radius around the service principle itself okay um now let's go look at I mean and that's pretty much what we're doing with the service principle and you can see here um we're for eaching our over our environments for both the service principal module um we're passing in a generic name so in Azure in Azure ad I'm I'm sorry entra ID we're going to see um an app 

registration and uh you know with this name um which and it'll have a client secret there so uh and and then we'll have a rooll assignment in the respective subscription for what we set up over in um you know uh in the diagram so now the back end okay the back end uh again I'm using I'm using another one of my modules this is a keep it simple stupid module um that basically sets a tarform backend a baseline 

tarform backend right so this is uh this is a storage account with public internet access um of course you need to have the storage account keys and stuff in order to access it so um or you need to have uh a rooll assignment that grants you access to the storage account um which our uh newly created terraform service principles have access to so this backend module so we'll call this 

the mark TI Azure RM terraform backend module is going to create um a storage account well it's going to create a resource Group it's going to create a storage account it's going to create a container a storage account container it's very confusing because it uses the word container which has been 

retro fitted right and we're going to create um a different back end in a different subscription and so uh who what happened to this line there we go so you can see what I'm doing here um I have two providers defined and one is Alias as Dev and I'm getting the subscription ID from my input variable map um and I'm grabbing the dev subscription ID so this provider 

block is now the dev subscription and then this provider block is now the prod subscription uh and then you can see that I am declaring two instances of my terraform my Baseline terraform backend and I'm specifying the dev provider and the prod provider and then to make things super simple I'm creating a local map using Dev and prod and I'm just kind of hard hard uh just jamming them in 

there at the right spot so this is how I'm able to use locals uh to Output that now the backend config is an object that I output from my terraform my Baseline terraform backend which conforms identically very conveniently to the object structure that my GitHub atat takes in for the backend configuration so this is one of those things where you can use 

objects um in terraform um complex objects as inputs and outputs to kind of streamline the interfaces between two codependent or interdependent modules um or modules that you want to Loosely couple together right so um it it does streamline the integration of these modules um but again I'm using bigo notation of one there is no nesting going on here it's like I I just have a 

single object that has three attributes which is the resource Group name the storage account name and the storage account container name that's it um so we're not we're not going too nuts with the complex objects um so that's pretty much the anatomy of this sample there's a lot of stuff going on here right um but it makes for a very simple TurnKey experience as we're going to see so I've 

got all this stuff set up you want to see me run it yeah smash like if you want to see me run it let's uh let's let's go okay so we are about to go create 51 items and these 51 items are going to span three terraform providers the gith ter the GitHub terraform provider the Azure RM terraform provider the Azure ad terraformer provider folks this is why 

terraform is a superpower like literally I can automate consistently across all three of these platforms um in a completely seamless manner it is it is truly amazing so um I'm going to go create 51 things this is literally going to set up a you know a single GitHub repo um that has a fully working terraform codebase that all it does is provision a resource Group um it 

it's going to set up um a service principle with a client Secret in both my Dev and prod subscriptions it's going to set up an Azure RM backend using Azure blob storage in both my Dev and my prod subscriptions it's going to create the environments within GitHub actions and it's going to go tie all those things together and when this is done I'll be able to go to this repo on GitHub this newly minted repo and I'll be able to go run terraform 

plan and terraform apply in both my Dev and my prod environments and it'll actually provision that Resource Group out into that subscription and store it in a state file I mean it's it's literally TurnKey um no setup on your part so for a little bit of run good uh smash like in 3 2 1 and hopefully we can get a clean terraform apply 

here oh no see some of you didn't smash like that that must have been what it was so let's see what happens it looks like it looks like we just had like a 

little environment variable that failed um maybe it was a transient air uh for some extra extra run good if you have if you're one of those folks that didn't smash like and caused you know my terraform apply to fail please for for all the other viewers watching please smash like on a count of three two one just give us a little bit extra run good let's let's let's see if we can get it this time D there we go see if you only smashed like the first time we would 

have been fine you know um but uh just just goes to show you you know all right so we have a fully uh provisioned environment I'm going to run apply again and it's going to tell me there are no changes to my environment which is going to be a wonderful thing because remember terraform is item potent which means I can keep running it over and over again and as long as nothing changes it's going to have nothing to do 

there we go zero added zero change Zero destroyed no changes your infrastructure matches the configuration what a wonderful feeling what a wonderful feeling so now let's go out to GitHub oops so now let's go out to GitHub and look at interrogate what we've created so I'm out here on GitHub let me see if I can find my new my newly minted repo I've got lots of repos going on here here it is live virtual Wan updated 3 minutes ago magical my awesome code base 

uh I this you know go log in issue I I need to I need to fix the uh description the default description uh of the GitHub repos that the uh the GitHub atat sets up but you know what at-ats are awesome so it's not really a bug it's more of a feature anyway um anyway so here we go uh let's go look at settings let's see what else we got here we got we got environments we got Dev and we got prod 

all right we can go look at this stuff what do we have here we have a subscription ID 32 Charlie tenant um we got a a backend Resource Group name uh zti um random strings okay and all the good things okay let's go look at let's go look at prod and see if it's different so remember the sub is 32 Charlie and the the backend Resource Group is uh zti let's go look at prod and see if it's different it should be 

different so the subscription ID is is not 32 Charlie it's 20 Echo and then the re backend Resource Group name is zero whiskey 4 which is not zti so as you can see we have two environments that are provisioned um to two different subscriptions and we have a different Resource Group with a different storage account um to hold terraform State the storage accounts largely have the same structure um you know we got a terraform 

TF State container name um but that really doesn't matter okay um the the point is we have one code base with our awesome terraform code in it here um that is uh you know really I mean it's very it's very awesome it's going to produce this amazing Resource Group name it's absolutely amazing um very simple uh you you can go add whatever you want you know once you use the GitHub atat you know just go just 

clone the repo and slam whatever you want in Main and you're Off to the Races because guess what I can go over here I can run plan I'm going to run plan against my Dev environment now again I haven't set up gitf flow so you know I'm using manual triggers to trigger plans and to trigger applies this is something that I want to improve um but if you're building a lab environment having a the ability to manual manually trigger plan and apply is a pretty useful thing if you're working on a team you're probably 

going to want to set up gitf flow where plan a plan gets executed on pull requests uh to do kind of speculative to do kind of a to to do kind of a speculative terraform plan um on code changes that haven't been merged yet that you're evaluating whether you want to merge them into Main and then a terraform plan that gets executed on the merge into Main or whatever long lip branches that you want to maintain 

environments for so let's go see if this oh yeah sitting here yapping and the plan was successful we want to go create this Resource Group in West us3 um we're we're doing we're looking good so let's go let's go run apply on dev and while we're doing that we're going to we're going to run uh plan on prod I'm being a good little terraformer and I'm running the plan before I run run the apply um I have not fully set up 

a fully multi-stage pipeline in GitHub actions I'm still kind of new with GitHub actions but my Azure devops pipeline is a beautiful multi-stage pipeline that uses compiled plans um so definitely check that one out my GitHub actions though is a little bit uh you know not quite there uh cuz we're I'm not I'm not using uh a true multi-stage pipeline so so we created a resource Group now because it is mutable let me 

run let me run apply again on dev and we should see no changes this should prove that the terraform state is working let me also ceue up a run of apply on prod and we should see this happen so we got terraform apply on dev terraform apply on prod while it's doing that let me go look at my resource groups so I've got my state zti here zero whiskey 4 uh one is in development 

one is in prod so my resource groups with the terraform State files are in there we go look at the containers and I've got my TF State container and I've got my you know obligatory application name and environment name as the backend key of course this is another thing that uh that the GitHub ATA sets up automatically for you and you can see that we do have a random in there and we got a resource Group that's set up in there so I think we're in good shape um 

our state files looking in in what in good order let me go look um at for the resource Group that we provisioned so let's let's go look at the dev environment let's get the resource Group name I can't remember um I I guess if I search for RG AZT TF lab it should come back with all the things so I've got actf lab there's actually a whole bunch bunch of them I guess I've been doing this a little a few a few too many 

times uh so we're looking for uh we're looking for Yankee to Mike Yankee to Mike Yankee to Mike there it is and that's our beautiful glorious Resource Group okay um and over here this is this is the only time I've done this to production so uh we have our beautiful production Resource Group uh papa papa Delta Juliet so let's go look at the um the apply on production and we 

should be able to see papa Delta Juliet as the resource Group name so there we go prod Papa Delta Juliet there we go folks I have set up a fully working endtoend Azure terraform project on GitHub actions with a full cicd pipeline that Provisions my Azure infrastructure using terraform using a GitHub action based cicd pipeline this is the power of 

the GitHub atat so as I say don't be a silly Nerf hurder hop into your atat and blast the tedious setup that you do in GitHub and Azure devops to Smither I hope you enjoyed this go check out my terraform at-ats both the Azure devops Edition and the GitHub edition if you like this module please smash that like button and consider subscribing to my channel and also if you want to work closer with me consider Channel membership just like Andrew Webster and 

Steven Carlson really appreciate the support and don't forget there are Channel membership levels that get you more exclusive access to Yours Truly so if you want to work with me more closely uh definitely consider those options and sign up today again that's it for me happy as you're terraforming it's even more fun when you do it from the comfort of your own cozy terraform atat that's it for me this is the Azure terraformer sign 

off
