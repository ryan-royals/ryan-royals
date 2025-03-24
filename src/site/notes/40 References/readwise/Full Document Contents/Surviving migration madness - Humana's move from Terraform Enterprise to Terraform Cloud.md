---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/surviving-migration-madness-humana-s-move-from-terraform-enterprise-to-terraform-cloud/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/sZn_yERFYUk/maxresdefault.jpg)

[Music] all right it's morning right good morning so really quick before I forget early detection saves life first stage Brer or breast cancer survivor so I wanted to mention that CU it's October all right so let's get started thank you so surviving migration Madness yeah 

human did move from terraform Enterprise to hcp terraform and it was a lot of fun so hi my name is IET via and I am associate director of automation engineering and advancement for human down here I have Jamon Joshi and he is one of my senior engineers and he played a key role in our migration success so Corner him later with all your questions because um the wonderful product that 

Arman talked about yesterday terraform migrate did not exist when we started our Venture so um thanks to Thomas which is back home and Jamon um we were successful with our own automation so a little bit about myself my background so I have been with Humana for a little over 2 and a half years uh prior to coming to Humana I was at American Express Global business travel um there my then boss which happens to be my 

current director he and I stood up the site reliability engineering organization so SRE for those of you familiar and uh as my friend Shashi says one of my Sr Engineers that's where I got all these Grays as well so yay so after about a year of running the SR org and our phones were ringing at all hours of the night and we were best friends with the major Incident Management team we decided we needed an observability 

and automation team so we needed some monitoring some alerting and hopefully some self-healing right and that was the evolution so for those of you who are not familiar with human so we are a Health Care Organization we're currently servicing over 16 million members across us Washington DC and Puerto Rico we've been around for over 30 years and we have over I'm going to stop doing that I 

swear we have over 67,000 employees my team sits in uh part of the organization that's responsible for core Enterprise Engineering Services and more specifically my team is automation platforms and we are responsible for things like terraform and anible and a few others so 2,6 95 is the number of workspaces and five 

was the number of environments right so this basically sums up the data that was available to me the day that we decided to move from terraform Enterprise to hcp terraform and so for those of you that are familiar with Enterprise it's your infrastructure it's your database it's your data to retrieve so first things first we needed some data we needed a lay of the land 

and fortunately due to the nature of what my team is responsible for I have a Powershell Master on the team so within no time we had some data so what did the data show us first it showed us a breakdown of the 2,695 workspaces by environment as you can see we name our environments very fancy metadata there a through e and so um the other thing that it it 

showed us was and this graph if you're looking for it it's not on there it also showed us that we had almost 300 approved modules available for users we didn't have visibility to the utilization of the modules so I knew I had 300 modules that could potentially be utilized at any time what else did the data tell us this one was scary when I put this pivot together the 2,695 work spaces were spread across 132 

organizations within human the data also showed us some good stuff though it showed us that there were some optimization opportunities that existed for over 500 workspaces and what I mean by that was the footprint of component to workspace utilization could be simplified and we could then have a a smaller footprint in in workspaces for particular teams in particular 

organizations um so what we knew is we could reduce our workspace footprint prior to moving all right so what did we do next well it was time to plan the work right we started by building the runway so a big thing for me was simplifying the migration and requiring a minimal level of effort from our tenants and 

from all of our dependencies so networking and everything else so when we talked about standing up our hcp terraform agents we decided that we would use the same name space as our existing terraform Enterprise agents next we needed to build automation so we needed to create automation because the automation available from Hashi at the time so terraform migrate wasn't 

available and the automation that was available would require us to move all of our workspaces at once and as you guys can see from the complexity 132 organizations five environments and 2600 workspaces that wasn't really going to happen so we needed to find a way to do that on our own so we built automation to create the new workspaces to copy the variables over build the team relationships ownerships and move State 

files then we also had two automation workflows that were used to build new workspaces so we needed to Pivot those workflows to start building hcp Terror form workspaces instead now one of those workflows we owned and we managed it was ours we could do as we wanted and so that was going to be easier than our second our second workflow was tightly coupled with another platform SL environment 

