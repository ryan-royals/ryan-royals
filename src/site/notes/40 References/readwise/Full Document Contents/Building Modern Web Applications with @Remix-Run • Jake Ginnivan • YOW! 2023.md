---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/building-modern-web-applications-with-remix-run-jake-ginnivan-yow-2023/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/O9hxS1bQY78/maxresdefault.jpg)

good afternoon excuse me whatever's going around so this will be fun uh good afternoon everyone I'm going to be talking to you today about building mod modern web applications with remix uh who here has heard of the remix web framework before we get started just as I expected a handful of you um it it's one of these Frameworks that uh when I first saw it I was like 

oh wow this is this is actually a direction that I I think the web should be going um and so today my goal is to really share with all of you how the remix web framework will kind of get us back on track and remove some of the complexity in the web ecosystem take us back to some of the fundamentals and uh and yeah so my application that I'm going to be showing today is called Bic beats uh it 

is a DND inspired Spotify clone uh and it's a really good example because it has the properties of a web application you get to browse through various playlists um song lists get artist information they're kind of properties of a normal website but then it is a full client application so we want to play our music we want to skip if I'm navigating around the the the the site I 

want my song to keep playing so it's a nice really it's a really good example of these like hybrid apps that we we kind of we're using single page applications to build but remix Bridges the gap between a traditional web apps and S the complexity of single page applications little bit about myself before we get started uh as Michelle said my name is Jake ginan you can hit me up on any of the social 

uh I am a principal consultant at a consultancy called Arana uh we we tend to focus more in the Azure space uh but I my focus there is kind of building internal product IP reusability and and making sure that we're we continue improving our consistency across all of our different engagements I also help run DDD Perth which is a large conference in Perth uh Community Conference held on a Saturday um was really really cool if you ever get over 

there highly recommend uh DDD Brisbane was here on Saturday uh and recently I've just launched through Arana uh a product called feature board so they're the things that I'm kind of focusing on at the moment before Arana I worked at seven West media uh my team and myself built thewest.com.au and Perth now and finally 7news.com.au so we we really wanted to pick newer web Technologies 

and and push the bounds of of what you're kind of used to with the with news Stacks um if any of you have visited a News website without an ad brocker on who's done that yeah it's a terrible experience right so um the problem with the like all of this advertising when free products is that there is a heap of JavaScript that has to be loaded and then when you na ating around the site 

every page transition you've got to load up a whole lot of JavaScript again the browser's got to repaz that so we wanted to kind of follow the the way that Washington Post and New York Times had had been going and build web stack using react there wasn't any nextjs at the time there wasn't any kind of serde rendering Frameworks it was all kind of vanilla react and we built our own server side rendering framework called project Watchtower and so building the 

service i' rendering staff understanding how we can uh load the data and then make sure we uh don't render too many times and all these fun problems that you you hit when building one of these Frameworks gave me a real appreciation for the the problems that they're trying to solve and that kind of gave me the perspective when remix came along I was like ha that's kind of what I want um I I'm not a huge fan of the complexity and the non-standard way some of these other 

Frameworks work before we go too much into remix I want to kind of take you on a journey of the web so far there's really two types of web applications we've got the multi-page web applications and single page applications it's a bit of a spectrum so I'm oversimplifying it but with your multi-page web applications we load the page click a link and it loads another page each of these are new essentially 

new instances of the page um there's a heap of really good properties about this type of application as opposed to single page applications you launch an empty HTML page and then it loads some CSS and and JavaScript and then the app boots up and then it renders all client side so they're they're broadly the two types now it's I find it really interesting why did we introduce all of the complexity that comes along with single page web applications like 

multi-page web applications have worked for years they're they're incredibly scalable they they leverage some of the the fundamentals of the web that have been around for a long time um so what ended up happening is a multi-page web applications we started using a bit more JavaScript and started creating these enhanced pages so if you visit a page then a whole bunch of JavaScript and loads it gives you client side 

navigation like toggles forms on and off could be clients like Gmail where you get a whole email browser that sort of thing um we just kept creating more and more complexity here so typical devs just throw more JavaScript at the problem uh this is what ended up happening unfortunately but what was actually happening in reality is we were building two applications the first application was our still 

multi-page web application the second was a JavaScript application so the the first applications written in a backend language whatever your choice is PHP all it needed to do was be able to handle requests and render out a view um you there's heaps of web Frameworks in all the different programming languages it has support for form validation it renders HTML um the second application is written in 

