---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/automate-your-rest-ap-is-with-swagger-open-api-specification/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/qdp7rFlnJug/maxresdefault.jpg?sqp=-oaymwEmCIAKENAF8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGBYgRih_MA8=&rs=AOn4CLAXTtLX3vBr3S0BgUO0UTWDim1-6A)

hello and welcome back to Azure terraformer I'm going to be starting a new series where I'll be drawing from a series of private one-on-one mentorship sessions that I gave to my LEAP intern the LEAP program is a wonderful program at Microsoft where we try and draw Talent from other Industries into Microsoft to increase the diversity of thought and bring New Perspectives to software engineering I think it's a great idea in fact some of the strongest software Architects software Engineers 

that I've ever met don't have computer science degrees they came into this industry as self-taught individuals quite inspiring so I was humbled to be selected by my manager to be a leap mentor and as part of this program I spent quite a lot of one-onone time sharing whatever I could of my knowledge in software development and software architecture in cloud and devops to help this person succeed so this series might be a little bit eclectic it might be a 

little bit rough because I'm doing all of this off the top of my head with no plan so bear with me I hope you find it useful at least some of the topics but I've got about 36 hours of recording so it's going to take me a while to chop these up but this is the first talk it's all about Swagger and the open API specification seems like a good enough place as any to get started anyways without further Ado here we go Swagger is a Json based description language for what a rest API can do um so it has 

structure to it that's uniform and consistent which means you can build tooling around it that generates a UI like Swagger UI and Swagger UI is just like okay we have a consistent format for describing how to interact with the rest API now I can build a simple guey that reads that Json specification for how to interact with that rest API and then I can build kind of a pretty 

interface that'll let a developer like try out the rest API so it's it took us Beyond manually documenting rest apis to fully automated documentation of rest apis because you could just like with any no matter what language it's written in C Java python go you know there were plugins that would basically emit a swag 

specification for your rest API um and no M so no matter what you code it in you had a consistent specification for how to interact with it so once we had that we went beyond the just automating the documentation now we could kind of automate the clients and that is both a graphical user interface which is Swagger UI which allows developers to kind of test out arrest API that maybe 

they've deployed or maybe somebody else has deployed and they've been granted access to but it also allows us to do things client side like generate an SDK around a rest API in a convenience language so I've got a rest API and it lets you order pizzas through my pizza shop I want anybody who wants to build a mobile app or website Facebook plug-in widget whatever I want anybody to be able to be able to order a pizza through my pizza 

shop so I publish an open API specification out there no matter what application You're Building what language you're writing it in whether it's a desktop Windows application whether it's a Mac OS application an iPhone app a JavaScript web app you can take that open API specification you can generate a client side client side code in whatever language you're writing it in and 

basically you it it'll abstract the low level HTTP operations from you so instead of like me ordering a pizza I don't have to know like oh HTTP post at this like magic string pass in build a build a string request body and attach these headers and do all this craziness and then submit http HTTP post with open API 

specification I can be like okay I'm writing this in Java so I'm going to run Java Swagger code gen and generate a Java client library and now I've got a class called Pizza client and pizza client has a method called order pizza and that takes in simple parameters like the size of the pizza and the toppings on the pizza and rather than having to know all the crazy HTTP 

stuff I just say new pizza client pizza client. order pizza that's it so it makes it super super easy for me as a developer that's trying to use that rest API to consume it cuz I don't have to worry about all the plumbing of dealing with low-level HTTP stuff in the Swagger specification the Swagger specification has to Define get post put all that stuff in the Swagger spec but the 

Swagger code gen comes later and the Swagger code generation basically takes that specification which describes get post put pizza and all the and all the crazy Json that describes a pizza size and a pizza toppings and all that jazz and the code generator the Swagger code generator looks at this that Swagger specification and generates the Java 

code and makes it simp simplified so that I don't have to know get postp put whatever I'm just like oh yeah create a pizza get status of pizza and so the specification also allows you to as a rest API developer you can embed metadata that can provide a better experience for those code generators like what's the description of this 

method what is the name of this method like so that it will generate a method that's a little bit more common sensical that's like order pizza as opposed to Pizza post so the Swagger specification has a little bit of a little bit of metadata like that is kind of a creative writing exercise for the the rest author to inform how the documentation should be written but mostly it's autogenerated 

B based on like the actual code that is creating these these end points and and in asp.net it's in the controllers in your controller you define methods and then you annotate those methods to you know using asp.net attributes to say oh this is a HTTP uh post or this is HTTP get here's the route here's the request type that it'll take in here's the potential response types that it'll send back yada 

yada
