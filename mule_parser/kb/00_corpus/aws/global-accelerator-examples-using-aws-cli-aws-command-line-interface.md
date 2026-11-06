# Global Accelerator examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_global-accelerator_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_global-accelerator_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Global Accelerator.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-custom-routing-endpoints`.

- **AWS CLI**
- 
            
                    **To add a VPC subnet endpoint to an endpoint group for a custom routing accelerator**The following `add-custom-routing-endpoints`example adds a VPC subnet endpoint to an endpoint group for a custom routing accelerator.`aws globalaccelerator add-custom-routing-endpoints \ --endpoint-group-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/4321abcd`\ --endpoint-configurations`"EndpointId=subnet-1234567890abcdef0"`Output: `{ "EndpointDescriptions": [ { "EndpointId": "subnet-1234567890abcdef0" } ], "EndpointGroupArn":"arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/4321abcd" }`For more information, see [VPC subnet endpoints for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [AddCustomRoutingEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/add-custom-routing-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `advertise-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To advertise an address range**The following `advertise-byoip-cidr`example requests AWS to advertise an address range that you've provisioned for use with your AWS resources.`aws globalaccelerator advertise-byoip-cidr \ --cidr``198.51.100.0/24`Output: `{ "ByoipCidr": { "Cidr": "198.51.100.0/24", "State": "PENDING_ADVERTISING" } }`For more information, see [Bring Your Own IP Address in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [AdvertiseByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/advertise-byoip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allow-custom-routing-traffic`.

- **AWS CLI**
- 
            
                    **To allow traffic to specific Amazon EC2 instance destinations in a VPC subnet for a custom routing accelerator**The following `allow-custom-routing-traffic`example specifies that traffic is allowed to certain Amazon EC2 instance (destination) IP addresses and ports for a VPC subnet endpoint in a custom routing accelerator can receive traffic.`aws globalaccelerator allow-custom-routing-traffic \ --endpoint-group-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/ab88888example`\ --endpoint-id`subnet-abcd123example`\ --destination-addresses`"172.31.200.6"``"172.31.200.7"`\ --destination-ports`80``81`This command produces no output. For more information, see [VPC subnet endpoints for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [AllowCustomRoutingTraffic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/allow-custom-routing-traffic.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-accelerator`.

- **AWS CLI**
- 
            
                    **To create an accelerator**The following `create-accelerator`example creates an accelerator with two tags with two BYOIP static IP addresses. You must specify the`US-West-2 (Oregon)`Region to create or update an accelerator.`aws globalaccelerator create-accelerator \ --name``ExampleAccelerator`\ --tags Key="Name",Value="Example Name" Key="Project",Value="Example Project" \ --ip-addresses`192.0.2.250``198.51.100.52`Output: `{ "Accelerator": { "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", "IpAddressType": "IPV4", "Name": "ExampleAccelerator", "Enabled": true, "Status": "IN_PROGRESS", "IpSets": [ { "IpAddresses": [ "192.0.2.250", "198.51.100.52" ], "IpFamily": "IPv4" } ], "DnsName":"a1234567890abcdef.awsglobalaccelerator.com", "CreatedTime": 1542394847.0, "LastModifiedTime": 1542394847.0 } }`For more information, see [Accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [CreateAccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-accelerator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-custom-routing-accelerator`.

- **AWS CLI**
- 
            
                    **To create a custom routing accelerator**The following `create-custom-routing-accelerator`example creates a custom routing accelerator with the tags`Name`and`Project`.`aws globalaccelerator create-custom-routing-accelerator \ --name``ExampleCustomRoutingAccelerator`\ --tags Key="Name",Value="Example Name" Key="Project",Value="Example Project" \ --ip-addresses`192.0.2.250``198.51.100.52`Output: `{ "Accelerator": { "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", "IpAddressType": "IPV4", "Name": "ExampleCustomRoutingAccelerator", "Enabled": true, "Status": "IN_PROGRESS", "IpSets": [ { "IpAddresses": [ "192.0.2.250", "198.51.100.52" ], "IpFamily": "IPv4" } ], "DnsName":"a1234567890abcdef.awsglobalaccelerator.com", "CreatedTime": 1542394847.0, "LastModifiedTime": 1542394847.0 } }`For more information, see [Custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [CreateCustomRoutingAccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-accelerator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-custom-routing-endpoint-group`.

- **AWS CLI**
- 
            
                    **To create an endpoint group for a custom routing accelerator**The following `create-custom-routing-endpoint-group`example creates an endpoint group for a custom routing accelerator.`aws globalaccelerator create-custom-routing-endpoint-group \ --listener-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz`\ --endpoint-group-region`us-east-2`\ --destination-configurations`"FromPort=80,ToPort=81,Protocols=TCP,UDP"`Output: `{ "EndpointGroup": { "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/4321abcd", "EndpointGroupRegion": "us-east-2", "DestinationDescriptions": [ { "FromPort": 80, "ToPort": 81, "Protocols": [ "TCP", "UDP" ] } ], "EndpointDescriptions": [] } }`For more information, see [Endpoint groups for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [CreateCustomRoutingEndpointGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-endpoint-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-custom-routing-listener`.

- **AWS CLI**
- 
            
                    **To create a listener for a custom routing accelerator**The following `create-custom-routing-listener`example creates a listener with a port range from 5000 to 10000 for a custom routing accelerator.`aws globalaccelerator create-custom-routing-listener \ --accelerator-arn``arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --port-ranges`FromPort=5000,ToPort=10000`Output: `{ "Listener": { "PortRange": [ "FromPort": 5000, "ToPort": 10000 ], "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz" } }`For more information, see [Listeners for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [CreateCustomRoutingListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-custom-routing-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-endpoint-group`.

- **AWS CLI**
- 
            
                    **To create an endpoint group**The following `create-endpoint-group`example creates an endpoint group with one endpoint.`aws globalaccelerator create-endpoint-group \ --listener-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz`\ --endpoint-group-region`us-east-1`\ --endpoint-configurations`EndpointId=i-1234567890abcdef0,Weight=128`Output: `{ "EndpointGroup": { "TrafficDialPercentage": 100.0, "EndpointDescriptions": [ { "Weight": 128, "EndpointId": "i-1234567890abcdef0" } ], "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/098765zyxwvu", "EndpointGroupRegion": "us-east-1" } }`For more information, see [Endpoint groups in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [CreateEndpointGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-endpoint-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-listener`.

- **AWS CLI**
- 
            
                    **To create a listener**The following `create-listener`example creates a listener with two ports.`aws globalaccelerator create-listener \ --accelerator-arn``arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --port-ranges`FromPort=80,ToPort=80``FromPort=81,ToPort=81`\ --protocol`TCP`Output: `{ "Listener": { "PortRanges": [ { "ToPort": 80, "FromPort": 80 }, { "ToPort": 81, "FromPort": 81 } ], "ClientAffinity": "NONE", "Protocol": "TCP", "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz" } }`For more information, see [Listeners in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [CreateListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/create-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deny-custom-routing-traffic`.

- **AWS CLI**
- 
            
                    **To specify a destination address that cannot receive traffic in a custom routing accelerator**The following `deny-custom-routing-traffic`example specifies destination address or addresses in a subnet endpoint that cannot receive traffic for a custom routing accelerator. To specify more than one destination address, separate the addresses with a space. There's no response for a successful deny-custom-routing-traffic call.`aws globalaccelerator deny-custom-routing-traffic \ --endpoint-group-arn``"arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/ab88888example"`\ --endpoint-id`"subnet-abcd123example"`\ --destination-addresses`"198.51.100.52"`This command produces no output. For more information, see [VPC subnet endpoints for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoints.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DenyCustomRoutingTraffic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/deny-custom-routing-traffic.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deprovision-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To deprovision an address range**The following `deprovision-byoip-cidr`example releases the specified address range that you provisioned to use with your AWS resources.`aws globalaccelerator deprovision-byoip-cidr \ --cidr``"198.51.100.0/24"`Output: `{ "ByoipCidr": { "Cidr": "198.51.100.0/24", "State": "PENDING_DEPROVISIONING" } }`For more information, see [Bring your own IP address in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DeprovisionByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/deprovision-byoip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-accelerator-attributes`.

- **AWS CLI**
- 
            
                    **To describe an accelerator's attributes**The following `describe-accelerator-attributes`example retrieves the attribute details for an accelerator.`aws globalaccelerator describe-accelerator-attributes \ --accelerator-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "AcceleratorAttributes": { "FlowLogsEnabled": true "FlowLogsS3Bucket": flowlogs-abc "FlowLogsS3Prefix": bucketprefix-abc } }`For more information, see [Accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeAcceleratorAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-accelerator-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-accelerator`.

- **AWS CLI**
- 
            
                    **To describe an accelerator**The following `describe-accelerator`example retrieves the details about the specified accelerator.`aws globalaccelerator describe-accelerator \ --accelerator-arn``arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "Accelerator": { "AcceleratorArn": "arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", "IpAddressType": "IPV4", "Name": "ExampleAccelerator", "Enabled": true, "Status": "IN_PROGRESS", "IpSets": [ { "IpAddresses": [ "192.0.2.250", "198.51.100.52" ], "IpFamily": "IPv4" } ], "DnsName":"a1234567890abcdef.awsglobalaccelerator.com", "CreatedTime": 1542394847, "LastModifiedTime": 1542395013 } }`For more information, see [Accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeAccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-accelerator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-custom-routing-accelerator-attributes`.

- **AWS CLI**
- 
            
                    **To describe a custom routing accelerator's attributes**The following `describe-custom-routing-accelerator-attributes`example describes the attributes for a custom routing accelerator.`aws globalaccelerator describe-custom-routing-accelerator-attributes \ --accelerator-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "AcceleratorAttributes": { "FlowLogsEnabled": false } }`For more information, see [Custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeCustomRoutingAcceleratorAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-accelerator-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-custom-routing-accelerator`.

- **AWS CLI**
- 
            
                    **To describe a custom routing accelerator**The following `describe-custom-routing-accelerator`example retrieves the details about the specified custom routing accelerator.`aws globalaccelerator describe-custom-routing-accelerator \ --accelerator-arn``arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "Accelerator": { "AcceleratorArn": "arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", "IpAddressType": "IPV4", "Name": "ExampleCustomRoutingAccelerator", "Enabled": true, "Status": "IN_PROGRESS", "IpSets": [ { "IpAddresses": [ "192.0.2.250", "198.51.100.52" ], "IpFamily": "IPv4" } ], "DnsName":"a1234567890abcdef.awsglobalaccelerator.com", "CreatedTime": 1542394847, "LastModifiedTime": 1542395013 } }`For more information, see [Custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeCustomRoutingAccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-accelerator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-custom-routing-endpoint-group`.

- **AWS CLI**
- 
            
                    **To describe an endpoint group for a custom routing accelerator**The following `describe-custom-routing-endpoint-group`example describes an endpoint group for a custom routing accelerator.`aws globalaccelerator describe-custom-routing-endpoint-group \ --endpoint-group-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz/endpoint-group/ab88888example`Output: `{ "EndpointGroup": { "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz/endpoint-group/ab88888example", "EndpointGroupRegion": "us-east-2", "DestinationDescriptions": [ { "FromPort": 5000, "ToPort": 10000, "Protocols": [ "UDP" ] } ], "EndpointDescriptions": [ { "EndpointId": "subnet-1234567890abcdef0" } ] } }`For more information, see [Endpoint groups for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeCustomRoutingEndpointGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-endpoint-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-custom-routing-listener`.

- **AWS CLI**
- 
            
                    **To describe a listener for a custom routing accelerator**The following `describe-custom-routing-listener`example describes a listener for a custom routing accelerator.`aws globalaccelerator describe-custom-routing-listener \ --listener-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234`Output: `{ "Listener": { "PortRanges": [ "FromPort": 5000, "ToPort": 10000 ], "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234" } }`For more information, see [Listeners for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeCustomRoutingListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-custom-routing-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-endpoint-group`.

- **AWS CLI**
- 
            
                    **To describe an endpoint group**The following `describe-endpoint-group`example retrieves details about an endpoint group with the following endpoints: an Amazon EC2 instance, an ALB, and an NLB.`aws globalaccelerator describe-endpoint-group \ --endpoint-group-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/ab88888example`Output: `{ "EndpointGroup": { "TrafficDialPercentage": 100.0, "EndpointDescriptions": [ { "Weight": 128, "EndpointId": "i-1234567890abcdef0" }, { "Weight": 128, "EndpointId": "arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/app/ALBTesting/alb01234567890xyz" }, { "Weight": 128, "EndpointId": "arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/net/NLBTesting/alb01234567890qrs" } ], "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/4321abcd-abcd-4321-abcd-4321abcdefg", "EndpointGroupRegion": "us-east-1" } }`For more information, see [Endpoint groups in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeEndpointGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-endpoint-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-listener`.

- **AWS CLI**
- 
            
                    **To describe a listener**The following `describe-listener`example describes a listener.`aws globalaccelerator describe-listener \ --listener-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234`Output: `{ "Listener": { "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234", "PortRanges": [ { "FromPort": 80, "ToPort": 80 } ], "Protocol": "TCP", "ClientAffinity": "NONE" } }`For more information, see [Listeners in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [DescribeListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/describe-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-accelerators`.

- **AWS CLI**
- 
            
                    **To list your accelerators**The following `list-accelerators`example lists the accelerators in your AWS account. This account has two accelerators.`aws globalaccelerator list-accelerators`Output: `{ "Accelerators": [ { "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/5555abcd-abcd-5555-abcd-5555EXAMPLE1", "Name": "TestAccelerator", "IpAddressType": "IPV4", "Enabled": true, "IpSets": [ { "IpFamily": "IPv4", "IpAddresses": [ "192.0.2.250", "198.51.100.52" ] } ], "DnsName": "5a5a5a5a5a5a5a5a.awsglobalaccelerator.com", "Status": "DEPLOYED", "CreatedTime": 1552424416.0, "LastModifiedTime": 1569375641.0 }, { "AcceleratorArn": "arn:aws:globalaccelerator::888888888888:accelerator/8888abcd-abcd-8888-abcd-8888EXAMPLE2", "Name": "ExampleAccelerator", "IpAddressType": "IPV4", "Enabled": true, "IpSets": [ { "IpFamily": "IPv4", "IpAddresses": [ "192.0.2.100", "198.51.100.10" ] } ], "DnsName": "6a6a6a6a6a6a6a.awsglobalaccelerator.com", "Status": "DEPLOYED", "CreatedTime": 1575585564.0, "LastModifiedTime": 1579809243.0 }, ] }`For more information, see [Accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListAccelerators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-accelerators.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To list your address ranges**The following `list-byoip-cidr`example list the bring your own IP address (BYOIP) address ranges that you've provisioned for use with Global Accelerator.`aws globalaccelerator list-byoip-cidrs`Output: `{ "ByoipCidrs": [ { "Cidr": "198.51.100.0/24", "State": "READY" } { "Cidr": "203.0.113.25/24", "State": "READY" } ] }`For more information, see [Bring your own IP address in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-byoip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-custom-routing-accelerators`.

- **AWS CLI**
- 
            
                    **To list your custom routing accelerators**The following `list-custom-routing-accelerators`example lists the custom routing accelerators in an AWS account.`aws globalaccelerator list-custom-routing-accelerators`Output: `{ "Accelerators": [ { "AcceleratorArn": "arn:aws:globalaccelerator::012345678901:accelerator/5555abcd-abcd-5555-abcd-5555EXAMPLE1", "Name": "TestCustomRoutingAccelerator", "IpAddressType": "IPV4", "Enabled": true, "IpSets": [ { "IpFamily": "IPv4", "IpAddresses": [ "192.0.2.250", "198.51.100.52" ] } ], "DnsName": "5a5a5a5a5a5a5a5a.awsglobalaccelerator.com", "Status": "DEPLOYED", "CreatedTime": 1552424416.0, "LastModifiedTime": 1569375641.0 }, { "AcceleratorArn": "arn:aws:globalaccelerator::888888888888:accelerator/8888abcd-abcd-8888-abcd-8888EXAMPLE2", "Name": "ExampleCustomRoutingAccelerator", "IpAddressType": "IPV4", "Enabled": true, "IpSets": [ { "IpFamily": "IPv4", "IpAddresses": [ "192.0.2.100", "198.51.100.10" ] } ], "DnsName": "6a6a6a6a6a6a6a.awsglobalaccelerator.com", "Status": "DEPLOYED", "CreatedTime": 1575585564.0, "LastModifiedTime": 1579809243.0 }, ] }`For more information, see [Custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListCustomRoutingAccelerators](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-accelerators.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-custom-routing-endpoint-groups`.

- **AWS CLI**
- 
            
                    **To list endpoint groups for a listener in a custom routing accelerator**The following `list-custom-routing-endpoint-groups`example lists the endpoint groups for a listener in a custom routing accelerator.`aws globalaccelerator list-custom-routing-endpoint-groups \ --listener-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234`Output: `{ "EndpointGroups": [ { "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234/endpoint-group/ab88888example", "EndpointGroupRegion": "eu-central-1", "DestinationDescriptions": [ { "FromPort": 80, "ToPort": 80, "Protocols": [ "TCP", "UDP" ] } ] "EndpointDescriptions": [ { "EndpointId": "subnet-abcd123example" } ] } ] }`For more information, see [Endpoint groups for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-endpoint-groups.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListCustomRoutingEndpointGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-endpoint-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-custom-routing-listeners`.

- **AWS CLI**
- 
            
                    **To list listeners for custom routing accelerators**The following `list-custom-routing-listeners`example lists the listeners for a custom routing accelerator.`aws globalaccelerator list-custom-routing-listeners \ --accelerator-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "Listeners": [ { "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234", "PortRanges": [ { "FromPort": 5000, "ToPort": 10000 } ], "Protocol": "TCP" } ] }`For more information, see [Listeners for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListCustomRoutingListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-listeners.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-custom-routing-port-mappings-by-destination`.

- **AWS CLI**
- 
            
                    **To list the port mappings for a specific custom routing accelerator destination**The following `list-custom-routing-port-mappings-by-destination`example provides the port mappings for a specific destination EC2 server (at the destination address) for a custom routing accelerator.`aws globalaccelerator list-custom-routing-port-mappings-by-destination \ --endpoint-id``subnet-abcd123example`\ --destination-address`198.51.100.52`Output: `{ "DestinationPortMappings": [ { "AcceleratorArn": "arn:aws:globalaccelerator::402092451327:accelerator/24ea29b8-d750-4489-8919-3095f3c4b0a7", "AcceleratorSocketAddresses": [ { "IpAddress": "192.0.2.250", "Port": 65514 }, { "IpAddress": "192.10.100.99", "Port": 65514 } ], "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/ab88888example", "EndpointId": "subnet-abcd123example", "EndpointGroupRegion": "us-west-2", "DestinationSocketAddress": { "IpAddress": "198.51.100.52", "Port": 80 }, "IpAddressType": "IPv4", "DestinationTrafficState": "ALLOW" } ] }`For more information, see [How custom routing accelerators work in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-how-it-works.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListCustomRoutingPortMappingsByDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-port-mappings-by-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-custom-routing-port-mappings`.

- **AWS CLI**
- 
            
                    **To list the port mappings in a custom routing accelerator**The following `list-custom-routing-port-mappings`example provides a partial list of the port mappings in a custom routing accelerator.`aws globalaccelerator list-custom-routing-port-mappings \ --accelerator-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "PortMappings": [ { "AcceleratorPort": 40480, "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/098765zyxwvu", "EndpointId": "subnet-1234567890abcdef0", "DestinationSocketAddress": { "IpAddress": "192.0.2.250", "Port": 80 }, "Protocols": [ "TCP", "UDP" ], "DestinationTrafficState": "ALLOW" } { "AcceleratorPort": 40481, "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz/endpoint-group/098765zyxwvu", "EndpointId": "subnet-1234567890abcdef0", "DestinationSocketAddress": { "IpAddress": "192.0.2.251", "Port": 80 }, "Protocols": [ "TCP", "UDP" ], "DestinationTrafficState": "ALLOW" } ] }`For more information, see [How custom routing accelerators work in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-how-it-works.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListCustomRoutingPortMappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-custom-routing-port-mappings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-endpoint-groups`.

- **AWS CLI**
- 
            
                    **To list endpoint groups**The following `list-endpoint-groups`example lists the endpoint groups for a listener. This listener has two endpoint groups.`aws globalaccelerator --region``us-west-2``list-endpoint-groups`\ --listener-arn`arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234`Output: `{ "EndpointGroups": [ { "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234/endpoint-group/ab88888example", "EndpointGroupRegion": "eu-central-1", "EndpointDescriptions": [], "TrafficDialPercentage": 100.0, "HealthCheckPort": 80, "HealthCheckProtocol": "TCP", "HealthCheckIntervalSeconds": 30, "ThresholdCount": 3 } { "EndpointGroupArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234/endpoint-group/ab99999example", "EndpointGroupRegion": "us-east-1", "EndpointDescriptions": [], "TrafficDialPercentage": 50.0, "HealthCheckPort": 80, "HealthCheckProtocol": "TCP", "HealthCheckIntervalSeconds": 30, "ThresholdCount": 3 } ] }`For more information, see [Endpoint Groups in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListEndpointGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-endpoint-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-listeners`.

- **AWS CLI**
- 
            
                    **To list listeners**The following `list-listeners`example lists the listeners for an accelerator.`aws globalaccelerator list-listeners \ --accelerator-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "Listeners": [ { "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/abcdef1234", "PortRanges": [ { "FromPort": 80, "ToPort": 80 } ], "Protocol": "TCP", "ClientAffinity": "NONE" } ] }`For more information, see [Listeners in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-listeners.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for an accelerator**The following `list-tags-for-resource`example lists the tags for a specific accelerator.`aws globalaccelerator list-tags-for-resource \ --resource-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`Output: `{ "Tags": [ { "Key": "Project", "Value": "A123456" } ] }`For more information, see [Tagging in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `provision-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To provision an address range**The following `provision-byoip-cidr`example provisions the specified address range to use with your AWS resources.`aws globalaccelerator provision-byoip-cidr \ --cidr``192.0.2.250/24`\ --cidr-authorization-context Message="$text_message",Signature="$signed_message"Output: `{ "ByoipCidr": { "Cidr": "192.0.2.250/24", "State": "PENDING_PROVISIONING" } }`For more information, see [Bring your own IP address in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [ProvisionByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/provision-byoip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag an accelerator**The following `tag-resource`example adds tags Name and Project to an accelerator, along with corresponding values for each.`aws globalaccelerator tag-resource \ --resource-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --tags Key="Name",Value="Example Name" Key="Project",Value="Example Project"This command produces no output. For more information, see [Tagging in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from an accelerator**The following `untag-resource`example removes the tags Name and Project from an accelerator.`aws globalaccelerator untag-resource \ --resource-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --tag-keys Key="Name" Key="Project"This command produces no output. For more information, see [Tagging in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/tagging-in-global-accelerator.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-accelerator-attributes`.

- **AWS CLI**
- 
            
                    **To update an accelerator's attributes**The following `update-accelerator-attributes`example updates an accelerator to enable flow logs. You must specify the`US-West-2 (Oregon)`Region to create or update accelerator attributes.`aws globalaccelerator update-accelerator-attributes \ --accelerator-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --flow-logs-enabled \ --flow-logs-s3-bucket`flowlogs-abc`\ --flow-logs-s3-prefix`bucketprefix-abc`Output: `{ "AcceleratorAttributes": { "FlowLogsEnabled": true "FlowLogsS3Bucket": flowlogs-abc "FlowLogsS3Prefix": bucketprefix-abc } }`For more information, see [Accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UpdateAcceleratorAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-accelerator`.

- **AWS CLI**
- 
            
                    **To update an accelerator**The following `update-accelerator`example modifies an accelerator to change the accelerator name to`ExampleAcceleratorNew`. You must specify the`US-West-2 (Oregon)`Region to create or update accelerators.`aws globalaccelerator update-accelerator \ --accelerator-arn``arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --name`ExampleAcceleratorNew`Output: `{ "Accelerator": { "AcceleratorArn": "arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", "IpAddressType": "IPV4", "Name": "ExampleAcceleratorNew", "Enabled": true, "Status": "IN_PROGRESS", "IpSets": [ { "IpAddresses": [ "192.0.2.250", "198.51.100.52" ], "IpFamily": "IPv4" } ], "DnsName":"a1234567890abcdef.awsglobalaccelerator.com", "CreatedTime": 1232394847, "LastModifiedTime": 1232395654 } }`For more information, see [Accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UpdateAccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-accelerator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-custom-routing-accelerator-attributes`.

- **AWS CLI**
- 
            
                    **To update a custom routing accelerator's attributes**The following `update-custom-routing-accelerator-attributes`example updates a custom routing accelerator to enable flow logs.`aws globalaccelerator update-custom-routing-accelerator-attributes \ --accelerator-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --flow-logs-enabled \ --flow-logs-s3-bucket`flowlogs-abc`\ --flow-logs-s3-prefix`bucketprefix-abc`Output: `{ "AcceleratorAttributes": { "FlowLogsEnabled": true "FlowLogsS3Bucket": flowlogs-abc "FlowLogsS3Prefix": bucketprefix-abc } }`For more information, see [Custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UpdateCustomRoutingAcceleratorAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-custom-routing-accelerator-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-custom-routing-accelerator`.

- **AWS CLI**
- 
            
                    **To update a custom routing accelerator**The following `update-custom-routing-accelerator`example modifies a custom routing accelerator to change the accelerator name.`aws globalaccelerator --region``us-west-2``update-custom-routing-accelerator`\ --accelerator-arn`arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh`\ --name`ExampleCustomRoutingAcceleratorNew`Output: `{ "Accelerator": { "AcceleratorArn": "arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh", "IpAddressType": "IPV4", "Name": "ExampleCustomRoutingAcceleratorNew", "Enabled": true, "Status": "IN_PROGRESS", "IpSets": [ { "IpAddresses": [ "192.0.2.250", "198.51.100.52" ], "IpFamily": "IPv4" } ], "DnsName":"a1234567890abcdef.awsglobalaccelerator.com", "CreatedTime": 1232394847, "LastModifiedTime": 1232395654 } }`For more information, see [Custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-accelerators.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UpdateCustomRoutingAccelerator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-custom-routing-accelerator.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-custom-routing-listener`.

- **AWS CLI**
- 
            
                    **To update a listener for a custom routing accelerator**The following `update-custom-routing-listener`example updates a listener to change the port range.`aws globalaccelerator update-custom-routing-listener \ --listener-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz`\ --port-ranges`FromPort=10000,ToPort=20000`Output: `{ "Listener": { "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz "PortRanges": [ { "FromPort": 10000, "ToPort": 20000 } ], "Protocol": "TCP" } }`For more information, see [Listeners for custom routing accelerators in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-custom-routing-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UpdateCustomRoutingListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-custom-routing-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-endpoint-group`.

- **AWS CLI**
- 
            
                    **To update an endpoint group**The following `update-endpoint-group`example adds three endpoints to an endpoint group: an Elastic IP address, an ALB, and an NLB.`aws globalaccelerator update-endpoint-group \ --endpoint-group-arn``arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/ab88888example`\ --endpoint-configurations \`EndpointId=eipalloc-eip01234567890abc,Weight=128`\`EndpointId=arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/app/ALBTesting/alb01234567890xyz,Weight=128`\`EndpointId=arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/net/NLBTesting/alb01234567890qrs,Weight=128`Output: `{ "EndpointGroup": { "TrafficDialPercentage": 100, "EndpointDescriptions": [ { "Weight": 128, "EndpointId": "eip01234567890abc" }, { "Weight": 128, "EndpointId": "arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/app/ALBTesting/alb01234567890xyz" }, { "Weight": 128, "EndpointId": "arn:aws:elasticloadbalancing:us-east-1:000123456789:loadbalancer/net/NLBTesting/alb01234567890qrs" } ], "EndpointGroupArn": "arn:aws:globalaccelerator::123456789012:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/6789vxyz-vxyz-6789-vxyz-6789lmnopqrs/endpoint-group/4321abcd-abcd-4321-abcd-4321abcdefg", "EndpointGroupRegion": "us-east-1" } }`For more information, see [Endpoint groups in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UpdateEndpointGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-endpoint-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-listener`.

- **AWS CLI**
- 
            
                    **To update a listener**The following `update-listener`example updates a listener to change the port to 100.`aws globalaccelerator update-listener \ --listener-arn``arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz`\ --port-ranges`FromPort=100,ToPort=100`Output: `{ "Listener": { "ListenerArn": "arn:aws:globalaccelerator::012345678901:accelerator/1234abcd-abcd-1234-abcd-1234abcdefgh/listener/0123vxyz "PortRanges": [ { "FromPort": 100, "ToPort": 100 } ], "Protocol": "TCP", "ClientAffinity": "NONE" } }`For more information, see [Listeners in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/about-listeners.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [UpdateListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/update-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `withdraw-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To withdraw an address range**The following `withdraw-byoip-cidr`example withdraws an address range from AWS Global Accelerator that you previously advertised for use with your AWS resources.`aws globalaccelerator withdraw-byoip-cidr \ --cidr``192.0.2.250/24`Output: `{ "ByoipCidr": { "Cidr": "192.0.2.250/24", "State": "PENDING_WITHDRAWING" } }`For more information, see [Bring your own IP address in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/using-byoip.html)in the*AWS Global Accelerator Developer Guide*.- 
                    For API details, see [WithdrawByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/globalaccelerator/withdraw-byoip-cidr.html)in*AWS CLI Command Reference*.
 
-