JavaScript it has form validation logic often implemented twice and the problem with this model is the second application is up updating the HTML of the first application this type of coupling between two applications is there's nowhere else in the software development industry that you you'd actually introduce purposefully this sort of coupling and so it just really over complicated everything 

um but what single page applications uh enabled us to do is if we dropped that server component so now we just had went to back one application we could rapidly experiment with the web and that's kind of why we we introduced single page applications got rid of the server uh but there's a heap of things that we we needed to resolve we left the platform behind things like uh urls so many single page applications 

actually never update the URL so you can't send your current page uh forms the number of react form libraries out there is insane because you you introducing all of this client side state that the browser used to manage for you uh State Management we had cookies we had local storage we had all of these things that uh was built into the browser and we had to build these again SEO and 

accessibility way way worse in react applications and I'm I'm singling out react because that's been my predominant uh single page application language but most single page application uh Frameworks suffer from these problems but the way I like to look at it is Spar were actually a little bit of a detour for us they allowed us to rapidly experiment with the web ecosystem they they we experimented with build tools how we could introduce hot 

module reloading um all sorts of CSS and JS and and push the boundaries of of of all of these different tools there was heaps and heaps of innovation there for me remix takes us back a little bit re-embrace the platform and goes back to all what we were trying to achieve with that multi-page progressively enhanced application but without a lot of the the 

drawbacks for those that haven't heard of remix it's actually backed by react router the the team behind that is built on top of react router which is an incredibly popular open source framework um the guys behind react router run a Consulting business called react training and they did that for seven or eight years and did a heap of Consulting around delivering applications react applications and finally Shopify have become the stewards of remix a little 

while ago they were building their own hydrogen framework using react server components and then they kept looking at what the remix team was doing and they're like let's just sponsor them so they can just keep working on it um so this this kind of gives you a really good signal that it's not going to go away Shopify have a really good reputation for just supporting open source in the long term letting that project uh mature in its own way um and 

it gives you the the certainty that if you pick it it's going to be around for a while because now if you do a new Shopify storefront it will be built on top of remix so it it's it's going to end up it's usage is going to just continue growing so the best way I've heard remix described is it is a center stack framework for react what do I mean by that well if I've got 

the browser and I've got my server those two things need to talk so I put in a URL and the browser knows how to turn a URL into a request to my server it then gets a bunch of HTML back it understands the HTML it understands hyper media so I can click on a link and the browser knows that the hyper media means I want to navigate to the next 

page so I click on that link and then it will update the URL because the URL is updated the browser will go get that new page and return me some new HTML that HTML might have a form on it um notice there's no crazy form libraries it's just just needs a type and a name um and the form has a method and so the browser understands that if I submit that form I need to make a post to the same URL or I can specify the action and post to a 

completely different URL these are all built into the browser because of these standards and and knowing how to jump that Gap uh all of the web Frameworks knew how to pause the data that was serialized by the browser these were all standards so it was really really easy to know what you were going to get in the back end from your front end and then finally you can return either some more HTML or you can return a location header and then the browser will follow that location and update to 

the final URL which is a thanks we'll be in touch shortly so this is what the browser does for us and that's really what the center stack is it is the glue between your front end and your back end the browser provides that Center stack things like URLs hyper media navigation forms State Management these are the things that the browser does for us now 

when we talk about what remix is it is emulating what the browser does because we want to progressively enhance this website and if I navigate around uh I want it to like a normal web app but do all these as client side transitions using modern apis if the if the JavaScript is loaded um so it's really designed to emulate what the browser does cross the gap between the the the your front end and your back end uh and 

it's not really a front-end framework and it's not a backend framework a lot of these larger JavaScript web applications they know how to connect to a database and um and have these concerns with remix it just gets you to your server and then you can make an API call to another service in another language that is far more scalable than JavaScript so it enables it a lot of really flexible options there so really 

all all remix is is is it is a browser emulator a really really fancy browser emulator but why why do we want this well there's a couple of things server code is so much easier to write than client code as soon as you have state that needs to be managed over time it in complexity grows and so HTTP requests come in they're basically cure functions that have a request they make um not 

quite but make a a like database query and then they return the result so but they don't persist State between those requests unless you know how to look up that state based on the inputs it's also been built over many many years and this is why I said single page applications enabled us to really rapidly experiment because you don't want to experiment with a with the 

browser because if we if we experiment with the browser we all have to live with it forever um we don't want to break that platform it's kind of the guarantee of of JavaScript in the with the web is your websites that you created 20 years ago will still run now and the web and browsers are massively scalable HTTP solves caching and a whole bunch of other things uh it's accessible by default and it's reasonably secure browsers they enforce the security model for you 

