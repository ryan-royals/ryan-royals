---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/how-to-structure-terraform-project-3-levels/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/nMVXs8VnrF4/maxresdefault.jpg)

in this video we'll go through the typical evolution of a terraform project we start with a small personal project or maybe a startup and gradually evolve it into large scale Enterprise terraform deployments when you're just getting started you may create a separate git repository for example Cod infra and start putting all your terraform files there in the main.tf file you might initialize terone provider and define components like adbs VPC for Simplicity let's say you deploy your app using ec2 

instances as time goes by you'll learn some terraform naming conventions and decide to refactor you place the tform provider in its own file you might also be ready to invite some clients to start using your application at this point you realize that developing and serving real customers from the same environment is not a good idea first you try to make your code more reusable you refactor a few variables and place them in 

variables. TF file at this point you would create multiple folders in the root of your repository you might have folders for development production staging QA and other production environments in different regions you would also have a folder for global resources such as IM users S3 buckets and Docker repositories that should be Global to promote your artifacts between different environments so far everything looks straightforward as your project continues to grow you add more 

infrastructure components in the main.tf file or place them as separate files under environment folders no matter which approach you take all these components will be stored in the same terraform State you'll be able to reference these components for example by using atbs VPC to pull VPC ID and use it in different resources this approach creates implicit graph with dependencies ch form will first create VPC and when 

it's ready it will create subnet when VPC ID value is available there are a couple of issues with this approach first if you have hundreds of terraform resources it becomes very slow to refresh the state when you run terraform plan if you actively working and testing your infrastructure you might wait a few minutes for teror to refresh the state adding more resources will make it even slower the second issue is that everything is inside the same state file if some something happens to that file 

for example if you accidentally delete or corrupt it by using CH Forum remove or import State commands it becomes a single point of failure this is not good in large projects we start to create subfolders for each component under each environment for example you would have a VPC component subnet component eks component application component ET this way you split your ter form State into multiple files in the following tutorial I'll go into detail and explain all the 

pitfalls and work arounds for instance you won't be able to use terraform resource references directly I'll explain a common pattern to address this issue through the rest of the tutorial at this point you have enough experience and are ready to group some terraform resources together and create modules the next approach is Monaro in the root you would have environments and modules folders each environment would have the same component on but now we create 

modules for example you might have a VPC module a subnet module Etc at this point you simply invoke those modules from environment folders this approach is simple and works well until you change or upgrade a tform module since it's just a folder and is referenced in all environments any change to that module will trigger updates in all your environments simultaneously which is not what we want we want to control upgrades 

for each environment one at a time to solve this in the monor repo setup you would simply copy and paste the module and give it a new version then you can update anything in that module when you're ready you can update the reference to the module in each environment and ensure everything works fine as your team grows you decide to start using a more advanced structure in this case you create a git repository for each individual terraform module however you need to be careful because 

having hundreds of modules would mean creating hundreds of git repositories I suggest trying to create reusable modules that you can apply to different applications to minimize the number of git repositories using this approach you can reference a terraform module by using a git repository and git tag when you update the tform module you just create a new git tag and use that tag in your code we'll go through the evolution step by step and I'll explain why certain decisions are 

made let's go ahead and create version one each version folder will represent a g repository for managing your terraform project when you're getting started you will usually have multiple folders for your environments for example you might have a development environment it's typically small and used for development and testing you will also have a production environment where you deploy customer facing applications this 

environment is usually much larger and more expensive than development and other environments you could also have a staging environment a QA environment or maybe multiple production environments in different regions for instance you might have one in United States another in Canada Europe Etc besides that you would have some Global components as well this could include IM users in adbs or frequently glob mobal S3 buckets or 

Docker repositories for all environments this setup allows you to test and promote the same artifact between different environments for example you might build your jar or Docker image and then deployed to development environment then maybe staging and finally to your production environments so this artifacts are immutable Global and must be shared across all environments let's keep it very simple for the first 

iteration and Define all our infrastructure in a single folder or even a single file we'll call our first file main.tf first we need to initialize terraform provider in this video we'll create a couple of ads resources such as VPC and a subnet so you can follow along without any cost the tform project structure we use here will also apply to other Cloud platforms at the very least 

we need to specify the region for the adabs terraform provider let's use us east2 next let's say we want to create advs virtual private network using plain terraform resources we'll start using modules later for now let's configure a few parameters such as cedar block DNS support and the tag now this is bare minimum you need to start using terraform let's go ahead and switch to the development environment folder ER to 

initialize terraform project this will download ads terraform provider and initialize local state since we haven't configured remote state yet it defaults to local backend and uses Terra forum. TF State file next let's go ahead and apply configuration terraform will refresh the state and ask you if you want to create a VPC in ads if you answer yes tform will make necessary API calls to create private Network so far 

