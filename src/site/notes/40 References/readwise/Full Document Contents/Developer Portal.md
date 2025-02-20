---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/developer-portal/","tags":["rw/articles"]}
---

![rw-book-cover](https://discord.com/assets/4b357782daec4239711055c06af93881.png)

![IDs found in app settings](https://discord.com/assets/f50de8365b25e5497da0a29d038b0286.png)IDs found in app settings
![Configuring bot permissions in app settings](https://discord.com/assets/23c2baf1ec6eb6b4c167a30fb684c521.png)Configuring bot permissions in app settings
![ngrok forwarding address](https://discord.com/assets/9892b2d42ce01aaad0c5dede53020807.png)ngrok forwarding address
![Interactions Endpoint URL](https://discord.com/assets/dbf6d50814a559181735bb77c87e2545.png)Interactions Endpoint URL
#### Deployment

This repository is set up to automatically deploy to Cloudflare Workers when new changes land on the `main` branch. To deploy manually, run `npm run publish`, which uses the `wrangler publish` command under the hood.

Publishing via a GitHub Action requires obtaining an [API Token and your Account ID from Cloudflare](https://developers.cloudflare.com/workers/cli-wrangler/authentication/). These are stored [as secrets in the GitHub repository](https://docs.github.com/en/actions/security-guides/encrypted-secrets), making them available to GitHub Actions.

The following configuration in `.github/workflows/ci.yaml` demonstrates how to tie it all together:

```
release:
  if: github.ref == 'refs/heads/main'
  runs-on: ubuntu-latest
  needs: [test, lint]
  steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-node@v2
      with:
        node-version: 16
    - run: npm install
    - run: npm run publish
      env:
        CF_API_TOKEN: ${{ secrets.CF_API_TOKEN }}
        CF_ACCOUNT_ID: ${{ secrets.CF_ACCOUNT_ID }}

```

#### Code deep dive

Most of the interesting code in this app lives in `src/server.js`. Cloudflare Workers require exposing a `fetch` function, which is called as the entry point for each request. This code will largely do two things for us: validate the request is valid and actually came from Discord, and hand the request over to a router to help give us a little more control over execution.

```
export default {
  /**
   * Every request to a worker will start in the `fetch` method.
   * Verify the signature with the request, and dispatch to the router.
   * @param {*} request A Fetch Request object
   * @param {*} env A map of key/value pairs with env vars and secrets from the cloudflare env.
   * @returns
   */
  async fetch(request, env) {
    if (request.method === 'POST') {
      // Using the incoming headers, verify this request actually came from discord.
      const signature = request.headers.get('x-signature-ed25519');
      const timestamp = request.headers.get('x-signature-timestamp');
      const body = await request.clone().arrayBuffer();
      const isValidRequest = verifyKey(
        body,
        signature,
        timestamp,
        env.DISCORD_PUBLIC_KEY
      );
      if (!isValidRequest) {
        console.error('Invalid Request');
        return new Response('Bad request signature.', { status: 401 });
      }
    }

    // Dispatch the request to the appropriate route
    return router.handle(request, env);
  },
};

```

All of the API calls from Discord in this example will be POSTed to `/`. From here, we will use the [`discord-interactions`](https://github.com/discord/discord-interactions-js) npm module to help us interpret the event, and to send results.

```
/**
 * Main route for all requests sent from Discord.  All incoming messages will
 * include a JSON payload described here:
 * https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object
 */
router.post('/', async (request, env) => {
  const message = await request.json();
  console.log(message);
  if (message.type === InteractionType.PING) {
    // The `PING` message is used during the initial webhook handshake, and is
    // required to configure the webhook in the developer portal.
    console.log('Handling Ping request');
    return new JsonResponse({
      type: InteractionResponseType.PONG,
    });
  }

  if (message.type === InteractionType.APPLICATION_COMMAND) {
    // Most user commands will come as `APPLICATION_COMMAND`.
    switch (message.data.name.toLowerCase()) {
      case AWW_COMMAND.name.toLowerCase(): {
        console.log('handling cute request');
        const cuteUrl = await getCuteUrl();
        return new JsonResponse({
          type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
          data: {
            content: cuteUrl,
          },
        });
      }
      case INVITE_COMMAND.name.toLowerCase(): {
        const applicationId = env.DISCORD_APPLICATION_ID;
        const INVITE_URL = `https://discord.com/oauth2/authorize?client_id=${applicationId}&scope=applications.commands`;
        return new JsonResponse({
          type: InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
          data: {
            content: INVITE_URL,
            flags: InteractionResponseFlags.EPHEMERAL,
          },
        });
      }
      default:
        console.error('Unknown Command');
        return new JsonResponse({ error: 'Unknown Type' }, { status: 400 });
    }
  }

  console.error('Unknown Type');
  return new JsonResponse({ error: 'Unknown Type' }, { status: 400 });
});

```

#### Next steps

In case you need to reference any of the code, you can find the repo [on GitHub](https://github.com/discord/cloudflare-sample-app)

With your app built and deployed, you can start customizing it to be your own:

* Use [message components](https://discord.com/developers/docs/interactions/message-components) in your app to add more interactivity (like buttons and select menus).
* Take a look at different [public APIs](https://github.com/public-apis/public-apis) on GitHub.
* Join the [Discord Developers server](https://discord.gg/discord-developers) to ask questions about the API, attend events hosted by the Discord API team, and interact with other developers.