so it's kind of the the model that we want um we but I don't just want to build websites I want to build web apps so I want to build my website and then enhance it without having to build two applications I also don't want to write react code at nearly as much if I'm just showing a form or rendering a page why do I need state why do I have to handle all of this complexity I just 

want the the same model that I used to have so let's jump into it the first concept that I really want to uh to cover is um routing it it's the first kind of important concept to understand so this is this is BIC beats um it is URL based so you can see playlist SL id/ artist and then another ID and that renders the the playlist but it also 

renders artist information how does that actually break down well we have a root component that is the layout for our entire application so that includes the sidebar all of the or bits up the top for our top bar I then go down to the next level and it is a nested route and that is playlist. ID remix has file system based routing that will match part of the path and match it down to uh 

the the file system routes so playlist. dooll ID matches to playlist slid parameterized and finally the last bit is another nested route which is arst slid the routing is file based you don't have to but I'm going to go through file based routing um there's a couple of really simple conventions underscores make that file name or that segment of 

the file name invisible to the URL soore player doore index that will match the root URL um remix will warn you if logically you have two routes that conflict I can then also goore player. library now this is really useful because underscore player I can introduce a layout component that's shared between those so I don't have to share between or routes and a whole bunch of other things um so you just 

keep building this out uh and and continuing on um with nested routes at each of these different levels but you can see here that I can introduce api. playay and that matches API doplay or/ playay in terms of the the URL um that's where that underscore player comes in that it's the the layout for all of the UI components that I want 

because I don't want to render my sidebar and top bar for my API riots or my orth callbacks or any of that sort of stuff so that's the first concept is is this file system based routing um and it is pluggable so you can you can either Define it in code or you can there's plenty of third party libraries that have different layouts if you would like the next thing is the data fetching cycle so there's three main parts around involved in dat data fing in remix first 

a route has a loader and that runs on the server as the request comes in if you're used to asp.net that's kind of like your controller action um it and then once that returns some data remix will render the component for that route and you can access the data from the loader in the component that then goes back to the client and it's serice side rendered what's really interesting is if 

if that was a client side navigation remix will use RPC and call your server to invoke the loader send the loader data back via uh Json over the wire is an API like an RPC API call and then your your component can use that um so it's really really flexible and and it kind of gives you that multi model either it can be done as a traditional web application or a single page 

application the the model is exactly the same for you finally we have actions if I submit a form that is the thing that handles post requests and put requests on the server and uh and you either return some HTML or data or a new location or redirect so this is kind of the cycle um and it it kind of guarantees that doesn't really matter if you are client side or server side 

your loaders and actions will always run on the server they'll never run on the client your components will be rendered either on the server or on the client whichever makes sense based on where you are and navigating and this is what it looks like we just have a module that's the route module I export the loader that loader can get access to http requests all the headers everything that we used to and it can return a response uh that 

response can have a status code it could have headers it could do um specify caching headers for instance uh to enable you to to leverage the browser's cache um you then have a default function export this is your react component and finally I have my action that can handle my put and post requests now these two the loaders and the actions always run on the server so if I'm doing a client side navigation or 

a a client side form submission it will make an RPC call to remix and remix will route it to the appropriate loader so that's pretty cool so what I'm going to do is jump into Bic beats and show you this search route uh and a bit of the data fetching so here we have um oops we have I'm G to have to revoke 

that now uh so we have various different routes we've seen that here we've got our different um like playlist create playlist ID those sort of things we have a playlist uh search route if I'm going to jump into Bic beats this is my search route here and I can search for what's a uh Brisbane band huh powder 

finger so I can search that and then I get my search results now what's really cool about this is I can navigate around um go into the different playlists this is just htif hitting the Spotify API behind the scenes um all of this is working with brows uh JavaScript disabled in the browser so it is just a traditional web application using um the normal request response this is a mult multi page application if I and reenable 

JavaScript and then search again I might have to refresh you can see that I get like the single page application where it updates the state so that's pretty nifty um what does that actually look 

like there's a few bits that make this work as I said there's the loader the loader does things like ensuring that the request is authenticated so grabbing out making sure that there's a session initializing the Spotify SDK based on that session it grabs the URL out of the query string and then it makes a API call to Spotify to search for tracks playlist artist that sort of stuff finally I return my Json to the 

client I then have this in my react component here I have this hook called use loader data now use loader data I use typescript to say this is type of loader and if I hover over that you can see that the type is uh understands what's been sent from the server it also does things really clever things like dates moving from the client to the server um 

