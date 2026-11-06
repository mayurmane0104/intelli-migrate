# VPC Lattice examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_vpc-lattice_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_vpc-lattice_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with VPC Lattice.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-listener`.

- **AWS CLI**
- 
            
                    **To create a listener**The following `create-listener`example creates an HTTPS listener with a default rule that forwards traffic to the specified VPC Lattice target group.`aws vpc-lattice create-listener \ --name``my-service-listener`\ --protocol`HTTPS`\ --port`443`\ --service-identifier`svc-0285b53b2eEXAMPLE`\ --default-action`file://listener-config.json`Contents of `listener-config.json`:`{ "forward": { "targetGroups": [ { "targetGroupIdentifier": "tg-0eaa4b9ab4EXAMPLE" } ] } }`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE/listener/listener-07cc7fb0abEXAMPLE", "defaultAction": { "forward": { "targetGroups": [ { "targetGroupIdentifier": "tg-0eaa4b9ab4EXAMPLE", "weight": 100 } ] } }, "id": "listener-07cc7fb0abEXAMPLE", "name": "my-service-listener", "port": 443, "protocol": "HTTPS", "serviceArn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE", "serviceId": "svc-0285b53b2eEXAMPLE" }`For more information, see [Listeners](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource-configuration`.

- **AWS CLI**
- 
            
                    **To create a resource configuration**The following `create-resource-configuration`example creates a resource configuration that specifies a single IPv4 address.`aws vpc-lattice create-resource-configuration \ --name``my-resource-config`\ --type`SINGLE`\ --resource-gateway-identifier`rgw-0bba03f3d56060135`\ --resource-configuration-definition '`ipResource={ipAddress=10.0.14.85}`'Output: `{ "allowAssociationToShareableServiceNetwork": true, "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-07129f3acded87625", "id": "rcfg-07129f3acded87625", "name": "my-resource-config", "portRanges": [ "1-65535" ], "protocol": "TCP", "resourceConfigurationDefinition": { "ipResource": { "ipAddress": "10.0.14.85" } }, "resourceGatewayId": "rgw-0bba03f3d56060135", "status": "ACTIVE", "type": "SINGLE" }`For more information, see [Resource configurations for VPC resources](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateResourceConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource-gateway`.

- **AWS CLI**
- 
            
                    **To create a resource gateway**The following `create-resource-gateway`example creates a resource gateway for the specified subnet.`aws vpc-lattice create-resource-gateway \ --name``my-resource-gateway`\ --vpc-identifier`vpc-0bf4c2739bc05a69`\ --subnet-ids`subnet-08e8943905b63a683`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourcegateway/rgw-0bba03f3d56060135", "id": "rgw-0bba03f3d56060135", "ipAddressType": "IPV4", "name": "my-resource-gateway", "securityGroupIds": [ "sg-087ffd596c5fe962c" ], "status": "ACTIVE", "subnetIds": [ "subnet-08e8943905b63a683" ], "vpcIdentifier": "vpc-0bf4c2739bc05a694" }`For more information, see [Resource gateways in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateResourceGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-resource-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service-network-service-association`.

- **AWS CLI**
- 
            
                    **To create a service association**The following `create-service-network-service-association`example associates the specified service with the specified service network.`aws vpc-lattice create-service-network-service-association \ --service-identifier``svc-0285b53b2eEXAMPLE`\ --service-network-identifier`sn-080ec7dc93EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetworkserviceassociation/snsa-0e16955a8cEXAMPLE", "createdBy": "123456789012", "dnsEntry": { "domainName": "my-lattice-service-0285b53b2eEXAMPLE.7d67968.vpc-lattice-svcs.us-east-2.on.aws", "hostedZoneId": "Z09127221KTH2CEXAMPLE" }, "id": "snsa-0e16955a8cEXAMPLE", "status": "CREATE_IN_PROGRESS" }`For more information, see [Manage service associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateServiceNetworkServiceAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-service-network-service-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service-network-vpc-association`.

- **AWS CLI**
- 
            
                    **To create a VPC association**The following `create-service-network-vpc-association`example associates the specified vpc with the specified service network. The specified security group controls which resources in the VPC can access the service network and its services.`aws vpc-lattice create-service-network-vpc-association \ --vpc-identifier``vpc-0a1b2c3d4eEXAMPLE`\ --service-network-identifier`sn-080ec7dc93EXAMPLE`\ --security-group-ids`sg-0aee16bc6cEXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetworkvpcassociation/snva-0821fc8631EXAMPLE", "createdBy": "123456789012", "id": "snva-0821fc8631EXAMPLE", "securityGroupIds": [ "sg-0aee16bc6cEXAMPLE" ], "status": "CREATE_IN_PROGRESS" }`For more information, see [Manage VPC associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateServiceNetworkVpcAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-service-network-vpc-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service-network`.

- **AWS CLI**
- 
            
                    **To create a service network**The following `create-service-network`example creates a service network with the specified name.`aws vpc-lattice create-service-network \ --name``my-service-network`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-080ec7dc93EXAMPLE", "authType": "NONE", "id": "sn-080ec7dc93EXAMPLE", "name": "my-service-network" }`For more information, see [Service networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateServiceNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-service-network.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service`.

- **AWS CLI**
- 
            
                    **To create a service**The following `create-service`example creates a service with the specified name.`aws vpc-lattice create-service \ --name``my-lattice-service`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE", "authType": "NONE", "dnsEntry": { "domainName": "my-lattice-service-0285b53b2eEXAMPLE.1a2b3c4.vpc-lattice-svcs.us-east-2.on.aws", "hostedZoneId": "Z09127221KTH2CEXAMPLE" }, "id": "svc-0285b53b2eEXAMPLE", "name": "my-lattice-service", "status": "CREATE_IN_PROGRESS" }`For more information, see [Services in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-target-group`.

- **AWS CLI**
- 
            
                    **Example 1: To create a target group of type INSTANCE**The following `create-target-group`example creates a target group with the specified name, type, and configuration.`aws vpc-lattice create-target-group \ --name``my-lattice-target-group-instance`\ --type`INSTANCE`\ --config`file://tg-config.json`Contents of `tg-config.json`:`{ "port": 443, "protocol": "HTTPS", "protocolVersion": "HTTP1", "vpcIdentifier": "vpc-f1663d9868EXAMPLE" }`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE", "config": { "healthCheck": { "enabled": true, "healthCheckIntervalSeconds": 30, "healthCheckTimeoutSeconds": 5, "healthyThresholdCount": 5, "matcher": { "httpCode": "200" }, "path": "/", "protocol": "HTTPS", "protocolVersion": "HTTP1", "unhealthyThresholdCount": 2 }, "port": 443, "protocol": "HTTPS", "protocolVersion": "HTTP1", "vpcIdentifier": "vpc-f1663d9868EXAMPLE" }, "id": "tg-0eaa4b9ab4EXAMPLE", "name": "my-lattice-target-group-instance", "status": "CREATE_IN_PROGRESS", "type": "INSTANCE" }`**Example 2: To create a target group of type IP**The following `create-target-group`example creates a target group with the specified name, type, and configuration.`aws vpc-lattice create-target-group \ --name``my-lattice-target-group-ip`\ --type`IP`\ --config`file://tg-config.json`Contents of `tg-config.json`:`{ "ipAddressType": "IPV4", "port": 443, "protocol": "HTTPS", "protocolVersion": "HTTP1", "vpcIdentifier": "vpc-f1663d9868EXAMPLE" }`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE", "config": { "healthCheck": { "enabled": true, "healthCheckIntervalSeconds": 30, "healthCheckTimeoutSeconds": 5, "healthyThresholdCount": 5, "matcher": { "httpCode": "200" }, "path": "/", "protocol": "HTTPS", "protocolVersion": "HTTP1", "unhealthyThresholdCount": 2 }, "ipAddressType": "IPV4", "port": 443, "protocol": "HTTPS", "protocolVersion": "HTTP1", "vpcIdentifier": "vpc-f1663d9868EXAMPLE" }, "id": "tg-0eaa4b9ab4EXAMPLE", "name": "my-lattice-target-group-ip", "status": "CREATE_IN_PROGRESS", "type": "IP" }`**Example 3: To create a target group of type LAMBDA**The following `create-target-group`example creates a target group with the specified name, type, and configuration.`aws vpc-lattice create-target-group \ --name``my-lattice-target-group-lambda`\ --type`LAMBDA`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE", "id": "tg-0eaa4b9ab4EXAMPLE", "name": "my-lattice-target-group-lambda", "status": "CREATE_IN_PROGRESS", "type": "LAMBDA" }`**Example 4: To create a target group of type ALB**The following `create-target-group`example creates a target group with the specified name, type, and configuration.`aws vpc-lattice create-target-group \ --name``my-lattice-target-group-alb`\ --type`ALB`\ --config`file://tg-config.json`Contents of `tg-config.json`:`{ "port": 443, "protocol": "HTTPS", "protocolVersion": "HTTP1", "vpcIdentifier": "vpc-f1663d9868EXAMPLE" }`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE", "config": { "port": 443, "protocol": "HTTPS", "protocolVersion": "HTTP1", "vpcIdentifier": "vpc-f1663d9868EXAMPLE" }, "id": "tg-0eaa4b9ab4EXAMPLE", "name": "my-lattice-target-group-alb", "status": "CREATE_IN_PROGRESS", "type": "ALB" }`For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [CreateTargetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/create-target-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-auth-policy`.

- **AWS CLI**
- 
            
                    **To delete an auth policy**The following `delete-auth-policy`example deletes the auth policy for the specified service.`aws vpc-lattice delete-auth-policy \ --resource-identifier``svc-0285b53b2eEXAMPLE`This command produces no output. For more information, see [Auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteAuthPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-auth-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-listener`.

- **AWS CLI**
- 
            
                    **To delete a listener**The following `delete-listener`example deletes the specified listener.`aws vpc-lattice delete-listener \ --listener-identifier``listener-07cc7fb0abEXAMPLE`\ --service-identifier`svc-0285b53b2eEXAMPLE`This command produces no output. For more information, see [Listeners](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listeners.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-configuration`.

- **AWS CLI**
- 
            
                    **To delete a resource configuration**The following `delete-resource-configuration`example deletes the specified resource configuration.`aws vpc-lattice delete-resource-configuration \ --resource-configuration-identifier``rcfg-07129f3acded87625`This command produces no output. For more information, see [Resource gateways in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteResourceConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-resource-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-gateway`.

- **AWS CLI**
- 
            
                    **To delete a resource gateway**The following `delete-resource-gateway`example deletes the specified resource gateway.`aws vpc-lattice delete-resource-gateway \ --resource-gateway-identifier``rgw-0bba03f3d56060135`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourcegateway/rgw-0bba03f3d56060135", "id": "rgw-0bba03f3d56060135", "name": "my-resource-gateway", "status": "DELETE_IN_PROGRESS" }`For more information, see [Resource gateways in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteResourceGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-resource-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service-network-service-association`.

- **AWS CLI**
- 
            
                    **To delete a service association**The following `delete-service-network-service-association`example disassociates the specified service association.`aws vpc-lattice delete-service-network-service-association \ --service-network-service-association-identifier``snsa-031fabb4d8EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetworkserviceassociation/snsa-031fabb4d8EXAMPLE", "id": "snsa-031fabb4d8EXAMPLE", "status": "DELETE_IN_PROGRESS" }`For more information, see [Manage service associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteServiceNetworkServiceAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-service-network-service-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service-network-vpc-association`.

- **AWS CLI**
- 
            
                    **To delete a VPC association**The following `delete-service-network-vpc-association`example disassociates the specified VPC association.`aws vpc-lattice delete-service-network-vpc-association \ --service-network-vpc-association-identifier``snva-0821fc8631EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetworkvpcassociation/snva-0821fc8631EXAMPLE", "id": "snva-0821fc8631EXAMPLE", "status": "DELETE_IN_PROGRESS" }`For more information, see [Manage VPC associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteServiceNetworkVpcAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-service-network-vpc-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service-network`.

- **AWS CLI**
- 
            
                    **To delete a service network**The following `delete-service-network`example deletes the specified service network.`aws vpc-lattice delete-service-network \ --service-network-identifier``sn-080ec7dc93EXAMPLE`This command produces no output. For more information, see [Service networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteServiceNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-service-network.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service`.

- **AWS CLI**
- 
            
                    **To delete a service**The following `delete-service`example deletes the specified service.`aws vpc-lattice delete-service \ --service-identifier``svc-0285b53b2eEXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-west-2:123456789012:service/svc-0285b53b2eEXAMPLE", "id": "svc-0285b53b2eEXAMPLE", "name": "my-lattice-service", "status": "DELETE_IN_PROGRESS" }`For more information, see [Services in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-target-group`.

- **AWS CLI**
- 
            
                    **To delete a target group**The following `delete-target-group`example deletes the specified target group.`aws vpc-lattice delete-target-group \ --target-group-identifier``tg-0eaa4b9ab4EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE", "id": "tg-0eaa4b9ab4EXAMPLE", "status": "DELETE_IN_PROGRESS" }`For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeleteTargetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/delete-target-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-targets`.

- **AWS CLI**
- 
            
                    **To deregister a target**The following `deregister-targets`example deregisters the specified target from the specified target group.`aws vpc-lattice deregister-targets \ --targets``i-07dd579bc5EXAMPLE`\ --target-group-identifier`tg-0eaa4b9ab4EXAMPLE`Output: `{ "successful": [ { "id": "i-07dd579bc5EXAMPLE", "port": 443 } ], "unsuccessful": [] }`For more information, see [Register targets](https://docs.aws.amazon.com/vpc-lattice/latest/ug/register-targets.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [DeregisterTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/deregister-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-auth-policy`.

- **AWS CLI**
- 
            
                    **To get information about an auth policy**The following `get-auth-policy`example gets information about the auth policy for the specified service.`aws vpc-lattice get-auth-policy \ --resource-identifier``svc-0285b53b2eEXAMPLE`Output: `{ "createdAt": "2023-06-07T03:51:20.266Z", "lastUpdatedAt": "2023-06-07T04:39:27.082Z", "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:role/my-clients\"},\"Action\":\"vpc-lattice-svcs:Invoke\",\"Resource\":\"arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE\"}]}", "state": "Active" }`For more information, see [Auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetAuthPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-auth-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-listener`.

- **AWS CLI**
- 
            
                    **To get information about a service listener**The following `get-listener`example gets information about the specified listener for the specified service.`aws vpc-lattice get-listener \ --listener-identifier``listener-0ccf55918cEXAMPLE`\ --service-identifier`svc-0285b53b2eEXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE/listener/listener-0ccf55918cEXAMPLE", "createdAt": "2023-05-07T05:08:45.192Z", "defaultAction": { "forward": { "targetGroups": [ { "targetGroupIdentifier": "tg-0ff213abb6EXAMPLE", "weight": 1 } ] } }, "id": "listener-0ccf55918cEXAMPLE", "lastUpdatedAt": "2023-05-07T05:08:45.192Z", "name": "http-80", "port": 80, "protocol": "HTTP", "serviceArn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE", "serviceId": "svc-0285b53b2eEXAMPLE" }`For more information, see [Define routing](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#define-routing)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetListener](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-listener.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-configuration`.

- **AWS CLI**
- 
            
                    **To get information about a resource configuration**The following `get-resource-configuration`example gets information about the specified resource configuration.`aws vpc-lattice get-resource-configuration \ --resource-configuration-identifier``rcfg-07129f3acded87625`Output: `{ "allowAssociationToShareableServiceNetwork": true, "amazonManaged": false, "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-07129f3acded87625", "createdAt": "2025-02-01T00:57:35.871000+00:00", "id": "rcfg-07129f3acded87625", "lastUpdatedAt": "2025-02-01T00:57:46.874000+00:00", "name": "my-resource-config", "portRanges": [ "1-65535" ], "protocol": "TCP", "resourceConfigurationDefinition": { "ipResource": { "ipAddress": "10.0.14.85" } }, "resourceGatewayId": "rgw-0bba03f3d56060135", "status": "ACTIVE", "type": "SINGLE" }`For more information, see [Resource gateways in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetResourceConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-resource-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource-gateway`.

- **AWS CLI**
- 
            
                    **To get information about a resource gateway**The following `get-resource-gateway`example gets information about the specified resource gateway.`aws vpc-lattice get-resource-gateway \ --resource-gateway-identifier``rgw-0bba03f3d56060135`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourcegateway/rgw-0bba03f3d56060135", "createdAt": "2025-02-01T00:57:33.241000+00:00", "id": "rgw-0bba03f3d56060135", "ipAddressType": "IPV4", "lastUpdatedAt": "2025-02-01T00:57:44.351000+00:00", "name": "my-resource-gateway", "securityGroupIds": [ "sg-087ffd596c5fe962c" ], "status": "ACTIVE", "subnetIds": [ "subnet-08e8943905b63a683" ], "vpcId": "vpc-0bf4c2739bc05a694" }`For more information, see [Resource gateways in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetResourceGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-resource-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-network-service-association`.

- **AWS CLI**
- 
            
                    **To get information about a service association**The following `get-service-network-service-association`example gets information about the specified service association.`aws vpc-lattice get-service-network-service-association \ --service-network-service-association-identifier``snsa-031fabb4d8EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetworkserviceassociation/snsa-031fabb4d8EXAMPLE", "createdAt": "2023-05-05T21:48:16.076Z", "createdBy": "123456789012", "dnsEntry": { "domainName": "my-lattice-service-0285b53b2eEXAMPLE.7d67968.vpc-lattice-svcs.us-east-2.on.aws", "hostedZoneId": "Z09127221KTH2CEXAMPLE" }, "id": "snsa-031fabb4d8EXAMPLE", "serviceArn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE", "serviceId": "svc-0285b53b2eEXAMPLE", "serviceName": "my-lattice-service", "serviceNetworkArn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-080ec7dc93EXAMPLE", "serviceNetworkId": "sn-080ec7dc93EXAMPLE", "serviceNetworkName": "my-service-network", "status": "ACTIVE" }`For more information, see [Manage service associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetServiceNetworkServiceAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-service-network-service-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-network-vpc-association`.

- **AWS CLI**
- 
            
                    **To get information about a VPC association**The following `get-service-network-vpc-association`example gets information about the specified VPC association.`aws vpc-lattice get-service-network-vpc-association \ --service-network-vpc-association-identifier``snva-0821fc8631EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetworkvpcassociation/snva-0821fc8631EXAMPLE", "createdAt": "2023-06-06T23:41:08.421Z", "createdBy": "123456789012", "id": "snva-0c5dcb60d6EXAMPLE", "lastUpdatedAt": "2023-06-06T23:41:08.421Z", "securityGroupIds": [ "sg-0aee16bc6cEXAMPLE" ], "serviceNetworkArn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-080ec7dc93EXAMPLE", "serviceNetworkId": "sn-080ec7dc93EXAMPLE", "serviceNetworkName": "my-service-network", "status": "ACTIVE", "vpcId": "vpc-0a1b2c3d4eEXAMPLE" }`For more information, see [Manage VPC associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetServiceNetworkVpcAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-service-network-vpc-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-network`.

- **AWS CLI**
- 
            
                    **To get information about a service network**The following `get-service-network`example gets information about the specified service network.`aws vpc-lattice get-service-network \ --service-network-identifier``sn-080ec7dc93EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-080ec7dc93EXAMPLE", "authType": "AWS_IAM", "createdAt": "2023-05-05T15:26:08.417Z", "id": "sn-080ec7dc93EXAMPLE", "lastUpdatedAt": "2023-05-05T15:26:08.417Z", "name": "my-service-network", "numberOfAssociatedServices": 2, "numberOfAssociatedVPCs": 3 }`For more information, see [Service networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetServiceNetwork](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-service-network.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service`.

- **AWS CLI**
- 
            
                    **To get information about a service**The following `get-service`example gets information about the specified service.`aws vpc-lattice get-service \ --service-identifier``svc-0285b53b2eEXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE", "authType": "AWS_IAM", "createdAt": "2023-05-05T21:35:29.339Z", "dnsEntry": { "domainName": "my-lattice-service-0285b53b2eEXAMPLE.7d67968.vpc-lattice-svcs.us-east-2.on.aws", "hostedZoneId": "Z09127221KTH2CFUOHIZH" }, "id": "svc-0285b53b2eEXAMPLE", "lastUpdatedAt": "2023-05-05T21:35:29.339Z", "name": "my-lattice-service", "status": "ACTIVE" }`For more information, see [Services](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-target-group`.

- **AWS CLI**
- 
            
                    **To get information about a target group**The following `get-target-group`example gets information about the specified target group, which has a target type of`INSTANCE`.`aws vpc-lattice get-target-group \ --target-group-identifier``tg-0eaa4b9ab4EXAMPLE`Output: `{ "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-0eaa4b9ab4EXAMPLE", "config": { "healthCheck": { "enabled": true, "healthCheckIntervalSeconds": 30, "healthCheckTimeoutSeconds": 5, "healthyThresholdCount": 5, "matcher": { "httpCode": "200" }, "path": "/", "protocol": "HTTPS", "protocolVersion": "HTTP1", "unhealthyThresholdCount": 2 }, "port": 443, "protocol": "HTTPS", "protocolVersion": "HTTP1", "vpcIdentifier": "vpc-f1663d9868EXAMPLE" }, "createdAt": "2023-05-06T04:41:04.122Z", "id": "tg-0eaa4b9ab4EXAMPLE", "lastUpdatedAt": "2023-05-06T04:41:04.122Z", "name": "my-target-group", "serviceArns": [ "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE" ], "status": "ACTIVE", "type": "INSTANCE" }`For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [GetTargetGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/get-target-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-listeners`.

- **AWS CLI**
- 
            
                    **To list service listeners**The following `list-listeners`example lists the listeners for the specified service.`aws vpc-lattice list-listeners \ --service-identifier``svc-0285b53b2eEXAMPLE`Output: `{ "items": [ { "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE/listener/listener-0ccf55918cEXAMPLE", "createdAt": "2023-05-07T05:08:45.192Z", "id": "listener-0ccf55918cEXAMPLE", "lastUpdatedAt": "2023-05-07T05:08:45.192Z", "name": "http-80", "port": 80, "protocol": "HTTP" } ] }`For more information, see [Define routing](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html#define-routing)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListListeners](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-listeners.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-configurations`.

- **AWS CLI**
- 
            
                    **To list your resource configurations**The following `list-resource-configurations`example lists your resource configurations.`aws vpc-lattice list-resource-configurations`Output: `{ "items": [ { "amazonManaged": false, "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-07129f3acded87625", "createdAt": "2025-02-01T00:57:35.871000+00:00", "id": "rcfg-07129f3acded87625", "lastUpdatedAt": "2025-02-01T00:57:46.874000+00:00", "name": "my-resource-config", "resourceGatewayId": "rgw-0bba03f3d56060135", "status": "ACTIVE", "type": "SINGLE" } ] }`For more information, see [Resource configurations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListResourceConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-resource-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-endpoint-associations`.

- **AWS CLI**
- 
            
                    **To list the VPC endpoint associations**The following `list-resource-endpoint-associations`example lists the VPC endpoints associated with the specified resource configuration.`aws vpc-lattice list-resource-endpoint-associations \ --resource-configuration-identifier``rcfg-07129f3acded87625`Output: `{ "items": [ { "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceendpointassociation/rea-0956a7435baf89326", "createdAt": "2025-02-01T00:57:38.998000+00:00", "id": "rea-0956a7435baf89326", "resourceConfigurationArn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourceconfiguration/rcfg-07129f3acded87625", "resourceConfigurationId": "rcfg-07129f3acded87625", "vpcEndpointId": "vpce-019b90d6f16d4f958", "vpcEndpointOwner": "123456789012" } ] }`For more information, see [Manage associations for a VPC Lattice resource configuration](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-configuration-associations.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListResourceEndpointAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-resource-endpoint-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-gateways`.

- **AWS CLI**
- 
            
                    **To list your resource gateways**The following `list-resource-gateways`example lists your resource gateways.`aws vpc-lattice list-resource-gateways`Output: `{ "items": [ { "arn": "arn:aws:vpc-lattice:us-east-1:123456789012:resourcegateway/rgw-0bba03f3d56060135", "createdAt": "2025-02-01T00:57:33.241000+00:00", "id": "rgw-0bba03f3d56060135", "ipAddressType": "IPV4", "lastUpdatedAt": "2025-02-01T00:57:44.351000+00:00", "name": "my-resource-gateway", "seurityGroupIds": [ "sg-087ffd596c5fe962c" ], "status": "ACTIVE", "subnetIds": [ "subnet-08e8943905b63a683" ], "vpcIdentifier": "vpc-0bf4c2739bc05a694" } ] }`For more information, see [Resource gateways in VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/resource-gateway.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListResourceGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-resource-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-network-service-associations`.

- **AWS CLI**
- 
            
                    **To list service associations**The following `list-service-network-service-associations`example lists the service associations for the specified service network. The`--query`option scopes the output to the IDs of the service associations.`aws vpc-lattice list-service-network-service-associations \ --service-network-identifier``sn-080ec7dc93EXAMPLE`\ --query`items[*].id`Output: `[ "snsa-031fabb4d8EXAMPLE", "snsa-0e16955a8cEXAMPLE" ]`For more information, see [Manage service associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-service-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListServiceNetworkServiceAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-service-network-service-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-network-vpc-associations`.

- **AWS CLI**
- 
            
                    **To list VPC associations**The following `list-service-network-vpc-associations`example lists the VPC associations for the specified service network. The`--query`option scopes the output to the IDs of the VPC associations.`aws vpc-lattice list-service-network-vpc-associations \ --service-network-identifier``sn-080ec7dc93EXAMPLE`\ --query`items[*].id`Output: `[ "snva-0821fc8631EXAMPLE", "snva-0c5dcb60d6EXAMPLE" ]`For more information, see [Manage VPC associations](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html#service-network-vpc-associations)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListServiceNetworkVpcAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-service-network-vpc-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-network-vpc-endpoint-associations`.

- **AWS CLI**
- 
            
                    **To list the VPC endpoint associations**The following `list-service-network-vpc-endpoint-associations`example lists the VPC endpoints associated with the specific service network.`aws vpc-lattice list-service-network-vpc-endpoint-associations \ --service-network-identifier``sn-0808d1748faee0c1e`Output: `{ "items": [ { "createdAt": "2025-02-01T01:21:36.667000+00:00", "serviceNetworkArn": "arn:aws:vpc-lattice:us-east-1:123456789012:servicenetwork/sn-0808d1748faee0c1e", "state": "ACTIVE", "vpcEndpointId": "vpce-0cc199f605eaeace7", "vpcEndpointOwnerId": "123456789012" } ] }`For more information, see [Manage the associations for a VPC Lattice service network](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-network-associations.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListServiceNetworkVpcEndpointAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-service-network-vpc-endpoint-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-networks`.

- **AWS CLI**
- 
            
                    **To list your service networks**The following `list-service-networks`example lists the service networks owned or shared with the calling account. The`--query`option scopes the results to the Amazon Resource Names (ARN) of the service networks.`aws vpc-lattice list-service-networks \ --query``items[*].arn`Output: `[ "arn:aws:vpc-lattice:us-east-2:123456789012:servicenetwork/sn-080ec7dc93EXAMPLE", "arn:aws:vpc-lattice:us-east-2:111122223333:servicenetwork/sn-0ec4d436cfEXAMPLE" ]`For more information, see [Service networks](https://docs.aws.amazon.com/vpc-lattice/latest/ug/service-networks.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListServiceNetworks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-service-networks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-services`.

- **AWS CLI**
- 
            
                    **To list your services**The following `list-services`example lists the services owned or shared with the calling account. The`--query`option scopes the results to the Amazon Resource Names (ARN) of the services.`aws vpc-lattice list-services \ --query``items[*].arn`Output: `[ "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE", "arn:aws:vpc-lattice:us-east-2:111122223333:service/svc-0b8ac96550EXAMPLE" ]`For more information, see [Services](https://docs.aws.amazon.com/vpc-lattice/latest/ug/services.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-target-groups`.

- **AWS CLI**
- 
            
                    **To list your target groups**The following `list-target-groups`example lists the target groups with a target type of`LAMBDA`.`aws vpc-lattice list-target-groups \ --target-group-type``LAMBDA`Output: `{ "items": [ { "arn": "arn:aws:vpc-lattice:us-east-2:123456789012:targetgroup/tg-045c1b7d9dEXAMPLE", "createdAt": "2023-05-06T05:22:16.637Z", "id": "tg-045c1b7d9dEXAMPLE", "lastUpdatedAt": "2023-05-06T05:22:16.637Z", "name": "my-target-group-lam", "serviceArns": [ "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE" ], "status": "ACTIVE", "type": "LAMBDA" } ] }`For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListTargetGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-target-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-targets`.

- **AWS CLI**
- 
            
                    **To list the targets for a target group**The following `list-targets`example lists the targets for the specified target group.`aws vpc-lattice list-targets \ --target-group-identifier``tg-0eaa4b9ab4EXAMPLE`Output: `{ "items": [ { "id": "i-07dd579bc5EXAMPLE", "port": 443, "status": "HEALTHY" }, { "id": "i-047b3c9078EXAMPLE", "port": 443, "reasonCode": "HealthCheckFailed", "status": "UNHEALTHY" } ] }`For more information, see [Target groups](https://docs.aws.amazon.com/vpc-lattice/latest/ug/target-groups.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [ListTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/list-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-auth-policy`.

- **AWS CLI**
- 
            
                    **To create an auth policy for a service**The following `put-auth-policy`example grants access to requests from any authenticated principal that uses the specified IAM role. The resource is the ARN of the service to which the policy is attached.`aws vpc-lattice put-auth-policy \ --resource-identifier``svc-0285b53b2eEXAMPLE`\ --policy`file://auth-policy.json`Contents of `auth-policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::123456789012:role/my-clients" }, "Action": "vpc-lattice-svcs:Invoke", "Resource": "arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE" } ] }`Output: `{ "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::123456789012:role/my-clients\"},\"Action\":\"vpc-lattice-svcs:Invoke\",\"Resource\":\"arn:aws:vpc-lattice:us-east-2:123456789012:service/svc-0285b53b2eEXAMPLE\"}]}", "state": "Active" }`For more information, see [Auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [PutAuthPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/put-auth-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-targets`.

- **AWS CLI**
- 
            
                    **To register a target**The following `register-targets`example registers the specified targets with the specified target group.`aws vpc-lattice register-targets \ --targets``id=i-047b3c9078EXAMPLE``id=i-07dd579bc5EXAMPLE`\ --target-group-identifier`tg-0eaa4b9ab4EXAMPLE`Output: `{ "successful": [ { "id": "i-07dd579bc5EXAMPLE", "port": 443 } ], "unsuccessful": [ { "failureCode": "UnsupportedTarget", "failureMessage": "Instance targets must be in the same VPC as their target group", "id": "i-047b3c9078EXAMPLE", "port": 443 } ] }`For more information, see [Register targets](https://docs.aws.amazon.com/vpc-lattice/latest/ug/register-targets.html)in the*Amazon VPC Lattice User Guide*.- 
                    For API details, see [RegisterTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/vpc-lattice/register-targets.html)in*AWS CLI Command Reference*.
 
-