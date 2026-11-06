# Elastic Load Balancing - Version 1 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-load-balancing_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-load-balancing_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Elastic Load Balancing - Version 1.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags`.

- **AWS CLI**
- 
            
                    **To add a tag to a load balancer**This example adds tags to the specified load balancer. Command: `aws elb add-tags --load-balancer-name``my-load-balancer`--tags`"Key=project,Value=lima"``"Key=department,Value=digital-media"`- 
                    For API details, see [AddTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/add-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `apply-security-groups-to-load-balancer`.

- **AWS CLI**
- 
            
                    **To associate a security group with a load balancer in a VPC**This example associates a security group with the specified load balancer in a VPC. Command: `aws elb apply-security-groups-to-load-balancer --load-balancer-name``my-load-balancer`--security-groups`sg-fc448899`Output: `{ "SecurityGroups": [ "sg-fc448899" ] }`- 
                    For API details, see [ApplySecurityGroupsToLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/apply-security-groups-to-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-load-balancer-to-subnets`.

- **AWS CLI**
- 
            
                    **To attach subnets to a load balancer**This example adds the specified subnet to the set of configured subnets for the specified load balancer. Command: `aws elb attach-load-balancer-to-subnets --load-balancer-name``my-load-balancer`--subnets`subnet-0ecac448`Output: `{ "Subnets": [ "subnet-15aaab61", "subnet-0ecac448" ] }`- 
                    For API details, see [AttachLoadBalancerToSubnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/attach-load-balancer-to-subnets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `configure-health-check`.

- **AWS CLI**
- 
            
                    **To specify the health check settings for your backend EC2 instances**This example specifies the health check settings used to evaluate the health of your backend EC2 instances. Command: `aws elb configure-health-check --load-balancer-name``my-load-balancer`--health-check`Target=HTTP:80/png,Interval=30,UnhealthyThreshold=2,HealthyThreshold=2,Timeout=3`Output: `{ "HealthCheck": { "HealthyThreshold": 2, "Interval": 30, "Target": "HTTP:80/png", "Timeout": 3, "UnhealthyThreshold": 2 } }`- 
                    For API details, see [ConfigureHealthCheck](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/configure-health-check.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-app-cookie-stickiness-policy`.

- **AWS CLI**
- 
            
                    **To generate a stickiness policy for your HTTPS load balancer**This example generates a stickiness policy that follows the sticky session lifetimes of the application-generated cookie. Command: `aws elb create-app-cookie-stickiness-policy --load-balancer-name``my-load-balancer`--policy-name`my-app-cookie-policy`--cookie-name`my-app-cookie`- 
                    For API details, see [CreateAppCookieStickinessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-app-cookie-stickiness-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-lb-cookie-stickiness-policy`.

- **AWS CLI**
- 
            
                    **To generate a duration-based stickiness policy for your HTTPS load balancer**This example generates a stickiness policy with sticky session lifetimes controlled by the specified expiration period. Command: `aws elb create-lb-cookie-stickiness-policy --load-balancer-name``my-load-balancer`--policy-name`my-duration-cookie-policy`--cookie-expiration-period`60`- 
                    For API details, see [CreateLbCookieStickinessPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-lb-cookie-stickiness-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-load-balancer-listeners`.

- **AWS CLI**
- 
            
                    **To create HTTP listeners for a load balancer**This example creates a listener for your load balancer at port 80 using the HTTP protocol. Command: `aws elb create-load-balancer-listeners --load-balancer-name``my-load-balancer`--listeners`"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"`**To create HTTPS listeners for a load balancer**This example creates a listener for your load balancer at port 443 using the HTTPS protocol. Command: `aws elb create-load-balancer-listeners --load-balancer-name``my-load-balancer`--listeners`"Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80"`- 
                    For API details, see [CreateLoadBalancerListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-listeners.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-load-balancer-policy`.

- **AWS CLI**
- 
            
                    **To create a policy that enables Proxy Protocol on a load balancer**This example creates a policy that enables Proxy Protocol on the specified load balancer. Command: `aws elb create-load-balancer-policy --load-balancer-name``my-load-balancer`--policy-name`my-ProxyProtocol-policy`--policy-type-name`ProxyProtocolPolicyType`--policy-attributes`AttributeName=ProxyProtocol,AttributeValue=true`**To create an SSL negotiation policy using the recommended security policy**This example creates an SSL negotiation policy for the specified HTTPS load balancer using the recommended security policy. Command: `aws elb create-load-balancer-policy --load-balancer-name``my-load-balancer`--policy-name`my-SSLNegotiation-policy`--policy-type-name`SSLNegotiationPolicyType`--policy-attributes`AttributeName=Reference-Security-Policy,AttributeValue=ELBSecurityPolicy-2015-03`**To create an SSL negotiation policy using a custom security policy**This example creates an SSL negotiation policy for your HTTPS load balancer using a custom security policy by enabling the protocols and the ciphers. Command: `aws elb create-load-balancer-policy --load-balancer-name``my-load-balancer`--policy-name`my-SSLNegotiation-policy`--policy-type-name`SSLNegotiationPolicyType`--policy-attributes`AttributeName=Protocol-SSLv3,AttributeValue=true``AttributeName=Protocol-TLSv1.1,AttributeValue=true``AttributeName=DHE-RSA-AES256-SHA256,AttributeValue=true``AttributeName=Server-Defined-Cipher-Order,AttributeValue=true`**To create a public key policy**This example creates a public key policy. Command: `aws elb create-load-balancer-policy --load-balancer-name``my-load-balancer`--policy-name`my-PublicKey-policy`--policy-type-name`PublicKeyPolicyType`--policy-attributes`AttributeName=PublicKey,AttributeValue=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAwAYUjnfyEyXr1pxjhFWBpMlggUcqoi3kl+dS74kj//c6x7ROtusUaeQCTgIUkayttRDWchuqo1pHC1u+n5xxXnBBe2ejbb2WRsKIQ5rXEeixsjFpFsojpSQKkzhVGI6mJVZBJDVKSHmswnwLBdofLhzvllpovBPTHe+o4haAWvDBALJU0pkSI1FecPHcs2hwxf14zHoXy1e2k36A64nXW43wtfx5qcVSIxtCEOjnYRg7RPvybaGfQ+v6Iaxb/+7J5kEvZhTFQId+bSiJImF1FSUT1W1xwzBZPUbcUkkXDj45vC2s3Z8E+Lk7a3uZhvsQHLZnrfuWjBWGWvZ/MhZYgEXAMPLE`**To create a backend server authentication policy**This example creates a backend server authentication policy that enables authentication on your backend instance using a public key policy. Command: `aws elb create-load-balancer-policy --load-balancer-name``my-load-balancer`--policy-name`my-authentication-policy`--policy-type-name`BackendServerAuthenticationPolicyType`--policy-attributes`AttributeName=PublicKeyPolicyName,AttributeValue=my-PublicKey-policy`- 
                    For API details, see [CreateLoadBalancerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-load-balancer`.

- **AWS CLI**
- 
            
                    **To create an HTTP load balancer**This example creates a load balancer with an HTTP listener in a VPC. Command: `aws elb create-load-balancer --load-balancer-name``my-load-balancer`--listeners`"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"`--subnets`subnet-15aaab61`--security-groups`sg-a61988c3`Output: `{ "DNSName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com" }`This example creates a load balancer with an HTTP listener in EC2-Classic. Command: `aws elb create-load-balancer --load-balancer-name``my-load-balancer`--listeners`"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"`--availability-zones`us-west-2a``us-west-2b`Output: `{ "DNSName": "my-load-balancer-123456789.us-west-2.elb.amazonaws.com" }`**To create an HTTPS load balancer**This example creates a load balancer with an HTTPS listener in a VPC. Command: `aws elb create-load-balancer --load-balancer-name``my-load-balancer`--listeners`"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"``"Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80,SSLCertificateId=arn:aws:iam::123456789012:server-certificate/my-server-cert"`--subnets`subnet-15aaab61`--security-groups`sg-a61988c3`Output: `{ "DNSName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com" }`This example creates a load balancer with an HTTPS listener in EC2-Classic. Command: `aws elb create-load-balancer --load-balancer-name``my-load-balancer`--listeners`"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"``"Protocol=HTTPS,LoadBalancerPort=443,InstanceProtocol=HTTP,InstancePort=80,SSLCertificateId=arn:aws:iam::123456789012:server-certificate/my-server-cert"`--availability-zones`us-west-2a``us-west-2b`Output: `{ "DNSName": "my-load-balancer-123456789.us-west-2.elb.amazonaws.com" }`**To create an internal load balancer**This example creates an internal load balancer with an HTTP listener in a VPC. Command: `aws elb create-load-balancer --load-balancer-name``my-load-balancer`--listeners`"Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80"`--scheme`internal`--subnets`subnet-a85db0df`--security-groups`sg-a61988c3`Output: `{ "DNSName": "internal-my-load-balancer-123456789.us-west-2.elb.amazonaws.com" }`- 
                    For API details, see [CreateLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/create-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-load-balancer-listeners`.

- **AWS CLI**
- 
            
                    **To delete a listener from your load balancer**This example deletes the listener for the specified port from the specified load balancer. Command: `aws elb delete-load-balancer-listeners --load-balancer-name``my-load-balancer`--load-balancer-ports`80`- 
                    For API details, see [DeleteLoadBalancerListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-listeners.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-load-balancer-policy`.

- **AWS CLI**
- 
            
                    **To delete a policy from your load balancer**This example deletes the specified policy from the specified load balancer. The policy must not be enabled on any listener. Command: `aws elb delete-load-balancer-policy --load-balancer-name``my-load-balancer`--policy-name`my-duration-cookie-policy`- 
                    For API details, see [DeleteLoadBalancerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-load-balancer`.

- **AWS CLI**
- 
            
                    **To delete a load balancer**This example deletes the specified load balancer. Command: `aws elb delete-load-balancer --load-balancer-name``my-load-balancer`- 
                    For API details, see [DeleteLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/delete-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-instances-from-load-balancer`.

- **AWS CLI**
- 
            
                    **To deregister instances from a load balancer**This example deregisters the specified instance from the specified load balancer. Command: `aws elb deregister-instances-from-load-balancer --load-balancer-name``my-load-balancer`--instances`i-d6f6fae3`Output: `{ "Instances": [ { "InstanceId": "i-207d9717" }, { "InstanceId": "i-afefb49b" } ] }`- 
                    For API details, see [DeregisterInstancesFromLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/deregister-instances-from-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-limits`.

- **AWS CLI**
- 
            
                    **To describe your Classic Load Balancer limits**The following `describe-account-limits`example displays details about the Classic Load Balancer limits for your AWS account.`aws elb describe-account-limits`Output: `{ "Limits": [ { "Name": "classic-load-balancers", "Max": "20" }, { "Name": "classic-listeners", "Max": "100" }, { "Name": "classic-registered-instances", "Max": "1000" } ] }`- 
                    For API details, see [DescribeAccountLimits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-account-limits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-health`.

- **AWS CLI**
- 
            
                    **To describe the health of the instances for a load balancer**This example describes the health of the instances for the specified load balancer. Command: `aws elb describe-instance-health --load-balancer-name``my-load-balancer`Output: `{ "InstanceStates": [ { "InstanceId": "i-207d9717", "ReasonCode": "N/A", "State": "InService", "Description": "N/A" }, { "InstanceId": "i-afefb49b", "ReasonCode": "N/A", "State": "InService", "Description": "N/A" } ] }`**To describe the health of an instance for a load balancer**This example describes the health of the specified instance for the specified load balancer. Command: `aws elb describe-instance-health --load-balancer-name``my-load-balancer`--instances`i-7299c809`The following is an example response for an instance that is registering. Output: `{ "InstanceStates": [ { "InstanceId": "i-7299c809", "ReasonCode": "ELB", "State": "OutOfService", "Description": "Instance registration is still in progress." } ] }`The following is an example response for an unhealthy instance. Output: `{ "InstanceStates": [ { "InstanceId": "i-7299c809", "ReasonCode": "Instance", "State": "OutOfService", "Description": "Instance has failed at least the UnhealthyThreshold number of health checks consecutively." } ] }`- 
                    For API details, see [DescribeInstanceHealth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-instance-health.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancer-attributes`.

- **AWS CLI**
- 
            
                    **To describe the attributes of a load balancer**This example describes the attributes of the specified load balancer. Command: `aws elb describe-load-balancer-attributes --load-balancer-name``my-load-balancer`Output: `{ "LoadBalancerAttributes": { "ConnectionDraining": { "Enabled": false, "Timeout": 300 }, "CrossZoneLoadBalancing": { "Enabled": true }, "ConnectionSettings": { "IdleTimeout": 30 }, "AccessLog": { "Enabled": false } } }`- 
                    For API details, see [DescribeLoadBalancerAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancer-policies`.

- **AWS CLI**
- 
            
                    **To describe all policies associated with a load balancer**This example describes all of the policies associated with the specified load balancer. Command: `aws elb describe-load-balancer-policies --load-balancer-name``my-load-balancer`Output: `{ "PolicyDescriptions": [ { "PolicyAttributeDescriptions": [ { "AttributeName": "ProxyProtocol", "AttributeValue": "true" } ], "PolicyName": "my-ProxyProtocol-policy", "PolicyTypeName": "ProxyProtocolPolicyType" }, { "PolicyAttributeDescriptions": [ { "AttributeName": "CookieName", "AttributeValue": "my-app-cookie" } ], "PolicyName": "my-app-cookie-policy", "PolicyTypeName": "AppCookieStickinessPolicyType" }, { "PolicyAttributeDescriptions": [ { "AttributeName": "CookieExpirationPeriod", "AttributeValue": "60" } ], "PolicyName": "my-duration-cookie-policy", "PolicyTypeName": "LBCookieStickinessPolicyType" }, . . . ] }`**To describe a specific policy associated with a load balancer**This example describes the specified policy associated with the specified load balancer. Command: `aws elb describe-load-balancer-policies --load-balancer-name``my-load-balancer`--policy-name`my-authentication-policy`Output: `{ "PolicyDescriptions": [ { "PolicyAttributeDescriptions": [ { "AttributeName": "PublicKeyPolicyName", "AttributeValue": "my-PublicKey-policy" } ], "PolicyName": "my-authentication-policy", "PolicyTypeName": "BackendServerAuthenticationPolicyType" } ] }`- 
                    For API details, see [DescribeLoadBalancerPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancer-policy-types`.

- **AWS CLI**
- 
            
                    **To describe the load balancer policy types defined by Elastic Load Balancing**This example describes the load balancer policy types that you can use to create policy configurations for your load balancer. Command: `aws elb describe-load-balancer-policy-types`Output: `{ "PolicyTypeDescriptions": [ { "PolicyAttributeTypeDescriptions": [ { "Cardinality": "ONE", "AttributeName": "ProxyProtocol", "AttributeType": "Boolean" } ], "PolicyTypeName": "ProxyProtocolPolicyType", "Description": "Policy that controls whether to include the IP address and port of the originating request for TCP messages. This policy operates on TCP/SSL listeners only" }, { "PolicyAttributeTypeDescriptions": [ { "Cardinality": "ONE", "AttributeName": "PublicKey", "AttributeType": "String" } ], "PolicyTypeName": "PublicKeyPolicyType", "Description": "Policy containing a list of public keys to accept when authenticating the back-end server(s). This policy cannot be applied directly to back-end servers or listeners but must be part of a BackendServerAuthenticationPolicyType." }, { "PolicyAttributeTypeDescriptions": [ { "Cardinality": "ONE", "AttributeName": "CookieName", "AttributeType": "String" } ], "PolicyTypeName": "AppCookieStickinessPolicyType", "Description": "Stickiness policy with session lifetimes controlled by the lifetime of the application-generated cookie. This policy can be associated only with HTTP/HTTPS listeners." }, { "PolicyAttributeTypeDescriptions": [ { "Cardinality": "ZERO_OR_ONE", "AttributeName": "CookieExpirationPeriod", "AttributeType": "Long" } ], "PolicyTypeName": "LBCookieStickinessPolicyType", "Description": "Stickiness policy with session lifetimes controlled by the browser (user-agent) or a specified expiration period. This policy can be associated only with HTTP/HTTPS listeners." }, { "PolicyAttributeTypeDescriptions": [ . . . ], "PolicyTypeName": "SSLNegotiationPolicyType", "Description": "Listener policy that defines the ciphers and protocols that will be accepted by the load balancer. This policy can be associated only with HTTPS/SSL listeners." }, { "PolicyAttributeTypeDescriptions": [ { "Cardinality": "ONE_OR_MORE", "AttributeName": "PublicKeyPolicyName", "AttributeType": "PolicyName" } ], "PolicyTypeName": "BackendServerAuthenticationPolicyType", "Description": "Policy that controls authentication to back-end server(s) and contains one or more policies, such as an instance of a PublicKeyPolicyType. This policy can be associated only with back-end servers that are using HTTPS/SSL." } ] }`- 
                    For API details, see [DescribeLoadBalancerPolicyTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancer-policy-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancers`.

- **AWS CLI**
- 
            
                    **To describe your load balancers**This example describes all of your load balancers. Command: `aws elb describe-load-balancers`**To describe one of your load balancers**This example describes the specified load balancer. Command: `aws elb describe-load-balancers --load-balancer-name``my-load-balancer`The following example response is for an HTTPS load balancer in a VPC. Output: `{ "LoadBalancerDescriptions": [ { "Subnets": [ "subnet-15aaab61" ], "CanonicalHostedZoneNameID": "Z3DZXE0EXAMPLE", "CanonicalHostedZoneName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com", "ListenerDescriptions": [ { "Listener": { "InstancePort": 80, "LoadBalancerPort": 80, "Protocol": "HTTP", "InstanceProtocol": "HTTP" }, "PolicyNames": [] }, { "Listener": { "InstancePort": 443, "SSLCertificateId": "arn:aws:iam::123456789012:server-certificate/my-server-cert", "LoadBalancerPort": 443, "Protocol": "HTTPS", "InstanceProtocol": "HTTPS" }, "PolicyNames": [ "ELBSecurityPolicy-2015-03" ] } ], "HealthCheck": { "HealthyThreshold": 2, "Interval": 30, "Target": "HTTP:80/png", "Timeout": 3, "UnhealthyThreshold": 2 }, "VPCId": "vpc-a01106c2", "BackendServerDescriptions": [ { "InstancePort": 80, "PolicyNames": [ "my-ProxyProtocol-policy" ] } ], "Instances": [ { "InstanceId": "i-207d9717" }, { "InstanceId": "i-afefb49b" } ], "DNSName": "my-load-balancer-1234567890.us-west-2.elb.amazonaws.com", "SecurityGroups": [ "sg-a61988c3" ], "Policies": { "LBCookieStickinessPolicies": [ { "PolicyName": "my-duration-cookie-policy", "CookieExpirationPeriod": 60 } ], "AppCookieStickinessPolicies": [], "OtherPolicies": [ "my-PublicKey-policy", "my-authentication-policy", "my-SSLNegotiation-policy", "my-ProxyProtocol-policy", "ELBSecurityPolicy-2015-03" ] }, "LoadBalancerName": "my-load-balancer", "CreatedTime": "2015-03-19T03:24:02.650Z", "AvailabilityZones": [ "us-west-2a" ], "Scheme": "internet-facing", "SourceSecurityGroup": { "OwnerAlias": "123456789012", "GroupName": "my-elb-sg" } } ] }`- 
                    For API details, see [DescribeLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-load-balancers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **To describe the tags assigned to a load balancer**This example describes the tags assigned to the specified load balancer. Command: `aws elb describe-tags --load-balancer-name``my-load-balancer`Output: `{ "TagDescriptions": [ { "Tags": [ { "Value": "lima", "Key": "project" }, { "Value": "digital-media", "Key": "department" } ], "LoadBalancerName": "my-load-balancer" } ] }`- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-load-balancer-from-subnets`.

- **AWS CLI**
- 
            
                    **To detach load balancers from subnets**This example detaches the specified load balancer from the specified subnet. Command: `aws elb detach-load-balancer-from-subnets --load-balancer-name``my-load-balancer`--subnets`subnet-0ecac448`Output: `{ "Subnets": [ "subnet-15aaab61" ] }`- 
                    For API details, see [DetachLoadBalancerFromSubnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/detach-load-balancer-from-subnets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-availability-zones-for-load-balancer`.

- **AWS CLI**
- 
            
                    **To disable Availability Zones for a load balancer**This example removes the specified Availability Zone from the set of Availability Zones for the specified load balancer. Command: `aws elb disable-availability-zones-for-load-balancer --load-balancer-name``my-load-balancer`--availability-zones`us-west-2a`Output: `{ "AvailabilityZones": [ "us-west-2b" ] }`- 
                    For API details, see [DisableAvailabilityZonesForLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/disable-availability-zones-for-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-availability-zones-for-load-balancer`.

- **AWS CLI**
- 
            
                    **To enable Availability Zones for a load balancer**This example adds the specified Availability Zone to the specified load balancer. Command: `aws elb enable-availability-zones-for-load-balancer --load-balancer-name``my-load-balancer`--availability-zones`us-west-2b`Output: `{ "AvailabilityZones": [ "us-west-2a", "us-west-2b" ] }`- 
                    For API details, see [EnableAvailabilityZonesForLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/enable-availability-zones-for-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-load-balancer-attributes`.

- **AWS CLI**
- 
            
                    **To modify the attributes of a load balancer**This example modifies the `CrossZoneLoadBalancing`attribute of the specified load balancer.Command: `aws elb modify-load-balancer-attributes --load-balancer-name``my-load-balancer`--load-balancer-attributes "{\"CrossZoneLoadBalancing\":{\"Enabled\":true}}"Output: `{ "LoadBalancerAttributes": { "CrossZoneLoadBalancing": { "Enabled": true } }, "LoadBalancerName": "my-load-balancer" }`This example modifies the `ConnectionDraining`attribute of the specified load balancer.Command: `aws elb modify-load-balancer-attributes --load-balancer-name``my-load-balancer`--load-balancer-attributes "{\"ConnectionDraining\":{\"Enabled\":true,\"Timeout\":300}}"Output: `{ "LoadBalancerAttributes": { "ConnectionDraining": { "Enabled": true, "Timeout": 300 } }, "LoadBalancerName": "my-load-balancer" }`- 
                    For API details, see [ModifyLoadBalancerAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/modify-load-balancer-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-instances-with-load-balancer`.

- **AWS CLI**
- 
            
                    **To register instances with a load balancer**This example registers the specified instance with the specified load balancer. Command: `aws elb register-instances-with-load-balancer --load-balancer-name``my-load-balancer`--instances`i-d6f6fae3`Output: `{ "Instances": [ { "InstanceId": "i-d6f6fae3" }, { "InstanceId": "i-207d9717" }, { "InstanceId": "i-afefb49b" } ] }`- 
                    For API details, see [RegisterInstancesWithLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/register-instances-with-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags`.

- **AWS CLI**
- 
            
                    **To remove tags from a load balancer**This example removes a tag from the specified load balancer. Command: `aws elb remove-tags --load-balancer-name``my-load-balancer`--tags`project`- 
                    For API details, see [RemoveTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/remove-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-load-balancer-listener-ssl-certificate`.

- **AWS CLI**
- 
            
                    **To update the SSL certificate for an HTTPS load balancer**This example replaces the existing SSL certificate for the specified HTTPS load balancer. Command: `aws elb set-load-balancer-listener-ssl-certificate --load-balancer-name``my-load-balancer`--load-balancer-port`443`--ssl-certificate-id`arn:aws:iam::123456789012:server-certificate/new-server-cert`- 
                    For API details, see [SetLoadBalancerListenerSslCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-listener-ssl-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-load-balancer-policies-for-backend-server`.

- **AWS CLI**
- 
            
                    **To replace the policies associated with a port for a backend instance**This example replaces the policies that are currently associated with the specified port. Command: `aws elb set-load-balancer-policies-for-backend-server --load-balancer-name``my-load-balancer`--instance-port`80`--policy-names`my-ProxyProtocol-policy`**To remove all policies that are currently associated with a port on your backend instance**This example removes all policies associated with the specified port. Command: `aws elb set-load-balancer-policies-for-backend-server --load-balancer-name``my-load-balancer`--instance-port`80`--policy-names`[]`To confirm that the policies are removed, use the `describe-load-balancer-policies`command.- 
                    For API details, see [SetLoadBalancerPoliciesForBackendServer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-for-backend-server.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-load-balancer-policies-of-listener`.

- **AWS CLI**
- 
            
                    **To replace the policies associated with a listener**This example replaces the policies that are currently associated with the specified listener. Command: `aws elb set-load-balancer-policies-of-listener --load-balancer-name``my-load-balancer`--load-balancer-port`443`--policy-names`my-SSLNegotiation-policy`**To remove all policies associated with your listener**This example removes all policies that are currently associated with the specified listener. Command: `aws elb set-load-balancer-policies-of-listener --load-balancer-name``my-load-balancer`--load-balancer-port`443`--policy-names`[]`To confirm that the policies are removed from the load balancer, use the `describe-load-balancer-policies`command.- 
                    For API details, see [SetLoadBalancerPoliciesOfListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elb/set-load-balancer-policies-of-listener.html)in*AWS CLI Command Reference*.
 
-