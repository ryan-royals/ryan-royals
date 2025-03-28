---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/stop-deploying-web-application-firewalls/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.macchaffee.com/static/favicon.png)

I wanted to write this because I don't hear enough real people discouraging the use of Web Application Firewalls (WAFs). Probably because the search results for "Web Application Firewall" are all written by WAF vendors. Anyone reading just that could conclude that WAFs are a good idea. I'm here to offer another perspective, after having suffered through using a WAF for two years.

Web Application Firewalls were created early in the Internet's history, especially popularized by the [ModSecurity project in 2002](https://en.wikipedia.org/wiki/ModSecurity). WAFs essentially work by intercepting every single HTTP request (and sometimes responses too) and evaluating several hundred regular expressions over the URI, headers, and body, sometimes aided by machine learning. If the request kinda looks like SQL, shell code, etc., the server may block your request.

In the infancy of the cybersecurity field, WAFs seemed like a good idea. HTTP requests were tiny, infrequent, and mostly contained mundane form data. But today, WAFs have overstayed their welcome in the security toolbelt. There are better techniques you can use that make even the most advanced WAFs entirely obsolete.

#### WAFs have Horrible Performance

Since WAFs run hundreds of regular expressions on every request, you may ask, "isn't that super inefficient?" Yes, very.

|  | WAF | No WAF |
| --- | --- | --- |
| Average time taken to upload 9,462 text files | 7.36 | 4.55 |
| Average requests per second | 1285 | 2079 |
| Number of requests blocked erroneously | 5 | 0 |
| Peak nginx CPU during trial | 73% | 8% |

 *Specifics about the benchmark* The easiest way I know to get modsecurity + CoreRuleSet installed is through ingress-nginx, which I've installed in a Kind cluster.

```
# https://kind.sigs.k8s.io/docs/user/quick-start/
cat <<EOF | kind create cluster --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 32080
    hostPort: 32080
    protocol: TCP
  - containerPort: 32443
    hostPort: 32443
    protocol: TCP
EOF
# https://kubernetes.github.io/ingress-nginx/user-guide/third-party-addons/modsecurity/
helm upgrade --install ingress-nginx ingress-nginx \
  --repo https://kubernetes.github.io/ingress-nginx \
  --namespace ingress-nginx --create-namespace \
  --set controller.service.type=NodePort \
  --set controller.service.nodePorts.https=32443 \
  --set controller.service.nodePorts.http=32080 \
  --set controller.ingressClassResource.default=true \
  --set controller.allowSnippetAnnotations=true

```

For the test, I'll be uploading files to MinIO using these values:

```
replicas: 1
mode: standalone
resources:
  requests:
    memory: 512Mi
persistence:
  enabled: false
rootUser: rootuser
rootPassword: rootpass123
buckets:
  - name: bucket1
    policy: none
    purge: false
ingress:
  enabled: true
  hosts: [minio-waf.localhost]
  annotations:
    nginx.ingress.kubernetes.io/enable-modsecurity: "true"
    nginx.ingress.kubernetes.io/enable-owasp-core-rules: "true"
    nginx.ingress.kubernetes.io/modsecurity-snippet: |
      Include /etc/nginx/owasp-modsecurity-crs/nginx-modsecurity.conf
      SecRuleEngine On
      # Even the core rules are ridiculous, blocking PUT requests, certain content-types, or any body with "options" in it
      SecRuleRemoveById 911100 920420 921110

```

```
helm upgrade --install minio minio/minio -f values.yaml -n minio --create-namespace
helm upgrade --install minio-waf minio/minio -f values-waf.yaml -n minio-waf --create-namespace
# Verify the WAF is working (should get a 403)
curl 'http://minio-waf.localhost:32080/?q=../../etc/passwd'

```

We'll be uploading just the "Documentation" folder of the v6.6 Linux Kernel, which contains 9462 files for a total of 65MB.

```
curl -LO https://github.com/torvalds/linux/archive/refs/tags/v6.6.zip
unzip v6.6.zip 'linux-6.6/Documentation/*'

```

Configure the minio client:

