# Deployment Options | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/runtime-manager/deployment-strategies](https://docs.mulesoft.com/runtime-manager/deployment-strategies)

---

Runtime Fabric supports Anypoint Monitoring.

This feature is available only if your organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform. For more information, see the [Pricing and Packaging](../general/pricing) documentation.

# Deployment Options

Mule applications that run in the Anypoint Studio or Anypoint Code Builder IDEs deploy to an embedded test server in within the IDE. Because this server is not meant for production deployment and uptime restrictions apply, deploy your Mule applications using one of the deployment options supported by Anypoint Runtime Manager.

## CloudHub 2.0

CloudHub 2.0 is a fully managed, containerized integration platform as a service (iPaaS) where you can deploy APIs and integrations as lightweight containers in the cloud.

You can deploy your applications from the [Anypoint Platform](https://anypoint.mulesoft.com) Runtime Manager cloud console and host them in [CloudHub 2.0](../cloudhub-2/). For more information about how to deploy applications to CloudHub 2.0, see [Deploying Apps to CloudHub 2.0](../cloudhub-2/ch2-deploy).

## CloudHub

CloudHub is a complete integration platform as a service (iPaaS) that provides server functionality for you to deploy your applications without having to configure a hosting environment. Based on your contract, you control how many resources to assign to your application.

You can deploy your applications from the [Anypoint Platform](https://anypoint.mulesoft.com) Runtime Manager cloud console and host them in [CloudHub](../cloudhub/). For more information on how to deploy applications to CloudHub, see [Deploy to CloudHub](../cloudhub/deploying-to-cloudhub).

## Hybrid Deployments

With the hybrid deployment option, you deploy your applications from the Runtime Manager cloud console to your Mule servers and use Runtime Manager to manage them. This option provides you with flexibility and control over your on-premises security but requires you to provide the hosting infrastructure.

To use the hybrid option, you first register your Mule servers with the Runtime Manager agent. Then, from Runtime Manager, you can optionally add those servers to server groups or clusters to provide high availability. Finally, you deploy your applications from Runtime Manager to either a server, server group, or cluster.

For more information on how to deploy applications to your Mule servers, see [Deploy to Your Servers](deploying-to-your-own-servers).

## Anypoint Platform Private Cloud Edition

[Anypoint Platform Private Cloud Edition](../private-cloud/latest/) is a containerized distribution of the management and engagement capabilities of Anypoint Platform that you host on-premises or in your organization’s private cloud environment.

If your organization has strict regulatory or compliance requirements that limit the use of cloud solutions, you can use Anypoint Platform PCE to deploy and host your applications on-premises.

For more information on how to deploy applications to Anypoint Platform Private Cloud Edition, see [Deploy to Your Servers](deploying-to-your-own-servers).

## Anypoint Runtime Fabric Deployments

Anypoint Runtime Fabric is a container service that automates the deployment and orchestration of Mule applications and API gateways. Runtime Fabric runs within a customer-managed infrastructure on AWS, Azure, virtual machines (VMs), and bare-metal servers.

Runtime Fabric contains all of the components it requires. These components, including Docker and Kubernetes, are optimized to work efficiently with Mule runtimes and other MuleSoft services.

To use the Runtime Fabric option, you first create a Runtime Fabric using Runtime Manager. Then, you install Runtime Fabric on your infrastructure. Finally, you deploy your applications from the Runtime Manager cloud console to the Runtime Fabric you created.

You can deploy your applications from the [Anypoint Platform](https://anypoint.mulesoft.com) Runtime Manager cloud console and host them in [Anypoint Runtime Fabric](../runtime-fabric/latest/). For more information on how to deploy applications to Runtime Fabric, see [Deploying Mule Apps to Runtime Fabric Using Runtime Manager](../runtime-fabric/latest/deploy-to-runtime-fabric).

## Deployment Option Icons

Icons appear at the begining of each page in the Runtime Manager documentation, indicating the deployment options to which the content applies.

| Deployment Option | Icon | 
|---|---|
| CloudHub 2.0 | 
 | 
| CloudHub | 
 | 
| Hybrid | 
 | 
| Anypoint Platform Private Cloud Edition | 
 | 
| Anypoint Runtime Fabric | 
 | 

## Runtime Manager Features

For an overview of the Runtime Manager features available with each deployment option, see:

### High Availability

| Deployment Option | Implementation | More Information | 
|---|---|---|
| CloudHub 2.0 | Via clustering with two or more replicas and Anypoint VPN. | |
| CloudHub | Via clustering with two or more workers and Anypoint VPN. | 
 | 
| Hybrid | Via server groups or clusters. Clustered Mule instances have distributed shared memory, which provides persistent VM queues, transactions, and cluster-wide data storage. | 
 | 
| Private Cloud Edition | Via server groups or clusters. Clustered Mule instances have distributed shared memory, which provides persistent VM queues, transactions, and cluster-wide data storage. | 
 | 
| Runtime Fabric | Via automatic application fail-over. You obtain high availability when you deploy two or more replicas per application. | 

### Java Versions

| Deployment Option | Version | More Information | 
|---|---|---|
| CloudHub 2.0 | Java 8, Java 17 | 
 | 
| CloudHub | Java 8, Java 17 | 
 | 
| Hybrid | See the Mule runtime engine release notes to determine the minimum supported Java version. | |
| Private Cloud Edition | See the Mule runtime engine release notes to determine the minimum Java supported version. | 

### Load Balancing

| Deployment Option | Supported Load Balancing | Alternative/Workaround | 
|---|---|---|
| CloudHub 2.0 | When deploying your application to two or more replicas, the CloudHub HTTP load balancing service distributes requests across these replicas. See  | |
| CloudHub | If your application runs on multiple workers, the CloudHub shared load automatically balances incoming traffic. See  | Use the optional dedicated load balancer (DLB) component to route external traffic to multiple Mule applications deployed to CloudHub workers in Anypoint Virtual Private Cloud (VPC). | 
| Hybrid | Not Supported. | You can manage load balancing with the tools connected to your on-premises resources. | 
| Private Cloud Edition | Not Supported. | You can manage load balancing with the tools connected to your on-premises resources. | 
| Runtime Fabric | Internal load balancer for basic load balancing. | You can also forward logs from Runtime Fabric to a rsyslog server. | 

### Logging

| Deployment Option | Description | Alternative/Workaround | More Information | 
|---|---|---|---|
| CloudHub 2.0 | CloudHub 2.0 provides access to log data that includes deployment messages and events for each replica and Mule runtime engine logs. | ||
| CloudHub | CloudHub provides a logging service for customizing log levels, searching logs, and downloading logs. | ||
| Hybrid | The Runtime Manager logging feature is not available for hybrid deployments. | You can configure on-premises applications to send data to external analytics tools, such as Splunk or ELK, to manage your logs. | 
 | 
| Private Cloud Edition | The Runtime Manager logging feature is not available for hybrid deployments. | The Runtime Manager logging feature is not available for hybrid deployments. | 
 | 
| Runtime Fabric | You can also forward logs from Runtime Fabric to a rsyslog server. | 

### Monitoring

| Deployment Option | Implementation | Functionality | More Information | 
|---|---|---|---|
| CloudHub 2.0 | - You can create alerts in  | - Run thread dumps. Configure application alerts. | -  | 
| CloudHub | Runtime Manager dashboards provide performance metrics for all deployed applications. | Alerts based on alert conditions on deployed applications. Standard notifications to inform you when events occur in your applications. Add a CloudHub connector to your application’s flows and set up custom alerts and notifications triggered by any event. | |
| Hybrid | Runtime Manager dashboards provide performance metrics for all deployed applications. | Alerts based on alert conditions on deployed applications. Standard notifications to inform you when events occur in your applications. Alerts triggered by events related to the servers on which they run. | |
| Private Cloud Edition | Anypoint Platform PCE does not support Runtime Manager dashboards. | Alerts based on alert conditions on deployed applications. Standard notifications to inform you when events occur in your applications. Alerts triggered by events related to the servers on which they run. | |
| Runtime Fabric | - The Runtime Fabric agent monitors Kubernetes Deployments labelled with  | When Kubernetes updates the state of the deployment, the agent sends that update to the control plane. | -  | 

### Object Store

| Deployment Option | Implementation | Note | More Information | 
|---|---|---|---|
| CloudHub 2.0 | You do not need to configure your applications to use Object Store in CloudHub 2.0. Additionally, Mule 4 applications support Object Store v2, which can be enabled from Anypoint Runtime Manager console. | When you enable Object Store v2 in CloudHub 2.0, note that it is rate limited. | |
| CloudHub | CloudHub provides a preconfigured default object store that you can reference using Anypoint Connector for Object Store. | Idempotent routers work only with in-memory stores. | |
| Hybrid | Not available for hybrid deployments. | To use object stores, you must configure a database to store data. | |
| Private Cloud Edition | Not available for Anypoint Platform PCE deployments. | To use object stores, you must configure a database to store data. | |
| Runtime Fabric | Not available for Runtime Fabric deployments. | To use object stores, you must configure a database to store data. | 

### Scheduling

| Deployment Option | Implementation | Note | More Information | 
|---|---|---|---|
| CloudHub 2.0 | You can use Runtime Manager to view and control the Scheduler components within the flows in your deployed applications without changing your running application. | To view the application schedules, you must have the Exchange Viewer permission, in addition to the Read Applications permission. | |
| CloudHub | You can use Runtime Manager to view and control the Scheduler components within the flows in your deployed applications. | You cannot manage CloudHub schedules using scripts. Use the  | |
| Hybrid | Not available for hybrid deployments. | To schedule tasks, use the Scheduler endpoint element in your flows. | |
| Private Cloud Edition | Not available for Anypoint Platform PCE deployments | To schedule tasks, use the Scheduler endpoint element in your flows. | |
| Runtime Fabric | Not available for Runtime Fabric deployments. | To schedule tasks, use the Scheduler endpoint element in your flows. | 

### Security Updates

| Deployment Option | Implementation | More Information | 
|---|---|---|
| CloudHub 2.0 | CloudHub 2.0 regularly applies security patches as needed to ensure that your application is secure. | |
| CloudHub | CloudHub applies security patches as needed to ensure that your application is secure and, once per month, it updates Mule to maintain the stability of your application. | |
| Hybrid | After an application is deployed and running, you must apply any security updates for the selected runtime version manually. | |
| Private Cloud Edition | After an application is deployed and running, you must apply any security updates for the selected runtime version manually. | |
| Runtime Fabric | When a security update is available for the runtime version for an app, you can see and apply the update in Runtime Manager. | 

### Shared Resource Support

| Deployment Option | Implementation | More Information | 
|---|---|---|
| CloudHub 2.0 | A shared space is an elastic cloud of resources that includes Mule instances running in a multi-tenant environment. CloudHub 2.0 provides one shared space in each supported region, to which you deploy your integration applications. | |
| CloudHub | Each application deployed to CloudHub runs on a separate virtual server. You don’t need to use domains to share ports or other resources between applications. | |
| Hybrid | When deploying on-premises, you can create  | |
| Private Cloud Edition | When deploying on-premises, you can create   | 

### Troubleshooting

| Deployment Option | Implementation | 
|---|---|
| CloudHub 2.0 | Use the MuleSoft diagnostics agent to troubleshoot your Mule applications deployed to CloudHub 2.0. This feature leverages Einstein generative AI to automate diagnostics collection and provide intelligent, actionable insights. See  | 
| CloudHub | - The  | 
| Hybrid | The  | 
| Private Cloud Edition | Anypoint Platform PCE does not include the  | 
| Runtime Fabric | Use Anypoint Monitoring to view information about applications deployed to Runtime Fabric. To obtain the health status of the cluster and components, use Runtime Fabric command-line tools. See  | 

### Horizontal Autoscaling

![CloudHub 2.0 logo cloud2 active](_images/logo-cloud2-active.png)


Horizontal autoscaling makes Mule apps deployed to CloudHub 2.0 responsive to CPU usage by automatically scaling up or down replica capacity as needed. In Kubernetes, a Horizontal Pod Autoscaler (HPA) automatically updates a workload resource to automatically match demand.

| This feature applies to select customers who opted into the new pricing and packaging model. For more details, visit [Anypoint Platform Pricing](../general/pricing). | 

## Security for Hybrid Deployments

![Hybrid logo hybrid active](_images/logo-hybrid-active.png)


By default, only metadata pushed by the Runtime Manager agent in each Mule runtime engine flows to the cloud. No application data is exposed.

The agent monitors and controls Mule, and publishes its data to the control plane. You can control Mule from external systems by calling Runtime Manager agent APIs, or you can specify that Mule publishes its data to external systems.

You can change the default behavior so that the agent pushes IDs, final average numbers, or any data you find useful for monitoring or keeping control of applications.
See [Runtime Manager Agent](runtime-manager-agent).

## Shared Resource Support for On-Premises App Deployments

![Hybrid logo hybrid active](_images/logo-hybrid-active.png) 

![Anypoint Platform PCE logo server active](_images/logo-server-active.png)


When deploying on-premises, you can create `Domain` mule projects with no flows and a set of global configuration elements to share among other applications deployed to the same server.

Use this strategy to avoid configuring the same settings and credentials for each application. You can also use it to configure multiple applications to listen on the same HTTP host and port, or other exclusive resources.

See [Shared Resources](../mule-runtime/latest/shared-resources).