# AWS IoT Greengrass V2 examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_greengrassv2_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_greengrassv2_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT Greengrass V2.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-service-role-to-account`.

- **AWS CLI**
- 
            
                    **To associate the Greengrass service role to your AWS account**The following `associate-service-role-to-account`example associates a service role with AWS IoT Greengrass for your AWS account.`aws greengrassv2 associate-service-role-to-account \ --role-arn``arn:aws:iam::123456789012:role/service-role/Greengrass_ServiceRole`Output: `{ "associatedAt": "2022-01-19T19:21:53Z" }`For more information, see [Greengrass service role](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [AssociateServiceRoleToAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/associate-service-role-to-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-associate-client-device-with-core-device`.

- **AWS CLI**
- 
            
                    **To associate client devices with a core device**The following `batch-associate-client-device-with-core-device`example associates two client devices with a core device.`aws greengrassv2 batch-associate-client-device-with-core-device \ --core-device-thing-name``MyGreengrassCore`\ --entries`thingName=MyClientDevice1``thingName=MyClientDevice2`Output: `{ "errorEntries": [] }`For more information, see [Interact with local IoT devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [BatchAssociateClientDeviceWithCoreDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/batch-associate-client-device-with-core-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-disassociate-client-device-from-core-device`.

- **AWS CLI**
- 
            
                    **To disassociate client devices from a core device**The following `batch-disassociate-client-device-from-core-device`example disassociates two client devices from a core device.`aws greengrassv2 batch-disassociate-client-device-from-core-device \ --core-device-thing-name``MyGreengrassCore`\ --entries`thingName=MyClientDevice1``thingName=MyClientDevice2`Output: `{ "errorEntries": [] }`For more information, see [Interact with local IoT devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [BatchDisassociateClientDeviceFromCoreDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/batch-disassociate-client-device-from-core-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-deployment`.

- **AWS CLI**
- 
            
                    **To cancel a deployment**The following `cancel-deployment`example stops a continuous deployment to a thing group.`aws greengrassv2 cancel-deployment \ --deployment-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "message": "SUCCESS" }`For more information, see [Cancel deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/cancel-deployments.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [CancelDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/cancel-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-component-version`.

- **AWS CLI**
- 
            
                    **Example 1: To create a component version from a recipe**The following `create-component-version`example creates a version of a Hello World component from a recipe file.`aws greengrassv2 create-component-version \ --inline-recipe``fileb://com.example.HelloWorld-1.0.0.json`Contents of `com.example.HelloWorld-1.0.0.json`:`{ "RecipeFormatVersion": "2020-01-25", "ComponentName": "com.example.HelloWorld", "ComponentVersion": "1.0.0", "ComponentDescription": "My first AWS IoT Greengrass component.", "ComponentPublisher": "Amazon", "ComponentConfiguration": { "DefaultConfiguration": { "Message": "world" } }, "Manifests": [ { "Platform": { "os": "linux" }, "Lifecycle": { "Run": "echo 'Hello {configuration:/Message}'" } } ] }`Output: `{ "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0", "componentName": "com.example.HelloWorld", "componentVersion": "1.0.0", "creationTimestamp": "2021-01-07T16:24:33.650000-08:00", "status": { "componentState": "REQUESTED", "message": "NONE", "errors": {} } }`For more information, see [Create custom components](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-components.html)and[Upload components to deploy](https://docs.aws.amazon.com/greengrass/v2/developerguide/upload-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.**Example 2: To create a component version from an AWS Lambda function**The following `create-component-version`example creates a version of a Hello World component from an AWS Lambda function.`aws greengrassv2 create-component-version \ --cli-input-json``file://lambda-function-component.json`Contents of `lambda-function-component.json`:`{ "lambdaFunction": { "lambdaArn": "arn:aws:lambda:us-west-2:123456789012:function:HelloWorldPythonLambda:1", "componentName": "com.example.HelloWorld", "componentVersion": "1.0.0", "componentLambdaParameters": { "eventSources": [ { "topic": "hello/world/+", "type": "IOT_CORE" } ] } } }`Output: `{ "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0", "componentName": "com.example.HelloWorld", "componentVersion": "1.0.0", "creationTimestamp": "2021-01-07T17:05:27.347000-08:00", "status": { "componentState": "REQUESTED", "message": "NONE", "errors": {} } }`For more information, see [Run AWS Lambda functions](https://docs.aws.amazon.com/greengrass/v2/developerguide/run-lambda-functions.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [CreateComponentVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/create-component-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-deployment`.

- **AWS CLI**
- 
            
                    **Example 1: To create a deployment**The following `create-deployment`example deploys the AWS IoT Greengrass Command Line Interface to a core device.`aws greengrassv2 create-deployment \ --cli-input-json``file://cli-deployment.json`Contents of `cli-deployment.json`:`{ "targetArn": "arn:aws:iot:us-west-2:123456789012:thing/MyGreengrassCore", "deploymentName": "Deployment for MyGreengrassCore", "components": { "aws.greengrass.Cli": { "componentVersion": "2.0.3" } }, "deploymentPolicies": { "failureHandlingPolicy": "DO_NOTHING", "componentUpdatePolicy": { "timeoutInSeconds": 60, "action": "NOTIFY_COMPONENTS" }, "configurationValidationPolicy": { "timeoutInSeconds": 60 } }, "iotJobConfiguration": {} }`Output: `{ "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html)in the*AWS IoT Greengrass V2 Developer Guide*.**Example 2: To create a deployment that updates component configurations**The following `create-deployment`example deploys the AWS IoT Greengrass nucleus component to a group of core devices. This deployment applies the following configuration updates for the nucleus component:Reset the target devices' proxy settings to their default no proxy settings.Reset the target devices' MQTT settings to their defaults.Sets the JVM options for the nucleus' JVM.Sets the logging level for the nucleus. `aws greengrassv2 create-deployment \ --cli-input-json``file://nucleus-deployment.json`Contents of `nucleus-deployment.json`:`{ "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup", "deploymentName": "Deployment for MyGreengrassCoreGroup", "components": { "aws.greengrass.Nucleus": { "componentVersion": "2.0.3", "configurationUpdate": { "reset": [ "/networkProxy", "/mqtt" ], "merge": "{\"jvmOptions\":\"-Xmx64m\",\"logging\":{\"level\":\"WARN\"}}" } } }, "deploymentPolicies": { "failureHandlingPolicy": "ROLLBACK", "componentUpdatePolicy": { "timeoutInSeconds": 60, "action": "NOTIFY_COMPONENTS" }, "configurationValidationPolicy": { "timeoutInSeconds": 60 } }, "iotJobConfiguration": {} }`Output: `{ "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "iotJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "iotJobArn": "arn:aws:iot:us-west-2:123456789012:job/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" }`For more information, see [Create deployments](https://docs.aws.amazon.com/greengrass/v2/developerguide/create-deployments.html)and[Update component configurations](https://docs.aws.amazon.com/greengrass/v2/developerguide/update-component-configurations.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [CreateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/create-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-component`.

- **AWS CLI**
- 
            
                    **To delete a component version**The following `delete-component`example deletes a Hello World component.`aws greengrassv2 delete-component \ --arn``arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0`This command produces no output. For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [DeleteComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/delete-component.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-core-device`.

- **AWS CLI**
- 
            
                    **To delete a core device**The following `delete-core-device`example deletes an AWS IoT Greengrass core device.`aws greengrassv2 delete-core-device \ --core-device-thing-name``MyGreengrassCore`This command produces no output. For more information, see [Uninstall the AWS IoT Greengrass Core software](https://docs.aws.amazon.com/greengrass/v2/developerguide/configure-greengrass-core-v2.html#uninstall-greengrass-core-v2)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [DeleteCoreDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/delete-core-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-component`.

- **AWS CLI**
- 
            
                    **To describe a component version**The following `describe-component`example describes a Hello World component.`aws greengrassv2 describe-component \ --arn``arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0`Output: `{ "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0", "componentName": "com.example.HelloWorld", "componentVersion": "1.0.0", "creationTimestamp": "2021-01-07T17:12:11.133000-08:00", "publisher": "Amazon", "description": "My first AWS IoT Greengrass component.", "status": { "componentState": "DEPLOYABLE", "message": "NONE", "errors": {} }, "platforms": [ { "attributes": { "os": "linux" } } ] }`For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [DescribeComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/describe-component.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-service-role-from-account`.

- **AWS CLI**
- 
            
                    **To disassociate the Greengrass service role from your AWS account**The following `disassociate-service-role-from-account`example disassociates the Greengrass service role from AWS IoT Greengrass for your AWS account.`aws greengrassv2 disassociate-service-role-from-account`Output: `{ "disassociatedAt": "2022-01-19T19:26:09Z" }`For more information, see [Greengrass service role](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [DisassociateServiceRoleFromAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/disassociate-service-role-from-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-component-version-artifact`.

- **AWS CLI**
- 
            
                    **To get a URL to download a component artifact**The following `get-component-version-artifact`example gets a URL to download the local debug console component's JAR file.`aws greengrassv2 get-component-version-artifact \ --arn``arn:aws:greengrass:us-west-2:aws:components:aws.greengrass.LocalDebugConsole:versions:2.0.3`\ --artifact-name`"Uvt6ZEzQ9TKiAuLbfXBX_APdY0TWks3uc46tHFHTzBM=/aws.greengrass.LocalDebugConsole.jar"`Output: `{ "preSignedUrl": "https://evergreencomponentmanageme-artifactbucket7410c9ef-g18n1iya8kwr.s3.us-west-2.amazonaws.com/public/aws.greengrass.LocalDebugConsole/2.0.3/s3/ggv2-component-releases-prod-pdx/EvergreenHttpDebugView/2ffc496ba41b39568968b22c582b4714a937193ee7687a45527238e696672521/aws.greengrass.LocalDebugConsole/aws.greengrass.LocalDebugConsole.jar?X-Amz-Security-Token=KwfLKSdEXAMPLE..." }`For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [GetComponentVersionArtifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-component-version-artifact.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-component`.

- **AWS CLI**
- 
            
                    **Example 1: To download a component's recipe in YAML format (Linux, macOS, or Unix)**The following `get-component`example downloads a Hello World component's recipe to a file in YAML format. This command does the following:Uses the `--output`and`--query`parameters to control the command's output. These parameters extract the recipe blob from the command's output. For more information about controlling output, see[Controlling Command Output](https://docs.aws.amazon.com/cli/latest/userguide/controlling-output.html)in the*AWS Command Line Interface User Guide*.Uses the`base64`utility. This utility decodes the extracted blob to the original text. The blob that is returned by a successful`get-component`command is base64-encoded text. You must decode this blob to obtain the original text.Saves the decoded text to a file. The final section of the command (`> com.example.HelloWorld-1.0.0.json`) saves the decoded text to a file.`aws greengrassv2 get-component \ --arn``arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0`\ --recipe-output-format`YAML`\ --query`recipe`\ --output`text``|``base64`--decode`>``com.example.HelloWorld-1.0.0.json`For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.**Example 2: To download a component's recipe in YAML format (Windows CMD)**The following `get-component`example downloads a Hello World component's recipe to a file in YAML format. This command uses the`certutil`utility.`aws greengrassv2 get-component``^`--arn`arn:aws:greengrass:us-west-2:675946970638:components:com.example.HelloWorld:versions:1.0.0``^`--recipe-output-format`YAML``^`--query`recipe``^`--output`text``>``com.example.HelloWorld-1.0.0.yaml.b64``certutil``-decode``com.example.HelloWorld-1.0.0.yaml.b64``com.example.HelloWorld-1.0.0.yaml`For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.**Example 3: To download a component's recipe in YAML format (Windows PowerShell)**The following `get-component`example downloads a Hello World component's recipe to a file in YAML format. This command uses the`certutil`utility.`aws greengrassv2 get-component````--arn`arn:aws:greengrass:us-west-2:675946970638:components:com.example.HelloWorld:versions:1.0.0````--recipe-output-format`YAML````--query`recipe````--output`text``>``com.example.HelloWorld-1.0.0.yaml.b64``certutil``-decode``com.example.HelloWorld-1.0.0.yaml.b64``com.example.HelloWorld-1.0.0.yaml`For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [GetComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-component.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-connectivity-info`.

- **AWS CLI**
- 
            
                    **To get the connectivity information for a Greengrass core device**The following `get-connectivity-info`example gets the connectivity information for a Greengrass core device. Client devices use this information to connect to the MQTT broker that runs on this core device.`aws greengrassv2 get-connectivity-info \ --thing-name``MyGreengrassCore`Output: `{ "connectivityInfo": [ { "id": "localIP_192.0.2.0", "hostAddress": "192.0.2.0", "portNumber": 8883 } ] }`For more information, see [Manage core device endpoints](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-core-device-endpoints.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [GetConnectivityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-connectivity-info.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-core-device`.

- **AWS CLI**
- 
            
                    **To get a core device**The following `get-core-device`example gets information about an AWS IoT Greengrass core device.`aws greengrassv2 get-core-device \ --core-device-thing-name``MyGreengrassCore`Output: `{ "coreDeviceThingName": "MyGreengrassCore", "coreVersion": "2.0.3", "platform": "linux", "architecture": "amd64", "status": "HEALTHY", "lastStatusUpdateTimestamp": "2021-01-08T04:57:58.838000-08:00", "tags": {} }`For more information, see [Check core device status](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-status.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [GetCoreDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-core-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment`.

- **AWS CLI**
- 
            
                    **To get a deployment**The following `get-deployment`example gets information about the deployment of the AWS IoT Greengrass nucleus component to a group of core devices.`aws greengrassv2 get-deployment \ --deployment-id``a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup", "revisionId": "14", "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "deploymentName": "Deployment for MyGreengrassCoreGroup", "deploymentStatus": "ACTIVE", "iotJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "iotJobArn": "arn:aws:iot:us-west-2:123456789012:job/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "components": { "aws.greengrass.Nucleus": { "componentVersion": "2.0.3", "configurationUpdate": { "merge": "{\"jvmOptions\":\"-Xmx64m\",\"logging\":{\"level\":\"WARN\"}}", "reset": [ "/networkProxy", "/mqtt" ] } } }, "deploymentPolicies": { "failureHandlingPolicy": "ROLLBACK", "componentUpdatePolicy": { "timeoutInSeconds": 60, "action": "NOTIFY_COMPONENTS" }, "configurationValidationPolicy": { "timeoutInSeconds": 60 } }, "iotJobConfiguration": {}, "creationTimestamp": "2021-01-07T17:21:20.691000-08:00", "isLatestForTarget": false, "tags": {} }`For more information, see [Deploy components to devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [GetDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-role-for-account`.

- **AWS CLI**
- 
            
                    **To get the Greengrass service role for your AWS account**The following `get-service-role-for-account`example gets the service role that's associated with AWS IoT Greengrass for your AWS account.`aws greengrassv2 get-service-role-for-account`Output: `{ "associatedAt": "2022-01-19T19:21:53Z", "roleArn": "arn:aws:iam::123456789012:role/service-role/Greengrass_ServiceRole" }`For more information, see [Greengrass service role](https://docs.aws.amazon.com/greengrass/v2/developerguide/greengrass-service-role.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [GetServiceRoleForAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/get-service-role-for-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-client-devices-associated-with-core-device`.

- **AWS CLI**
- 
            
                    **To list the client devices associated with a core device**The following `list-client-devices-associated-with-core-device`example lists all client devices associated with a core device.`aws greengrassv2 list-client-devices-associated-with-core-device \ --core-device-thing-name``MyTestGreengrassCore`Output: `{ "associatedClientDevices": [ { "thingName": "MyClientDevice2", "associationTimestamp": "2021-07-12T16:33:55.843000-07:00" }, { "thingName": "MyClientDevice1", "associationTimestamp": "2021-07-12T16:33:55.843000-07:00" } ] }`For more information, see [Interact with local IoT devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/interact-with-local-iot-devices.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListClientDevicesAssociatedWithCoreDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-client-devices-associated-with-core-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-component-versions`.

- **AWS CLI**
- 
            
                    **To list the versions of a component**The following `list-component-versions`example lists all versions of a Hello World component.`aws greengrassv2 list-component-versions \ --arn``arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld`Output: `{ "componentVersions": [ { "componentName": "com.example.HelloWorld", "componentVersion": "1.0.1", "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.1" }, { "componentName": "com.example.HelloWorld", "componentVersion": "1.0.0", "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.0" } ] }`For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListComponentVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-component-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-components`.

- **AWS CLI**
- 
            
                    **To list components**The following `list-components`example lists each component and its latest version defined in your AWS account in the current Region.`aws greengrassv2 list-components`Output: `{ "components": [ { "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld", "componentName": "com.example.HelloWorld", "latestVersion": { "arn": "arn:aws:greengrass:us-west-2:123456789012:components:com.example.HelloWorld:versions:1.0.1", "componentVersion": "1.0.1", "creationTimestamp": "2021-01-08T16:51:07.352000-08:00", "description": "My first AWS IoT Greengrass component.", "publisher": "Amazon", "platforms": [ { "attributes": { "os": "linux" } } ] } } ] }`For more information, see [Manage components](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-components.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListComponents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-components.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-core-devices`.

- **AWS CLI**
- 
            
                    **To list core devices**The following `list-core-devices`example lists the AWS IoT Greengrass core devices in your AWS account in the current Region.`aws greengrassv2 list-core-devices`Output: `{ "coreDevices": [ { "coreDeviceThingName": "MyGreengrassCore", "status": "HEALTHY", "lastStatusUpdateTimestamp": "2021-01-08T04:57:58.838000-08:00" } ] }`For more information, see [Check core device status](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-status.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListCoreDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-core-devices.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployments`.

- **AWS CLI**
- 
            
                    **To list deployments**The following `list-deployments`example lists the latest revision of each deployment defined in your AWS account in the current Region.`aws greengrassv2 list-deployments`Output: `{ "deployments": [ { "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup", "revisionId": "14", "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "deploymentName": "Deployment for MyGreengrassCoreGroup", "creationTimestamp": "2021-01-07T17:21:20.691000-08:00", "deploymentStatus": "ACTIVE", "isLatestForTarget": false }, { "targetArn": "arn:aws:iot:us-west-2:123456789012:thing/MyGreengrassCore", "revisionId": "1", "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "deploymentName": "Deployment for MyGreengrassCore", "creationTimestamp": "2021-01-06T16:10:42.407000-08:00", "deploymentStatus": "COMPLETED", "isLatestForTarget": false } ] }`For more information, see [Deploy components to devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-effective-deployments`.

- **AWS CLI**
- 
            
                    **To list deployment jobs**The following `list-effective-deployments`example lists the deployments that apply to an AWS IoT Greengrass core device.`aws greengrassv2 list-effective-deployments \ --core-device-thing-name``MyGreengrassCore`Output: `{ "effectiveDeployments": [ { "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "deploymentName": "Deployment for MyGreengrassCore", "iotJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "targetArn": "arn:aws:iot:us-west-2:123456789012:thing/MyGreengrassCore", "coreDeviceExecutionStatus": "COMPLETED", "reason": "SUCCESSFUL", "creationTimestamp": "2021-01-06T16:10:42.442000-08:00", "modifiedTimestamp": "2021-01-08T17:21:27.830000-08:00" }, { "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "deploymentName": "Deployment for MyGreengrassCoreGroup", "iotJobId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444", "iotJobArn": "arn:aws:iot:us-west-2:123456789012:job/a1b2c3d4-5678-90ab-cdef-EXAMPLE44444", "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup", "coreDeviceExecutionStatus": "SUCCEEDED", "reason": "SUCCESSFUL", "creationTimestamp": "2021-01-07T17:19:20.394000-08:00", "modifiedTimestamp": "2021-01-07T17:21:20.721000-08:00" } ] }`For more information, see [Check core device status](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-status.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListEffectiveDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-effective-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-installed-components`.

- **AWS CLI**
- 
            
                    **To list components installed on a core device**The following `list-installed-components`example lists the components that are installed on an AWS IoT Greengrass core device.`aws greengrassv2 list-installed-components \ --core-device-thing-name``MyGreengrassCore`Output: `{ "installedComponents": [ { "componentName": "aws.greengrass.Cli", "componentVersion": "2.0.3", "lifecycleState": "RUNNING", "isRoot": true }, { "componentName": "aws.greengrass.Nucleus", "componentVersion": "2.0.3", "lifecycleState": "FINISHED", "isRoot": true } ] }`For more information, see [Check core device status](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-status.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListInstalledComponents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-installed-components.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a resource**The following `list-tags-for-resource`example lists all tags for an AWS IoT Greengrass core device.`aws greengrassv2 list-tags-for-resource \ --resource-arn``arn:aws:greengrass:us-west-2:123456789012:coreDevices:MyGreengrassCore`Output: `{ "tags": { "Owner": "richard-roe" } }`For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to a resource**The following `tag-resource`example adds an owner tag to an AWS IoT Greengrass core device. You can use this tag to control access to the core device based on who owns it.`aws greengrassv2 tag-resource \ --resource-arn``arn:aws:greengrass:us-west-2:123456789012:coreDevices:MyGreengrassCore`\ --tags`Owner=richard-roe`This command produces no output. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resource`example removes an owner tag from an AWS IoT Greengrass core device.`aws iotsitewise untag-resource \ --resource-arn``arn:aws:greengrass:us-west-2:123456789012:coreDevices:MyGreengrassCore`\ --tag-keys`Owner`This command produces no output. For more information, see [Tag your resources](https://docs.aws.amazon.com/greengrass/v2/developerguide/tag-resources.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-connectivity-info`.

- **AWS CLI**
- 
            
                    **To update connectivity information for a Greengrass core device**The following `update-connectivity-info`example gets the connectivity information for a Greengrass core device. Client devices use this information to connect to the MQTT broker that runs on this core device.`aws greengrassv2 update-connectivity-info \ --thing-name``MyGreengrassCore`\ --cli-input-json`file://core-device-connectivity-info.json`Contents of `core-device-connectivity-info.json`:`{ "connectivityInfo": [ { "hostAddress": "192.0.2.0", "portNumber": 8883, "id": "localIP_192.0.2.0" } ] }`Output: `{ "version": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Manage core device endpoints](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-core-device-endpoints.html)in the*AWS IoT Greengrass V2 Developer Guide*.- 
                    For API details, see [UpdateConnectivityInfo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/update-connectivity-info.html)in*AWS CLI Command Reference*.
 
-