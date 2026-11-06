# Omni Gateway Deployment Models | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/gateway/latest/flex-architecture-basic-deployments](https://docs.mulesoft.com/gateway/latest/flex-architecture-basic-deployments)

---

# Omni Gateway Deployment Models

Omni Gateway supports multiple deployment models, which apply to both Connected Mode and Local Mode:

You can extend the deployment models in this overview to all technological stacks that have the appropriate network controls applied. For more information about routing configuration modes, see [Routing Configuration Methods](#routing-configuration-methods).

All the following diagrams show Omni Gateway running in Connected Mode. For Omni Gateway running in Local Mode, the only difference is that Anypoint Platform would not be present in the deployment model. This does not affect how information flows between Omni Gateway and the upstream and downstream services.

## Standalone Deployment

In a standalone deployment, Omni Gateway acts as a standalone service that protects one or more integration API flows by managing internal traffic.

As the following diagram shows, all traffic is inside an organization-owned network. The traffic passes through Omni Gateway before reaching the consumer APIs.

![In a standalone deployment, Omni Gateway and the consumer applications are in the same network.](_images/ad-standalone-deployment.png)


## Ingress Deployment

Similar to standalone deployment, in an ingress deployment, Omni Gateway acts as a standalone service that protects one or more integration API flows. However, in an ingress deployment, Omni Gateway manages external traffic entering the internal network. Ingress deployment is the most common deployment model.

Omni Gateway can act as both an ingress and an egress gateway.

As the following diagram shows, all external traffic passes through Omni Gateway before reaching the consumer APIs. Omni Gateway is typically deployed behind a load balancer, and the consumer application does not belong to the same network as Omni Gateway or the APIs.

![In an ingress deployment, Omni Gateway and the consumer applications are in different networks.](_images/ad-ingress-deployment.png)


| Ingress deployment is not the same as a Kubernetes Ingress controller or Ingress `Resource`. For more information about routing configuration, see[Routing Configuration Methods](#routing-configuration-methods). | 

## Egress Deployment

An egress deployment is the opposite deployment model of an ingress deployment. Omni Gateway still acts as a standalone service that protects one or more integration API flows. However, in an egress deployment, Omni Gateway manages internal traffic exiting the internal network, for example, API requests to non-organization-owned APIs.

Omni Gateway can act as both an ingress and an egress gateway.

As the following diagram shows, all internal traffic from the consumer application passes through Omni Gateway before reaching the external APIs.

![A diagram of Anypoint Platform depicting the flow of data between the platform, an Omni Gateway, APIs, and a user](_images/ad-egress-deployment.png)


## Sidecar Deployment

In a sidecar deployment, each Omni Gateway deployment only protects the APIs exposed by its protected service. A new Omni Gateway replica is added with each new protected service.

As the following diagram shows, traffic in a sidecar deployment passes through Omni Gateway to the respective consumer API. The consumer application can belong to the same network as Omni Gateway or an external network.

![In a sidecar deployment, Omni Gateway and the consumer application are in the same Kubernetes pod.](_images/ad-sidecar-deployment.png)


## Routing Configuration Methods

There are different routing configuration methods dependent on what mode Omni Gateway is running in or what technological stack Omni Gateway is deployed on.

How connections between Omni Gateway and services are configured is independent of the deployment model.

### Control Plane

In control plane routing configuration, Omni Gateway and service connections are configured in a remote control plane. For Omni Gateway, the control plane is Anypoint Platfrom. Control plane configuration is only available in Omni Gateway Connected Mode.

### Custom Resource Definitions (CRDs)

In custom resource definitions (CRDs) routing configuration, Omni Gateway and service connections are configured in custom resource yaml files.

For Omni Gateway, the CRDs are `APIinstance`, `Service`, `PolicyBinding`, and `Configuration` and are defined in the [Declarative Configuration Reference Guide](flex-local-configuration-reference-guide).

In Omni Gateway CRDs define connections in Local Mode but are also necessary for some connections in Connected Mode.

### Kubernetes Ingress Resource

Omni Gateways running in Local Mode and deployed on Kubernetes can use Kubernetes `Ingress` resources to define connection routing. When routing is defined via `Ingress` resources, Omni Gateway acts as an Ingress Controller. `Ingress` resources are only avaliable in Kubernetes Local Mode.

You can use `Ingress` resources and CRDs simultaneously.

For more information about how to configure Omni Gateway as an Ingress Controller, see [Configure Omni Gateway as an Ingress Controller in Local Mode](flex-gateway-k8-ingress-class).