sorry other way around server to the clients will always be serialized as strings so the types will do that for you and you get type safety from your apis across so if you're using an SDK um you noticing here this is all the types coming from the Spotify SDK they flow all the way to the client and I don't have to explicitly type anything this makes remix really really good for prototyping because you don't have to create your API contracts generate a 

client for the the server sorry a client uh from your server contracts and then uh yeah and and then try and worry about that contract between the client and the server what we do is just if I redeploy reload the application because the version's changed and uh off we go so it kind of is a really really good way to just rapidly iterate great for building out prototypes that sort of stuff but it can scale to all of my backends just 

like I'm calling the Spotify API here I could be calling my own backend apis that are using event sourcing or any of the um the the cool techniques that we've seen at Yao over this conference um I then can get the used navigation and I can see that if it is navigating it gives me the location that I'm navigating to so this is kind of this Progressive enhancement but what I'm going to do is 

I'm going to change this to an action and what I need to do is be able to instead of doing a get request that puts the question mark Q equals as a get request I'm going to make it a post to update to so you can see both um we still need a a loader 

and instead of this URL what I'll do instead is grab the action functions Z and then I can go const query equals request. form data now you notice if you're familiar with the web in general um and fetch what's been happening over the last couple of years is we've been moving away from Custom libraries like request and axios to introduce standard 

libraries like the fetch API to JavaScript um remix is built on all of those standards so as a side effect of just using remix you will learn the web stack more which makes it quite good for um quite good for like not having that vendor lock in you're just not learning all the specifics of the the framework 

cool um that all looks good instead instead of use loader data I'm going to go use action 

data this allows you to return data from your action and you can see that the types all flow through so that's pretty nifty um all of this can stay the same I can't provide the default value anymore um and I'm just going to change the method of this to a post um I'm just going to have to kill this I'll tell you why 

later okay cool so you can see oops I'll remove the search you can see here that it's not updating the URL it's just using a post instead and we still get the single page 

application so that's kind of the the the data fetching model for uh remix um you can also see here that uh if I jump in it this is actually a full-blown Spotify client I'll share the link later but um I can if I play transfer the playback it is a uh a full-blown client so there's quite a few bits of data that we're we're loading here I'm loading all 

the playlist data I'm loading some user data up the top I'm loading information about the artist and I'm also loading the artist's top tracks um the really nice thing about this is it gives us some performance improvements as well and we're going to jump in so a single page application you load we saw that white page earlier um we load the HTML first it needs to 

download pause and then it will trigger the loading of the CSS JavaScript fonts that sort of stuff static assets finally it will make an API call to go get the data around like who's the user that's logged in uh and then once it's got that it'll make further API calls to fetch more data you can see this in Twitter if you go to Twitter now you start with a spinner and then you get two spinners and then you get more spinners and it's about seven cascading Spinners and this is because of the 

single page application approach you can't render the child until you get the data of the parent um what remix allows us to do is move those initial API calls to the server and so we kick that off and then send the data back with the HTML um so your initial time to First Bite does uh or does slow down but the full page with useful user data speeds 

up quite a bit so what's really Nifty about this is uh if we want to do Progressive enhancement for instance um I will jump in in a second but um I'll demonstrate when I load the artist panel it's really slow like I click it's a really crappy user experience so what I'm going to do is 

fix that um ideally you can just make your backend fast that's the best way to fix any web application um but ideally like sometimes we can't we we don't support like we don't control that backend API or it's too expensive to fix or whatever the reasons are um so we are going to work around it by just creating a better user experience I'll quickly demonstrate what the problem is so if we jump in 

here and go into hot hits Australia and then click on Jack harow waiting waiting waiting waiting bet Spotify is like died me or 

something let's figure out what the problem is okay so this is my um nested artist and this is my playlist so um the uh the way that we display child routes as you can see I'm not actually getting that panel is I render a comp specific component 

called the outlet component and an outlet just allows a route to render child routes so I'm going to Chuck this into here now if I click on Jack or whatever you can see it's pretty slow so click on Beyonce finally loads really really slow it's pretty crappy user experience this is supposed to be a single page or like experience so what's happening well in 

here I've got a really slow API call that's getting the tracks um what we're going to do and this is where you get some really really Nifty levers inside uh remix is we can go instead of just rendering the outlet I can render navigation Dot location as we saw 

before a path name so this is if I'm navigating to this path and the path uh starts with um 

so if the path name starts with playlistplaylist id/ artist so I'm going to that nested child route I will render a div class name equals artist description what detail 

style then finally I will render a loading dot dot dot 

