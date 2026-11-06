# Direct Connect examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_direct-connect_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_direct-connect_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Direct Connect.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `accept-direct-connect-gateway-association-proposal`.

- **AWS CLI**
- 
            
                    **To accept a gateway association proposal**The following `accept-direct-connect-gateway-association-proposal`accepts the specified proposal.`aws directconnect accept-direct-connect-gateway-association-proposal \ --direct-connect-gateway-id``11460968-4ac1-4fd3-bdb2-00599EXAMPLE`\ --proposal-id`cb7f41cb-8128-43a5-93b1-dcaedEXAMPLE`\ --associated-gateway-owner-account`111122223333``{`"directConnectGatewayAssociation":`{`"directConnectGatewayId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE", "directConnectGatewayOwnerAccount": "111122223333", "associationState": "associating", "associatedGateway":`{`"id": "tgw-02f776b1a7EXAMPLE", "type": "transitGateway", "ownerAccount": "111122223333", "region":`"us-east-1"``},`"associationId": "6441f8bf-5917-4279-ade1-9708bEXAMPLE", "allowedPrefixesToDirectConnectGateway":`[``{`"cidr":`"192.168.1.0/30"``}``]``}``}`For more information, see [Accepting or Rejecting a Transit Gateway Association Proposal](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-tgw.html#multi-account-tgw-accept-reject-proposal)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [AcceptDirectConnectGatewayAssociationProposal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/accept-direct-connect-gateway-association-proposal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-connection-on-interconnect`.

- **AWS CLI**
- 
            
                    **To create a hosted connection on an interconnect**The following `allocate-connection-on-interconnect`command creates a hosted connection on an interconnect:`aws directconnect allocate-connection-on-interconnect --bandwidth``500Mbps`--connection-name`mydcinterconnect`--owner-account`123456789012`--interconnect-id`dxcon-fgktov66`--vlan`101`Output: `{ "partnerName": "TIVIT", "vlan": 101, "ownerAccount": "123456789012", "connectionId": "dxcon-ffzc51m1", "connectionState": "ordering", "bandwidth": "500Mbps", "location": "TIVIT", "connectionName": "mydcinterconnect", "region": "sa-east-1" }`- 
                    For API details, see [AllocateConnectionOnInterconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-connection-on-interconnect.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-hosted-connection`.

- **AWS CLI**
- 
            
                    **To create a hosted connection on an interconnect**The following `allocate-hosted-connection`example creates a hosted connection on the specified interconnect.`aws directconnect allocate-hosted-connection \ --bandwidth``500Mbps`\ --connection-name`mydcinterconnect`\ --owner-account`123456789012`\ --connection-id`dxcon-fgktov66`\ --vlan`101`Output: `{ "partnerName": "TIVIT", "vlan": 101, "ownerAccount": "123456789012", "connectionId": "dxcon-ffzc51m1", "connectionState": "ordering", "bandwidth": "500Mbps", "location": "TIVIT", "connectionName": "mydcinterconnect", "region": "sa-east-1" }`- 
                    For API details, see [AllocateHostedConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-hosted-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-private-virtual-interface`.

- **AWS CLI**
- 
            
                    **To provision a private virtual interface**The following `allocate-private-virtual-interface`command provisions a private virtual interface to be owned by a different customer:`aws directconnect allocate-private-virtual-interface --connection-id``dxcon-ffjrkx17`--owner-account`123456789012`--new-private-virtual-interface-allocation`virtualInterfaceName=PrivateVirtualInterface,vlan=1000,asn=65000,authKey=asdf34example,amazonAddress=192.168.1.1/30,customerAddress=192.168.1.2/30`Output: `{ "virtualInterfaceState": "confirming", "asn": 65000, "vlan": 1000, "customerAddress": "192.168.1.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-ffjrkx17", "virtualInterfaceId": "dxvif-fgy8orxu", "authKey": "asdf34example", "routeFilterPrefixes": [], "location": "TIVIT", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n <logical_connection id=\"dxvif-fgy8orxu\">\n <vlan>1000</vlan>\n <customer_address>192.168.1.2/30</customer_address>\n <amazon_address>192.168.1.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>asdf34example</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>private</connection_type>\n</logical_connection>\n", "amazonAddress": "192.168.1.1/30", "virtualInterfaceType": "private", "virtualInterfaceName": "PrivateVirtualInterface" }`- 
                    For API details, see [AllocatePrivateVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-private-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-public-virtual-interface`.

- **AWS CLI**
- 
            
                    **To provision a public virtual interface**The following `allocate-public-virtual-interface`command provisions a public virtual interface to be owned by a different customer:`aws directconnect allocate-public-virtual-interface --connection-id``dxcon-ffjrkx17`--owner-account`123456789012`--new-public-virtual-interface-allocation`virtualInterfaceName=PublicVirtualInterface,vlan=2000,asn=65000,authKey=asdf34example,amazonAddress=203.0.113.1/30,customerAddress=203.0.113.2/30,routeFilterPrefixes=[{cidr=203.0.113.0/30},{cidr=203.0.113.4/30}]`Output: `{ "virtualInterfaceState": "confirming", "asn": 65000, "vlan": 2000, "customerAddress": "203.0.113.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-ffjrkx17", "virtualInterfaceId": "dxvif-fg9xo9vp", "authKey": "asdf34example", "routeFilterPrefixes": [ { "cidr": "203.0.113.0/30" }, { "cidr": "203.0.113.4/30" } ], "location": "TIVIT", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fg9xo9vp\">\n <vlan>2000</vlan>\n <customer_address>203.0.113.2/30</customer_address>\n <amazon_address>203.0.113.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>asdf34example</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>public</connection_type>\n</logical_connection>\n", "amazonAddress": "203.0.113.1/30", "virtualInterfaceType": "public", "virtualInterfaceName": "PublicVirtualInterface" }`- 
                    For API details, see [AllocatePublicVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-public-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `allocate-transit-virtual-interface`.

- **AWS CLI**
- 
            
                    **To provision a transit virtual interface to be owned by the specified AWS account**The following `allocate-transit-virtual-interface`example provisions a transit virtual interface for the specified account.`aws directconnect allocate-transit-virtual-interface \ --connection-id``dxlag-fEXAMPLE`\ --owner-account`123456789012`\ --new-transit-virtual-interface-allocation`"virtualInterfaceName=Example Transit Virtual Interface,vlan=126,asn=65110,mtu=1500,authKey=0xzxgA9YoW9h58u8SEXAMPLE,amazonAddress=192.168.1.1/30,customerAddress=192.168.1.2/30,addressFamily=ipv4,tags=[{key=Tag,value=Example}]"`Output: `{ "virtualInterface": { "ownerAccount": "123456789012", "virtualInterfaceId": "dxvif-fEXAMPLE", "location": "loc1", "connectionId": "dxlag-fEXAMPLE", "virtualInterfaceType": "transit", "virtualInterfaceName": "Example Transit Virtual Interface", "vlan": 126, "asn": 65110, "amazonSideAsn": 7224, "authKey": "0xzxgA9YoW9h58u8SEXAMPLE", "amazonAddress": "192.168.1.1/30", "customerAddress": "192.168.1.2/30", "addressFamily": "ipv4", "virtualInterfaceState": "confirming", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fEXAMPLE\">\n <vlan>126</vlan>\n <customer_address>192.168.1.2/30</customer_address>\n <amazon_address>192.168.1.1/30</amazon_address>\n <bgp_asn>65110</bgp_asn>\n <bgp_auth_key>0xzxgA9YoW9h58u8SEXAMPLE</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>transit</connection_type>\n</logical_connection>\n", "mtu": 1500, "jumboFrameCapable": true, "virtualGatewayId": "", "directConnectGatewayId": "", "routeFilterPrefixes": [], "bgpPeers": [ { "bgpPeerId": "dxpeer-fEXAMPLE", "asn": 65110, "authKey": "0xzxgA9YoW9h58u8EXAMPLE", "addressFamily": "ipv4", "amazonAddress": "192.168.1.1/30", "customerAddress": "192.168.1.2/30", "bgpPeerState": "pending", "bgpStatus": "down", "awsDeviceV2": "loc1-26wz6vEXAMPLE" } ], "region": "sa-east-1", "awsDeviceV2": "loc1-26wz6vEXAMPLE", "tags": [ { "key": "Tag", "value": "Example" } ] } }`For more information, see [Creating a Hosted Transit Virtual Interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/createhostedvirtualinterface.html#create-hosted-transit-vif)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [AllocateTransitVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/allocate-transit-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-connection-with-lag`.

- **AWS CLI**
- 
            
                    **To associate a connection with a LAG**The following example associates the specified connection with the specified LAG. Command: `aws directconnect associate-connection-with-lag --lag-id``dxlag-fhccu14t`--connection-id`dxcon-fg9607vm`Output: `{ "ownerAccount": "123456789012", "connectionId": "dxcon-fg9607vm", "lagId": "dxlag-fhccu14t", "connectionState": "requested", "bandwidth": "1Gbps", "location": "EqDC2", "connectionName": "Con2ForLag", "region": "us-east-1" }`- 
                    For API details, see [AssociateConnectionWithLag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-connection-with-lag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-hosted-connection`.

- **AWS CLI**
- 
            
                    **To associate a hosted connection with a LAG**The following example associates the specified hosted connection with the specified LAG. Command: `aws directconnect associate-hosted-connection --parent-connection-id``dxlag-fhccu14t`--connection-id`dxcon-fg9607vm`Output: `{ "partnerName": "TIVIT", "vlan": 101, "ownerAccount": "123456789012", "connectionId": "dxcon-fg9607vm", "lagId": "dxlag-fhccu14t", "connectionState": "ordering", "bandwidth": "500Mbps", "location": "TIVIT", "connectionName": "mydcinterconnect", "region": "sa-east-1" }`- 
                    For API details, see [AssociateHostedConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-hosted-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-virtual-interface`.

- **AWS CLI**
- 
            
                    **To associate a virtual interface with a connection**The following example associates the specified virtual interface with the specified LAG. Alternatively, to associate the virtual interface with a connection, specify the ID of an AWS Direct Connect connection for `--connection-id`; for example,`dxcon-ffnikghc`.Command: `aws directconnect associate-virtual-interface --connection-id``dxlag-ffjhj9lx`--virtual-interface-id`dxvif-fgputw0j`Output: `{ "virtualInterfaceState": "pending", "asn": 65000, "vlan": 123, "customerAddress": "169.254.255.2/30", "ownerAccount": "123456789012", "connectionId": "dxlag-ffjhj9lx", "addressFamily": "ipv4", "virtualGatewayId": "vgw-38e90b51", "virtualInterfaceId": "dxvif-fgputw0j", "authKey": "0x123pK5_VBqv.UQ3kJ4123_", "routeFilterPrefixes": [], "location": "CSVA1", "bgpPeers": [ { "bgpStatus": "down", "customerAddress": "169.254.255.2/30", "addressFamily": "ipv4", "authKey": "0x123pK5_VBqv.UQ3kJ4123_", "bgpPeerState": "deleting", "amazonAddress": "169.254.255.1/30", "asn": 65000 }, { "bgpStatus": "down", "customerAddress": "169.254.255.2/30", "addressFamily": "ipv4", "authKey": "0x123pK5_VBqv.UQ3kJ4123_", "bgpPeerState": "pending", "amazonAddress": "169.254.255.1/30", "asn": 65000 } ], "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fgputw0j\">\n <vlan>123</vlan>\n <customer_address>169.254.255.2/30</customer_address>\n <amazon_address>169.254.255.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>0x123pK5_VBqv.UQ3kJ4123_</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>private</connection_type>\n</logical_connection>\n", "amazonAddress": "169.254.255.1/30", "virtualInterfaceType": "private", "virtualInterfaceName": "VIF1A" }`- 
                    For API details, see [AssociateVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/associate-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-connection`.

- **AWS CLI**
- 
            
                    **To confirm the creation of a hosted connection on an interconnect**The following `confirm-connection`command confirms the creation of a hosted connection on an interconnect:`aws directconnect confirm-connection --connection-id``dxcon-fg2wi7hy`Output: `{ "connectionState": "pending" }`- 
                    For API details, see [ConfirmConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-private-virtual-interface`.

- **AWS CLI**
- 
            
                    **To accept ownership of a private virtual interface**The following `confirm-private-virtual-interface`command accepts ownership of a private virtual interface created by another customer:`aws directconnect confirm-private-virtual-interface --virtual-interface-id``dxvif-fgy8orxu`--virtual-gateway-id`vgw-e4a47df9`Output: `{ "virtualInterfaceState": "pending" }`- 
                    For API details, see [ConfirmPrivateVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-private-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-public-virtual-interface`.

- **AWS CLI**
- 
            
                    **To accept ownership of a public virtual interface**The following `confirm-public-virtual-interface`command accepts ownership of a public virtual interface created by another customer:`aws directconnect confirm-public-virtual-interface --virtual-interface-id``dxvif-fg9xo9vp`Output: `{ "virtualInterfaceState": "verifying" }`- 
                    For API details, see [ConfirmPublicVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-public-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `confirm-transit-virtual-interface`.

- **AWS CLI**
- 
            
                    **To accept ownership of a transit virtual interface**The following `confirm-transit-virtual-interface`accepts ownership of a transit virtual interface created by another customer.`aws directconnect confirm-transit-virtual-interface \ --virtual-interface-id``dxvif-fEXAMPLE`\ --direct-connect-gateway-id`4112ccf9-25e9-4111-8237-b6c5dEXAMPLE`Output: `{ "virtualInterfaceState": "pending" }`For more information, see [Accepting a Hosted Virtual Interface](https://docs.aws.amazon.com/directconnect/latest/UserGuide/accepthostedvirtualinterface.html)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [ConfirmTransitVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/confirm-transit-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-bgp-peer`.

- **AWS CLI**
- 
            
                    **To create an IPv6 BGP peering session**The following example creates an IPv6 BGP peering session on private virtual interface `dxvif-fg1vuj3d`. The peer IPv6 addresses are automatically allocated by Amazon.Command: `aws directconnect create-bgp-peer --virtual-interface-id``dxvif-fg1vuj3d`--new-bgp-peer`asn=64600,addressFamily=ipv6`Output: `{ "virtualInterface": { "virtualInterfaceState": "available", "asn": 65000, "vlan": 125, "customerAddress": "169.254.255.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-fguhmqlc", "addressFamily": "ipv4", "virtualGatewayId": "vgw-f9eb0c90", "virtualInterfaceId": "dxvif-fg1vuj3d", "authKey": "0xC_ukbCerl6EYA0example", "routeFilterPrefixes": [], "location": "EqDC2", "bgpPeers": [ { "bgpStatus": "down", "customerAddress": "169.254.255.2/30", "addressFamily": "ipv4", "authKey": "0xC_ukbCerl6EYA0uexample", "bgpPeerState": "available", "amazonAddress": "169.254.255.1/30", "asn": 65000 }, { "bgpStatus": "down", "customerAddress": "2001:db8:1100:2f0:0:1:9cb4:4216/125", "addressFamily": "ipv6", "authKey": "0xS27kAIU_VHPjjAexample", "bgpPeerState": "pending", "amazonAddress": "2001:db8:1100:2f0:0:1:9cb4:4211/125", "asn": 64600 } ], "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fg1vuj3d\">\n <vlan>125</vlan>\n <customer_address>169.254.255.2/30</customer_address>\n <amazon_address>169.254.255.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>0xC_ukbCerl6EYA0uexample</bgp_auth_key>\n <ipv6_customer_address>2001:db8:1100:2f0:0:1:9cb4:4216/125</ipv6_customer_address>\n <ipv6_amazon_address>2001:db8:1100:2f0:0:1:9cb4:4211/125</ipv6_amazon_address>\n <ipv6_bgp_asn>64600</ipv6_bgp_asn>\n <ipv6_bgp_auth_key>0xS27kAIU_VHPjjAexample</ipv6_bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>private</connection_type>\n</logical_connection>\n", "amazonAddress": "169.254.255.1/30", "virtualInterfaceType": "private", "virtualInterfaceName": "Test" } }`- 
                    For API details, see [CreateBgpPeer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-bgp-peer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-connection`.

- **AWS CLI**
- 
            
                    **To create a connection from your network to an AWS Direct Connect location**The following `create-connection`command creates a connection from your network to an AWS Direct Connect location:`aws directconnect create-connection --location``TIVIT`--bandwidth`1Gbps`--connection-name`"Connection to AWS"`Output: `{ "ownerAccount": "123456789012", "connectionId": "dxcon-fg31dyv6", "connectionState": "requested", "bandwidth": "1Gbps", "location": "TIVIT", "connectionName": "Connection to AWS", "region": "sa-east-1" }`- 
                    For API details, see [CreateConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-direct-connect-gateway-association-proposal`.

- **AWS CLI**
- 
            
                    **To create a proposal to associate the specified transit gateway with the specified Direct Connect gateway**The following `create-direct-connect-gateway-association-proposal`example creates a proposal that associates the specified transit gateway with the specified Direct Connect gateway.`aws directconnect create-direct-connect-gateway-association-proposal \ --direct-connect-gateway-id``11460968-4ac1-4fd3-bdb2-00599EXAMPLE`\ --direct-connect-gateway-owner-account`111122223333`\ --gateway-id`tgw-02f776b1a7EXAMPLE`\ --add-allowed-prefixes-to-direct-connect-gateway`cidr=192.168.1.0/30`Output: `{ "directConnectGatewayAssociationProposal": { "proposalId": "cb7f41cb-8128-43a5-93b1-dcaedEXAMPLE", "directConnectGatewayId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE", "directConnectGatewayOwnerAccount": "111122223333", "proposalState": "requested", "associatedGateway": { "id": "tgw-02f776b1a7EXAMPLE", "type": "transitGateway", "ownerAccount": "111122223333", "region": "us-east-1" }, "requestedAllowedPrefixesToDirectConnectGateway": [ { "cidr": "192.168.1.0/30" } ] } }`For more information, see [Creating a Transit Gateway Association Proposal](https://docs.aws.amazon.com/directconnect/latest/UserGuide/multi-account-associate-tgw.html#multi-account-tgw-create-proposal)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [CreateDirectConnectGatewayAssociationProposal](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway-association-proposal.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-direct-connect-gateway-association`.

- **AWS CLI**
- 
            
                    **To associate a virtual private gateway with a Direct Connect gateway**The following example associates virtual private gateway `vgw-6efe725e`with Direct Connect gateway`5f294f92-bafb-4011-916d-9b0bexample`. You must run the command in the region in which the virtual private gateway is located.Command: `aws directconnect create-direct-connect-gateway-association --direct-connect-gateway-id``5f294f92-bafb-4011-916d-9b0bexample`--virtual-gateway-id`vgw-6efe725e`Output: `{ "directConnectGatewayAssociation": { "associationState": "associating", "virtualGatewayOwnerAccount": "123456789012", "directConnectGatewayId": "5f294f92-bafb-4011-916d-9b0bexample", "virtualGatewayId": "vgw-6efe725e", "virtualGatewayRegion": "us-east-2" } }`- 
                    For API details, see [CreateDirectConnectGatewayAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-direct-connect-gateway`.

- **AWS CLI**
- 
            
                    **To create a Direct Connect gateway**The following example creates a Direct Connect gateway with the name `DxGateway1`.Command: `aws directconnect create-direct-connect-gateway --direct-connect-gateway-name``"DxGateway1"`Output: `{ "directConnectGateway": { "amazonSideAsn": 64512, "directConnectGatewayId": "5f294f92-bafb-4011-916d-9b0bdexample", "ownerAccount": "123456789012", "directConnectGatewayName": "DxGateway1", "directConnectGatewayState": "available" } }`- 
                    For API details, see [CreateDirectConnectGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-direct-connect-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-interconnect`.

- **AWS CLI**
- 
            
                    **To create an interconnect between a partner's network and AWS**The following `create-interconnect`command creates an interconnect between an AWS Direct Connect partner's network and a specific AWS Direct Connect location:`aws directconnect create-interconnect --interconnect-name``"1G Interconnect to AWS"`--bandwidth`1Gbps`--location`TIVIT`Output: `{ "region": "sa-east-1", "bandwidth": "1Gbps", "location": "TIVIT", "interconnectName": "1G Interconnect to AWS", "interconnectId": "dxcon-fgktov66", "interconnectState": "requested" }`- 
                    For API details, see [CreateInterconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-interconnect.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-lag`.

- **AWS CLI**
- 
            
                    **To create a LAG with new connections**The following example creates a LAG and requests two new AWS Direct Connect connections for the LAG with a bandwidth of 1 Gbps. Command: `aws directconnect create-lag --location``CSVA1`--number-of-connections`2`--connections-bandwidth`1Gbps`--lag-name`1GBLag`Output: `{ "awsDevice": "CSVA1-23u8tlpaz8iks", "numberOfConnections": 2, "lagState": "pending", "ownerAccount": "123456789012", "lagName": "1GBLag", "connections": [ { "ownerAccount": "123456789012", "connectionId": "dxcon-ffqr6x5q", "lagId": "dxlag-ffjhj9lx", "connectionState": "requested", "bandwidth": "1Gbps", "location": "CSVA1", "connectionName": "Requested Connection 1 for Lag dxlag-ffjhj9lx", "region": "us-east-1" }, { "ownerAccount": "123456789012", "connectionId": "dxcon-fflqyj95", "lagId": "dxlag-ffjhj9lx", "connectionState": "requested", "bandwidth": "1Gbps", "location": "CSVA1", "connectionName": "Requested Connection 2 for Lag dxlag-ffjhj9lx", "region": "us-east-1" } ], "lagId": "dxlag-ffjhj9lx", "minimumLinks": 0, "connectionsBandwidth": "1Gbps", "region": "us-east-1", "location": "CSVA1" }`**To create a LAG using an existing connection**The following example creates a LAG from an existing connection in your account, and requests a second new connection for the LAG with the same bandwidth and location as the existing connection. Command: `aws directconnect create-lag --location``EqDC2`--number-of-connections`2`--connections-bandwidth`1Gbps`--lag-name`2ConnLAG`--connection-id`dxcon-fgk145dr`Output: `{ "awsDevice": "EqDC2-4h6ce2r1bes6", "numberOfConnections": 2, "lagState": "pending", "ownerAccount": "123456789012", "lagName": "2ConnLAG", "connections": [ { "ownerAccount": "123456789012", "connectionId": "dxcon-fh6ljcvo", "lagId": "dxlag-fhccu14t", "connectionState": "requested", "bandwidth": "1Gbps", "location": "EqDC2", "connectionName": "Requested Connection 1 for Lag dxlag-fhccu14t", "region": "us-east-1" }, { "ownerAccount": "123456789012", "connectionId": "dxcon-fgk145dr", "lagId": "dxlag-fhccu14t", "connectionState": "down", "bandwidth": "1Gbps", "location": "EqDC2", "connectionName": "VAConn1", "region": "us-east-1" } ], "lagId": "dxlag-fhccu14t", "minimumLinks": 0, "connectionsBandwidth": "1Gbps", "region": "us-east-1", "location": "EqDC2" }`- 
                    For API details, see [CreateLag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-lag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-private-virtual-interface`.

- **AWS CLI**
- 
            
                    **To create a private virtual interface**The following `create-private-virtual-interface`command creates a private virtual interface:`aws directconnect create-private-virtual-interface --connection-id``dxcon-ffjrkx17`--new-private-virtual-interface`virtualInterfaceName=PrivateVirtualInterface,vlan=101,asn=65000,authKey=asdf34example,amazonAddress=192.168.1.1/30,customerAddress=192.168.1.2/30,virtualGatewayId=vgw-aba37db6`Output: `{ "virtualInterfaceState": "pending", "asn": 65000, "vlan": 101, "customerAddress": "192.168.1.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-ffjrkx17", "virtualGatewayId": "vgw-aba37db6", "virtualInterfaceId": "dxvif-ffhhk74f", "authKey": "asdf34example", "routeFilterPrefixes": [], "location": "TIVIT", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-ffhhk74f\">\n <vlan>101</vlan>\n <customer_address>192.168.1.2/30</customer_address>\n <amazon_address>192.168.1.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>asdf34example</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>private</connection_type>\n</logical_connection>\n", "amazonAddress": "192.168.1.1/30", "virtualInterfaceType": "private", "virtualInterfaceName": "PrivateVirtualInterface" }`- 
                    For API details, see [CreatePrivateVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-private-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-public-virtual-interface`.

- **AWS CLI**
- 
            
                    **To create a public virtual interface**The following `create-public-virtual-interface`command creates a public virtual interface:`aws directconnect create-public-virtual-interface --connection-id``dxcon-ffjrkx17`--new-public-virtual-interface`virtualInterfaceName=PublicVirtualInterface,vlan=2000,asn=65000,authKey=asdf34example,amazonAddress=203.0.113.1/30,customerAddress=203.0.113.2/30,routeFilterPrefixes=[{cidr=203.0.113.0/30},{cidr=203.0.113.4/30}]`Output: `{ "virtualInterfaceState": "verifying", "asn": 65000, "vlan": 2000, "customerAddress": "203.0.113.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-ffjrkx17", "virtualInterfaceId": "dxvif-fgh0hcrk", "authKey": "asdf34example", "routeFilterPrefixes": [ { "cidr": "203.0.113.0/30" }, { "cidr": "203.0.113.4/30" } ], "location": "TIVIT", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fgh0hcrk\">\n <vlan>2000</vlan>\n <customer_address>203.0.113.2/30</customer_address>\n <amazon_address>203.0.113.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>asdf34example</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>public</connection_type>\n</logical_connection>\n", "amazonAddress": "203.0.113.1/30", "virtualInterfaceType": "public", "virtualInterfaceName": "PublicVirtualInterface" }`- 
                    For API details, see [CreatePublicVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-public-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-transit-virtual-interface`.

- **AWS CLI**
- 
            
                    **To create a transit virtual interface**The following `create-transit-virtual-interface`example creates a transit virtual interface for the specified connection.`aws directconnect create-transit-virtual-interface \ --connection-id``dxlag-fEXAMPLE`\ --new-transit-virtual-interface`"virtualInterfaceName=Example Transit Virtual Interface,vlan=126,asn=65110,mtu=1500,authKey=0xzxgA9YoW9h58u8SvEXAMPLE,amazonAddress=192.168.1.1/30,customerAddress=192.168.1.2/30,addressFamily=ipv4,directConnectGatewayId=8384da05-13ce-4a91-aada-5a1baEXAMPLE,tags=[{key=Tag,value=Example}]"`Output: `{ "virtualInterface": { "ownerAccount": "1111222233333", "virtualInterfaceId": "dxvif-fEXAMPLE", "location": "loc1", "connectionId": "dxlag-fEXAMPLE", "virtualInterfaceType": "transit", "virtualInterfaceName": "Example Transit Virtual Interface", "vlan": 126, "asn": 65110, "amazonSideAsn": 4200000000, "authKey": "0xzxgA9YoW9h58u8SEXAMPLE", "amazonAddress": "192.168.1.1/30", "customerAddress": "192.168.1.2/30", "addressFamily": "ipv4", "virtualInterfaceState": "pending", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fEXAMPLE\">\n <vlan>126</vlan>\n <customer_address>192.168.1.2/30</customer_address>\n <amazon_address>192.168.1.1/30</amazon_address>\n <bgp_asn>65110</bgp_asn>\n <bgp_auth_key>0xzxgA9YoW9h58u8SvOmXRTw</bgp_auth_key>\n <amazon_bgp_asn>4200000000</amazon_bgp_asn>\n <connection_type>transit</connection_type>\n</logical_connection>\n", "mtu": 1500, "jumboFrameCapable": true, "virtualGatewayId": "", "directConnectGatewayId": "8384da05-13ce-4a91-aada-5a1baEXAMPLE", "routeFilterPrefixes": [], "bgpPeers": [ { "bgpPeerId": "dxpeer-EXAMPLE", "asn": 65110, "authKey": "0xzxgA9YoW9h58u8SEXAMPLE", "addressFamily": "ipv4", "amazonAddress": "192.168.1.1/30", "customerAddress": "192.168.1.2/30", "bgpPeerState": "pending", "bgpStatus": "down", "awsDeviceV2": "loc1-26wz6vEXAMPLE" } ], "region": "sa-east-1", "awsDeviceV2": "loc1-26wz6vEXAMPLE", "tags": [ { "key": "Tag", "value": "Example" } ] } }`For more information, see [Creating a Transit Virtual Interface to the Direct Connect Gateway](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html#create-transit-vif)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [CreateTransitVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/create-transit-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-bgp-peer`.

- **AWS CLI**
- 
            
                    **To delete a BGP peer from a virtual interface**The following example deletes the IPv6 BGP peer from virtual interface `dxvif-fg1vuj3d`.Command: `aws directconnect delete-bgp-peer --virtual-interface-id``dxvif-fg1vuj3d`--asn`64600`--customer-address`2001:db8:1100:2f0:0:1:9cb4:4216/125`Output: `{ "virtualInterface": { "virtualInterfaceState": "available", "asn": 65000, "vlan": 125, "customerAddress": "169.254.255.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-fguhmqlc", "addressFamily": "ipv4", "virtualGatewayId": "vgw-f9eb0c90", "virtualInterfaceId": "dxvif-fg1vuj3d", "authKey": "0xC_ukbCerl6EYA0example", "routeFilterPrefixes": [], "location": "EqDC2", "bgpPeers": [ { "bgpStatus": "down", "customerAddress": "169.254.255.2/30", "addressFamily": "ipv4", "authKey": "0xC_ukbCerl6EYA0uexample", "bgpPeerState": "available", "amazonAddress": "169.254.255.1/30", "asn": 65000 }, { "bgpStatus": "down", "customerAddress": "2001:db8:1100:2f0:0:1:9cb4:4216/125", "addressFamily": "ipv6", "authKey": "0xS27kAIU_VHPjjAexample", "bgpPeerState": "deleting", "amazonAddress": "2001:db8:1100:2f0:0:1:9cb4:4211/125", "asn": 64600 } ], "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fg1vuj3d\">\n <vlan>125</vlan>\n <customer_address>169.254.255.2/30</customer_address>\n <amazon_address>169.254.255.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>0xC_ukbCerl6EYA0example</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>private</connection_type>\n</logical_connection>\n", "amazonAddress": "169.254.255.1/30", "virtualInterfaceType": "private", "virtualInterfaceName": "Test" } }`- 
                    For API details, see [DeleteBgpPeer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-bgp-peer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-connection`.

- **AWS CLI**
- 
            
                    **To delete a connection**The following `delete-connection`command deletes the specified connection:`aws directconnect delete-connection --connection-id``dxcon-fg31dyv6`Output: `{ "ownerAccount": "123456789012", "connectionId": "dxcon-fg31dyv6", "connectionState": "deleted", "bandwidth": "1Gbps", "location": "TIVIT", "connectionName": "Connection to AWS", "region": "sa-east-1" }`- 
                    For API details, see [DeleteConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-direct-connect-gateway-association`.

- **AWS CLI**
- 
            
                    **To delete a Direct Connect gateway association**The following `delete-direct-connect-gateway-association`example deletes the Direct Connect gateway association with a transit gateway that has the specified association ID.`aws directconnect delete-direct-connect-gateway-association --association-id``be85116d-46eb-4b43-a27a-da0c2ad648de`Output: `{ "directConnectGatewayAssociation": { "directConnectGatewayId": "11460968-4ac1-4fd3-bdb2-00599EXAMPlE", "directConnectGatewayOwnerAccount": "123456789012", "associationState": "disassociating", "associatedGateway": { "id": "tgw-095b3b0b54EXAMPLE", "type": "transitGateway", "ownerAccount": "123456789012", "region": "us-east-1" }, "associationId": " be85116d-46eb-4b43-a27a-da0c2ad648deEXAMPLE ", "allowedPrefixesToDirectConnectGateway": [ { "cidr": "192.0.1.0/28" } ] } }`For more information, see [Associating and Disassociating Transit Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html#associate-tgw-with-direct-connect-gateway)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [DeleteDirectConnectGatewayAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-direct-connect-gateway`.

- **AWS CLI**
- 
            
                    **To delete a Direct Connect gateway**The following example deletes Direct Connect gateway `5f294f92-bafb-4011-916d-9b0bexample`.Command: `aws directconnect delete-direct-connect-gateway --direct-connect-gateway-id``5f294f92-bafb-4011-916d-9b0bexample`Output: `{ "directConnectGateway": { "amazonSideAsn": 64512, "directConnectGatewayId": "5f294f92-bafb-4011-916d-9b0bexample", "ownerAccount": "123456789012", "directConnectGatewayName": "DxGateway1", "directConnectGatewayState": "deleting" } }`- 
                    For API details, see [DeleteDirectConnectGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-direct-connect-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-interconnect`.

- **AWS CLI**
- 
            
                    **To delete an interconnect**The following `delete-interconnect`command deletes the specified interconnect:`aws directconnect delete-interconnect --interconnect-id``dxcon-fgktov66`Output: `{ "interconnectState": "deleted" }`- 
                    For API details, see [DeleteInterconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-interconnect.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-lag`.

- **AWS CLI**
- 
            
                    **To delete a LAG**The following example deletes the specified LAG. Command: `aws directconnect delete-lag --lag-id``dxlag-ffrhowd9`Output: `{ "awsDevice": "EqDC2-4h6ce2r1bes6", "numberOfConnections": 0, "lagState": "deleted", "ownerAccount": "123456789012", "lagName": "TestLAG", "connections": [], "lagId": "dxlag-ffrhowd9", "minimumLinks": 0, "connectionsBandwidth": "1Gbps", "region": "us-east-1", "location": "EqDC2" }`- 
                    For API details, see [DeleteLag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-lag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-virtual-interface`.

- **AWS CLI**
- 
            
                    **To delete a virtual interface**The following `delete-virtual-interface`command deletes the specified virtual interface:`aws directconnect delete-virtual-interface --virtual-interface-id``dxvif-ffhhk74f`Output: `{ "virtualInterfaceState": "deleting" }`- 
                    For API details, see [DeleteVirtualInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/delete-virtual-interface.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-connection-loa`.

- **AWS CLI**
- 
            
                    **To describe your LOA-CFA for a connection using Linux or Mac OS X**The following example describes your LOA-CFA for connection `dxcon-fh6ayh1d`. The contents of the LOA-CFA are base64-encoded. This command uses the`--output`and`--query`parameters to control the output and extract the contents of the`loaContent`structure. The final part of the command decodes the content using the`base64`utility, and sends the output to a PDF file.`aws directconnect describe-connection-loa --connection-id``dxcon-fh6ayh1d`--output`text`--query`loa.loaContent|base64`--decode`>``myLoaCfa.pdf`**To describe your LOA-CFA for a connection using Windows**The previous example requires the use of the `base64`utility to decode the output. On a Windows computer, you can use`certutil`instead. In the following example, the first command describes your LOA-CFA for connection`dxcon-fh6ayh1d`and uses the`--output`and`--query`parameters to control the output and extract the contents of the`loaContent`structure to a file called`myLoaCfa.base64`. The second command uses the`certutil`utility to decode the file and send the output to a PDF file.`aws directconnect describe-connection-loa --connection-id``dxcon-fh6ayh1d`--output`text`--query`loa.loaContent``>``myLoaCfa.base64``certutil -decode myLoaCfa.base64 myLoaCfa.pdf`For more information about controlling AWS CLI output, see [Controlling Command Output from the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [DescribeConnectionLoa](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connection-loa.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-connections-on-interconnect`.

- **AWS CLI**
- 
            
                    **To list connections on an interconnect**The following `describe-connections-on-interconnect`command lists connections that have been provisioned on the given interconnect:`aws directconnect describe-connections-on-interconnect --interconnect-id``dxcon-fgktov66`Output: `{ "connections": [ { "partnerName": "TIVIT", "vlan": 101, "ownerAccount": "123456789012", "connectionId": "dxcon-ffzc51m1", "connectionState": "ordering", "bandwidth": "500Mbps", "location": "TIVIT", "connectionName": "mydcinterconnect", "region": "sa-east-1" } ] }`- 
                    For API details, see [DescribeConnectionsOnInterconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connections-on-interconnect.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-connections`.

- **AWS CLI**
- 
            
                    **To list all connections in the current region**The following `describe-connections`command lists all connections in the current region:`aws directconnect describe-connections`Output: `{ "connections": [ { "awsDevice": "EqDC2-123h49s71dabc", "ownerAccount": "123456789012", "connectionId": "dxcon-fguhmqlc", "lagId": "dxlag-ffrz71kw", "connectionState": "down", "bandwidth": "1Gbps", "location": "EqDC2", "connectionName": "My_Connection", "loaIssueTime": 1491568964.0, "region": "us-east-1" } ] }`- 
                    For API details, see [DescribeConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-direct-connect-gateway-association-proposals`.

- **AWS CLI**
- 
            
                    **To describe your Direct Connect gateway association proposals**The following `describe-direct-connect-gateway-association-proposals`example displays details about your Direct Connect gateway association proposals.`aws directconnect describe-direct-connect-gateway-association-proposals`Output: `{ "directConnectGatewayAssociationProposals": [ { "proposalId": "c2ede9b4-bbc6-4d33-923c-bc4feEXAMPLE", "directConnectGatewayId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE", "directConnectGatewayOwnerAccount": "111122223333", "proposalState": "requested", "associatedGateway": { "id": "tgw-02f776b1a7EXAMPLE", "type": "transitGateway", "ownerAccount": "111122223333", "region": "us-east-1" }, "existingAllowedPrefixesToDirectConnectGateway": [ { "cidr": "192.168.2.0/30" }, { "cidr": "192.168.1.0/30" } ], "requestedAllowedPrefixesToDirectConnectGateway": [ { "cidr": "192.168.1.0/30" } ] }, { "proposalId": "cb7f41cb-8128-43a5-93b1-dcaedEXAMPLE", "directConnectGatewayId": "11560968-4ac1-4fd3-bcb2-00599EXAMPLE", "directConnectGatewayOwnerAccount": "111122223333", "proposalState": "accepted", "associatedGateway": { "id": "tgw-045776b1a7EXAMPLE", "type": "transitGateway", "ownerAccount": "111122223333", "region": "us-east-1" }, "existingAllowedPrefixesToDirectConnectGateway": [ { "cidr": "192.168.4.0/30" }, { "cidr": "192.168.5.0/30" } ], "requestedAllowedPrefixesToDirectConnectGateway": [ { "cidr": "192.168.5.0/30" } ] } ] }`For more information, see [Associating and Disassociating Transit Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html#associate-tgw-with-direct-connect-gateway)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [DescribeDirectConnectGatewayAssociationProposals](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-association-proposals.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-direct-connect-gateway-associations`.

- **AWS CLI**
- 
            
                    **To describe Direct Connect gateway associations**The following example describes all the associations with Direct Connect gateway `5f294f92-bafb-4011-916d-9b0bexample`.Command: `aws directconnect describe-direct-connect-gateway-associations --direct-connect-gateway-id``5f294f92-bafb-4011-916d-9b0bexample`Output: `{ "nextToken": "eyJ2IjoxLCJzIjoxLCJpIjoiOU83OTFodzdycnZCbkN4MExHeHVwQT09IiwiYyI6InIxTEN0UEVHV0I1UFlkaWFnNlUxanJkRWF6eW1iOElHM0FRVW1MdHRJK0dxcnN1RWtvcFBKWFE2ZjRNRGdGTkhCa0tDZmVINEtZOEYwZ0dEYWZpbmU0ZnZMYVhKRjdXRVdENmdQZ1Y4d2w0PSJ9", "directConnectGatewayAssociations": [ { "associationState": "associating", "virtualGatewayOwnerAccount": "123456789012", "directConnectGatewayId": "5f294f92-bafb-4011-916d-9b0bexample", "virtualGatewayId": "vgw-6efe725e", "virtualGatewayRegion": "us-east-2" }, { "associationState": "disassociating", "virtualGatewayOwnerAccount": "123456789012", "directConnectGatewayId": "5f294f92-bafb-4011-916d-9b0bexample", "virtualGatewayId": "vgw-ebaa27db", "virtualGatewayRegion": "us-east-2" } ] }`- 
                    For API details, see [DescribeDirectConnectGatewayAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-direct-connect-gateway-attachments`.

- **AWS CLI**
- 
            
                    **To describe Direct Connect gateway attachments**The following example describes the virtual interfaces that are attached to Direct Connect gateway `5f294f92-bafb-4011-916d-9b0bexample`.Command: `aws directconnect describe-direct-connect-gateway-attachments --direct-connect-gateway-id``5f294f92-bafb-4011-916d-9b0bexample`Output: `{ "directConnectGatewayAttachments": [ { "virtualInterfaceOwnerAccount": "123456789012", "directConnectGatewayId": "5f294f92-bafb-4011-916d-9b0bexample", "virtualInterfaceRegion": "us-east-2", "attachmentState": "attaching", "virtualInterfaceId": "dxvif-fg9zyabc" } ], "nextToken": "eyJ2IjoxLCJzIjoxLCJpIjoibEhXdlNpUXF5RzhoL1JyUW52SlV2QT09IiwiYyI6Im5wQjFHQ0RyQUdRS3puNnNXcUlINCtkTTA4dTk3KzBiU0xtb05JQmlaczZ6NXRIYmk3c3VESUxFTTd6a2FzVHM0VTFwaGJkZGNxTytqWmQ3QzMzOGRQaTVrTThrOG1zelRsV3gyMWV3VTNFPSJ9" }`- 
                    For API details, see [DescribeDirectConnectGatewayAttachments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateway-attachments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-direct-connect-gateways`.

- **AWS CLI**
- 
            
                    **To describe your Direct Connect gateways**The following example describe all of your Direct Connect gateways. Command: `aws directconnect describe-direct-connect-gateways`Output: `{ "directConnectGateways": [ { "amazonSideAsn": 64512, "directConnectGatewayId": "cf68415c-f4ae-48f2-87a7-3b52cexample", "ownerAccount": "123456789012", "directConnectGatewayName": "DxGateway2", "directConnectGatewayState": "available" }, { "amazonSideAsn": 64512, "directConnectGatewayId": "5f294f92-bafb-4011-916d-9b0bdexample", "ownerAccount": "123456789012", "directConnectGatewayName": "DxGateway1", "directConnectGatewayState": "available" } ] }`- 
                    For API details, see [DescribeDirectConnectGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-direct-connect-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-hosted-connections`.

- **AWS CLI**
- 
            
                    **To list connections on an interconnect**The following example lists connections that have been provisioned on the given interconnect. Command: `aws directconnect describe-hosted-connections --connection-id``dxcon-fgktov66`Output: `{ "connections": [ { "partnerName": "TIVIT", "vlan": 101, "ownerAccount": "123456789012", "connectionId": "dxcon-ffzc51m1", "connectionState": "ordering", "bandwidth": "500Mbps", "location": "TIVIT", "connectionName": "mydcinterconnect", "region": "sa-east-1" } ] }`- 
                    For API details, see [DescribeHostedConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-hosted-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-interconnect-loa`.

- **AWS CLI**
- 
            
                    **To describe your LOA-CFA for an interconnect using Linux or Mac OS X**The following example describes your LOA-CFA for interconnect `dxcon-fh6ayh1d`. The contents of the LOA-CFA are base64-encoded. This command uses the`--output`and`--query`parameters to control the output and extract the contents of the`loaContent`structure. The final part of the command decodes the content using the`base64`utility, and sends the output to a PDF file.`aws directconnect describe-interconnect-loa --interconnect-id``dxcon-fh6ayh1d`--output`text`--query`loa.loaContent|base64`--decode`>``myLoaCfa.pdf`**To describe your LOA-CFA for an interconnect using Windows**The previous example requires the use of the `base64`utility to decode the output. On a Windows computer, you can use`certutil`instead. In the following example, the first command describes your LOA-CFA for interconnect`dxcon-fh6ayh1d`and uses the`--output`and`--query`parameters to control the output and extract the contents of the`loaContent`structure to a file called`myLoaCfa.base64`. The second command uses the`certutil`utility to decode the file and send the output to a PDF file.`aws directconnect describe-interconnect-loa --interconnect-id``dxcon-fh6ayh1d`--output`text`--query`loa.loaContent``>``myLoaCfa.base64``certutil -decode myLoaCfa.base64 myLoaCfa.pdf`For more information about controlling AWS CLI output, see [Controlling Command Output from the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [DescribeInterconnectLoa](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-interconnect-loa.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-interconnects`.

- **AWS CLI**
- 
            
                    **To list interconnects**The following `describe-interconnects`command lists the interconnects owned by your AWS account:`aws directconnect describe-interconnects`Output: `{ "interconnects": [ { "region": "sa-east-1", "bandwidth": "1Gbps", "location": "TIVIT", "interconnectName": "1G Interconnect to AWS", "interconnectId": "dxcon-fgktov66", "interconnectState": "down" } ] }`- 
                    For API details, see [DescribeInterconnects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-interconnects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-lags`.

- **AWS CLI**
- 
            
                    **To describe your LAGs**The following command describes all of your LAGs for the current region. Command: `aws directconnect describe-lags`Output: `{ "lags": [ { "awsDevice": "EqDC2-19y7z3m17xpuz", "numberOfConnections": 2, "lagState": "down", "ownerAccount": "123456789012", "lagName": "DA-LAG", "connections": [ { "ownerAccount": "123456789012", "connectionId": "dxcon-ffnikghc", "lagId": "dxlag-fgsu9erb", "connectionState": "requested", "bandwidth": "10Gbps", "location": "EqDC2", "connectionName": "Requested Connection 1 for Lag dxlag-fgsu9erb", "region": "us-east-1" }, { "ownerAccount": "123456789012", "connectionId": "dxcon-fglgbdea", "lagId": "dxlag-fgsu9erb", "connectionState": "requested", "bandwidth": "10Gbps", "location": "EqDC2", "connectionName": "Requested Connection 2 for Lag dxlag-fgsu9erb", "region": "us-east-1" } ], "lagId": "dxlag-fgsu9erb", "minimumLinks": 0, "connectionsBandwidth": "10Gbps", "region": "us-east-1", "location": "EqDC2" } ] }`- 
                    For API details, see [DescribeLags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-lags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-loa`.

- **AWS CLI**
- 
            
                    **To describe your LOA-CFA for a connection using Linux or Mac OS X**The following example describes your LOA-CFA for connection `dxcon-fh6ayh1d`. The contents of the LOA-CFA are base64-encoded. This command uses the`--output`and`--query`parameters to control the output and extract the contents of the`loaContent`structure. The final part of the command decodes the content using the`base64`utility, and sends the output to a PDF file.`aws directconnect describe-loa --connection-id``dxcon-fh6ayh1d`--output`text`--query`loa.loaContent|base64`--decode`>``myLoaCfa.pdf`**To describe your LOA-CFA for a connection using Windows**The previous example requires the use of the `base64`utility to decode the output. On a Windows computer, you can use`certutil`instead. In the following example, the first command describes your LOA-CFA for connection`dxcon-fh6ayh1d`and uses the`--output`and`--query`parameters to control the output and extract the contents of the`loaContent`structure to a file called`myLoaCfa.base64`. The second command uses the`certutil`utility to decode the file and send the output to a PDF file.`aws directconnect describe-loa --connection-id``dxcon-fh6ayh1d`--output`text`--query`loa.loaContent``>``myLoaCfa.base64``certutil -decode myLoaCfa.base64 myLoaCfa.pdf`For more information about controlling AWS CLI output, see [Controlling Command Output from the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html)in the*AWS Command Line Interface User Guide*.- 
                    For API details, see [DescribeLoa](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-loa.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-locations`.

- **AWS CLI**
- 
            
                    **To list AWS Direct Connect partners and locations**The following `describe-locations`command lists AWS Direct Connect partners and locations in the current region:`aws directconnect describe-locations`Output: `{ "locations": [ { "locationName": "NAP do Brasil, Barueri, Sao Paulo", "locationCode": "TNDB" }, { "locationName": "Tivit - Site Transamerica (Sao Paulo)", "locationCode": "TIVIT" } ] }`- 
                    For API details, see [DescribeLocations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-locations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **To describe tags for your AWS Direct Connect resources**The following command describes the tags for the connection `dxcon-abcabc12`.Command: `aws directconnect describe-tags --resource-arns``arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-abcabc12`Output: `{ "resourceTags": [ { "resourceArn": "arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-abcabc12", "tags": [ { "value": "VAConnection", "key": "Name" } ] } ] }`- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-virtual-gateways`.

- **AWS CLI**
- 
            
                    **To list virtual private gateways**The following `describe-virtual-gateways`command lists virtual private gateways owned by your AWS account:`aws directconnect describe-virtual-gateways`Output: `{ "virtualGateways": [ { "virtualGatewayId": "vgw-aba37db6", "virtualGatewayState": "available" } ] }`- 
                    For API details, see [DescribeVirtualGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-virtual-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-virtual-interfaces`.

- **AWS CLI**
- 
            
                    **To list all virtual interfaces**The following `describe-virtual-interfaces`command lists the information about all virtual interfaces associated with your AWS account:`aws directconnect describe-virtual-interfaces --connection-id``dxcon-ffjrkx17`Output: `{ "virtualInterfaces": [ { "virtualInterfaceState": "down", "asn": 65000, "vlan": 101, "customerAddress": "192.168.1.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-ffjrkx17", "virtualGatewayId": "vgw-aba37db6", "virtualInterfaceId": "dxvif-ffhhk74f", "authKey": "asdf34example", "routeFilterPrefixes": [], "location": "TIVIT", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-ffhhk74f\">\n <vlan>101</vlan>\n <customer_address>192.168.1.2/30</customer_address>\n <amazon_address>192.168.1.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>asdf34example</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>private</connection_type>\n</logical_connection>\n", "amazonAddress": "192.168.1.1/30", "virtualInterfaceType": "private", "virtualInterfaceName": "PrivateVirtualInterface" }, { "virtualInterfaceState": "verifying", "asn": 65000, "vlan": 2000, "customerAddress": "203.0.113.2/30", "ownerAccount": "123456789012", "connectionId": "dxcon-ffjrkx17", "virtualGatewayId": "", "virtualInterfaceId": "dxvif-fgh0hcrk", "authKey": "asdf34example", "routeFilterPrefixes": [ { "cidr": "203.0.113.4/30" }, { "cidr": "203.0.113.0/30" } ], "location": "TIVIT", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fgh0hcrk\">\n <vlan>2000</vlan>\n <customer_address>203.0.113.2/30</customer_address>\n <amazon_address>203.0.113.1/30</amazon_address>\n <bgp_asn>65000</bgp_asn>\n <bgp_auth_key>asdf34example</bgp_auth_key>\n <amazon_bgp_asn>7224</amazon_bgp_asn>\n <connection_type>public</connection_type>\n</logical_connection>\n", "amazonAddress": "203.0.113.1/30", "virtualInterfaceType": "public", "virtualInterfaceName": "PublicVirtualInterface" } ] }`- 
                    For API details, see [DescribeVirtualInterfaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/describe-virtual-interfaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-connection-from-lag`.

- **AWS CLI**
- 
            
                    **To disassociate a connection from a LAG**The following example disassociates the specified connection from the specified LAG. Command: `aws directconnect disassociate-connection-from-lag --lag-id``dxlag-fhccu14t`--connection-id`dxcon-fg9607vm`Output: `{ "ownerAccount": "123456789012", "connectionId": "dxcon-fg9607vm", "connectionState": "requested", "bandwidth": "1Gbps", "location": "EqDC2", "connectionName": "Con2ForLag", "region": "us-east-1" }`- 
                    For API details, see [DisassociateConnectionFromLag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/disassociate-connection-from-lag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to an AWS Direct Connect resource**The following command adds a tag with a key of `Name`and a value of`VAConnection`to the connection`dxcon-abcabc12`. If the command succeeds, no output is returned.Command: `aws directconnect tag-resource --resource-arn``arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-abcabc12`--tags`"key=Name,value=VAConnection"`- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from an AWS Direct Connect resource**The following command removes the tag with the key `Name`from connection`dxcon-abcabc12`. If the command succeeds, no output is returned.Command: `aws directconnect untag-resource --resource-arn``arn:aws:directconnect:us-east-1:123456789012:dxcon/dxcon-abcabc12`--tag-keys`Name`- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-direct-connect-gateway-association`.

- **AWS CLI**
- 
            
                    **To update the specified attributes of the Direct Connect gateway association**The following `update-direct-connect-gateway-association`example adds the specified CIDR block to a Direct Connect gateway association.`aws directconnect update-direct-connect-gateway-association \ --association-id``820a6e4f-5374-4004-8317-3f64bEXAMPLE`\ --add-allowed-prefixes-to-direct-connect-gateway`cidr=192.168.2.0/30`Output: `{ "directConnectGatewayAssociation": { "directConnectGatewayId": "11460968-4ac1-4fd3-bdb2-00599EXAMPLE", "directConnectGatewayOwnerAccount": "111122223333", "associationState": "updating", "associatedGateway": { "id": "tgw-02f776b1a7EXAMPLE", "type": "transitGateway", "ownerAccount": "111122223333", "region": "us-east-1" }, "associationId": "820a6e4f-5374-4004-8317-3f64bEXAMPLE", "allowedPrefixesToDirectConnectGateway": [ { "cidr": "192.168.2.0/30" }, { "cidr": "192.168.1.0/30" } ] } }`For more information, see [Working with Direct Connect Gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [UpdateDirectConnectGatewayAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-direct-connect-gateway-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-lag`.

- **AWS CLI**
- 
            
                    **To update a LAG**The following example changes the name of the specified LAG. Command: `aws directconnect update-lag --lag-id``dxlag-ffjhj9lx`--lag-name`2ConnLag`Output: `{ "awsDevice": "CSVA1-23u8tlpaz8iks", "numberOfConnections": 2, "lagState": "down", "ownerAccount": "123456789012", "lagName": "2ConnLag", "connections": [ { "ownerAccount": "123456789012", "connectionId": "dxcon-fflqyj95", "lagId": "dxlag-ffjhj9lx", "connectionState": "requested", "bandwidth": "1Gbps", "location": "CSVA1", "connectionName": "Requested Connection 2 for Lag dxlag-ffjhj9lx", "region": "us-east-1" }, { "ownerAccount": "123456789012", "connectionId": "dxcon-ffqr6x5q", "lagId": "dxlag-ffjhj9lx", "connectionState": "requested", "bandwidth": "1Gbps", "location": "CSVA1", "connectionName": "Requested Connection 1 for Lag dxlag-ffjhj9lx", "region": "us-east-1" } ], "lagId": "dxlag-ffjhj9lx", "minimumLinks": 0, "connectionsBandwidth": "1Gbps", "region": "us-east-1", "location": "CSVA1" }`- 
                    For API details, see [UpdateLag](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-lag.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-virtual-interface-attributes`.

- **AWS CLI**
- 
            
                    **To update the MTU of a virtual interface**The following `update-virtual-interface-attributes`example updates the MTU of the specified virtual interface.`aws directconnect update-virtual-interface-attributes \ --virtual-interface-id``dxvif-fEXAMPLE`\ --mtu`1500`Output: `{ "ownerAccount": "1111222233333", "virtualInterfaceId": "dxvif-fEXAMPLE", "location": "loc1", "connectionId": "dxlag-fEXAMPLE", "virtualInterfaceType": "transit", "virtualInterfaceName": "example transit virtual interface", "vlan": 125, "asn": 650001, "amazonSideAsn": 64512, "authKey": "0xzxgA9YoW9h58u8SEXAMPLE", "amazonAddress": "169.254.248.1/30", "customerAddress": "169.254.248.2/30", "addressFamily": "ipv4", "virtualInterfaceState": "down", "customerRouterConfig": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<logical_connection id=\"dxvif-fEXAMPLE\">\n <vlan>125</vlan>\n <customer_address>169.254.248.2/30</customer_address>\n <amazon_address>169.254.248.1/30</amazon_address>\n <bgp_asn>650001</bgp_asn>\n <bgp_auth_key>0xzxgA9YoW9h58u8SEXAMPLE</bgp_auth_key>\n <amazon_bgp_asn>64512</amazon_bgp_asn>\n <connection_type>transit</connection_type>\n</logical_connection>\n", "mtu": 1500, "jumboFrameCapable": true, "virtualGatewayId": "", "directConnectGatewayId": "879b76a1-403d-4700-8b53-4a56ed85436e", "routeFilterPrefixes": [], "bgpPeers": [ { "bgpPeerId": "dxpeer-fEXAMPLE", "asn": 650001, "authKey": "0xzxgA9YoW9h58u8SEXAMPLE", "addressFamily": "ipv4", "amazonAddress": "169.254.248.1/30", "customerAddress": "169.254.248.2/30", "bgpPeerState": "available", "bgpStatus": "down", "awsDeviceV2": "loc1-26wz6vEXAMPLE" } ], "region": "sa-east-1", "awsDeviceV2": "loc1-26wz6vEXAMPLE", "tags": [] }`For more information, see [Setting Network MTU for Private Virtual Interfaces or Transit Virtual Interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/set-jumbo-frames-vif.html)in the*AWS Direct Connect User Guide*.- 
                    For API details, see [UpdateVirtualInterfaceAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/directconnect/update-virtual-interface-attributes.html)in*AWS CLI Command Reference*.
 
-