# Lightsail examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_lightsail_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_lightsail_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Lightsail.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `allocate-static-ip`.

- **AWS CLI**
- 
            
                    **To create a static IP**The following `allocate-static-ip`example creates the specified static IP, which can be attached to an instance.`aws lightsail allocate-static-ip \ --static-ip-name``StaticIp-1`Output: `{ "operations": [ { "id": "b5d06d13-2f19-4683-889f-dEXAMPLEed79", "resourceName": "StaticIp-1", "resourceType": "StaticIp", "createdAt": 1571071325.076, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "AllocateStaticIp", "status": "Succeeded", "statusChangedAt": 1571071325.274 } ] }`- 
                    For API details, see [AllocateStaticIp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/allocate-static-ip.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-disk`.

- **AWS CLI**
- 
            
                    **To attach a block storage disk to an instance**The following `attach-disk`example attaches disk`Disk-1`to instance`WordPress_Multisite-1`with the disk path of`/dev/xvdf``aws lightsail attach-disk \ --disk-name``Disk-1`\ --disk-path`/dev/xvdf`\ --instance-name`WordPress_Multisite-1`Output: `{ "operations": [ { "id": "10a08267-19ce-43be-b913-6EXAMPLE7e80", "resourceName": "Disk-1", "resourceType": "Disk", "createdAt": 1571071465.472, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "WordPress_Multisite-1", "operationType": "AttachDisk", "status": "Started", "statusChangedAt": 1571071465.472 }, { "id": "2912c477-5295-4539-88c9-bEXAMPLEd1f0", "resourceName": "WordPress_Multisite-1", "resourceType": "Instance", "createdAt": 1571071465.474, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "Disk-1", "operationType": "AttachDisk", "status": "Started", "statusChangedAt": 1571071465.474 } ] }`- 
                    For API details, see [AttachDisk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-disk.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-instances-to-load-balancer`.

- **AWS CLI**
- 
            
                    **To attach instances to a load balancer**The following `attach-instances-to-load-balancer`example attaches instances`MEAN-1`,`MEAN-2`, and`MEAN-3`to the load balancer`LoadBalancer-1`.`aws lightsail attach-instances-to-load-balancer \ --instance-names {"MEAN-1","MEAN-2","MEAN-3"} \ --load-balancer-name``LoadBalancer-1`Output: `{ "operations": [ { "id": "8055d19d-abb2-40b9-b527-1EXAMPLE3c7b", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571071699.892, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "MEAN-2", "operationType": "AttachInstancesToLoadBalancer", "status": "Started", "statusChangedAt": 1571071699.892 }, { "id": "c35048eb-8538-456a-a118-0EXAMPLEfb73", "resourceName": "MEAN-2", "resourceType": "Instance", "createdAt": 1571071699.887, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "LoadBalancer-1", "operationType": "AttachInstancesToLoadBalancer", "status": "Started", "statusChangedAt": 1571071699.887 }, { "id": "910d09e0-adc5-4372-bc2e-0EXAMPLEd891", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571071699.882, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "MEAN-3", "operationType": "AttachInstancesToLoadBalancer", "status": "Started", "statusChangedAt": 1571071699.882 }, { "id": "178b18ac-43e8-478c-9bed-1EXAMPLE4755", "resourceName": "MEAN-3", "resourceType": "Instance", "createdAt": 1571071699.901, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "LoadBalancer-1", "operationType": "AttachInstancesToLoadBalancer", "status": "Started", "statusChangedAt": 1571071699.901 }, { "id": "fb62536d-2a98-4190-a6fc-4EXAMPLE7470", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571071699.885, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "MEAN-1", "operationType": "AttachInstancesToLoadBalancer", "status": "Started", "statusChangedAt": 1571071699.885 }, { "id": "787dac0d-f98d-46c3-8571-3EXAMPLE5a85", "resourceName": "MEAN-1", "resourceType": "Instance", "createdAt": 1571071699.901, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "LoadBalancer-1", "operationType": "AttachInstancesToLoadBalancer", "status": "Started", "statusChangedAt": 1571071699.901 } ] }`- 
                    For API details, see [AttachInstancesToLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-instances-to-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-load-balancer-tls-certificate`.

- **AWS CLI**
- 
            
                    **To attach a TLS certificate to a load balancer**The following `attach-load-balancer-tls-certificate`example attaches the load balancer TLS certificate`Certificate2`to the load balancer`LoadBalancer-1`.`aws lightsail attach-load-balancer-tls-certificate \ --certificate-name``Certificate2`\ --load-balancer-name`LoadBalancer-1`Output: `{ "operations": [ { "id": "cf1ad6e3-3cbb-4b8a-a7f2-3EXAMPLEa118", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571072255.416, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "Certificate2", "operationType": "AttachLoadBalancerTlsCertificate", "status": "Succeeded", "statusChangedAt": 1571072255.416 }, { "id": "dae1bcfb-d531-4c06-b4ea-bEXAMPLEc04e", "resourceName": "Certificate2", "resourceType": "LoadBalancerTlsCertificate", "createdAt": 1571072255.416, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "LoadBalancer-1", "operationType": "AttachLoadBalancerTlsCertificate", "status": "Succeeded", "statusChangedAt": 1571072255.416 } ] }`- 
                    For API details, see [AttachLoadBalancerTlsCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-load-balancer-tls-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `attach-static-ip`.

- **AWS CLI**
- 
            
                    **To attach a static IP to an instance**The following `attach-static-ip`example attaches static IP`StaticIp-1`to instance`MEAN-1`.`aws lightsail attach-static-ip \ --static-ip-name``StaticIp-1`\ --instance-name`MEAN-1`Output: `{ "operations": [ { "id": "45e6fa13-4808-4b8d-9292-bEXAMPLE20b2", "resourceName": "StaticIp-1", "resourceType": "StaticIp", "createdAt": 1571072569.375, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "MEAN-1", "operationType": "AttachStaticIp", "status": "Succeeded", "statusChangedAt": 1571072569.375 }, { "id": "9ee09a17-863c-4e51-8a6d-3EXAMPLE5475", "resourceName": "MEAN-1", "resourceType": "Instance", "createdAt": 1571072569.376, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "StaticIp-1", "operationType": "AttachStaticIp", "status": "Succeeded", "statusChangedAt": 1571072569.376 } ] }`- 
                    For API details, see [AttachStaticIp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/attach-static-ip.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `close-instance-public-ports`.

- **AWS CLI**
- 
            
                    **To close firewall ports for an instance**The following `close-instance-public-ports`example closes TCP port`22`on instance`MEAN-2`.`aws lightsail close-instance-public-ports \ --instance-name``MEAN-2`\ --port-info`fromPort=22,protocol=TCP,toPort=22`Output: `{ "operation": { "id": "4f328636-1c96-4649-ae6d-1EXAMPLEf446", "resourceName": "MEAN-2", "resourceType": "Instance", "createdAt": 1571072845.737, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "22/tcp", "operationType": "CloseInstancePublicPorts", "status": "Succeeded", "statusChangedAt": 1571072845.737 } }`- 
                    For API details, see [CloseInstancePublicPorts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/close-instance-public-ports.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-snapshot`.

- **AWS CLI**
- 
            
                    **Example 1: To copy a snapshot within the same AWS Region**The following `copy-snapshot`example copies instance snapshot`MEAN-1-1571075291`as instance snapshot`MEAN-1-Copy`within the same AWS Region`us-west-2`.`aws lightsail copy-snapshot \ --source-snapshot-name``MEAN-1-1571075291`\ --target-snapshot-name`MEAN-1-Copy`\ --source-region`us-west-2`Output: `{ "operations": [ { "id": "ced16fc1-f401-4556-8d82-1EXAMPLEb982", "resourceName": "MEAN-1-Copy", "resourceType": "InstanceSnapshot", "createdAt": 1571075581.498, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "us-west-2:MEAN-1-1571075291", "operationType": "CopySnapshot", "status": "Started", "statusChangedAt": 1571075581.498 } ] }`For more information, see [Copying snapshots from one AWS Region to another in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-copying-snapshots-from-one-region-to-another)in the*Lightsail Dev Guide*.**Example 2: To copy a snapshot from one AWS Region to another**The following `copy-snapshot`example copies instance snapshot`MEAN-1-1571075291`as instance snapshot`MEAN-1-1571075291-Copy`from AWS Region`us-west-2`to`us-east-1`.`aws lightsail copy-snapshot \ --source-snapshot-name``MEAN-1-1571075291`\ --target-snapshot-name`MEAN-1-1571075291-Copy`\ --source-region`us-west-2`\ --region`us-east-1`Output: `{ "operations": [ { "id": "91116b79-119c-4451-b44a-dEXAMPLEd97b", "resourceName": "MEAN-1-1571075291-Copy", "resourceType": "InstanceSnapshot", "createdAt": 1571075695.069, "location": { "availabilityZone": "all", "regionName": "us-east-1" }, "isTerminal": false, "operationDetails": "us-west-2:MEAN-1-1571075291", "operationType": "CopySnapshot", "status": "Started", "statusChangedAt": 1571075695.069 } ] }`For more information, see [Copying snapshots from one AWS Region to another in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-copying-snapshots-from-one-region-to-another)in the*Lightsail Dev Guide*.**Example 3: To copy an automatic snapshot within the same AWS Region**The following `copy-snapshot`example copies automatic snapshot`2019-10-14`of instance`WordPress-1`as a manual snapshot`WordPress-1-10142019`in the AWS Region`us-west-2`.`aws lightsail copy-snapshot \ --source-resource-name``WordPress-1`\ --restore-date`2019-10-14`\ --target-snapshot-name`WordPress-1-10142019`\ --source-region`us-west-2`Output: `{ "operations": [ { "id": "be3e6754-cd1d-48e6-ad9f-2EXAMPLE1805", "resourceName": "WordPress-1-10142019", "resourceType": "InstanceSnapshot", "createdAt": 1571082412.311, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "us-west-2:WordPress-1", "operationType": "CopySnapshot", "status": "Started", "statusChangedAt": 1571082412.311 } ] }`For more information, see [Keeping automatic snapshots of instances or disks in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-keeping-automatic-snapshots)in the*Lightsail Dev Guide*.**Example 4: To copy an automatic snapshot from one AWS Region to another**The following `copy-snapshot`example copies automatic snapshot`2019-10-14`of instance`WordPress-1`as a manual snapshot`WordPress-1-10142019`from the AWS Region`us-west-2`to`us-east-1`.`aws lightsail copy-snapshot \ --source-resource-name``WordPress-1`\ --restore-date`2019-10-14`\ --target-snapshot-name`WordPress-1-10142019`\ --source-region`us-west-2`\ --region`us-east-1`Output: `{ "operations": [ { "id": "dffa128b-0b07-476e-b390-bEXAMPLE3775", "resourceName": "WordPress-1-10142019", "resourceType": "InstanceSnapshot", "createdAt": 1571082493.422, "location": { "availabilityZone": "all", "regionName": "us-east-1" }, "isTerminal": false, "operationDetails": "us-west-2:WordPress-1", "operationType": "CopySnapshot", "status": "Started", "statusChangedAt": 1571082493.422 } ] }`For more information, see [Keeping automatic snapshots of instances or disks in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-keeping-automatic-snapshots)in the*Lightsail Dev Guide*.- 
                    For API details, see [CopySnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/copy-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-disk-from-snapshot`.

- **AWS CLI**
- 
            
                    **To create a create a disk from a disk snapshot**The following `create-disk-from-snapshot`example creates a block storage disk named`Disk-2`from the specified block storage disk snapshot. The disk is created in the specified AWS Region and Availability Zone, with 32 GB of storage space.`aws lightsail create-disk-from-snapshot \ --disk-name``Disk-2`\ --disk-snapshot-name`Disk-1-1566839161`\ --availability-zone`us-west-2a`\ --size-in-gb`32`Output: `{ "operations": [ { "id": "d42b605d-5ef1-4b4a-8791-7a3e8b66b5e7", "resourceName": "Disk-2", "resourceType": "Disk", "createdAt": 1569624941.471, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateDiskFromSnapshot", "status": "Started", "statusChangedAt": 1569624941.791 } ] }`For more information, see [Creating a block storage disk from a snapshot in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/create-new-block-storage-disk-from-snapshot)in the*Lightsail Developer Guide*.- 
                    For API details, see [CreateDiskFromSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk-from-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-disk-snapshot`.

- **AWS CLI**
- 
            
                    **Example 1: To create a snapshot of a disk**The following `create-disk-snapshot`example creates a snapshot named`DiskSnapshot-1`of the specified block storage disk.`aws lightsail create-disk-snapshot \ --disk-name``Disk-1`\ --disk-snapshot-name`DiskSnapshot-1`Output: `{ "operations": [ { "id": "fa74c6d2-03a3-4f42-a7c7-792f124d534b", "resourceName": "DiskSnapshot-1", "resourceType": "DiskSnapshot", "createdAt": 1569625129.739, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "Disk-1", "operationType": "CreateDiskSnapshot", "status": "Started", "statusChangedAt": 1569625129.739 }, { "id": "920a25df-185c-4528-87cd-7b85f5488c06", "resourceName": "Disk-1", "resourceType": "Disk", "createdAt": 1569625129.739, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "DiskSnapshot-1", "operationType": "CreateDiskSnapshot", "status": "Started", "statusChangedAt": 1569625129.739 } ] }`**Example 2: To create a snapshot of an instance's system disk**The following `create-disk-snapshot`example creates a snapshot of the specified instance's system disk.`aws lightsail create-disk-snapshot \ --instance-name``WordPress-1`\ --disk-snapshot-name`SystemDiskSnapshot-1`Output: `{ "operations": [ { "id": "f508cf1c-6597-42a6-a4c3-4aebd75af0d9", "resourceName": "SystemDiskSnapshot-1", "resourceType": "DiskSnapshot", "createdAt": 1569625294.685, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "WordPress-1", "operationType": "CreateDiskSnapshot", "status": "Started", "statusChangedAt": 1569625294.685 }, { "id": "0bb9f712-da3b-4d99-b508-3bf871d989e5", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1569625294.685, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "SystemDiskSnapshot-1", "operationType": "CreateDiskSnapshot", "status": "Started", "statusChangedAt": 1569625294.685 } ] }`For more information, see [Snapshots in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-instance-snapshots-in-amazon-lightsail)and[Creating a snapshot of an instance root volume in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-create-an-instance-root-volume-snapshot)in the*Lightsail Developer Guide*.- 
                    For API details, see [CreateDiskSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-disk`.

- **AWS CLI**
- 
            
                    **To create a block storage disk**The following `create-disk`example creates a block storage disk`Disk-1`in the specified AWS Region and Availability Zone, with 32 GB of storage space.`aws lightsail create-disk \ --disk-name``Disk-1`\ --availability-zone`us-west-2a`\ --size-in-gb`32`Output: `{ "operations": [ { "id": "1c85e2ec-86ba-4697-b936-77f4d3dc013a", "resourceName": "Disk-1", "resourceType": "Disk", "createdAt": 1569449220.36, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateDisk", "status": "Started", "statusChangedAt": 1569449220.588 } ] }`- 
                    For API details, see [CreateDisk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-disk.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-domain-entry`.

- **AWS CLI**
- 
            
                    **To create a domain entry (DNS record)**The following `create-domain-entry`example creates a DNS record (A) for the apex of the specified domain that points to an instance's IP address.**Note:**Lightsail's domain-related API operations are available in only the`us-east-1`Region. If your CLI profile is configured to use a different Region, you must include the`--region us-east-1`parameter or the command fails.`aws lightsail create-domain-entry \ --region``us-east-1`\ --domain-name`example.com`\ --domain-entry`name=example.com,type=A,target=192.0.2.0`Output: `{ "operation": { "id": "5be4494d-56f4-41fc-8730-693dcd0ef9e2", "resourceName": "example.com", "resourceType": "Domain", "createdAt": 1569865296.519, "location": { "availabilityZone": "all", "regionName": "global" }, "isTerminal": true, "operationType": "CreateDomainEntry", "status": "Succeeded", "statusChangedAt": 1569865296.519 } }`For more information, see [DNS in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-dns-in-amazon-lightsail)and[Creating a DNS zone to manage your domain's DNS records in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/lightsail-how-to-create-dns-entry)in the*Lightsail Developer Guide*.- 
                    For API details, see [CreateDomainEntry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-domain-entry.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-domain`.

- **AWS CLI**
- 
            
                    **To create a domain (DNS zone)**The following `create-domain`example creates a DNS zone for the specified domain.**Note:**Lightsail's domain-related API operations are available in only the`us-east-1`Region. If your CLI profile is configured to use a different Region, you must include the`--region us-east-1`parameter or the command fails.`aws lightsail create-domain \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "operation": { "id": "64e522c8-9ae1-4c05-9b65-3f237324dc34", "resourceName": "example.com", "resourceType": "Domain", "createdAt": 1569864291.92, "location": { "availabilityZone": "all", "regionName": "global" }, "isTerminal": true, "operationType": "CreateDomain", "status": "Succeeded", "statusChangedAt": 1569864292.109 } }`For more information, see [DNS in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-dns-in-amazon-lightsail)and[Creating a DNS zone to manage your domain's DNS records in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/lightsail-how-to-create-dns-entry)in the*Lightsail Developer Guide*.- 
                    For API details, see [CreateDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-instance-snapshot`.

- **AWS CLI**
- 
            
                    **To create a snapshot of an instance**The following `create-instance-snapshot`example creates a snapshot from the specified instance.`aws lightsail create-instance-snapshot \ --instance-name``WordPress-1`\ --instance-snapshot-name`WordPress-Snapshot-1`Output: `{ "operations": [ { "id": "4c3db559-9dd0-41e7-89c0-2cb88c19786f", "resourceName": "WordPress-Snapshot-1", "resourceType": "InstanceSnapshot", "createdAt": 1569866438.48, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "WordPress-1", "operationType": "CreateInstanceSnapshot", "status": "Started", "statusChangedAt": 1569866438.48 }, { "id": "c04fdc45-2981-488c-88b5-d6d2fd759a6a", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1569866438.48, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "WordPress-Snapshot-1", "operationType": "CreateInstanceSnapshot", "status": "Started", "statusChangedAt": 1569866438.48 } ] }`- 
                    For API details, see [CreateInstanceSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instance-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-instances-from-snapshot`.

- **AWS CLI**
- 
            
                    **To create an instance from a snapshot**The following `create-instances-from-snapshot`example creates an instance from the specified instance snapshot, in the specified AWS Region and Availability Zone, using the $12 USD bundle.**Note:**The bundle that you specify must be equal to or greater in specifications than the bundle of the original source instance used to create the snapshot.`aws lightsail create-instances-from-snapshot \ --instance-snapshot-name``WordPress-1-1569866208`\ --instance-names`WordPress-2`\ --availability-zone`us-west-2a`\ --bundle-id`small_3_0`Output: `{ "operations": [ { "id": "003f8271-b711-464d-b9b8-7f3806cb496e", "resourceName": "WordPress-2", "resourceType": "Instance", "createdAt": 1569865914.908, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateInstancesFromSnapshot", "status": "Started", "statusChangedAt": 1569865914.908 } ] }`- 
                    For API details, see [CreateInstancesFromSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances-from-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-instances`.

- **AWS CLI**
- 
            
                    **Example 1: To create a single instance**The following `create-instances`example creates an instance in the specified AWS Region and Availability Zone, using the WordPress blueprint, and the $5.00 USD bundle.`aws lightsail create-instances \ --instance-names``Instance-1`\ --availability-zone`us-west-2a`\ --blueprint-id`wordpress`\ --bundle-id`nano_3_0`Output: `{ "operations": [ { "id": "9a77158f-7be3-4d6d-8054-cf5ae2b720cc", "resourceName": "Instance-1", "resourceType": "Instance", "createdAt": 1569447986.061, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateInstance", "status": "Started", "statusChangedAt": 1569447986.061 } ] }`**Example 2: To create multiple instances at one time**The following `create-instances`example creates three instances in the specified AWS Region and Availability Zone, using the WordPress blueprint, and the $5.00 USD bundle.`aws lightsail create-instances \ --instance-names {"Instance1","Instance2","Instance3"} \ --availability-zone``us-west-2a`\ --blueprint-id`wordpress`\ --bundle-id`nano_3_0`Output: `{ "operations": [ { "id": "5492f015-9d2e-48c6-8eea-b516840e6903", "resourceName": "Instance1", "resourceType": "Instance", "createdAt": 1569448780.054, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateInstance", "status": "Started", "statusChangedAt": 1569448780.054 }, { "id": "c58b5f46-2676-44c8-b95c-3ad375898515", "resourceName": "Instance2", "resourceType": "Instance", "createdAt": 1569448780.054, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateInstance", "status": "Started", "statusChangedAt": 1569448780.054 }, { "id": "a5ad8006-9bee-4499-9eb7-75e42e6f5882", "resourceName": "Instance3", "resourceType": "Instance", "createdAt": 1569448780.054, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateInstance", "status": "Started", "statusChangedAt": 1569448780.054 } ] }`- 
                    For API details, see [CreateInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-key-pair`.

- **AWS CLI**
- 
            
                    **To create a key pair**The following `create-key-pair`example creates a key pair that you can use to authenticate and connect to an instance.`aws lightsail create-key-pair \ --key-pair-name``MyPersonalKeyPair`The output provides the private key base64 value that you can use to authenticate to instances that use the created key pair. **Note:**Copy and paste the private key base64 value to a safe location because you cannot retrieve it later.`{ "keyPair": { "name": "MyPersonalKeyPair", "arn": "arn:aws:lightsail:us-west-2:111122223333:KeyPair/55025c71-198f-403b-b42f-a69433e724fb", "supportCode": "621291663362/MyPersonalKeyPair", "createdAt": 1569866556.567, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "KeyPair" }, "publicKeyBase64": "ssh-rsa ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCV0xUEwx96amPERH7K1bVT1tTFl9OmNk6o7m5YVHk9xlOdMbDRbFvhtXvw4jzJXXz5pBMxWOaGMz5K8QyTVOznoqp13Z8SBooH29hgmBNXiII1XPzEwqbj8mfo1+YVM5s5VuxWwm+BHUgedGUXno6uF7agqxZNO1kPLJBIVTW26SSYBJ0tE+y804UyVsjrbUqCaMXDhmfXpWulMPwuXhwcKh7e8hwoTfkiX0E6Ql+KqF/MiA3w6DCjEqvvdIO7SiEZJFsuGNfYDDN3w60Rel5MUhmn3OJdn4y/A7NWb3IxL4pPfVE4rgFRKU8n1jp9kwRnlVMVBOWuGXk6n+H6M2f1 ", "privateKeyBase64": "-----BEGIN RSA PRIVATE KEY-----EXAMPLETCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC\nVVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6\nb24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsEXAMPLEd\nBgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN\nMTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD\nVQQHEwdTZWF0dGxlMQ8wDQEXAMPLEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z\nb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt\nYXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMEXAMPLE4GmWIWJ\n21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T\nrDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE\nIbb3OhjZnzcvQAaREXAMPLEMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4\nnUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb\nFFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OEXAMPLELvjx79LjSTb\nNYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=\n-----END RSA PRIVATE KEY-----", "operation": { "id": "67f984db-9994-45fe-ad38-59bafcaf82ef", "resourceName": "MyPersonalKeyPair", "resourceType": "KeyPair", "createdAt": 1569866556.567, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "CreateKeyPair", "status": "Succeeded", "statusChangedAt": 1569866556.704 } }`- 
                    For API details, see [CreateKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-load-balancer-tls-certificate`.

- **AWS CLI**
- 
            
                    **To create a TLS certificate for a load balancer**The following `create-load-balancer-tls-certificate`example creates a TLS certificate that is attached to the specified load balancer. The certificate created applies to the specified domains.**Note:**Only two certificates can be created for a load balancer.`aws lightsail create-load-balancer-tls-certificate \ --certificate-alternative-names``abc.example.com`\ --certificate-domain-name`example.com`\ --certificate-name`MySecondCertificate`\ --load-balancer-name`MyFirstLoadBalancer`Output: `{ "operations": [ { "id": "be663aed-cb46-41e2-9b23-e2f747245bd4", "resourceName": "MySecondCertificate", "resourceType": "LoadBalancerTlsCertificate", "createdAt": 1569867364.971, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "MyFirstLoadBalancer", "operationType": "CreateLoadBalancerTlsCertificate", "status": "Succeeded", "statusChangedAt": 1569867365.219 }, { "id": "f3dfa930-969e-41cc-ac7d-337178716f6d", "resourceName": "MyFirstLoadBalancer", "resourceType": "LoadBalancer", "createdAt": 1569867364.971, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "MySecondCertificate", "operationType": "CreateLoadBalancerTlsCertificate", "status": "Succeeded", "statusChangedAt": 1569867365.219 } ] }`- 
                    For API details, see [CreateLoadBalancerTlsCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-load-balancer-tls-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-load-balancer`.

- **AWS CLI**
- 
            
                    **To create a load balancer**The following `create-load-balancer`example creates a load balancer with a TLS certificate. The TLS certificate applies to the specified domains, and routes traffic to instances on port 80.`aws lightsail create-load-balancer \ --certificate-alternative-names``www.example.com``test.example.com`\ --certificate-domain-name`example.com`\ --certificate-name`Certificate-1`\ --instance-port`80`\ --load-balancer-name`LoadBalancer-1`Output: `{ "operations": [ { "id": "cc7b920a-83d8-4762-a74e-9174fe1540be", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1569867169.406, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateLoadBalancer", "status": "Started", "statusChangedAt": 1569867169.406 }, { "id": "658ed43b-f729-42f3-a8e4-3f8024d3c98d", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancerTlsCertificate", "createdAt": 1569867170.193, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "LoadBalancer-1", "operationType": "CreateLoadBalancerTlsCertificate", "status": "Succeeded", "statusChangedAt": 1569867170.54 }, { "id": "4757a342-5181-4870-b1e0-227eebc35ab5", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1569867170.193, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "Certificate-1", "operationType": "CreateLoadBalancerTlsCertificate", "status": "Succeeded", "statusChangedAt": 1569867170.54 } ] }`For more information, see [Lightsail load balancers](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/understanding-lightsail-load-balancers)in the*Lightsail Developer Guide*.- 
                    For API details, see [CreateLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-relational-database-from-snapshot`.

- **AWS CLI**
- 
            
                    **To create a managed database from a snapshot**The following `create-relational-database-from-snapshot`example creates a managed database from the specified snapshot in the specified AWS Region and Availability Zone, using the $15 USD standard database bundle.**Note:**The bundle that you specify must be equal to or greater in specifications than the bundle of the original source database used to create the snapshot.`aws lightsail create-relational-database-from-snapshot \ --relational-database-snapshot-name``Database-Oregon-1-1566839359`\ --relational-database-name`Database-1`\ --availability-zone`us-west-2a`\ --relational-database-bundle-id`micro_1_0`\ --no-publicly-accessibleOutput: `{ "operations": [ { "id": "ad6d9193-9d5c-4ea1-97ae-8fe6de600b4c", "resourceName": "Database-1", "resourceType": "RelationalDatabase", "createdAt": 1569867916.938, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateRelationalDatabaseFromSnapshot", "status": "Started", "statusChangedAt": 1569867918.643 } ] }`- 
                    For API details, see [CreateRelationalDatabaseFromSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database-from-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-relational-database-snapshot`.

- **AWS CLI**
- 
            
                    **To create a snapshot of a managed database**The following `create-relational-database-snapshot`example creates a snapshot of the specified managed database.`aws lightsail create-relational-database-snapshot \ --relational-database-name``Database1`\ --relational-database-snapshot-name`RelationalDatabaseSnapshot1`Output: `{ "operations": [ { "id": "853667fb-ea91-4c02-8d20-8fc5fd43b9eb", "resourceName": "RelationalDatabaseSnapshot1", "resourceType": "RelationalDatabaseSnapshot", "createdAt": 1569868074.645, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "Database1", "operationType": "CreateRelationalDatabaseSnapshot", "status": "Started", "statusChangedAt": 1569868074.645 }, { "id": "fbafa521-3cac-4be8-9773-1c143780b239", "resourceName": "Database1", "resourceType": "RelationalDatabase", "createdAt": 1569868074.645, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "RelationalDatabaseSnapshot1", "operationType": "CreateRelationalDatabaseSnapshot", "status": "Started", "statusChangedAt": 1569868074.645 } ] }`- 
                    For API details, see [CreateRelationalDatabaseSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-relational-database`.

- **AWS CLI**
- 
            
                    **To create a managed database**The following `create-relational-database`example creates a managed database in the specified AWS Region and Availability Zone, using the MySQL 5.6 database engine (mysql_5_6), and the $15 USD standard database bundle (micro_1_0). The managed database is pre-populated a master user name, and is not publicly accessible.`aws lightsail create-relational-database \ --relational-database-name``Database-1`\ --availability-zone`us-west-2a`\ --relational-database-blueprint-id`mysql_5_6`\ --relational-database-bundle-id`micro_1_0`\ --master-database-name`dbmaster`\ --master-`user`name user \ --no-publicly-accessibleOutput: `{ "operations": [ { "id": "b52bedee-73ed-4798-8d2a-9c12df89adcd", "resourceName": "Database-1", "resourceType": "RelationalDatabase", "createdAt": 1569450017.244, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "CreateRelationalDatabase", "status": "Started", "statusChangedAt": 1569450018.637 } ] }`- 
                    For API details, see [CreateRelationalDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-relational-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-auto-snapshot`.

- **AWS CLI**
- 
            
                    **To delete an automatic snapshot**The following `delete-auto-snapshot`example deletes the automatic snapshot`2019-10-10`of instance`WordPress-1`.`aws lightsail delete-auto-snapshot \ --resource-name``WordPress-1`\ --date`2019-10-10`Output: `{ "operations": [ { "id": "31c36e09-3d52-46d5-b6d8-7EXAMPLE534a", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1571088141.501, "location": { "availabilityZone": "us-west-2", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "DeleteAutoSnapshot-2019-10-10", "operationType": "DeleteAutoSnapshot", "status": "Succeeded" } ] }`For more information, see [Deleting automatic snapshots of instances or disks in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-deleting-automatic-snapshots)in the*Lightsail Dev Guide*.- 
                    For API details, see [DeleteAutoSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-auto-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-disk-snapshot`.

- **AWS CLI**
- 
            
                    **To delete a snapshot of a block storage disk**The following `delete-disk-snapshot`example deletes the specified snapshot of a block storage disk`aws lightsail delete-disk-snapshot \ --disk-snapshot-name``DiskSnapshot-1`Output: `{ "operations": [ { "id": "d1e5766d-b81e-4595-ad5d-02afbccfcd5d", "resourceName": "DiskSnapshot-1", "resourceType": "DiskSnapshot", "createdAt": 1569873552.79, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteDiskSnapshot", "status": "Succeeded", "statusChangedAt": 1569873552.79 } ] }`- 
                    For API details, see [DeleteDiskSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-disk-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-disk`.

- **AWS CLI**
- 
            
                    **To delete a block storage disk**The following `delete-disk`example deletes the specified block storage disk.`aws lightsail delete-disk \ --disk-name``Disk-1`Output: `{ "operations": [ { "id": "6378c70f-4d75-4f7a-ab66-730fca0bb2fc", "resourceName": "Disk-1", "resourceType": "Disk", "createdAt": 1569872887.864, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteDisk", "status": "Succeeded", "statusChangedAt": 1569872887.864 } ] }`- 
                    For API details, see [DeleteDisk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-disk.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain-entry`.

- **AWS CLI**
- 
            
                    **To delete a domain entry (DNS record)**The following `delete-domain-entry`example deletes the specified domain entry from an existing domain.**Note:**Lightsail's domain-related API operations are available in only the`us-east-1`Region. If your CLI profile is configured to use a different Region, you must include the`--region us-east-1`parameter or the command fails.`aws lightsail delete-domain-entry \ --region``us-east-1`\ --domain-name`example.com`\ --domain-entry`name=123.example.com,target=192.0.2.0,type=A`Output: `{ "operation": { "id": "06eacd01-d785-420e-8daa-823150c7dca1", "resourceName": "example.com ", "resourceType": "Domain", "createdAt": 1569874157.005, "location": { "availabilityZone": "all", "regionName": "global" }, "isTerminal": true, "operationType": "DeleteDomainEntry", "status": "Succeeded", "statusChangedAt": 1569874157.005 } }`- 
                    For API details, see [DeleteDomainEntry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-domain-entry.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain`.

- **AWS CLI**
- 
            
                    **To delete a domain (DNS zone)**The following `delete-domain`example deletes the specified domain and all of the entries in the domain (DNS records).**Note:**Lightsail's domain-related API operations are available in only the`us-east-1`Region. If your CLI profile is configured to use a different Region, you must include the`--region us-east-1`parameter or the command fails.`aws lightsail delete-domain \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "operation": { "id": "fcef5265-5af1-4a46-a3d7-90b5e18b9b32", "resourceName": "example.com", "resourceType": "Domain", "createdAt": 1569873788.13, "location": { "availabilityZone": "all", "regionName": "global" }, "isTerminal": true, "operationType": "DeleteDomain", "status": "Succeeded", "statusChangedAt": 1569873788.13 } }`- 
                    For API details, see [DeleteDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-instance-snapshot`.

- **AWS CLI**
- 
            
                    **title**The following `delete-instance-snapshot`example deletes the specified snapshot of an instance.`aws lightsail delete-instance-snapshot \ --instance-snapshot-name``WordPress-1-Snapshot-1`Output: `{ "operations": [ { "id": "14dad182-976a-46c6-bfd4-9480482bf0ea", "resourceName": "WordPress-1-Snapshot-1", "resourceType": "InstanceSnapshot", "createdAt": 1569874524.562, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteInstanceSnapshot", "status": "Succeeded", "statusChangedAt": 1569874524.562 } ] }`- 
                    For API details, see [DeleteInstanceSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-instance-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-instance`.

- **AWS CLI**
- 
            
                    **To delete an instance**The following `delete-instance`example deletes the specified instance.`aws lightsail delete-instance \ --instance-name``WordPress-1`Output: `{ "operations": [ { "id": "d77345a3-8f80-4d2e-b47d-aaa622718df2", "resourceName": "Disk-1", "resourceType": "Disk", "createdAt": 1569874357.469, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "WordPress-1", "operationType": "DetachDisk", "status": "Started", "statusChangedAt": 1569874357.469 }, { "id": "708fa606-2bfd-4e48-a2c1-0b856585b5b1", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1569874357.465, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "Disk-1", "operationType": "DetachDisk", "status": "Started", "statusChangedAt": 1569874357.465 }, { "id": "3187e823-8acb-405d-b098-fad5ceb17bec", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1569874357.829, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteInstance", "status": "Succeeded", "statusChangedAt": 1569874357.829 } ] }`- 
                    For API details, see [DeleteInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-key-pair`.

- **AWS CLI**
- 
            
                    **To delete a key pair**The following `delete-key-pair`example deletes the specified key pair.`aws lightsail delete-key-pair \ --key-pair-name``MyPersonalKeyPair`Output: `{ "operation": { "id": "81621463-df38-4810-b866-6e801a15abbf", "resourceName": "MyPersonalKeyPair", "resourceType": "KeyPair", "createdAt": 1569874626.466, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteKeyPair", "status": "Succeeded", "statusChangedAt": 1569874626.685 } }`- 
                    For API details, see [DeleteKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-known-host-keys`.

- **AWS CLI**
- 
            
                    **To delete known host keys from an instance**The following `delete-known-host-keys`example deletes the known host key from the specified instance.`aws lightsail delete-known-host-keys \ --instance-name``Instance-1`Output: `{ "operations": [ { "id": "c61afe9c-45a4-41e6-a97e-d212364da3f5", "resourceName": "Instance-1", "resourceType": "Instance", "createdAt": 1569874760.201, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteKnownHostKeys", "status": "Succeeded", "statusChangedAt": 1569874760.201 } ] }`For more information, see [Troubleshooting connection issues with the Amazon Lightsail browser-based SSH or RDP client](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-troubleshooting-browser-based-ssh-rdp-client-connection)in the*Lightsail Dev Guide*.- 
                    For API details, see [DeleteKnownHostKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-known-host-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-load-balancer-tls-certificate`.

- **AWS CLI**
- 
            
                    **To delete a TLS certificate for a load balancer**The following `delete-load-balancer-tls-certificate`example deletes the specifie TLS certificate from the specified load balancer.`aws lightsail delete-load-balancer-tls-certificate \ --load-balancer-name``MyFirstLoadBalancer`\ --certificate-name`MyFirstCertificate`Output: `{ "operations": [ { "id": "50bec274-e45e-4caa-8a69-b763ef636583", "resourceName": "MyFirstCertificate", "resourceType": "LoadBalancerTlsCertificate", "createdAt": 1569874989.48, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "DeleteLoadBalancerTlsCertificate", "status": "Started", "statusChangedAt": 1569874989.48 }, { "id": "78c58cdc-a59a-4b27-8213-500638634a8f", "resourceName": "MyFirstLoadBalancer", "resourceType": "LoadBalancer", "createdAt": 1569874989.48, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "DeleteLoadBalancerTlsCertificate", "status": "Started", "statusChangedAt": 1569874989.48 } ] }`- 
                    For API details, see [DeleteLoadBalancerTlsCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-load-balancer-tls-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-load-balancer`.

- **AWS CLI**
- 
            
                    **To delete a load balancer**The following `delete-load-balancer`example deletes the specified load balancer and any associated TLS certificates.`aws lightsail delete-load-balancer \ --load-balancer-name``MyFirstLoadBalancer`Output: `{ "operations": [ { "id": "a8c968c7-72a3-4680-a714-af8f03eea535", "resourceName": "MyFirstLoadBalancer", "resourceType": "LoadBalancer", "createdAt": 1569875092.125, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteLoadBalancer", "status": "Succeeded", "statusChangedAt": 1569875092.125 }, { "id": "f91a29fc-8ce3-4e69-a227-ea70ca890bf5", "resourceName": "MySecondCertificate", "resourceType": "LoadBalancerTlsCertificate", "createdAt": 1569875091.938, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "DeleteLoadBalancerTlsCertificate", "status": "Started", "statusChangedAt": 1569875091.938 }, { "id": "cf64c060-154b-4eb4-ba57-84e2e41563d6", "resourceName": "MyFirstLoadBalancer", "resourceType": "LoadBalancer", "createdAt": 1569875091.94, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "DeleteLoadBalancerTlsCertificate", "status": "Started", "statusChangedAt": 1569875091.94 } ] }`For more information, see title in the *guide*.- 
                    For API details, see [DeleteLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-relational-database-snapshot`.

- **AWS CLI**
- 
            
                    **To delete a snapshot of a managed database**The following `delete-relational-database-snapshot`example deletes the specified snapshot of a managed database.`aws lightsail delete-relational-database-snapshot \ --relational-database-snapshot-name``Database-Oregon-1-1566839359`Output: `{ "operations": [ { "id": "b99acae8-735b-4823-922f-30af580e3729", "resourceName": "Database-Oregon-1-1566839359", "resourceType": "RelationalDatabaseSnapshot", "createdAt": 1569875293.58, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "DeleteRelationalDatabaseSnapshot", "status": "Succeeded", "statusChangedAt": 1569875293.58 } ] }`- 
                    For API details, see [DeleteRelationalDatabaseSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-relational-database`.

- **AWS CLI**
- 
            
                    **To delete a managed database**The following `delete-relational-database`example deletes the specified managed database.`aws lightsail delete-relational-database \ --relational-database-name``Database-1`Output: `{ "operations": [ { "id": "3b0c41c1-053d-46f0-92a3-14f76141dc86", "resourceName": "Database-1", "resourceType": "RelationalDatabase", "createdAt": 1569875210.999, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "DeleteRelationalDatabase", "status": "Started", "statusChangedAt": 1569875210.999 }, { "id": "01ddeae8-a87a-4a4b-a1f3-092c71bf9180", "resourceName": "Database-1", "resourceType": "RelationalDatabase", "createdAt": 1569875211.029, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "Database-1-FinalSnapshot-1569875210793", "operationType": "CreateRelationalDatabaseSnapshot", "status": "Started", "statusChangedAt": 1569875211.029 }, { "id": "74d73681-30e8-4532-974e-1f23cd3f9f73", "resourceName": "Database-1-FinalSnapshot-1569875210793", "resourceType": "RelationalDatabaseSnapshot", "createdAt": 1569875211.029, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "Database-1", "operationType": "CreateRelationalDatabaseSnapshot", "status": "Started", "statusChangedAt": 1569875211.029 } ] }`- 
                    For API details, see [DeleteRelationalDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-relational-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detach-static-ip`.

- **AWS CLI**
- 
            
                    **To detach a static IP from an instance**The following `detach-static-ip`example detaches static IP`StaticIp-1`from any attached instance.`aws lightsail detach-static-ip \ --static-ip-name``StaticIp-1`Output: `{ "operations": [ { "id": "2a43d8a3-9f2d-4fe7-bdd0-eEXAMPLE3cf3", "resourceName": "StaticIp-1", "resourceType": "StaticIp", "createdAt": 1571088261.999, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "MEAN-1", "operationType": "DetachStaticIp", "status": "Succeeded", "statusChangedAt": 1571088261.999 }, { "id": "41a7d40c-74e8-4d2e-a837-cEXAMPLEf747", "resourceName": "MEAN-1", "resourceType": "Instance", "createdAt": 1571088262.022, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "StaticIp-1", "operationType": "DetachStaticIp", "status": "Succeeded", "statusChangedAt": 1571088262.022 } ] }`- 
                    For API details, see [DetachStaticIp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/detach-static-ip.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-active-names`.

- **AWS CLI**
- 
            
                    **To get active resource names**The following `get-active-names`example returns the active resource names in the configured AWS Region.`aws lightsail get-active-names`Output: `{ "activeNames": [ "WordPress-1", "StaticIp-1", "MEAN-1", "Plesk_Hosting_Stack_on_Ubuntu-1" ] }`- 
                    For API details, see [GetActiveNames](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-active-names.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-auto-snapshots`.

- **AWS CLI**
- 
            
                    **To get the available automatic snapshots for an instance**The following `get-auto-snapshots`example returns the available automatic snapshots for instance`WordPress-1`.`aws lightsail get-auto-snapshots \ --resource-name``WordPress-1`Output: `{ "resourceName": "WordPress-1", "resourceType": "Instance", "autoSnapshots": [ { "date": "2019-10-14", "createdAt": 1571033872.0, "status": "Success", "fromAttachedDisks": [] }, { "date": "2019-10-13", "createdAt": 1570947473.0, "status": "Success", "fromAttachedDisks": [] }, { "date": "2019-10-12", "createdAt": 1570861072.0, "status": "Success", "fromAttachedDisks": [] }, { "date": "2019-10-11", "createdAt": 1570774672.0, "status": "Success", "fromAttachedDisks": [] } ] }`For more information, see [Keeping automatic snapshots of instances or disks in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-keeping-automatic-snapshots)in the*Lightsail Dev Guide*.- 
                    For API details, see [GetAutoSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-auto-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-blueprints`.

- **AWS CLI**
- 
            
                    **To get the blueprints for new instances**The following `get-blueprints`example displays details about all of the available blueprints that can be used to create new instances in Amazon Lightsail.`aws lightsail get-blueprints`Output: `{ "blueprints": [ { "blueprintId": "wordpress", "name": "WordPress", "group": "wordpress", "type": "app", "description": "Bitnami, the leaders in application packaging, and Automattic, the experts behind WordPress, have teamed up to offer this official WordPress image. This image is a pre-configured, ready-to-run image for running WordPress on Amazon Lightsail. WordPress is the world's most popular content management platform. Whether it's for an enterprise or small business website, or a personal or corporate blog, content authors can easily create content using its new Gutenberg editor, and developers can extend the base platform with additional features. Popular plugins like Jetpack, Akismet, All in One SEO Pack, WP Mail, Google Analytics for WordPress, and Amazon Polly are all pre-installed in this image. Let's Encrypt SSL certificates are supported through an auto-configuration script.", "isActive": true, "minPower": 0, "version": "6.5.3-0", "versionCode": "1", "productUrl": "https://aws.amazon.com/marketplace/pp/B00NN8Y43U", "licenseUrl": "https://aws.amazon.com/marketplace/pp/B00NN8Y43U#pdp-usage", "platform": "LINUX_UNIX" }, { "blueprintId": "lamp_8_bitnami", "name": "LAMP (PHP 8)", "group": "lamp_8", "type": "app", "description": "LAMP with PHP 8.X packaged by Bitnami enables you to quickly start building your websites and applications by providing a coding framework. As a developer, it provides standalone project directories to store your applications. This blueprint is configured for production environments. It includes SSL auto-configuration with Let's Encrypt certificates, and the latest releases of PHP, Apache, and MariaDB on Linux. This application also includes phpMyAdmin, PHP main modules and Composer.", "isActive": true, "minPower": 0, "version": "8.2.18-4", "versionCode": "1", "productUrl": "https://aws.amazon.com/marketplace/pp/prodview-6g3gzfcih6dvu", "licenseUrl": "https://aws.amazon.com/marketplace/pp/prodview-6g3gzfcih6dvu#pdp-usage", "platform": "LINUX_UNIX" }, { "blueprintId": "nodejs", "name": "Node.js", "group": "node", "type": "app", "description": "Node.js packaged by Bitnami is a pre-configured, ready to run image for Node.js on Amazon EC2. It includes the latest version of Node.js, Apache, Python and Redis. The image supports multiple Node.js applications, each with its own virtual host and project directory. It is configured for production use and is secure by default, as all ports except HTTP, HTTPS and SSH ports are closed. Let's Encrypt SSL certificates are supported through an auto-configuration script. Developers benefit from instant access to a secure, update and consistent Node.js environment without having to manually install and configure multiple components and libraries.", "isActive": true, "minPower": 0, "version": "18.20.2-0", "versionCode": "1", "productUrl": "https://aws.amazon.com/marketplace/pp/B00NNZUAKO", "licenseUrl": "https://aws.amazon.com/marketplace/pp/B00NNZUAKO#pdp-usage", "platform": "LINUX_UNIX" }, ... } ] }`- 
                    For API details, see [GetBlueprints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-blueprints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-bundles`.

- **AWS CLI**
- 
            
                    **To get the bundles for new instances**The following `get-bundles`example displays details about all of the available bundles that can be used to create new instances in Amazon Lightsail.`aws lightsail get-bundles`Output: `{ "bundles": [ { "price": 5.0, "cpuCount": 2, "diskSizeInGb": 20, "bundleId": "nano_3_0", "instanceType": "nano", "isActive": true, "name": "Nano", "power": 298, "ramSizeInGb": 0.5, "transferPerMonthInGb": 1024, "supportedPlatforms": [ "LINUX_UNIX" ] }, { "price": 7.0, "cpuCount": 2, "diskSizeInGb": 40, "bundleId": "micro_3_0", "instanceType": "micro", "isActive": true, "name": "Micro", "power": 500, "ramSizeInGb": 1.0, "transferPerMonthInGb": 2048, "supportedPlatforms": [ "LINUX_UNIX" ] }, { "price": 12.0, "cpuCount": 2, "diskSizeInGb": 60, "bundleId": "small_3_0", "instanceType": "small", "isActive": true, "name": "Small", "power": 1000, "ramSizeInGb": 2.0, "transferPerMonthInGb": 3072, "supportedPlatforms": [ "LINUX_UNIX" ] }, ... } ] }`- 
                    For API details, see [GetBundles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-bundles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-cloud-formation-stack-records`.

- **AWS CLI**
- 
            
                    **To get the CloudFormation stack records and their associated stacks**The following `get-cloud-formation-stack-records`example displays details about the CloudFormation stack records and their associated stacks used to create Amazon EC2 resources from exported Amazon Lightsail snapshots.`aws lightsail get-cloud-formation-stack-records`Output: `{ "cloudFormationStackRecords": [ { "name": "CloudFormationStackRecord-588a4243-e2d1-490d-8200-3a7513ecebdf", "arn": "arn:aws:lightsail:us-west-2:111122223333:CloudFormationStackRecord/28d646ab-27bc-48d9-a422-1EXAMPLE6d37", "createdAt": 1565301666.586, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "CloudFormationStackRecord", "state": "Succeeded", "sourceInfo": [ { "resourceType": "ExportSnapshotRecord", "name": "ExportSnapshotRecord-e02f23d7-0453-4aa9-9c95-91aa01a141dd", "arn": "arn:aws:lightsail:us-west-2:111122223333:ExportSnapshotRecord/f12b8792-f3ea-4d6f-b547-2EXAMPLE8796" } ], "destinationInfo": { "id": "arn:aws:cloudformation:us-west-2:111122223333:stack/Lightsail-Stack-588a4243-e2d1-490d-8200-3EXAMPLEebdf/063203b0-ba28-11e9-838b-0EXAMPLE8b00", "service": "Aws::CloudFormation::Stack" } } ] }`- 
                    For API details, see [GetCloudFormationStackRecords](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-cloud-formation-stack-records.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-disk-snapshot`.

- **AWS CLI**
- 
            
                    **To get information about a disk snapshot**The following `get-disk-snapshot`example displays details about the disk snapshot`Disk-1-1566839161`.`aws lightsail get-disk-snapshot \ --disk-snapshot-name``Disk-1-1566839161`Output: `{ "diskSnapshot": { "name": "Disk-1-1566839161", "arn": "arn:aws:lightsail:us-west-2:111122223333:DiskSnapshot/e2d0fa53-8ee0-41a0-8e56-0EXAMPLE1051", "supportCode": "6EXAMPLE3362/snap-0EXAMPLE06100d09", "createdAt": 1566839163.749, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "DiskSnapshot", "tags": [], "sizeInGb": 8, "state": "completed", "progress": "100%", "fromDiskName": "Disk-1", "fromDiskArn": "arn:aws:lightsail:us-west-2:111122223333:Disk/c21cfb0a-07f2-44ae-9a23-bEXAMPLE8096", "isFromAutoSnapshot": false } }`For more information, see title in the *guide*.- 
                    For API details, see [GetDiskSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-disk-snapshots`.

- **AWS CLI**
- 
            
                    **To get information about all disk snapshots**The following `get-disk-snapshots`example displays details about all of the disk snapshots in the configured AWS Region.`aws lightsail get-disk-snapshots`Output: `{ "diskSnapshots": [ { "name": "Disk-2-1571090588", "arn": "arn:aws:lightsail:us-west-2:111122223333:DiskSnapshot/32e889a9-38d4-4687-9f21-eEXAMPLE7839", "supportCode": "6EXAMPLE3362/snap-0EXAMPLE1ca192a4", "createdAt": 1571090591.226, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "DiskSnapshot", "tags": [], "sizeInGb": 8, "state": "completed", "progress": "100%", "fromDiskName": "Disk-2", "fromDiskArn": "arn:aws:lightsail:us-west-2:111122223333:Disk/6a343ff8-6341-422d-86e2-bEXAMPLE16c2", "isFromAutoSnapshot": false }, { "name": "Disk-1-1566839161", "arn": "arn:aws:lightsail:us-west-2:111122223333:DiskSnapshot/e2d0fa53-8ee0-41a0-8e56-0EXAMPLE1051", "supportCode": "6EXAMPLE3362/snap-0EXAMPLEe06100d09", "createdAt": 1566839163.749, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "DiskSnapshot", "tags": [], "sizeInGb": 8, "state": "completed", "progress": "100%", "fromDiskName": "Disk-1", "fromDiskArn": "arn:aws:lightsail:us-west-2:111122223333:Disk/c21cfb0a-07f2-44ae-9a23-bEXAMPLE8096", "isFromAutoSnapshot": false } ] }`- 
                    For API details, see [GetDiskSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-disk`.

- **AWS CLI**
- 
            
                    **To get information about a block storage disk**The following `get-disk`example displays details about the disk`Disk-1`.`aws lightsail get-disk \ --disk-name``Disk-1`Output: `{ "disk": { "name": "Disk-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:Disk/c21cfb0a-07f2-44ae-9a23-bEXAMPLE8096", "supportCode": "6EXAMPLE3362/vol-0EXAMPLEf2f88b32f", "createdAt": 1566585439.587, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Disk", "tags": [], "sizeInGb": 8, "isSystemDisk": false, "iops": 100, "path": "/dev/xvdf", "state": "in-use", "attachedTo": "WordPress_Multisite-1", "isAttached": true, "attachmentState": "attached" } }`For more information, see title in the *guide*.- 
                    For API details, see [GetDisk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disk.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-disks`.

- **AWS CLI**
- 
            
                    **To get information about all block storage disks**The following `get-disks`example displays details about all of the disks in the configured AWS Region.`aws lightsail get-disks`Output: `{ "disks": [ { "name": "Disk-2", "arn": "arn:aws:lightsail:us-west-2:111122223333:Disk/6a343ff8-6341-422d-86e2-bEXAMPLE16c2", "supportCode": "6EXAMPLE3362/vol-0EXAMPLE929602087", "createdAt": 1571090461.634, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Disk", "tags": [], "sizeInGb": 8, "isSystemDisk": false, "iops": 100, "state": "available", "isAttached": false, "attachmentState": "detached" }, { "name": "Disk-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:Disk/c21cfb0a-07f2-44ae-9a23-bEXAMPLE8096", "supportCode": "6EXAMPLE3362/vol-0EXAMPLEf2f88b32f", "createdAt": 1566585439.587, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Disk", "tags": [], "sizeInGb": 8, "isSystemDisk": false, "iops": 100, "path": "/dev/xvdf", "state": "in-use", "attachedTo": "WordPress_Multisite-1", "isAttached": true, "attachmentState": "attached" } ] }`- 
                    For API details, see [GetDisks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-disks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain`.

- **AWS CLI**
- 
            
                    **To get information about a domain**The following `get-domain`example displays details about the domain`example.com`.**Note:**Lightsail's domain-related API operations are available in only the`us-east-1`AWS Region. If your CLI profile is configured to use a different Region, you must include the`` --region us-east-1`` parameter or the command fails.`aws lightsail get-domain \ --domain-name``example.com`\ --region`us-east-1`Output: `{ "domain": { "name": "example.com", "arn": "arn:aws:lightsail:global:111122223333:Domain/28cda903-3f15-44b2-9baf-3EXAMPLEb304", "supportCode": "6EXAMPLE3362//hostedzone/ZEXAMPLEONGSC1", "createdAt": 1570728588.6, "location": { "availabilityZone": "all", "regionName": "global" }, "resourceType": "Domain", "tags": [], "domainEntries": [ { "id": "-1682899164", "name": "example.com", "target": "192.0.2.0", "isAlias": false, "type": "A" }, { "id": "1703104243", "name": "example.com", "target": "ns-137.awsdns-17.com", "isAlias": false, "type": "NS" }, { "id": "-1038331153", "name": "example.com", "target": "ns-1710.awsdns-21.co.uk", "isAlias": false, "type": "NS" }, { "id": "-2107289565", "name": "example.com", "target": "ns-692.awsdns-22.net", "isAlias": false, "type": "NS" }, { "id": "1582095705", "name": "example.com", "target": "ns-1436.awsdns-51.org", "isAlias": false, "type": "NS" }, { "id": "-1769796132", "name": "example.com", "target": "ns-1710.awsdns-21.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400", "isAlias": false, "type": "SOA" } ] } }`- 
                    For API details, see [GetDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domains`.

- **AWS CLI**
- 
            
                    **To get information about all domains**The following `get-domains`example displays details about all of the domains in the configured AWS Region.**Note:**Lightsail's domain-related API operations are available in only the`us-east-1`AWS Region. If your CLI profile is configured to use a different Region, you must include the`--region us-east-1`parameter or the command fails.`aws lightsail get-domains \ --region``us-east-1`Output: `{ "domains": [ { "name": "example.com", "arn": "arn:aws:lightsail:global:111122223333:Domain/28cda903-3f15-44b2-9baf-3EXAMPLEb304", "supportCode": "6EXAMPLE3362//hostedzone/ZEXAMPLEONGSC1", "createdAt": 1570728588.6, "location": { "availabilityZone": "all", "regionName": "global" }, "resourceType": "Domain", "tags": [], "domainEntries": [ { "id": "-1682899164", "name": "example.com", "target": "192.0.2.0", "isAlias": false, "type": "A" }, { "id": "1703104243", "name": "example.com", "target": "ns-137.awsdns-17.com", "isAlias": false, "type": "NS" }, { "id": "-1038331153", "name": "example.com", "target": "ns-4567.awsdns-21.co.uk", "isAlias": false, "type": "NS" }, { "id": "-2107289565", "name": "example.com", "target": "ns-333.awsdns-22.net", "isAlias": false, "type": "NS" }, { "id": "1582095705", "name": "example.com", "target": "ns-1111.awsdns-51.org", "isAlias": false, "type": "NS" }, { "id": "-1769796132", "name": "example.com", "target": "ns-1234.awsdns-21.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400", "isAlias": false, "type": "SOA" }, { "id": "1029454894", "name": "_dead6a124ede046a0319eb44a4eb3cbc.example.com", "target": "_be133b0a0899fb7b6bf79d9741d1a383.hkvuiqjoua.acm-validations.aws", "isAlias": false, "type": "CNAME" } ] }, { "name": "example.net", "arn": "arn:aws:lightsail:global:111122223333:Domain/9c9f0d70-c92e-4753-86c2-6EXAMPLE029d", "supportCode": "6EXAMPLE3362//hostedzone/ZEXAMPLE5TPKMV", "createdAt": 1556661071.384, "location": { "availabilityZone": "all", "regionName": "global" }, "resourceType": "Domain", "tags": [], "domainEntries": [ { "id": "-766320943", "name": "example.net", "target": "192.0.2.2", "isAlias": false, "type": "A" }, { "id": "-453913825", "name": "example.net", "target": "ns-123.awsdns-10.net", "isAlias": false, "type": "NS" }, { "id": "1553601564", "name": "example.net", "target": "ns-4444.awsdns-47.co.uk", "isAlias": false, "type": "NS" }, { "id": "1653797661", "name": "example.net", "target": "ns-7890.awsdns-61.org", "isAlias": false, "type": "NS" }, { "id": "706414698", "name": "example.net", "target": "ns-123.awsdns-44.com", "isAlias": false, "type": "NS" }, { "id": "337271745", "name": "example.net", "target": "ns-4444.awsdns-47.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400", "isAlias": false, "type": "SOA" }, { "id": "-1785431096", "name": "www.example.net", "target": "192.0.2.2", "isAlias": false, "type": "A" } ] }, { "name": "example.org", "arn": "arn:aws:lightsail:global:111122223333:Domain/f0f13ba3-3df0-4fdc-8ebb-1EXAMPLEf26e", "supportCode": "6EXAMPLE3362//hostedzone/ZEXAMPLEAFO38", "createdAt": 1556661199.106, "location": { "availabilityZone": "all", "regionName": "global" }, "resourceType": "Domain", "tags": [], "domainEntries": [ { "id": "2065301345", "name": "example.org", "target": "192.0.2.4", "isAlias": false, "type": "A" }, { "id": "-447198516", "name": "example.org", "target": "ns-123.awsdns-45.com", "isAlias": false, "type": "NS" }, { "id": "136463022", "name": "example.org", "target": "ns-9999.awsdns-15.co.uk", "isAlias": false, "type": "NS" }, { "id": "1395941679", "name": "example.org", "target": "ns-555.awsdns-01.net", "isAlias": false, "type": "NS" }, { "id": "872052569", "name": "example.org", "target": "ns-6543.awsdns-38.org", "isAlias": false, "type": "NS" }, { "id": "1001949377", "name": "example.org", "target": "ns-1234.awsdns-15.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400", "isAlias": false, "type": "SOA" }, { "id": "1046191192", "name": "www.example.org", "target": "192.0.2.4", "isAlias": false, "type": "A" } ] } ] }`- 
                    For API details, see [GetDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-export-snapshot-record`.

- **AWS CLI**
- 
            
                    **To get the records of snapshots exported to Amazon EC2**The following `get-export-snapshot-record`example displays details about Amazon Lightsail instance or disk snapshots exported to Amazon EC2.`aws lightsail get-export-snapshot-records`Output: `{ "exportSnapshotRecords": [ { "name": "ExportSnapshotRecord-d2da10ce-0b3c-4ae1-ab3a-2EXAMPLEa586", "arn": "arn:aws:lightsail:us-west-2:111122223333:ExportSnapshotRecord/076c7060-b0cc-4162-98f0-2EXAMPLEe28e", "createdAt": 1543534665.678, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "ExportSnapshotRecord", "state": "Succeeded", "sourceInfo": { "resourceType": "InstanceSnapshot", "createdAt": 1540339310.706, "name": "WordPress-512MB-Oregon-1-1540339219", "arn": "arn:aws:lightsail:us-west-2:111122223333:InstanceSnapshot/5446f534-ed60-4c17-b4a5-bEXAMPLEf8b7", "fromResourceName": "WordPress-512MB-Oregon-1", "fromResourceArn": "arn:aws:lightsail:us-west-2:111122223333:Instance/4b8f1f24-e4d1-4cf3-88ff-cEXAMPLEa397", "instanceSnapshotInfo": { "fromBundleId": "nano_2_0", "fromBlueprintId": "wordpress_4_9_8", "fromDiskInfo": [ { "path": "/dev/sda1", "sizeInGb": 20, "isSystemDisk": true } ] } }, "destinationInfo": { "id": "ami-0EXAMPLEc0d65058e", "service": "Aws::EC2::Image" } }, { "name": "ExportSnapshotRecord-1c94e884-40ff-4fe1-9302-0EXAMPLE14c2", "arn": "arn:aws:lightsail:us-west-2:111122223333:ExportSnapshotRecord/fb392ce8-6567-4013-9bfd-3EXAMPLE5b4c", "createdAt": 1543432110.2, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "ExportSnapshotRecord", "state": "Succeeded", "sourceInfo": { "resourceType": "InstanceSnapshot", "createdAt": 1540833603.545, "name": "LAMP_PHP_5-512MB-Oregon-1-1540833565", "arn": "arn:aws:lightsail:us-west-2:111122223333:InstanceSnapshot/82334399-b5f2-49ec-8382-0EXAMPLEe45f", "fromResourceName": "LAMP_PHP_5-512MB-Oregon-1", "fromResourceArn": "arn:aws:lightsail:us-west-2:111122223333:Instance/863b9f35-ab1e-4418-bdd2-1EXAMPLEbab2", "instanceSnapshotInfo": { "fromBundleId": "nano_2_0", "fromBlueprintId": "lamp_5_6_37_2", "fromDiskInfo": [ { "path": "/dev/sda1", "sizeInGb": 20, "isSystemDisk": true } ] } }, "destinationInfo": { "id": "ami-0EXAMPLE7c5ec84e2", "service": "Aws::EC2::Image" } } ] }`- 
                    For API details, see [GetExportSnapshotRecord](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-export-snapshot-record.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-access-details`.

- **AWS CLI**
- 
            
                    **To get host key information for an instance**The following `get-instance-access-details`example displays host key information for instance`WordPress_Multisite-1`.`aws lightsail get-instance-access-details \ --instance-name``WordPress_Multisite-1`Output: `{ "accessDetails": { "certKey": "ssh-rsa-cert-v01@openssh.com AEXAMPLEaC1yc2EtY2VydC12MDFAb3BlbnNzaC5jb20AAAAgNf076Dt3ppmPd0fPxZVMmS491aEAYYH9cHqAJ3fNML8AAAADAQABAAABAQD4APep5Ta2gHLk7m/vEXAMPLE2eBWJyQvn7ol/i0+s966h5sx8qUD79lPB7q5UESd5VZGFtytrykfQJnjiwqe7EV5agzvjblLj26Fb37EKda9HVfCOu8pWbvky7Tyn9w299a6CsG5o8HrkOymDE2c59lYxXGkilKo5I9aZLBAdXn3t3oKtq9zsjYGjyEmarPYoVDT1ft8HaUGu4aCv1peI0+ZEXAMPLEAWaucW9Huh0WYN5yrmL252c4v13JTVmytaEZvLvt5itVoWXQY0ZDyrLUcZSKxyq5n00Mgvj2fiZdt+xMfQM9xVz0rXZmqx8uJidJpRgLCMTviofwQJU/K1EXAMPLEAAAAAAAABAAAALS00MzMzMDU4MzA4ODg1MTY2NjM4Onp6UWlndHk4UElRSG9STitOTG5QSEE9PQAAAAsAAAAHYml0bmFtaQAAAABdpPL7AAEXAMPLEgcAAAAAAAAAggAAABVwZXJtaXQtWDExLWZvcndhcmRpbmcAAAAAAAAAF3Blcm1pdC1hZ2VudC1mb3J3YXJkaW5nAAAAAAAAABZwZXJtaXQtEXAMPLEmb3J3YXJkaW5nAAAAAAAAAApwZXJtaXQtcHR5AAAAAAAAAA5wZXJtaXQtdXNlci1yYwAAAAAAAAAAAAACFwAAAAdzc2gtcnNhAAAAAwEAAQEXAMPLECqCbiK9b450HtRD1ZpiksT6oxc8U7nLNkVFC1j7JqZvP9ee3ux+LiB+ozNbUA0cdNL9Y67x7qPv/R7XhTc21+2A+8+GuVpK/Kz9dqDMKNAEXAMPLE+YYN+tiXm7Y8OgziK+7iDB7xUuQ4vghmn4+qgz9mKwYgWvVe2+0XLuV7cnWPB7iUlHQg+E3LUKrV4ZFw9pj7X2dFdNKfMxwWgI1ISWKimEXAMPLEeHjrf1Rqc/QH6TpWCvPfcx8uvwVqdwTfkE/SfA5BCzbGGI1UmIUadh8nHcb5FamQ1hK7kECy47K/x9FMn/KwmM7pCwJbSLDMO7n9bnbvck6m8ZoB2N2YLMG5dW7BerEXAMPLEobqfdtyYJHHel1EyyEJs1fWNU3D5JIGlgzcPAV+ZlbQyUCZXf0oslSa+HE85fO/FRq9SVSBSHrmbeb0frlPhgMzgSmqLeyhlbr6wwWIDbREXAMPLEJZ49H7RdQxdKyYrZPWvRgcr0qI2EL0tAajnpQQ8UZqeO9/Aqter0xN5PhFL0J49OWTacwCGRAjLhibAx7K1t/1ZXWo6c+ijq8clll327EXAMPLE/e89GC89KcmKCxfGQniDAUgF8UqofIbq3ZOUgiAAYCVXclI4L68NhVXyoWuQXPBRQSEXAMPLEWm74tDL9tFN3c7tSe/Oz0cTR+4sAAAIPAAAAB3NzaC1yc2EAAAIAQnG/L0DqiSnLrWhEox4aHqMgd0m0oLLAYx6OQH9F0TM9EXAMPLE961rzSCMon7ZgsWNnL0OwZQgDG+rtJ4N0B7HOVwns4ynUFbzNQ3qFGGeE3lKwX1L41vV1iSy7sDk8aI0LmrKJi1LE1Qc1l8uboRlwoXOYEXAMPLEaUCeX+10+WEXAMPLEg6Y4U4ZvE2B3xyRdpvysb5TGFNtk5qPslacnVkoLOGsZZXMpLGJnG4OBpQLLtpj9sNMxAgZPCAUjhkqkQWYJxJzvFN7sUMOArUwKPFJE2kaEXAMPLEOUrVGBbCTioRztlPsxY7hoXm73N929eZpNhxP3U+nxO9O4NUZ2pTWbVSUaV1gm6pug9xbwNO1Im21t34JeLlKTqxcJ6zzS8W0c0KKpAm5c4hWkseMbyutS2jav/4hiS+BhrYgptzfwe5qRXEXAMPLEHZQr3YfGzYoBJ/lLK3NHhxOihhsfAYwMei0BFZT1F/7CT3IH4iitEkIgodi06/Mw6UDqMPozyQCK1lEA6LFhYCOZG9drWcoRa74lM4kY9TP028Za8gDMh1WpkXLq9Gixon5OHP8aM/sEXAMPLEr2+fnkw+1BtoO5L6+VKoPlXaGqZ/fBYEXAMPLEAMQHjnLM1JYNvtEEPhp+TNzXHzuixWf/Ht04m0AVpXrzIDXaS1O2tXY=", "ipAddress": "192.0.2.0", "privateKey": "-----BEGIN RSA PRIVATE KEY-----\nEXAMPLEBAAKCAQEA+AD3qeU2toBy5O5v7wnRLVo/tngVickL5+6Jf4tPrPeuoebM\nfKlA+/ZTwe6uVBEneVWRhbcra8pH0CZ44sKnuxFeWoM7425S49uhW9+xCnWvR1Xw\njrvKVm75Mu08p/cNvfWugrBuaPB65DspgxNnOfZWMVxpIpSqOSPWmSwQHV597d6C\nrEXAMPLEo8hJmqz2KFQ09X7fB2lBruGgr9aXiNPmWmovYKqwFmrnFvR7odFmDecq\n5EXAMPLE9dyU1ZsrWhGby77eYrVaFl0GNGQ8qy1HGUiscquZ9NDIL49n4mXbfsTH\n0EXAMPLE12ZqsfLiYnSaUYCwjE74qH8ECVPytQIDAQABAoIBAHeZV9Z58JHAjifz\nCEXAMPLEEqC3doOVDgXSlkKI92qNo4z2VcUEho878paCuVVXVHcCGgSnGeyIh2tN\nMEXAMPLESohR427BhH3YLA+3Z5SIvnejbTgYPfLC37B8khTaYqkqMvdZiFVZK5qn\nIEXAMPLEM93oF9eSZCjcLKB/jGHsfb0eCDMP8BshHE2beuqzVMoK1DxOnvoP3+Fp\nAEXAMPLESq6pDpCo9YVUX8g1u3Ro9cPl2LXHDy+oVEY5KhbZQJ7VU1I72WOvppWW\nOEXAMPLEkgYlq7p6qYtYcSgTEjz14gDiMfQ7SyHB3alkIoNONQ9ZPaWHyJvymeud\noQTNuz0CgYEA/LFWNTEZrzdzdR1kJmyNRmAermU0B6utyNENChAlHGSHkB+1lVSh\nbEXAMPLEQo9ooUeW5UxO3YwacZLoDT1mwxw1Ptc1+PNycZoLe1fE9UdARrdmGTob\n8l7CPLSXp3xuR8VqSp2fnIc7hfiQs/NrPX9gm/EOrB0we0RKyDSzWScCgYEA+z/r\niob+nJZq0YbnOSuP6oMULP4vnWniWj8MIhUJU53LwSAM8DeJdONKDdkuiOd52aAL\nVgn7nLo88rVWKhJwVc4tu/rNgZLcR3bP4+kL6zand0KQnMLyOzNA2Ys26aa5udH1\nqWl0WTt9WEm/h10ndC1knOMectrvsG17b38y5sMCgYEA54NiRGGz8oCPW6GN/FZA\nKEXAMPLE5tw34GEH3Uxlc9n3CejDaQmczOATwX4nIwRZDEqWyYZcS0btg1jhGiBD\nYEXAMPLEkc8Z71L/agZEAaVCEog9FqfSqwB+XTfoKh8qur74X1yCu9p6gof1q6k9\neEXAMPLEchJcNNOg4ETIfMkCgYBdVORRhE4mqvWpOdzA7v66FdEz2YSkjAXKkmsW\naEXAMPLE8Z/8yBSmuBv1Qv03XA12my462uB92uzzGAuW+1yBc2Kn1sXqYTy0y1z0\ngEXAMPLEBogjw4MqHKL1bPKMHyQU8/q24PaYgzHPzy13wlH6pTYf1XqlHdE2D6Vv\nyEXAMPLEgQC3i/kVVhky/2XRwRVlC7JO2Bg3QGTx38hpmDa5IuofKANjA+Wa3/zy\nbEXAMPLE6ytQgD9GN/YtBq+uhO+2ZkvXPL+CWRi0ZRXpPwYDBBFU9Cw0AuWWGlL8\nwEXAMPLExMlcysRgcWB9RNgf3AuOpFd2i6XT/riNsvvkpmJ+VooU8g==\n-----END RSA PRIVATE KEY-----\n", "protocol": "ssh", "instanceName": "WordPress_Multisite-1", "username": "bitnami", "hostKeys": [ { "algorithm": "ssh-rsa", "publicKey": "AEXAMPLEaC1yc2EAAAADAQABAAABAQCoeR9ieZTjQ3pXCHczuAYZFjlF7t+uBkXuqeGMRex78pCvmS+DiEXAMPLEuJ1Q8dcKhrQL4HpXbD9dosVCTaJnJwb4MQqsuSVFdHFzy3guP+BKclWqtxJEXAMPLEsBGqZZlrIv6a9bTA0TCplZ8AD+hSRTaSXXqg6FT+Qf16IktH0XlMs7xIEXAMPLEmNtjCpzZiGXDHzytoMvUgwa8uHPp44Og36EUu4VqQxoUHPJKoXvcQizyk3K8ym0hP0TpDZhD8cqwRfd6EHp4Q1br/Ot6y9HwvykEXAMPLEAfbKjbR42+u6+OSlkr4d339q2U1sTDytJhhs8HUel1wTfGRfp", "witnessedAt": 1570744377.699, "fingerprintSHA1": "SHA1:GEXAMPLEMoYgUg0ucadqU9Bt3Lk", "fingerprintSHA256": "SHA256:IEXAMPLEcB5vgxnAUoJawbdZ+MwELhIp6FUxuwq/LIU" }, { "algorithm": "ssh-ed25519", "publicKey": "AEXAMPLEaC1lZDI1NTE5AAAAIC1gwGPDfGaONxEXAMPLEJX3UNap781QxHQmn8nzlrUv", "witnessedAt": 1570744377.697, "fingerprintSHA1": "SHA1:VEXAMPLE5ReqSmTgv03sSUw9toU", "fingerprintSHA256": "SHA256:0EXAMPLEdE6tI95k3TJpG+qhJbAoknB0yz9nAEaDt3A" }, { "algorithm": "ecdsa-sha2-nistp256", "publicKey": "AEXAMPLEZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABEXAMPLE9B4mZy8YSsZW7cixCDq5yHSAAxjJkDo54C+EnKlDCsYtUkxxEXAMPLE6VOWL2z63RTKa2AUPgd8irjxWI=", "witnessedAt": 1570744377.707, "fingerprintSHA1": "SHA1:UEXAMPLEOYCfXsCf2G6tDg+7YG0", "fingerprintSHA256": "SHA256:wEXAMPLEQ9a/iEXAMPLEhRufm6U9vFU4cpkMPHnBsNA" } ] } }`- 
                    For API details, see [GetInstanceAccessDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-access-details.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-metric-data`.

- **AWS CLI**
- 
            
                    **To get metric data for an instance**The following `get-instance-metric-data`example returns the average percent of`CPUUtilization`every`7200`seconds (2 hours) between`1571342400`and`1571428800`for instance`MEAN-1`.We recommend that you use a unix time converter to identify the start and end times. `aws lightsail get-instance-metric-data \ --instance-name``MEAN-1`\ --metric-name`CPUUtilization`\ --period`7200`\ --start-time`1571342400`\ --end-time`1571428800`\ --unit`Percent`\ --statistics`Average`Output: `{ "metricName": "CPUUtilization", "metricData": [ { "average": 0.26113718770120725, "timestamp": 1571342400.0, "unit": "Percent" }, { "average": 0.26861268928111953, "timestamp": 1571392800.0, "unit": "Percent" }, { "average": 0.28187475104748777, "timestamp": 1571378400.0, "unit": "Percent" }, { "average": 0.2651936960458352, "timestamp": 1571421600.0, "unit": "Percent" }, { "average": 0.2561856213712188, "timestamp": 1571371200.0, "unit": "Percent" }, { "average": 0.3021383254607764, "timestamp": 1571356800.0, "unit": "Percent" }, { "average": 0.2618381649223539, "timestamp": 1571407200.0, "unit": "Percent" }, { "average": 0.26331929394825787, "timestamp": 1571400000.0, "unit": "Percent" }, { "average": 0.2576348407007818, "timestamp": 1571385600.0, "unit": "Percent" }, { "average": 0.2513008454658378, "timestamp": 1571364000.0, "unit": "Percent" }, { "average": 0.26329974562758346, "timestamp": 1571414400.0, "unit": "Percent" }, { "average": 0.2667092536656445, "timestamp": 1571349600.0, "unit": "Percent" } ] }`- 
                    For API details, see [GetInstanceMetricData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-metric-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-port-states`.

- **AWS CLI**
- 
            
                    **To get firewall information for an instance**The following `get-instance-port-states`example returns the firewall ports configured for instance`MEAN-1`.`aws lightsail get-instance-port-states \ --instance-name``MEAN-1`Output: `{ "portStates": [ { "fromPort": 80, "toPort": 80, "protocol": "tcp", "state": "open" }, { "fromPort": 22, "toPort": 22, "protocol": "tcp", "state": "open" }, { "fromPort": 443, "toPort": 443, "protocol": "tcp", "state": "open" } ] }`- 
                    For API details, see [GetInstancePortStates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-port-states.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-snapshot`.

- **AWS CLI**
- 
            
                    **To get information about a specified instance snapshot**The following `get-instance-snapshot`example displays details about the specified instance snapshot.`aws lightsail get-instance-snapshot \ --instance-snapshot-name``MEAN-1-1571419854`Output: `{ "instanceSnapshot": { "name": "MEAN-1-1571419854", "arn": "arn:aws:lightsail:us-west-2:111122223333:InstanceSnapshot/ac54700c-48a8-40fd-b065-2EXAMPLEac8f", "supportCode": "6EXAMPLE3362/ami-0EXAMPLE67a73020d", "createdAt": 1571419891.927, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "InstanceSnapshot", "tags": [], "state": "available", "fromAttachedDisks": [], "fromInstanceName": "MEAN-1", "fromInstanceArn": "arn:aws:lightsail:us-west-2:111122223333:Instance/bd470fc5-a68b-44c5-8dbc-8EXAMPLEbada", "fromBlueprintId": "mean", "fromBundleId": "medium_3_0", "isFromAutoSnapshot": false, "sizeInGb": 80 } }`- 
                    For API details, see [GetInstanceSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-snapshots`.

- **AWS CLI**
- 
            
                    **To get information about all of your instance snapshots**The following `get-instance-snapshots`example displays details about all of the instance snapshots in the configured AWS Region.`aws lightsail get-instance-snapshots`Output: `{ "instanceSnapshots": [ { "name": "MEAN-1-1571421498", "arn": "arn:aws:lightsail:us-west-2:111122223333:InstanceSnapshot/a20e6ebe-b0ee-4ae4-a750-3EXAMPLEcb0c", "supportCode": "6EXAMPLE3362/ami-0EXAMPLEe33cabfa1", "createdAt": 1571421527.755, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "InstanceSnapshot", "tags": [ { "key": "no_delete" } ], "state": "available", "fromAttachedDisks": [], "fromInstanceName": "MEAN-1", "fromInstanceArn": "arn:aws:lightsail:us-west-2:111122223333:Instance/1761aa0a-6038-4f25-8b94-2EXAMPLE19fd", "fromBlueprintId": "wordpress", "fromBundleId": "micro_3_0", "isFromAutoSnapshot": false, "sizeInGb": 40 }, { "name": "MEAN-1-1571419854", "arn": "arn:aws:lightsail:us-west-2:111122223333:InstanceSnapshot/ac54700c-48a8-40fd-b065-2EXAMPLEac8f", "supportCode": "6EXAMPLE3362/ami-0EXAMPLE67a73020d", "createdAt": 1571419891.927, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "InstanceSnapshot", "tags": [], "state": "available", "fromAttachedDisks": [], "fromInstanceName": "MEAN-1", "fromInstanceArn": "arn:aws:lightsail:us-west-2:111122223333:Instance/bd470fc5-a68b-44c5-8dbc-8EXAMPLEbada", "fromBlueprintId": "mean", "fromBundleId": "medium_3_0", "isFromAutoSnapshot": false, "sizeInGb": 80 } ] }`- 
                    For API details, see [GetInstanceSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance-state`.

- **AWS CLI**
- 
            
                    **To get information about the state of an instance**The following `get-instance-state`example returns the state of the specified instance.`aws lightsail get-instance-state \ --instance-name``MEAN-1`Output: `{ "state": { "code": 16, "name": "running" } }`- 
                    For API details, see [GetInstanceState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance`.

- **AWS CLI**
- 
            
                    **To get information about an instance**The following `get-instance`example displays details about the instance`MEAN-1`.`aws lightsail get-instance \ --instance-name``MEAN-1`Output: `{ "instance": { "name": "MEAN-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:Instance/bd470fc5-a68b-44c5-8dbc-EXAMPLE4bada", "supportCode": "6EXAMPLE3362/i-05EXAMPLE407c97d3", "createdAt": 1570635023.124, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Instance", "tags": [], "blueprintId": "mean", "blueprintName": "MEAN", "bundleId": "medium_3_0", "isStaticIp": false, "privateIpAddress": "192.0.2.0", "publicIpAddress": "192.0.2.0", "hardware": { "cpuCount": 2, "disks": [ { "createdAt": 1570635023.124, "sizeInGb": 80, "isSystemDisk": true, "iops": 240, "path": "/dev/xvda", "attachedTo": "MEAN-1", "attachmentState": "attached" } ], "ramSizeInGb": 4.0 }, "networking": { "monthlyTransfer": { "gbPerMonthAllocated": 4096 }, "ports": [ { "fromPort": 80, "toPort": 80, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" }, { "fromPort": 22, "toPort": 22, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" }, { "fromPort": 443, "toPort": 443, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" } ] }, "state": { "code": 16, "name": "running" }, "username": "bitnami", "sshKeyName": "MyKey" } }`- 
                    For API details, see [GetInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instances`.

- **AWS CLI**
- 
            
                    **To get information about all instances**The following `get-instances`example displays details about all of the instances in the configured AWS Region.`aws lightsail get-instances`Output: `{ "instances": [ { "name": "Windows_Server_2022-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:Instance/0f44fbb9-8f55-4e47-a25e-EXAMPLE04763", "supportCode": "62EXAMPLE362/i-0bEXAMPLE71a686b9", "createdAt": 1571332358.665, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Instance", "tags": [], "blueprintId": "windows_server_2022", "blueprintName": "Windows Server 2022", "bundleId": "large_win_3_0", "isStaticIp": false, "privateIpAddress": "192.0.2.0", "publicIpAddress": "192.0.2.0", "hardware": { "cpuCount": 1, "disks": [ { "createdAt": 1571332358.665, "sizeInGb": 160, "isSystemDisk": true, "iops": 180, "path": "/dev/sda1", "attachedTo": "Windows_Server_2022-1", "attachmentState": "attached" }, { "name": "my-disk-for-windows-server", "arn": "arn:aws:lightsail:us-west-2:111122223333:Disk/4123a81c-484c-49ea-afea-5EXAMPLEda87", "supportCode": "6EXAMPLE3362/vol-0EXAMPLEb2b99ca3d", "createdAt": 1571355063.494, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Disk", "tags": [], "sizeInGb": 128, "isSystemDisk": false, "iops": 384, "path": "/dev/xvdf", "state": "in-use", "attachedTo": "Windows_Server_2022-1", "isAttached": true, "attachmentState": "attached" } ], "ramSizeInGb": 8.0 }, "networking": { "monthlyTransfer": { "gbPerMonthAllocated": 3072 }, "ports": [ { "fromPort": 80, "toPort": 80, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" }, { "fromPort": 22, "toPort": 22, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" }, { "fromPort": 3389, "toPort": 3389, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" } ] }, "state": { "code": 16, "name": "running" }, "username": "Administrator", "sshKeyName": "LightsailDefaultKeyPair" }, { "name": "MEAN-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:Instance/bd470fc5-a68b-44c5-8dbc-8EXAMPLEbada", "supportCode": "6EXAMPLE3362/i-0EXAMPLEa407c97d3", "createdAt": 1570635023.124, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Instance", "tags": [], "blueprintId": "mean", "blueprintName": "MEAN", "bundleId": "medium_3_0", "isStaticIp": false, "privateIpAddress": "192.0.2.0", "publicIpAddress": "192.0.2.0", "hardware": { "cpuCount": 2, "disks": [ { "name": "Disk-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:Disk/c21cfb0a-07f2-44ae-9a23-bEXAMPLE8096", "supportCode": "6EXAMPLE3362/vol-0EXAMPLEf2f88b32f", "createdAt": 1566585439.587, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "Disk", "tags": [ { "key": "test" } ], "sizeInGb": 8, "isSystemDisk": false, "iops": 240, "path": "/dev/xvdf", "state": "in-use", "attachedTo": "MEAN-1", "isAttached": true, "attachmentState": "attached" }, { "createdAt": 1570635023.124, "sizeInGb": 80, "isSystemDisk": true, "iops": 240, "path": "/dev/sda1", "attachedTo": "MEAN-1", "attachmentState": "attached" } ], "ramSizeInGb": 4.0 }, "networking": { "monthlyTransfer": { "gbPerMonthAllocated": 4096 }, "ports": [ { "fromPort": 80, "toPort": 80, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" }, { "fromPort": 22, "toPort": 22, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" }, { "fromPort": 443, "toPort": 443, "protocol": "tcp", "accessFrom": "Anywhere (0.0.0.0/0)", "accessType": "public", "commonName": "", "accessDirection": "inbound" } ] }, "state": { "code": 16, "name": "running" }, "username": "bitnami", "sshKeyName": "MyTestKey" } ] }`- 
                    For API details, see [GetInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-key-pair`.

- **AWS CLI**
- 
            
                    **To get information about a key pair**The following `get-key-pair`example displays details about the specified key pair.`aws lightsail get-key-pair \ --key-pair-name``MyKey1`Output: `{ "keyPair": { "name": "MyKey1", "arn": "arn:aws:lightsail:us-west-2:111122223333:KeyPair/19a4efdf-3054-43d6-91fd-eEXAMPLE21bf", "supportCode": "6EXAMPLE3362/MyKey1", "createdAt": 1571255026.975, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "KeyPair", "tags": [], "fingerprint": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:gg:hh:ii:jj" } }`- 
                    For API details, see [GetKeyPair](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pair.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-key-pairs`.

- **AWS CLI**
- 
            
                    **To get information about all key pairs**The following `get-key-pairs`example displays details about all of the key pairs in the configured AWS Region.`aws lightsail get-key-pairs`Output: `{ "keyPairs": [ { "name": "MyKey1", "arn": "arn:aws:lightsail:us-west-2:111122223333:KeyPair/19a4efdf-3054-43d6-91fd-eEXAMPLE21bf", "supportCode": "6EXAMPLE3362/MyKey1", "createdAt": 1571255026.975, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "KeyPair", "tags": [], "fingerprint": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff:gg:hh:ii:jj" } ] }`- 
                    For API details, see [GetKeyPairs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pairs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-load-balancer-tls-certificates`.

- **AWS CLI**
- 
            
                    **To get information about TLS certificates for a load balancer**The following `get-load-balancer-tls-certificates`example displays details about the TLS certificates for the specified load balancer.`aws lightsail get-load-balancer-tls-certificates \ --load-balancer-name``LoadBalancer-1`Output: `{ "tlsCertificates": [ { "name": "example-com", "arn": "arn:aws:lightsail:us-west-2:111122223333:LoadBalancerTlsCertificate/d7bf4643-6a02-4cd4-b3c4-fEXAMPLE9b4d", "supportCode": "6EXAMPLE3362/arn:aws:acm:us-west-2:333322221111:certificate/9af8e32c-a54e-4a67-8c63-cEXAMPLEb314", "createdAt": 1571678025.3, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "LoadBalancerTlsCertificate", "loadBalancerName": "LoadBalancer-1", "isAttached": false, "status": "ISSUED", "domainName": "example.com", "domainValidationRecords": [ { "name": "_dEXAMPLE4ede046a0319eb44a4eb3cbc.example.com.", "type": "CNAME", "value": "_bEXAMPLE0899fb7b6bf79d9741d1a383.hkvuiqjoua.acm-validations.aws.", "validationStatus": "SUCCESS", "domainName": "example.com" } ], "issuedAt": 1571678070.0, "issuer": "Amazon", "keyAlgorithm": "RSA-2048", "notAfter": 1605960000.0, "notBefore": 1571616000.0, "serial": "00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff", "signatureAlgorithm": "SHA256WITHRSA", "subject": "CN=example.com", "subjectAlternativeNames": [ "example.com" ] } ] }`- 
                    For API details, see [GetLoadBalancerTlsCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer-tls-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-load-balancer`.

- **AWS CLI**
- 
            
                    **To get information about a load balancer**The following `get-load-balancer`example displays details about the specified load balancer.`aws lightsail get-load-balancer \ --load-balancer-name``LoadBalancer-1`Output: `{ "loadBalancer": { "name": "LoadBalancer-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:LoadBalancer/40486b2b-1ad0-4152-83e4-cEXAMPLE6f4b", "supportCode": "6EXAMPLE3362/arn:aws:elasticloadbalancing:us-west-2:333322221111:loadbalancer/app/bEXAMPLE128cb59d86f946a9395dd304/1EXAMPLE8dd9d77e", "createdAt": 1571677906.723, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "LoadBalancer", "tags": [], "dnsName": "bEXAMPLE128cb59d86f946a9395dd304-1486911371.us-west-2.elb.amazonaws.com", "state": "active", "protocol": "HTTP", "publicPorts": [ 80 ], "healthCheckPath": "/", "instancePort": 80, "instanceHealthSummary": [ { "instanceName": "MEAN-3", "instanceHealth": "healthy" }, { "instanceName": "MEAN-1", "instanceHealth": "healthy" }, { "instanceName": "MEAN-2", "instanceHealth": "healthy" } ], "tlsCertificateSummaries": [ { "name": "example-com", "isAttached": false } ], "configurationOptions": { "SessionStickinessEnabled": "false", "SessionStickiness_LB_CookieDurationSeconds": "86400" } } }`- 
                    For API details, see [GetLoadBalancer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-load-balancers`.

- **AWS CLI**
- 
            
                    **To get information about all load balancers**The following `get-load-balancers`example displays details about all of the load balancers in the configured AWS Region.`aws lightsail get-load-balancers`Output: `{ "loadBalancers": [ { "name": "LoadBalancer-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:LoadBalancer/40486b2b-1ad0-4152-83e4-cEXAMPLE6f4b", "supportCode": "6EXAMPLE3362/arn:aws:elasticloadbalancing:us-west-2:333322221111:loadbalancer/app/bEXAMPLE128cb59d86f946a9395dd304/1EXAMPLE8dd9d77e", "createdAt": 1571677906.723, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "LoadBalancer", "tags": [], "dnsName": "bEXAMPLE128cb59d86f946a9395dd304-1486911371.us-west-2.elb.amazonaws.com", "state": "active", "protocol": "HTTP", "publicPorts": [ 80 ], "healthCheckPath": "/", "instancePort": 80, "instanceHealthSummary": [ { "instanceName": "MEAN-3", "instanceHealth": "healthy" }, { "instanceName": "MEAN-1", "instanceHealth": "healthy" }, { "instanceName": "MEAN-2", "instanceHealth": "healthy" } ], "tlsCertificateSummaries": [ { "name": "example-com", "isAttached": false } ], "configurationOptions": { "SessionStickinessEnabled": "false", "SessionStickiness_LB_CookieDurationSeconds": "86400" } } ] }`- 
                    For API details, see [GetLoadBalancers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-load-balancers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-operation`.

- **AWS CLI**
- 
            
                    **To get information about a single operation**The following `get-operation`example displays details about the specified operation.`aws lightsail get-operation \ --operation-id``e5700e8a-daf2-4b49-bc01-3EXAMPLE910a`Output: `{ "operation": { "id": "e5700e8a-daf2-4b49-bc01-3EXAMPLE910a", "resourceName": "Instance-1", "resourceType": "Instance", "createdAt": 1571679872.404, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "CreateInstance", "status": "Succeeded", "statusChangedAt": 1571679890.304 } }`- 
                    For API details, see [GetOperation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-operation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-operations-for-resource`.

- **AWS CLI**
- 
            
                    **To get all operations for a resource**The following `get-operations-for-resource`example displays details about all operations for the specified resource.`aws lightsail get-operations-for-resource \ --resource-name``LoadBalancer-1`Output: `{ "operations": [ { "id": "e2973046-43f8-4252-a4b4-9EXAMPLE69ce", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571678786.071, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "MEAN-1", "operationType": "DetachInstancesFromLoadBalancer", "status": "Succeeded", "statusChangedAt": 1571679087.57 }, { "id": "2d742a18-0e7f-48c8-9705-3EXAMPLEf98a", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571678782.784, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "MEAN-1", "operationType": "AttachInstancesToLoadBalancer", "status": "Succeeded", "statusChangedAt": 1571678798.465 }, { "id": "6c700fcc-4246-40ab-952b-1EXAMPLEdac2", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571678775.297, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "MEAN-3", "operationType": "AttachInstancesToLoadBalancer", "status": "Succeeded", "statusChangedAt": 1571678842.806 }, ... } ] }`- 
                    For API details, see [GetOperationsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-operations-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-operations`.

- **AWS CLI**
- 
            
                    **To get information about all operations**The following `get-operations`example displays details about all of the operations in the configured AWS Region.`aws lightsail get-operations`Output: `{ "operations": [ { "id": "e5700e8a-daf2-4b49-bc01-3EXAMPLE910a", "resourceName": "Instance-1", "resourceType": "Instance", "createdAt": 1571679872.404, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "CreateInstance", "status": "Succeeded", "statusChangedAt": 1571679890.304 }, { "id": "701a3339-930e-4914-a9f9-7EXAMPLE68d7", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1571678786.072, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "LoadBalancer-1", "operationType": "DetachInstancesFromLoadBalancer", "status": "Succeeded", "statusChangedAt": 1571679086.399 }, { "id": "e2973046-43f8-4252-a4b4-9EXAMPLE69ce", "resourceName": "LoadBalancer-1", "resourceType": "LoadBalancer", "createdAt": 1571678786.071, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "WordPress-1", "operationType": "DetachInstancesFromLoadBalancer", "status": "Succeeded", "statusChangedAt": 1571679087.57 }, ... } ] }`- 
                    For API details, see [GetOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-regions`.

- **AWS CLI**
- 
            
                    **To get all AWS Regions for Amazon Lightsail**The following `get-regions`example displays details about all of the AWS Regions for Amazon Lightsail.`aws lightsail get-regions`Output: `{ "regions": [ { "continentCode": "NA", "description": "This region is recommended to serve users in the eastern United States", "displayName": "Virginia", "name": "us-east-1", "availabilityZones": [], "relationalDatabaseAvailabilityZones": [] }, { "continentCode": "NA", "description": "This region is recommended to serve users in the eastern United States", "displayName": "Ohio", "name": "us-east-2", "availabilityZones": [], "relationalDatabaseAvailabilityZones": [] }, { "continentCode": "NA", "description": "This region is recommended to serve users in the northwestern United States, Alaska, and western Canada", "displayName": "Oregon", "name": "us-west-2", "availabilityZones": [], "relationalDatabaseAvailabilityZones": [] }, ... } ] }`- 
                    For API details, see [GetRegions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-regions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-blueprints`.

- **AWS CLI**
- 
            
                    **To get the blueprints for new relational databases**The following `get-relational-database-blueprints`example displays details about all of the available relational database blueprints that can be used to create new relational databases in Amazon Lightsail.`aws lightsail get-relational-database-blueprints`Output: `{ "blueprints": [ { "blueprintId": "mysql_5_6", "engine": "mysql", "engineVersion": "5.6.44", "engineDescription": "MySQL Community Edition", "engineVersionDescription": "MySQL 5.6.44", "isEngineDefault": false }, { "blueprintId": "mysql_5_7", "engine": "mysql", "engineVersion": "5.7.26", "engineDescription": "MySQL Community Edition", "engineVersionDescription": "MySQL 5.7.26", "isEngineDefault": true }, { "blueprintId": "mysql_8_0", "engine": "mysql", "engineVersion": "8.0.16", "engineDescription": "MySQL Community Edition", "engineVersionDescription": "MySQL 8.0.16", "isEngineDefault": false }, { "blueprintId": "postgres_9_6", "engine": "postgres", "engineVersion": "9.6.15", "engineDescription": "PostgreSQL", "engineVersionDescription": "PostgreSQL 9.6.15-R1", "isEngineDefault": false }, { "blueprintId": "postgres_10", "engine": "postgres", "engineVersion": "10.10", "engineDescription": "PostgreSQL", "engineVersionDescription": "PostgreSQL 10.10-R1", "isEngineDefault": false }, { "blueprintId": "postgres_11", "engine": "postgres", "engineVersion": "11.5", "engineDescription": "PostgreSQL", "engineVersionDescription": "PostgreSQL 11.5-R1", "isEngineDefault": true } ] }`- 
                    For API details, see [GetRelationalDatabaseBlueprints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-blueprints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-bundles`.

- **AWS CLI**
- 
            
                    **To get the bundles for new relational databases**The following `get-relational-database-bundles`example displays details about all of the available relational database bundles that can be used to create new relational databases in Amazon Lightsail. Note that the response does not include inactive bundles because the`--include-inactive`flag is not specified in the command. You cannot use inactive bundles to create new relational databases.`aws lightsail get-relational-database-bundles`Output: `{ "bundles": [ { "bundleId": "micro_2_0", "name": "Micro", "price": 15.0, "ramSizeInGb": 1.0, "diskSizeInGb": 40, "transferPerMonthInGb": 100, "cpuCount": 2, "isEncrypted": true, "isActive": true }, { "bundleId": "micro_ha_2_0", "name": "Micro with High Availability", "price": 30.0, "ramSizeInGb": 1.0, "diskSizeInGb": 40, "transferPerMonthInGb": 100, "cpuCount": 2, "isEncrypted": true, "isActive": true }, { "bundleId": "small_2_0", "name": "Small", "price": 30.0, "ramSizeInGb": 2.0, "diskSizeInGb": 80, "transferPerMonthInGb": 100, "cpuCount": 2, "isEncrypted": true, "isActive": true }, { "bundleId": "small_ha_2_0", "name": "Small with High Availability", "price": 60.0, "ramSizeInGb": 2.0, "diskSizeInGb": 80, "transferPerMonthInGb": 100, "cpuCount": 2, "isEncrypted": true, "isActive": true }, { "bundleId": "medium_2_0", "name": "Medium", "price": 60.0, "ramSizeInGb": 4.0, "diskSizeInGb": 120, "transferPerMonthInGb": 100, "cpuCount": 2, "isEncrypted": true, "isActive": true }, { "bundleId": "medium_ha_2_0", "name": "Medium with High Availability", "price": 120.0, "ramSizeInGb": 4.0, "diskSizeInGb": 120, "transferPerMonthInGb": 100, "cpuCount": 2, "isEncrypted": true, "isActive": true }, { "bundleId": "large_2_0", "name": "Large", "price": 115.0, "ramSizeInGb": 8.0, "diskSizeInGb": 240, "transferPerMonthInGb": 200, "cpuCount": 2, "isEncrypted": true, "isActive": true }, { "bundleId": "large_ha_2_0", "name": "Large with High Availability", "price": 230.0, "ramSizeInGb": 8.0, "diskSizeInGb": 240, "transferPerMonthInGb": 200, "cpuCount": 2, "isEncrypted": true, "isActive": true } ] }`For more information, see [Creating a database in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-creating-a-database)in the*Amazon Lightsail Developer Guide*.- 
                    For API details, see [GetRelationalDatabaseBundles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-bundles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-events`.

- **AWS CLI**
- 
            
                    **To get the events for a relational database**The following `get-relational-database-events`example displays details about events in the last 17 hours (1020 minutes) for the specified relational database.`aws lightsail get-relational-database-events \ --relational-database-name``Database-1`\ --duration-in-minutes`1020`Output: `{ "relationalDatabaseEvents": [ { "resource": "Database-1", "createdAt": 1571654146.553, "message": "Backing up Relational Database", "eventCategories": [ "backup" ] }, { "resource": "Database-1", "createdAt": 1571654249.98, "message": "Finished Relational Database backup", "eventCategories": [ "backup" ] } ] }`- 
                    For API details, see [GetRelationalDatabaseEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-log-events`.

- **AWS CLI**
- 
            
                    **To get log events for a relational database**The following `get-relational-database-log-events`example displays details about the specified log between`1570733176`and`1571597176`for relational database`Database1`. The information returned is configured to start from`head`.We recommend that you use a unix time converter to identify the start and end times. `aws lightsail get-relational-database-log-events \ --relational-database-name``Database1`\ --log-stream-name`error`\ --start-from-head \ --start-time`1570733176`\ --end-time`1571597176`Output: `{ "resourceLogEvents": [ { "createdAt": 1570820267.0, "message": "2019-10-11 18:57:47 20969 [Warning] IP address '192.0.2.0' could not be resolved: Name or service not known" }, { "createdAt": 1570860974.0, "message": "2019-10-12 06:16:14 20969 [Warning] IP address '8192.0.2.0' could not be resolved: Temporary failure in name resolution" }, { "createdAt": 1570860977.0, "message": "2019-10-12 06:16:17 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution" }, { "createdAt": 1570860979.0, "message": "2019-10-12 06:16:19 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution" }, { "createdAt": 1570860981.0, "message": "2019-10-12 06:16:21 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution" }, { "createdAt": 1570860982.0, "message": "2019-10-12 06:16:22 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution" }, { "createdAt": 1570860984.0, "message": "2019-10-12 06:16:24 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution" }, { "createdAt": 1570860986.0, "message": "2019-10-12 06:16:26 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution" }, ... } ], "nextBackwardToken": "eEXAMPLEZXJUZXh0IjoiZnRWb3F3cUpRSlQ5NndMYThxelRUZlFhR3J6c2dKWEEvM2kvajZMZzVVVWpqRDN0YjFXTjNrak5pRk9iVFRZdjkwVGlpZGw5NFJGSFRQTEdJSjdpQnFCRk5CZFJlYTZaSXpScStuZjJEYXhqM2grUFVJOEpIYlU5YWJ2QitvQWN5cEFyVUo3VDk1QWY3bVF6MEwvcVovVldZdGc9Iiwibm9uY2UiOiJBNHpzdWMvUkZZKzRvUzhEIiwiY2lwaGVyIjoiQUVTL0dDTS9Ob1BhZGEXAMPLEQ==", "nextForwardToken": "eEXAMPLEZXJUZXh0IjoiT09Lb0Z6ZFRJbHhaNEQ5N2tPbkkwRmwwNUxPZjFTbFFwUklQbzlSaWgvMWVXbEk4aG56VHg4bW1Gb3grbDVodUVNZEdiZXN0TzVYcjlLK1FUdFB2RlJLS2FMcU05WkN3Rm1uVzBkOFpDR2g0b1BBVlg2NVFGNDNPazZzRXJieHRuU0xzdkRNTkFUMTZibU9HM2YyaGxiS0hUUDA9Iiwibm9uY2UiOiJFQmI4STQ3cU5aWXNXZ0g4IiwiY2lwaGVyIjoiQUVTL0dDTS9Ob1BhZGEXAMPLEQ==" }`- 
                    For API details, see [GetRelationalDatabaseLogEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-log-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-log-streams`.

- **AWS CLI**
- 
            
                    **To get the log streams for a relational database**The following `get-relational-database-log-streams`example returns all of the available log streams for the specified relational database.`aws lightsail get-relational-database-log-streams \ --relational-database-name``Database1`Output: `{ "logStreams": [ "audit", "error", "general", "slowquery" ] }`- 
                    For API details, see [GetRelationalDatabaseLogStreams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-log-streams.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-master-user-password`.

- **AWS CLI**
- 
            
                    **To get the master user password for a relational database**The following `get-relational-database-master-user-password`example returns information about the master user password for the specified relational database.`aws lightsail get-relational-database-master-user-password \ --relational-database-name``Database-1`Output: `{ "masterUserPassword": "VEXAMPLEec.9qvx,_t<)Wkf)kwboM,>2", "createdAt": 1571259453.959 }`- 
                    For API details, see [GetRelationalDatabaseMasterUserPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-master-user-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-metric-data`.

- **AWS CLI**
- 
            
                    **To get metric data for a relational database**The following `get-relational-database-metric-data`example returns the count sum of the metric`DatabaseConnections`over the period of 24 hours (`86400`seconds) between`1570733176`and`1571597176`for relational database`Database1`.We recommend that you use a unix time converter to identify the start and end times. `aws lightsail get-relational-database-metric-data \ --relational-database-name``Database1`\ --metric-name`DatabaseConnections`\ --period`86400`\ --start-time`1570733176`\ --end-time`1571597176`\ --unit`Count`\ --statistics`Sum`Output: `{ "metricName": "DatabaseConnections", "metricData": [ { "sum": 1.0, "timestamp": 1571510760.0, "unit": "Count" }, { "sum": 1.0, "timestamp": 1570733160.0, "unit": "Count" }, { "sum": 1.0, "timestamp": 1570992360.0, "unit": "Count" }, { "sum": 0.0, "timestamp": 1571251560.0, "unit": "Count" }, { "sum": 721.0, "timestamp": 1570819560.0, "unit": "Count" }, { "sum": 1.0, "timestamp": 1571078760.0, "unit": "Count" }, { "sum": 2.0, "timestamp": 1571337960.0, "unit": "Count" }, { "sum": 684.0, "timestamp": 1570905960.0, "unit": "Count" }, { "sum": 0.0, "timestamp": 1571165160.0, "unit": "Count" }, { "sum": 1.0, "timestamp": 1571424360.0, "unit": "Count" } ] }`- 
                    For API details, see [GetRelationalDatabaseMetricData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-metric-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-parameters`.

- **AWS CLI**
- 
            
                    **To get parameters for a relational database**The following `get-relational-database-parameters`example returns information about all of the available parameters for the specified relational database.`aws lightsail get-relational-database-parameters \ --relational-database-name``Database-1`Output: `{ "parameters": [ { "allowedValues": "0,1", "applyMethod": "pending-reboot", "applyType": "dynamic", "dataType": "boolean", "description": "Automatically set all granted roles as active after the user has authenticated successfully.", "isModifiable": true, "parameterName": "activate_all_roles_on_login", "parameterValue": "0" }, { "allowedValues": "0,1", "applyMethod": "pending-reboot", "applyType": "static", "dataType": "boolean", "description": "Controls whether user-defined functions that have only an xxx symbol for the main function can be loaded", "isModifiable": false, "parameterName": "allow-suspicious-udfs" }, { "allowedValues": "0,1", "applyMethod": "pending-reboot", "applyType": "dynamic", "dataType": "boolean", "description": "Sets the autocommit mode", "isModifiable": true, "parameterName": "autocommit" }, { "allowedValues": "0,1", "applyMethod": "pending-reboot", "applyType": "static", "dataType": "boolean", "description": "Controls whether the server autogenerates SSL key and certificate files in the data directory, if they do not already exist.", "isModifiable": false, "parameterName": "auto_generate_certs" }, ... } ] }`For more information, see [Updating database parameters in Amazon Lightsail](https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-updating-database-parameters)in the*Lightsail Dev Guide*.- 
                    For API details, see [GetRelationalDatabaseParameters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-parameters.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-snapshot`.

- **AWS CLI**
- 
            
                    **To get information about a relational database snapshot**The following `get-relational-database-snapshot`example displays details about the specified relational database snapshot.`aws lightsail get-relational-database-snapshot \ --relational-database-snapshot-name``Database-1-1571350042`Output: `{ "relationalDatabaseSnapshot": { "name": "Database-1-1571350042", "arn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabaseSnapshot/0389bbad-4b85-4c3d-9EXAMPLEaee3643d2", "supportCode": "6EXAMPLE3362/ls-8EXAMPLE2ba7ad041451946fafc2ad19cfbd9eb2", "createdAt": 1571350046.238, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "RelationalDatabaseSnapshot", "tags": [], "engine": "mysql", "engineVersion": "8.0.16", "sizeInGb": 40, "state": "available", "fromRelationalDatabaseName": "Database-1", "fromRelationalDatabaseArn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabase/7ea932b1-b85a-4bd5-9b3e-bEXAMPLE8cc4", "fromRelationalDatabaseBundleId": "micro_1_0", "fromRelationalDatabaseBlueprintId": "mysql_8_0" } }`- 
                    For API details, see [GetRelationalDatabaseSnapshot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshot.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database-snapshots`.

- **AWS CLI**
- 
            
                    **To get information about all relational database snapshots**The following `get-relational-database-snapshots`example displays details about all of the relational database snapshots in the configured AWS Region.`aws lightsail get-relational-database-snapshots`Output: `{ "relationalDatabaseSnapshots": [ { "name": "Database-1-1571350042", "arn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabaseSnapshot/0389bbad-4b85-4c3d-9861-6EXAMPLE43d2", "supportCode": "6EXAMPLE3362/ls-8EXAMPLE2ba7ad041451946fafc2ad19cfbd9eb2", "createdAt": 1571350046.238, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "RelationalDatabaseSnapshot", "tags": [], "engine": "mysql", "engineVersion": "8.0.16", "sizeInGb": 40, "state": "available", "fromRelationalDatabaseName": "Database-1", "fromRelationalDatabaseArn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabase/7ea932b1-b85a-4bd5-9b3e-bEXAMPLE8cc4", "fromRelationalDatabaseBundleId": "micro_1_0", "fromRelationalDatabaseBlueprintId": "mysql_8_0" }, { "name": "Database1-Console", "arn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabaseSnapshot/8b94136e-06ec-4b1a-a3fb-5EXAMPLEe1e9", "supportCode": "6EXAMPLE3362/ls-9EXAMPLE14b000d34c8d1c432734e137612d5b5c", "createdAt": 1571249981.025, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "RelationalDatabaseSnapshot", "tags": [ { "key": "test" } ], "engine": "mysql", "engineVersion": "5.6.44", "sizeInGb": 40, "state": "available", "fromRelationalDatabaseName": "Database1", "fromRelationalDatabaseArn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabase/a6161cb7-4535-4f16-9dcf-8EXAMPLE3d4e", "fromRelationalDatabaseBundleId": "micro_1_0", "fromRelationalDatabaseBlueprintId": "mysql_5_6" } ] }`- 
                    For API details, see [GetRelationalDatabaseSnapshots](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-snapshots.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-database`.

- **AWS CLI**
- 
            
                    **To get information about a relational database**The following `get-relational-database`example displays details about the specified relational database.`aws lightsail get-relational-database \ --relational-database-name``Database-1`Output: `{ "relationalDatabase": { "name": "Database-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabase/7ea932b1-b85a-4bd5-9b3e-bEXAMPLE8cc4", "supportCode": "6EXAMPLE3362/ls-9EXAMPLE8ad863723b62cc8901a8aa6e794ae0d2", "createdAt": 1571259453.795, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "RelationalDatabase", "tags": [], "relationalDatabaseBlueprintId": "mysql_8_0", "relationalDatabaseBundleId": "micro_1_0", "masterDatabaseName": "dbmaster", "hardware": { "cpuCount": 1, "diskSizeInGb": 40, "ramSizeInGb": 1.0 }, "state": "available", "backupRetentionEnabled": false, "pendingModifiedValues": {}, "engine": "mysql", "engineVersion": "8.0.16", "masterUsername": "dbmasteruser", "parameterApplyStatus": "in-sync", "preferredBackupWindow": "10:01-10:31", "preferredMaintenanceWindow": "sat:11:14-sat:11:44", "publiclyAccessible": true, "masterEndpoint": { "port": 3306, "address": "ls-9EXAMPLE8ad863723b62ccEXAMPLEa6e794ae0d2.czowadgeezqi.us-west-2.rds.amazonaws.com" }, "pendingMaintenanceActions": [] } }`- 
                    For API details, see [GetRelationalDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-relational-databases`.

- **AWS CLI**
- 
            
                    **To get information about all relational databases**The following `get-relational-databases`example displays details about all of the relational databases in the configured AWS Region.`aws lightsail get-relational-databases`Output: `{ "relationalDatabases": [ { "name": "MySQL", "arn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabase/8529020c-3ab9-4d51-92af-5EXAMPLE8979", "supportCode": "6EXAMPLE3362/ls-3EXAMPLEa995d8c3b06b4501356e5f2f28e1aeba", "createdAt": 1554306019.155, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "RelationalDatabase", "tags": [], "relationalDatabaseBlueprintId": "mysql_8_0", "relationalDatabaseBundleId": "micro_1_0", "masterDatabaseName": "dbmaster", "hardware": { "cpuCount": 1, "diskSizeInGb": 40, "ramSizeInGb": 1.0 }, "state": "available", "backupRetentionEnabled": true, "pendingModifiedValues": {}, "engine": "mysql", "engineVersion": "8.0.15", "latestRestorableTime": 1571686200.0, "masterUsername": "dbmasteruser", "parameterApplyStatus": "in-sync", "preferredBackupWindow": "07:51-08:21", "preferredMaintenanceWindow": "tue:12:18-tue:12:48", "publiclyAccessible": true, "masterEndpoint": { "port": 3306, "address": "ls-3EXAMPLEa995d8c3b06b4501356e5f2fEXAMPLEa.czowadgeezqi.us-west-2.rds.amazonaws.com" }, "pendingMaintenanceActions": [] }, { "name": "Postgres", "arn": "arn:aws:lightsail:us-west-2:111122223333:RelationalDatabase/e9780b6b-d0ab-4af2-85f1-1EXAMPLEac68", "supportCode": "6EXAMPLE3362/ls-3EXAMPLEb4fffb5cec056220c734713e14bd5fcd", "createdAt": 1554306000.814, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "resourceType": "RelationalDatabase", "tags": [], "relationalDatabaseBlueprintId": "postgres_11", "relationalDatabaseBundleId": "micro_1_0", "masterDatabaseName": "dbmaster", "hardware": { "cpuCount": 1, "diskSizeInGb": 40, "ramSizeInGb": 1.0 }, "state": "available", "backupRetentionEnabled": true, "pendingModifiedValues": {}, "engine": "postgres", "engineVersion": "11.1", "latestRestorableTime": 1571686339.0, "masterUsername": "dbmasteruser", "parameterApplyStatus": "in-sync", "preferredBackupWindow": "06:19-06:49", "preferredMaintenanceWindow": "sun:10:19-sun:10:49", "publiclyAccessible": false, "masterEndpoint": { "port": 5432, "address": "ls-3EXAMPLEb4fffb5cec056220c734713eEXAMPLEd.czowadgeezqi.us-west-2.rds.amazonaws.com" }, "pendingMaintenanceActions": [] } ] }`- 
                    For API details, see [GetRelationalDatabases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-databases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-static-ip`.

- **AWS CLI**
- 
            
                    **To get information about a static IP**The following `get-static-ip`example displays details about the specified static IP.`aws lightsail get-static-ip \ --static-ip-name``StaticIp-1`Output: `{ "staticIp": { "name": "StaticIp-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:StaticIp/2257cd76-1f0e-4ac0-82e2-2EXAMPLE23ad", "supportCode": "6EXAMPLE3362/192.0.2.0", "createdAt": 1571071325.076, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "StaticIp", "ipAddress": "192.0.2.0", "isAttached": false } }`- 
                    For API details, see [GetStaticIp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-static-ip.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-static-ips`.

- **AWS CLI**
- 
            
                    **To get information about all static IPs**The following `get-static-ips`example displays details about all of the static IPs in the configured AWS Region.`aws lightsail get-static-ips`Output: `{ "staticIps": [ { "name": "StaticIp-1", "arn": "arn:aws:lightsail:us-west-2:111122223333:StaticIp/2257cd76-1f0e-4ac0-8EXAMPLE16f9423ad", "supportCode": "6EXAMPLE3362/192.0.2.0", "createdAt": 1571071325.076, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "StaticIp", "ipAddress": "192.0.2.0", "isAttached": false }, { "name": "StaticIP-2", "arn": "arn:aws:lightsail:us-west-2:111122223333:StaticIp/c61edb40-e5f0-4fd6-ae7c-8EXAMPLE19f8", "supportCode": "6EXAMPLE3362/192.0.2.2", "createdAt": 1568305385.681, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "resourceType": "StaticIp", "ipAddress": "192.0.2.2", "attachedTo": "WordPress-1", "isAttached": true } ] }`- 
                    For API details, see [GetStaticIps](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-static-ips.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `is-vpc-peered`.

- **AWS CLI**
- 
            
                    **To identify if your Amazon Lightsail virtual private cloud is peered**The following `is-vpc-peered`example returns the peering status of the Amazon Lightsail virtual private cloud (VPC) for the specified AWS Region.`aws lightsail is-vpc-peered \ --region``us-west-2`Output: `{ "isPeered": true }`- 
                    For API details, see [IsVpcPeered](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/is-vpc-peered.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `open-instance-public-ports`.

- **AWS CLI**
- 
            
                    **To open firewall ports for an instance**The following `open-instance-public-ports`example opens TCP port 22 on the specified instance.`aws lightsail open-instance-public-ports \ --instance-name``MEAN-2`\ --port-info`fromPort=22,protocol=TCP,toPort=22`Output: `{ "operation": { "id": "719744f0-a022-46f2-9f11-6EXAMPLE4642", "resourceName": "MEAN-2", "resourceType": "Instance", "createdAt": 1571072906.849, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "22/tcp", "operationType": "OpenInstancePublicPorts", "status": "Succeeded", "statusChangedAt": 1571072906.849 } }`- 
                    For API details, see [OpenInstancePublicPorts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/open-instance-public-ports.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `peer-vpc`.

- **AWS CLI**
- 
            
                    **To peer the Amazon Lightsail virtual private cloud**The following `peer-vpc`example peers the Amazon Lightsail virtual private cloud (VPC) for the specified AWS Region.`aws lightsail peer-vpc \ --region``us-west-2`Output: `{ "operation": { "id": "787e846a-54ac-497f-bce2-9EXAMPLE5d91", "resourceName": "vpc-0EXAMPLEa5261efb3", "resourceType": "PeeredVpc", "createdAt": 1571694233.104, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "vpc-e2b3eb9b", "operationType": "PeeredVpc", "status": "Succeeded", "statusChangedAt": 1571694233.104 } }`- 
                    For API details, see [PeerVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/peer-vpc.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-instance`.

- **AWS CLI**
- 
            
                    **To reboot an instance**The following `reboot-instance`example reboots the specified instance.`aws lightsail reboot-instance \ --instance-name``MEAN-1`Output: `{ "operations": [ { "id": "2b679f1c-8b71-4bb4-8e97-8EXAMPLEed93", "resourceName": "MEAN-1", "resourceType": "Instance", "createdAt": 1571694445.49, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "", "operationType": "RebootInstance", "status": "Succeeded", "statusChangedAt": 1571694445.49 } ] }`- 
                    For API details, see [RebootInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/reboot-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-relational-database`.

- **AWS CLI**
- 
            
                    **To reboot a relational database**The following `reboot-relational-database`example reboots the specified relational database.`aws lightsail reboot-relational-database \ --relational-database-name``Database-1`Output: `{ "operations": [ { "id": "e4c980c0-3137-496c-9c91-1EXAMPLEdec2", "resourceName": "Database-1", "resourceType": "RelationalDatabase", "createdAt": 1571694532.91, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationDetails": "", "operationType": "RebootRelationalDatabase", "status": "Started", "statusChangedAt": 1571694532.91 } ] }`- 
                    For API details, see [RebootRelationalDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/reboot-relational-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `release-static-ip`.

- **AWS CLI**
- 
            
                    **To delete a static IP**The following `release-static-ip`example deletes the specified static IP.`aws lightsail release-static-ip \ --static-ip-name``StaticIp-1`Output: `{ "operations": [ { "id": "e374c002-dc6d-4c7f-919f-2EXAMPLE13ce", "resourceName": "StaticIp-1", "resourceType": "StaticIp", "createdAt": 1571694962.003, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationType": "ReleaseStaticIp", "status": "Succeeded", "statusChangedAt": 1571694962.003 } ] }`- 
                    For API details, see [ReleaseStaticIp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/release-static-ip.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-instance`.

- **AWS CLI**
- 
            
                    **To start an instance**The following `start-instance`example starts the specified instance.`aws lightsail start-instance \ --instance-name``WordPress-1`Output: `{ "operations": [ { "id": "f88d2a93-7cea-4165-afce-2d688cb18f23", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1571695583.463, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "StartInstance", "status": "Started", "statusChangedAt": 1571695583.463 } ] }`- 
                    For API details, see [StartInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/start-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-relational-database`.

- **AWS CLI**
- 
            
                    **To start a relational database**The following `start-relational-database`example starts the specified relational database.`aws lightsail start-relational-database \ --relational-database-name``Database-1`Output: `{ "operations": [ { "id": "4d5294ec-a38a-4fda-9e37-aEXAMPLE0d24", "resourceName": "Database-1", "resourceType": "RelationalDatabase", "createdAt": 1571695998.822, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "StartRelationalDatabase", "status": "Started", "statusChangedAt": 1571695998.822 } ] }`- 
                    For API details, see [StartRelationalDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/start-relational-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-instance`.

- **AWS CLI**
- 
            
                    **To stop an instance**The following `stop-instance`example stops the specified instance.`aws lightsail stop-instance \ --instance-name``WordPress-1`Output: `{ "operations": [ { "id": "265357e2-2943-4d51-888a-1EXAMPLE7585", "resourceName": "WordPress-1", "resourceType": "Instance", "createdAt": 1571695471.134, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "StopInstance", "status": "Started", "statusChangedAt": 1571695471.134 } ] }`- 
                    For API details, see [StopInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-relational-database`.

- **AWS CLI**
- 
            
                    **To stop a relational database**The following `stop-relational-database`example stops the specified relational database.`aws lightsail stop-relational-database \ --relational-database-name``Database-1`Output: `{ "operations": [ { "id": "cc559c19-4adb-41e4-b75b-5EXAMPLE4e61", "resourceName": "Database-1", "resourceType": "RelationalDatabase", "createdAt": 1571695526.29, "location": { "availabilityZone": "us-west-2a", "regionName": "us-west-2" }, "isTerminal": false, "operationType": "StopRelationalDatabase", "status": "Started", "statusChangedAt": 1571695526.29 } ] }`- 
                    For API details, see [StopRelationalDatabase](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/stop-relational-database.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `unpeer-vpc`.

- **AWS CLI**
- 
            
                    **To unpeer the Amazon Lightsail virtual private cloud**The following `unpeer-vpc`example unpeers the Amazon Lightsail virtual private cloud (VPC) for the specified AWS Region.`aws lightsail unpeer-vpc \ --region``us-west-2`Output: `{ "operation": { "id": "531aca64-7157-47ab-84c6-eEXAMPLEd898", "resourceName": "vpc-0EXAMPLEa5261efb3", "resourceType": "PeeredVpc", "createdAt": 1571694109.945, "location": { "availabilityZone": "all", "regionName": "us-west-2" }, "isTerminal": true, "operationDetails": "vpc-e2b3eb9b", "operationType": "UnpeeredVpc", "status": "Succeeded", "statusChangedAt": 1571694109.945 } }`- 
                    For API details, see [UnpeerVpc](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/unpeer-vpc.html)in*AWS CLI Command Reference*.
 
-