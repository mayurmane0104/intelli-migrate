# Inter-network traffic privacy in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/internetwork-traffic-privacy.html](https://docs.aws.amazon.com/quick/latest/userguide/internetwork-traffic-privacy.html)

---

To use Amazon Quick, users need access to the internet. They also need access to a compatible browser or a mobile device with the Amazon Quick mobile app installed. They don't need access to the data sources they want to analyze. This access is handled inside Amazon Quick. User connections to Amazon Quick are protected through the use of SSL. So that users can access Amazon Quick, allow access to HTTPS and Web Sockets Secure (wss://) protocol.

You can use a Microsoft AD connector and single sign-on (IAM Identity Center) in a corporate network environment. You can further restrict access through the identity provider. Optionally, you can also use MFA.

Amazon Quick accesses data sources by using connection information supplied by the data source owner in Amazon Quick. Connections are protected both between Amazon Quick and on-premises applications and between Amazon Quick and other AWS resources within the same AWS Region. For connections to any source, the data source must allow connections from Amazon Quick.

## Traffic between service and on-premises clients and applications

      You have two connectivity options between your private network and AWS:

- 
          An AWS Site-to-Site VPN connection. For more information, see [What is AWS site-to-site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- 
          An Direct Connect connection. For more information, see [What is AWS direct connect?](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)

If you are using AWS API operations to interact with Amazon Quick through the network,
        clients must support Transport Layer Security (TLS) 1.0. We recommend TLS 1.2. Clients must
        also support cipher suites with Perfect Forward Secrecy (PFS), such as Ephemeral
        Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman Ephemeral (ECDHE). Most modern systems
        such as Java 7 and later support these modes. You must sign requests using an access key ID
        and a secret access key that are associated with an IAM principal, or you can use the
          [AWS Security Token
          Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) to generate temporary security credentials to sign requests. 

## Traffic between AWS resources in the same region

      An Amazon Virtual Private Cloud (Amazon VPC) endpoint for Amazon Quick is a logical entity within a VPC that allows connectivity only to Amazon Quick. The VPC routes requests to Amazon Quick and routes responses back to the VPC. For more information, see the following:

- 
          [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)in the*Amazon VPC User Guide*