so good once completed you will be able to see VPC in adabs console now in the transform State we have a single resource with all its attributes this attributes are very important because we can use them dynamically in other terraform resources for example many terraform resources require VPC ID instead of hardcoding this ID we can dynamically pull it from 

the state next you'll typically realize that you want to create the same resources in different environments to achieve this you would use variables instead of hardcoding those values this allows for more flexibility and reusability of your terraform code across different environments terraform doesn't require specific file names but following some naming conventions can be very helpful especially when working in a team for 

example for variables we typically use variables. TF file this helps keep your project organized and understandable to everyone involved let's go ahead and refactor some of our code first we'll extract the region variable we'll create a region variable and set the default to us East to this way you don't need to provide it every time you run plan or apply 

and of course we need to replace hardcoded value with terraform variable there are multiple ways to overwrite variables you can explicitly provide them during execution or use environment variables this flexibility allows you to customize your terraform deployments according to different environments and requirements next let's refactor cedar block you might want to set different Cedar blocks for your production 

environments especially if you plan to peer them together later VPC peering requires having different Cedar blocks for each VPC let's also set a default for now and replace hardcoded cedar block with a variable this change will make it easier to manage and modify the cedar block settings across different environments finally let's create a variable that will identify our environment we can call it environment or n v the name doesn't really 

matter now let's replace the dev prefix with this environment variable as you can see we gradually making our tform configuration more flexible whenever you make any changes or simply refactor try to frequently run terraform plan to catch any drift we should expect no changes and everything looks good for 

now this approach ensures that your infrastructure remains consistent with your terraform configurations next let's follow some additional naming conventions and move provider configuration to its own file besides the provider itself we usually Define some constraints for the tform and for the provider itself this 

can include specifying the required versions of the tform and the provider to ensure compatibility and predictability in deployments placing these configurations in a separate file typically named provider. TF helps keep your terraform code organized and clear Let's test one more time and refresh the state by running terraform plan by frequently verifying the plan you maintain a clear understanding of how your changes will affect your 

environment before making them live now a VPC is certainly not the only component that we would manage using terraform you can continue to add more terraform resources to the main.tf file or you can create additional files in the same development folder no matter where you place these configurations all the information will be still saved in the same terraform State file let's say we want to create a subnet and obviously we need VPC ID for that if you have used 

tform before you know how it works but let's wait a bit before we start refactoring for now let's hardcode the other subnet parameters the simplest way is to use terraform resource reference to dynamically pull values from other objects and to build a graph with dependencies first we use resource name atbs VPC then we use a resource variable in this case main next we need to find the 

attribute we want to reference the easiest way is to Google adabs VPC resource and scroll all the way down so we're going to use ID attribute all right that's all for the subnet besides dynamically pulling VPC 

ID from atbs resource we also created implicit graph transform will first apply atbs VPC resource and when it's ready it will apply subnet and provide VPC ID value let's go ahead and apply it 

all right let's open terraform State file now we have adbs subnet with dependencies and adbs VPC objects in the terraform State when you work on a terraform project you can add more resources in the main.tf file or you can create and host those resources in the separate files within the same folder this approach lets you use resource references and build dependency graphs 

however there are two major issues with this approach first if you have hundreds of transform resources in the same state file it becomes very slow to refresh the state when you run terraform plan it may take several minutes which can be very annoying if your team members are actively working on something second everything is hosted in a single state file if you accidentally corrupt it you'll be in trouble we frequently use T form remove or import State commands and 

keeping everything in one place creates a single point of failure to avoid these issues in large projects we typically create subfolders under environment folders this helps split transform project and more importantly tform State into multiple components before we start refactoring let me destroy VPC and a subnet now let's go ahead and create a VPC folder in a real life you would most 

likely host everything related to networking in a single folder this example is just to demonstrate my point let's move everything to the VPC folder let's also create another component folder for the Subnet in practice this could be a folder for the eks cluster which would also require VPC ID in the subnet component let's copy and paste variables TF file and keep all 

the variables for now just replace C range for the subnet to be a subset of the VPC CED range next let's copy providers. TF file as well you'll soon see that we have to copy and paste some files if you don't want to do it manually I suggest watching Terr tutorial on my channel we'll keep providers file as it is and won't change anything let's go ahead and create main.tf file for the subnet I'll remove 

the subnet from the VPC component and paste it into the subnet component for now let's keep VPC reference in place since we now have two components we need to apply VPC folder first then switch to the subnet component and apply it as well all right let me go to the VPC initialize terraform and then apply it so far we have created atbs VPC and 