owner and we were going to need to work with them to build that Automation and make that pivot happen and then the third piece was the terraform modules so as I had mentioned we had over 300 or approximately 300 terraform modules that needed to be refactored for hcp terraform my automation platform team sits under automation engineering and my brother team which is service enablement 

was responsible for that uh so we partnered with them and obviously ensured that they were working within our timelines and really supporting um that that effort so next we worked on simplifying the journey um this is actually one of my favorite ones because so I mentioned that I've been I I've been with Humana for 2 and a half years what I didn't mention is I had been with Humana about a month when my boss said hey I really 

want to move to terraform Cloud how do we make that happen so my tenants didn't even know who I was yet right and here I am planning this huge migration and so I thought well do an introduction hi my name's Evette I'm new here by the way making plans don't have any dates yet and don't know what it's going to take but at some stage in the near future we will be migrating to I swear I 

feel like I'm doing the Twitter and exting but then it was terraform Cloud but hcp terraform right so the communication went out and then in the communication I took the opportunity to highlight the fact that there were some optimization opportunities coming so hey maybe a potential reach out on our end uh to work with you and then I called out one of my favorite things that the data told us and that was that we had teams that 

didn't always remember to delete their workspaces when they were done with them and so we might have had a few of those lying around um and so there was a great opportunity and optimization there because I knew we were moving and I was willing to have yard sales for sure and anything else to get rid of the things that we didn't want to take with us right and so I wasn't going to take workspaces that didn't need to be utilized or were no longer utilized right um and I didn't need to take over 

very complex um mappings of workspace to components so we worked on those and this was my opportunity it's huge because we kind of hit them with a lot of information so now I've told all these people we're doing these things and we don't know how we're going to do them so now we started to work to minimize that impact right to simplify the steps that meant getting together to understand what it was going to take for each 

tenant in their individual I'm sitting in front of my keyboard what is it going to take and then figure out what can we do for them which ones of those steps are things that we can do and which ones of those steps are things that we need them to do so obviously there were things that were um variables and things that are related to security that we would not be able to move for them and we had different iterations also of maturity right in terms of our 

deployments and pieces like that so we we definitely needed to identify what we could do for them and then what we did is we began working with the teams to simplify their workspace footprint so there were really only a handful of teams this was not all 132 organizations or that I don't know that I'd be done yet uh but we had a handful of teams that had a huge foot print and a great opportunity and so it 

really was a win-win I didn't have to do a lot of convincing even though there was level of effort on their part what I did need to do is provide an engineer that had the vision and could guide them to what we were recommending so they can make that happen and of course we also built some automation so that we could go in and clean out unused workspaces based off of some criteria that we had determined 

right created a policy communicated to teams and so uh we built that automation to start doing cleanup as well so these are artifacts of our simplified migration path so at human we have some internal governance processes that I won't tremendously bore you with but these Graphics at the top are actually artifacts from our governance 

process and the documentation that we submitted the intent here was really to highlight that it will be simple it's a big ask in terms of number of workspaces but in terms of level of effort to to our tenants it can be mitigated and controlled so what we show on the left is environments a through e uh those tenants could move interdependent of one each of of one another so at any point whenever they were ready they could move 

um we obviously start by again oversimplified standing up terraform right we copying over their workspace and then they would be moving their variables and they would be doing their validation and then once everybody did that I could Sunset terraform Enterprise wo and then on the right what you see is we have one environment e that required all of the workspaces to move at the same time and that would be 

controlled by the platform team that own that environment uh this is also the environment that had the workflow that was creating their own Enterprise workspaces and they would have to build automation to adjust that so after months of working our simplification and optimization getting our Runway built so infrastructure all those good pieces um 

some of our governance processes we were ready to actually welcome people into hcp terraform at that point we had 1941 number of workspaces and two migration paths so I would be lying if I didn't say I was very excited by this point so Ready set go yes environments a through D so so hcp terraform is open for business 

