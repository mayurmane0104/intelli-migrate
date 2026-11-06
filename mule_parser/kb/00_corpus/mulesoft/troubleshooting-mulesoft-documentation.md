# Troubleshooting | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/runtime-manager/troubleshooting](https://docs.mulesoft.com/runtime-manager/troubleshooting)

---

# Troubleshooting

If you experience problems with your deployed apps, Runtime Manager provides several tools that can help you determine the cause.

The troubleshooting resources available to you depend on your deployment strategy.

## Troubleshoot Applications

You can access information to help you troubleshoot applications using the following tools:

- 
MuleSoft Diagnostics Agent ![CloudHub 2.0 logo cloud2 active](_images/logo-cloud2-active.png)  ![CloudHub logo cloud active](_images/logo-cloud-active.png) Use the MuleSoft diagnostics agent to troubleshoot your Mule applications deployed to [CloudHub](../cloudhub/ch-diagnostics-agent)and[CloudHub 2.0](../cloudhub-2/ch2-view-diag). This feature leverages Einstein generative AI to automate diagnostics collection and provide intelligent, actionable insights.
- 
[Insight](insight)![CloudHub logo cloud active](_images/logo-cloud-active.png)  ![Hybrid logo hybrid active](_images/logo-hybrid-active.png) You can access a dashboard with key metrics and see events at an individual transaction level of detail. 
- 
[API Functional Monitoring](../api-functional-monitoring/)![CloudHub logo cloud active](_images/logo-cloud-active.png)  ![Hybrid logo hybrid active](_images/logo-hybrid-active.png)  ![Anypoint Platform PCE logo server active](_images/logo-server-active.png)  ![Runtime Fabric logo rtf active](_images/logo-rtf-active.png) Using API functional monitoring, you can automate testing and generate reports to verify API functionality and validate the results that the API generates. You can monitor APIs at each stage of the software development life cycle and in production. 
- 
View application log data ![CloudHub 2.0 logo cloud2 active](_images/logo-cloud2-active.png)  ![CloudHub logo cloud active](_images/logo-cloud-active.png) For applications deployed to [CloudHub](../cloudhub/viewing-log-data)and[CloudHub 2.0](../cloudhub-2/ch2-view-logs), you can access log data that includes deployment messages and events for each worker or replica and Mule runtime engine logs.For applications deployed to your own servers, you can export log data to third-party software to view there. 

## Troubleshoot Servers

![Hybrid logo hybrid active](_images/logo-hybrid-active.png) 

![Anypoint Platform PCE logo server active](_images/logo-server-active.png)


With applications deployed to your own servers, you can access information to help you troubleshoot them through the following tools:

- 
Use alerts and dashboards to get information about the servers. 
- 
[Export data to external analytics tools](sending-data-from-arm-to-external-analytics-software)Send data to an external tool like Splunk or ELK. 

## Troubleshoot Runtime Manager Agent Upgrades

![Hybrid logo hybrid active](_images/logo-hybrid-active.png) 

![Anypoint Platform PCE logo server active](_images/logo-server-active.png)


### TLS Handshake Failures After Upgrading to Runtime Manager Agent 2.7.x in FIPS Environments

If you upgrade the Runtime Manager Agent from 2.6.x to 2.7.x in a FIPS-enabled environment, you might see `handshake_failure` errors in your `mule_ee.log` files.

Cause

Runtime Manager Agent 2.6.x had no `tls-fips140-2.conf` file mechanism and used all JVM-supported ciphers with TLSv1.2. Starting with 2.7.x, the agent reads its cipher list from the `tls-fips140-2.conf` file. If ciphers required by your environment are not present in that file, TLS handshakes fail.

Solution

Add the required ciphers to the `tls-fips140-2.conf` file and restart the Runtime Manager Agent.