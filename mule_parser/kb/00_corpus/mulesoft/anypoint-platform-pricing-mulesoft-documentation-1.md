# Anypoint Platform Pricing | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/pricing](https://docs.mulesoft.com/general/pricing)

---

mule.nano

# Anypoint Platform Pricing

The Usage Reports page supports pricing packages for [integration](https://www.mulesoft.com/anypoint-pricing). When your organization opts in to a usage-based pricing plan, such as the Anypoint Integration Advanced package, you must redeploy your apps. After redeploying your apps, your usage reports are shown.

For CloudHub and CloudHub 2.0, apps are automatically redeployed during the monthly runtime patch update cycle. For more information, see [CloudHub Runtime Continuous Updates](../cloudhub/cloudhub-app-runtime-version-updates) and [CloudHub 2.0 Operating System Patch Updates](../cloudhub-2/ch2-patch-updates).

For Runtime Fabric, you must manually redeploy apps to remain in compliance with your Anypoint Platform contract.

## Metrics Definitions

Usage-based pricing packages and their usage reports are based on your organization’s use of allotted Mule components.

To understand the technical aspects of metering and pricing concepts within Anypoint Platform, see [Usage and Pricing Metrics Reference](usage-metrics) documentation.

## Global Resource Pool Limits

Root organizations provisioned with usage-based pricing receive a shared global pool of CPU and memory resources for CloudHub and CloudHub 2.0 deployments across all business groups and environments in the organization. This pool of resources is large enough to consume all the purchased flows and messages without interruption.

If an organization runs out of resources, actions that consume more resources, such as deploying new applications or starting stopped applications are blocked until sufficient resources are available. You can free up resources by stopping or deleting unused applications, or reducing the replica size or resources that an existing application consumes.

When your organization approaches the resource limit on the Applications List UI, Application Deployment UI, and Manage Application UI, you receive a warning. To avoid reaching limits, allocate only the needed resources by using granular replica sizes in CloudHub and CloudHub 2.0.

Contact Support if you require an exception when you reach the resource limit.

| This limit doesn’t impact applications configured with [Configuring Horizontal Autoscaling (HPA) for CloudHub 2.0 Deployments](../cloudhub-2/ch2-configure-horizontal-autoscaling). You can continue to deploy applications if Horizontal Pod Autoscaling is enabled even if you reach the global resource limits. | 

## CloudHub 2.0 Application Deployment

For organizations provisioned with a usage-based pricing package, CloudHub 2.0 uses replica sizing for application deployment. You can choose replica sizes based on the application profile or size and display the equivalent in terms of legacy vCores. Replica sizes with the suffix `.mem` are memory-intensive options with the same compute.

| Offering | Equivalent vCore Size | Total Memory | Heap Memory | Storage | 
|---|---|---|---|---|
| 0.05 | 1 GB | 0.5 GB | 8 GB | |
| mule.micro | 0.1 | 1 GB | 0.5 GB | 8 GB | 
| mule.micro.mem | 0.1 | 2 GB | 1 GB | 8 GB | 
| mule.small | 0.2 | 2 GB | 1 GB | 8 GB | 
| mule.medium | 0.5 | 3 GB | 1.5 GB | 10 GB | 
| mule.medium.mem | 0.5 | 5 GB | 2.5 GB | 10 GB | 
| mule.large | 1 | 4 GB | 2 GB | 12 GB | 
| mule.large.mem | 1 | 8 GB | 4 GB | 12 GB | 
| mule.xlarge | 2 | 7 GB | 3.5 GB | 20 GB | 
| mule.xlarge.mem | 2 | 12 GB | 6 GB | 20 GB | 
| mule.2xlarge | 4 | 15 GB | 7.5 GB | 20 GB | 

During the monthly patching cycle, your applications automatically migrate to an equivalent replica size.

## Access Management Entitlements

Accounts provisioned with a usage-based pricing package show flows, messages, and throughput entitlements in Access Management instead of vCores. These entitlements are available only at the root organization level. Because vCores are no longer the purchased entity, they can no longer be tracked or allocated among business groups. To view your monthly usage of flows, messages, and throughput, [access usage reports](usage-reports#access-usage-reports) in the Access Management UI.