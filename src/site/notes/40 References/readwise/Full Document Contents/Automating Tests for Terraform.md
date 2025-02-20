---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/automating-tests-for-terraform/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/oLRtFy6mYSg/maxresdefault.jpg)

okay and hello everyone uh welcome and thank you for joining today's snapshot um so I'm Kon you can call me KY I'm a Solutions engineer based in Singapore so before I go deeper I just like to talk about the test pyramid and this concept in itself is not new to many especially application developers so the idea here is at the bottom of the pyramid we have unit test followed by contract integration and end 

to end test and the idea here is as we move up the pyramid um the time and resource needed to run the test increases which is why many organization like to focus their effort at the bottom of the pyramid especially through unit testing so for unit testing we are trying to answer the question of does my configuration of plan contain the correct metadata and as an example say 

we have a module that performs some form of processing for an input variable and the point of the unit testing is to Ure that the output of the module is as expected so say we have a module that does some form of processing for a given string uh say to add prefix and when we do a terraform plan we want to make sure that the prefix is correctly added and for contract testing we look at the question of does the expected input um to theel module match what I 

think I should pass to it so in essence we uh here we are just relying on some form of validation pre and post processing checks to make sure that the given input to a module is allowed and some examples of checks are say things like setting a range of acceptable values or having some form of post-processing checks to make sure an Ami is off a certain OS and for integration test we check if the module can integrate with um it's 

upstream or Downstream dependencies correctly so maybe I'm spinning up an ec2 into the VPC and we look at whether the vc2 is spun up into the correct VPC and subnets and whether the proper networking configuration has been applied and lastly for end to end and this is usually the most expensive form of testing because it require the entire infrastructure to be up and running before it can be conducted and end to end is usually done in the context of a 

end from the perspective of the end user when they're interacting with their applications and with terraform these test can be performed through each of these different capabilities so we can use terraform check for our endtoend test we can use tform test for our integration and our unit testing and we can have validation and pre and postcondition checks for for our contract test but our Focus for today will be form on the tform test capability within 

this pyramid so this is a typical producer consumer workflow for a terap module and at the top we have the platform team and who are the producers and they are the one that's responsible for crafting and deploying modules to be used by the rest of the organization and at the bottom we have the application team so these are the ones that consume the published modules to be deployed resources into the 

environment so the application team will essentially write a template that references the module and then do a telephone plan and apply to create the resources and as Cloud adoption increases within the organization and the number of consumer increases we needed a mechanism to ensure that the modules that have been published by the platform team is well tested and would not cause any unexpected breaking changes for the downstream consumers and this is where telone test comes into 

play and it provides a systematic and automated approach to testing changes to telone files here before any changes can be published we can automate a set of predefined tests to run the module against and only when the test passes do we allow the module to be published and with this any unexpected changes can be caught before it is rolled up to the rest of the organization 

so this is how the full endtoend flow will look like we have the platform team first writing the modules and then having some form of tform test ideally choose some form automated capabilities and before publishing the module and once the module is published then again the application team will consume the module to deploy the resources and we that context in place and let's dig into the tform test framework and this is available in t from 1.6 and higher so the idea here is 

we have the all the test that we are trying to run is written in the htl format the hashiko configuration language and it must end with a TF test. htl extension to execute a test we do ter uh we run the command terraform test and what happens behind the scene is terraform would then look up for all will look up all thef test. htl files within your directory and and consolidate all the different tests and 

then running uh and then running the test against what has been defined so one thing to note the test are always executed with temporary in memories and so it doesn't affect existing life resources so say you have an existing deployment that deploy certain Cloud resources and now I want to do a test on my telephone file the test itself will not affect the life resources there will be no changes to it and if tform test needs to clean uh 

needs to create any resources it also does the automatic clean up of these resources helping to streamline your test experience so engineers and developers don't have to worry about having to clean up after they've done their testing so if we look at the anatomy of a test these are some of the key um um key blocks to look up for when we are looking into a tform test file so whenever we publish a module 

