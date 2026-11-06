# Infrastructure Security for this AWS Product or Service - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/infrastructure-security.html](https://docs.aws.amazon.com/cli/latest/userguide/infrastructure-security.html)

---

This AWS product or service uses managed services, and therefore is protected by the AWS
    global network security. For information about AWS security services and how AWS protects
    infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To
    design your AWS environment using the best practices for infrastructure security, see 

[Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html)in

*Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access this AWS Product or Service through the network. Clients must support the following:

- 
          Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3. 
- 
          Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes. 

Additionally, requests must be signed by using an access key ID and a secret access key
        that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/Welcome.html) (AWS STS) to generate temporary
        security credentials to sign requests.

This AWS product or service follows the [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) 
  through the specific Amazon Web Services (AWS) services it supports. For AWS service security information, see the 

[AWS service security documentation page](https://docs.aws.amazon.com/security/?id=docs_gateway#aws-security)and

[AWS services that are in scope of AWS compliance efforts by compliance program](https://aws.amazon.com/compliance/services-in-scope/).