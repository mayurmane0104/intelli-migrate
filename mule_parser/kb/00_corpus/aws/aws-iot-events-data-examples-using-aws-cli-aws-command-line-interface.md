# AWS IoT Events-Data examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-events-data_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-events-data_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT Events-Data.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-put-message`.

- **AWS CLI**
- 
            
                    **To send messages (inputs) to AWS IoT Events**The following `batch-put-message`example sends a set of messages to the AWS IoT Events system. Each message payload is transformed into the input you specify (`inputName`) and ingested into any detectors that monitor that input. If multiple messages are sent, the order in which the messages are processed isn't guaranteed. To guarantee ordering, you must send messages one at a time and wait for a successful response.`aws iotevents-data batch-put-message \ --cli-binary-format``raw-in-base64-out`\ --cli-input-json`file://highPressureMessage.json`Contents of `highPressureMessage.json`:`{ "messages": [ { "messageId": "00001", "inputName": "PressureInput", "payload": "{\"motorid\": \"Fulton-A32\", \"sensorData\": {\"pressure\": 80, \"temperature\": 39} }" } ] }`Output: `{ "BatchPutMessageErrorEntries": [] }`For more information, see [BatchPutMessage](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-data-BatchPutMessage)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [BatchPutMessage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/batch-put-message.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-update-detector`.

