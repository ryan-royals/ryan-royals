---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/rag-semantic-search-embedding-vector-find-out-what-the-terms-used-with-generative-ai-mean/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/orLGv2LgWDE/maxresdefault.jpg)

hi everyone in this video I want to explore a few terms we hear over and over again when we talk about artificial intelligence when we think about generative large language models we have terms like Rag and semantic index and semantic search and vectors and embedding so what do all these things mean so my goal in this video is to walk through them and explain why they are so important now if I take a step back and 

I completely ignore the idea of technology for a second I can think of some interactions I have had in the last week so there's me now I am really the sum of the things I've learned over time I've been trained on various books and information so I have a set of capabilities in my brain based on how those neurons are connected to resp respond and perform certain 

functions now I had a customer and the customer asked a question and the question was hey is my Azure environment resilient now I have no access to their environment I have no knowledge of their environment so with my abilities that I have I can't generate a response based on their question instead I I need some knowledge 

now if the customer then says to me hey can you tell me if my environment is resilient by the way I can run queries I have permissions against the Azure cloud and I could send you the responses well this now changes things they're telling me a tool set they have so I can say well here's a plan of the things I want you to do they can then run those aure resource grph queries 

they get a set of responses and now they can ask the question again but they add the responses to those things that they gave me now I can give them a response I have not changed really what I've been trained on I've not relearned their environment but based on the request and based on information they gave me well I can take my existing knowledge and skill set and with the 

extra data give them a response now the same thing applies with the idea that also it's the same me it's not a clone it's just a different time my boss we make them kind of angry devil my boss asked me a question and it was hey can you give me a summary of the meeting well I I don't have the detail 

of that but once again my boss has access to in this case the Microsoft graph and they can put in a request for the transcript of the meeting and then they can ask me hey can you summarize this for me and here's the transcript because they're too important to bother to read it themselves and then again based on the knowledge that I've been trained on the skills I have they ask me the question and provide the transcript so they're giving me different data well I 

can go through it and then I can very begrudgingly that I can give them a response so it's the same me I've not changed my training in any way but based on different information they had access to that they could pass to me as part of that question it enabled me to do different things so if we think about really what's happening in these scenarios well they are doing a 

retrieval of data that is augmenting my ability so it's augmented the ability for me to generate content retrieval augmented generation so that's rag that's all it is 

it's the ability that as part of the prompt that I'm going to give a large language model I go and fetch some other information that's relevant that's going to augment its ability to generate a higher quality response so information is being retrieved that's going to enhance his capabilities and that that's really all it is when we talk about rag it's just hey the model is trained on 

some data but I want it to be able to respond based on a different set of data and that's what this is all about so let's actually talk about computers that's probably a bit more useful when we really want to think about what's happening and why we take that approach with a large language model so think about for a second how a large language model actually works a huge amount of training so the 

whole point is we have this training that training is based on huge amounts of data it takes a huge amount of time a huge amount of computational power a huge amount of money so all of that training goes in and that's what creates this normal Network we go through many many iterations we create these hugely powerful models and at the the end of it 

once it's finished all that training we get our large language model that's what enables it to be generative and based on information we give it it can then do inference the ability to predict well what should come next I answer whatever we are giving now a key point at this once the model has been trained it's essentially read only 

that model is now usable but it doesn't change it's hugely timec consuming and expensive to train that model so we're not constantly retraining it every time I send an email that's not what's happening this large language model is now complete and what's actually happening behind the scenes is if you think about again I work in the Microsoft space so I'm going to focus just those for examples if you then go and look at things is like well hey it has a 

copy of this large language model for services like Bing co-pilot for the Azure open AI Services when we think of things like Microsoft 365 co-pilot it creates different instances that live within the various Regulatory 

and privacy requirements of those particular services but they don't change the model it is that same large language model which therefore how does it do that job if all it knows is what it's trained on how is the being able to go and get information from the web how does the Microsoft co-pilot know about things in our documents our email messages how does the security co-pilot hook into those things so obviously we need the ability to get extra 

information into those and I did a whole video on how large language models work so I'll I'll link to that up there if you're interested to that so okay great we have these large language models and we know these various services do different things and as the example of me well I can do different things based on well what additional in information do you the person asking me 

to do a task have and based on the prompt the question you're giving me it's my same brain but I can do different things and my ability to respond is in a huge part based on the quality of that additional information you give me that whole garbage in garbage out will apply here if you don't give me good data well my response to you is going to be not very good so we have the large language model so how do I get it additional 

information well you've guessed it already obviously we're talking about that whole point of the rag that retrieval augmented generation that's exactly what we're going to use here this is the key point now when we use these Services we don't actually often just talk directly to the large language model what the solution is actually going to do is there's some orchestration engine so we have have an 

orchestration now there are different solutions for this Microsoft has a semantic kernel that enables us to perform a lot of this but you'll hear the term grounding and so what's happening here is we have a user and that user makes some request in some context depending on what tool they're in what they're actually doing at the at this moment in 