we're excited a communication goes out to all the teams notifying them you can request at any time now to be migrated over right we execute the automation to actually create the work spaces and move their variables and all that and we're waiting for them to come tell us just move my state file I'm ready also to support we created rapid migration sessions so rapid migration 

sessions was something really successful in my previous life and we'll get into that in the lessons learned and I thought it would be amazing to create sessions Wednesdays and Fridays where teams could come and migrate with Engineers that would be there to answer questions and help them out right so teams were invited everybody that they needed was there and available and we did have some teams to show up and we did complete some migrations 

so 1% that's the percentage of workspaces that moved after my announcement so I like to call this the truth hurts cuz it does um we were excited right it was disheartening but from the conversations that I was having with teams either the ones we were working to optimize with or just teams within my you know my blast radius as I like to say um one thing that was the common denominator is that 

they had competing priorities and I really was offering them the door was open but I wasn't telling them when I was closing the other door and so it was time to Pivot so in thinking about those conversations and thinking about where we were we needed to come up with a different way so we decided we'd move them we basically migrate for them and the one thing that we would need them to 

do is bring in their sensitive variables and the things that we did not have access to so we also knew we needed to build automation to lock their TF workspaces right so we scheduled a migration for them we built the automation to lock those terraform workspaces for environments a through D we communicated to the teams that their TF workspaces were not going to be available after 

that specified date and we gave him time we won't talk about how much time but we gave him time and then we executed the migration on the specified date right till the automation scripts ran we created the new workspaces variables all the relationships and we moved their state file and we locked their Enterprise workspaces yay four down one to go all right 

so it was all along we were working with the team that owned environment e but just like all other teams they had competing priorities and their environment is a significant environment in our road map at human and so there was a lot of bartering negotia no I'm just kidding there was a lot of working to ensure that we were going to get the cycles that we needed from the team members and at what point right so we worked with them we aligned on when they would be able to move and we sent out 

the communication very similar to a through D let them know what their migration date would be and then we executed the migration on that date so this is what I wished for when I was planning my migration Journey right it be like yay we start here and we trickle down at the end I clean up and I'm good to go this is actually what I got 

so the red line depicts the number of licenses cuz I like to really live on the edge and I told my rep which wasn't Sue at the time I told my rep yeah we're not going to need more licenses we're going to be just fine you know I'm super excited everybody's excited they're going to move we're good so anyway so as you guys can see here this little green star represents the time when environment e 

platform owners told us that they actually weren't going to be able to migrate and do everything that we were asking of them until April of 2024 so 12 months is what they were asking for about here this is when I started stressing a little bit about the license count maybe just a little bit I might have had nights that looked like this I don't know I don't know this is what happens when 

you tell AI to give you uh I think the prompt was woman counting workspaces as she sleeps so for those of you that that wanted were interested in the prompt I'm pretty sure that's what it was so anyway so green star shows when they actually moved when we were ready to you know start migrating uh or I should say getting rid of the workspaces we were using to manage the platform the workspace they were using and and all 

that good stuff right so if we look back um I think this is something I would have wanted to know right off the bat in my migration is kind of how am I going to spend my time do I have the right oh I can't believe say do I have the right people on the bus do I have the right people on the team you know do I have the right resources and skill sets so the majority of our time I would say was split between communication and collaboration m maintance and optimization and planning right in 

planning would go um contract negotiations the strategy the data extraction visualizations analysis and it really was plan due check right coming back um communication and collaboration was huge so uh I purposely started each one of the uh slides on communication simply because I did have a few people that said I 

didn't know this was happening but for the most part that did not happen and we're talking about a lot of users right uh I communicated uh what was coming and what I did know and that's always challenging and most people are hesitant to communicate and I've been one of those when you don't know all the answers right you don't know everything but I think um we have learned that it's nice to know what to anticipate and so communic Comm unication was huge collaborating 

