---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-mutual-tls-m-tls/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.cloudflare.com/static/b30a57477bde900ba55c0b5f98c4e524/Cloudflare_default_OG_.png)

## Full Document
[[40 References/readwise/Full Document Contents/What is mutual TLS (mTLS)\|Full Document Contents/What is mutual TLS (mTLS).md]]

## Highlights
Mutual TLS, or mTLS for short, is a method for [mutual authentication](https://www.cloudflare.com/learning/access-management/what-is-mutual-authentication/). mTLS ensures that the parties at each end of a network connection are who they claim to be by verifying that they both have the correct private [key](https://www.cloudflare.com/learning/ssl/what-is-a-cryptographic-key/). The information within their respective [TLS certificates](https://www.cloudflare.com/learning/ssl/what-is-an-ssl-certificate/) provides additional verification. ([View Highlight] (https://read.readwise.io/read/01jnmp0hyzay8dfs00g0bpq6g0))


In mTLS, however, both the client and server have a certificate, and both sides authenticate using their public/private key pair. Compared to regular TLS, there are additional steps in mTLS to verify both parties (additional steps in **bold**):
1. Client connects to server
2. Server presents its TLS certificate
3. Client verifies the server's certificate
4. **Client presents its TLS certificate**
5. **Server verifies the client's certificate**
6. **Server grants access**
7. Client and server exchange information over encrypted TLS connection
![The basic steps in a mutual TLS (mTLS) handshake](https://www.cloudflare.com/resources/images/slt3lc6tev37/5SjaQfZzDLEGqyzFkA0AA4/d227a26bbd7bc6d24363e9b9aaabef55/how_mtls_works-what_is_mutual_tls.png) ([View Highlight] (https://read.readwise.io/read/01jnmp11gss0qydms4nchr1b11))


Certificate authorities in mTLS
The organization implementing mTLS acts as its own certificate authority. This contrasts with standard TLS, in which the certificate authority is an external organization that checks if the certificate owner legitimately owns the associated [domain](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/) (learn about [TLS certificate validation](https://www.cloudflare.com/learning/ssl/types-of-ssl-certificates/)).
A "root" TLS certificate is necessary for mTLS; this enables an organization to be their own certificate authority. The certificates used by authorized clients and servers have to correspond to this root certificate. The root certificate is self-signed, meaning that the organization creates it themselves. (This approach does not work for one-way TLS on the public Internet because an external certificate authority has to issue those certificates.) ([View Highlight] (https://read.readwise.io/read/01jnmp1h6ngf3w8wzh19hhnww6))


