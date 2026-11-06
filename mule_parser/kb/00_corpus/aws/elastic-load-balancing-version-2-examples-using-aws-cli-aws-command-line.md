# Elastic Load Balancing - Version 2 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-load-balancing-v2_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_elastic-load-balancing-v2_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Elastic Load Balancing - Version 2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-listener-certificates`.

- **AWS CLI**
- 
            
                    **To add a certificate to a secure listener**This example adds the specified certificate to the specified secure listener. Command: `aws elbv2 add-listener-certificates --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`--certificates`CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/5cc54884-f4a3-4072-80be-05b9ba72f705`Output: `{ "Certificates": [ { "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/5cc54884-f4a3-4072-80be-05b9ba72f705", "IsDefault": false } ] }`- 
                    For API details, see [AddListenerCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-listener-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `add-tags`.

- **AWS CLI**
- 
            
                    **To add tags to a load balancer**The following `add-tags`example adds the`project`and`department`tags to the specified load balancer.`aws elbv2 add-tags \ --resource-arns``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`\ --tags`"Key=project,Value=lima"``"Key=department,Value=digital-media"`- 
                    For API details, see [AddTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/add-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-listener`.

- **AWS CLI**
- 
            
                    **Example 1: To create an HTTP listener**The following `create-listener`example creates an HTTP listener for the specified Application Load Balancer that forwards requests to the specified target group.`aws elbv2 create-listener \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`\ --protocol`HTTP`\ --port`80`\ --default-actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`For more information, see [Tutorial: Create an Application Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html#create-load-balancer-aws-cli)in the*User Guide for Application Load Balancers*.**Example 2: To create an HTTPS listener**The following `create-listener`example creates an HTTPS listener for the specified Application Load Balancer that forwards requests to the specified target group. You must specify an SSL certificate for an HTTPS listener. You can create and manage certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).`aws elbv2 create-listener \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`\ --protocol`HTTPS`\ --port`443`\ --certificates`CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/3dcb0a41-bd72-4774-9ad9-756919c40557`\ --ssl-policy`ELBSecurityPolicy-2016-08`\ --default-actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`For more information, see [Add an HTTPS listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html#https-listener-aws-cli)in the*User Guide for Application Load Balancers*.**Example 3: To create a TCP listener**The following `create-listener`example creates a TCP listener for the specified Network Load Balancer that forwards requests to the specified target group.`aws elbv2 create-listener \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/5d1b75f4f1cee11e`\ --protocol`TCP`\ --port`80`\ --default-actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-targets/b6bba954d1361c78`For more information, see [Tutorial: Create a Network Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-cli.html#create-load-balancer-aws-cli)in the*User Guide for Network Load Balancers*.**Example 4: To create a TLS listener**The following `create-listener`example creates a TLS listener for the specified Network Load Balancer that forwards requests to the specified target group. You must specify an SSL certificate for a TLS listener.`aws elbv2 create-listener \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`\ --protocol`TLS`\ --port`443`\ --certificates`CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/3dcb0a41-bd72-4774-9ad9-756919c40557`\ --ssl-policy`ELBSecurityPolicy-2016-08`\ --default-actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`For more information, see [TLS listeners for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html)in the*User Guide for Network Load Balancers*.**Example 5: To create a UDP listener**The following `create-listener`example creates a UDP listener for the specified Network Load Balancer that forwards requests to the specified target group.`aws elbv2 create-listener \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/5d1b75f4f1cee11e`\ --protocol`UDP`\ --port`53`\ --default-actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-targets/b6bba954d1361c78`For more information, see [Tutorial: Create a Network Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-cli.html#create-load-balancer-aws-cli)in the*User Guide for Network Load Balancers*.**Example 6: To create a listener for the specified gateway and forwarding**The following `create-listener`example creates a listener for the specified Gateway Load Balancer that forwards requests to the specified target group.`aws elbv2 create-listener \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-east-1:850631746142:loadbalancer/gwy/my-gateway-load-balancer/e0f9b3d5c7f7d3d6`\ --default-actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:850631746142:targetgroup/my-glb-targets/007ca469fae3bb1615`Output: `{ "Listeners": [ { "ListenerArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:listener/gwy/my-agw-lb-example2/e0f9b3d5c7f7d3d6/afc127db15f925de", "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:loadbalancer/gwy/my-agw-lb-example2/e0f9b3d5c7f7d3d6", "DefaultActions": [ { "Type": "forward", "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:targetgroup/test-tg-agw-2/007ca469fae3bb1615", "ForwardConfig": { "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:targetgroup/test-tg-agw-2/007ca469fae3bb1615" } ] } } ] } ] }`For more information, see [Getting started with Gateway Load Balancers using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started-cli.html)in the*User Guide for Gateway Load Balancers*.- 
                    For API details, see [CreateListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-load-balancer`.

- **AWS CLI**
- 
            
                    **Example 1: To create an Internet-facing load balancer**The following `create-load-balancer`example creates an Internet-facing Application Load Balancer and enables the Availability Zones for the specified subnets.`aws elbv2 create-load-balancer \ --name``my-load-balancer`\ --subnets`subnet-b7d581c0``subnet-8360a9e7`Output: `{ "LoadBalancers": [ { "Type": "application", "Scheme": "internet-facing", "IpAddressType": "ipv4", "VpcId": "vpc-3ac0fb5f", "AvailabilityZones": [ { "ZoneName": "us-west-2a", "SubnetId": "subnet-8360a9e7" }, { "ZoneName": "us-west-2b", "SubnetId": "subnet-b7d581c0" } ], "CreatedTime": "2017-08-25T21:26:12.920Z", "CanonicalHostedZoneId": "Z2P70J7EXAMPLE", "DNSName": "my-load-balancer-424835706.us-west-2.elb.amazonaws.com", "SecurityGroups": [ "sg-5943793c" ], "LoadBalancerName": "my-load-balancer", "State": { "Code": "provisioning" }, "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188" } ] }`For more information, see [Tutorial: Create an Application Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html)in the*User Guide for Application Load Balancers*.**Example 2: To create an internal load balancer**The following `create-load-balancer`example creates an internal Application Load Balancer and enables the Availability Zones for the specified subnets.`aws elbv2 create-load-balancer \ --name``my-internal-load-balancer`\ --scheme`internal`\ --subnets`subnet-b7d581c0``subnet-8360a9e7`Output: `{ "LoadBalancers": [ { "Type": "application", "Scheme": "internal", "IpAddressType": "ipv4", "VpcId": "vpc-3ac0fb5f", "AvailabilityZones": [ { "ZoneName": "us-west-2a", "SubnetId": "subnet-8360a9e7" }, { "ZoneName": "us-west-2b", "SubnetId": "subnet-b7d581c0" } ], "CreatedTime": "2016-03-25T21:29:48.850Z", "CanonicalHostedZoneId": "Z2P70J7EXAMPLE", "DNSName": "internal-my-internal-load-balancer-1529930873.us-west-2.elb.amazonaws.com", "SecurityGroups": [ "sg-5943793c" ], "LoadBalancerName": "my-internal-load-balancer", "State": { "Code": "provisioning" }, "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-internal-load-balancer/5b49b8d4303115c2" } ] }`For more information, see [Tutorial: Create an Application Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html)in the*User Guide for Application Load Balancers*.**Example 3: To create a Network Load Balancer**The following `create-load-balancer`example creates an Internet-facing Network Load Balancer and enables the Availability Zone for the specified subnet. It uses a subnet mapping to associate the specified Elastic IP address with the network interface used by the load balancer nodes for the Availability Zone.`aws elbv2 create-load-balancer \ --name``my-network-load-balancer`\ --type`network`\ --subnet-mappings`SubnetId=subnet-b7d581c0,AllocationId=eipalloc-64d5890a`Output: `{ "LoadBalancers": [ { "Type": "network", "Scheme": "internet-facing", "IpAddressType": "ipv4", "VpcId": "vpc-3ac0fb5f", "AvailabilityZones": [ { "LoadBalancerAddresses": [ { "IpAddress": "35.161.207.171", "AllocationId": "eipalloc-64d5890a" } ], "ZoneName": "us-west-2b", "SubnetId": "subnet-5264e837" } ], "CreatedTime": "2017-10-15T22:41:25.657Z", "CanonicalHostedZoneId": "Z2P70J7EXAMPLE", "DNSName": "my-network-load-balancer-5d1b75f4f1cee11e.elb.us-west-2.amazonaws.com", "LoadBalancerName": "my-network-load-balancer", "State": { "Code": "provisioning" }, "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/5d1b75f4f1cee11e" } ] }`For more information, see [Tutorial: Create a Network Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-cli.html)in the*User Guide for Network Load Balancers*.**Example 4: To create a Gateway Load Balancer**The following `create-load-balancer`example creates a Gateway Load Balancer and enables the Availability Zones for the specified subnets.`aws elbv2 create-load-balancer \ --name``my-gateway-load-balancer`\ --type`gateway`\ --subnets`subnet-dc83f691``subnet-a62583f9`Output: `{ "LoadBalancers": [ { "Type": "gateway", "VpcId": "vpc-838475fe", "AvailabilityZones": [ { "ZoneName": "us-east-1b", "SubnetId": "subnet-a62583f9" }, { "ZoneName": "us-east-1a", "SubnetId": "subnet-dc83f691" } ], "CreatedTime": "2021-07-14T19:33:43.324000+00:00", "LoadBalancerName": "my-gateway-load-balancer", "State": { "Code": "provisioning" }, "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:loadbalancer/gwy/my-gateway-load-balancer/dfbb5a7d32cdee79" } ] }`For more information, see [Getting started with Gateway Load Balancers using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started-cli.html)in the*User Guide for Gateway Load Balancers*.- 
                    For API details, see [CreateLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-rule`.

- **AWS CLI**
- 
            
                    **Example 1: To create a rule using a path condition and a forward action**The following `create-rule`example creates a rule that forwards requests to the specified target group if the URL contains the specified pattern.`aws elbv2 create-rule \ --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`\ --priority`5`\ --conditions`file://conditions-pattern.json`--actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`Contents of `conditions-pattern.json`:`[ { "Field": "path-pattern", "PathPatternConfig": { "Values": ["/images/*"] } } ]`**Example 2: To create a rule using a host condition and a fixed response**The following `create-rule`example creates a rule that provides a fixed response if the hostname in the host header matches the specified hostname.`aws elbv2 create-rule \ --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`\ --priority`10`\ --conditions`file://conditions-host.json`\ --actions`file://actions-fixed-response.json`Contents of `conditions-host.json``[ { "Field": "host-header", "HostHeaderConfig": { "Values": ["*.example.com"] } } ]`Contents of `actions-fixed-response.json``[ { "Type": "fixed-response", "FixedResponseConfig": { "MessageBody": "Hello world", "StatusCode": "200", "ContentType": "text/plain" } } ]`**Example 3: To create a rule using a source IP address condition, an authenticate action, and a forward action**The following `create-rule`example creates a rule that authenticates the user if the source IP address matches the specified IP address, and forwards the request to the specified target group if authentication is successful.`aws elbv2 create-rule \ --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`\ --priority`20`\ --conditions`file://conditions-source-ip.json`\ --actions`file://actions-authenticate.json`Contents of `conditions-source-ip.json``[ { "Field": "source-ip", "SourceIpConfig": { "Values": ["192.0.2.0/24", "198.51.100.10/32"] } } ]`Contents of `actions-authenticate.json``[ { "Type": "authenticate-oidc", "AuthenticateOidcConfig": { "Issuer": "https://idp-issuer.com", "AuthorizationEndpoint": "https://authorization-endpoint.com", "TokenEndpoint": "https://token-endpoint.com", "UserInfoEndpoint": "https://user-info-endpoint.com", "ClientId": "abcdefghijklmnopqrstuvwxyz123456789", "ClientSecret": "123456789012345678901234567890", "SessionCookieName": "my-cookie", "SessionTimeout": 3600, "Scope": "email", "AuthenticationRequestExtraParams": { "display": "page", "prompt": "login" }, "OnUnauthenticatedRequest": "deny" }, "Order": 1 }, { "Type": "forward", "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:880185128111:targetgroup/cli-test/642a97ecb0e0f26b", "Order": 2 } ]`- 
                    For API details, see [CreateRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-target-group`.

- **AWS CLI**
- 
            
                    **Example 1: To create a target group for an Application Load Balancer**The following `create-target-group`example creates a target group for an Application Load Balancer where you register targets by instance ID (the target type is`instance`). This target group uses the HTTP protocol, port 80, and the default health check settings for an HTTP target group.`aws elbv2 create-target-group \ --name``my-targets`\ --protocol`HTTP`\ --port`80`\ --target-type`instance`\ --vpc-id`vpc-3ac0fb5f`Output: `{ "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "TargetGroupName": "my-targets", "Protocol": "HTTP", "Port": 80, "VpcId": "vpc-3ac0fb5f", "HealthCheckProtocol": "HTTP", "HealthCheckPort": "traffic-port", "HealthCheckEnabled": true, "HealthCheckIntervalSeconds": 30, "HealthCheckTimeoutSeconds": 5, "HealthyThresholdCount": 5, "UnhealthyThresholdCount": 2, "HealthCheckPath": "/", "Matcher": { "HttpCode": "200" }, "TargetType": "instance", "ProtocolVersion": "HTTP1", "IpAddressType": "ipv4" } ] }`For more information, see [Create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-target-group.html)in the*User Guide for Application Load Balancers*.**Example 2: To create a target group to route traffic from an Application Load Balancer to a Lambda function**The following `create-target-group`example creates a target group for an Application Load Balancer where the target is a Lambda function (the target type is`lambda`). Health checks are disabled for this target group by default.`aws elbv2 create-target-group \ --name``my-lambda-target`\ --target-type`lambda`Output: `{ "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-lambda-target/a3003e085dbb8ddc", "TargetGroupName": "my-lambda-target", "HealthCheckEnabled": false, "HealthCheckIntervalSeconds": 35, "HealthCheckTimeoutSeconds": 30, "HealthyThresholdCount": 5, "UnhealthyThresholdCount": 2, "HealthCheckPath": "/", "Matcher": { "HttpCode": "200" }, "TargetType": "lambda", "IpAddressType": "ipv4" } ] }`For more information, see [Lambda functions as targets](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/lambda-functions.html)in the*User Guide for Application Load Balancers*.**Example 3: To create a target group for a Network Load Balancer**The following `create-target-group`example creates a target group for a Network Load Balancer where you register targets by IP address (the target type is`ip`). This target group uses the TCP protocol, port 80, and the default health check settings for a TCP target group.`aws elbv2 create-target-group \ --name``my-ip-targets`\ --protocol`TCP`\ --port`80`\ --target-type`ip`\ --vpc-id`vpc-3ac0fb5f`Output: `{ "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-ip-targets/b6bba954d1361c78", "TargetGroupName": "my-ip-targets", "Protocol": "TCP", "Port": 80, "VpcId": "vpc-3ac0fb5f", "HealthCheckEnabled": true, "HealthCheckProtocol": "TCP", "HealthCheckPort": "traffic-port", "HealthCheckIntervalSeconds": 30, "HealthCheckTimeoutSeconds": 10, "HealthyThresholdCount": 5, "UnhealthyThresholdCount": 2, "TargetType": "ip", "IpAddressType": "ipv4" } ] }`For more information, see [Create a target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-target-group.html)in the*User Guide for Network Load Balancers*.**Example 4: To create a target group to route traffic from a Network Load Balancer to an Application Load Balancer**The following `create-target-group`example creates a target group for a Network Load Balancer where you register an Application Load Balancer as a target (the target type is`alb`).aws elbv2 create-target-group --name my-alb-target --protocol TCP --port 80 --target-type alb --vpc-id vpc-3ac0fb5f Output: `{ "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-alb-target/a3003e085dbb8ddc", "TargetGroupName": "my-alb-target", "Protocol": "TCP", "Port": 80, "VpcId": "vpc-838475fe", "HealthCheckProtocol": "HTTP", "HealthCheckPort": "traffic-port", "HealthCheckEnabled": true, "HealthCheckIntervalSeconds": 30, "HealthCheckTimeoutSeconds": 6, "HealthyThresholdCount": 5, "UnhealthyThresholdCount": 2, "HealthCheckPath": "/", "Matcher": { "HttpCode": "200-399" }, "TargetType": "alb", "IpAddressType": "ipv4" } ] }`For more information, see [Create a target group with an Application Load Balancer as the target](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/application-load-balancer-target.html)in the*User Guide for Network Load Balancers*.**Example 5: To create a target group for a Gateway Load Balancer**The following `create-target-group`example creates a target group for a Gateway Load Balancer where the target is an instance, and the target group protocol is`GENEVE`.`aws elbv2 create-target-group \ --name``my-glb-targetgroup`\ --protocol`GENEVE`\ --port`6081`\ --target-type`instance`\ --vpc-id`vpc-838475fe`Output: `{ "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-glb-targetgroup/00c3d57eacd6f40b6f", "TargetGroupName": "my-glb-targetgroup", "Protocol": "GENEVE", "Port": 6081, "VpcId": "vpc-838475fe", "HealthCheckProtocol": "TCP", "HealthCheckPort": "80", "HealthCheckEnabled": true, "HealthCheckIntervalSeconds": 10, "HealthCheckTimeoutSeconds": 5, "HealthyThresholdCount": 5, "UnhealthyThresholdCount": 2, "TargetType": "instance" } ] }`For more information, see Create a target group <https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/create-target-group.html>`__ in the *Gateway Load Balancer User Guide*.- 
                    For API details, see [CreateTargetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-target-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-listener`.

- **AWS CLI**
- 
            
                    **To delete a listener**The following `delete-listener`example deletes the specified listener.`aws elbv2 delete-listener \ --listener-arn``arn:aws:elasticloadbalancing:ua-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`- 
                    For API details, see [DeleteListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-load-balancer`.

- **AWS CLI**
- 
            
                    **To delete a load balancer**The following `delete-load-balancer`example deletes the specified load balancer.`aws elbv2 delete-load-balancer \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`- 
                    For API details, see [DeleteLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-rule`.

- **AWS CLI**
- 
            
                    **To delete a rule**The following `delete-rule`example deletes the specified rule.`aws elbv2 delete-rule \ --rule-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3`- 
                    For API details, see [DeleteRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-target-group`.

- **AWS CLI**
- 
            
                    **To delete a target group**The following `delete-target-group`example deletes the specified target group.`aws elbv2 delete-target-group \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`This command produces no output. For more information, see [Delete a load balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-delete.html)in the*Application Load Balancer Guide*.- 
                    For API details, see [DeleteTargetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/delete-target-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-targets`.

- **AWS CLI**
- 
            
                    **Example 1: To deregister a target from a target group**The following `deregister-targets`example removes the specified instance from the specified target group.`aws elbv2 deregister-targets \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`\ --targets`Id=i-1234567890abcdef0`**Example 2: To deregister a target registered using port overrides**The following `deregister-targets`example removes an instance from a target group that was registered using port overrides.`aws elbv2 deregister-targets \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-internal-targets/3bb63f11dfb0faf9`\ --targets`Id=i-1234567890abcdef0,Port=80``Id=i-1234567890abcdef0,Port=766`- 
                    For API details, see [DeregisterTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/deregister-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-limits`.

- **AWS CLI**
- 
            
                    **To describe your Elastic Load Balancing limits**The following `describe-account-limits`example displays the Elastic Load Balancing limits for your AWS account in the current Region.`aws elbv2 describe-account-limits`Output: `{ "Limits": [ { "Name": "target-groups", "Max": "3000" }, { "Name": "targets-per-application-load-balancer", "Max": "1000" }, { "Name": "listeners-per-application-load-balancer", "Max": "50" }, { "Name": "rules-per-application-load-balancer", "Max": "100" }, { "Name": "network-load-balancers", "Max": "50" }, { "Name": "targets-per-network-load-balancer", "Max": "3000" }, { "Name": "targets-per-availability-zone-per-network-load-balancer", "Max": "500" }, { "Name": "listeners-per-network-load-balancer", "Max": "50" }, { "Name": "condition-values-per-alb-rule", "Max": "5" }, { "Name": "condition-wildcards-per-alb-rule", "Max": "5" }, { "Name": "target-groups-per-application-load-balancer", "Max": "100" }, { "Name": "target-groups-per-action-on-application-load-balancer", "Max": "5" }, { "Name": "target-groups-per-action-on-network-load-balancer", "Max": "1" }, { "Name": "certificates-per-application-load-balancer", "Max": "25" }, { "Name": "certificates-per-network-load-balancer", "Max": "25" }, { "Name": "targets-per-target-group", "Max": "1000" }, { "Name": "target-id-registrations-per-application-load-balancer", "Max": "1000" }, { "Name": "network-load-balancer-enis-per-vpc", "Max": "1200" }, { "Name": "application-load-balancers", "Max": "50" }, { "Name": "gateway-load-balancers", "Max": "100" }, { "Name": "gateway-load-balancers-per-vpc", "Max": "100" }, { "Name": "geneve-target-groups", "Max": "100" }, { "Name": "targets-per-availability-zone-per-gateway-load-balancer", "Max": "300" } ] }`For more information, see [Quotas](https://docs.aws.amazon.com/general/latest/gr/elb.html#limits_elastic_load_balancer)in the*AWS General Reference*.- 
                    For API details, see [DescribeAccountLimits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-account-limits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-listener-certificates`.

- **AWS CLI**
- 
            
                    **To describe the certificates for a secure listener**This example describes the certificates for the specified secure listener. Command: `aws elbv2 describe-listener-certificates --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`Output: `{ "Certificates": [ { "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/5cc54884-f4a3-4072-80be-05b9ba72f705", "IsDefault": false }, { "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/3dcb0a41-bd72-4774-9ad9-756919c40557", "IsDefault": false }, { "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/fe59da96-6f58-4a22-8eed-6d0d50477e1d", "IsDefault": true } ] }`- 
                    For API details, see [DescribeListenerCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listener-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-listeners`.

- **AWS CLI**
- 
            
                    **To describe a listener**This example describes the specified listener. Command: `aws elbv2 describe-listeners --listener-arns``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`Output: `{ "Listeners": [ { "Port": 80, "Protocol": "HTTP", "DefaultActions": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "Type": "forward" } ], "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188", "ListenerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2" } ] }`**To describe the listeners for a load balancer**This example describe the listeners for the specified load balancer. Command: `aws elbv2 describe-listeners --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`Output: `{ "Listeners": [ { "Port": 443, "Protocol": "HTTPS", "DefaultActions": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "Type": "forward" } ], "SslPolicy": "ELBSecurityPolicy-2015-05", "Certificates": [ { "CertificateArn": "arn:aws:iam::123456789012:server-certificate/my-server-cert" } ], "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188", "ListenerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65" }, { "Port": 80, "Protocol": "HTTP", "DefaultActions": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "Type": "forward" } ], "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188", "ListenerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2" } ] }`- 
                    For API details, see [DescribeListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-listeners.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancer-attributes`.

- **AWS CLI**
- 
            
                    **To describe load balancer attributes**The following `describe-load-balancer-attributes`example displays the attributes of the specified load balancer.`aws elbv2 describe-load-balancer-attributes \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`The following example output show the attributes for an Application Load Balancer. `{ "Attributes": [ { "Value": "false", "Key": "access_logs.s3.enabled" }, { "Value": "", "Key": "access_logs.s3.bucket" }, { "Value": "", "Key": "access_logs.s3.prefix" }, { "Value": "60", "Key": "idle_timeout.timeout_seconds" }, { "Value": "false", "Key": "deletion_protection.enabled" }, { "Value": "true", "Key": "routing.http2.enabled" } ] }`The following example output includes the attributes for a Network Load Balancer. `{ "Attributes": [ { "Value": "false", "Key": "access_logs.s3.enabled" }, { "Value": "", "Key": "access_logs.s3.bucket" }, { "Value": "", "Key": "access_logs.s3.prefix" }, { "Value": "false", "Key": "deletion_protection.enabled" }, { "Value": "false", "Key": "load_balancing.cross_zone.enabled" } ] }`- 
                    For API details, see [DescribeLoadBalancerAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-load-balancer-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-load-balancers`.

- **AWS CLI**
- 
            
                    **To describe a load balancer**This example describes the specified load balancer. Command: `aws elbv2 describe-load-balancers --load-balancer-arns``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`Output: `{ "LoadBalancers": [ { "Type": "application", "Scheme": "internet-facing", "IpAddressType": "ipv4", "VpcId": "vpc-3ac0fb5f", "AvailabilityZones": [ { "ZoneName": "us-west-2a", "SubnetId": "subnet-8360a9e7" }, { "ZoneName": "us-west-2b", "SubnetId": "subnet-b7d581c0" } ], "CreatedTime": "2016-03-25T21:26:12.920Z", "CanonicalHostedZoneId": "Z2P70J7EXAMPLE", "DNSName": "my-load-balancer-424835706.us-west-2.elb.amazonaws.com", "SecurityGroups": [ "sg-5943793c" ], "LoadBalancerName": "my-load-balancer", "State": { "Code": "active" }, "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188" } ] }`**To describe all load balancers**This example describes all of your load balancers. Command: `aws elbv2 describe-load-balancers`- 
                    For API details, see [DescribeLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-load-balancers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-rules`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a rule**The following `describe-rules`example displays details for the specified rule.`aws elbv2 describe-rules \ --rule-arns``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee`**Example 2: To describe the rules for a listener**The following `describe-rules`example displays details for the rules for the specified listener. The output includes the default rule and any other rules that you've added.`aws elbv2 describe-rules \ --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`- 
                    For API details, see [DescribeRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ssl-policies`.

- **AWS CLI**
- 
            
                    **Example 1: To list the policies used for SSL negotiation by load balancer type**The following `describe-ssl-policies`example displays the names of the polices that you can use for SSL negotiation with an Application Load Balancer. The example uses the`--query`parameter to display only the names of the policies.`aws elbv2 describe-ssl-policies \ --load-balancer-type``application`\ --query`SslPolicies[*].Name`Output: `[ "ELBSecurityPolicy-2016-08", "ELBSecurityPolicy-TLS13-1-2-2021-06", "ELBSecurityPolicy-TLS13-1-2-Res-2021-06", "ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06", "ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06", "ELBSecurityPolicy-TLS13-1-1-2021-06", "ELBSecurityPolicy-TLS13-1-0-2021-06", "ELBSecurityPolicy-TLS13-1-3-2021-06", "ELBSecurityPolicy-TLS-1-2-2017-01", "ELBSecurityPolicy-TLS-1-1-2017-01", "ELBSecurityPolicy-TLS-1-2-Ext-2018-06", "ELBSecurityPolicy-FS-2018-06", "ELBSecurityPolicy-2015-05", "ELBSecurityPolicy-TLS-1-0-2015-04", "ELBSecurityPolicy-FS-1-2-Res-2019-08", "ELBSecurityPolicy-FS-1-1-2019-08", "ELBSecurityPolicy-FS-1-2-2019-08", "ELBSecurityPolicy-FS-1-2-Res-2020-10" ]`**Example 2: To list the policies that support a specific protocol**The following `describe-ssl-policies`example displays the names of the polices that support the TLS 1.3 protocol. The example uses the`--query`parameter to display only the names of the policies.`aws elbv2 describe-ssl-policies \ --load-balancer-type``application`\ --query SslPolicies[?contains(SslProtocols,'TLSv1.3')].NameOutput: `[ "ELBSecurityPolicy-TLS13-1-2-2021-06", "ELBSecurityPolicy-TLS13-1-2-Res-2021-06", "ELBSecurityPolicy-TLS13-1-2-Ext1-2021-06", "ELBSecurityPolicy-TLS13-1-2-Ext2-2021-06", "ELBSecurityPolicy-TLS13-1-1-2021-06", "ELBSecurityPolicy-TLS13-1-0-2021-06", "ELBSecurityPolicy-TLS13-1-3-2021-06" ]`**Example 3: To display the ciphers for a policy**The following `describe-ssl-policies`example displays the names of the ciphers for the specified policy. The example uses the`--query`parameter to display only the cipher names. The first cipher in the list has priority 1, and the remaining ciphers are in priority order.`aws elbv2 describe-ssl-policies \ --names``ELBSecurityPolicy-TLS13-1-2-2021-06`\ --query`SslPolicies[*].Ciphers[*].Name`Output: `[ "TLS_AES_128_GCM_SHA256", "TLS_AES_256_GCM_SHA384", "TLS_CHACHA20_POLY1305_SHA256", "ECDHE-ECDSA-AES128-GCM-SHA256", "ECDHE-RSA-AES128-GCM-SHA256", "ECDHE-ECDSA-AES128-SHA256", "ECDHE-RSA-AES128-SHA256", "ECDHE-ECDSA-AES256-GCM-SHA384", "ECDHE-RSA-AES256-GCM-SHA384", "ECDHE-ECDSA-AES256-SHA384", "ECDHE-RSA-AES256-SHA384" ]`For more information, see [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies)in the*User Guide for Application Load Balancers*.- 
                    For API details, see [DescribeSslPolicies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-ssl-policies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **To describe the tags assigned to a load balancer**This example describes the tags assigned to the specified load balancer. Command: `aws elbv2 describe-tags --resource-arns``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`Output: `{ "TagDescriptions": [ { "ResourceArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188", "Tags": [ { "Value": "lima", "Key": "project" }, { "Value": "digital-media", "Key": "department" } ] } ] }`- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-target-group-attributes`.

- **AWS CLI**
- 
            
                    **To describe target group attributes**The following `describe-target-group-attributes`example displays the attributes of the specified target group.`aws elbv2 describe-target-group-attributes \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`The output includes the attributes if the protocol is HTTP or HTTPS and the target type is `instance`or`ip`.`{ "Attributes": [ { "Value": "false", "Key": "stickiness.enabled" }, { "Value": "300", "Key": "deregistration_delay.timeout_seconds" }, { "Value": "lb_cookie", "Key": "stickiness.type" }, { "Value": "86400", "Key": "stickiness.lb_cookie.duration_seconds" }, { "Value": "0", "Key": "slow_start.duration_seconds" } ] }`The following output includes the attributes if the protocol is HTTP or HTTPS and the target type is `lambda`.`{ "Attributes": [ { "Value": "false", "Key": "lambda.multi_value_headers.enabled" } ] }`The following output includes the attributes if the protocol is TCP, TLS, UDP, or TCP_UDP. `{ "Attributes": [ { "Value": "false", "Key": "proxy_protocol_v2.enabled" }, { "Value": "300", "Key": "deregistration_delay.timeout_seconds" } ] }`- 
                    For API details, see [DescribeTargetGroupAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-group-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-target-groups`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a target group**The following `describe-target-groups`example displays details for the specified target group.`aws elbv2 describe-target-groups \ --target-group-arns``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`Output: `{ "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "TargetGroupName": "my-targets", "Protocol": "HTTP", "Port": 80, "VpcId": "vpc-3ac0fb5f", "HealthCheckProtocol": "HTTP", "HealthCheckPort": "traffic-port", "HealthCheckEnabled": true, "HealthCheckIntervalSeconds": 30, "HealthCheckTimeoutSeconds": 5, "HealthyThresholdCount": 5, "UnhealthyThresholdCount": 2, "HealthCheckPath": "/", "Matcher": { "HttpCode": "200" }, "LoadBalancerArns": [ "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188" ], "TargetType": "instance", "ProtocolVersion": "HTTP1", "IpAddressType": "ipv4" } ] }`**Example 2: To describe all target groups for a load balancer**The following `describe-target-groups`example displays details for all target groups for the specified load balancer. The example uses the`--query`parameter to display only the target group names.`aws elbv2 describe-target-groups \ --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`\ --query`TargetGroups[*].TargetGroupName`Output: `[ "my-instance-targets", "my-ip-targets", "my-lambda-target" ]`For more information, see [Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)in the*Application Load Balancers Guide*.- 
                    For API details, see [DescribeTargetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-target-health`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the health of the targets for a target group**The following `describe-target-health`example displays health details for the targets of the specified target group. These targets are healthy.`aws elbv2 describe-target-health \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`Output: `{ "TargetHealthDescriptions": [ { "HealthCheckPort": "80", "Target": { "Id": "i-ceddcd4d", "Port": 80 }, "TargetHealth": { "State": "healthy" } }, { "HealthCheckPort": "80", "Target": { "Id": "i-0f76fade", "Port": 80 }, "TargetHealth": { "State": "healthy" } } ] }`**Example 2: To describe the health of a target**The following `describe-target-health`example displays health details for the specified target. This target is healthy.`aws elbv2 describe-target-health \ --targets``Id=i-0f76fade,Port=80`\ --target-group-arn`arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`Output: `{ "TargetHealthDescriptions": [ { "HealthCheckPort": "80", "Target": { "Id": "i-0f76fade", "Port": 80 }, "TargetHealth": { "State": "healthy" } } ] }`The following example output is for a target whose target group is not specified in an action for a listener. This target can't receive traffic from the load balancer. `{ "TargetHealthDescriptions": [ { "HealthCheckPort": "80", "Target": { "Id": "i-0f76fade", "Port": 80 }, "TargetHealth": { "State": "unused", "Reason": "Target.NotInUse", "Description": "Target group is not configured to receive traffic from the load balancer" } } ] }`The following example output is for a target whose target group was just specified in an action for a listener. The target is still being registered. `{ "TargetHealthDescriptions": [ { "HealthCheckPort": "80", "Target": { "Id": "i-0f76fade", "Port": 80 }, "TargetHealth": { "State": "initial", "Reason": "Elb.RegistrationInProgress", "Description": "Target registration is in progress" } } ] }`The following example output is for an unhealthy target. `{ "TargetHealthDescriptions": [ { "HealthCheckPort": "80", "Target": { "Id": "i-0f76fade", "Port": 80 }, "TargetHealth": { "State": "unhealthy", "Reason": "Target.Timeout", "Description": "Connection to target timed out" } } ] }`The following example output is for a target that is a Lambda function and health checks are disabled. `{ "TargetHealthDescriptions": [ { "Target": { "Id": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "AvailabilityZone": "all", }, "TargetHealth": { "State": "unavailable", "Reason": "Target.HealthCheckDisabled", "Description": "Health checks are not enabled for this target" } } ] }`- 
                    For API details, see [DescribeTargetHealth](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-health.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-listener`.

- **AWS CLI**
- 
            
                    **Example 1: To change the default action to a forward action**The following `modify-listener`example changes the default action to a`forward`action for the specified listener.`aws elbv2 modify-listener \ --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`\ --default-actions`Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f`Output: `{ "Listeners": [ { "ListenerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2", "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188", "Protocol": "HTTP", "Port": 80, "DefaultActions": [ { "Type": "forward", "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-new-targets/2453ed029918f21f" } ] } ] }`**Example 2: To change the default action to a redirect action**The following `modify-listener`example changes the default action to a`redirect`action for the specified listener.`aws elbv2 modify-listener \ --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`\ --default-actions`Type=redirect,`RedirectConfig='{Protocol=HTTPS,StatusCode=HTTP_302}'Output: `{ "Listeners": [ { "ListenerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2", "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188", "Protocol": "HTTP", "Port": 80, "DefaultActions": [ { "Type": "redirect", "RedirectConfig": { "Protocol": "HTTPS", "Port": "#{port}", "Host": "#{host}", "Path": "/#{path}", "Query": "#{query}", "StatusCode": "HTTP_302", } } ] } ] }`**Example 3: To change the server certificate**The following `modify-listener`example changes the server certificate for the specified HTTPS listener.`aws elbv2 modify-listener \ --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65`\ --certificates`CertificateArn=arn:aws:iam::123456789012:server-certificate/my-new-server-cert`Output: `{ "Listeners": [ { "ListenerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/0467ef3c8400ae65", "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188", "Protocol": "HTTPS", "Port": 443, "DefaultActions": [ { "Type": "forward", "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067" } ], "SslPolicy": "ELBSecurityPolicy-2015-05", "Certificates": [ { "CertificateArn": "arn:aws:iam::123456789012:server-certificate/my-new-server-cert" } ], } ] }`For more information, see [Listener rules](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html#listener-rules)in the*Application Load Balancers User Guide*.- 
                    For API details, see [ModifyListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-load-balancer-attributes`.

- **AWS CLI**
- 
            
                    **To enable deletion protection**This example enables deletion protection for the specified load balancer. Command: `aws elbv2 modify-load-balancer-attributes --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`--attributes`Key=deletion_protection.enabled,Value=true`Output: `{ "Attributes": [ { "Value": "true", "Key": "deletion_protection.enabled" }, { "Value": "false", "Key": "access_logs.s3.enabled" }, { "Value": "60", "Key": "idle_timeout.timeout_seconds" }, { "Value": "", "Key": "access_logs.s3.prefix" }, { "Value": "", "Key": "access_logs.s3.bucket" } ] }`**To change the idle timeout**This example changes the idle timeout value for the specified load balancer. Command: `aws elbv2 modify-load-balancer-attributes --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`--attributes`Key=idle_timeout.timeout_seconds,Value=30`Output: `{ "Attributes": [ { "Value": "30", "Key": "idle_timeout.timeout_seconds" }, { "Value": "false", "Key": "access_logs.s3.enabled" }, { "Value": "", "Key": "access_logs.s3.prefix" }, { "Value": "true", "Key": "deletion_protection.enabled" }, { "Value": "", "Key": "access_logs.s3.bucket" } ] }`**To enable access logs**This example enables access logs for the specified load balancer. Note that the S3 bucket must exist in the same region as the load balancer and must have a policy attached that grants access to the Elastic Load Balancing service. Command: `aws elbv2 modify-load-balancer-attributes --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`--attributes`Key=access_logs.s3.enabled,Value=true``Key=access_logs.s3.bucket,Value=my-loadbalancer-logs``Key=access_logs.s3.prefix,Value=myapp`Output: `{ "Attributes": [ { "Value": "true", "Key": "access_logs.s3.enabled" }, { "Value": "my-load-balancer-logs", "Key": "access_logs.s3.bucket" }, { "Value": "myapp", "Key": "access_logs.s3.prefix" }, { "Value": "60", "Key": "idle_timeout.timeout_seconds" }, { "Value": "false", "Key": "deletion_protection.enabled" } ] }`- 
                    For API details, see [ModifyLoadBalancerAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-load-balancer-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-rule`.

- **AWS CLI**
- 
            
                    **To modify a rule**The following `modify-rule`example updates the actions and conditions for the specified rule.`aws elbv2 modify-rule \ --actions``Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`\ --conditions Field=path-pattern,Values='/images/*' --rule-arn`arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee`Output: `{ "Rules": [ { "Priority": "10", "Conditions": [ { "Field": "path-pattern", "Values": [ "/images/*" ] } ], "RuleArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee", "IsDefault": false, "Actions": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "Type": "forward" } ] } ] }`- 
                    For API details, see [ModifyRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-target-group-attributes`.

- **AWS CLI**
- 
            
                    **To modify the deregistration delay timeout**This example sets the deregistration delay timeout to the specified value for the specified target group. Command: `aws elbv2 modify-target-group-attributes --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`--attributes`Key=deregistration_delay.timeout_seconds,Value=600`Output: `{ "Attributes": [ { "Value": "false", "Key": "stickiness.enabled" }, { "Value": "600", "Key": "deregistration_delay.timeout_seconds" }, { "Value": "lb_cookie", "Key": "stickiness.type" }, { "Value": "86400", "Key": "stickiness.lb_cookie.duration_seconds" } ] }`- 
                    For API details, see [ModifyTargetGroupAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-target-group`.

- **AWS CLI**
- 
            
                    **To modify the health check configuration for a target group**The following `modify-target-group`example changes the configuration of the health checks used to evaluate the health of the targets for the specified target group. Note that due to the way the CLI parses commas, you must surround the range for the`--matcher`option with single quotes instead of double quotes.`aws elbv2 modify-target-group \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f`\ --health-check-protocol`HTTPS`\ --health-check-port`443`\ --matcher HttpCode='200,299'Output: `{ "TargetGroups": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-https-targets/2453ed029918f21f", "TargetGroupName": "my-https-targets", "Protocol": "HTTPS", "Port": 443, "VpcId": "vpc-3ac0fb5f", "HealthCheckProtocol": "HTTPS", "HealthCheckPort": "443", "HealthCheckEnabled": true, "HealthCheckIntervalSeconds": 30, "HealthCheckTimeoutSeconds": 5, "HealthyThresholdCount": 5, "UnhealthyThresholdCount": 2, "Matcher": { "HttpCode": "200,299" }, "LoadBalancerArns": [ "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188" ], "TargetType": "instance", "ProtocolVersion": "HTTP1", "IpAddressType": "ipv4" } ] }`For more information, see [Target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html)in the*Application Load Balancers Guide*.- 
                    For API details, see [ModifyTargetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-targets`.

- **AWS CLI**
- 
            
                    **Example 1: To register targets with a target group by instance ID**The following `register-targets`example registers the specified instances with a target group. The target group must have a target type of`instance`.`aws elbv2 register-targets \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067`\ --targets`Id=i-1234567890abcdef0``Id=i-0abcdef1234567890`**Example 2: To register targets with a target group using port overrides**The following `register-targets`example registers the specified instance with a target group using multiple ports. This enables you to register containers on the same instance as targets in the target group.`aws elbv2 register-targets \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-internal-targets/3bb63f11dfb0faf9`\ --targets`Id=i-0598c7d356eba48d7,Port=80``Id=i-0598c7d356eba48d7,Port=766`**Example 3: To register targets with a target group by IP address**The following `register-targets`example registers the specified IP addresses with a target group. The target group must have a target type of`ip`.`aws elbv2 register-targets \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-ip-targets/8518e899d173178f`\ --targets`Id=10.0.1.15``Id=10.0.1.23`**Example 4: To register a Lambda function as a target**The following `register-targets`example registers the specified IP addresses with a target group. The target group must have a target type of`lambda`. You must grant Elastic Load Balancing permission to invoke the Lambda function.`aws elbv2 register-targets \ --target-group-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-ip-targets/8518e899d173178f`\ --targets`Id=arn:aws:lambda:us-west-2:123456789012:function:my-function`- 
                    For API details, see [RegisterTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/register-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-listener-certificates`.

- **AWS CLI**
- 
            
                    **To remove a certificate from a secure listener**This example removes the specified certificate from the specified secure listener. Command: `aws elbv2 remove-listener-certificates --listener-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2`--certificates`CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/5cc54884-f4a3-4072-80be-05b9ba72f705`- 
                    For API details, see [RemoveListenerCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-listener-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags`.

- **AWS CLI**
- 
            
                    **To remove tags from a load balancer**The following `remove-tags`example removes the`project`and`department`tags from the specified load balancer.`aws elbv2 remove-tags \ --resource-arns``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`\ --tag-keys`project``department`- 
                    For API details, see [RemoveTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/remove-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-ip-address-type`.

- **AWS CLI**
- 
            
                    **To set the address type of a load balancer**This example sets the address type of the specified load balancer to `dualstack`. The load balancer subnets must have associated IPv6 CIDR blocks.Command: `aws elbv2 set-ip-address-type --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`--ip-address-type`dualstack`Output: `{ "IpAddressType": "dualstack" }`- 
                    For API details, see [SetIpAddressType](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-ip-address-type.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-rule-priorities`.

- **AWS CLI**
- 
            
                    **To set the rule priority**This example sets the priority of the specified rule. Command: `aws elbv2 set-rule-priorities --rule-priorities``RuleArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3,Priority=5`Output: `{ "Rules": [ { "Priority": "5", "Conditions": [ { "Field": "path-pattern", "Values": [ "/img/*" ] } ], "RuleArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/1291d13826f405c3", "IsDefault": false, "Actions": [ { "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067", "Type": "forward" } ] } ] }`- 
                    For API details, see [SetRulePriorities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-rule-priorities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-security-groups`.

- **AWS CLI**
- 
            
                    **To associate a security group with a load balancer**This example associates the specified security group with the specified load balancer. Command: `aws elbv2 set-security-groups --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`--security-groups`sg-5943793c`Output: `{ "SecurityGroupIds": [ "sg-5943793c" ] }`- 
                    For API details, see [SetSecurityGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-security-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-subnets`.

- **AWS CLI**
- 
            
                    **To enable Availability Zones for a load balancer**This example enables the Availability Zone for the specified subnet for the specified load balancer. Command: `aws elbv2 set-subnets --load-balancer-arn``arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188`--subnets`subnet-8360a9e7``subnet-b7d581c0`Output: `{ "AvailabilityZones": [ { "SubnetId": "subnet-8360a9e7", "ZoneName": "us-west-2a" }, { "SubnetId": "subnet-b7d581c0", "ZoneName": "us-west-2b" } ] }`- 
                    For API details, see [SetSubnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/set-subnets.html)in*AWS CLI Command Reference*.
 
-