we have a local terap forum. TF State file that describes the objects managed by terraform in this file we'll see only a single resource atbs VPC most importantly we will need this VPC ID in most of the other components including subnet for now let's switch to the subnet and try to apply it while still using resource reference 

now you can see the problem created by splitting all those components into different folders if you have a small project it's much easier to manage in a single tform state file and a single folder so how can we solve this the first solution is to use data blocks specific to the components we need to WR reference for example you can use data 

atbs VPC and provide parameters to locate this object in atbs however you would still need to provide VPC ID for other resources you might provide generic names to locate those objects this approach as you can see is not very flexible and doesn't work well with adbs VPC since we need to provide the ID another common pattern is to reference remote State output variable this pattern is frequently used in large 

projects chant offers something more flexible but it's outside the scope of this tutorial now let's comment this out for now since it's in a broken State then let's create terraform remote State data block it works with all back ends such as local S3 buckets Etc there are just different ways to initialize that data Block in our case we just use local backend and simply need to specify the path to the state file we want to 

reference in this case we want to reference VPC State file under VPC folder this way we'll get access to all attributes from atbs VPC resource but there is more for now let's test and see what variables are exposed from the VPC component we can create output variable call it whatever you want and we'll remove it later for the value we need to reference the remote State VPC data block 

while we still in the subnet folder let's go ahead and apply it you'll see that there are no attributes available in the test variable the output variable is empty so let's fix that by exposing variables we need from the VPC component in the VPC f folder let's create outputs. TF 

file then let's create output variable let's call it VPC ID or you can name it whatever you want the value will be a reference to the adbs VPC terraform resource first reference adbs VPC then main variable and finally I attribute all right we have output 

variable but we still need to run terraform apply to register that output to the terraform State we need to do this in the VPC folder first now you can see we have VPC ID output variable next let's switch to the subnet folder and run apply as well to see our test output variable finally we have VPC ID variable that we 

can reference in the subnet component this could also be reference in a Lambda or eks component now we can uncommon the subnet and provide VPC ID from the different terraform State file after VPC we have outputs and finally VPC ID Z 

variable we no longer need test output so we can remove it this is a very common pattern for referencing other components in your terraform project in terround you can use dependency let's apply terraform and see if you can create subnet all right now we have adbs PC and the private subnet we can slightly 

refactor this code to use it in other environments such as production we can use a c variable and EnV variable for the name tag also we frequently Place data blocks in data. TF files if you follow the same naming conventions it will be easier for your teammates to locate necessary objects quickly usually many people in 

the company work on a terraform project so it's not just you creating all the components let's run plan to make sure everything is up to date as you can see by splitting project into multiple components you only need to refresh a subset of your infrastructure each time you run plan all right but now we have a problem we don't have a dependency graph so we need to create and Destroy teror infrastructure in the same order let's go ahead and Destroy ads subnet first 

then we need to switch to the VPC and destroy it as well when you split terraform into multiple components you need to create some kind of higher obstruction layer unless you use terrant this could be a simple bash script that applies one component at a time or you could integrate it into your cicd pipeline for example you might have a GitHub action step for the VPC C component followed by the step to apply 

subnet etc for Simplicity let me create a very simple bash script to show the idea let's put it under def folder for now and you can name it tf. sh first let's create apply function that goes to each component and applies terraform then we could have a destroy function that in the reverse order 

destroys those components based on the bash argument we either apply or destroy in real life this is going to be much more complicated of course let's go up to the development folder and make our script executable first then let's run TF apply to create both VPC and subnet 

now we have both atbs VPC and private subnet we can destroy infrastructure using TF destroy command that's the basic idea create a script or integrate it into your pipeline let me copy and paste the same setup into the production environment you can update some environment 

variables maybe you want to use a different cedar block or deploy to a different region which is a common for different production environments let me update the same variable in the subnet as well all right this is the first version when you're just getting started and not using terraform modules yet there is nothing wrong with this approach it involves a lot of copy pasting but it makes day two operations easier when you update your existing 

infrastructure now let's say you have been using terraform for a while and you are ready to move to a more advanced structure let's go ahead and create V2 folder that will represent a single git repository in that folder you would create a subfolder like envs or maybe even environments some people call it infrastructure life or just life environment ments Etc we'll also create 

another subfolder for the modules this is the Monaro approach and we'll go over the benefits and drawbacks of this approach you might not even need to move to more advanced structure a terraform module is just a bunch of terraform files and resources grouped together and placed in the same folder let's create the same development production and Global environments next let's create a VPC module by simply copying and pting in the VPC 

folder we'll make some changes to follow best practices when it comes to modules first of all we never initialize tform provider inside the module we do it from the live environments folder let's rename providers to versions. TF file as this is one of the naming conventions in the terraform community next create a VPC folder under Dev 

