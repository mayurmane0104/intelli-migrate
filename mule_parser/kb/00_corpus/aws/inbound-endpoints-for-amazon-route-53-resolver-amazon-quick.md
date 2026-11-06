# Inbound endpoints for Amazon Route 53 Resolver - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-route-53.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-route-53.html)

---

*Amazon Route 53 Resolver* provides DNS query capabilities to your VPC.
            Route 53 Resolver resolves all local DNS queries and recursively looks up any DNS queries
            that aren't local on public DNS servers. 

Amazon Quick can't directly use Route 53 Resolver to query private DNS servers. However,
            you can set up Route 53 Resolver inbound endpoints to make these queries indirectly. For
            more information about inbound endpoints, see [Forwarding inbound DNS queries to your VPCs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) in the *Route 53 Resolver
                Developer Guide*. To use inbound endpoints in Amazon Quick, provide the IP
            addresses of the endpoints for **DNS resolver endpoints** when you
            create a VPC connection.