otherwise I'll render the outlet so what I'm trying to do here is which I've got something wrong somewhere which I will spot in a sec after I explain it um what I'm trying to do is if I'm navigating show a loading like bit of loading text so I can see that I'm navigating to that next page uh just to give the user an idea that something is happening 

um cool so over here now if I click Paul Russell I get a loading uh and then it loads in so that's pretty cool we've now kind of started this Progressive enhancement but we can do better than this with remix um remix just gives you a whole bunch of different tools one of the really Nifty features is if I instead of returning Json in this I can 

return a um defer instead now a defer allows us to come on why are you not any a defer allows us to return a promise over the wire instead of data so if I go top tracks and remove this a weight you can see top tracks is now just a promise of the the top track results this obviously doesn't work down here so 

I can render a suspense boundary so suspense is a new technology inside react 18 that allows you to kind of load data and uh gives kind of reactor understanding of what data is it loading so we can provide a fallback component if any children under this suspense boundary is loading I can then use an weight component and I say I'm resolving my top 

tracks and I move this all up as a function so the await component will only render its children once that promise has resolved and I'm missing my close for the suspense okay so a pretty minimal 

change and it's allowed me to return a promise over the wire now that's slightly different because previously without that if I if I refreshed that page I would get a um a delay that page load now if I refresh you'll notice the top tracks are actually in a loading State for the server side render up show why that's 

important so this was our our waterfall of everything happening before you'll notice that we are slowed down rendering anything because of that really big slow request um so if we do the optimistic UI what that that allows us to do is pull that in but only for client side navigations 

we're still slow on the server that initial page load by using defer that allows us to to pass the promise across the wire and then remix takes care of streaming the result across so that's pretty nifty so really like remix is two things now it's a it's a browser emulator but it's really just a toolbox that gives you all of these tool tools to create a fully Dynamic UI by 

progressively uh enhancing what the browser has there's a couple of things that I want to cover uh before we wrap up the first one is vit so vit is a uh build tool that's come out relatively recently and it replaces tools like web pack uh it's extremely fast um because 

it really leans into the esm side of things uh if you're aware of esm is the new JavaScript bundle format at the moment remix is has its own compiler and it is its own web framework um the Nifty thing about where it's moving is remix is becoming just a v plug-in rather than an its own closed comp that you can't extend so that's the first thing um that in terms of where 

remix is going the second thing is around react server components if you have been watching X uh recently like the nextjs comp for instance you would have seen a heap of uh like heap of talk around react server components remix is far less bullish than versel around react server components but you will see more and more react server components inside 

remix uh as they stabilize the first thing that they're going to do is allow you to return react components on the server to the client so inside your loader I can return a react component that will serialize on the server send it across to the client and then I can just render that component on the client what's really cool about this is you don't have uh any of that like 

JavaScript for that component isn't in your client bundle all of that stays on the server so that's really really cool when say you're rendering uh markdown into react it's a real pain because you have to either pass HTML across and dangerously set in HTML and all all those sort of hacks to make it scale um this is a a really Nifty way to to kind of get around that there's going to be a lot of extra uh react server components um the remix 

team are expanding the apis over time uh so they can once all of these things are stable they'll start collapsing and the way they do that is with these future Flags so future Flags allow you to opt in to Breaking changes so at the moment remix is V2 and you can opt in to uh a feature called fetcher persist and then it is a braking change but it allows you to opt in to every breaking change over 

time um and gives you a couple of months leadup so when V3 gets released you just upgrade there's no braking changes you've already made all of the braking changes reducing your risk so as they add these different apis and those apis come in to react and react server components or server actions solve the problem that remix first class apis already have they you'll be able to opt 

into that and start using the new way if you'd like to look at baric beats uh that is the GitHub URL I'll share the slides after um and I really encourage you to just have a look at the quick start and play with remix it's there's a heap of cool tutorials on the optimistic UI and all of these problems that are really really difficult to solve Like Remix if you start if you submit a form and then navigate it'll try and cancel that 

request just like the browser does it handles all sorts of concurrency problems that you just you don't realize are there the the team make a huge amount of effort to solve these really hard problems that just make it quite amazing to use one of the uh um I should have added it here but uh there's a bunch of remix singles they're called that Ryan Florence does and he records these 5 to 10 minute Clips um he's 

recently been building a Trello clone and one of the things that are quite challenging is if I'm adding a task and then while that's creating I'm moving it to another column for instance there's a heap of inflight requests dealing with all of that very very hard remix does it extremely well and elegantly the apis are very very well thought out so that's been building modern web applications with remix uh we've got some time for questions so uh hit me 

up
