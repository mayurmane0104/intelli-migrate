# Using API Catalog CLI with a Network Proxy | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/apicat-use-proxy](https://docs.mulesoft.com/exchange/apicat-use-proxy)

---

`$ export HTTP_PROXY=http://`*proxy-server*:80

or

`$ export HTTPS_PROXY=https://`*proxy-server*:443

MuleSoft MCP Support is now available

Create connected experiences with AI

Future of connected AI agents

Go from composability to agent actionability

2.x

Mule 4

1.12

2.x

Using API Catalog CLI with a Network Proxy

Using API Catalog CLI with a Network Proxy

API Catalog CLI can be run through a network proxy to add a layer of security. To use the API Catalog CLI with a proxy server, configure the `HTTP_PROXY` or `HTTPS_PROXY` environment variables with the hostname or IP addresses of your proxy servers as shown in the following sections.

To configure a proxy server that does not require authentication, use the following commands:

Linux, macOS, or Unix

`$ export HTTP_PROXY=http://`*proxy-server*:80

or

`$ export HTTPS_PROXY=https://`*proxy-server*:443

Windows

`> set HTTP_PROXY=http://`*proxy-server*:80

or

`> set HTTPS_PROXY=https//`*proxy-server*:443

To configure a proxy server that requires authentication, use these commands:

Linux, macOS, or Unix

`$ export HTTP_PROXY=http://`*username*:*password*@*proxy-server*:80

or

`$ export HTTPS_PROXY=https://`*username*:*password*@*proxy-server*:443

Windows

`> set HTTP_PROXY=http://`*username*:*password*@*proxy-server*:80

or

`> set HTTPS_PROXY=https://`*username*:*password*@*proxy-server*:443