# AWS Cloud Map examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_servicediscovery_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_servicediscovery_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Cloud Map.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-http-namespace`.

- **AWS CLI**
- 
            
                    **To create an HTTP namespace**The following `create-http-namespace`example creates an HTTP namespace`example.com`.`aws servicediscovery create-http-namespace \ --name``example.com`\ --creator-request-id`example-request-id`Output: `{ "OperationId": "gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9302yzd" }`To confirm that the operation succeeded, you can run `get-operation`. For more information, see[get-operation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/get-operation.html).For more information about creating a namespace, see [Creating an AWS Cloud Map namespace to group application services](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [CreateHttpNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-http-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-private-dns-namespace`.

- **AWS CLI**
- 
            
                    **To create a private DNS namespace**The following `create-private-dns-namespace`example creates a private DNS namespace.`aws servicediscovery create-private-dns-namespace \ --name``example.com`\ --vpc`vpc-1c56417b`Output: `{ "OperationId": "gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9302yzd" }`To confirm that the operation succeeded, you can run `get-operation`. For more information, see[get-operation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/get-operation.html).For more information, see [Creating namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [CreatePrivateDnsNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-private-dns-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-public-dns-namespace`.

- **AWS CLI**
- 
            
                    **To create an public DNS namespace**The following `create-public-dns-namespace`example creates an public DNS namespace`example.com`.`aws servicediscovery create-public-dns-namespace \ --name``example-public-dns.com`\ --creator-request-id`example-public-request-id`\ --properties`DnsProperties={SOA={TTL=60}}`Output: `{ "OperationId": "gv4g5meo7ndmeh4fqskygvk23d2fijwa-k9302yzd" }`To confirm that the operation succeeded, you can run `get-operation`.For more information about creating a namespace, see [Creating an AWS Cloud Map namespace to group application services](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [CreatePublicDnsNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-public-dns-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service`.

- **AWS CLI**
- 
            
                    **Example 1: To create a service using namespace ID**The following `create-service`example creates a service.`aws servicediscovery create-service \ --name``myservice`\ --namespace-id`ns-ylexjili4cdxy3xm`\ --dns-config`"RoutingPolicy=MULTIVALUE,DnsRecords=[{Type=A,TTL=60}]"`Output: `{ "Service": { "Id": "srv-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Name": "myservice", "NamespaceId": "ns-abcd1234xmpl5678", "DnsConfig": { "NamespaceId": "ns-abcd1234xmpl5678", "RoutingPolicy": "MULTIVALUE", "DnsRecords": [ { "Type": "A", "TTL": 60 } ] }, "Type": "DNS_HTTP", "CreateDate": "2025-08-18T13:45:31.023000-05:00", "CreatorRequestId": "abcd1234-5678-90ab-cdef-xmpl12345678", "CreatedByAccount": "123456789012" } }`For more information, see [Creating an AWS Cloud Map service for an application component](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To create a service using namespace ARN**The following `create-service`example creates a service using a namespace ARN instead of namespace ID. Specifying a namespace ARN is necessary when creating a service in a shared namespace.`aws servicediscovery create-service \ --name``myservice-arn`\ --namespace-id`arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678`\ --dns-config`"RoutingPolicy=MULTIVALUE,DnsRecords=[{Type=A,TTL=60}]"`Output: `{ "Service": { "Id": "srv-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Name": "myservice-arn", "NamespaceId": "ns-abcd1234xmpl5678", "DnsConfig": { "NamespaceId": "ns-abcd1234xmpl5678", "RoutingPolicy": "MULTIVALUE", "DnsRecords": [ { "Type": "A", "TTL": 60 } ] }, "Type": "DNS_HTTP", "CreateDate": "2025-08-18T13:45:31.023000-05:00", "CreatorRequestId": "abcd1234-5678-90ab-cdef-xmpl12345678", "CreatedByAccount": "123456789012" } }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [CreateService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/create-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-namespace`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a namespace**The following `delete-namespace`example deletes a namespace.`aws servicediscovery delete-namespace \ --id``ns-abcd1234xmpl5678`Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`To confirm that the operation succeeded, you can run `get-operation`. For more information, see[get-operation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/get-operation.html).For more information, see [Deleting an AWS Cloud Map namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-namespaces.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To delete a namespace using namespace ARN**The following `delete-namespace`example deletes a namespace using its ARN.`aws servicediscovery delete-namespace \ --id``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678`Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`For more information, see [Deleting an AWS Cloud Map namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [DeleteNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/delete-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service-attributes`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a service attribute**The following `delete-service-attributes`example deletes a service attribute with the key`Port`that is associated with the specified service.`aws servicediscovery delete-service-attributes \ --service-id``srv-abcd1234xmpl5678`\ --attributes`Port`This command produces no output. For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To delete a service attribute using ARN**The following `delete-service-attributes`example deletes a service attribute using the service ARN. Specifying the ARN is necessary for deleting attributes associated with services created in namespaces shared with your account.`aws servicediscovery delete-service-attributes \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678`\ --attributes`Port`This command produces no output. For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)and[Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [DeleteServiceAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/delete-service-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service`.

- **AWS CLI**
- 
            
                    **Example 1: To delete a service**The following `delete-service`example deletes a service.`aws servicediscovery delete-service \ --id``srv-abcd1234xmpl5678`This command produces no output. For more information, see [Deleting an AWS Cloud Map service](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To delete a service using ARN**The following `delete-service`example deletes a service using its ARN.`aws servicediscovery delete-service \ --id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678`This command produces no output. For more information, see [Deleting an AWS Cloud Map service](https://docs.aws.amazon.com/cloud-map/latest/dg/deleting-services.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [DeleteService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/delete-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-instance`.

- **AWS CLI**
- 
            
                    **Example 1: To deregister a service instance**The following `deregister-instance`example deregisters a service instance.`aws servicediscovery deregister-instance \ --service-id``srv-p5zdwlg5uvvzjita`\ --instance-id`myservice-53`Output: `{ "OperationId": "4yejorelbukcjzpnr6tlmrghsjwpngf4-k98rnaiq" }`To confirm that the operation succeeded, you can run `get-operation`. For more information, see[get-operation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/get-operation.html).For more information, see [Deregistering service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/deregistering-instances.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To deregister a service instance using service ARN for shared namespaces**The following `deregister-instance`example deregisters a service instance using a service ARN instead of service ID. Specifying an ARN is required when deregistering instances from services created in namespaces that are shared with your account.`aws servicediscovery deregister-instance \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-p5zdwlg5uvvzjita`\ --instance-id`web-server-01`Output: `{ "OperationId": "gv4g5meo7ndmkqjrhpn39wk42xmpl" }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)and[Deregistering an AWS Cloud Map service instance](https://docs.aws.amazon.com/cloud-map/latest/dg/deregistering-instances.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [DeregisterInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/deregister-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `discover-instances-revision`.

- **AWS CLI**
- 
            
                    **Example 1: To discover the revision of an instance**The following `discover-instances-revision`example discovers the increasing revision of an instance.`aws servicediscovery discover-instances-revision \ --namespace-name``example.com`\ --service-name`myservice`Output: `{ "InstancesRevision": 123456 }`For more information, see [AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To discover the revision of instances from a specific owner account**The following `discover-instances-revision`example discovers the revision of instances from a specific owner account. The owner-account parameter is necessary for instances in namespaces that are shared with your account.`aws servicediscovery discover-instances-revision \ --namespace-name``shared-namespace`\ --service-name`shared-service`\ --owner-account`123456789111`Output: `{ "InstancesRevision": 1234567890 }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)and[AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [DiscoverInstancesRevision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances-revision.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `discover-instances`.

- **AWS CLI**
- 
            
                    **Example 1: To discover registered instances**The following `discover-instances`example discovers registered instances.`aws servicediscovery discover-instances \ --namespace-name``example.com`\ --service-name`myservice`\ --max-results`10`\ --health-status`ALL`Output: `{ "Instances": [ { "InstanceId": "myservice-53", "NamespaceName": "example.com", "ServiceName": "myservice", "HealthStatus": "UNKNOWN", "Attributes": { "AWS_INSTANCE_IPV4": "172.2.1.3", "AWS_INSTANCE_PORT": "808" } } ], "InstancesRevision": 85648075627387284 }`For more information, see [AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To discover instances from a specific owner account**The following `discover-instances`example discovers registered instances from a specific owner account. This parameter is necessary to discover instances in namespaces that are shared with your account.`aws servicediscovery discover-instances \ --namespace-name``shared-namespace`\ --service-name`shared-service`\ --owner-account`123456789111`Output: `{ "Instances": [ { "InstanceId": "shared-instance-1234", "NamespaceName": "shared-namespace", "ServiceName": "shared-service", "HealthStatus": "HEALTHY", "Attributes": { "AWS_INSTANCE_IPV4": "203.0.113.75", "AWS_INSTANCE_PORT": "80" } } ], "InstancesRevision": 1234567890 }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)and[AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [DiscoverInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/discover-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instance`.

- **AWS CLI**
- 
            
                    **Example 1: To get the details of an instance**The following `get-instance`example gets the attributes of a service.`aws servicediscovery get-instance \ --service-id``srv-e4anhexample0004`--instance-id`i-abcd1234`Output: `{ "ResourceOwner": "123456789012", "Instance": { "Id": "arn:aws:servicediscovery:us-west-2:111122223333;:service/srv-e4anhexample0004", "Attributes": { "AWS_INSTANCE_IPV4": "192.0.2.44", "AWS_INSTANCE_PORT": "80", "color": "green", "region": "us-west-2", "stage": "beta" }, "CreatedByAccount": "123456789012" } }`For more information, see [AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To get the details of an instance using service ARN for shared namespaces**The following `get-instance`example gets the attributes of an instance using a service ARN instead of service ID. Specifying an ARN is required when getting details of instances associated with namespaces that are shared with your account. The instance returned in this example was registered by account`123456789111`in a namespace owned by account`123456789012`.`aws servicediscovery get-instance \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-p5zdwlg5uvvzjita`\ --instance-id`web-server-01`Output: `{ "ResourceOwner": "123456789012", "Instance": { "Id": "web-server-01", "Attributes": { "AWS_INSTANCE_IPV4": "203.0.113.15", "AWS_INSTANCE_PORT": "80" }, "CreatedByAccount": "123456789111" } }`For more information about cross-account namespace sharing, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [GetInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-instances-health-status`.

- **AWS CLI**
- 
            
                    **Example 1: To get the health status of instances associated with a service**The following `get-instances-health-status`example gets the health status of instances associated with the specified service.`aws servicediscovery get-instances-health-status \ --service-id``srv-e4anhexample0004`Output: `{ "Status": { "i-abcd1234": "HEALTHY", "i-abcd1235": "UNHEALTHY" } }`For more information, see [AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To get the health status of instances using service ARN for shared namespaces**The following `get-instances-health-status`example gets the health status of instances using a service ARN instead of service ID. Specifying an ARN is required when getting health status for instances associated with namespaces that are shared with the requester's account.`aws servicediscovery get-instances-health-status \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-p5zdwlg5uvvzjita`Output: `{ "Status": { "web-server-01": "HEALTHY", "web-server-02": "UNHEALTHY" } }`For more information, see [AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-instances.html)and[Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [GetInstancesHealthStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-instances-health-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-namespace`.

- **AWS CLI**
- 
            
                    **Example 1: To get the details of a namespace**The following `get-namespace`example retrieves information about the specified namespace.`aws servicediscovery get-namespace \ --id``ns-abcd1234xmpl5678`Output: `{ "Namespace": { "Id": "ns-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Name": "example-http.com", "Type": "HTTP", "Description": "Example.com AWS Cloud Map HTTP Namespace", "Properties": { "DnsProperties": {}, "HttpProperties": { "HttpName": "example-http.com" } }, "CreateDate": "2024-02-23T13:35:21.874000-06:00", "CreatorRequestId": "abcd1234-5678-90ab-cdef-xmpl12345678" } }`For more information, see [AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To get the details of a namespace using ARN**The following `get-namespace`example retrieves information about the specified namespace using its ARN. Specifying the ARN is necessary for retrieving details of a namespace shared with your account.`aws servicediscovery get-namespace \ --id``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678`Output: `{ "Namespace": { "Id": "ns-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Name": "example-http.com", "Type": "HTTP", "Description": "Example.com AWS Cloud Map HTTP Namespace", "Properties": { "DnsProperties": {}, "HttpProperties": { "HttpName": "example-http.com" } }, "CreateDate": "2024-02-23T13:35:21.874000-06:00", "CreatorRequestId": "abcd1234-5678-90ab-cdef-xmpl12345678" } }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [GetNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-operation`.

- **AWS CLI**
- 
            
                    **Example 1: To get the result of an operation**The following `get-operation`example gets the result of a namespace creation operation.`aws servicediscovery get-operation \ --operation-id``abcd1234xmpl5678abcd1234xmpl5678-abcd1234`Output: `{ "Operation": { "Id": "abcd1234xmpl5678abcd1234xmpl5678-abcd1234", "Type": "CREATE_NAMESPACE", "Status": "SUCCESS", "CreateDate": "2025-01-13T13:35:21.874000-06:00", "UpdateDate": "2025-01-13T13:36:02.469000-06:00", "Targets": { "NAMESPACE": "ns-abcd1234xmpl5678" } } }`For more information, see [Creating an AWS Cloud Map namespace to group application services](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-namespaces.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To get an operation from a specific owner account**The following `get-operation`example gets the result of an operation associated with a specific namespace owner account. This parameter is necessary to get the result of operations associated with namespaces shared with your account.`aws servicediscovery get-operation \ --operation-id``abcd1234xmpl5678abcd1234xmpl5678-abcd1234`\ --owner-account`123456789111`Output: `{ "Operation": { "Id": "abcd1234xmpl5678abcd1234xmpl5678-abcd1234", "OwnerAccount": "123456789111", "Type": "CREATE_NAMESPACE", "Status": "SUCCESS", "CreateDate": "2025-01-13T13:35:21.874000-06:00", "UpdateDate": "2025-01-13T13:36:02.469000-06:00", "Targets": { "NAMESPACE": "ns-abcd1234xmpl5678" } } }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [GetOperation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-operation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-attributes`.

- **AWS CLI**
- 
            
                    **Example 1: To get the attributes of a service**The following `get-service-attributes`example gets the attributes of a service.`aws servicediscovery get-service-attributes \ --service-id``srv-abcd1234xmpl5678`Output: `{ "ServiceAttributes": { "ServiceArn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Attributes": { "Port": "80" } } }`For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To get the attributes of a service using ARN**The following `get-service-attributes`example gets the attributes of a service using its ARN. Specifying an ARN is necessary for getting attributes of a service created in a namespace shared with your account.`aws servicediscovery get-service-attributes \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678`Output: `{ "ServiceAttributes": { "ServiceArn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Attributes": { "Port": "80" } } }`For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)and[Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [GetServiceAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service`.

- **AWS CLI**
- 
            
                    **Example 1: To get the settings of a service**The following `get-service`example gets the settings of a specified service.`aws servicediscovery get-service \ --id``srv-abcd1234xmpl5678`Output: `{ "Service": { "Id": "srv-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Name": "test-service", "NamespaceId": "ns-abcd1234xmpl5678", "DnsConfig": {}, "Type": "HTTP", "CreateDate": "2025-08-18T13:53:02.775000-05:00", "CreatorRequestId": "abcd1234-5678-90ab-cdef-xmpl12345678", "CreatedByAccount": "123456789012" } }`For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To get the settings of a service using ARN**The following `get-service`example gets the settings of a specified service using its ARN. Specifying the ARN is necessary when retrieving information about a service created in a namespace that is shared with your account. The caller account`123456789111`created the service in a namespace shared by account`123456789012`.`aws servicediscovery get-service \ --id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678`Output: `{ "Service": { "Id": "srv-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Name": "test-service", "NamespaceId": "ns-abcd1234xmpl5678", "DnsConfig": {}, "Type": "HTTP", "CreateDate": "2025-08-18T13:53:02.775000-05:00", "CreatorRequestId": "abcd1234-5678-90ab-cdef-xmpl12345678", "CreatedByAccount": "123456789111" } }`For more information, see [Creating an AWS Cloud Map service for an application component](https://docs.aws.amazon.com/cloud-map/latest/dg/creating-services.html)and[Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [GetService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/get-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-instances`.

- **AWS CLI**
- 
            
                    **Example 1: To list service instances**The following `list-instances`example lists service instances.`aws servicediscovery list-instances \ --service-id``srv-qzpwvt2tfqcegapy`Output: `{ "Instances": [ { "Id": "i-06bdabbae60f65a4e", "Attributes": { "AWS_INSTANCE_IPV4": "172.2.1.3", "AWS_INSTANCE_PORT": "808" }, "CreatedByAccount": "123456789012" } ], "ResourceOwner": "123456789012" }`For more information, see [Listing AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-instances.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To list service instances using service ARN**The following `list-instances`example lists service instances using a service ARN instead of service ID. Specifying an ARN is required when listing instances associated with namespaces that are shared with your account.`aws servicediscovery list-instances \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-p5zdwlg5uvvzjita`Output: `{ "ResourceOwner": "123456789012", "Instances": [ { "Id": "web-server-01", "Attributes": { "AWS_INSTANCE_IPV4": "203.0.113.15", "AWS_INSTANCE_PORT": "80" }, "CreatedByAccount": "123456789012" }, { "Id": "web-server-02", "Attributes": { "AWS_INSTANCE_IPV4": "203.0.113.16", "AWS_INSTANCE_PORT": "80" }, "CreatedByAccount": "123456789012" } ] }`For more information about cross-account namespace sharing, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)and[Listing AWS Cloud Map service instances](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-instances.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [ListInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-namespaces`.

- **AWS CLI**
- 
            
                    **Example 1: To list namespaces**The following `list-namespaces`example lists namespaces.`aws servicediscovery list-namespaces`Output: `{ "Namespaces": [ { "Id": "ns-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678", "ResourceOwner": "123456789012", "Name": "local", "Type": "DNS_PRIVATE", "Properties": { "DnsProperties": { "HostedZoneId": "Z06752353VBUDTC32S84S", "SOA": {} }, "HttpProperties": { "HttpName": "local" } }, "CreateDate": "2023-07-17T13:37:27.872000-05:00" }, { "Id": "ns-abcd1234xmpl9012", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl9012", "ResourceOwner": "123456789012", "Name": "My-second-namespace", "Type": "HTTP", "Description": "My second namespace", "Properties": { "DnsProperties": { "SOA": {} }, "HttpProperties": { "HttpName": "My-second-namespace" } }, "CreateDate": "2023-11-14T10:35:47.840000-06:00" } ] }`For more information, see [Listing AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-namespaces.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To list namespaces shared by other accounts**The following `list-namespaces`example lists namespaces that are shared with the caller account by other AWS accounts using the`RESOURCE_OWNER`filter.`aws servicediscovery list-namespaces \ --filters``Name=RESOURCE_OWNER,Values=OTHER_ACCOUNTS,Condition=EQ`Output: `{ "Namespaces": [ { "Id": "ns-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789111:namespace/ns-abcd1234xmpl5678", "ResourceOwner": "123456789111", "Name": "shared-namespace", "Type": "HTTP", "Description": "Namespace shared from another account", "Properties": { "DnsProperties": { "SOA": {} }, "HttpProperties": { "HttpName": "shared-namespace" } }, "CreateDate": "2025-01-13T13:35:21.874000-06:00" } ] }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [ListNamespaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-namespaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-operations`.

- **AWS CLI**
- 
            
                    **To list operations that meet the specified criteria**The following `list-operations`example lists operations that have a status of`PENDING`or`SUCCESS`.`aws servicediscovery list-operations \ --service-id``srv-e4anhexample0004`\ --filters`Name=STATUS,Condition=IN,Values=PENDING,SUCCESS`Output: `{ "Operations": [ { "Id": "76yy8ovhpdz0plmjzbsnqgnrqvpv2qdt-kexample", "Status": "SUCCESS" }, { "Id": "prysnyzpji3u2ciy45nke83x2zanl7yk-dexample", "Status": "SUCCESS" }, { "Id": "ko4ekftir7kzlbechsh7xvcdgcpk66gh-7example", "Status": "PENDING" } ] }`For more information, see [What is AWS Cloud Map?](https://docs.aws.amazon.com/cloud-map/latest/dg/what-is-cloud-map.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [ListOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-services`.

- **AWS CLI**
- 
            
                    **Example 1: To list services**The following `list-services`example lists services.`aws servicediscovery list-services`Output: `{ "Services": [ { "Id": "srv-p5zdwlg5uvvzjita", "Arn": "arn:aws:servicediscovery:us-west-2:123456789012:service/srv-p5zdwlg5uvvzjita", "Name": "myservice", "DnsConfig": { "RoutingPolicy": "MULTIVALUE", "DnsRecords": [ { "Type": "A", "TTL": 60 } ] }, "CreateDate": 1587081768.334 } ] }`For more information, see [Listing AWS Cloud Map services in a namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To list services created in shared namespaces**The following `list-services`example lists services that are created in namespaces shared with the caller account`123456789012`by other AWS accounts using the`RESOURCE_OWNER`filter.`aws servicediscovery list-services \ --filters``Name=RESOURCE_OWNER,Values=OTHER_ACCOUNTS,Condition=EQ`Output: `{ "Services": [ { "Id": "srv-abcd1234xmpl5678", "Arn": "arn:aws:servicediscovery:us-west-2:123456789111:service/srv-abcd1234xmpl5678", "ResourceOwner": "123456789111", "Name": "shared-service", "NamespaceId": "ns-abcd1234xmpl5678", "Type": "HTTP", "Description": "Service in shared namespace", "DnsConfig": {}, "CreateDate": "2025-01-13T13:35:21.874000-06:00", "CreatorRequestId": "abcd1234-5678-90ab-cdef-xmpl12345678", "CreatedByAccount": "123456789012" } ] }`For more information, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)and[Listing AWS Cloud Map services in a namespace](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-services.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [ListServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags associated with the specified resource**The following `list-tags-for-resource`example lists tags for the specified resource.`aws servicediscovery list-tags-for-resource \ --resource-arn``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e4anhexample0004`Output: `{ "Tags": [ { "Key": "Project", "Value": "Zeta" }, { "Key": "Department", "Value": "Engineering" } ] }`For more information, see [Tagging your AWS Cloud Map resources](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-instances.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-instance`.

- **AWS CLI**
- 
            
                    **Example 1: To register a service instance using service ID**The following `register-instance`example registers a service instance.`aws servicediscovery register-instance \ --service-id``srv-p5zdwlg5uvvzjita`\ --instance-id`myservice-53`\ --attributes=AWS_INSTANCE_IPV4=172.2.1.3,AWS_INSTANCE_PORT=808Output: `{ "OperationId": "4yejorelbukcjzpnr6tlmrghsjwpngf4-k95yg2u7" }`To confirm that the operation succeeded, you can run `get-operation`. For more information, see[get-operation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/get-operation.html).For more information about registering an instance, see [Registering a resource as an AWS Cloud Map service instance](https://docs.aws.amazon.com/cloud-map/latest/dg/registering-instances.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To register a service instance using service ARN**The following `register-instance`example registers a service instance using a service ARN. Specifying the ARN is required when registering instances in services that are shared with your account.`aws servicediscovery register-instance \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-p5zdwlg5uvvzjita`\ --instance-id`web-server-01`\ --attributes=AWS_INSTANCE_IPV4=203.0.113.15,AWS_INSTANCE_PORT=80Output: `{ "OperationId": "gv4g5meo7ndmkqjrhpn39wk42xmpl" }`For more information about cross-account namespace sharing, see [Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [RegisterInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/register-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To associate tags with the specified resource**The following `tag-resource`example associates a`Department`tag with the value`Engineering`with the specified namespace.`aws servicediscovery tag-resource \ --resource-arn``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e4anhexample0004`\ --tags`Key=Department,``Value=Engineering`This command produces no output. For more information, see [Tagging your AWS Cloud Map resources](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-instances.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from the specified resource**The following `untag-resource`example removes a`Department`tag from the specified namespace.`aws servicediscovery untag-resource \ --resource-arn``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-e4anhexample0004`\ --tag-keys`Department`This command produces no output. For more information, see [Tagging your AWS Cloud Map resources](https://docs.aws.amazon.com/cloud-map/latest/dg/listing-instances.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-http-namespace`.

- **AWS CLI**
- 
            
                    **Example 1: To update an HTTP namespace**The following `update-http-namespace`example updates the specified HTTP namespace's description.`aws servicediscovery update-http-namespace \ --id``ns-abcd1234xmpl5678`\ --updater-request-id`abcd1234-5678-90ab-cdef-xmpl12345678`\ --namespace Description="The updated namespace description."Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`To confirm that the operation succeeded, you can run `get-operation`. For more information, see[get-operation](https://docs.aws.amazon.com/cli/latest/reference/servicediscovery/get-operation.html).For more information, see [AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To update an HTTP namespace using ARN**The following `update-http-namespace`example updates the specified HTTP namespace using its ARN.`aws servicediscovery update-http-namespace \ --id``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678`\ --updater-request-id`abcd1234-5678-90ab-cdef-xmpl12345678`\ --namespace Description="The updated namespace description."Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`For more information, see [AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [UpdateHttpNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-http-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-instance-custom-health-status`.

- **AWS CLI**
- 
            
                    **Example 1: To update a custom health check**The following `update-instance-custom-health-status`example updates the status of the custom health check for the specified service and example service instance to`HEALTHY`.`aws servicediscovery update-instance-custom-health-status \ --service-id``srv-e4anhexample0004`\ --instance-id`example`\ --status`HEALTHY`This command produces no output. For more information, see [AWS Cloud Map service health check configuration](https://docs.aws.amazon.com/cloud-map/latest/dg/services-health-checks.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To update a custom health check using service ARN**The following `update-instance-custom-health-status`example updates the status of the custom health check using a service ARN. The ARN is required when updating health status for instances associated with namespaces that are shared with the your account.`aws servicediscovery update-instance-custom-health-status \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-p5zdwlg5uvvzjita`\ --instance-id`web-server-01`\ --status`HEALTHY`This command produces no output. For more information, see [AWS Cloud Map service health check configuration](https://docs.aws.amazon.com/cloud-map/latest/dg/services-health-checks.html)and[Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [UpdateInstanceCustomHealthStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-instance-custom-health-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-private-dns-namespace`.

- **AWS CLI**
- 
            
                    **Example 1: To update a private DNS namespace using ID**The following `update-private-dns-namespace`example updates the description of a private DNS namespace using namespace ID.`aws servicediscovery update-private-dns-namespace \ --id``ns-abcd1234xmpl5678`\ --updater-request-id`abcd1234-5678-90ab-cdef-xmpl12345678`\ --namespace Description="The updated namespace description."Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`To confirm that the operation succeeded, you can run `get-operation`.For more information, see [AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To update a private DNS namespace using ARN**The following `update-private-dns-namespace`example updates a private DNS namespace using its ARN.`aws servicediscovery update-private-dns-namespace \ --id``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678`\ --updater-request-id`abcd1234-5678-90ab-cdef-xmpl12345678`\ --namespace Description="The updated namespace description."Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`For more information, see [AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [UpdatePrivateDnsNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-private-dns-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-public-dns-namespace`.

- **AWS CLI**
- 
            
                    **Example 1: To update a public DNS namespace using ID**The following `update-public-dns-namespace`example updates the description of a public DNS namespace using its ID.`aws servicediscovery update-public-dns-namespace \ --id``ns-abcd1234xmpl5678`\ --updater-request-id`abcd1234-5678-90ab-cdef-xmpl12345678`\ --namespace Description="The updated namespace description."Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`To confirm that the operation succeeded, you can run `get-operation`.For more information, see [AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To update a public DNS namespace using ARN**The following `update-public-dns-namespace`example updates a public DNS namespace using its ARN.`aws servicediscovery update-public-dns-namespace \ --id``arn:aws:servicediscovery:us-west-2:123456789012:namespace/ns-abcd1234xmpl5678`\ --updater-request-id`abcd1234-5678-90ab-cdef-xmpl12345678`\ --namespace Description="The updated namespace description."Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`For more information, see [AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [UpdatePublicDnsNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-public-dns-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-service-attributes`.

- **AWS CLI**
- 
            
                    **Example 1: To update a service to add an attribute**The following `update-service-attributes`example updates the specified service to add a service attribute with a key`Port`and a value`80`.`aws servicediscovery update-service-attributes \ --service-id``srv-abcd1234xmpl5678`\ --attributes`Port=80`This command produces no output. For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To update a service attributes using ARN**The following `update-service-attributes`example updates a service using its ARN to add a service attribute. Specifying the ARN is necessary for adding attributes to services created in namespaces shared with your account.`aws servicediscovery update-service-attributes \ --service-id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678`\ --attributes`Port=80`This command produces no output. For more information, see [AWS Cloud Map services](https://docs.aws.amazon.com/cloud-map/latest/dg/working-with-services.html)and[Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [UpdateServiceAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-service`.

- **AWS CLI**
- 
            
                    **Example 1: To update a service**The following `update-service`example updates a service to update the`DnsConfig`and`HealthCheckConfig`settings.`aws servicediscovery update-service \ --id``srv-abcd1234xmpl5678`\ --service`"DnsConfig={DnsRecords=[{Type=A,TTL=60}]},HealthCheckConfig={Type=HTTP,ResourcePath=/,FailureThreshold=2}"`Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`To confirm that the operation succeeded, you can run `get-operation`.For more information about updating a service, see [Updating an AWS Cloud Map service](https://docs.aws.amazon.com/cloud-map/latest/dg/editing-services.html)in the*AWS Cloud Map Developer Guide*.**Example 2: To update a service using ARN**The following `update-service`example updates a service using its ARN. Specifying an ARN is necessary for services that are created in namespaces shared with your account.`aws servicediscovery update-service \ --id``arn:aws:servicediscovery:us-west-2:123456789012:service/srv-abcd1234xmpl5678`\ --service`"DnsConfig={DnsRecords=[{Type=A,TTL=60}]},HealthCheckConfig={Type=HTTP,ResourcePath=/,FailureThreshold=2}"`Output: `{ "OperationId": "abcd1234-5678-90ab-cdef-xmpl12345678" }`For more information about updating a service, see [Updating an AWS Cloud Map service](https://docs.aws.amazon.com/cloud-map/latest/dg/editing-services.html)and[Shared AWS Cloud Map namespaces](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html)in the*AWS Cloud Map Developer Guide*.- 
                    For API details, see [UpdateService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicediscovery/update-service.html)in*AWS CLI Command Reference*.
 
-