time well I need to get additional Data before I send it to the large language model because if I just say hey summarize all the messages from my manager it has no knowledge of that whatsoever it has to get more information now remember one of the things a large language model can do is it can help generate a plan just as it said to me hey I want you to tell me about my resiliency I have access to Azure I said well okay run these 

commands for me and send me the responses so sometimes this orchestration will actually use the large language model telling it what it wants to do and hey here are the tools available to you and then it will respond with the plan of the things it wants you to do because there is some knowledge it could be the Microsoft graph it could be some d Spas whatever that is the orchestration will then 

go run whatever the question it needs to do it will get the data back and then send that with the prompt and whatever that data is to enable the large language model to respond with a quality response based on what the user asked based on this additional information that additional information remember 

was all about the retrieval augmented generation this is what makes it powerful that ability to go and get the knowledge and add that to the prompt so now that large language model it doesn't have to have been trained on your data that's impractical to do but as part of the prompt I'm getting additional data to give to it so it can now hey do really good decisions and it's those improvements in the grounding it's those improvements in the ability to go and get the most 

relevant data is how we see these huge improvements in the types of responses these actually give and this is why again Microsoft 365 co-pilot they're not creating a special version trained on your data that's completely impractical it's the same large language model that was originally trained up there but you have access to certain data the orchestration acts on your behalf to make queries against some knowledge set the Microsoft graph um 

security apis Azure restful apis whatever that might be whatever the context of what you're trying to do so large language model can perform different levels of help depending on well what tools it's told is available to it what additional augmented retriever is possible to help in its generation okay so if rag is the ability to go and get 

information to make my response better then what's the big deal with all those other terms remember we had all those other terms floating around what do we have so we talked about the idea of um vectors we had the idea of semantic indexes you'll hear about semantic search you'll hear about 

embeddings what's all that about how do these terms play into the idea of this retrieval augmented generation why are they important at all so if I think about this typical knowledge that we have here very often that knowledge well that knowledge could be in the form of text 

it could be a document PDF file something else Json doc docx it could be an image it could be audio there's a whole set of different formats that could be in and if I just think about the English language I I use the word manager well there's a whole bunch of synonyms for that manager boss leader Etc and some words can mean different things depending on their 

context some things are similar and so if I was just to chuse a traditional exact match or even a fuzzy search where a few characters could be different we call this a lexical search if this data was just stored in a regular database and I'm using natural language there's a lot of flexibility if I try to perform a traditional exact match search on the words it's not going to work very well when I'm in these natural language 

environments those lexical searches which need the exact term or maybe a character or two out it's just not going to function very well I'm not going to get good responses and it's not going to work when I have things like images and audio it's going to break at that point and so how do I solve that challenge and especially if we think about with computers they really prefer working with numbers anyway so what we have to do is we have to take this and we need to 

run it through we call it an embedding model and what this embedding model is going to do is going to create this onedimensional array of floating numbers over a huge number of Dimensions that means it has Vector we think of hey Direction and magnitude but it's going to have hundreds or thousands of numbers to represent the data but it's not just going to represent the words the whole point of this is going 

to represent the actual uh meaning it's going to be an interpretation of the information so that semantic semantic meaning of the context not just what was the actual basic input and so this data we're going to run it through and 

embedding model now these em embedding models have been specifically trained to perform this task this is not the same model as the large language model this is specifically trained to create Vector representations of the input now a very common one you'll see is a O2 and that's actually what I'm going to demo here so the whole point of this is I'm going to send 

it my input and there are versions that can work against text and documents I can do it with images typically then it's going to use image to understand what's in the image the context of the image and then apply it to the vector audio the same videos I can take all of these things but the net result is it's going to spit out for each of those it's going to create a 

Vector representation so this huge array of floating points it's got be much bigger than this um etc etc and then obviously it's going to store them so I'm going to go and store that in something some just draw this and this is going to be my semantic index so the whole key of this is going to 

store those values and it has its own index specific to these vectors that it's generating which is in a science unto itself to actually create those um indexes that's going to then enable us to quickly go and find things in there and so for a bit of fun fun to give you an idea so I went in and I've created an instance of of the Ada O2 

model and all I'm going to do is here I'm going against my particular version I've created and my input is can you tell me about embedding models now obviously I could put in anything I want hey you tell me about pizza blah blah blah blah blah I'm going to run this and I can convert the output which is Json into some objects so we can see that completed if I then go and look at the 

embedding the actual embedding not one character well there's a lot of numbers all of these floating points how many is there well it's 1536 it's always 1536 with the Ada O2 model but we can see the whole point here is that yeah we got this embedding back which is the vector representation of the meaning the semantic meaning of my 

