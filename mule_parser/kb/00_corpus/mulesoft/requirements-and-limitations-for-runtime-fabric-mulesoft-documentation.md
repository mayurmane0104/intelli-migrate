# Requirements and Limitations for Runtime Fabric | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/runtime-fabric/latest/limitations-self](https://docs.mulesoft.com/runtime-fabric/latest/limitations-self)

---

# Requirements and Limitations for Runtime Fabric

Review the following requirements and limitations before installing, configuring, and managing Anypoint Runtime Fabric.

## MuleSoft License Compliance

You are responsible for ensuring that you remain compliant with your MuleSoft licensing. To remain compliant, ensure one of the following:

- 
The sum of CPU Limits allocated to each Mule application replica is less than or equal to the total license quantity. 
- 
The total CPU capacity provided by Runtime Fabric worker nodes running Mule applications is less than or equal to the licensed quantity. 

For Runtime Fabric usage reports, see [Runtime Fabric Compliance Tracking](../../general/usage-metrics#rtf-compliance-tracking).

## Limitations

The following table provides Runtime Fabric limitations.

| Limitation | Description | 
|---|---|
| Node types | VM-based nodes are required. For example, Fargate is not supported. | 
| Replicas per application | Runtime Fabric supports a maximum of 16 replicas per application in all forms except when you use the usage pricing and Horizontal Pod Autoscaling feature. In this case, the maximum number of replicas per application is 8. | 
| Associated environments per Runtime Fabric | You can associate a Runtime Fabric with up to 200 environments in any Business Group. For example, if you associate a development and a production environments with Org A and another development environment with Org B, that is three environment associations. | 
| Business groups | You can create up to 50 Runtime Fabrics per org in a Business Group. Any sub org can contain up to 50 Runtime Fabrics, in addition to any shared with another sub org. For example, for a parent Org A and its child Org B, you can have 50 Runtime Fabrics in Org A and 50 in Org B. You can also share all 50 Runtime Fabrics from Org A with Org B, and as a result, you will see 100 Runtime Fabrics in total in the list view of Org B. | 

## Use of Third-Party Software within a Runtime Fabric K8s Cluster

You are expected to use authorized namespaces features to ensure isolation between third-party software and Runtime Fabric software or Mule deployments. Install third-party software in non-rtf specific namespaces to ensure they do not interfere with Runtime Fabric or Mule runtime engine functionality.

## How Antivirus and DPI Software Impacts Runtime Fabric Functionality

Anypoint Runtime Fabric has specific hardware and OS requirements. MuleSoft Support provides Support SLA and Severity Levels based on our validation and certification of the requirements specified in the installation prerequisites for [Runtime Fabric ](./).

Some third-party software requires root access to the host. This software includes, but is not limited to, antivirus and DPI software, which has been found to interfere with the behavior and requirements of Runtime Fabric. In many support cases where MuleSoft Support has detected antivirus software, they have seen issues such as port blocking, node-to-node communication blocking, Docker default bridge deletion, and filesystem access issues that interfere with Runtime Fabric installation, upgrade, and normal operations.

In the event that abnormal behavior is observed with Runtime Fabric, you may be asked to disable any running third-party software (including anti-virus or DPI software) to determine if it is the cause of the behavior. If disabling such software restores proper Runtime Fabric functionality, this would demonstrate an implicit incompatibility between that software package and Runtime Fabric, and we would consider the support case resolved.

If you are strictly required to run traditional security tools that interfere with certain components of Runtime Fabric, vendors and security experts that support Kubernetes can support you in meeting this requirement. Cloud platform vendors often add cloud-centric controls that are consistent with well-known security benchmarks, such as the [Center for Internet Security (CIS) Kubernetes Benchmark](https://www.cisecurity.org/benchmark/kubernetes/).

## Requirements for Runtime Fabric

The following descriptions provide you with the general requirements for running Anypoint Runtime Fabric.

### Kubernetes Support

Runtime Fabric requires a Kubernetes cluster that is provisioned and operational. Verify whether your environment is correctly configured using the `rtfctl` command-line utility. See [Install Runtime Fabric](install-self-managed).

Refer to the [release notes](../../release-notes/runtime-fabric/runtime-fabric-release-notes-2.x.x) for the list of supported Kubernetes versions for your Runtime Fabric.

### Supported Architectures

Anypoint Runtime Fabric requires worker nodes with the x86-64 architecture. ARM-based nodes are not supported.

### Operating Systems

Anypoint Runtime Fabric works on any Linux distribution supported by:

- 
Alibaba Cloud Container Service (ACK) 
- 
Amazon Elastics Kubernetes Service (EKS) 
- 
Amazon EKS Anywhere (EKS-A) 
- 
Google Kubernetes Engine (GKE) 
- 
Microsoft Azure Kubernetes Service (AKS) 
- 
Rancher Kubernetes Engine (RKE2) 
- 
Red Hat OpenShift 
- 
VMware Tanzu 

Runtime Fabric agent supports most Linux distributions. However, you must conduct your own testing to ensure that Runtime Fabric is compatible with your chosen operating system. Also validate [Mule runtime engine compatibility](../../mule-runtime/latest/hardware-and-software-requirements) and [Anypoint Monitoring compatibility](../../monitoring/am-installing#os-support) with your operating system.

### Nodes and Resources

In general, you should follow the best practices provided by your Kubernetes vendor to ensure availability and simplify the administration of your infrastructure.

To ensure optimal performance, Runtime Fabric installation requires at least two nodes each equipped with:

- 
Minimum of two CPU cores 
- 
At least 15 GiB of RAM 
- 
At least 250 GiB of available disk space 

Adjust the number of nodes and amount of resources allocated according to the amount and type of workload you run on each Anypoint Runtime Fabric instance.

### Runtime Fabric Kubernetes Roles

The following Runtime Fabric roles manage data stored in Kubernetes secrets:

- 
`rtf:agent`
- 
`rtf:certificate-renewal`
- 
`rtf-restricted`
- 
`rtf:cluster-status`
- 
`rtf:install`
- 
`rtf:persistence-gateway-clro-read-only`
- 
`rtf:upgrade`
- 
`rtf:mule-clusterip-service`

| Starting with Runtime Fabric agent version 3.0.0, the  | 

Runtime Fabric components, such as RTF agent, have a legitimate use case to consume the Kube API from the cluster where they are running to monitor or update some Kubernetes resources related to delivering Runtime Fabric features.

### Anypoint Platform Roles and Permissions

To successfully use Anypoint Runtime Fabric, your Anypoint Platform account must have the following permissions:

- 
To manage permissions for Anypoint Platform users, you must have the ability to use [Anypoint Access Management](../../access-management/).
- 
To deploy and manage applications ensure you have: - 
The ability to use Anypoint Runtime Manager 
- 
The Exchange Contributors permission enabled for your Anypoint Platform account 
- 
The read permissions for Applications and Runtime Fabric instances, which are needed to view applications on the Applications page in the Runtime Manager 
 
- 
- 
To use Runtime Fabric, you must have the Organization Administrators permission or the Manage Runtime Fabrics permission for the corresponding environments. 
- 
To delete Runtime Fabric instances, administrators need the Manage Runtime Fabrics permission at the organization level. 

### Network Configuration

Anypoint Runtime Fabric requires an IT administrator to configure network ports, hostnames, and certificates to function correctly. See [Configuring Your Network to Support Runtime Fabric](install-self-managed-network-configuration).

### Ingress Controller

Runtime Fabric supports any ingress controller that works well in your Kubernetes environment. It also supports a deployment model with a dedicated ingress per application. Most off-the-shelf ingress controllers support this model.

| The default behavior of the ingress controller included with GKE is to provide a separate HTTP load balancer for each application. If you find this behavior undesirable, explore possible solutions or consider using another ingress controller. | 

### Logs

Anypoint Monitoring provides access to [log data](../../monitoring/logs) for applications deployed to Runtime Fabric. To access logs with Anypoint Monitoring, you need the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform.

It is common practice for applications deployed on Runtime Fabric to log directly to `stdout`. The container runtime stores the console log in a file on disk. The storage location of this file depends on your container runtime and configuration. Refer to the documentation for your Kubernetes environment for details.

### External Log Forwarding

Anypoint Runtime Fabric does not forward logs to an external system. You are responsible for installing and managing this configuration. Any external log forwarding agent compatible with your Kubernetes environment running on Amazon EKS, AKS, or GKE can be used. Commonly used log forwarding agents include:

- 
Fluentbit 

Runtime Fabric supports Log4j appenders.

### Monitoring

[Anypoint Monitoring](../../monitoring/) provides metrics for applications and API gateways deployed to Runtime Fabric.

To collect metrics, Anypoint Monitoring employs sidecar containers as part of each application deployment on Runtime Fabric. See [Monitor Applications Deployed to Runtime Fabric](manage-monitor-applications) for details, including how to manage monitoring.

Runtime Fabric does not provide support for integrating third-party monitoring solutions.