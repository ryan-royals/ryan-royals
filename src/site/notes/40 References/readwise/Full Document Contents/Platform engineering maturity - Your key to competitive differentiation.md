---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/platform-engineering-maturity-your-key-to-competitive-differentiation/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/l0vzDJwTm30/maxresdefault.jpg)

[Music] hello everyone uh my name is Hikaru Sao from Eon smart technology uh I'm very honored to be here uh today I presenting on how Eon has enhanced its technological maturity and Market competitiveness uh through platform Eng 

engering our goal is to rever technology to provide the best experience for our customers thank you for joining let me introduce myself as I mentioned before my name is Hikaru Sito from Japan and I lead both uh the SR team and the and the platform team I'm passionate about kubernetes a t home and V 

I'm certified as a kuest note and hold hash cope certifications this C code links to my ex account so feel free to follow me uh if you'd like but I not in Japanese do you understand uh onto the main presentation uh Eon is the is one of the most uh biggest ler company in Japan uh 

it was founded in 1758 H and today we have over 300 subsidiaries and more than 600,000 employees and operate over 177,000 stores across 14 countries throughout our history we have continuously grown and evolved to better serve our customers expanding into both physical stores and online 

markets uh we are developing div diverse businesses with a focus on retail and and as a group we are working to enhance business value specifically we have business business in finance Healthcare supermarkets and more and the Synergy between these is an important factor uh here uh I would like to highlight 

ion's philosophy gives a central P pillar Wheels in Japanese D it means adapt to changes in the environment and transform the company itself this is an expression that symbolize the agility of a company and has become an important philosophy in engineering as well uh today I'll share how Eon uh has 

achieved success in engineering uh by applying uh this philosophy the retail environment is changing rapidly customer Behavior Lifestyles and technological innovations are all influencing our business as customer expectations increase we focus on delivering a CS shopping experience 

that integrates both physical and digital elements e uh digital transformation challenges consist of four keys at first transforming its business into CS shopping experience that integrates both physical and digital elements second building a customer Centric equ system through the use of 

Technology third uh creating new Revenue models uh through data integration finally uh reamping existing operations by using uh data and AI to achieve this uh we have set set several Q pills customer centricity aity security and governance and data driven 

decision making by focusing on these areas we are building a sustainable and competitive platform and then uh Eon smart technology leads the digital transformation of eon group and promotes inter uh insource development we have introduced agile methodologies and uh fostering a new culture that aims to uh enhance 

technical capabilities across the organization now uh I would like to address uh journey to obtain higher platform engineering maturity uh first uh I share history of cloud adoption we have been using the public card for over eight years uh mainly utilizing uh 

as uh however as our business have gone has grown complexity and cognitive load uh increased have increased leading to inconsistent architecture to address these challenges we have Focus focused on advancing our platform engineering the primary goal or platform for engineering is create an environment 

where the applica application development team can focus on their core activities by reducing the uh cognitive load for developers to manage INF infrastructure and tools we a to ensure that they can provide the best possible customer experience Ally this allow us to maximize the value we deliver to our 

customers when starting platform engineering one key consideration was to avoid beginning with the introduction of internal develop platform uh everyone here knows there is an exent product uh of course Waypoint or boxy something like that uh however uh we need needed to establish 

foundational tools infrastructure processes first the following is a quote from an article by Wy uh titled platform engineering the next step in operations the fantasy of platform engineering is one quick deployment I strongly resonate with this statement let let's take a look at the 

overview we are we are implementing platform Engineering in four steps step one build team and reliability step two uh weeky and in inventory step three standardization and higher usability step four uh self service and IDP first let's go over step one 

the first step in platform engineering was team building and uh establishing reliability we initially formed a combined SRE and platform team working closely with the development team to identify and eliminate the high toil tasks this helped us build trust and enhance the platform's reliability 

what's important here is to start with collaboration you can achieve Self Service wide from the beginning by collaborating and maintaining close communication you can identify the issues through the process of establishing Solutions uh it becomes possible to turn them into services like ex service this is also mentioned in team typologies have you read this 

