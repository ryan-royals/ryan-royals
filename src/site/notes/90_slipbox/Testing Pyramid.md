---
{"dg-publish":true,"permalink":"/90-slipbox/testing-pyramid/","tags":["notes"],"created":"2026-03-27T09:57:51.497+10:30","updated":"2026-03-27T09:57:51.497+10:30","dg-note-properties":{"created":"2024-07-08","tags":"notes","related":null,"references":["https://www.browserstack.com/guide/testing-pyramid-for-test-automation"],"modified":"2026-03-03"}}
---


![Testing Pyramid-1720401944908.png](/img/user/10_attachments/Testing%20Pyramid-1720401944908.png)

## Unit Test

> Unit tests form the base of the test automation pyramid. They test individual components or functionalities to validate that it works as expected in isolated conditions. It is essential to run several scenarios in unit tests – happy path, error handling, etc.

## Integration Tests

> Integration tests need to be run to test how this code interacts with other code (that form the entire software). Essentially, these are tests that validate the interaction of a piece of code with external components. These components can range from databases to external services (APIs).

## End to End Tests

> Ensure that the entire application is functioning as required. End-to-end tests do precisely what the name suggests: test that the application works flawlessly from start to finish.
