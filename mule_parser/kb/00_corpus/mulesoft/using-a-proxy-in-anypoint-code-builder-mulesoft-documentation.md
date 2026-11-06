# Using a Proxy in Anypoint Code Builder | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/ref-proxy-settings](https://docs.mulesoft.com/anypoint-code-builder/ref-proxy-settings)

---

Anypoint Platform services: CloudHub, Exchange, Core Services

# Using a Proxy in Anypoint Code Builder

Execute network-dependent functions in Anypoint Code Builder, such as publishing to Exchange, logging into Anypoint Platform, and running or debugging applications, by configuring your proxy settings in Visual Studio Code (VS Code).

| Proxy settings doesn’t work on the cloud IDE | 

## Before You Begin Configuring Your Proxy

Take into account these considerations before configuring your proxy setting in VS Code:

- 
When setting a proxy URL, the `protocol`can be`HTTP`or`SOCKS`. For example:- 
PROTOCOL://username:password@host:port 
- 
PROTOCOL://host:port Anypoint Code Builder supports `SOCKS`proxies without authentication but doesn’t support`SOCKS`proxies with basic authentication.
 
- 
- 
Anypoint Code Builder ignores these fields and reads settings from the proxy URL and the no-proxy list: - 
Proxy Authorization 
- 
Proxy Kerberos Service Principal 
- 
Proxy Strict SSL 
 
- 
- 
To exclude certain hosts from the proxy, use the **Proxy bypass**settings.

## Configure Your Proxy Settings in VS Code

To configure your proxy settings for Anypoint Code Builder:

- 
Open VS Code. 
- 
Open VS Code settings: - 
In Windows, go to **File > Preferences > Settings**.
- 
In macOS, go to **Code > Settings > Settings**.
 
- 
- 
Search for "proxy" in the settings search bar. 
- 
Configure your proxy URL and no-proxy settings. 
- 
Configure your proxy settings in your Maven `settings.xml`file. See[Configure a Proxy in Maven](https://maven.apache.org/guides/mini/guide-proxies.html)for configuration instructions.
- 
Set the 'Proxy Support' setting to 'override' or 'on'. 
- 
Restart VS Code to apply your changes. 

## Add Anypoint Platform URLs to an Allowlist

If your organization uses an allowlist, add these Anypoint Code Builder and Anypoint Platform URLs:

| MuleSoft | URL | 
|---|---|
| 
 | |
| Assets downloaded from Exchange | 
 | 
| Resources for API Portals | 
 | 

| Third Party | URL | 
|---|---|
| Eclipse libraries and Eclipse update sites | 
 | 
| MuleSoft Maven repositories and connectors update site | 
 | 

| For services that use the web browser, such as the LoginorExchangeoperations, refer to the browser documentation to learn about the browser network requirements. If you use an external identity provider (IdP), you must also grant permission to other third-party domains. |