```
# You may need to add these hosts to /etc/hosts
export MC_HOST_nowaf='http://rootuser:rootpass123@minio.localhost:32080'
export MC_HOST_waf='http://rootuser:rootpass123@minio-waf.localhost:32080'

```

Run the benchmark (5 times each):

```
time mc cp -r linux-6.6/Documentation/ waf/bucket1/
time mc cp -r linux-6.6/Documentation/ nowaf/bucket1/

```

In addition to slowing down every request, you also need significant additional RAM for buffering requests. Since not a single byte in the buffer can be flushed to the backend server until the WAF completes its analysis, you need several gigabytes of RAM to store request bodies. Servers like nginx buffer requests by default, but enough large concurrent requests (like pushing a container image) can make a buffering web server run out of RAM. When using a WAF, every server becomes a buffering web server, which is simply incompatible with many types of applications.

I know computers are fast and hardware is cheap, but we shouldn't be spending that kind of CPU and RAM on WAFs unless they're a really effective security tool. But they aren't, as you'll see next.

#### WAFs are Easily Bypassed

WAF vendors and attackers are locked in a constant arms race, but it seems [attackers are much better armed](https://github.com/0xInfection/Awesome-WAF#evasion-techniques). How could they not be? Many of the attacks that a WAF purports to block involve complex grammars like SQL, shell code, and entire programming languages. They often include comments, character escaping, encoding issues, and more oddities. These oddities mean that attackers always have a significant advantage and can typically bypass any WAF rule if they are clever enough.

For example, you might think [Log4shell](https://en.wikipedia.org/wiki/Log4Shell) is pretty easy to catch: just check for `${jndi`, right? Unfortunately, Log4J supports nested "[lookups](https://logging.apache.org/log4j/2.x/manual/lookups.html)", including ones that convert letters to upper/lower case like `${lower:J}`

That means an attacker can insert an arbitrary number of nested lookups around each letter and still perform the attack, like this: `${${lower:J}ndi:...`. This lead CloudFlare to say ["WAF vendors need to be looking at any occurrence of `${` and treating it as suspicious"](https://blog.cloudflare.com/exploitation-of-cve-2021-44228-before-public-disclosure-and-evolution-of-waf-evasion-patterns/), which is just another hilarious example of how WAFs can never live up to the expectations placed on them.

I just discussed the fairly simple grammar that is Log4J Lookups, but you can imagine how many more evasion tactics you could use in a language as complex as SQL or PHP, especially when considering encoding tricks. For an in-depth description of specific WAF bypass techniques, check out [this awesome post](https://habr.com/en/companies/dsec/articles/454592/).

Another way to bypass a WAF involves just padding your attack string to appear [>8KB or so](https://docs.aws.amazon.com/waf/latest/developerguide/waf-oversize-request-components.html) into the request body. Like I mentioned in the section on performance, request bodies must be buffered into RAM for analysis, so WAFs must choose some cut-off point to avoid spending infinite CPU and RAM on a single request. For some WAFs like AWS's, that cutoff point is around 8KB. So if you just put 8192 innocuous characters before your Log4Shell attack string, you've rendered the WAF worthless.

#### WAFs are an Attack Vector

In 2019, CapitalOne experienced a breach of 100 million credit applications that was [allegedly caused by a WAF misconfiguration](https://krebsonsecurity.com/2019/08/what-we-can-learn-from-the-capital-one-hack/). The attacker allegedly tricked the WAF into sending requests to the EC2 Metadata Service, which handed out a credential that allowed reading sensitive files from S3.

While this is just one example, it illustrates the curious fact that WAFs actually have a large attack surface.

Most WAFs are giant, complex codebases that are usually closed-source and written in memory-unsafe languages. Since they're expensive "enterprise" products, companies stuff them full of unnecessary features to make them stand out more than competitors. All of this adds up to make WAFs yet another example of a dangerous "security" tool, [just like SolarWinds](https://www.macchaffee.com/blog/2023/solarwinds-hack-lessons-learned/).

No security officer would approve taking such a risky piece of software, putting it directly on the internet, making it parse mountains of untrusted input, and giving it access to all your backend servers, logging infra, SIEM, alerting systems, [and even JIRA for some reason](https://docs.fastly.com/en/ngwaf/jira) UNLESS it's covered in security buzzwords and costs 5-6 figures per year.

Somehow, companies that sell security products have gotten a pass on implementing foundational security principles like secure by default, secure by design, attack surface reduction, and the principle of least privilege. Don't let them keep getting away with that.

#### WAFs have a High False Positive Rate

Over the last twenty years, open-source WAF rulesets have expanded considerably to detect more-recent types of attack. Apparently all those proprietary WAFs are doing the same. That means there are more and more possible strings that could trigger a WAF to block your request. If you want to write a comment on an article discussing Log4shell, you might be blocked for including the string `${jndi` in your comment. So naturally the false positive rate continues to rise with every new rule, and it's already quite high based on my experience maintaining a giant list of ModSecurity rule exceptions.

So-called "next-generation" WAFs claim to solve this problem by [looking at multiple requests](https://docs.fastly.com/en/ngwaf/about-next-gen-waf) or by using [IP reputation systems](https://docs.fastly.com/en/ngwaf/about-the-architecture#about-the-collection-and-analysis-system). While these can improve false positive rates, they can never truly solve the problem. In some ways, less false positives can increase the impact of particular false positives since neither users nor support teams have a clear procedure for fixing it. CloudFlare's algorithm can randomly decide to block you and [you will have no recourse](https://www.ctrl.blog/entry/cloudflare-ip-blockade.html). Imagine that happening to someone less tech-savvy.

This is the classic problem with using an outdated security tool like a WAF: defenders have to configure the tool absolutely perfectly to be safe and avoid false positives, but attackers just need to find a single weakness. Those are horrible odds. You should use alternatives that don't require perfection from imperfect humans.

#### Alternatives to WAFs

Since WAFs are resource-hungry, inneffective, unsafe, and noisy, how do I convince an auditor to not make me use one? The technical term would be to use "compensating controls", but that sounds like such a weak term to describe the powerful and simple alternatives to WAFs I'm about to describe:

* **Isolation:** Isolation involves ensuring that a breach in one component can not affect the rest of the system, and there are many technologies that provide isolation.
	+ Browsers do this by executing all code inside special sandboxed processes that don't have carte blanch access to cookies, saved passwords, other tabs, etc. Imagine how slow the web would be if every piece of JavaScript needed to be analyzed by hundreds of regexes before being executed!
	+ Microservices are designed with isolation in mind, but you can also do it in a monolith with a variety of [libraries and languages](https://github.com/dckc/awesome-ocap#libraries-and-frameworks).
* **Immutability:** Entire classes of attack can be eliminated by removing a few assumptions, like having a [readOnlyRootFilesystem](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/), a [package manager that requires rebooting](https://thenewstack.io/3-immutable-operating-systems-bottlerocket-flatcar-and-talos-linux/), or append-only/[immutable backups](https://www.rsync.net/resources/faq.html#9a).
* **Static Analysis:** SQL injection has a miracle cure called "prepared statements". The problem is that devs forget to use them. Static analysis checks in a CI pipeline can all but ensure that zero SQL injection vulnerabilities are in your codebase, at which point there is no need for any SQL injection WAF rules. No, "defense in depth" is not a valid excuse to use a WAF anyway, because it provides no real defense! Like surrounding Fort Knox with an army of guard guinea pigs.
* **Capability-based security:** Not every API endpoint needs to have unrestricted read/write access to your entire database and file system, but that is the normal way people build APIs today. By using capabilities, you can express exactly that "GET /api/v1/books" only needs read access to the "books" table. Or that "POST /api/v1/imageupload" needs write access to a specific folder, but doesn't need the ability to spawn processes.

Now I'll admit these ideas are quite broad; you'll need to adapt them to your particular app. WAF vendors offer a one-WAF-fits-all fantasy that I can't match. But these secure-by-design strategies are the way that the security industry needs to be heading. Unfortunately, it's a lot harder for the security industry to profit off of design-based techniques, so don't hold your breath.
