# Anypoint Platform Hosting Overview | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/hosting-home](https://docs.mulesoft.com/hosting-home)

---

# Anypoint Platform Hosting Overview

Host the Anypoint Platform control plane and runtime plane in different locations to meet your security, data privacy, and compliance requirements. Choose from MuleSoft-managed cloud options or self-hosted environments to control where your data is stored and processed. Each option keeps your data within the physical location your organization requires.

## Control Plane and Runtime Plane

Anypoint Platform architecture separates into two distinct planes that can be hosted independently:

![Diagram of contents of the control plane and runtime plane](_images/intro-control-runtime-planes.png)


- Control plane
- 
The components you use to design, deploy, and manage APIs and Mule applications. The control plane includes Anypoint Design Center, Anypoint Management Center, and Anypoint Exchange. 
- Runtime plane
- 
The components where your APIs and Mule applications are deployed and made available to your users. The runtime plane includes the Mule runtime engine and supporting services. 

## Control Plane Hosting Options

MuleSoft provides cloud-managed and self-hosted control plane options. This table summarizes each option, including data residency and applicable compliance standards.

| Control Plane | Platform URL | Data Residency | Description | Compliance / Notes | 
|---|---|---|---|---|
| US Cloud (default) | 
 | United States | MuleSoft-managed control plane hosted in the US. Supports the widest range of runtime regions globally. | Standard commercial terms | 
| EU Cloud | 
 | European Union | MuleSoft-managed control plane hosted in the EU. Supports EU-based runtime regions. | EU data residency | 
| Canada Cloud | 
 | Canada | MuleSoft-managed control plane hosted in Canada. See  | Canadian data residency | 
| Japan Cloud | 
 | Japan | MuleSoft-managed control plane hosted in Japan. See  | Japanese data residency | 
| India Cloud | 
 | India | MuleSoft-managed control plane hosted in India. See  | Indian data residency | 
| MuleSoft Government Cloud | 
 | United States | Federal Risk and Authorization Management Program (FedRAMP)-compliant control plane managed by MuleSoft, suitable for US government agencies. | FedRAMP authorized. See  | 
| Customer-Hosted (Anypoint Platform Private Cloud Edition (PCE)) | N/A (self-hosted) | Customer-managed | Self-hosted control plane deployed in your own data center, virtual server, or third-party cloud (for example, Amazon Web Services (AWS)). You control where assets and metadata are stored. | Full data sovereignty. See  | 

### Available Runtime Regions by Control Plane

This table lists the runtime regions available for each control plane:

| Control Plane | Geographic Area | Region | Region Name | 
|---|---|---|---|
| 
 | North America | US East (N. Virginia) | 
 | 
| US East (Ohio) | 
 | ||
| US West (N. California) | 
 | ||
| US West (Oregon) | 
 | ||
| Canada (Montreal) | 
 | ||
| South America | Brazil (São Paulo) | 
 | |
| Asia Pacific | Singapore (Singapore) | 
 | |
| Australia (Sydney) | 
 | ||
| Japan (Tokyo) | 
 | ||
| Europe | Ireland (Dublin) | 
 | |
| Germany (Frankfurt) | 
 | ||
| UK (London) | 
 | ||
| 
 | Europe | Ireland (Dublin) | 
 | 
| Germany (Frankfurt) | 
 | ||
| 
 | North America | Canada (Montreal) | 
 | 
| 
 | Asia Pacific | Japan (Tokyo) | 
 | 
| 
 | Asia Pacific | India (Mumbai) | 
 | 
| 
 | US Government | US GovCloud (West) | 
 | 

### Anypoint MQ in Government Cloud

You can’t access or configure some Anypoint MQ features, such as client apps and unencrypted queues.
For information, see [Anypoint MQ in MuleSoft Government Cloud](../mq/#mq-in-govcloud).

## Runtime Plane Hosting Options

MuleSoft provides different options for hosting the runtime plane:

| Runtime Option | Description | Managed By | Key Characteristics | 
|---|---|---|---|
| CloudHub 2.0 | Fully managed, containerized integration platform as a service (iPaaS) for deploying APIs and integrations as lightweight containers in the cloud. Supports deployments across 12 regions globally with single or shared tenancy. | MuleSoft | Auto-scaling, high availability, dynamic infrastructure. See  | 
| CloudHub | MuleSoft’s cloud-based environment for hosting Mule runtime. Provides high availability, clustering, failover, and load balancing. | MuleSoft | See  | 
| Runtime Fabric | Container service for running Mule applications and API gateways in your own data center or third-party cloud. Bundled with Docker and Kubernetes for high availability, failover, clustering, and load balancing. | Customer (infrastructure) and MuleSoft (orchestration) | |
| Hybrid Standalone Runtimes | Mule runtime engine hosted in your environment (physical server, virtual machine (VM), or cloud like AWS/Azure) with centralized management through the MuleSoft control plane. | Customer (infrastructure) and MuleSoft (management) | Deployments within your trust boundary with cloud-based centralized management. See  | 
| Standalone Runtimes | Mule runtime engine on a single instance with no required connection to the control plane. You manage high availability (HA), failover, clustering, and load balancing manually. Suited for air-gapped or disconnected environments. | Customer (fully self-managed) | 

### Component Support by Runtime Option

Not all Anypoint Platform components are available in each runtime option:

| Component | CloudHub 2.0 | CloudHub | Runtime Fabric | Standalone | 
|---|---|---|---|---|
| Mule runtime engine | Yes | Yes | Yes | Yes | 
| Anypoint MQ | Yes | Yes | Yes | Yes | 
| Anypoint Object Store v2 | Yes | Yes | No  | No  | 
| Anypoint DataGraph | No | Yes | No | No | 
| Connectors  | Yes | Yes | Yes | Yes | 

1 Runtime Fabric and standalone runtimes support Mule clustering instead of Object Store v2. On Runtime Fabric, multiple replicas of the same application can share objects. See [Cluster Runtime Instances](../mule-runtime/latest/choosing-the-right-clustering-topology).

2 File system connectors (for example, Anypoint Connector for File) are not supported on Runtime Fabric because deployed apps lack file system access.

## Control Plane and Runtime Plane Compatibility

This matrix shows which runtime plane options are supported in each control plane:

| Runtime Plane | US Cloud | EU Cloud | Canada Cloud | Japan Cloud | MuleSoft Government Cloud | Anypoint Platform PCE | 
|---|---|---|---|---|---|---|
| CloudHub 2.0 | Yes | Yes | Yes | Yes | No | No | 
| CloudHub | Yes | Yes | No | No | Yes | No | 
| Runtime Fabric | Yes | Yes | Yes | Yes | No | No | 
| Hybrid Standalone Runtimes | Yes | Yes | No | No | Yes | Yes | 

## Choosing a Hosting Option

Anypoint Platform lets you host the control plane and runtime plane independently. Depending on your requirements, you can choose from these options:

- 
Use Anypoint Platform in the MuleSoft-managed control plane and runtime plane. 
- 
Host and manage the runtime plane within your own infrastructure while connecting it with the MuleSoft-managed control plane. 
- 
Host both the control plane and runtime plane locally within your infrastructure. 

See the [Control Plane Hosting Options](#control-plane-hosting-options) and [Runtime Plane Hosting Options](#runtime-plane-hosting-options) tables for available options, and the [Control Plane and Runtime Plane Compatibility](#support-matrix-control-plane) to verify which combinations are supported.