input and then that would go and be stored and utilized in other places for how we're going to use this in the future and that's really the whole point of this the whole idea of these embedding models is whatever that input object is the embedding model will then allow it to be described in this vect VOR space so now we have this number this 

representation of it now if it was a very large amount of data it will chunk it up it will break it into chunks to enable it to run through and be stored now when you hear the term embedding and you hear the term Vector they're very often used interchangeably I guess to be the most accurate the embedding is the representation of the data in a structured way whereas the vector is that numeric representation but again um you're often going to hear them 

interchangeably but the point is now these vectors represent the meaning that semantic meaning of whatever the input was so even if the words were different it understands the meaning so like inputs will have similar vectors they're going to be on a again I I can't visualize 15,36 Dimensions I can barely visualize three but you can imagine there's that 

Vector that represents and so there'll be similar vectors if that input is similar as well it's probably easier to understand if I try and put this in two dimensions that's basically as much as my brain's going to handle so in two Dimensions if we think about it for a second then I would have this idea of um that idea of a 

boss manager leader they would all be grouped close together if I had cat um kitten and remember it would work with pictures so if I had a picture of a cat that was actually distinguishable as a cat it could also have that as a vector and so that would be close as 

well so it's going to be a to merge these different things together so now in those two Dimensions I can get the idea that things that had a like semantic meaning will be closer together their vectors will be closer together if I think of having those 1500 Dimensions think how richer those meanings can actually be so my whole point is I'm building up my semantic index that has all of these vectors in 

it which now makes it more retrievable by my solution now as I showed there I work in the Azure space so this is um Azure and the Azure AI search which was formerly known as Azure cognitive search so that does the job of creating these embeddings and it can get that from blob from aqal database from Cosmos DB dat Lake Etc it handles cracking open open the files it could be a PDF or whatever 

chunking it up creating those vectors and they're designed for the very fast retrieval and similarity search that's really a key Point you'll also hear today about a number of database services are starting to hook into AI services like Azure Cosmos DB for mongod DB Vore Azure postgress secret database they now have the ability to call into AI services to go and get those Vector represent s generated and then they get 

sent back and they can store them and then they can perform Vector searches as well so this why you keep hearing about Vector search and embeddings it's key to the whole point of making these large language models work on your data it's why if you want to do Microsoft 365 co-pilot it talks about having to have the semantic index enabled for your organization hey your Microsoft graph it has to go and create these vectors for all of the data in it to make it function okay so so what does all this have to do 

though with actually doing something actually using this well remember I have some question I have something I want to be able to find against all this data so now as the user well that user has a question but the question goes into the same embedding model which means the question now has a vector generated for 

it so now the whole point is not that so now the whole point is we do a semantic search and that's the end result we really really care about the whole point of the semantic search is these systems have the ability to mathematically go and find the 

smallest angles between those vectors I.E the nearest neighbor and I could maybe say hey I want the top three nearest neighbors return to me and so even if the original words were completely dissimilar it doesn't care because it's based on the semantic meaning of what I typed in so if my question here was based on the word chief for example I typed in Chief well semantically they'd still be close 

together so it would be able to find responses that talked about boss or manager or leader or any of those things so the net result would be when I think of that retrieval augmented generation I'm going to get the closest data I'm going to get the highest quality the nearest neighbor and that's possible because of these embedding models that create the 

vectors that represent the semantic meaning of all my data that then create one based on the semantic meaning of my question find the closest nearest neighbors based on those vectors and a whole lot of really clever math and so now the end result is I'm going to send the highest quality nearest neighbor data with my prompt to large language model so it's got the best input the most relevant data so it's going to give me the best output that is the whole 

point of that and this is why those concept of vectors and embeddings and semantic index and semantic search is so important without that I would not get quality results against the data that's going to enable it to do its job that's why we focus on that so much if I just did text based queries it would not work now you will hear Concepts like hybrid retrieval because funny enough the semantic search 

is not great at exact matches I'm trying to find this exact skew maybe a part number well that's actually where an exact match electrical search would give a better result so what you're seeing in a lot of these Solutions Azure AI search is it will do a hybrid search it will do the semantic search against the vectors and it will do electrical search against the exact words and then it will fuse those together and then it will run other algorithms on top of that to find the best possible results which it then 

gives to the orchestrator that then adds to the prompt and sends that in and so there you go I mean that that really is everything that's a fairly high level but that's why it's so important the large language model is not retrained every time we send an email or anything else that's impossible the whole point is it doesn't need to be we have have the ability to add additional information that we retrieve 

from A system that will augment its ability to generate a quality response and what enables us to retrieve that great information is we take all our information we create a mathematical Vector representation of it based on its meaning its intent that semantic meaning through an embedding model that we store in this index that is designed for fast retrieval and to be able to do those searches for nearest neighbor the 

closest the smallest angle between them that it can then give back to me that we can add to the prompt and we get great results I hope that helped I hope that was interesting I thought this was really really cool as always till next video take care
