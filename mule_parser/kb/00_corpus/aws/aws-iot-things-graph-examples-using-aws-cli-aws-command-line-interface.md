# AWS IoT Things Graph examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iotthingsgraph_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iotthingsgraph_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT Things Graph.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-entity-to-thing`.

- **AWS CLI**
- 
            
                    **To associate a thing with a device**The following `associate-entity-to-thing`example associates a thing with a device. The example uses a motion sensor device that is in the public namespace.`aws iotthingsgraph associate-entity-to-thing \ --thing-name``"MotionSensorName"`\ --entity-id`"urn:tdm:aws/examples:Device:HCSR501MotionSensor"`This command produces no output. For more information, see [Creating and Uploading Models](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-models-gs.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [AssociateEntityToThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/associate-entity-to-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-flow-template`.

- **AWS CLI**
- 
            
                    **To create a flow**The following `create-flow-template`example creates a flow (workflow). The value of`MyFlowDefinition`is the GraphQL that models the flow.`aws iotthingsgraph create-flow-template \ --definition language=GRAPHQL,text="MyFlowDefinition"`Output: `{ "summary": { "createdAt": 1559248067.545, "id": "urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow", "revisionNumber": 1 } }`For more information, see [Working with Flows](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-workflows.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [CreateFlowTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-flow-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-system-instance`.

- **AWS CLI**
- 
            
                    **To create a system instance**The following `create-system-instance`example creates a system instance. The value of`MySystemInstanceDefinition`is the GraphQL that models the system instance.`aws iotthingsgraph create``-`system-instance -\ --definition language=GRAPHQL,text="MySystemInstanceDefinition" \ --target`CLOUD`\ --flow-actions-role-arn`myRoleARN`Output: `{ "summary": { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:Room218", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room218", "status": "NOT_DEPLOYED", "target": "CLOUD", "createdAt": 1559249315.208, "updatedAt": 1559249315.208 } }`For more information, see [Working with Systems and Flow Configurations](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [CreateSystemInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-system-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-system-template`.

- **AWS CLI**
- 
            
                    **To create a system**The following `create-system-template`example creates a system. The value of MySystemDefinition is the GraphQL that models the system.`aws iotthingsgraph create-system-template \ --definition language=GRAPHQL,text="MySystemDefinition"`Output: `{ "summary": { "createdAt": 1559249776.254, "id": "urn:tdm:us-west-2/123456789012/default:System:MySystem", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:System/default/MySystem", "revisionNumber": 1 } }`For more information, see [Creating Systems](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy-systems.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [CreateSystemTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/create-system-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-flow-template`.

- **AWS CLI**
- 
            
                    **To delete a flow**The following `delete-flow-template`example deletes a flow (workflow).`aws iotthingsgraph delete-flow-template \ --id``"urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow"`This command produces no output. For more information, see [Lifecycle Management for AWS IoT Things Graph Entities, Flows, Systems, and Deployments](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-lifecycle.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DeleteFlowTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-flow-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-namespace`.

- **AWS CLI**
- 
            
                    **To delete a namespace**The following `delete-namespace`example deletes a namespace.`aws iotthingsgraph delete-namespace`Output: `{ "namespaceArn": "arn:aws:iotthingsgraph:us-west-2:123456789012", "namespaceName": "us-west-2/123456789012/default" }`For more information, see [Lifecycle Management for AWS IoT Things Graph Entities, Flows, Systems, and Deployments](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-lifecycle.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DeleteNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-system-instance`.

- **AWS CLI**
- 
            
                    **To delete a system instance**The following `delete-system-instance`example deletes a system instance.`aws iotthingsgraph delete-system-instance \ --id``"urn:tdm:us-west-2/123456789012/default:Deployment:Room218"`This command produces no output. For more information, see [Lifecycle Management for AWS IoT Things Graph Entities, Flows, Systems, and Deployments](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-lifecycle.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DeleteSystemInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-system-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-system-template`.

- **AWS CLI**
- 
            
                    **To delete a system**The following `delete-system-template`example deletes a system.`aws iotthingsgraph delete-system-template \ --id``"urn:tdm:us-west-2/123456789012/default:System:MySystem"`This command produces no output. For more information, see [Lifecycle Management for AWS IoT Things Graph Entities, Flows, Systems, and Deployments](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-lifecycle.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DeleteSystemTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/delete-system-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deploy-system-instance`.

- **AWS CLI**
- 
            
                    **To deploy a system instance**The following `delete-system-template`example deploys a system instance.`aws iotthingsgraph deploy-system-instance \ --id``"urn:tdm:us-west-2/123456789012/default:Deployment:Room218"`Output: `{ "summary": { "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment:Room218", "createdAt": 1559249776.254, "id": "urn:tdm:us-west-2/123456789012/default:Deployment:Room218", "status": "DEPLOYED_IN_TARGET", "target": "CLOUD", "updatedAt": 1559249776.254 } }`For more information, see [Working with Systems and Flow Configurations](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DeploySystemInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deploy-system-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deprecate-flow-template`.

- **AWS CLI**
- 
            
                    **To deprecate a flow**The following `deprecate-flow-template`example deprecates a flow (workflow).`aws iotthingsgraph deprecate-flow-template \ --id``"urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow"`This command produces no output. For more information, see [Lifecycle Management for AWS IoT Things Graph Entities, Flows, Systems, and Deployments](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-lifecycle.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DeprecateFlowTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deprecate-flow-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deprecate-system-template`.

- **AWS CLI**
- 
            
                    **To deprecate a system**The following `deprecate-system-template`example deprecates a system.`aws iotthingsgraph deprecate-system-template \ --id``"urn:tdm:us-west-2/123456789012/default:System:MySystem"`This command produces no output. For more information, see [Lifecycle Management for AWS IoT Things Graph Entities, Flows, Systems, and Deployments](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-lifecycle.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DeprecateSystemTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/deprecate-system-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-namespace`.

- **AWS CLI**
- 
            
                    **To get a description of your namespace**The following `describe-namespace`example gets a description of your namespace.`aws iotthingsgraph describe-namespace`Output: `{ "namespaceName": "us-west-2/123456789012/default", "trackingNamespaceName": "aws", "trackingNamespaceVersion": 1, "namespaceVersion": 5 }`For more information, see [Namespaces](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-whatis-namespace.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DescribeNamespace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/describe-namespace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `dissociate-entity-from-thing`.

- **AWS CLI**
- 
            
                    **To dissociate a thing from a device**The following `dissociate-entity-from-thing`example dissociates a thing from a device.`aws iotthingsgraph dissociate-entity-from-thing \ --thing-name``"MotionSensorName"`\ --entity-type`"DEVICE"`This command produces no output. For more information, see [Creating and Uploading Models](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-models-gs.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [DissociateEntityFromThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/dissociate-entity-from-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-entities`.

- **AWS CLI**
- 
            
                    **To get definitions for entities**The following `get-entities`example gets a definition for a device model.`aws iotthingsgraph get-entities \ --ids``"urn:tdm:aws/examples:DeviceModel:MotionSensor"`Output: `{ "descriptions": [ { "id": "urn:tdm:aws/examples:DeviceModel:MotionSensor", "type": "DEVICE_MODEL", "createdAt": 1559256190.599, "definition": { "language": "GRAPHQL", "text": "##\n# Specification of motion sensor devices interface.\n##\ntype MotionSensor @deviceModel(id: \"urn:tdm:aws/examples:deviceModel:MotionSensor\",\n capability: \"urn:tdm:aws/examples:capability:MotionSensorCapability\") {ignore:void}" } } ] }`For more information, see [Creating and Uploading Models](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-models-gs.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-entities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-flow-template-revisions`.

- **AWS CLI**
- 
            
                    **To get revision information about a flow**The following `get-flow-template-revisions`example gets revision information about a flow (workflow).`aws iotthingsgraph get-flow-template-revisions \ --id``urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow`Output: `{ "summaries": [ { "id": "urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow", "revisionNumber": 1, "createdAt": 1559247540.292 } ] }`For more information, see [Working with Flows](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-workflows.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetFlowTemplateRevisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-flow-template-revisions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-flow-template`.

- **AWS CLI**
- 
            
                    **To get a flow definition**The following `get-flow-template`example gets a definition for a flow (workflow).`aws iotthingsgraph get-flow-template \ --id``"urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow"`Output: `{ "description": { "summary": { "id": "urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow", "revisionNumber": 1, "createdAt": 1559247540.292 }, "definition": { "language": "GRAPHQL", "text": "{\nquery MyFlow($camera: string!, $screen: string!) @workflowType(id: \"urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow\") @annotation(type: \"tgc:FlowEvent\", id: \"sledged790c1b2bcd949e09da0c9bfc077f79d\", x: 1586, y: 653) @triggers(definition: \"{MotionSensor(description: \\\"\\\") @position(x: 1045, y: 635.6666564941406) {\\n condition(expr: \\\"devices[name == \\\\\\\"motionSensor\\\\\\\"].events[name == \\\\\\\"StateChanged\\\\\\\"].lastEvent\\\")\\n action(expr: \\\"\\\")\\n}}\") {\n variables {\n cameraResult @property(id: \"urn:tdm:aws/examples:property:CameraStateProperty\")\n }\n steps {\n step(name: \"Camera\", outEvent: [\"sledged790c1b2bcd949e09da0c9bfc077f79d\"]) @position(x: 1377, y: 638.6666564941406) {\n DeviceActivity(deviceModel: \"urn:tdm:aws/examples:deviceModel:Camera\", out: \"cameraResult\", deviceId: \"${camera}\") {\n capture\n }\n }\n step(name: \"Screen\", inEvent: [\"sledged790c1b2bcd949e09da0c9bfc077f79d\"]) @position(x: 1675.6666870117188, y: 637.9999847412109) {\n DeviceActivity(deviceModel: \"urn:tdm:aws/examples:deviceModel:Screen\", deviceId: \"${screen}\") {\n display(imageUrl: \"${cameraResult.lastClickedImage}\")\n }\n }\n }\n}\n}" }, "validatedNamespaceVersion": 5 } }`For more information, see [Working with Flows](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-workflows.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetFlowTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-flow-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-namespace-deletion-status`.

- **AWS CLI**
- 
            
                    **To get the status of the namespace deletion task**The following `get-namespace-deletion-status`example gets the status of the namespace deletion task.`aws iotthingsgraph get-namespace-deletion-status`Output: `{ "namespaceArn": "arn:aws:iotthingsgraph:us-west-2:123456789012", "namespaceName": "us-west-2/123456789012/default" "status": "SUCCEEDED " }`For more information, see [Namespaces](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-whatis-namespace.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetNamespaceDeletionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-namespace-deletion-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-system-instance`.

- **AWS CLI**
- 
            
                    **To get a system instance**The following `get-system-instance`example gets a definition for a system instance.`aws iotthingsgraph get-system-instance \ --id``"urn:tdm:us-west-2/123456789012/default:Deployment:Room218"`Output: `{ "description": { "summary": { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:Room218", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room218", "status": "NOT_DEPLOYED", "target": "CLOUD", "createdAt": 1559249315.208, "updatedAt": 1559249315.208 }, "definition": { "language": "GRAPHQL", "text": "{\r\nquery Room218 @deployment(id: \"urn:tdm:us-west-2/123456789012/default:Deployment:Room218\", systemId: \"urn:tdm:us-west-2/123456789012/default:System:SecurityFlow\") {\r\n motionSensor(deviceId: \"MotionSensorName\")\r\n screen(deviceId: \"ScreenName\")\r\n camera(deviceId: \"CameraName\") \r\n triggers {MotionEventTrigger(description: \"a trigger\") { \r\n condition(expr: \"devices[name == 'motionSensor'].events[name == 'StateChanged'].lastEvent\") \r\n action(expr: \"ThingsGraph.startFlow('SecurityFlow', bindings[name == 'camera'].deviceId, bindings[name == 'screen'].deviceId)\")\r\n }\r\n }\r\n }\r\n }" }, "metricsConfiguration": { "cloudMetricEnabled": false }, "validatedNamespaceVersion": 5, "flowActionsRoleArn": "arn:aws:iam::123456789012:role/ThingsGraphRole" } }`For more information, see [Working with Systems and Flow Configurations](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetSystemInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-system-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-system-template-revisions`.

- **AWS CLI**
- 
            
                    **To get revision information about a system**The following `get-system-template-revisions`example gets revision information about a system.`aws iotthingsgraph get-system-template-revisions \ --id``"urn:tdm:us-west-2/123456789012/default:System:MySystem"`Output: `{ "summaries": [ { "id": "urn:tdm:us-west-2/123456789012/default:System:MySystem", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:System/default/MySystem", "revisionNumber": 1, "createdAt": 1559247540.656 } ] }`For more information, see [Working with Systems and Flow Configurations](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetSystemTemplateRevisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-system-template-revisions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-system-template`.

- **AWS CLI**
- 
            
                    **To get a system**The following `get-system-template`example gets a definition for a system.`aws iotthingsgraph get-system-template \ --id``"urn:tdm:us-west-2/123456789012/default:System:MySystem"`Output: `{ "description": { "summary": { "id": "urn:tdm:us-west-2/123456789012/default:System:MySystem", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:System/default/MyFlow", "revisionNumber": 1, "createdAt": 1559247540.656 }, "definition": { "language": "GRAPHQL", "text": "{\ntype MySystem @systemType(id: \"urn:tdm:us-west-2/123456789012/default:System:MySystem\", description: \"\") {\n camera: Camera @thing(id: \"urn:tdm:aws/examples:deviceModel:Camera\")\n screen: Screen @thing(id: \"urn:tdm:aws/examples:deviceModel:Screen\")\n motionSensor: MotionSensor @thing(id: \"urn:tdm:aws/examples:deviceModel:MotionSensor\")\n MyFlow: MyFlow @workflow(id: \"urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow\")\n}\n}" }, "validatedNamespaceVersion": 5 } }`For more information, see [Working with Systems and Flow Configurations](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetSystemTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-system-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-upload-status`.

- **AWS CLI**
- 
            
                    **To get the status of your entity upload**The following `get-upload-status`example gets the status of your entity upload operation. The value of`MyUploadId`is the ID value returned by the`upload-entity-definitions`operation.`aws iotthingsgraph get-upload-status \ --upload-id``"MyUploadId"`Output: `{ "namespaceName": "us-west-2/123456789012/default", "namespaceVersion": 5, "uploadId": "f6294f1e-b109-4bbe-9073-f451a2dda2da", "uploadStatus": "SUCCEEDED" }`For more information, see [Modeling Entities](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-modelmanagement.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [GetUploadStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/get-upload-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-flow-execution-messages`.

- **AWS CLI**
- 
            
                    **To get information about events in a flow execution**The following `list-flow-execution-messages`example gets information about events in a flow execution.`aws iotthingsgraph list-flow-execution-messages \ --flow-execution-id``"urn:tdm:us-west-2/123456789012/default:Workflow:SecurityFlow_2019-05-11T19:39:55.317Z_MotionSensor_69b151ad-a611-42f5-ac21-fe537f9868ad"`Output: `{ "messages": [ { "eventType": "EXECUTION_STARTED", "messageId": "f6294f1e-b109-4bbe-9073-f451a2dda2da", "payload": "Flow execution started", "timestamp": 1559247540.656 } ] }`For more information, see [Working with Flows](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-workflows.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [ListFlowExecutionMessages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/list-flow-execution-messages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list all tags for a resource**The following `list-tags-for-resource`example list all tags for an AWS IoT Things Graph resource.`aws iotthingsgraph list-tags-for-resource \ --resource-arn``"arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room218"`Output: `{ "tags": [ { "key": "Type", "value": "Residential" } ] }`For more information, see [Tagging Your AWS IoT Things Graph Resources](https://docs.aws.amazon.com/thingsgraph/latest/ug/tagging-tg.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-entities`.

- **AWS CLI**
- 
            
                    **To search for entities**The following `search-entities`example searches for all entities of type`EVENT`.`aws iotthingsgraph search-entities \ --entity-types``"EVENT"`Output: `{ "descriptions": [ { "id": "urn:tdm:aws/examples:Event:MotionSensorEvent", "type": "EVENT", "definition": { "language": "GRAPHQL", "text": "##\n# Description of events emitted by motion sensor.\n##\ntype MotionSensorEvent @eventType(id: \"urn:tdm:aws/examples:event:MotionSensorEvent\",\n payload: \"urn:tdm:aws/examples:property:MotionSensorStateProperty\") {ignore:void}" } }, { "id": "urn:tdm:us-west-2/123456789012/default:Event:CameraClickedEventV2", "type": "EVENT", "definition": { "language": "GRAPHQL", "text": "type CameraClickedEventV2 @eventType(id: \"urn:tdm:us-west-2/123456789012/default:event:CameraClickedEventV2\",\r\npayload: \"urn:tdm:aws:Property:Boolean\"){ignore:void}" } }, { "id": "urn:tdm:us-west-2/123456789012/default:Event:MotionSensorEventV2", "type": "EVENT", "definition": { "language": "GRAPHQL", "text": "# Event emitted by the motion sensor.\r\ntype MotionSensorEventV2 @eventType(id: \"urn:tdm:us-west-2/123456789012/default:event:MotionSensorEventV2\",\r\npayload: \"urn:tdm:us-west-2/123456789012/default:property:MotionSensorStateProperty2\") {ignore:void}" } } ], "nextToken": "urn:tdm:us-west-2/123456789012/default:Event:MotionSensorEventV2" }`For more information, see [AWS IoT Things Graph Data Model Reference](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-models.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [SearchEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-entities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-flow-executions`.

- **AWS CLI**
- 
            
                    **To search for flow executions**The following `search-flow-executions`example search for all executions of a flow in a specified system instance.`aws iotthingsgraph search-flow-executions \ --system-instance-id``"urn:tdm:us-west-2/123456789012/default:Deployment:Room218"`Output: `{ "summaries": [ { "createdAt": 1559247540.656, "flowExecutionId": "f6294f1e-b109-4bbe-9073-f451a2dda2da", "flowTemplateId": "urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow", "status": "RUNNING ", "systemInstanceId": "urn:tdm:us-west-2/123456789012/default:System:MySystem", "updatedAt": 1559247540.656 } ] }`For more information, see [Working with Systems and Flow Configurations](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [SearchFlowExecutions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-flow-executions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-flow-templates`.

- **AWS CLI**
- 
            
                    **To search for flows (or workflows)**The following `search-flow-templates`example searches for all flows (workflows) that contain the Camera device model.`aws iotthingsgraph search-flow-templates \ --filters name="DEVICE_MODEL_ID",value="urn:tdm:aws/examples:DeviceModel:Camera"`Output: `{ "summaries": [ { "id": "urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow", "revisionNumber": 1, "createdAt": 1559247540.292 }, { "id": "urn:tdm:us-west-2/123456789012/default:Workflow:SecurityFlow", "revisionNumber": 3, "createdAt": 1548283099.27 } ] }`For more information, see [Working with Flows](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-workflows.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [SearchFlowTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-flow-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-system-instances`.

- **AWS CLI**
- 
            
                    **To search for system instances**The following `search-system-instances`example searches for all system instances that contain the specified system.`aws iotthingsgraph search-system-instances \ --filters name="SYSTEM_TEMPLATE_ID",value="urn:tdm:us-west-2/123456789012/default:System:SecurityFlow"`Output: `{ "summaries": [ { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:DeploymentForSample", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/DeploymentForSample", "status": "NOT_DEPLOYED", "target": "GREENGRASS", "greengrassGroupName": "ThingsGraphGrnGr", "createdAt": 1555716314.707, "updatedAt": 1555716314.707 }, { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:MockDeployment", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/MockDeployment", "status": "DELETED_IN_TARGET", "target": "GREENGRASS", "greengrassGroupName": "ThingsGraphGrnGr", "createdAt": 1549416462.049, "updatedAt": 1549416722.361, "greengrassGroupId": "01d04b07-2a51-467f-9d03-0c90b3cdcaaf", "greengrassGroupVersionId": "7365aed7-2d3e-4d13-aad8-75443d45eb05" }, { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:MockDeployment2", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/MockDeployment2", "status": "DEPLOYED_IN_TARGET", "target": "GREENGRASS", "greengrassGroupName": "ThingsGraphGrnGr", "createdAt": 1549572385.774, "updatedAt": 1549572418.408, "greengrassGroupId": "01d04b07-2a51-467f-9d03-0c90b3cdcaaf", "greengrassGroupVersionId": "bfa70ab3-2bf7-409c-a4d4-bc8328ae5b86" }, { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:Room215", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room215", "status": "NOT_DEPLOYED", "target": "GREENGRASS", "greengrassGroupName": "ThingsGraphGG", "createdAt": 1547056918.413, "updatedAt": 1547056918.413 }, { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:Room218", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room218", "status": "NOT_DEPLOYED", "target": "CLOUD", "createdAt": 1559249315.208, "updatedAt": 1559249315.208 } ] }`For more information, see [Working with Systems and Flow Configurations](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [SearchSystemInstances](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-system-instances.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-system-templates`.

- **AWS CLI**
- 
            
                    **To search for system**The following `search-system-templates`example searches for all systems that contain the specified flow.`aws iotthingsgraph search-system-templates \ --filters name="FLOW_TEMPLATE_ID",value="urn:tdm:us-west-2/123456789012/default:Workflow:SecurityFlow"`Output: `{ "summaries": [ { "id": "urn:tdm:us-west-2/123456789012/default:System:SecurityFlow", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:System/default/SecurityFlow", "revisionNumber": 1, "createdAt": 1548283099.433 } ] }`For more information, see [Working with Flows](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-workflows.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [SearchSystemTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-system-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-things`.

- **AWS CLI**
- 
            
                    **To search for things associated with devices and device models**The following `search-things`example searches for all things that are associated with the HCSR501MotionSensor device.`aws iotthingsgraph search-things \ --entity-id``"urn:tdm:aws/examples:Device:HCSR501MotionSensor"`Output: `{ "things": [ { "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/MotionSensor1", "thingName": "MotionSensor1" }, { "thingArn": "arn:aws:iot:us-west-2:123456789012:thing/TG_MS", "thingName": "TG_MS" } ] }`For more information, see [Creating and Uploading Models](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-models-gs.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [SearchThings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/search-things.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To create a tag for a resource**The following `tag-resource`example creates a tag for the specified resource.`aws iotthingsgraph tag-resource \ --resource-arn``"arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room218"`\ --tags key="Type",value="Residential"This command produces no output. For more information, see [Tagging Your AWS IoT Things Graph Resources](https://docs.aws.amazon.com/thingsgraph/latest/ug/tagging-tg.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `undeploy-system-instance`.

- **AWS CLI**
- 
            
                    **To undeploy a system instance from its target**The following `undeploy-system-instance`example removes a system instance from its target.`aws iotthingsgraph undeploy-system-instance \ --id``"urn:tdm:us-west-2/123456789012/default:Deployment:Room215"`Output: `{ "summary": { "id": "urn:tdm:us-west-2/123456789012/default:Deployment:Room215", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room215", "status": "PENDING_DELETE", "target": "GREENGRASS", "greengrassGroupName": "ThingsGraphGrnGr", "createdAt": 1553189694.255, "updatedAt": 1559344549.601, "greengrassGroupId": "01d04b07-2a51-467f-9d03-0c90b3cdcaaf", "greengrassGroupVersionId": "731b371d-d644-4b67-ac64-3934e99b75d7" } }`For more information, see [Lifecycle Management for AWS IoT Things Graph Entities, Flows, Systems, and Deployments](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-lifecycle.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [UndeploySystemInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/undeploy-system-instance.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag for a resource**The following `untag-resource`example removes a tag for the specified resource.`aws iotthingsgraph untag-resource \ --resource-arn``"arn:aws:iotthingsgraph:us-west-2:123456789012:Deployment/default/Room218"`\ --tag-keys`"Type"`This command produces no output. For more information, see [Tagging Your AWS IoT Things Graph Resources](https://docs.aws.amazon.com/thingsgraph/latest/ug/tagging-tg.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-flow-template`.

- **AWS CLI**
- 
            
                    **To update a flow**The following `update-flow-template`example updates a flow (workflow). The value of`MyFlowDefinition`is the GraphQL that models the flow.`aws iotthingsgraph update-flow-template \ --id``"urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow"`\ --definition language=GRAPHQL,text="MyFlowDefinition"Output: `{ "summary": { "createdAt": 1559248067.545, "id": "urn:tdm:us-west-2/123456789012/default:Workflow:MyFlow", "revisionNumber": 2 } }`For more information, see [Working with Flows](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-workflows.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [UpdateFlowTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/update-flow-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-system-template`.

- **AWS CLI**
- 
            
                    **To update a system**The following `update-system-template`example updates a system. The value of`MySystemDefinition`is the GraphQL that models the system.`aws iotthingsgraph update-system-template \ --id``"urn:tdm:us-west-2/123456789012/default:System:MySystem"`\ --definition language=GRAPHQL,text="MySystemDefinition"Output: `{ "summary": { "createdAt": 1559249776.254, "id": "urn:tdm:us-west-2/123456789012/default:System:MySystem", "arn": "arn:aws:iotthingsgraph:us-west-2:123456789012:System/default/MySystem", "revisionNumber": 2 } }`For more information, see [Creating Systems](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-sysdeploy-systems.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [UpdateSystemTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/update-system-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-entity-definitions`.

- **AWS CLI**
- 
            
                    **To upload entity definitions**The following `upload-entity-definitions`example uploads entity definitions to your namespace. The value of`MyEntityDefinitions`is the GraphQL that models the entities.`aws iotthingsgraph upload-entity-definitions \ --document language=GRAPHQL,text="MyEntityDefinitions"`Output: `{ "uploadId": "f6294f1e-b109-4bbe-9073-f451a2dda2da" }`For more information, see [Modeling Entities](https://docs.aws.amazon.com/thingsgraph/latest/ug/iot-tg-modelmanagement.html)in the*AWS IoT Things Graph User Guide*.- 
                    For API details, see [UploadEntityDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotthingsgraph/upload-entity-definitions.html)in*AWS CLI Command Reference*.
 
-