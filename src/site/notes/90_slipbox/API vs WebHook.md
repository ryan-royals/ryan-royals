---
{"dg-publish":true,"permalink":"/90-slipbox/api-vs-web-hook/","tags":["notes"]}
---


[Webhook vs. API What's the difference and when should you use each one](https://zapier.com/blog/webhook-vs-api/)  
Webhooks and API calls are very familiar to each other, the key differences is that Webhooks are a event driven message, while a API is a ongoing communication.  
Webhooks don't expect a response beyond a succeed or failed message, whilst API is more for ongoing communication, as it can send something like a User ID generated from a API endpoint that creates a new user.

Kind of similar to UDP vs TCP. If Webhooks are UDP, its because they just want to send a message and don't care after it has been released.  
API would be like TCP, as it has handshakes a long the way and points of interaction to make sure everything is working.

> An API is something you call to. For example I ask the Facebook API for a list of my friends or ask it to post to my wall.  
> A webhook is something that calls to you. So I could ask Facebook to let me know when a new friend request comes in or when I receive a new private message.  
> Webhooks save you from having to poll their system constantly. Imagine asking if you have a new message every 10 seconds vs just being told the second it happens.  
> [What's the difference between a webhook and api? : r/webdev](https://www.reddit.com/r/webdev/comments/d6o9j4/whats_the_difference_between_a_webhook_and_api/)
