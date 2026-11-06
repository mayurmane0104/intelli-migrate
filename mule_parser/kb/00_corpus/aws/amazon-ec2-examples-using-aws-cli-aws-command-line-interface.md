# Amazon EC2 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ec2_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ec2_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon EC2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-address-transfer`.

- **AWS CLI**
- 
            
                    **To accept an Elastic IP address transferred to your account**The following `accept-address-transfer`example accepts the transfer of the specified Elastic IP address to your account.`aws ec2 accept-address-transfer \ --address``100.21.184.216`Output: `{ "AddressTransfer": { "PublicIp": "100.21.184.216", "AllocationId": "eipalloc-09ad461b0d03f6aaf", "TransferAccountId": "123456789012", "TransferOfferExpirationTimestamp": "2023-02-22T20:51:10.000Z", "TransferOfferAcceptedTimestamp": "2023-02-22T22:52:54.000Z", "AddressTransferStatus": "accepted" } }`For more information, see [Transfer Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html#transfer-EIPs-intro)in the*Amazon VPC User Guide*.- 
                    For API details, see [AcceptAddressTransfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-address-transfer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `accept-reserved-instances-exchange-quote`.

- **AWS CLI**
- 
            
                    **To perform a Convertible Reserved Instance exchange**This example performs an exchange of the specified Convertible Reserved Instances. Command: `aws ec2 accept-reserved-instances-exchange-quote --reserved-instance-ids``7b8750c3-397e-4da4-bbcb-a45ebexample`--target-configurations`OfferingId=b747b472-423c-48f3-8cee-679bcexample`Output: `{ "ExchangeId": "riex-e68ed3c1-8bc8-4c17-af77-811afexample" }`- 
                    For API details, see [AcceptReservedInstancesExchangeQuote](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-reserved-instances-exchange-quote.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `accept-transit-gateway-peering-attachment`.

- **AWS CLI**
- 
            
                    **To accept a transit gateway peering attachment**The following `accept-transit-gateway-peering-attachment`example accepts the specified transit gateway peering attachment. The`--region`parameter specifies the Region that the accepter transit gateway is located in.`aws ec2 accept-transit-gateway-peering-attachment \ --transit-gateway-attachment-id``tgw-attach-4455667788aabbccd`\ --region`us-east-2`Output: `{ "TransitGatewayPeeringAttachment": { "TransitGatewayAttachmentId": "tgw-attach-4455667788aabbccd", "RequesterTgwInfo": { "TransitGatewayId": "tgw-123abc05e04123abc", "OwnerId": "123456789012", "Region": "us-west-2" }, "AccepterTgwInfo": { "TransitGatewayId": "tgw-11223344aabbcc112", "OwnerId": "123456789012", "Region": "us-east-2" }, "State": "pending", "CreationTime": "2019-12-09T11:38:31.000Z" } }`For more information, see [Transit Gateway Peering Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)in the*Transit Gateways Guide*.- 
                    For API details, see [AcceptTransitGatewayPeeringAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-transit-gateway-peering-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `accept-transit-gateway-vpc-attachment`.

- **AWS CLI**
- 
            
                    **To accept a request to attach a VPC to a transit gateway.**The following `accept-transit-gateway-vpc-attachment`example accepts the request forte specified attachment.`aws ec2 accept-transit-gateway-vpc-attachment \ --transit-gateway-attachment-id``tgw-attach-0a34fe6b4fEXAMPLE`Output: `{ "TransitGatewayVpcAttachment": { "TransitGatewayAttachmentId": "tgw-attach-0a34fe6b4fEXAMPLE", "TransitGatewayId": "tgw-0262a0e521EXAMPLE", "VpcId": "vpc-07e8ffd50fEXAMPLE", "VpcOwnerId": "123456789012", "State": "pending", "SubnetIds": [ "subnet-0752213d59EXAMPLE" ], "CreationTime": "2019-07-10T17:33:46.000Z", "Options": { "DnsSupport": "enable", "Ipv6Support": "disable" } } }`For more information, see [Transit Gateway Attachments to a VPC](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html)in the*Transit Gateways Guide*.- 
                    For API details, see [AcceptTransitGatewayVpcAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-transit-gateway-vpc-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `accept-vpc-endpoint-connections`.

- **AWS CLI**
- 
            
                    **To accept an interface endpoint connection request**This example accepts the specified endpoint connection request for the specified endpoint service. Command: `aws ec2 accept-vpc-endpoint-connections --service-id``vpce-svc-03d5ebb7d9579a2b3`--vpc-endpoint-ids`vpce-0c1308d7312217abc`Output: `{ "Unsuccessful": [] }`- 
                    For API details, see [AcceptVpcEndpointConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-vpc-endpoint-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `accept-vpc-peering-connection`.

- **AWS CLI**
- 
            
                    **To accept a VPC peering connection**This example accepts the specified VPC peering connection request. Command: `aws ec2 accept-vpc-peering-connection --vpc-peering-connection-id``pcx-1a2b3c4d`Output: `{ "VpcPeeringConnection": { "Status": { "Message": "Provisioning", "Code": "provisioning" }, "Tags": [], "AccepterVpcInfo": { "OwnerId": "444455556666", "VpcId": "vpc-44455566", "CidrBlock": "10.0.1.0/28" }, "VpcPeeringConnectionId": "pcx-1a2b3c4d", "RequesterVpcInfo": { "OwnerId": "444455556666", "VpcId": "vpc-111abc45", "CidrBlock": "10.0.0.0/28" } } }`- 
                    For API details, see [AcceptVpcPeeringConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/accept-vpc-peering-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `advertise-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To advertise an address range**The following `advertise-byoip-cidr`example advertises the specified public IPv4 address range.`aws ec2 advertise-byoip-cidr \ --cidr``203.0.113.25/24`Output: `{ "ByoipCidr": { "Cidr": "203.0.113.25/24", "StatusMessage": "ipv4pool-ec2-1234567890abcdef0", "State": "provisioned" } }`- 
                    For API details, see [AdvertiseByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/advertise-byoip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-address`.

- **AWS CLI**
- 
            
                    **Example 1: To allocate an Elastic IP address from Amazon's address pool**The following `allocate-address`example allocates an Elastic IP address. Amazon EC2 selects the address from Amazon's address pool.`aws ec2 allocate-address`Output: `{ "PublicIp": "70.224.234.241", "AllocationId": "eipalloc-01435ba59eEXAMPLE", "PublicIpv4Pool": "amazon", "NetworkBorderGroup": "us-west-2", "Domain": "vpc" }`For more information, see [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)in the*Amazon EC2 User Guide*.**Example 2: To allocate an Elastic IP address and associate it with a network border group**The following `allocate-address`example allocates an Elastic IP address and associates it with the specified network border group.`aws ec2 allocate-address \ --network-border-group``us-west-2-lax-1`Output: `{ "PublicIp": "70.224.234.241", "AllocationId": "eipalloc-e03dd489ceEXAMPLE", "PublicIpv4Pool": "amazon", "NetworkBorderGroup": "us-west-2-lax-1", "Domain": "vpc" }`For more information, see [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)in the*Amazon EC2 User Guide*.**Example 3: To allocate an Elastic IP address from an address pool that you own**The following `allocate-address`example allocates an Elastic IP address from an address pool that you have brought to your Amazon Web Services account. Amazon EC2 selects the address from the address pool.`aws ec2 allocate-address \ --public-ipv4-pool``ipv4pool-ec2-1234567890abcdef0`Output: `{ "AllocationId": "eipalloc-02463d08ceEXAMPLE", "NetworkBorderGroup": "us-west-2", "CustomerOwnedIp": "18.218.95.81", "CustomerOwnedIpv4Pool": "ipv4pool-ec2-1234567890abcdef0", "Domain": "vpc" "NetworkBorderGroup": "us-west-2", }`For more information, see [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)in the*Amazon EC2 User Guide*.**Example 4: To allocate an Elastic IP address from an IPAM pool**The following `allocate-address`example allocates a specific /32 Elastic IP address from an Amazon VPC IP Address Manager (IPAM) pool.`aws ec2 allocate-address \ --region``us-east-1`\ --ipam-pool-id`ipam-pool-1234567890abcdef0`\ --address`192.0.2.0`Output: `{ "PublicIp": "192.0.2.0", "AllocationId": "eipalloc-abcdef01234567890", "PublicIpv4Pool": "ipam-pool-1234567890abcdef0", "NetworkBorderGroup": "us-east-1", "Domain": "vpc" }`For more information, see [Allocate sequential Elastic IP addresses from an IPAM pool](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-eip-pool.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [AllocateAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-hosts`.

- **AWS CLI**
- 
            
                    **Example 1: To allocate a Dedicated Host**The following `allocate-hosts`example allocates a single Dedicated Host in the`eu-west-1a`Availability Zone, onto which you can launch`m5.large`instances. By default, the Dedicated Host accepts only target instance launches, and does not support host recovery.`aws ec2 allocate-hosts \ --instance-type``m5.large`\ --availability-zone`eu-west-1a`\ --quantity`1`Output: `{ "HostIds": [ "h-07879acf49EXAMPLE" ] }`**Example 2: To allocate a Dedicated Host with auto-placement and host recovery enabled**The following `allocate-hosts`example allocates a single Dedicated Host in the`eu-west-1a`Availability Zone with auto-placement and host recovery enabled.`aws ec2 allocate-hosts \ --instance-type``m5.large`\ --availability-zone`eu-west-1a`\ --auto-placement`on`\ --host-recovery`on`\ --quantity`1`Output: `{ "HostIds": [ "h-07879acf49EXAMPLE" ] }`**Example 3: To allocate a Dedicated Host with tags**The following `allocate-hosts`example allocates a single Dedicated Host and applies a tag with a key named`purpose`and a value of`production`.`aws ec2 allocate-hosts \ --instance-type``m5.large`\ --availability-zone`eu-west-1a`\ --quantity`1`\ --tag-specifications '`ResourceType=dedicated-host,Tags={Key=purpose,Value=production}`'Output: `{ "HostIds": [ "h-07879acf49EXAMPLE" ] }`For more information, see [Allocate a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-allocating.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [AllocateHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-hosts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-ipam-pool-cidr`.

- **AWS CLI**
- 
            
                    **To allocate a CIDR from an IPAM pool**The following `allocate-ipam-pool-cidr`example allocates a CIDR from an IPAM pool.(Linux): `aws ec2 allocate-ipam-pool-cidr \ --ipam-pool-id``ipam-pool-0533048da7d823723`\ --netmask-length`24`(Windows): `aws ec2 allocate-ipam-pool-cidr``^`--ipam-pool-id`ipam-pool-0533048da7d823723``^`--netmask-length`24`Output: `{ "IpamPoolAllocation": { "Cidr": "10.0.0.0/24", "IpamPoolAllocationId": "ipam-pool-alloc-018ecc28043b54ba38e2cd99943cebfbd", "ResourceType": "custom", "ResourceOwner": "123456789012" } }`For more information, see [Manually allocate a CIDR to a pool to reserve IP address space](https://docs.aws.amazon.com/vpc/latest/ipam/manually-allocate-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [AllocateIpamPoolCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/allocate-ipam-pool-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `apply-security-groups-to-client-vpn-target-network`.

- **AWS CLI**
- 
            
                    **To apply security groups to a target network for a Client VPN endpoint**The following `apply-security-groups-to-client-vpn-target-network`example applies security group`sg-01f6e627a89f4db32`to the association between the specified target network and Client VPN endpoint.`aws ec2 apply-security-groups-to-client-vpn-target-network \ --security-group-ids``sg-01f6e627a89f4db32`\ --vpc-id`vpc-0e2110c2f324332e0`\ --client-vpn-endpoint-id`cvpn-endpoint-123456789123abcde`Output: `{ "SecurityGroupIds": [ "sg-01f6e627a89f4db32" ] }`For more information, see [Target Networks](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [ApplySecurityGroupsToClientVpnTargetNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/apply-security-groups-to-client-vpn-target-network.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `assign-ipv6-addresses`.

- **AWS CLI**
- 
            
                    **To assign specific IPv6 addresses to a network interface**This example assigns the specified IPv6 addresses to the specified network interface. Command: `aws ec2 assign-ipv6-addresses --network-interface-id``eni-38664473`--ipv6-addresses`2001:db8:1234:1a00:3304:8879:34cf:4071``2001:db8:1234:1a00:9691:9503:25ad:1761`Output: `{ "AssignedIpv6Addresses": [ "2001:db8:1234:1a00:3304:8879:34cf:4071", "2001:db8:1234:1a00:9691:9503:25ad:1761" ], "NetworkInterfaceId": "eni-38664473" }`**To assign IPv6 addresses that Amazon selects to a network interface**This example assigns two IPv6 addresses to the specified network interface. Amazon automatically assigns these IPv6 addresses from the available IPv6 addresses in the IPv6 CIDR block range of the subnet. Command: `aws ec2 assign-ipv6-addresses --network-interface-id``eni-38664473`--ipv6-address-count`2`Output: `{ "AssignedIpv6Addresses": [ "2001:db8:1234:1a00:3304:8879:34cf:4071", "2001:db8:1234:1a00:9691:9503:25ad:1761" ], "NetworkInterfaceId": "eni-38664473" }`- 
                    For API details, see [AssignIpv6Addresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-ipv6-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `assign-private-ip-addresses`.

- **AWS CLI**
- 
            
                    **To assign a specific secondary private IP address a network interface**This example assigns the specified secondary private IP address to the specified network interface. If the command succeeds, no output is returned. Command: `aws ec2 assign-private-ip-addresses --network-interface-id``eni-e5aa89a3`--private-ip-addresses`10.0.0.82`**To assign secondary private IP addresses that Amazon EC2 selects to a network interface**This example assigns two secondary private IP addresses to the specified network interface. Amazon EC2 automatically assigns these IP addresses from the available IP addresses in the CIDR block range of the subnet the network interface is associated with. If the command succeeds, no output is returned. Command: `aws ec2 assign-private-ip-addresses --network-interface-id``eni-e5aa89a3`--secondary-private-ip-address-count`2`- 
                    For API details, see [AssignPrivateIpAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-private-ip-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `assign-private-nat-gateway-address`.

- **AWS CLI**
- 
            
                    **To assign private IP addresses to your private NAT gateway**The following `assign-private-nat-gateway-address`example assigns two private IP addresses to the specified private NAT gateway.`aws ec2 assign-private-nat-gateway-address \ --nat-gateway-id``nat-1234567890abcdef0`\ --private-ip-address-count`2`Output: `{ "NatGatewayId": "nat-1234567890abcdef0", "NatGatewayAddresses": [ { "NetworkInterfaceId": "eni-0065a61b324d1897a", "IsPrimary": false, "Status": "assigning" }, { "NetworkInterfaceId": "eni-0065a61b324d1897a", "IsPrimary": false, "Status": "assigning" } ] }`For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [AssignPrivateNatGatewayAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/assign-private-nat-gateway-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-address`.

- **AWS CLI**
- 
            
                    **Example 1: To associate an Elastic IP address with an instance**The following `associate-address`example associates an Elastic IP address with the specified EC2 instance.`aws ec2 associate-address \ --instance-id``i-0b263919b6498b123`\ --allocation-id`eipalloc-64d5890a`Output: `{ "AssociationId": "eipassoc-2bebb745" }`**Example 2: To associate an Elastic IP address with a network interface**The following `associate-address`example associates the specified Elastic IP address with the specified network interface.`aws ec2 associate-address --allocation-id``eipalloc-64d5890a`\ --network-interface-id`eni-1a2b3c4d`Output: `{ "AssociationId": "eipassoc-2bebb745" }`**Example 3: To associate an Elastic IP address with a private IP address**The following `associate-address`example associates the specified Elastic IP address with the specified private IP address in the specified network interface.`aws ec2 associate-address \ --allocation-id``eipalloc-64d5890a`\ --network-interface-id`eni-1a2b3c4d`\ --private-ip-address`10.0.0.85`Output: `{ "AssociationId": "eipassoc-2bebb745" }`For more information, see [Elastic IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [AssociateAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-client-vpn-target-network`.

- **AWS CLI**
- 
            
                    **To associate a target network with a Client VPN endpoint**The following `associate-client-vpn-target-network`example associates a subnet with the specified Client VPN endpoint.`aws ec2 associate-client-vpn-target-network \ --subnet-id``subnet-0123456789abcabca`\ --client-vpn-endpoint-id`cvpn-endpoint-123456789123abcde`Output: `{ "AssociationId": "cvpn-assoc-12312312312312312", "Status": { "Code": "associating" } }`For more information, see [Target Networks](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [AssociateClientVpnTargetNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-client-vpn-target-network.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-dhcp-options`.

- **AWS CLI**
- 
            
                    **To associate a DHCP options set with your VPC**This example associates the specified DHCP options set with the specified VPC. If the command succeeds, no output is returned. Command: `aws ec2 associate-dhcp-options --dhcp-options-id``dopt-d9070ebb`--vpc-id`vpc-a01106c2`**To associate the default DHCP options set with your VPC**This example associates the default DHCP options set with the specified VPC. If the command succeeds, no output is returned. Command: `aws ec2 associate-dhcp-options --dhcp-options-id``default`--vpc-id`vpc-a01106c2`- 
                    For API details, see [AssociateDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-dhcp-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-iam-instance-profile`.

- **AWS CLI**
- 
            
                    **To associate an IAM instance profile with an instance**This example associates an IAM instance profile named `admin-role`with instance`i-123456789abcde123`.Command: `aws ec2 associate-iam-instance-profile --instance-id``i-123456789abcde123`--iam-instance-profile`Name=admin-role`Output: `{ "IamInstanceProfileAssociation": { "InstanceId": "i-123456789abcde123", "State": "associating", "AssociationId": "iip-assoc-0e7736511a163c209", "IamInstanceProfile": { "Id": "AIPAJBLK7RKJKWDXVHIEC", "Arn": "arn:aws:iam::123456789012:instance-profile/admin-role" } } }`- 
                    For API details, see [AssociateIamInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-iam-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-instance-event-window`.

- **AWS CLI**
- 
            
                    **Example 1: To associate one or more instances with an event window**The following `associate-instance-event-window`example associates one or more instances with an event window.`aws ec2 associate-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --association-target`"InstanceIds=i-1234567890abcdef0,i-0598c7d356eba48d7"`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [ "i-1234567890abcdef0", "i-0598c7d356eba48d7" ], "Tags": [], "DedicatedHostIds": [] }, "State": "creating" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 2: To associate instance tags with an event window**The following `associate-instance-event-window`example associates instance tags with an event window. Enter an`instance-event-window-id`parameter to specify the event window. To associate instance tags, specify the`association-target`parameter, and for the parameter value, specify one or more tags.`aws ec2 associate-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --association-target`"InstanceTags=[{Key=k2,Value=v2},{Key=k1,Value=v1}]"`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [ { "Key": "k2", "Value": "v2" }, { "Key": "k1", "Value": "v1" } ], "DedicatedHostIds": [] }, "State": "creating" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 3: To associate a Dedicated Host with an event window**The following `associate-instance-event-window`example associates a Dedicated Host with an event window. Enter an`instance-event-window-id`parameter to specify the event window. To associate a Dedicated Host, specify the`--association-target`parameter, and for the parameter values, specify one of more Dedicated Host IDs.`aws ec2 associate-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --association-target`"DedicatedHostIds=h-029fa35a02b99801d"`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": [ "h-029fa35a02b99801d" ] }, "State": "creating" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.- 
                    For API details, see [AssociateInstanceEventWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-instance-event-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-ipam-resource-discovery`.

- **AWS CLI**
- 
            
                    **To associate a resource discovery with an IPAM**In this example, you are an IPAM delegated admin and a resource discovery has been created and shared with you by another AWS account so that you can use IPAM to manage and monitor resource CIDRs owned by the other account. Note To complete this request, you'll need the resource discovery ID which you can get with [describe-ipam-resource-discoveries](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-resource-discoveries.html)and the IPAM ID which you can get with[describe-ipams](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipams.html).The resource discovery that you are associating must have first been shared with your account using AWS RAM.The`--region`you enter must match the home Region of the IPAM you are associating it with.The following `associate-ipam-resource-discovery`example associates a resource discovery with an IPAM.`aws ec2 associate-ipam-resource-discovery \ --ipam-id``ipam-005f921c17ebd5107`\ --ipam-resource-discovery-id`ipam-res-disco-03e0406de76a044ee`\ --tag-specifications '`ResourceType=ipam-resource-discovery,Tags=[{Key=cost-center,Value=cc123}]`' \ --region`us-east-1`Output: `{ { "IpamResourceDiscoveryAssociation": { "OwnerId": "320805250157", "IpamResourceDiscoveryAssociationId": "ipam-res-disco-assoc-04382a6346357cf82", "IpamResourceDiscoveryAssociationArn": "arn:aws:ec2::320805250157:ipam-resource-discovery-association/ipam-res-disco-assoc-04382a6346357cf82", "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe", "IpamId": "ipam-005f921c17ebd5107", "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-005f921c17ebd5107", "IpamRegion": "us-east-1", "IsDefault": false, "ResourceDiscoveryStatus": "active", "State": "associate-in-progress", "Tags": [] } } }`Once you associate a resource discovery, you can monitor and/or manage the IP addresses of resources created by the other accounts. For more information, see [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [AssociateIpamResourceDiscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-ipam-resource-discovery.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-nat-gateway-address`.

- **AWS CLI**
- 
            
                    **To associate an Elastic IP address with a public NAT gateway**The following `associate-nat-gateway-address`example associates the specified Elastic IP address with the specified public NAT gateway. AWS automatically assigns a secondary private IPv4 address.`aws ec2 associate-nat-gateway-address \ --nat-gateway-id``nat-1234567890abcdef0`\ --allocation-ids`eipalloc-0be6ecac95EXAMPLE`Output: `{ "NatGatewayId": "nat-1234567890abcdef0", "NatGatewayAddresses": [ { "AllocationId": "eipalloc-0be6ecac95EXAMPLE", "NetworkInterfaceId": "eni-09cc4b2558794f7f9", "IsPrimary": false, "Status": "associating" } ] }`For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [AssociateNatGatewayAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-nat-gateway-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-route-table`.

- **AWS CLI**
- 
            
                    **To associate a route table with a subnet**This example associates the specified route table with the specified subnet. Command: `aws ec2 associate-route-table --route-table-id``rtb-22574640`--subnet-id`subnet-9d4a7b6c`Output: `{ "AssociationId": "rtbassoc-781d0d1a" }`- 
                    For API details, see [AssociateRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-security-group-vpc`.

- **AWS CLI**
- 
            
                    **To associate a security group with another VPC**The following `associate-security-group-vpc`example associates the specified security group with the specified VPC.`aws ec2 associate-security-group-vpc \ --group-id``sg-04dbb43907d3f8a78`\ --vpc-id`vpc-0bf4c2739bc05a694`Output: `{ "State": "associating" }`For more information, see [Associate security groups with multiple VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-assoc.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [AssociateSecurityGroupVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-security-group-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-subnet-cidr-block`.

- **AWS CLI**
- 
            
                    **To associate an IPv6 CIDR block with a subnet**This example associates an IPv6 CIDR block with the specified subnet. Command: `aws ec2 associate-subnet-cidr-block --subnet-id``subnet-5f46ec3b`--ipv6-cidr-block`2001:db8:1234:1a00::/64`Output: `{ "SubnetId": "subnet-5f46ec3b", "Ipv6CidrBlockAssociation": { "Ipv6CidrBlock": "2001:db8:1234:1a00::/64", "AssociationId": "subnet-cidr-assoc-3aa54053", "Ipv6CidrBlockState": { "State": "associating" } } }`- 
                    For API details, see [AssociateSubnetCidrBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-subnet-cidr-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-transit-gateway-multicast-domain`.

- **AWS CLI**
- 
            
                    **To associate a transit gateway with a multicast domain**The following `associate-transit-gateway-multicast-domain`example associates the specified subnet and attachment with the specified multicast domain.`aws ec2 associate-transit-gateway-multicast-domain \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef79d6e597`\ --transit-gateway-attachment-id`tgw-attach-028c1dd0f8f5cbe8e`\ --subnet-ids`subnet-000de86e3b49c932a`\ --transit-gateway-multicast-domain-id`tgw-mcast-domain-0c4905cef7EXAMPLE`Output: `{ "Associations": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef79d6e597", "TransitGatewayAttachmentId": "tgw-attach-028c1dd0f8f5cbe8e", "ResourceId": "vpc-01128d2c240c09bd5", "ResourceType": "vpc", "Subnets": [ { "SubnetId": "subnet-000de86e3b49c932a", "State": "associating" } ] } }`For more information, see [Multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-domains-about.html)in the*Transit Gateways Guide*.- 
                    For API details, see [AssociateTransitGatewayMulticastDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-transit-gateway-multicast-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-transit-gateway-route-table`.

- **AWS CLI**
- 
            
                    **To associate a transit gateway route table with a transit gateway attachment**The following example associates the specified transit gateway route table with the specified VPC attachment. `aws ec2 associate-transit-gateway-route-table \ --transit-gateway-route-table-id``tgw-rtb-002573ed1eEXAMPLE`\ --transit-gateway-attachment-id`tgw-attach-0b5968d3b6EXAMPLE`Output: `{ "Association": { "TransitGatewayRouteTableId": "tgw-rtb-002573ed1eEXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-0b5968d3b6EXAMPLE", "ResourceId": "vpc-0065acced4EXAMPLE", "ResourceType": "vpc", "State": "associating" } }`For more information, see [Associate a Transit Gateway Route Table](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#associate-tgw-route-table)in the*AWS Transit Gateways Guide*.- 
                    For API details, see [AssociateTransitGatewayRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-transit-gateway-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-vpc-cidr-block`.

- **AWS CLI**
- 
            
                    **Example 1: To associate an Amazon-provided IPv6 CIDR block with a VPC**The following `associate-vpc-cidr-block`example associates an IPv6 CIDR block with the specified VPC.:`aws ec2 associate-vpc-cidr-block \ --amazon-provided-ipv6-cidr-block \ --ipv6-cidr-block-network-border-group``us-west-2-lax-1`\ --vpc-id`vpc-8EXAMPLE`Output: `{ "Ipv6CidrBlockAssociation": { "AssociationId": "vpc-cidr-assoc-0838ce7d9dEXAMPLE", "Ipv6CidrBlockState": { "State": "associating" }, "NetworkBorderGroup": "us-west-2-lax-1" }, "VpcId": "vpc-8EXAMPLE" }`**Example 2:To associate an additional IPv4 CIDR block with a VPC**The following `associate-vpc-cidr-block`example associates the IPv4 CIDR block`10.2.0.0/16`with the specified VPC.`aws ec2 associate-vpc-cidr-block \ --vpc-id``vpc-1EXAMPLE`\ --cidr-block`10.2.0.0/16`Output: `{ "CidrBlockAssociation": { "AssociationId": "vpc-cidr-assoc-2EXAMPLE", "CidrBlock": "10.2.0.0/16", "CidrBlockState": { "State": "associating" } }, "VpcId": "vpc-1EXAMPLE" }`- 
                    For API details, see [AssociateVpcCidrBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-vpc-cidr-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-classic-link-vpc`.

- **AWS CLI**
- 
            
                    **To link (attach) an EC2-Classic instance to a VPC**This example links instance i-1234567890abcdef0 to VPC vpc-88888888 through the VPC security group sg-12312312. Command: `aws ec2 attach-classic-link-vpc --instance-id``i-1234567890abcdef0`--vpc-id`vpc-88888888`--groups`sg-12312312`Output: `{ "Return": true }`- 
                    For API details, see [AttachClassicLinkVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-classic-link-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-internet-gateway`.

- **AWS CLI**
- 
            
                    **To attach an internet gateway to your VPC**The following `attach-internet-gateway`example attaches the specified internet gateway to the specific VPC.`aws ec2 attach-internet-gateway \ --internet-gateway-id``igw-0d0fb496b3EXAMPLE`\ --vpc-id`vpc-0a60eb65b4EXAMPLE`This command produces no output. For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [AttachInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-internet-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-network-interface`.

- **AWS CLI**
- 
            
                    **Example 1: To attach a network interface to an instance**The following `attach-network-interface`example attaches the specified network interface to the specified instance.`aws ec2 attach-network-interface \ --network-interface-id``eni-0dc56a8d4640ad10a`\ --instance-id`i-1234567890abcdef0`\ --device-index`1`Output: `{ "AttachmentId": "eni-attach-01a8fc87363f07cf9" }`For more information, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)in the*Amazon EC2 User Guide*.**Example 2: To attach a network interface to an instance with multiple network cards**The following `attach-network-interface`example attaches the specified network interface to the specified instance and network card.`aws ec2 attach-network-interface \ --network-interface-id``eni-07483b1897541ad83`\ --instance-id`i-01234567890abcdef`\ --network-card-index`1`\ --device-index`1`Output: `{ "AttachmentId": "eni-attach-0fbd7ee87a88cd06c" }`For more information, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [AttachNetworkInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-network-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-verified-access-trust-provider`.

- **AWS CLI**
- 
            
                    **To attach a trust provider to an instance**The following `attach-verified-access-trust-provider`example attaches the specified Verified Access trust provider to the specified Verified Access instance.`aws ec2 attach-verified-access-trust-provider \ --verified-access-instance-id``vai-0ce000c0b7643abea`\ --verified-access-trust-provider-id`vatp-0bb32de759a3e19e7`Output: `{ "VerifiedAccessTrustProvider": { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "Description": "", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center", "PolicyReferenceName": "idc", "CreationTime": "2023-08-25T19:00:38", "LastUpdatedTime": "2023-08-25T19:00:38" }, "VerifiedAccessInstance": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "", "VerifiedAccessTrustProviders": [ { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center" } ], "CreationTime": "2023-08-25T18:27:56", "LastUpdatedTime": "2023-08-25T18:27:56" } }`For more information, see [Verified Access instances](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-instances.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [AttachVerifiedAccessTrustProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-verified-access-trust-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-volume`.

- **AWS CLI**
- 
            
                    **To attach a volume to an instance**This example command attaches a volume ( `vol-1234567890abcdef0`) to an instance (`i-01474ef662b89480`) as`/dev/sdf`.Command: `aws ec2 attach-volume --volume-id``vol-1234567890abcdef0`--instance-id`i-01474ef662b89480`--device`/dev/sdf`Output: `{ "AttachTime": "YYYY-MM-DDTHH:MM:SS.000Z", "InstanceId": "i-01474ef662b89480", "VolumeId": "vol-1234567890abcdef0", "State": "attaching", "Device": "/dev/sdf" }`- 
                    For API details, see [AttachVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-volume.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-vpn-gateway`.

- **AWS CLI**
- 
            
                    **To attach a virtual private gateway to your VPC**The following `attach-vpn-gateway`example attaches the specified virtual private gateway to the specified VPC.`aws ec2 attach-vpn-gateway \ --vpn-gateway-id``vgw-9a4cacf3`\ --vpc-id`vpc-a01106c2`Output: `{ "VpcAttachment": { "State": "attaching", "VpcId": "vpc-a01106c2" } }`- 
                    For API details, see [AttachVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-vpn-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `authorize-client-vpn-ingress`.

- **AWS CLI**
- 
            
                    **To add an authorization rule for a Client VPN endpoint**The following `authorize-client-vpn-ingress`example adds an ingress authorization rule that permits all clients to access the internet (`0.0.0.0/0`).`aws ec2 authorize-client-vpn-ingress \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --target-network-cidr`0.0.0.0/0`\ --authorize-all-groupsOutput: `{ "Status": { "Code": "authorizing" } }`For more information, see [Authorization Rules](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [AuthorizeClientVpnIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/authorize-client-vpn-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `authorize-security-group-egress`.

- **AWS CLI**
- 
            
                    **Example 1: To add a rule that allows outbound traffic to a specific address range**The following `authorize-security-group-egress`example adds a rule that grants access to the specified address ranges on TCP port 80.`aws ec2 authorize-security-group-egress \ --group-id``sg-1234567890abcdef0`\ --ip-permissions '`IpProtocol=tcp,FromPort=80,ToPort=80,IpRanges=[{CidrIp=10.0.0.0/16}]`'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-0b15794cdb17bf29c", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": true, "IpProtocol": "tcp", "FromPort": 80, "ToPort": 80, "CidrIpv4": "10.0.0.0/16" } ] }`**Example 2: To add a rule that allows outbound traffic to a specific security group**The following `authorize-security-group-egress`example adds a rule that grants access to the specified security group on TCP port 80.`aws ec2 authorize-security-group-egress \ --group-id``sg-1234567890abcdef0`\ --ip-permissions '`IpProtocol=tcp,FromPort=80,ToPort=80,UserIdGroupPairs=[{GroupId=sg-0aad1c26bbeec5c22}]`'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-0b5dd815afcea9cc3", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": true, "IpProtocol": "tcp", "FromPort": 80, "ToPort": 80, "ReferencedGroupInfo": { "GroupId": "sg-0aad1c26bbeec5c22", "UserId": "123456789012" } } ] }`For more information, see [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [AuthorizeSecurityGroupEgress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/authorize-security-group-egress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `authorize-security-group-ingress`.

- **AWS CLI**
- 
            
                    **Example 1: To add a rule that allows inbound SSH traffic**The following `authorize-security-group-ingress`example adds a rule that allows inbound traffic on TCP port 22 (SSH).`aws ec2 authorize-security-group-ingress \ --group-id``sg-1234567890abcdef0`\ --protocol`tcp`\ --port`22`\ --cidr`203.0.113.0/24`Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-01afa97ef3e1bedfc", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "CidrIpv4": "203.0.113.0/24" } ] }`**Example 2: To add a rule that allows inbound HTTP traffic from another security group**The following `authorize-security-group-ingress`example adds a rule that allows inbound access on TCP port 80 from the source security group`sg-1a2b3c4d`. The source group must be in the same VPC or in a peer VPC (requires a VPC peering connection). Incoming traffic is allowed based on the private IP addresses of instances that are associated with the source security group (not the public IP address or Elastic IP address).`aws ec2 authorize-security-group-ingress \ --group-id``sg-1234567890abcdef0`\ --protocol`tcp`\ --port`80`\ --source-group`sg-1a2b3c4d`Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-01f4be99110f638a7", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "tcp", "FromPort": 80, "ToPort": 80, "ReferencedGroupInfo": { "GroupId": "sg-1a2b3c4d", "UserId": "123456789012" } } ] }`**Example 3: To add multiple rules in the same call**The following `authorize-security-group-ingress`example uses the`ip-permissions`parameter to add two inbound rules, one that enables inbound access on TCP port 3389 (RDP) and the other that enables ping/ICMP.`aws ec2 authorize-security-group-ingress \ --group-id``sg-1234567890abcdef0`\ --ip-permissions '`IpProtocol=tcp,FromPort=3389,ToPort=3389,IpRanges=[{CidrIp=172.31.0.0/16}]`' '`IpProtocol=icmp,FromPort=-1,ToPort=-1,IpRanges=[{CidrIp=172.31.0.0/16}]`'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-00e06e5d3690f29f3", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "tcp", "FromPort": 3389, "ToPort": 3389, "CidrIpv4": "172.31.0.0/16" }, { "SecurityGroupRuleId": "sgr-0a133dd4493944b87", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "tcp", "FromPort": -1, "ToPort": -1, "CidrIpv4": "172.31.0.0/16" } ] }`**Example 4: To add a rule for ICMP traffic**The following `authorize-security-group-ingress`example uses the`ip-permissions`parameter to add an inbound rule that allows the ICMP message`Destination Unreachable: Fragmentation Needed and Don't Fragment was Set`(Type 3, Code 4) from anywhere.`aws ec2 authorize-security-group-ingress \ --group-id``sg-1234567890abcdef0`\ --ip-permissions '`IpProtocol=icmp,FromPort=3,ToPort=4,IpRanges=[{CidrIp=0.0.0.0/0}]`'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-0de3811019069b787", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "icmp", "FromPort": 3, "ToPort": 4, "CidrIpv4": "0.0.0.0/0" } ] }`**Example 5: To add a rule for IPv6 traffic**The following `authorize-security-group-ingress`example uses the`ip-permissions`parameter to add an inbound rule that allows SSH access (port 22) from the IPv6 range`2001:db8:1234:1a00::/64`.`aws ec2 authorize-security-group-ingress \ --group-id``sg-1234567890abcdef0`\ --ip-permissions '`IpProtocol=tcp,FromPort=22,ToPort=22,Ipv6Ranges=[{CidrIpv6=2001:db8:1234:1a00::/64}]`'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-0455bc68b60805563", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "tcp", "FromPort": 22, "ToPort": 22, "CidrIpv6": "2001:db8:1234:1a00::/64" } ] }`**Example 6: To add a rule for ICMPv6 traffic**The following `authorize-security-group-ingress`example uses the`ip-permissions`parameter to add an inbound rule that allows ICMPv6 traffic from anywhere.`aws ec2 authorize-security-group-ingress \ --group-id``sg-1234567890abcdef0`\ --ip-permissions '`IpProtocol=icmpv6,Ipv6Ranges=[{CidrIpv6=::/0}]`'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-04b612d9363ab6327", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "icmpv6", "FromPort": -1, "ToPort": -1, "CidrIpv6": "::/0" } ] }`**Example 7: Add a rule with a description**The following `authorize-security-group-ingress`example uses the`ip-permissions`parameter to add an inbound rule that allows RDP traffic from the specified IPv4 address range. The rule includes a description to help you identify it later.`aws ec2 authorize-security-group-ingress \ --group-id``sg-1234567890abcdef0`\ --ip-permissions 'IpProtocol=tcp,FromPort=3389,ToPort=3389,IpRanges=[{CidrIp=203.0.113.0/24,Description='RDP`access``from``NY`office'}]'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-0397bbcc01e974db3", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "tcp", "FromPort": 3389, "ToPort": 3389, "CidrIpv4": "203.0.113.0/24", "Description": "RDP access from NY office" } ] }`**Example 8: To add an inbound rule that uses a prefix list**The following `authorize-security-group-ingress`example uses the`ip-permissions`parameter to add an inbound rule that allows all traffic for the CIDR ranges in the specified prefix list.`aws ec2 authorize-security-group-ingress \ --group-id``sg-04a351bfe432d4e71`\ --ip-permissions '`IpProtocol=all,PrefixListIds=[{PrefixListId=pl-002dc3ec097de1514}]`'Output: `{ "Return": true, "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-09c74b32f677c6c7c", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "123456789012", "IsEgress": false, "IpProtocol": "-1", "FromPort": -1, "ToPort": -1, "PrefixListId": "pl-0721453c7ac4ec009" } ] }`For more information, see [Security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [AuthorizeSecurityGroupIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/authorize-security-group-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `bundle-instance`.

- **AWS CLI**
- 
            
                    **To bundle an instance**This example bundles instance `i-1234567890abcdef0`to a bucket called`bundletasks`. Before you specify values for your access key IDs, review and follow the guidance in Best Practices for Managing AWS Access Keys.Command: `aws ec2 bundle-instance --instance-id``i-1234567890abcdef0`--bucket`bundletasks`--prefix`winami`--owner-akid`AK12AJEXAMPLE`--owner-sak`example123example`Output: `{ "BundleTask": { "UpdateTime": "2015-09-15T13:30:35.000Z", "InstanceId": "i-1234567890abcdef0", "Storage": { "S3": { "Prefix": "winami", "Bucket": "bundletasks" } }, "State": "pending", "StartTime": "2015-09-15T13:30:35.000Z", "BundleId": "bun-294e041f" } }`- 
                    For API details, see [BundleInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/bundle-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-bundle-task`.

- **AWS CLI**
- 
            
                    **To cancel a bundle task**This example cancels bundle task `bun-2a4e041c`.Command: `aws ec2 cancel-bundle-task --bundle-id``bun-2a4e041c`Output: `{ "BundleTask": { "UpdateTime": "2015-09-15T13:27:40.000Z", "InstanceId": "i-1234567890abcdef0", "Storage": { "S3": { "Prefix": "winami", "Bucket": "bundletasks" } }, "State": "cancelling", "StartTime": "2015-09-15T13:24:35.000Z", "BundleId": "bun-2a4e041c" } }`- 
                    For API details, see [CancelBundleTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-bundle-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-capacity-reservation-fleets`.

- **AWS CLI**
- 
            
                    **To cancel a Capacity Reservation Fleet**The following `cancel-capacity-reservation-fleets`example cancels the specified Capacity Reservation Fleet and the capacity it reserves. When you cancel a Fleet, its status changes to`cancelled`, and it can no longer create new Capacity Reservations. Additionally, all of the individual Capacity Reservations in the Fleet are cancelled, and the instances that were previously running in the reserved capacity continue to run normally in shared capacity.`aws ec2 cancel-capacity-reservation-fleets \ --capacity-reservation-fleet-ids``crf-abcdef01234567890`Output: `{ "SuccessfulFleetCancellations": [ { "CurrentFleetState": "cancelling", "PreviousFleetState": "active", "CapacityReservationFleetId": "crf-abcdef01234567890" } ], "FailedFleetCancellations": [] }`For more information about Capacity Reservation Fleets, see [Capacity Reservation Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CancelCapacityReservationFleets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation-fleets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-capacity-reservation`.

- **AWS CLI**
- 
            
                    **To cancel a capacity reservation**The following `cancel-capacity-reservation`example cancels the specified capacity reservation.`aws ec2 cancel-capacity-reservation \ --capacity-reservation-id``cr-1234abcd56EXAMPLE`Output: `{ "Return": true }`For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CancelCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-capacity-reservation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-conversion-task`.

- **AWS CLI**
- 
            
                    **To cancel an active conversion of an instance or a volume**This example cancels the upload associated with the task ID import-i-fh95npoc. If the command succeeds, no output is returned. Command: `aws ec2 cancel-conversion-task --conversion-task-id``import-i-fh95npoc`- 
                    For API details, see [CancelConversionTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-conversion-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-export-task`.

- **AWS CLI**
- 
            
                    **To cancel an active export task**This example cancels an active export task with the task ID export-i-fgelt0i7. If the command succeeds, no output is returned. Command: `aws ec2 cancel-export-task --export-task-id``export-i-fgelt0i7`- 
                    For API details, see [CancelExportTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-export-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-image-launch-permission`.

- **AWS CLI**
- 
            
                    **To cancel having an AMI shared with your Amazon Web Services account**The following `cancel-image-launch-permission`example removes your account from the specified AMI's launch permissions.`aws ec2 cancel-image-launch-permission \ --image-id``ami-0123456789example`\ --region`us-east-1`Output: `{ "Return": true }`For more information, see [Cancel having an AMI shared with your Amazon Web Services account](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-sharing-an-AMI.html#cancel-image-launch-permission)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CancelImageLaunchPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-image-launch-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-import-task`.

- **AWS CLI**
- 
            
                    **To cancel an import task**The following `cancel-import-task`example cancels the specified import image task.`aws ec2 cancel-import-task \ --import-task-id``import-ami-1234567890abcdef0`Output: `{ "ImportTaskId": "import-ami-1234567890abcdef0", "PreviousState": "active", "State": "deleting" }`- 
                    For API details, see [CancelImportTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-import-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-reserved-instances-listing`.

- **AWS CLI**
- 
            
                    **To cancel a Reserved Instance listing**The following `cancel-reserved-instances-listing`example cancels the specified Reserved Instance listing.`aws ec2 cancel-reserved-instances-listing \ --reserved-instances-listing-id``5ec28771-05ff-4b9b-aa31-9e57dexample`- 
                    For API details, see [CancelReservedInstancesListing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-reserved-instances-listing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-spot-fleet-requests`.

- **AWS CLI**
- 
            
                    **Example 1: To cancel a Spot fleet request and terminate the associated instances**The following `cancel-spot-fleet-requests`example cancels a Spot Fleet request and terminates the associated On-Demand Instances and Spot Instances.`aws ec2 cancel-spot-fleet-requests \ --spot-fleet-request-ids``sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`\ --terminate-instancesOutput: `{ "SuccessfulFleetRequests": [ { "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "CurrentSpotFleetRequestState": "cancelled_terminating", "PreviousSpotFleetRequestState": "active" } ], "UnsuccessfulFleetRequests": [] }`**Example 2: To cancel a Spot fleet request without terminating the associated instances**The following `cancel-spot-fleet-requests`example cancels a Spot Fleet request without terminating the associated On-Demand Instances and Spot Instances.`aws ec2 cancel-spot-fleet-requests \ --spot-fleet-request-ids``sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`\ --no-terminate-instancesOutput: `{ "SuccessfulFleetRequests": [ { "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "CurrentSpotFleetRequestState": "cancelled_running", "PreviousSpotFleetRequestState": "active" } ], "UnsuccessfulFleetRequests": [] }`For more information, see [Cancel a Spot Fleet request](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cancel-spot-fleet.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CancelSpotFleetRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-fleet-requests.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-spot-instance-requests`.

- **AWS CLI**
- 
            
                    **To cancel Spot Instance requests**This example command cancels a Spot Instance request. Command: `aws ec2 cancel-spot-instance-requests --spot-instance-request-ids``sir-08b93456`Output: `{ "CancelledSpotInstanceRequests": [ { "State": "cancelled", "SpotInstanceRequestId": "sir-08b93456" } ] }`- 
                    For API details, see [CancelSpotInstanceRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/cancel-spot-instance-requests.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-product-instance`.

- **AWS CLI**
- 
            
                    **To confirm the product instance**This example determines whether the specified product code is associated with the specified instance. Command: `aws ec2 confirm-product-instance --product-code``774F4FF8`--instance-id`i-1234567890abcdef0`Output: `{ "OwnerId": "123456789012" }`- 
                    For API details, see [ConfirmProductInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/confirm-product-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-fpga-image`.

- **AWS CLI**
- 
            
                    **To copy an Amazon FPGA image**This example copies the specified AFI from the `us-east-1`region to the current region (`eu-west-1`).Command: `aws ec2 copy-fpga-image --name``copy-afi`--source-fpga-image-id`afi-0d123e123bfc85abc`--source-region`us-east-1`--region`eu-west-1`Output: `{ "FpgaImageId": "afi-06b12350a123fbabc" }`- 
                    For API details, see [CopyFpgaImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-fpga-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-image`.

- **AWS CLI**
- 
            
                    **Example 1: To copy an AMI to another Region**The following `copy-image`example command copies the specified AMI from the`us-west-2`Region to the`us-east-1`Region and adds a short description.`aws ec2 copy-image \ --region``us-east-1`\ --name`ami-name`\ --source-region`us-west-2`\ --source-image-id`ami-066877671789bd71b`\ --description`"This is my copied image."`Output: `{ "ImageId": "ami-0123456789abcdefg" }`For more information, see [Copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)in the*Amazon EC2 User Guide*.**Example 2: To copy an AMI to another Region and encrypt the backing snapshot**The following `copy-image`command copies the specified AMI from the`us-west-2`Region to the current Region and encrypts the backing snapshot using the specified KMS key.`aws ec2 copy-image \ --source-region``us-west-2`\ --name`ami-name`\ --source-image-id`ami-066877671789bd71b`\ --encrypted \ --kms-key-id`alias/my-kms-key`Output: `{ "ImageId": "ami-0123456789abcdefg" }`For more information, see [Copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)in the*Amazon EC2 User Guide*.**Example 3: To include your user-defined AMI tags when copying an AMI**The following `copy-image`command uses the`--copy-image-tags`parameter to copy your user-defined AMI tags when copying the AMI.`aws ec2 copy-image \ --region``us-east-1`\ --name`ami-name`\ --source-region`us-west-2`\ --source-image-id`ami-066877671789bd71b`\ --description`"This is my copied image."`--copy-image-tagsOutput: `{ "ImageId": "ami-0123456789abcdefg" }`For more information, see [Copy an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/CopyingAMIs.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CopyImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-snapshot`.

- **AWS CLI**
- 
            
                    **Example 1: To copy a snapshot to another Region**The following `copy-snapshot`example command copies the specified snapshot from the`us-west-2`Region to the`us-east-1`Region and adds a short description.`aws ec2 copy-snapshot \ --region``us-east-1`\ --source-region`us-west-2`\ --source-snapshot-id`snap-066877671789bd71b`\ --description '`This is my copied snapshot.`'Output: `{ "SnapshotId": "snap-066877671789bd71b" }`**Example 2: To copy an unencrypted snapshot and encrypt the new snapshot**The following `copy-snapshot`command copies the specified unencrypted snapshot from the`us-west-2`Region to the current Region and encrypts the new snapshot using the specified KMS key.`aws ec2 copy-snapshot \ --source-region``us-west-2`\ --source-snapshot-id`snap-066877671789bd71b`\ --encrypted \ --kms-key-id`alias/my-kms-key`Output: `{ "SnapshotId": "snap-066877671789bd71b" }`For more information, see [Copy an Amazon EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-copy-snapshot.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [CopySnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-capacity-reservation-fleet`.

- **AWS CLI**
- 
            
                    **To create a Capacity Reservation Fleet**The following `create-capacity-reservation-fleet`example creates a Capacity Reservation Fleet for the instance type specified in the request, up to the specified total target capacity. The number of instances for which the Capacity Reservation Fleet reserves capacity depends on the total target capacity and instance type weights that you specify in the request. Specify the instance types to use and a priority for each of the designated instance types.`aws ec2 create-capacity-reservation-fleet \ --total-target-capacity``24`\ --allocation-strategy`prioritized`\ --instance-match-criteria`open`\ --tenancy`default`\ --end-date`2022-12-31T23:59:59.000Z`\ --instance-type-specifications`file://instanceTypeSpecification.json`Contents of `instanceTypeSpecification.json`:`[ { "InstanceType": "m5.xlarge", "InstancePlatform": "Linux/UNIX", "Weight": 3.0, "AvailabilityZone":"us-east-1a", "EbsOptimized": true, "Priority" : 1 } ]`Output: `{ "Status": "submitted", "TotalFulfilledCapacity": 0.0, "CapacityReservationFleetId": "crf-abcdef01234567890", "TotalTargetCapacity": 24 }`For more information about Capacity Reservation Fleets, see [Capacity Reservation Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html)in the*Amazon EC2 User Guide*.For more information about instance type weight and total target capacity, see [Instance type weight](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-weight)and[Total target capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#target-capacity)in the*Amazon EC2 User Guide*.For more information about designating priority for specified instance types, see [Allocation strategy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#allocation-strategy)and[Instance type priority](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/crfleet-concepts.html#instance-priority)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateCapacityReservationFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-capacity-reservation-fleet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-capacity-reservation`.

- **AWS CLI**
- 
            
                    **Example 1: To create a Capacity Reservation**The following `create-capacity-reservation`example creates a capacity reservation in the`eu-west-1a`Availability Zone, into which you can launch three`t2.medium`instances running a Linux/Unix operating system. By default, the capacity reservation is created with open instance matching criteria and no support for ephemeral storage, and it remains active until you manually cancel it.`aws ec2 create-capacity-reservation \ --availability-zone``eu-west-1a`\ --instance-type`t2.medium`\ --instance-platform`Linux/UNIX`\ --instance-count`3`Output: `{ "CapacityReservation": { "CapacityReservationId": "cr-1234abcd56EXAMPLE ", "EndDateType": "unlimited", "AvailabilityZone": "eu-west-1a", "InstanceMatchCriteria": "open", "EphemeralStorage": false, "CreateDate": "2019-08-16T09:27:35.000Z", "AvailableInstanceCount": 3, "InstancePlatform": "Linux/UNIX", "TotalInstanceCount": 3, "State": "active", "Tenancy": "default", "EbsOptimized": false, "InstanceType": "t2.medium" } }`**Example 2: To create a Capacity Reservation that automatically ends at a specified date/time**The following `create-capacity-reservation`example creates a capacity reservation in the`eu-west-1a`Availability Zone, into which you can launch three`m5.large`instances running a Linux/Unix operating system. This capacity reservation automatically ends on 08/31/2019 at 23:59:59.`aws ec2 create-capacity-reservation \ --availability-zone``eu-west-1a`\ --instance-type`m5.large`\ --instance-platform`Linux/UNIX`\ --instance-count`3`\ --end-date-type`limited`\ --end-date`2019-08-31T23:59:59Z`Output: `{ "CapacityReservation": { "CapacityReservationId": "cr-1234abcd56EXAMPLE ", "EndDateType": "limited", "AvailabilityZone": "eu-west-1a", "EndDate": "2019-08-31T23:59:59.000Z", "InstanceMatchCriteria": "open", "EphemeralStorage": false, "CreateDate": "2019-08-16T10:15:53.000Z", "AvailableInstanceCount": 3, "InstancePlatform": "Linux/UNIX", "TotalInstanceCount": 3, "State": "active", "Tenancy": "default", "EbsOptimized": false, "InstanceType": "m5.large" } }`**Example 3: To create a Capacity Reservation that accepts only targeted instance launches**The following `create-capacity-reservation`example creates a capacity reservation that accepts only targeted instance launches.`aws ec2 create-capacity-reservation \ --availability-zone``eu-west-1a`\ --instance-type`m5.large`\ --instance-platform`Linux/UNIX`\ --instance-count`3`\ --instance-match-criteria`targeted`Output: `{ "CapacityReservation": { "CapacityReservationId": "cr-1234abcd56EXAMPLE ", "EndDateType": "unlimited", "AvailabilityZone": "eu-west-1a", "InstanceMatchCriteria": "targeted", "EphemeralStorage": false, "CreateDate": "2019-08-16T10:21:57.000Z", "AvailableInstanceCount": 3, "InstancePlatform": "Linux/UNIX", "TotalInstanceCount": 3, "State": "active", "Tenancy": "default", "EbsOptimized": false, "InstanceType": "m5.large" } }`For more information, see [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-using.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-capacity-reservation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-carrier-gateway`.

- **AWS CLI**
- 
            
                    **To create a carrier gateway**The following `create-carrier-gateway`example creates a carrier gateway for the specified VPC.`aws ec2 create-carrier-gateway \ --vpc-id``vpc-0c529aEXAMPLE1111`Output: `{ "CarrierGateway": { "CarrierGatewayId": "cagw-0465cdEXAMPLE1111", "VpcId": "vpc-0c529aEXAMPLE1111", "State": "pending", "OwnerId": "123456789012" } }`For more information, see [Carrier gateways](https://docs.aws.amazon.com/wavelength/latest/developerguide/carrier-gateways.html)in the*AWS Wavelength User Guide*.- 
                    For API details, see [CreateCarrierGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-carrier-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-client-vpn-endpoint`.

- **AWS CLI**
- 
            
                    **To create a Client VPN endpoint**The following `create-client-vpn-endpoint`example creates a Client VPN endpoint that uses mutual authentication and specifies a value for the client CIDR block.`aws ec2 create-client-vpn-endpoint \ --client-cidr-block``"172.31.0.0/16"`\ --server-certificate-arn`arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE`\ --authentication-options`Type=certificate-authentication,MutualAuthentication={ClientRootCertificateChainArn=arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE}`\ --connection-log-options`Enabled=false`Output: `{ "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "Status": { "Code": "pending-associate" }, "DnsName": "cvpn-endpoint-123456789123abcde.prod.clientvpn.ap-south-1.amazonaws.com" }`For more information, see [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [CreateClientVpnEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-client-vpn-route`.

- **AWS CLI**
- 
            
                    **To create a route for a Client VPN endpoint**The following `create-client-vpn-route`example adds a route to the internet (`0.0.0.0/0`) for the specified subnet of the Client VPN endpoint.`aws ec2 create-client-vpn-route \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --destination-cidr-block`0.0.0.0/0`\ --target-vpc-subnet-id`subnet-0123456789abcabca`Output: `{ "Status": { "Code": "creating" } }`For more information, see [Routes](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [CreateClientVpnRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-client-vpn-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-coip-cidr`.

- **AWS CLI**
- 
            
                    **To create a range of customer-owned IP (CoIP) addresses**The following `create-coip-cidr`example creates the specified range of CoIP addresses in the specified CoIP pool.`aws ec2 create-coip-cidr \ --cidr``15.0.0.0/24`\ --coip-pool-id`ipv4pool-coip-1234567890abcdefg`Output: `{ "CoipCidr": { "Cidr": "15.0.0.0/24", "CoipPoolId": "ipv4pool-coip-1234567890abcdefg", "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890" } }`For more information, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing)in the*AWS Outposts User Guide*.- 
                    For API details, see [CreateCoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-coip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-coip-pool`.

- **AWS CLI**
- 
            
                    **To create a pool of customer-owned IP (CoIP) addresses**The following `create-coip-pool`example creates a CoIP pool for CoIP addresses in the specified local gateway route table.`aws ec2 create-coip-pool \ --local-gateway-route-table-id``lgw-rtb-abcdefg1234567890`Output: `{ "CoipPool": { "PoolId": "ipv4pool-coip-1234567890abcdefg", "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890", "PoolArn": "arn:aws:ec2:us-west-2:123456789012:coip-pool/ipv4pool-coip-1234567890abcdefg" } }`For more information, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing)in the*AWS Outposts User Guide*.- 
                    For API details, see [CreateCoipPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-coip-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-customer-gateway`.

- **AWS CLI**
- 
            
                    **To create a customer gateway**This example creates a customer gateway with the specified IP address for its outside interface. Command: `aws ec2 create-customer-gateway --type``ipsec.1`--public-ip`12.1.2.3`--bgp-asn`65534`Output: `{ "CustomerGateway": { "CustomerGatewayId": "cgw-0e11f167", "IpAddress": "12.1.2.3", "State": "available", "Type": "ipsec.1", "BgpAsn": "65534" } }`- 
                    For API details, see [CreateCustomerGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-customer-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-default-subnet`.

- **AWS CLI**
- 
            
                    **To create a default subnet**This example creates a default subnet in Availability Zone `us-east-2a`.Command: `aws ec2 create-default-subnet --availability-zone us-east-2a { "Subnet": { "AvailabilityZone": "us-east-2a", "Tags": [], "AvailableIpAddressCount": 4091, "DefaultForAz": true, "Ipv6CidrBlockAssociationSet": [], "VpcId": "vpc-1a2b3c4d", "State": "available", "MapPublicIpOnLaunch": true, "SubnetId": "subnet-1122aabb", "CidrBlock": "172.31.32.0/20", "AssignIpv6AddressOnCreation": false } }`- 
                    For API details, see [CreateDefaultSubnet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-default-subnet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-default-vpc`.

- **AWS CLI**
- 
            
                    **To create a default VPC**This example creates a default VPC. Command: `aws ec2 create-default-vpc`Output: `{ "Vpc": { "VpcId": "vpc-8eaae5ea", "InstanceTenancy": "default", "Tags": [], "Ipv6CidrBlockAssociationSet": [], "State": "pending", "DhcpOptionsId": "dopt-af0c32c6", "CidrBlock": "172.31.0.0/16", "IsDefault": true } }`- 
                    For API details, see [CreateDefaultVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-default-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-dhcp-options`.

- **AWS CLI**
- 
            
                    **To create a set of DHCP options**The following `create-dhcp-options`example creates a set of DHCP options that specifies the domain name, the domain name servers, and the NetBIOS node type.`aws ec2 create-dhcp-options \ --dhcp-configuration \``"Key=domain-name-servers,Values=10.2.5.1,10.2.5.2"`\`"Key=domain-name,Values=example.com"`\`"Key=netbios-node-type,Values=2"`Output: `{ "DhcpOptions": { "DhcpConfigurations": [ { "Key": "domain-name", "Values": [ { "Value": "example.com" } ] }, { "Key": "domain-name-servers", "Values": [ { "Value": "10.2.5.1" }, { "Value": "10.2.5.2" } ] }, { "Key": "netbios-node-type", "Values": [ { "Value": "2" } ] } ], "DhcpOptionsId": "dopt-06d52773eff4c55f3" } }`- 
                    For API details, see [CreateDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-dhcp-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-egress-only-internet-gateway`.

- **AWS CLI**
- 
            
                    **To create an egress-only Internet gateway**This example creates an egress-only Internet gateway for the specified VPC. Command: `aws ec2 create-egress-only-internet-gateway --vpc-id``vpc-0c62a468`Output: `{ "EgressOnlyInternetGateway": { "EgressOnlyInternetGatewayId": "eigw-015e0e244e24dfe8a", "Attachments": [ { "State": "attached", "VpcId": "vpc-0c62a468" } ] } }`- 
                    For API details, see [CreateEgressOnlyInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-egress-only-internet-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-fleet`.

- **AWS CLI**
- 
            
                    **Example 1: To create an EC2 Fleet that launches Spot Instances as the default purchasing model**The following `create-fleet`example creates an EC2 Fleet using the minimum parameters required to launch a fleet: a launch template, target capacity, and default purchasing model. The launch template is identified by its launch template ID and version number. The target capacity for the fleet is 2 instances, and the default purchasing model is`spot`, which results in the fleet launching 2 Spot Instances.When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch. `aws ec2 create-fleet \ --cli-input-json``file://file_name.json`Contents of file_name.json: `{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-0e8c754449b27161c", "Version": "1" } } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 2, "DefaultTargetCapacityType": "spot" } }`Output: `{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE" }`**Example 2: To create an EC2 Fleet that launches On-Demand Instances as the default purchasing model**The following `create-fleet`example creates an EC2 Fleet using the minimum parameters required to launch a fleet: a launch template, target capacity, and default purchasing model. The launch template is identified by its launch template ID and version number. The target capacity for the fleet is 2 instances, and the default purchasing model is`on-demand`, which results in the fleet launching 2 On-Demand Instances.When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch. `aws ec2 create-fleet \ --cli-input-json``file://file_name.json`Contents of file_name.json: `{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-0e8c754449b27161c", "Version": "1" } } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 2, "DefaultTargetCapacityType": "on-demand" } }`Output: `{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE" }`**Example 3: To create an EC2 Fleet that launches On-Demand Instances as the primary capacity**The following `create-fleet`example creates an EC2 Fleet that specifies the total target capacity of 2 instances for the fleet, and a target capacity of 1 On-Demand Instance. The default purchasing model is`spot`. The fleet launches 1 On-Demand Instance as specified, but needs to launch one more instance to fulfil the total target capacity. The purchasing model for the difference is calculated as`TotalTargetCapacity`-`OnDemandTargetCapacity`=`DefaultTargetCapacityType`, which results in the fleet launching 1 Spot Instance.When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch. `aws ec2 create-fleet \ --cli-input-json``file://file_name.json`Contents of file_name.json: `{ "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-0e8c754449b27161c", "Version": "1" } } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 2, "OnDemandTargetCapacity":1, "DefaultTargetCapacityType": "spot" } }`Output: `{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE" }`**Example 4: To create an EC2 Fleet that launches Spot Instances using the lowest-price allocation strategy**If the allocation strategy for Spot Instances is not specified, the default allocation strategy, which is `lowest-price`, is used. The following`create-fleet`example creates an EC2 Fleet using the`lowest-price`allocation strategy. The three launch specifications, which override the launch template, have different instance types but the same weighted capacity and subnet. The total target capacity is 2 instances and the default purchasing model is`spot`. The EC2 Fleet launches 2 Spot Instances using the instance type of the launch specification with the lowest price.When you create an EC2 Fleet, use a JSON file to specify information about the instances to launch. `aws ec2 create-fleet \ --cli-input-json``file://file_name.jsonContents``of``file_name.json::``{`"LaunchTemplateConfigs":`[``{`"LaunchTemplateSpecification":`{`"LaunchTemplateId": "lt-0e8c754449b27`1`61c", "Version": "1"`},`"Overrides":`[``{`"InstanceType": "c4.large", "WeightedCapacity":`1,`"SubnetId":`"subnet-a4f6c5d3"``},``{`"InstanceType": "c3.large", "WeightedCapacity":`1,`"SubnetId":`"subnet-a4f6c5d3"``},``{`"InstanceType": "c5.large", "WeightedCapacity":`1,`"SubnetId":`"subnet-a4f6c5d3"``}``]``}``],`"TargetCapacitySpecification":`{`"TotalTargetCapacity":`2,`"DefaultTargetCapacityType":`"spot"``}``}`Output: `{ "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE" }`- 
                    For API details, see [CreateFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fleet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-flow-logs`.

- **AWS CLI**
- 
            
                    **Example 1: To create a flow log**The following `create-flow-logs`example creates a flow log that captures all rejected traffic for the specified network interface. The flow logs are delivered to a log group in CloudWatch Logs using the permissions in the specified IAM role.`aws ec2 create-flow-logs \ --resource-type``NetworkInterface`\ --resource-ids`eni-11223344556677889`\ --traffic-type`REJECT`\ --log-group-name`my-flow-logs`\ --deliver-logs-permission-arn`arn:aws:iam::123456789101:role/publishFlowLogs`Output: `{ "ClientToken": "so0eNA2uSHUNlHI0S2cJ305GuIX1CezaRdGtexample", "FlowLogIds": [ "fl-12345678901234567" ], "Unsuccessful": [] }`For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)in the*Amazon VPC User Guide*.**Example 2: To create a flow log with a custom format**The following `create-flow-logs`example creates a flow log that captures all traffic for the specified VPC and delivers the flow logs to an Amazon S3 bucket. The`--log-format`parameter specifies a custom format for the flow log records. To run this command on Windows, change the single quotes (') to double quotes (").`aws ec2 create-flow-logs \ --resource-type``VPC`\ --resource-ids`vpc-00112233344556677`\ --traffic-type`ALL`\ --log-destination-type`s3`\ --log-destination`arn:aws:s3:::flow-log-bucket/my-custom-flow-logs/`\ --log-format '`${version} ${vpc-id} ${subnet-id} ${instance-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${tcp-flags} ${type} ${pkt-srcaddr} ${pkt-dstaddr}`'For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)in the*Amazon VPC User Guide*.**Example 3: To create a flow log with a one-minute maximum aggregation interval**The following `create-flow-logs`example creates a flow log that captures all traffic for the specified VPC and delivers the flow logs to an Amazon S3 bucket. The`--max-aggregation-interval`parameter specifies a maximum aggregation interval of 60 seconds (1 minute).`aws ec2 create-flow-logs \ --resource-type``VPC`\ --resource-ids`vpc-00112233344556677`\ --traffic-type`ALL`\ --log-destination-type`s3`\ --log-destination`arn:aws:s3:::flow-log-bucket/my-custom-flow-logs/`\ --max-aggregation-interval`60`For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [CreateFlowLogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-flow-logs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-fpga-image`.

- **AWS CLI**
- 
            
                    **To create an Amazon FPGA image**This example creates an AFI from the specified tarball in the specified bucket. Command: `aws ec2 create-fpga-image --name``my-afi`--description`test-afi`--input-storage-location`Bucket=my-fpga-bucket,Key=dcp/17_12_22-103226.Developer_CL.tar`--logs-storage-location`Bucket=my-fpga-bucket,Key=logs`Output: `{ "FpgaImageId": "afi-0d123e123bfc85abc", "FpgaImageGlobalId": "agfi-123cb27b5e84a0abc" }`- 
                    For API details, see [CreateFpgaImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-fpga-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-image`.

- **AWS CLI**
- 
            
                    **Example 1: To create an AMI from an Amazon EBS-backed instance**The following `create-image`example creates an AMI from the specified instance.`aws ec2 create-image \ --instance-id``i-1234567890abcdef0`\ --name`"My server"`\ --description`"An AMI for my server"`Output: `{ "ImageId": "ami-abcdef01234567890" }`For more information about specifying a block device mapping for your AMI, see [Specifying a block device mapping for an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#create-ami-bdm)in the*Amazon EC2 User Guide*.**Example 2: To create an AMI from an Amazon EBS-backed instance without reboot**The following `create-image`example creates an AMI and sets the --no-reboot parameter, so that the instance is not rebooted before the image is created.`aws ec2 create-image \ --instance-id``i-1234567890abcdef0`\ --name`"My server"`\ --no-rebootOutput: `{ "ImageId": "ami-abcdef01234567890" }`For more information about specifying a block device mapping for your AMI, see [Specifying a block device mapping for an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html#create-ami-bdm)in the*Amazon EC2 User Guide*.**Example 3: To tag an AMI and snapshots on creation**The following `create-image`example creates an AMI, and tags the AMI and the snapshots with the same tag`cost-center=cc123``aws ec2 create-image \ --instance-id``i-1234567890abcdef0`\ --name`"My server"`\ --tag-specifications`"ResourceType=image,Tags=[{Key=cost-center,Value=cc123}]"``"ResourceType=snapshot,Tags=[{Key=cost-center,Value=cc123}]"`Output: `{ "ImageId": "ami-abcdef01234567890" }`For more information about tagging your resources on creation, see [Add tags on resource creation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-on-create-examples)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-instance-connect-endpoint`.

- **AWS CLI**
- 
            
                    **To create an EC2 Instance Connect Endpoint**The following `create-instance-connect-endpoint`example creates an EC2 Instance Connect Endpoint in the specified subnet.`aws ec2 create-instance-connect-endpoint \ --region``us-east-1`\ --subnet-id`subnet-0123456789example`Output: `{ "VpcId": "vpc-0123abcd", "InstanceConnectEndpointArn": "arn:aws:ec2:us-east-1:111111111111:instance-connect-endpoint/eice-0123456789example", "AvailabilityZone": "us-east-1a", "NetworkInterfaceIds": [ "eni-0123abcd" ], "PreserveClientIp": true, "Tags": [], "FipsDnsName": "eice-0123456789example.0123abcd.fips.ec2-instance-connect-endpoint.us-east-1.amazonaws.com", "StateMessage": "", "State": "create-complete", "DnsName": "eice-0123456789example.0123abcd.ec2-instance-connect-endpoint.us-east-1.amazonaws.com", "SubnetId": "subnet-0123abcd", "OwnerId": "111111111111", "SecurityGroupIds": [ "sg-0123abcd" ], "InstanceConnectEndpointId": "eice-0123456789example", "CreatedAt": "2023-04-07T15:43:53.000Z" }`For more information, see [Create an EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-instance-connect-endpoints.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateInstanceConnectEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-instance-connect-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-instance-event-window`.

- **AWS CLI**
- 
            
                    **Example 1: To create an event window with a time range**The following `create-instance-event-window`example creates an event window with a time range. You can't also specify the`cron-expression`parameter.`aws ec2 create-instance-event-window \ --region``us-east-1`\ --time-range`StartWeekDay=monday,StartHour=2,EndWeekDay=wednesday,EndHour=8`\ --tag-specifications`"ResourceType=instance-event-window,Tags=[{Key=K1,Value=V1}]"`\ --name`myEventWindowName`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "TimeRanges": [ { "StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8 } ], "Name": "myEventWindowName", "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1" } ] } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 2: To create an event window with a cron expression**The following `create-instance-event-window`example creates an event window with a cron expression. You can't also specify the`time-range`parameter.`aws ec2 create-instance-event-window \ --region``us-east-1`\ --cron-expression`"* 21-23 * * 2,3"`\ --tag-specifications`"ResourceType=instance-event-window,Tags=[{Key=K1,Value=V1}]"`\ --name`myEventWindowName`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1" } ] } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateInstanceEventWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-instance-event-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-instance-export-task`.

- **AWS CLI**
- 
            
                    **To export an instance**This example command creates a task to export the instance i-1234567890abcdef0 to the Amazon S3 bucket myexportbucket. Command: `aws ec2 create-instance-export-task --description``"RHEL5 instance"`--instance-id`i-1234567890abcdef0`--target-environment`vmware`--export-to-s3-task`DiskImageFormat=vmdk,ContainerFormat=ova,S3Bucket=myexportbucket,S3Prefix=RHEL5`Output: `{ "ExportTask": { "State": "active", "InstanceExportDetails": { "InstanceId": "i-1234567890abcdef0", "TargetEnvironment": "vmware" }, "ExportToS3Task": { "S3Bucket": "myexportbucket", "S3Key": "RHEL5export-i-fh8sjjsq.ova", "DiskImageFormat": "vmdk", "ContainerFormat": "ova" }, "Description": "RHEL5 instance", "ExportTaskId": "export-i-fh8sjjsq" } }`- 
                    For API details, see [CreateInstanceExportTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-instance-export-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-internet-gateway`.

- **AWS CLI**
- 
            
                    **To create an internet gateway**The following `create-internet-gateway`example creates an internet gateway with the tag`Name=my-igw`.`aws ec2 create-internet-gateway \ --tag-specifications``ResourceType=internet-gateway,Tags=[{Key=Name,Value=my-igw}]`Output: `{ "InternetGateway": { "Attachments": [], "InternetGatewayId": "igw-0d0fb496b3994d755", "OwnerId": "123456789012", "Tags": [ { "Key": "Name", "Value": "my-igw" } ] } }`For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [CreateInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-internet-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ipam-pool`.

- **AWS CLI**
- 
            
                    **To create an IPAM pool**The following `create-ipam-pool`example creates an IPAM pool.(Linux): `aws ec2 create-ipam-pool \ --ipam-scope-id``ipam-scope-02fc38cd4c48e7d38`\ --address-family`ipv4`\ --auto-import \ --allocation-min-netmask-length`16`\ --allocation-max-netmask-length`26`\ --allocation-default-netmask-length`24`\ --allocation-resource-tags`"Key=Environment,Value=Preprod"`\ --tag-specifications '`ResourceType=ipam-pool,Tags=[{Key=Name,Value="Preprod pool"}]`'(Windows): `aws ec2 create-ipam-pool``^`--ipam-scope-id`ipam-scope-02fc38cd4c48e7d38``^`--address-family`ipv4``^`--auto-import`^`--allocation-min-netmask-length`16``^`--allocation-max-netmask-length`26``^`--allocation-default-netmask-length`24``^`--allocation-resource-tags`"Key=Environment,Value=Preprod"``^`--tag-specifications ResourceType=ipam-pool,Tags=[{Key=Name,Value="Preprod pool"}]Output: `{ "IpamPool": { "OwnerId": "123456789012", "IpamPoolId": "ipam-pool-0533048da7d823723", "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0533048da7d823723", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-02fc38cd4c48e7d38", "IpamScopeType": "private", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "Locale": "None", "PoolDepth": 1, "State": "create-in-progress", "AutoImport": true, "AddressFamily": "ipv4", "AllocationMinNetmaskLength": 16, "AllocationMaxNetmaskLength": 26, "AllocationDefaultNetmaskLength": 24, "AllocationResourceTags": [ { "Key": "Environment", "Value": "Preprod" } ], "Tags": [ { "Key": "Name", "Value": "Preprod pool" } ] } }`For more information, see [Plan for IP address provisioning](https://docs.aws.amazon.com/vpc/latest/ipam/planning-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [CreateIpamPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ipam-resource-discovery`.

- **AWS CLI**
- 
            
                    **To create a resource discovery**In this example, you're a delegated IPAM admin who wants to create and share a resource discovery with the IPAM admin in another AWS Organization so that the admin in the other organization can manage and monitor the IP addresses of resources in your organization. Important This example includes both the `--region`and`--operating-regions`options because, while they are optional, they must be configured in a particular way to successfully integrate a resource discovery with an IPAM. *`--operating-regions`must match the Regions where you have resources that you want IPAM to discover. If there are Regions where you do not want IPAM to manage the IP addresses (for example for compliance reasons), do not include them. *`--region`must match the home Region of the IPAM you want to associate it with. You must create the resource discovery in the same Region that the IPAM was created in. For example, if the IPAM you are associating with was created in us-east-1, include`--region us-east-1`in the request.Both the`--region`and`--operating-regions`options default to the Region you're running the command in if you don't specify them.In this example, the operating Regions of the IPAM we're integrating with include `us-west-1`,`us-west-2`, and`ap-south-1`. When we create the resource discovery, we want IPAM to discover the resource IP addresses in`us-west-1`and`us-west-2`but not`ap-south-1`. So we are including only`--operating-regions RegionName='us-west-1' RegionName='us-west-2'`in the request.The following `create-ipam-resource-discovery`example creates an IPAM resource discovery.`aws ec2 create-ipam-resource-discovery \ --description '``Example-resource-discovery`' \ --tag-specifications '`ResourceType=ipam-resource-discovery,Tags=[{Key=cost-center,Value=cc123}]`' \ --operating-regions RegionName='us-west-1' RegionName='us-west-2' \ --region`us-east-1`Output: `{ "IpamResourceDiscovery":{ "OwnerId": "149977607591", "IpamResourceDiscoveryId": "ipam-res-disco-0257046d8aa78b8bc", "IpamResourceDiscoveryArn": "arn:aws:ec2::149977607591:ipam-resource-discovery/ipam-res-disco-0257046d8aa78b8bc", "IpamResourceDiscoveryRegion": "us-east-1", "Description": "'Example-resource-discovery'", "OperatingRegions":[ {"RegionName": "us-west-1"}, {"RegionName": "us-west-2"}, {"RegionName": "us-east-1"} ], "IsDefault": false, "State": "create-in-progress", "Tags": [ { "Key": "cost-center", "Value": "cc123" } ] }`Once you create a resource discovery, you may want to share it with another IPAM delegated admin, which you can do with [create-resource-share](https://docs.aws.amazon.com/cli/latest/reference/ram/create-resource-share.html). For more information, see[Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [CreateIpamResourceDiscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-resource-discovery.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ipam-scope`.

- **AWS CLI**
- 
            
                    **To create an IPAM scope**The following `create-ipam-scope`example creates an IPAM scope.(Linux): `aws ec2 create-ipam-scope \ --ipam-id``ipam-08440e7a3acde3908`\ --description`"Example description"`\ --tag-specifications '`ResourceType=ipam-scope,Tags=[{Key=Name,Value="Example name value"}]`'(Windows): `aws ec2 create-ipam-scope``^`--ipam-id`ipam-08440e7a3acde3908``^`--description`"Example description"``^`--tag-specifications ResourceType=ipam-scope,Tags=[{Key=Name,Value="Example name value"}]Output: `{ "IpamScope": { "OwnerId": "123456789012", "IpamScopeId": "ipam-scope-01c1ebab2b63bd7e4", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-01c1ebab2b63bd7e4", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "IpamScopeType": "private", "IsDefault": false, "Description": "Example description", "PoolCount": 0, "State": "create-in-progress", "Tags": [ { "Key": "Name", "Value": "Example name value" } ] } }`For more information, see [Create additional scopes](https://docs.aws.amazon.com/vpc/latest/ipam/add-scope-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [CreateIpamScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-ipam`.

- **AWS CLI**
- 
            
                    **To create an IPAM**The following `create-ipam`example creates an IPAM.(Linux): `aws ec2 create-ipam \ --description``"Example description"`\ --operating-regions`"RegionName=us-east-2"``"RegionName=us-west-1"`\ --tag-specifications '`ResourceType=ipam,Tags=[{Key=Name,Value=ExampleIPAM}]`'(Windows): `aws ec2 create-ipam``^`--description`"Example description"``^`--operating-regions`"RegionName=us-east-2"``"RegionName=us-west-1"``^`--tag-specifications`ResourceType=ipam,Tags=[{Key=Name,Value=ExampleIPAM}]`Output: `{ "Ipam": { "OwnerId": "123456789012", "IpamId": "ipam-036486dfa6af58ee0", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-036486dfa6af58ee0", "IpamRegion": "us-east-1", "PublicDefaultScopeId": "ipam-scope-071b8042b0195c183", "PrivateDefaultScopeId": "ipam-scope-0807405dece705a30", "ScopeCount": 2, "OperatingRegions": [ { "RegionName": "us-east-2" }, { "RegionName": "us-west-1" }, { "RegionName": "us-east-1" } ], "State": "create-in-progress", "Tags": [ { "Key": "Name", "Value": "ExampleIPAM" } ] } }`For more information, see [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [CreateIpam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-ipam.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-key-pair`.

- **AWS CLI**
- 
            
                    **To create a key pair**This example creates a key pair named `MyKeyPair`.Command: `aws ec2 create-key-pair --key-name``MyKeyPair`The output is an ASCII version of the private key and key fingerprint. You need to save the key to a file. For more information, see Using Key Pairs in the *AWS Command Line Interface User Guide*.- 
                    For API details, see [CreateKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-launch-template-version`.

- **AWS CLI**
- 
            
                    **To create a launch template version**This example creates a new launch template version based on version 1 of the launch template and specifies a different AMI ID. Command: `aws ec2 create-launch-template-version --launch-template-id``lt-0abcd290751193123`--version-description`WebVersion2`--source-version`1`--launch-template-data '`{"ImageId":"ami-c998b6b2"}`'Output: `{ "LaunchTemplateVersion": { "VersionDescription": "WebVersion2", "LaunchTemplateId": "lt-0abcd290751193123", "LaunchTemplateName": "WebServers", "VersionNumber": 2, "CreatedBy": "arn:aws:iam::123456789012:root", "LaunchTemplateData": { "ImageId": "ami-c998b6b2", "InstanceType": "t2.micro", "NetworkInterfaces": [ { "Ipv6Addresses": [ { "Ipv6Address": "2001:db8:1234:1a00::123" } ], "DeviceIndex": 0, "SubnetId": "subnet-7b16de0c", "AssociatePublicIpAddress": true } ] }, "DefaultVersion": false, "CreateTime": "2017-12-01T13:35:46.000Z" } }`- 
                    For API details, see [CreateLaunchTemplateVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-launch-template`.

- **AWS CLI**
- 
            
                    **Example 1: To create a launch template**The following `create-launch-template`example creates a launch template that specifies the subnet in which to launch the instance , assigns a public IP address and an IPv6 address to the instance, and creates a tag for the instance.`aws ec2 create-launch-template \ --launch-template-name``TemplateForWebServer`\ --version-description`WebVersion1`\ --launch-template-data '`{"NetworkInterfaces":[{"AssociatePublicIpAddress":true,"DeviceIndex":0,"Ipv6AddressCount":1,"SubnetId":"subnet-7b16de0c"}],"ImageId":"ami-8c1be5f6","InstanceType":"t2.small","TagSpecifications":[{"ResourceType":"instance","Tags":[{"Key":"purpose","Value":"webserver"}]}]}`'Output: `{ "LaunchTemplate": { "LatestVersionNumber": 1, "LaunchTemplateId": "lt-01238c059e3466abc", "LaunchTemplateName": "TemplateForWebServer", "DefaultVersionNumber": 1, "CreatedBy": "arn:aws:iam::123456789012:user/Bob", "CreateTime": "2019-01-27T09:13:24.000Z" } }`For more information, see Launching an Instance from a Launch Template in the *Amazon Elastic Compute Cloud User Guide*. For information about quoting JSON-formatted parameters, see Quoting Strings in the*AWS Command Line Interface User Guide*.**Example 2: To create a launch template for Amazon EC2 Auto Scaling**The following `create-launch-template`example creates a launch template with multiple tags and a block device mapping to specify an additional EBS volume when an instance launches. Specify a value for`Groups`that corresponds to security groups for the VPC that your Auto Scaling group will launch instances into. Specify the VPC and subnets as properties of the Auto Scaling group.`aws ec2 create-launch-template \ --launch-template-name``TemplateForAutoScaling`\ --version-description`AutoScalingVersion1`\ --launch-template-data '`{"NetworkInterfaces":[{"DeviceIndex":0,"AssociatePublicIpAddress":true,"Groups":["sg-7c227019,sg-903004f8"],"DeleteOnTermination":true}],"ImageId":"ami-b42209de","InstanceType":"m4.large","TagSpecifications":[{"ResourceType":"instance","Tags":[{"Key":"environment","Value":"production"},{"Key":"purpose","Value":"webserver"}]},{"ResourceType":"volume","Tags":[{"Key":"environment","Value":"production"},{"Key":"cost-center","Value":"cc123"}]}],"BlockDeviceMappings":[{"DeviceName":"/dev/sda1","Ebs":{"VolumeSize":100}}]}`' --region`us-east-1`Output: `{ "LaunchTemplate": { "LatestVersionNumber": 1, "LaunchTemplateId": "lt-0123c79c33a54e0abc", "LaunchTemplateName": "TemplateForAutoScaling", "DefaultVersionNumber": 1, "CreatedBy": "arn:aws:iam::123456789012:user/Bob", "CreateTime": "2019-04-30T18:16:06.000Z" } }`For more information, see Creating a Launch Template for an Auto Scaling Group in the *Amazon EC2 Auto Scaling User Guide*. For information about quoting JSON-formatted parameters, see Quoting Strings in the*AWS Command Line Interface User Guide*.**Example 3: To create a launch template that specifies encryption of EBS volumes**The following `create-launch-template`example creates a launch template that includes encrypted EBS volumes created from an unencrypted snapshot. It also tags the volumes during creation. If encryption by default is disabled, you must specify the`"Encrypted"`option as shown in the following example. If you use the`"KmsKeyId"`option to specify a customer managed CMK, you also must specify the`"Encrypted"`option even if encryption by default is enabled.`aws ec2 create-launch-template \ --launch-template-name``TemplateForEncryption`\ --launch-template-data`file://config.json`Contents of `config.json`:`{ "BlockDeviceMappings":[ { "DeviceName":"/dev/sda1", "Ebs":{ "VolumeType":"gp2", "DeleteOnTermination":true, "SnapshotId":"snap-066877671789bd71b", "Encrypted":true, "KmsKeyId":"arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef" } } ], "ImageId":"ami-00068cd7555f543d5", "InstanceType":"c5.large", "TagSpecifications":[ { "ResourceType":"volume", "Tags":[ { "Key":"encrypted", "Value":"yes" } ] } ] }`Output: `{ "LaunchTemplate": { "LatestVersionNumber": 1, "LaunchTemplateId": "lt-0d5bd51bcf8530abc", "LaunchTemplateName": "TemplateForEncryption", "DefaultVersionNumber": 1, "CreatedBy": "arn:aws:iam::123456789012:user/Bob", "CreateTime": "2020-01-07T19:08:36.000Z" } }`For more information, see Restoring an Amazon EBS Volume from a Snapshot and Encryption by Default in the *Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [CreateLaunchTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-launch-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-local-gateway-route-table-virtual-interface-group-association`.

- **AWS CLI**
- 
            
                    **To associate a local gateway route table with a virtual interfaces (VIFs) group**The following `create-local-gateway-route-table-virtual-interface-group-association`example creates an association between the specified local gateway route table and VIF group.`aws ec2 create-local-gateway-route-table-virtual-interface-group-association \ --local-gateway-route-table-id``lgw-rtb-exampleidabcd1234`\ --local-gateway-virtual-interface-group-id`lgw-vif-grp-exampleid0123abcd`Output: `{ "LocalGatewayRouteTableVirtualInterfaceGroupAssociation": { "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": "lgw-vif-grp-assoc-exampleid12345678", "LocalGatewayVirtualInterfaceGroupId": "lgw-vif-grp-exampleid0123abcd", "LocalGatewayId": "lgw-exampleid11223344", "LocalGatewayRouteTableId": "lgw-rtb-exampleidabcd1234", "LocalGatewayRouteTableArn": "arn:aws:ec2:us-west-2:111122223333:local-gateway-route-table/lgw-rtb-exampleidabcd1234", "OwnerId": "111122223333", "State": "pending", "Tags": [] } }`For more information, see [VIF group associations](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#vif-group-associations)in the*AWS Outposts User Guide*.- 
                    For API details, see [CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-local-gateway-route-table-virtual-interface-group-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-local-gateway-route-table-vpc-association`.

- **AWS CLI**
- 
            
                    **To associate a VPC with a route table**The following `create-local-gateway-route-table-vpc-association`example associates the specified VPC with the specified local gateway route table.`aws ec2 create-local-gateway-route-table-vpc-association \ --local-gateway-route-table-id``lgw-rtb-059615ef7dEXAMPLE`\ --vpc-id`vpc-07ef66ac71EXAMPLE`Output: `{ "LocalGatewayRouteTableVpcAssociation": { "LocalGatewayRouteTableVpcAssociationId": "lgw-vpc-assoc-0ee765bcc8EXAMPLE", "LocalGatewayRouteTableId": "lgw-rtb-059615ef7dEXAMPLE", "LocalGatewayId": "lgw-09b493aa7cEXAMPLE", "VpcId": "vpc-07ef66ac71EXAMPLE", "State": "associated" } }`- 
                    For API details, see [CreateLocalGatewayRouteTableVpcAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-local-gateway-route-table-vpc-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-local-gateway-route-table`.

- **AWS CLI**
- 
            
                    **To create a local gateway route table**The following `create-local-gateway-route-table`example creates a local gateway route table with the direct VPC routing mode.`aws ec2 create-local-gateway-route-table \ --local-gateway-id``lgw-1a2b3c4d5e6f7g8h9`\ --mode`direct-vpc-routing`Output: `{ "LocalGatewayRouteTable": { "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890", "LocalGatewayRouteTableArn": "arn:aws:ec2:us-west-2:111122223333:local-gateway-route-table/lgw-rtb-abcdefg1234567890", "LocalGatewayId": "lgw-1a2b3c4d5e6f7g8h9", "OutpostArn": "arn:aws:outposts:us-west-2:111122223333:outpost/op-021345abcdef67890", "OwnerId": "111122223333", "State": "pending", "Tags": [], "Mode": "direct-vpc-routing" } }`For more information, see [Local gateway route tables](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [CreateLocalGatewayRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-local-gateway-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-local-gateway-route`.

- **AWS CLI**
- 
            
                    **To create a static route for a local gateway route table**The following `create-local-gateway-route`example creates the specified route in the specified local gateway route table.`aws ec2 create-local-gateway-route \ --destination-cidr-block``0.0.0.0/0`\ --local-gateway-route-table-id`lgw-rtb-059615ef7dEXAMPLE`Output: `{ "Route": { "DestinationCidrBlock": "0.0.0.0/0", "LocalGatewayVirtualInterfaceGroupId": "lgw-vif-grp-07145b276bEXAMPLE", "Type": "static", "State": "deleted", "LocalGatewayRouteTableId": "lgw-rtb-059615ef7dEXAMPLE" } }`- 
                    For API details, see [CreateLocalGatewayRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-local-gateway-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-managed-prefix-list`.

- **AWS CLI**
- 
            
                    **To create a prefix list**The following `create-managed-prefix-list`example creates an IPv4 prefix list with a maximum of 10 entries, and creates 2 entries in the prefix list.`aws ec2 create-managed-prefix-list \ --address-family``IPv4`\ --max-entries`10`\ --entries`Cidr=10.0.0.0/16,Description=vpc-a``Cidr=10.2.0.0/16,Description=vpc-b`\ --prefix-list-name`vpc-cidrs`Output: `{ "PrefixList": { "PrefixListId": "pl-0123456abcabcabc1", "AddressFamily": "IPv4", "State": "create-in-progress", "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456abcabcabc1", "PrefixListName": "vpc-cidrs", "MaxEntries": 10, "Version": 1, "Tags": [], "OwnerId": "123456789012" } }`For more information, see [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [CreateManagedPrefixList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-managed-prefix-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-nat-gateway`.

- **AWS CLI**
- 
            
                    **Example 1: To create a public NAT gateway**The following `create-nat-gateway`example creates a public NAT gateway in the specified subnet and associates the Elastic IP address with the specified allocation ID. When you create a public NAT gateway, you must associate an Elastic IP address.`aws ec2 create-nat-gateway \ --subnet-id``subnet-0250c25a1fEXAMPLE`\ --allocation-id`eipalloc-09ad461b0dEXAMPLE`Output: `{ "NatGateway": { "CreateTime": "2021-12-01T22:22:38.000Z", "NatGatewayAddresses": [ { "AllocationId": "eipalloc-09ad461b0dEXAMPLE" } ], "NatGatewayId": "nat-0c61bf8a12EXAMPLE", "State": "pending", "SubnetId": "subnet-0250c25a1fEXAMPLE", "VpcId": "vpc-0a60eb65b4EXAMPLE", "ConnectivityType": "public" } }`For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)in the*Amazon VPC User Guide*.**Example 2: To create a private NAT gateway**The following `create-nat-gateway`example creates a private NAT gateway in the specified subnet. A private NAT gateway does not have an associated Elastic IP address.`aws ec2 create-nat-gateway \ --subnet-id``subnet-0250c25a1fEXAMPLE`\ --connectivity-type`private`Output: `{ "NatGateway": { "CreateTime": "2021-12-01T22:26:00.000Z", "NatGatewayAddresses": [ {} ], "NatGatewayId": "nat-011b568379EXAMPLE", "State": "pending", "SubnetId": "subnet-0250c25a1fEXAMPLE", "VpcId": "vpc-0a60eb65b4EXAMPLE", "ConnectivityType": "private" } }`For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [CreateNatGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-nat-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-network-acl-entry`.

- **AWS CLI**
- 
            
                    **To create a network ACL entry**This example creates an entry for the specified network ACL. The rule allows ingress traffic from any IPv4 address (0.0.0.0/0) on UDP port 53 (DNS) into any associated subnet. If the command succeeds, no output is returned. Command: `aws ec2 create-network-acl-entry --network-acl-id``acl-5fb85d36`--ingress --rule-number`100`--protocol`udp`--port-range`From=53,To=53`--cidr-block`0.0.0.0/0`--rule-action`allow`This example creates a rule for the specified network ACL that allows ingress traffic from any IPv6 address (::/0) on TCP port 80 (HTTP). Command: `aws ec2 create-network-acl-entry --network-acl-id``acl-5fb85d36`--ingress --rule-number`120`--protocol`tcp`--port-range`From=80,To=80`--ipv6-cidr-block`::/0`--rule-action`allow`- 
                    For API details, see [CreateNetworkAclEntry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl-entry.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-network-acl`.

- **AWS CLI**
- 
            
                    **To create a network ACL**This example creates a network ACL for the specified VPC. Command: `aws ec2 create-network-acl --vpc-id``vpc-a01106c2`Output: `{ "NetworkAcl": { "Associations": [], "NetworkAclId": "acl-5fb85d36", "VpcId": "vpc-a01106c2", "Tags": [], "Entries": [ { "CidrBlock": "0.0.0.0/0", "RuleNumber": 32767, "Protocol": "-1", "Egress": true, "RuleAction": "deny" }, { "CidrBlock": "0.0.0.0/0", "RuleNumber": 32767, "Protocol": "-1", "Egress": false, "RuleAction": "deny" } ], "IsDefault": false } }`- 
                    For API details, see [CreateNetworkAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-network-insights-access-scope`.

- **AWS CLI**
- 
            
                    **To create a Network Access Scope**The following `create-network-insights-access-scope`example creates a Network Access Scope.`aws ec2 create-network-insights-access-scope \ --cli-input-json``file://access-scope-file.json`Contents of `access-scope-file.json`:`{ "MatchPaths": [ { "Source": { "ResourceStatement": { "Resources": [ "vpc-abcd12e3" ] } } } ], "ExcludePaths": [ { "Source": { "ResourceStatement": { "ResourceTypes": [ "AWS::EC2::InternetGateway" ] } } } ] }`Output: `{ "NetworkInsightsAccessScope": { "NetworkInsightsAccessScopeId": "nis-123456789abc01234", "NetworkInsightsAccessScopeArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-access-scope/nis-123456789abc01234", "CreatedDate": "2022-01-25T19:20:28.796000+00:00", "UpdatedDate": "2022-01-25T19:20:28.797000+00:00" }, "NetworkInsightsAccessScopeContent": { "NetworkInsightsAccessScopeId": "nis-123456789abc01234", "MatchPaths": [ { "Source": { "ResourceStatement": { "Resources": [ "vpc-abcd12e3" ] } } } ], "ExcludePaths": [ { "Source": { "ResourceStatement": { "ResourceTypes": [ "AWS::EC2::InternetGateway" ] } } } ] } }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [CreateNetworkInsightsAccessScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-insights-access-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-network-insights-path`.

- **AWS CLI**
- 
            
                    **To create a path**The following `create-network-insights-path`example creates a path. The source is the specified internet gateway and the destination is the specified EC2 instance. To determine whether the destination is reachable using the specified protocol and port, analyze the path using the`start-network-insights-analysis`command.`aws ec2 create-network-insights-path \ --source``igw-0797cccdc9d73b0e5`\ --destination`i-0495d385ad28331c7`\ --destination-port`22`\ --protocol`TCP`Output: `{ "NetworkInsightsPaths": { "NetworkInsightsPathId": "nip-0b26f224f1d131fa8", "NetworkInsightsPathArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-path/nip-0b26f224f1d131fa8", "CreatedDate": "2021-01-20T22:43:46.933Z", "Source": "igw-0797cccdc9d73b0e5", "Destination": "i-0495d385ad28331c7", "Protocol": "tcp" } }`For more information, see [Getting started using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/reachability/getting-started-cli.html)in the*Reachability Analyzer Guide*.- 
                    For API details, see [CreateNetworkInsightsPath](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-insights-path.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-network-interface-permission`.

- **AWS CLI**
- 
            
                    **To create a network interface permission**This example grants permission to account `123456789012`to attach network interface`eni-1a2b3c4d`to an instance.Command: `aws ec2 create-network-interface-permission --network-interface-id``eni-1a2b3c4d`--aws-account-id`123456789012`--permission`INSTANCE-ATTACH`Output: `{ "InterfacePermission": { "PermissionState": { "State": "GRANTED" }, "NetworkInterfacePermissionId": "eni-perm-06fd19020ede149ea", "NetworkInterfaceId": "eni-1a2b3c4d", "Permission": "INSTANCE-ATTACH", "AwsAccountId": "123456789012" } }`- 
                    For API details, see [CreateNetworkInterfacePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-interface-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-network-interface`.

- **AWS CLI**
- 
            
                    **Example 1: To specify an IPv4 address for a network interface**The following `create-network-interface`example creates a network interface for the specified subnet with the specified primary IPv4 address.`aws ec2 create-network-interface \ --subnet-id``subnet-00a24d0d67acf6333`\ --description`"my network interface"`\ --groups`sg-09dfba7ed20cda78b`\ --private-ip-address`10.0.8.17`Output: `{ "NetworkInterface": { "AvailabilityZone": "us-west-2a", "Description": "my network interface", "Groups": [ { "GroupName": "my-security-group", "GroupId": "sg-09dfba7ed20cda78b" } ], "InterfaceType": "interface", "Ipv6Addresses": [], "MacAddress": "06:6a:0f:9a:49:37", "NetworkInterfaceId": "eni-0492b355f0cf3b3f8", "OwnerId": "123456789012", "PrivateDnsName": "ip-10-0-8-18.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.17", "PrivateIpAddresses": [ { "Primary": true, "PrivateDnsName": "ip-10-0-8-17.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.17" } ], "RequesterId": "AIDA4Z3Y7GSXTMEXAMPLE", "RequesterManaged": false, "SourceDestCheck": true, "Status": "pending", "SubnetId": "subnet-00a24d0d67acf6333", "TagSet": [], "VpcId": "vpc-02723a0feeeb9d57b" } }`**Example 2: To create a network interface with an IPv4 address and an IPv6 address**The following `create-network-interface`example creates a network interface for the specified subnet with an IPv4 address and an IPv6 address that are selected by Amazon EC2.`aws ec2 create-network-interface \ --subnet-id``subnet-00a24d0d67acf6333`\ --description`"my dual stack network interface"`\ --ipv6-address-count`1`\ --groups`sg-09dfba7ed20cda78b`Output: `{ "NetworkInterface": { "AvailabilityZone": "us-west-2a", "Description": "my dual stack network interface", "Groups": [ { "GroupName": "my-security-group", "GroupId": "sg-09dfba7ed20cda78b" } ], "InterfaceType": "interface", "Ipv6Addresses": [ { "Ipv6Address": "2600:1f13:cfe:3650:a1dc:237c:393a:4ba7", "IsPrimaryIpv6": false } ], "MacAddress": "06:b8:68:d2:b2:2d", "NetworkInterfaceId": "eni-05da417453f9a84bf", "OwnerId": "123456789012", "PrivateDnsName": "ip-10-0-8-18.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.18", "PrivateIpAddresses": [ { "Primary": true, "PrivateDnsName": "ip-10-0-8-18.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.18" } ], "RequesterId": "AIDA4Z3Y7GSXTMEXAMPLE", "RequesterManaged": false, "SourceDestCheck": true, "Status": "pending", "SubnetId": "subnet-00a24d0d67acf6333", "TagSet": [], "VpcId": "vpc-02723a0feeeb9d57b", "Ipv6Address": "2600:1f13:cfe:3650:a1dc:237c:393a:4ba7" } }`**Example 3: To create a network interface with connection tracking configuration options**The following `create-network-interface`example creates a network interface and configures the idle connection tracking timeouts.`aws ec2 create-network-interface \ --subnet-id``subnet-00a24d0d67acf6333`\ --groups`sg-02e57dbcfe0331c1b`\ --connection-tracking-specification`TcpEstablishedTimeout=86400,UdpTimeout=60`Output: `{ "NetworkInterface": { "AvailabilityZone": "us-west-2a", "ConnectionTrackingConfiguration": { "TcpEstablishedTimeout": 86400, "UdpTimeout": 60 }, "Description": "", "Groups": [ { "GroupName": "my-security-group", "GroupId": "sg-02e57dbcfe0331c1b" } ], "InterfaceType": "interface", "Ipv6Addresses": [], "MacAddress": "06:4c:53:de:6d:91", "NetworkInterfaceId": "eni-0c133586e08903d0b", "OwnerId": "123456789012", "PrivateDnsName": "ip-10-0-8-94.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.94", "PrivateIpAddresses": [ { "Primary": true, "PrivateDnsName": "ip-10-0-8-94.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.94" } ], "RequesterId": "AIDA4Z3Y7GSXTMEXAMPLE", "RequesterManaged": false, "SourceDestCheck": true, "Status": "pending", "SubnetId": "subnet-00a24d0d67acf6333", "TagSet": [], "VpcId": "vpc-02723a0feeeb9d57b" } }`**Example 4: To create an Elastic Fabric Adapter**The following `create-network-interface`example creates an EFA.`aws ec2 create-network-interface \ --interface-type``efa`\ --subnet-id`subnet-00a24d0d67acf6333`\ --description`"my efa"`\ --groups`sg-02e57dbcfe0331c1b`Output: `{ "NetworkInterface": { "AvailabilityZone": "us-west-2a", "Description": "my efa", "Groups": [ { "GroupName": "my-efa-sg", "GroupId": "sg-02e57dbcfe0331c1b" } ], "InterfaceType": "efa", "Ipv6Addresses": [], "MacAddress": "06:d7:a4:f7:4d:57", "NetworkInterfaceId": "eni-034acc2885e862b65", "OwnerId": "123456789012", "PrivateDnsName": "ip-10-0-8-180.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.180", "PrivateIpAddresses": [ { "Primary": true, "PrivateDnsName": "ip-10-0-8-180.us-west-2.compute.internal", "PrivateIpAddress": "10.0.8.180" } ], "RequesterId": "AIDA4Z3Y7GSXTMEXAMPLE", "RequesterManaged": false, "SourceDestCheck": true, "Status": "pending", "SubnetId": "subnet-00a24d0d67acf6333", "TagSet": [], "VpcId": "vpc-02723a0feeeb9d57b" } }`For more information, see [Elastic network interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateNetworkInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-network-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-placement-group`.

- **AWS CLI**
- 
            
                    **To create a placement group**This example command creates a placement group with the specified name. Command: `aws ec2 create-placement-group --group-name``my-cluster`--strategy`cluster`**To create a partition placement group**This example command creates a partition placement group named `HDFS-Group-A`with five partitions.Command: `aws ec2 create-placement-group --group-name``HDFS-Group-A`--strategy`partition`--partition-count`5`- 
                    For API details, see [CreatePlacementGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-placement-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-replace-root-volume-task`.

- **AWS CLI**
- 
            
                    **Example 1: To restore a root volume to its initial launch state**The following `create-replace-root-volume-task`example restores the root volume of instance i-0123456789abcdefa to its initial launch state.`aws ec2 create-replace-root-volume-task \ --instance-id``i-0123456789abcdefa`Output: `{ "ReplaceRootVolumeTask": { "InstanceId": "i-0123456789abcdefa", "ReplaceRootVolumeTaskId": "replacevol-0111122223333abcd", "TaskState": "pending", "StartTime": "2022-03-14T15:06:38Z", "Tags": [] } }`**Example 2: To restore a root volume to a specific snapshot**The following `create-replace-root-volume-task`example restores the root volume of instance i-0123456789abcdefa to snapshot snap-0abcdef1234567890.`aws ec2 create-replace-root-volume-task \ --instance-id``i-0123456789abcdefa`\ --snapshot-id`snap-0abcdef1234567890`Output: `{ "ReplaceRootVolumeTask": { "InstanceId": "i-0123456789abcdefa", "ReplaceRootVolumeTaskId": "replacevol-0555566667777abcd", "TaskState": "pending", "StartTime": "2022-03-14T15:16:28Z", "Tags": [] } }`For more information, see [Replace a root volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/replace-root.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateReplaceRootVolumeTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-replace-root-volume-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-reserved-instances-listing`.

- **AWS CLI**
- 
            
                    **To list a Reserved Instance in the Reserved Instance Marketplace**The following `create-reserved-instances-listing`example creates a listing for the specified Reserved Instance in the Reserved Instance Marketplace.`aws ec2 create-reserved-instances-listing \ --reserved-instances-id``5ec28771-05ff-4b9b-aa31-9e57dexample`\ --instance-count`3`\ --price-schedules`CurrencyCode=USD,Price=25.50`\ --client-token`550e8400-e29b-41d4-a716-446655440000`- 
                    For API details, see [CreateReservedInstancesListing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-reserved-instances-listing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-restore-image-task`.

- **AWS CLI**
- 
            
                    **To restore an AMI from an S3 bucket**The following `create-restore-image-task`example restores an AMI from an S3 bucket. Use the values for`S3ObjectKey `` and ``Bucket`from the`describe-store-image-tasks`output, specify the object key of the AMI and the name of the S3 bucket to which the AMI was copied, and specify the name for the restored AMI. The name must be unique for AMIs in the Region for this account. The restored AMI will receive a new AMI ID.`aws ec2 create-restore-image-task \ --object-key``ami-1234567890abcdef0.bin`\ --bucket`my-ami-bucket`\ --name '`New AMI Name`'Output: `{ "ImageId": "ami-0eab20fe36f83e1a8" }`For more information, see [Store and restore an AMI using S3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateRestoreImageTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-restore-image-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-route-table`.

- **AWS CLI**
- 
            
                    **To create a route table**This example creates a route table for the specified VPC. Command: `aws ec2 create-route-table --vpc-id``vpc-a01106c2`Output: `{ "RouteTable": { "Associations": [], "RouteTableId": "rtb-22574640", "VpcId": "vpc-a01106c2", "PropagatingVgws": [], "Tags": [], "Routes": [ { "GatewayId": "local", "DestinationCidrBlock": "10.0.0.0/16", "State": "active" } ] } }`- 
                    For API details, see [CreateRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-route`.

- **AWS CLI**
- 
            
                    **To create a route**This example creates a route for the specified route table. The route matches all IPv4 traffic ( `0.0.0.0/0`) and routes it to the specified Internet gateway. If the command succeeds, no output is returned.Command: `aws ec2 create-route --route-table-id``rtb-22574640`--destination-cidr-block`0.0.0.0/0`--gateway-id`igw-c0a643a9`This example command creates a route in route table rtb-g8ff4ea2. The route matches traffic for the IPv4 CIDR block 10.0.0.0/16 and routes it to VPC peering connection, pcx-111aaa22. This route enables traffic to be directed to the peer VPC in the VPC peering connection. If the command succeeds, no output is returned. Command: `aws ec2 create-route --route-table-id``rtb-g8ff4ea2`--destination-cidr-block`10.0.0.0/16`--vpc-peering-connection-id`pcx-1a2b3c4d`This example creates a route in the specified route table that matches all IPv6 traffic ( `::/0`) and routes it to the specified egress-only Internet gateway.Command: `aws ec2 create-route --route-table-id``rtb-dce620b8`--destination-ipv6-cidr-block`::/0`--egress-only-internet-gateway-id`eigw-01eadbd45ecd7943f`- 
                    For API details, see [CreateRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-security-group`.

- **AWS CLI**
- 
            
                    **To create a security group for EC2-Classic**This example creates a security group named `MySecurityGroup`.Command: `aws ec2 create-security-group --group-name``MySecurityGroup`--description`"My security group"`Output: `{ "GroupId": "sg-903004f8" }`**To create a security group for EC2-VPC**This example creates a security group named `MySecurityGroup`for the specified VPC.Command: `aws ec2 create-security-group --group-name``MySecurityGroup`--description`"My security group"`--vpc-id`vpc-1a2b3c4d`Output: `{ "GroupId": "sg-903004f8" }`For more information, see Using Security Groups in the *AWS Command Line Interface User Guide*.- 
                    For API details, see [CreateSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-security-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-snapshot`.

- **AWS CLI**
- 
            
                    **To create a snapshot**This example command creates a snapshot of the volume with a volume ID of `vol-1234567890abcdef0`and a short description to identify the snapshot.Command: `aws ec2 create-snapshot --volume-id``vol-1234567890abcdef0`--description`"This is my root volume snapshot"`Output: `{ "Description": "This is my root volume snapshot", "Tags": [], "Encrypted": false, "VolumeId": "vol-1234567890abcdef0", "State": "pending", "VolumeSize": 8, "StartTime": "2018-02-28T21:06:01.000Z", "Progress": "", "OwnerId": "012345678910", "SnapshotId": "snap-066877671789bd71b" }`**To create a snapshot with tags**This example command creates a snapshot and applies two tags: purpose=prod and costcenter=123. Command: `aws ec2 create-snapshot --volume-id``vol-1234567890abcdef0`--description '`Prod backup`' --tag-specifications '`ResourceType=snapshot,Tags=[{Key=purpose,Value=prod},{Key=costcenter,Value=123}]`'Output: `{ "Description": "Prod backup", "Tags": [ { "Value": "prod", "Key": "purpose" }, { "Value": "123", "Key": "costcenter" } ], "Encrypted": false, "VolumeId": "vol-1234567890abcdef0", "State": "pending", "VolumeSize": 8, "StartTime": "2018-02-28T21:06:06.000Z", "Progress": "", "OwnerId": "012345678910", "SnapshotId": "snap-09ed24a70bc19bbe4" }`- 
                    For API details, see [CreateSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-snapshots`.

- **AWS CLI**
- 
            
                    **Example 1: To create a multi-volume snapshot**The following `create-snapshots`example creates snapshots of all volumes attached to the specified instance.`aws ec2 create-snapshots \ --instance-specification``InstanceId=i-1234567890abcdef0`\ --description`"This is snapshot of a volume from my-instance"`Output: `{ "Snapshots": [ { "Description": "This is a snapshot of a volume from my-instance", "Tags": [], "Encrypted": false, "VolumeId": "vol-0a01d2d5a34697479", "State": "pending", "VolumeSize": 16, "StartTime": "2019-08-05T16:58:19.000Z", "Progress": "", "OwnerId": "123456789012", "SnapshotId": "snap-07f30e3909aa0045e" }, { "Description": "This is a snapshot of a volume from my-instance", "Tags": [], "Encrypted": false, "VolumeId": "vol-02d0d4947008cb1a2", "State": "pending", "VolumeSize": 20, "StartTime": "2019-08-05T16:58:19.000Z", "Progress": "", "OwnerId": "123456789012", "SnapshotId": "snap-0ec20b602264aad48" }, ... ] }`**Example 2: To create a multi-volume snapshot with tags from the source volume**The following `create-snapshots`example creates snapshots of all volumes attached to the specified instance and copies the tags from each volume to its corresponding snapshot.`aws ec2 create-snapshots \ --instance-specification``InstanceId=i-1234567890abcdef0`\ --copy-tags-from-source`volume`\ --description`"This is snapshot of a volume from my-instance"`Output: `{ "Snapshots": [ { "Description": "This is a snapshot of a volume from my-instance", "Tags": [ { "Key": "Name", "Value": "my-volume" } ], "Encrypted": false, "VolumeId": "vol-02d0d4947008cb1a2", "State": "pending", "VolumeSize": 20, "StartTime": "2019-08-05T16:53:04.000Z", "Progress": "", "OwnerId": "123456789012", "SnapshotId": "snap-053bfaeb821a458dd" } ... ] }`**Example 3: To create a multi-volume snapshot not including the root volume**The following `create-snapshots`example creates a snapshot of all volumes attached to the specified instance except for the root volume.`aws ec2 create-snapshots \ --instance-specification``InstanceId=i-1234567890abcdef0,ExcludeBootVolume=true`See example 1 for sample output. **Example 4: To create a multi-volume snapshot and add tags**The following `create-snapshots`example creates snapshots of all volumes attached to the specified instance and adds two tags to each snapshot.`aws ec2 create-snapshots \ --instance-specification``InstanceId=i-1234567890abcdef0`\ --tag-specifications '`ResourceType=snapshot,Tags=[{Key=Name,Value=backup},{Key=costcenter,Value=123}]`'See example 1 for sample output. - 
                    For API details, see [CreateSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-spot-datafeed-subscription`.

- **AWS CLI**
- 
            
                    **To create a Spot Instance data feed**The following `create-spot-datafeed-subscription`example creates a Spot Instance data feed.`aws ec2 create-spot-datafeed-subscription \ --bucket``amzn-s3-demo-bucket`\ --prefix`spot-data-feed`Output: `{ "SpotDatafeedSubscription": { "Bucket": "amzn-s3-demo-bucket", "OwnerId": "123456789012", "Prefix": "spot-data-feed", "State": "Active" } }`The data feed is stored in the Amazon S3 bucket that you specified. The file names for this data feed have the following format. `amzn-s3-demo-bucket.s3.amazonaws.com/spot-data-feed/123456789012.YYYY-MM-DD-HH.n.abcd1234.gz`For more information, see [Spot Instance data feed](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-data-feeds.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateSpotDatafeedSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-spot-datafeed-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-store-image-task`.

- **AWS CLI**
- 
            
                    **To store an AMI in an S3 bucket**The following `create-store-image-task`example stores an AMI in an S3 bucket. Specify the ID of the AMI and the name of the S3 bucket in which to store the AMI.`aws ec2 create-store-image-task \ --image-id``ami-1234567890abcdef0`\ --bucket`my-ami-bucket`Output: `{ "ObjectKey": "ami-1234567890abcdef0.bin" }`For more information, see [Store and restore an AMI using S3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateStoreImageTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-store-image-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subnet-cidr-reservation`.

- **AWS CLI**
- 
            
                    **To create a subnet CIDR reservation**The following `create-subnet-cidr-reservation`example creates a subnet CIDR reservation for the specified subnet and CIDR range.`aws ec2 create-subnet-cidr-reservation \ --subnet-id``subnet-03c51e2eEXAMPLE`\ --reservation-type`prefix`\ --cidr`10.1.0.20/26`Output: `{ "SubnetCidrReservation": { "SubnetCidrReservationId": "scr-044f977c4eEXAMPLE", "SubnetId": "subnet-03c51e2e6cEXAMPLE", "Cidr": "10.1.0.16/28", "ReservationType": "prefix", "OwnerId": "123456789012" } }`For more information, see [Subnet CIDR reservations](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [CreateSubnetCidrReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-subnet-cidr-reservation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-subnet`.

- **AWS CLI**
- 
            
                    **Example 1: To create a subnet with an IPv4 CIDR block only**The following `create-subnet`example creates a subnet in the specified VPC with the specified IPv4 CIDR block.`aws ec2 create-subnet \ --vpc-id``vpc-081ec835f3EXAMPLE`\ --cidr-block`10.0.0.0/24`\ --tag-specifications`ResourceType=subnet,Tags=[{Key=Name,Value=my-ipv4-only-subnet}]`Output: `{ "Subnet": { "AvailabilityZone": "us-west-2a", "AvailabilityZoneId": "usw2-az2", "AvailableIpAddressCount": 251, "CidrBlock": "10.0.0.0/24", "DefaultForAz": false, "MapPublicIpOnLaunch": false, "State": "available", "SubnetId": "subnet-0e99b93155EXAMPLE", "VpcId": "vpc-081ec835f3EXAMPLE", "OwnerId": "123456789012", "AssignIpv6AddressOnCreation": false, "Ipv6CidrBlockAssociationSet": [], "Tags": [ { "Key": "Name", "Value": "my-ipv4-only-subnet" } ], "SubnetArn": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0e99b93155EXAMPLE" } }`**Example 2: To create a subnet with both IPv4 and IPv6 CIDR blocks**The following `create-subnet`example creates a subnet in the specified VPC with the specified IPv4 and IPv6 CIDR blocks.`aws ec2 create-subnet \ --vpc-id``vpc-081ec835f3EXAMPLE`\ --cidr-block`10.0.0.0/24`\ --ipv6-cidr-block`2600:1f16:cfe:3660::/64`\ --tag-specifications`ResourceType=subnet,Tags=[{Key=Name,Value=my-ipv4-ipv6-subnet}]`Output: `{ "Subnet": { "AvailabilityZone": "us-west-2a", "AvailabilityZoneId": "usw2-az2", "AvailableIpAddressCount": 251, "CidrBlock": "10.0.0.0/24", "DefaultForAz": false, "MapPublicIpOnLaunch": false, "State": "available", "SubnetId": "subnet-0736441d38EXAMPLE", "VpcId": "vpc-081ec835f3EXAMPLE", "OwnerId": "123456789012", "AssignIpv6AddressOnCreation": false, "Ipv6CidrBlockAssociationSet": [ { "AssociationId": "subnet-cidr-assoc-06c5f904499fcc623", "Ipv6CidrBlock": "2600:1f13:cfe:3660::/64", "Ipv6CidrBlockState": { "State": "associating" } } ], "Tags": [ { "Key": "Name", "Value": "my-ipv4-ipv6-subnet" } ], "SubnetArn": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-0736441d38EXAMPLE" } }`**Example 3: To create a subnet with an IPv6 CIDR block only**The following `create-subnet`example creates a subnet in the specified VPC with the specified IPv6 CIDR block.`aws ec2 create-subnet \ --vpc-id``vpc-081ec835f3EXAMPLE`\ --ipv6-native \ --ipv6-cidr-block`2600:1f16:115:200::/64`\ --tag-specifications`ResourceType=subnet,Tags=[{Key=Name,Value=my-ipv6-only-subnet}]`Output: `{ "Subnet": { "AvailabilityZone": "us-west-2a", "AvailabilityZoneId": "usw2-az2", "AvailableIpAddressCount": 0, "DefaultForAz": false, "MapPublicIpOnLaunch": false, "State": "available", "SubnetId": "subnet-03f720e7deEXAMPLE", "VpcId": "vpc-081ec835f3EXAMPLE", "OwnerId": "123456789012", "AssignIpv6AddressOnCreation": true, "Ipv6CidrBlockAssociationSet": [ { "AssociationId": "subnet-cidr-assoc-01ef639edde556709", "Ipv6CidrBlock": "2600:1f13:cfe:3660::/64", "Ipv6CidrBlockState": { "State": "associating" } } ], "Tags": [ { "Key": "Name", "Value": "my-ipv6-only-subnet" } ], "SubnetArn": "arn:aws:ec2:us-west-2:123456789012:subnet/subnet-03f720e7deEXAMPLE" } }`For more information, see [VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [CreateSubnet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-subnet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-tags`.

- **AWS CLI**
- 
            
                    **Example 1: To add a tag to a resource**The following `create-tags`example adds the tag`Stack=production`to the specified image, or overwrites an existing tag for the AMI where the tag key is`Stack`.`aws ec2 create-tags \ --resources``ami-1234567890abcdef0`\ --tags`Key=Stack,Value=production`This command produces no output **Example 2: To add tags to multiple resources**The following `create-tags`example adds (or overwrites) two tags for an AMI and an instance. One of the tags has a key (`webserver`) but no value (value is set to an empty string). The other tag has a key (`stack`) and a value (`Production`).`aws ec2 create-tags \ --resources``ami-1a2b3c4d``i-1234567890abcdef0`\ --tags`Key=webserver,Value=``Key=stack,Value=Production`This command produces no output **Example 3: To add tags containing special characters**The following `create-tags`examples add the tag`[Group]=test`for an instance. The square brackets ([ and ]) are special characters, and must be escaped. The following examples also use the line continuation character appropriate for each environment.If you are using Windows, surround the element that has special characters with double quotes ("), and then precede each double quote character with a backslash (\) as follows. `aws ec2 create-tags``^`--resources`i-1234567890abcdef0``^`--tags Key=\"[Group]\",Value=testIf you are using Windows PowerShell, surround the element the value that has special characters with double quotes ("), precede each double quote character with a backslash (\), and then surround the entire key and value structure with single quotes (') as follows. `aws ec2 create-tags````--resources`i-1234567890abcdef0````--tags '`Key=\"[Group]\",Value=test`'If you are using Linux or OS X, surround the element that has special characters with double quotes ("), and then surround the entire key and value structure with single quotes (') as follows. `aws ec2 create-tags \ --resources``i-1234567890abcdef0`\ --tags '`Key="[Group]",Value=test`'For more information, see [Tag your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [CreateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-traffic-mirror-filter-rule`.

- **AWS CLI**
- 
            
                    **To create a filter rule for incoming TCP traffic**The following `create-traffic-mirror-filter-rule`example creates a rule that you can use to mirror all incoming TCP traffic. Before you run this command, use`create-traffic-mirror-filter`to create the the traffic mirror filter.`aws ec2 create-traffic-mirror-filter-rule \ --description '``TCP Rule`' \ --destination-cidr-block`0.0.0.0/0`\ --protocol`6`\ --rule-action`accept`\ --rule-number`1`\ --source-cidr-block`0.0.0.0/0`\ --traffic-direction`ingress`\ --traffic-mirror-filter-id`tmf-04812ff784b25ae67`Output: `{ "TrafficMirrorFilterRule": { "DestinationCidrBlock": "0.0.0.0/0", "TrafficMirrorFilterId": "tmf-04812ff784b25ae67", "TrafficMirrorFilterRuleId": "tmfr-02d20d996673f3732", "SourceCidrBlock": "0.0.0.0/0", "TrafficDirection": "ingress", "Description": "TCP Rule", "RuleNumber": 1, "RuleAction": "accept", "Protocol": 6 }, "ClientToken": "4752b573-40a6-4eac-a8a4-a72058761219" }`For more information, see [Create a traffic mirror filter](https://docs.aws.amazon.com/vpc/latest/mirroring/create-traffic-mirroring-filter.html)in the*Traffic Mirroring Guide*.- 
                    For API details, see [CreateTrafficMirrorFilterRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-filter-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-traffic-mirror-filter`.

- **AWS CLI**
- 
            
                    **To create a traffic mirror filter**The following `create-traffic-mirror-filter`example creates a traffic mirror filter. After you create the filter, use`create-traffic-mirror-filter-rule`to add rules.`aws ec2 create-traffic-mirror-filter \ --description '``TCP Filter`'Output: `{ "ClientToken": "28908518-100b-4987-8233-8c744EXAMPLE", "TrafficMirrorFilter": { "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE", "Description": "TCP Filter", "EgressFilterRules": [], "IngressFilterRules": [], "Tags": [], "NetworkServices": [] } }`For more information, see [Create a traffic mirror filter](https://docs.aws.amazon.com/vpc/latest/mirroring/create-traffic-mirroring-filter.html)in the*Traffic Mirroring Guide*.- 
                    For API details, see [CreateTrafficMirrorFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-traffic-mirror-session`.

- **AWS CLI**
- 
            
                    **To create a traffic mirror session**The following `create-traffic-mirror-session`command creates a traffic mirror session for the specified source and target for 25 bytes of the packet.`aws ec2 create-traffic-mirror-session \ --description '``example session`' \ --traffic-mirror-target-id`tmt-07f75d8feeEXAMPLE`\ --network-interface-id`eni-070203f901EXAMPLE`\ --session-number`1`\ --packet-length`25`\ --traffic-mirror-filter-id`tmf-04812ff784EXAMPLE`Output: `{ "TrafficMirrorSession": { "TrafficMirrorSessionId": "tms-08a33b1214EXAMPLE", "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE", "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE", "NetworkInterfaceId": "eni-070203f901EXAMPLE", "OwnerId": "111122223333", "PacketLength": 25, "SessionNumber": 1, "VirtualNetworkId": 7159709, "Description": "example session", "Tags": [] }, "ClientToken": "5236cffc-ee13-4a32-bb5b-388d9da09d96" }`For more information, see [Create a traffic mirror session](https://docs.aws.amazon.com/vpc/latest/mirroring/create-traffic-mirroring-session.html)in the*Traffic Mirroring Guide*.- 
                    For API details, see [CreateTrafficMirrorSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-traffic-mirror-target`.

- **AWS CLI**
- 
            
                    **To create a a Network Load Balancer traffic mirror target**The following `create-traffic-mirror-target`example creates a Network Load Balancer traffic mirror target.`aws ec2 create-traffic-mirror-target \ --description '``Example Network Load Balancer Target`' \ --network-load-balancer-arn`arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/net/NLB/7cdec873EXAMPLE`Output: `{ "TrafficMirrorTarget": { "Type": "network-load-balancer", "Tags": [], "Description": "Example Network Load Balancer Target", "OwnerId": "111122223333", "NetworkLoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:724145273726:loadbalancer/net/NLB/7cdec873EXAMPLE", "TrafficMirrorTargetId": "tmt-0dabe9b0a6EXAMPLE" }, "ClientToken": "d5c090f5-8a0f-49c7-8281-72c796a21f72" }`**To create a network traffic mirror target**The following `create-traffic-mirror-target`example creates a network interface Traffic Mirror target.`aws ec2 create-traffic-mirror-target \ --description '``Network interface target`' \ --network-interface-id`eni-eni-01f6f631eEXAMPLE`Output: `{ "ClientToken": "5289a345-0358-4e62-93d5-47ef3061d65e", "TrafficMirrorTarget": { "Description": "Network interface target", "NetworkInterfaceId": "eni-01f6f631eEXAMPLE", "TrafficMirrorTargetId": "tmt-02dcdbe2abEXAMPLE", "OwnerId": "111122223333", "Type": "network-interface", "Tags": [] } }`For more information, see [Create a traffic mirror target](https://docs.aws.amazon.com/vpc/latest/mirroring/create-traffic-mirroring-target.html)in the*Traffic Mirroring Guide*.- 
                    For API details, see [CreateTrafficMirrorTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-traffic-mirror-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-connect-peer`.

- **AWS CLI**
- 
            
                    **To create a Transit Gateway Connect peer**The following `create-transit-gateway-connect-peer`example creates a Connect peer.`aws ec2 create-transit-gateway-connect-peer \ --transit-gateway-attachment-id``tgw-attach-0f0927767cEXAMPLE`\ --peer-address`172.31.1.11`\ --inside-cidr-blocks`169.254.6.0/29`Output: `{ "TransitGatewayConnectPeer": { "TransitGatewayAttachmentId": "tgw-attach-0f0927767cEXAMPLE", "TransitGatewayConnectPeerId": "tgw-connect-peer-0666adbac4EXAMPLE", "State": "pending", "CreationTime": "2021-10-13T03:35:17.000Z", "ConnectPeerConfiguration": { "TransitGatewayAddress": "10.0.0.234", "PeerAddress": "172.31.1.11", "InsideCidrBlocks": [ "169.254.6.0/29" ], "Protocol": "gre", "BgpConfigurations": [ { "TransitGatewayAsn": 64512, "PeerAsn": 64512, "TransitGatewayAddress": "169.254.6.2", "PeerAddress": "169.254.6.1", "BgpStatus": "down" }, { "TransitGatewayAsn": 64512, "PeerAsn": 64512, "TransitGatewayAddress": "169.254.6.3", "PeerAddress": "169.254.6.1", "BgpStatus": "down" } ] } } }`For more information, see [Transit gateway Connect attachments and Transit Gateway Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayConnectPeer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-connect-peer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-connect`.

- **AWS CLI**
- 
            
                    **To create a transit gateway Connect attachment**The following `create-transit-gateway-connect`example creates a Connect attachment, with the "gre" protocol, for the specified attachment.`aws ec2 create-transit-gateway-connect \ --transport-transit-gateway-attachment-id``tgw-attach-0a89069f57EXAMPLE`\ --options`"Protocol=gre"`Output: `{ "TransitGatewayConnect": { "TransitGatewayAttachmentId": "tgw-attach-037012e5dcEXAMPLE", "TransportTransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "State": "pending", "CreationTime": "2021-03-09T19:59:17+00:00", "Options": { "Protocol": "gre" } } }`For more information, see [Transit gateway Connect attachments and Transit Gateway Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayConnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-connect.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-multicast-domain`.

- **AWS CLI**
- 
            
                    **Example 1: To create an IGMP multicast domain**The following `create-transit-gateway-multicast-domain`example creates a multicast domain for the specified transit gateway. With static sources disabled, any instances in subnets associated with the multicast domain can send multicast traffic. If at least one member uses the IGMP protocol, you must enable IGMPv2 support.`aws ec2 create-transit-gateway-multicast-domain \ --transit-gateway-id``tgw-0bf0bffefaEXAMPLE`\ --options`StaticSourcesSupport=disable,Igmpv2Support=enable`Output: `{ "TransitGatewayMulticastDomain": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c9e29e2a7EXAMPLE", "TransitGatewayId": "tgw-0bf0bffefaEXAMPLE", "TransitGatewayMulticastDomainArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-multicast-domain/tgw-mcast-domain-0c9e29e2a7EXAMPLE", "OwnerId": "123456789012", "Options": { "Igmpv2Support": "enable", "StaticSourcesSupport": "disable", "AutoAcceptSharedAssociations": "disable" }, "State": "pending", "CreationTime": "2021-09-29T22:17:13.000Z" } }`**Example 2: To create a static multicast domain**The following `create-transit-gateway-multicast-domain`example creates a multicast domain for the specified transit gateway. With static sources enabled, you must statically add sources.`aws ec2 create-transit-gateway-multicast-domain \ --transit-gateway-id``tgw-0bf0bffefaEXAMPLE`\ --options`StaticSourcesSupport=enable,Igmpv2Support=disable`Output: `{ "TransitGatewayMulticastDomain": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-000fb24d04EXAMPLE", "TransitGatewayId": "tgw-0bf0bffefaEXAMPLE", "TransitGatewayMulticastDomainArn": "arn:aws:ec2:us-west-2:123456789012:transit-gateway-multicast-domain/tgw-mcast-domain-000fb24d04EXAMPLE", "OwnerId": "123456789012", "Options": { "Igmpv2Support": "disable", "StaticSourcesSupport": "enable", "AutoAcceptSharedAssociations": "disable" }, "State": "pending", "CreationTime": "2021-09-29T22:20:19.000Z" } }`For more information, see [Managing multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/manage-domain.html)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayMulticastDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-multicast-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-peering-attachment`.

- **AWS CLI**
- 
            
                    **To create a transit gateway peering attachment**The following `create-transit-gateway-peering-attachment`example creates a peering attachment request between the two specified transit gateways.`aws ec2 create-transit-gateway-peering-attachment \ --transit-gateway-id``tgw-123abc05e04123abc`\ --peer-transit-gateway-id`tgw-11223344aabbcc112`\ --peer-account-id`123456789012`\ --peer-region`us-east-2`Output: `{ "TransitGatewayPeeringAttachment": { "TransitGatewayAttachmentId": "tgw-attach-4455667788aabbccd", "RequesterTgwInfo": { "TransitGatewayId": "tgw-123abc05e04123abc", "OwnerId": "123456789012", "Region": "us-west-2" }, "AccepterTgwInfo": { "TransitGatewayId": "tgw-11223344aabbcc112", "OwnerId": "123456789012", "Region": "us-east-2" }, "State": "initiatingRequest", "CreationTime": "2019-12-09T11:38:05.000Z" } }`For more information, see [Transit Gateway Peering Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayPeeringAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-peering-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-policy-table`.

- **AWS CLI**
- 
            
                    **To create a transit gateway policy table**The following `create-transit-gateway-policy-table`example creates a transit gateway policy table for the specified transit gateway.`aws ec2 create-transit-gateway-policy-table \ --transit-gateway-id``tgw-067f8505c18f0bd6e`Output: `{ "TransitGatewayPolicyTable": { "TransitGatewayPolicyTableId": "tgw-ptb-0a16f134b78668a81", "TransitGatewayId": "tgw-067f8505c18f0bd6e", "State": "pending", "CreationTime": "2023-11-28T16:36:43+00:00" } }`For more information, see [Transit gateway policy tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-policy-tables.html)in the*Transit Gateway User Guide*.- 
                    For API details, see [CreateTransitGatewayPolicyTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-policy-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-prefix-list-reference`.

- **AWS CLI**
- 
            
                    **To create a reference to a prefix list**The following `create-transit-gateway-prefix-list-reference`example creates a reference to the specified prefix list in the specified transit gateway route table.`aws ec2 create-transit-gateway-prefix-list-reference \ --transit-gateway-route-table-id``tgw-rtb-0123456789abcd123`\ --prefix-list-id`pl-11111122222222333`\ --transit-gateway-attachment-id`tgw-attach-aaaaaabbbbbb11111`Output: `{ "TransitGatewayPrefixListReference": { "TransitGatewayRouteTableId": "tgw-rtb-0123456789abcd123", "PrefixListId": "pl-11111122222222333", "PrefixListOwnerId": "123456789012", "State": "pending", "Blackhole": false, "TransitGatewayAttachment": { "TransitGatewayAttachmentId": "tgw-attach-aaaaaabbbbbb11111", "ResourceType": "vpc", "ResourceId": "vpc-112233445566aabbc" } } }`For more information, see [Create a prefix list reference](https://docs.aws.amazon.com/vpc/latest/tgw/create-prefix-list-reference.html)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayPrefixListReference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-prefix-list-reference.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-route-table`.

- **AWS CLI**
- 
            
                    **To create a Transit Gateway Route Table**The following `create-transit-gateway-route-table`example creates a route table for the specified transit gateway.`aws ec2 create-transit-gateway-route-table \ --transit-gateway-id``tgw-0262a0e521EXAMPLE`Output: `{ "TransitGatewayRouteTable": { "TransitGatewayRouteTableId": "tgw-rtb-0960981be7EXAMPLE", "TransitGatewayId": "tgw-0262a0e521EXAMPLE", "State": "pending", "DefaultAssociationRouteTable": false, "DefaultPropagationRouteTable": false, "CreationTime": "2019-07-10T19:01:46.000Z" } }`For more information, see [Create a transit gateway route table](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#create-tgw-route-table)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-route`.

- **AWS CLI**
- 
            
                    **To create a transit gateway route**The following `create-transit-gateway-route`example creates a route, with the specified destination, for the specified route table.`aws ec2 create-transit-gateway-route \ --destination-cidr-block``10.0.2.0/24`\ --transit-gateway-route-table-id`tgw-rtb-0b6f6aaa01EXAMPLE`\ --transit-gateway-attachment-id`tgw-attach-0b5968d3b6EXAMPLE`Output: `{ "Route": { "DestinationCidrBlock": "10.0.2.0/24", "TransitGatewayAttachments": [ { "ResourceId": "vpc-0065acced4EXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-0b5968d3b6EXAMPLE", "ResourceType": "vpc" } ], "Type": "static", "State": "active" } }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway-vpc-attachment`.

- **AWS CLI**
- 
            
                    **Example 1: To associate a transit gateway with a VPC**The following `create-transit-gateway-vpc-attachment`example creates a transit gateway attachment to the specified VPC.`aws ec2 create-transit-gateway-vpc-attachment \ --transit-gateway-id``tgw-0262a0e521EXAMPLE`\ --vpc-id`vpc-07e8ffd50f49335df`\ --subnet-id`subnet-0752213d59EXAMPLE`Output: `{ "TransitGatewayVpcAttachment": { "TransitGatewayAttachmentId": "tgw-attach-0a34fe6b4fEXAMPLE", "TransitGatewayId": "tgw-0262a0e521EXAMPLE", "VpcId": "vpc-07e8ffd50fEXAMPLE", "VpcOwnerId": "111122223333", "State": "pending", "SubnetIds": [ "subnet-0752213d59EXAMPLE" ], "CreationTime": "2019-07-10T17:33:46.000Z", "Options": { "DnsSupport": "enable", "Ipv6Support": "disable" } } }`For more information, see [Create a transit gateway attachment to a VPC](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#create-vpc-attachment)in the*Transit Gateways Guide*.**Example 2: To associate a transit gateway with multiple subnets in a VPC**The following `create-transit-gateway-vpc-attachment`example creates a transit gateway attachment to the specified VPC and subnets.`aws ec2 create-transit-gateway-vpc-attachment \ --transit-gateway-id``tgw-02f776b1a7EXAMPLE`\ --vpc-id`vpc-3EXAMPLE`\ --subnet-ids`"subnet-dEXAMPLE"``"subnet-6EXAMPLE"`Output: `{ "TransitGatewayVpcAttachment": { "TransitGatewayAttachmentId": "tgw-attach-0e141e0bebEXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "VpcId": "vpc-3EXAMPLE", "VpcOwnerId": "111122223333", "State": "pending", "SubnetIds": [ "subnet-6EXAMPLE", "subnet-dEXAMPLE" ], "CreationTime": "2019-12-17T20:07:52.000Z", "Options": { "DnsSupport": "enable", "Ipv6Support": "disable" } } }`For more information, see [Create a transit gateway attachment to a VPC](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#create-vpc-attachment)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGatewayVpcAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway-vpc-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-gateway`.

- **AWS CLI**
- 
            
                    **To create a transit gateway**The following `create-transit-gateway`example creates a transit gateway.`aws ec2 create-transit-gateway \ --description``MyTGW`\ --options`AmazonSideAsn=64516,AutoAcceptSharedAttachments=enable,DefaultRouteTableAssociation=enable,DefaultRouteTablePropagation=enable,VpnEcmpSupport=enable,DnsSupport=enable`Output: `{ "TransitGateway": { "TransitGatewayId": "tgw-0262a0e521EXAMPLE", "TransitGatewayArn": "arn:aws:ec2:us-east-2:111122223333:transit-gateway/tgw-0262a0e521EXAMPLE", "State": "pending", "OwnerId": "111122223333", "Description": "MyTGW", "CreationTime": "2019-07-10T14:02:12.000Z", "Options": { "AmazonSideAsn": 64516, "AutoAcceptSharedAttachments": "enable", "DefaultRouteTableAssociation": "enable", "AssociationDefaultRouteTableId": "tgw-rtb-018774adf3EXAMPLE", "DefaultRouteTablePropagation": "enable", "PropagationDefaultRouteTableId": "tgw-rtb-018774adf3EXAMPLE", "VpnEcmpSupport": "enable", "DnsSupport": "enable" } } }`For more information, see [Create a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#create-tgw)in the*Transit Gateways Guide*.- 
                    For API details, see [CreateTransitGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-transit-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-verified-access-endpoint`.

- **AWS CLI**
- 
            
                    **To create a Verified Access endpoint**The following `create-verified-access-endpoint`example creates a Verified Access endpoint for the specified Verified Access group. The specified network interface and security group must belong to the same VPC.`aws ec2 create-verified-access-endpoint \ --verified-access-group-id``vagr-0dbe967baf14b7235`\ --endpoint-type`network-interface`\ --attachment-type`vpc`\ --domain-certificate-arn`arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE`\ --application-domain`example.com`\ --endpoint-domain-prefix`my-ava-app`\ --security-group-ids`sg-004915970c4c8f13a`\ --network-interface-options`NetworkInterfaceId=eni-0aec70418c8d87a0f,Protocol=https,Port=443`\ --tag-specifications`ResourceType=verified-access-endpoint,Tags=[{Key=Name,Value=my-va-endpoint}]`Output: `{ "VerifiedAccessEndpoint": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessEndpointId": "vae-066fac616d4d546f2", "ApplicationDomain": "example.com", "EndpointType": "network-interface", "AttachmentType": "vpc", "DomainCertificateArn": "arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE", "EndpointDomain": "my-ava-app.edge-00c3372d53b1540bb.vai-0ce000c0b7643abea.prod.verified-access.us-east-2.amazonaws.com", "SecurityGroupIds": [ "sg-004915970c4c8f13a" ], "NetworkInterfaceOptions": { "NetworkInterfaceId": "eni-0aec70418c8d87a0f", "Protocol": "https", "Port": 443 }, "Status": { "Code": "pending" }, "Description": "", "CreationTime": "2023-08-25T20:54:43", "LastUpdatedTime": "2023-08-25T20:54:43", "Tags": [ { "Key": "Name", "Value": "my-va-endpoint" } ] } }`For more information, see [Verified Access endpoints](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [CreateVerifiedAccessEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-verified-access-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-verified-access-group`.

- **AWS CLI**
- 
            
                    **To create a Verified Access group**The following `create-verified-access-group`example creates a Verified Access group for the specified Verified Access instance.`aws ec2 create-verified-access-group \ --verified-access-instance-id``vai-0ce000c0b7643abea`\ --tag-specifications`ResourceType=verified-access-group,Tags=[{Key=Name,Value=my-va-group}]`Output: `{ "VerifiedAccessGroup": { "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "", "Owner": "123456789012", "VerifiedAccessGroupArn": "arn:aws:ec2:us-east-2:123456789012:verified-access-group/vagr-0dbe967baf14b7235", "CreationTime": "2023-08-25T19:55:19", "LastUpdatedTime": "2023-08-25T19:55:19", "Tags": [ { "Key": "Name", "Value": "my-va-group" } ] } }`For more information, see [Verified Access groups](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [CreateVerifiedAccessGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-verified-access-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-verified-access-instance`.

- **AWS CLI**
- 
            
                    **To create a Verified Access instance**The following `create-verified-access-instance`example creates a Verified Access instance with a Name tag.`aws ec2 create-verified-access-instance \ --tag-specifications``ResourceType=verified-access-instance,Tags=[{Key=Name,Value=my-va-instance}]`Output: `{ "VerifiedAccessInstance": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "", "VerifiedAccessTrustProviders": [], "CreationTime": "2023-08-25T18:27:56", "LastUpdatedTime": "2023-08-25T18:27:56", "Tags": [ { "Key": "Name", "Value": "my-va-instance" } ] } }`For more information, see [Verified Access instances](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-instances.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [CreateVerifiedAccessInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-verified-access-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-verified-access-trust-provider`.

- **AWS CLI**
- 
            
                    **To create a Verified Access trust provider**The following `create-verified-access-trust-provider`example sets up a Verified Access trust provider using AWS Identity Center.`aws ec2 create-verified-access-trust-provider \ --trust-provider-type``user`\ --user-trust-provider-type`iam-identity-center`\ --policy-reference-name`idc`\ --tag-specifications`ResourceType=verified-access-trust-provider,Tags=[{Key=Name,Value=my-va-trust-provider}]`Output: `{ "VerifiedAccessTrustProvider": { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "Description": "", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center", "PolicyReferenceName": "idc", "CreationTime": "2023-08-25T18:40:36", "LastUpdatedTime": "2023-08-25T18:40:36", "Tags": [ { "Key": "Name", "Value": "my-va-trust-provider" } ] } }`For more information, see [Trust providers for Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/trust-providers.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [CreateVerifiedAccessTrustProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-verified-access-trust-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-volume`.

- **AWS CLI**
- 
            
                    **To create an empty General Purpose SSD (gp2) volume**The following `create-volume`example creates an 80 GiB General Purpose SSD (gp2) volume in the specified Availability Zone. Note that the current Region must be`us-east-1`, or you can add the`--region`parameter to specify the Region for the command.`aws ec2 create-volume \ --volume-type``gp2`\ --size`80`\ --availability-zone`us-east-1a`Output: `{ "AvailabilityZone": "us-east-1a", "Tags": [], "Encrypted": false, "VolumeType": "gp2", "VolumeId": "vol-1234567890abcdef0", "State": "creating", "Iops": 240, "SnapshotId": "", "CreateTime": "YYYY-MM-DDTHH:MM:SS.000Z", "Size": 80 }`If you do not specify a volume type, the default volume type is `gp2`.`aws ec2 create-volume \ --size``80`\ --availability-zone`us-east-1a`**Example 2: To create a Provisioned IOPS SSD (io1) volume from a snapshot**The following `create-volume`example creates a Provisioned IOPS SSD (io1) volume with 1000 provisioned IOPS in the specified Availability Zone using the specified snapshot.`aws ec2 create-volume \ --volume-type``io1`\ --iops`1000`\ --snapshot-id`snap-066877671789bd71b`\ --availability-zone`us-east-1a`Output: `{ "AvailabilityZone": "us-east-1a", "Tags": [], "Encrypted": false, "VolumeType": "io1", "VolumeId": "vol-1234567890abcdef0", "State": "creating", "Iops": 1000, "SnapshotId": "snap-066877671789bd71b", "CreateTime": "YYYY-MM-DDTHH:MM:SS.000Z", "Size": 500 }`**Example 3: To create an encrypted volume**The following `create-volume`example creates an encrypted volume using the default CMK for EBS encryption. If encryption by default is disabled, you must specify the`--encrypted`parameter as follows.`aws ec2 create-volume \ --size``80`\ --encrypted \ --availability-zone`us-east-1a`Output: `{ "AvailabilityZone": "us-east-1a", "Tags": [], "Encrypted": true, "VolumeType": "gp2", "VolumeId": "vol-1234567890abcdef0", "State": "creating", "Iops": 240, "SnapshotId": "", "CreateTime": "YYYY-MM-DDTHH:MM:SS.000Z", "Size": 80 }`If encryption by default is enabled, the following example command creates an encrypted volume, even without the `--encrypted`parameter.`aws ec2 create-volume \ --size``80`\ --availability-zone`us-east-1a`If you use the `--kms-key-id`parameter to specify a customer managed CMK, you must specify the`--encrypted`parameter even if encryption by default is enabled.`aws ec2 create-volume \ --volume-type``gp2`\ --size`80`\ --encrypted \ --kms-key-id`0ea3fef3-80a7-4778-9d8c-1c0c6EXAMPLE`\ --availability-zone`us-east-1a`**Example 4: To create a volume with tags**The following `create-volume`example creates a volume and adds two tags.`aws ec2 create-volume \ --availability-zone``us-east-1a`\ --volume-type`gp2`\ --size`80`\ --tag-specifications '`ResourceType=volume,Tags=[{Key=purpose,Value=production},{Key=cost-center,Value=cc123}]`'- 
                    For API details, see [CreateVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-volume.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpc-endpoint-connection-notification`.

- **AWS CLI**
- 
            
                    **To create an endpoint connection notification**This example creates a notification for a specific endpoint service that alerts you when interface endpoints have connected to your service and when endpoints have been accepted for your service. Command: `aws ec2 create-vpc-endpoint-connection-notification --connection-notification-arn``arn:aws:sns:us-east-2:123456789012:VpceNotification`--connection-events`Connect``Accept`--service-id`vpce-svc-1237881c0d25a3abc`Output: `{ "ConnectionNotification": { "ConnectionNotificationState": "Enabled", "ConnectionNotificationType": "Topic", "ServiceId": "vpce-svc-1237881c0d25a3abc", "ConnectionEvents": [ "Accept", "Connect" ], "ConnectionNotificationId": "vpce-nfn-008776de7e03f5abc", "ConnectionNotificationArn": "arn:aws:sns:us-east-2:123456789012:VpceNotification" } }`- 
                    For API details, see [CreateVpcEndpointConnectionNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint-connection-notification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpc-endpoint-service-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To create an endpoint service configuration for an interface endpoint**The following `create-vpc-endpoint-service-configuration`example creates a VPC endpoint service configuration using the Network Load Balancer`nlb-vpce`. This example also specifies that requests to connect to the service through an interface endpoint must be accepted.`aws ec2 create-vpc-endpoint-service-configuration \ --network-load-balancer-arns``arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532`\ --acceptance-requiredOutput: `{ "ServiceConfiguration": { "ServiceType": [ { "ServiceType": "Interface" } ], "NetworkLoadBalancerArns": [ "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532" ], "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-03d5ebb7d9579a2b3", "ServiceState": "Available", "ServiceId": "vpce-svc-03d5ebb7d9579a2b3", "AcceptanceRequired": true, "AvailabilityZones": [ "us-east-1d" ], "BaseEndpointDnsNames": [ "vpce-svc-03d5ebb7d9579a2b3.us-east-1.vpce.amazonaws.com" ] } }`For more information, see [Create an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html)in the*AWS PrivateLink User Guide*.**Example 2: To create an endpoint service configuration for a Gateway Load Balancer endpoint**The following `create-vpc-endpoint-service-configuration`example creates a VPC endpoint service configuration using the Gateway Load Balancer`GWLBService`. Requests to connect to the service through a Gateway Load Balancer endpoint are automatically accepted.`aws ec2 create-vpc-endpoint-service-configuration \ --gateway-load-balancer-arns``arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/123123123123abcc`\ --no-acceptance-requiredOutput: `{ "ServiceConfiguration": { "ServiceType": [ { "ServiceType": "GatewayLoadBalancer" } ], "ServiceId": "vpce-svc-123123a1c43abc123", "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123", "ServiceState": "Available", "AvailabilityZones": [ "us-east-1d" ], "AcceptanceRequired": false, "ManagesVpcEndpoints": false, "GatewayLoadBalancerArns": [ "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/123123123123abcc" ] } }`For more information, see [Create a Gateway Load Balancer endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-gateway-load-balancer-endpoint-service.html)in the*AWS PrivateLink User Guide*.- 
                    For API details, see [CreateVpcEndpointServiceConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint-service-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpc-endpoint`.

- **AWS CLI**
- 
            
                    **Example 1: To create a gateway endpoint**The following `create-vpc-endpoint`example creates a gateway VPC endpoint between VPC`vpc-1a2b3c4d`and Amazon S3 in the`us-east-1`region, and associates route table`rtb-11aa22bb`with the endpoint.`aws ec2 create-vpc-endpoint \ --vpc-id``vpc-1a2b3c4d`\ --service-name`com.amazonaws.us-east-1.s3`\ --route-table-ids`rtb-11aa22bb`Output: `{ "VpcEndpoint": { "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Sid\":\"\",\"Effect\":\"Allow\",\"Principal\":\"\*\",\"Action\":\"\*\",\"Resource\":\"\*\"}]}", "VpcId": "vpc-1a2b3c4d", "State": "available", "ServiceName": "com.amazonaws.us-east-1.s3", "RouteTableIds": [ "rtb-11aa22bb" ], "VpcEndpointId": "vpc-1a2b3c4d", "CreationTimestamp": "2015-05-15T09:40:50Z" } }`For more information, see [Create a gateway endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html#create-gateway-endpoint-s3)in the*AWS PrivateLink User Guide*.**Example 2: To create an interface endpoint**The following `create-vpc-endpoint`example creates an interface VPC endpoint between VPC`vpc-1a2b3c4d`and Amazon S3 in the`us-east-1`region. The command creates the endpoint in subnet`subnet-1a2b3c4d`, associates it with security group`sg-1a2b3c4d`, and adds a tag with a key of "Service" and a Value of "S3".`aws ec2 create-vpc-endpoint \ --vpc-id``vpc-1a2b3c4d`\ --vpc-endpoint-type`Interface`\ --service-name`com.amazonaws.us-east-1.s3`\ --subnet-ids`subnet-7b16de0c`\ --security-group-id`sg-1a2b3c4d`\ --tag-specifications`ResourceType=vpc-endpoint,Tags=[{Key=service,Value=S3}]`Output: `{ "VpcEndpoint": { "VpcEndpointId": "vpce-1a2b3c4d5e6f1a2b3", "VpcEndpointType": "Interface", "VpcId": "vpc-1a2b3c4d", "ServiceName": "com.amazonaws.us-east-1.s3", "State": "pending", "RouteTableIds": [], "SubnetIds": [ "subnet-1a2b3c4d" ], "Groups": [ { "GroupId": "sg-1a2b3c4d", "GroupName": "default" } ], "PrivateDnsEnabled": false, "RequesterManaged": false, "NetworkInterfaceIds": [ "eni-0b16f0581c8ac6877" ], "DnsEntries": [ { "DnsName": "*.vpce-1a2b3c4d5e6f1a2b3-9hnenorg.s3.us-east-1.vpce.amazonaws.com", "HostedZoneId": "Z7HUB22UULQXV" }, { "DnsName": "*.vpce-1a2b3c4d5e6f1a2b3-9hnenorg-us-east-1c.s3.us-east-1.vpce.amazonaws.com", "HostedZoneId": "Z7HUB22UULQXV" } ], "CreationTimestamp": "2021-03-05T14:46:16.030000+00:00", "Tags": [ { "Key": "service", "Value": "S3" } ], "OwnerId": "123456789012" } }`For more information, see [Create an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html)in the*AWS PrivateLink User Guide*.**Example 3: To create a Gateway Load Balancer endpoint**The following `create-vpc-endpoint`example creates a Gateway Load Balancer endpoint between VPC`vpc-111122223333aabbc`and and a service that is configured using a Gateway Load Balancer.`aws ec2 create-vpc-endpoint \ --service-name``com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123`\ --vpc-endpoint-type`GatewayLoadBalancer`\ --vpc-id`vpc-111122223333aabbc`\ --subnet-ids`subnet-0011aabbcc2233445`Output: `{ "VpcEndpoint": { "VpcEndpointId": "vpce-aabbaabbaabbaabba", "VpcEndpointType": "GatewayLoadBalancer", "VpcId": "vpc-111122223333aabbc", "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123", "State": "pending", "SubnetIds": [ "subnet-0011aabbcc2233445" ], "RequesterManaged": false, "NetworkInterfaceIds": [ "eni-01010120203030405" ], "CreationTimestamp": "2020-11-11T08:06:03.522Z", "OwnerId": "123456789012" } }`For more information, see [Gateway Load Balancer endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/gateway-load-balancer-endpoints.html)in the*AWS PrivateLink User Guide*.**Example 4: To create a resource endpoint**The following `create-vpc-endpoint`example creates a resource endpoint.`aws ec2 create-vpc-endpoint \ --vpc-endpoint-type``Resource`\ --vpc-id`vpc-111122223333aabbc`\ --subnet-ids`subnet-0011aabbcc2233445`\ --resource-configuration-arn`arn:aws:vpc-lattice-us-east-1:123456789012:resourceconfiguration/rcfg-0123abcde98765432`Output: `{ "VpcEndpoint": { "VpcEndpointId": "vpce-00939a7ed9EXAMPLE", "VpcEndpointType": "Resource", "VpcId": "vpc-111122223333aabbc", "State": "Pending", "SubnetIds": [ "subnet-0011aabbcc2233445" ], "Groups": [ { "GroupId": "sg-03e2f15fbfc09b000", "GroupName": "default" } ], "IpAddressType": "IPV4", "PrivateDnsEnabled": false, "CreationTimestamp": "2025-02-06T23:38:49.525000+00:00", "Tags": [], "OwnerId": "123456789012", "ResourceConfigurationArn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-0123abcde98765432" } }`For more information, see [Resource endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-resources.html)in the*AWS PrivateLink User Guide*.**Example 5: To create a service network endpoint**The following `create-vpc-endpoint`example creates a service network endpoint.`aws ec2 create-vpc-endpoint \ --vpc-endpoint-type``ServiceNetwork`\ --vpc-id`vpc-111122223333aabbc`\ --subnet-ids`subnet-0011aabbcc2233445`\ --service-network-arn`arn:aws:vpc-lattice:us-east-1:123456789012:servicenetwork/sn-0101abcd5432abcd0`\ --security-group-ids`sg-0123456789012abcd`Output: `{ "VpcEndpoint": { "VpcEndpointId": "vpce-0f00567fa8EXAMPLE", "VpcEndpointType": "ServiceNetwork", "VpcId": "vpc-111122223333aabbc", "State": "Pending", "SubnetIds": [ "subnet-0011aabbcc2233445" ], "Groups": [ { "GroupId": "sg-0123456789012abcd", "GroupName": "my-security-group" } ], "IpAddressType": "IPV4", "PrivateDnsEnabled": false, "CreationTimestamp": "2025-02-06T23:44:20.449000+00:00", "Tags": [], "OwnerId": "123456789012", "ServiceNetworkArn": "arn:aws:vpc-lattice:us-east-1:123456789012:servicenetwork/sn-0101abcd5432abcd0" } }`For more information, see [Service network endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-service-networks.html)in the*AWS PrivateLink User Guide*.- 
                    For API details, see [CreateVpcEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpc-peering-connection`.

- **AWS CLI**
- 
            
                    **To create a VPC peering connection between your VPCs**This example requests a peering connection between your VPCs vpc-1a2b3c4d and vpc-11122233. Command: `aws ec2 create-vpc-peering-connection --vpc-id``vpc-1a2b3c4d`--peer-vpc-id`vpc-11122233`Output: `{ "VpcPeeringConnection": { "Status": { "Message": "Initiating Request to 444455556666", "Code": "initiating-request" }, "Tags": [], "RequesterVpcInfo": { "OwnerId": "444455556666", "VpcId": "vpc-1a2b3c4d", "CidrBlock": "10.0.0.0/28" }, "VpcPeeringConnectionId": "pcx-111aaa111", "ExpirationTime": "2014-04-02T16:13:36.000Z", "AccepterVpcInfo": { "OwnerId": "444455556666", "VpcId": "vpc-11122233" } } }`**To create a VPC peering connection with a VPC in another account**This example requests a peering connection between your VPC (vpc-1a2b3c4d), and a VPC (vpc-11122233) that belongs AWS account 123456789012. Command: `aws ec2 create-vpc-peering-connection --vpc-id``vpc-1a2b3c4d`--peer-vpc-id`vpc-11122233`--peer-owner-id`123456789012`**To create a VPC peering connection with a VPC in a different region**This example requests a peering connection between your VPC in the current region (vpc-1a2b3c4d), and a VPC (vpc-11122233) in your account in the `us-west-2`region.Command: `aws ec2 create-vpc-peering-connection --vpc-id``vpc-1a2b3c4d`--peer-vpc-id`vpc-11122233`--peer-region`us-west-2`This example requests a peering connection between your VPC in the current region (vpc-1a2b3c4d), and a VPC (vpc-11122233) that belongs AWS account 123456789012 that's in the `us-west-2`region.Command: `aws ec2 create-vpc-peering-connection --vpc-id``vpc-1a2b3c4d`--peer-vpc-id`vpc-11122233`--peer-owner-id`123456789012`--peer-region`us-west-2`- 
                    For API details, see [CreateVpcPeeringConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-peering-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpc`.

- **AWS CLI**
- 
            
                    **Example 1: To create a VPC**The following `create-vpc`example creates a VPC with the specified IPv4 CIDR block and a Name tag.`aws ec2 create-vpc \ --cidr-block``10.0.0.0/16`\ --tag-specifications`ResourceType=vpc,Tags=[{Key=Name,Value=MyVpc}]`Output: `{ "Vpc": { "CidrBlock": "10.0.0.0/16", "DhcpOptionsId": "dopt-5EXAMPLE", "State": "pending", "VpcId": "vpc-0a60eb65b4EXAMPLE", "OwnerId": "123456789012", "InstanceTenancy": "default", "Ipv6CidrBlockAssociationSet": [], "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-07501b79ecEXAMPLE", "CidrBlock": "10.0.0.0/16", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false, "Tags": [ { "Key": "Name", "Value": MyVpc" } ] } }`**Example 2: To create a VPC with dedicated tenancy**The following `create-vpc`example creates a VPC with the specified IPv4 CIDR block and dedicated tenancy.`aws ec2 create-vpc \ --cidr-block``10.0.0.0/16`\ --instance-tenancy`dedicated`Output: `{ "Vpc": { "CidrBlock": "10.0.0.0/16", "DhcpOptionsId": "dopt-19edf471", "State": "pending", "VpcId": "vpc-0a53287fa4EXAMPLE", "OwnerId": "111122223333", "InstanceTenancy": "dedicated", "Ipv6CidrBlockAssociationSet": [], "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-00b24cc1c2EXAMPLE", "CidrBlock": "10.0.0.0/16", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false } }`**Example 3: To create a VPC with an IPv6 CIDR block**The following `create-vpc`example creates a VPC with an Amazon-provided IPv6 CIDR block.`aws ec2 create-vpc \ --cidr-block``10.0.0.0/16`\ --amazon-provided-ipv6-cidr-blockOutput: `{ "Vpc": { "CidrBlock": "10.0.0.0/16", "DhcpOptionsId": "dopt-dEXAMPLE", "State": "pending", "VpcId": "vpc-0fc5e3406bEXAMPLE", "OwnerId": "123456789012", "InstanceTenancy": "default", "Ipv6CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-068432c60bEXAMPLE", "Ipv6CidrBlock": "", "Ipv6CidrBlockState": { "State": "associating" }, "Ipv6Pool": "Amazon", "NetworkBorderGroup": "us-west-2" } ], "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-0669f8f9f5EXAMPLE", "CidrBlock": "10.0.0.0/16", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false } }`**Example 4: To create a VPC with a CIDR from an IPAM pool**The following `create-vpc`example creates a VPC with a CIDR from an Amazon VPC IP Address Manager (IPAM) pool.Linux and macOS: `aws ec2 create-vpc \ --ipv4-ipam-pool-id``ipam-pool-0533048da7d823723`\ --tag-specifications ResourceType=vpc,Tags='[{Key=Environment,Value="Preprod"},{Key=Owner,Value="Build Team"}]'Windows: `aws ec2 create-vpc``^`--ipv4-ipam-pool-id`ipam-pool-0533048da7d823723``^`--tag-specifications ResourceType=vpc,Tags=[{Key=Environment,Value="Preprod"},{Key=Owner,Value="Build Team"}]Output: `{ "Vpc": { "CidrBlock": "10.0.1.0/24", "DhcpOptionsId": "dopt-2afccf50", "State": "pending", "VpcId": "vpc-010e1791024eb0af9", "OwnerId": "123456789012", "InstanceTenancy": "default", "Ipv6CidrBlockAssociationSet": [], "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-0a77de1d803226d4b", "CidrBlock": "10.0.1.0/24", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false, "Tags": [ { "Key": "Environment", "Value": "Preprod" }, { "Key": "Owner", "Value": "Build Team" } ] } }`For more information, see [Create a VPC that uses an IPAM pool CIDR](https://docs.aws.amazon.com/vpc/latest/ipam/create-vpc-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [CreateVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpn-connection-route`.

- **AWS CLI**
- 
            
                    **To create a static route for a VPN connection**This example creates a static route for the specified VPN connection. If the command succeeds, no output is returned. Command: `aws ec2 create-vpn-connection-route --vpn-connection-id``vpn-40f41529`--destination-cidr-block`11.12.0.0/16`- 
                    For API details, see [CreateVpnConnectionRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpn-connection`.

- **AWS CLI**
- 
            
                    **Example 1: To create a VPN connection with dynamic routing**The following `create-vpn-connection`example creates a VPN connection between the specified virtual private gateway and the specified customer gateway, and applies tags to the VPN connection. The output includes the configuration information for your customer gateway device, in XML format.`aws ec2 create-vpn-connection \ --type``ipsec.1`\ --customer-gateway-id`cgw-001122334455aabbc`\ --vpn-gateway-id`vgw-1a1a1a1a1a1a2b2b2`\ --tag-specification '`ResourceType=vpn-connection,Tags=[{Key=Name,Value=BGP-VPN}]`'Output: `{ "VpnConnection": { "CustomerGatewayConfiguration": "...configuration information...", "CustomerGatewayId": "cgw-001122334455aabbc", "Category": "VPN", "State": "pending", "VpnConnectionId": "vpn-123123123123abcab", "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2", "Options": { "EnableAcceleration": false, "StaticRoutesOnly": false, "LocalIpv4NetworkCidr": "0.0.0.0/0", "RemoteIpv4NetworkCidr": "0.0.0.0/0", "TunnelInsideIpVersion": "ipv4", "TunnelOptions": [ {}, {} ] }, "Routes": [], "Tags": [ { "Key": "Name", "Value": "BGP-VPN" } ] } }`For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)in the*AWS Site-to-Site VPN User Guide*.**Example 2: To create a VPN connection with static routing**The following `create-vpn-connection`example creates a VPN connection between the specified virtual private gateway and the specified customer gateway. The options specify static routing. The output includes the configuration information for your customer gateway device, in XML format.`aws ec2 create-vpn-connection \ --type``ipsec.1`\ --customer-gateway-id`cgw-001122334455aabbc`\ --vpn-gateway-id`vgw-1a1a1a1a1a1a2b2b2`\ --options "{\"StaticRoutesOnly\":true}"Output: `{ "VpnConnection": { "CustomerGatewayConfiguration": "..configuration information...", "CustomerGatewayId": "cgw-001122334455aabbc", "Category": "VPN", "State": "pending", "VpnConnectionId": "vpn-123123123123abcab", "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2", "Options": { "EnableAcceleration": false, "StaticRoutesOnly": true, "LocalIpv4NetworkCidr": "0.0.0.0/0", "RemoteIpv4NetworkCidr": "0.0.0.0/0", "TunnelInsideIpVersion": "ipv4", "TunnelOptions": [ {}, {} ] }, "Routes": [], "Tags": [] } }`For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)in the*AWS Site-to-Site VPN User Guide*.**Example 3: To create a VPN connection and specify your own inside CIDR and pre-shared key**The following `create-vpn-connection`example creates a VPN connection and specifies the inside IP address CIDR block and a custom pre-shared key for each tunnel. The specified values are returned in the`CustomerGatewayConfiguration`information.`aws ec2 create-vpn-connection \ --type``ipsec.1`\ --customer-gateway-id`cgw-001122334455aabbc`\ --vpn-gateway-id`vgw-1a1a1a1a1a1a2b2b2`\ --options TunnelOptions='[{TunnelInsideCidr=169.254.12.0/30,PreSharedKey=ExamplePreSharedKey1},{TunnelInsideCidr=169.254.13.0/30,PreSharedKey=ExamplePreSharedKey2}]'Output: `{ "VpnConnection": { "CustomerGatewayConfiguration": "..configuration information...", "CustomerGatewayId": "cgw-001122334455aabbc", "Category": "VPN", "State": "pending", "VpnConnectionId": "vpn-123123123123abcab", "VpnGatewayId": "vgw-1a1a1a1a1a1a2b2b2", "Options": { "EnableAcceleration": false, "StaticRoutesOnly": false, "LocalIpv4NetworkCidr": "0.0.0.0/0", "RemoteIpv4NetworkCidr": "0.0.0.0/0", "TunnelInsideIpVersion": "ipv4", "TunnelOptions": [ { "OutsideIpAddress": "203.0.113.3", "TunnelInsideCidr": "169.254.12.0/30", "PreSharedKey": "ExamplePreSharedKey1" }, { "OutsideIpAddress": "203.0.113.5", "TunnelInsideCidr": "169.254.13.0/30", "PreSharedKey": "ExamplePreSharedKey2" } ] }, "Routes": [], "Tags": [] } }`For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)in the*AWS Site-to-Site VPN User Guide*.**Example 4: To create a VPN connection that supports IPv6 traffic**The following `create-vpn-connection`example creates a VPN connection that supports IPv6 traffic between the specified transit gateway and specified customer gateway. The tunnel options for both tunnels specify that AWS must initiate the IKE negotiation.`aws ec2 create-vpn-connection \ --type``ipsec.1`\ --transit-gateway-id`tgw-12312312312312312`\ --customer-gateway-id`cgw-001122334455aabbc`\ --options`TunnelInsideIpVersion=ipv6,TunnelOptions=[{StartupAction=start},{StartupAction=start}]`Output: `{ "VpnConnection": { "CustomerGatewayConfiguration": "..configuration information...", "CustomerGatewayId": "cgw-001122334455aabbc", "Category": "VPN", "State": "pending", "VpnConnectionId": "vpn-11111111122222222", "TransitGatewayId": "tgw-12312312312312312", "Options": { "EnableAcceleration": false, "StaticRoutesOnly": false, "LocalIpv6NetworkCidr": "::/0", "RemoteIpv6NetworkCidr": "::/0", "TunnelInsideIpVersion": "ipv6", "TunnelOptions": [ { "OutsideIpAddress": "203.0.113.3", "StartupAction": "start" }, { "OutsideIpAddress": "203.0.113.5", "StartupAction": "start" } ] }, "Routes": [], "Tags": [] } }`For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)in the*AWS Site-to-Site VPN User Guide*.- 
                    For API details, see [CreateVpnConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpn-gateway`.

- **AWS CLI**
- 
            
                    **To create a virtual private gateway**This example creates a virtual private gateway. Command: `aws ec2 create-vpn-gateway --type``ipsec.1`Output: `{ "VpnGateway": { "AmazonSideAsn": 64512, "State": "available", "Type": "ipsec.1", "VpnGatewayId": "vgw-9a4cacf3", "VpcAttachments": [] } }`**To create a virtual private gateway with a specific Amazon-side ASN**This example creates a virtual private gateway and specifies the Autonomous System Number (ASN) for the Amazon side of the BGP session. Command: `aws ec2 create-vpn-gateway --type``ipsec.1`--amazon-side-asn`65001`Output: `{ "VpnGateway": { "AmazonSideAsn": 65001, "State": "available", "Type": "ipsec.1", "VpnGatewayId": "vgw-9a4cacf3", "VpcAttachments": [] } }`- 
                    For API details, see [CreateVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-carrier-gateway`.

- **AWS CLI**
- 
            
                    **To delete your carrier gateway**The following `delete-carrier-gateway`example deletes the specified carrier gateway.`aws ec2 delete-carrier-gateway \ --carrier-gateway-id``cagw-0465cdEXAMPLE1111`Output: `{ "CarrierGateway": { "CarrierGatewayId": "cagw-0465cdEXAMPLE1111", "VpcId": "vpc-0c529aEXAMPLE1111", "State": "deleting", "OwnerId": "123456789012" } }`For more information, see [Carrier gateways](https://docs.aws.amazon.com/vpc/latest/userguide/Carrier_Gateway.html)in the*Amazon Virtual Private Cloud User Guide*.- 
                    For API details, see [DeleteCarrierGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-carrier-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-client-vpn-endpoint`.

- **AWS CLI**
- 
            
                    **To delete a Client VPN endpoint**The following `delete-client-vpn-endpoint`example deletes the specified Client VPN endpoint.`aws ec2 delete-client-vpn-endpoint \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`Output: `{ "Status": { "Code": "deleting" } }`For more information, see [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DeleteClientVpnEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-client-vpn-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-client-vpn-route`.

- **AWS CLI**
- 
            
                    **To delete a route for a Client VPN endpoint**The following `delete-client-vpn-route`example deletes the`0.0.0.0/0`route for the specified subnet of a Client VPN endpoint.`aws ec2 delete-client-vpn-route \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --destination-cidr-block`0.0.0.0/0`\ --target-vpc-subnet-id`subnet-0123456789abcabca`Output: `{ "Status": { "Code": "deleting" } }`For more information, see [Routes](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DeleteClientVpnRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-client-vpn-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-coip-cidr`.

- **AWS CLI**
- 
            
                    **To delete a range of customer-owned IP (CoIP) addresses**The following `delete-coip-cidr`example deletes the specified range of CoIP addresses in the specified CoIP pool.`aws ec2 delete-coip-cidr \ --cidr``14.0.0.0/24`\ --coip-pool-id`ipv4pool-coip-1234567890abcdefg`Output: `{ "CoipCidr": { "Cidr": "14.0.0.0/24", "CoipPoolId": "ipv4pool-coip-1234567890abcdefg", "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890" } }`For more information, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing)in the*AWS Outposts User Guide*.- 
                    For API details, see [DeleteCoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-coip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-coip-pool`.

- **AWS CLI**
- 
            
                    **To delete a pool of customer-owned IP (CoIP) addresses**The following `delete-coip-pool`example deletes a CoIP pool of CoIP addresses.`aws ec2 delete-coip-pool \ --coip-pool-id``ipv4pool-coip-1234567890abcdefg`Output: `{ "CoipPool": { "PoolId": "ipv4pool-coip-1234567890abcdefg", "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890", "PoolArn": "arn:aws:ec2:us-west-2:123456789012:coip-pool/ipv4pool-coip-1234567890abcdefg" } }`For more information, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing)in the*AWS Outposts User Guide*.- 
                    For API details, see [DeleteCoipPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-coip-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-customer-gateway`.

- **AWS CLI**
- 
            
                    **To delete a customer gateway**This example deletes the specified customer gateway. If the command succeeds, no output is returned. Command: `aws ec2 delete-customer-gateway --customer-gateway-id``cgw-0e11f167`- 
                    For API details, see [DeleteCustomerGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-customer-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-dhcp-options`.

- **AWS CLI**
- 
            
                    **To delete a DHCP options set**This example deletes the specified DHCP options set. If the command succeeds, no output is returned. Command: `aws ec2 delete-dhcp-options --dhcp-options-id``dopt-d9070ebb`- 
                    For API details, see [DeleteDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-dhcp-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-egress-only-internet-gateway`.

- **AWS CLI**
- 
            
                    **To delete an egress-only Internet gateway**This example deletes the specified egress-only Internet gateway. Command: `aws ec2 delete-egress-only-internet-gateway --egress-only-internet-gateway-id``eigw-01eadbd45ecd7943f`Output: `{ "ReturnCode": true }`- 
                    For API details, see [DeleteEgressOnlyInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-egress-only-internet-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-fleets`.

- **AWS CLI**
- 
            
                    **Example 1: To delete an EC2 Fleet and terminate the associated instances**The following `delete-fleets`example deletes the specified EC2 Fleet and terminates the associated On-Demand Instances and Spot Instances.`aws ec2 delete-fleets \ --fleet-ids``fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE`\ --terminate-instancesOutput: `{ "SuccessfulFleetDeletions": [ { "CurrentFleetState": "deleted_terminating", "PreviousFleetState": "active", "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE" } ], "UnsuccessfulFleetDeletions": [] }`For more information, see [Delete an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#delete-fleet)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.**Example 2: To delete an EC2 Fleet without terminating the associated instances**The following `delete-fleets`example deletes the specified EC2 Fleet without terminating the associated On-Demand Instances and Spot Instances.`aws ec2 delete-fleets \ --fleet-ids``fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE`\ --no-terminate-instancesOutput: `{ "SuccessfulFleetDeletions": [ { "CurrentFleetState": "deleted_running", "PreviousFleetState": "active", "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE" } ], "UnsuccessfulFleetDeletions": [] }`For more information, see [Delete an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html#delete-fleet)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DeleteFleets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-fleets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-flow-logs`.

- **AWS CLI**
- 
            
                    **To delete a flow log**The following `delete-flow-logs`example deletes the specified flow log.`aws ec2 delete-flow-logs --flow-log-id``fl-11223344556677889`Output: `{ "Unsuccessful": [] }`- 
                    For API details, see [DeleteFlowLogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-flow-logs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-fpga-image`.

- **AWS CLI**
- 
            
                    **To delete an Amazon FPGA image**This example deletes the specified AFI. Command: `aws ec2 delete-fpga-image --fpga-image-id``afi-06b12350a123fbabc`Output: `{ "Return": true }`- 
                    For API details, see [DeleteFpgaImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-fpga-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-instance-connect-endpoint`.

- **AWS CLI**
- 
            
                    **To delete an EC2 Instance Connect Endpoint**The following `delete-instance-connect-endpoint`example deletes the specified EC2 Instance Connect Endpoint.`aws ec2 delete-instance-connect-endpoint \ --instance-connect-endpoint-id``eice-03f5e49b83924bbc7`Output: `{ "InstanceConnectEndpoint": { "OwnerId": "111111111111", "InstanceConnectEndpointId": "eice-0123456789example", "InstanceConnectEndpointArn": "arn:aws:ec2:us-east-1:111111111111:instance-connect-endpoint/eice-0123456789example", "State": "delete-in-progress", "StateMessage": "", "NetworkInterfaceIds": [], "VpcId": "vpc-0123abcd", "AvailabilityZone": "us-east-1d", "CreatedAt": "2023-02-07T12:05:37+00:00", "SubnetId": "subnet-0123abcd" } }`For more information, see [Remove EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-ec2-instance-connect-endpoint.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DeleteInstanceConnectEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-instance-connect-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-instance-event-window`.

- **AWS CLI**
- 
            
                    **Example 1: To delete an event window**The following `delete-instance-event-window`example deletes an event window.`aws ec2 delete-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`Output: `{ "InstanceEventWindowState": { "InstanceEventWindowId": "iew-0abcdef1234567890", "State": "deleting" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 2: To force delete an event window**The following `delete-instance-event-window`example force deletes an event window if the event window is currently associated with targets.`aws ec2 delete-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --force-deleteOutput: `{ "InstanceEventWindowState": { "InstanceEventWindowId": "iew-0abcdef1234567890", "State": "deleting" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.- 
                    For API details, see [DeleteInstanceEventWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-instance-event-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-internet-gateway`.

- **AWS CLI**
- 
            
                    **To delete an internet gateway**The following `delete-internet-gateway`example deletes the specified internet gateway.`aws ec2 delete-internet-gateway \ --internet-gateway-id``igw-0d0fb496b3EXAMPLE`This command produces no output. For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DeleteInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-internet-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ipam-pool`.

- **AWS CLI**
- 
            
                    **To delete an IPAM pool**In this example, you're a IPAM delegated admin who wants to delete an IPAM pool that you no longer need, but the pool has a CIDR provisioned to it. You cannot delete a pool if it has CIDRs provisioned to it unless you use the `--cascade`option, so you'll use`--cascade`.To complete this request: You'll need the IPAM pool ID which you can get with [describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html).The`--region`must be the IPAM home Region.The following `delete-ipam-pool`example deletes an IPAM pool in your AWS account.`aws ec2 delete-ipam-pool \ --ipam-pool-id``ipam-pool-050c886a3ca41cd5b`\ --cascade \ --region`us-east-1`Output: `{ "IpamPool": { "OwnerId": "320805250157", "IpamPoolId": "ipam-pool-050c886a3ca41cd5b", "IpamPoolArn": "arn:aws:ec2::320805250157:ipam-pool/ipam-pool-050c886a3ca41cd5b", "IpamScopeArn": "arn:aws:ec2::320805250157:ipam-scope/ipam-scope-0a158dde35c51107b", "IpamScopeType": "private", "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-005f921c17ebd5107", "IpamRegion": "us-east-1", "Locale": "None", "PoolDepth": 1, "State": "delete-in-progress", "Description": "example", "AutoImport": false, "AddressFamily": "ipv4", "AllocationMinNetmaskLength": 0, "AllocationMaxNetmaskLength": 32 } }`For more information, see [Delete a pool](https://docs.aws.amazon.com/vpc/latest/ipam/delete-pool-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DeleteIpamPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-ipam-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ipam-resource-discovery`.

- **AWS CLI**
- 
            
                    **To delete a resource discovery**In this example, you're a IPAM delegated admin who wants to delete a non-default resource discovery that you created to share with another IPAM admin during the process of integrating IPAM with accounts outside of your organization. To complete this request: The `--region`must be the Region where you created the resource discovery.You cannot delete a default resource discovery if`"IsDefault": true`. A default resource discovery is one that is created automatically in the account that creates an IPAM. To delete a default resource discovery, you have to delete the IPAM.The following `delete-ipam-resource-discovery`example deletes a resource discovery.`aws ec2 delete-ipam-resource-discovery \ --ipam-resource-discovery-id``ipam-res-disco-0e39761475298ee0f`\ --region`us-east-1`Output: `{ "IpamResourceDiscovery": { "OwnerId": "149977607591", "IpamResourceDiscoveryId": "ipam-res-disco-0e39761475298ee0f", "IpamResourceDiscoveryArn": "arn:aws:ec2::149977607591:ipam-resource-discovery/ipam-res-disco-0e39761475298ee0f", "IpamResourceDiscoveryRegion": "us-east-1", "OperatingRegions": [ { "RegionName": "us-east-1" } ], "IsDefault": false, "State": "delete-in-progress" } }`For more information about resource discoveries, see [Work with resource discoveries](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DeleteIpamResourceDiscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-ipam-resource-discovery.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ipam-scope`.

- **AWS CLI**
- 
            
                    **To delete an IPAM scope**The following `delete-ipam-scope`example deletes an IPAM.`aws ec2 delete-ipam-scope \ --ipam-scope-id``ipam-scope-01c1ebab2b63bd7e4`Output: `{ "IpamScope": { "OwnerId": "123456789012", "IpamScopeId": "ipam-scope-01c1ebab2b63bd7e4", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-01c1ebab2b63bd7e4", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "IpamScopeType": "private", "IsDefault": false, "Description": "Example description", "PoolCount": 0, "State": "delete-in-progress" } }`For more information, see [Delete a scope](https://docs.aws.amazon.com/vpc/latest/ipam/delete-scope-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DeleteIpamScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-ipam-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-ipam`.

- **AWS CLI**
- 
            
                    **To delete an IPAM**The following `delete-ipam`example deletes an IPAM.`aws ec2 delete-ipam \ --ipam-id``ipam-036486dfa6af58ee0`Output: `{ "Ipam": { "OwnerId": "123456789012", "IpamId": "ipam-036486dfa6af58ee0", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-036486dfa6af58ee0", "IpamRegion": "us-east-1", "PublicDefaultScopeId": "ipam-scope-071b8042b0195c183", "PrivateDefaultScopeId": "ipam-scope-0807405dece705a30", "ScopeCount": 2, "OperatingRegions": [ { "RegionName": "us-east-1" }, { "RegionName": "us-east-2" }, { "RegionName": "us-west-1" } ], "State": "delete-in-progress" } }`For more information, see [Delete an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/delete-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DeleteIpam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-ipam.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-key-pair`.

- **AWS CLI**
- 
            
                    **To delete a key pair**The following `delete-key-pair`example deletes the specified key pair.`aws ec2 delete-key-pair \ --key-name``my-key-pair`Output: `{ "Return": true, "KeyPairId": "key-03c8d3aceb53b507" }`For more information, see [Create and delete key pairs](https://docs.aws.amazon.com/cli/latest/userguide/cli-ec2-keypairs.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [DeleteKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-launch-template-versions`.

- **AWS CLI**
- 
            
                    **To delete a launch template version**This example deletes the specified launch template version. Command: `aws ec2 delete-launch-template-versions --launch-template-id``lt-0abcd290751193123`--versions`1`Output: `{ "UnsuccessfullyDeletedLaunchTemplateVersions": [], "SuccessfullyDeletedLaunchTemplateVersions": [ { "LaunchTemplateName": "TestVersion", "VersionNumber": 1, "LaunchTemplateId": "lt-0abcd290751193123" } ] }`- 
                    For API details, see [DeleteLaunchTemplateVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-launch-template-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-launch-template`.

- **AWS CLI**
- 
            
                    **To delete a launch template**This example deletes the specified launch template. Command: `aws ec2 delete-launch-template --launch-template-id``lt-0abcd290751193123`Output: `{ "LaunchTemplate": { "LatestVersionNumber": 2, "LaunchTemplateId": "lt-0abcd290751193123", "LaunchTemplateName": "TestTemplate", "DefaultVersionNumber": 2, "CreatedBy": "arn:aws:iam::123456789012:root", "CreateTime": "2017-11-23T16:46:25.000Z" } }`- 
                    For API details, see [DeleteLaunchTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-launch-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-local-gateway-route-table-virtual-interface-group-association`.

- **AWS CLI**
- 
            
                    **To disassociate a local gateway route table from a virtual interfaces (VIFs) group**The following `delete-local-gateway-route-table-virtual-interface-group-association`example deletes the association between the specified local gateway route table and VIF group.`aws ec2 delete-local-gateway-route-table-virtual-interface-group-association \ --local-gateway-route-table-virtual-interface-group-association-id``lgw-vif-grp-assoc-exampleid12345678`Output: `{ "LocalGatewayRouteTableVirtualInterfaceGroupAssociation": { "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": "lgw-vif-grp-assoc-exampleid12345678", "LocalGatewayVirtualInterfaceGroupId": "lgw-vif-grp-exampleid0123abcd", "LocalGatewayId": "lgw-exampleid11223344", "LocalGatewayRouteTableId": "lgw-rtb-exampleidabcd1234", "LocalGatewayRouteTableArn": "arn:aws:ec2:us-west-2:111122223333:local-gateway-route-table/lgw-rtb-exampleidabcd1234", "OwnerId": "111122223333", "State": "disassociating", "Tags": [] } }`For more information, see [VIF group associations](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#vif-group-associations)in the*AWS Outposts User Guide*.- 
                    For API details, see [DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-local-gateway-route-table-virtual-interface-group-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-local-gateway-route-table-vpc-association`.

- **AWS CLI**
- 
            
                    **To disassociate a local gateway route table from a VPC**The following `delete-local-gateway-route-table-vpc-association`example deletes the association between the specified local gateway route table and VPC.`aws ec2 delete-local-gateway-route-table-vpc-association \ --local-gateway-route-table-vpc-association-id``vpc-example0123456789`Output: `{ "LocalGatewayRouteTableVpcAssociation": { "LocalGatewayRouteTableVpcAssociationId": "lgw-vpc-assoc-abcd1234wxyz56789", "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890", "LocalGatewayRouteTableArn": "arn:aws:ec2:us-west-2:555555555555:local-gateway-route-table/lgw-rtb-abcdefg1234567890", "LocalGatewayId": "lgw-exampleid01234567", "VpcId": "vpc-example0123456789", "OwnerId": "555555555555", "State": "disassociating" } }`For more information, see [VPC associations](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#vpc-associations)in the*AWS Outposts User Guide*.- 
                    For API details, see [DeleteLocalGatewayRouteTableVpcAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-local-gateway-route-table-vpc-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-local-gateway-route-table`.

- **AWS CLI**
- 
            
                    **To delete a local gateway route table**The following `delete-local-gateway-route-table`example creates a local gateway route table with the direct VPC routing mode.`aws ec2 delete-local-gateway-route-table \ --local-gateway-route-table-id``lgw-rtb-abcdefg1234567890`Output: `{ "LocalGatewayRouteTable": { "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890", "LocalGatewayRouteTableArn": "arn:aws:ec2:us-west-2:111122223333:local-gateway-route-table/lgw-rtb-abcdefg1234567890", "LocalGatewayId": "lgw-1a2b3c4d5e6f7g8h9", "OutpostArn": "arn:aws:outposts:us-west-2:111122223333:outpost/op-021345abcdef67890", "OwnerId": "111122223333", "State": "deleting", "Tags": [], "Mode": "direct-vpc-routing" } }`For more information, see [Local gateway route tables](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [DeleteLocalGatewayRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-local-gateway-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-local-gateway-route`.

- **AWS CLI**
- 
            
                    **To delete a route from a local gateway route table**The following `delete-local-gateway-route`example deletes the specified route from the specified local gateway route table.`aws ec2 delete-local-gateway-route \ --destination-cidr-block``0.0.0.0/0`\ --local-gateway-route-table-id`lgw-rtb-059615ef7dEXAMPLE`Output: `{ "Route": { "DestinationCidrBlock": "0.0.0.0/0", "LocalGatewayVirtualInterfaceGroupId": "lgw-vif-grp-07145b276bEXAMPLE", "Type": "static", "State": "deleted", "LocalGatewayRouteTableId": "lgw-rtb-059615ef7EXAMPLE" } }`- 
                    For API details, see [DeleteLocalGatewayRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-local-gateway-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-managed-prefix-list`.

- **AWS CLI**
- 
            
                    **To delete a prefix list**The following `delete-managed-prefix-list`example deletes the specified prefix list.`aws ec2 delete-managed-prefix-list \ --prefix-list-id``pl-0123456abcabcabc1`Output: `{ "PrefixList": { "PrefixListId": "pl-0123456abcabcabc1", "AddressFamily": "IPv4", "State": "delete-in-progress", "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456abcabcabc1", "PrefixListName": "test", "MaxEntries": 10, "Version": 1, "OwnerId": "123456789012" } }`For more information, see [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DeleteManagedPrefixList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-managed-prefix-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-nat-gateway`.

- **AWS CLI**
- 
            
                    **To delete a NAT gateway**This example deletes NAT gateway `nat-04ae55e711cec5680`.Command: `aws ec2 delete-nat-gateway --nat-gateway-id``nat-04ae55e711cec5680`Output: `{ "NatGatewayId": "nat-04ae55e711cec5680" }`- 
                    For API details, see [DeleteNatGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-nat-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-acl-entry`.

- **AWS CLI**
- 
            
                    **To delete a network ACL entry**This example deletes ingress rule number 100 from the specified network ACL. If the command succeeds, no output is returned. Command: `aws ec2 delete-network-acl-entry --network-acl-id``acl-5fb85d36`--ingress --rule-number`100`- 
                    For API details, see [DeleteNetworkAclEntry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-acl-entry.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-acl`.

- **AWS CLI**
- 
            
                    **To delete a network ACL**This example deletes the specified network ACL. If the command succeeds, no output is returned. Command: `aws ec2 delete-network-acl --network-acl-id``acl-5fb85d36`- 
                    For API details, see [DeleteNetworkAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-insights-access-scope-analysis`.

- **AWS CLI**
- 
            
                    **To delete a Network Access Scope analysis**The following `delete-network-insights-access-scope-analysis`example deletes the specified Network Access Scope analysis.`aws ec2 delete-network-insights-access-scope-analysis \ --network-insights-access-scope-analysis-id``nisa-01234567891abcdef`Output: `{ "NetworkInsightsAccessScopeAnalysisId": "nisa-01234567891abcdef }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [DeleteNetworkInsightsAccessScopeAnalysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-insights-access-scope-analysis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-insights-access-scope`.

- **AWS CLI**
- 
            
                    **To delete a Network Access Scope**The following `delete-network-insights-access-scope`example deletes the specified Network Access Scope.`aws ec2 delete-network-insights-access-scope \ --network-insights-access-scope-id``nis-123456789abc01234`Output: `{ "NetworkInsightsAccessScopeId": "nis-123456789abc01234" }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [DeleteNetworkInsightsAccessScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-insights-access-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-insights-analysis`.

- **AWS CLI**
- 
            
                    **To delete a path analysis**The following `delete-network-insights-analysis`example deletes the specified analysis.`aws ec2 delete-network-insights-analysis \ --network-insights-analysis-id``nia-02207aa13eb480c7a`Output: `{ "NetworkInsightsAnalysisId": "nia-02207aa13eb480c7a" }`For more information, see [Getting started using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/reachability/getting-started-cli.html)in the*Reachability Analyzer Guide*.- 
                    For API details, see [DeleteNetworkInsightsAnalysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-insights-analysis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-insights-path`.

- **AWS CLI**
- 
            
                    **To delete a path**The following `delete-network-insights-path`example deletes the specified path. Before you can delete a path, you must delete all its analyses using the`delete-network-insights-analysis`command.`aws ec2 delete-network-insights-path \ --network-insights-path-id``nip-0b26f224f1d131fa8`Output: `{ "NetworkInsightsPathId": "nip-0b26f224f1d131fa8" }`For more information, see [Getting started using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/reachability/getting-started-cli.html)in the*Reachability Analyzer Guide*.- 
                    For API details, see [DeleteNetworkInsightsPath](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-insights-path.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-interface-permission`.

- **AWS CLI**
- 
            
                    **To delete a network interface permission**This example deletes the specified network interface permission. Command: `aws ec2 delete-network-interface-permission --network-interface-permission-id``eni-perm-06fd19020ede149ea`Output: `{ "Return": true }`- 
                    For API details, see [DeleteNetworkInterfacePermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-interface-permission.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-network-interface`.

- **AWS CLI**
- 
            
                    **To delete a network interface**This example deletes the specified network interface. If the command succeeds, no output is returned. Command: `aws ec2 delete-network-interface --network-interface-id``eni-e5aa89a3`- 
                    For API details, see [DeleteNetworkInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-placement-group`.

- **AWS CLI**
- 
            
                    **To delete a placement group**This example command deletes the specified placement group. Command: `aws ec2 delete-placement-group --group-name``my-cluster`- 
                    For API details, see [DeletePlacementGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-placement-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-queued-reserved-instances`.

- **AWS CLI**
- 
            
                    **To delete a queued purchase**The following `delete-queued-reserved-instances`example deletes the specified Reserved Instance, which was queued for purchase.`aws ec2 delete-queued-reserved-instances \ --reserved-instances-ids``af9f760e-6f91-4559-85f7-4980eexample`Output: `{ "SuccessfulQueuedPurchaseDeletions": [ { "ReservedInstancesId": "af9f760e-6f91-4559-85f7-4980eexample" } ], "FailedQueuedPurchaseDeletions": [] }`- 
                    For API details, see [DeleteQueuedReservedInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-queued-reserved-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-route-table`.

- **AWS CLI**
- 
            
                    **To delete a route table**This example deletes the specified route table. If the command succeeds, no output is returned. Command: `aws ec2 delete-route-table --route-table-id``rtb-22574640`- 
                    For API details, see [DeleteRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-route`.

- **AWS CLI**
- 
            
                    **To delete a route**This example deletes the specified route from the specified route table. If the command succeeds, no output is returned. Command: `aws ec2 delete-route --route-table-id``rtb-22574640`--destination-cidr-block`0.0.0.0/0`- 
                    For API details, see [DeleteRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-security-group`.

- **AWS CLI**
- 
            
                    **[EC2-Classic] To delete a security group**This example deletes the security group named `MySecurityGroup`. If the command succeeds, no output is returned.Command: `aws ec2 delete-security-group --group-name``MySecurityGroup`**[EC2-VPC] To delete a security group**This example deletes the security group with the ID `sg-903004f8`. Note that you can't reference a security group for EC2-VPC by name. If the command succeeds, no output is returned.Command: `aws ec2 delete-security-group --group-id``sg-903004f8`For more information, see Using Security Groups in the *AWS Command Line Interface User Guide*.- 
                    For API details, see [DeleteSecurityGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-security-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-snapshot`.

- **AWS CLI**
- 
            
                    **To delete a snapshot**This example command deletes a snapshot with the snapshot ID of `snap-1234567890abcdef0`. If the command succeeds, no output is returned.Command: `aws ec2 delete-snapshot --snapshot-id``snap-1234567890abcdef0`- 
                    For API details, see [DeleteSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-spot-datafeed-subscription`.

- **AWS CLI**
- 
            
                    **To cancel a Spot Instance data feed subscription**This example command deletes a Spot data feed subscription for the account. If the command succeeds, no output is returned. Command: `aws ec2 delete-spot-datafeed-subscription`- 
                    For API details, see [DeleteSpotDatafeedSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-spot-datafeed-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-subnet-cidr-reservation`.

- **AWS CLI**
- 
            
                    **To delete a subnet CIDR reservation**The following `delete-subnet-cidr-reservation`example deletes the specified subnet CIDR reservation.`aws ec2 delete-subnet-cidr-reservation \ --subnet-cidr-reservation-id``scr-044f977c4eEXAMPLE`Output: `{ "DeletedSubnetCidrReservation": { "SubnetCidrReservationId": "scr-044f977c4eEXAMPLE", "SubnetId": "subnet-03c51e2e6cEXAMPLE", "Cidr": "10.1.0.16/28", "ReservationType": "prefix", "OwnerId": "123456789012" } }`For more information, see [Subnet CIDR reservations](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DeleteSubnetCidrReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-subnet-cidr-reservation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-subnet`.

- **AWS CLI**
- 
            
                    **To delete a subnet**This example deletes the specified subnet. If the command succeeds, no output is returned. Command: `aws ec2 delete-subnet --subnet-id``subnet-9d4a7b6c`- 
                    For API details, see [DeleteSubnet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-subnet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-tags`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a tag from a resource**The following `delete-tags`example deletes the tag`Stack=Test`from the specified image. When you specify both a value and a key name, the tag is deleted only if the tag's value matches the specified value.`aws ec2 delete-tags \ --resources``ami-1234567890abcdef0`\ --tags`Key=Stack,Value=Test`It's optional to specify the value for a tag. The following `delete-tags`example deletes the tag with the key name`purpose`from the specified instance, regardless of the tag value for the tag.`aws ec2 delete-tags \ --resources``i-1234567890abcdef0`\ --tags`Key=purpose`If you specify the empty string as the tag value, the tag is deleted only if the tag's value is the empty string. The following `delete-tags`example specifies the empty string as the tag value for the tag to delete.`aws ec2 delete-tags \ --resources``i-1234567890abcdef0`\ --tags`Key=Name,Value=`**Example 2: To delete a tag from multiple resources**The following `delete-tags`example deletes the tag``Purpose=Test`` from both an instance and an AMI. As shown in the previous example, you can omit the tag value from the command.`aws ec2 delete-tags \ --resources``i-1234567890abcdef0``ami-1234567890abcdef0`\ --tags`Key=Purpose`- 
                    For API details, see [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-traffic-mirror-filter-rule`.

- **AWS CLI**
- 
            
                    **To delete a traffic mirror filter rule**The following `delete-traffic-mirror-filter-rule`example deletes the specified traffic mirror filter rule.`aws ec2 delete-traffic-mirror-filter-rule \ --traffic-mirror-filter-rule-id``tmfr-081f71283bEXAMPLE`Output: `{ "TrafficMirrorFilterRuleId": "tmfr-081f71283bEXAMPLE" }`For more information, see [Modify Your Traffic Mirror Filter Rules](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html#modify-traffic-mirroring-filter-rules)in the*AWS Traffic Mirroring Guide*.- 
                    For API details, see [DeleteTrafficMirrorFilterRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-filter-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-traffic-mirror-filter`.

- **AWS CLI**
- 
            
                    **To delete a traffic mirror filter**The following `delete-traffic-mirror-filter`example deletes the specified traffic mirror filter.`aws ec2 delete-traffic-mirror-filter \ --traffic-mirror-filter-id``tmf-0be0b25fcdEXAMPLE`Output: `{ "TrafficMirrorFilterId": "tmf-0be0b25fcdEXAMPLE" }`For more information, see [Delete a Traffic Mirror Filter](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html#delete-traffic-mirroring-filter)in the*AWS Traffic Mirroring Guide*.- 
                    For API details, see [DeleteTrafficMirrorFilter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-filter.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-traffic-mirror-session`.

- **AWS CLI**
- 
            
                    **To delete a traffic mirror session**The following `delete-traffic-mirror-session`example deletes the specified traffic mirror-session.`aws ec2 delete-traffic-mirror-session \ --traffic-mirror-session-id``tms-0af3141ce5EXAMPLE`Output: `{ "TrafficMirrorSessionId": "tms-0af3141ce5EXAMPLE" }`For more information, see [Delete a Traffic Mirror Session](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html#delete-traffic-mirroring-session)in the*AWS Traffic Mirroring Guide*.- 
                    For API details, see [DeleteTrafficMirrorSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-traffic-mirror-target`.

- **AWS CLI**
- 
            
                    **To delete a traffic mirror target**The following `delete-traffic-mirror-target`example deletes the specified traffic mirror target.`aws ec2 delete-traffic-mirror-target \ --traffic-mirror-target-id``tmt-060f48ce9EXAMPLE`Output: `{ "TrafficMirrorTargetId": "tmt-060f48ce9EXAMPLE" }`For more information, see [Delete a Traffic Mirror Target](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-target.html#delete-traffic-mirroring-target)in the*AWS Traffic Mirroring Guide*.- 
                    For API details, see [DeleteTrafficMirrorTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-traffic-mirror-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-connect-peer`.

- **AWS CLI**
- 
            
                    **To delete a Transit Gateway Connect peer**The following `delete-transit-gateway-connect-peer`example deletes the specified Connect peer.`aws ec2 delete-transit-gateway-connect-peer \ --transit-gateway-connect-peer-id``tgw-connect-peer-0666adbac4EXAMPLE`Output: `{ "TransitGatewayConnectPeer": { "TransitGatewayAttachmentId": "tgw-attach-0f0927767cEXAMPLE", "TransitGatewayConnectPeerId": "tgw-connect-peer-0666adbac4EXAMPLE", "State": "deleting", "CreationTime": "2021-10-13T03:35:17.000Z", "ConnectPeerConfiguration": { "TransitGatewayAddress": "10.0.0.234", "PeerAddress": "172.31.1.11", "InsideCidrBlocks": [ "169.254.6.0/29" ], "Protocol": "gre", "BgpConfigurations": [ { "TransitGatewayAsn": 64512, "PeerAsn": 64512, "TransitGatewayAddress": "169.254.6.2", "PeerAddress": "169.254.6.1", "BgpStatus": "down" }, { "TransitGatewayAsn": 64512, "PeerAsn": 64512, "TransitGatewayAddress": "169.254.6.3", "PeerAddress": "169.254.6.1", "BgpStatus": "down" } ] } } }`For more information, see [Transit gateway Connect attachments and Transit Gateway Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayConnectPeer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-connect-peer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-connect`.

- **AWS CLI**
- 
            
                    **To delete a transit gateway Connect attachment**The following `delete-transit-gateway-connect`example deletes the specified Connect attachment.`aws ec2 delete-transit-gateway-connect \ --transit-gateway-attachment-id``tgw-attach-037012e5dcEXAMPLE`Output: `{ "TransitGatewayConnect": { "TransitGatewayAttachmentId": "tgw-attach-037012e5dcEXAMPLE", "TransportTransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "State": "deleting", "CreationTime": "2021-03-09T19:59:17+00:00", "Options": { "Protocol": "gre" } } }`For more information, see [Transit gateway Connect attachments and Transit Gateway Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayConnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-connect.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-multicast-domain`.

- **AWS CLI**
- 
            
                    **To delete a transit gateway multicast domain**The following `delete-transit-gateway-multicast-domain`example deletes the specified multicast domain.`aws ec2 delete-transit-gateway-multicast-domain \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef7EXAMPLE`Output: `{ "TransitGatewayMulticastDomain": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-02bb79002bEXAMPLE", "TransitGatewayId": "tgw-0d88d2d0d5EXAMPLE", "State": "deleting", "CreationTime": "2019-11-20T22:02:03.000Z" } }`For more information, see [Managing multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/manage-domain.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayMulticastDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-multicast-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-peering-attachment`.

- **AWS CLI**
- 
            
                    **To delete a transit gateway peering attachment**The following `delete-transit-gateway-peering-attachment`example deletes the specified transit gateway peering attachment.`aws ec2 delete-transit-gateway-peering-attachment \ --transit-gateway-attachment-id``tgw-attach-4455667788aabbccd`Output: `{ "TransitGatewayPeeringAttachment": { "TransitGatewayAttachmentId": "tgw-attach-4455667788aabbccd", "RequesterTgwInfo": { "TransitGatewayId": "tgw-123abc05e04123abc", "OwnerId": "123456789012", "Region": "us-west-2" }, "AccepterTgwInfo": { "TransitGatewayId": "tgw-11223344aabbcc112", "OwnerId": "123456789012", "Region": "us-east-2" }, "State": "deleting", "CreationTime": "2019-12-09T11:38:31.000Z" } }`For more information, see [Transit Gateway Peering Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayPeeringAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-peering-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-policy-table`.

- **AWS CLI**
- 
            
                    **To delete a transit gateway policy table**The following `delete-transit-gateway-policy-table`example deletes the specified transit gateway policy table.`aws ec2 delete-transit-gateway-policy-table \ --transit-gateway-policy-table-id``tgw-ptb-0a16f134b78668a81`Output: `{ "TransitGatewayPolicyTables": [ { "TransitGatewayPolicyTableId": "tgw-ptb-0a16f134b78668a81", "TransitGatewayId": "tgw-067f8505c18f0bd6e", "State": "deleting", "CreationTime": "2023-11-28T16:36:43+00:00", "Tags": [] } ] }`For more information, see [Transit gateway policy tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-policy-tables.html)in the*Transit Gateway User Guide*.- 
                    For API details, see [DeleteTransitGatewayPolicyTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-policy-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-prefix-list-reference`.

- **AWS CLI**
- 
            
                    **To delete a prefix list reference**The following `delete-transit-gateway-prefix-list-reference`example deletes the specified prefix list reference.`aws ec2 delete-transit-gateway-prefix-list-reference \ --transit-gateway-route-table-id``tgw-rtb-0123456789abcd123`\ --prefix-list-id`pl-11111122222222333`Output: `{ "TransitGatewayPrefixListReference": { "TransitGatewayRouteTableId": "tgw-rtb-0123456789abcd123", "PrefixListId": "pl-11111122222222333", "PrefixListOwnerId": "123456789012", "State": "deleting", "Blackhole": false, "TransitGatewayAttachment": { "TransitGatewayAttachmentId": "tgw-attach-aabbccddaabbccaab", "ResourceType": "vpc", "ResourceId": "vpc-112233445566aabbc" } } }`For more information, see [Prefix list references](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-prefix-lists.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayPrefixListReference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-prefix-list-reference.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-route-table`.

- **AWS CLI**
- 
            
                    **To delete a transit gateway route table**The following `delete-transit-gateway-route-table`example deletes the specified transit gateway route table.`aws ec2 delete-transit-gateway-route-table \ --transit-gateway-route-table-id``tgw-rtb-0b6f6aaa01EXAMPLE`Output: `{ "TransitGatewayRouteTable": { "TransitGatewayRouteTableId": "tgw-rtb-0b6f6aaa01EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "State": "deleting", "DefaultAssociationRouteTable": false, "DefaultPropagationRouteTable": false, "CreationTime": "2019-07-17T20:27:26.000Z" } }`For more information, see [Delete a transit gateway route table](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#delete-tgw-route-table)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-route`.

- **AWS CLI**
- 
            
                    **To delete a CIDR block from a route table**The following `delete-transit-gateway-route`example deletes the CIDR block from the specified transit gateway route table.`aws ec2 delete-transit-gateway-route \ --transit-gateway-route-table-id``tgw-rtb-0b6f6aaa01EXAMPLE`\ --destination-cidr-block`10.0.2.0/24`Output: `{ "Route": { "DestinationCidrBlock": "10.0.2.0/24", "TransitGatewayAttachments": [ { "ResourceId": "vpc-0065acced4EXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-0b5968d3b6EXAMPLE", "ResourceType": "vpc" } ], "Type": "static", "State": "deleted" } }`For more information, see [Delete a static route](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#tgw-delete-static-route)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway-vpc-attachment`.

- **AWS CLI**
- 
            
                    **To delete a transit gateway VPC attachment**The following `delete-transit-gateway-vpc-attachment`example deletes the specified VPC attachment.`aws ec2 delete-transit-gateway-vpc-attachment \ --transit-gateway-attachment-id``tgw-attach-0d2c54bdbEXAMPLE`Output: `{ "TransitGatewayVpcAttachment": { "TransitGatewayAttachmentId": "tgw-attach-0d2c54bdb3EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "VpcId": "vpc-0065acced4f61c651", "VpcOwnerId": "111122223333", "State": "deleting", "CreationTime": "2019-07-17T16:04:27.000Z" } }`For more information, see [Delete a VPC attachment](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#delete-vpc-attachment)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGatewayVpcAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway-vpc-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-transit-gateway`.

- **AWS CLI**
- 
            
                    **To delete a transit gateway**The following `delete-transit-gateway`example deletes the specified transit gateway.`aws ec2 delete-transit-gateway \ --transit-gateway-id``tgw-01f04542b2EXAMPLE`Output: `{ "TransitGateway": { "TransitGatewayId": "tgw-01f04542b2EXAMPLE", "State": "deleting", "OwnerId": "123456789012", "Description": "Example Transit Gateway", "CreationTime": "2019-08-27T15:04:35.000Z", "Options": { "AmazonSideAsn": 64515, "AutoAcceptSharedAttachments": "disable", "DefaultRouteTableAssociation": "enable", "AssociationDefaultRouteTableId": "tgw-rtb-0ce7a6948fEXAMPLE", "DefaultRouteTablePropagation": "enable", "PropagationDefaultRouteTableId": "tgw-rtb-0ce7a6948fEXAMPLE", "VpnEcmpSupport": "enable", "DnsSupport": "enable" } } }`For more information, see [Delete a transit gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html#delete-tgw)in the*Transit Gateways Guide*.- 
                    For API details, see [DeleteTransitGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-transit-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-verified-access-endpoint`.

- **AWS CLI**
- 
            
                    **To delete a Verified Access endpoint**The following `delete-verified-access-endpoint`example deletes the specified Verified Access endpoint.`aws ec2 delete-verified-access-endpoint \ --verified-access-endpoint-id``vae-066fac616d4d546f2`Output: `{ "VerifiedAccessEndpoint": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessEndpointId": "vae-066fac616d4d546f2", "ApplicationDomain": "example.com", "EndpointType": "network-interface", "AttachmentType": "vpc", "DomainCertificateArn": "arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE", "EndpointDomain": "my-ava-app.edge-00c3372d53b1540bb.vai-0ce000c0b7643abea.prod.verified-access.us-east-2.amazonaws.com", "SecurityGroupIds": [ "sg-004915970c4c8f13a" ], "NetworkInterfaceOptions": { "NetworkInterfaceId": "eni-0aec70418c8d87a0f", "Protocol": "https", "Port": 443 }, "Status": { "Code": "deleting" }, "Description": "Testing Verified Access", "CreationTime": "2023-08-25T20:54:43", "LastUpdatedTime": "2023-08-25T22:46:32" } }`For more information, see [Verified Access endpoints](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DeleteVerifiedAccessEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-verified-access-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-verified-access-group`.

- **AWS CLI**
- 
            
                    **To delete a Verified Access group**The following `delete-verified-access-group`example deletes the specified Verified Access group.`aws ec2 delete-verified-access-group \ --verified-access-group-id``vagr-0dbe967baf14b7235`Output: `{ "VerifiedAccessGroup": { "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "Testing Verified Access", "Owner": "123456789012", "VerifiedAccessGroupArn": "arn:aws:ec2:us-east-2:123456789012:verified-access-group/vagr-0dbe967baf14b7235", "CreationTime": "2023-08-25T19:55:19", "LastUpdatedTime": "2023-08-25T22:49:03", "DeletionTime": "2023-08-26T00:58:31" } }`For more information, see [Verified Access groups](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DeleteVerifiedAccessGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-verified-access-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-verified-access-instance`.

- **AWS CLI**
- 
            
                    **To delete a Verified Access instance**The following `delete-verified-access-instance`example deletes the specified Verified Access instance.`aws ec2 delete-verified-access-instance \ --verified-access-instance-id``vai-0ce000c0b7643abea`Output: `{ "VerifiedAccessInstance": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "Testing Verified Access", "VerifiedAccessTrustProviders": [], "CreationTime": "2023-08-25T18:27:56", "LastUpdatedTime": "2023-08-26T01:00:18" } }`For more information, see [Verified Access instances](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-instances.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DeleteVerifiedAccessInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-verified-access-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-verified-access-trust-provider`.

- **AWS CLI**
- 
            
                    **To delete a Verified Access trust provider**The following `delete-verified-access-trust-provider`example deletes the specified Verified Access trust provider.`aws ec2 delete-verified-access-trust-provider \ --verified-access-trust-provider-id``vatp-0bb32de759a3e19e7`Output: `{ "VerifiedAccessTrustProvider": { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "Description": "Testing Verified Access", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center", "PolicyReferenceName": "idc", "CreationTime": "2023-08-25T18:40:36", "LastUpdatedTime": "2023-08-25T18:40:36" } }`For more information, see [Trust providers for Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/trust-providers.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DeleteVerifiedAccessTrustProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-verified-access-trust-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-volume`.

- **AWS CLI**
- 
            
                    **To delete a volume**This example command deletes an available volume with the volume ID of `vol-049df61146c4d7901`. If the command succeeds, no output is returned.Command: `aws ec2 delete-volume --volume-id``vol-049df61146c4d7901`- 
                    For API details, see [DeleteVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-volume.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpc-endpoint-connection-notifications`.

- **AWS CLI**
- 
            
                    **To delete an endpoint connection notification**This example deletes the specified endpoint connection notification. Command: `aws ec2 delete-vpc-endpoint-connection-notifications --connection-notification-ids``vpce-nfn-008776de7e03f5abc`Output: `{ "Unsuccessful": [] }`- 
                    For API details, see [DeleteVpcEndpointConnectionNotifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint-connection-notifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpc-endpoint-service-configurations`.

- **AWS CLI**
- 
            
                    **To delete an endpoint service configuration**This example deletes the specified endpoint service configuration. Command: `aws ec2 delete-vpc-endpoint-service-configurations --service-ids``vpce-svc-03d5ebb7d9579a2b3`Output: `{ "Unsuccessful": [] }`- 
                    For API details, see [DeleteVpcEndpointServiceConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoint-service-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpc-endpoints`.

- **AWS CLI**
- 
            
                    **To delete an endpoint**This example deletes endpoints vpce-aa22bb33 and vpce-1a2b3c4d. If the command is partially successful or unsuccessful, a list of unsuccessful items is returned. If the command succeeds, the returned list is empty. Command: `aws ec2 delete-vpc-endpoints --vpc-endpoint-ids``vpce-aa22bb33``vpce-1a2b3c4d`Output: `{ "Unsuccessful": [] }`- 
                    For API details, see [DeleteVpcEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpc-peering-connection`.

- **AWS CLI**
- 
            
                    **To delete a VPC peering connection**This example deletes the specified VPC peering connection. Command: `aws ec2 delete-vpc-peering-connection --vpc-peering-connection-id``pcx-1a2b3c4d`Output: `{ "Return": true }`- 
                    For API details, see [DeleteVpcPeeringConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc-peering-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpc`.

- **AWS CLI**
- 
            
                    **To delete a VPC**This example deletes the specified VPC. If the command succeeds, no output is returned. Command: `aws ec2 delete-vpc --vpc-id``vpc-a01106c2`- 
                    For API details, see [DeleteVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpn-connection-route`.

- **AWS CLI**
- 
            
                    **To delete a static route from a VPN connection**This example deletes the specified static route from the specified VPN connection. If the command succeeds, no output is returned. Command: `aws ec2 delete-vpn-connection-route --vpn-connection-id``vpn-40f41529`--destination-cidr-block`11.12.0.0/16`- 
                    For API details, see [DeleteVpnConnectionRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-connection-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpn-connection`.

- **AWS CLI**
- 
            
                    **To delete a VPN connection**This example deletes the specified VPN connection. If the command succeeds, no output is returned. Command: `aws ec2 delete-vpn-connection --vpn-connection-id``vpn-40f41529`- 
                    For API details, see [DeleteVpnConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpn-gateway`.

- **AWS CLI**
- 
            
                    **To delete a virtual private gateway**This example deletes the specified virtual private gateway. If the command succeeds, no output is returned. Command: `aws ec2 delete-vpn-gateway --vpn-gateway-id``vgw-9a4cacf3`- 
                    For API details, see [DeleteVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-vpn-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deprovision-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To remove an IP address range from use**The following example removes the specified address range from use with AWS. `aws ec2 deprovision-byoip-cidr \ --cidr``203.0.113.25/24`Output: `{ "ByoipCidr": { "Cidr": "203.0.113.25/24", "State": "pending-deprovision" } }`- 
                    For API details, see [DeprovisionByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deprovision-byoip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deprovision-ipam-pool-cidr`.

- **AWS CLI**
- 
            
                    **To deprovision an IPAM pool CIDR**The following `deprovision-ipam-pool-cidr`example deprovisions a CIDR provisioned to an IPAM pool.(Linux): `aws ec2 deprovision-ipam-pool-cidr \ --ipam-pool-id``ipam-pool-02ec043a19bbe5d08`\ --cidr`11.0.0.0/16`(Windows): `aws ec2 deprovision-ipam-pool-cidr``^`--ipam-pool-id`ipam-pool-02ec043a19bbe5d08``^`--cidr`11.0.0.0/16`Output: `{ "IpamPoolCidr": { "Cidr": "11.0.0.0/16", "State": "pending-deprovision" } }`For more information, see [Deprovision pool CIDRs](https://docs.aws.amazon.com/vpc/latest/ipam/depro-pool-cidr-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DeprovisionIpamPoolCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deprovision-ipam-pool-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-image`.

- **AWS CLI**
- 
            
                    **To deregister an AMI**This example deregisters the specified AMI. If the command succeeds, no output is returned. Command: `aws ec2 deregister-image --image-id``ami-4fa54026`- 
                    For API details, see [DeregisterImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-instance-event-notification-attributes`.

- **AWS CLI**
- 
            
                    **Example 1: To remove all tags from event notifications**The following `deregister-instance-event-notification-attributes`example removes`IncludeAllTagsOfInstance=true`, which has the effect of setting`IncludeAllTagsOfInstance`to`false`.`aws ec2 deregister-instance-event-notification-attributes \ --instance-tag-attribute``IncludeAllTagsOfInstance=true`Output: `{ "InstanceTagAttribute": { "InstanceTagKeys": [], "IncludeAllTagsOfInstance": true } }`For more information, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.**Example 2: To remove specific tags from event notifications**The following `deregister-instance-event-notification-attributes`example removes the specified tag from the tags included in event notifications. To describe the remaining tags included in event notifications, use`describe-instance-event-notification-attributes`.`aws ec2 deregister-instance-event-notification-attributes \ --instance-tag-attribute InstanceTagKeys="tag-key2"`Output: `{ "InstanceTagAttribute": { "InstanceTagKeys": [ "tag-key2" ], "IncludeAllTagsOfInstance": false } }`For more information, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DeregisterInstanceEventNotificationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-instance-event-notification-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-transit-gateway-multicast-group-members`.

- **AWS CLI**
- 
            
                    **To deregister group members from a multicast group**This example deregisters the specified network interface group member from the transit gateway multicast group. `aws ec2 deregister-transit-gateway-multicast-group-members \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef7EXAMPLE`\ --group-ip-address`224.0.1.0`\ --network-interface-ids`eni-0e246d3269EXAMPLE`Output: `{ "DeregisteredMulticastGroupMembers": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef7EXAMPLE", "RegisteredNetworkInterfaceIds": [ "eni-0e246d3269EXAMPLE" ], "GroupIpAddress": "224.0.1.0" } }`For more information, see [Deregister Members from a Multicast Group](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-multicast.html#remove-members-multicast-group)in the*AWS Transit Gateways Users Guide*.- 
                    For API details, see [DeregisterTransitGatewayMulticastGroupMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-transit-gateway-multicast-group-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-transit-gateway-multicast-group-source`.

- **AWS CLI**
- 
            
                    **To deregister a source from the transit gateway multicast group**This example deregisters the specified network interface group source from the multicast group. `aws ec2 register-transit-gateway-multicast-group-sources \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef79d6e597`\ --group-ip-address`224.0.1.0`\ --network-interface-ids`eni-07f290fc3c090cbae`Output: `{ "DeregisteredMulticastGroupSources": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef79d6e597", "DeregisteredNetworkInterfaceIds": [ "eni-07f290fc3c090cbae" ], "GroupIpAddress": "224.0.1.0" } }`For more information, see [Deregister Sources from a Multicast Group](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-multicast.html#remove-source-multicast-group)in the*AWS Transit Gateways User Guide*.- 
                    For API details, see [DeregisterTransitGatewayMulticastGroupSource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/deregister-transit-gateway-multicast-group-source.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-account-attributes`.

- **AWS CLI**
- 
            
                    **To describe all the attributes for your AWS account**This example describes the attributes for your AWS account. Command: `aws ec2 describe-account-attributes`Output: `{ "AccountAttributes": [ { "AttributeName": "vpc-max-security-groups-per-interface", "AttributeValues": [ { "AttributeValue": "5" } ] }, { "AttributeName": "max-instances", "AttributeValues": [ { "AttributeValue": "20" } ] }, { "AttributeName": "supported-platforms", "AttributeValues": [ { "AttributeValue": "EC2" }, { "AttributeValue": "VPC" } ] }, { "AttributeName": "default-vpc", "AttributeValues": [ { "AttributeValue": "none" } ] }, { "AttributeName": "max-elastic-ips", "AttributeValues": [ { "AttributeValue": "5" } ] }, { "AttributeName": "vpc-max-elastic-ips", "AttributeValues": [ { "AttributeValue": "5" } ] } ] }`**To describe a single attribute for your AWS account**This example describes the `supported-platforms`attribute for your AWS account.Command: `aws ec2 describe-account-attributes --attribute-names``supported-platforms`Output: `{ "AccountAttributes": [ { "AttributeName": "supported-platforms", "AttributeValues": [ { "AttributeValue": "EC2" }, { "AttributeValue": "VPC" } ] } ] }`- 
                    For API details, see [DescribeAccountAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-account-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-address-transfers`.

- **AWS CLI**
- 
            
                    **To describe an Elastic IP address transfer**The following `describe-address-transfers`example describes the Elastic IP address transfer for the specified Elastic IP address.`aws ec2 describe-address-transfers \ --allocation-ids``eipalloc-09ad461b0d03f6aaf`Output: `{ "AddressTransfers": [ { "PublicIp": "100.21.184.216", "AllocationId": "eipalloc-09ad461b0d03f6aaf", "TransferAccountId": "123456789012", "TransferOfferExpirationTimestamp": "2023-02-22T22:51:01.000Z", "AddressTransferStatus": "pending" } ] }`For more information, see [Transfer Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html#transfer-EIPs-intro)in the*Amazon VPC User Guide*.- 
                    For API details, see [DescribeAddressTransfers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-address-transfers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-addresses-attribute`.

- **AWS CLI**
- 
            
                    **To view the attributes of the domain name associated with an elastic IP address**The following `describe-addresses-attribute`examples return the attributes of the domain name associated with the elastic IP address.Linux: `aws ec2 describe-addresses-attribute \ --allocation-ids``eipalloc-abcdef01234567890`\ --attribute`domain-name`Windows: `aws ec2 describe-addresses-attribute``^`--allocation-ids`eipalloc-abcdef01234567890``^`--attribute`domain-name`Output: `{ "Addresses": [ { "PublicIp": "192.0.2.0", "AllocationId": "eipalloc-abcdef01234567890", "PtrRecord": "example.com." } ] }`To view the attributes of an elastic IP address, you must have first associated a domain name with the elastic IP address. For more information, see [Use reverse DNS for email applications](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#Using_Elastic_Addressing_Reverse_DNS)in the*Amazon EC2 User Guide*or[modify-address-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-address-attribute.html)in the*AWS CLI Command Reference*.- 
                    For API details, see [DescribeAddressesAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-addresses-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-addresses`.

- **AWS CLI**
- 
            
                    **Example 1: To retrieve details about all of your Elastic IP addresses**The following `describe addresses`example displays details about your Elastic IP addresses.`aws ec2 describe-addresses`Output: `{ "Addresses": [ { "InstanceId": "i-1234567890abcdef0", "PublicIp": "198.51.100.0", "PublicIpv4Pool": "amazon", "Domain": "standard" }, { "Domain": "vpc", "PublicIpv4Pool": "amazon", "InstanceId": "i-1234567890abcdef0", "NetworkInterfaceId": "eni-12345678", "AssociationId": "eipassoc-12345678", "NetworkInterfaceOwnerId": "123456789012", "PublicIp": "203.0.113.0", "AllocationId": "eipalloc-12345678", "PrivateIpAddress": "10.0.1.241" } ] }`**Example 2: To retrieve details your Elastic IP addresses for EC2-VPC**The following `describe-addresses`example displays details about your Elastic IP addresses for use with instances in a VPC.`aws ec2 describe-addresses \ --filters``"Name=domain,Values=vpc"`Output: `{ "Addresses": [ { "Domain": "vpc", "PublicIpv4Pool": "amazon", "InstanceId": "i-1234567890abcdef0", "NetworkInterfaceId": "eni-12345678", "AssociationId": "eipassoc-12345678", "NetworkInterfaceOwnerId": "123456789012", "PublicIp": "203.0.113.0", "AllocationId": "eipalloc-12345678", "PrivateIpAddress": "10.0.1.241" } ] }`**Example 3: To retrieve details about an Elastic IP address specified by allocation ID**The following `describe-addresses`example displays details about the Elastic IP address with the specified allocation ID, which is associated with an instance in EC2-VPC.`aws ec2 describe-addresses \ --allocation-ids``eipalloc-282d9641`Output: `{ "Addresses": [ { "Domain": "vpc", "PublicIpv4Pool": "amazon", "InstanceId": "i-1234567890abcdef0", "NetworkInterfaceId": "eni-1a2b3c4d", "AssociationId": "eipassoc-123abc12", "NetworkInterfaceOwnerId": "1234567891012", "PublicIp": "203.0.113.25", "AllocationId": "eipalloc-282d9641", "PrivateIpAddress": "10.251.50.12" } ] }`**Example 4: To retrieve details about an Elastic IP address specified by its VPC private IP address**The following `describe-addresses`example displays details about the Elastic IP address associated with a particular private IP address in EC2-VPC.`aws ec2 describe-addresses \ --filters``"Name=private-ip-address,Values=10.251.50.12"`**Example 5: To retrieve details about Elastic IP addresses in EC2-Classic**The following `describe-addresses`example displays details about your Elastic IP addresses for use in EC2-Classic.`aws ec2 describe-addresses \ --filters``"Name=domain,Values=standard"`Output: `{ "Addresses": [ { "InstanceId": "i-1234567890abcdef0", "PublicIp": "203.0.110.25", "PublicIpv4Pool": "amazon", "Domain": "standard" } ] }`**Example 6: To retrieve details about an Elastic IP addresses specified by its public IP address**The following `describe-addresses`example displays details about the Elastic IP address with the value`203.0.110.25`, which is associated with an instance in EC2-Classic.`aws ec2 describe-addresses \ --public-ips``203.0.110.25`Output: `{ "Addresses": [ { "InstanceId": "i-1234567890abcdef0", "PublicIp": "203.0.110.25", "PublicIpv4Pool": "amazon", "Domain": "standard" } ] }`- 
                    For API details, see [DescribeAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-aggregate-id-format`.

- **AWS CLI**
- 
            
                    **To describe the longer ID format settings for all resource types in a Region**The following `describe-aggregate-id-format`example describes the overall long ID format status for the current Region. The`Deadline`value indicates that the deadlines for these resources to permanently switch from the short ID format to the long ID format expired. The`UseLongIdsAggregated`value indicates that all IAM users and IAM roles are configured to use long ID format for all resource types.`aws ec2 describe-aggregate-id-format`Output: `{ "UseLongIdsAggregated": true, "Statuses": [ { "Deadline": "2018-08-13T02:00:00.000Z", "Resource": "network-interface-attachment", "UseLongIds": true }, { "Deadline": "2016-12-13T02:00:00.000Z", "Resource": "instance", "UseLongIds": true }, { "Deadline": "2018-08-13T02:00:00.000Z", "Resource": "elastic-ip-association", "UseLongIds": true }, ... ] }`- 
                    For API details, see [DescribeAggregateIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-aggregate-id-format.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-availability-zones`.

- **AWS CLI**
- 
            
                    **To describe your Availability Zones**The following example `describe-availability-zones`displays details for the Availability Zones that are available to you. The response includes Availability Zones only for the current Region. In this example, it uses the profiles default`us-west-2`(Oregon) Region.`aws ec2 describe-availability-zones`Output: `{ "AvailabilityZones": [ { "State": "available", "OptInStatus": "opt-in-not-required", "Messages": [], "RegionName": "us-west-2", "ZoneName": "us-west-2a", "ZoneId": "usw2-az1", "GroupName": "us-west-2", "NetworkBorderGroup": "us-west-2" }, { "State": "available", "OptInStatus": "opt-in-not-required", "Messages": [], "RegionName": "us-west-2", "ZoneName": "us-west-2b", "ZoneId": "usw2-az2", "GroupName": "us-west-2", "NetworkBorderGroup": "us-west-2" }, { "State": "available", "OptInStatus": "opt-in-not-required", "Messages": [], "RegionName": "us-west-2", "ZoneName": "us-west-2c", "ZoneId": "usw2-az3", "GroupName": "us-west-2", "NetworkBorderGroup": "us-west-2" }, { "State": "available", "OptInStatus": "opt-in-not-required", "Messages": [], "RegionName": "us-west-2", "ZoneName": "us-west-2d", "ZoneId": "usw2-az4", "GroupName": "us-west-2", "NetworkBorderGroup": "us-west-2" }, { "State": "available", "OptInStatus": "opted-in", "Messages": [], "RegionName": "us-west-2", "ZoneName": "us-west-2-lax-1a", "ZoneId": "usw2-lax1-az1", "GroupName": "us-west-2-lax-1", "NetworkBorderGroup": "us-west-2-lax-1" } ] }`- 
                    For API details, see [DescribeAvailabilityZones](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-availability-zones.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-aws-network-performance-metric-subscription`.

- **AWS CLI**
- 
            
                    **To describe your metric subscriptions**The following `describe-aws-network-performance-metric-subscriptions`example describes your metric subscriptions.`aws ec2 describe-aws-network-performance-metric-subscriptions`Output: `{ "Subscriptions": [ { "Source": "us-east-1", "Destination": "eu-west-1", "Metric": "aggregate-latency", "Statistic": "p50", "Period": "five-minutes" } ] }`For more information, see [Manage subscriptions](https://docs.aws.amazon.com/network-manager/latest/infrastructure-performance/nmip-subscriptions-cw.html)in the*Infrastructure Performance User Guide*.- 
                    For API details, see [DescribeAwsNetworkPerformanceMetricSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-aws-network-performance-metric-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-aws-network-performance-metric-subscriptions`.

- **AWS CLI**
- 
            
                    **To describe your metric subscriptions**The following `describe-aws-network-performance-metric-subscriptions`example describes your metric subscriptions.`aws ec2 describe-aws-network-performance-metric-subscriptions`Output: `{ "Subscriptions": [ { "Source": "us-east-1", "Destination": "eu-west-1", "Metric": "aggregate-latency", "Statistic": "p50", "Period": "five-minutes" } ] }`For more information, see [Manage subscriptions](https://docs.aws.amazon.com/network-manager/latest/infrastructure-performance/nmip-subscriptions-cw.html)in the*Infrastructure Performance User Guide*.- 
                    For API details, see [DescribeAwsNetworkPerformanceMetricSubscriptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-aws-network-performance-metric-subscriptions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-bundle-tasks`.

- **AWS CLI**
- 
            
                    **To describe your bundle tasks**This example describes all of your bundle tasks. Command: `aws ec2 describe-bundle-tasks`Output: `{ "BundleTasks": [ { "UpdateTime": "2015-09-15T13:26:54.000Z", "InstanceId": "i-1234567890abcdef0", "Storage": { "S3": { "Prefix": "winami", "Bucket": "bundletasks" } }, "State": "bundling", "StartTime": "2015-09-15T13:24:35.000Z", "Progress": "3%", "BundleId": "bun-2a4e041c" } ] }`- 
                    For API details, see [DescribeBundleTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-bundle-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-byoip-cidrs`.

- **AWS CLI**
- 
            
                    **To describe your provisioned address ranges**The following `describe-byoip-cidrs`example displays details about the public IPv4 address ranges that you provisioned for use by AWS.`aws ec2 describe-byoip-cidrs \ --max-results``5`Output: `{ "ByoipCidrs": [ { "Cidr": "203.0.113.25/24", "StatusMessage": "ipv4pool-ec2-1234567890abcdef0", "State": "provisioned" } ] }`- 
                    For API details, see [DescribeByoipCidrs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-byoip-cidrs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-capacity-reservation-fleets`.

- **AWS CLI**
- 
            
                    **To view a Capacity Reservation Fleet**The following `describe-capacity-reservation-fleets`example lists configuration and capacity information for the specified Capacity Reservation Fleet. It also lists details about the individual Capacity Reservations that are inside the Fleet.`aws ec2 describe-capacity-reservation-fleets \ --capacity-reservation-fleet-ids``crf-abcdef01234567890`Output: `{ "CapacityReservationFleets": [ { "State": "active", "EndDate": "2022-12-31T23:59:59.000Z", "InstanceMatchCriteria": "open", "Tags": [], "CapacityReservationFleetId": "crf-abcdef01234567890", "Tenancy": "default", "InstanceTypeSpecifications": [ { "CapacityReservationId": "cr-1234567890abcdef0", "AvailabilityZone": "us-east-1a", "FulfilledCapacity": 5.0, "Weight": 1.0, "CreateDate": "2022-07-02T08:34:33.398Z", "InstancePlatform": "Linux/UNIX", "TotalInstanceCount": 5, "Priority": 1, "EbsOptimized": true, "InstanceType": "m5.xlarge" } ], "TotalTargetCapacity": 5, "TotalFulfilledCapacity": 5.0, "CreateTime": "2022-07-02T08:34:33.397Z", "AllocationStrategy": "prioritized" } ] }`For more information about Capacity Reservation Fleets, see [Capacity Reservation Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeCapacityReservationFleets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-reservation-fleets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-capacity-reservations`.

- **AWS CLI**
- 
            
                    **Example 1: To describe one or more of your capacity reservations**The following `describe-capacity-reservations`example displays details about all of your capacity reservations in the current AWS Region.`aws ec2 describe-capacity-reservations`Output: `{ "CapacityReservations": [ { "CapacityReservationId": "cr-1234abcd56EXAMPLE ", "OwnerId": "123456789111", "CapacityReservationArn": "arn:aws:ec2:us-east-1:123456789111:capacity-reservation/cr-1234abcd56EXAMPLE", "AvailabilityZoneId": "use1-az2", "InstanceType": "c5.large", "InstancePlatform": "Linux/UNIX", "AvailabilityZone": "us-east-1a", "Tenancy": "default", "TotalInstanceCount": 1, "AvailableInstanceCount": 1, "EbsOptimized": true, "EphemeralStorage": false, "State": "active", "StartDate": "2024-10-23T15:00:24+00:00", "EndDateType": "unlimited", "InstanceMatchCriteria": "open", "CreateDate": "2024-10-23T15:00:24+00:00", "Tags": [], "CapacityAllocations": [] }, { "CapacityReservationId": "cr-abcdEXAMPLE9876ef ", "OwnerId": "123456789111", "CapacityReservationArn": "arn:aws:ec2:us-east-1:123456789111:capacity-reservation/cr-abcdEXAMPLE9876ef", "AvailabilityZoneId": "use1-az2", "InstanceType": "c4.large", "InstancePlatform": "Linux/UNIX", "AvailabilityZone": "us-east-1a", "Tenancy": "default", "TotalInstanceCount": 1, "AvailableInstanceCount": 1, "EbsOptimized": true, "EphemeralStorage": false, "State": "cancelled", "StartDate": "2024-10-23T15:01:03+00:00", "EndDateType": "unlimited", "InstanceMatchCriteria": "open", "CreateDate": "2024-10-23T15:01:02+00:00", "Tags": [], "CapacityAllocations": [] } ] }`**Example 2: To describe one or more of your capacity reservations**The following `describe-capacity-reservations`example displays details about the specified capacity reservation.`aws ec2 describe-capacity-reservations \ --capacity-reservation-ids``cr-1234abcd56EXAMPLE`Output: `{ "CapacityReservations": [ { "CapacityReservationId": "cr-abcdEXAMPLE9876ef ", "OwnerId": "123456789111", "CapacityReservationArn": "arn:aws:ec2:us-east-1:123456789111:capacity-reservation/cr-abcdEXAMPLE9876ef", "AvailabilityZoneId": "use1-az2", "InstanceType": "c4.large", "InstancePlatform": "Linux/UNIX", "AvailabilityZone": "us-east-1a", "Tenancy": "default", "TotalInstanceCount": 1, "AvailableInstanceCount": 1, "EbsOptimized": true, "EphemeralStorage": false, "State": "active", "StartDate": "2024-10-23T15:01:03+00:00", "EndDateType": "unlimited", "InstanceMatchCriteria": "open", "CreateDate": "2024-10-23T15:01:02+00:00", "Tags": [], "CapacityAllocations": [] } ] }`For more information, see [Viewing a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-using.html#capacity-reservations-view)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DescribeCapacityReservations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-reservations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-carrier-gateways`.

- **AWS CLI**
- 
            
                    **To describe all carrier gateways**The following `describe-carrier-gateways`example lists all your carrier gateways.`aws ec2 describe-carrier-gateways`Output: `{ "CarrierGateways": [ { "CarrierGatewayId": "cagw-0465cdEXAMPLE1111", "VpcId": "vpc-0c529aEXAMPLE", "State": "available", "OwnerId": "123456789012", "Tags": [ { "Key": "example", "Value": "tag" } ] } ] }`For more information, see Carrier gateways<https://docs.aws.amazon.com/vpc/latest/userguide/Carrier_Gateway.html> in the *Amazon Virtual Private Cloud User Guide*.- 
                    For API details, see [DescribeCarrierGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-carrier-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-classic-link-instances`.

- **AWS CLI**
- 
            
                    **To describe linked EC2-Classic instances**This example lists all of your linked EC2-Classic instances. Command: `aws ec2 describe-classic-link-instances`Output: `{ "Instances": [ { "InstanceId": "i-1234567890abcdef0", "VpcId": "vpc-88888888", "Groups": [ { "GroupId": "sg-11122233" } ], "Tags": [ { "Value": "ClassicInstance", "Key": "Name" } ] }, { "InstanceId": "i-0598c7d356eba48d7", "VpcId": "vpc-12312312", "Groups": [ { "GroupId": "sg-aabbccdd" } ], "Tags": [ { "Value": "ClassicInstance2", "Key": "Name" } ] } ] }`This example lists all of your linked EC2-Classic instances, and filters the response to include only instances that are linked to VPC vpc-88888888. Command: `aws ec2 describe-classic-link-instances --filter``"Name=vpc-id,Values=vpc-88888888"`Output: `{ "Instances": [ { "InstanceId": "i-1234567890abcdef0", "VpcId": "vpc-88888888", "Groups": [ { "GroupId": "sg-11122233" } ], "Tags": [ { "Value": "ClassicInstance", "Key": "Name" } ] } ] }`- 
                    For API details, see [DescribeClassicLinkInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-classic-link-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-client-vpn-authorization-rules`.

- **AWS CLI**
- 
            
                    **To describe the authorization rules for a Client VPN endpoint**The following `describe-client-vpn-authorization-rules`example displays details about the authorization rules for the specified Client VPN endpoint.`aws ec2 describe-client-vpn-authorization-rules \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`Output: `{ "AuthorizationRules": [ { "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "GroupId": "", "AccessAll": true, "DestinationCidr": "0.0.0.0/0", "Status": { "Code": "active" } } ] }`For more information, see [Authorization Rules](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DescribeClientVpnAuthorizationRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-authorization-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-client-vpn-connections`.

- **AWS CLI**
- 
            
                    **To describe the connections to a Client VPN endpoint**The following `describe-client-vpn-connections`example displays details about the client connections to the specified Client VPN endpoint.`aws ec2 describe-client-vpn-connections \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`Output: `{ "Connections": [ { "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "Timestamp": "2019-08-12 07:58:34", "ConnectionId": "cvpn-connection-0e03eb24267165acd", "ConnectionEstablishedTime": "2019-08-12 07:57:14", "IngressBytes": "32302", "EgressBytes": "5696", "IngressPackets": "332", "EgressPackets": "67", "ClientIp": "172.31.0.225", "CommonName": "client1.domain.tld", "Status": { "Code": "terminated" }, "ConnectionEndTime": "2019-08-12 07:58:34" }, { "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "Timestamp": "2019-08-12 08:02:54", "ConnectionId": "cvpn-connection-00668867a40f18253", "ConnectionEstablishedTime": "2019-08-12 08:02:53", "IngressBytes": "2951", "EgressBytes": "2611", "IngressPackets": "9", "EgressPackets": "6", "ClientIp": "172.31.0.226", "CommonName": "client1.domain.tld", "Status": { "Code": "active" }, "ConnectionEndTime": "-" } ] }`For more information, see [Client Connections](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DescribeClientVpnConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-client-vpn-endpoints`.

- **AWS CLI**
- 
            
                    **To describe your Client VPN endpoints**The following `describe-client-vpn-endpoints`example displays details about all of your Client VPN endpoints.`aws ec2 describe-client-vpn-endpoints`Output: `{ "ClientVpnEndpoints": [ { "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "Description": "Endpoint for Admin access", "Status": { "Code": "available" }, "CreationTime": "2020-11-13T11:37:27", "DnsName": "*.cvpn-endpoint-123456789123abcde.prod.clientvpn.ap-south-1.amazonaws.com", "ClientCidrBlock": "172.31.0.0/16", "DnsServers": [ "8.8.8.8" ], "SplitTunnel": false, "VpnProtocol": "openvpn", "TransportProtocol": "udp", "VpnPort": 443, "ServerCertificateArn": "arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "AuthenticationOptions": [ { "Type": "certificate-authentication", "MutualAuthentication": { "ClientRootCertificateChain": "arn:aws:acm:ap-south-1:123456789012:certificate/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE" } } ], "ConnectionLogOptions": { "Enabled": true, "CloudwatchLogGroup": "Client-vpn-connection-logs", "CloudwatchLogStream": "cvpn-endpoint-123456789123abcde-ap-south-1-2020/11/13-FCD8HEMVaCcw" }, "Tags": [ { "Key": "Name", "Value": "Client VPN" } ], "SecurityGroupIds": [ "sg-aabbcc11223344567" ], "VpcId": "vpc-a87f92c1", "SelfServicePortalUrl": "https://self-service.clientvpn.amazonaws.com/endpoints/cvpn-endpoint-123456789123abcde", "ClientConnectOptions": { "Enabled": false } } ] }`For more information, see [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DescribeClientVpnEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-client-vpn-routes`.

- **AWS CLI**
- 
            
                    **To describe the routes for a Client VPN endpoint**The following `describe-client-vpn-routes`example displays details about the routes for the specified Client VPN endpoint.`aws ec2 describe-client-vpn-routes \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`Output: `{ "Routes": [ { "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "DestinationCidr": "10.0.0.0/16", "TargetSubnet": "subnet-0123456789abcabca", "Type": "Nat", "Origin": "associate", "Status": { "Code": "active" }, "Description": "Default Route" }, { "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "DestinationCidr": "0.0.0.0/0", "TargetSubnet": "subnet-0123456789abcabca", "Type": "Nat", "Origin": "add-route", "Status": { "Code": "active" } } ] }`For more information, see [Routes](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-routes.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DescribeClientVpnRoutes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-routes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-client-vpn-target-networks`.

- **AWS CLI**
- 
            
                    **To describe the target networks for a Client VPN endpoint**The following `describe-client-vpn-target-networks`example displays details about the target networks for the specified Client VPN endpoint.`aws ec2 describe-client-vpn-target-networks \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`Output: `{ "ClientVpnTargetNetworks": [ { "AssociationId": "cvpn-assoc-012e837060753dc3d", "VpcId": "vpc-11111222222333333", "TargetNetworkId": "subnet-0123456789abcabca", "ClientVpnEndpointId": "cvpn-endpoint-123456789123abcde", "Status": { "Code": "associating" }, "SecurityGroups": [ "sg-012345678910abcab" ] } ] }`For more information, see [Target Networks](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DescribeClientVpnTargetNetworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-client-vpn-target-networks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-coip-pools`.

- **AWS CLI**
- 
            
                    **To describe customer-owned IP address pools**The following `describe-coip-pools`example describes the customer-owned IP address pools in your AWS account.`aws ec2 describe-coip-pools`Output: `{ "CoipPools": [ { "PoolId": "ipv4pool-coip-123a45678bEXAMPLE", "PoolCidrs": [ "0.0.0.0/0" ], "LocalGatewayRouteTableId": "lgw-rtb-059615ef7dEXAMPLE", "PoolArn": "arn:aws:ec2:us-west-2:123456789012:coip-pool/ipv4pool-coip-123a45678bEXAMPLE" } ] }`For more information, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-networking-components.html#ip-addressing)in the*AWS Outposts User Guide*.- 
                    For API details, see [DescribeCoipPools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-coip-pools.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-conversion-tasks`.

- **AWS CLI**
- 
            
                    **To view the status of a conversion task**This example returns the status of a conversion task with the ID import-i-ffvko9js. Command: `aws ec2 describe-conversion-tasks --conversion-task-ids``import-i-ffvko9js`Output: `{ "ConversionTasks": [ { "ConversionTaskId": "import-i-ffvko9js", "ImportInstance": { "InstanceId": "i-1234567890abcdef0", "Volumes": [ { "Volume": { "Id": "vol-049df61146c4d7901", "Size": 16 }, "Status": "completed", "Image": { "Size": 1300687360, "ImportManifestUrl": "https://s3.amazonaws.com/myimportbucket/411443cd-d620-4f1c-9d66-13144EXAMPLE/RHEL5.vmdkmanifest.xml?AWSAccessKeyId=AKIAIOSFODNN7EXAMPLE&Expires=140EXAMPLE&Signature=XYNhznHNgCqsjDxL9wRL%2FJvEXAMPLE", "Format": "VMDK" }, "BytesConverted": 1300682960, "AvailabilityZone": "us-east-1d" } ] }, "ExpirationTime": "2014-05-14T22:06:23Z", "State": "completed" } ] }`- 
                    For API details, see [DescribeConversionTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-conversion-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-customer-gateways`.

- **AWS CLI**
- 
            
                    **To describe your customer gateways**This example describes your customer gateways. Command: `aws ec2 describe-customer-gateways`Output: `{ "CustomerGateways": [ { "CustomerGatewayId": "cgw-b4dc3961", "IpAddress": "203.0.113.12", "State": "available", "Type": "ipsec.1", "BgpAsn": "65000" }, { "CustomerGatewayId": "cgw-0e11f167", "IpAddress": "12.1.2.3", "State": "available", "Type": "ipsec.1", "BgpAsn": "65534" } ] }`**To describe a specific customer gateway**This example describes the specified customer gateway. Command: `aws ec2 describe-customer-gateways --customer-gateway-ids``cgw-0e11f167`Output: `{ "CustomerGateways": [ { "CustomerGatewayId": "cgw-0e11f167", "IpAddress": "12.1.2.3", "State": "available", "Type": "ipsec.1", "BgpAsn": "65534" } ] }`- 
                    For API details, see [DescribeCustomerGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-customer-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-dhcp-options`.

- **AWS CLI**
- 
            
                    **Example 1: To describe your DHCP options**The following `describe-dhcp-options`example retrieves details about your DHCP options.`aws ec2 describe-dhcp-options`Output: `{ "DhcpOptions": [ { "DhcpConfigurations": [ { "Key": "domain-name", "Values": [ { "Value": "us-east-2.compute.internal" } ] }, { "Key": "domain-name-servers", "Values": [ { "Value": "AmazonProvidedDNS" } ] } ], "DhcpOptionsId": "dopt-19edf471", "OwnerId": "111122223333" }, { "DhcpConfigurations": [ { "Key": "domain-name", "Values": [ { "Value": "us-east-2.compute.internal" } ] }, { "Key": "domain-name-servers", "Values": [ { "Value": "AmazonProvidedDNS" } ] } ], "DhcpOptionsId": "dopt-fEXAMPLE", "OwnerId": "111122223333" } ] }`For more information, see [Working with DHCP Option Sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html#DHCPOptionSet)in the*AWS VPC User Guide*.**Example 2: To describe your DHCP options and filter the output**The following `describe-dhcp-options`example describes your DHCP options and uses a filter to return only DHCP options that have`example.com`for the domain name server. The example uses the`--query`parameter to display only the configuration information and ID in the output.`aws ec2 describe-dhcp-options \ --filters``Name=key,Values=domain-name-servers``Name=value,Values=example.com`\ --query`"DhcpOptions[*].[DhcpConfigurations,DhcpOptionsId]"`Output: `[ [ [ { "Key": "domain-name", "Values": [ { "Value": "example.com" } ] }, { "Key": "domain-name-servers", "Values": [ { "Value": "172.16.16.16" } ] } ], "dopt-001122334455667ab" ] ]`For more information, see [Working with DHCP Option Sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html#DHCPOptionSet)in the*AWS VPC User Guide*.- 
                    For API details, see [DescribeDhcpOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-dhcp-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-egress-only-internet-gateways`.

- **AWS CLI**
- 
            
                    **To describe your egress-only Internet gateways**This example describes your egress-only Internet gateways. Command: `aws ec2 describe-egress-only-internet-gateways`Output: `{ "EgressOnlyInternetGateways": [ { "EgressOnlyInternetGatewayId": "eigw-015e0e244e24dfe8a", "Attachments": [ { "State": "attached", "VpcId": "vpc-0c62a468" } ] } ] }`- 
                    For API details, see [DescribeEgressOnlyInternetGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-egress-only-internet-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-elastic-gpus`.

- **AWS CLI**
- 
            
                    **To describe an Elastic GPU**Command: `aws ec2 describe-elastic-gpus --elastic-gpu-ids``egpu-12345678901234567890abcdefghijkl`- 
                    For API details, see [DescribeElasticGpus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-elastic-gpus.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-export-image-tasks`.

- **AWS CLI**
- 
            
                    **To monitor an export image task**The following `describe-export-image-tasks`example checks the status of the specified export image task. The resulting image file in Amazon S3 is`my-export-bucket/exports/export-ami-1234567890abcdef0.vmdk`.`aws ec2 describe-export-image-tasks \ --export-image-task-ids``export-ami-1234567890abcdef0`Output for an export image task that is in progress. `{ "ExportImageTasks": [ { "ExportImageTaskId": "export-ami-1234567890abcdef0" "Progress": "21", "S3ExportLocation": { "S3Bucket": "my-export-bucket", "S3Prefix": "exports/" }, "Status": "active", "StatusMessage": "updating" } ] }`Output for an export image task that is completed. `{ "ExportImageTasks": [ { "ExportImageTaskId": "export-ami-1234567890abcdef0" "S3ExportLocation": { "S3Bucket": "my-export-bucket", "S3Prefix": "exports/" }, "Status": "completed" } ] }`For more information, see [Export a VM from an AMI](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport_image.html)in the*VM Import/Export User Guide*.- 
                    For API details, see [DescribeExportImageTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-export-image-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-export-tasks`.

- **AWS CLI**
- 
            
                    **To list details about an instance export task**This example describes the export task with ID export-i-fh8sjjsq. Command: `aws ec2 describe-export-tasks --export-task-ids``export-i-fh8sjjsq`Output: `{ "ExportTasks": [ { "State": "active", "InstanceExportDetails": { "InstanceId": "i-1234567890abcdef0", "TargetEnvironment": "vmware" }, "ExportToS3Task": { "S3Bucket": "myexportbucket", "S3Key": "RHEL5export-i-fh8sjjsq.ova", "DiskImageFormat": "vmdk", "ContainerFormat": "ova" }, "Description": "RHEL5 instance", "ExportTaskId": "export-i-fh8sjjsq" } ] }`- 
                    For API details, see [DescribeExportTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-export-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fast-launch-images`.

- **AWS CLI**
- 
            
                    **To describe the details for Windows AMIs that are configured for faster launching**The following `describe-fast-launch-images`example describes the details for each of the AMIs in your account that are configured for faster launching, including the resource type, the snapshot configuration, the launch template details, the maximum number of parallel launches, the AMI owner ID, the state of the fast launch configuration, the reason the state was changed, and the time that the state change occurred.`aws ec2 describe-fast-launch-images`Output: `{ "FastLaunchImages": [ { "ImageId": "ami-01234567890abcedf", "ResourceType": "snapshot", "SnapshotConfiguration": {}, "LaunchTemplate": { "LaunchTemplateId": "lt-01234567890abcedf", "LaunchTemplateName": "EC2FastLaunchDefaultResourceCreation-a8c6215d-94e6-441b-9272-dbd1f87b07e2", "Version": "1" }, "MaxParallelLaunches": 6, "OwnerId": "0123456789123", "State": "enabled", "StateTransitionReason": "Client.UserInitiated", "StateTransitionTime": "2022-01-27T22:20:06.552000+00:00" } ] }`For more information about configuring a Windows AMI for faster launching, see [Configure your AMI for faster launching](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/windows-ami-version-history.html#win-ami-config-fast-launch)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeFastLaunchImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fast-launch-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fast-snapshot-restores`.

- **AWS CLI**
- 
            
                    **To describe fast snapshot restores**The following `describe-fast-snapshot-restores`example displays details for all fast snapshot restores with a state of`disabled`.`aws ec2 describe-fast-snapshot-restores \ --filters``Name=state,Values=disabled`Output: `{ "FastSnapshotRestores": [ { "SnapshotId": "snap-1234567890abcdef0", "AvailabilityZone": "us-west-2c", "State": "disabled", "StateTransitionReason": "Client.UserInitiated - Lifecycle state transition", "OwnerId": "123456789012", "EnablingTime": "2020-01-25T23:57:49.596Z", "OptimizingTime": "2020-01-25T23:58:25.573Z", "EnabledTime": "2020-01-25T23:59:29.852Z", "DisablingTime": "2020-01-26T00:40:56.069Z", "DisabledTime": "2020-01-26T00:41:27.390Z" } ] }`The following `describe-fast-snapshot-restores`example describes all fast snapshot restores.`aws ec2 describe-fast-snapshot-restores`- 
                    For API details, see [DescribeFastSnapshotRestores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fast-snapshot-restores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleet-history`.

- **AWS CLI**
- 
            
                    **To describe EC2 Fleet history**The following `describe-fleet-history`example returns the history for the specified EC2 Fleet starting at the specified time. The output is for an EC2 Fleet with two running instances.`aws ec2 describe-fleet-history \ --fleet-id``fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE`\ --start-time`2020-09-01T00:00:00Z`Output: `{ "HistoryRecords": [ { "EventInformation": { "EventSubType": "submitted" }, "EventType": "fleetRequestChange", "Timestamp": "2020-09-01T18:26:05.000Z" }, { "EventInformation": { "EventSubType": "active" }, "EventType": "fleetRequestChange", "Timestamp": "2020-09-01T18:26:15.000Z" }, { "EventInformation": { "EventDescription": "t2.small, ami-07c8bc5c1ce9598c3, ...", "EventSubType": "progress" }, "EventType": "fleetRequestChange", "Timestamp": "2020-09-01T18:26:17.000Z" }, { "EventInformation": { "EventDescription": "{\"instanceType\":\"t2.small\", ...}", "EventSubType": "launched", "InstanceId": "i-083a1c446e66085d2" }, "EventType": "instanceChange", "Timestamp": "2020-09-01T18:26:17.000Z" }, { "EventInformation": { "EventDescription": "{\"instanceType\":\"t2.small\", ...}", "EventSubType": "launched", "InstanceId": "i-090db02406cc3c2d6" }, "EventType": "instanceChange", "Timestamp": "2020-09-01T18:26:17.000Z" } ], "LastEvaluatedTime": "2020-09-01T19:10:19.000Z", "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE", "StartTime": "2020-08-31T23:53:20.000Z" }`For more information, see [Managing an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DescribeFleetHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleet-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleet-instances`.

- **AWS CLI**
- 
            
                    **To describe the running instances for an EC2 Fleet**The following `describe-fleet-instances`example describes the running instances for the specified EC2 Fleet.`aws ec2 describe-fleet-instances \ --fleet-id``12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE`Output: `{ "ActiveInstances": [ { "InstanceId": "i-090db02406cc3c2d6", "InstanceType": "t2.small", "SpotInstanceRequestId": "sir-a43gtpfk", "InstanceHealth": "healthy" }, { "InstanceId": "i-083a1c446e66085d2", "InstanceType": "t2.small", "SpotInstanceRequestId": "sir-iwcit2nj", "InstanceHealth": "healthy" } ], "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE" }`For more information, see [Managing an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DescribeFleetInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleet-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fleets`.

- **AWS CLI**
- 
            
                    **To describe an EC2 Fleet**The following `describe-fleets`example describes the specified EC2 Fleet.`aws ec2 describe-fleets \ --fleet-ids``fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE`Output: `{ "Fleets": [ { "ActivityStatus": "pending_fulfillment", "CreateTime": "2020-09-01T18:26:05.000Z", "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE", "FleetState": "active", "ExcessCapacityTerminationPolicy": "termination", "FulfilledCapacity": 0.0, "FulfilledOnDemandCapacity": 0.0, "LaunchTemplateConfigs": [ { "LaunchTemplateSpecification": { "LaunchTemplateId": "lt-0e632f2855a979cd5", "Version": "1" } } ], "TargetCapacitySpecification": { "TotalTargetCapacity": 2, "OnDemandTargetCapacity": 0, "SpotTargetCapacity": 2, "DefaultTargetCapacityType": "spot" }, "TerminateInstancesWithExpiration": false, "Type": "maintain", "ReplaceUnhealthyInstances": false, "SpotOptions": { "AllocationStrategy": "lowestPrice", "InstanceInterruptionBehavior": "terminate", "InstancePoolsToUseCount": 1 }, "OnDemandOptions": { "AllocationStrategy": "lowestPrice" } } ] }`For more information, see [Managing an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DescribeFleets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-flow-logs`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all of your flow logs**The following `describe-flow-logs`example displays details for all of your flow logs.`aws ec2 describe-flow-logs`Output: `{ "FlowLogs": [ { "CreationTime": "2018-02-21T13:22:12.644Z", "DeliverLogsPermissionArn": "arn:aws:iam::123456789012:role/flow-logs-role", "DeliverLogsStatus": "SUCCESS", "FlowLogId": "fl-aabbccdd112233445", "MaxAggregationInterval": 600, "FlowLogStatus": "ACTIVE", "LogGroupName": "FlowLogGroup", "ResourceId": "subnet-12345678901234567", "TrafficType": "ALL", "LogDestinationType": "cloud-watch-logs", "LogFormat": "${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}" }, { "CreationTime": "2020-02-04T15:22:29.986Z", "DeliverLogsStatus": "SUCCESS", "FlowLogId": "fl-01234567890123456", "MaxAggregationInterval": 60, "FlowLogStatus": "ACTIVE", "ResourceId": "vpc-00112233445566778", "TrafficType": "ACCEPT", "LogDestinationType": "s3", "LogDestination": "arn:aws:s3:::my-flow-log-bucket/custom", "LogFormat": "${version} ${vpc-id} ${subnet-id} ${instance-id} ${interface-id} ${account-id} ${type} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${pkt-srcaddr} ${pkt-dstaddr} ${protocol} ${bytes} ${packets} ${start} ${end} ${action} ${tcp-flags} ${log-status}" } ] }`**Example 2: To describe a subset of your flow logs**The following `describe-flow-logs`example uses a filter to display details for only those flow logs that are in the specified log group in Amazon CloudWatch Logs.`aws ec2 describe-flow-logs \ --filter``"Name=log-group-name,Values=MyFlowLogs"`- 
                    For API details, see [DescribeFlowLogs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-flow-logs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fpga-image-attribute`.

- **AWS CLI**
- 
            
                    **To describe the attributes of an Amazon FPGA image**This example describes the load permissions for the specified AFI. Command: `aws ec2 describe-fpga-image-attribute --fpga-image-id``afi-0d123e123bfc85abc`--attribute`loadPermission`Output: `{ "FpgaImageAttribute": { "FpgaImageId": "afi-0d123e123bfc85abc", "LoadPermissions": [ { "UserId": "123456789012" } ] } }`- 
                    For API details, see [DescribeFpgaImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fpga-image-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-fpga-images`.

- **AWS CLI**
- 
            
                    **To describe Amazon FPGA images**This example describes AFIs that are owned by account `123456789012`.Command: `aws ec2 describe-fpga-images --filters``Name=owner-id,Values=123456789012`Output: `{ "FpgaImages": [ { "UpdateTime": "2017-12-22T12:09:14.000Z", "Name": "my-afi", "PciId": { "SubsystemVendorId": "0xfedd", "VendorId": "0x1d0f", "DeviceId": "0xf000", "SubsystemId": "0x1d51" }, "FpgaImageGlobalId": "agfi-123cb27b5e84a0abc", "Public": false, "State": { "Code": "available" }, "ShellVersion": "0x071417d3", "OwnerId": "123456789012", "FpgaImageId": "afi-0d123e123bfc85abc", "CreateTime": "2017-12-22T11:43:33.000Z", "Description": "my-afi" } ] }`- 
                    For API details, see [DescribeFpgaImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fpga-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-host-reservation-offerings`.

- **AWS CLI**
- 
            
                    **To describe Dedicated Host Reservation offerings**This example describes the Dedicated Host Reservations for the M4 instance family that are available to purchase. Command: `aws ec2 describe-host-reservation-offerings --filter``Name=instance-family,Values=m4`Output: `{ "OfferingSet": [ { "HourlyPrice": "1.499", "OfferingId": "hro-03f707bf363b6b324", "InstanceFamily": "m4", "PaymentOption": "NoUpfront", "UpfrontPrice": "0.000", "Duration": 31536000 }, { "HourlyPrice": "1.045", "OfferingId": "hro-0ef9181cabdef7a02", "InstanceFamily": "m4", "PaymentOption": "NoUpfront", "UpfrontPrice": "0.000", "Duration": 94608000 }, { "HourlyPrice": "0.714", "OfferingId": "hro-04567a15500b92a51", "InstanceFamily": "m4", "PaymentOption": "PartialUpfront", "UpfrontPrice": "6254.000", "Duration": 31536000 }, { "HourlyPrice": "0.484", "OfferingId": "hro-0d5d7a9d23ed7fbfe", "InstanceFamily": "m4", "PaymentOption": "PartialUpfront", "UpfrontPrice": "12720.000", "Duration": 94608000 }, { "HourlyPrice": "0.000", "OfferingId": "hro-05da4108ca998c2e5", "InstanceFamily": "m4", "PaymentOption": "AllUpfront", "UpfrontPrice": "23913.000", "Duration": 94608000 }, { "HourlyPrice": "0.000", "OfferingId": "hro-0a9f9be3b95a3dc8f", "InstanceFamily": "m4", "PaymentOption": "AllUpfront", "UpfrontPrice": "12257.000", "Duration": 31536000 } ] }`- 
                    For API details, see [DescribeHostReservationOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-host-reservation-offerings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-host-reservations`.

- **AWS CLI**
- 
            
                    **To describe Dedicated Host Reservations in your account**This example describes the Dedicated Host Reservations in your account. Command: `aws ec2 describe-host-reservations`Output: `{ "HostReservationSet": [ { "Count": 1, "End": "2019-01-10T12:14:09Z", "HourlyPrice": "1.499", "InstanceFamily": "m4", "OfferingId": "hro-03f707bf363b6b324", "PaymentOption": "NoUpfront", "State": "active", "HostIdSet": [ "h-013abcd2a00cbd123" ], "Start": "2018-01-10T12:14:09Z", "HostReservationId": "hr-0d418a3a4ffc669ae", "UpfrontPrice": "0.000", "Duration": 31536000 } ] }`- 
                    For API details, see [DescribeHostReservations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-host-reservations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-hosts`.

- **AWS CLI**
- 
            
                    **To view details about Dedicated Hosts**The following `describe-hosts`example displays details for the`available`Dedicated Hosts in your AWS account.`aws ec2 describe-hosts --filter``"Name=state,Values=available"`Output: `{ "Hosts": [ { "HostId": "h-07879acf49EXAMPLE", "Tags": [ { "Value": "production", "Key": "purpose" } ], "HostProperties": { "Cores": 48, "TotalVCpus": 96, "InstanceType": "m5.large", "Sockets": 2 }, "Instances": [], "State": "available", "AvailabilityZone": "eu-west-1a", "AvailableCapacity": { "AvailableInstanceCapacity": [ { "AvailableCapacity": 48, "InstanceType": "m5.large", "TotalCapacity": 48 } ], "AvailableVCpus": 96 }, "HostRecovery": "on", "AllocationTime": "2019-08-19T08:57:44.000Z", "AutoPlacement": "off" } ] }`For more information, see [Viewing Dedicated Hosts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-managing)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DescribeHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-hosts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-iam-instance-profile-associations`.

- **AWS CLI**
- 
            
                    **To describe IAM instance profile associations**This example describes all of your IAM instance profile associations. Command: `aws ec2 describe-iam-instance-profile-associations`Output: `{ "IamInstanceProfileAssociations": [ { "InstanceId": "i-09eb09efa73ec1dee", "State": "associated", "AssociationId": "iip-assoc-0db249b1f25fa24b8", "IamInstanceProfile": { "Id": "AIPAJVQN4F5WVLGCJDRGM", "Arn": "arn:aws:iam::123456789012:instance-profile/admin-role" } }, { "InstanceId": "i-0402909a2f4dffd14", "State": "associating", "AssociationId": "iip-assoc-0d1ec06278d29f44a", "IamInstanceProfile": { "Id": "AGJAJVQN4F5WVLGCJABCM", "Arn": "arn:aws:iam::123456789012:instance-profile/user1-role" } } ] }`- 
                    For API details, see [DescribeIamInstanceProfileAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-iam-instance-profile-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-id-format`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the ID format of a resource**The following `describe-id-format`example describes the ID format for security groups.`aws ec2 describe-id-format \ --resource``security-group`In the following example output, the `Deadline`value indicates that the deadline for this resource type to permanently switch from the short ID format to the long ID format expired at 00:00 UTC on August 15, 2018.`{ "Statuses": [ { "Deadline": "2018-08-15T00:00:00.000Z", "Resource": "security-group", "UseLongIds": true } ] }`**Example 2: To describe the ID format for all resources**The following `describe-id-format`example describes the ID format for all resource types. All resource types that supported the short ID format were switched to use the long ID format.`aws ec2 describe-id-format`- 
                    For API details, see [DescribeIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-id-format.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-identity-id-format`.

- **AWS CLI**
- 
            
                    **To describe the ID format for an IAM role**The following `describe-identity-id-format`example describes the ID format received by instances created by the IAM role`EC2Role`in your AWS account.`aws ec2 describe-identity-id-format \ --principal-arn``arn:aws:iam::123456789012:role/my-iam-role`\ --resource`instance`The following output indicates that instances created by this role receive IDs in long ID format. `{ "Statuses": [ { "Deadline": "2016-12-15T00:00:00Z", "Resource": "instance", "UseLongIds": true } ] }`**To describe the ID format for an IAM user**The following `describe-identity-id-format`example describes the ID format received by snapshots created by the IAM user`AdminUser`in your AWS account.`aws ec2 describe-identity-id-format \ --principal-arn``arn:aws:iam::123456789012:user/AdminUser`\ --resource`snapshot`The output indicates that snapshots created by this user receive IDs in long ID format. `{ "Statuses": [ { "Deadline": "2016-12-15T00:00:00Z", "Resource": "snapshot", "UseLongIds": true } ] }`- 
                    For API details, see [DescribeIdentityIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-identity-id-format.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-image-attribute`.

- **AWS CLI**
- 
            
                    **To describe the launch permissions for an AMI**This example describes the launch permissions for the specified AMI. Command: `aws ec2 describe-image-attribute --image-id``ami-5731123e`--attribute`launchPermission`Output: `{ "LaunchPermissions": [ { "UserId": "123456789012" } ], "ImageId": "ami-5731123e", }`**To describe the product codes for an AMI**This example describes the product codes for the specified AMI. Note that this AMI has no product codes. Command: `aws ec2 describe-image-attribute --image-id``ami-5731123e`--attribute`productCodes`Output: `{ "ProductCodes": [], "ImageId": "ami-5731123e", }`- 
                    For API details, see [DescribeImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-image-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-images`.

- **AWS CLI**
- 
            
                    **Example 1: To describe an AMI**The following `describe-images`example describes the specified AMI in the specified Region.`aws ec2 describe-images \ --region``us-east-1`\ --image-ids`ami-1234567890EXAMPLE`Output: `{ "Images": [ { "VirtualizationType": "hvm", "Description": "Provided by Red Hat, Inc.", "PlatformDetails": "Red Hat Enterprise Linux", "EnaSupport": true, "Hypervisor": "xen", "State": "available", "SriovNetSupport": "simple", "ImageId": "ami-1234567890EXAMPLE", "UsageOperation": "RunInstances:0010", "BlockDeviceMappings": [ { "DeviceName": "/dev/sda1", "Ebs": { "SnapshotId": "snap-111222333444aaabb", "DeleteOnTermination": true, "VolumeType": "gp2", "VolumeSize": 10, "Encrypted": false } } ], "Architecture": "x86_64", "ImageLocation": "123456789012/RHEL-8.0.0_HVM-20190618-x86_64-1-Hourly2-GP2", "RootDeviceType": "ebs", "OwnerId": "123456789012", "RootDeviceName": "/dev/sda1", "CreationDate": "2019-05-10T13:17:12.000Z", "Public": true, "ImageType": "machine", "Name": "RHEL-8.0.0_HVM-20190618-x86_64-1-Hourly2-GP2" } ] }`For more information, see [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)in the*Amazon EC2 User Guide*.**Example 2: To describe AMIs based on filters**The following `describe-images`example describes Windows AMIs provided by Amazon that are backed by Amazon EBS.`aws ec2 describe-images \ --owners``amazon`\ --filters`"Name=platform,Values=windows"``"Name=root-device-type,Values=ebs"`For an example of the output for `describe-images`, see Example 1.For additional examples using filters, see [Listing and filtering your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI)in the*Amazon EC2 User Guide*.**Example 3: To describe AMIs based on tags**The following `describe-images`example describes all AMIs that have the tag`Type=Custom`. The example uses the`--query`parameter to display only the AMI IDs.`aws ec2 describe-images \ --filters``"Name=tag:Type,Values=Custom"`\ --query '`Images[*].[ImageId]`' \ --output`text`Output: `ami-1234567890EXAMPLE ami-0abcdef1234567890`For additional examples using tag filters, see [Working with tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-import-image-tasks`.

- **AWS CLI**
- 
            
                    **To monitor an import image task**The following `describe-import-image-tasks`example checks the status of the specified import image task.`aws ec2 describe-import-image-tasks \ --import-task-ids``import-ami-1234567890abcdef0`Output for an import image task that is in progress. `{ "ImportImageTasks": [ { "ImportTaskId": "import-ami-1234567890abcdef0", "Progress": "28", "SnapshotDetails": [ { "DiskImageSize": 705638400.0, "Format": "ova", "Status": "completed", "UserBucket": { "S3Bucket": "my-import-bucket", "S3Key": "vms/my-server-vm.ova" } } ], "Status": "active", "StatusMessage": "converting" } ] }`Output for an import image task that is completed. The ID of the resulting AMI is provided by `ImageId`.`{ "ImportImageTasks": [ { "ImportTaskId": "import-ami-1234567890abcdef0", "ImageId": "ami-1234567890abcdef0", "SnapshotDetails": [ { "DiskImageSize": 705638400.0, "Format": "ova", "SnapshotId": "snap-1234567890abcdef0" "Status": "completed", "UserBucket": { "S3Bucket": "my-import-bucket", "S3Key": "vms/my-server-vm.ova" } } ], "Status": "completed" } ] }`- 
                    For API details, see [DescribeImportImageTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-import-image-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-import-snapshot-tasks`.

- **AWS CLI**
- 
            
                    **To monitor an import snapshot task**The following `describe-import-snapshot-tasks`example checks the status of the specified import snapshot task.`aws ec2 describe-import-snapshot-tasks \ --import-task-ids``import-snap-1234567890abcdef0`Output for an import snapshot task that is in progress: `{ "ImportSnapshotTasks": [ { "Description": "My server VMDK", "ImportTaskId": "import-snap-1234567890abcdef0", "SnapshotTaskDetail": { "Description": "My server VMDK", "DiskImageSize": "705638400.0", "Format": "VMDK", "Progress": "42", "Status": "active", "StatusMessage": "downloading/converting", "UserBucket": { "S3Bucket": "my-import-bucket", "S3Key": "vms/my-server-vm.vmdk" } } } ] }`Output for an import snapshot task that is completed. The ID of the resulting snapshot is provided by `SnapshotId`.`{ "ImportSnapshotTasks": [ { "Description": "My server VMDK", "ImportTaskId": "import-snap-1234567890abcdef0", "SnapshotTaskDetail": { "Description": "My server VMDK", "DiskImageSize": "705638400.0", "Format": "VMDK", "SnapshotId": "snap-1234567890abcdef0" "Status": "completed", "UserBucket": { "S3Bucket": "my-import-bucket", "S3Key": "vms/my-server-vm.vmdk" } } } ] }`- 
                    For API details, see [DescribeImportSnapshotTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-import-snapshot-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-attribute`.

- **AWS CLI**
- 
            
                    **To describe the instance type**This example describes the instance type of the specified instance. Command: `aws ec2 describe-instance-attribute --instance-id``i-1234567890abcdef0`--attribute`instanceType`Output: `{ "InstanceId": "i-1234567890abcdef0" "InstanceType": { "Value": "t1.micro" } }`**To describe the disableApiTermination attribute**This example describes the `disableApiTermination`attribute of the specified instance.Command: `aws ec2 describe-instance-attribute --instance-id``i-1234567890abcdef0`--attribute`disableApiTermination`Output: `{ "InstanceId": "i-1234567890abcdef0" "DisableApiTermination": { "Value": "false" } }`**To describe the block device mapping for an instance**This example describes the `blockDeviceMapping`attribute of the specified instance.Command: `aws ec2 describe-instance-attribute --instance-id``i-1234567890abcdef0`--attribute`blockDeviceMapping`Output: `{ "InstanceId": "i-1234567890abcdef0" "BlockDeviceMappings": [ { "DeviceName": "/dev/sda1", "Ebs": { "Status": "attached", "DeleteOnTermination": true, "VolumeId": "vol-049df61146c4d7901", "AttachTime": "2013-05-17T22:42:34.000Z" } }, { "DeviceName": "/dev/sdf", "Ebs": { "Status": "attached", "DeleteOnTermination": false, "VolumeId": "vol-049df61146c4d7901", "AttachTime": "2013-09-10T23:07:00.000Z" } } ], }`- 
                    For API details, see [DescribeInstanceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-connect-endpoints`.

- **AWS CLI**
- 
            
                    **To describe an EC2 Instance Connect Endpoint**The following `describe-instance-connect-endpoints`example describes the specified EC2 Instance Connect Endpoint.`aws ec2 describe-instance-connect-endpoints \ --region``us-east-1`\ --instance-connect-endpoint-ids`eice-0123456789example`Output: `{ "InstanceConnectEndpoints": [ { "OwnerId": "111111111111", "InstanceConnectEndpointId": "eice-0123456789example", "InstanceConnectEndpointArn": "arn:aws:ec2:us-east-1:111111111111:instance-connect-endpoint/eice-0123456789example", "State": "create-complete", "StateMessage": "", "DnsName": "eice-0123456789example.b67b86ba.ec2-instance-connect-endpoint.us-east-1.amazonaws.com", "NetworkInterfaceIds": [ "eni-0123456789example" ], "VpcId": "vpc-0123abcd", "AvailabilityZone": "us-east-1d", "CreatedAt": "2023-02-07T12:05:37+00:00", "SubnetId": "subnet-0123abcd", "Tags": [] } ] }`For more information, see [Create an EC2 Instance Connect Endpoint](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-ec2-instance-connect-endpoints.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeInstanceConnectEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-connect-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-credit-specifications`.

- **AWS CLI**
- 
            
                    **To describe the credit option for CPU usage of one or more instances**The following `describe-instance-credit-specifications`example describes the CPU credit option for the specified instance.`aws ec2 describe-instance-credit-specifications \ --instance-ids``i-1234567890abcdef0`Output: `{ "InstanceCreditSpecifications": [ { "InstanceId": "i-1234567890abcdef0", "CpuCredits": "unlimited" } ] }`For more information, see [Work with burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances-how-to.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeInstanceCreditSpecifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-credit-specifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-event-notification-attributes`.

- **AWS CLI**
- 
            
                    **To describe the tags for scheduled event notifications**The following `describe-instance-event-notification-attributes`example describes the tags to appear in scheduled event notifications.`aws ec2 describe-instance-event-notification-attributes`Output: `{ "InstanceTagAttribute": { "InstanceTagKeys": [], "IncludeAllTagsOfInstance": true } }`For more information, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html)in the*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DescribeInstanceEventNotificationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-event-notification-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-event-windows`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all event windows**The following `describe-instance-event-windows`example describes all event windows in the specified Region.`aws ec2 describe-instance-event-windows \ --region``us-east-1`Output: `{ "InstanceEventWindows": [ { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [ "i-1234567890abcdef0", "i-0598c7d356eba48d7" ], "Tags": [], "DedicatedHostIds": [] }, "State": "active", "Tags": [] } ... ], "NextToken": "9d624e0c-388b-4862-a31e-a85c64fc1d4a" }`**Example 2: To describe a specific event window**The following `describe-instance-event-windows`example describes a specific event by using the`instance-event-window`parameter to describe a specific event window.`aws ec2 describe-instance-event-windows \ --region``us-east-1`\ --instance-event-window-ids`iew-0abcdef1234567890`Output: `{ "InstanceEventWindows": [ { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [ "i-1234567890abcdef0", "i-0598c7d356eba48d7" ], "Tags": [], "DedicatedHostIds": [] }, "State": "active", "Tags": [] } }`**Example 3: To describe event windows that match one or more filters**The following `describe-instance-event-windows`example describes event windows that match one or more filters using the`filter`parameter. The`instance-id`filter is used to describe all of the event windows that are associated with the specified instance. When a filter is used, it performs a direct match. However, the`instance-id`filter is different. If there is no direct match to the instance ID, then it falls back to indirect associations with the event window, such as the tags of the instance or Dedicated Host ID (if the instance is a Dedicated Host).`aws ec2 describe-instance-event-windows \ --region``us-east-1`\ --filters`Name=instance-id,Values=i-1234567890abcdef0`\ --max-results`100`\ --next-token`<next-token-value>`Output: `{ "InstanceEventWindows": [ { "InstanceEventWindowId": "iew-0dbc0adb66f235982", "TimeRanges": [ { "StartWeekDay": "sunday", "StartHour": 2, "EndWeekDay": "sunday", "EndHour": 8 } ], "Name": "myEventWindowName", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": [ "h-0140d9a7ecbd102dd" ] }, "State": "active", "Tags": [] } ] }`In the example output, the instance is on a Dedicated Host, which is associated with the event window. For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeInstanceEventWindows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-event-windows.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-image-metadata`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the AMI metadata for all instances**The following `describe-instance-image-metadata`example describes the AMI metadata of all the instances in your AWS account in the specified Region.`aws ec2 describe-instance-image-metadata \ --region``us-east-1`Output: `{ "InstanceImageMetadata": [ { "InstanceId": "i-1234567890EXAMPLE", "InstanceType": "t2.micro", "LaunchTime": "2024-08-28T11:25:45+00:00", "AvailabilityZone": "us-east-1a", "State": { "Code": 16, "Name": "running" }, "OwnerId": "123412341234", "Tags": [ { "Key": "MyTagName", "Value": "my-tag-value" } ], "ImageMetadata": { "ImageId": "ami-0b752bf1df193a6c4", "Name": "al2023-ami-2023.5.20240819.0-kernel-6.1-x86_64", "OwnerId": "137112412989", "State": "available", "ImageOwnerAlias": "amazon", "CreationDate": "2023-01-25T17:20:40Z", "DeprecationTime": "2025-01-25T17:20:40Z", "IsPublic": true } } ], "NextToken": "...EXAMPLEwIAABAA2JHaFxLnEXAMPLE..." }`For more information, see [Amazon Machine Images in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)in the*Amazon EC2 User Guide*.**Example 2: To describe the AMI metadata for the specified instances**The following `describe-instance-image-metadata`example describes the AMI metadata for the specified instances.`aws ec2 describe-instance-image-metadata \ --region``us-east-1`\ --instance-ids`i-1234567890EXAMPLE``i-0987654321EXAMPLE`Output: `{ "InstanceImageMetadata": [ { "InstanceId": "i-1234567890EXAMPLE", "InstanceType": "t2.micro", "LaunchTime": "2024-08-28T11:25:45+00:00", "AvailabilityZone": "us-east-1a", "State": { "Code": 16, "Name": "running" }, "OwnerId": "123412341234", "Tags": [ { "Key": "MyTagName", "Value": "my-tag-value" } ], "ImageMetadata": { "ImageId": "ami-0b752bf1df193a6c4", "Name": "al2023-ami-2023.5.20240819.0-kernel-6.1-x86_64", "OwnerId": "137112412989", "State": "available", "ImageOwnerAlias": "amazon", "CreationDate": "2023-01-25T17:20:40Z", "DeprecationTime": "2025-01-25T17:20:40Z", "IsPublic": true } }, { "InstanceId": "i-0987654321EXAMPLE", "InstanceType": "t2.micro", "LaunchTime": "2024-08-28T11:25:45+00:00", "AvailabilityZone": "us-east-1a", "State": { "Code": 16, "Name": "running" }, "OwnerId": "123412341234", "Tags": [ { "Key": "MyTagName", "Value": "my-tag-value" } ], "ImageMetadata": { "ImageId": "ami-0b752bf1df193a6c4", "Name": "al2023-ami-2023.5.20240819.0-kernel-6.1-x86_64", "OwnerId": "137112412989", "State": "available", "ImageOwnerAlias": "amazon", "CreationDate": "2023-01-25T17:20:40Z", "DeprecationTime": "2025-01-25T17:20:40Z", "IsPublic": true } } ] }`For more information, see [Amazon Machine Images in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)in the*Amazon EC2 User Guide*.**Example 3: To describe the AMI metadata for instances based on filters**The following `describe-instance-image-metadata`example describes the AMI metadata for`t2.nano`and`t2.micro`instances in the`us-east-1a`Availability Zone.`aws ec2 describe-instance-image-metadata \ --region``us-east-1`\ --filters`Name=availability-zone,Values=us-east-1a``Name=instance-type,Values=t2.nano,t2.micro`Output: `{ "InstanceImageMetadata": [ { "InstanceId": "i-1234567890EXAMPLE", "InstanceType": "t2.micro", "LaunchTime": "2024-08-28T11:25:45+00:00", "AvailabilityZone": "us-east-1a", "State": { "Code": 16, "Name": "running" }, "OwnerId": "123412341234", "Tags": [ { "Key": "MyTagName", "Value": "my-tag-value" } ], "ImageMetadata": { "ImageId": "ami-0b752bf1df193a6c4", "Name": "al2023-ami-2023.5.20240819.0-kernel-6.1-x86_64", "OwnerId": "137112412989", "State": "available", "ImageOwnerAlias": "amazon", "CreationDate": "2023-01-25T17:20:40Z", "DeprecationTime": "2025-01-25T17:20:40Z", "IsPublic": true } }, { "InstanceId": "i-0987654321EXAMPLE", "InstanceType": "t2.micro", "LaunchTime": "2024-08-28T11:25:45+00:00", "AvailabilityZone": "us-east-1a", "State": { "Code": 16, "Name": "running" }, "OwnerId": "123412341234", "Tags": [ { "Key": "MyTagName", "Value": "my-tag-value" } ], "ImageMetadata": { "ImageId": "ami-0b752bf1df193a6c4", "Name": "al2023-ami-2023.5.20240819.0-kernel-6.1-x86_64", "OwnerId": "137112412989", "State": "available", "ImageOwnerAlias": "amazon", "CreationDate": "2023-01-25T17:20:40Z", "DeprecationTime": "2025-01-25T17:20:40Z", "IsPublic": true } } ], "NextToken": "...EXAMPLEV7ixRYHwIAABAA2JHaFxLnDAzpatfEXAMPLE..." }`For more information, see [Amazon Machine Images in Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeInstanceImageMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-image-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-status`.

- **AWS CLI**
- 
            
                    **To describe the status of an instance**The following `describe-instance-status`example describes the current status of the specified instance.`aws ec2 describe-instance-status \ --instance-ids``i-1234567890abcdef0`Output: `{ "InstanceStatuses": [ { "InstanceId": "i-1234567890abcdef0", "InstanceState": { "Code": 16, "Name": "running" }, "AvailabilityZone": "us-east-1d", "SystemStatus": { "Status": "ok", "Details": [ { "Status": "passed", "Name": "reachability" } ] }, "InstanceStatus": { "Status": "ok", "Details": [ { "Status": "passed", "Name": "reachability" } ] } } ] }`For more information, see [Monitor the status of your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeInstanceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-topology`.

- **AWS CLI**
- 
            
                    **To describe the instance topology of all your instances**The following `describe-instance-topology`example describes the topology of all your instances that match the supported instance types for this command.`aws ec2 describe-instance-topology \ --region``us-west-2`Output: `{ "Instances": [ { "InstanceId": "i-1111111111example", "InstanceType": "p4d.24xlarge", "GroupName": "my-ml-cpg", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example" ], "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a" }, { "InstanceId": "i-2222222222example", "InstanceType": "p4d.24xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-2222222222example", "nn-3333333333example" ], "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a" }, { "InstanceId": "i-3333333333example", "InstanceType": "trn1.32xlarge", "NetworkNodes": [ "nn-1212121212example", "nn-1211122211example", "nn-1311133311example" ], "ZoneId": "usw2-az4", "AvailabilityZone": "us-west-2d" }, { "InstanceId": "i-444444444example", "InstanceType": "trn1.2xlarge", "NetworkNodes": [ "nn-1111111111example", "nn-5434334334example", "nn-1235301234example" ], "ZoneId": "usw2-az2", "AvailabilityZone": "us-west-2a" } ], "NextToken": "SomeEncryptedToken" }`For more information, including more examples, see [Amazon EC2 instance topology](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-topology.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeInstanceTopology](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-topology.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-type-offerings`.

- **AWS CLI**
- 
            
                    **Example 1: To list the instance types offered in a Region**The following `describe-instance-type-offerings`example lists the instance types offered in the Region configured as the default Region for the AWS CLI.`aws ec2 describe-instance-type-offerings`To list the instance types offered in a different Region, specify the Region using the `--region`parameter.`aws ec2 describe-instance-type-offerings \ --region``us-east-2`Output: `{ "InstanceTypeOfferings": [ { "InstanceType": "m5.2xlarge", "LocationType": "region", "Location": "us-east-2" }, { "InstanceType": "t3.micro", "LocationType": "region", "Location": "us-east-2" }, ... ] }`**Example 2: To list the instance types offered in an Availability Zone**The following `describe-instance-type-offerings`example lists the instance types offered in the specified Availability Zone. The Availability Zone must be in the specified Region.`aws ec2 describe-instance-type-offerings \ --location-type``availability-zone`\ --filters`Name=location,Values=us-east-2a`\ --region`us-east-2`**Example 3: To check whether an instance type is supported**The following `describe-instance-type-offerings`command indicates whether the`c5.xlarge`instance type is supported in the specified Region.`aws ec2 describe-instance-type-offerings \ --filters``Name=instance-type,Values=c5.xlarge`\ --region`us-east-2`The following `describe-instance-type-offerings`example lists all C5 instance types that are supported in the specified Region.`aws ec2 describe-instance-type-offerings \ --filters``Name=instance-type,Values=c5*`\ --query`"InstanceTypeOfferings[].InstanceType"`\ --region`us-east-2`Output: `[ "c5d.12xlarge", "c5d.9xlarge", "c5n.xlarge", "c5.xlarge", "c5d.metal", "c5n.metal", "c5.large", "c5d.2xlarge", "c5n.4xlarge", "c5.2xlarge", "c5n.large", "c5n.9xlarge", "c5d.large", "c5.18xlarge", "c5d.18xlarge", "c5.12xlarge", "c5n.18xlarge", "c5.metal", "c5d.4xlarge", "c5.24xlarge", "c5d.xlarge", "c5n.2xlarge", "c5d.24xlarge", "c5.9xlarge", "c5.4xlarge" ]`- 
                    For API details, see [DescribeInstanceTypeOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-type-offerings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instance-types`.

- **AWS CLI**
- 
            
                    **Example 1: To describe an instance type**The following `describe-instance-types`example displays details for the specified instance type.`aws ec2 describe-instance-types \ --instance-types``t2.micro`Output: `{ "InstanceTypes": [ { "InstanceType": "t2.micro", "CurrentGeneration": true, "FreeTierEligible": true, "SupportedUsageClasses": [ "on-demand", "spot" ], "SupportedRootDeviceTypes": [ "ebs" ], "BareMetal": false, "Hypervisor": "xen", "ProcessorInfo": { "SupportedArchitectures": [ "i386", "x86_64" ], "SustainedClockSpeedInGhz": 2.5 }, "VCpuInfo": { "DefaultVCpus": 1, "DefaultCores": 1, "DefaultThreadsPerCore": 1, "ValidCores": [ 1 ], "ValidThreadsPerCore": [ 1 ] }, "MemoryInfo": { "SizeInMiB": 1024 }, "InstanceStorageSupported": false, "EbsInfo": { "EbsOptimizedSupport": "unsupported", "EncryptionSupport": "supported" }, "NetworkInfo": { "NetworkPerformance": "Low to Moderate", "MaximumNetworkInterfaces": 2, "Ipv4AddressesPerInterface": 2, "Ipv6AddressesPerInterface": 2, "Ipv6Supported": true, "EnaSupport": "unsupported" }, "PlacementGroupInfo": { "SupportedStrategies": [ "partition", "spread" ] }, "HibernationSupported": false, "BurstablePerformanceSupported": true, "DedicatedHostsSupported": false, "AutoRecoverySupported": true } ] }`For more information, see [Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)in*Amazon Elastic Compute Cloud User Guide for Linux Instances*.**Example 2: To filter the available instance types**You can specify a filter to scope the results to instance types that have a specific characteristic. The following `describe-instance-types`example lists the instance types that support hibernation.`aws ec2 describe-instance-types \ --filters``Name=hibernation-supported,Values=true`--query '`InstanceTypes[*].InstanceType`'Output: `[ "m5.8xlarge", "r3.large", "c3.8xlarge", "r5.large", "m4.4xlarge", "c4.large", "m5.xlarge", "m4.xlarge", "c3.large", "c4.8xlarge", "c4.4xlarge", "c5.xlarge", "c5.12xlarge", "r5.4xlarge", "c5.4xlarge" ]`For more information, see [Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)in*Amazon Elastic Compute Cloud User Guide for Linux Instances*.- 
                    For API details, see [DescribeInstanceTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instance-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-instances`.

- **AWS CLI**
- 
            
                    **Example 1: To describe an instance**The following `describe-instances`example describes the specified instance.`aws ec2 describe-instances \ --instance-ids``i-1234567890abcdef0`Output: `{ "Reservations": [ { "Groups": [], "Instances": [ { "AmiLaunchIndex": 0, "ImageId": "ami-0abcdef1234567890", "InstanceId": "i-1234567890abcdef0", "InstanceType": "t3.nano", "KeyName": "my-key-pair", "LaunchTime": "2022-11-15T10:48:59+00:00", "Monitoring": { "State": "disabled" }, "Placement": { "AvailabilityZone": "us-east-2a", "GroupName": "", "Tenancy": "default" }, "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal", "PrivateIpAddress": "10-0-0-157", "ProductCodes": [], "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com", "PublicIpAddress": "34.253.223.13", "State": { "Code": 16, "Name": "running" }, "StateTransitionReason": "", "SubnetId": "subnet-04a636d18e83cfacb", "VpcId": "vpc-1234567890abcdef0", "Architecture": "x86_64", "BlockDeviceMappings": [ { "DeviceName": "/dev/xvda", "Ebs": { "AttachTime": "2022-11-15T10:49:00+00:00", "DeleteOnTermination": true, "Status": "attached", "VolumeId": "vol-02e6ccdca7de29cf2" } } ], "ClientToken": "1234abcd-1234-abcd-1234-d46a8903e9bc", "EbsOptimized": true, "EnaSupport": true, "Hypervisor": "xen", "IamInstanceProfile": { "Arn": "arn:aws:iam::111111111111:instance-profile/AmazonSSMRoleForInstancesQuickSetup", "Id": "111111111111111111111" }, "NetworkInterfaces": [ { "Association": { "IpOwnerId": "amazon", "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com", "PublicIp": "34.253.223.13" }, "Attachment": { "AttachTime": "2022-11-15T10:48:59+00:00", "AttachmentId": "eni-attach-1234567890abcdefg", "DeleteOnTermination": true, "DeviceIndex": 0, "Status": "attached", "NetworkCardIndex": 0 }, "Description": "", "Groups": [ { "GroupName": "launch-wizard-146", "GroupId": "sg-1234567890abcdefg" } ], "Ipv6Addresses": [], "MacAddress": "00:11:22:33:44:55", "NetworkInterfaceId": "eni-1234567890abcdefg", "OwnerId": "104024344472", "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal", "PrivateIpAddress": "10-0-0-157", "PrivateIpAddresses": [ { "Association": { "IpOwnerId": "amazon", "PublicDnsName": "ec2-34-253-223-13.us-east-2.compute.amazonaws.com", "PublicIp": "34.253.223.13" }, "Primary": true, "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal", "PrivateIpAddress": "10-0-0-157" } ], "SourceDestCheck": true, "Status": "in-use", "SubnetId": "subnet-1234567890abcdefg", "VpcId": "vpc-1234567890abcdefg", "InterfaceType": "interface" } ], "RootDeviceName": "/dev/xvda", "RootDeviceType": "ebs", "SecurityGroups": [ { "GroupName": "launch-wizard-146", "GroupId": "sg-1234567890abcdefg" } ], "SourceDestCheck": true, "Tags": [ { "Key": "Name", "Value": "my-instance" } ], "VirtualizationType": "hvm", "CpuOptions": { "CoreCount": 1, "ThreadsPerCore": 2 }, "CapacityReservationSpecification": { "CapacityReservationPreference": "open" }, "HibernationOptions": { "Configured": false }, "MetadataOptions": { "State": "applied", "HttpTokens": "optional", "HttpPutResponseHopLimit": 1, "HttpEndpoint": "enabled", "HttpProtocolIpv6": "disabled", "InstanceMetadataTags": "enabled" }, "EnclaveOptions": { "Enabled": false }, "PlatformDetails": "Linux/UNIX", "UsageOperation": "RunInstances", "UsageOperationUpdateTime": "2022-11-15T10:48:59+00:00", "PrivateDnsNameOptions": { "HostnameType": "ip-name", "EnableResourceNameDnsARecord": true, "EnableResourceNameDnsAAAARecord": false }, "MaintenanceOptions": { "AutoRecovery": "default" } } ], "OwnerId": "111111111111", "ReservationId": "r-1234567890abcdefg" } ] }`**Example 2: To filter for instances with the specified type**The following `describe-instances`example uses filters to scope the results to instances of the specified type.`aws ec2 describe-instances \ --filters``Name=instance-type,Values=m5.large`For example output, see Example 1. For more information, see [List and filter using the CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI)in the*Amazon EC2 User Guide*.**Example 3: To filter for instances with the specified type and Availability Zone**The following `describe-instances`example uses multiple filters to scope the results to instances with the specified type that are also in the specified Availability Zone.`aws ec2 describe-instances \ --filters``Name=instance-type,Values=t2.micro,t3.micro``Name=availability-zone,Values=us-east-2c`For example output, see Example 1. **Example 4: To filter for instances with the specified type and Availability Zone using a JSON file**The following `describe-instances`example uses a JSON input file to perform the same filtering as the previous example. When filters get more complicated, they can be easier to specify in a JSON file.`aws ec2 describe-instances \ --filters``file://filters.json`Contents of `filters.json`:`[ { "Name": "instance-type", "Values": ["t2.micro", "t3.micro"] }, { "Name": "availability-zone", "Values": ["us-east-2c"] } ]`For example output, see Example 1. **Example 5: To filter for instances with the specified Owner tag**The following `describe-instances`example uses tag filters to scope the results to instances that have a tag with the specified tag key (Owner), regardless of the tag value.`aws ec2 describe-instances \ --filters``"Name=tag-key,Values=Owner"`For example output, see Example 1. **Example 6: To filter for instances with the specified my-team tag value**The following `describe-instances`example uses tag filters to scope the results to instances that have a tag with the specified tag value (my-team), regardless of the tag key.`aws ec2 describe-instances \ --filters``"Name=tag-value,Values=my-team"`For example output, see Example 1. **Example 7: To filter for instances with the specified Owner tag and my-team value**The following `describe-instances`example uses tag filters to scope the results to instances that have the specified tag (Owner=my-team).`aws ec2 describe-instances \ --filters``"Name=tag:Owner,Values=my-team"`For example output, see Example 1. **Example 8: To display only instance and subnet IDs for all instances**The following `describe-instances`examples use the`--query`parameter to display only the instance and subnet IDs for all instances, in JSON format.Linux and macOS: `aws ec2 describe-instances \ --query '``Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId}`' \ --output`json`Windows: `aws ec2 describe-instances``^`--query`"Reservations[*].Instances[*].{Instance:InstanceId,Subnet:SubnetId}"``^`--output`json`Output: `[ { "Instance": "i-057750d42936e468a", "Subnet": "subnet-069beee9b12030077" }, { "Instance": "i-001efd250faaa6ffa", "Subnet": "subnet-0b715c6b7db68927a" }, { "Instance": "i-027552a73f021f3bd", "Subnet": "subnet-0250c25a1f4e15235" } ... ]`**Example 9: To filter instances of the specified type and only display their instance IDs**The following `describe-instances`example uses filters to scope the results to instances of the specified type and the`--query`parameter to display only the instance IDs.`aws ec2 describe-instances \ --filters``"Name=instance-type,Values=t2.micro"`\ --query`"Reservations[*].Instances[*].[InstanceId]"`\ --output`text`Output: `i-031c0dc19de2fb70c i-00d8bff789a736b75 i-0b715c6b7db68927a i-0626d4edd54f1286d i-00b8ae04f9f99908e i-0fc71c25d2374130c`**Example 10: To filter instances of the specified type and only display their instance IDs, Availability Zone, and the specified tag value**The following `describe-instances`examples display the instance ID, Availability Zone, and the value of the`Name`tag for instances that have a tag with the name`tag-key`, in table format.Linux and macOS: `aws ec2 describe-instances \ --filters``Name=tag-key,Values=Name`\ --query '`Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==`Name`]|[0].Value}`' \ --output`table`Windows: `aws ec2 describe-instances``^`--filters`Name=tag-key,Values=Name``^`--query`"Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='Name']|[0].Value}"``^`--output`table`Output: `------------------------------------------------------------- | DescribeInstances | +--------------+-----------------------+--------------------+ | AZ | Instance | Name | +--------------+-----------------------+--------------------+ | us-east-2b | i-057750d42936e468a | my-prod-server | | us-east-2a | i-001efd250faaa6ffa | test-server-1 | | us-east-2a | i-027552a73f021f3bd | test-server-2 | +--------------+-----------------------+--------------------+`**Example 11: To describe instances in a partition placement group**The following `describe-instances`example describes the specified instance. The output includes the placement information for the instance, which contains the placement group name and the partition number for the instance.`aws ec2 describe-instances \ --instance-ids``i-0123a456700123456`\ --query`"Reservations[*].Instances[*].Placement"`Output: `[ [ { "AvailabilityZone": "us-east-1c", "GroupName": "HDFS-Group-A", "PartitionNumber": 3, "Tenancy": "default" } ] ]`For more information, see [Describing instances in a placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#describe-instance-placement)in the*Amazon EC2 User Guide*.**Example 12: To filter to instances with the specified placement group and partition number**The following `describe-instances`example filters the results to only those instances with the specified placement group and partition number.`aws ec2 describe-instances \ --filters``"Name=placement-group-name,Values=HDFS-Group-A"``"Name=placement-partition-number,Values=7"`The following shows only the relevant information from the output. `"Instances": [ { "InstanceId": "i-0123a456700123456", "InstanceType": "r4.large", "Placement": { "AvailabilityZone": "us-east-1c", "GroupName": "HDFS-Group-A", "PartitionNumber": 7, "Tenancy": "default" } }, { "InstanceId": "i-9876a543210987654", "InstanceType": "r4.large", "Placement": { "AvailabilityZone": "us-east-1c", "GroupName": "HDFS-Group-A", "PartitionNumber": 7, "Tenancy": "default" } ],`For more information, see [Describing instances in a placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#describe-instance-placement)in the*Amazon EC2 User Guide*.**Example 13: To filter to instances that are configured to allow access to tags from instance metadata**The following `describe-instances`example filters the results to only those instances that are configured to allow access to instance tags from instance metadata.`aws ec2 describe-instances \ --filters``"Name=metadata-options.instance-metadata-tags,Values=enabled"`\ --query`"Reservations[*].Instances[*].InstanceId"`\ --output`text`The following shows the expected output. `i-1234567890abcdefg i-abcdefg1234567890 i-11111111aaaaaaaaa i-aaaaaaaa111111111`For more information, see [Work with instance tags in instance metadata](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/Using_Tags.html#view-access-to-tags-in-IMDS)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-internet-gateways`.

- **AWS CLI**
- 
            
                    **To describe an internet gateway**The following `describe-internet-gateways`example describes the specified internet gateway.`aws ec2 describe-internet-gateways \ --internet-gateway-ids``igw-0d0fb496b3EXAMPLE`Output: `{ "InternetGateways": [ { "Attachments": [ { "State": "available", "VpcId": "vpc-0a60eb65b4EXAMPLE" } ], "InternetGatewayId": "igw-0d0fb496b3EXAMPLE", "OwnerId": "123456789012", "Tags": [ { "Key": "Name", "Value": "my-igw" } ] } ] }`For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DescribeInternetGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-internet-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ipam-pools`.

- **AWS CLI**
- 
            
                    **To view the details for an IPAM pool**The following `describe-ipam-pools`example shows the details for pools.(Linux): `aws ec2 describe-ipam-pools \ --filters``Name=owner-id,Values=123456789012``Name=ipam-scope-id,Values=ipam-scope-02fc38cd4c48e7d38`(Windows): `aws ec2 describe-ipam-pools``^`--filters`Name=owner-id,Values=123456789012``Name=ipam-scope-id,Values=ipam-scope-02fc38cd4c48e7d38`Output: `{ "IpamPools": [ { "OwnerId": "123456789012", "IpamPoolId": "ipam-pool-02ec043a19bbe5d08", "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-02ec043a19bbe5d08", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-02fc38cd4c48e7d38", "IpamScopeType": "private", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "Locale": "None", "PoolDepth": 1, "State": "create-complete", "AutoImport": true, "AddressFamily": "ipv4", "AllocationMinNetmaskLength": 16, "AllocationMaxNetmaskLength": 26, "AllocationDefaultNetmaskLength": 24, "AllocationResourceTags": [ { "Key": "Environment", "Value": "Preprod" } ], "Tags": [ { "Key": "Name", "Value": "Preprod pool" } ] } ] }`- 
                    For API details, see [DescribeIpamPools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-pools.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ipam-resource-discoveries`.

- **AWS CLI**
- 
            
                    **Example 1: View complete details of resource discoveries**In this example, you're a delegated IPAM admin who wants to create and share a resource discovery with the IPAM admin in another AWS Organization so that the admin can manage and monitor the IP addresses of resources in your organization. This example may be useful if: You tried to create a resource discovery, but you got an error that you've reached your limit of 1. You realize that you may have already created a resource discovery and you want to view it in your account.You have resources in a Region that are not being discovered by the IPAM. You want to view the `--operating-regions`defined for the resource and ensure that you've added the right Region as an operating Region so that the resources there can be discovered.The following `describe-ipam-resource-discoveries`example lists the details of the resource discovery in your AWS account. You can have one resource discovery per AWS Region.`aws ec2 describe-ipam-resource-discoveries \ --region``us-east-1`Output: `{ "IpamResourceDiscoveries": [ { "OwnerId": "149977607591", "IpamResourceDiscoveryId": "ipam-res-disco-0f8bdee9067137c0d", "IpamResourceDiscoveryArn": "arn:aws:ec2::149977607591:ipam-resource-discovery/ipam-res-disco-0f8bdee9067137c0d", "IpamResourceDiscoveryRegion": "us-east-1", "OperatingRegions": [ { "RegionName": "us-east-1" } ], "IsDefault": false, "State": "create-complete", "Tags": [] } ] }`For more information, see [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)in the*Amazon VPC IPAM User Guide*.**Example 2: View only resource discovery IDs**The following `describe-ipam-resource-discoveries`example lists the ID of the resource discovery in your AWS account. You can have one resource discovery per AWS Region.`aws ec2 describe-ipam-resource-discoveries \ --query``"IpamResourceDiscoveries[*].IpamResourceDiscoveryId"`\ --output`text`Output: `ipam-res-disco-0481e39b242860333`For more information, see [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DescribeIpamResourceDiscoveries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-resource-discoveries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ipam-resource-discovery-associations`.

- **AWS CLI**
- 
            
                    **To view all resource discovery associations with your IPAM**In this example, you're a IPAM delegated admin who has associated resource discoveries with your IPAM to integrate other accounts with your IPAM. You've noticed that your IPAM is not discovering the resources in the operating Regions of the resource discovery as expected. You want to check the status and state of the resource discovery to ensure that the account that created it is still active and the resource discovery is still being shared. The `--region`must be the home Region of your IPAM.The following `describe-ipam-resource-discovery-associations`example lists the resource discovery associations in your AWS account.`aws ec2 describe-ipam-resource-discovery-associations \ --region``us-east-1`Output: `{ "IpamResourceDiscoveryAssociations": [ { "OwnerId": "320805250157", "IpamResourceDiscoveryAssociationId": "ipam-res-disco-assoc-05e6b45eca5bf5cf7", "IpamResourceDiscoveryAssociationArn": "arn:aws:ec2::320805250157:ipam-resource-discovery-association/ipam-res-disco-assoc-05e6b45eca5bf5cf7", "IpamResourceDiscoveryId": "ipam-res-disco-0f4ef577a9f37a162", "IpamId": "ipam-005f921c17ebd5107", "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-005f921c17ebd5107", "IpamRegion": "us-east-1", "IsDefault": true, "ResourceDiscoveryStatus": "active", "State": "associate-complete", "Tags": [] }, { "OwnerId": "149977607591", "IpamResourceDiscoveryAssociationId": "ipam-res-disco-assoc-0dfd21ae189ab5f62", "IpamResourceDiscoveryAssociationArn": "arn:aws:ec2::149977607591:ipam-resource-discovery-association/ipam-res-disco-assoc-0dfd21ae189ab5f62", "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe", "IpamId": "ipam-005f921c17ebd5107", "IpamArn": "arn:aws:ec2::149977607591:ipam/ipam-005f921c17ebd5107", "IpamRegion": "us-east-1", "IsDefault": false, "ResourceDiscoveryStatus": "active", "State": "create-complete", "Tags": [] } ] }`In this example, after running this command, you notice that you have one non-default resource discovery ( `"IsDefault": false ``) that is ``"ResourceDiscoveryStatus": "not-found"`and`"State": "create-complete"`. The resource discovery owner's account has been closed. If, in another case, you notice that is`"ResourceDiscoveryStatus": "not-found"`and`"State": "associate-complete"`, this indicates that one of the following has happened:The resource discovery was deleted by the resource discovery owner.The resource discovery owner unshared the resource discovery. For more information, see [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DescribeIpamResourceDiscoveryAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-resource-discovery-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ipam-scopes`.

- **AWS CLI**
- 
            
                    **To view the details for an IPAM scope**The following `describe-ipam-scopes`example shows the details for scopes.`aws ec2 describe-ipam-scopes \ --filters``Name=owner-id,Values=123456789012``Name=ipam-id,Values=ipam-08440e7a3acde3908`Output: `{ "IpamScopes": [ { "OwnerId": "123456789012", "IpamScopeId": "ipam-scope-02fc38cd4c48e7d38", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-02fc38cd4c48e7d38", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "IpamScopeType": "private", "IsDefault": true, "PoolCount": 2, "State": "create-complete", "Tags": [] }, { "OwnerId": "123456789012", "IpamScopeId": "ipam-scope-0b9eed026396dbc16", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0b9eed026396dbc16", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "IpamScopeType": "public", "IsDefault": true, "PoolCount": 0, "State": "create-complete", "Tags": [] }, { "OwnerId": "123456789012", "IpamScopeId": "ipam-scope-0f1aff29486355c22", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-0f1aff29486355c22", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "IpamScopeType": "private", "IsDefault": false, "Description": "Example description", "PoolCount": 0, "State": "create-complete", "Tags": [ { "Key": "Name", "Value": "Example name value" } ] } ] }`- 
                    For API details, see [DescribeIpamScopes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-scopes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ipams`.

- **AWS CLI**
- 
            
                    **To view the details for an IPAM**The following `describe-ipams`example shows the details of an IPAM.`aws ec2 describe-ipams \ --filters``Name=owner-id,Values=123456789012`Output: `{ "Ipams": [ { "OwnerId": "123456789012", "IpamId": "ipam-08440e7a3acde3908", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "PublicDefaultScopeId": "ipam-scope-0b9eed026396dbc16", "PrivateDefaultScopeId": "ipam-scope-02fc38cd4c48e7d38", "ScopeCount": 3, "OperatingRegions": [ { "RegionName": "us-east-1" }, { "RegionName": "us-east-2" }, { "RegionName": "us-west-1" } ], "State": "create-complete", "Tags": [ { "Key": "Name", "Value": "ExampleIPAM" } ] } ] }`- 
                    For API details, see [DescribeIpams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-ipv6-pools`.

- **AWS CLI**
- 
            
                    **To describe your IPv6 address pools**The following `describe-ipv6-pools`example displays details for all of your IPv6 address pools.`aws ec2 describe-ipv6-pools`Output: `{ "Ipv6Pools": [ { "PoolId": "ipv6pool-ec2-012345abc12345abc", "PoolCidrBlocks": [ { "Cidr": "2001:db8:123::/48" } ], "Tags": [ { "Key": "pool-1", "Value": "public" } ] } ] }`- 
                    For API details, see [DescribeIpv6Pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipv6-pools.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-key-pairs`.

- **AWS CLI**
- 
            
                    **To display a key pair**The following `describe-key-pairs`example displays information about the specified key pair.`aws ec2 describe-key-pairs \ --key-names``my-key-pair`Output: `{ "KeyPairs": [ { "KeyPairId": "key-0b94643da6EXAMPLE", "KeyFingerprint": "1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca:9f:f5:f1:6f", "KeyName": "my-key-pair", "KeyType": "rsa", "Tags": [], "CreateTime": "2022-05-27T21:51:16.000Z" } ] }`For more information, see [Describe public keys](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/describe-keys.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeKeyPairs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-key-pairs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-launch-template-versions`.

- **AWS CLI**
- 
            
                    **To describe launch template versions**This example describes the versions of the specified launch template. Command: `aws ec2 describe-launch-template-versions --launch-template-id``lt-068f72b72934aff71`Output: `{ "LaunchTemplateVersions": [ { "LaunchTemplateId": "lt-068f72b72934aff71", "LaunchTemplateName": "Webservers", "VersionNumber": 3, "CreatedBy": "arn:aws:iam::123456789102:root", "LaunchTemplateData": { "KeyName": "kp-us-east", "ImageId": "ami-6057e21a", "InstanceType": "t2.small", "NetworkInterfaces": [ { "SubnetId": "subnet-7b16de0c", "DeviceIndex": 0, "Groups": [ "sg-7c227019" ] } ] }, "DefaultVersion": false, "CreateTime": "2017-11-20T13:19:54.000Z" }, { "LaunchTemplateId": "lt-068f72b72934aff71", "LaunchTemplateName": "Webservers", "VersionNumber": 2, "CreatedBy": "arn:aws:iam::123456789102:root", "LaunchTemplateData": { "KeyName": "kp-us-east", "ImageId": "ami-6057e21a", "InstanceType": "t2.medium", "NetworkInterfaces": [ { "SubnetId": "subnet-1a2b3c4d", "DeviceIndex": 0, "Groups": [ "sg-7c227019" ] } ] }, "DefaultVersion": false, "CreateTime": "2017-11-20T13:12:32.000Z" }, { "LaunchTemplateId": "lt-068f72b72934aff71", "LaunchTemplateName": "Webservers", "VersionNumber": 1, "CreatedBy": "arn:aws:iam::123456789102:root", "LaunchTemplateData": { "UserData": "", "KeyName": "kp-us-east", "ImageId": "ami-aabbcc11", "InstanceType": "t2.medium", "NetworkInterfaces": [ { "SubnetId": "subnet-7b16de0c", "DeviceIndex": 0, "DeleteOnTermination": false, "Groups": [ "sg-7c227019" ], "AssociatePublicIpAddress": true } ] }, "DefaultVersion": true, "CreateTime": "2017-11-20T12:52:33.000Z" } ] }`- 
                    For API details, see [DescribeLaunchTemplateVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-template-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-launch-templates`.

- **AWS CLI**
- 
            
                    **To describe launch templates**This example describes your launch templates. Command: `aws ec2 describe-launch-templates`Output: `{ "LaunchTemplates": [ { "LatestVersionNumber": 2, "LaunchTemplateId": "lt-0e06d290751193123", "LaunchTemplateName": "TemplateForWebServer", "DefaultVersionNumber": 2, "CreatedBy": "arn:aws:iam::123456789012:root", "CreateTime": "2017-11-27T09:30:23.000Z" }, { "LatestVersionNumber": 6, "LaunchTemplateId": "lt-0c45b5e061ec98456", "LaunchTemplateName": "DBServersTemplate", "DefaultVersionNumber": 1, "CreatedBy": "arn:aws:iam::123456789012:root", "CreateTime": "2017-11-20T09:25:22.000Z" }, { "LatestVersionNumber": 1, "LaunchTemplateId": "lt-0d47d774e8e52dabc", "LaunchTemplateName": "MyLaunchTemplate2", "DefaultVersionNumber": 1, "CreatedBy": "arn:aws:iam::123456789012:root", "CreateTime": "2017-11-02T12:06:21.000Z" }, { "LatestVersionNumber": 3, "LaunchTemplateId": "lt-01e5f948eb4f589d6", "LaunchTemplateName": "testingtemplate2", "DefaultVersionNumber": 1, "CreatedBy": "arn:aws:sts::123456789012:assumed-role/AdminRole/i-03ee35176e2e5aabc", "CreateTime": "2017-12-01T08:19:48.000Z" }, ] }`- 
                    For API details, see [DescribeLaunchTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-launch-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-local-gateway-route-table-virtual-interface-group-associations`.

- **AWS CLI**
- 
            
                    **To describe associations between virtual interface groups and local gateway route tables**The following `describe-local-gateway-route-table-virtual-interface-group-associations`example describes the associations between virtual interface groups and local gateway route tables in your AWS account.`aws ec2 describe-local-gateway-route-table-virtual-interface-group-associations`Output: `{ "LocalGatewayRouteTableVirtualInterfaceGroupAssociations": [ { "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": "lgw-vif-grp-assoc-07145b276bEXAMPLE", "LocalGatewayVirtualInterfaceGroupId": "lgw-vif-grp-07145b276bEXAMPLE", "LocalGatewayId": "lgw-0ab1c23d4eEXAMPLE", "LocalGatewayRouteTableId": "lgw-rtb-059615ef7dEXAMPLE", "LocalGatewayRouteTableArn": "arn:aws:ec2:us-west-2:123456789012:local-gateway-route-table/lgw-rtb-059615ef7dEXAMPLE", "OwnerId": "123456789012", "State": "associated", "Tags": [] } ] }`For more information, see [Working with local gateways](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-local-gateway-route-table-virtual-interface-group-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-local-gateway-route-table-vpc-associations`.

- **AWS CLI**
- 
            
                    **To describe the associations between VPCs and local gateway route tables**The following `describe-local-gateway-route-table-vpc-associations`example displays information about the specified association between VPCs and local gateway route tables.`aws ec2 describe-local-gateway-route-table-vpc-associations \ --local-gateway-route-table-vpc-association-ids``lgw-vpc-assoc-0e0f27af15EXAMPLE`Output: `{ "LocalGatewayRouteTableVpcAssociation": { "LocalGatewayRouteTableVpcAssociationId": "lgw-vpc-assoc-0e0f27af1EXAMPLE", "LocalGatewayRouteTableId": "lgw-rtb-059615ef7dEXAMPLE", "LocalGatewayId": "lgw-09b493aa7cEXAMPLE", "VpcId": "vpc-0efe9bde08EXAMPLE", "State": "associated" } }`For more information, see [Local gateway route tables](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html)in the*Outposts User Guide*.- 
                    For API details, see [DescribeLocalGatewayRouteTableVpcAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-local-gateway-route-table-vpc-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-local-gateway-route-tables`.

- **AWS CLI**
- 
            
                    **To describe your Local Gateway Route Tables**The following `describe-local-gateway-route-tables`example displays details about the local gateway route tables.`aws ec2 describe-local-gateway-route-tables`Output: `{ "LocalGatewayRouteTables": [ { "LocalGatewayRouteTableId": "lgw-rtb-059615ef7deEXAMPLE", "LocalGatewayId": "lgw-09b493aa7cEXAMPLE", "OutpostArn": "arn:aws:outposts:us-west-2:111122223333:outpost/op-0dc11b66edEXAMPLE", "State": "available" } ] }`- 
                    For API details, see [DescribeLocalGatewayRouteTables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-local-gateway-route-tables.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-local-gateway-virtual-interface-groups`.

- **AWS CLI**
- 
            
                    **To describe local gateway virtual interface groups**The following `describe-local-gateway-virtual-interface-groups`example describes the local gateway virtual interface groups in your AWS account.`aws ec2 describe-local-gateway-virtual-interface-groups`Output: `{ "LocalGatewayVirtualInterfaceGroups": [ { "LocalGatewayVirtualInterfaceGroupId": "lgw-vif-grp-07145b276bEXAMPLE", "LocalGatewayVirtualInterfaceIds": [ "lgw-vif-01a23bc4d5EXAMPLE", "lgw-vif-543ab21012EXAMPLE" ], "LocalGatewayId": "lgw-0ab1c23d4eEXAMPLE", "OwnerId": "123456789012", "Tags": [] } ] }`For more information, see [Working with local gateways](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [DescribeLocalGatewayVirtualInterfaceGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-local-gateway-virtual-interface-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-local-gateway-virtual-interfaces`.

- **AWS CLI**
- 
            
                    **To describe local gateway virtual interfaces**The following `describe-local-gateway-virtual-interfaces`example describes the local gateway virtual interfaces in your AWS account.`aws ec2 describe-local-gateway-virtual-interfaces`Output: `{ "LocalGatewayVirtualInterfaces": [ { "LocalGatewayVirtualInterfaceId": "lgw-vif-01a23bc4d5EXAMPLE", "LocalGatewayId": "lgw-0ab1c23d4eEXAMPLE", "Vlan": 2410, "LocalAddress": "0.0.0.0/0", "PeerAddress": "0.0.0.0/0", "LocalBgpAsn": 65010, "PeerBgpAsn": 65000, "OwnerId": "123456789012", "Tags": [] }, { "LocalGatewayVirtualInterfaceId": "lgw-vif-543ab21012EXAMPLE", "LocalGatewayId": "lgw-0ab1c23d4eEXAMPLE", "Vlan": 2410, "LocalAddress": "0.0.0.0/0", "PeerAddress": "0.0.0.0/0", "LocalBgpAsn": 65010, "PeerBgpAsn": 65000, "OwnerId": "123456789012", "Tags": [] } ] }`For more information, see [Working with local gateways](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-local-gateways.html)in the*AWS Outposts User Guide*.- 
                    For API details, see [DescribeLocalGatewayVirtualInterfaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-local-gateway-virtual-interfaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-local-gateways`.

- **AWS CLI**
- 
            
                    **To describe your Local Gateways**The following `describe-local-gateways`example displays details for the local gateways that are available to you.`aws ec2 describe-local-gateways`Output: `{ "LocalGateways": [ { "LocalGatewayId": "lgw-09b493aa7cEXAMPLE", "OutpostArn": "arn:aws:outposts:us-west-2:123456789012:outpost/op-0dc11b66ed59f995a", "OwnerId": "123456789012", "State": "available" } ] }`- 
                    For API details, see [DescribeLocalGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-local-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-locked-snapshots`.

- **AWS CLI**
- 
            
                    **To describe the lock status of a snapshot**The following `describe-locked-snapshots`example describes the lock status of the specified snapshot.`aws ec2 describe-locked-snapshots \ --snapshot-ids``snap-0b5e733b4a8df6e0d`Output: `{ "Snapshots": [ { "OwnerId": "123456789012", "SnapshotId": "snap-0b5e733b4a8df6e0d", "LockState": "governance", "LockDuration": 365, "LockCreatedOn": "2024-05-05T00:56:06.208000+00:00", "LockDurationStartTime": "2024-05-05T00:56:06.208000+00:00", "LockExpiresOn": "2025-05-05T00:56:06.208000+00:00" } ] }`For more information, see [Snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lock.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [DescribeLockedSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-locked-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-managed-prefix-lists`.

- **AWS CLI**
- 
            
                    **To describe managed prefix lists**The following `describe-managed-prefix-lists`example describes the prefix lists owned by AWS account`123456789012`.`aws ec2 describe-managed-prefix-lists \ --filters``Name=owner-id,Values=123456789012`Output: `{ "PrefixLists": [ { "PrefixListId": "pl-11223344556677aab", "AddressFamily": "IPv6", "State": "create-complete", "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-11223344556677aab", "PrefixListName": "vpc-ipv6-cidrs", "MaxEntries": 25, "Version": 1, "Tags": [], "OwnerId": "123456789012" }, { "PrefixListId": "pl-0123456abcabcabc1", "AddressFamily": "IPv4", "State": "active", "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456abcabcabc1", "PrefixListName": "vpc-cidrs", "MaxEntries": 10, "Version": 1, "Tags": [], "OwnerId": "123456789012" } ] }`For more information, see [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DescribeManagedPrefixLists](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-managed-prefix-lists.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-moving-addresses`.

- **AWS CLI**
- 
            
                    **To describe your moving addresses**This example describes all of your moving Elastic IP addresses. Command: `aws ec2 describe-moving-addresses`Output: `{ "MovingAddressStatuses": [ { "PublicIp": "198.51.100.0", "MoveStatus": "MovingToVpc" } ] }`This example describes all addresses that are moving to the EC2-VPC platform. Command: `aws ec2 describe-moving-addresses --filters``Name=moving-status,Values=MovingToVpc`- 
                    For API details, see [DescribeMovingAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-moving-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-nat-gateways`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a public NAT gateway**The following `describe-nat-gateways`example describes the specified public NAT gateway.`aws ec2 describe-nat-gateways \ --nat-gateway-id``nat-01234567890abcdef`Output: `{ "NatGateways": [ { "CreateTime": "2023-08-25T01:56:51.000Z", "NatGatewayAddresses": [ { "AllocationId": "eipalloc-0790180cd2EXAMPLE", "NetworkInterfaceId": "eni-09cc4b2558794f7f9", "PrivateIp": "10.0.0.211", "PublicIp": "54.85.121.213", "AssociationId": "eipassoc-04d295cc9b8815b24", "IsPrimary": true, "Status": "succeeded" }, { "AllocationId": "eipalloc-0be6ecac95EXAMPLE", "NetworkInterfaceId": "eni-09cc4b2558794f7f9", "PrivateIp": "10.0.0.74", "PublicIp": "3.211.231.218", "AssociationId": "eipassoc-0f96bdca17EXAMPLE", "IsPrimary": false, "Status": "succeeded" } ], "NatGatewayId": "nat-01234567890abcdef", "State": "available", "SubnetId": "subnet-655eab5f08EXAMPLE", "VpcId": "vpc-098eb5ef58EXAMPLE", "Tags": [ { "Key": "Name", "Value": "public-nat" } ], "ConnectivityType": "public" } ] }`**Example 2: To describe a private NAT gateway**The following `describe-nat-gateways`example describes the specified private NAT gateway.`aws ec2 describe-nat-gateways \ --nat-gateway-id``nat-1234567890abcdef0`Output: `{ "NatGateways": [ { "CreateTime": "2023-08-25T00:50:05.000Z", "NatGatewayAddresses": [ { "NetworkInterfaceId": "eni-0065a61b324d1897a", "PrivateIp": "10.0.20.240", "IsPrimary": true, "Status": "succeeded" }, { "NetworkInterfaceId": "eni-0065a61b324d1897a", "PrivateIp": "10.0.20.33", "IsPrimary": false, "Status": "succeeded" }, { "NetworkInterfaceId": "eni-0065a61b324d1897a", "PrivateIp": "10.0.20.197", "IsPrimary": false, "Status": "succeeded" } ], "NatGatewayId": "nat-1234567890abcdef0", "State": "available", "SubnetId": "subnet-08fc749671EXAMPLE", "VpcId": "vpc-098eb5ef58EXAMPLE", "Tags": [ { "Key": "Name", "Value": "private-nat" } ], "ConnectivityType": "private" } ] }`For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DescribeNatGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-nat-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-acls`.

- **AWS CLI**
- 
            
                    **To describe your network ACLs**The following `describe-network-acls`example retrieves details about your network ACLs.`aws ec2 describe-network-acls`Output: `{ "NetworkAcls": [ { "Associations": [ { "NetworkAclAssociationId": "aclassoc-0c1679dc41EXAMPLE", "NetworkAclId": "acl-0ea1f54ca7EXAMPLE", "SubnetId": "subnet-0931fc2fa5EXAMPLE" } ], "Entries": [ { "CidrBlock": "0.0.0.0/0", "Egress": true, "Protocol": "-1", "RuleAction": "allow", "RuleNumber": 100 }, { "CidrBlock": "0.0.0.0/0", "Egress": true, "Protocol": "-1", "RuleAction": "deny", "RuleNumber": 32767 }, { "CidrBlock": "0.0.0.0/0", "Egress": false, "Protocol": "-1", "RuleAction": "allow", "RuleNumber": 100 }, { "CidrBlock": "0.0.0.0/0", "Egress": false, "Protocol": "-1", "RuleAction": "deny", "RuleNumber": 32767 } ], "IsDefault": true, "NetworkAclId": "acl-0ea1f54ca7EXAMPLE", "Tags": [], "VpcId": "vpc-06e4ab6c6cEXAMPLE", "OwnerId": "111122223333" }, { "Associations": [], "Entries": [ { "CidrBlock": "0.0.0.0/0", "Egress": true, "Protocol": "-1", "RuleAction": "allow", "RuleNumber": 100 }, { "Egress": true, "Ipv6CidrBlock": "::/0", "Protocol": "-1", "RuleAction": "allow", "RuleNumber": 101 }, { "CidrBlock": "0.0.0.0/0", "Egress": true, "Protocol": "-1", "RuleAction": "deny", "RuleNumber": 32767 }, { "Egress": true, "Ipv6CidrBlock": "::/0", "Protocol": "-1", "RuleAction": "deny", "RuleNumber": 32768 }, { "CidrBlock": "0.0.0.0/0", "Egress": false, "Protocol": "-1", "RuleAction": "allow", "RuleNumber": 100 }, { "Egress": false, "Ipv6CidrBlock": "::/0", "Protocol": "-1", "RuleAction": "allow", "RuleNumber": 101 }, { "CidrBlock": "0.0.0.0/0", "Egress": false, "Protocol": "-1", "RuleAction": "deny", "RuleNumber": 32767 }, { "Egress": false, "Ipv6CidrBlock": "::/0", "Protocol": "-1", "RuleAction": "deny", "RuleNumber": 32768 } ], "IsDefault": true, "NetworkAclId": "acl-0e2a78e4e2EXAMPLE", "Tags": [], "VpcId": "vpc-03914afb3eEXAMPLE", "OwnerId": "111122223333" } ] }`For more information, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)in the*AWS VPC User Guide*.- 
                    For API details, see [DescribeNetworkAcls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-acls.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-insights-access-scope-analyses`.

- **AWS CLI**
- 
            
                    **To describe Network Insights access scope analyses**The following `describe-network-insights-access-scope-analyses`example describes the access scope analysis in your AWS account.`aws ec2 describe-network-insights-access-scope-analyses \ --region``us-east-1`Output: `{ "NetworkInsightsAccessScopeAnalyses": [ { "NetworkInsightsAccessScopeAnalysisId": "nisa-123456789111", "NetworkInsightsAccessScopeAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-access-scope-analysis/nisa-123456789111", "NetworkInsightsAccessScopeId": "nis-123456789222", "Status": "succeeded", "StartDate": "2022-01-25T19:45:36.842000+00:00", "FindingsFound": "true", "Tags": [] } ] }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli-naa.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [DescribeNetworkInsightsAccessScopeAnalyses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-insights-access-scope-analyses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-insights-access-scopes`.

- **AWS CLI**
- 
            
                    **To describe Network Insights access scopes**The following `describe-network-insights-access-scopes`example describes the access-scope analyses in your AWS account.`aws ec2 describe-network-insights-access-scopes \ --region``us-east-1`Output: `{ "NetworkInsightsAccessScopes": [ { "NetworkInsightsAccessScopeId": "nis-123456789111", "NetworkInsightsAccessScopeArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-access-scope/nis-123456789111", "CreatedDate": "2021-11-29T21:12:41.416000+00:00", "UpdatedDate": "2021-11-29T21:12:41.416000+00:00", "Tags": [] } ] }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli-naa.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [DescribeNetworkInsightsAccessScopes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-insights-access-scopes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-insights-analyses`.

- **AWS CLI**
- 
            
                    **To view the results of a path analysis**The following `describe-network-insights-analyses`example describes the specified analysis. In this example, the source is an internet gateway, the destination is an EC2 instance, and the protocol is TCP. The analysis succeeded (`Status`is`succeeded`) and the path is not reachable (`NetworkPathFound`is`false`). The explanation code`ENI_SG_RULES_MISMATCH`indicates that the security group for the instance does not contain a rule that allows traffic on the destination port.`aws ec2 describe-network-insights-analyses \ --network-insights-analysis-ids``nia-02207aa13eb480c7a`Output: `{ "NetworkInsightsAnalyses": [ { "NetworkInsightsAnalysisId": "nia-02207aa13eb480c7a", "NetworkInsightsAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-analysis/nia-02207aa13eb480c7a", "NetworkInsightsPathId": "nip-0b26f224f1d131fa8", "StartDate": "2021-01-20T22:58:37.495Z", "Status": "succeeded", "NetworkPathFound": false, "Explanations": [ { "Direction": "ingress", "ExplanationCode": "ENI_SG_RULES_MISMATCH", "NetworkInterface": { "Id": "eni-0a25edef15a6cc08c", "Arn": "arn:aws:ec2:us-east-1:123456789012:network-interface/eni-0a25edef15a6cc08c" }, "SecurityGroups": [ { "Id": "sg-02f0d35a850ba727f", "Arn": "arn:aws:ec2:us-east-1:123456789012:security-group/sg-02f0d35a850ba727f" } ], "Subnet": { "Id": "subnet-004ff41eccb4d1194", "Arn": "arn:aws:ec2:us-east-1:123456789012:subnet/subnet-004ff41eccb4d1194" }, "Vpc": { "Id": "vpc-f1663d98ad28331c7", "Arn": "arn:aws:ec2:us-east-1:123456789012:vpc/vpc-f1663d98ad28331c7" } } ], "Tags": [] } ] }`For more information, see [Getting started using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/reachability/getting-started-cli.html)in the*Reachability Analyzer Guide*.- 
                    For API details, see [DescribeNetworkInsightsAnalyses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-insights-analyses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-insights-paths`.

- **AWS CLI**
- 
            
                    **To describe a path**The following `describe-network-insights-paths`example describes the specified path.`aws ec2 describe-network-insights-paths \ --network-insights-path-ids``nip-0b26f224f1d131fa8`Output: `{ "NetworkInsightsPaths": [ { "NetworkInsightsPathId": "nip-0b26f224f1d131fa8", "NetworkInsightsPathArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-path/nip-0b26f224f1d131fa8", "CreatedDate": "2021-01-20T22:43:46.933Z", "Source": "igw-0797cccdc9d73b0e5", "Destination": "i-0495d385ad28331c7", "Protocol": "tcp" } ] }`For more information, see [Getting started using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/reachability/getting-started-cli.html)in the*Reachability Analyzer Guide*.- 
                    For API details, see [DescribeNetworkInsightsPaths](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-insights-paths.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-interface-attribute`.

- **AWS CLI**
- 
            
                    **To describe the attachment attribute of a network interface**This example command describes the `attachment`attribute of the specified network interface.Command: `aws ec2 describe-network-interface-attribute --network-interface-id``eni-686ea200`--attribute`attachment`Output: `{ "NetworkInterfaceId": "eni-686ea200", "Attachment": { "Status": "attached", "DeviceIndex": 0, "AttachTime": "2015-05-21T20:02:20.000Z", "InstanceId": "i-1234567890abcdef0", "DeleteOnTermination": true, "AttachmentId": "eni-attach-43348162", "InstanceOwnerId": "123456789012" } }`**To describe the description attribute of a network interface**This example command describes the `description`attribute of the specified network interface.Command: `aws ec2 describe-network-interface-attribute --network-interface-id``eni-686ea200`--attribute`description`Output: `{ "NetworkInterfaceId": "eni-686ea200", "Description": { "Value": "My description" } }`**To describe the groupSet attribute of a network interface**This example command describes the `groupSet`attribute of the specified network interface.Command: `aws ec2 describe-network-interface-attribute --network-interface-id``eni-686ea200`--attribute`groupSet`Output: `{ "NetworkInterfaceId": "eni-686ea200", "Groups": [ { "GroupName": "my-security-group", "GroupId": "sg-903004f8" } ] }`**To describe the sourceDestCheck attribute of a network interface**This example command describes the `sourceDestCheck`attribute of the specified network interface.Command: `aws ec2 describe-network-interface-attribute --network-interface-id``eni-686ea200`--attribute`sourceDestCheck`Output: `{ "NetworkInterfaceId": "eni-686ea200", "SourceDestCheck": { "Value": true } }`- 
                    For API details, see [DescribeNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interface-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-interface-permissions`.

- **AWS CLI**
- 
            
                    **To describe your network interface permissions**This example describes all of your network interface permissions. Command: `aws ec2 describe-network-interface-permissions`Output: `{ "NetworkInterfacePermissions": [ { "PermissionState": { "State": "GRANTED" }, "NetworkInterfacePermissionId": "eni-perm-06fd19020ede149ea", "NetworkInterfaceId": "eni-b909511a", "Permission": "INSTANCE-ATTACH", "AwsAccountId": "123456789012" } ] }`- 
                    For API details, see [DescribeNetworkInterfacePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interface-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-network-interfaces`.

- **AWS CLI**
- 
            
                    **To describe your network interfaces**This example describes all your network interfaces. Command: `aws ec2 describe-network-interfaces`Output: `{ "NetworkInterfaces": [ { "Status": "in-use", "MacAddress": "02:2f:8f:b0:cf:75", "SourceDestCheck": true, "VpcId": "vpc-a01106c2", "Description": "my network interface", "Association": { "PublicIp": "203.0.113.12", "AssociationId": "eipassoc-0fbb766a", "PublicDnsName": "ec2-203-0-113-12.compute-1.amazonaws.com", "IpOwnerId": "123456789012" }, "NetworkInterfaceId": "eni-e5aa89a3", "PrivateIpAddresses": [ { "PrivateDnsName": "ip-10-0-1-17.ec2.internal", "Association": { "PublicIp": "203.0.113.12", "AssociationId": "eipassoc-0fbb766a", "PublicDnsName": "ec2-203-0-113-12.compute-1.amazonaws.com", "IpOwnerId": "123456789012" }, "Primary": true, "PrivateIpAddress": "10.0.1.17" } ], "RequesterManaged": false, "Ipv6Addresses": [], "PrivateDnsName": "ip-10-0-1-17.ec2.internal", "AvailabilityZone": "us-east-1d", "Attachment": { "Status": "attached", "DeviceIndex": 1, "AttachTime": "2013-11-30T23:36:42.000Z", "InstanceId": "i-1234567890abcdef0", "DeleteOnTermination": false, "AttachmentId": "eni-attach-66c4350a", "InstanceOwnerId": "123456789012" }, "Groups": [ { "GroupName": "default", "GroupId": "sg-8637d3e3" } ], "SubnetId": "subnet-b61f49f0", "OwnerId": "123456789012", "TagSet": [], "PrivateIpAddress": "10.0.1.17" }, { "Status": "in-use", "MacAddress": "02:58:f5:ef:4b:06", "SourceDestCheck": true, "VpcId": "vpc-a01106c2", "Description": "Primary network interface", "Association": { "PublicIp": "198.51.100.0", "IpOwnerId": "amazon" }, "NetworkInterfaceId": "eni-f9ba99bf", "PrivateIpAddresses": [ { "Association": { "PublicIp": "198.51.100.0", "IpOwnerId": "amazon" }, "Primary": true, "PrivateIpAddress": "10.0.1.149" } ], "RequesterManaged": false, "Ipv6Addresses": [], "AvailabilityZone": "us-east-1d", "Attachment": { "Status": "attached", "DeviceIndex": 0, "AttachTime": "2013-11-30T23:35:33.000Z", "InstanceId": "i-0598c7d356eba48d7", "DeleteOnTermination": true, "AttachmentId": "eni-attach-1b9db777", "InstanceOwnerId": "123456789012" }, "Groups": [ { "GroupName": "default", "GroupId": "sg-8637d3e3" } ], "SubnetId": "subnet-b61f49f0", "OwnerId": "123456789012", "TagSet": [], "PrivateIpAddress": "10.0.1.149" } ] }`This example describes network interfaces that have a tag with the key `Purpose`and the value`Prod`.Command: `aws ec2 describe-network-interfaces --filters``Name=tag:Purpose,Values=Prod`Output: `{ "NetworkInterfaces": [ { "Status": "available", "MacAddress": "12:2c:bd:f9:bf:17", "SourceDestCheck": true, "VpcId": "vpc-8941ebec", "Description": "ProdENI", "NetworkInterfaceId": "eni-b9a5ac93", "PrivateIpAddresses": [ { "PrivateDnsName": "ip-10-0-1-55.ec2.internal", "Primary": true, "PrivateIpAddress": "10.0.1.55" }, { "PrivateDnsName": "ip-10-0-1-117.ec2.internal", "Primary": false, "PrivateIpAddress": "10.0.1.117" } ], "RequesterManaged": false, "PrivateDnsName": "ip-10-0-1-55.ec2.internal", "AvailabilityZone": "us-east-1d", "Ipv6Addresses": [], "Groups": [ { "GroupName": "MySG", "GroupId": "sg-905002f5" } ], "SubnetId": "subnet-31d6c219", "OwnerId": "123456789012", "TagSet": [ { "Value": "Prod", "Key": "Purpose" } ], "PrivateIpAddress": "10.0.1.55" } ] }`- 
                    For API details, see [DescribeNetworkInterfaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-network-interfaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-placement-groups`.

- **AWS CLI**
- 
            
                    **To describe your placement groups**This example command describes all of your placement groups. Command: `aws ec2 describe-placement-groups`Output: `{ "PlacementGroups": [ { "GroupName": "my-cluster", "State": "available", "Strategy": "cluster" }, ... ] }`- 
                    For API details, see [DescribePlacementGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-placement-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-prefix-lists`.

- **AWS CLI**
- 
            
                    **To describe prefix lists**This example lists all available prefix lists for the region. Command: `aws ec2 describe-prefix-lists`Output: `{ "PrefixLists": [ { "PrefixListName": "com.amazonaws.us-east-1.s3", "Cidrs": [ "54.231.0.0/17" ], "PrefixListId": "pl-63a5400a" } ] }`- 
                    For API details, see [DescribePrefixLists](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-prefix-lists.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-principal-id-format`.

- **AWS CLI**
- 
            
                    **To describe the ID format for IAM users and roles with long ID format enabled**The following `describe-principal-id-format`example describes the ID format for the root user, all IAM roles, and all IAM users with long ID format enabled.`aws ec2 describe-principal-id-format \ --resource``instance`Output: `{ "Principals": [ { "Arn": "arn:aws:iam::123456789012:root", "Statuses": [ { "Deadline": "2016-12-15T00:00:00.000Z", "Resource": "reservation", "UseLongIds": true }, { "Deadline": "2016-12-15T00:00:00.000Z", "Resource": "instance", "UseLongIds": true }, { "Deadline": "2016-12-15T00:00:00.000Z", "Resource": "volume", "UseLongIds": true }, ] }, ... ] }`- 
                    For API details, see [DescribePrincipalIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-principal-id-format.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-public-ipv4-pools`.

- **AWS CLI**
- 
            
                    **To describe your public IPv4 address pools**The following `describe-public-ipv4-pools`example displays details about the address pools that were created when you provisioned public IPv4 address ranges using Bring Your Own IP Addresses (BYOIP).`aws ec2 describe-public-ipv4-pools`Output: `{ "PublicIpv4Pools": [ { "PoolId": "ipv4pool-ec2-1234567890abcdef0", "PoolAddressRanges": [ { "FirstAddress": "203.0.113.0", "LastAddress": "203.0.113.255", "AddressCount": 256, "AvailableAddressCount": 256 } ], "TotalAddressCount": 256, "TotalAvailableAddressCount": 256 } ] }`- 
                    For API details, see [DescribePublicIpv4Pools](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-public-ipv4-pools.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-regions`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all of your enabled Regions**The following `describe-regions`example describes all of the Regions that are enabled for your account.`aws ec2 describe-regions`Output: `{ "Regions": [ { "Endpoint": "ec2.eu-north-1.amazonaws.com", "RegionName": "eu-north-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-south-1.amazonaws.com", "RegionName": "ap-south-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-west-3.amazonaws.com", "RegionName": "eu-west-3", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-west-2.amazonaws.com", "RegionName": "eu-west-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-west-1.amazonaws.com", "RegionName": "eu-west-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-northeast-3.amazonaws.com", "RegionName": "ap-northeast-3", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-northeast-2.amazonaws.com", "RegionName": "ap-northeast-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-northeast-1.amazonaws.com", "RegionName": "ap-northeast-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.sa-east-1.amazonaws.com", "RegionName": "sa-east-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ca-central-1.amazonaws.com", "RegionName": "ca-central-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-southeast-1.amazonaws.com", "RegionName": "ap-southeast-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-southeast-2.amazonaws.com", "RegionName": "ap-southeast-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-central-1.amazonaws.com", "RegionName": "eu-central-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-east-1.amazonaws.com", "RegionName": "us-east-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-east-2.amazonaws.com", "RegionName": "us-east-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-west-1.amazonaws.com", "RegionName": "us-west-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-west-2.amazonaws.com", "RegionName": "us-west-2", "OptInStatus": "opt-in-not-required" } ] }`For more information, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)in the*Amazon EC2 User Guide*.**Example 2: To describe enabled Regions with an endpoint whose name contains a specific string**The following `describe-regions`example describes all Regions that you have enabled that have the string "us" in the endpoint.`aws ec2 describe-regions \ --filters``"Name=endpoint,Values=*us*"`Output: `{ "Regions": [ { "Endpoint": "ec2.us-east-1.amazonaws.com", "RegionName": "us-east-1" }, { "Endpoint": "ec2.us-east-2.amazonaws.com", "RegionName": "us-east-2" }, { "Endpoint": "ec2.us-west-1.amazonaws.com", "RegionName": "us-west-1" }, { "Endpoint": "ec2.us-west-2.amazonaws.com", "RegionName": "us-west-2" } ] }`For more information, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)in the*Amazon EC2 User Guide*.**Example 3: To describe all Regions**The following `describe-regions`example describes all available Regions, including Regions that are disabled.`aws ec2 describe-regions \ --all-regions`Output: `{ "Regions": [ { "Endpoint": "ec2.eu-north-1.amazonaws.com", "RegionName": "eu-north-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-south-1.amazonaws.com", "RegionName": "ap-south-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-west-3.amazonaws.com", "RegionName": "eu-west-3", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-west-2.amazonaws.com", "RegionName": "eu-west-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-west-1.amazonaws.com", "RegionName": "eu-west-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-northeast-3.amazonaws.com", "RegionName": "ap-northeast-3", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.me-south-1.amazonaws.com", "RegionName": "me-south-1", "OptInStatus": "not-opted-in" }, { "Endpoint": "ec2.ap-northeast-2.amazonaws.com", "RegionName": "ap-northeast-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-northeast-1.amazonaws.com", "RegionName": "ap-northeast-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.sa-east-1.amazonaws.com", "RegionName": "sa-east-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ca-central-1.amazonaws.com", "RegionName": "ca-central-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-east-1.amazonaws.com", "RegionName": "ap-east-1", "OptInStatus": "not-opted-in" }, { "Endpoint": "ec2.ap-southeast-1.amazonaws.com", "RegionName": "ap-southeast-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.ap-southeast-2.amazonaws.com", "RegionName": "ap-southeast-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.eu-central-1.amazonaws.com", "RegionName": "eu-central-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-east-1.amazonaws.com", "RegionName": "us-east-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-east-2.amazonaws.com", "RegionName": "us-east-2", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-west-1.amazonaws.com", "RegionName": "us-west-1", "OptInStatus": "opt-in-not-required" }, { "Endpoint": "ec2.us-west-2.amazonaws.com", "RegionName": "us-west-2", "OptInStatus": "opt-in-not-required" } ] }`For more information, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)in the*Amazon EC2 User Guide*.**Example 4: To list the Region names only**The following `describe-regions`example uses the`--query`parameter to filter the output and return only the names of the Regions as text.`aws ec2 describe-regions \ --all-regions \ --query``"Regions[].{Name:RegionName}"`\ --output`text`Output: `eu-north-1 ap-south-1 eu-west-3 eu-west-2 eu-west-1 ap-northeast-3 ap-northeast-2 me-south-1 ap-northeast-1 sa-east-1 ca-central-1 ap-east-1 ap-southeast-1 ap-southeast-2 eu-central-1 us-east-1 us-east-2 us-west-1 us-west-2`For more information, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeRegions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-regions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-replace-root-volume-tasks`.

- **AWS CLI**
- 
            
                    **Example 1: To view information about a specific root volume replacement task**The following `describe-replace-root-volume-tasks`example describes root volume replacement task replacevol-0111122223333abcd.`aws ec2 describe-replace-root-volume-tasks \ --replace-root-volume-task-ids``replacevol-0111122223333abcd`Output: `{ "ReplaceRootVolumeTasks": [ { "ReplaceRootVolumeTaskId": "replacevol-0111122223333abcd", "Tags": [], "InstanceId": "i-0123456789abcdefa", "TaskState": "succeeded", "StartTime": "2022-03-14T15:16:28Z", "CompleteTime": "2022-03-14T15:16:52Z" } ] }`For more information, see [Replace a root volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-restoring-volume.html#replace-root)in the*Amazon Elastic Compute Cloud User Guide*.**Example 2: To view information about all root volume replacement tasks for a specific instance**The following `describe-replace-root-volume-tasks`example describes all of the root volume replacement tasks for instance i-0123456789abcdefa.`aws ec2 describe-replace-root-volume-tasks \ --filters``Name=instance-id,Values=i-0123456789abcdefa`Output: `{ "ReplaceRootVolumeTasks": [ { "ReplaceRootVolumeTaskId": "replacevol-0111122223333abcd", "Tags": [], "InstanceId": "i-0123456789abcdefa", "TaskState": "succeeded", "StartTime": "2022-03-14T15:06:38Z", "CompleteTime": "2022-03-14T15:07:03Z" }, { "ReplaceRootVolumeTaskId": "replacevol-0444455555555abcd", "Tags": [], "InstanceId": "i-0123456789abcdefa", "TaskState": "succeeded", "StartTime": "2022-03-14T15:16:28Z", "CompleteTime": "2022-03-14T15:16:52Z" } ] }`For more information, see [Replace a root volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-restoring-volume.html#replace-root)in the*Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [DescribeReplaceRootVolumeTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-replace-root-volume-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-instances-listings`.

- **AWS CLI**
- 
            
                    **To describe a Reserved Instance listing**The following `describe-reserved-instances-listings`example retrieves information about the specified Reserved Instance listing.`aws ec2 describe-reserved-instances-listings \ --reserved-instances-listing-id``5ec28771-05ff-4b9b-aa31-9e57dexample`This command produces no output. - 
                    For API details, see [DescribeReservedInstancesListings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances-listings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-instances-modifications`.

- **AWS CLI**
- 
            
                    **To describe Reserved Instances modifications**This example command describes all the Reserved Instances modification requests that have been submitted for your account. Command: `aws ec2 describe-reserved-instances-modifications`Output: `{ "ReservedInstancesModifications": [ { "Status": "fulfilled", "ModificationResults": [ { "ReservedInstancesId": "93bbbca2-62f1-4d9d-b225-16bada29e6c7", "TargetConfiguration": { "AvailabilityZone": "us-east-1b", "InstanceType": "m1.large", "InstanceCount": 3 } }, { "ReservedInstancesId": "1ba8e2e3-aabb-46c3-bcf5-3fe2fda922e6", "TargetConfiguration": { "AvailabilityZone": "us-east-1d", "InstanceType": "m1.xlarge", "InstanceCount": 1 } } ], "EffectiveDate": "2015-08-12T17:00:00.000Z", "CreateDate": "2015-08-12T17:52:52.630Z", "UpdateDate": "2015-08-12T18:08:06.698Z", "ClientToken": "c9adb218-3222-4889-8216-0cf0e52dc37e: "ReservedInstancesModificationId": "rimod-d3ed4335-b1d3-4de6-ab31-0f13aaf46687", "ReservedInstancesIds": [ { "ReservedInstancesId": "b847fa93-e282-4f55-b59a-1342f5bd7c02" } ] } ] }`- 
                    For API details, see [DescribeReservedInstancesModifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances-modifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-instances-offerings`.

- **AWS CLI**
- 
            
                    **To describe Reserved Instances offerings**This example command describes all Reserved Instances available for purchase in the region. Command: `aws ec2 describe-reserved-instances-offerings`Output: `{ "ReservedInstancesOfferings": [ { "OfferingType": "Partial Upfront", "AvailabilityZone": "us-east-1b", "InstanceTenancy": "default", "PricingDetails": [], "ProductDescription": "Red Hat Enterprise Linux", "UsagePrice": 0.0, "RecurringCharges": [ { "Amount": 0.088, "Frequency": "Hourly" } ], "Marketplace": false, "CurrencyCode": "USD", "FixedPrice": 631.0, "Duration": 94608000, "ReservedInstancesOfferingId": "9a06095a-bdc6-47fe-a94a-2a382f016040", "InstanceType": "c1.medium" }, { "OfferingType": "PartialUpfront", "AvailabilityZone": "us-east-1b", "InstanceTenancy": "default", "PricingDetails": [], "ProductDescription": "Linux/UNIX", "UsagePrice": 0.0, "RecurringCharges": [ { "Amount": 0.028, "Frequency": "Hourly" } ], "Marketplace": false, "CurrencyCode": "USD", "FixedPrice": 631.0, "Duration": 94608000, "ReservedInstancesOfferingId": "bfbefc6c-0d10-418d-b144-7258578d329d", "InstanceType": "c1.medium" }, ... }`**To describe your Reserved Instances offerings using options**This example lists Reserved Instances offered by AWS with the following specifications: t1.micro instance types, Windows (Amazon VPC) product, and Heavy Utilization offerings. Command: `aws ec2 describe-reserved-instances-offerings --no-include-marketplace --instance-type``"t1.micro"`--product-description`"Windows (Amazon VPC)"`--offering-type`"no upfront"`Output: `{ "ReservedInstancesOfferings": [ { "OfferingType": "No Upfront", "AvailabilityZone": "us-east-1b", "InstanceTenancy": "default", "PricingDetails": [], "ProductDescription": "Windows", "UsagePrice": 0.0, "RecurringCharges": [ { "Amount": 0.015, "Frequency": "Hourly" } ], "Marketplace": false, "CurrencyCode": "USD", "FixedPrice": 0.0, "Duration": 31536000, "ReservedInstancesOfferingId": "c48ab04c-fe69-4f94-8e39-a23842292823", "InstanceType": "t1.micro" }, ... { "OfferingType": "No Upfront", "AvailabilityZone": "us-east-1d", "InstanceTenancy": "default", "PricingDetails": [], "ProductDescription": "Windows (Amazon VPC)", "UsagePrice": 0.0, "RecurringCharges": [ { "Amount": 0.015, "Frequency": "Hourly" } ], "Marketplace": false, "CurrencyCode": "USD", "FixedPrice": 0.0, "Duration": 31536000, "ReservedInstancesOfferingId": "3a98bf7d-2123-42d4-b4f5-8dbec4b06dc6", "InstanceType": "t1.micro" } ] }`- 
                    For API details, see [DescribeReservedInstancesOfferings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances-offerings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-reserved-instances`.

- **AWS CLI**
- 
            
                    **To describe your Reserved Instances**This example command describes the Reserved Instances that you own. Command: `aws ec2 describe-reserved-instances`Output: `{ "ReservedInstances": [ { "ReservedInstancesId": "b847fa93-e282-4f55-b59a-1342fexample", "OfferingType": "No Upfront", "AvailabilityZone": "us-west-1c", "End": "2016-08-14T21:34:34.000Z", "ProductDescription": "Linux/UNIX", "UsagePrice": 0.00, "RecurringCharges": [ { "Amount": 0.104, "Frequency": "Hourly" } ], "Start": "2015-08-15T21:34:35.086Z", "State": "active", "FixedPrice": 0.0, "CurrencyCode": "USD", "Duration": 31536000, "InstanceTenancy": "default", "InstanceType": "m3.medium", "InstanceCount": 2 }, ... ] }`**To describe your Reserved Instances using filters**This example filters the response to include only three-year, t2.micro Linux/UNIX Reserved Instances in us-west-1c. Command: `aws ec2 describe-reserved-instances --filters``Name=duration,Values=94608000``Name=instance-type,Values=t2.micro``Name=product-description,Values=Linux/UNIX``Name=availability-zone,Values=us-east-1e`Output: `{ "ReservedInstances": [ { "ReservedInstancesId": "f127bd27-edb7-44c9-a0eb-0d7e09259af0", "OfferingType": "All Upfront", "AvailabilityZone": "us-east-1e", "End": "2018-03-26T21:34:34.000Z", "ProductDescription": "Linux/UNIX", "UsagePrice": 0.00, "RecurringCharges": [], "Start": "2015-03-27T21:34:35.848Z", "State": "active", "FixedPrice": 151.0, "CurrencyCode": "USD", "Duration": 94608000, "InstanceTenancy": "default", "InstanceType": "t2.micro", "InstanceCount": 1 } ] }`For more information, see Using Amazon EC2 Instances in the *AWS Command Line Interface User Guide*.- 
                    For API details, see [DescribeReservedInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-route-tables`.

- **AWS CLI**
- 
            
                    **To describe your route tables**The following `describe-route-tables`example retrieves the details about your route tables`aws ec2 describe-route-tables`Output: `{ "RouteTables": [ { "Associations": [ { "Main": true, "RouteTableAssociationId": "rtbassoc-0df3f54e06EXAMPLE", "RouteTableId": "rtb-09ba434c1bEXAMPLE" } ], "PropagatingVgws": [], "RouteTableId": "rtb-09ba434c1bEXAMPLE", "Routes": [ { "DestinationCidrBlock": "10.0.0.0/16", "GatewayId": "local", "Origin": "CreateRouteTable", "State": "active" }, { "DestinationCidrBlock": "0.0.0.0/0", "NatGatewayId": "nat-06c018cbd8EXAMPLE", "Origin": "CreateRoute", "State": "blackhole" } ], "Tags": [], "VpcId": "vpc-0065acced4EXAMPLE", "OwnerId": "111122223333" }, { "Associations": [ { "Main": true, "RouteTableAssociationId": "rtbassoc-9EXAMPLE", "RouteTableId": "rtb-a1eec7de" } ], "PropagatingVgws": [], "RouteTableId": "rtb-a1eec7de", "Routes": [ { "DestinationCidrBlock": "172.31.0.0/16", "GatewayId": "local", "Origin": "CreateRouteTable", "State": "active" }, { "DestinationCidrBlock": "0.0.0.0/0", "GatewayId": "igw-fEXAMPLE", "Origin": "CreateRoute", "State": "active" } ], "Tags": [], "VpcId": "vpc-3EXAMPLE", "OwnerId": "111122223333" }, { "Associations": [ { "Main": false, "RouteTableAssociationId": "rtbassoc-0b100c28b2EXAMPLE", "RouteTableId": "rtb-07a98f76e5EXAMPLE", "SubnetId": "subnet-0d3d002af8EXAMPLE" } ], "PropagatingVgws": [], "RouteTableId": "rtb-07a98f76e5EXAMPLE", "Routes": [ { "DestinationCidrBlock": "10.0.0.0/16", "GatewayId": "local", "Origin": "CreateRouteTable", "State": "active" }, { "DestinationCidrBlock": "0.0.0.0/0", "GatewayId": "igw-06cf664d80EXAMPLE", "Origin": "CreateRoute", "State": "active" } ], "Tags": [], "VpcId": "vpc-0065acced4EXAMPLE", "OwnerId": "111122223333" } ] }`For more information, see [Working with Route Tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#WorkWithRouteTables)in the*AWS VPC User Guide*.- 
                    For API details, see [DescribeRouteTables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-route-tables.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scheduled-instance-availability`.

- **AWS CLI**
- 
            
                    **To describe an available schedule**This example describes a schedule that occurs every week on Sunday, starting on the specified date. Command: `aws ec2 describe-scheduled-instance-availability --recurrence``Frequency=Weekly,Interval=1,OccurrenceDays=[1]`--first-slot-start-time-range`EarliestTime=2016-01-31T00:00:00Z,LatestTime=2016-01-31T04:00:00Z`Output: `{ "ScheduledInstanceAvailabilitySet": [ { "AvailabilityZone": "us-west-2b", "TotalScheduledInstanceHours": 1219, "PurchaseToken": "eyJ2IjoiMSIsInMiOjEsImMiOi...", "MinTermDurationInDays": 366, "AvailableInstanceCount": 20, "Recurrence": { "OccurrenceDaySet": [ 1 ], "Interval": 1, "Frequency": "Weekly", "OccurrenceRelativeToEnd": false }, "Platform": "Linux/UNIX", "FirstSlotStartTime": "2016-01-31T00:00:00Z", "MaxTermDurationInDays": 366, "SlotDurationInHours": 23, "NetworkPlatform": "EC2-VPC", "InstanceType": "c4.large", "HourlyPrice": "0.095" }, ... ] }`To narrow the results, you can add filters that specify the operating system, network, and instance type. Command: --filters Name=platform,Values=Linux/UNIX Name=network-platform,Values=EC2-VPC Name=instance-type,Values=c4.large - 
                    For API details, see [DescribeScheduledInstanceAvailability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instance-availability.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-scheduled-instances`.

- **AWS CLI**
- 
            
                    **To describe your Scheduled Instances**This example describes the specified Scheduled Instance. Command: `aws ec2 describe-scheduled-instances --scheduled-instance-ids``sci-1234-1234-1234-1234-123456789012`Output: `{ "ScheduledInstanceSet": [ { "AvailabilityZone": "us-west-2b", "ScheduledInstanceId": "sci-1234-1234-1234-1234-123456789012", "HourlyPrice": "0.095", "CreateDate": "2016-01-25T21:43:38.612Z", "Recurrence": { "OccurrenceDaySet": [ 1 ], "Interval": 1, "Frequency": "Weekly", "OccurrenceRelativeToEnd": false, "OccurrenceUnit": "" }, "Platform": "Linux/UNIX", "TermEndDate": "2017-01-31T09:00:00Z", "InstanceCount": 1, "SlotDurationInHours": 32, "TermStartDate": "2016-01-31T09:00:00Z", "NetworkPlatform": "EC2-VPC", "TotalScheduledInstanceHours": 1696, "NextSlotStartTime": "2016-01-31T09:00:00Z", "InstanceType": "c4.large" } ] }`This example describes all your Scheduled Instances. Command: `aws ec2 describe-scheduled-instances`- 
                    For API details, see [DescribeScheduledInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-scheduled-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-security-group-references`.

- **AWS CLI**
- 
            
                    **To describe security group references**This example describes the security group references for `sg-bbbb2222`. The response indicates that security group`sg-bbbb2222`is being referenced by a security group in VPC`vpc-aaaaaaaa`.Command: `aws ec2 describe-security-group-references --group-id``sg-bbbbb22222`Output: `{ "SecurityGroupsReferenceSet": [ { "ReferencingVpcId": "vpc-aaaaaaaa ", "GroupId": "sg-bbbbb22222", "VpcPeeringConnectionId": "pcx-b04deed9" } ] }`- 
                    For API details, see [DescribeSecurityGroupReferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-group-references.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-security-group-rules`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the security group rules for a security group**The following `describe-security-group-rules`example describes the security group rules of a specified security group. Use the`filters`option to scope the results to a specific security group.`aws ec2 describe-security-group-rules \ --filters Name="group-id",Values="sg-1234567890abcdef0"`Output: `{ "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-abcdef01234567890", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "111122223333", "IsEgress": false, "IpProtocol": "-1", "FromPort": -1, "ToPort": -1, "ReferencedGroupInfo": { "GroupId": "sg-1234567890abcdef0", "UserId": "111122223333" }, "Tags": [] }, { "SecurityGroupRuleId": "sgr-bcdef01234567890a", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "111122223333", "IsEgress": true, "IpProtocol": "-1", "FromPort": -1, "ToPort": -1, "CidrIpv6": "::/0", "Tags": [] }, { "SecurityGroupRuleId": "sgr-cdef01234567890ab", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "111122223333", "IsEgress": true, "IpProtocol": "-1", "FromPort": -1, "ToPort": -1, "CidrIpv4": "0.0.0.0/0", "Tags": [] } ] }`**Example 2: To describe a security group rule**The following `describe-security-group-rules`example describes the specified security group rule.`aws ec2 describe-security-group-rules \ --security-group-rule-ids``sgr-cdef01234567890ab`Output: `{ "SecurityGroupRules": [ { "SecurityGroupRuleId": "sgr-cdef01234567890ab", "GroupId": "sg-1234567890abcdef0", "GroupOwnerId": "111122223333", "IsEgress": true, "IpProtocol": "-1", "FromPort": -1, "ToPort": -1, "CidrIpv4": "0.0.0.0/0", "Tags": [] } ] }`For more information, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DescribeSecurityGroupRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-group-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-security-group-vpc-associations`.

- **AWS CLI**
- 
            
                    **To describe VPC associations**The following `describe-security-group-vpc-associations`example describes the VPC associations for the specified security group.`aws ec2 describe-security-group-vpc-associations \ --filters``Name=group-id,Values=sg-04dbb43907d3f8a78`Output: `{ "SecurityGroupVpcAssociations": [ { "GroupId": "sg-04dbb43907d3f8a78", "VpcId": "vpc-0bf4c2739bc05a694", "VpcOwnerId": "123456789012", "State": "associated" } ] }`For more information, see [Associate security groups with multiple VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-assoc.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DescribeSecurityGroupVpcAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-group-vpc-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-security-groups`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a security group**The following `describe-security-groups`example describes the specified security group.`aws ec2 describe-security-groups \ --group-ids``sg-903004f8`Output: `{ "SecurityGroups": [ { "IpPermissionsEgress": [ { "IpProtocol": "-1", "IpRanges": [ { "CidrIp": "0.0.0.0/0" } ], "UserIdGroupPairs": [], "PrefixListIds": [] } ], "Description": "My security group", "Tags": [ { "Value": "SG1", "Key": "Name" } ], "IpPermissions": [ { "IpProtocol": "-1", "IpRanges": [], "UserIdGroupPairs": [ { "UserId": "123456789012", "GroupId": "sg-903004f8" } ], "PrefixListIds": [] }, { "PrefixListIds": [], "FromPort": 22, "IpRanges": [ { "Description": "Access from NY office", "CidrIp": "203.0.113.0/24" } ], "ToPort": 22, "IpProtocol": "tcp", "UserIdGroupPairs": [] } ], "GroupName": "MySecurityGroup", "VpcId": "vpc-1a2b3c4d", "OwnerId": "123456789012", "GroupId": "sg-903004f8", } ] }`**Example 2: To describe security groups that have specific rules**The following `describe-security-groups`example uses filters to scope the results to security groups that have a rule that allows SSH traffic (port 22) and a rule that allows traffic from all addresses (`0.0.0.0/0`). The example uses the`--query`parameter to display only the names of the security groups. Security groups must match all filters to be returned in the results; however, a single rule does not have to match all filters. For example, the output returns a security group with a rule that allows SSH traffic from a specific IP address and another rule that allows HTTP traffic from all addresses.`aws ec2 describe-security-groups \ --filters``Name=ip-permission.from-port,Values=22``Name=ip-permission.to-port,Values=22`Name=ip-permission.cidr,Values='0.0.0.0/0' \ --query`"SecurityGroups[*].[GroupName]"`\ --output`text`Output: `default my-security-group web-servers launch-wizard-1`**Example 3: To describe security groups based on tags**The following `describe-security-groups`example uses filters to scope the results to security groups that include`test`in the security group name, and that have the tag`Test=To-delete`. The example uses the`--query`parameter to display only the names and IDs of the security groups.`aws ec2 describe-security-groups \ --filters``Name=group-name,Values=*test*``Name=tag:Test,Values=To-delete`\ --query`"SecurityGroups[*].{Name:GroupName,ID:GroupId}"`Output: `[ { "Name": "testfornewinstance", "ID": "sg-33bb22aa" }, { "Name": "newgrouptest", "ID": "sg-1a2b3c4d" } ]`For additional examples using tag filters, see [Working with tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeSecurityGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-security-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-snapshot-attribute`.

- **AWS CLI**
- 
            
                    **To describe the snapshot attributes for a snapshot**The following `describe-snapshot-attribute`example lists the accounts with which a snapshot is shared.`aws ec2 describe-snapshot-attribute \ --snapshot-id``snap-01234567890abcedf`\ --attribute`createVolumePermission`Output: `{ "SnapshotId": "snap-01234567890abcedf", "CreateVolumePermissions": [ { "UserId": "123456789012" } ] }`For more information, see [Share an Amazon EBS snapshot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modifying-snapshot-permissions.html#share-unencrypted-snapshot)in the*Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [DescribeSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshot-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-snapshot-tier-status`.

- **AWS CLI**
- 
            
                    **To view archival information about an archived snapshot**The following `describe-snapshot-tier-status`example provides archival information about an archived snapshot.`aws ec2 describe-snapshot-tier-status \ --filters``"Name=snapshot-id, Values=snap-01234567890abcedf"`Output: `{ "SnapshotTierStatuses": [ { "Status": "completed", "ArchivalCompleteTime": "2021-09-15T17:33:16.147Z", "LastTieringProgress": 100, "Tags": [], "VolumeId": "vol-01234567890abcedf", "LastTieringOperationState": "archival-completed", "StorageTier": "archive", "OwnerId": "123456789012", "SnapshotId": "snap-01234567890abcedf", "LastTieringStartTime": "2021-09-15T16:44:37.574Z" } ] }`For more information, see [View archived snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-snapshot-archiving.html#view-archived-snapshot)in the*Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [DescribeSnapshotTierStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshot-tier-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-snapshots`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a snapshot**The following `describe-snapshots`example describes the specified snapshot.`aws ec2 describe-snapshots \ --snapshot-ids``snap-1234567890abcdef0`Output: `{ "Snapshots": [ { "Description": "This is my snapshot", "Encrypted": false, "VolumeId": "vol-049df61146c4d7901", "State": "completed", "VolumeSize": 8, "StartTime": "2019-02-28T21:28:32.000Z", "Progress": "100%", "OwnerId": "012345678910", "SnapshotId": "snap-01234567890abcdef", "Tags": [ { "Key": "Stack", "Value": "test" } ] } ] }`For more information, see [Amazon EBS snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)in the*Amazon EC2 User Guide*.**Example 2: To describe snapshots based on filters**The following `describe-snapshots`example uses filters to scope the results to snapshots owned by your AWS account that are in the`pending`state. The example uses the`--query`parameter to display only the snapshot IDs and the time the snapshot was started.`aws ec2 describe-snapshots \ --owner-ids``self`\ --filters`Name=status,Values=pending`\ --query`"Snapshots[*].{ID:SnapshotId,Time:StartTime}"`Output: `[ { "ID": "snap-1234567890abcdef0", "Time": "2019-08-04T12:48:18.000Z" }, { "ID": "snap-066877671789bd71b", "Time": "2019-08-04T02:45:16.000Z }, ... ]`The following `describe-snapshots`example uses filters to scope the results to snapshots created from the specified volume. The example uses the`--query`parameter to display only the snapshot IDs.`aws ec2 describe-snapshots \ --filters``Name=volume-id,Values=049df61146c4d7901`\ --query`"Snapshots[*].[SnapshotId]"`\ --output`text`Output: `snap-1234567890abcdef0 snap-08637175a712c3fb9 ...`For additional examples using filters, see [Listing and filtering your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI)in the*Amazon EC2 User Guide*.**Example 3: To describe snapshots based on tags**The following `describe-snapshots`example uses tag filters to scope the results to snapshots that have the tag`Stack=Prod`.`aws ec2 describe-snapshots \ --filters``Name=tag:Stack,Values=prod`For an example of the output for `describe-snapshots`, see Example 1.For additional examples using tag filters, see [Working with tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI)in the*Amazon EC2 User Guide*.**Example 4: To describe snapshots based on age**The following `describe-snapshots`example uses JMESPath expressions to describe all snapshots created by your AWS account before the specified date. It displays only the snapshot IDs.`aws ec2 describe-snapshots \ --owner-ids``012345678910`\ --query`"Snapshots[?(StartTime<='2020-03-31')].[SnapshotId]"`For additional examples using filters, see [Listing and filtering your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI)in the*Amazon EC2 User Guide*.**Example 5: To view only archived snapshots**The following `describe-snapshots`example lists only snapshots that are stored in the archive tier.`aws ec2 describe-snapshots \ --filters``"Name=storage-tier,Values=archive"`Output: `{ "Snapshots": [ { "Description": "Snap A", "Encrypted": false, "VolumeId": "vol-01234567890aaaaaa", "State": "completed", "VolumeSize": 8, "StartTime": "2021-09-07T21:00:00.000Z", "Progress": "100%", "OwnerId": "123456789012", "SnapshotId": "snap-01234567890aaaaaa", "StorageTier": "archive", "Tags": [] }, ] }`For more information, see [View archived snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-snapshot-archiving.html#view-archived-snapshot)in the*Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [DescribeSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-spot-datafeed-subscription`.

- **AWS CLI**
- 
            
                    **To describe Spot Instance datafeed subscription for an account**This example command describes the data feed for the account. Command: `aws ec2 describe-spot-datafeed-subscription`Output: `{ "SpotDatafeedSubscription": { "OwnerId": "123456789012", "Prefix": "spotdata", "Bucket": "amzn-s3-demo-bucket", "State": "Active" } }`- 
                    For API details, see [DescribeSpotDatafeedSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-datafeed-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-spot-fleet-instances`.

- **AWS CLI**
- 
            
                    **To describe the Spot Instances associated with a Spot fleet**This example command lists the Spot instances associated with the specified Spot fleet. Command: `aws ec2 describe-spot-fleet-instances --spot-fleet-request-id``sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`Output: `{ "ActiveInstances": [ { "InstanceId": "i-1234567890abcdef0", "InstanceType": "m3.medium", "SpotInstanceRequestId": "sir-08b93456" }, ... ], "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" }`- 
                    For API details, see [DescribeSpotFleetInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-spot-fleet-request-history`.

- **AWS CLI**
- 
            
                    **To describe Spot fleet history**This example command returns the history for the specified Spot fleet starting at the specified time. Command: `aws ec2 describe-spot-fleet-request-history --spot-fleet-request-id``sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`--start-time`2015-05-26T00:00:00Z`The following example output shows the successful launches of two Spot Instances for the Spot fleet. Output: `{ "HistoryRecords": [ { "Timestamp": "2015-05-26T23:17:20.697Z", "EventInformation": { "EventSubType": "submitted" }, "EventType": "fleetRequestChange" }, { "Timestamp": "2015-05-26T23:17:20.873Z", "EventInformation": { "EventSubType": "active" }, "EventType": "fleetRequestChange" }, { "Timestamp": "2015-05-26T23:21:21.712Z", "EventInformation": { "InstanceId": "i-1234567890abcdef0", "EventSubType": "launched" }, "EventType": "instanceChange" }, { "Timestamp": "2015-05-26T23:21:21.816Z", "EventInformation": { "InstanceId": "i-1234567890abcdef1", "EventSubType": "launched" }, "EventType": "instanceChange" } ], "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "NextToken": "CpHNsscimcV5oH7bSbub03CI2Qms5+ypNpNm+53MNlR0YcXAkp0xFlfKf91yVxSExmbtma3awYxMFzNA663ZskT0AHtJ6TCb2Z8bQC2EnZgyELbymtWPfpZ1ZbauVg+P+TfGlWxWWB/Vr5dk5d4LfdgA/DRAHUrYgxzrEXAMPLE=", "StartTime": "2015-05-26T00:00:00Z" }`- 
                    For API details, see [DescribeSpotFleetRequestHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-request-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-spot-fleet-requests`.

- **AWS CLI**
- 
            
                    **To describe your Spot fleet requests**This example describes all of your Spot fleet requests. Command: `aws ec2 describe-spot-fleet-requests`Output: `{ "SpotFleetRequestConfigs": [ { "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "SpotFleetRequestConfig": { "TargetCapacity": 20, "LaunchSpecifications": [ { "EbsOptimized": false, "NetworkInterfaces": [ { "SubnetId": "subnet-a61dafcf", "DeviceIndex": 0, "DeleteOnTermination": false, "AssociatePublicIpAddress": true, "SecondaryPrivateIpAddressCount": 0 } ], "InstanceType": "cc2.8xlarge", "ImageId": "ami-1a2b3c4d" }, { "EbsOptimized": false, "NetworkInterfaces": [ { "SubnetId": "subnet-a61dafcf", "DeviceIndex": 0, "DeleteOnTermination": false, "AssociatePublicIpAddress": true, "SecondaryPrivateIpAddressCount": 0 } ], "InstanceType": "r3.8xlarge", "ImageId": "ami-1a2b3c4d" } ], "SpotPrice": "0.05", "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role" }, "SpotFleetRequestState": "active" }, { "SpotFleetRequestId": "sfr-306341ed-9739-402e-881b-ce47bEXAMPLE", "SpotFleetRequestConfig": { "TargetCapacity": 20, "LaunchSpecifications": [ { "EbsOptimized": false, "NetworkInterfaces": [ { "SubnetId": "subnet-6e7f829e", "DeviceIndex": 0, "DeleteOnTermination": false, "AssociatePublicIpAddress": true, "SecondaryPrivateIpAddressCount": 0 } ], "InstanceType": "m3.medium", "ImageId": "ami-1a2b3c4d" } ], "SpotPrice": "0.05", "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role" }, "SpotFleetRequestState": "active" } ] }`**To describe a Spot fleet request**This example describes the specified Spot fleet request. Command: `aws ec2 describe-spot-fleet-requests --spot-fleet-request-ids``sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`Output: `{ "SpotFleetRequestConfigs": [ { "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE", "SpotFleetRequestConfig": { "TargetCapacity": 20, "LaunchSpecifications": [ { "EbsOptimized": false, "NetworkInterfaces": [ { "SubnetId": "subnet-a61dafcf", "DeviceIndex": 0, "DeleteOnTermination": false, "AssociatePublicIpAddress": true, "SecondaryPrivateIpAddressCount": 0 } ], "InstanceType": "cc2.8xlarge", "ImageId": "ami-1a2b3c4d" }, { "EbsOptimized": false, "NetworkInterfaces": [ { "SubnetId": "subnet-a61dafcf", "DeviceIndex": 0, "DeleteOnTermination": false, "AssociatePublicIpAddress": true, "SecondaryPrivateIpAddressCount": 0 } ], "InstanceType": "r3.8xlarge", "ImageId": "ami-1a2b3c4d" } ], "SpotPrice": "0.05", "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role" }, "SpotFleetRequestState": "active" } ] }`- 
                    For API details, see [DescribeSpotFleetRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-fleet-requests.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-spot-instance-requests`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a Spot Instance request**The following `describe-spot-instance-requests`example describes the specified Spot Instance request.`aws ec2 describe-spot-instance-requests \ --spot-instance-request-ids``sir-08b93456`Output: `{ "SpotInstanceRequests": [ { "CreateTime": "2018-04-30T18:14:55.000Z", "InstanceId": "i-1234567890abcdef1", "LaunchSpecification": { "InstanceType": "t2.micro", "ImageId": "ami-003634241a8fcdec0", "KeyName": "my-key-pair", "SecurityGroups": [ { "GroupName": "default", "GroupId": "sg-e38f24a7" } ], "BlockDeviceMappings": [ { "DeviceName": "/dev/sda1", "Ebs": { "DeleteOnTermination": true, "SnapshotId": "snap-0e54a519c999adbbd", "VolumeSize": 8, "VolumeType": "standard", "Encrypted": false } } ], "NetworkInterfaces": [ { "DeleteOnTermination": true, "DeviceIndex": 0, "SubnetId": "subnet-049df61146c4d7901" } ], "Placement": { "AvailabilityZone": "us-east-2b", "Tenancy": "default" }, "Monitoring": { "Enabled": false } }, "LaunchedAvailabilityZone": "us-east-2b", "ProductDescription": "Linux/UNIX", "SpotInstanceRequestId": "sir-08b93456", "SpotPrice": "0.010000" "State": "active", "Status": { "Code": "fulfilled", "Message": "Your Spot request is fulfilled.", "UpdateTime": "2018-04-30T18:16:21.000Z" }, "Tags": [], "Type": "one-time", "InstanceInterruptionBehavior": "terminate" } ] }`**Example 2: To describe Spot Instance requests based on filters**The following `describe-spot-instance-requests`example uses filters to scope the results to Spot Instance requests with the specified instance type in the specified Availability Zone. The example uses the`--query`parameter to display only the instance IDs.`aws ec2 describe-spot-instance-requests \ --filters``Name=launch.instance-type,Values=m3.medium``Name=launched-availability-zone,Values=us-east-2a`\ --query`"SpotInstanceRequests[*].[InstanceId]"`\ --output`text`Output: `i-057750d42936e468a i-001efd250faaa6ffa i-027552a73f021f3bd ...`For additional examples using filters, see [Listing and filtering your resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI)in the*Amazon Elastic Compute Cloud User Guide*.**Example 3: To describe Spot Instance requests based on tags**The following `describe-spot-instance-requests`example uses tag filters to scope the results to Spot Instance requests that have the tag`cost-center=cc123`.`aws ec2 describe-spot-instance-requests \ --filters``Name=tag:cost-center,Values=cc123`For an example of the output for `describe-spot-instance-requests`, see Example 1.For additional examples using tag filters, see [Working with tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeSpotInstanceRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-instance-requests.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-spot-price-history`.

- **AWS CLI**
- 
            
                    **To describe Spot price history**This example command returns the Spot Price history for m1.xlarge instances for a particular day in January. Command: `aws ec2 describe-spot-price-history --instance-types``m1.xlarge`--start-time`2014-01-06T07:08:09`--end-time`2014-01-06T08:09:10`Output: `{ "SpotPriceHistory": [ { "Timestamp": "2014-01-06T07:10:55.000Z", "ProductDescription": "SUSE Linux", "InstanceType": "m1.xlarge", "SpotPrice": "0.087000", "AvailabilityZone": "us-west-1b" }, { "Timestamp": "2014-01-06T07:10:55.000Z", "ProductDescription": "SUSE Linux", "InstanceType": "m1.xlarge", "SpotPrice": "0.087000", "AvailabilityZone": "us-west-1c" }, { "Timestamp": "2014-01-06T05:42:36.000Z", "ProductDescription": "SUSE Linux (Amazon VPC)", "InstanceType": "m1.xlarge", "SpotPrice": "0.087000", "AvailabilityZone": "us-west-1a" }, ... }`**To describe Spot price history for Linux/UNIX Amazon VPC**This example command returns the Spot Price history for m1.xlarge, Linux/UNIX Amazon VPC instances for a particular day in January. Command: `aws ec2 describe-spot-price-history --instance-types``m1.xlarge`--product-description`"Linux/UNIX (Amazon VPC)"`--start-time`2014-01-06T07:08:09`--end-time`2014-01-06T08:09:10`Output: `{ "SpotPriceHistory": [ { "Timestamp": "2014-01-06T04:32:53.000Z", "ProductDescription": "Linux/UNIX (Amazon VPC)", "InstanceType": "m1.xlarge", "SpotPrice": "0.080000", "AvailabilityZone": "us-west-1a" }, { "Timestamp": "2014-01-05T11:28:26.000Z", "ProductDescription": "Linux/UNIX (Amazon VPC)", "InstanceType": "m1.xlarge", "SpotPrice": "0.080000", "AvailabilityZone": "us-west-1c" } ] }`- 
                    For API details, see [DescribeSpotPriceHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-spot-price-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-stale-security-groups`.

- **AWS CLI**
- 
            
                    **To describe stale security groups**This example describes stale security group rules for `vpc-11223344`. The response shows that sg-5fa68d3a in your account has a stale ingress SSH rule that references`sg-279ab042`in the peer VPC, and that`sg-fe6fba9a`in your account has a stale egress SSH rule that references`sg-ef6fba8b`in the peer VPC.Command: `aws ec2 describe-stale-security-groups --vpc-id``vpc-11223344`Output: `{ "StaleSecurityGroupSet": [ { "VpcId": "vpc-11223344", "StaleIpPermissionsEgress": [ { "ToPort": 22, "FromPort": 22, "UserIdGroupPairs": [ { "VpcId": "vpc-7a20e51f", "GroupId": "sg-ef6fba8b", "VpcPeeringConnectionId": "pcx-b04deed9", "PeeringStatus": "active" } ], "IpProtocol": "tcp" } ], "GroupName": "MySG1", "StaleIpPermissions": [], "GroupId": "sg-fe6fba9a", "Description": MySG1" }, { "VpcId": "vpc-11223344", "StaleIpPermissionsEgress": [], "GroupName": "MySG2", "StaleIpPermissions": [ { "ToPort": 22, "FromPort": 22, "UserIdGroupPairs": [ { "VpcId": "vpc-7a20e51f", "GroupId": "sg-279ab042", "Description": "Access from pcx-b04deed9", "VpcPeeringConnectionId": "pcx-b04deed9", "PeeringStatus": "active" } ], "IpProtocol": "tcp" } ], "GroupId": "sg-5fa68d3a", "Description": "MySG2" } ] }`- 
                    For API details, see [DescribeStaleSecurityGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-stale-security-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-store-image-tasks`.

- **AWS CLI**
- 
            
                    **To describe the progress of an AMI store task**The following `describe-store-image-tasks`example describes the progress of an AMI store task.`aws ec2 describe-store-image-tasks`Output: `{ "StoreImageTaskResults": [ { "AmiId": "ami-1234567890abcdef0", "Bucket": "my-ami-bucket", "ProgressPercentage": 17, "S3objectKey": "ami-1234567890abcdef0.bin", "StoreTaskState": "InProgress", "StoreTaskFailureReason": null, "TaskStartTime": "2022-01-01T01:01:01.001Z" } ] }`For more information about storing and restoring an AMI using S3, see Store and restore an AMI using S3 <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-store-restore.html> in the *Amazon EC2 User Guide*.- 
                    For API details, see [DescribeStoreImageTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-store-image-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-subnets`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all your subnets**The following `describe-subnets`example displays the details of your subnets.`aws ec2 describe-subnets`Output: `{ "Subnets": [ { "AvailabilityZone": "us-east-1d", "AvailabilityZoneId": "use1-az2", "AvailableIpAddressCount": 4089, "CidrBlock": "172.31.80.0/20", "DefaultForAz": true, "MapPublicIpOnLaunch": false, "MapCustomerOwnedIpOnLaunch": true, "State": "available", "SubnetId": "subnet-0bb1c79de3EXAMPLE", "VpcId": "vpc-0ee975135dEXAMPLE", "OwnerId": "111122223333", "AssignIpv6AddressOnCreation": false, "Ipv6CidrBlockAssociationSet": [], "CustomerOwnedIpv4Pool:": 'pool-2EXAMPLE', "SubnetArn": "arn:aws:ec2:us-east-2:111122223333:subnet/subnet-0bb1c79de3EXAMPLE", "EnableDns64": false, "Ipv6Native": false, "PrivateDnsNameOptionsOnLaunch": { "HostnameType": "ip-name", "EnableResourceNameDnsARecord": false, "EnableResourceNameDnsAAAARecord": false } }, { "AvailabilityZone": "us-east-1d", "AvailabilityZoneId": "use1-az2", "AvailableIpAddressCount": 4089, "CidrBlock": "172.31.80.0/20", "DefaultForAz": true, "MapPublicIpOnLaunch": true, "MapCustomerOwnedIpOnLaunch": false, "State": "available", "SubnetId": "subnet-8EXAMPLE", "VpcId": "vpc-3EXAMPLE", "OwnerId": "1111222233333", "AssignIpv6AddressOnCreation": false, "Ipv6CidrBlockAssociationSet": [], "Tags": [ { "Key": "Name", "Value": "MySubnet" } ], "SubnetArn": "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-8EXAMPLE", "EnableDns64": false, "Ipv6Native": false, "PrivateDnsNameOptionsOnLaunch": { "HostnameType": "ip-name", "EnableResourceNameDnsARecord": false, "EnableResourceNameDnsAAAARecord": false } } ] }`For more information, see [Working with VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html)in the*AWS VPC User Guide*.**Example 2: To describe the subnets of a specific VPC**The following `describe-subnets`example uses a filter to retrieve details for the subnets of the specified VPC.`aws ec2 describe-subnets \ --filters``"Name=vpc-id,Values=vpc-3EXAMPLE"`Output: `{ "Subnets": [ { "AvailabilityZone": "us-east-1d", "AvailabilityZoneId": "use1-az2", "AvailableIpAddressCount": 4089, "CidrBlock": "172.31.80.0/20", "DefaultForAz": true, "MapPublicIpOnLaunch": true, "MapCustomerOwnedIpOnLaunch": false, "State": "available", "SubnetId": "subnet-8EXAMPLE", "VpcId": "vpc-3EXAMPLE", "OwnerId": "1111222233333", "AssignIpv6AddressOnCreation": false, "Ipv6CidrBlockAssociationSet": [], "Tags": [ { "Key": "Name", "Value": "MySubnet" } ], "SubnetArn": "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-8EXAMPLE", "EnableDns64": false, "Ipv6Native": false, "PrivateDnsNameOptionsOnLaunch": { "HostnameType": "ip-name", "EnableResourceNameDnsARecord": false, "EnableResourceNameDnsAAAARecord": false } } ] }`For more information, see [Working with VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html)in the*AWS VPC User Guide*.**Example 3: To describe the subnets with a specific tag**The following `describe-subnets`example uses a filter to retrieve the details of those subnets with the tag`CostCenter=123`and the`--query`parameter to display the subnet IDs of the subnets with this tag.`aws ec2 describe-subnets \ --filters``"Name=tag:CostCenter,Values=123"`\ --query`"Subnets[*].SubnetId"`\ --output`text`Output: `subnet-0987a87c8b37348ef subnet-02a95061c45f372ee subnet-03f720e7de2788d73`For more information, see [Working with VPCs and Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-vpcs.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DescribeSubnets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-subnets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all tags for a single resource**The following `describe-tags`example describes the tags for the specified instance.`aws ec2 describe-tags \ --filters``"Name=resource-id,Values=i-1234567890abcdef8"`Output: `{ "Tags": [ { "ResourceType": "instance", "ResourceId": "i-1234567890abcdef8", "Value": "Test", "Key": "Stack" }, { "ResourceType": "instance", "ResourceId": "i-1234567890abcdef8", "Value": "Beta Server", "Key": "Name" } ] }`**Example 2: To describe all tags for a resource type**The following `describe-tags`example describes the tags for your volumes.`aws ec2 describe-tags \ --filters``"Name=resource-type,Values=volume"`Output: `{ "Tags": [ { "ResourceType": "volume", "ResourceId": "vol-1234567890abcdef0", "Value": "Project1", "Key": "Purpose" }, { "ResourceType": "volume", "ResourceId": "vol-049df61146c4d7901", "Value": "Logs", "Key": "Purpose" } ] }`**Example 3: To describe all your tags**The following `describe-tags`example describes the tags for all your resources.`aws ec2 describe-tags`**Example 4: To describe the tags for your resources based on a tag key**The following `describe-tags`example describes the tags for your resources that have a tag with the key`Stack`.`aws ec2 describe-tags \ --filters``Name=key,Values=Stack`Output: `{ "Tags": [ { "ResourceType": "volume", "ResourceId": "vol-027552a73f021f3b", "Value": "Production", "Key": "Stack" }, { "ResourceType": "instance", "ResourceId": "i-1234567890abcdef8", "Value": "Test", "Key": "Stack" } ] }`**Example 5: To describe the tags for your resources based on a tag key and tag value**The following `describe-tags`example describes the tags for your resources that have the tag`Stack=Test`.`aws ec2 describe-tags \ --filters``Name=key,Values=Stack``Name=value,Values=Test`Output: `{ "Tags": [ { "ResourceType": "image", "ResourceId": "ami-3ac336533f021f3bd", "Value": "Test", "Key": "Stack" }, { "ResourceType": "instance", "ResourceId": "i-1234567890abcdef8", "Value": "Test", "Key": "Stack" } ] }`The following `describe-tags`example uses alternate syntax to describe resources with the tag`Stack=Test`.`aws ec2 describe-tags \ --filters``"Name=tag:Stack,Values=Test"`The following `describe-tags`example describes the tags for all your instances that have a tag with the key`Purpose`and no value.`aws ec2 describe-tags \ --filters``"Name=resource-type,Values=instance"``"Name=key,Values=Purpose"``"Name=value,Values="`Output: `{ "Tags": [ { "ResourceType": "instance", "ResourceId": "i-1234567890abcdef5", "Value": null, "Key": "Purpose" } ] }`- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-traffic-mirror-filters`.

- **AWS CLI**
- 
            
                    **To view your traffic mirror filters**The following `describe-traffic-mirror-filters`example displays details for all of your traffic mirror filters.`aws ec2 describe-traffic-mirror-filters`Output: `{ "TrafficMirrorFilters": [ { "TrafficMirrorFilterId": "tmf-0293f26e86EXAMPLE", "IngressFilterRules": [ { "TrafficMirrorFilterRuleId": "tmfr-0ca76e0e08EXAMPLE", "TrafficMirrorFilterId": "tmf-0293f26e86EXAMPLE", "TrafficDirection": "ingress", "RuleNumber": 100, "RuleAction": "accept", "Protocol": 6, "DestinationCidrBlock": "10.0.0.0/24", "SourceCidrBlock": "10.0.0.0/24", "Description": "TCP Rule" } ], "EgressFilterRules": [], "NetworkServices": [], "Description": "Example filter", "Tags": [] } ] }`For more information, see [View your traffic mirror filters](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html#view-traffic-mirroring-filter)in the*Traffic Mirroring Guide*.- 
                    For API details, see [DescribeTrafficMirrorFilters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-traffic-mirror-filters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-traffic-mirror-sessions`.

- **AWS CLI**
- 
            
                    **To describe a Traffic Mirror Session**The following `describe-traffic-mirror-sessions`example displays details of the your Traffic Mirror sessions.`aws ec2 describe-traffic-mirror-sessions`Output: `{ "TrafficMirrorSessions": [ { "Tags": [], "VirtualNetworkId": 42, "OwnerId": "111122223333", "Description": "TCP Session", "NetworkInterfaceId": "eni-0a471a5cf3EXAMPLE", "TrafficMirrorTargetId": "tmt-0dabe9b0a6EXAMPLE", "TrafficMirrorFilterId": "tmf-083e18f985EXAMPLE", "PacketLength": 20, "SessionNumber": 1, "TrafficMirrorSessionId": "tms-0567a4c684EXAMPLE" }, { "Tags": [ { "Key": "Name", "Value": "tag test" } ], "VirtualNetworkId": 13314501, "OwnerId": "111122223333", "Description": "TCP Session", "NetworkInterfaceId": "eni-0a471a5cf3EXAMPLE", "TrafficMirrorTargetId": "tmt-03665551cbEXAMPLE", "TrafficMirrorFilterId": "tmf-06c787846cEXAMPLE", "SessionNumber": 2, "TrafficMirrorSessionId": "tms-0060101cf8EXAMPLE" } ] }`For more information, see [View Traffic Mirror Session Details](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html#view-traffic-mirroring-session)in the*AWS Traffic Mirroring Guide*.- 
                    For API details, see [DescribeTrafficMirrorSessions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-traffic-mirror-sessions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-traffic-mirror-targets`.

- **AWS CLI**
- 
            
                    **To describe a traffic mirror target**The following `describe-traffic-mirror-targets`example displays information about the specified traffic mirror target.`aws ec2 describe-traffic-mirror-targets \ --traffic-mirror-target-ids``tmt-0dabe9b0a6EXAMPLE`Output: `{ "TrafficMirrorTargets": [ { "TrafficMirrorTargetId": "tmt-0dabe9b0a6EXAMPLE", "NetworkLoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:111122223333:loadbalancer/net/NLB/7cdec873fEXAMPLE", "Type": "network-load-balancer", "Description": "Example Network Load Balancer target", "OwnerId": "111122223333", "Tags": [] } ] }`For more information, see [Traffic mirror targets](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-target.html)in the*Amazon VPC Traffic Mirroring Guide*.- 
                    For API details, see [DescribeTrafficMirrorTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-traffic-mirror-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-attachments`.

- **AWS CLI**
- 
            
                    **To view your transit gateway attachments**The following `describe-transit-gateway-attachments`example displays details for your transit gateway attachments.`aws ec2 describe-transit-gateway-attachments`Output: `{ "TransitGatewayAttachments": [ { "TransitGatewayAttachmentId": "tgw-attach-01f8100bc7EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "TransitGatewayOwnerId": "123456789012", "ResourceOwnerId": "123456789012", "ResourceType": "vpc", "ResourceId": "vpc-3EXAMPLE", "State": "available", "Association": { "TransitGatewayRouteTableId": "tgw-rtb-002573ed1eEXAMPLE", "State": "associated" }, "CreationTime": "2019-08-26T14:59:25.000Z", "Tags": [ { "Key": "Name", "Value": "Example" } ] }, { "TransitGatewayAttachmentId": "tgw-attach-0b5968d3b6EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "TransitGatewayOwnerId": "123456789012", "ResourceOwnerId": "123456789012", "ResourceType": "vpc", "ResourceId": "vpc-0065acced4EXAMPLE", "State": "available", "Association": { "TransitGatewayRouteTableId": "tgw-rtb-002573ed1eEXAMPLE", "State": "associated" }, "CreationTime": "2019-08-07T17:03:07.000Z", "Tags": [] }, { "TransitGatewayAttachmentId": "tgw-attach-08e0bc912cEXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "TransitGatewayOwnerId": "123456789012", "ResourceOwnerId": "123456789012", "ResourceType": "direct-connect-gateway", "ResourceId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE", "State": "available", "Association": { "TransitGatewayRouteTableId": "tgw-rtb-002573ed1eEXAMPLE", "State": "associated" }, "CreationTime": "2019-08-14T20:27:44.000Z", "Tags": [] }, { "TransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "TransitGatewayOwnerId": "123456789012", "ResourceOwnerId": "123456789012", "ResourceType": "direct-connect-gateway", "ResourceId": "8384da05-13ce-4a91-aada-5a1baEXAMPLE", "State": "available", "Association": { "TransitGatewayRouteTableId": "tgw-rtb-002573ed1eEXAMPLE", "State": "associated" }, "CreationTime": "2019-08-14T20:33:02.000Z", "Tags": [] } ] }`For more information, see [Work with transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-transit-gateways.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DescribeTransitGatewayAttachments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-attachments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-connect-peers`.

- **AWS CLI**
- 
            
                    **To describe a Transit Gateway Connect peer**The following `describe-transit-gateway-connect-peers`example describes the specified Connect peer.`aws ec2 describe-transit-gateway-connect-peers \ --transit-gateway-connect-peer-ids``tgw-connect-peer-0666adbac4EXAMPLE`Output: `{ "TransitGatewayConnectPeers": [ { "TransitGatewayAttachmentId": "tgw-attach-0f0927767cEXAMPLE", "TransitGatewayConnectPeerId": "tgw-connect-peer-0666adbac4EXAMPLE", "State": "available", "CreationTime": "2021-10-13T03:35:17.000Z", "ConnectPeerConfiguration": { "TransitGatewayAddress": "10.0.0.234", "PeerAddress": "172.31.1.11", "InsideCidrBlocks": [ "169.254.6.0/29" ], "Protocol": "gre", "BgpConfigurations": [ { "TransitGatewayAsn": 64512, "PeerAsn": 64512, "TransitGatewayAddress": "169.254.6.2", "PeerAddress": "169.254.6.1", "BgpStatus": "down" }, { "TransitGatewayAsn": 64512, "PeerAsn": 64512, "TransitGatewayAddress": "169.254.6.3", "PeerAddress": "169.254.6.1", "BgpStatus": "down" } ] }, "Tags": [] } ] }`For more information, see [Transit gateway Connect attachments and Transit Gateway Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DescribeTransitGatewayConnectPeers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-connect-peers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-connects`.

- **AWS CLI**
- 
            
                    **To describe a transit gateway Connect attachment**The following `describe-transit-gateway-connects`example describes the specified Connect attachment.`aws ec2 describe-transit-gateway-connects \ --transit-gateway-attachment-ids``tgw-attach-037012e5dcEXAMPLE`Output: `{ "TransitGatewayConnects": [ { "TransitGatewayAttachmentId": "tgw-attach-037012e5dcEXAMPLE", "TransportTransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE", "TransitGatewayId": "tgw-02f776b1a7EXAMPLE", "State": "available", "CreationTime": "2021-03-09T19:59:17+00:00", "Options": { "Protocol": "gre" }, "Tags": [] } ] }`For more information, see [Transit gateway Connect attachments and Transit Gateway Connect peers](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-connect.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DescribeTransitGatewayConnects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-connects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-multicast-domains`.

- **AWS CLI**
- 
            
                    **To describe your transit gateway multicast domains**The following `describe-transit-gateway-multicast-domains`example displays details for all of your transit gateway multicast domains.`aws ec2 describe-transit-gateway-multicast-domains`Output: `{ "TransitGatewayMulticastDomains": [ { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-000fb24d04EXAMPLE", "TransitGatewayId": "tgw-0bf0bffefaEXAMPLE", "TransitGatewayMulticastDomainArn": "arn:aws:ec2:us-east-1:123456789012:transit-gateway-multicast-domain/tgw-mcast-domain-000fb24d04EXAMPLE", "OwnerId": "123456789012", "Options": { "Igmpv2Support": "disable", "StaticSourcesSupport": "enable", "AutoAcceptSharedAssociations": "disable" }, "State": "available", "CreationTime": "2019-12-10T18:32:50+00:00", "Tags": [ { "Key": "Name", "Value": "mc1" } ] } ] }`For more information, see [Managing multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/manage-domain.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DescribeTransitGatewayMulticastDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-multicast-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-peering-attachments`.

- **AWS CLI**
- 
            
                    **To describe your transit gateway peering attachments**The following `describe-transit-gateway-peering-attachments`example displays details for all of your transit gateway peering attachments.`aws ec2 describe-transit-gateway-peering-attachments`Output: `{ "TransitGatewayPeeringAttachments": [ { "TransitGatewayAttachmentId": "tgw-attach-4455667788aabbccd", "RequesterTgwInfo": { "TransitGatewayId": "tgw-123abc05e04123abc", "OwnerId": "123456789012", "Region": "us-west-2" }, "AccepterTgwInfo": { "TransitGatewayId": "tgw-11223344aabbcc112", "OwnerId": "123456789012", "Region": "us-east-2" }, "State": "pendingAcceptance", "CreationTime": "2019-12-09T11:38:05.000Z", "Tags": [] } ] }`For more information, see [Transit Gateway Peering Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DescribeTransitGatewayPeeringAttachments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-peering-attachments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-policy-tables`.

- **AWS CLI**
- 
            
                    **To describe a transit gateway policy table**The following `describe-transit-gateway-policy-tables`example describes the specified transit gateway policy table.`aws ec2 describe-transit-gateway-policy-tables \ --transit-gateway-policy-table-ids``tgw-ptb-0a16f134b78668a81`Output: `{ "TransitGatewayPolicyTables": [ { "TransitGatewayPolicyTableId": "tgw-ptb-0a16f134b78668a81", "TransitGatewayId": "tgw-067f8505c18f0bd6e", "State": "available", "CreationTime": "2023-11-28T16:36:43+00:00", "Tags": [] } ] }`For more information, see [Transit gateway policy tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-policy-tables.html)in the*Transit Gateway User Guide*.- 
                    For API details, see [DescribeTransitGatewayPolicyTables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-policy-tables.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-route-tables`.

- **AWS CLI**
- 
            
                    **To describe your transit gateway route tables**The following `describe-transit-gateway-route-tables`example displays details for your transit gateway route tables.`aws ec2 describe-transit-gateway-route-tables`Output: `{ "TransitGatewayRouteTables": [ { "TransitGatewayRouteTableId": "tgw-rtb-0ca78a549EXAMPLE", "TransitGatewayId": "tgw-0bc994abffEXAMPLE", "State": "available", "DefaultAssociationRouteTable": true, "DefaultPropagationRouteTable": true, "CreationTime": "2018-11-28T14:24:49.000Z", "Tags": [] }, { "TransitGatewayRouteTableId": "tgw-rtb-0e8f48f148EXAMPLE", "TransitGatewayId": "tgw-0043d72bb4EXAMPLE", "State": "available", "DefaultAssociationRouteTable": true, "DefaultPropagationRouteTable": true, "CreationTime": "2018-11-28T14:24:00.000Z", "Tags": [] } ] }`For more information, see [View transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#view-tgw-route-tables)in the*Transit Gateways Guide*.- 
                    For API details, see [DescribeTransitGatewayRouteTables](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-route-tables.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateway-vpc-attachments`.

- **AWS CLI**
- 
            
                    **To describe your transit gateway VPC attachments**The following `describe-transit-gateway-vpc-attachments`example displays details for your transit gateway VPC attachments.`aws ec2 describe-transit-gateway-vpc-attachments`Output: `{ "TransitGatewayVpcAttachments": [ { "TransitGatewayAttachmentId": "tgw-attach-0a08e88308EXAMPLE", "TransitGatewayId": "tgw-0043d72bb4EXAMPLE", "VpcId": "vpc-0f501f7ee8EXAMPLE", "VpcOwnerId": "111122223333", "State": "available", "SubnetIds": [ "subnet-045d586432EXAMPLE", "subnet-0a0ad478a6EXAMPLE" ], "CreationTime": "2019-02-13T11:04:02.000Z", "Options": { "DnsSupport": "enable", "Ipv6Support": "disable" }, "Tags": [ { "Key": "Name", "Value": "attachment name" } ] } ] }`For more information, see [View your VPC attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html#view-vpc-attachment)in the*Transit Gateways Guide*.- 
                    For API details, see [DescribeTransitGatewayVpcAttachments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateway-vpc-attachments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-transit-gateways`.

- **AWS CLI**
- 
            
                    **To describe your transit gateways**The following `describe-transit-gateways`example retrieves details about your transit gateways.`aws ec2 describe-transit-gateways`Output: `{ "TransitGateways": [ { "TransitGatewayId": "tgw-0262a0e521EXAMPLE", "TransitGatewayArn": "arn:aws:ec2:us-east-2:111122223333:transit-gateway/tgw-0262a0e521EXAMPLE", "State": "available", "OwnerId": "111122223333", "Description": "MyTGW", "CreationTime": "2019-07-10T14:02:12.000Z", "Options": { "AmazonSideAsn": 64516, "AutoAcceptSharedAttachments": "enable", "DefaultRouteTableAssociation": "enable", "AssociationDefaultRouteTableId": "tgw-rtb-018774adf3EXAMPLE", "DefaultRouteTablePropagation": "enable", "PropagationDefaultRouteTableId": "tgw-rtb-018774adf3EXAMPLE", "VpnEcmpSupport": "enable", "DnsSupport": "enable" }, "Tags": [] }, { "TransitGatewayId": "tgw-0fb8421e2dEXAMPLE", "TransitGatewayArn": "arn:aws:ec2:us-east-2:111122223333:transit-gateway/tgw-0fb8421e2da853bf3", "State": "available", "OwnerId": "111122223333", "CreationTime": "2019-03-15T22:57:33.000Z", "Options": { "AmazonSideAsn": 65412, "AutoAcceptSharedAttachments": "disable", "DefaultRouteTableAssociation": "enable", "AssociationDefaultRouteTableId": "tgw-rtb-06a241a3d8EXAMPLE", "DefaultRouteTablePropagation": "enable", "PropagationDefaultRouteTableId": "tgw-rtb-06a241a3d8EXAMPLE", "VpnEcmpSupport": "enable", "DnsSupport": "enable" }, "Tags": [ { "Key": "Name", "Value": "TGW1" } ] } ] }`- 
                    For API details, see [DescribeTransitGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-transit-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-verified-access-endpoints`.

- **AWS CLI**
- 
            
                    **To describe a Verified Access endpoint**The following `describe-verified-access-endpoints`example describes the specified Verified Access endpoint.`aws ec2 describe-verified-access-endpoints \ --verified-access-endpoint-ids``vae-066fac616d4d546f2`Output: `{ "VerifiedAccessEndpoints": [ { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessEndpointId": "vae-066fac616d4d546f2", "ApplicationDomain": "example.com", "EndpointType": "network-interface", "AttachmentType": "vpc", "DomainCertificateArn": "arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE", "EndpointDomain": "my-ava-app.edge-00c3372d53b1540bb.vai-0ce000c0b7643abea.prod.verified-access.us-east-2.amazonaws.com", "SecurityGroupIds": [ "sg-004915970c4c8f13a" ], "NetworkInterfaceOptions": { "NetworkInterfaceId": "eni-0aec70418c8d87a0f", "Protocol": "https", "Port": 443 }, "Status": { "Code": "active" }, "Description": "", "CreationTime": "2023-08-25T20:54:43", "LastUpdatedTime": "2023-08-25T22:17:26", "Tags": [ { "Key": "Name", "Value": "my-va-endpoint" } ] } ] }`For more information, see [Verified Access endpoints](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DescribeVerifiedAccessEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-verified-access-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-verified-access-groups`.

- **AWS CLI**
- 
            
                    **To describe a Verified Access group**The following `describe-verified-access-groups`example describes the specified Verified Access group.`aws ec2 describe-verified-access-groups \ --verified-access-group-ids``vagr-0dbe967baf14b7235`Output: `{ "VerifiedAccessGroups": [ { "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "Testing Verified Access", "Owner": "123456789012", "VerifiedAccessGroupArn": "arn:aws:ec2:us-east-2:123456789012:verified-access-group/vagr-0dbe967baf14b7235", "CreationTime": "2023-08-25T19:55:19", "LastUpdatedTime": "2023-08-25T22:17:25", "Tags": [ { "Key": "Name", "Value": "my-va-group" } ] } ] }`For more information, see [Verified Access groups](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DescribeVerifiedAccessGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-verified-access-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-verified-access-instance-logging-configurations`.

- **AWS CLI**
- 
            
                    **To describe the logging configuration for a Verified Access instance**The following `describe-verified-access-instance-logging-configurations`example describes the logging configuration for the specified Verified Access instance.`aws ec2 describe-verified-access-instance-logging-configurations \ --verified-access-instance-ids``vai-0ce000c0b7643abea`Output: `{ "LoggingConfigurations": [ { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "AccessLogs": { "S3": { "Enabled": false }, "CloudWatchLogs": { "Enabled": true, "DeliveryStatus": { "Code": "success" }, "LogGroup": "my-log-group" }, "KinesisDataFirehose": { "Enabled": false }, "LogVersion": "ocsf-1.0.0-rc.2", "IncludeTrustContext": false } } ] }`For more information, see [Verified Access logs](https://docs.aws.amazon.com/verified-access/latest/ug/access-logs.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DescribeVerifiedAccessInstanceLoggingConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-verified-access-instance-logging-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-verified-access-instances`.

- **AWS CLI**
- 
            
                    **To describe a Verified Access instance**The following `describe-verified-access-instances`example describes the specified Verified Access instance.`aws ec2 describe-verified-access-instances \ --verified-access-instance-ids``vai-0ce000c0b7643abea`Output: `{ "VerifiedAccessInstances": [ { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "Testing Verified Access", "VerifiedAccessTrustProviders": [ { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center" } ], "CreationTime": "2023-08-25T18:27:56", "LastUpdatedTime": "2023-08-25T19:03:32", "Tags": [ { "Key": "Name", "Value": "my-ava-instance" } ] } ] }`For more information, see [Verified Access instances](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-instances.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DescribeVerifiedAccessInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-verified-access-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-verified-access-trust-providers`.

- **AWS CLI**
- 
            
                    **To describe a Verified Access trust provider**The following `describe-verified-access-trust-providers`example describes the specified Verified Access trust provider.`aws ec2 describe-verified-access-trust-providers \ --verified-access-trust-provider-ids``vatp-0bb32de759a3e19e7`Output: `{ "VerifiedAccessTrustProviders": [ { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "Description": "Testing Verified Access", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center", "PolicyReferenceName": "idc", "CreationTime": "2023-08-25T19:00:38", "LastUpdatedTime": "2023-08-25T19:03:32", "Tags": [ { "Key": "Name", "Value": "my-va-trust-provider" } ] } ] }`For more information, see [Trust providers for Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/trust-providers.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DescribeVerifiedAccessTrustProviders](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-verified-access-trust-providers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-volume-attribute`.

- **AWS CLI**
- 
            
                    **To describe a volume attribute**This example command describes the `autoEnableIo`attribute of the volume with the ID`vol-049df61146c4d7901`.Command: `aws ec2 describe-volume-attribute --volume-id``vol-049df61146c4d7901`--attribute`autoEnableIO`Output: `{ "AutoEnableIO": { "Value": false }, "VolumeId": "vol-049df61146c4d7901" }`- 
                    For API details, see [DescribeVolumeAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-volume-status`.

- **AWS CLI**
- 
            
                    **To describe the status of a single volume**This example command describes the status for the volume `vol-1234567890abcdef0`.Command: `aws ec2 describe-volume-status --volume-ids``vol-1234567890abcdef0`Output: `{ "VolumeStatuses": [ { "VolumeStatus": { "Status": "ok", "Details": [ { "Status": "passed", "Name": "io-enabled" }, { "Status": "not-applicable", "Name": "io-performance" } ] }, "AvailabilityZone": "us-east-1a", "VolumeId": "vol-1234567890abcdef0", "Actions": [], "Events": [] } ] }`**To describe the status of impaired volumes**This example command describes the status for all volumes that are impaired. In this example output, there are no impaired volumes. Command: `aws ec2 describe-volume-status --filters``Name=volume-status.status,Values=impaired`Output: `{ "VolumeStatuses": [] }`If you have a volume with a failed status check (status is impaired), see Working with an Impaired Volume in the *Amazon EC2 User Guide*.- 
                    For API details, see [DescribeVolumeStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-volumes-modifications`.

- **AWS CLI**
- 
            
                    **To describe the modification status for a volume**The following `describe-volumes-modifications`example describes the volume modification status of the specified volume.`aws ec2 describe-volumes-modifications \ --volume-ids``vol-1234567890abcdef0`Output: `{ "VolumeModification": { "TargetSize": 150, "TargetVolumeType": "io1", "ModificationState": "optimizing", "VolumeId": " vol-1234567890abcdef0", "TargetIops": 100, "StartTime": "2019-05-17T11:27:19.000Z", "Progress": 70, "OriginalVolumeType": "io1", "OriginalIops": 100, "OriginalSize": 100 } }`- 
                    For API details, see [DescribeVolumesModifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes-modifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-volumes`.

- **AWS CLI**
- 
            
                    **Example 1: To describe a volume**The following `describe-volumes`example describes the specified volumes in the current Region.`aws ec2 describe-volumes \ --volume-ids``vol-049df61146c4d7901``vol-1234567890abcdef0`Output: `{ "Volumes": [ { "AvailabilityZone": "us-east-1a", "Attachments": [ { "AttachTime": "2013-12-18T22:35:00.000Z", "InstanceId": "i-1234567890abcdef0", "VolumeId": "vol-049df61146c4d7901", "State": "attached", "DeleteOnTermination": true, "Device": "/dev/sda1" } ], "Encrypted": true, "KmsKeyId": "arn:aws:kms:us-east-2a:123456789012:key/8c5b2c63-b9bc-45a3-a87a-5513eEXAMPLE, "VolumeType": "gp2", "VolumeId": "vol-049df61146c4d7901", "State": "in-use", "Iops": 100, "SnapshotId": "snap-1234567890abcdef0", "CreateTime": "2019-12-18T22:35:00.084Z", "Size": 8 }, { "AvailabilityZone": "us-east-1a", "Attachments": [], "Encrypted": false, "VolumeType": "gp2", "VolumeId": "vol-1234567890abcdef0", "State": "available", "Iops": 300, "SnapshotId": "", "CreateTime": "2020-02-27T00:02:41.791Z", "Size": 100 } ] }`**Example 2: To describe volumes that are attached to a specific instance**The following `describe-volumes`example describes all volumes that are both attached to the specified instance and set to delete when the instance terminates.`aws ec2 describe-volumes \ --region``us-east-1`\ --filters`Name=attachment.instance-id,Values=i-1234567890abcdef0``Name=attachment.delete-on-termination,Values=true`For an example of the output for `describe-volumes`, see Example 1.**Example 3: To describe available volumes in a specific Availability Zone**The following `describe-volumes`example describes all volumes that have a status of`available`and are in the specified Availability Zone.`aws ec2 describe-volumes \ --filters``Name=status,Values=available``Name=availability-zone,Values=us-east-1a`For an example of the output for `describe-volumes`, see Example 1.**Example 4: To describe volumes based on tags**The following `describe-volumes`example describes all volumes that have the tag key`Name`and a value that begins with`Test`. The output is then filtered with a query that displays only the tags and IDs of the volumes.`aws ec2 describe-volumes \ --filters``Name=tag:Name,Values=Test*`\ --query`"Volumes[*].{ID:VolumeId,Tag:Tags}"`Output: `[ { "Tag": [ { "Value": "Test2", "Key": "Name" } ], "ID": "vol-1234567890abcdef0" }, { "Tag": [ { "Value": "Test1", "Key": "Name" } ], "ID": "vol-049df61146c4d7901" } ]`For additional examples using tag filters, see [Working with tags](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#Using_Tags_CLI)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DescribeVolumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volumes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-attribute`.

- **AWS CLI**
- 
            
                    **To describe the enableDnsSupport attribute**This example describes the `enableDnsSupport`attribute. This attribute indicates whether DNS resolution is enabled for the VPC. If this attribute is`true`, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not.Command: `aws ec2 describe-vpc-attribute --vpc-id``vpc-a01106c2`--attribute`enableDnsSupport`Output: `{ "VpcId": "vpc-a01106c2", "EnableDnsSupport": { "Value": true } }`**To describe the enableDnsHostnames attribute**This example describes the `enableDnsHostnames`attribute. This attribute indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is`true`, instances in the VPC get DNS hostnames; otherwise, they do not.Command: `aws ec2 describe-vpc-attribute --vpc-id``vpc-a01106c2`--attribute`enableDnsHostnames`Output: `{ "VpcId": "vpc-a01106c2", "EnableDnsHostnames": { "Value": true } }`- 
                    For API details, see [DescribeVpcAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-classic-link-dns-support`.

- **AWS CLI**
- 
            
                    **To describe ClassicLink DNS support for your VPCs**This example describes the ClassicLink DNS support status of all of your VPCs. Command: `aws ec2 describe-vpc-classic-link-dns-support`Output: `{ "Vpcs": [ { "VpcId": "vpc-88888888", "ClassicLinkDnsSupported": true }, { "VpcId": "vpc-1a2b3c4d", "ClassicLinkDnsSupported": false } ] }`- 
                    For API details, see [DescribeVpcClassicLinkDnsSupport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-classic-link-dns-support.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-classic-link`.

- **AWS CLI**
- 
            
                    **To describe the ClassicLink status of your VPCs**This example lists the ClassicLink status of vpc-88888888. Command: `aws ec2 describe-vpc-classic-link --vpc-id``vpc-88888888`Output: `{ "Vpcs": [ { "ClassicLinkEnabled": true, "VpcId": "vpc-88888888", "Tags": [ { "Value": "classiclinkvpc", "Key": "Name" } ] } ] }`This example lists only VPCs that are enabled for Classiclink (the filter value of `is-classic-link-enabled`is set to`true`).Command: `aws ec2 describe-vpc-classic-link --filter``"Name=is-classic-link-enabled,Values=true"`- 
                    For API details, see [DescribeVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-classic-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-endpoint-associations`.

- **AWS CLI**
- 
            
                    **To describe VPC endpoint associations**The following `describe-vpc-endpoint-associations`example describes your VPC endpoint associations.`aws ec2 describe-vpc-endpoint-associations`Output: `{ "VpcEndpointAssociations": [ { "Id": "vpce-rsc-asc-0a810ca6ac8866bf9", "VpcEndpointId": "vpce-019b90d6f16d4f958", "AssociatedResourceAccessibility": "Accessible", "DnsEntry": { "DnsName": "vpce-019b90d6f16d4f958.rcfg-07129f3acded87625.4232ccc.vpc-lattice-rsc.us-east-2.on.aws", "HostedZoneId": "Z03265862FOUNWMZOKUF4" }, "AssociatedResourceArn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-07129f3acded87625" } ] }`For more information, see [Manage VPC endpoint associations](https://docs.aws.amazon.com/vpc/latest/privatelink/resource-configuration-associations.html#resource-config-manage-ep-association)in the*AWS PrivateLink User Guide*.- 
                    For API details, see [DescribeVpcEndpointAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-endpoint-connection-notifications`.

- **AWS CLI**
- 
            
                    **To describe endpoint connection notifications**The following `describe-vpc-endpoint-connection-notifications`example describes all of your endpoint connection notifications.`aws ec2 describe-vpc-endpoint-connection-notifications`Output: `{ "ConnectionNotificationSet": [ { "ConnectionNotificationState": "Enabled", "ConnectionNotificationType": "Topic", "ConnectionEvents": [ "Accept", "Reject", "Delete", "Connect" ], "ConnectionNotificationId": "vpce-nfn-04bcb952bc8af7abc", "ConnectionNotificationArn": "arn:aws:sns:us-east-1:123456789012:VpceNotification", "VpcEndpointId": "vpce-0324151a02f327123" } ] }`- 
                    For API details, see [DescribeVpcEndpointConnectionNotifications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-connection-notifications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-endpoint-connections`.

- **AWS CLI**
- 
            
                    **To describe VPC endpoint connections**This example describes the interface endpoint connections to your endpoint service and filters the results to display endpoints that are `PendingAcceptance`.Command: `aws ec2 describe-vpc-endpoint-connections --filters``Name=vpc-endpoint-state,Values=pendingAcceptance`Output: `{ "VpcEndpointConnections": [ { "VpcEndpointId": "vpce-0abed31004e618123", "ServiceId": "vpce-svc-0abced088d20def56", "CreationTimestamp": "2017-11-30T10:00:24.350Z", "VpcEndpointState": "pendingAcceptance", "VpcEndpointOwner": "123456789012" } ] }`- 
                    For API details, see [DescribeVpcEndpointConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-endpoint-service-configurations`.

- **AWS CLI**
- 
            
                    **To describe endpoint service configurations**The following `describe-vpc-endpoint-service-configurations`example describes your endpoint service configurations.`aws ec2 describe-vpc-endpoint-service-configurations`Output: `{ "ServiceConfigurations": [ { "ServiceType": [ { "ServiceType": "GatewayLoadBalancer" } ], "ServiceId": "vpce-svc-012d33a1c4321cabc", "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-012d33a1c4321cabc", "ServiceState": "Available", "AvailabilityZones": [ "us-east-1d" ], "AcceptanceRequired": false, "ManagesVpcEndpoints": false, "GatewayLoadBalancerArns": [ "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/123210844e429123" ], "Tags": [] }, { "ServiceType": [ { "ServiceType": "Interface" } ], "ServiceId": "vpce-svc-123cabc125efa123", "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-123cabc125efa123", "ServiceState": "Available", "AvailabilityZones": [ "us-east-1a" ], "AcceptanceRequired": true, "ManagesVpcEndpoints": false, "NetworkLoadBalancerArns": [ "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/NLBforService/1238753950b25123" ], "BaseEndpointDnsNames": [ "vpce-svc-123cabc125efa123.us-east-1.vpce.amazonaws.com" ], "PrivateDnsName": "example.com", "PrivateDnsNameConfiguration": { "State": "failed", "Type": "TXT", "Value": "vpce:qUAth3FdeABCApUiXabc", "Name": "_1d367jvbg34znqvyefrj" }, "Tags": [] } ] }`For more information, see [Concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)in the*AWS PrivateLink User Guide*.- 
                    For API details, see [DescribeVpcEndpointServiceConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-service-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-endpoint-service-permissions`.

- **AWS CLI**
- 
            
                    **To describe endpoint service permissions**This example describes the permissions for the specified endpoint service. Command: `aws ec2 describe-vpc-endpoint-service-permissions --service-id``vpce-svc-03d5ebb7d9579a2b3`Output: `{ "AllowedPrincipals": [ { "PrincipalType": "Account", "Principal": "arn:aws:iam::123456789012:root" } ] }`- 
                    For API details, see [DescribeVpcEndpointServicePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-service-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-endpoint-services`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all VPC endpoint services**The following `describe-vpc-endpoint-services`example lists all VPC endpoint services for an AWS Region.`aws ec2 describe-vpc-endpoint-services`Output: `{ "ServiceDetails": [ { "ServiceType": [ { "ServiceType": "Gateway" } ], "AcceptanceRequired": false, "ServiceName": "com.amazonaws.us-east-1.dynamodb", "VpcEndpointPolicySupported": true, "Owner": "amazon", "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e", "us-east-1f" ], "BaseEndpointDnsNames": [ "dynamodb.us-east-1.amazonaws.com" ] }, { "ServiceType": [ { "ServiceType": "Interface" } ], "PrivateDnsName": "ec2.us-east-1.amazonaws.com", "ServiceName": "com.amazonaws.us-east-1.ec2", "VpcEndpointPolicySupported": false, "Owner": "amazon", "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e", "us-east-1f" ], "AcceptanceRequired": false, "BaseEndpointDnsNames": [ "ec2.us-east-1.vpce.amazonaws.com" ] }, { "ServiceType": [ { "ServiceType": "Interface" } ], "PrivateDnsName": "ssm.us-east-1.amazonaws.com", "ServiceName": "com.amazonaws.us-east-1.ssm", "VpcEndpointPolicySupported": true, "Owner": "amazon", "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e" ], "AcceptanceRequired": false, "BaseEndpointDnsNames": [ "ssm.us-east-1.vpce.amazonaws.com" ] } ], "ServiceNames": [ "com.amazonaws.us-east-1.dynamodb", "com.amazonaws.us-east-1.ec2", "com.amazonaws.us-east-1.ec2messages", "com.amazonaws.us-east-1.elasticloadbalancing", "com.amazonaws.us-east-1.kinesis-streams", "com.amazonaws.us-east-1.s3", "com.amazonaws.us-east-1.ssm" ] }`**Example 2: To describe the details about an endpoint service**The following `describe-vpc-endpoint-services`example lists the details of the Amazon S3 interface endpoint service.`aws ec2 describe-vpc-endpoint-services \ --filter '``Name=service-type,Values=Interface`'`Name=service-name,Values=com.amazonaws.us-east-1.s3`Output: `{ "ServiceDetails": [ { "ServiceName": "com.amazonaws.us-east-1.s3", "ServiceId": "vpce-svc-081d84efcdEXAMPLE", "ServiceType": [ { "ServiceType": "Interface" } ], "AvailabilityZones": [ "us-east-1a", "us-east-1b", "us-east-1c", "us-east-1d", "us-east-1e", "us-east-1f" ], "Owner": "amazon", "BaseEndpointDnsNames": [ "s3.us-east-1.vpce.amazonaws.com" ], "VpcEndpointPolicySupported": true, "AcceptanceRequired": false, "ManagesVpcEndpoints": false, "Tags": [] } ], "ServiceNames": [ "com.amazonaws.us-east-1.s3" ] }`For more information, see [View available AWS service names](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html#vpce-view-available-services)in the*AWS PrivateLink User Guide*.- 
                    For API details, see [DescribeVpcEndpointServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoint-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-endpoints`.

- **AWS CLI**
- 
            
                    **To describe your VPC endpoints**The following `describe-vpc-endpoints`example displays details for all of your VPC endpoints.`aws ec2 describe-vpc-endpoints`Output: `{ "VpcEndpoints": [ { "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}", "VpcId": "vpc-aabb1122", "NetworkInterfaceIds": [], "SubnetIds": [], "PrivateDnsEnabled": true, "State": "available", "ServiceName": "com.amazonaws.us-east-1.dynamodb", "RouteTableIds": [ "rtb-3d560345" ], "Groups": [], "VpcEndpointId": "vpce-032a826a", "VpcEndpointType": "Gateway", "CreationTimestamp": "2017-09-05T20:41:28Z", "DnsEntries": [], "OwnerId": "123456789012" }, { "PolicyDocument": "{\n \"Statement\": [\n {\n \"Action\": \"*\", \n \"Effect\": \"Allow\", \n \"Principal\": \"*\", \n \"Resource\": \"*\"\n }\n ]\n}", "VpcId": "vpc-1a2b3c4d", "NetworkInterfaceIds": [ "eni-2ec2b084", "eni-1b4a65cf" ], "SubnetIds": [ "subnet-d6fcaa8d", "subnet-7b16de0c" ], "PrivateDnsEnabled": false, "State": "available", "ServiceName": "com.amazonaws.us-east-1.elasticloadbalancing", "RouteTableIds": [], "Groups": [ { "GroupName": "default", "GroupId": "sg-54e8bf31" } ], "VpcEndpointId": "vpce-0f89a33420c1931d7", "VpcEndpointType": "Interface", "CreationTimestamp": "2017-09-05T17:55:27.583Z", "DnsEntries": [ { "HostedZoneId": "Z7HUB22UULQXV", "DnsName": "vpce-0f89a33420c1931d7-bluzidnv.elasticloadbalancing.us-east-1.vpce.amazonaws.com" }, { "HostedZoneId": "Z7HUB22UULQXV", "DnsName": "vpce-0f89a33420c1931d7-bluzidnv-us-east-1b.elasticloadbalancing.us-east-1.vpce.amazonaws.com" }, { "HostedZoneId": "Z7HUB22UULQXV", "DnsName": "vpce-0f89a33420c1931d7-bluzidnv-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com" } ], "OwnerId": "123456789012" }, { "VpcEndpointId": "vpce-aabbaabbaabbaabba", "VpcEndpointType": "GatewayLoadBalancer", "VpcId": "vpc-111122223333aabbc", "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123", "State": "available", "SubnetIds": [ "subnet-0011aabbcc2233445" ], "RequesterManaged": false, "NetworkInterfaceIds": [ "eni-01010120203030405" ], "CreationTimestamp": "2020-11-11T08:06:03.522Z", "Tags": [], "OwnerId": "123456789012" } ] }`For more information, see [Concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)in the*AWS PrivateLink User Guide*.- 
                    For API details, see [DescribeVpcEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpc-peering-connections`.

- **AWS CLI**
- 
            
                    **To describe your VPC peering connections**This example describes all of your VPC peering connections. Command: `aws ec2 describe-vpc-peering-connections`Output: `{ "VpcPeeringConnections": [ { "Status": { "Message": "Active", "Code": "active" }, "Tags": [ { "Value": "Peering-1", "Key": "Name" } ], "AccepterVpcInfo": { "OwnerId": "111122223333", "VpcId": "vpc-1a2b3c4d", "CidrBlock": "10.0.1.0/28" }, "VpcPeeringConnectionId": "pcx-11122233", "RequesterVpcInfo": { "PeeringOptions": { "AllowEgressFromLocalVpcToRemoteClassicLink": false, "AllowEgressFromLocalClassicLinkToRemoteVpc": false }, "OwnerId": "444455556666", "VpcId": "vpc-123abc45", "CidrBlock": "192.168.0.0/16" } }, { "Status": { "Message": "Pending Acceptance by 444455556666", "Code": "pending-acceptance" }, "Tags": [], "RequesterVpcInfo": { "PeeringOptions": { "AllowEgressFromLocalVpcToRemoteClassicLink": false, "AllowEgressFromLocalClassicLinkToRemoteVpc": false }, "OwnerId": "444455556666", "VpcId": "vpc-11aa22bb", "CidrBlock": "10.0.0.0/28" }, "VpcPeeringConnectionId": "pcx-abababab", "ExpirationTime": "2014-04-03T09:12:43.000Z", "AccepterVpcInfo": { "OwnerId": "444455556666", "VpcId": "vpc-33cc44dd" } } ] }`**To describe specific VPC peering connections**This example describes all of your VPC peering connections that are in the pending-acceptance state. Command: `aws ec2 describe-vpc-peering-connections --filters``Name=status-code,Values=pending-acceptance`This example describes all of your VPC peering connections that have the tag Owner=Finance. Command: `aws ec2 describe-vpc-peering-connections --filters``Name=tag:Owner,Values=Finance`This example describes all of the VPC peering connections you requested for the specified VPC, vpc-1a2b3c4d. Command: `aws ec2 describe-vpc-peering-connections --filters``Name=requester-vpc-info.vpc-id,Values=vpc-1a2b3c4d`- 
                    For API details, see [DescribeVpcPeeringConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-peering-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpcs`.

- **AWS CLI**
- 
            
                    **Example 1: To describe all of your VPCs**The following `describe-vpcs`example retrieves details about your VPCs.`aws ec2 describe-vpcs`Output: `{ "Vpcs": [ { "CidrBlock": "30.1.0.0/16", "DhcpOptionsId": "dopt-19edf471", "State": "available", "VpcId": "vpc-0e9801d129EXAMPLE", "OwnerId": "111122223333", "InstanceTenancy": "default", "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-062c64cfafEXAMPLE", "CidrBlock": "30.1.0.0/16", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false, "Tags": [ { "Key": "Name", "Value": "Not Shared" } ] }, { "CidrBlock": "10.0.0.0/16", "DhcpOptionsId": "dopt-19edf471", "State": "available", "VpcId": "vpc-06e4ab6c6cEXAMPLE", "OwnerId": "222222222222", "InstanceTenancy": "default", "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-00b17b4eddEXAMPLE", "CidrBlock": "10.0.0.0/16", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false, "Tags": [ { "Key": "Name", "Value": "Shared VPC" } ] } ] }`**Example 2: To describe a specified VPC**The following `describe-vpcs`example retrieves details for the specified VPC.`aws ec2 describe-vpcs \ --vpc-ids``vpc-06e4ab6c6cEXAMPLE`Output: `{ "Vpcs": [ { "CidrBlock": "10.0.0.0/16", "DhcpOptionsId": "dopt-19edf471", "State": "available", "VpcId": "vpc-06e4ab6c6cEXAMPLE", "OwnerId": "111122223333", "InstanceTenancy": "default", "CidrBlockAssociationSet": [ { "AssociationId": "vpc-cidr-assoc-00b17b4eddEXAMPLE", "CidrBlock": "10.0.0.0/16", "CidrBlockState": { "State": "associated" } } ], "IsDefault": false, "Tags": [ { "Key": "Name", "Value": "Shared VPC" } ] } ] }`- 
                    For API details, see [DescribeVpcs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpcs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpn-connections`.

- **AWS CLI**
- 
            
                    **Example 1: To describe your VPN connections**The following `describe-vpn-connections`example describes all of your Site-to-Site VPN connections.`aws ec2 describe-vpn-connections`Output: `{ "VpnConnections": [ { "CustomerGatewayConfiguration": "...configuration information...", "CustomerGatewayId": "cgw-01234567abcde1234", "Category": "VPN", "State": "available", "Type": "ipsec.1", "VpnConnectionId": "vpn-1122334455aabbccd", "TransitGatewayId": "tgw-00112233445566aab", "Options": { "EnableAcceleration": false, "StaticRoutesOnly": true, "LocalIpv4NetworkCidr": "0.0.0.0/0", "RemoteIpv4NetworkCidr": "0.0.0.0/0", "TunnelInsideIpVersion": "ipv4" }, "Routes": [], "Tags": [ { "Key": "Name", "Value": "CanadaVPN" } ], "VgwTelemetry": [ { "AcceptedRouteCount": 0, "LastStatusChange": "2020-07-29T10:35:11.000Z", "OutsideIpAddress": "203.0.113.3", "Status": "DOWN", "StatusMessage": "" }, { "AcceptedRouteCount": 0, "LastStatusChange": "2020-09-02T09:09:33.000Z", "OutsideIpAddress": "203.0.113.5", "Status": "UP", "StatusMessage": "" } ] } ] }`For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)in the*AWS Site-to-Site VPN User Guide*.**Example 2: To describe your available VPN connections**The following `describe-vpn-connections`example describes your Site-to-Site VPN connections with a state of`available`.`aws ec2 describe-vpn-connections \ --filters``"Name=state,Values=available"`For more information, see [How AWS Site-to-Site VPN works](https://docs.aws.amazon.com/vpn/latest/s2svpn/how_it_works.html)in the*AWS Site-to-Site VPN User Guide*.- 
                    For API details, see [DescribeVpnConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-vpn-gateways`.

- **AWS CLI**
- 
            
                    **To describe your virtual private gateways**This example describes your virtual private gateways. Command: `aws ec2 describe-vpn-gateways`Output: `{ "VpnGateways": [ { "State": "available", "Type": "ipsec.1", "VpnGatewayId": "vgw-f211f09b", "VpcAttachments": [ { "State": "attached", "VpcId": "vpc-98eb5ef5" } ] }, { "State": "available", "Type": "ipsec.1", "VpnGatewayId": "vgw-9a4cacf3", "VpcAttachments": [ { "State": "attaching", "VpcId": "vpc-a01106c2" } ] } ] }`- 
                    For API details, see [DescribeVpnGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-classic-link-vpc`.

- **AWS CLI**
- 
            
                    **To unlink (detach) an EC2-Classic instance from a VPC**This example unlinks instance i-0598c7d356eba48d7 from VPC vpc-88888888. Command: `aws ec2 detach-classic-link-vpc --instance-id``i-0598c7d356eba48d7`--vpc-id`vpc-88888888`Output: `{ "Return": true }`- 
                    For API details, see [DetachClassicLinkVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-classic-link-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-internet-gateway`.

- **AWS CLI**
- 
            
                    **To detach an internet gateway from your VPC**The following `detach-internet-gateway`example detaches the specified internet gateway from the specific VPC.`aws ec2 detach-internet-gateway \ --internet-gateway-id``igw-0d0fb496b3EXAMPLE`\ --vpc-id`vpc-0a60eb65b4EXAMPLE`This command produces no output. For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DetachInternetGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-internet-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-network-interface`.

- **AWS CLI**
- 
            
                    **To detach a network interface from your instance**This example detaches the specified network interface from the specified instance. If the command succeeds, no output is returned. Command: `aws ec2 detach-network-interface --attachment-id``eni-attach-66c4350a`- 
                    For API details, see [DetachNetworkInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-network-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-verified-access-trust-provider`.

- **AWS CLI**
- 
            
                    **To detach a trust provider from an instance**The following `detach-verified-access-trust-provider`example detaches the specified Verified Access trust provider from the specified Verified Access instance.`aws ec2 detach-verified-access-trust-provider \ --verified-access-instance-id``vai-0ce000c0b7643abea`\ --verified-access-trust-provider-id`vatp-0bb32de759a3e19e7`Output: `{ "VerifiedAccessTrustProvider": { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "Description": "Testing Verified Access", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center", "PolicyReferenceName": "idc", "CreationTime": "2023-08-25T19:00:38", "LastUpdatedTime": "2023-08-25T19:00:38" }, "VerifiedAccessInstance": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "Testing Verified Access", "VerifiedAccessTrustProviders": [], "CreationTime": "2023-08-25T18:27:56", "LastUpdatedTime": "2023-08-25T18:27:56" } }`For more information, see [Verified Access instances](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-instances.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [DetachVerifiedAccessTrustProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-verified-access-trust-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-volume`.

- **AWS CLI**
- 
            
                    **To detach a volume from an instance**This example command detaches the volume ( `vol-049df61146c4d7901`) from the instance it is attached to.Command: `aws ec2 detach-volume --volume-id``vol-1234567890abcdef0`Output: `{ "AttachTime": "2014-02-27T19:23:06.000Z", "InstanceId": "i-1234567890abcdef0", "VolumeId": "vol-049df61146c4d7901", "State": "detaching", "Device": "/dev/sdb" }`- 
                    For API details, see [DetachVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-volume.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-vpn-gateway`.

- **AWS CLI**
- 
            
                    **To detach a virtual private gateway from your VPC**This example detaches the specified virtual private gateway from the specified VPC. If the command succeeds, no output is returned. Command: `aws ec2 detach-vpn-gateway --vpn-gateway-id``vgw-9a4cacf3`--vpc-id`vpc-a01106c2`- 
                    For API details, see [DetachVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-vpn-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-address-transfer`.

- **AWS CLI**
- 
            
                    **To disable an Elastic IP address transfer**The following `disable-address-transfer`example disables Elastic IP address transfer for the specified Elastic IP address.`aws ec2 disable-address-transfer \ --allocation-id``eipalloc-09ad461b0d03f6aaf`Output: `{ "AddressTransfer": { "PublicIp": "100.21.184.216", "AllocationId": "eipalloc-09ad461b0d03f6aaf", "AddressTransferStatus": "disabled" } }`For more information, see [Transfer Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html#transfer-EIPs-intro)in the*Amazon VPC User Guide*.- 
                    For API details, see [DisableAddressTransfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-address-transfer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-aws-network-performance-metric-subscription`.

- **AWS CLI**
- 
            
                    **To disable a metric subscription**The following `disable-aws-network-performance-metric-subscription`example disables the monitoring of aggregate network latency between the specified source and destination Regions.`aws ec2 disable-aws-network-performance-metric-subscription \ --source``us-east-1`\ --destination`eu-west-1`\ --metric`aggregate-latency`\ --statistic`p50`Output: `{ "Output": true }`For more information, see [Manage CloudWatch subscriptions using the CLI](https://docs.aws.amazon.com/network-manager/latest/infrastructure-performance/getting-started-nmip-cli.html)in the*Infrastructure Performance User Guide*.- 
                    For API details, see [DisableAwsNetworkPerformanceMetricSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-aws-network-performance-metric-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-ebs-encryption-by-default`.

- **AWS CLI**
- 
            
                    **To disable EBS encryption by default**The following `disable-ebs-encryption-by-default`example disables EBS encryption by default for your AWS account in the current Region.`aws ec2 disable-ebs-encryption-by-default`Output: `{ "EbsEncryptionByDefault": false }`- 
                    For API details, see [DisableEbsEncryptionByDefault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-ebs-encryption-by-default.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-fast-launch`.

- **AWS CLI**
- 
            
                    **To discontinue fast launching for an image**The following `disable-fast-launch`example discontinues Fast Launch for the specified AMI, and cleans up existing pre-provisioned snapshots.`aws ec2 disable-fast-launch \ --image-id``ami-01234567890abcedf`Output: `{ "ImageId": "ami-01234567890abcedf", "ResourceType": "snapshot", "SnapshotConfiguration": {}, "LaunchTemplate": { "LaunchTemplateId": "lt-01234567890abcedf", "LaunchTemplateName": "EC2FastLaunchDefaultResourceCreation-a8c6215d-94e6-441b-9272-dbd1f87b07e2", "Version": "1" }, "MaxParallelLaunches": 6, "OwnerId": "0123456789123", "State": "disabling", "StateTransitionReason": "Client.UserInitiated", "StateTransitionTime": "2022-01-27T22:47:29.265000+00:00" }`For more information, see [Configure EC2 Fast Launch settings for your Windows AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-configure.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DisableFastLaunch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-fast-launch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-fast-snapshot-restores`.

- **AWS CLI**
- 
            
                    **To disable fast snapshot restore**The following `disable-fast-snapshot-restores`example disables fast snapshot restore for the specified snapshot in the specified Availability Zone.`aws ec2 disable-fast-snapshot-restores \ --availability-zones``us-east-2a`\ --source-snapshot-ids`snap-1234567890abcdef0`Output: `{ "Successful": [ { "SnapshotId": "snap-1234567890abcdef0" "AvailabilityZone": "us-east-2a", "State": "disabling", "StateTransitionReason": "Client.UserInitiated", "OwnerId": "123456789012", "EnablingTime": "2020-01-25T23:57:49.602Z" } ], "Unsuccessful": [] }`- 
                    For API details, see [DisableFastSnapshotRestores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-fast-snapshot-restores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-image-block-public-access`.

- **AWS CLI**
- 
            
                    **To disable block public access for AMIs in the specified Region**The following `disable-image-block-public-access`example disables block public access for AMIs at the account level in the specified Region.`aws ec2 disable-image-block-public-access \ --region``us-east-1`Output: `{ "ImageBlockPublicAccessState": "unblocked" }`For more information, see [Block public access to your AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-public-access-to-amis.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DisableImageBlockPublicAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-image-block-public-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-image-deprecation`.

- **AWS CLI**
- 
            
                    **To cancel the deprecation of an AMI**The following `disable-image-deprecation`example cancels the deprecation of an AMI, which removes the`DeprecationTime`field from the`describe-images`output. You must be the AMI owner to perform this procedure.`aws ec2 disable-image-deprecation \ --image-id``ami-1234567890abcdef0`Output: `{ "RequestID": "11aabb229-4eac-35bd-99ed-be587EXAMPLE", "Return": "true" }`For more information, see [Deprecate an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DisableImageDeprecation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-image-deprecation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-image-deregistration-protection`.

- **AWS CLI**
- 
            
                    **To disable deregistration protection**The following `disable-image-deregistration-protection`example disables deregistration protection for the specified image.`aws ec2 disable-image-deregistration-protection \ --image-id``ami-0b1a928a144a74ec9`Output: `{ "Return": "disabled" }`For more information, see [Protect an AMI from deregistration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deregistration-protection.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DisableImageDeregistrationProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-image-deregistration-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-image`.

- **AWS CLI**
- 
            
                    **To disable an AMI**The following `disable-image`example disables the specified AMI.`aws ec2 disable-image \ --image-id``ami-1234567890abcdef0`Output: `{ "Return": "true" }`For more information, see [Disable an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disable-an-ami.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DisableImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-ipam-organization-admin-account`.

- **AWS CLI**
- 
            
                    **To disable the delegated IPAM admin**In certain scenarios, you'll integrate IPAM with AWS Organizations. When you do that, the AWS Organizations management account delegates an AWS Organizations member account as the IPAM admin. In this example, you are the AWS Organizations management account that delegated the IPAM admin account and you want to disable that account from being the IPAM admin. You can use any AWS Region for `--region`when making this request. You don't have to use the Region where you originally delegated the admin, where the IPAM was created, or an IPAM operating Region. If you disable the delegated admin account, you can re-enable it at any time or delegate a new account as IPAM admin.The following `disable-ipam-organization-admin-account`example disables the delegated IPAM admin in your AWS account.`aws ec2 disable-ipam-organization-admin-account \ --delegated-admin-account-id``320805250157`\ --region`ap-south-1`Output: `{ "Success": true }`For more information, see [Integrate IPAM with accounts in an AWS Organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DisableIpamOrganizationAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-ipam-organization-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-serial-console-access`.

- **AWS CLI**
- 
            
                    **To disable access to the EC2 serial console for your account**The following `disable-serial-console-access`example disables account access to the serial console.`aws ec2 disable-serial-console-access`Output: `{ "SerialConsoleAccessEnabled": false }`For more information, see [EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [DisableSerialConsoleAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-serial-console-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-snapshot-block-public-access`.

- **AWS CLI**
- 
            
                    **To disable block public access for snapshots**The following `disable-snapshot-block-public-access`example disables block public access for snapshots to allow public sharing of your snapshots.`aws ec2 disable-snapshot-block-public-access`Output: `{ "State": "unblocked" }`For more information, see [Block public access for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [DisableSnapshotBlockPublicAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-snapshot-block-public-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-transit-gateway-route-table-propagation`.

- **AWS CLI**
- 
            
                    **To disable a transit gateway attachment to propagate routes to the specified propagation route table**The following `disable-transit-gateway-route-table-propagation`example disables the specified attachment to propagate routes to the specified propagation route table.`aws ec2 disable-transit-gateway-route-table-propagation \ --transit-gateway-route-table-id``tgw-rtb-0a823edbdeEXAMPLE`\ --transit-gateway-attachment-id`tgw-attach-09b52ccdb5EXAMPLE`Output: `{ "Propagation": { "TransitGatewayAttachmentId": "tgw-attach-09b52ccdb5EXAMPLE", "ResourceId": "vpc-4d7de228", "ResourceType": "vpc", "TransitGatewayRouteTableId": "tgw-rtb-0a823edbdeEXAMPLE", "State": "disabled" } }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DisableTransitGatewayRouteTablePropagation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-transit-gateway-route-table-propagation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-vgw-route-propagation`.

- **AWS CLI**
- 
            
                    **To disable route propagation**This example disables the specified virtual private gateway from propagating static routes to the specified route table. If the command succeeds, no output is returned. Command: `aws ec2 disable-vgw-route-propagation --route-table-id``rtb-22574640`--gateway-id`vgw-9a4cacf3`- 
                    For API details, see [DisableVgwRoutePropagation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vgw-route-propagation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-vpc-classic-link-dns-support`.

- **AWS CLI**
- 
            
                    **To disable ClassicLink DNS support for a VPC**This example disables ClassicLink DNS support for `vpc-88888888`.Command: `aws ec2 disable-vpc-classic-link-dns-support --vpc-id``vpc-88888888`Output: `{ "Return": true }`- 
                    For API details, see [DisableVpcClassicLinkDnsSupport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vpc-classic-link-dns-support.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-vpc-classic-link`.

- **AWS CLI**
- 
            
                    **To disable ClassicLink for a VPC**This example disables ClassicLink for vpc-8888888. Command: `aws ec2 disable-vpc-classic-link --vpc-id``vpc-88888888`Output: `{ "Return": true }`- 
                    For API details, see [DisableVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vpc-classic-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-address`.

- **AWS CLI**
- 
            
                    **To disassociate an Elastic IP addresses in EC2-Classic**This example disassociates an Elastic IP address from an instance in EC2-Classic. If the command succeeds, no output is returned. Command: `aws ec2 disassociate-address --public-ip``198.51.100.0`**To disassociate an Elastic IP address in EC2-VPC**This example disassociates an Elastic IP address from an instance in a VPC. If the command succeeds, no output is returned. Command: `aws ec2 disassociate-address --association-id``eipassoc-2bebb745`- 
                    For API details, see [DisassociateAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-client-vpn-target-network`.

- **AWS CLI**
- 
            
                    **To disassociate a network from a Client VPN endpoint**The following `disassociate-client-vpn-target-network`example disassociates the target network that's associated with the`cvpn-assoc-12312312312312312`association ID for the specified Client VPN endpoint.`aws ec2 disassociate-client-vpn-target-network \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --association-id`cvpn-assoc-12312312312312312`Output: `{ "AssociationId": "cvpn-assoc-12312312312312312", "Status": { "Code": "disassociating" } }`For more information, see [Target Networks](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-target.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [DisassociateClientVpnTargetNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-client-vpn-target-network.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-iam-instance-profile`.

- **AWS CLI**
- 
            
                    **To disassociate an IAM instance profile**This example disassociates an IAM instance profile with the association ID `iip-assoc-05020b59952902f5f`.Command: `aws ec2 disassociate-iam-instance-profile --association-id``iip-assoc-05020b59952902f5f`Output: `{ "IamInstanceProfileAssociation": { "InstanceId": "i-123456789abcde123", "State": "disassociating", "AssociationId": "iip-assoc-05020b59952902f5f", "IamInstanceProfile": { "Id": "AIPAI5IVIHMFFYY2DKV5Y", "Arn": "arn:aws:iam::123456789012:instance-profile/admin-role" } } }`- 
                    For API details, see [DisassociateIamInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-iam-instance-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-instance-event-window`.

- **AWS CLI**
- 
            
                    **Example 1: To disassociate one or more instances from an event window**The following `disassociate-instance-event-window`example disassociates one or more instances from an event window. Specify the`instance-event-window-id`parameter to specify the event window. To disassociate instances, specify the`association-target`parameter, and for the parameter values, specify one or more instance IDs.`aws ec2 disassociate-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --association-target`"InstanceIds=i-1234567890abcdef0,i-0598c7d356eba48d7"`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": [] }, "State": "creating" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 2: To disassociate instance tags from an event window**The following `disassociate-instance-event-window`example disassociates instance tags from an event window. Specify the`instance-event-window-id`parameter to specify the event window. To disassociate instance tags, specify the`association-target`parameter, and for the parameter values, specify one or more tags.`aws ec2 disassociate-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --association-target`"InstanceTags=[{Key=k2,Value=v2},{Key=k1,Value=v1}]"`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": [] }, "State": "creating" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 3: To disassociate a Dedicated Host from an event window**The following `disassociate-instance-event-window`example disassociates a Dedicated Host from an event window. Specify the`instance-event-window-id`parameter to specify the event window. To disassociate a Dedicated Host, specify the`association-target`parameter, and for the parameter values, specify one or more Dedicated Host IDs.`aws ec2 disassociate-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --association-target`DedicatedHostIds=h-029fa35a02b99801d`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [], "Tags": [], "DedicatedHostIds": [] }, "State": "creating" } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.- 
                    For API details, see [DisassociateInstanceEventWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-instance-event-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-ipam-resource-discovery`.

- **AWS CLI**
- 
            
                    **To disassociate a resource discovery from an IPAM**In this example, you are an IPAM delegated admin account and you want to disassociate an IPAM resource discovery from your IPAM. You ran the describe command and noticed that the `"ResourceDiscoveryStatus": "not-found"`and you want to disassociate it from your IPAM to make room for other associations.The following `disassociate-ipam-resource-discovery`example disassociates an IPAM resource discovery in your AWS account.`aws ec2 disassociate-ipam-resource-discovery \ --ipam-resource-discovery-association-id``ipam-res-disco-assoc-04382a6346357cf82`\ --region`us-east-1`Output: `{ "IpamResourceDiscoveryAssociation": { "OwnerId": "320805250157", "IpamResourceDiscoveryAssociationId": "ipam-res-disco-assoc-04382a6346357cf82", "IpamResourceDiscoveryAssociationArn": "arn:aws:ec2::320805250157:ipam-resource-discovery-association/ipam-res-disco-assoc-04382a6346357cf82", "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe", "IpamId": "ipam-005f921c17ebd5107", "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-005f921c17ebd5107", "IpamRegion": "us-east-1", "IsDefault": false, "ResourceDiscoveryStatus": "not-found", "State": "disassociate-in-progress" } }`For more information, see [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [DisassociateIpamResourceDiscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-ipam-resource-discovery.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-nat-gateway-address`.

- **AWS CLI**
- 
            
                    **To disassociate an Elastic IP address from a public NAT gateway**The following `disassociate-nat-gateway-address`example disassociates the specified Elastic IP address from the specified public NAT gateway.`aws ec2 disassociate-nat-gateway-address \ --nat-gateway-id``nat-1234567890abcdef0`\ --association-ids`eipassoc-0f96bdca17EXAMPLE`Output: `{ "NatGatewayId": "nat-1234567890abcdef0", "NatGatewayAddresses": [ { "AllocationId": "eipalloc-0be6ecac95EXAMPLE", "NetworkInterfaceId": "eni-09cc4b2558794f7f9", "PrivateIp": "10.0.0.74", "PublicIp": "3.211.231.218", "AssociationId": "eipassoc-0f96bdca17EXAMPLE", "IsPrimary": false, "Status": "disassociating" } ] }`For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DisassociateNatGatewayAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-nat-gateway-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-route-table`.

- **AWS CLI**
- 
            
                    **To disassociate a route table**This example disassociates the specified route table from the specified subnet. If the command succeeds, no output is returned. Command: `aws ec2 disassociate-route-table --association-id``rtbassoc-781d0d1a`- 
                    For API details, see [DisassociateRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-security-group-vpc`.

- **AWS CLI**
- 
            
                    **To disassociate a security group from a VPC**The following `disassociate-security-group-vpc`example disassociates the specified security group from the specified VPC.`aws ec2 disassociate-security-group-vpc \ --group-id``sg-04dbb43907d3f8a78`\ --vpc-id`vpc-0bf4c2739bc05a694`Output: `{ "State": "disassociating" }`For more information, see [Associate security groups with multiple VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/security-group-assoc.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [DisassociateSecurityGroupVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-security-group-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-subnet-cidr-block`.

- **AWS CLI**
- 
            
                    **To disassociate an IPv6 CIDR block from a subnet**This example disassociates an IPv6 CIDR block from a subnet using the association ID for the CIDR block. Command: `aws ec2 disassociate-subnet-cidr-block --association-id``subnet-cidr-assoc-3aa54053`Output: `{ "SubnetId": "subnet-5f46ec3b", "Ipv6CidrBlockAssociation": { "Ipv6CidrBlock": "2001:db8:1234:1a00::/64", "AssociationId": "subnet-cidr-assoc-3aa54053", "Ipv6CidrBlockState": { "State": "disassociating" } } }`- 
                    For API details, see [DisassociateSubnetCidrBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-subnet-cidr-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-transit-gateway-multicast-domain`.

- **AWS CLI**
- 
            
                    **To disassociate subnets from a multicast domain**The following `disassociate-transit-gateway-multicast-domain`example disassociates a subnet from the specified multicast domain.`aws ec2 disassociate-transit-gateway-multicast-domain \ --transit-gateway-attachment-id``tgw-attach-070e571cd1EXAMPLE`\ --subnet-id`subnet-000de86e3bEXAMPLE`\ --transit-gateway-multicast-domain-id`tgw-mcast-domain-0c4905cef7EXAMPLE`Output: `{ "Associations": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef7EXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-070e571cd1EXAMPLE", "ResourceId": "vpc-7EXAMPLE", "ResourceType": "vpc", "Subnets": [ { "SubnetId": "subnet-000de86e3bEXAMPLE", "State": "disassociating" } ] } }`For more information, see [Multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-domains-about.html)in the*Transit Gateways Guide*'.- 
                    For API details, see [DisassociateTransitGatewayMulticastDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-transit-gateway-multicast-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-transit-gateway-route-table`.

- **AWS CLI**
- 
            
                    **To disassociate a transit gateway route table from a resource attachment**The following `disassociate-transit-gateway-route-table`example disassociates the specified attachment from the transit gateway route table.`aws ec2 disassociate-transit-gateway-route-table \ --transit-gateway-route-table-id``tgw-rtb-002573ed1eEXAMPLE`\ --transit-gateway-attachment-id`tgw-attach-08e0bc912cEXAMPLE`Output: `{ "Association": { "TransitGatewayRouteTableId": "tgw-rtb-002573ed1eEXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-08e0bc912cEXAMPLE", "ResourceId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE", "ResourceType": "direct-connect-gateway", "State": "disassociating" } }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [DisassociateTransitGatewayRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-transit-gateway-route-table.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-vpc-cidr-block`.

- **AWS CLI**
- 
            
                    **To disassociate an IPv6 CIDR block from a VPC**This example disassociates an IPv6 CIDR block from a VPC using the association ID for the CIDR block. Command: `aws ec2 disassociate-vpc-cidr-block --association-id``vpc-cidr-assoc-eca54085`Output: `{ "Ipv6CidrBlockAssociation": { "Ipv6CidrBlock": "2001:db8:1234:1a00::/56", "AssociationId": "vpc-cidr-assoc-eca54085", "Ipv6CidrBlockState": { "State": "disassociating" } }, "VpcId": "vpc-a034d6c4" }`**To disassociate an IPv4 CIDR block from a VPC**This example disassociates an IPv4 CIDR block from a VPC. Command: `aws ec2 disassociate-vpc-cidr-block --association-id``vpc-cidr-assoc-0287ac6b`Output: `{ "CidrBlockAssociation": { "AssociationId": "vpc-cidr-assoc-0287ac6b", "CidrBlock": "172.18.0.0/16", "CidrBlockState": { "State": "disassociating" } }, "VpcId": "vpc-27621243" }`- 
                    For API details, see [DisassociateVpcCidrBlock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disassociate-vpc-cidr-block.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-address-transfer`.

- **AWS CLI**
- 
            
                    **To enable an Elastic IP address transfer**The following `enable-address-transfer`example enables Elastic IP address transfer for the specified Elastic IP address to the specified account.`aws ec2 enable-address-transfer \ --allocation-id``eipalloc-09ad461b0d03f6aaf`\ --transfer-account-id`123456789012`Output: `{ "AddressTransfer": { "PublicIp": "100.21.184.216", "AllocationId": "eipalloc-09ad461b0d03f6aaf", "TransferAccountId": "123456789012", "TransferOfferExpirationTimestamp": "2023-02-22T20:51:01.000Z", "AddressTransferStatus": "pending" } }`For more information, see [Transfer Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/WorkWithEIPs.html#transfer-EIPs-intro)in the*Amazon VPC User Guide*.- 
                    For API details, see [EnableAddressTransfer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-address-transfer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-aws-network-performance-metric-subscription`.

- **AWS CLI**
- 
            
                    **To enable a metric subscription**The following `enable-aws-network-performance-metric-subscription`example enables the monitoring of aggregate network latency between the specified source and destination Regions.`aws ec2 enable-aws-network-performance-metric-subscription \ --source``us-east-1`\ --destination`eu-west-1`\ --metric`aggregate-latency`\ --statistic`p50`Output: `{ "Output": true }`For more information, see [Manage subscriptions](https://docs.aws.amazon.com/network-manager/latest/infrastructure-performance/nmip-subscriptions-cw.html)in the*Infrastructure Performance User Guide*.- 
                    For API details, see [EnableAwsNetworkPerformanceMetricSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-aws-network-performance-metric-subscription.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-ebs-encryption-by-default`.

- **AWS CLI**
- 
            
                    **To enable EBS encryption by default**The following `enable-ebs-encryption-by-default`example enables EBS encryption by default for your AWS account in the current Region.`aws ec2 enable-ebs-encryption-by-default`Output: `{ "EbsEncryptionByDefault": true }`- 
                    For API details, see [EnableEbsEncryptionByDefault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-ebs-encryption-by-default.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-fast-launch`.

- **AWS CLI**
- 
            
                    **To start fast launching for an image**The following `enable-fast-launch`example configures the specified AMI for Fast Launch and sets the maximum number of parallel instances to launch to 6. The type of resource to use to pre-provision the AMI is set to`snapshot`, which is also the default value.`aws ec2 enable-fast-launch \ --image-id``ami-01234567890abcedf`\ --max-parallel-launches`6`\ --resource-type`snapshot`Output: `{ "ImageId": "ami-01234567890abcedf", "ResourceType": "snapshot", "SnapshotConfiguration": { "TargetResourceCount": 10 }, "LaunchTemplate": {}, "MaxParallelLaunches": 6, "OwnerId": "0123456789123", "State": "enabling", "StateTransitionReason": "Client.UserInitiated", "StateTransitionTime": "2022-01-27T22:16:03.199000+00:00" }`For more information, see [Configure EC2 Fast Launch settings for your Windows AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/win-fast-launch-configure.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [EnableFastLaunch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-launch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-fast-snapshot-restores`.

- **AWS CLI**
- 
            
                    **To enable fast snapshot restore**The following `enable-fast-snapshot-restores`example enables fast snapshot restore for the specified snapshot in the specified Availability Zones.`aws ec2 enable-fast-snapshot-restores \ --availability-zones``us-east-2a``us-east-2b`\ --source-snapshot-ids`snap-1234567890abcdef0`Output: `{ "Successful": [ { "SnapshotId": "snap-1234567890abcdef0" "AvailabilityZone": "us-east-2a", "State": "enabling", "StateTransitionReason": "Client.UserInitiated", "OwnerId": "123456789012", "EnablingTime": "2020-01-25T23:57:49.602Z" }, { "SnapshotId": "snap-1234567890abcdef0" "AvailabilityZone": "us-east-2b", "State": "enabling", "StateTransitionReason": "Client.UserInitiated", "OwnerId": "123456789012", "EnablingTime": "2020-01-25T23:57:49.596Z" } ], "Unsuccessful": [] }`- 
                    For API details, see [EnableFastSnapshotRestores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-snapshot-restores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-image-block-public-access`.

- **AWS CLI**
- 
            
                    **To enable block public access for AMIs in the specified Region**The following `enable-image-block-public-access`example enables block public access for AMIs at the account level in the specified Region.`aws ec2 enable-image-block-public-access \ --region``us-east-1`\ --image-block-public-access-state`block-new-sharing`Output: `{ "ImageBlockPublicAccessState": "block-new-sharing" }`For more information, see [Block public access to your AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-intro.html#block-public-access-to-amis)in the*Amazon EC2 User Guide*.- 
                    For API details, see [EnableImageBlockPublicAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-image-block-public-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-image-deprecation`.

- **AWS CLI**
- 
            
                    **To deprecate an AMI**The following `enable-image-deprecation`example deprecates an AMI on a specific date and time. If you specify a value for seconds, Amazon EC2 rounds the seconds to the nearest minute. You must be the AMI owner to perform this procedure.`aws ec2 enable-image-deprecation \ --image-id``ami-1234567890abcdef0`\ --deprecate-at '`2022-10-15T13:17:12.000Z`'Output: `{ "RequestID": "59dbff89-35bd-4eac-99ed-be587EXAMPLE", "Return": "true" }`For more information, see [Deprecate an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deprecate.html#deprecate-ami)in the*Amazon EC2 User Guide*.- 
                    For API details, see [EnableImageDeprecation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-image-deprecation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-image-deregistration-protection`.

- **AWS CLI**
- 
            
                    **To enable deregistration protection**The following `enable-image-deregistration-protection`example enables deregistration protection for the specified image.`aws ec2 enable-image-deregistration-protection \ --image-id``ami-0b1a928a144a74ec9`Output: `{ "Return": "enabled-without-cooldown" }`For more information, see [Protect an EC2 AMI from deregistration](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-deregistration-protection.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [EnableImageDeregistrationProtection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-image-deregistration-protection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-image`.

- **AWS CLI**
- 
            
                    **To enable an AMI**The following `enable-image`example enables the specified AMI.`aws ec2 enable-image \ --image-id``ami-1234567890abcdef0`Output: `{ "Return": "true" }`For more information, see [Disable an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/disable-an-ami.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [EnableImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-ipam-organization-admin-account`.

- **AWS CLI**
- 
            
                    **To integrate with AWS Organizations and delegate a member account as the IPAM account**The following `enable-ipam-organization-admin-account`example integrates IPAM with AWS Organizations and delegates a member account as the IPAM account.`aws ec2 enable-ipam-organization-admin-account \ --delegated-admin-account-id``320805250157`Output: `{ "Success": true }`For more information, see [Integrate IPAM with AWS Organizations](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [EnableIpamOrganizationAdminAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-ipam-organization-admin-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-reachability-analyzer-organization-sharing`.

- **AWS CLI**
- 
            
                    **To enable trusted access for Reachability Analyzer**The following `enable-reachability-analyzer-organization-sharing`example enables trusted access for Reachability Analyzer.`aws ec2 enable-reachability-analyzer-organization-sharing`This command produces no output. For more information, see [Cross-account analyses](https://docs.aws.amazon.com/vpc/latest/reachability/multi-account.html)in the*Reachability Analyzer User Guide*.- 
                    For API details, see [EnableReachabilityAnalyzerOrganizationSharing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-reachability-analyzer-organization-sharing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-serial-console-access`.

- **AWS CLI**
- 
            
                    **To enable access to the serial console for your account**The following `enable-serial-console-access`example enables account access to the serial console.`aws ec2 enable-serial-console-access`Output: `{ "SerialConsoleAccessEnabled": true }`For more information, see [EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [EnableSerialConsoleAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-serial-console-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-snapshot-block-public-access`.

- **AWS CLI**
- 
            
                    **To enable block public access for snapshots**The following `enable-snapshot-block-public-access`example blocks all public sharing of your snapshots.`aws ec2 enable-snapshot-block-public-access \ --state``block-all-sharing`Output: `{ "State": "block-all-sharing" }`For more information, see [Block public access for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [EnableSnapshotBlockPublicAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-snapshot-block-public-access.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-transit-gateway-route-table-propagation`.

- **AWS CLI**
- 
            
                    **To enable a transit gateway attachment to propagate routes to the specified propagation route table**The following `enable-transit-gateway-route-table-propagation`example enables the specified attachment to propagate routes to the specified propagation route table.`aws ec2 enable-transit-gateway-route-table-propagation \ --transit-gateway-route-table-id``tgw-rtb-0a823edbdeEXAMPLE`\ --transit-gateway-attachment-id`tgw-attach-09b52ccdb5EXAMPLE`Output: `{ "Propagation": { "TransitGatewayAttachmentId": "tgw-attach-09b52ccdb5EXAMPLE", "ResourceId": "vpc-4d7de228", "ResourceType": "vpc", "TransitGatewayRouteTableId": "tgw-rtb-0a823edbdeEXAMPLE", "State": "disabled" } }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [EnableTransitGatewayRouteTablePropagation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-transit-gateway-route-table-propagation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-vgw-route-propagation`.

- **AWS CLI**
- 
            
                    **To enable route propagation**This example enables the specified virtual private gateway to propagate static routes to the specified route table. If the command succeeds, no output is returned. Command: `aws ec2 enable-vgw-route-propagation --route-table-id``rtb-22574640`--gateway-id`vgw-9a4cacf3`- 
                    For API details, see [EnableVgwRoutePropagation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-vgw-route-propagation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-volume-io`.

- **AWS CLI**
- 
            
                    **To enable I/O for a volume**This example enables I/O on volume `vol-1234567890abcdef0`.Command: `aws ec2 enable-volume-io --volume-id``vol-1234567890abcdef0`Output: `{ "Return": true }`- 
                    For API details, see [EnableVolumeIo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-volume-io.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-vpc-classic-link-dns-support`.

- **AWS CLI**
- 
            
                    **To enable ClassicLink DNS support for a VPC**This example enables ClassicLink DNS support for `vpc-88888888`.Command: `aws ec2 enable-vpc-classic-link-dns-support --vpc-id``vpc-88888888`Output: `{ "Return": true }`- 
                    For API details, see [EnableVpcClassicLinkDnsSupport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-vpc-classic-link-dns-support.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-vpc-classic-link`.

- **AWS CLI**
- 
            
                    **To enable a VPC for ClassicLink**This example enables vpc-8888888 for ClassicLink. Command: `aws ec2 enable-vpc-classic-link --vpc-id``vpc-88888888`Output: `{ "Return": true }`- 
                    For API details, see [EnableVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-vpc-classic-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `export-client-vpn-client-certificate-revocation-list`.

- **AWS CLI**
- 
            
                    **To export a client certificate revocation list**The following `export-client-vpn-client-certificate-revocation-list`example exports the client certificate revocation list for the specified Client VPN endpoint. In this example, the output is returned in text format to make it easier to read.`aws ec2 export-client-vpn-client-certificate-revocation-list \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --output`text`Output: `-----BEGIN X509 CRL----- MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END X509 CRL----- STATUS pending`For more information, see [Client Certificate Revocation Lists](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [ExportClientVpnClientCertificateRevocationList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-client-vpn-client-certificate-revocation-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `export-client-vpn-client-configuration`.

- **AWS CLI**
- 
            
                    **To export the client configuration**The following `export-client-vpn-client-configuration`example exports the client configuration for the specified Client VPN endpoint. In this example, the output is returned in text format to make it easier to read.`aws ec2 export-client-vpn-client-configuration \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --output`text`Output: `client dev tun proto udp remote cvpn-endpoint-123456789123abcde.prod.clientvpn.ap-south-1.amazonaws.com 443 remote-random-hostname resolv-retry infinite nobind persist-key persist-tun remote-cert-tls server cipher AES-256-GCM verb 3 <ca> -----BEGIN CERTIFICATE----- MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END CERTIFICATE----- </ca> reneg-sec 0`For more information, see [Client VPN endpoint configuration file export](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoint-export.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [ExportClientVpnClientConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-client-vpn-client-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `export-image`.

- **AWS CLI**
- 
            
                    **To export a VM from an AMI**The following `export-image`example exports the specified AMI to the specified bucket in the specified format.`aws ec2 export-image \ --image-id``ami-1234567890abcdef0`\ --disk-image-format`VMDK`\ --s3-export-location`S3Bucket=my-export-bucket,S3Prefix=exports/`Output: `{ "DiskImageFormat": "vmdk", "ExportImageTaskId": "export-ami-1234567890abcdef0" "ImageId": "ami-1234567890abcdef0", "RoleName": "vmimport", "Progress": "0", "S3ExportLocation": { "S3Bucket": "my-export-bucket", "S3Prefix": "exports/" }, "Status": "active", "StatusMessage": "validating" }`- 
                    For API details, see [ExportImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/export-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-associated-ipv6-pool-cidrs`.

- **AWS CLI**
- 
            
                    **To get the associations for an IPv6 address pool**The following `get-associated-ipv6-pool-cidrs`example gets the associations for the specified IPv6 address pool.`aws ec2 get-associated-ipv6-pool-cidrs \ --pool-id``ipv6pool-ec2-012345abc12345abc`Output: `{ "Ipv6CidrAssociations": [ { "Ipv6Cidr": "2001:db8:1234:1a00::/56", "AssociatedResource": "vpc-111111222222333ab" } ] }`- 
                    For API details, see [GetAssociatedIpv6PoolCidrs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-associated-ipv6-pool-cidrs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-aws-network-performance-data`.

- **AWS CLI**
- 
            
                    **To get network performance data**The following `get-aws-network-performance-data`example retrieves data about the network performance between the specified Regions in the specified time period.`aws ec2 get-aws-network-performance-data \ --start-time``2022-10-26T12:00:00.000Z`\ --end-time`2022-10-26T12:30:00.000Z`\ --data-queries`Id=my-query,Source=us-east-1,Destination=eu-west-1,Metric=aggregate-latency,Statistic=p50,Period=five-minutes`Output: `{ "DataResponses": [ { "Id": "my-query", "Source": "us-east-1", "Destination": "eu-west-1", "Metric": "aggregate-latency", "Statistic": "p50", "Period": "five-minutes", "MetricPoints": [ { "StartDate": "2022-10-26T12:00:00+00:00", "EndDate": "2022-10-26T12:05:00+00:00", "Value": 62.44349, "Status": "OK" }, { "StartDate": "2022-10-26T12:05:00+00:00", "EndDate": "2022-10-26T12:10:00+00:00", "Value": 62.483498, "Status": "OK" }, { "StartDate": "2022-10-26T12:10:00+00:00", "EndDate": "2022-10-26T12:15:00+00:00", "Value": 62.51248, "Status": "OK" }, { "StartDate": "2022-10-26T12:15:00+00:00", "EndDate": "2022-10-26T12:20:00+00:00", "Value": 62.635475, "Status": "OK" }, { "StartDate": "2022-10-26T12:20:00+00:00", "EndDate": "2022-10-26T12:25:00+00:00", "Value": 62.733974, "Status": "OK" }, { "StartDate": "2022-10-26T12:25:00+00:00", "EndDate": "2022-10-26T12:30:00+00:00", "Value": 62.773975, "Status": "OK" }, { "StartDate": "2022-10-26T12:30:00+00:00", "EndDate": "2022-10-26T12:35:00+00:00", "Value": 62.75349, "Status": "OK" } ] } ] }`For more information, see [Monitor network performance](https://docs.aws.amazon.com/network-manager/latest/infrastructure-performance/nmip-performance-cli.html)in the*Infrastructure Performance User Guide*.- 
                    For API details, see [GetAwsNetworkPerformanceData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-aws-network-performance-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-capacity-reservation-usage`.

- **AWS CLI**
- 
            
                    **To view capacity reservation usage across AWS accounts**The following `get-capacity-reservation-usage`example displays usage information for the specified capacity reservation.`aws ec2 get-capacity-reservation-usage \ --capacity-reservation-id``cr-1234abcd56EXAMPLE`Output: `{ "CapacityReservationId": "cr-1234abcd56EXAMPLE ", "InstanceUsages": [ { "UsedInstanceCount": 1, "AccountId": "123456789012" } ], "AvailableInstanceCount": 4, "TotalInstanceCount": 5, "State": "active", "InstanceType": "t2.medium" }`For more information, see [Shared Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservation-sharing.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetCapacityReservationUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-capacity-reservation-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-coip-pool-usage`.

- **AWS CLI**
- 
            
                    **To get customer-owned IP address pool usage**The following `get-coip-pool-usage`example gets the usage details for the specified customer-owned IP address pool.`aws ec2 get-coip-pool-usage \ --pool-id``ipv4pool-coip-123a45678bEXAMPLE`Output: `{ "CoipPoolId": "ipv4pool-coip-123a45678bEXAMPLE", "CoipAddressUsages": [ { "CoIp": "0.0.0.0" }, { "AllocationId": "eipalloc-123ab45c6dEXAMPLE", "AwsAccountId": "123456789012", "CoIp": "0.0.0.0" }, { "AllocationId": "eipalloc-123ab45c6dEXAMPLE", "AwsAccountId": "123456789111", "CoIp": "0.0.0.0" } ], "LocalGatewayRouteTableId": "lgw-rtb-059615ef7dEXAMPLE" }`For more information, see [Customer-owned IP addresses](https://docs.aws.amazon.com/outposts/latest/userguide/routing.html#ip-addressing)in the*AWS Outposts User Guide for Outposts racks*.- 
                    For API details, see [GetCoipPoolUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-coip-pool-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-console-output`.

- **AWS CLI**
- 
            
                    **Example 1: To get the console output**The following `get-console-output`example gets the console output for the specified Linux instance.`aws ec2 get-console-output \ --instance-id``i-1234567890abcdef0`Output: `{ "InstanceId": "i-1234567890abcdef0", "Timestamp": "2013-07-25T21:23:53.000Z", "Output": "..." }`For more information, see [Instance console output](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html#instance-console-console-output)in the*Amazon EC2 User Guide*.**Example 2: To get the latest console output**The following `get-console-output`example gets the latest console output for the specified Linux instance.`aws ec2 get-console-output \ --instance-id``i-1234567890abcdef0`\ --latest \ --output`text`Output: `i-1234567890abcdef0 [ 0.000000] Command line: root=LABEL=/ console=tty1 console=ttyS0 selinux=0 nvme_core.io_timeout=4294967295 [ 0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers' [ 0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers' [ 0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers' ... Cloud-init v. 0.7.6 finished at Wed, 09 May 2018 19:01:13 +0000. Datasource DataSourceEc2. Up 21.50 seconds Amazon Linux AMI release 2018.03 Kernel 4.14.26-46.32.amzn1.x`For more information, see [Instance console output](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-console.html#instance-console-console-output)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetConsoleOutput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-console-output.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-console-screenshot`.

- **AWS CLI**
- 
            
                    **To retrieve a screenshot of a running instance**The following `get-console-screenshot`example retrieves a screenshot of the specified instance in .jpg format. The screenshot is returned as a Base64-encoded string.`aws ec2 get-console-screenshot \ --instance-id``i-1234567890abcdef0`Output: `{ "ImageData": "997987/8kgj49ikjhewkwwe0008084EXAMPLE", "InstanceId": "i-1234567890abcdef0" }`- 
                    For API details, see [GetConsoleScreenshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-console-screenshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-default-credit-specification`.

- **AWS CLI**
- 
            
                    **To describe the default credit option**The following `get-default-credit-specification`example describes the default credit option for T2 instances.`aws ec2 get-default-credit-specification \ --instance-family``t2`Output: `{ "InstanceFamilyCreditSpecification": { "InstanceFamily": "t2", "CpuCredits": "standard" } }`- 
                    For API details, see [GetDefaultCreditSpecification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-default-credit-specification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ebs-default-kms-key-id`.

- **AWS CLI**
- 
            
                    **To describe your default CMK for EBS encryption**The following `get-ebs-default-kms-key-id`example describes the default CMK for EBS encryption for your AWS account.`aws ec2 get-ebs-default-kms-key-id`The output shows the default CMK for EBS encryption, which is an AWS managed CMK with the alias `alias/aws/ebs`.`{ "KmsKeyId": "alias/aws/ebs" }`The following output shows a custom CMK for EBS encryption. `{ "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/0ea3fef3-80a7-4778-9d8c-1c0c6EXAMPLE" }`- 
                    For API details, see [GetEbsDefaultKmsKeyId](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ebs-default-kms-key-id.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ebs-encryption-by-default`.

- **AWS CLI**
- 
            
                    **To describe whether EBS encryption by default is enabled**The following `get-ebs-encryption-by-default`example indicates whether EBS encryption by default is enabled for your AWS account in the current Region.`aws ec2 get-ebs-encryption-by-default`The following output indicates that EBS encryption by default is disabled. `{ "EbsEncryptionByDefault": false }`The following output indicates that EBS encryption by default is enabled. `{ "EbsEncryptionByDefault": true }`- 
                    For API details, see [GetEbsEncryptionByDefault](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ebs-encryption-by-default.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-flow-logs-integration-template`.

- **AWS CLI**
- 
            
                    **To create a CloudFormation template to automate the integration of VPC flow logs with Amazon Athena**The following `get-flow-logs-integration-template`examples create a CloudFormation template to automate the integration of VPC flow logs with Amazon Athena.Linux: `aws ec2 get-flow-logs-integration-template \ --flow-log-id``fl-1234567890abcdef0`\ --config-delivery-s3-destination-arn`arn:aws:s3:::amzn-s3-demo-bucket`\ --integrate-services AthenaIntegrations='[{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00},{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00}]'Windows: `aws ec2 get-flow-logs-integration-template``^`--flow-log-id`fl-1234567890abcdef0``^`--config-delivery-s3-destination-arn`arn:aws:s3:::amzn-s3-demo-bucket``^`--integrate-services`AthenaIntegrations=[{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00},{IntegrationResultS3DestinationArn=arn:aws:s3:::amzn-s3-demo-bucket,PartitionLoadFrequency=none,PartitionStartDate=2021-07-21T00:40:00,PartitionEndDate=2021-07-21T00:42:00}]`Output: `{ "Result": "https://amzn-s3-demo-bucket.s3.us-east-2.amazonaws.com/VPCFlowLogsIntegrationTemplate_fl-1234567890abcdef0_Wed%20Jul%2021%2000%3A57%3A56%20UTC%202021.yml" }`For information on using CloudFormation templates, see [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html)in the*AWS CloudFormation User Guide*.For information on using Amazon Athena and flow logs, see [Query flow logs using Amazon Athena](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs-athena.html)in the*Amazon Virtual Private Cloud User Guide*.- 
                    For API details, see [GetFlowLogsIntegrationTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-flow-logs-integration-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-groups-for-capacity-reservation`.

- **AWS CLI**
- 
            
                    **To list the resource groups with a Capacity Reservation**The following `get-groups-for-capacity-reservation`example lists the resource groups to which the specified Capacity Reservation was added.`aws ec2 get-groups-for-capacity-reservation \ --capacity-reservation-id``cr-1234abcd56EXAMPLE`Output: `{ "CapacityReservationsGroup": [ { "GroupArn": "arn:aws:resource-groups:us-west-2:123456789012:group/my-resource-group", "OwnerId": "123456789012" } ] }`For more information, see [Capacity Reservation groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cr-group.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetGroupsForCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-groups-for-capacity-reservation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-host-reservation-purchase-preview`.

- **AWS CLI**
- 
            
                    **To get a purchase preview for a Dedicated Host Reservation**This example provides a preview of the costs for a specified Dedicated Host Reservation for the specified Dedicated Host in your account. Command: `aws ec2 get-host-reservation-purchase-preview --offering-id``hro-03f707bf363b6b324`--host-id-set`h-013abcd2a00cbd123`Output: `{ "TotalHourlyPrice": "1.499", "Purchase": [ { "HourlyPrice": "1.499", "InstanceFamily": "m4", "PaymentOption": "NoUpfront", "HostIdSet": [ "h-013abcd2a00cbd123" ], "UpfrontPrice": "0.000", "Duration": 31536000 } ], "TotalUpfrontPrice": "0.000" }`- 
                    For API details, see [GetHostReservationPurchasePreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-host-reservation-purchase-preview.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image-block-public-access-state`.

- **AWS CLI**
- 
            
                    **To get the block public access state for AMIs in the specified Region**The following `get-image-block-public-access-state`example gets the block public access state for AMIs at the account level in the specified Region.`aws ec2 get-image-block-public-access-state \ --region``us-east-1`Output: `{ "ImageBlockPublicAccessState": "block-new-sharing" }`For more information, see [Block public access to your AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-intro.html#block-public-access-to-amis)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetImageBlockPublicAccessState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-image-block-public-access-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-types-from-instance-requirements`.

- **AWS CLI**
- 
            
                    **To preview the instance types that match specified attributes**The following `get-instance-types-from-instance-requirements`example first generates a list of all of the possible attributes that can be specified using the`--generate-cli-skeleton`parameter, and saves the list to a JSON file. Then, the JSON file is used to customize the attributes for which to preview matched instance types.To generate all possible attributes and save the output directly to a JSON file, use the following command. `aws ec2 get-instance-types-from-instance-requirements \ --region``us-east-1`\ --generate-cli-skeleton`input``>``attributes.json`Output: `{ "DryRun": true, "ArchitectureTypes": [ "x86_64_mac" ], "VirtualizationTypes": [ "paravirtual" ], "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 0 }, "MemoryMiB": { "Min": 0, "Max": 0 }, "CpuManufacturers": [ "intel" ], "MemoryGiBPerVCpu": { "Min": 0.0, "Max": 0.0 }, "ExcludedInstanceTypes": [ "" ], "InstanceGenerations": [ "current" ], "SpotMaxPricePercentageOverLowestPrice": 0, "OnDemandMaxPricePercentageOverLowestPrice": 0, "BareMetal": "included", "BurstablePerformance": "excluded", "RequireHibernateSupport": true, "NetworkInterfaceCount": { "Min": 0, "Max": 0 }, "LocalStorage": "required", "LocalStorageTypes": [ "hdd" ], "TotalLocalStorageGB": { "Min": 0.0, "Max": 0.0 }, "BaselineEbsBandwidthMbps": { "Min": 0, "Max": 0 }, "AcceleratorTypes": [ "inference" ], "AcceleratorCount": { "Min": 0, "Max": 0 }, "AcceleratorManufacturers": [ "xilinx" ], "AcceleratorNames": [ "t4" ], "AcceleratorTotalMemoryMiB": { "Min": 0, "Max": 0 } }, "MaxResults": 0, "NextToken": "" }`Configure the JSON file. You must provide values for `ArchitectureTypes`,`VirtualizationTypes`,`VCpuCount`, and`MemoryMiB`. You can omit the other attributes. When omitted, default values are used. For a description of each attribute and their default values, see get-instance-types-from-instance-requirements <https://docs.aws.amazon.com/cli/latest/reference/ec2/get-instance-types-from-instance-requirements.html>.Preview the instance types that have the attributes specified in `attributes.json`. Specify the name and path to your JSON file by using the`--cli-input-json`parameter. In the following request, the output is formatted as a table.`aws ec2 get-instance-types-from-instance-requirements \ --cli-input-json``file://attributes.json`\ --output`table`Contents of `attributes.json`file:`{ "ArchitectureTypes": [ "x86_64" ], "VirtualizationTypes": [ "hvm" ], "InstanceRequirements": { "VCpuCount": { "Min": 4, "Max": 6 }, "MemoryMiB": { "Min": 2048 }, "InstanceGenerations": [ "current" ] } }`Output: `------------------------------------------ |GetInstanceTypesFromInstanceRequirements| +----------------------------------------+ || InstanceTypes || |+--------------------------------------+| || InstanceType || |+--------------------------------------+| || c4.xlarge || || c5.xlarge || || c5a.xlarge || || c5ad.xlarge || || c5d.xlarge || || c5n.xlarge || || d2.xlarge || ...`For more information about attribute-based instance type selection, see [How attribute-based instance type selection works](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abs-how-it-works)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetInstanceTypesFromInstanceRequirements](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-instance-types-from-instance-requirements.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-uefi-data`.

- **AWS CLI**
- 
            
                    **To retrieve UEFI data from an instance**The following `get-instance-uefi-data`example retrieves UEFI data from an instance. If the output is empty, the instance does not contain UEFI data.`aws ec2 get-instance-uefi-data \ --instance-id``i-0123456789example`Output: `{ "InstanceId": "i-0123456789example", "UefiData": "QU1aTlVFRkkf+uLXAAAAAHj5a7fZ9+3dBzxXb/. <snipped> AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD4L/J/AODshho=" }`For more information, see [UEFI Secure Boot](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetInstanceUefiData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-instance-uefi-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ipam-address-history`.

- **AWS CLI**
- 
            
                    **To get the history of a CIDR**The following `get-ipam-address-history`example gets the history of a CIDR.(Linux): `aws ec2 get-ipam-address-history \ --cidr``10.0.0.0/16`\ --ipam-scope-id`ipam-scope-02fc38cd4c48e7d38`\ --start-time`2021-12-08T01:00:00.000Z`\ --end-time`2021-12-10T01:00:00.000Z`(Windows): `aws ec2 get-ipam-address-history``^`--cidr`10.0.0.0/16``^`--ipam-scope-id`ipam-scope-02fc38cd4c48e7d38``^`--start-time`2021-12-08T01:00:00.000Z``^`--end-time`2021-12-10T01:00:00.000Z`Output: `{ "HistoryRecords": [ { "ResourceOwnerId": "123456789012", "ResourceRegion": "us-west-1", "ResourceType": "vpc", "ResourceId": "vpc-06cbefa9ee907e1c0", "ResourceCidr": "10.0.0.0/16", "ResourceName": "Demo", "ResourceComplianceStatus": "unmanaged", "ResourceOverlapStatus": "overlapping", "VpcId": "vpc-06cbefa9ee907e1c0", "SampledStartTime": "2021-12-08T19:54:57.675000+00:00" }, { "ResourceOwnerId": "123456789012", "ResourceRegion": "us-east-2", "ResourceType": "vpc", "ResourceId": "vpc-042702f474812c9ad", "ResourceCidr": "10.0.0.0/16", "ResourceName": "test", "ResourceComplianceStatus": "unmanaged", "ResourceOverlapStatus": "overlapping", "VpcId": "vpc-042702f474812c9ad", "SampledStartTime": "2021-12-08T19:54:59.019000+00:00" }, { "ResourceOwnerId": "123456789012", "ResourceRegion": "us-east-2", "ResourceType": "vpc", "ResourceId": "vpc-042b8a44f64267d67", "ResourceCidr": "10.0.0.0/16", "ResourceName": "tester", "ResourceComplianceStatus": "unmanaged", "ResourceOverlapStatus": "overlapping", "VpcId": "vpc-042b8a44f64267d67", "SampledStartTime": "2021-12-08T19:54:59.019000+00:00" } ] }`For more information, see [View the history of IP addresses](https://docs.aws.amazon.com/vpc/latest/ipam/view-history-cidr-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [GetIpamAddressHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-address-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ipam-discovered-accounts`.

- **AWS CLI**
- 
            
                    **To view the accounts discovered by an IPAM**In this scenario, you're a IPAM delegated admin who wants to view the AWS accounts that own resources that the IPAM is discovering. The `--discovery-region`is the IPAM operating Region you want to view the monitored account statuses in. For example, if you have three IPAM operating Regions, you may want to make this request three times to view the timestamps specific to discovery in each of those particular Regions.The following `get-ipam-discovered-accounts`example lists the AWS accounts that own resources that the IPAM is discovering.`aws ec2 get-ipam-discovered-accounts \ --ipam-resource-discovery-id``ipam-res-disco-0365d2977fc1672fe`\ --discovery-region`us-east-1`Output: `{ "IpamDiscoveredAccounts": [ { "AccountId": "149977607591", "DiscoveryRegion": "us-east-1", "LastAttemptedDiscoveryTime": "2024-02-09T19:04:31.379000+00:00", "LastSuccessfulDiscoveryTime": "2024-02-09T19:04:31.379000+00:00" } ] }`For more information, see [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [GetIpamDiscoveredAccounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-discovered-accounts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ipam-discovered-public-addresses`.

- **AWS CLI**
- 
            
                    **To view discovered public IP addresses**In this example, you are an IPAM delegated admin and you want to view the IP addresses of resources discovered by IPAM. You can get the resource discovery ID with [describe-ipam-resource-discoveries](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-resource-discoveries.html).The following `get-ipam-discovered-public-addresses`example shows the discovered public IP addresses for a resource discovery.`aws ec2 get-ipam-discovered-public-addresses \ --ipam-resource-discovery-id``ipam-res-disco-0f4ef577a9f37a162`\ --address-region`us-east-1`\ --region`us-east-1`Output: `{ "IpamDiscoveredPublicAddresses": [ { "IpamResourceDiscoveryId": "ipam-res-disco-0f4ef577a9f37a162", "AddressRegion": "us-east-1", "Address": "54.208.155.7", "AddressOwnerId": "320805250157", "AssociationStatus": "associated", "AddressType": "ec2-public-ip", "VpcId": "vpc-073b294916198ce49", "SubnetId": "subnet-0b6c8a8839e9a4f15", "NetworkInterfaceId": "eni-081c446b5284a5e06", "NetworkInterfaceDescription": "", "InstanceId": "i-07459a6fca5b35823", "Tags": {}, "NetworkBorderGroup": "us-east-1c", "SecurityGroups": [ { "GroupName": "launch-wizard-2", "GroupId": "sg-0a489dd6a65c244ce" } ], "SampleTime": "2024-04-05T15:13:59.228000+00:00" }, { "IpamResourceDiscoveryId": "ipam-res-disco-0f4ef577a9f37a162", "AddressRegion": "us-east-1", "Address": "44.201.251.218", "AddressOwnerId": "470889052923", "AssociationStatus": "associated", "AddressType": "ec2-public-ip", "VpcId": "vpc-6c31a611", "SubnetId": "subnet-062f47608b99834b1", "NetworkInterfaceId": "eni-024845359c2c3ae9b", "NetworkInterfaceDescription": "", "InstanceId": "i-04ef786d9c4e03f41", "Tags": {}, "NetworkBorderGroup": "us-east-1a", "SecurityGroups": [ { "GroupName": "launch-wizard-32", "GroupId": "sg-0ed1a426e96a68374" } ], "SampleTime": "2024-04-05T15:13:59.145000+00:00" } }`For more information, see [View public IP insights](https://docs.aws.amazon.com/vpc/latest/ipam/view-public-ip-insights.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [GetIpamDiscoveredPublicAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-discovered-public-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ipam-discovered-resource-cidrs`.

- **AWS CLI**
- 
            
                    **To view the IP address CIDRs discovered by an IPAM**In this example, you're a IPAM delegated admin who wants to view details related to the IP address CIDRs for resources that the IPAM is discovering. To complete this request: The resource discovery you choose must be associated with the IPAM.The `--resource-region`is the AWS Region where resource was created.The following `get-ipam-discovered-resource-cidrs`example lists the IP addresses for resources that the IPAM is discovering.`aws ec2 get-ipam-discovered-resource-cidrs \ --ipam-resource-discovery-id``ipam-res-disco-0365d2977fc1672fe`\ --resource-region`us-east-1`Output: `{ { "IpamDiscoveredResourceCidrs": [ { "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe", "ResourceRegion": "us-east-1", "ResourceId": "vpc-0c974c95ca7ceef4a", "ResourceOwnerId": "149977607591", "ResourceCidr": "172.31.0.0/16", "ResourceType": "vpc", "ResourceTags": [], "IpUsage": 0.375, "VpcId": "vpc-0c974c95ca7ceef4a", "SampleTime": "2024-02-09T19:15:16.529000+00:00" }, { "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe", "ResourceRegion": "us-east-1", "ResourceId": "subnet-07fe028119082a8c1", "ResourceOwnerId": "149977607591", "ResourceCidr": "172.31.0.0/20", "ResourceType": "subnet", "ResourceTags": [], "IpUsage": 0.0012, "VpcId": "vpc-0c974c95ca7ceef4a", "SampleTime": "2024-02-09T19:15:16.529000+00:00" }, { "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe", "ResourceRegion": "us-east-1", "ResourceId": "subnet-0a96893763984cc4e", "ResourceOwnerId": "149977607591", "ResourceCidr": "172.31.64.0/20", "ResourceType": "subnet", "ResourceTags": [], "IpUsage": 0.0012, "VpcId": "vpc-0c974c95ca7ceef4a", "SampleTime": "2024-02-09T19:15:16.529000+00:00" } } }`For more information, see [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [GetIpamDiscoveredResourceCidrs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-discovered-resource-cidrs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ipam-pool-allocations`.

- **AWS CLI**
- 
            
                    **To get the CIDRs allocated from an IPAM pool**The following `get-ipam-pool-allocations`example gets the CIDRs allocated from an IPAM pool.(Linux): `aws ec2 get-ipam-pool-allocations \ --ipam-pool-id``ipam-pool-0533048da7d823723`\ --filters`Name=ipam-pool-allocation-id,Values=ipam-pool-alloc-0e6186d73999e47389266a5d6991e6220`(Windows): `aws ec2 get-ipam-pool-allocations``^`--ipam-pool-id`ipam-pool-0533048da7d823723``^`--filters`Name=ipam-pool-allocation-id,Values=ipam-pool-alloc-0e6186d73999e47389266a5d6991e6220`Output: `{ "IpamPoolAllocations": [ { "Cidr": "10.0.0.0/16", "IpamPoolAllocationId": "ipam-pool-alloc-0e6186d73999e47389266a5d6991e6220", "ResourceType": "custom", "ResourceOwner": "123456789012" } ] }`- 
                    For API details, see [GetIpamPoolAllocations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-pool-allocations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ipam-pool-cidrs`.

- **AWS CLI**
- 
            
                    **To get the CIDRs provisioned to an IPAM pool**The following `get-ipam-pool-cidrs`example gets the CIDRs provisioned to an IPAM pool.(Linux): `aws ec2 get-ipam-pool-cidrs \ --ipam-pool-id``ipam-pool-0533048da7d823723`\ --filters '`Name=cidr,Values=10.*`'(Windows): `aws ec2 get-ipam-pool-cidrs``^`--ipam-pool-id`ipam-pool-0533048da7d823723``^`--filters`Name=cidr,Values=10.*`Output: `{ "IpamPoolCidr": { "Cidr": "10.0.0.0/24", "State": "provisioned" } }`- 
                    For API details, see [GetIpamPoolCidrs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-pool-cidrs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-ipam-resource-cidrs`.

- **AWS CLI**
- 
            
                    **To get the CIDRs allocated to a resource**The following `get-ipam-resource-cidrs`example gets the CIDRs allocated to a resource.(Linux): `aws ec2 get-ipam-resource-cidrs \ --ipam-scope-id``ipam-scope-02fc38cd4c48e7d38`\ --filters`Name=management-state,Values=unmanaged`(Windows): `aws ec2 get-ipam-resource-cidrs``^`--ipam-scope-id`ipam-scope-02fc38cd4c48e7d38``^`--filters`Name=management-state,Values=unmanaged`Output: `{ "IpamResourceCidrs": [ { "IpamId": "ipam-08440e7a3acde3908", "IpamScopeId": "ipam-scope-02fc38cd4c48e7d38", "ResourceRegion": "us-east-2", "ResourceOwnerId": "123456789012", "ResourceId": "vpc-621b8709", "ResourceName": "Default AWS VPC", "ResourceCidr": "172.33.0.0/16", "ResourceType": "vpc", "ResourceTags": [ { "Key": "Environment", "Value": "Test" }, { "Key": "Name", "Value": "Default AWS VPC" } ], "IpUsage": 0.0039, "ComplianceStatus": "unmanaged", "ManagementState": "unmanaged", "OverlapStatus": "nonoverlapping", "VpcId": "vpc-621b8709" } ] }`For more information, see [Monitor CIDR usage by resource](https://docs.aws.amazon.com/vpc/latest/ipam/monitor-cidr-compliance-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [GetIpamResourceCidrs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-ipam-resource-cidrs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-launch-template-data`.

- **AWS CLI**
- 
            
                    **To get instance data for a launch template**This example gets data about the specified instance and uses the `--query`option to return the contents in`LaunchTemplateData`. You can use the output as a base to create a new launch template or launch template version.Command: `aws ec2 get-launch-template-data --instance-id``i-0123d646e8048babc`--query '`LaunchTemplateData`'Output: `{ "Monitoring": {}, "ImageId": "ami-8c1be5f6", "BlockDeviceMappings": [ { "DeviceName": "/dev/xvda", "Ebs": { "DeleteOnTermination": true } } ], "EbsOptimized": false, "Placement": { "Tenancy": "default", "GroupName": "", "AvailabilityZone": "us-east-1a" }, "InstanceType": "t2.micro", "NetworkInterfaces": [ { "Description": "", "NetworkInterfaceId": "eni-35306abc", "PrivateIpAddresses": [ { "Primary": true, "PrivateIpAddress": "10.0.0.72" } ], "SubnetId": "subnet-7b16de0c", "Groups": [ "sg-7c227019" ], "Ipv6Addresses": [ { "Ipv6Address": "2001:db8:1234:1a00::123" } ], "PrivateIpAddress": "10.0.0.72" } ] }`- 
                    For API details, see [GetLaunchTemplateData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-launch-template-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-managed-prefix-list-associations`.

- **AWS CLI**
- 
            
                    **To get prefix list associations**The following `get-managed-prefix-list-associations`example gets the resources that are associated with the specified prefix list.`aws ec2 get-managed-prefix-list-associations \ --prefix-list-id``pl-0123456abcabcabc1`Output: `{ "PrefixListAssociations": [ { "ResourceId": "sg-0abc123456abc12345", "ResourceOwner": "123456789012" } ] }`For more information, see [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [GetManagedPrefixListAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-managed-prefix-list-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-managed-prefix-list-entries`.

- **AWS CLI**
- 
            
                    **To get the entries for a prefix list**The following `get-managed-prefix-list-entries`gets the entries for the specified prefix list.`aws ec2 get-managed-prefix-list-entries \ --prefix-list-id``pl-0123456abcabcabc1`Output: `{ "Entries": [ { "Cidr": "10.0.0.0/16", "Description": "vpc-a" }, { "Cidr": "10.2.0.0/16", "Description": "vpc-b" } ] }`For more information, see [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [GetManagedPrefixListEntries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-managed-prefix-list-entries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-network-insights-access-scope-analysis-findings`.

- **AWS CLI**
- 
            
                    **To get the findings of Network Insights access scope analysis**The following `get-network-insights-access-scope-analysis-findings`example gets the selected scope analysis findings in your AWS account.`aws ec2 get-network-insights-access-scope-analysis-findings \ --region``us-east-1`\ --network-insights-access-scope-analysis-id`nis`\ --nis-123456789111Output: `{ "NetworkInsightsAccessScopeAnalysisId": "nisa-123456789222", "AnalysisFindings": [ { "NetworkInsightsAccessScopeAnalysisId": "nisa-123456789222", "NetworkInsightsAccessScopeId": "nis-123456789111", "FindingComponents": [ { "SequenceNumber": 1, "Component": { "Id": "eni-02e3d42d5cceca67d", "Arn": "arn:aws:ec2:us-east-1:936459623503:network-interface/eni-02e3d32d9cceca17d" }, "OutboundHeader": { "DestinationAddresses": [ "0.0.0.0/5", "11.0.0.0/8", "12.0.0.0/6", "128.0.0.0/3", "16.0.0.0/4", "160.0.0.0/5", "168.0.0.0/6", "172.0.0.0/12" "8.0.0.0/7" ], "DestinationPortRanges": [ { "From": 0, "To": 65535 } ], "Protocol": "6", "SourceAddresses": [ "10.0.2.253/32" ], "SourcePortRanges": [ { "From": 0, "To": 65535 } ] }, [etc] ] } } ] }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [GetNetworkInsightsAccessScopeAnalysisFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-network-insights-access-scope-analysis-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-network-insights-access-scope-content`.

- **AWS CLI**
- 
            
                    **To get Network Insights access scope content**The following `get-network-insights-access-scope-content`example gets the content of the selected scope analysis ID in your AWS account.`aws ec2 get-network-insights-access-scope-content \ --region``us-east-1`\ --network-insights-access-scope-id`nis-123456789222`Output: `{ "NetworkInsightsAccessScopeContent": { "NetworkInsightsAccessScopeId": "nis-123456789222", "MatchPaths": [ { "Source": { "ResourceStatement": { "ResourceTypes": [ "AWS::EC2::NetworkInterface" ] } }, "Destination": { "ResourceStatement": { "ResourceTypes": [ "AWS::EC2::InternetGateway" ] } } } ] } }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [GetNetworkInsightsAccessScopeContent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-network-insights-access-scope-content.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-password-data`.

- **AWS CLI**
- 
            
                    **To get the encrypted password**This example gets the encrypted password. Command: `aws ec2 get-password-data --instance-id``i-1234567890abcdef0`Output: `{ "InstanceId": "i-1234567890abcdef0", "Timestamp": "2013-08-07T22:18:38.000Z", "PasswordData": "gSlJFq+VpcZXqy+iktxMF6NyxQ4qCrT4+gaOuNOenX1MmgXPTj7XEXAMPLE UQ+YeFfb+L1U4C4AKv652Ux1iRB3CPTYP7WmU3TUnhsuBd+p6LVk7T2lKUml6OXbk6WPW1VYYm/TRPB1 e1DQ7PY4an/DgZT4mwcpRFigzhniQgDDeO1InvSDcwoUTwNs0Y1S8ouri2W4n5GNlriM3Q0AnNVelVz/ 53TkDtxbNoU606M1gK9zUWSxqEgwvbV2j8c5rP0WCuaMWSFl4ziDu4bd7q+4RSyi8NUsVWnKZ4aEZffu DPGzKrF5yLlf3etP2L4ZR6CvG7K1hx7VKOQVN32Dajw==" }`**To get the decrypted password**This example gets the decrypted password. Command: `aws ec2 get-password-data --instance-id``i-1234567890abcdef0`--priv-launch-key C:\Keys\MyKeyPair.pemOutput: `{ "InstanceId": "i-1234567890abcdef0", "Timestamp": "2013-08-30T23:18:05.000Z", "PasswordData": "&ViJ652e*u" }`- 
                    For API details, see [GetPasswordData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-password-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reserved-instances-exchange-quote`.

- **AWS CLI**
- 
            
                    **To get a quote for exchanging a Convertible Reserved Instance**This example gets the exchange information for the specified Convertible Reserved Instances. Command: `aws ec2 get-reserved-instances-exchange-quote --reserved-instance-ids``7b8750c3-397e-4da4-bbcb-a45ebexample`--target-configurations`OfferingId=6fea5434-b379-434c-b07b-a7abexample`Output: `{ "CurrencyCode": "USD", "ReservedInstanceValueSet": [ { "ReservedInstanceId": "7b8750c3-397e-4da4-bbcb-a45ebexample", "ReservationValue": { "RemainingUpfrontValue": "0.000000", "HourlyPrice": "0.027800", "RemainingTotalValue": "730.556200" } } ], "PaymentDue": "424.983828", "TargetConfigurationValueSet": [ { "TargetConfiguration": { "InstanceCount": 5, "OfferingId": "6fea5434-b379-434c-b07b-a7abexample" }, "ReservationValue": { "RemainingUpfrontValue": "424.983828", "HourlyPrice": "0.016000", "RemainingTotalValue": "845.447828" } } ], "IsValidExchange": true, "OutputReservedInstancesWillExpireAt": "2020-10-01T13:03:39Z", "ReservedInstanceValueRollup": { "RemainingUpfrontValue": "0.000000", "HourlyPrice": "0.027800", "RemainingTotalValue": "730.556200" }, "TargetConfigurationValueRollup": { "RemainingUpfrontValue": "424.983828", "HourlyPrice": "0.016000", "RemainingTotalValue": "845.447828" } }`- 
                    For API details, see [GetReservedInstancesExchangeQuote](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-reserved-instances-exchange-quote.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-security-groups-for-vpc`.

- **AWS CLI**
- 
            
                    **To view security groups that can be associated with network interfaces in a specified VPC.**The following `get-security-groups-for-vpc`example shows the security groups that can be associated with network interfaces in the VPC.`aws ec2 get-security-groups-for-vpc \ --vpc-id``vpc-6c31a611`\ --region`us-east-1`Output: `{ "SecurityGroupForVpcs": [ { "Description": "launch-wizard-36 created 2022-08-29T15:59:35.338Z", "GroupName": "launch-wizard-36", "OwnerId": "470889052923", "GroupId": "sg-007e0c3027ee885f5", "Tags": [], "PrimaryVpcId": "vpc-6c31a611" }, { "Description": "launch-wizard-18 created 2024-01-19T20:22:27.527Z", "GroupName": "launch-wizard-18", "OwnerId": "470889052923", "GroupId": "sg-0147193bef51c9eef", "Tags": [], "PrimaryVpcId": "vpc-6c31a611" } }`- 
                    For API details, see [GetSecurityGroupsForVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-security-groups-for-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-serial-console-access-status`.

- **AWS CLI**
- 
            
                    **To view the status of account access to the serial console**The following `get-serial-console-access-status`example determines whether serial console access is enabled for your account.`aws ec2 get-serial-console-access-status`Output: `{ "SerialConsoleAccessEnabled": true }`For more information, see [EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetSerialConsoleAccessStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-serial-console-access-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-snapshot-block-public-access-state`.

- **AWS CLI**
- 
            
                    **To get the current state of block public access for snapshots**The following `get-snapshot-block-public-access-state`example gets the current state of block public access for snapshots.`aws ec2 get-snapshot-block-public-access-state`Output: `{ "State": "block-all-sharing" }`For more information, see [Block public access for snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/block-public-access-snapshots.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [GetSnapshotBlockPublicAccessState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-snapshot-block-public-access-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-spot-placement-scores`.

- **AWS CLI**
- 
            
                    **To calculate the Spot placement score for specified requirements**The following `get-spot-placement-scores`example first generates a list of all of the possible parameters that can be specified for the Spot placement score configuration using the`--generate-cli-skeleton`parameter, and saves the list to a JSON file. Then, the JSON file is used to configure the requirements to use to calculate the Spot placement score.To generate all possible parameters that can be specified for the Spot placement score configuration, and save the output directly to a JSON file. `aws ec2 get-spot-placement-scores \ --region``us-east-1`\ --generate-cli-skeleton`input``>``attributes.json`Output: `{ "InstanceTypes": [ "" ], "TargetCapacity": 0, "TargetCapacityUnitType": "vcpu", "SingleAvailabilityZone": true, "RegionNames": [ "" ], "InstanceRequirementsWithMetadata": { "ArchitectureTypes": [ "x86_64_mac" ], "VirtualizationTypes": [ "hvm" ], "InstanceRequirements": { "VCpuCount": { "Min": 0, "Max": 0 }, "MemoryMiB": { "Min": 0, "Max": 0 }, "CpuManufacturers": [ "amd" ], "MemoryGiBPerVCpu": { "Min": 0.0, "Max": 0.0 }, "ExcludedInstanceTypes": [ "" ], "InstanceGenerations": [ "previous" ], "SpotMaxPricePercentageOverLowestPrice": 0, "OnDemandMaxPricePercentageOverLowestPrice": 0, "BareMetal": "excluded", "BurstablePerformance": "excluded", "RequireHibernateSupport": true, "NetworkInterfaceCount": { "Min": 0, "Max": 0 }, "LocalStorage": "included", "LocalStorageTypes": [ "hdd" ], "TotalLocalStorageGB": { "Min": 0.0, "Max": 0.0 }, "BaselineEbsBandwidthMbps": { "Min": 0, "Max": 0 }, "AcceleratorTypes": [ "fpga" ], "AcceleratorCount": { "Min": 0, "Max": 0 }, "AcceleratorManufacturers": [ "amd" ], "AcceleratorNames": [ "vu9p" ], "AcceleratorTotalMemoryMiB": { "Min": 0, "Max": 0 } } }, "DryRun": true, "MaxResults": 0, "NextToken": "" }`Configure the JSON file. You must provide a value for `TargetCapacity`. For a description of each parameter and their default values, see Calculate the Spot placement score (AWS CLI) <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html#calculate-sps-cli>.Calculate the Spot placement score for the requirements specified in `attributes.json`. Specify the name and path to your JSON file by using the`--cli-input-json`parameter.`aws ec2 get-spot-placement-scores \ --region``us-east-1`\ --cli-input-json`file://attributes.json`Output if `SingleAvailabilityZone`is set to`false`or omitted (if omitted, it defaults to`false`). A scored list of Regions is returned.`"Recommendation": [ { "Region": "us-east-1", "Score": 7 }, { "Region": "us-west-1", "Score": 5 }, ...`Output if `SingleAvailabilityZone`is set to`true`. A scored list of SingleAvailability Zones is returned.`"Recommendation": [ { "Region": "us-east-1", "AvailabilityZoneId": "use1-az1" "Score": 8 }, { "Region": "us-east-1", "AvailabilityZoneId": "usw2-az3" "Score": 6 }, ...`For more information about calculating a Spot placement score, and for example configurations, see [Calculate a Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html#work-with-spot-placement-score)in the*Amazon EC2 User Guide*.- 
                    For API details, see [GetSpotPlacementScores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-spot-placement-scores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-subnet-cidr-reservations`.

- **AWS CLI**
- 
            
                    **To get information about a subnet CIDR reservation**The following `get-subnet-cidr-reservations`example displays information about the specified subnet CIDR reservation.`aws ec2 get-subnet-cidr-reservations \ --subnet-id``subnet-03c51e2e6cEXAMPLE`Output: `{ "SubnetIpv4CidrReservations": [ { "SubnetCidrReservationId": "scr-044f977c4eEXAMPLE", "SubnetId": "subnet-03c51e2e6cEXAMPLE", "Cidr": "10.1.0.16/28", "ReservationType": "prefix", "OwnerId": "123456789012" } ], "SubnetIpv6CidrReservations": [] }`For more information, see [Subnet CIDR reservations](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-cidr-reservation.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [GetSubnetCidrReservations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-subnet-cidr-reservations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-transit-gateway-attachment-propagations`.

- **AWS CLI**
- 
            
                    **To list the route tables to which the specified resource attachment propagates routes**The following `get-transit-gateway-attachment-propagations`example lists the route table to which the specified resource attachment propagates routes.`aws ec2 get-transit-gateway-attachment-propagations \ --transit-gateway-attachment-id``tgw-attach-09fbd47ddfEXAMPLE`Output: `{ "TransitGatewayAttachmentPropagations": [ { "TransitGatewayRouteTableId": "tgw-rtb-0882c61b97EXAMPLE", "State": "enabled" } ] }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [GetTransitGatewayAttachmentPropagations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-attachment-propagations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-transit-gateway-multicast-domain-associations`.

- **AWS CLI**
- 
            
                    **To view the information about the transit gateway multicast domain associations**The following `get-transit-gateway-multicast-domain-associations`example returns the associations for the specified multicast domain.`aws ec2 get-transit-gateway-multicast-domain-associations \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef7EXAMPLE`Output: `{ "MulticastDomainAssociations": [ { "TransitGatewayAttachmentId": "tgw-attach-028c1dd0f8EXAMPLE", "ResourceId": "vpc-01128d2c24EXAMPLE", "ResourceType": "vpc", "Subnet": { "SubnetId": "subnet-000de86e3bEXAMPLE", "State": "associated" } }, { "TransitGatewayAttachmentId": "tgw-attach-070e571cd1EXAMPLE", "ResourceId": "vpc-7EXAMPLE", "ResourceType": "vpc", "Subnet": { "SubnetId": "subnet-4EXAMPLE", "State": "associated" } }, { "TransitGatewayAttachmentId": "tgw-attach-070e571cd1EXAMPLE", "ResourceId": "vpc-7EXAMPLE", "ResourceType": "vpc", "Subnet": { "SubnetId": "subnet-5EXAMPLE", "State": "associated" } }, { "TransitGatewayAttachmentId": "tgw-attach-070e571cd1EXAMPLE", "ResourceId": "vpc-7EXAMPLE", "ResourceType": "vpc", "Subnet": { "SubnetId": "subnet-aEXAMPLE", "State": "associated" } }, { "TransitGatewayAttachmentId": "tgw-attach-070e571cd1EXAMPLE", "ResourceId": "vpc-7EXAMPLE", "ResourceType": "vpc", "Subnet": { "SubnetId": "subnet-fEXAMPLE", "State": "associated" } } ] }`For more information, see [Multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-domains-about.html)in the*Transit Gateways Guide*.- 
                    For API details, see [GetTransitGatewayMulticastDomainAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-multicast-domain-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-transit-gateway-prefix-list-references`.

- **AWS CLI**
- 
            
                    **To get prefix list references in a transit gateway route table**The following `get-transit-gateway-prefix-list-references`example gets the prefix list references for the specified transit gateway route table, and filters by the ID of a specific prefix list.`aws ec2 get-transit-gateway-prefix-list-references \ --transit-gateway-route-table-id``tgw-rtb-0123456789abcd123`\ --filters`Name=prefix-list-id,Values=pl-11111122222222333`Output: `{ "TransitGatewayPrefixListReferences": [ { "TransitGatewayRouteTableId": "tgw-rtb-0123456789abcd123", "PrefixListId": "pl-11111122222222333", "PrefixListOwnerId": "123456789012", "State": "available", "Blackhole": false, "TransitGatewayAttachment": { "TransitGatewayAttachmentId": "tgw-attach-aabbccddaabbccaab", "ResourceType": "vpc", "ResourceId": "vpc-112233445566aabbc" } } ] }`For more information, see [Prefix list references](https://docs.aws.amazon.com/vpc/latest/tgw/create-prefix-list-reference.html)in the*Transit Gateways Guide*.- 
                    For API details, see [GetTransitGatewayPrefixListReferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-prefix-list-references.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-transit-gateway-route-table-associations`.

- **AWS CLI**
- 
            
                    **To get information about the associations for the specified transit gateway route table**The following `get-transit-gateway-route-table-associations`example displays information about the associations for the specified transit gateway route table.`aws ec2 get-transit-gateway-route-table-associations \ --transit-gateway-route-table-id``tgw-rtb-0a823edbdeEXAMPLE`Output: `{ "Associations": [ { "TransitGatewayAttachmentId": "tgw-attach-09b52ccdb5EXAMPLE", "ResourceId": "vpc-4d7de228", "ResourceType": "vpc", "State": "associating" } ] }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html#associate-tgw-route-table)in the*Transit Gateways Guide*.- 
                    For API details, see [GetTransitGatewayRouteTableAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-route-table-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-transit-gateway-route-table-propagations`.

- **AWS CLI**
- 
            
                    **To display information about the route table propagations for the specified transit gateway route table**The following `get-transit-gateway-route-table-propagations`example returns the route table propagations for the specified route table.`aws ec2 get-transit-gateway-route-table-propagations \ --transit-gateway-route-table-id``tgw-rtb-002573ed1eEXAMPLE`Output: `{ "TransitGatewayRouteTablePropagations": [ { "TransitGatewayAttachmentId": "tgw-attach-01f8100bc7EXAMPLE", "ResourceId": "vpc-3EXAMPLE", "ResourceType": "vpc", "State": "enabled" }, { "TransitGatewayAttachmentId": "tgw-attach-08e0bc912cEXAMPLE", "ResourceId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE", "ResourceType": "direct-connect-gateway", "State": "enabled" }, { "TransitGatewayAttachmentId": "tgw-attach-0a89069f57EXAMPLE", "ResourceId": "8384da05-13ce-4a91-aada-5a1baEXAMPLE", "ResourceType": "direct-connect-gateway", "State": "enabled" } ] }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [GetTransitGatewayRouteTablePropagations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-transit-gateway-route-table-propagations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-verified-access-endpoint-policy`.

- **AWS CLI**
- 
            
                    **To get the Verified Access policy of an endpoint**The following `get-verified-access-endpoint-policy`example gets the Verified Access policy of the specified endpoint.`aws ec2 get-verified-access-endpoint-policy \ --verified-access-endpoint-id``vae-066fac616d4d546f2`Output: `{ "PolicyEnabled": true, "PolicyDocument": "permit(principal,action,resource)\nwhen {\n context.identity.groups.contains(\"finance\") &&\n context.identity.email_verified == true\n};" }`For more information, see [Verified Access policies](https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [GetVerifiedAccessEndpointPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-verified-access-endpoint-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-verified-access-group-policy`.

- **AWS CLI**
- 
            
                    **To get the Verified Access policy of a group**The following `get-verified-access-group-policy`example gets the Verified Access policy of the specified group.`aws ec2 get-verified-access-group-policy \ --verified-access-group-id``vagr-0dbe967baf14b7235`Output: `{ "PolicyEnabled": true, "PolicyDocument": "permit(principal,action,resource)\nwhen {\n context.identity.groups.contains(\"finance\") &&\n context.identity.email_verified == true\n};" }`For more information, see [Verified Access groups](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [GetVerifiedAccessGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-verified-access-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-vpn-connection-device-sample-configuration`.

- **AWS CLI**
- 
            
                    **To download a sample configuration file**The following `get-vpn-connection-device-sample-configuration`example downloads the specified sample configuration file. To list the gateway devices with a sample configuration file, call the`get-vpn-connection-device-types`command.`aws ec2 get-vpn-connection-device-sample-configuration \ --vpn-connection-id``vpn-123456789abc01234`\ --vpn-connection-device-type-id`5fb390ba`Output: `{ "VpnConnectionDeviceSampleConfiguration": "contents-of-the-sample-configuration-file" }`For more information, see [Download the configuration file](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-download-config)in the*AWS Site-to-Site VPN User Guide*.- 
                    For API details, see [GetVpnConnectionDeviceSampleConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-vpn-connection-device-sample-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-vpn-connection-device-types`.

- **AWS CLI**
- 
            
                    **To list gateway devices with a sample configuration file**The following `get-vpn-connection-device-types`example lists the gateway devices from Palo Alto Networks that have sample configuration files.`aws ec2 get-vpn-connection-device-types \ --query``"VpnConnectionDeviceTypes[?Vendor==`Palo Alto Networks`]"`Output: `[ { "VpnConnectionDeviceTypeId": "754a6372", "Vendor": "Palo Alto Networks", "Platform": "PA Series", "Software": "PANOS 4.1.2+" }, { "VpnConnectionDeviceTypeId": "9612cbed", "Vendor": "Palo Alto Networks", "Platform": "PA Series", "Software": "PANOS 4.1.2+ (GUI)" }, { "VpnConnectionDeviceTypeId": "5fb390ba", "Vendor": "Palo Alto Networks", "Platform": "PA Series", "Software": "PANOS 7.0+" } ]`For more information, see [Download the configuration file](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-download-config)in the*AWS Site-to-Site VPN user Guide*.- 
                    For API details, see [GetVpnConnectionDeviceTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-vpn-connection-device-types.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-client-vpn-client-certificate-revocation-list`.

- **AWS CLI**
- 
            
                    **To import a client certificate revocation list**The following `import-client-vpn-client-certificate-revocation-list`example imports a client certificate revocation list to the Client VPN endpoint by specifying the location of the file on the local computer.`aws ec2 import-client-vpn-client-certificate-revocation-list \ --certificate-revocation-list``file:///path/to/crl.pem`\ --client-vpn-endpoint-id`cvpn-endpoint-123456789123abcde`Output: `{ "Return": true }`For more information, see [Client Certificate Revocation Lists](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-certificates.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [ImportClientVpnClientCertificateRevocationList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-client-vpn-client-certificate-revocation-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-image`.

- **AWS CLI**
- 
            
                    **To import a VM image file as an AMI**The following `import-image`example imports the specified OVA.`aws ec2 import-image \ --disk-containers Format=ova,UserBucket="{S3Bucket=my-import-bucket,S3Key=vms/my-server-vm.ova}"`Output: `{ "ImportTaskId": "import-ami-1234567890abcdef0", "Progress": "2", "SnapshotDetails": [ { "DiskImageSize": 0.0, "Format": "ova", "UserBucket": { "S3Bucket": "my-import-bucket", "S3Key": "vms/my-server-vm.ova" } } ], "Status": "active", "StatusMessage": "pending" }`- 
                    For API details, see [ImportImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-key-pair`.

- **AWS CLI**
- 
            
                    **To import a public key**First, generate a key pair with the tool of your choice. For example, use this ssh-keygen command: Command: `ssh-keygen -t rsa -C "my-key" -f ~/.ssh/my-key`Output: `Generating public/private rsa key pair. Enter passphrase (empty for no passphrase): Enter same passphrase again: Your identification has been saved in /home/ec2-user/.ssh/my-key. Your public key has been saved in /home/ec2-user/.ssh/my-key.pub. ...`This example command imports the specified public key. Command: `aws ec2 import-key-pair --key-name``"my-key"`--public-key-material`fileb://~/.ssh/my-key.pub`Output: `{ "KeyName": "my-key", "KeyFingerprint": "1f:51:ae:28:bf:89:e9:d8:1f:25:5d:37:2d:7d:b8:ca" }`- 
                    For API details, see [ImportKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-snapshot`.

- **AWS CLI**
- 
            
                    **To import a snapshot**The following `import-snapshot`example imports the specified disk as a snapshot.`aws ec2 import-snapshot \ --description``"My server VMDK"`\ --disk-container Format=VMDK,UserBucket={'S3Bucket=my-import-bucket,S3Key=vms/my-server-vm.vmdk'}Output: `{ "Description": "My server VMDK", "ImportTaskId": "import-snap-1234567890abcdef0", "SnapshotTaskDetail": { "Description": "My server VMDK", "DiskImageSize": "0.0", "Format": "VMDK", "Progress": "3", "Status": "active", "StatusMessage": "pending" "UserBucket": { "S3Bucket": "my-import-bucket", "S3Key": "vms/my-server-vm.vmdk" } } }`- 
                    For API details, see [ImportSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-images-in-recycle-bin`.

- **AWS CLI**
- 
            
                    **To list the images in the Recycle Bin**The following `list-images-in-recycle-bin`example lists all of the images that are currently retained in the Recycle Bin.`aws ec2 list-images-in-recycle-bin`Output: `{ "Images": [ { "RecycleBinEnterTime": "2022-03-14T15:35:08.000Z", "Description": "Monthly AMI One", "RecycleBinExitTime": "2022-03-15T15:35:08.000Z", "Name": "AMI_01", "ImageId": "ami-0111222333444abcd" } ] }`For more information, see [Recover deleted AMIs from the Recycle Bin](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-amis.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [ListImagesInRecycleBin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/list-images-in-recycle-bin.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-snapshots-in-recycle-bin`.

- **AWS CLI**
- 
            
                    **To view snapshots in the Recycle Bin**The following `list-snapshots-in-recycle-bin`example lists information about snapshots in the Recycle Bin, including the snapshot ID, a description of the snapshot, The ID of the volume from which the snapshot was created, the date and time when the snapshot was deleted and it entered the Recycle Bin, and the date and time when the retention period expires.`aws ec2 list-snapshots-in-recycle-bin \ --snapshot-id``snap-01234567890abcdef`Output: `{ "SnapshotRecycleBinInfo": [ { "Description": "Monthly data backup snapshot", "RecycleBinEnterTime": "2022-12-01T13:00:00.000Z", "RecycleBinExitTime": "2022-12-15T13:00:00.000Z", "VolumeId": "vol-abcdef09876543210", "SnapshotId": "snap-01234567890abcdef" } ] }`For more information about Recycle Bin, see [Recover deleted snapshots from the Recycle Bin](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-snaps.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [ListSnapshotsInRecycleBin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/list-snapshots-in-recycle-bin.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `lock-snapshot`.

- **AWS CLI**
- 
            
                    **Example 1: To lock a snapshot in governance mode**The following `lock-snapshot`example locks the specified snapshot in governance mode.`aws ec2 lock-snapshot \ --snapshot-id``snap-0b5e733b4a8df6e0d`\ --lock-mode`governance`\ --lock-duration`365`Output: `{ "SnapshotId": "snap-0b5e733b4a8df6e0d", "LockState": "governance", "LockDuration": 365, "LockCreatedOn": "2024-05-05T00:56:06.208000+00:00", "LockExpiresOn": "2025-05-05T00:56:06.208000+00:00", "LockDurationStartTime": "2024-05-05T00:56:06.208000+00:00" }`For more information, see [Snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lock.html)in the*Amazon EBS User Guide*.**Example 2: To lock a snapshot in compliance mode**The following `lock-snapshot`example lock the specified snapshot in compliance mode.`aws ec2 lock-snapshot \ --snapshot-id``snap-0163a8524c5b9901f`\ --lock-mode`compliance`\ --cool-off-period`24`\ --lock-duration`365`Output: `{ "SnapshotId": "snap-0b5e733b4a8df6e0d", "LockState": "compliance-cooloff", "LockDuration": 365, "CoolOffPeriod": 24, "CoolOffPeriodExpiresOn": "2024-05-06T01:02:20.527000+00:00", "LockCreatedOn": "2024-05-05T01:02:20.527000+00:00", "LockExpiresOn": "2025-05-05T01:02:20.527000+00:00", "LockDurationStartTime": "2024-05-05T01:02:20.527000+00:00" }`For more information, see [Snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lock.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [LockSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/lock-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-address-attribute`.

- **AWS CLI**
- 
            
                    **To modify the domain name attribute associated with an elastic IP address**The following `modify-address-attribute`examples modify the domain name attribute of an elastic IP address.Linux: `aws ec2 modify-address-attribute \ --allocation-id``eipalloc-abcdef01234567890`\ --domain-name`example.com`Windows: `aws ec2 modify-address-attribute``^`--allocation-id`eipalloc-abcdef01234567890``^`--domain-name`example.com`Output: `{ "Addresses": [ { "PublicIp": "192.0.2.0", "AllocationId": "eipalloc-abcdef01234567890", "PtrRecord": "example.net." "PtrRecordUpdate": { "Value": "example.com.", "Status": "PENDING" } ] }`To monitor the pending change and to view the modified attributes of an elastic IP address, see [describe-addresses-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-addresses-attribute.html)in the*AWS CLI Command Reference*.- 
                    For API details, see [ModifyAddressAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-address-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-availability-zone-group`.

- **AWS CLI**
- 
            
                    **To enable a zone group**The following `modify-availability-zone-group`example enables the specified zone group.`aws ec2 modify-availability-zone-group \ --group-name``us-west-2-lax-1`\ --opt-in-status`opted-in`Output: `{ "Return": true }`For more information, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyAvailabilityZoneGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-availability-zone-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-capacity-reservation-fleet`.

- **AWS CLI**
- 
            
                    **Example 1: To modify the total target capacity of a Capacity Reservation Fleet**The following `modify-capacity-reservation-fleet`example modifies the total target capacity of the specified Capacity Reservation Fleet. When you modify the total target capacity of a Capacity Reservation Fleet, the Fleet automatically creates new Capacity Reservations, or modifies or cancels existing Capacity Reservations in the Fleet to meet the new total target capacity. You can't attempt additional modifications to a Fleet while it is in the`modifying`state.`aws ec2 modify-capacity-reservation-fleet \ --capacity-reservation-fleet-id``crf-01234567890abcedf`\ --total-target-capacity`160`Output: `{ "Return": true }`**Example 2: To modify the end date of a Capacity Reservation Fleet**The following `modify-capacity-reservation-fleet`example modifies the end date of the specified Capacity Reservation Fleet. When you modify the end date for the Fleet, the end dates for all of the individual Capacity Reservations are updated accordingly. You can't attempt additional modifications to a Fleet while it is in the`modifying`state.`aws ec2 modify-capacity-reservation-fleet \ --capacity-reservation-fleet-id``crf-01234567890abcedf`\ --end-date`2022-07-04T23:59:59.000Z`Output: `{ "Return": true }`For more information about Capacity Reservation Fleets, see [Capacity Reservation Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyCapacityReservationFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-capacity-reservation-fleet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-capacity-reservation`.

- **AWS CLI**
- 
            
                    **Example 1: To change the number of instances reserved by an existing capacity reservation**The following `modify-capacity-reservation`example changes the number of instances for which the capacity reservation reserves capacity.`aws ec2 modify-capacity-reservation \ --capacity-reservation-id``cr-1234abcd56EXAMPLE`\ --instance-count`5`Output: `{ "Return": true }`For more information, see [Modify a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify.html)in the*Amazon EC2 User Guide*.**Example 2: To change the end date and time for an existing capacity reservation**The following `modify-capacity-reservation`example modifies an existing capacity reservation to end at the specified date and time.`aws ec2 modify-capacity-reservation \ --capacity-reservation-id``cr-1234abcd56EXAMPLE`\ --end-date-type`limited`\ --end-date`2019-08-31T23:59:59Z`For more information, see [Modify a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyCapacityReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-capacity-reservation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-client-vpn-endpoint`.

- **AWS CLI**
- 
            
                    **To modify a Client VPN endpoint**The following `modify-client-vpn-endpoint`example enables client connection logging for the specified Client VPN endpoint.`aws ec2 modify-client-vpn-endpoint \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --connection-log-options`Enabled=true,CloudwatchLogGroup=ClientVPNLogs`Output: `{ "Return": true }`For more information, see [Client VPN Endpoints](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-endpoints.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [ModifyClientVpnEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-client-vpn-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-default-credit-specification`.

- **AWS CLI**
- 
            
                    **To modify the default credit option**The following `modify-default-credit-specification`example modifies the default credit option for T2 instances.`aws ec2 modify-default-credit-specification \ --instance-family``t2`\ --cpu-credits`unlimited`Output: `{ "InstanceFamilyCreditSpecification": { "InstanceFamily": "t2", "CpuCredits": "unlimited" } }`- 
                    For API details, see [ModifyDefaultCreditSpecification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-default-credit-specification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-ebs-default-kms-key-id`.

- **AWS CLI**
- 
            
                    **To set your default CMK for EBS encryption**The following `modify-ebs-default-kms-key-id`example sets the specified CMK as the default CMK for EBS encryption for your AWS account in the current Region.`aws ec2 modify-ebs-default-kms-key-id \ --kms-key-id``alias/my-cmk`Output: `{ "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/0ea3fef3-80a7-4778-9d8c-1c0c6EXAMPLE" }`- 
                    For API details, see [ModifyEbsDefaultKmsKeyId](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ebs-default-kms-key-id.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-fleet`.

- **AWS CLI**
- 
            
                    **To scale an EC2 Fleet**The following `modify-fleet`example modifies the target capacity of the specified EC2 Fleet. If the specified value is greater than the current capacity, the EC2 Fleet launches additional instances. If the specified value is less than the current capacity, the EC2 Fleet cancels any open requests and if the termination policy is`terminate`, the EC2 fleet terminates any instances that exceed the new target capacity.`aws ec2 modify-fleet \ --fleet-id``fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE`\ --target-capacity-specification`TotalTargetCapacity=5`Output: `{ "Return": true }`For more information, see [Manage an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-fleet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-fpga-image-attribute`.

- **AWS CLI**
- 
            
                    **To modify the attributes of an Amazon FPGA image**This example adds load permissions for account ID `123456789012`for the specified AFI.Command: `aws ec2 modify-fpga-image-attribute --attribute``loadPermission`--fpga-image-id`afi-0d123e123bfc85abc`--load-permission`Add=[{UserId=123456789012}]`Output: `{ "FpgaImageAttribute": { "FpgaImageId": "afi-0d123e123bfc85abc", "LoadPermissions": [ { "UserId": "123456789012" } ] } }`- 
                    For API details, see [ModifyFpgaImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-fpga-image-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-hosts`.

- **AWS CLI**
- 
            
                    **Example 1: To enable auto-placement for a Dedicated Host**The following `modify-hosts`example enables auto-placement for a Dedicated Host so that it accepts any untargeted instance launches that match its instance type configuration.`aws ec2 modify-hosts \ --host-id``h-06c2f189b4EXAMPLE`\ --auto-placement`on`Output: `{ "Successful": [ "h-06c2f189b4EXAMPLE" ], "Unsuccessful": [] }`For more information, see [Modify the auto-placement setting for a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-host-auto-placement.html)in the*Amazon EC2 User Guide*.**Example 2: To enable host recovery for a Dedicated Host**The following `modify-hosts`example enables host recovery for the specified Dedicated Host.`aws ec2 modify-hosts \ --host-id``h-06c2f189b4EXAMPLE`\ --host-recovery`on`Output: `{ "Successful": [ "h-06c2f189b4EXAMPLE" ], "Unsuccessful": [] }`For more information, see [Modify the auto-placement setting for a Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-host-auto-placement.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-hosts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-id-format`.

- **AWS CLI**
- 
            
                    **To enable the longer ID format for a resource**The following `modify-id-format`example enables the longer ID format for the`instance`resource type.`aws ec2 modify-id-format \ --resource``instance`\ --use-long-ids**To disable the longer ID format for a resource**The following `modify-id-format`example disables the longer ID format for the`instance`resource type.`aws ec2 modify-id-format \ --resource``instance`\ --no-use-long-idsThe following `modify-id-format`example enables the longer ID format for all supported resource types that are within their opt-in period.`aws ec2 modify-id-format \ --resource``all-current`\ --use-long-ids- 
                    For API details, see [ModifyIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-id-format.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-identity-id-format`.

- **AWS CLI**
- 
            
                    **To enable an IAM role to use longer IDs for a resource**The following `modify-identity-id-format`example enables the IAM role`EC2Role`in your AWS account to use long ID format for the`instance`resource type.`aws ec2 modify-identity-id-format \ --principal-arn``arn:aws:iam::123456789012:role/EC2Role`\ --resource`instance`\ --use-long-ids**To enable an IAM user to use longer IDs for a resource**The following `modify-identity-id-format`example enables the IAM user`AdminUser`in your AWS account to use the longer ID format for the`volume`resource type.`aws ec2 modify-identity-id-format \ --principal-arn``arn:aws:iam::123456789012:user/AdminUser`\ --resource`volume`\ --use-long-idsThe following `modify-identity-id-format`example enables the IAM user`AdminUser`in your AWS account to use the longer ID format for all supported resource types that are within their opt-in period.`aws ec2 modify-identity-id-format \ --principal-arn``arn:aws:iam::123456789012:user/AdminUser`\ --resource`all-current`\ --use-long-ids- 
                    For API details, see [ModifyIdentityIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-identity-id-format.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-image-attribute`.

- **AWS CLI**
- 
            
                    **Example 1: To make an AMI public**The following `modify-instance-attribute`example makes the specified AMI public.`aws ec2 modify-image-attribute \ --image-id``ami-5731123e`\ --launch-permission`"Add=[{Group=all}]"`This command produces no output. **Example 2: To make an AMI private**The following `modify-instance-attribute`example makes the specified AMI private.`aws ec2 modify-image-attribute \ --image-id``ami-5731123e`\ --launch-permission`"Remove=[{Group=all}]"`This command produces no output. **Example 3: To grant launch permission to an AWS account**The following `modify-instance-attribute`example grants launch permissions to the specified AWS account.`aws ec2 modify-image-attribute \ --image-id``ami-5731123e`\ --launch-permission`"Add=[{UserId=123456789012}]"`This command produces no output. **Example 4: To remove launch permission from an AWS account**The following `modify-instance-attribute`example removes launch permissions from the specified AWS account.`aws ec2 modify-image-attribute \ --image-id``ami-5731123e`\ --launch-permission`"Remove=[{UserId=123456789012}]"`- 
                    For API details, see [ModifyImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-image-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-attribute`.

- **AWS CLI**
- 
            
                    **Example 1: To modify the instance type**The following `modify-instance-attribute`example modifies the instance type of the specified instance. The instance must be in the`stopped`state.`aws ec2 modify-instance-attribute \ --instance-id``i-1234567890abcdef0`\ --instance-type "{\"Value\": \"m1.small\"}"This command produces no output. **Example 2: To enable enhanced networking on an instance**The following `modify-instance-attribute`example enables enhanced networking for the specified instance. The instance must be in the`stopped`state.`aws ec2 modify-instance-attribute \ --instance-id``i-1234567890abcdef0`\ --sriov-net-support`simple`This command produces no output. **Example 3: To modify the sourceDestCheck attribute**The following `modify-instance-attribute`example sets the`sourceDestCheck`attribute of the specified instance to`true`. The instance must be in a VPC.`aws ec2 modify-instance-attribute --instance-id``i-1234567890abcdef0`--source-dest-check "{\"Value\": true}"This command produces no output. **Example 4: To modify the deleteOnTermination attribute of the root volume**The following `modify-instance-attribute`example sets the`deleteOnTermination`attribute for the root volume of the specified Amazon EBS-backed instance to`false`. By default, this attribute is`true`for the root volume.Command: `aws ec2 modify-instance-attribute \ --instance-id``i-1234567890abcdef0`\ --block-device-mappings "[{\"DeviceName\": \"/dev/sda1\",\"Ebs\":{\"DeleteOnTermination\":false}}]"This command produces no output. **Example 5: To modify the user data attached to an instance**The following `modify-instance-attribute`example adds the contents of the file`UserData.txt`as the UserData for the specified instance.Contents of original file `UserData.txt`:`#!/bin/bash yum update -y service httpd start chkconfig httpd on`The contents of the file must be base64 encoded. The first command converts the text file to base64 and saves it as a new file. Linux/macOS version of the command: `base64 UserData.txt > UserData.base64.txt`This command produces no output. Windows version of the command: `certutil -encode UserData.txt tmp.b64 && findstr /v /c:- tmp.b64 > UserData.base64.txt`Output: `Input Length = 67 Output Length = 152 CertUtil: -encode command completed successfully.`Now you can reference that file in the CLI command that follows: `aws ec2 modify-instance-attribute \ --instance-id=i-09b5a14dbca622e76 \ --attribute``userData`--value`file://UserData.base64.txt`This command produces no output. For more information, see [User Data and the AWS CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html#user-data-api-cli)in the*EC2 User Guide*.- 
                    For API details, see [ModifyInstanceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-capacity-reservation-attributes`.

- **AWS CLI**
- 
            
                    **Example 1: To modify an instance's capacity reservation targeting settings**The following `modify-instance-capacity-reservation-attributes`example modifies a stopped instance to target a specific capacity reservation.`aws ec2 modify-instance-capacity-reservation-attributes \ --instance-id``i-EXAMPLE8765abcd4e`\ --capacity-reservation-specification '`CapacityReservationTarget={CapacityReservationId= cr-1234abcd56EXAMPLE }`'Output: `{ "Return": true }`For more information, see [Modify the Capacity Reservation settings of your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify-instance.html)in the*Amazon EC2 User Guide*.**Example 2: To modify an instance's capacity reservation targeting settings**The following `modify-instance-capacity-reservation-attributes`example modifies a stopped instance that targets the specified capacity reservation to launch in any capacity reservation that has matching attributes (instance type, platform, Availability Zone) and that has open instance matching criteria.`aws ec2 modify-instance-capacity-reservation-attributes \ --instance-id``i-EXAMPLE8765abcd4e`\ --capacity-reservation-specification '`CapacityReservationPreference=open`'Output: `{ "Return": true }`For more information, see [Modify the Capacity Reservation settings of your instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-modify-instance.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyInstanceCapacityReservationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-capacity-reservation-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-credit-specification`.

- **AWS CLI**
- 
            
                    **To modify the credit option for CPU usage of an instance**This example modifies the credit option for CPU usage of the specified instance in the specified region to "unlimited". Valid credit options are "standard" and "unlimited". Command: `aws ec2 modify-instance-credit-specification --instance-credit-specification``"InstanceId=i-1234567890abcdef0,CpuCredits=unlimited"`Output: `{ "SuccessfulInstanceCreditSpecifications": [ { "InstanceId": "i-1234567890abcdef0" } ], "UnsuccessfulInstanceCreditSpecifications": [] }`- 
                    For API details, see [ModifyInstanceCreditSpecification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-credit-specification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-event-start-time`.

- **AWS CLI**
- 
            
                    **To modify the event start time for an instance**The following `modify-instance-event-start-time`command shows how to modify the event start time for the specified instance. Specify the event ID by using the`--instance-event-id`parameter. Specify the new date and time by using the`--not-before`parameter.`aws ec2 modify-instance-event-start-time --instance-id``i-1234567890abcdef0`--instance-event-id`instance-event-0abcdef1234567890`--not-before`2019-03-25T10:00:00.000`Output: `"Event": { "InstanceEventId": "instance-event-0abcdef1234567890", "Code": "system-reboot", "Description": "scheduled reboot", "NotAfter": "2019-03-25T12:00:00.000Z", "NotBefore": "2019-03-25T10:00:00.000Z", "NotBeforeDeadline": "2019-04-22T21:00:00.000Z" }`For more information, see Working with Instances Scheduled for Reboot in the *Amazon Elastic Compute Cloud User Guide*- 
                    For API details, see [ModifyInstanceEventStartTime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-event-start-time.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-event-window`.

- **AWS CLI**
- 
            
                    **Example 1: To modify the time range of an event window**The following `modify-instance-event-window`example modifies the time range of an event window. Specify the`time-range`parameter to modify the time range. You can't also specify the`cron-expression`parameter.`aws ec2 modify-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`--time-range`StartWeekDay=monday,StartHour=2,EndWeekDay=wednesday,EndHour=8`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "TimeRanges": [ { "StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8 } ], "Name": "myEventWindowName", "AssociationTarget": { "InstanceIds": [ "i-0abcdef1234567890", "i-0be35f9acb8ba01f0" ], "Tags": [], "DedicatedHostIds": [] }, "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1" } ] } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 2: To modify a set of time ranges for an event window**The following `modify-instance-event-window`example modifies the time range of an event window. Specify the`time-range`parameter to modify the time range. You can't also specify the`cron-expression`parameter.`aws ec2 modify-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --time-range '`[{"StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8}, {"StartWeekDay": "thursday", "StartHour": 2, "EndWeekDay": "friday", "EndHour": 8}]`'Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "TimeRanges": [ { "StartWeekDay": "monday", "StartHour": 2, "EndWeekDay": "wednesday", "EndHour": 8 }, { "StartWeekDay": "thursday", "StartHour": 2, "EndWeekDay": "friday", "EndHour": 8 } ], "Name": "myEventWindowName", "AssociationTarget": { "InstanceIds": [ "i-0abcdef1234567890", "i-0be35f9acb8ba01f0" ], "Tags": [], "DedicatedHostIds": [] }, "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1" } ] } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.**Example 3: To modify the cron expression of an event window**The following `modify-instance-event-window`example modifies the cron expression of an event window. Specify the`cron-expression`parameter to modify the cron expression. You can't also specify the`time-range`parameter.`aws ec2 modify-instance-event-window \ --region``us-east-1`\ --instance-event-window-id`iew-0abcdef1234567890`\ --cron-expression`"* 21-23 * * 2,3"`Output: `{ "InstanceEventWindow": { "InstanceEventWindowId": "iew-0abcdef1234567890", "Name": "myEventWindowName", "CronExpression": "* 21-23 * * 2,3", "AssociationTarget": { "InstanceIds": [ "i-0abcdef1234567890", "i-0be35f9acb8ba01f0" ], "Tags": [], "DedicatedHostIds": [] }, "State": "creating", "Tags": [ { "Key": "K1", "Value": "V1" } ] } }`For event window constraints, see [Considerations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/event-windows.html#event-windows-considerations)in the Scheduled Events section of the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyInstanceEventWindow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-event-window.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-maintenance-options`.

- **AWS CLI**
- 
            
                    **Example 1: To disable the recovery behavior of an instance**The following `modify-instance-maintenance-options`example disables simplified automatic recovery for a running or stopped instance.`aws ec2 modify-instance-maintenance-options \ --instance-id``i-0abcdef1234567890`\ --auto-recovery`disabled`Output: `{ "InstanceId": "i-0abcdef1234567890", "AutoRecovery": "disabled" }`For more information, see [Configure simplified automatic recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-configuration-recovery.html)in the*Amazon EC2 User Guide*.**Example 2: To set the recovery behavior of an instance to default**The following `modify-instance-maintenance-options`example sets the automatic recovery behavior to default which enables simplified automatic recovery for supported instance types.`aws ec2 modify-instance-maintenance-options \ --instance-id``i-0abcdef1234567890`\ --auto-recovery`default`Output: `{ "InstanceId": "i-0abcdef1234567890", "AutoRecovery": "default" }`For more information, see [Configure simplified automatic recovery](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-configuration-recovery.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyInstanceMaintenanceOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-maintenance-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-metadata-options`.

- **AWS CLI**
- 
            
                    **Example 1: To enable IMDSv2**The following `modify-instance-metadata-options`example configures the use of IMDSv2 on the specified instance.`aws ec2 modify-instance-metadata-options \ --instance-id``i-1234567898abcdef0`\ --http-tokens`required`\ --http-endpoint`enabled`Output: `{ "InstanceId": "i-1234567898abcdef0", "InstanceMetadataOptions": { "State": "pending", "HttpTokens": "required", "HttpPutResponseHopLimit": 1, "HttpEndpoint": "enabled" } }`For more information, see [Instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)in the*Amazon EC2 User Guide*.**Example 2: To disable instance metadata**The following `modify-instance-metadata-options`example disables the use of all versions of instance metadata on the specified instance.`aws ec2 modify-instance-metadata-options \ --instance-id``i-1234567898abcdef0`\ --http-endpoint`disabled`Output: `{ "InstanceId": "i-1234567898abcdef0", "InstanceMetadataOptions": { "State": "pending", "HttpTokens": "required", "HttpPutResponseHopLimit": 1, "HttpEndpoint": "disabled" } }`For more information, see [Instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)in the*Amazon EC2 User Guide*.**Example 3: To enable instance metadata IPv6 endpoint for your instance**The following `modify-instance-metadata-options`example shows you how to turn on the IPv6 endpoint for the instance metadata service. By default, the IPv6 endpoint is disabled. This is true even if you have launched an instance into an IPv6-only subnet. The IPv6 endpoint for IMDS is only accessible on instances built on the Nitro System.`aws ec2 modify-instance-metadata-options \ --instance-id``i-1234567898abcdef0`\ --http-protocol-ipv6`enabled`\ --http-endpoint`enabled`Output: `{ "InstanceId": "i-1234567898abcdef0", "InstanceMetadataOptions": { "State": "pending", "HttpTokens": "required", "HttpPutResponseHopLimit": 1, "HttpEndpoint": "enabled", HttpProtocolIpv6": "enabled" } }`For more information, see [Instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyInstanceMetadataOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-metadata-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-instance-placement`.

- **AWS CLI**
- 
            
                    **Example 1: To remove an instance's affinity with a Dedicated Host**The following `modify-instance-placement`example removes an instance's affinity with a Dedicated Host and enables it to launch on any available Dedicated Host in your account that supports its instance type.`aws ec2 modify-instance-placement \ --instance-id``i-0e6ddf6187EXAMPLE`\ --affinity`default`Output: `{ "Return": true }`**Example 2: To establish affinity between an instance and the specified Dedicated Host**The following `modify-instance-placement`example establishes a launch relationship between an instance and a Dedicated Host. The instance is only able to run on the specified Dedicated Host.`aws ec2 modify-instance-placement \ --instance-id``i-0e6ddf6187EXAMPLE`\ --affinity`host`\ --host-id`i-0e6ddf6187EXAMPLE`Output: `{ "Return": true }`**Example 3: To move an instance to a placement group**The following `modify-instance-placement`example moves an instance to a placement group, stop the instance, modify the instance placement, and then restart the instance.`aws ec2 stop-instances \ --instance-ids``i-0123a456700123456``aws``ec2``modify-instance-placement`\ --instance-id`i-0123a456700123456`\ --group-name`MySpreadGroup``aws``ec2``start-instances`\ --instance-ids`i-0123a456700123456`**Example 4: To remove an instance from a placement group**The following `modify-instance-placement`example removes an instance from a placement group by stopping the instance, modifying the instance placement, and then restarting the instance. The following example specifies an empty string ("") for the placement group name to indicate that the instance is not to be located in a placement group.Stop the instance: `aws ec2 stop-instances \ --instance-ids``i-0123a456700123456`Modify the placement (Windows Command Prompt): `aws ec2 modify-instance-placement \ --instance-id``i-0123a456700123456`\ --group-name ""Modify the placement (Windows PowerShell, Linux, and macOS): `aws ec2 modify-instance-placement````--instance-id`i-0123a456700123456````--group-name ''Restart the instance: `aws ec2 start-instances \ --instance-ids``i-0123a456700123456`Output: `{ "Return": true }`For more information, see [Modify Dedicated Host tenancy and affinity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/moving-instances-dedicated-hosts.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyInstancePlacement](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-placement.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-ipam-pool`.

- **AWS CLI**
- 
            
                    **To modify an IPAM pool**The following `modify-ipam-pool`example modifies an IPAM pool.(Linux): `aws ec2 modify-ipam-pool \ --ipam-pool-id``ipam-pool-0533048da7d823723`\ --add-allocation-resource-tags`"Key=Owner,Value=Build Team"`\ --clear-allocation-default-netmask-length \ --allocation-min-netmask-length`14`(Windows): `aws ec2 modify-ipam-pool``^`--ipam-pool-id`ipam-pool-0533048da7d823723``^`--add-allocation-resource-tags`"Key=Owner,Value=Build Team"``^`--clear-allocation-default-netmask-length`^`--allocation-min-netmask-length`14`Output: `{ "IpamPool": { "OwnerId": "123456789012", "IpamPoolId": "ipam-pool-0533048da7d823723", "IpamPoolArn": "arn:aws:ec2::123456789012:ipam-pool/ipam-pool-0533048da7d823723", "IpamScopeArn": "arn:aws:ec2::123456789012:ipam-scope/ipam-scope-02fc38cd4c48e7d38", "IpamScopeType": "private", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "Locale": "None", "PoolDepth": 1, "State": "modify-complete", "AutoImport": true, "AddressFamily": "ipv4", "AllocationMinNetmaskLength": 14, "AllocationMaxNetmaskLength": 26, "AllocationResourceTags": [ { "Key": "Environment", "Value": "Preprod" }, { "Key": "Owner", "Value": "Build Team" } ] } }`For more information, see [Edit a pool](https://docs.aws.amazon.com/vpc/latest/ipam/mod-pool-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [ModifyIpamPool](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam-pool.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-ipam-resource-cidr`.

- **AWS CLI**
- 
            
                    **To modify the CIDR allocated to a resource**The following `modify-ipam-resource-cidr`example modifies a resource CIDR.(Linux): `aws ec2 modify-ipam-resource-cidr \ --current-ipam-scope-id``ipam-scope-02fc38cd4c48e7d38`\ --destination-ipam-scope-id`ipam-scope-0da34c61fd189a141`\ --resource-id`vpc-010e1791024eb0af9`\ --resource-cidr`10.0.1.0/24`\ --resource-region`us-east-1`\ --monitored(Windows): `aws ec2 modify-ipam-resource-cidr``^`--current-ipam-scope-id`ipam-scope-02fc38cd4c48e7d38``^`--destination-ipam-scope-id`ipam-scope-0da34c61fd189a141``^`--resource-id`vpc-010e1791024eb0af9``^`--resource-cidr`10.0.1.0/24``^`--resource-region`us-east-1``^`--monitoredOutput: `{ "IpamResourceCidr": { "IpamId": "ipam-08440e7a3acde3908", "IpamScopeId": "ipam-scope-0da34c61fd189a141", "IpamPoolId": "ipam-pool-0533048da7d823723", "ResourceRegion": "us-east-1", "ResourceOwnerId": "123456789012", "ResourceId": "vpc-010e1791024eb0af9", "ResourceCidr": "10.0.1.0/24", "ResourceType": "vpc", "ResourceTags": [ { "Key": "Environment", "Value": "Preprod" }, { "Key": "Owner", "Value": "Build Team" } ], "IpUsage": 0.0, "ComplianceStatus": "noncompliant", "ManagementState": "managed", "OverlapStatus": "overlapping", "VpcId": "vpc-010e1791024eb0af9" } }`For more information on moving resources, see [Move resource CIDRs between scopes](https://docs.aws.amazon.com/vpc/latest/ipam/move-resource-ipam.html)in the*Amazon VPC IPAM User Guide*.For more information on changing monitoring states, see [Change the monitoring state of resource CIDRs](https://docs.aws.amazon.com/vpc/latest/ipam/change-monitoring-state-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [ModifyIpamResourceCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam-resource-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-ipam-resource-discovery`.

- **AWS CLI**
- 
            
                    **To modify the operating regions of a resource discovery**In this example, you're an IPAM delegated admin who wants to modify the operating regions of a resource discovery. To complete this request: You cannot modify a default resource discovery and you must be the owner of the resource discovery.You need the resource discovery ID, which you can get with [describe-ipam-resource-discoveries](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-resource-discoveries.html).The following `modify-ipam-resource-discovery`example modifies a non-default resource discovery in your AWS account.`aws ec2 modify-ipam-resource-discovery \ --ipam-resource-discovery-id``ipam-res-disco-0f4ef577a9f37a162`\ --add-operating-regions RegionName='us-west-1' \ --remove-operating-regions RegionName='us-east-2' \ --region`us-east-1`Output: `{ "IpamResourceDiscovery": { "OwnerId": "149977607591", "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe", "IpamResourceDiscoveryArn": "arn:aws:ec2::149977607591:ipam-resource-discovery/ipam-res-disco-0365d2977fc1672fe", "IpamResourceDiscoveryRegion": "us-east-1", "Description": "Example", "OperatingRegions": [ { "RegionName": "us-east-1" }, { "RegionName": "us-west-1" } ], "IsDefault": false, "State": "modify-in-progress" } }`For more information, see [Work with resource discoveries](https://docs.aws.amazon.com/vpc/latest/ipam/res-disc-work-with.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [ModifyIpamResourceDiscovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam-resource-discovery.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-ipam-scope`.

- **AWS CLI**
- 
            
                    **To modify the description of a scope**In this scenario, you're an IPAM delegated admin who wants to modify the description of an IPAM scope. To complete this request, you'll need the scope ID, which you can get with [describe-ipam-scopes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-scopes.html).The following `modify-ipam-scope`example updates the description of the scope.`aws ec2 modify-ipam-scope \ --ipam-scope-id``ipam-scope-0d3539a30b57dcdd1`\ --description`example`\ --region`us-east-1`Output: `{ "IpamScope": { "OwnerId": "320805250157", "IpamScopeId": "ipam-scope-0d3539a30b57dcdd1", "IpamScopeArn": "arn:aws:ec2::320805250157:ipam-scope/ipam-scope-0d3539a30b57dcdd1", "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-005f921c17ebd5107", "IpamRegion": "us-east-1", "IpamScopeType": "public", "IsDefault": true, "Description": "example", "PoolCount": 1, "State": "modify-in-progress" } }`For more information about scopes, see [How IPAM works](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [ModifyIpamScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-ipam`.

- **AWS CLI**
- 
            
                    **To modify an IPAM**The following `modify-ipam`example modifies an IPAM by adding an Operating Region.(Linux): `aws ec2 modify-ipam \ --ipam-id``ipam-08440e7a3acde3908`\ --add-operating-regions`RegionName=us-west-2`(Windows): `aws ec2 modify-ipam``^`--ipam-id`ipam-08440e7a3acde3908``^`--add-operating-regions`RegionName=us-west-2`Output: `{ "Ipam": { "OwnerId": "123456789012", "IpamId": "ipam-08440e7a3acde3908", "IpamArn": "arn:aws:ec2::123456789012:ipam/ipam-08440e7a3acde3908", "IpamRegion": "us-east-1", "PublicDefaultScopeId": "ipam-scope-0b9eed026396dbc16", "PrivateDefaultScopeId": "ipam-scope-02fc38cd4c48e7d38", "ScopeCount": 3, "OperatingRegions": [ { "RegionName": "us-east-1" }, { "RegionName": "us-east-2" }, { "RegionName": "us-west-1" }, { "RegionName": "us-west-2" } ], "State": "modify-in-progress" } }`- 
                    For API details, see [ModifyIpam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-ipam.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-launch-template`.

- **AWS CLI**
- 
            
                    **To change the default launch template version**This example specifies version 2 of the specified launch template as the default version. Command: `aws ec2 modify-launch-template --launch-template-id``lt-0abcd290751193123`--default-version`2`Output: `{ "LaunchTemplate": { "LatestVersionNumber": 2, "LaunchTemplateId": "lt-0abcd290751193123", "LaunchTemplateName": "WebServers", "DefaultVersionNumber": 2, "CreatedBy": "arn:aws:iam::123456789012:root", "CreateTime": "2017-12-01T13:35:46.000Z" } }`- 
                    For API details, see [ModifyLaunchTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-launch-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-managed-prefix-list`.

- **AWS CLI**
- 
            
                    **To modify a prefix list**The following `modify-managed-prefix-list`example adds an entry to the specified prefix list.`aws ec2 modify-managed-prefix-list \ --prefix-list-id``pl-0123456abcabcabc1`\ --add-entries`Cidr=10.1.0.0/16,Description=vpc-c`\ --current-version`1`Output: `{ "PrefixList": { "PrefixListId": "pl-0123456abcabcabc1", "AddressFamily": "IPv4", "State": "modify-in-progress", "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456abcabcabc1", "PrefixListName": "vpc-cidrs", "MaxEntries": 10, "Version": 1, "OwnerId": "123456789012" } }`For more information, see [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [ModifyManagedPrefixList](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-managed-prefix-list.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-network-interface-attribute`.

- **AWS CLI**
- 
            
                    **To modify the attachment attribute of a network interface**This example command modifies the `attachment`attribute of the specified network interface.Command: `aws ec2 modify-network-interface-attribute --network-interface-id``eni-686ea200`--attachment`AttachmentId=eni-attach-43348162,DeleteOnTermination=false`**To modify the description attribute of a network interface**This example command modifies the `description`attribute of the specified network interface.Command: `aws ec2 modify-network-interface-attribute --network-interface-id``eni-686ea200`--description`"My description"`**To modify the groupSet attribute of a network interface**This example command modifies the `groupSet`attribute of the specified network interface.Command: `aws ec2 modify-network-interface-attribute --network-interface-id``eni-686ea200`--groups`sg-903004f8``sg-1a2b3c4d`**To modify the sourceDestCheck attribute of a network interface**This example command modifies the `sourceDestCheck`attribute of the specified network interface.Command: `aws ec2 modify-network-interface-attribute --network-interface-id``eni-686ea200`--no-source-dest-check- 
                    For API details, see [ModifyNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-network-interface-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-private-dns-name-options`.

- **AWS CLI**
- 
            
                    **To modify the options for instance hostnames**The following `modify-private-dns-name-options`example disables the option to respond to DNS queries for instance hostnames with DNS A records.`aws ec2 modify-private-dns-name-options \ --instance-id``i-1234567890abcdef0`\ --no-enable-resource-name-dns-a-recordOutput: `{ "Return": true }`For more information, see [Amazon EC2 instance hostname types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-naming.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifyPrivateDnsNameOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-private-dns-name-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-reserved-instances`.

- **AWS CLI**
- 
            
                    **To modify Reserved Instances**This example command moves a Reserved Instance to another Availability Zone in the same region. Command: `aws ec2 modify-reserved-instances --reserved-instances-ids``b847fa93-e282-4f55-b59a-1342f5bd7c02`--target-configurations`AvailabilityZone=us-west-1c,Platform=EC2-Classic,InstanceCount=10`Output: `{ "ReservedInstancesModificationId": "rimod-d3ed4335-b1d3-4de6-ab31-0f13aaf46687" }`**To modify the network platform of Reserved Instances**This example command converts EC2-Classic Reserved Instances to EC2-VPC. Command: `aws ec2 modify-reserved-instances --reserved-instances-ids``f127bd27-edb7-44c9-a0eb-0d7e09259af0`--target-configurations`AvailabilityZone=us-west-1c,Platform=EC2-VPC,InstanceCount=5`Output: `{ "ReservedInstancesModificationId": "rimod-82fa9020-668f-4fb6-945d-61537009d291" }`For more information, see Modifying Your Reserved Instances in the *Amazon EC2 User Guide*.**To modify the instance size of Reserved Instances**This example command modifies a Reserved Instance that has 10 m1.small Linux/UNIX instances in us-west-1c so that 8 m1.small instances become 2 m1.large instances, and the remaining 2 m1.small become 1 m1.medium instance in the same Availability Zone. Command: `aws ec2 modify-reserved-instances --reserved-instances-ids``1ba8e2e3-3556-4264-949e-63ee671405a9`--target-configurations`AvailabilityZone=us-west-1c,Platform=EC2-Classic,InstanceCount=2,InstanceType=m1.large``AvailabilityZone=us-west-1c,Platform=EC2-Classic,InstanceCount=1,InstanceType=m1.medium`Output: `{ "ReservedInstancesModificationId": "rimod-acc5f240-080d-4717-b3e3-1c6b11fa00b6" }`For more information, see Modifying the Instance Size of Your Reservations in the *Amazon EC2 User Guide*.- 
                    For API details, see [ModifyReservedInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-reserved-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-security-group-rules`.

- **AWS CLI**
- 
            
                    **To modify a security group rules to update the rule description, the IP protocol, and the CidrIpv4 address range**The following `modify-security-group-rules`example updates the description, the IP protocol, and the IPV4 CIDR range of a specified security group rule. Use the`security-group-rules`parameter to enter the updates for the specified security group rules.`-1`specifies all protocols.`aws ec2 modify-security-group-rules \ --group-id``sg-1234567890abcdef0`\ --security-group-rules SecurityGroupRuleId=sgr-abcdef01234567890,SecurityGroupRule='{Description=test,IpProtocol=-1,CidrIpv4=0.0.0.0/0}'Output: `{ "Return": true }`For more information about security group rules, see [Security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ModifySecurityGroupRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-security-group-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-snapshot-attribute`.

- **AWS CLI**
- 
            
                    **Example 1: To modify a snapshot attribute**The following `modify-snapshot-attribute`example updates the`createVolumePermission`attribute for the specified snapshot, removing volume permissions for the specified user.`aws ec2 modify-snapshot-attribute \ --snapshot-id``snap-1234567890abcdef0`\ --attribute`createVolumePermission`\ --operation-type`remove`\ --user-ids`123456789012`**Example 2: To make a snapshot public**The following `modify-snapshot-attribute`example makes the specified snapshot public.`aws ec2 modify-snapshot-attribute \ --snapshot-id``snap-1234567890abcdef0`\ --attribute`createVolumePermission`\ --operation-type`add`\ --group-names`all`- 
                    For API details, see [ModifySnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-snapshot-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-snapshot-tier`.

- **AWS CLI**
- 
            
                    **To archive a snapshot**The following `modify-snapshot-tier`example archives the specified snapshot. The`TieringStartTime`response parameter indicates the date and time at which the archive process was started, in UTC time format (YYYY-MM-DDTHH:MM:SSZ).`aws ec2 modify-snapshot-tier \ --snapshot-id``snap-01234567890abcedf`\ --storage-tier`archive`Output: `{ "SnapshotId": "snap-01234567890abcedf", "TieringStartTime": "2021-09-15T16:44:37.574Z" }`For more information about snapshot archiving, see [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [ModifySnapshotTier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-snapshot-tier.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-spot-fleet-request`.

- **AWS CLI**
- 
            
                    **To modify a Spot fleet request**This example command updates the target capacity of the specified Spot fleet request. Command: `aws ec2 modify-spot-fleet-request --target-capacity``20`--spot-fleet-request-id`sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`Output: `{ "Return": true }`This example command decreases the target capacity of the specified Spot fleet request without terminating any Spot Instances as a result. Command: `aws ec2 modify-spot-fleet-request --target-capacity``10`--excess-capacity-termination-policy`NoTermination`--spot-fleet-request-id`sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE`Output: `{ "Return": true }`- 
                    For API details, see [ModifySpotFleetRequest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-spot-fleet-request.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-subnet-attribute`.

- **AWS CLI**
- 
            
                    **To change a subnet's public IPv4 addressing behavior**This example modifies subnet-1a2b3c4d to specify that all instances launched into this subnet are assigned a public IPv4 address. If the command succeeds, no output is returned. Command: `aws ec2 modify-subnet-attribute --subnet-id``subnet-1a2b3c4d`--map-public-ip-on-launch**To change a subnet's IPv6 addressing behavior**This example modifies subnet-1a2b3c4d to specify that all instances launched into this subnet are assigned an IPv6 address from the range of the subnet. Command: `aws ec2 modify-subnet-attribute --subnet-id``subnet-1a2b3c4d`--assign-ipv6-address-on-creationFor more information, see IP Addressing in Your VPC in the *AWS Virtual Private Cloud User Guide*.- 
                    For API details, see [ModifySubnetAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-subnet-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-traffic-mirror-filter-network-services`.

- **AWS CLI**
- 
            
                    **To add network services to a Traffic Mirror filter**The following `modify-traffic-mirror-filter-network-services`example adds the Amazon DNS network services to the specified filter.`aws ec2 modify-traffic-mirror-filter-network-services \ --traffic-mirror-filter-id``tmf-04812ff784EXAMPLE`\ --add-network-service`amazon-dns`Output: `{ "TrafficMirrorFilter": { "Tags": [ { "Key": "Name", "Value": "Production" } ], "EgressFilterRules": [], "NetworkServices": [ "amazon-dns" ], "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE", "IngressFilterRules": [ { "SourceCidrBlock": "0.0.0.0/0", "RuleNumber": 1, "DestinationCidrBlock": "0.0.0.0/0", "Description": "TCP Rule", "Protocol": 6, "TrafficDirection": "ingress", "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE", "RuleAction": "accept", "TrafficMirrorFilterRuleId": "tmf-04812ff784EXAMPLE" } ] } }`For more information, see [Modify Traffic Mirror Filter Network Services](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html#modify-traffic-mirroring-filter-network-services)in the*AWS Traffic Mirroring Guide*.- 
                    For API details, see [ModifyTrafficMirrorFilterNetworkServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-filter-network-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-traffic-mirror-filter-rule`.

- **AWS CLI**
- 
            
                    **To modify a traffic mirror filter rule**The following `modify-traffic-mirror-filter-rule`example modifies the description of the specified traffic mirror filter rule.`aws ec2 modify-traffic-mirror-filter-rule \ --traffic-mirror-filter-rule-id``tmfr-0ca76e0e08EXAMPLE`\ --description`"TCP Rule"`Output: `{ "TrafficMirrorFilterRule": { "TrafficMirrorFilterRuleId": "tmfr-0ca76e0e08EXAMPLE", "TrafficMirrorFilterId": "tmf-0293f26e86EXAMPLE", "TrafficDirection": "ingress", "RuleNumber": 100, "RuleAction": "accept", "Protocol": 6, "DestinationCidrBlock": "10.0.0.0/24", "SourceCidrBlock": "10.0.0.0/24", "Description": "TCP Rule" } }`For more information, see [Modify Your Traffic Mirror Filter Rules](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filter.html#modify-traffic-mirroring-filter-rules)in the*AWS Traffic Mirroring Guide*.- 
                    For API details, see [ModifyTrafficMirrorFilterRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-filter-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-traffic-mirror-session`.

- **AWS CLI**
- 
            
                    **To modify a traffic mirror session**The following `modify-traffic-mirror-session`example changes the traffic mirror session description and the number of packets to mirror.`aws ec2 modify-traffic-mirror-session \ --description``"Change packet length"`\ --traffic-mirror-session-id`tms-08a33b1214EXAMPLE`\ --remove-fields`"packet-length"`Output: `{ "TrafficMirrorSession": { "TrafficMirrorSessionId": "tms-08a33b1214EXAMPLE", "TrafficMirrorTargetId": "tmt-07f75d8feeEXAMPLE", "TrafficMirrorFilterId": "tmf-04812ff784EXAMPLE", "NetworkInterfaceId": "eni-070203f901EXAMPLE", "OwnerId": "111122223333", "SessionNumber": 1, "VirtualNetworkId": 7159709, "Description": "Change packet length", "Tags": [] } }`For more information, see [Modify your traffic mirror session](https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html#modify-traffic-mirroring-session)in the*Traffic Mirroring Guide*.- 
                    For API details, see [ModifyTrafficMirrorSession](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-traffic-mirror-session.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-transit-gateway-prefix-list-reference`.

- **AWS CLI**
- 
            
                    **To modify a reference to a prefix list**The following `modify-transit-gateway-prefix-list-reference`example modifies the prefix list reference in the specified route table by changing the attachment to which traffic is routed.`aws ec2 modify-transit-gateway-prefix-list-reference \ --transit-gateway-route-table-id``tgw-rtb-0123456789abcd123`\ --prefix-list-id`pl-11111122222222333`\ --transit-gateway-attachment-id`tgw-attach-aabbccddaabbccaab`Output: `{ "TransitGatewayPrefixListReference": { "TransitGatewayRouteTableId": "tgw-rtb-0123456789abcd123", "PrefixListId": "pl-11111122222222333", "PrefixListOwnerId": "123456789012", "State": "modifying", "Blackhole": false, "TransitGatewayAttachment": { "TransitGatewayAttachmentId": "tgw-attach-aabbccddaabbccaab", "ResourceType": "vpc", "ResourceId": "vpc-112233445566aabbc" } } }`For more information, see [Prefix list references](https://docs.aws.amazon.com/vpc/latest/tgw/create-prefix-list-reference.html)in the*Transit Gateways Guide*.- 
                    For API details, see [ModifyTransitGatewayPrefixListReference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway-prefix-list-reference.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-transit-gateway-vpc-attachment`.

- **AWS CLI**
- 
            
                    **To modify a transit gateway VPC attachment**The following `modify-transit-gateway-vpc-attachment`example adds a subnet to the specified transit gateway VPC attachment.`aws ec2 modify-transit-gateway-vpc-attachment \ --transit-gateway-attachment-id``tgw-attach-09fbd47ddfEXAMPLE`\ --add-subnet-ids`subnet-0e51f45802EXAMPLE`Output: `{ "TransitGatewayVpcAttachment": { "TransitGatewayAttachmentId": "tgw-attach-09fbd47ddfEXAMPLE", "TransitGatewayId": "tgw-0560315ccfEXAMPLE", "VpcId": "vpc-5eccc927", "VpcOwnerId": "111122223333", "State": "modifying", "SubnetIds": [ "subnet-0e51f45802EXAMPLE", "subnet-1EXAMPLE" ], "CreationTime": "2019-08-08T16:47:38.000Z", "Options": { "DnsSupport": "enable", "Ipv6Support": "disable" } } }`For more information, see [Transit gateway attachments to a VPC](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html)in the*Transit Gateways Guide*.- 
                    For API details, see [ModifyTransitGatewayVpcAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway-vpc-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-transit-gateway`.

- **AWS CLI**
- 
            
                    **To modify a transit gateway**The following `modify-transit-gateway`example modifies the specified transit gateway by enabling ECMP support for VPN attachments.`aws ec2 modify-transit-gateway \ --transit-gateway-id``tgw-111111222222aaaaa`\ --options`VpnEcmpSupport=enable`Output: `{ "TransitGateway": { "TransitGatewayId": "tgw-111111222222aaaaa", "TransitGatewayArn": "64512", "State": "modifying", "OwnerId": "123456789012", "CreationTime": "2020-04-30T08:41:37.000Z", "Options": { "AmazonSideAsn": 64512, "AutoAcceptSharedAttachments": "disable", "DefaultRouteTableAssociation": "enable", "AssociationDefaultRouteTableId": "tgw-rtb-0123456789abcd123", "DefaultRouteTablePropagation": "enable", "PropagationDefaultRouteTableId": "tgw-rtb-0123456789abcd123", "VpnEcmpSupport": "enable", "DnsSupport": "enable" } } }`For more information, see [Transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html)in the*Transit Gateways Guide*.- 
                    For API details, see [ModifyTransitGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-transit-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-verified-access-endpoint-policy`.

- **AWS CLI**
- 
            
                    **To configure the Verified Access policy for an endpoint**The following `modify-verified-access-endpoint-policy`example adds the specified Verified Access policy to the specified Verified Access endpoint.`aws ec2 modify-verified-access-endpoint-policy \ --verified-access-endpoint-id``vae-066fac616d4d546f2`\ --policy-enabled \ --policy-document`file://policy.txt`Contents of `policy.txt`:`permit(principal,action,resource) when { context.identity.groups.contains("finance") && context.identity.email.verified == true };`Output: `{ "PolicyEnabled": true, "PolicyDocument": "permit(principal,action,resource)\nwhen {\n context.identity.groups.contains(\"finance\") &&\n context.identity.email_verified == true\n};" }`For more information, see [Verified Access policies](https://docs.aws.amazon.com/verified-access/latest/ug/auth-policies.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [ModifyVerifiedAccessEndpointPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-endpoint-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-verified-access-endpoint`.

- **AWS CLI**
- 
            
                    **To modify the configuration of a Verified Access endpoint**The following `modify-verified-access-endpoint`example adds the specified description to the specified Verified Access endpoint.`aws ec2 modify-verified-access-endpoint \ --verified-access-endpoint-id``vae-066fac616d4d546f2`\ --description '`Testing Verified Access`'Output: `{ "VerifiedAccessEndpoint": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessEndpointId": "vae-066fac616d4d546f2", "ApplicationDomain": "example.com", "EndpointType": "network-interface", "AttachmentType": "vpc", "DomainCertificateArn": "arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE", "EndpointDomain": "my-ava-app.edge-00c3372d53b1540bb.vai-0ce000c0b7643abea.prod.verified-access.us-east-2.amazonaws.com", "SecurityGroupIds": [ "sg-004915970c4c8f13a" ], "NetworkInterfaceOptions": { "NetworkInterfaceId": "eni-0aec70418c8d87a0f", "Protocol": "https", "Port": 443 }, "Status": { "Code": "updating" }, "Description": "Testing Verified Access", "CreationTime": "2023-08-25T20:54:43", "LastUpdatedTime": "2023-08-25T22:46:32" } }`For more information, see [Verified Access endpoints](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [ModifyVerifiedAccessEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-verified-access-group-policy`.

- **AWS CLI**
- 
            
                    **To configure a Verified Access policy for a group**The following `modify-verified-access-group-policy`example adds the specified Verified Access policy to the specified Verified Access group.`aws ec2 modify-verified-access-group-policy \ --verified-access-group-id``vagr-0dbe967baf14b7235`\ --policy-enabled \ --policy-document`file://policy.txt`Contents of `policy.txt`:`permit(principal,action,resource) when { context.identity.groups.contains("finance") && context.identity.email.verified == true };`Output: `{ "PolicyEnabled": true, "PolicyDocument": "permit(principal,action,resource)\nwhen {\n context.identity.groups.contains(\"finance\") &&\n context.identity.email_verified == true\n};" }`For more information, see [Verified Access groups](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [ModifyVerifiedAccessGroupPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-group-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-verified-access-group`.

- **AWS CLI**
- 
            
                    **To modify the configuration of a Verified Access group**The following `modify-verified-access-group`example adds the specified description to the specified Verified Access group.`aws ec2 modify-verified-access-group \ --verified-access-group-id``vagr-0dbe967baf14b7235`\ --description`"Testing Verified Access"`Output: `{ "VerifiedAccessGroup": { "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235", "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "Testing Verified Access", "Owner": "123456789012", "VerifiedAccessGroupArn": "arn:aws:ec2:us-east-2:123456789012:verified-access-group/vagr-0dbe967baf14b7235", "CreationTime": "2023-08-25T19:55:19", "LastUpdatedTime": "2023-08-25T22:17:25" } }`For more information, see [Verified Access groups](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-groups.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [ModifyVerifiedAccessGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-verified-access-instance-logging-configuration`.

- **AWS CLI**
- 
            
                    **To enable logging for a Verified Access instance**The following `modify-verified-access-instance-logging-configuration`example enables access logging for the specified Verified Access instance. The logs will be delivered to the specified CloudWatch Logs log group.`aws ec2 modify-verified-access-instance-logging-configuration \ --verified-access-instance-id``vai-0ce000c0b7643abea`\ --access-logs`CloudWatchLogs={Enabled=true,LogGroup=my-log-group}`Output: `{ "LoggingConfiguration": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "AccessLogs": { "S3": { "Enabled": false }, "CloudWatchLogs": { "Enabled": true, "DeliveryStatus": { "Code": "success" }, "LogGroup": "my-log-group" }, "KinesisDataFirehose": { "Enabled": false }, "LogVersion": "ocsf-1.0.0-rc.2", "IncludeTrustContext": false } } }`For more information, see [Verified Access logs](https://docs.aws.amazon.com/verified-access/latest/ug/access-logs.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [ModifyVerifiedAccessInstanceLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-instance-logging-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-verified-access-instance`.

- **AWS CLI**
- 
            
                    **To modify the configuration of a Verified Access instance**The following `modify-verified-access-instance`example adds the specified description to the specified Verified Access instance.`aws ec2 modify-verified-access-instance \ --verified-access-instance-id``vai-0ce000c0b7643abea`\ --description`"Testing Verified Access"`Output: `{ "VerifiedAccessInstance": { "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea", "Description": "Testing Verified Access", "VerifiedAccessTrustProviders": [ { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center" } ], "CreationTime": "2023-08-25T18:27:56", "LastUpdatedTime": "2023-08-25T22:41:04" } }`For more information, see [Verified Access instances](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-instances.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [ModifyVerifiedAccessInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-verified-access-trust-provider`.

- **AWS CLI**
- 
            
                    **To modify the configuration of a Verified Access trust provider**The following `modify-verified-access-trust-provider`example adds the specified description to the specified Verified Access trust provider.`aws ec2 modify-verified-access-trust-provider \ --verified-access-trust-provider-id``vatp-0bb32de759a3e19e7`\ --description`"Testing Verified Access"`Output: `{ "VerifiedAccessTrustProvider": { "VerifiedAccessTrustProviderId": "vatp-0bb32de759a3e19e7", "Description": "Testing Verified Access", "TrustProviderType": "user", "UserTrustProviderType": "iam-identity-center", "PolicyReferenceName": "idc", "CreationTime": "2023-08-25T19:00:38", "LastUpdatedTime": "2023-08-25T19:18:21" } }`For more information, see [Trust providers for Verified Access](https://docs.aws.amazon.com/verified-access/latest/ug/trust-providers.html)in the*AWS Verified Access User Guide*.- 
                    For API details, see [ModifyVerifiedAccessTrustProvider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-verified-access-trust-provider.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-volume-attribute`.

- **AWS CLI**
- 
            
                    **To modify a volume attribute**This example sets the `autoEnableIo`attribute of the volume with the ID`vol-1234567890abcdef0`to`true`. If the command succeeds, no output is returned.Command: `aws ec2 modify-volume-attribute --volume-id``vol-1234567890abcdef0`--auto-enable-io- 
                    For API details, see [ModifyVolumeAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-volume`.

- **AWS CLI**
- 
            
                    **Example 1: To modify a volume by changing its size**The following `modify-volume`example changes the size of the specified volume to 150GB.Command: `aws ec2 modify-volume --size``150`--volume-id`vol-1234567890abcdef0`Output: `{ "VolumeModification": { "TargetSize": 150, "TargetVolumeType": "io1", "ModificationState": "modifying", "VolumeId": " vol-1234567890abcdef0", "TargetIops": 100, "StartTime": "2019-05-17T11:27:19.000Z", "Progress": 0, "OriginalVolumeType": "io1", "OriginalIops": 100, "OriginalSize": 100 } }`**Example 2: To modify a volume by changing its type, size, and IOPS value**The following `modify-volume`example changes the volume type to Provisioned IOPS SSD, sets the target IOPS rate to 10000, and sets the volume size to 350GB.`aws ec2 modify-volume \ --volume-type``io1`\ --iops`10000`\ --size`350`\ --volume-id`vol-1234567890abcdef0`Output: `{ "VolumeModification": { "TargetSize": 350, "TargetVolumeType": "io1", "ModificationState": "modifying", "VolumeId": "vol-0721c1a9d08c93bf6", "TargetIops": 10000, "StartTime": "2019-05-17T11:38:57.000Z", "Progress": 0, "OriginalVolumeType": "gp2", "OriginalIops": 150, "OriginalSize": 50 } }`- 
                    For API details, see [ModifyVolume](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-volume.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-attribute`.

- **AWS CLI**
- 
            
                    **To modify the enableDnsSupport attribute**This example modifies the `enableDnsSupport`attribute. This attribute indicates whether DNS resolution is enabled for the VPC. If this attribute is`true`, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not. If the command succeeds, no output is returned.Command: `aws ec2 modify-vpc-attribute --vpc-id``vpc-a01106c2`--enable-dns-support "{\"Value\":false}"**To modify the enableDnsHostnames attribute**This example modifies the `enableDnsHostnames`attribute. This attribute indicates whether instances launched in the VPC get DNS hostnames. If this attribute is`true`, instances in the VPC get DNS hostnames; otherwise, they do not. If the command succeeds, no output is returned.Command: `aws ec2 modify-vpc-attribute --vpc-id``vpc-a01106c2`--enable-dns-hostnames "{\"Value\":false}"- 
                    For API details, see [ModifyVpcAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-endpoint-connection-notification`.

- **AWS CLI**
- 
            
                    **To modify an endpoint connection notification**This example changes the SNS topic for the specified endpoint connection notification. Command: `aws ec2 modify-vpc-endpoint-connection-notification --connection-notification-id``vpce-nfn-008776de7e03f5abc`--connection-events`Accept``Reject`--connection-notification-arn`arn:aws:sns:us-east-2:123456789012:mytopic`Output: `{ "ReturnValue": true }`- 
                    For API details, see [ModifyVpcEndpointConnectionNotification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-connection-notification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-endpoint-service-configuration`.

- **AWS CLI**
- 
            
                    **To modify an endpoint service configuration**This example changes the acceptance requirement for the specified endpoint service. Command: `aws ec2 modify-vpc-endpoint-service-configuration --service-id``vpce-svc-09222513e6e77dc86`--no-acceptance-requiredOutput: `{ "ReturnValue": true }`- 
                    For API details, see [ModifyVpcEndpointServiceConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-service-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-endpoint-service-payer-responsibility`.

- **AWS CLI**
- 
            
                    **To modify the payer responsibility**The following `modify-vpc-endpoint-service-payer-responsibility`example modifies the payer responsibility of the specified endpoint service.`aws ec2 modify-vpc-endpoint-service-payer-responsibility \ --service-id``vpce-svc-071afff70666e61e0`\ --payer-responsibility`ServiceOwner`This command produces no output. - 
                    For API details, see [ModifyVpcEndpointServicePayerResponsibility](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-service-payer-responsibility.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-endpoint-service-permissions`.

- **AWS CLI**
- 
            
                    **To modify endpoint service permissions**This example adds permission for an AWS account to connect to the specified endpoint service. Command: `aws ec2 modify-vpc-endpoint-service-permissions --service-id``vpce-svc-03d5ebb7d9579a2b3`--add-allowed-principals '`["arn:aws:iam::123456789012:root"]`'Output: `{ "ReturnValue": true }`This example adds permission for a specific IAM user ( `admin`) to connect to the specified endpoint service.Command: `aws ec2 modify-vpc-endpoint-service-permissions --service-id``vpce-svc-03d5ebb7d9579a2b3`--add-allowed-principals '`["arn:aws:iam::123456789012:user/admin"]`'- 
                    For API details, see [ModifyVpcEndpointServicePermissions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint-service-permissions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-endpoint`.

- **AWS CLI**
- 
            
                    **To modify a gateway endpoint**This example modifies gateway endpoint `vpce-1a2b3c4d`by associating route table`rtb-aaa222bb`with the endpoint, and resetting the policy document.Command: `aws ec2 modify-vpc-endpoint --vpc-endpoint-id``vpce-1a2b3c4d`--add-route-table-ids`rtb-aaa222bb`--reset-policyOutput: `{ "Return": true }`**To modify an interface endpoint**This example modifies interface endpoint `vpce-0fe5b17a0707d6fa5`by adding subnet`subnet-d6fcaa8d`to the endpoint.Command: `aws ec2 modify-vpc-endpoint --vpc-endpoint-id``vpce-0fe5b17a0707d6fa5`--add-subnet-id`subnet-d6fcaa8d`Output: `{ "Return": true }`- 
                    For API details, see [ModifyVpcEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-peering-connection-options`.

- **AWS CLI**
- 
            
                    **To enable communication over a VPC peering connection from your local ClassicLink connection**In this example, for peering connection `pcx-aaaabbb`, the owner of the requester VPC modifies the VPC peering connection options to enable a local ClassicLink connection to communicate with the peer VPC.Command: `aws ec2 modify-vpc-peering-connection-options --vpc-peering-connection-id``pcx-aaaabbbb`--requester-peering-connection-options`AllowEgressFromLocalClassicLinkToRemoteVpc=true`Output: `{ "RequesterPeeringConnectionOptions": { "AllowEgressFromLocalClassicLinkToRemoteVpc": true } }`**To enable communication over a VPC peering connection from your local VPC to a remote ClassicLink connection**In this example, the owner of the accepter VPC modifies the VPC peering connection options to enable the local VPC to communicate with the ClassicLink connection in the peer VPC. Command: `aws ec2 modify-vpc-peering-connection-options --vpc-peering-connection-id``pcx-aaaabbbb`--accepter-peering-connection-options`AllowEgressFromLocalVpcToRemoteClassicLink=true`Output: `{ "AccepterPeeringConnectionOptions": { "AllowEgressFromLocalVpcToRemoteClassicLink": true } }`**To enable DNS resolution support for the VPC peering connection**In this example, the owner of the requester VPC modifies the VPC peering connection options for `pcx-aaaabbbb`to enable the local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.Command: `aws ec2 modify-vpc-peering-connection-options --vpc-peering-connection-id``pcx-aaaabbbb`--requester-peering-connection-options`AllowDnsResolutionFromRemoteVpc=true`Output: `{ "RequesterPeeringConnectionOptions": { "AllowDnsResolutionFromRemoteVpc": true } }`- 
                    For API details, see [ModifyVpcPeeringConnectionOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-peering-connection-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpc-tenancy`.

- **AWS CLI**
- 
            
                    **To modify the tenancy of a VPC**This example modifies the tenancy of VPC `vpc-1a2b3c4d`to`default`.Command: `aws ec2 modify-vpc-tenancy --vpc-id``vpc-1a2b3c4d`--instance-tenancy`default`Output: `{ "Return": true }`- 
                    For API details, see [ModifyVpcTenancy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpc-tenancy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpn-connection-options`.

- **AWS CLI**
- 
            
                    **To modify your VPN connection options**The following `modify-vpn-connection-options`example modifies the local IPv4 CIDR on the customer gateway side of the specified VPN connection.`aws ec2 modify-vpn-connection-options \ --vpn-connection-id``vpn-1122334455aabbccd`\ --local-ipv4-network-cidr`10.0.0.0/16`Output: `{ "VpnConnections": [ { "CustomerGatewayConfiguration": "...configuration information...", "CustomerGatewayId": "cgw-01234567abcde1234", "Category": "VPN", "State": "modifying", "Type": "ipsec.1", "VpnConnectionId": "vpn-1122334455aabbccd", "TransitGatewayId": "tgw-00112233445566aab", "Options": { "EnableAcceleration": false, "StaticRoutesOnly": true, "LocalIpv4NetworkCidr": "10.0.0.0/16", "RemoteIpv4NetworkCidr": "0.0.0.0/0", "TunnelInsideIpVersion": "ipv4" }, "Routes": [], "Tags": [ { "Key": "Name", "Value": "CanadaVPN" } ], "VgwTelemetry": [ { "AcceptedRouteCount": 0, "LastStatusChange": "2020-07-29T10:35:11.000Z", "OutsideIpAddress": "203.0.113.3", "Status": "DOWN", "StatusMessage": "" }, { "AcceptedRouteCount": 0, "LastStatusChange": "2020-09-02T09:09:33.000Z", "OutsideIpAddress": "203.0.113.5", "Status": "UP", "StatusMessage": "" } ] } ] }`For more information, see [Modifying Site-to-Site VPN connection options](https://docs.aws.amazon.com/vpn/latest/s2svpn/modify-vpn-connection-options.html)in the*AWS Site-to-Site VPN User Guide*.- 
                    For API details, see [ModifyVpnConnectionOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-connection-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpn-connection`.

- **AWS CLI**
- 
            
                    **To modify a VPN connection**The following `modify-vpn-connection`example changes the target gateway for VPN connection`vpn-12345678901234567`to virtual private gateway`vgw-11223344556677889`:`aws ec2 modify-vpn-connection \ --vpn-connection-id``vpn-12345678901234567`\ --vpn-gateway-id`vgw-11223344556677889`Output: `{ "VpnConnection": { "CustomerGatewayConfiguration": "...configuration information...", "CustomerGatewayId": "cgw-aabbccddee1122334", "Category": "VPN", "State": "modifying", "Type": "ipsec.1", "VpnConnectionId": "vpn-12345678901234567", "VpnGatewayId": "vgw-11223344556677889", "Options": { "StaticRoutesOnly": false }, "VgwTelemetry": [ { "AcceptedRouteCount": 0, "LastStatusChange": "2019-07-17T07:34:00.000Z", "OutsideIpAddress": "18.210.3.222", "Status": "DOWN", "StatusMessage": "IPSEC IS DOWN" }, { "AcceptedRouteCount": 0, "LastStatusChange": "2019-07-20T21:20:16.000Z", "OutsideIpAddress": "34.193.129.33", "Status": "DOWN", "StatusMessage": "IPSEC IS DOWN" } ] } }`- 
                    For API details, see [ModifyVpnConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpn-tunnel-certificate`.

- **AWS CLI**
- 
            
                    **To rotate a VPN tunnel certificate**The following `modify-vpn-tunnel-certificate`example rotates the certificate for the specified tunnel for a VPN connection`aws ec2 modify-vpn-tunnel-certificate \ --vpn-tunnel-outside-ip-address``203.0.113.17`\ --vpn-connection-id`vpn-12345678901234567`Output: `{ "VpnConnection": { "CustomerGatewayConfiguration": ...configuration information..., "CustomerGatewayId": "cgw-aabbccddee1122334", "Category": "VPN", "State": "modifying", "Type": "ipsec.1", "VpnConnectionId": "vpn-12345678901234567", "VpnGatewayId": "vgw-11223344556677889", "Options": { "StaticRoutesOnly": false }, "VgwTelemetry": [ { "AcceptedRouteCount": 0, "LastStatusChange": "2019-09-11T17:27:14.000Z", "OutsideIpAddress": "203.0.113.17", "Status": "DOWN", "StatusMessage": "IPSEC IS DOWN", "CertificateArn": "arn:aws:acm:us-east-1:123456789101:certificate/c544d8ce-20b8-4fff-98b0-example" }, { "AcceptedRouteCount": 0, "LastStatusChange": "2019-09-11T17:26:47.000Z", "OutsideIpAddress": "203.0.114.18", "Status": "DOWN", "StatusMessage": "IPSEC IS DOWN", "CertificateArn": "arn:aws:acm:us-east-1:123456789101:certificate/5ab64566-761b-4ad3-b259-example" } ] } }`- 
                    For API details, see [ModifyVpnTunnelCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-tunnel-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-vpn-tunnel-options`.

- **AWS CLI**
- 
            
                    **To modify the tunnel options for a VPN connection**The following `modify-vpn-tunnel-options`example updates the Diffie-Hellman groups that are permitted for the specified tunnel and VPN connection.`aws ec2 modify-vpn-tunnel-options \ --vpn-connection-id``vpn-12345678901234567`\ --vpn-tunnel-outside-ip-address`203.0.113.17`\ --tunnel-options`Phase1DHGroupNumbers=[{Value=14},{Value=15},{Value=16},{Value=17},{Value=18}],Phase2DHGroupNumbers=[{Value=14},{Value=15},{Value=16},{Value=17},{Value=18}]`Output: `{ "VpnConnection": { "CustomerGatewayConfiguration": "...configuration information...", "CustomerGatewayId": "cgw-aabbccddee1122334", "Category": "VPN", "State": "available", "Type": "ipsec.1", "VpnConnectionId": "vpn-12345678901234567", "VpnGatewayId": "vgw-11223344556677889", "Options": { "StaticRoutesOnly": false, "TunnelOptions": [ { "OutsideIpAddress": "203.0.113.17", "Phase1DHGroupNumbers": [ { "Value": 14 }, { "Value": 15 }, { "Value": 16 }, { "Value": 17 }, { "Value": 18 } ], "Phase2DHGroupNumbers": [ { "Value": 14 }, { "Value": 15 }, { "Value": 16 }, { "Value": 17 }, { "Value": 18 } ] }, { "OutsideIpAddress": "203.0.114.19" } ] }, "VgwTelemetry": [ { "AcceptedRouteCount": 0, "LastStatusChange": "2019-09-10T21:56:54.000Z", "OutsideIpAddress": "203.0.113.17", "Status": "DOWN", "StatusMessage": "IPSEC IS DOWN" }, { "AcceptedRouteCount": 0, "LastStatusChange": "2019-09-10T21:56:43.000Z", "OutsideIpAddress": "203.0.114.19", "Status": "DOWN", "StatusMessage": "IPSEC IS DOWN" } ] } }`- 
                    For API details, see [ModifyVpnTunnelOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-vpn-tunnel-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `monitor-instances`.

- **AWS CLI**
- 
            
                    **To enable detailed monitoring for an instance**This example command enables detailed monitoring for the specified instance. Command: `aws ec2 monitor-instances --instance-ids``i-1234567890abcdef0`Output: `{ "InstanceMonitorings": [ { "InstanceId": "i-1234567890abcdef0", "Monitoring": { "State": "pending" } } ] }`- 
                    For API details, see [MonitorInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/monitor-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `move-address-to-vpc`.

- **AWS CLI**
- 
            
                    **To move an address to EC2-VPC**This example moves Elastic IP address 54.123.4.56 to the EC2-VPC platform. Command: `aws ec2 move-address-to-vpc --public-ip``54.123.4.56`Output: `{ "Status": "MoveInProgress" }`- 
                    For API details, see [MoveAddressToVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/move-address-to-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `move-byoip-cidr-to-ipam`.

- **AWS CLI**
- 
            
                    **To transfer a BYOIP CIDR to IPAM**The following `move-byoip-cidr-to-ipam`example transfers a BYOIP CIDR to IPAM.(Linux): `aws ec2 move-byoip-cidr-to-ipam \ --region``us-west-2`\ --ipam-pool-id`ipam-pool-0a03d430ca3f5c035`\ --ipam-pool-owner`111111111111`\ --cidr`130.137.249.0/24`(Windows): `aws ec2 move-byoip-cidr-to-ipam``^`--region`us-west-2``^`--ipam-pool-id`ipam-pool-0a03d430ca3f5c035``^`--ipam-pool-owner`111111111111``^`--cidr`130.137.249.0/24`Output: `{ "ByoipCidr": { "Cidr": "130.137.249.0/24", "State": "pending-transfer" } }`For more information, see [Tutorial: Transfer an existing BYOIP IPv4 CIDR to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoip-ipam-transfer-ipv4.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [MoveByoipCidrToIpam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/move-byoip-cidr-to-ipam.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `network-insights-access-scope`.

- **AWS CLI**
- 
            
                    **To create Network Insights access scopes**The following `create-network-insights-access-scope`example creates a network insights access scope in your AWS account.`aws ec2 create-network-insights-access-scope \ --cli-input-json``file://access-scope-file.json`Contents of `access-scope-file.json`:`{ { "MatchPaths": [ { "Source": { "ResourceStatement": { "Resources": [ "vpc-abcd12e3" ] } } } ], "ExcludePaths": [ { "Source": { "ResourceStatement": { "ResourceTypes": [ "AWS::EC2::InternetGateway" ] } } } ] } }`Output: `{ "NetworkInsightsAccessScopeAnalysisId": "nisa-123456789111" }{ "NetworkInsightsAccessScope": { "NetworkInsightsAccessScopeId": "nis-123456789222", "NetworkInsightsAccessScopeArn": "arn:aws:ec2:us-east-1:123456789222:network-insights-access-scope/nis-123456789222", "CreatedDate": "2022-01-25T19:20:28.796000+00:00", "UpdatedDate": "2022-01-25T19:20:28.797000+00:00" }, "NetworkInsightsAccessScopeContent": { "NetworkInsightsAccessScopeId": "nis-04c0c0fbca737c404", "MatchPaths": [ { "Source": { "ResourceStatement": { "Resources": [ "vpc-abcd12e3" ] } } } ], "ExcludePaths": [ { "Source": { "ResourceStatement": { "ResourceTypes": [ "AWS::EC2::InternetGateway" ] } } } ] } }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli-naa.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [NetworkInsightsAccessScope](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/network-insights-access-scope.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `provision-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To provision an address range**The following `provision-byoip-cidr`example provisions a public IP address range for use with AWS.`aws ec2 provision-byoip-cidr \ --cidr``203.0.113.25/24`\ --cidr-authorization-context Message="$text_message",Signature="$signed_message"Output: `{ "ByoipCidr": { "Cidr": "203.0.113.25/24", "State": "pending-provision" } }`For more information about creating the messages strings for the authorization context, see [Bring Your Own IP Addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-byoip.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [ProvisionByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/provision-byoip-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `provision-ipam-pool-cidr`.

- **AWS CLI**
- 
            
                    **To provision a CIDR to an IPAM pool**The following `provision-ipam-pool-cidr`example provisions a CIDR to an IPAM pool.(Linux): `aws ec2 provision-ipam-pool-cidr \ --ipam-pool-id``ipam-pool-0533048da7d823723`\ --cidr`10.0.0.0/24`(Windows): `aws ec2 provision-ipam-pool-cidr``^`--ipam-pool-id`ipam-pool-0533048da7d823723``^`--cidr`10.0.0.0/24`Output: `{ "IpamPoolCidr": { "Cidr": "10.0.0.0/24", "State": "pending-provision" } }`For more information, see [Provision CIDRs to a pool](https://docs.aws.amazon.com/vpc/latest/ipam/prov-cidr-ipam.html)in the*Amazon VPC IPAM User Guide*.- 
                    For API details, see [ProvisionIpamPoolCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/provision-ipam-pool-cidr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purchase-host-reservation`.

- **AWS CLI**
- 
            
                    **To purchase a Dedicated Host Reservation**This example purchases the specified Dedicated Host Reservation offering for the specified Dedicated Host in your account. Command: `aws ec2 purchase-host-reservation --offering-id``hro-03f707bf363b6b324`--host-id-set`h-013abcd2a00cbd123`Output: `{ "TotalHourlyPrice": "1.499", "Purchase": [ { "HourlyPrice": "1.499", "InstanceFamily": "m4", "PaymentOption": "NoUpfront", "HostIdSet": [ "h-013abcd2a00cbd123" ], "HostReservationId": "hr-0d418a3a4ffc669ae", "UpfrontPrice": "0.000", "Duration": 31536000 } ], "TotalUpfrontPrice": "0.000" }`- 
                    For API details, see [PurchaseHostReservation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-host-reservation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purchase-reserved-instances-offering`.

- **AWS CLI**
- 
            
                    **To purchase a Reserved Instance offering**This example command illustrates a purchase of a Reserved Instances offering, specifying an offering ID and instance count. Command: `aws ec2 purchase-reserved-instances-offering --reserved-instances-offering-id``ec06327e-dd07-46ee-9398-75b5fexample`--instance-count`3`Output: `{ "ReservedInstancesId": "af9f760e-6f91-4559-85f7-4980eexample" }`- 
                    For API details, see [PurchaseReservedInstancesOffering](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-reserved-instances-offering.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `purchase-scheduled-instances`.

- **AWS CLI**
- 
            
                    **To purchase a Scheduled Instance**This example purchases a Scheduled Instance. Command: `aws ec2 purchase-scheduled-instances --purchase-requests``file://purchase-request.json`Purchase-request.json: `[ { "PurchaseToken": "eyJ2IjoiMSIsInMiOjEsImMiOi...", "InstanceCount": 1 } ]`Output: `{ "ScheduledInstanceSet": [ { "AvailabilityZone": "us-west-2b", "ScheduledInstanceId": "sci-1234-1234-1234-1234-123456789012", "HourlyPrice": "0.095", "CreateDate": "2016-01-25T21:43:38.612Z", "Recurrence": { "OccurrenceDaySet": [ 1 ], "Interval": 1, "Frequency": "Weekly", "OccurrenceRelativeToEnd": false, "OccurrenceUnit": "" }, "Platform": "Linux/UNIX", "TermEndDate": "2017-01-31T09:00:00Z", "InstanceCount": 1, "SlotDurationInHours": 32, "TermStartDate": "2016-01-31T09:00:00Z", "NetworkPlatform": "EC2-VPC", "TotalScheduledInstanceHours": 1696, "NextSlotStartTime": "2016-01-31T09:00:00Z", "InstanceType": "c4.large" } ] }`- 
                    For API details, see [PurchaseScheduledInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-scheduled-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-instances`.

- **AWS CLI**
- 
            
                    **To reboot an Amazon EC2 instance**This example reboots the specified instance. If the command succeeds, no output is returned. Command: `aws ec2 reboot-instances --instance-ids``i-1234567890abcdef5`For more information, see Reboot Your Instance in the *Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [RebootInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reboot-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-image`.

- **AWS CLI**
- 
            
                    **Example 1: To register an AMI using a manifest file**The following `register-image`example registers an AMI using the specified manifest file in Amazon S3.`aws ec2 register-image \ --name``my-image`\ --image-location`amzn-s3-demo-bucket/myimage/image.manifest.xml`Output: `{ "ImageId": "ami-1234567890EXAMPLE" }`For more information, see [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)in the*Amazon EC2 User Guide*.**Example 2: To register an AMI using a snapshot of a root device**The following `register-image`example registers an AMI using the specified snapshot of an EBS root volume as device`/dev/xvda`. The block device mapping also includes an empty 100 GiB EBS volume as device`/dev/xvdf`.`aws ec2 register-image \ --name``my-image`\ --root-device-name`/dev/xvda`\ --block-device-mappings`DeviceName=/dev/xvda,Ebs={SnapshotId=snap-0db2cf683925d191f}``DeviceName=/dev/xvdf,Ebs={VolumeSize=100}`Output: `{ "ImageId": "ami-1a2b3c4d5eEXAMPLE" }`For more information, see [Amazon Machine Images (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [RegisterImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-instance-event-notification-attributes`.

- **AWS CLI**
- 
            
                    **Example 1: To include all tags in event notifications**The following `register-instance-event-notification-attributes`example includes all tags in event notifications.`aws ec2 register-instance-event-notification-attributes \ --instance-tag-attribute``IncludeAllTagsOfInstance=true`Output: `{ "InstanceTagAttribute": { "InstanceTagKeys": [], "IncludeAllTagsOfInstance": true } }`For more information, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html)in the*Amazon EC2 User Guide*.**Example 2: To include specific tags in event notifications**The following `register-instance-event-notification-attributes`example includes the specified tags in event notifications. You cannot specify tags if`IncludeAllTagsOfInstance`is`true`.`aws ec2 register-instance-event-notification-attributes \ --instance-tag-attribute InstanceTagKeys="tag-key1","tag-key2"`Output: `{ "InstanceTagAttribute": { "InstanceTagKeys": [ "tag-key1", "tag-key2" ], "IncludeAllTagsOfInstance": false } }`For more information, see [Scheduled events for your instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [RegisterInstanceEventNotificationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-instance-event-notification-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-transit-gateway-multicase-group-sources`.

- **AWS CLI**
- 
            
                    **To register a source with a transit gateway multicast group.**The following `register-transit-gateway-multicast-group-sources`example registers the specified network interface group source with a multicast group.`aws ec2 register-transit-gateway-multicast-group-sources \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef79d6e597`\ --group-ip-address`224.0.1.0`\ --network-interface-ids`eni-07f290fc3c090cbae`Output: `{ "RegisteredMulticastGroupSources": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef79d6e597", "RegisteredNetworkInterfaceIds": [ "eni-07f290fc3c090cbae" ], "GroupIpAddress": "224.0.1.0" } }`For more information, see [Register Sources with a Multicast Group](https://docs.aws.amazon.com/vpc/latest/tgw/working-with-multicast.html#add-source-multicast-group)in the*AWS Transit Gateways User Guide*.- 
                    For API details, see [RegisterTransitGatewayMulticaseGroupSources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-transit-gateway-multicase-group-sources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-transit-gateway-multicast-group-members`.

- **AWS CLI**
- 
            
                    **To view the information about the transit gateway multicast domain associations**The following `register-transit-gateway-multicast-group-members`example returns the associations for the specified multicast domain.`aws ec2 register-transit-gateway-multicast-group-members \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef79d6e597`\ --group-ip-address`224.0.1.0`\ --network-interface-ids`eni-0e246d32695012e81`Output: `{ "RegisteredMulticastGroupMembers": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef79d6e597", "RegisteredNetworkInterfaceIds": [ "eni-0e246d32695012e81" ], "GroupIpAddress": "224.0.1.0" } }`For more information, see [Multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-domains-about.html)in the*Transit Gateways User Guide*.- 
                    For API details, see [RegisterTransitGatewayMulticastGroupMembers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-transit-gateway-multicast-group-members.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-transit-gateway-multicast-group-sources`.

- **AWS CLI**
- 
            
                    **To register a source with a transit gateway multicast group.**The following `register-transit-gateway-multicast-group-sources`example registers the specified network interface group source with a multicast group.`aws ec2 register-transit-gateway-multicast-group-sources \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-0c4905cef79d6e597`\ --group-ip-address`224.0.1.0`\ --network-interface-ids`eni-07f290fc3c090cbae`Output: `{ "RegisteredMulticastGroupSources": { "TransitGatewayMulticastDomainId": "tgw-mcast-domain-0c4905cef79d6e597", "RegisteredNetworkInterfaceIds": [ "eni-07f290fc3c090cbae" ], "GroupIpAddress": "224.0.1.0" } }`For more information, see [Multicast domains](https://docs.aws.amazon.com/vpc/latest/tgw/multicast-domains-about.html)in the*Transit Gateways Guide*.- 
                    For API details, see [RegisterTransitGatewayMulticastGroupSources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/register-transit-gateway-multicast-group-sources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-transit-gateway-peering-attachment`.

- **AWS CLI**
- 
            
                    **To reject a transit gateway peering attachment**The following `reject-transit-gateway-peering-attachment`example rejects the specified transit gateway peering attachment request. The`--region`parameter specifies the Region that the accepter transit gateway is located in.`aws ec2 reject-transit-gateway-peering-attachment \ --transit-gateway-attachment-id``tgw-attach-4455667788aabbccd`\ --region`us-east-2`Output: `{ "TransitGatewayPeeringAttachment": { "TransitGatewayAttachmentId": "tgw-attach-4455667788aabbccd", "RequesterTgwInfo": { "TransitGatewayId": "tgw-123abc05e04123abc", "OwnerId": "123456789012", "Region": "us-west-2" }, "AccepterTgwInfo": { "TransitGatewayId": "tgw-11223344aabbcc112", "OwnerId": "123456789012", "Region": "us-east-2" }, "State": "rejecting", "CreationTime": "2019-12-09T11:50:31.000Z" } }`For more information, see [Transit Gateway Peering Attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-peering.html)in the*Transit Gateways Guide*.- 
                    For API details, see [RejectTransitGatewayPeeringAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-transit-gateway-peering-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-transit-gateway-vpc-attachment`.

- **AWS CLI**
- 
            
                    **To reject a transit gateway VPC attachment**The following `reject-transit-gateway-vpc-attachment`example rejects the specified transit gateway VPC attachment.`aws ec2 reject-transit-gateway-vpc-attachment \ --transit-gateway-attachment-id``tgw-attach-0a34fe6b4fEXAMPLE`Output: `{ "TransitGatewayVpcAttachment": { "TransitGatewayAttachmentId": "tgw-attach-0a34fe6b4fEXAMPLE", "TransitGatewayId": "tgw-0262a0e521EXAMPLE", "VpcId": "vpc-07e8ffd50fEXAMPLE", "VpcOwnerId": "111122223333", "State": "pending", "SubnetIds": [ "subnet-0752213d59EXAMPLE" ], "CreationTime": "2019-07-10T17:33:46.000Z", "Options": { "DnsSupport": "enable", "Ipv6Support": "disable" } } }`For more information, see [Transit gateway attachments to a VPC](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html)in the*Transit Gateways Guide*.- 
                    For API details, see [RejectTransitGatewayVpcAttachment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-transit-gateway-vpc-attachment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-transit-gateway-vpc-attachments`.

- **AWS CLI**
- 
            
                    **To reject a transit gateway VPC attachment**The following `reject-transit-gateway-vpc-attachment`example rejects the specified transit gateway VPC attachment.`aws ec2 reject-transit-gateway-vpc-attachment \ --transit-gateway-attachment-id``tgw-attach-0a34fe6b4fEXAMPLE`Output: `{ "TransitGatewayVpcAttachment": { "TransitGatewayAttachmentId": "tgw-attach-0a34fe6b4fEXAMPLE", "TransitGatewayId": "tgw-0262a0e521EXAMPLE", "VpcId": "vpc-07e8ffd50fEXAMPLE", "VpcOwnerId": "111122223333", "State": "pending", "SubnetIds": [ "subnet-0752213d59EXAMPLE" ], "CreationTime": "2019-07-10T17:33:46.000Z", "Options": { "DnsSupport": "enable", "Ipv6Support": "disable" } } }`For more information, see [Transit gateway attachments to a VPC](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html)in the*Transit Gateways Guide*.- 
                    For API details, see [RejectTransitGatewayVpcAttachments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-transit-gateway-vpc-attachments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-vpc-endpoint-connections`.

- **AWS CLI**
- 
            
                    **To reject an interface endpoint connection request**This example rejects the specified endpoint connection request for the specified endpoint service. Command: `aws ec2 reject-vpc-endpoint-connections --service-id``vpce-svc-03d5ebb7d9579a2b3`--vpc-endpoint-ids`vpce-0c1308d7312217abc`Output: `{ "Unsuccessful": [] }`- 
                    For API details, see [RejectVpcEndpointConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-vpc-endpoint-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-vpc-peering-connection`.

- **AWS CLI**
- 
            
                    **To reject a VPC peering connection**This example rejects the specified VPC peering connection request. Command: `aws ec2 reject-vpc-peering-connection --vpc-peering-connection-id``pcx-1a2b3c4d`Output: `{ "Return": true }`- 
                    For API details, see [RejectVpcPeeringConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reject-vpc-peering-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `release-address`.

- **AWS CLI**
- 
            
                    **To release an Elastic IP addresses for EC2-Classic**This example releases an Elastic IP address for use with instances in EC2-Classic. If the command succeeds, no output is returned. Command: `aws ec2 release-address --public-ip``198.51.100.0`**To release an Elastic IP address for EC2-VPC**This example releases an Elastic IP address for use with instances in a VPC. If the command succeeds, no output is returned. Command: `aws ec2 release-address --allocation-id``eipalloc-64d5890a`- 
                    For API details, see [ReleaseAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `release-hosts`.

- **AWS CLI**
- 
            
                    **To release a Dedicated host from your account**To release a Dedicated host from your account. Instances that are on the host must be stopped or terminated before the host can be released. Command: `aws ec2 release-hosts --host-id=h-0029d6e3cacf1b3da`Output: `{ "Successful": [ "h-0029d6e3cacf1b3da" ], "Unsuccessful": [] }`- 
                    For API details, see [ReleaseHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-hosts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `release-ipam-pool-allocation`.

- **AWS CLI**
- 
            
                    **To release an IPAM pool allocation**In this example, you're an IPAM delegated admin who tried to delete an IPAM pool but received an error that you cannot delete the pool while the pool has allocations. You are using this command to release a pool allocation. Note the following: You can only use this command for custom allocations. To remove an allocation for a resource without deleting the resource, set its monitored state to false using [modify-ipam-resource-cidr](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-ipam-resource-cidr.html).To complete this request, you'll need the IPAM pool ID, which you can get with[describe-ipam-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipam-pools.html). You'll also need the allocation ID, which you can get with[get-ipam-pool-allocations](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-ipam-pool-allocations.html).If you do not want to remove allocations one by one, you can use the`--cascade option`when you delete an IPAM pool to automatically release any allocations in the pool before deleting it.There are a number of prerequisites before running this command. For more information, see[Release an allocation](https://docs.aws.amazon.com/vpc/latest/ipam/release-alloc-ipam.html)in the*Amazon VPC IPAM User Guide*.The`--region`in which you run this command must be the locale of the IPAM pool where the allocation is.The following `release-ipam-pool-allocation`example releases an IPAM pool allocation.`aws ec2 release-ipam-pool-allocation \ --ipam-pool-id``ipam-pool-07bdd12d7c94e4693`\ --cidr`10.0.0.0/23`\ --ipam-pool-allocation-id`ipam-pool-alloc-0e66a1f730da54791b99465b79e7d1e89`\ --region`us-west-1`Output: `{ "Success": true }`Once you release an allocation, you may want to run [delete-ipam-pool](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-ipam-pool.html).- 
                    For API details, see [ReleaseIpamPoolAllocation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/release-ipam-pool-allocation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replace-iam-instance-profile-association`.

- **AWS CLI**
- 
            
                    **To replace an IAM instance profile for an instance**This example replaces the IAM instance profile represented by the association `iip-assoc-060bae234aac2e7fa`with the IAM instance profile named`AdminRole`.`aws ec2 replace-iam-instance-profile-association \ --iam-instance-profile``Name=AdminRole`\ --association-id`iip-assoc-060bae234aac2e7fa`Output: `{ "IamInstanceProfileAssociation": { "InstanceId": "i-087711ddaf98f9489", "State": "associating", "AssociationId": "iip-assoc-0b215292fab192820", "IamInstanceProfile": { "Id": "AIPAJLNLDX3AMYZNWYYAY", "Arn": "arn:aws:iam::123456789012:instance-profile/AdminRole" } } }`- 
                    For API details, see [ReplaceIamInstanceProfileAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-iam-instance-profile-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replace-network-acl-association`.

- **AWS CLI**
- 
            
                    **To replace the network ACL associated with a subnet**This example associates the specified network ACL with the subnet for the specified network ACL association. Command: `aws ec2 replace-network-acl-association --association-id``aclassoc-e5b95c8c`--network-acl-id`acl-5fb85d36`Output: `{ "NewAssociationId": "aclassoc-3999875b" }`- 
                    For API details, see [ReplaceNetworkAclAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replace-network-acl-entry`.

- **AWS CLI**
- 
            
                    **To replace a network ACL entry**This example replaces an entry for the specified network ACL. The new rule 100 allows ingress traffic from 203.0.113.12/24 on UDP port 53 (DNS) into any associated subnet. Command: `aws ec2 replace-network-acl-entry --network-acl-id``acl-5fb85d36`--ingress --rule-number`100`--protocol`udp`--port-range`From=53,To=53`--cidr-block`203.0.113.12/24`--rule-action`allow`- 
                    For API details, see [ReplaceNetworkAclEntry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-network-acl-entry.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replace-route-table-association`.

- **AWS CLI**
- 
            
                    **To replace the route table associated with a subnet**This example associates the specified route table with the subnet for the specified route table association. Command: `aws ec2 replace-route-table-association --association-id``rtbassoc-781d0d1a`--route-table-id`rtb-22574640`Output: `{ "NewAssociationId": "rtbassoc-3a1f0f58" }`- 
                    For API details, see [ReplaceRouteTableAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-route-table-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replace-route`.

- **AWS CLI**
- 
            
                    **To replace a route**This example replaces the specified route in the specified route table. The new route matches the specified CIDR and sends the traffic to the specified virtual private gateway. If the command succeeds, no output is returned. Command: `aws ec2 replace-route --route-table-id``rtb-22574640`--destination-cidr-block`10.0.0.0/16`--gateway-id`vgw-9a4cacf3`- 
                    For API details, see [ReplaceRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `replace-transit-gateway-route`.

- **AWS CLI**
- 
            
                    **To replace the specified route in the specified transit gateway route table**The following `replace-transit-gateway-route`example replaces the route in the specified transit gateway route table.`aws ec2 replace-transit-gateway-route \ --destination-cidr-block``10.0.2.0/24`\ --transit-gateway-attachment-id`tgw-attach-09b52ccdb5EXAMPLE`\ --transit-gateway-route-table-id`tgw-rtb-0a823edbdeEXAMPLE`Output: `{ "Route": { "DestinationCidrBlock": "10.0.2.0/24", "TransitGatewayAttachments": [ { "ResourceId": "vpc-4EXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-09b52ccdb5EXAMPLE", "ResourceType": "vpc" } ], "Type": "static", "State": "active" } }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [ReplaceTransitGatewayRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-transit-gateway-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `report-instance-status`.

- **AWS CLI**
- 
            
                    **To report status feedback for an instance**This example command reports status feedback for the specified instance. Command: `aws ec2 report-instance-status --instances``i-1234567890abcdef0`--status`impaired`--reason-codes`unresponsive`- 
                    For API details, see [ReportInstanceStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/report-instance-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `request-spot-fleet`.

- **AWS CLI**
- 
            
                    **To request a Spot fleet in the subnet with the lowest price**This example command creates a Spot fleet request with two launch specifications that differ only by subnet. The Spot fleet launches the instances in the specified subnet with the lowest price. If the instances are launched in a default VPC, they receive a public IP address by default. If the instances are launched in a nondefault VPC, they do not receive a public IP address by default. Note that you can't specify different subnets from the same Availability Zone in a Spot fleet request. Command: `aws ec2 request-spot-fleet --spot-fleet-request-config``file://config.json`Config.json: `{ "SpotPrice": "0.04", "TargetCapacity": 2, "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role", "LaunchSpecifications": [ { "ImageId": "ami-1a2b3c4d", "KeyName": "my-key-pair", "SecurityGroups": [ { "GroupId": "sg-1a2b3c4d" } ], "InstanceType": "m3.medium", "SubnetId": "subnet-1a2b3c4d, subnet-3c4d5e6f", "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role" } } ] }`Output: `{ "SpotFleetRequestId": "sfr-73fbd2ce-aa30-494c-8788-1cee4EXAMPLE" }`**To request a Spot fleet in the Availability Zone with the lowest price**This example command creates a Spot fleet request with two launch specifications that differ only by Availability Zone. The Spot fleet launches the instances in the specified Availability Zone with the lowest price. If your account supports EC2-VPC only, Amazon EC2 launches the Spot instances in the default subnet of the Availability Zone. If your account supports EC2-Classic, Amazon EC2 launches the instances in EC2-Classic in the Availability Zone. Command: `aws ec2 request-spot-fleet --spot-fleet-request-config``file://config.json`Config.json: `{ "SpotPrice": "0.04", "TargetCapacity": 2, "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role", "LaunchSpecifications": [ { "ImageId": "ami-1a2b3c4d", "KeyName": "my-key-pair", "SecurityGroups": [ { "GroupId": "sg-1a2b3c4d" } ], "InstanceType": "m3.medium", "Placement": { "AvailabilityZone": "us-west-2a, us-west-2b" }, "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role" } } ] }`**To launch Spot instances in a subnet and assign them public IP addresses**This example command assigns public addresses to instances launched in a nondefault VPC. Note that when you specify a network interface, you must include the subnet ID and security group ID using the network interface. Command: `aws ec2 request-spot-fleet --spot-fleet-request-config``file://config.json`Config.json: `{ "SpotPrice": "0.04", "TargetCapacity": 2, "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role", "LaunchSpecifications": [ { "ImageId": "ami-1a2b3c4d", "KeyName": "my-key-pair", "InstanceType": "m3.medium", "NetworkInterfaces": [ { "DeviceIndex": 0, "SubnetId": "subnet-1a2b3c4d", "Groups": [ "sg-1a2b3c4d" ], "AssociatePublicIpAddress": true } ], "IamInstanceProfile": { "Arn": "arn:aws:iam::880185128111:instance-profile/my-iam-role" } } ] }`**To request a Spot fleet using the diversified allocation strategy**This example command creates a Spot fleet request that launches 30 instances using the diversified allocation strategy. The launch specifications differ by instance type. The Spot fleet distributes the instances across the launch specifications such that there are 10 instances of each type. Command: `aws ec2 request-spot-fleet --spot-fleet-request-config``file://config.json`Config.json: `{ "SpotPrice": "0.70", "TargetCapacity": 30, "AllocationStrategy": "diversified", "IamFleetRole": "arn:aws:iam::123456789012:role/my-spot-fleet-role", "LaunchSpecifications": [ { "ImageId": "ami-1a2b3c4d", "InstanceType": "c4.2xlarge", "SubnetId": "subnet-1a2b3c4d" }, { "ImageId": "ami-1a2b3c4d", "InstanceType": "m3.2xlarge", "SubnetId": "subnet-1a2b3c4d" }, { "ImageId": "ami-1a2b3c4d", "InstanceType": "r3.2xlarge", "SubnetId": "subnet-1a2b3c4d" } ] }`For more information, see Spot Fleet Requests in the *Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [RequestSpotFleet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/request-spot-fleet.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `request-spot-instances`.

- **AWS CLI**
- 
            
                    **To request Spot Instances**This example command creates a one-time Spot Instance request for five instances in the specified Availability Zone. If your account supports EC2-VPC only, Amazon EC2 launches the instances in the default subnet of the specified Availability Zone. If your account supports EC2-Classic, Amazon EC2 launches the instances in EC2-Classic in the specified Availability Zone. Command: `aws ec2 request-spot-instances --spot-price``"0.03"`--instance-count`5`--type`"one-time"`--launch-specification`file://specification.json`Specification.json: `{ "ImageId": "ami-1a2b3c4d", "KeyName": "my-key-pair", "SecurityGroupIds": [ "sg-1a2b3c4d" ], "InstanceType": "m3.medium", "Placement": { "AvailabilityZone": "us-west-2a" }, "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role" } }`Output: `{ "SpotInstanceRequests": [ { "Status": { "UpdateTime": "2014-03-25T20:54:21.000Z", "Code": "pending-evaluation", "Message": "Your Spot request has been submitted for review, and is pending evaluation." }, "ProductDescription": "Linux/UNIX", "SpotInstanceRequestId": "sir-df6f405d", "State": "open", "LaunchSpecification": { "Placement": { "AvailabilityZone": "us-west-2a" }, "ImageId": "ami-1a2b3c4d", "KeyName": "my-key-pair", "SecurityGroups": [ { "GroupName": "my-security-group", "GroupId": "sg-1a2b3c4d" } ], "Monitoring": { "Enabled": false }, "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role" }, "InstanceType": "m3.medium" }, "Type": "one-time", "CreateTime": "2014-03-25T20:54:20.000Z", "SpotPrice": "0.050000" }, ... ] }`This example command creates a one-time Spot Instance request for five instances in the specified subnet. Amazon EC2 launches the instances in the specified subnet. If the VPC is a nondefault VPC, the instances do not receive a public IP address by default. Command: `aws ec2 request-spot-instances --spot-price``"0.050"`--instance-count`5`--type`"one-time"`--launch-specification`file://specification.json`Specification.json: `{ "ImageId": "ami-1a2b3c4d", "SecurityGroupIds": [ "sg-1a2b3c4d" ], "InstanceType": "m3.medium", "SubnetId": "subnet-1a2b3c4d", "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role" } }`Output: `{ "SpotInstanceRequests": [ { "Status": { "UpdateTime": "2014-03-25T22:21:58.000Z", "Code": "pending-evaluation", "Message": "Your Spot request has been submitted for review, and is pending evaluation." }, "ProductDescription": "Linux/UNIX", "SpotInstanceRequestId": "sir-df6f405d", "State": "open", "LaunchSpecification": { "Placement": { "AvailabilityZone": "us-west-2a" } "ImageId": "ami-1a2b3c4d" "SecurityGroups": [ { "GroupName": "my-security-group", "GroupID": "sg-1a2b3c4d" } ] "SubnetId": "subnet-1a2b3c4d", "Monitoring": { "Enabled": false }, "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role" }, "InstanceType": "m3.medium", }, "Type": "one-time", "CreateTime": "2014-03-25T22:21:58.000Z", "SpotPrice": "0.050000" }, ... ] }`This example assigns a public IP address to the Spot Instances that you launch in a nondefault VPC. Note that when you specify a network interface, you must include the subnet ID and security group ID using the network interface. Command: `aws ec2 request-spot-instances --spot-price``"0.050"`--instance-count`1`--type`"one-time"`--launch-specification`file://specification.json`Specification.json: `{ "ImageId": "ami-1a2b3c4d", "KeyName": "my-key-pair", "InstanceType": "m3.medium", "NetworkInterfaces": [ { "DeviceIndex": 0, "SubnetId": "subnet-1a2b3c4d", "Groups": [ "sg-1a2b3c4d" ], "AssociatePublicIpAddress": true } ], "IamInstanceProfile": { "Arn": "arn:aws:iam::123456789012:instance-profile/my-iam-role" } }`- 
                    For API details, see [RequestSpotInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/request-spot-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-address-attribute`.

- **AWS CLI**
- 
            
                    **To reset the domain name attribute associated with an elastic IP address**The following `reset-address-attribute`examples reset the domain name attribute of an elastic IP address.Linux: `aws ec2 reset-address-attribute \ --allocation-id``eipalloc-abcdef01234567890`\ --attribute`domain-name`Windows: `aws ec2 reset-address-attribute``^`--allocation-id`eipalloc-abcdef01234567890``^`--attribute`domain-name`Output: `{ "Addresses": [ { "PublicIp": "192.0.2.0", "AllocationId": "eipalloc-abcdef01234567890", "PtrRecord": "example.com." "PtrRecordUpdate": { "Value": "example.net.", "Status": "PENDING" } ] }`To monitor the pending change, see [describe-addresses-attribute](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-addresses-attribute.html)in the*AWS CLI Command Reference*.- 
                    For API details, see [ResetAddressAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-address-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-ebs-default-kms-key-id`.

- **AWS CLI**
- 
            
                    **To reset your default CMK for EBS encryption**The following `reset-ebs-default-kms-key-id`example resets the default CMK for EBS encryption for your AWS account in the current Region.`aws ec2 reset-ebs-default-kms-key-id`Output: `{ "KmsKeyId": "arn:aws:kms:us-west-2:123456789012:key/8c5b2c63-b9bc-45a3-a87a-5513eEXAMPLE" }`- 
                    For API details, see [ResetEbsDefaultKmsKeyId](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-ebs-default-kms-key-id.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-fpga-image-attribute`.

- **AWS CLI**
- 
            
                    **To reset the attributes of an Amazon FPGA image**This example resets the load permissions for the specified AFI. Command: `aws ec2 reset-fpga-image-attribute --fpga-image-id``afi-0d123e123bfc85abc`--attribute`loadPermission`Output: `{ "Return": true }`- 
                    For API details, see [ResetFpgaImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-fpga-image-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-image-attribute`.

- **AWS CLI**
- 
            
                    **To reset the launchPermission attribute**This example resets the `launchPermission`attribute for the specified AMI to its default value. By default, AMIs are private. If the command succeeds, no output is returned.Command: `aws ec2 reset-image-attribute --image-id``ami-5731123e`--attribute`launchPermission`- 
                    For API details, see [ResetImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-image-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-instance-attribute`.

- **AWS CLI**
- 
            
                    **To reset the sourceDestCheck attribute**This example resets the `sourceDestCheck`attribute of the specified instance. The instance must be in a VPC. If the command succeeds, no output is returned.Command: `aws ec2 reset-instance-attribute --instance-id``i-1234567890abcdef0`--attribute`sourceDestCheck`**To reset the kernel attribute**This example resets the `kernel`attribute of the specified instance. The instance must be in the`stopped`state. If the command succeeds, no output is returned.Command: `aws ec2 reset-instance-attribute --instance-id``i-1234567890abcdef0`--attribute`kernel`**To reset the ramdisk attribute**This example resets the `ramdisk`attribute of the specified instance. The instance must be in the`stopped`state. If the command succeeds, no output is returned.Command: `aws ec2 reset-instance-attribute --instance-id``i-1234567890abcdef0`--attribute`ramdisk`- 
                    For API details, see [ResetInstanceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-instance-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-network-interface-attribute`.

- **AWS CLI**
- 
            
                    **To reset a network interface attribute**The following `reset-network-interface-attribute`example resets the value of the source/destination checking attribute to`true`.`aws ec2 reset-network-interface-attribute \ --network-interface-id``eni-686ea200`\ --source-dest-check`sourceDestCheck`This command produces no output. - 
                    For API details, see [ResetNetworkInterfaceAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-network-interface-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reset-snapshot-attribute`.

- **AWS CLI**
- 
            
                    **To reset a snapshot attribute**This example resets the create volume permissions for snapshot `snap-1234567890abcdef0`. If the command succeeds, no output is returned.Command: `aws ec2 reset-snapshot-attribute --snapshot-id``snap-1234567890abcdef0`--attribute`createVolumePermission`- 
                    For API details, see [ResetSnapshotAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-snapshot-attribute.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-address-to-classic`.

- **AWS CLI**
- 
            
                    **To restore an address to EC2-Classic**This example restores Elastic IP address 198.51.100.0 to the EC2-Classic platform. Command: `aws ec2 restore-address-to-classic --public-ip``198.51.100.0`Output: `{ "Status": "MoveInProgress", "PublicIp": "198.51.100.0" }`- 
                    For API details, see [RestoreAddressToClassic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/restore-address-to-classic.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-image-from-recycle-bin`.

- **AWS CLI**
- 
            
                    **To restore an image from the Recycle Bin**The following `restore-image-from-recycle-bin`example restores AMI ami-0111222333444abcd from the Recycle Bin.`aws ec2 restore-image-from-recycle-bin \ --image-id``ami-0111222333444abcd`Output: `{ "Return": true }`For more information, see [Recover deleted AMIs from the Recycle Bin](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-amis.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [RestoreImageFromRecycleBin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/restore-image-from-recycle-bin.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-managed-prefix-list-version`.

- **AWS CLI**
- 
            
                    us-west-2**To restore a prefix list version** The following `restore-managed-prefix-list-version`restores the entries from version 1 of the specified prefix list.`aws ec2 restore-managed-prefix-list-version \ --prefix-list-id``pl-0123456abcabcabc1`\ --current-version`2`\ --previous-version`1`Output: `{ "PrefixList": { "PrefixListId": "pl-0123456abcabcabc1", "AddressFamily": "IPv4", "State": "restore-in-progress", "PrefixListArn": "arn:aws:ec2:us-west-2:123456789012:prefix-list/pl-0123456abcabcabc1", "PrefixListName": "vpc-cidrs", "MaxEntries": 10, "Version": 2, "OwnerId": "123456789012" } }`For more information, see [Managed prefix lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [RestoreManagedPrefixListVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/restore-managed-prefix-list-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-snapshot-from-recycle-bin`.

- **AWS CLI**
- 
            
                    **To restore snapshots from the Recycle Bin**The following `restore-snapshot-from-recycle-bin`example restores a snapshot from the Recycle Bin. When you restore a snapshot from the Recycle Bin, the snapshot is immediately available for use, and it is removed from the Recycle Bin. You can use a restored snapshot in the same way that you use any other snapshot in your account.`aws ec2 restore-snapshot-from-recycle-bin \ --snapshot-id``snap-01234567890abcdef`Output: `{ "SnapshotId": "snap-01234567890abcdef", "Description": "Monthly data backup snapshot", "Encrypted": false, "OwnerId": "111122223333", "Progress": "99%", "StartTime": "2021-12-01T13:00:00.000000+00:00", "State": "recovering", "VolumeId": "vol-ffffffff", "VolumeSize": 30 }`For more information about Recycle Bin, see [Recover deleted snapshots from the Recycle Bin](https://docs.aws.amazon.com/ebs/latest/userguide/recycle-bin-working-with-snaps.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [RestoreSnapshotFromRecycleBin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/restore-snapshot-from-recycle-bin.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-snapshot-tier`.

- **AWS CLI**
- 
            
                    **Example 1: To permanently restore an archived snapshot**The following `restore-snapshot-tier`example permanently restores the specified snapshot. Specify the`--snapshot-id`and include the`permanent-restore`option.`aws ec2 restore-snapshot-tier \ --snapshot-id``snap-01234567890abcedf`\ --permanent-restoreOutput: `{ "SnapshotId": "snap-01234567890abcedf", "IsPermanentRestore": true }`For more information about snapshot archiving, see [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html)in the*Amazon EBS User Guide*.**Example 2: To temporarily restore an archived snapshot**The following `restore-snapshot-tier`example temporarily restores the specified snapshot. Omit the`--permanent-restore`option. Specify the`--snapshot-id`and, for`temporary-restore-days`, specify the number of days for which to restore the snapshot.`temporary-restore-days`must be specified in days. The allowed range is`1`to`180`. If you do not specify a value, it defaults to`1`day.`aws ec2 restore-snapshot-tier \ --snapshot-id``snap-01234567890abcedf`\ --temporary-restore-days`5`Output: `{ "SnapshotId": "snap-01234567890abcedf", "RestoreDuration": 5, "IsPermanentRestore": false }`For more information about snapshot archiving, see [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html)in the*Amazon EBS User Guide*.**Example 3: To modify the restore period**The following `restore-snapshot-tier`example changes the restore period for the specified snapshot to`10`days.`aws ec2 restore-snapshot-tier \ --snapshot-id``snap-01234567890abcedf`--temporary-restore-days`10`Output: `{ "SnapshotId": "snap-01234567890abcedf", "RestoreDuration": 10, "IsPermanentRestore": false }`For more information about snapshot archiving, see [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html)in the*Amazon EBS User Guide*.**Example 4: To modify the restore type**The following `restore-snapshot-tier`example changes the restore type for the specified snapshot from temporary to permanent.`aws ec2 restore-snapshot-tier \ --snapshot-id``snap-01234567890abcedf`--permanent-restoreOutput: `{ "SnapshotId": "snap-01234567890abcedf", "IsPermanentRestore": true }`For more information about snapshot archiving, see [Archive Amazon EBS snapshots](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [RestoreSnapshotTier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/restore-snapshot-tier.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-client-vpn-ingress`.

- **AWS CLI**
- 
            
                    **To revoke an authorization rule for a Client VPN endpoint**The following `revoke-client-vpn-ingress`example revokes a rule for internet access (`0.0.0.0/0`) for all groups.`aws ec2 revoke-client-vpn-ingress \ --client-vpn-endpoint-id``cvpn-endpoint-123456789123abcde`\ --target-network-cidr`0.0.0.0/0`--revoke-all-groupsOutput: `{ "Status": { "Code": "revoking" } }`For more information, see [Authorization Rules](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-rules.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [RevokeClientVpnIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-client-vpn-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-security-group-egress`.

- **AWS CLI**
- 
            
                    **Example 1: To remove the rule that allows outbound traffic to a specific address range**The following `revoke-security-group-egress`example command removes the rule that grants access to the specified address ranges on TCP port 80.`aws ec2 revoke-security-group-egress \ --group-id``sg-026c12253ce15eff7`\ --ip-permissions`[{IpProtocol=tcp,FromPort=80,ToPort=80,IpRanges=[{CidrIp=10.0.0.0/16}]`This command produces no output. For more information, see [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)in the*Amazon EC2 User Guide*.**Example 2: To remove the rule that allows outbound traffic to a specific security group**The following `revoke-security-group-egress`example command removes the rule that grants access to the specified security group on TCP port 80.`aws ec2 revoke-security-group-egress \ --group-id``sg-026c12253ce15eff7`\ --ip-permissions '`[{"IpProtocol": "tcp", "FromPort": 443, "ToPort": 443,"UserIdGroupPairs": [{"GroupId": "sg-06df23a01ff2df86d"}]}]`'This command produces no output. For more information, see [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [RevokeSecurityGroupEgress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-security-group-egress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-security-group-ingress`.

- **AWS CLI**
- 
            
                    **Example 1: To remove a rule from a security group**The following `revoke-security-group-ingress`example removes TCP port 22 access for the`203.0.113.0/24`address range from the specified security group for a default VPC.`aws ec2 revoke-security-group-ingress \ --group-name``mySecurityGroup`--protocol`tcp`\ --port`22`\ --cidr`203.0.113.0/24`This command produces no output if it succeeds. For more information, see [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)in the*Amazon EC2 User Guide*.**Example 2: To remove a rule using the IP permissions set**The following `revoke-security-group-ingress`example uses the`ip-permissions`parameter to remove an inbound rule that allows the ICMP message`Destination Unreachable: Fragmentation Needed and Don't Fragment was Set`(Type 3, Code 4).`aws ec2 revoke-security-group-ingress \ --group-id``sg-026c12253ce15eff7`\ --ip-permissions`IpProtocol=icmp,FromPort=3,ToPort=4,IpRanges=[{CidrIp=0.0.0.0/0}]`This command produces no output if it succeeds. For more information, see [Security groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [RevokeSecurityGroupIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/revoke-security-group-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `run-instances`.

- **AWS CLI**
- 
            
                    **Example 1: To launch an instance into a default subnet**The following `run-instances`example launches a single instance of type`t2.micro`into the default subnet for the current Region and associates it with the default subnet for the default VPC for the Region. The key pair is optional if you do not plan to connect to your instance using SSH (Linux) or RDP (Windows).`aws ec2 run-instances \ --image-id``ami-0abcdef1234567890`\ --instance-type`t2.micro`\ --key-name`MyKeyPair`Output: `{ "Instances": [ { "AmiLaunchIndex": 0, "ImageId": "ami-0abcdef1234567890", "InstanceId": "i-1231231230abcdef0", "InstanceType": "t2.micro", "KeyName": "MyKeyPair", "LaunchTime": "2018-05-10T08:05:20.000Z", "Monitoring": { "State": "disabled" }, "Placement": { "AvailabilityZone": "us-east-2a", "GroupName": "", "Tenancy": "default" }, "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal", "PrivateIpAddress": "10.0.0.157", "ProductCodes": [], "PublicDnsName": "", "State": { "Code": 0, "Name": "pending" }, "StateTransitionReason": "", "SubnetId": "subnet-04a636d18e83cfacb", "VpcId": "vpc-1234567890abcdef0", "Architecture": "x86_64", "BlockDeviceMappings": [], "ClientToken": "", "EbsOptimized": false, "Hypervisor": "xen", "NetworkInterfaces": [ { "Attachment": { "AttachTime": "2018-05-10T08:05:20.000Z", "AttachmentId": "eni-attach-0e325c07e928a0405", "DeleteOnTermination": true, "DeviceIndex": 0, "Status": "attaching" }, "Description": "", "Groups": [ { "GroupName": "MySecurityGroup", "GroupId": "sg-0598c7d356eba48d7" } ], "Ipv6Addresses": [], "MacAddress": "0a:ab:58:e0:67:e2", "NetworkInterfaceId": "eni-0c0a29997760baee7", "OwnerId": "123456789012", "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal", "PrivateIpAddress": "10.0.0.157", "PrivateIpAddresses": [ { "Primary": true, "PrivateDnsName": "ip-10-0-0-157.us-east-2.compute.internal", "PrivateIpAddress": "10.0.0.157" } ], "SourceDestCheck": true, "Status": "in-use", "SubnetId": "subnet-04a636d18e83cfacb", "VpcId": "vpc-1234567890abcdef0", "InterfaceType": "interface" } ], "RootDeviceName": "/dev/xvda", "RootDeviceType": "ebs", "SecurityGroups": [ { "GroupName": "MySecurityGroup", "GroupId": "sg-0598c7d356eba48d7" } ], "SourceDestCheck": true, "StateReason": { "Code": "pending", "Message": "pending" }, "Tags": [], "VirtualizationType": "hvm", "CpuOptions": { "CoreCount": 1, "ThreadsPerCore": 1 }, "CapacityReservationSpecification": { "CapacityReservationPreference": "open" }, "MetadataOptions": { "State": "pending", "HttpTokens": "optional", "HttpPutResponseHopLimit": 1, "HttpEndpoint": "enabled" } } ], "OwnerId": "123456789012", "ReservationId": "r-02a3f596d91211712" }`**Example 2: To launch an instance into a non-default subnet and add a public IP address**The following `run-instances`example requests a public IP address for an instance that you're launching into a nondefault subnet. The instance is associated with the specified security group.`aws ec2 run-instances \ --image-id``ami-0abcdef1234567890`\ --instance-type`t2.micro`\ --subnet-id`subnet-08fc749671b2d077c`\ --security-group-ids`sg-0b0384b66d7d692f9`\ --associate-public-ip-address \ --key-name`MyKeyPair`For an example of the output for `run-instances`, see Example 1.**Example 3: To launch an instance with additional volumes**The following `run-instances`example uses a block device mapping, specified in mapping.json, to attach additional volumes at launch. A block device mapping can specify EBS volumes, instance store volumes, or both EBS volumes and instance store volumes.`aws ec2 run-instances \ --image-id``ami-0abcdef1234567890`\ --instance-type`t2.micro`\ --subnet-id`subnet-08fc749671b2d077c`\ --security-group-ids`sg-0b0384b66d7d692f9`\ --key-name`MyKeyPair`\ --block-device-mappings`file://mapping.json`Contents of `mapping.json`. This example adds`/dev/sdh`an empty EBS volume with a size of 100 GiB.`[ { "DeviceName": "/dev/sdh", "Ebs": { "VolumeSize": 100 } } ]`Contents of `mapping.json`. This example adds`ephemeral1`as an instance store volume.`[ { "DeviceName": "/dev/sdc", "VirtualName": "ephemeral1" } ]`For an example of the output for `run-instances`, see Example 1.For more information about block device mappings, see [Block device mapping](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/block-device-mapping-concepts.html)in the*Amazon EC2 User Guide*.**Example 4: To launch an instance and add tags on creation**The following `run-instances`example adds a tag with a key of`webserver`and value of`production`to the instance. The command also applies a tag with a key of`cost-center`and a value of`cc123`to any EBS volume that's created (in this case, the root volume).`aws ec2 run-instances \ --image-id``ami-0abcdef1234567890`\ --instance-type`t2.micro`\ --count`1`\ --subnet-id`subnet-08fc749671b2d077c`\ --key-name`MyKeyPair`\ --security-group-ids`sg-0b0384b66d7d692f9`\ --tag-specifications '`ResourceType=instance,Tags=[{Key=webserver,Value=production}]`' '`ResourceType=volume,Tags=[{Key=cost-center,Value=cc123}]`'For an example of the output for `run-instances`, see Example 1.**Example 5: To launch an instance with user data**The following `run-instances`example passes user data in a file called`my_script.txt`that contains a configuration script for your instance. The script runs at launch.`aws ec2 run-instances \ --image-id``ami-0abcdef1234567890`\ --instance-type`t2.micro`\ --count`1`\ --subnet-id`subnet-08fc749671b2d077c`\ --key-name`MyKeyPair`\ --security-group-ids`sg-0b0384b66d7d692f9`\ --user-data`file://my_script.txt`For an example of the output for `run-instances`, see Example 1.For more information about instance user data, see [Working with instance user data](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-add-user-data.html)in the*Amazon EC2 User Guide*.**Example 6: To launch a burstable performance instance**The following `run-instances`example launches a t2.micro instance with the`unlimited`credit option. When you launch a T2 instance, if you do not specify`--credit-specification`, the default is the`standard`credit option. When you launch a T3 instance, the default is the`unlimited`credit option.`aws ec2 run-instances \ --image-id``ami-0abcdef1234567890`\ --instance-type`t2.micro`\ --count`1`\ --subnet-id`subnet-08fc749671b2d077c`\ --key-name`MyKeyPair`\ --security-group-ids`sg-0b0384b66d7d692f9`\ --credit-specification`CpuCredits=unlimited`For an example of the output for `run-instances`, see Example 1.For more information about burstable performance instances, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)in the*Amazon EC2 User Guide*.- 
                    For API details, see [RunInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `run-scheduled-instances`.

- **AWS CLI**
- 
            
                    **To launch a Scheduled Instance**This example launches the specified Scheduled Instance in a VPC. Command: `aws ec2 run-scheduled-instances --scheduled-instance-id``sci-1234-1234-1234-1234-123456789012`--instance-count`1`--launch-specification`file://launch-specification.json`Launch-specification.json: `{ "ImageId": "ami-12345678", "KeyName": "my-key-pair", "InstanceType": "c4.large", "NetworkInterfaces": [ { "DeviceIndex": 0, "SubnetId": "subnet-12345678", "AssociatePublicIpAddress": true, "Groups": ["sg-12345678"] } ], "IamInstanceProfile": { "Name": "my-iam-role" } }`Output: `{ "InstanceIdSet": [ "i-1234567890abcdef0" ] }`This example launches the specified Scheduled Instance in EC2-Classic. Command: `aws ec2 run-scheduled-instances --scheduled-instance-id``sci-1234-1234-1234-1234-123456789012`--instance-count`1`--launch-specification`file://launch-specification.json`Launch-specification.json: `{ "ImageId": "ami-12345678", "KeyName": "my-key-pair", "SecurityGroupIds": ["sg-12345678"], "InstanceType": "c4.large", "Placement": { "AvailabilityZone": "us-west-2b" } "IamInstanceProfile": { "Name": "my-iam-role" } }`Output: `{ "InstanceIdSet": [ "i-1234567890abcdef0" ] }`- 
                    For API details, see [RunScheduledInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-scheduled-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-local-gateway-routes`.

- **AWS CLI**
- 
            
                    **To search for routes in a local gateway route table**The following `search-local-gateway-routes`example searches for static routes in the specified local gateway route table.`aws ec2 search-local-gateway-routes \ --local-gateway-route-table-id``lgw-rtb-059615ef7dEXAMPLE`\ --filters`"Name=type,Values=static"`Output: `{ "Route": { "DestinationCidrBlock": "0.0.0.0/0", "LocalGatewayVirtualInterfaceGroupId": "lgw-vif-grp-07145b276bEXAMPLE", "Type": "static", "State": "deleted", "LocalGatewayRouteTableId": "lgw-rtb-059615ef7EXAMPLE" } }`- 
                    For API details, see [SearchLocalGatewayRoutes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-local-gateway-routes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-transit-gateway-multicast-groups`.

- **AWS CLI**
- 
            
                    **To search one or more transit gateway multicast groups and return the group membership information**The following `search-transit-gateway-multicast-groups`example returns the group membership of the specified multicast group.`aws ec2 search-transit-gateway-multicast-groups \ --transit-gateway-multicast-domain-id``tgw-mcast-domain-000fb24d04EXAMPLE`Output: `{ "MulticastGroups": [ { "GroupIpAddress": "224.0.1.0", "TransitGatewayAttachmentId": "tgw-attach-0372e72386EXAMPLE", "SubnetId": "subnet-0187aff814EXAMPLE", "ResourceId": "vpc-0065acced4EXAMPLE", "ResourceType": "vpc", "NetworkInterfaceId": "eni-03847706f6EXAMPLE", "GroupMember": false, "GroupSource": true, "SourceType": "static" } ] }`For more information, see [Multicast on transit gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-multicast-overview.html)in the*Transit Gateways Guide*.- 
                    For API details, see [SearchTransitGatewayMulticastGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-transit-gateway-multicast-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-transit-gateway-routes`.

- **AWS CLI**
- 
            
                    **To search for routes in the specified transit gateway route table**The following `search-transit-gateway-routes`example returns all the routes that are of type`static`in the specified route table.`aws ec2 search-transit-gateway-routes \ --transit-gateway-route-table-id``tgw-rtb-0a823edbdeEXAMPLE`\ --filters`"Name=type,Values=static"`Output: `{ "Routes": [ { "DestinationCidrBlock": "10.0.2.0/24", "TransitGatewayAttachments": [ { "ResourceId": "vpc-4EXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-09b52ccdb5EXAMPLE", "ResourceType": "vpc" } ], "Type": "static", "State": "active" }, { "DestinationCidrBlock": "10.1.0.0/24", "TransitGatewayAttachments": [ { "ResourceId": "vpc-4EXAMPLE", "TransitGatewayAttachmentId": "tgw-attach-09b52ccdb5EXAMPLE", "ResourceType": "vpc" } ], "Type": "static", "State": "active" } ], "AdditionalRoutesAvailable": false }`For more information, see [Transit gateway route tables](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)in the*Transit Gateways Guide*.- 
                    For API details, see [SearchTransitGatewayRoutes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/search-transit-gateway-routes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-diagnostic-interrupt`.

- **AWS CLI**
- 
            
                    **To send a diagnostic interrupt**The following `send-diagnostic-interrupt`example sends a diagnostic interrupt to the specified instance.`aws ec2 send-diagnostic-interrupt \ --instance-id``i-1234567890abcdef0`This command produces no output. - 
                    For API details, see [SendDiagnosticInterrupt](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/send-diagnostic-interrupt.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-instances`.

- **AWS CLI**
- 
            
                    **To start an Amazon EC2 instance**This example starts the specified Amazon EBS-backed instance. Command: `aws ec2 start-instances --instance-ids``i-1234567890abcdef0`Output: `{ "StartingInstances": [ { "InstanceId": "i-1234567890abcdef0", "CurrentState": { "Code": 0, "Name": "pending" }, "PreviousState": { "Code": 80, "Name": "stopped" } } ] }`For more information, see Stop and Start Your Instance in the *Amazon Elastic Compute Cloud User Guide*.- 
                    For API details, see [StartInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-network-insights-access-scope-analysis`.

- **AWS CLI**
- 
            
                    **To start a Network Insights access scope analysis**The following `start-network-insights-access-scope-analysis`example starts the scope analysis in your AWS account.`aws ec2 start-network-insights-access-scope-analysis \ --region``us-east-1`\ --network-insights-access-scope-id`nis-123456789111`Output: `{ "NetworkInsightsAccessScopeAnalysis": { "NetworkInsightsAccessScopeAnalysisId": "nisa-123456789222", "NetworkInsightsAccessScopeAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-access-scope-analysis/nisa-123456789222", "NetworkInsightsAccessScopeId": "nis-123456789111", "Status": "running", "StartDate": "2022-01-26T00:47:06.814000+00:00" } }`For more information, see [Getting started with Network Access Analyzer using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/getting-started-cli.html)in the*Network Access Analyzer Guide*.- 
                    For API details, see [StartNetworkInsightsAccessScopeAnalysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-network-insights-access-scope-analysis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-network-insights-analysis`.

- **AWS CLI**
- 
            
                    **To analyze a path**The following `start-network-insights-analysis`example analyzes the path between the source and destination. To view the results of the path analysis, use the`describe-network-insights-analyses`command.`aws ec2 start-network-insights-analysis \ --network-insights-path-id``nip-0b26f224f1d131fa8`Output: `{ "NetworkInsightsAnalysis": { "NetworkInsightsAnalysisId": "nia-02207aa13eb480c7a", "NetworkInsightsAnalysisArn": "arn:aws:ec2:us-east-1:123456789012:network-insights-analysis/nia-02207aa13eb480c7a", "NetworkInsightsPathId": "nip-0b26f224f1d131fa8", "StartDate": "2021-01-20T22:58:37.495Z", "Status": "running" } }`For more information, see [Getting started using the AWS CLI](https://docs.aws.amazon.com/vpc/latest/reachability/getting-started-cli.html)in the*Reachability Analyzer Guide*.- 
                    For API details, see [StartNetworkInsightsAnalysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-network-insights-analysis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-vpc-endpoint-service-private-dns-verification`.

- **AWS CLI**
- 
            
                    **To initiate the DNS verification process**The following `start-vpc-endpoint-service-private-dns-verification`example initiates the DNS verification process for the specified endpoint service.`aws ec2 start-vpc-endpoint-service-private-dns-verification \ --service-id``vpce-svc-071afff70666e61e0`This command produces no output. For more information, see [Manage DNS names](https://docs.aws.amazon.com/vpc/latest/privatelink/manage-dns-names.html)in the*AWS PrivateLink User Guide*.- 
                    For API details, see [StartVpcEndpointServicePrivateDnsVerification](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/start-vpc-endpoint-service-private-dns-verification.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-instances`.

- **AWS CLI**
- 
            
                    **Example 1: To stop an Amazon EC2 instance**The following `stop-instances`example stops the specified Amazon EBS-backed instance.`aws ec2 stop-instances \ --instance-ids``i-1234567890abcdef0`Output: `{ "StoppingInstances": [ { "InstanceId": "i-1234567890abcdef0", "CurrentState": { "Code": 64, "Name": "stopping" }, "PreviousState": { "Code": 16, "Name": "running" } } ] }`For more information, see [Stop and Start Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Stop_Start.html)in the*Amazon Elastic Compute Cloud User Guide*.**Example 2: To hibernate an Amazon EC2 instance**The following `stop-instances`example hibernates Amazon EBS-backed instance if the instance is enabled for hibernation and meets the hibernation prerequisites. After the instance is put into hibernation the instance is stopped.`aws ec2 stop-instances \ --instance-ids``i-1234567890abcdef0`\ --hibernateOutput: `{ "StoppingInstances": [ { "CurrentState": { "Code": 64, "Name": "stopping" }, "InstanceId": "i-1234567890abcdef0", "PreviousState": { "Code": 16, "Name": "running" } } ] }`For more information, see [Hibernate your On-Demand Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Hibernate.html)in the*Amazon Elastic Cloud Compute User Guide*.- 
                    For API details, see [StopInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/stop-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `terminate-client-vpn-connections`.

- **AWS CLI**
- 
            
                    **To terminate a connection to a Client VPN endpoint**The following `terminate-client-vpn-connections`example terminates the specified connection to the Client VPN endpoint.`aws ec2 terminate-client-vpn-connections \ --client-vpn-endpoint-id``vpn-endpoint-123456789123abcde`\ --connection-id`cvpn-connection-04edd76f5201e0cb8`Output: `{ "ClientVpnEndpointId": "vpn-endpoint-123456789123abcde", "ConnectionStatuses": [ { "ConnectionId": "cvpn-connection-04edd76f5201e0cb8", "PreviousStatus": { "Code": "active" }, "CurrentStatus": { "Code": "terminating" } } ] }`For more information, see [Client Connections](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/cvpn-working-connections.html)in the*AWS Client VPN Administrator Guide*.- 
                    For API details, see [TerminateClientVpnConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-client-vpn-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `terminate-instances`.

- **AWS CLI**
- 
            
                    **To terminate an Amazon EC2 instance**This example terminates the specified instance. Command: `aws ec2 terminate-instances --instance-ids``i-1234567890abcdef0`Output: `{ "TerminatingInstances": [ { "InstanceId": "i-1234567890abcdef0", "CurrentState": { "Code": 32, "Name": "shutting-down" }, "PreviousState": { "Code": 16, "Name": "running" } } ] }`For more information, see Using Amazon EC2 Instances in the *AWS Command Line Interface User Guide*.- 
                    For API details, see [TerminateInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/terminate-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unassign-ipv6-addresses`.

- **AWS CLI**
- 
            
                    **To unassign an IPv6 address from a network interface**This example unassigns the specified IPv6 address from the specified network interface. Command: `aws ec2 unassign-ipv6-addresses --ipv6-addresses``2001:db8:1234:1a00:3304:8879:34cf:4071`--network-interface-id`eni-23c49b68`Output: `{ "NetworkInterfaceId": "eni-23c49b68", "UnassignedIpv6Addresses": [ "2001:db8:1234:1a00:3304:8879:34cf:4071" ] }`- 
                    For API details, see [UnassignIpv6Addresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-ipv6-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unassign-private-ip-addresses`.

- **AWS CLI**
- 
            
                    **To unassign a secondary private IP address from a network interface**This example unassigns the specified private IP address from the specified network interface. If the command succeeds, no output is returned. Command: `aws ec2 unassign-private-ip-addresses --network-interface-id``eni-e5aa89a3`--private-ip-addresses`10.0.0.82`- 
                    For API details, see [UnassignPrivateIpAddresses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-private-ip-addresses.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unassign-private-nat-gateway-address`.

- **AWS CLI**
- 
            
                    **To unassign a private IP address from your private NAT gateway**The following `unassign-private-nat-gateway-address`example unassigns the specified IP address from the specified private NAT gateway.`aws ec2 unassign-private-nat-gateway-address \ --nat-gateway-id``nat-1234567890abcdef0`\ --private-ip-addresses`10.0.20.197`Output: `{ "NatGatewayId": "nat-0ee3edd182361f662", "NatGatewayAddresses": [ { "NetworkInterfaceId": "eni-0065a61b324d1897a", "PrivateIp": "10.0.20.197", "IsPrimary": false, "Status": "unassigning" } ] }`For more information, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)in the*Amazon VPC User Guide*.- 
                    For API details, see [UnassignPrivateNatGatewayAddress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unassign-private-nat-gateway-address.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unlock-snapshot`.

- **AWS CLI**
- 
            
                    **To unlock a snapshot**The following `unlock-snapshot`example unlocks the specified snapshot.`aws ec2 unlock-snapshot \ --snapshot-id``snap-0b5e733b4a8df6e0d`Output: `{ "SnapshotId": "snap-0b5e733b4a8df6e0d" }`For more information, see [Snapshot lock](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-snapshot-lock.html)in the*Amazon EBS User Guide*.- 
                    For API details, see [UnlockSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unlock-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unmonitor-instances`.

- **AWS CLI**
- 
            
                    **To disable detailed monitoring for an instance**This example command disables detailed monitoring for the specified instance. Command: `aws ec2 unmonitor-instances --instance-ids``i-1234567890abcdef0`Output: `{ "InstanceMonitorings": [ { "InstanceId": "i-1234567890abcdef0", "Monitoring": { "State": "disabling" } } ] }`- 
                    For API details, see [UnmonitorInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/unmonitor-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-security-group-rule-descriptions-egress`.

- **AWS CLI**
- 
            
                    **To update the description of an outbound security group rule**The following `update-security-group-rule-descriptions-egress`example updates the description for the security group rule for the specified port and IPv4 address range. The description '`Outbound HTTP access to server 2`' replaces any existing description for the rule.`aws ec2 update-security-group-rule-descriptions-egress \ --group-id``sg-02f0d35a850ba727f`\ --ip-permissions IpProtocol=tcp,FromPort=80,ToPort=80,IpRanges=[{CidrIp=203.0.113.0/24,Description="Outbound HTTP access to server 2"}]Output: `{ "Return": true }`For more information, see [Security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#security-group-rules)in the*Amazon EC2 User Guide*.- 
                    For API details, see [UpdateSecurityGroupRuleDescriptionsEgress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/update-security-group-rule-descriptions-egress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-security-group-rule-descriptions-ingress`.

- **AWS CLI**
- 
            
                    **Example 1: To update the description of an inbound security group rule with a CIDR source**The following `update-security-group-rule-descriptions-ingress`example updates the description for the security group rule for the specified port and IPv4 address range. The description '`SSH access from ABC office`' replaces any existing description for the rule.`aws ec2 update-security-group-rule-descriptions-ingress \ --group-id``sg-02f0d35a850ba727f`\ --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,IpRanges='[{CidrIp=203.0.113.0/16,Description="SSH access from corpnet"}]'Output: `{ "Return": true }`For more information, see [Security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#security-group-rules)in the*Amazon EC2 User Guide*.**Example 2: To update the description of an inbound security group rule with a prefix list source**The following `update-security-group-rule-descriptions-ingress`example updates the description for the security group rule for the specified port and prefix list. The description '`SSH access from ABC office`' replaces any existing description for the rule.`aws ec2 update-security-group-rule-descriptions-ingress \ --group-id``sg-02f0d35a850ba727f`\ --ip-permissions IpProtocol=tcp,FromPort=22,ToPort=22,PrefixListIds='[{PrefixListId=pl-12345678,Description="SSH access from corpnet"}]'Output: `{ "Return": true }`For more information, see [Security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html#security-group-rules)in the*Amazon EC2 User Guide*.- 
                    For API details, see [UpdateSecurityGroupRuleDescriptionsIngress](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/update-security-group-rule-descriptions-ingress.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `withdraw-byoip-cidr`.

- **AWS CLI**
- 
            
                    **To stop advertising an address range**The following `withdraw-byoip-cidr`example stops advertising the specified address range.`aws ec2 withdraw-byoip-cidr --cidr``203.0.113.25/24`Output: `{ "ByoipCidr": { "Cidr": "203.0.113.25/24", "StatusMessage": "ipv4pool-ec2-1234567890abcdef0", "State": "advertised" } }`- 
                    For API details, see [WithdrawByoipCidr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/withdraw-byoip-cidr.html)in*AWS CLI Command Reference*.
 
-