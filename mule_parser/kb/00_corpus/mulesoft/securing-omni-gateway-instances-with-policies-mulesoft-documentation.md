# Securing Omni Gateway Instances with Policies | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/gateway/latest/flex-gateway-secure-apis](https://docs.mulesoft.com/gateway/latest/flex-gateway-secure-apis)

---

# Securing Omni Gateway Instances with Policies

Policies enforce rules when Omni Gateway processes requests, enabling you to secure and govern your Omni Gateway API, agent, and tool instances.

MuleSoft provides policies that you can apply to your instances via Anypoint Platform or declarative configuration files. The provided policies include rate limiting, caching, authentication, authorization, threat protection, monitoring, logging. For more information about MuleSoft-provided policies, see the [Inbound Policies Directory](policies-included-directory) and [Outbound Policies Directory](policies-outbound-directory).

To extend existing functionality or define new functionality, create custom policies based on your specific business requirements. For information about creating custom policies, see [Omni Gateway Policy Development Kit (PDK) Overview](../../pdk/latest/policies-pdk-overview).

Automated policies enable your instances to comply with common security and logging requirements by automatically applying the same set of policies to all instances running in Omni Gateway. See [Automated Policies](policies-automated-overview) for more information.

To apply a policy for Managed Omni Gateway or Connected Mode, see [Applying Policies for Managed Omni Gateways and Connected Mode](flex-gateway-secure-conn).

To apply a policy in Local Mode, see [Applying Policies in Local Mode](flex-gateway-secure-local).

For information about policy reordering, see [Ordering Policies](policies-reorder).

For information about DataWeave support, see [DataWeave Support in Omni Gateway Policies](policies-flex-dataweave-support).