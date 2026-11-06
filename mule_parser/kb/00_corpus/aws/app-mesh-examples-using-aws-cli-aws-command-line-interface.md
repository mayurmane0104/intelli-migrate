# App Mesh examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_app-mesh_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_app-mesh_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with App Mesh.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-mesh`.

- **AWS CLI**
- 
            
                    **Example 1: To create a new service mesh**The following `create-mesh`example creates a service mesh.`aws appmesh create-mesh \ --mesh-name``app1`Output: `{ "mesh":{ "meshName":"app1", "metadata":{ "arn":"arn:aws:appmesh:us-east-1:123456789012:mesh/app1", "createdAt":1563809909.282, "lastUpdatedAt":1563809909.282, "uid":"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version":1 }, "spec":{}, "status":{ "status":"ACTIVE" } } }`**Example 2: To create a new service mesh with multiple tags**The following `create-mesh`example creates a service mesh with multiple tags.`aws appmesh create-mesh \ --mesh-name``app2`\ --tags`key=key1,value=value1``key=key2,value=value2``key=key3,value=value3`Output: `{ "mesh":{ "meshName":"app2", "metadata":{ "arn":"arn:aws:appmesh:us-east-1:123456789012:mesh/app2", "createdAt":1563822121.877, "lastUpdatedAt":1563822121.877, "uid":"a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version":1 }, "spec":{}, "status":{ "status":"ACTIVE" } } }`For more information, see [Service Meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [CreateMesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-mesh.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-route`.

- **AWS CLI**
- 
            
                    **To create a new gRPC route**The following `create-route`example uses a JSON input file to create a gRPC route. GRPC traffic that has metadata that starts with 123 is routed to a virtual node named serviceBgrpc. If there are specific gRPC, HTTP, or TCP failures when attempting to communicate with the target of the route, the route is retried three times. There is a 15 second delay between each retry attempt.`aws appmesh create-route \ --cli-input-json``file://create-route-grpc.json`Contents of `create-route-grpc.json`:`{ "meshName" : "apps", "routeName" : "grpcRoute", "spec" : { "grpcRoute" : { "action" : { "weightedTargets" : [ { "virtualNode" : "serviceBgrpc", "weight" : 100 } ] }, "match" : { "metadata" : [ { "invert" : false, "match" : { "prefix" : "123" }, "name" : "myMetadata" } ], "methodName" : "GetColor", "serviceName" : "com.amazonaws.services.ColorService" }, "retryPolicy" : { "grpcRetryEvents" : [ "deadline-exceeded" ], "httpRetryEvents" : [ "server-error", "gateway-error" ], "maxRetries" : 3, "perRetryTimeout" : { "unit" : "s", "value" : 15 }, "tcpRetryEvents" : [ "connection-error" ] } }, "priority" : 100 }, "virtualRouterName" : "serviceBgrpc" }`Output: `{ "route": { "meshName": "apps", "metadata": { "arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/apps/virtualRouter/serviceBgrpc/route/grpcRoute", "createdAt": 1572010806.008, "lastUpdatedAt": 1572010806.008, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "routeName": "grpcRoute", "spec": { "grpcRoute": { "action": { "weightedTargets": [ { "virtualNode": "serviceBgrpc", "weight": 100 } ] }, "match": { "metadata": [ { "invert": false, "match": { "prefix": "123" }, "name": "mymetadata" } ], "methodName": "GetColor", "serviceName": "com.amazonaws.services.ColorService" }, "retryPolicy": { "grpcRetryEvents": [ "deadline-exceeded" ], "httpRetryEvents": [ "server-error", "gateway-error" ], "maxRetries": 3, "perRetryTimeout": { "unit": "s", "value": 15 }, "tcpRetryEvents": [ "connection-error" ] } }, "priority": 100 }, "status": { "status": "ACTIVE" }, "virtualRouterName": "serviceBgrpc" } }`**To create a new HTTP or HTTP/2 route**The following `create-route`example uses a JSON input file to create an HTTP/2 route. To create an HTTP route, replace http2Route with httpRoute under spec. All HTTP/2 traffic addressed to any URL prefix that has a header value that starts with 123 is routed to a virtual node named serviceBhttp2. If there are specific HTTP or TCP failures when attempting to communicate with the target of the route, the route is retried three times. There is a 15 second delay between each retry attempt.`aws appmesh create-route \ --cli-input-json``file://create-route-http2.json`Contents of `create-route-http2.json`:`{ "meshName": "apps", "routeName": "http2Route", "spec": { "http2Route": { "action": { "weightedTargets": [ { "virtualNode": "serviceBhttp2", "weight": 100 } ] }, "match": { "headers": [ { "invert": false, "match": { "prefix": "123" }, "name": "clientRequestId" } ], "method": "POST", "prefix": "/", "scheme": "http" }, "retryPolicy": { "httpRetryEvents": [ "server-error", "gateway-error" ], "maxRetries": 3, "perRetryTimeout": { "unit": "s", "value": 15 }, "tcpRetryEvents": [ "connection-error" ] } }, "priority": 200 }, "virtualRouterName": "serviceBhttp2" }`Output: `{ "route": { "meshName": "apps", "metadata": { "arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/apps/virtualRouter/serviceBhttp2/route/http2Route", "createdAt": 1572011008.352, "lastUpdatedAt": 1572011008.352, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "routeName": "http2Route", "spec": { "http2Route": { "action": { "weightedTargets": [ { "virtualNode": "serviceBhttp2", "weight": 100 } ] }, "match": { "headers": [ { "invert": false, "match": { "prefix": "123" }, "name": "clientRequestId" } ], "method": "POST", "prefix": "/", "scheme": "http" }, "retryPolicy": { "httpRetryEvents": [ "server-error", "gateway-error" ], "maxRetries": 3, "perRetryTimeout": { "unit": "s", "value": 15 }, "tcpRetryEvents": [ "connection-error" ] } }, "priority": 200 }, "status": { "status": "ACTIVE" }, "virtualRouterName": "serviceBhttp2" } }`**To create a new TCP route**The following `create-route`example uses a JSON input file to create a TCP route. 75 percent of traffic is routed to a virtual node named serviceBtcp, and 25 percent of traffic is routed to a virtual node named serviceBv2tcp. Specifying different weightings for different targets is an effective way to do a deployment of a new version of an application. You can adjust the weights so that eventually, 100 percent of all traffic is routed to a target that has the new version of an application.`aws appmesh create-route \ --cli-input-json``file://create-route-tcp.json`Contents of create-route-tcp.json: `{ "meshName": "apps", "routeName": "tcpRoute", "spec": { "priority": 300, "tcpRoute": { "action": { "weightedTargets": [ { "virtualNode": "serviceBtcp", "weight": 75 }, { "virtualNode": "serviceBv2tcp", "weight": 25 } ] } } }, "virtualRouterName": "serviceBtcp" }`Output: `{ "route": { "meshName": "apps", "metadata": { "arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/apps/virtualRouter/serviceBtcp/route/tcpRoute", "createdAt": 1572011436.26, "lastUpdatedAt": 1572011436.26, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "routeName": "tcpRoute", "spec": { "priority": 300, "tcpRoute": { "action": { "weightedTargets": [ { "virtualNode": "serviceBtcp", "weight": 75 }, { "virtualNode": "serviceBv2tcp", "weight": 25 } ] } } }, "status": { "status": "ACTIVE" }, "virtualRouterName": "serviceBtcp" } }`For more information, see [Routes](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [CreateRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-virtual-gateway`.

- **AWS CLI**
- 
            
                    **To create a new virtual gateway**The following `create-virtual-gateway`example uses a JSON input file to create a virtual gateway with a listener for HTTP using port 9080.`aws appmesh create-virtual-gateway \ --mesh-name``meshName`\ --virtual-gateway-name`virtualGatewayName`\ --cli-input-json`file://create-virtual-gateway.json`Contents of `create-virtual-gateway.json`:`{ "spec": { "listeners": [ { "portMapping": { "port": 9080, "protocol": "http" } } ] } }`Output: `{ "virtualGateway": { "meshName": "meshName", "metadata": { "arn": "arn:aws:appmesh:us-west-2:123456789012:mesh/meshName/virtualGateway/virtualGatewayName", "createdAt": "2022-04-06T10:42:42.015000-05:00", "lastUpdatedAt": "2022-04-06T10:42:42.015000-05:00", "meshOwner": "123456789012", "resourceOwner": "123456789012", "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "listeners": [ { "portMapping": { "port": 9080, "protocol": "http" } } ] }, "status": { "status": "ACTIVE" }, "virtualGatewayName": "virtualGatewayName" } }`For more information, see [Virtual Gateways](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_gateways.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [CreateVirtualGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-virtual-node`.

- **AWS CLI**
- 
            
                    **Example 1: To create a new virtual node that uses DNS for discovery**The following `create-virtual-node`example uses a JSON input file to create a virtual node that uses DNS for service discovery.`aws appmesh create-virtual-node \ --cli-input-json``file://create-virtual-node-dns.json`Contents of `create-virtual-node-dns.json`:`{ "meshName": "app1", "spec": { "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "dns": { "hostname": "serviceBv1.svc.cluster.local" } } }, "virtualNodeName": "vnServiceBv1" }`Output: `{ "virtualNode": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceBv1", "createdAt": 1563810019.874, "lastUpdatedAt": 1563810019.874, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "dns": { "hostname": "serviceBv1.svc.cluster.local" } } }, "status": { "status": "ACTIVE" }, "virtualNodeName": "vnServiceBv1" } }`**Example 2: To create a new virtual node that uses AWS Cloud Map for discovery**The following `create-virtual-node`example uses a JSON input file to create a virtual node that uses AWS Cloud Map for service discovery.`aws appmesh create-virtual-node \ --cli-input-json``file://create-virtual-node-cloud-map.json`Contents of `create-virtual-node-cloud-map.json`:`{ "meshName": "app1", "spec": { "backends": [ { "virtualService": { "virtualServiceName": "serviceA.svc.cluster.local" } } ], "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "awsCloudMap": { "attributes": [ { "key": "Environment", "value": "Testing" } ], "namespaceName": "namespace1", "serviceName": "serviceA" } } }, "virtualNodeName": "vnServiceA" }`Output: `{ "virtualNode": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceA", "createdAt": 1563810859.465, "lastUpdatedAt": 1563810859.465, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "backends": [ { "virtualService": { "virtualServiceName": "serviceA.svc.cluster.local" } } ], "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "awsCloudMap": { "attributes": [ { "key": "Environment", "value": "Testing" } ], "namespaceName": "namespace1", "serviceName": "serviceA" } } }, "status": { "status": "ACTIVE" }, "virtualNodeName": "vnServiceA" } }`For more information, see [Virtual Nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [CreateVirtualNode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-node.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-virtual-router`.

- **AWS CLI**
- 
            
                    **To create a new virtual router**The following `create-virtual-router`example uses a JSON input file to create a virtual router with a listener for HTTP using port 80.`aws appmesh create-virtual-router \ --cli-input-json``file://create-virtual-router.json`Contents of `create-virtual-router.json`:`{ "meshName": "app1", "spec": { "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ] }, "virtualRouterName": "vrServiceB" }`Output: `{ "virtualRouter": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB", "createdAt": 1563810546.59, "lastUpdatedAt": 1563810546.59, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ] }, "status": { "status": "ACTIVE" }, "virtualRouterName": "vrServiceB" } }`For more information, see [Virtual Routers](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [CreateVirtualRouter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-router.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-virtual-service`.

- **AWS CLI**
- 
            
                    **Example 1: To create a new virtual service with a virtual node provider**The following `create-virtual-service`example uses a JSON input file to create a virtual service with a virtual node provider.`aws appmesh create-virtual-service \ --cli-input-json``file://create-virtual-service-virtual-node.json`Contents of `create-virtual-service-virtual-node.json`:`{ "meshName": "app1", "spec": { "provider": { "virtualNode": { "virtualNodeName": "vnServiceA" } } }, "virtualServiceName": "serviceA.svc.cluster.local" }`Output: `{ "virtualService": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualService/serviceA.svc.cluster.local", "createdAt": 1563810859.474, "lastUpdatedAt": 1563810967.179, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 2 }, "spec": { "provider": { "virtualNode": { "virtualNodeName": "vnServiceA" } } }, "status": { "status": "ACTIVE" }, "virtualServiceName": "serviceA.svc.cluster.local" } }`For more information, see [Virtual Node](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)in the*AWS App Mesh User Guide*.**Example 2: To create a new virtual service with a virtual router provider**The following `create-virtual-service`example uses a JSON input file to create a virtual service with a virtual router provider.`aws appmesh create-virtual-service \ --cli-input-json``file://create-virtual-service-virtual-router.json`Contents of `create-virtual-service-virtual-router.json`:`{ "meshName": "app1", "spec": { "provider": { "virtualRouter": { "virtualRouterName": "vrServiceB" } } }, "virtualServiceName": "serviceB.svc.cluster.local" }`Output: `{ "virtualService": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualService/serviceB.svc.cluster.local", "createdAt": 1563908363.999, "lastUpdatedAt": 1563908363.999, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "provider": { "virtualRouter": { "virtualRouterName": "vrServiceB" } } }, "status": { "status": "ACTIVE" }, "virtualServiceName": "serviceB.svc.cluster.local" } }`For more information, see Virtual Services<https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html> in the *AWS App Mesh User Guide*- 
                    For API details, see [CreateVirtualService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-mesh`.

- **AWS CLI**
- 
            
                    **To delete a service mesh**The following `delete-mesh`example deletes the specified service mesh.`aws appmesh delete-mesh \ --mesh-name``app1`Output: `{ "mesh": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1", "createdAt": 1563809909.282, "lastUpdatedAt": 1563824981.248, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 2 }, "spec": { "egressFilter": { "type": "ALLOW_ALL" } }, "status": { "status": "DELETED" } } }`For more information, see [Service Meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DeleteMesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-mesh.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-route`.

- **AWS CLI**
- 
            
                    **To delete a route**The following `delete-route`example deletes the specified route.`aws appmesh delete-route \ --mesh-name``app1`\ --virtual-router-name`vrServiceB`\ --route-name`toVnServiceB-weighted`Output: `{ "route": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB/route/toVnServiceB-weighted", "createdAt": 1563811384.015, "lastUpdatedAt": 1563823915.936, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 3 }, "routeName": "toVnServiceB-weighted", "spec": { "httpRoute": { "action": { "weightedTargets": [ { "virtualNode": "vnServiceBv1", "weight": 80 }, { "virtualNode": "vnServiceBv2", "weight": 20 } ] }, "match": { "prefix": "/" } } }, "status": { "status": "DELETED" }, "virtualRouterName": "vrServiceB" } }`For more information, see [Routes](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DeleteRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-virtual-node`.

- **AWS CLI**
- 
            
                    **To delete a virtual node**The following `delete-virtual-node`example deletes the specified virtual node.`aws appmesh delete-virtual-node \ --mesh-name``app1`\ --virtual-node-name`vnServiceBv2`Output: `{ "virtualNode": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceBv2", "createdAt": 1563810117.297, "lastUpdatedAt": 1563824700.678, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 2 }, "spec": { "backends": [], "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "dns": { "hostname": "serviceBv2.svc.cluster.local" } } }, "status": { "status": "DELETED" }, "virtualNodeName": "vnServiceBv2" } }`For more information, see [Virtual Nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DeleteVirtualNode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-node.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-virtual-router`.

- **AWS CLI**
- 
            
                    **To delete a virtual router**The following `delete-virtual-router`example deletes the specified virtual router.`aws appmesh delete-virtual-router \ --mesh-name``app1`\ --virtual-router-name`vrServiceB`Output: `{ "virtualRouter": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB", "createdAt": 1563810546.59, "lastUpdatedAt": 1563824253.467, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 3 }, "spec": { "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ] }, "status": { "status": "DELETED" }, "virtualRouterName": "vrServiceB" } }`For more information, see [Virtual Routers](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DeleteVirtualRouter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-router.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-virtual-service`.

- **AWS CLI**
- 
            
                    **To delete a virtual service**The following `delete-virtual-service`example deletes the specified virtual service.`aws appmesh delete-virtual-service \ --mesh-name``app1`\ --virtual-service-name`serviceB.svc.cluster.local`Output: `{ "virtualService": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualService/serviceB.svc.cluster.local", "createdAt": 1563908363.999, "lastUpdatedAt": 1563913940.866, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 3 }, "spec": {}, "status": { "status": "DELETED" }, "virtualServiceName": "serviceB.svc.cluster.local" } }`For more information, see [Virtual Service](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DeleteVirtualService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-mesh`.

- **AWS CLI**
- 
            
                    **To describe a service mesh**The following `describe-mesh`example returns details about the specified service mesh.`aws appmesh describe-mesh \ --mesh-name``app1`Output: `{ "mesh": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1", "createdAt": 1563809909.282, "lastUpdatedAt": 1563809909.282, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": {}, "status": { "status": "ACTIVE" } } }`For more information, see [Service Meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DescribeMesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-mesh.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-route`.

- **AWS CLI**
- 
            
                    **To describe a route**The following `describe-route`example returns details about the specified route.`aws appmesh describe-route \ --mesh-name``app1`\ --virtual-router-name`vrServiceB`\ --route-name`toVnServiceB-weighted`Output: `{ "route": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB/route/toVnServiceB-weighted", "createdAt": 1563811384.015, "lastUpdatedAt": 1563811384.015, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "routeName": "toVnServiceB-weighted", "spec": { "httpRoute": { "action": { "weightedTargets": [ { "virtualNode": "vnServiceBv1", "weight": 90 }, { "virtualNode": "vnServiceBv2", "weight": 10 } ] }, "match": { "prefix": "/" } } }, "status": { "status": "ACTIVE" }, "virtualRouterName": "vrServiceB" } }`For more information, see [Routes](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DescribeRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-virtual-node`.

- **AWS CLI**
- 
            
                    **To describe a virtual node**The following `describe-virtual-node`example returns details about the specified virtual node.`aws appmesh describe-virtual-node \ --mesh-name``app1`\ --virtual-node-name`vnServiceBv1`Output: `{ "virtualNode": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceBv1", "createdAt": 1563810019.874, "lastUpdatedAt": 1563810019.874, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "backends": [], "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "dns": { "hostname": "serviceBv1.svc.cluster.local" } } }, "status": { "status": "ACTIVE" }, "virtualNodeName": "vnServiceBv1" } }`For more information, see [Virtual Nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DescribeVirtualNode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-node.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-virtual-router`.

- **AWS CLI**
- 
            
                    **To describe a virtual router**The following `describe-virtual-router`example returns details about the specified virtual router.`aws appmesh describe-virtual-router \ --mesh-name``app1`\ --virtual-router-name`vrServiceB`Output: `{ "virtualRouter": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB", "createdAt": 1563810546.59, "lastUpdatedAt": 1563810546.59, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "listeners": [ { "portMapping": { "port": 80, "protocol": "http" } } ] }, "status": { "status": "ACTIVE" }, "virtualRouterName": "vrServiceB" } }`For more information, see [Virtual Routers](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DescribeVirtualRouter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-router.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-virtual-service`.

- **AWS CLI**
- 
            
                    **To describe a virtual service**The following `describe-virtual-service`example returns details about the specified virtual service.`aws appmesh describe-virtual-service \ --mesh-name``app1`\ --virtual-service-name`serviceB.svc.cluster.local`Output: `{ "virtualService": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualService/serviceB.svc.cluster.local", "createdAt": 1563908363.999, "lastUpdatedAt": 1563908363.999, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 1 }, "spec": { "provider": { "virtualRouter": { "virtualRouterName": "vrServiceB" } } }, "status": { "status": "ACTIVE" }, "virtualServiceName": "serviceB.svc.cluster.local" } }`For more information, see [Virtual Services](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [DescribeVirtualService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-meshes`.

- **AWS CLI**
- 
            
                    **To list service meshes**The following `list-meshes`example lists all of the service meshes in the current AWS Region.`aws appmesh list-meshes`Output: `{ "meshes": [ { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1", "meshName": "app1" } ] }`For more information, see [Service Meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [ListMeshes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-meshes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-routes`.

- **AWS CLI**
- 
            
                    **To list routes**The following `list-routes`example lists all of the routes for the specified virtual router.`aws appmesh list-routes \ --mesh-name``app1`\ --virtual-router-name`vrServiceB`Output: `{ "routes": [ { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB/route/toVnServiceB", "meshName": "app1", "routeName": "toVnServiceB-weighted", "virtualRouterName": "vrServiceB" } ] }`For more information, see [Routes](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [ListRoutes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-routes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a resource**The following `list-tags-for-resource`example lists all of the tags assigned to the specified resource.`aws appmesh list-tags-for-resource \ --resource-arn``arn:aws:appmesh:us-east-1:123456789012:mesh/app1`Output: `{ "tags": [ { "key": "key1", "value": "value1" }, { "key": "key2", "value": "value2" }, { "key": "key3", "value": "value3" } ] }`- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-virtual-nodes`.

- **AWS CLI**
- 
            
                    **To list virtual nodes**The following `list-virtual-nodes`example lists all of the virtual nodes in the specified service mesh.`aws appmesh list-virtual-nodes \ --mesh-name``app1`Output: `{ "virtualNodes": [ { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceBv1", "meshName": "app1", "virtualNodeName": "vnServiceBv1" }, { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceBv2", "meshName": "app1", "virtualNodeName": "vnServiceBv2" } ] }`For more information, see [Virtual Nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [ListVirtualNodes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-nodes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-virtual-routers`.

- **AWS CLI**
- 
            
                    **To list virtual routers**The following `list-virtual-routers`example lists all of the virtual routers in the specified service mesh.`aws appmesh list-virtual-routers \ --mesh-name``app1`Output: `{ "virtualRouters": [ { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB", "meshName": "app1", "virtualRouterName": "vrServiceB" } ] }`For more information, see [Virtual Routers](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [ListVirtualRouters](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-routers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-virtual-services`.

- **AWS CLI**
- 
            
                    **To list virtual services**The following `list-virtual-services`example lists all of the virtual services in the specified service mesh.`aws appmesh list-virtual-services \ --mesh-name``app1`Output: `{ "virtualServices": [ { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualService/serviceA.svc.cluster.local", "meshName": "app1", "virtualServiceName": "serviceA.svc.cluster.local" }, { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualService/serviceB.svc.cluster.local", "meshName": "app1", "virtualServiceName": "serviceB.svc.cluster.local" } ] }`For more information, see [Virtual Services](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [ListVirtualServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example adds the tag`key1`with the value`value1`to the specified resource.`aws appmesh tag-resource \ --resource-arn``arn:aws:appmesh:us-east-1:123456789012:mesh/app1`\ --tags`key=key1,value=value1`This command produces no output. - 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To untag a resource**The following `untag-resource`example removes a tag with the key`key1`from the specified resource.`aws appmesh untag-resource \ --resource-arn``arn:aws:appmesh:us-east-1:123456789012:mesh/app1`\ --tag-keys`key1`This command produces no output. - 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-mesh`.

- **AWS CLI**
- 
            
                    **To update a service mesh**The following `update-mesh`example uses a JSON input file to update a service mesh to allow all external egress traffic to be forwarded through the Envoy proxy untouched.`aws appmesh update-mesh \ --cli-input-json``file://update-mesh.json`Contents of `update-mesh.json`:`{ "meshName": "app1", "spec": { "egressFilter": { "type": "ALLOW_ALL" } } }`Output: `{ "mesh": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1", "createdAt": 1563809909.282, "lastUpdatedAt": 1563812829.687, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 2 }, "spec": { "egressFilter": { "type": "ALLOW_ALL" } }, "status": { "status": "ACTIVE" } } }`For more information, see [Service Meshes](https://docs.aws.amazon.com/app-mesh/latest/userguide/meshes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [UpdateMesh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-mesh.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-route`.

- **AWS CLI**
- 
            
                    **To update a route**The following `update-route`example uses a JSON input file to update the weights for a route.`aws appmesh update-route \ --cli-input-json``file://update-route-weighted.json`Contents of `update-route-weighted.json`:`{ "meshName": "app1", "routeName": "toVnServiceB-weighted", "spec": { "httpRoute": { "action": { "weightedTargets": [ { "virtualNode": "vnServiceBv1", "weight": 80 }, { "virtualNode": "vnServiceBv2", "weight": 20 } ] }, "match": { "prefix": "/" } } }, "virtualRouterName": "vrServiceB" }`Output: `{ "route": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB/route/toVnServiceB-weighted", "createdAt": 1563811384.015, "lastUpdatedAt": 1563819600.022, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 2 }, "routeName": "toVnServiceB-weighted", "spec": { "httpRoute": { "action": { "weightedTargets": [ { "virtualNode": "vnServiceBv1", "weight": 80 }, { "virtualNode": "vnServiceBv2", "weight": 20 } ] }, "match": { "prefix": "/" } } }, "status": { "status": "ACTIVE" }, "virtualRouterName": "vrServiceB" } }`For more information, see [Routes](https://docs.aws.amazon.com/app-mesh/latest/userguide/routes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [UpdateRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-virtual-node`.

- **AWS CLI**
- 
            
                    **To update a virtual node**The following `update-virtual-node`example uses a JSON input file to add a health check to a virtual node.`aws appmesh update-virtual-node \ --cli-input-json``file://update-virtual-node.json`Contents of `update-virtual-node.json`:`{ "clientToken": "500", "meshName": "app1", "spec": { "listeners": [ { "healthCheck": { "healthyThreshold": 5, "intervalMillis": 10000, "path": "/", "port": 80, "protocol": "http", "timeoutMillis": 3000, "unhealthyThreshold": 3 }, "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "dns": { "hostname": "serviceBv1.svc.cluster.local" } } }, "virtualNodeName": "vnServiceBv1" }`Output: `{ "virtualNode": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualNode/vnServiceBv1", "createdAt": 1563810019.874, "lastUpdatedAt": 1563819234.825, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 2 }, "spec": { "listeners": [ { "healthCheck": { "healthyThreshold": 5, "intervalMillis": 10000, "path": "/", "port": 80, "protocol": "http", "timeoutMillis": 3000, "unhealthyThreshold": 3 }, "portMapping": { "port": 80, "protocol": "http" } } ], "serviceDiscovery": { "dns": { "hostname": "serviceBv1.svc.cluster.local" } } }, "status": { "status": "ACTIVE" }, "virtualNodeName": "vnServiceBv1" } }`For more information, see [Virtual Nodes](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_nodes.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [UpdateVirtualNode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-node.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-virtual-router`.

- **AWS CLI**
- 
            
                    **To update a virtual router**The following `update-virtual-router`example uses a JSON input file to update a virtual router listener port.`aws appmesh update-virtual-router \ --cli-input-json``file://update-virtual-router.json`Contents of `update-virtual-router.json`:`{ "meshName": "app1", "spec": { "listeners": [ { "portMapping": { "port": 8080, "protocol": "http" } } ] }, "virtualRouterName": "vrServiceB" }`Output: `{ "virtualRouter": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualRouter/vrServiceB", "createdAt": 1563810546.59, "lastUpdatedAt": 1563819431.352, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 2 }, "spec": { "listeners": [ { "portMapping": { "port": 8080, "protocol": "http" } } ] }, "status": { "status": "ACTIVE" }, "virtualRouterName": "vrServiceB" } }`For more information, see [Virtual Routers](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_routers.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [UpdateVirtualRouter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-router.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-virtual-service`.

- **AWS CLI**
- 
            
                    **To update a virtual service**The following `update-virtual-service`example uses a JSON input file to update a virtual service to use a virtual router provider.`aws appmesh update-virtual-service \ --cli-input-json``file://update-virtual-service.json`Contents of `update-virtual-service.json`:`{ "meshName": "app1", "spec": { "provider": { "virtualRouter": { "virtualRouterName": "vrServiceA" } } }, "virtualServiceName": "serviceA.svc.cluster.local" }`Output: `{ "virtualService": { "meshName": "app1", "metadata": { "arn": "arn:aws:appmesh:us-east-1:123456789012:mesh/app1/virtualService/serviceA.svc.cluster.local", "createdAt": 1563810859.474, "lastUpdatedAt": 1563820257.411, "uid": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE", "version": 3 }, "spec": { "provider": { "virtualRouter": { "virtualRouterName": "vrServiceA" } } }, "status": { "status": "ACTIVE" }, "virtualServiceName": "serviceA.svc.cluster.local" } }`For more information, see [Virtual Services](https://docs.aws.amazon.com/app-mesh/latest/userguide/virtual_services.html)in the*AWS App Mesh User Guide*.- 
                    For API details, see [UpdateVirtualService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-service.html)in*AWS CLI Command Reference*.
 
-