book and in this uh Team topologies it is further explain that while collaboration can be costly but it is ideal for exploring new approaches whereas Excel service models are suited for predictable delivery as teams deepen their understanding of technology and products through explanation uh the need for close collaboration decreases and the 

number of of collaboration targets Narrows uh as product and service boundaries become more defined uh many organization transition to ACC as a service in larger Enterprises uh this uh Discovery or uh exploration to establishment pattern is expected to continuously occur across 

across teams in different stages of deployment development here are some example of toil uh creating Cloud accounts uh detering architecture uh application deployment and platform stock deployment these are common example of toil uh but each one is fundamental and 

important uh in summary of step one uh the goal is uh everything from team building and reliability uh the outcome the reliability was built or reduction of human resources for deployment increased deployment frequency uh reduction of incidents to regard by deployments now next is step two Wiki 

and inventory The Next Step was setting up a centralized inventory of platforms and tools this significant significantly reduce redundancy of onboarding and education uh to F support developers uh we held internal workshops in addition to creating a comprehensive Wiki enabling them to manage infrastructure and tools more more 

effectively education will equip developers to with the knowledge uh to manage infrastructure and tools uh we don't rely solely on the wiy instead uh we organize internal workshops to facilitate Hands-On learning these workshops allow developers to engage more deeply with the platform uh gain practical 

experience and clarify and any questions they might have the platform team uh plays a crucial role in this process they act as enabler they support and guide guide development teams ensuring that that they are equipped to handle the infrastructure and tools themselves the goal is to foster a collaboration 

environment where running and support support are going uh by the way uh this is our technology stack for the wiki we use uh Aran conference and for the repository we use uh GitHub and uh a a develops ially you can get a sense of number of 

Technologies and products uh we are dealing with through this slide this also indicates the high cognitive load on the platform team which I will explain later in Con in conclusion of these steps the goal uh goals are reduction redundancy of on boarding in education and sharing knowledge the outcomes are uh decrease 

number of days it takes for few new employee to do first PR and reduction of support tickets uh it means uh changing requests and so on and increase tool usage now let's move on to step three uh standardization and higher reusability 

standardization and uh enhancing reusability were key to maximizing uh developer productivity we utilize tah modules to standardize workload infrastructure and improve the usability this allow uh developers to rec reconfigure based on their specific requirements uh using qu build uh templates and we have modularized each 

infrastructure component to make them usable uh like AKs or other functions up service a cach or databases and so on uh it would be uh beneficial uh to achieve the following uh for the six items below uh developers don't want to think about them and uh 

developers should ensure quality of them uh as on sh as shown on this page uh governance and security uh platform reliability observability cicd pipelines scalability they are just examples but it appes anything that application developers don't want to worry about and think about deeply 

uh to summarize this step the goal is to maximize The Rage of developer productivity and outcomes are uh short and late time to deploy the platform and reduction of Human Resources spent on design and configuration now we will uh discuss step four uh self service and and 

IDP uh as a future step uh we are planning to introd introduce self service and and IDP our goal is to improve the interface uh offering options like GUI cui or I and it depending on the developers skills and or preferences implementing IDP required 

specific UI skills which uh which we are carefully considering here I'd like to once again quote from W's article uh software developers probably already have tools and processes for managing the simplest and most commonly used paths which aren't necessarily the saying as we move forward with this step 

uh we must keep this in mind in mind it's important not to focus too much on integration so uh from here uh we will uh discuss uh team design when it comes to team design it's essential to revisit the structure based 

on the uh phase and situation of each company uh as the SR team goals uh we are considering splitting responsibilities uh to optimize scalability we aim to maintain two pict side team to ensure uh close communication while Distributing C cognitive load 

efficiently from here uh I will explain the evolution of our team design uh let's focus to the first phase of team design uh here we started with the smallest and simplest structure the SR team is responsible for uh platform engineering as well in this pH uh there 

are a few key characteristics uh it's simple uh arang for close communication with a small team it's easier to communicate and collaborate smoothly however uh scalability become becomes an issue and cognitive Road in on SR team uh grow 

