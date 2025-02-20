---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/0-to-lsp-neovim-rc-from-scratch/","tags":["rw/articles"]}
---

![rw-book-cover](https://i.ytimg.com/vi/w7i4amO_zaE/maxresdefault.jpg)

so I am gonna do this I am going to write my 
neovim config from scratch no I mean really   from scratch all right so this is gonna include 
my favorite plugins that I use the best remaps   of your lifetime LSP tree-sitter some basic editor 
settings the whole nine yards and I'm gonna do it   from the vanilla Neo Vim experience all the way up 
to the Giga chat neovim experience so I hope that   you've already pre-liked the video right there 
just press it right now and once you do that you   

can keep on going down you can go check out my new 
Vim RC on the GitHub link provided all right so I   guess the first thing I need to do is create the 
neovim directory CD into it and open up Vim now   this is a terrifying screen right here this is the 
default netrw experience which is the file Tree by   Vim along with the default color scheme which is 
I mean cyan's never looked this good okay 2023 is   going to be the year of cyan I can feel it right 
here if you don't know where to put this folder   this neovim folder just type in :h rtp you'll see 
right here at the very top this is where neovim's   

going to look and this bottom one right here 
very important we're going to use it as well all   right so the first thing we have to do is press % 
because that means create file because that's the   mnemonic that was chosen I don't know any man is 
creating a init.lua this will be the first place   that neovim looks I'm going to just type in print 
hello if you're not familiar with Lua it's a dead   simple language look at that hello bottom corner 
now let's press 'd' this will create a directory   

not delete directory probably would have gone 
with a capital D myself all right so let's create   the Lua directory any directory within the Lua 
directory is requireable by Lua so let's press   enter go right into the Lua directory press D 
again I'm going to create theprimeagen directory   you create whatever you want to press enter again 
% yup create file init.lua going here print hello   from theprimeagen then I'm going to press colon 
capital e x that stands for explore brings back   

up that beautiful cyan net RW hit enter on the 
two dots hit enter on the two dots go back to our   original one and require theprimeagen remember a 
knit.lua is like index.html it's just like the one   it goes to quit open beautiful we got something 
good going here so now let's make Vim usable all   right so the first thing I'm going to do is I'm 
actually going to add a remap to make it really   

easy to go back into netrw because I don't have to 
press colon ex enter I want something that feels   a little bit faster to me so I'm going to go down 
to Lua I'm going to go into theprimeagen and I'm   going to press percent sign to create that file 
again and call it remap.lua in here I'm going to   type in vim.g.map leader equals a space and then 
vim.key map set in normal mode leader ah leader   PV Vim command ex so what's going on here if 
you're not familiar with remaps effectively   

while in normal mode if I press leader PV it will 
execute this command for me leader of course is   the space all right just to test this out let's 
go colon SL this sources this file right here and   then space PV perfect it's looking good now the 
thing we can't forget to do is go over to my init   file in theprimeagen directory and go require 
theprimeagen remap by having this right here it   

will automatically get sourced every single time 
Neil Vim gets opened so quit reopen it back up   hello theprimeagen hello go into here leaderpv 
awesome now we're cruising so the next thing   we need to do is to get a plug-in manager and a 
fuzzy finder because I just feel like I need to   be able to hop between files quickly and nothing 
does that better than a fuzzy finder except alright so to get a plug-in manager all we need 
to do is go to the internet go to packer.niovim   

and from in here we can just copy this 
lovely command and just put it directly   into our shell lovely next go back to Packer 
grab these couple lines right here copy them   go back to Vim now we're gonna go into Lua into 
theprimeagen we're gonna create one more file   called packer.lua let's paste in what we got from 
the internet and that there we go and the function   do so to Source it uh-oh we hit an error you know 
why we haven't quit Vim reopen it back up going   

to Lua go all the way to here now do it awesome we 
just installed Packer so I didn't know about it so   now let's type in pack or sync just to give it a 
go look at that we got ourselves a plug-in manager   let's close it let's go back to the internet let's 
go to telescope.neovim it is a fuzzy finder built   by telescopic Johnson and maintained by Connie 
the true hero really the true hero let's scroll   on down copy this Packer statement right here go 
down to an empty line paste it in I press equal   

to align it nicely re-so to shout it out again 
and then of course pack or sync one more time   and look at that telescope is now installed but we 
don't have any ways to pull it up without simply   typing in the command so let's add some remaps so 
leaderpv brings back up netrw back one back one   create a directory called after going to after 
create a directory called plug-in go into plug   and create telescope.lua and now let's go back to 
Lua and grab these top two lines right here in the   

Lewis section copy it paste it let's have our own 
key bindings I want PF for project file it's going   to use find files and then we're going to do one 
more I'm going to jump in here and go CP for fuzzy   finding go FF right here and get files what this 
will do is allow me to have a git file search and   then an all file search since right now I'm not in 
a git Repository I want to be able to just simply   grab every file and that is fine files right 
here but there's times where you only want to   

look at just files that are in git it's just much 
faster think of node modules the heaviest thing   in the universe all right so let's add one more 
remap this one is super useful let's actually I'm   going to yank it from this one and go over here 
and let's go PS for project search and instead   of using this let's actually use a function 
so I'm just going to write straight up code   to just execute when I press this inside of here 
I'm going to take in built-in and do grep string   providing a search term which is going to be a 
Vim function input and I'm going to provide grep   

just like that boom put a little semicolon at the 
end even though I didn't need to do a little Esso   and now I can type in leader PF look at that very 
horribly colored fuzzy finder let's go to packer   wonderful I can even do leader PS which is 
going to give me a little grep string down   there and let's find everywhere that we say 
the word requires look at that we only have   it in one little place right there that's pretty 
cool right and then of course control P it airs   

we're not in it we're not in the git directory 
this doesn't count correct no it doesn't count   but honestly the cyan's not working for me okay 
I thought cyan was gonna be 2023 it's not going   to be so let's add a color scheme alright so 
I chose Rose Pine for neovim gonna come down   here copy this line right here for the Packer 
install paste it in equal AP for that beautiful   eight space indenting do a little so do a little 
Packer sync watch it go and fantastic Rose Pine   

is installed lost the waifu in the background 
probably gained your subscription because you're   so blown away at this point Thank you I'd like 
to say thank you especially when I set up that   LSP I know you're gonna like the video alright 
so I see two things kind of wrong here first off   our transparent background went away and second 
off the colors are just really not that great so   let's fix those two things so the first one's not 
too hard to fix leader PV jump back here jump back   here go into the after going to plug in create a 
file called colors.lua okay so we need to do two   

things one we're gonna set the color scheme and 
two we're gonna set a transparent background so   I'm going to create a global function I know you 
don't have to do it this way there's plenty of   better ways to do it but this is the way I have 
chosen I'm going to make sure I color it right   we're going to color the we're going to color 
those pencils I'm gonna say color equals color   or Rose Pine so that way I always have a default 
color so if it's just called from anywhere we're   always getting that nice Rose Pine experience 
Vim command color scheme ah color and then now   

we need to actually set the background to be 
transparent so I'm gonna go like this Vim API   Neil Vim set HL zeros just for the global space 
so every window gets this I'm gonna pass it normal   that just means like the thing this is just Vim 
why is it called normal I don't know it's been   around probably longer than I have do a little 
background equals none except of course lowercase 

then copy that do it one more 
time and do it for float that   way it also happens for floats and 
then give this a little shout out   beautiful but the colors are still not right we 
need tree sitter if you're not familiar with tree   sitter tree sitter allows for an amazingly fast 
parsing of your code that's in your editor right   now and it builds an incremental tree so every 
change just you know changes one small part of   it and it provides highlighting vim's working on 
indenting and it's incredibly fast it puts vs code   

to shame and yes emacs already uses it okay and 
pretty much every other editor Bud vs code alright   so let's go to tree sitter right here scroll on 
down and just grab their installation line right   here and now we need to translate this leader 
PF gonna open up my files go all the way over   to Packer go down to the bottom and let's add 
this line right here but this time let's go use   

put that in there jump over to this erase that 
and call it run equals TS update there we go we've   created the exact same thing translated from plug 
which is a different package manager to Packer   this one I'm gonna hit a beautiful so realize that 
I accidentally created a syntax error go back here   erase that little squirrely brace do another so 
do a little pack or sync awesome we now have tree   sitter and yes you'll notice that every single 
time we install we lost that so now I can just go   

Lua color my pencils but this time call it like 
a function and bam we're back in the action we   got ourselves the waifu okay everything's fine now 
but we now need to initialize tree sitter because   look at this it's still it's disgusting looking we 
don't have any parsers or anything set up we need   to get stuff in here so it looks good all right 
so I'm gonna go here I'm gonna go all the way   down to this and I'm just going to copy this whole 
chunk of code because there's some things we're   gonna need in here so copy it leader PV let's 
go back let's go back go after go plug and go   

tree sitter.lua hopefully you're starting to see 
a pattern here I create my Packer I install the   plugin I want I go to after I add the file that 
kind of configures it it's pretty straightforward   let's paste in what we got from the internet 
best way to do anything and I'm going to add   a couple items to this list because I also want 
help for the vimhelp and I also want JavaScript   just in case I need to do some JavaScript or some 
typescript because you never know you just never   know do I want to synchronously install it no 
Auto install true ignore get the hell out of   

here erase that comment I don't even know why I 
need it enable absolutely we want those delicious   highlights enabled get C out of there get this 
disable function out of there we don't need it   either do I want rejects doing highlighting no I 
don't awesome let's do a little shout out you'll   notice that we start downloading parsers right 
away these parsers will help give us beautiful   color and hopefully when it finishes we'll just 
automatically see it all done if not we'll make   

it happen alright so it looks like it didn't 
do it let's do a little colon e are you ready   foreign well that was boring let's we'll quit 
and then we'll open it back up okay let's go   into after plug-in tree sitter oh that looks 
so much better look at all the colors that   is significantly better if we go back to that 
Packer file tell me that does not look so much   better before it was just like only the strings 
got anything everything else was just white this   is the power of teresitter but can I show you just 
one more small thing something I just absolutely   

love let's go here and type in tree sitter 
playground neovan and go to this top option let's   scroll down the page okay it's just installed just 
like plug was so I'm just going to grab this line   go all the way down here paste it in change plug 
to use and call the function Shout It Out Packer   sync it's going to install playground I'm gonna 
quit again Lua color my pencils awesome but now   we get something amazing I'm gonna go like this 
TS here's all of our tree sitter functions right   

but I'm gonna go TS playground after restarting 
Vim we got this new function TS playground toggle   look at what happens when I do that we get all 
this information what is this well this is the   actual AST that exists right now inside of my 
editor due to tree sitter this is what you now   get access to if you ever wish to do any plugins 
it is mind-blowing the power that is contained now   within your editor and you get free access to it 
there's three more plugins we need to install to   

make the Vim experience amazing let me show you 
them so first one of course is mine Harpoon I   just think it's glorious way to navigate files so 
I'm going to copy the URL up there copy that jump   into here paste that in Shout It Out Packer sync 
it all right so Harpoon is installed let's just   open up any file within the after directory leader 
PV opens up that netrw create harpoon.lua now we   just need to do a quick configuration of Harpoon 
let's go like this local Mark equals require   

harpoon.mark copy paste replace a mark with UI and 
then of course now we just need to add some remaps   now before I do that I immediately notice my waifu 
is gone I'm scared okay we're back became a member   Man became a member thanks for becoming YouTube 
members I appreciate that both of you blazingly   appreciative all right so there's six remaps we 
need to do not too hard of m key map set in normal   

mode I want to be able to press leader a and add 
the current file that I'm on to harpoon copy that   let's then do say Ctrl e and we can do UI toggle 
quick menu and now I just need to be able to do   my navigations jump over to here do nav file one 
but since I'm calling it as a function I need to   wrap it in a function so let's just wrap that in a 
function really quickly there we go copy paste f h   

r t control a pace f h r n Ctrl a control a paste 
f h ah f h r s control AAA boom boom boom shout   this file out now we have a sweet navigation when 
I press Ctrl e here's my Harpoon menu we have no   files in here leader a we now have a file we can 
go right back to of course which is our Harpoon   file let's load up our Packer file let's add that 
to our Harpoon list let's put that as number one   

now we should be able to switch back and forth as 
fast as we'd like between Harpoon and Packer all   right awesome the next must have plug-in of course 
is undo tree right here so I'm just going to copy   the URL jump back over here copy paste paste it 
in Shout It Out Packer sync beautiful Harpoon   my way back to Harpoon open up netrw create undo 
tree.lua and now we need a remap I need to be able   to open up undo tree now I can't quite remember 
it so let's just jump over here scroll down here   

it is right here perfect that's the one we want 
I'm just gonna paste that in and I'm gonna go Vim   key map set normal mode leader U of course I want 
leader U and then all we need to do now is just   go Vim command undo tree fantastic let's shout it 
out let's get our waifu back and now if we press   leader U we can see everything we've done so let's 
go back to Packer and go leader U now what you're   going to see here is this little tree that's 
going on right here so that means I should be   

able to see all the changes that we have recently 
made so now if I go right here this is a branch   right in our undo history so I could actually 
start editing this branch and look at that we   actually have something moved around in here that 
means I can actually go back to this one and start   doing stuff in here as well so if you ever have 
something that ends up being in the past you can   search for it via undo tree it's very fantastic 
or if you ever accidentally make a change that   you need to recover from undo tree is just so good 
all right one more I'm just gonna copy I'm gonna   

paste I'm gonna go like this T Pope Vim fugitive 
I know the URL this point Shout It Out pack or   sync it we have fugitive again get the waifu back 
jump over to Harpoon create a new file let's call   it fugitive.lua and now we just need to add a 
simple remap vimkey map set in normal mode if   I press leader GS stands for git status that's how 
I think about it I want to execute Vim command get   

let's shout out this file leader GS I'm not in 
the git repository so just to try this thing out   go CD Neo Vim get a knit awesome jump back here 
leader GS it's still not there because you know   Vim just didn't know I was there to begin with 
leader GS look at that we now have the ability   to manipulate and do stuff in git at this point I 
think I have enough plugins to really be able to   move I have my undo tree I have a fuzzy finder I 
have Harpoon I have git integration I have a nice   

color scheme we're ready to rock all that's truly 
left is the LSP and we have an amazing Vim setup   all right to set up the LSP just go to LSP zero 
this thing is incredible I actually really like   it and so we need to find the installation face 
so just go right here with this huge amount of   different plug-in that it just is an amalgamation 
of everything you used to have to configure now   just into a single plug-in go back here jumped all 
the way down to Packer paste everything in I just   have to format it so let's do one of those I still 
have eight space indenting we're going to change   

that here in a little bit now just do a little 
so and of course Packer sync now we're going   to install all these other plugins that are all 
related to LSP I'm going to quit that window get   the waifu back jump back over to Harpoon and let's 
create a new file called LSP Lua and now we need   to configure our LSP so the easiest way to do that 
is actually just to jump up here and just grab   this this will give you a preset LSP everything 
set up ready to rock just for you I already have   kind of some things that I like so I need to kind 
of edit this setup a little bit so I just pasted   

in mine you don't need to see me set everything 
up here we go so I have TS server eslint some   Neko Lua and rust analyzer fantastic here are some 
remaps I like for when I'm doing my completion I   like control p and N to go you know previous 
and next on my completion list Ctrl y accepts   it space starts the completion I don't want any 
sign icons sign icons are just not for me there   we go we set up it with our custom mappings that 
I have for me this last one is a doozy but it's   

really cool so on attach happens on every single 
buffer that has an LSP that's associated with it   that means I'm going to have all these remaps only 
exist for the current buffer that I'm on of course   a buffer being the text we're editing right here 
that means these remaps only live for the life of   this buffer which means that if I go to something 
that doesn't have a buffer I can still use GD for   jump to definition and it'll try to do vim's best 
jump to definition effort but if I do have an LSP   I'll use my LSP instead this is a really handy 
thing to do it might be a bit complex I should   

probably take out this little print statement I 
don't need help I don't know what was going on   there but you get the idea so now I'm just going 
to save this and look at this we're installing   all these beautiful things awesome we have 
everything installed now we're ready to rock   so I opened up my Advent of code 2022 notice 
I still have the hello from theprimeagen and   hello let's go into here let's jump into say day 
one from 2022 Advent of code we should have our   

LSP automatically installed right here awesome 
everything's getting highlighted we're looking   good and I should just be able to start typing Max 
look at this you can see all right here's all the   different things that are available when I press 
this we now see all the different things that are   available for a you size integer which means I 
can call sort by look at that I can call sort on   this oh it's not a u size it's this oh this is a 
vector vector view size my bad but there we go LSP   setup it was that simple you didn't have to do all 
the remaps you could have just simply stuck with   

these three lines that have the default neovim 
LSP zero experience that's pretty dang easy it   uses Mason under the hood if you're not familiar 
with Mason effectively Mason allows you to just   peruse packages and install anything at your 
will oh you want Dino let's hit I boom we are   now installing Dino right now well look at that 
look at it go it's that easy and if you open up   a file in which it detects it will ask you hey do 
you want to install the language server associated   

with this file type it's pretty damn inconvenient 
at this point my Vim experience is pretty much on   point but it is missing a couple things notice 
I have no line numbers no relative line numbers   I'm still indenting at eight tab indents right so 
there's some basic sets that need to be set up for   my Vim experience to be complete and then I have 
some remaps that just really Turbo Charge my Vim   experience alright so the first thing I want to 
do is go back to my init let's remove this hello   statement we just don't need it in there let's 
go back let's go into our knit that's inside of   

theprimeagen folder and let's remove that one as 
well alright so now what we need to do is add some   sets to make my editor experience a bit better 
because like I want to automatically have line   numbers I want them to automatically be relative 
so as I move I can kind of jump between the lines   I want to be on like I want to be able to press 
8 up and know I need to go to that line all right   so let's add a set dot Lua let's make sure we 
go back to our knit folder copy that jump over   to this R and type and set I want to make sure 
I have that set file I should be able to use   

leader GD and notice that it jumps over here to 
set.lua since we have LSP zero installed that's   pretty handy all right so now it's just all my 
Vim sets I need to add so instead of typing them   I just cut and paste them all in here let me go 
over them one at a time I like a fat cursor so   right now when I press o and I go into insert mode 
notice my cursor is really really thin let's get   out of insert mode Let's type in shout out now 
notice some things just happened to my screen   but when I press o I still have that fat cursor 
it's just because I've been using Vim for just so   

long that it just feels normal and natural next 
of course line numbers I want line numbers plus   I want relative line numbers so if I wanted to 
jump all the way down here to wrap I just know   to press 9k or J sorry it's so Ingrid in my head 
I don't even remember the directions it goes this   next one just makes me have four space indents 
hey Vim try to be smart about my indenting I   don't like line wrap I don't want them to do any 
backups but instead I want my undo tree plug-in   to have access to Long running undo's that way I 
can undo things from Days upon days ago these neck   

X2 are out of the world awesome I do not like it 
when I search that it keeps the terms highlighted   but I love incremental search check this out so 
if I go Vim you'll notice that it's highlighting   as I search if I do dot star you'll notice it does 
the whole thing if I do equal space you can see it   kind of going so that way if you have some tricky 
searches or even searching or places that you're   doing you can use incremental search to really 
guide you if you're doing the right thing I like   good colors the only thing really interesting in 
here of course is scroll off which means that as I   

go down I'll never have less than eight characters 
towards the bottom except for when I'm at the end   of a file so if we were to add a bunch of spaces 
down here as I would go upwards you'll notice that   it never has eight or never has less than eight 
that's pretty cool right fast update time great   color column great and of course I think this is 
just a better place to put my leader key it's with   all the other sets alright so the last thing I 
need to do is just simply do all my high powered   amazing remaps so let's again let's go out here 
and let's create let's just jump into remap and   

let's start putting them in right here so I cut 
and paste my previous shortcuts that I used to   have but I realized that I had a convenience 
function for doing say a normal mode or remap   it kind of feels like the old vimway so let's 
actually do a really amazing find and replace   right here so what I want to do is I'm going to do 
this colon percent sign s that means do this for   the entire file I'm gonna do a slash and I'm gonna 
do a fighting one-eyed Kirby except for I just do   

a single dot so it's going to grab everything 
that has a DOT right here then I'm going to go   nor map no recursive mapping opening parenthesis 
then I'm going to replace that with Vim key map   set quotes slash one remember our first Little 
Match group that we did so notice that our V   right here V Norm map becomes right there oh yeah 
so good look at that did it all throughout the   entire thing right here hit enter everything has 
been remapped properly even the X mode right there   

let's go let me go over my remaps that I 
use they're quite amazing so these first   two are out of this world they use the move 
command and what they allow me to do is when   I'm highlighted I can go like this I can move 
things around and if there is an if statement then guess what we can take these and we can 
move them in and they'll automatically indent   how beautiful is that if you're not familiar 
with Jay Jay simply takes the line below you   and appends it to your current line with the space 
this one allows your cursor to remain in the same   

place even though you're applying line after 
line instead of putting your cursor way over   at the end because every time I did it my cursor 
would be way over here instead I didn't want that   I wanted my J to stay in place these next two 
are amazing what they do is they allow control   D and U which is half page jumping to just keep my 
cursor in the middle it helps me just look in one   place as I move and so it doesn't feel nearly as 
disorienting these next two are also fantastic it   allows Search terms to stay in the middle so when 
I search for Vim it'll just keep my cursor in the   

middle these are for good times on Twitch we're 
not going to talk about that this one's fantastic   so check this one out so you know how sometimes 
you have like say Foo and then you have bar and   you highlight and copy Foo and then you highlight 
Barb and you want to paste Foo over it without   losing your Foo current paste buffer I have 
leader p and what that's going to do is it's   going to delete my highlighted word into the void 
register and then paste it over because that means   

I still have Foo preserved how fantastic is 
that for those that don't know Vim too well   what would have happened is this I would have 
highlighted pasted and now I would just start   pasting bar and I didn't want that I didn't want 
that these next three are just awesome have to   thank asborne for these ones effectively if I go 
leader y it now goes to this right here you can   see it right here which is the plus register 
which is also your system clipboard so now if   I go AP yank this paragraph what will happen is 
I can now press Ctrl V and I can jump over here   

and I can start pasting those in somewhere else 
so I just have to do leader y to yank into my   system clipboard or just y to have it only within 
Vim that way I can have these two things separate   because it really sucks when they're together some 
more of that like deleting to void register either   in normal mode or in visual mode I know you're 
gonna make fun of me there's one reason why I do   this that's because in vertical edit mode if you 
just press control C to exit it won't actually   

save all these changes vertically instead you 
have to press Escape it's the only thing that   I can tell right now that's actually different 
between control C and Escape so I just put a   remap because I'm so used to it okay I picked 
up the Habit from IntelliJ 10 years ago give me   a break don't ever press capital Q honestly it's 
the worst place in the universe this right here is   fantastic this allows me to press Ctrl F and now 
I can switch projects I can go to Advent of code   2022. look at that we're back in our rust project 
let's go back via tmux previous session did you   

notice that little control a capital l that's 
using tmux how fantastic is that oh my goodness of   course this is just quick fix navigation if you're 
not used to the Quick Fix list it's out it's just   so good this last one's like a pretty fun command 
so if I go like this space s what it's going to   do is it's going to give me this little menu right 
here and now I can start replacing the word that I   was on pretty cool right and I really do like this 
last one right here to show you what it does let's   

create one more file let's call it Foo let's jump 
in here let's go octothorpe bang forward user bin   and Bash let's create a little bash script and 
let's go Echo hello and instead of doing that   thing where you have to go okay bash can up looks 
like I'm installing uh The Bash tree sitter parser   thank you so instead of going out to the command 
line and doing that chamode plus X path to this I   just go leader X and what oops leader X and what 
it's going to do it's going to actually just make   

this into something that is executable so when 
I go CD Lua theprimeagen ls you'll notice that   Foo is actually executable pretty cool huh let 
me delete that capital D deletes boom and there   you go we've just set up Vim to be amazing we have 
get control we have undo tree we have LSP support   we have telescope fuzzy finding we have Harpoon 
the greatest file Navigator ever tree sitter for   amazing colors awesome remaps to just make your 
Vim experience creamy smooth and of course sane   

default sets for a nice editor experience so I 
hope that you really like this again press the   like button okay this this was this was difficult 
and also if that final replace was magic say down   in the comments below let me know you want to 
see a video on just some sweet and macro and   Search Foo in vim and I can make it happen for 
you thank you the name is theprimeagen if you   haven't checked out kickstart.neovem it's made 
by telescopic Johnson it's a great way to get   started with neovim it gives you pretty much all 
the things you need off the rip and it's going   

to have a lot of keys set up in a way that are 
more familiar such as tab for scrolling through   autocomplete Etc so give it a check throw star 
on you can find the link down in the description
