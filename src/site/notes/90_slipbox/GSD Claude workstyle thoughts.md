---
{"dg-publish":true,"dg-path":"Slipbox Notes/GSD Claude workstyle thoughts.md","permalink":"/slipbox-notes/gsd-claude-workstyle-thoughts/","tags":["notes"],"created":"2025-08-29","updated":"2025-11-28"}
---

- Its like magic getting it to update the page as you are looking at it.
    - Remove this icon, change this font size, etc
- Its a nightmare getting to start from zero
    - No matter how long the prompt, getting it to do a MVP of the todo app ended in tragedy, and complex code everywhere.
- Having a ADR backing is perhaps the most impressive part, but its unclear how much it influences its thoughts.
- When given a task to troubleshoot, it finds its way into circles all the time.
    - Getting tests on all 3 apps was a joke, it made 3 ci workflows as well as nx ran commands, none of them worked.
    - Getting it to build and deploy the apps as docker containers is a joke, it just cant figure out how to get it to compile consistently.
- Getting it to scaffold the infra lead to bad practises, had to heavy hand guide it.
- Smaller tasks are better as it gives you more time to steer it, otherwise it just wants to go on a journey.
- I have gotten decently far knowing no substantial amount of TS or SQL, but I do need good fundamentals to be able to guide it to success.
- It did not want to think outside the box, when asking for the cheapest way to host the app, it didn't consider a vm with docker, even though its way cheaper than other options.
    - This is only for a dev env for just myself, its not a production use case at all.
- I think I could progress way faster with Claude Max, but that defeats the point of making my own app to save costs.
- It loves to refactor code with your adjectives "simple database" "fixed_todo", which is going to make the code illogical to maintain.
- It loves to leave one time files everywhere, and its becoming a messy desk that I have to keep asking it to tidy up.
- Getting it to review changed files and make a commit is a good way to get it to review its rats nest coding style.
- Working in a plan and apply style is working well. I'm getting it to track its progress in next_steps.md
- When using `dangerously-skip-permissions`, it seems to go off the rails a lot, and start adding random things to the the tech stack that make no sense.
- It wants to overengineer everything... you have to be very careful and actually watch it.

By the end of it all, got tired of burning credits working on a code base I never understood.  
It felt so close, but was lacking at the time. With new models, we might just get there.