with teams and the teams that were able to optimize their workspace consumption was significant right as you can see we spent a little sliver of time in our internal governance board right so that would be for example the simplified um migration path artifacts and and those came from that process um and I think most companies will have something similar through their Enterprise architecture Department uh ter form modules right 

refactoring so that definitely happened in partnership with our brother team and um but that that was one of the prerequisites to moving right I needed Runway I needed infrastructure there so I needed them to be able to access hcp terraform but they were used to their modules ready to gou fully baked with the blueprints from our security department right they don't have to think about those things so that was a a big piece of it the maintenance and 

optimization helped us to recoup workspaces um I call that the you know yard sale and going to the thrift store making donations before you leave everything that is removing clutter right I looked for those OP opportunities and since we were building Runway there was time to do that and then as you guys can see the moving of the workspaces was a much smaller piece especially when you move them for them 

my roller coaster ride so let's talk a little bit about the lessons learned the 1% these are not the people you know making 99% of the money that's not what I'm talking about here I'm talking about the 1% of the people that moved right or so what this taught me was that my excitement doesn't translate to everybody else cuz they're busy right and some people were excited and they were the first ones came knocking on the door they were waiting for us to be able 

to give them those workspaces but then everybody else they were busy right so dates help with competing priorities that's huge I feel cheesy using this one but so true so plan to check act so and be ready to adjust your plans um a few times in this migration as we were looking at some of the reporting that we built to track state files and update dates and who's using what and where we just realized that the migration 

wasn't moving the way that we wanted to and it gave us an opportunity to adjust our plans right so we never thought about admin users on terraform Enterprise workspaces and so as we were monitoring the progress of a migration what we found was that a user had unlocked themselves in terraform Enterprise and gone made updates done their releases they were good to go and so the State file that was sitting in hcp terraform was out of 

s so uh we reached out to the user made sure he understood what the issue was we resync the state file and then we wrote a little bit of automation to strip all the admin rights out of all of the workspaces so that we wouldn't have this problem moving forward the other thing is uh that I hadn't actually mentioned prior to but this was important was so users were worried we were a little 

concerned we had never done this we're going to delete a bunch of I delete 2,000 workspaces so what we had told users is we'll hold on to them for 60 days right and that way you could feel warm and fuzzy that no matter what it's sitting there and so um that was a big part of us having to strip out those permissions because those workspaces were going to exist for 60 days know your limits you can think of this one however you want but in my case as I needed to Pivot I was coming up 

against a change freeze right so I don't know depending on your industry um when I was in the travel industry in September we would do hard freezes no changes busy travel month and um so we were going to be coming up on a change freeze so I needed to understand that and weave that into my plans along with understanding my governance processes so those artifacts and those pieces that that came out of that um because I weaved that into my planning I was able 

to reuse artifacts I was able to tell the same story across the board it was always the same messaging so understanding and knowing your limits and knowing how to weave that in was important I love data data nerd and so data is everything right extract good data and create dashboards to track progress um or lack thereof like ours was uh but the data really told us a lot right add user somebody unlocked themselves things like that uh the data 

told me I had 132 organizations to work with at the beginning and therefore I knew that communication and collaboration was going to be key to the effort so I stole this from Steve Jobs great things in business are never done by one person they're done by a team of people so the success of this migration was only possible through the collaborative efforts of many teams at human I wrote that down cuz I wanted to 

say it right so but seriously from the teams that worked with us to optimize their workspaces that trusted us and said oh yeah we're really busy and we promised our leadership all these things but sure I'm going to do your initiative and um from my team so Thomas back home Wes even Doug and the rest of the team um our our platform teams that worked with us um it was an amazing journey really sets us up to start U utilizing uh hcp terraform the new 

capabilities and things that are coming now we've formed collaborative relationships with teams that we may be coming to later and saying hey new feature now I know which teams could use which features right so there were a lot of wins in the process in terms of collaboration and communication and working closely with those teams and respecting the fact that they have initiatives and their own deliverables um I think that that really helped us be successful so thank you 

[Music]