- **AWS CLI**
- 
            
                    **To update a detector (instance)**The following `batch-update-detector`example updates the state, variable values, and timer settings of one or more detectors (instances) of a specified detector model.`aws iotevents-data batch-update-detector \ --cli-input-json``file://budFulton-A32.json`Contents of `budFulton-A32.json`:`{ "detectors": [ { "messageId": "00001", "detectorModelName": "motorDetectorModel", "keyValue": "Fulton-A32", "state": { "stateName": "Normal", "variables": [ { "name": "pressureThresholdBreached", "value": "0" } ], "timers": [ ] } } ] }`Output: `{ "batchUpdateDetectorErrorEntries": [] }`For more information, see [BatchUpdateDetector](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-data-BatchUpdateDetector)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [BatchUpdateDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/batch-update-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-detector-model`.

- **AWS CLI**
- 
            
                    **To create a detector model**The following `create-detector-model`example creates a detector model.`aws iotevents create-detector-model \ --cli-input-json``file://motorDetectorModel.json`Contents of `motorDetectorModel.json`:`{ "detectorModelName": "motorDetectorModel", "detectorModelDefinition": { "states": [ { "stateName": "Normal", "onEnter": { "events": [ { "eventName": "init", "condition": "true", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "0" } } ] } ] }, "onInput": { "transitionEvents": [ { "eventName": "Overpressurized", "condition": "$input.PressureInput.sensorData.pressure > 70", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "$variable.pressureThresholdBreached + 3" } } ], "nextState": "Dangerous" } ] } }, { "stateName": "Dangerous", "onEnter": { "events": [ { "eventName": "Pressure Threshold Breached", "condition": "$variable.pressureThresholdBreached > 1", "actions": [ { "sns": { "targetArn": "arn:aws:sns:us-east-1:123456789012:underPressureAction" } } ] } ] }, "onInput": { "events": [ { "eventName": "Overpressurized", "condition": "$input.PressureInput.sensorData.pressure > 70", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "3" } } ] }, { "eventName": "Pressure Okay", "condition": "$input.PressureInput.sensorData.pressure <= 70", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "$variable.pressureThresholdBreached - 1" } } ] } ], "transitionEvents": [ { "eventName": "BackToNormal", "condition": "$input.PressureInput.sensorData.pressure <= 70 && $variable.pressureThresholdBreached <= 1", "nextState": "Normal" } ] }, "onExit": { "events": [ { "eventName": "Normal Pressure Restored", "condition": "true", "actions": [ { "sns": { "targetArn": "arn:aws:sns:us-east-1:123456789012:pressureClearedAction" } } ] } ] } } ], "initialStateName": "Normal" }, "key": "motorid", "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole" }`Output: `{ "detectorModelConfiguration": { "status": "ACTIVATING", "lastUpdateTime": 1560796816.077, "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole", "creationTime": 1560796816.077, "detectorModelArn": "arn:aws:iotevents:us-west-2:123456789012:detectorModel/motorDetectorModel", "key": "motorid", "detectorModelName": "motorDetectorModel", "detectorModelVersion": "1" } }`For more information, see [CreateDetectorModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-CreateDetectorModel)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [CreateDetectorModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/create-detector-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-input`.

- **AWS CLI**
- 
            
                    **To create an input**The following `create-input`example creates an input.`aws iotevents create-input \ --cli-input-json``file://pressureInput.json`Contents of `pressureInput.json`:`{ "inputName": "PressureInput", "inputDescription": "Pressure readings from a motor", "inputDefinition": { "attributes": [ { "jsonPath": "sensorData.pressure" }, { "jsonPath": "motorid" } ] } }`Output: `{ "inputConfiguration": { "status": "ACTIVE", "inputArn": "arn:aws:iotevents:us-west-2:123456789012:input/PressureInput", "lastUpdateTime": 1560795312.542, "creationTime": 1560795312.542, "inputName": "PressureInput", "inputDescription": "Pressure readings from a motor" } }`For more information, see [CreateInput](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-CreateInput)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [CreateInput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/create-input.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-detector-model`.

- **AWS CLI**
- 
            
                    **To delete a detector model**The following `delete-detector-model`example deletes a detector model. Any active instances of the detector model are also deleted.`aws iotevents delete-detector-model \ --detector-model-name``motorDetectorModel*`This command produces no output. For more information, see [DeleteDetectorModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-DeleteDetectorModel)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [DeleteDetectorModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/delete-detector-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-input`.

- **AWS CLI**
- 
            
                    **To delete an input**The following `delete-input`example deletes an input.`aws iotevents delete-input \ --input-name``PressureInput`This command produces no output. For more information, see [DeleteInput](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-DeleteInput)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [DeleteInput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/delete-input.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-detector-model`.

- **AWS CLI**
- 
            
                    **To get information about a detector model**The following `describe-detector-model`example describes a detector model. If the`version`parameter is not specified, the command returns information about the latest version.`aws iotevents describe-detector-model \ --detector-model-name``motorDetectorModel`Output: `{ "detectorModel": { "detectorModelConfiguration": { "status": "ACTIVE", "lastUpdateTime": 1560796816.077, "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole", "creationTime": 1560796816.077, "detectorModelArn": "arn:aws:iotevents:us-west-2:123456789012:detectorModel/motorDetectorModel", "key": "motorid", "detectorModelName": "motorDetectorModel", "detectorModelVersion": "1" }, "detectorModelDefinition": { "states": [ { "onInput": { "transitionEvents": [ { "eventName": "Overpressurized", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "$variable.pressureThresholdBreached + 3" } } ], "condition": "$input.PressureInput.sensorData.pressure > 70", "nextState": "Dangerous" } ], "events": [] }, "stateName": "Normal", "onEnter": { "events": [ { "eventName": "init", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "0" } } ], "condition": "true" } ] }, "onExit": { "events": [] } }, { "onInput": { "transitionEvents": [ { "eventName": "BackToNormal", "actions": [], "condition": "$input.PressureInput.sensorData.pressure <= 70 && $variable.pressureThresholdBreached <= 1", "nextState": "Normal" } ], "events": [ { "eventName": "Overpressurized", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "3" } } ], "condition": "$input.PressureInput.sensorData.pressure > 70" }, { "eventName": "Pressure Okay", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "$variable.pressureThresholdBreached - 1" } } ], "condition": "$input.PressureInput.sensorData.pressure <= 70" } ] }, "stateName": "Dangerous", "onEnter": { "events": [ { "eventName": "Pressure Threshold Breached", "actions": [ { "sns": { "targetArn": "arn:aws:sns:us-east-1:123456789012:underPressureAction" } } ], "condition": "$variable.pressureThresholdBreached > 1" } ] }, "onExit": { "events": [ { "eventName": "Normal Pressure Restored", "actions": [ { "sns": { "targetArn": "arn:aws:sns:us-east-1:123456789012:pressureClearedAction" } } ], "condition": "true" } ] } } ], "initialStateName": "Normal" } } }`For more information, see [DescribeDetectorModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-DescribeDetectorModel)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [DescribeDetectorModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/describe-detector-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-detector`.