environment we also need variables for example to use for the region when initializing adbs provider finally let's create main.cf file for the VPC itself first we need to initialize adbs provider then we call our VPC module I like this transform structure because you can work and update both modules and 

environments from the same place if you have a small team or a single devops person in the company I suggest sticking with this approach as it's easier to manage next we can provide some variables like environment and CID block next let's create another module for the subnet but before that let's create VPC using this more advanced approach let's initialize and apply 

terraform so far we have created VPC using new approach with a monor repo 

next let's copy and paste the subnet files into the subnet module first of all we don't need the data block inside the module so let's remove it 

then let's remove provider and rename the file to versions. TF as well next let's refactor VPC ID variable instead of using data resource inside the module we'll provide VPC ID as input variable to the module let's call it VPC ID and set no default value for 

it inside the resource we'll use that variable next we need to create a similar structure let's create a new subnet folder in the dev environment 

let's also create a variables. TF file with the region for the advs provider then create a main.cf file and initialize provider next we can call subnet module however we have a problem we need to provide VPC ID you might think that since we have 

output variable in VPC module we can use it right away well let's test it for now let's comment out the subnet module and Define data block and test output variables it's essentially the same thing switch to the subnet live folder 

initialize and apply tform and here you can see that we actually don't have any output variables we use outputs in the module but we have never registered them in the state file in other words if you create Subnet in the same folder as the VPC module you 

can use VPC module as an input variable however if they located in different folders it's not going to work to fix this we need to create output variable inside live VPC folder let's call it outputs. TF for the value we'll use module output variable 

all right now we need to go back to VPC and apply it next let's switch to the subnet and test it again all right now we have VPC ID attribute let's remove the test variable and use data attribute as input to our 

subnet module let's initialize and apply it 

again all right now it works we have created VPC and subnet using modules and a monor repo now we can pretty much copy these components to all other environments and maybe change Dev to prod I like this approach because it's simple but it has a significant drawback occasionally we need to change something 

in the module for example there might be a new feature in adabs and you need to upgrade adbs provider and use that feature inside terraform code there is a problem because our modules are just folders if you change anything in the module it will trigger updates in all other environments if you have five 10 or even more production environments you'll want to update them one by one and it's unlikely you can do it all in 

one day so you need a way to version your modules in a monor repo setup this is often done by simply copying and pasting for example let's copy VPC module and create a new V2 version it's totally fine to copy and paste using this particular intermediate approach now in this version let's say we want to refactor DNS support and use variable instead of hardcoding them let's create 

new variables and refactor terraform code now that we have a new version of our module we simply update the reference in each environment one by one and test that terraform code only makes 

the changes we intended first we need to initialize because we're using a new module then apply it and verify that only DNS support is changed if it looks good we can apply the changes after that you can go ahead and update the module in other 

environments this would be intermediate approach to structuring a terraform project now it's time for the most advanced approach let's go ahead and create a V3 folder in this repository will also create a live environments folder let's use the same development production and Global environments the biggest difference compared to the previous approach is that we'll put each terraform module in its own git repository so let's go ahead and create 

a new repository for the terraform VPC module we typically use the following naming convention for the terraform modules terraform prefix then provider and the component let's keep it private and add a redmi file next let's clone this Repository 

open it in a text editor and copy paste the VPC module from the previous example 

let's keep it as is for now and commit all the files the biggest benefit of this approach is been able to use git tags and Version Control for your modules for this version let's set 0.1.0 gitto you can reference branches like main Dev Etc but the preferred way 

is to reference git tax let's go ahead and push everything including tax to the remote repo now we have the source code in GitHub and we have git do that we can reference next let's create the same structure and create a VPC folder copy and paste the same files from V2 

version the difference is that instead of referencing the local path with the module will reference the git report and the git tag 

let's go ahead and apply it 

you can see it uses GitHub repository now let's say we want to make the same changes as in the previous example and release a new version of this module let's refactor the same variables out 

to release a new version we will commit all the files and create a new 0.1.1 git tag that we can reference 

now we have a new tck let's go ahead and upgrade it in Dev envirment for that we simply change the git tck while this looks like a better approach it can quickly become overwhelming if you have 

hundreds of modules you would need to create hundreds of git repositories if you have a small team or a single person managing infrastructure switching between different repositories can become cumbersome based on my experience if you decide to use this approach try to create reusable modules for deploying your applications for example your app may have the same autoscaling group network load balancer and other components instead of creating a terraform module for each micros service 

try to leverage the same module and make it flexible enough to deploy multiple applications version V2 is not as bad as you might think just because you need to copy and paste modules it's much easier to manage thank you for watching and I'll see you in the next video