we expose certain there are certain attributes or variables that we expose to be to be uh to be taken in as input when we want to deploy the module itself so the variables block is the mechanism for us to input such input uh to input the variables for the modules that we want to test against so in this case I have the variable block and I'm just uh I'm passing in the value of test to the bucket prefix varable then we have the provider block 

uh similar to how we have providers we are provide we provide provider blocks to our telephone files so tform knows how to interact with the external integration um the provider block allows the tform test to also integrate with external Integrations if it's needed then we have the actual run block and this is the actual unit test itself that we are running against uh in this case we are we have defined a unit test of valid streen con 

3A is interesting so this is the command itself uh there are two uh two possible values that's allowed here one is apply which is the default and plan so as the name suggests if the command is an apply what happens when you behind the scene when you do a terraform test is that the test would create the resources that's needed and once the once the test has been conducted terraform then destroys the resources that have been created 

whereas if the command is a plan terraform then does a speculative plan and then checking the plan against the conditions that have been defined for the test itself then we have the assert block and this is the actual condition checks that we are applying against um the resources that we want to test so in this case we are checking for the condition that if I'm passing the prefix of test to my module I expect the resource to and the 

name of the bucket um to be of test bucket when it's returned at the end there's also an Associated error message for when the condition when the condition fails and in this case it would say that the as bucket name did not match what is expected so other blocks include our pre-run variables provider and module block s which we will go through later on in the slides and within a tform test file 

at the top we have a variables that is at the root level and this is this can be seen as sort of a global variable that can be applied to all the Run blocks that has been defined within your test file so in this case we have a global variable of bucket prefi equals to test but we can override this variable within our run block if you want to test for other cases so in this case within my within the Run overrides root level value we Define another variable another 

variable block with a value of other for the bucket prefix so in this case when we are checking for our condition we are expecting that the bucket name to be of other bucket instead of test bucket since the new the variable value is uh the new variable value is being used for this particular test itself and when we are doing test there may be certain situations so where a 

successful test um is a is a result of having some form of failure against the conditions that we want to check against so in this example we have a variable region that only allows two given input AP sface one and AP sface 2 so for this test to be successful where um where we are looking for invalid valid uh invalid valid region if we pass the vision of us is one into the variable we expect this 

variable to fail for the test to be successful and how we Define that is using the expect expect failures block here we can we can give the expect failures attri uh the value of V region to expect the region variable to fail when we passing the value of us this one and we put if we put everything together this is roughly how it would look like at the top left we have our s3. PF so this is our usual terraform 

file where we have our VAR we have our variables so here we have a variable for bucket name and a varable for region and the actual resource that we are trying to create so here we just trying to create an S bucket resource we are taking in the bucket name and adding a dash bucket suffix on the right we have the actual test that we have created for this particular module here we have two we have running two sets of test first is the valid 

bucket name and second is the invalid Vision so for the valid bucket name if we passing the variable of of test for the bucket name we want to check that the bucket name when it returns ends with a dash bucket to make sure that the sub has already been added and for the invalid region we are checking to see that if we pass us is1 to in into the region that the region should fail and for us to conduct this test we just 

simply do a terraform test and terraform would then look up for all the TF test.c files consolidate all the different run blocks and then conducting the test so for more um there are for more advanced use cases for test there may be certain uh there may be certain prerequisites or requirements where we want to do some certain Baseline um before we deploy our resources so in 

this example before we deploy our resource we needed to set up a network so terapon pest also supports the calling or the ex um the execution of existing modules um to set up the environment that's needed for your test itself so in this example we are calling the networking module to create our vpcs and subnets and before we run the test itself we then get the VPC information and then passing it into the test um 

when we um before we do our actual test itself and so we can sort of chain the dependencies between different modules um before before we uh before the test is being conducted and there's uh with terapon 1.7 we introduced the concept of test mocking so mocking allows us to provide sort of like a um a replacement or a local copy of 

the different resources that we are trying to interact with in this in this example we are trying to mock the AWS provider so conventionally if you want to create when we are doing our telone test and we provide the AWS provider the test will reach out to the actual AWS provider and creating resources into your AWS account if we mock the provider itself um essentially what we do is we it creates a random data for all the different calculated attributes within 