- **AWS CLI**
- 
            
                    **To get information about a detector (instance)**The following `describe-detector`example returns information about the specified detector (instance).`aws iotevents-data describe-detector \ --detector-model-name``motorDetectorModel`\ --key-value`"Fulton-A32"`Output: `{ "detector": { "lastUpdateTime": 1560797852.776, "creationTime": 1560797852.775, "state": { "variables": [ { "name": "pressureThresholdBreached", "value": "3" } ], "stateName": "Dangerous", "timers": [] }, "keyValue": "Fulton-A32", "detectorModelName": "motorDetectorModel", "detectorModelVersion": "1" } }`For more information, see [DescribeDetector](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-data-DescribeDetector)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [DescribeDetector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/describe-detector.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-input`.

- **AWS CLI**
- 
            
                    **To get information about an input**The following `describe-input`example retrieves the details of an input.`aws iotevents describe-input \ --input-name``PressureInput`Output: `{ "input": { "inputConfiguration": { "status": "ACTIVE", "inputArn": "arn:aws:iotevents:us-west-2:123456789012:input/PressureInput", "lastUpdateTime": 1560795312.542, "creationTime": 1560795312.542, "inputName": "PressureInput", "inputDescription": "Pressure readings from a motor" }, "inputDefinition": { "attributes": [ { "jsonPath": "sensorData.pressure" }, { "jsonPath": "motorid" } ] } } }`For more information, see [DescribeInput](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-DescribeInput)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [DescribeInput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/describe-input.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-logging-options`.

- **AWS CLI**
- 
            
                    **To get information about logging settings**The following `describe-logging-options`example retrieves the current AWS IoT Events logging options.`aws iotevents describe-logging-options`Output: `{ "loggingOptions": { "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole", "enabled": false, "level": "ERROR" } }`For more information, see [DescribeLoggingOptions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-DescribeLoggingOptions)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [DescribeLoggingOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/describe-logging-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-detector-model-versions`.

- **AWS CLI**
- 
            
                    **To get information about versions of a detector model**The following `list-detector-model-versions`example lists all the versions of a detector model. Only the metadata associated with each detector model version is returned.`aws iotevents list-detector-model-versions \ --detector-model-name``motorDetectorModel`Output: `{ "detectorModelVersionSummaries": [ { "status": "ACTIVE", "lastUpdateTime": 1560796816.077, "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole", "creationTime": 1560796816.077, "detectorModelArn": "arn:aws:iotevents:us-west-2:123456789012:detectorModel/motorDetectorModel", "detectorModelName": "motorDetectorModel", "detectorModelVersion": "1" } ] }`For more information, see [ListDetectorModelVersions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-ListDetectorModelVersions)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [ListDetectorModelVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/list-detector-model-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-detector-models`.

- **AWS CLI**
- 
            
                    **To get a list of your detector models**The following `list-detector-models`example lists the detector models you have created. Only the metadata associated with each detector model is returned.`aws iotevents list-detector-models`Output: `{ "detectorModelSummaries": [ { "detectorModelName": "motorDetectorModel", "creationTime": 1552072424.212 "detectorModelDescription": "Detect overpressure in a motor." } ] }`For more information, see [ListDetectorModels](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-ListDetectorModels)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [ListDetectorModels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/list-detector-models.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-detectors`.

- **AWS CLI**
- 
            
                    **To get a list of detectors for a detector model**The following `list-detectors`example lists detectors (the instances of a detector model).`aws iotevents-data list-detectors \ --detector-model-name``motorDetectorModel`Output: `{ "detectorSummaries": [ { "lastUpdateTime": 1558129925.2, "creationTime": 1552073155.527, "state": { "stateName": "Normal" }, "keyValue": "Fulton-A32", "detectorModelName": "motorDetectorModel", "detectorModelVersion": "1" } ] }`For more information, see [ListDetectors](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-ListDetectors)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [ListDetectors](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/list-detectors.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-inputs`.

- **AWS CLI**
- 
            
                    **To list inputs**The following `list-inputs`example lists the inputs that you've created.`aws iotevents list-inputs`Output: `{ "status": "ACTIVE", "inputArn": "arn:aws:iotevents:us-west-2:123456789012:input/PressureInput", "lastUpdateTime": 1551742986.768, "creationTime": 1551742986.768, "inputName": "PressureInput", "inputDescription": "Pressure readings from a motor" }`For more information, see [ListInputs](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-ListInputs)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [ListInputs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/list-inputs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags assigned to a resource**The following `list-tags-for-resource`example lists the tags (metadata) you have assigned to the resource.`aws iotevents list-tags-for-resource \ --resource-arn``"arn:aws:iotevents:us-west-2:123456789012:input/PressureInput"`Output: `{ "tags": [ { "value": "motor", "key": "deviceType" } ] }`For more information, see [ListTagsForResource](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-ListTagsForResource)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-logging-options`.

- **AWS CLI**
- 
            
                    **To set logging options**The following `list-tags-for-resource`example sets or updates the AWS IoT Events logging options. If you update the value of any`loggingOptions`field, it takes up to one minute for the change to take effect. Also, if you change the policy attached to the role you specified in the`roleArn`field (for example, to correct an invalid policy) it takes up to five minutes for that change to take effect.`aws iotevents put-logging-options \ --cli-input-json``file://logging-options.json`Contents of `logging-options.json`:`{ "loggingOptions": { "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole", "level": "DEBUG", "enabled": true, "detectorDebugOptions": [ { "detectorModelName": "motorDetectorModel", "keyValue": "Fulton-A32" } ] } }`This command produces no output. For more information, see [PutLoggingOptions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-PutLoggingOptions)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [PutLoggingOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/put-logging-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to a resource**The following `tag-resource`example adds to or modifies the tags of the given resource. Tags are metadata that can be used to manage a resource.`aws iotevents tag-resource \ --cli-input-json``file://pressureInput.tag.json`Contents of `pressureInput.tag.json`:`{ "resourceArn": "arn:aws:iotevents:us-west-2:123456789012:input/PressureInput", "tags": [ { "key": "deviceType", "value": "motor" } ] }`This command produces no output. For more information, see [TagResource](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-TagResource)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a resource**The following `untag-resource`example removes the specified tags from the resource.`aws iotevents untag-resource \ --cli-input-json``file://pressureInput.untag.json`Contents of `pressureInput.untag.json`:`{ "resourceArn": "arn:aws:iotevents:us-west-2:123456789012:input/PressureInput", "tagKeys": [ "deviceType" ] }`This command produces no output. For more information, see [UntagResource](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-UntagResource)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-detector-model`.

- **AWS CLI**
- 
            
                    **To update a detector model**The following `update-detector-model`example updates a detector model. Detectors (instances) spawned by the previous version are deleted and then re-created as new inputs arrive.`aws iotevents update-detector-model \ --cli-input-json``file://motorDetectorModel.update.json`Contents of motorDetectorModel.update.json: `{ "detectorModelName": "motorDetectorModel", "detectorModelDefinition": { "states": [ { "stateName": "Normal", "onEnter": { "events": [ { "eventName": "init", "condition": "true", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "0" } } ] } ] }, "onInput": { "transitionEvents": [ { "eventName": "Overpressurized", "condition": "$input.PressureInput.sensorData.pressure > 70", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "$variable.pressureThresholdBreached + 3" } } ], "nextState": "Dangerous" } ] } }, { "stateName": "Dangerous", "onEnter": { "events": [ { "eventName": "Pressure Threshold Breached", "condition": "$variable.pressureThresholdBreached > 1", "actions": [ { "sns": { "targetArn": "arn:aws:sns:us-east-1:123456789012:underPressureAction" } } ] } ] }, "onInput": { "events": [ { "eventName": "Overpressurized", "condition": "$input.PressureInput.sensorData.pressure > 70", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "3" } } ] }, { "eventName": "Pressure Okay", "condition": "$input.PressureInput.sensorData.pressure <= 70", "actions": [ { "setVariable": { "variableName": "pressureThresholdBreached", "value": "$variable.pressureThresholdBreached - 1" } } ] } ], "transitionEvents": [ { "eventName": "BackToNormal", "condition": "$input.PressureInput.sensorData.pressure <= 70 && $variable.pressureThresholdBreached <= 1", "nextState": "Normal" } ] }, "onExit": { "events": [ { "eventName": "Normal Pressure Restored", "condition": "true", "actions": [ { "sns": { "targetArn": "arn:aws:sns:us-east-1:123456789012:pressureClearedAction" } } ] } ] } } ], "initialStateName": "Normal" }, "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole" }`Output: `{ "detectorModelConfiguration": { "status": "ACTIVATING", "lastUpdateTime": 1560799387.719, "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole", "creationTime": 1560799387.719, "detectorModelArn": "arn:aws:iotevents:us-west-2:123456789012:detectorModel/motorDetectorModel", "key": "motorid", "detectorModelName": "motorDetectorModel", "detectorModelVersion": "2" } }`For more information, see [UpdateDetectorModel](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-UpdateDetectorModel)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [UpdateDetectorModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/update-detector-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-input`.

- **AWS CLI**
- 
            
                    **To update an input**The following `update-input`example updates an input.`aws iotevents update-input \ --cli-input-json``file://pressureInput.json`Contents of `pressureInput.json`:`{ "inputName": "PressureInput", "inputDescription": "Pressure readings from a motor", "inputDefinition": { "attributes": [ { "jsonPath": "sensorData.pressure" }, { "jsonPath": "motorid" } ] } }`Output: `{ "inputConfiguration": { "status": "ACTIVE", "inputArn": "arn:aws:iotevents:us-west-2:123456789012:input/PressureInput", "lastUpdateTime": 1560795976.458, "creationTime": 1560795312.542, "inputName": "PressureInput", "inputDescription": "Pressure readings from a motor" } }`For more information, see [UpdateInput](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-commands.html#api-iotevents-UpdateInput)in the*AWS IoT Events Developer Guide**.- 
                    For API details, see [UpdateInput](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents-data/update-input.html)in*AWS CLI Command Reference*.
 
-