as the team expands uh it becomes difficult for the s team to handle all tasks U leading to increased burden thus uh while we begin with a simple approach uh in the next steps we will address these challenges as we progress uh the next phase of our team design uh involves splitting the SR team 

into a separate platform team at it goes in this stage uh the SR team focuses on liability uh of uh services or products while the platform team provides variable resources such as Wiki inventory and templates this clear division of responsibilities allows us to operate more 

effectively this table shows the differences uh in the responsibilities between the SR team and the platform team uh the responsibilities of Sr team the the implementing Sr practice with the developer team through embedding or enabling and uh they are responsible for liability 

of uh products or services and this team is a customer or platform as well uh on the other hand uh platform teams UH responsibilities are uh reliability of the platform and uh they are focusing focus on providing Wiki inventory uh templates and useful 

tools as our uh next uh phase three at our current stage we have established a cloud Center of Excellence to further expand platform engineering across the group The ccoe is responsible for strategy and providing Direction and best practices to the teams this setup ures cons 

consistency and quality across the platform throughout the group in the future uh we are considering further splitting the platform team to introduce and IDP we aim to create specialized teams uh such as template team uh theb Team sorry team for platform are based on skill based on skill sets and expert 

expertise this specialization will allow us to expand the platform's fun functionality and Achieve greater scalability in the long term if you like uh uh you can for the sprit platform team in uh based on uh infrastructure area uh such as Network or datab bases and uh you can replace uh team 

design number three and four uh or proceed with them in parallel uh it depend it depends on situation and phase of the company and what suits for uh what suits for each company so what outcome uh have we achieved through this 

initiative let's take a look here are the main business outcomes uh over the past two or three years we've achieved the following results uh the number of teams has increased approximately uh sixfold and the number of products uh has increased five fold uh fold and uh we we've we've reached 10 million 

app downloads which is a a remarkably fastpac in Japan at the same time the number of critical incidents has been reduced to one quarter improving quality as well as a result we have improved efficiency and customer satisfaction maximizing a value of cloud utilization and uh platform engineering how do you 

feel that on the different note let's examine how we maximize our crowd maturity uh using hash cope products uh by leveraging hcp tform and hcp V we have automated infrastructure management and enhanced secret management this has reduced our op burden uh while ensuring scalability and 

security here is a techn technical overview of our platform we are utilizing uh hcp tform and hcp b b as core Technologies and uh to manage our platform in security as this page shows uh pag Duty or new new Ric uh is managed on 

hcp telone and uh I will explain why we choose to use the hash cope Cloud platform uh with uh regular uh telone uh managing the state of infrastructure or running with motor uh can become complex however hcp T home centralized these tasks in 

the cloud this makes it easier to maintain State consist consistency uh even when infrastructure changes are being made across distributed teams allowing for smoother operations within larger teams uh this leads to a reduction of operational burden or our team the platform automates many man processes 

allowing us to focus on higher priority tasks this leads to the scalability uh of the organization with these capabilities we can quickly Ena uh dedicated tform usage for new teams even as our organization continues to grow and we are often asked why we Cho choose telone over 

bicep so I share here uh the primary reason is the Tome is the defa standard for the infrastructures called langage and it covers areas that the single cloud provider cannot address additionally uh T home the state F offers significant advantages for maintaining in infrastructure 

consistency uh next hcp about hcp vote uh hcp vote offers best practices for secret management uh including periodic rotation Lis proes uh auditing and encryption it centralized management automatic rotation and dynamic Secrets 

provide robust security for our platform so uh we will uh continue to enjoy our platform engineering Journey uh with hash products uh with uh uh sorry yes so finally uh let me share uh once again your own ion's philosophy I gave the central pillar 

Wheels uh in Japanese again uh it means adapt to changes in the environment and transform the company itself we will continue to provide value uh to our customers based on the this philosophy and together with hash cope products 

so uh that brings us to the end of the presentation uh presentation uh I will be around here after the session so please feel free to approach me if you have any questions or would like to have a discussion uh thank you very much for your attention that's it [Music]
