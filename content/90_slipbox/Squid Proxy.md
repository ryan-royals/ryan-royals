---
{"dg-publish":true,"dg-path":"Slipbox Notes/Squid Proxy.md","permalink":"/slipbox-notes/squid-proxy/","tags":["notes"],"created":"2025-02-07","updated":"2025-11-28"}
---


Squid Proxy is a configurable Proxy for ... Proxying traffic.

[[89_blog/Using a Squid Proxy container to quickly capture requested URLS\|Using a Squid Proxy container to quickly capture requested URLS]]  
Building a quick proxy for capturing traffic  
	- Configuring Container:  
		- `docker pull sameersbn/squid:3.5.27-2`  
		- `docker exec -it squid bash`  
			- `apt-get update`  
			- `apt-get install vim`  
			- `vim /etc/squid/squid.conf`  
				- insert line `http_access allow all`  
			- `exit`  
			- `docker stop squid && docker start squid`  
	- Configuring WSL:

		``` bash
		export ftp_proxy=http://localhost:3128
		export http_proxy=http://localhost:3128
		export https_proxy=http://localhost:3128
		```

	- Check logs:
		- `docker exec -it squid bash`
		- `cat /var/log/squid/access.log`
