# AWS IoT Wireless examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-wireless_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_iot-wireless_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS IoT Wireless.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-aws-account-with-partner-account`.

- **AWS CLI**
- 
            
                    **To associate a partner account with your AWS account**The following `associate-aws-account-with-partner-account`example associates the following Sidewalk account credentials with your AWS account.`aws iotwireless associate-aws-account-with-partner-account \ --sidewalk AmazonId="12345678901234",AppServerPrivateKey="a123b45c6d78e9f012a34cd5e6a7890b12c3d45e6f78a1b234c56d7e890a1234"`Output: `{ "Sidewalk": { "AmazonId": "12345678901234", "AppServerPrivateKey": "a123b45c6d78e9f012a34cd5e6a7890b12c3d45e6f78a1b234c56d7e890a1234" } }`For more information, see [Amazon Sidewalk Integration for AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AssociateAwsAccountWithPartnerAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-aws-account-with-partner-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-wireless-device-with-thing`.

- **AWS CLI**
- 
            
                    **To associate a thing to a wireless device**The following `associate-wireless-device-with-thing`example associates a thing to your wireless device that has the specified ID.`aws iotwireless associate-wireless-device-with-thing \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`\ --thing-arn`"arn:aws:iot:us-east-1:123456789012:thing/MyIoTWirelessThing"`This command produces no output. For more information, see [Add your gateways and wireless devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-devices.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AssociateWirelessDeviceWithThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-device-with-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-wireless-gateway-with-certificate`.

- **AWS CLI**
- 
            
                    **To associate the certificate with the wireless gateway**The following `associate-wireless-gateway-with-certificate`associates a wireless gateway with a certificate.`aws iotwireless associate-wireless-gateway-with-certificate \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`\ --iot-certificate-id`"a123b45c6d78e9f012a34cd5e6a7890b12c3d45e6f78a1b234c56d7e890a1234"`Output: `{ "IotCertificateId": "a123b45c6d78e9f012a34cd5e6a7890b12c3d45e6f78a1b234c56d7e890a1234" }`For more information, see [Add your gateways and wireless devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-devices.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AssociateWirelessGatewayWithCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-gateway-with-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-wireless-gateway-with-thing`.

- **AWS CLI**
- 
            
                    **To associate a thing to a wireless gateway**The following `associate-wireless-gateway-with-thing`example associates a thing to a wireless gateway.`aws iotwireless associate-wireless-gateway-with-thing \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`\ --thing-arn`"arn:aws:iot:us-east-1:123456789012:thing/MyIoTWirelessThing"`This command produces no output. For more information, see [Add your gateways and wireless devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-devices.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [AssociateWirelessGatewayWithThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/associate-wireless-gateway-with-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-destination`.

- **AWS CLI**
- 
            
                    **To create an IoT wireless destination**The following `create-destination`example creates a destination for mapping a device message to an AWS IoT rule. Before you run this command, you must have created an IAM role that gives AWS IoT Core for LoRaWAN the permissions necessary to send data to the AWS IoT rule.`aws iotwireless create-destination \ --name``IoTWirelessDestination`\ --expression-type`RuleName`\ --expression`IoTWirelessRule`\ --role-arn`arn:aws:iam::123456789012:role/IoTWirelessDestinationRole`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/IoTWirelessDestination", "Name": "IoTWirelessDestination" }`For more information, see [Add destinations to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-device-profile`.

- **AWS CLI**
- 
            
                    **To create a new device profile**The following `create-device-profile`example creates a new IoT wireless device profile.`aws iotwireless create-device-profile`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:123456789012:DeviceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d", "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d" }`For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateDeviceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-device-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service-profile`.

- **AWS CLI**
- 
            
                    **To create a new service profile**The following `create-service-profile`example creates a new IoT wireless service profile.`aws iotwireless create-service-profile`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:123456789012:ServiceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d", "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d" }`For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateServiceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-service-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-wireless-device`.

- **AWS CLI**
- 
            
                    **To create an IoT wireless device**The following `create-wireless-device`example creates a wireless device resource of the type LoRaWAN.`aws iotwireless create-wireless-device \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "Description": "My LoRaWAN wireless device" "DestinationName": "IoTWirelessDestination" "LoRaWAN": { "DeviceProfileId": "ab0c23d3-b001-45ef-6a01-2bc3de4f5333", "ServiceProfileId": "fe98dc76-cd12-001e-2d34-5550432da100", "OtaaV1_1": { "AppKey": "3f4ca100e2fc675ea123f4eb12c4a012", "JoinEui": "b4c231a359bc2e3d", "NwkKey": "01c3f004a2d6efffe32c4eda14bcd2b4" }, "DevEui": "ac12efc654d23fc2" }, "Name": "SampleIoTWirelessThing" "Type": LoRaWAN }`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/1ffd32c8-8130-4194-96df-622f072a315f", "Id": "1ffd32c8-8130-4194-96df-622f072a315f" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateWirelessDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-wireless-gateway-task-definition`.

- **AWS CLI**
- 
            
                    **To create a wireless gateway task definition**The following `create-wireless-gateway-task-definition`automatically creates tasks using this task definition for all gateways with the specified current version.`aws iotwireless create-wireless-gateway-task-definition \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "AutoCreateTasks": true, "Name": "TestAutoUpdate", "Update":{ "UpdateDataSource" : "s3://cupsalphagafirmwarebin/station", "UpdateDataRole" : "arn:aws:iam::001234567890:role/SDK_Test_Role", "LoRaWAN" :{ "CurrentVersion" :{ "PackageVersion" : "1.0.0", "Station" : "2.0.5", "Model" : "linux" }, "UpdateVersion" :{ "PackageVersion" : "1.0.1", "Station" : "2.0.5", "Model" : "minihub" } } } }`Output: `{ "Id": "b7d3baad-25c7-35e7-a4e1-1683a0d61da9" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateWirelessGatewayTaskDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway-task-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-wireless-gateway-task`.

- **AWS CLI**
- 
            
                    **To create the task for a wireless gateway**The following `create-wireless-gateway-task`example creates a task for a wireless gateway.`aws iotwireless create-wireless-gateway-task \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`\ --wireless-gateway-task-definition-id`"aa000102-0304-b0cd-ef56-a1b23cde456a"`Output: `{ "WirelessGatewayTaskDefinitionId": "aa204003-0604-30fb-ac82-a4f95aaf450a", "Status": "Success" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateWirelessGatewayTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-wireless-gateway`.

- **AWS CLI**
- 
            
                    **To create a wireless gateway**The following `create-wireless-gateway`example creates a wireless LoRaWAN device gateway.`aws iotwireless create-wireless-gateway \ --lorawan GatewayEui="a1b2c3d4567890ab",RfRegion="US915" \ --name``"myFirstLoRaWANGateway"`\ --description`"Using my first LoRaWAN gateway"`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessGateway/12345678-a1b2-3c45-67d8-e90fa1b2c34d", "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [CreateWirelessGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-destination`.

- **AWS CLI**
- 
            
                    **To delete an IoT wireless destination**The following `delete-destination`example deletes the wireless destination resource with the name`IoTWirelessDestination`that you created.`aws iotwireless delete-destination \ --name``"IoTWirelessDestination"`This command produces no output. For more information, see [Add destinations to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-device-profile`.

- **AWS CLI**
- 
            
                    **To delete a device profile**The following `delete-device-profile`example deletes a device profile with the specified ID that you created.`aws iotwireless delete-device-profile \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteDeviceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-device-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service-profile`.

- **AWS CLI**
- 
            
                    **To delete a service profile**The following `delete-service-profile`example deletes a service profile with the specified ID that you created.`aws iotwireless delete-service-profile \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteServiceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-service-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-wireless-device`.

- **AWS CLI**
- 
            
                    **To delete a wireless device**The following `delete-wireless-device`example deletes a wireless device that has the specified ID.`aws iotwireless delete-wireless-device \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteWirelessDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-wireless-gateway-task-definition`.

- **AWS CLI**
- 
            
                    **To delete a wireless gateway task definition**The following `delete-wireless-gateway-task-definition`example deletes the wireless gateway task definition that you created with the following ID.`aws iotwireless delete-wireless-gateway-task-definition \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteWirelessGatewayTaskDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-gateway-task-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-wireless-gateway-task`.

- **AWS CLI**
- 
            
                    **To delete a wireless gateway task**The following `delete-wireless-gateway-task`example deletes the wireless gateway task that has the specified ID.`aws iotwireless delete-wireless-gateway-task \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteWirelessGatewayTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-gateway-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-wireless-gateway`.

- **AWS CLI**
- 
            
                    **To delete a wireless gateway**The following `delete-wireless-gateway`example deletes a wireless gateway that has the specified ID.`aws iotwireless delete-wireless-gateway \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DeleteWirelessGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/delete-wireless-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-aws-account-from-partner-account`.

- **AWS CLI**
- 
            
                    **To disassociate the partner account from the AWS account**The following `disassociate-aws-account-from-partner-account`example disassociates a partner account from your currently associated AWS account.`aws iotwireless disassociate-aws-account-from-partner-account \ --partner-account-id``"12345678901234"`\ --partner-type`"Sidewalk"`This command produces no output. For more information, see [Add your gateways and wireless devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-devices.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DisassociateAwsAccountFromPartnerAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-aws-account-from-partner-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-wireless-device-from-thing`.

- **AWS CLI**
- 
            
                    **To disassociate the thing from the wireless device**The following `disassociate-wireless-device-from-thing`example disassociates a wireless device from its currently associated thing.`aws iotwireless disassociate-wireless-device-from-thing \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Add your gateways and wireless devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-devices.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DisassociateWirelessDeviceFromThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-device-from-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-wireless-gateway-from-certificate`.

- **AWS CLI**
- 
            
                    **To disassociate the certificate from the wireless gateway**The following `disassociate-wireless-gateway-from-certificate`disassociates a wireless gateway from its currently associated certificate.`aws iotwireless disassociate-wireless-gateway-from-certificate \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Add your gateways and wireless devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-devices.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DisassociateWirelessGatewayFromCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-gateway-from-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-wireless-gateway-from-thing`.

- **AWS CLI**
- 
            
                    **To disassociate the thing from the wireless gateway**The following `disassociate-wireless-gateway-from-thing`example disassociates a wireless gateway from its currently associated thing.`aws iotwireless disassociate-wireless-gateway-from-thing \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`This command produces no output. For more information, see [Add your gateways and wireless devices to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-onboard-devices.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [DisassociateWirelessGatewayFromThing](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/disassociate-wireless-gateway-from-thing.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-destination`.

- **AWS CLI**
- 
            
                    **To get information about an IoT wireless destination**The following `get-destination`example gets information about the destination resource with the name`IoTWirelessDestination`that you created.`aws iotwireless get-destination \ --name``"IoTWirelessDestination"`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/IoTWirelessDestination", "Name": "IoTWirelessDestination", "Expression": "IoTWirelessRule", "ExpressionType": "RuleName", "RoleArn": "arn:aws:iam::123456789012:role/IoTWirelessDestinationRole" }`For more information, see [Add destinations to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-device-profile`.

- **AWS CLI**
- 
            
                    **To get information about a device profile**The following `get-device-profile`example gets information about the device profile with the specified ID that you created.`aws iotwireless get-device-profile \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:123456789012:DeviceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d", "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d", "LoRaWAN": { "MacVersion": "1.0.3", "MaxDutyCycle": 10, "Supports32BitFCnt": false, "RegParamsRevision": "RP002-1.0.1", "SupportsJoin": true, "RfRegion": "US915", "MaxEirp": 13, "SupportsClassB": false, "SupportsClassC": false } }`For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetDeviceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-device-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-partner-account`.

- **AWS CLI**
- 
            
                    **To get the partner account information**The following `get-partner-account`example gets information about your Sidewalk account that has the following ID.`aws iotwireless get-partner-account \ --partner-account-id``"12345678901234"`\ --partner-type`"Sidewalk"`Output: `{ "Sidewalk": { "AmazonId": "12345678901234", "Fingerprint": "a123b45c6d78e9f012a34cd5e6a7890b12c3d45e6f78a1b234c56d7e890a1234" }, "AccountLinked": false }`For more information, see [Amazon Sidewalk Integration for AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetPartnerAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-partner-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-endpoint`.

- **AWS CLI**
- 
            
                    **To get the service endpoint**The following `get-service-endpoint`example gets the account-specific endpoint for CUPS protocol.`aws iotwireless get-service-endpoint`Output: `{ "ServiceType": "CUPS", "ServiceEndpoint": "https://A1RMKZ37ACAGOT.cups.lorawan.us-east-1.amazonaws.com:443", "ServerTrust": "-----BEGIN CERTIFICATE-----\n MIIESTCCAzGgAwIBAgITBn+UV4WH6Kx33rJTMlu8mYtWDTANBgkqhkiG9w0BAQsF\n ADA5MQswCQYDVQQGEwJVUzEPMA0GA1UEChMGQW1hem9uMRkwFwYDVQQDExBBbWF6\n b24gUm9vdCBDQSAxMB4XDTE1MTAyMjAwMDAwMFoXDTI1MTAxOTAwMDAwMFowRjEL\n MAkGA1UEBhMCVVMxDzANBgNVBAoTBkFtYXpvbjEVMBMGA1UECxMMU2VydmVyIENB\n IDFCMQ8wDQYDVQQDEwZBbWF6b24wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\n AoIBAQDCThZn3c68asg3Wuw6MLAd5tES6BIoSMzoKcG5blPVo+sDORrMd4f2AbnZ\n cMzPa43j4wNxhplty6aUKk4T1qe9BOwKFjwK6zmxxLVYo7bHViXsPlJ6qOMpFge5\n blDP+18x+B26A0piiQOuPkfyDyeR4xQghfj66Yo19V+emU3nazfvpFA+ROz6WoVm\n B5x+F2pV8xeKNR7u6azDdU5YVX1TawprmxRC1+WsAYmz6qP+z8ArDITC2FMVy2fw\n 0IjKOtEXc/VfmtTFch5+AfGYMGMqqvJ6LcXiAhqG5TI+Dr0RtM88k+8XUBCeQ8IG\n KuANaL7TiItKZYxK1MMuTJtV9IblAgMBAAGjggE7MIIBNzASBgNVHRMBAf8ECDAG\n AQH/AgEAMA4GA1UdDwEB/wQEAwIBhjAdBgNVHQ4EFgQUWaRmBlKge5WSPKOUByeW\n dFv5PdAwHwYDVR0jBBgwFoAUhBjMhTTsvAyUlC4IWZzHshBOCggwewYIKwYBBQUH\n AQEEbzBtMC8GCCsGAQUFBzABhiNodHRwOi8vb2NzcC5yb290Y2ExLmFtYXpvbnRy\n dXN0LmNvbTA6BggrBgEFBQcwAoYuaHR0cDovL2NydC5yb290Y2ExLmFtYXpvbnRy\n dXN0LmNvbS9yb290Y2ExLmNlcjA/BgNVHR8EODA2MDSgMqAwhi5odHRwOi8vY3Js\n LnJvb3RjYTEuYW1hem9udHJ1c3QuY29tL3Jvb3RjYTEuY3JsMBMGA1UdIAQMMAow\n CAYGZ4EMAQIBMA0GCSqGSIb3DQEBCwUAA4IBAQCFkr41u3nPo4FCHOTjY3NTOVI1\n 59Gt/a6ZiqyJEi+752+a1U5y6iAwYfmXss2lJwJFqMp2PphKg5625kXg8kP2CN5t\n 6G7bMQcT8C8xDZNtYTd7WPD8UZiRKAJPBXa30/AbwuZe0GaFEQ8ugcYQgSn+IGBI\n 8/LwhBNTZTUVEWuCUUBVV18YtbAiPq3yXqMB48Oz+ctBWuZSkbvkNodPLamkB2g1\n upRyzQ7qDn1X8nn8N8V7YJ6y68AtkHcNSRAnpTitxBKjtKPISLMVCx7i4hncxHZS\n yLyKQXhw2W2Xs0qLeC1etA+jTGDK4UfLeC0SF7FSi8o5LL21L8IzApar2pR/\n -----END CERTIFICATE-----\n" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetServiceEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-profile`.

- **AWS CLI**
- 
            
                    **To get information about a service profile**The following `get-service-profile`example gets information about the service profile with the specified ID that you created.`aws iotwireless get-service-profile \ --id``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`Output: `{ "Arn": "arn:aws:iotwireless:us-east-1:651419225604:ServiceProfile/538185bb-d7e7-4b95-96a0-c51aa4a5b9a0", "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d", "LoRaWAN": { "HrAllowed": false, "NwkGeoLoc": false, "DrMax": 15, "UlBucketSize": 4096, "PrAllowed": false, "ReportDevStatusBattery": false, "DrMin": 0, "DlRate": 60, "AddGwMetadata": false, "ReportDevStatusMargin": false, "MinGwDiversity": 1, "RaAllowed": false, "DlBucketSize": 4096, "DevStatusReqFreq": 24, "TargetPer": 5, "UlRate": 60 } }`For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetServiceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-service-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-device-statistics`.

- **AWS CLI**
- 
            
                    **To get operating information about a wireless device**The following `get-wireless-device-statistics`example gets operating information about a wireless device.`aws iotwireless get-wireless-device-statistics \ --wireless-device-id``"1ffd32c8-8130-4194-96df-622f072a315f"`Output: `{ "WirelessDeviceId": "1ffd32c8-8130-4194-96df-622f072a315f" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessDeviceStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-device-statistics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-device`.

- **AWS CLI**
- 
            
                    **To get information about the wireless device**The following `get-wireless-device`example lists the available widgets in your AWS account.`aws iotwireless get-wireless-device \ --identifier``"1ffd32c8-8130-4194-96df-622f072a315f"`\ --identifier-type`WirelessDeviceID`Output: `{ "Name": "myLoRaWANDevice", "ThingArn": "arn:aws:iot:us-east-1:123456789012:thing/44b87eb4-9bce-423d-b5fc-973f5ecc358b", "DestinationName": "IoTWirelessDestination", "Id": "1ffd32c8-8130-4194-96df-622f072a315f", "ThingName": "44b87eb4-9bce-423d-b5fc-973f5ecc358b", "Type": "LoRaWAN", "LoRaWAN": { "DeviceProfileId": "ab0c23d3-b001-45ef-6a01-2bc3de4f5333", "ServiceProfileId": "fe98dc76-cd12-001e-2d34-5550432da100", "OtaaV1_1": { "AppKey": "3f4ca100e2fc675ea123f4eb12c4a012", "JoinEui": "b4c231a359bc2e3d", "NwkKey": "01c3f004a2d6efffe32c4eda14bcd2b4" }, "DevEui": "ac12efc654d23fc2" }, "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/1ffd32c8-8130-4194-96df-622f072a315f", "Description": "My LoRaWAN wireless device" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-gateway-certificate`.

- **AWS CLI**
- 
            
                    **To get the ID of a certificate associated with a wireless gateway**The following `get-wireless-gateway-certificate`example gets the certificate ID associated with a wireless gateway that has the specified ID.`aws iotwireless get-wireless-gateway-certificate \ --id``"6c44ab31-8b4d-407a-bed3-19b6c7cda551"`Output: `{ "IotCertificateId": "8ea4aeae3db34c78cce75d9abd830356869ead6972997e0603e5fd032c804b6f" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessGatewayCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-gateway-firmware-information`.

- **AWS CLI**
- 
            
                    **To get firmware information about a wireless gateway**The following `get-wireless-gateway-firmware-information`example gets firmware version and other information about a wireless gateway.`aws iotwireless get-wireless-gateway-firmware-information \ --id``"3039b406-5cc9-4307-925b-9948c63da25b"`Output: `{ "LoRaWAN" :{ "CurrentVersion" :{ "PackageVersion" : "1.0.0", "Station" : "2.0.5", "Model" : "linux" } } }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessGatewayFirmwareInformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-firmware-information.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-gateway-statistics`.

- **AWS CLI**
- 
            
                    **To get operating information about a wireless gateway**The following `get-wireless-gateway-statistics`example gets operating information about a wireless gateway.`aws iotwireless get-wireless-gateway-statistics \ --wireless-gateway-id``"3039b406-5cc9-4307-925b-9948c63da25b"`Output: `{ "WirelessGatewayId": "3039b406-5cc9-4307-925b-9948c63da25b" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessGatewayStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-statistics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-gateway-task-definition`.

- **AWS CLI**
- 
            
                    **To get information about a wireless gateway task definition**The following `get-wireless-gateway-task-definition`example gets information about the wireless task definition with the specified ID.`aws iotwireless get-wireless-gateway-task-definition \ --id``"b7d3baad-25c7-35e7-a4e1-1683a0d61da9"`Output: `{ "AutoCreateTasks": true, "Name": "TestAutoUpdate", "Update":{ "UpdateDataSource" : "s3://cupsalphagafirmwarebin/station", "UpdateDataRole" : "arn:aws:iam::001234567890:role/SDK_Test_Role", "LoRaWAN" :{ "CurrentVersion" :{ "PackageVersion" : "1.0.0", "Station" : "2.0.5", "Model" : "linux" }, "UpdateVersion" :{ "PackageVersion" : "1.0.1", "Station" : "2.0.5", "Model" : "minihub" } } } }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessGatewayTaskDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-task-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-gateway-task`.

- **AWS CLI**
- 
            
                    **To get information about the wireless gateway task**The following `get-wireless-gateway-task`example gets information about the wireless gateway task with the specified ID.`aws iotwireless get-wireless-gateway-task \ --id``"11693a46-6866-47c3-a031-c9a616e7644b"`Output: `{ "WirelessGatewayId": "6c44ab31-8b4d-407a-bed3-19b6c7cda551", "WirelessGatewayTaskDefinitionId": "b7d3baad-25c7-35e7-a4e1-1683a0d61da9", "Status": "Success" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessGatewayTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-wireless-gateway`.

- **AWS CLI**
- 
            
                    **To get information about a wireless gateway**The following `get-wireless-gateway`example gets information about the wireless gateway`myFirstLoRaWANGateway`.`aws iotwireless get-wireless-gateway \ --identifier``"12345678-a1b2-3c45-67d8-e90fa1b2c34d"`\ --identifier-type`WirelessGatewayId`Output: `{ "Description": "My first LoRaWAN gateway", "ThingArn": "arn:aws:iot:us-east-1:123456789012:thing/a1b2c3d4-5678-90ab-cdef-12ab345c67de", "LoRaWAN": { "RfRegion": "US915", "GatewayEui": "a1b2c3d4567890ab" }, "ThingName": "a1b2c3d4-5678-90ab-cdef-12ab345c67de", "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d", "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessGateway/6c44ab31-8b4d-407a-bed3-19b6c7cda551", "Name": "myFirstLoRaWANGateway" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [GetWirelessGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/get-wireless-gateway.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-destinations`.

- **AWS CLI**
- 
            
                    **To list the wireless destinations**The following `list-destinations`example lists the available destinations registered to your AWS account.`aws iotwireless list-destinations`Output: `{ "DestinationList": [ { "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/IoTWirelessDestination", "Name": "IoTWirelessDestination", "Expression": "IoTWirelessRule", "Description": "Destination for messages processed using IoTWirelessRule", "RoleArn": "arn:aws:iam::123456789012:role/IoTWirelessDestinationRole" }, { "Arn": "arn:aws:iotwireless:us-east-1:123456789012:Destination/IoTWirelessDestination2", "Name": "IoTWirelessDestination2", "Expression": "IoTWirelessRule2", "RoleArn": "arn:aws:iam::123456789012:role/IoTWirelessDestinationRole" } ] }`For more information, see [Add destinations to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListDestinations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-destinations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-device-profiles`.

- **AWS CLI**
- 
            
                    **To list the device profiles**The following `list-device-profiles`example lists the available device profiles registered to your AWS account.`aws iotwireless list-device-profiles`Output: `{ "DeviceProfileList": [ { "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d", "Arn": "arn:aws:iotwireless:us-east-1:123456789012:DeviceProfile/12345678-a1b2-3c45-67d8-e90fa1b2c34d" }, { "Id": "a1b2c3d4-5678-90ab-cdef-12ab345c67de", "Arn": "arn:aws:iotwireless:us-east-1:123456789012:DeviceProfile/a1b2c3d4-5678-90ab-cdef-12ab345c67de" } ] }`For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListDeviceProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-device-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-partner-accounts`.

- **AWS CLI**
- 
            
                    **To list the partner accounts**The following `list-partner-accounts`example lists the available partner accounts associated with your AWS account.`aws iotwireless list-partner-accounts`Output: `{ "Sidewalk": [ { "AmazonId": "78965678771228", "Fingerprint": "bd96d8ef66dbfd2160eb60e156849e82ad7018b8b73c1ba0b4fc65c32498ee35" }, { "AmazonId": "89656787651228", "Fingerprint": "bc5e99e151c07be14be7e6603e4489c53f858b271213a36ebe3370777ba06e9b" } ] }`For more information, see [Amazon Sidewalk Integration for AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListPartnerAccounts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-partner-accounts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-profiles`.

- **AWS CLI**
- 
            
                    **To list the service profiles**The following `list-service-profiles`example lists the available service profiles registered to your AWS account.`aws iotwireless list-service-profiles`Output: `{ "ServiceProfileList": [ { "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d", "Arn": "arn:aws:iotwireless:us-east-1:123456789012:ServiceProfile/538185bb-d7e7-4b95-96a0-c51aa4a5b9a0" }, { "Id": "a1b2c3d4-5678-90ab-cdef-12ab345c67de", "Arn": "arn:aws:iotwireless:us-east-1:123456789012:ServiceProfile/ea8bc823-5d13-472e-8d26-9550737d8100" } ] }`For more information, see [Add profiles to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-define-profiles.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListServiceProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-service-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags assigned to the resource**The following `list-tags-for-resource`example lists the tags assigned to a wireless destination resource.`aws iotwireless list-tags-for-resource \ --resource-arn``"arn:aws:iotwireless:us-east-1:123456789012:Destination/IoTWirelessDestination"`Output: `{ "Tags": [ { "Value": "MyValue", "Key": "MyTag" } ] }`For more information, see [Describe your AWS IoT Core for LoRaWAN resources](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-describe-resource.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-wireless-devices`.

- **AWS CLI**
- 
            
                    **To list the available wireless devices**The following `list-wireless-devices`example lists the available wireless devices registered to your AWS account.`aws iotwireless list-wireless-devices`Output: `{ "WirelessDeviceList": [ { "Name": "myLoRaWANDevice", "DestinationName": "IoTWirelessDestination", "Id": "1ffd32c8-8130-4194-96df-622f072a315f", "Type": "LoRaWAN", "LoRaWAN": { "DevEui": "ac12efc654d23fc2" }, "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessDevice/1ffd32c8-8130-4194-96df-622f072a315f" } ] }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListWirelessDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-devices.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-wireless-gateway-task-definitions`.

- **AWS CLI**
- 
            
                    **To list the wireless gateway task definitions**The following `list-wireless-gateway-task-definitions`example lists the available wireless gateway task definitions registered to your AWS account.`aws iotwireless list-wireless-gateway-task-definitions`Output: `{ "TaskDefinitions": [ { "Id": "b7d3baad-25c7-35e7-a4e1-1683a0d61da9", "LoRaWAN" : { "CurrentVersion" :{ "PackageVersion" : "1.0.0", "Station" : "2.0.5", "Model" : "linux" }, "UpdateVersion" :{ "PackageVersion" : "1.0.1", "Station" : "2.0.5", "Model" : "minihub" } } } ] }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListWirelessGatewayTaskDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-gateway-task-definitions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-wireless-gateways`.

- **AWS CLI**
- 
            
                    **To list the wireless gateways**The following `list-wireless-gateways`example lists the available wireless gateways in your AWS account.`aws iotwireless list-wireless-gateways`Output: `{ "WirelessGatewayList": [ { "Description": "My first LoRaWAN gateway", "LoRaWAN": { "RfRegion": "US915", "GatewayEui": "dac632ebc01d23e4" }, "Id": "3039b406-5cc9-4307-925b-9948c63da25b", "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessGateway/3039b406-5cc9-4307-925b-9948c63da25b", "Name": "myFirstLoRaWANGateway" }, { "Description": "My second LoRaWAN gateway", "LoRaWAN": { "RfRegion": "US915", "GatewayEui": "cda123fffe92ecd2" }, "Id": "3285bdc7-5a12-4991-84ed-dadca65e342e", "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessGateway/3285bdc7-5a12-4991-84ed-dadca65e342e", "Name": "mySecondLoRaWANGateway" } ] }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [ListWirelessGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/list-wireless-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-data-to-wireless-device`.

- **AWS CLI**
- 
            
                    **To send data to the wireless device**The following `send-data-to-wireless-device`example sends a decrypted application data frame to the wireless device.`aws iotwireless send-data-to-wireless-device \ --id``"11aa5eae-2f56-4b8e-a023-b28d98494e49"`\ --transmit-mode`"1"`\ --payload-data`"SGVsbG8gVG8gRGV2c2lt"`\ --wireless-metadata`LoRaWAN={FPort=1}`Output: `{ MessageId: "6011dd36-0043d6eb-0072-0008" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [SendDataToWirelessDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/send-data-to-wireless-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To specify a tag key and value for a resource**The following `tag-resource`example tags the wireless destination`IoTWirelessDestination`with the key`MyTag`and value`MyValue`.`aws iotwireless tag-resource \ --resource-arn``"arn:aws:iotwireless:us-east-1:651419225604:Destination/IoTWirelessDestination"`\ --tags Key="MyTag",Value="MyValue"This command produces no output. For more information, see [Describe your AWS IoT Core for LoRaWAN resources](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-describe-resource.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-wireless-device`.

- **AWS CLI**
- 
            
                    **To test the wireless device**The following `test-wireless-device`example sends uplink data of`Hello`to a device with specified ID.`aws iotwireless test-wireless-device \ --id``"11aa5eae-2f56-4b8e-a023-b28d98494e49"`Output: `{ Result: "Test succeeded. one message is sent with payload: hello" }`For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [TestWirelessDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/test-wireless-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove one or more tags from a resource**The following `untag-resource`example removes the tag`MyTag`and its value from the wireless destination`IoTWirelessDestination`.`aws iotwireless untag-resource \ --resource-arn``"arn:aws:iotwireless:us-east-1:123456789012:Destination/IoTWirelessDestination"`\ --tag-keys`"MyTag"`This command produces no output. For more information, see [Describe your AWS IoT Core for LoRaWAN resources](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-describe-resource.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-destination`.

- **AWS CLI**
- 
            
                    **To update the properties of a destination**The following `update-destination`example updates the description property of a wireless destination.`aws iotwireless update-destination \ --name``"IoTWirelessDestination"`\ --description`"Destination for messages processed using IoTWirelessRule"`This command produces no output. For more information, see [Add destinations to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan-create-destinations.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateDestination](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-destination.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-partner-account`.

- **AWS CLI**
- 
            
                    **To update the properties of a partner account**The following `update-partner-account`updates the`AppServerPrivateKey`for the account that has the specified ID.`aws iotwireless update-partner-account \ --partner-account-id``"78965678771228"`\ --partner-type`"Sidewalk"`\ --sidewalk AppServerPrivateKey="f798ab4899346a88599180fee9e14fa1ada7b6df989425b7c6d2146dd6c815bb"This command produces no output. For more information, see [Amazon Sidewalk Integration for AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sidewalk.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdatePartnerAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-partner-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-wireless-device`.

- **AWS CLI**
- 
            
                    **To update the properties of a wireless device**The following `update-wireless-device`example updates the properties of a wireless device registered to your AWS account.`aws iotwireless update-wireless-device \ --id``"1ffd32c8-8130-4194-96df-622f072a315f"`\ --destination-name`IoTWirelessDestination2`\ --description`"Using my first LoRaWAN device"`This command produces no output. For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateWirelessDevice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-wireless-device.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-wireless-gateway`.

- **AWS CLI**
- 
            
                    **To update the wireless gateway**The following `update-wireless-gateway`example updates the description of your wireless gateway.`aws iotwireless update-wireless-gateway \ --id``"3285bdc7-5a12-4991-84ed-dadca65e342e"`\ --description`"Using my LoRaWAN gateway"`This command produces no output. For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html)in the*AWS IoT Developers Guide*.- 
                    For API details, see [UpdateWirelessGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/update-wireless-gateway.html)in*AWS CLI Command Reference*.
 
-