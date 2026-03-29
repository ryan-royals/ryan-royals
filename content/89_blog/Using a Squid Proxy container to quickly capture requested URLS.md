---
{"dg-publish":true,"dg-path":"Blog Posts/Using a Squid Proxy container to quickly capture requested URLS.md","permalink":"/blog-posts/using-a-squid-proxy-container-to-quickly-capture-requested-urls/","tags":["blogs"],"created":"2025-02-07","updated":"2025-11-28"}
---


Odds are whether you work in any Application or Infrastructure team, a someone will someday ask you "What are the URLs you need to get added to our whitelist proxy". Your first response is probably going to be to Google away your app stack, trying to figure out who sings out to what, but hopefully before wasting hours reading heaps of doco sources, you will think to just capture the traffic you need and go from there.

There are plenty of ways to capture network traffic, a immediate way that springs to mind is Wireshark. This tool works great, but is better suited to capturing Layer 3/4 traffic (IP's and Ports), than it is capturing the Layer 7 side of the world (URLs). Wireshark is also very noisy in the logs as you will most likely be capturing your primary NIC, and every app wants to sing home every 5 minutes to check if someone has sent you a cat gif.

For my use case, I wanted to capture traffic from Terraform, so we can run a `terraform init`, `terraform plan` and `terraform apply` with all the Providers and Modules downloading as we go.  
I chose to use [Squid]([squid : Optimising Web Delivery](https://www.squid-cache.org/)) as a proxy server as I have used it before, and I found a light weight [Container image]([sameersbn/docker-squid: Dockerfile to create a Docker container image for Squid proxy server](https://github.com/sameersbn/docker-squid)) I could use to spin it up on my machine without much hassle. I also have opted to use WSL as a clean environment to run Terraform from, as that way I don't have a heap of noisy applications ruining my logs. From here I have a few steps to get the end result that I want: **Download and Configure the container**, **Configure WSL to use the Proxy** and ultimately **Log the traffic that I need**.

The below is a simple guide on how I got this done. There are some optimizations to the workflow that could be improved I'm sure, but I just wanted to get in and out without spending 10 hours to make 10 seconds work easier (Just to try something different this time), and I want the confidence on the journey to not make other issues to diagnose.

## 1. Download and Configure the Container

*Assuming you have [Docker]([Install | Docker Docs](https://docs.docker.com/engine/install/)) already installed.*  
*This guide is an abbreviation from the [readme in the containers repo]([sameersbn/docker-squid: Dockerfile to create a Docker container image for Squid proxy server](https://github.com/sameersbn/docker-squid))*
1. Pull the container using `docker pull sameersbn/squid:3.5.27-2docker pull sameersbn/squid:3.5.27-2`
2. Start the container using `docker run --name squid -d --restart=always --publish 3128:3128 --volume /srv/docker/squid/cache:/var/spool/squid sameersbn/squid:3.5.27-2`
3. Log into Bash on the container using `docker exec -it squid bash`
4. Now we are in the container, we will need to install a tool to edit a text file. For me I use Vim, but you can substitute whatever tool you want:
	1. `apt-get update`
	2. `apt-get install vim`
	3. `vim /etc/squid/squid.conf`
5. The `/etc/squid/squid.conf` is a very well documented configuration file that can get you configured relatively easily. In the file every line is a comment, so we can delete everything and instead add the line `http_access allow all`. This does what it says on the tin, and and allows all traffic.
6. `exit` from bash and out of the container, and restart the container using `docker restart squid`

## 2. Configure WSL to Use the Proxy

Super easy step, but one of those commands that are easy to forget if you don't use everyday:

```bash
export ftp_proxy=http://localhost:3128
export http_proxy=http://localhost:3128
export https_proxy=http://localhost:3128
```

## 3. Run Your Workload to Capture Traffic

Now inside of WSL, do what you need to do to capture all the traffic you need.

## 4. Check the Logs

In your primary shell, log back into the container to grab your logs

```bash
docker exec -it squid bash
cat /var/log/squid/access.log
```

## 5. Tidy up

Hopefully now you have a good log of the traffic that you generated. An easy tip is copy it out of the terminal, and paste it into Excel, using the Text to Column function delimited by Spaces.  
When you are done done, remember to tidy up the container with `docker stop squid`, and exit from your WSL shell to clear the `export` so you can resume web traffic as per normal.