the provider so things like your S3 bucket uh your ec2 modules this have been replaced by um a local copy of what terapon would expect the um the expect the real provider to provide so this uh this is especially useful when we want to run test in an environment where say you don't have access credentials to your cloud account so you can mock the provider uh allowing terraform to run the test without ever 

having to interact with AWS and this is also useful if there you want to run the test uh if you want to in improve the speed and performance of your test itself and because we are mocking the provider there's no actual API calls being being sent to AWS we are not waiting for resources to be created everything can be done locally uh within your your testing environment so besides mocking the provider we can 

also mock resources and our data sources so in this example we are mocking the AWS S3 bucket resource and we are saying that whenever we are trying to create the AWS S3 bucket we will return the Arn in this particular format same goes for when we are trying to data source for a ss3 bucket we will return the value using this particular format and another Power powerful feature this is a feature that's only 

available on the hcp terraform is the ability to generate our modu test so using a large language model train on HDL and the tform test framework when a new module is published within terraform Cloud terraform Cloud will can look at the file understand how it's being created and provide suggestions and Sample codes as to what kind of test you could run against your module and so this essentially helps to 

lower the time needed to craft out the different test and using whatever has been recommended as a baseline for your F and then expanding on this set of test suite for your module and also if you're using hcp tform um there is a built-in mechanism to help automatically run the test whenever uh there's changes U being pushed to your modu itself so that's for the content I'm going to 

run through the actual demo itself so here so here in my ID I have my terraform a S3 module and so the file itself is very similar to the ones that I've shown in the slides earlier so here I'm creating my S3 bucket I'm taking in the uh a variable of bucket name and adding the bucket suffix and I also have some form of encryption configuration for the bucket itself so I've added all my test files in the 

test directory under s3. TF test. HCL and here I am running two unit tests first for a valid bucket name and second for a invalid Vision so I'm passing in my variables of lck demo and here I'm overriding it for to become L uh to be lick demo one and having a condition to check that when I create a bucket that it adds the um the bucket name L demo one has the 

appropriate suffix of Dash pocket that has been defined and second for invalid uh for the invalid Vision I'm passing a vision of USS one and I'm expecting the vision to fail if we look at variables. TF here the region this are the list of acceptable values uh us is one not being any of them so for me to run the test within my tform aw ss3 directory I just do a tform test test tone would then look up all 

the different test file and then running the test against it so I'm also going to push a change to my file so that we can see what happens when we use the tform console so in this example I'm adding a new variable and I'm just going to push the change up to my uh repository so this is my telone console itself 

s my session has expired I'll need to log in again and under my registry I have my S3 module so my repository has already been integrated with my VCS GitHub in this case and the module registry has been used to uh has has been configured to point to the Vio so with this repo can 

see that there is a view all test button if we click on it these are all the different tests that has been executed against this module so when we added a new variable earlier we can see that terraform has already automatically do uh done a tform test to test for the new changes if we click on the test itself these are the different uh these are the unit test that has been executed and once we have tested and we are happy with the 

module we can then publish a new version and when we publish a new version we get to see uh we get to uh this we get to see what has been the test result for this particular version that we want to publish in this case I'm going to publish uh the latest comit and I have a 0.012 so and so once you have submitted the one 

publish a new version then 0.012 will soon become available for the rest of the organization the other capability within HTTP tform is the ability to do test generation let's take note that this is still a better feature but essentially where you could use tform hcp tform to generate a test file so here tform looked and understands the file that has been given and then determine some form of unit test that can uh the appropriate unit test that can be run against so 

earlier when I was creating uh my uh when I was defining my module I didn't have any test for encryption configuration so terraform HTP terraform has given some recommendation as to okay this is the kind of uh this is a unit test that you could add for your module itself and for the new variable that has been added this are some of the uh these are suggesting some checks that I could run so from a develop and the engineer point of view I could just copy this set 

of Ts that has been generated and then pasting it into my module to have some form of uh to have some baseline checks uh for my module before um before I publish it so with that uh this is uh I've come to the end of the demo but if you would like to learn more about tform test we have a nice uh block about the tform test framework um so feel free to you 

know scan the QR code or visit the URL to learn more and with that um this uh that's all for uh for this snapshot
