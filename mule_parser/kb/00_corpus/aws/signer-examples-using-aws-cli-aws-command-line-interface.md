# Signer examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_signer_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_signer_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Signer.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `cancel-signing-profile`.

- **AWS CLI**
- 
            
                    **To delete a signing profile**The following `cancel-signing-profile`example removes an existing signing profile from AWS Signer.`aws signer cancel-signing-profile \ --profile-name``MyProfile1`This command produces no output. - 
                    For API details, see [CancelSigningProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/cancel-signing-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-signing-job`.

- **AWS CLI**
- 
            
                    **To display details about a signing job**The following `describe-signing-job`example displays details about the specified signing job.`aws signer describe-signing-job \ --job-id``2065c468-73e2-4385-a6c9-0123456789abc`Output: `{ "status": "Succeeded", "completedAt": 1568412037, "platformId": "AmazonFreeRTOS-Default", "signingMaterial": { "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc" }, "statusReason": "Signing Succeeded", "jobId": "2065c468-73e2-4385-a6c9-0123456789abc", "source": { "s3": { "version": "PNyFaUTgsQh5ZdMCcoCe6pT1gOpgB_M4", "bucketName": "signer-source", "key": "MyCode.rb" } }, "profileName": "MyProfile2", "signedObject": { "s3": { "bucketName": "signer-destination", "key": "signed-2065c468-73e2-4385-a6c9-0123456789abc" } }, "requestedBy": "arn:aws:iam::123456789012:user/maria", "createdAt": 1568412036 }`- 
                    For API details, see [DescribeSigningJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/describe-signing-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-signing-platform`.

- **AWS CLI**
- 
            
                    **To display details about a signing platform**The following `get-signing-platform`example displays details about the specified signing platform.`aws signer get-signing-platform \ --platform-id``AmazonFreeRTOS-TI-CC3220SF`Output: `{ "category": "AWS", "displayName": "Amazon FreeRTOS SHA1-RSA CC3220SF-Format", "target": "SHA1-RSA-TISHA1", "platformId": "AmazonFreeRTOS-TI-CC3220SF", "signingConfiguration": { "encryptionAlgorithmOptions": { "defaultValue": "RSA", "allowedValues": [ "RSA" ] }, "hashAlgorithmOptions": { "defaultValue": "SHA1", "allowedValues": [ "SHA1" ] } }, "maxSizeInMB": 16, "partner": "AmazonFreeRTOS", "signingImageFormat": { "defaultFormat": "JSONEmbedded", "supportedFormats": [ "JSONEmbedded" ] } }`- 
                    For API details, see [GetSigningPlatform](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/get-signing-platform.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-signing-profile`.

- **AWS CLI**
- 
            
                    **To display details about a signing profile**The following `get-signing-profile`example displays details about the specified signing profile.`aws signer get-signing-profile \ --profile-name``MyProfile3`Output: `{ "platformId": "AmazonFreeRTOS-TI-CC3220SF", "profileName": "MyProfile3", "status": "Active", "signingMaterial": { "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc" } }`- 
                    For API details, see [GetSigningProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/get-signing-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-signing-jobs`.

- **AWS CLI**
- 
            
                    **To list all signing jobs**The following `list-signing-jobs`example displays details about all signing jobs for the account.`aws signer list-signing-jobs`In this example, two jobs are returned, one successful, and one failed. `{ "jobs": [ { "status": "Succeeded", "signingMaterial": { "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc" }, "jobId": "2065c468-73e2-4385-a6c9-0123456789abc", "source": { "s3": { "version": "PNyFaUTgsQh5ZdMCcoCe6pT1gOpgB_M4", "bucketName": "signer-source", "key": "MyCode.rb" } }, "signedObject": { "s3": { "bucketName": "signer-destination", "key": "signed-2065c468-73e2-4385-a6c9-0123456789abc" } }, "createdAt": 1568412036 }, { "status": "Failed", "source": { "s3": { "version": "PNyFaUTgsQh5ZdMCcoCe6pT1gOpgB_M4", "bucketName": "signer-source", "key": "MyOtherCode.rb" } }, "signingMaterial": { "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc" }, "createdAt": 1568402690, "jobId": "74d9825e-22fc-4a0d-b962-0123456789abc" } ] }`- 
                    For API details, see [ListSigningJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-signing-platforms`.

- **AWS CLI**
- 
            
                    **To list all signing platforms**The following `list-signing-platforms`example displays details about all available signing platforms.`aws signer list-signing-platforms`Output: `{ "platforms": [ { "category": "AWS", "displayName": "AWS IoT Device Management SHA256-ECDSA ", "target": "SHA256-ECDSA", "platformId": "AWSIoTDeviceManagement-SHA256-ECDSA", "signingConfiguration": { "encryptionAlgorithmOptions": { "defaultValue": "ECDSA", "allowedValues": [ "ECDSA" ] }, "hashAlgorithmOptions": { "defaultValue": "SHA256", "allowedValues": [ "SHA256" ] } }, "maxSizeInMB": 2048, "partner": "AWSIoTDeviceManagement", "signingImageFormat": { "defaultFormat": "JSONDetached", "supportedFormats": [ "JSONDetached" ] } }, { "category": "AWS", "displayName": "Amazon FreeRTOS SHA1-RSA CC3220SF-Format", "target": "SHA1-RSA-TISHA1", "platformId": "AmazonFreeRTOS-TI-CC3220SF", "signingConfiguration": { "encryptionAlgorithmOptions": { "defaultValue": "RSA", "allowedValues": [ "RSA" ] }, "hashAlgorithmOptions": { "defaultValue": "SHA1", "allowedValues": [ "SHA1" ] } }, "maxSizeInMB": 16, "partner": "AmazonFreeRTOS", "signingImageFormat": { "defaultFormat": "JSONEmbedded", "supportedFormats": [ "JSONEmbedded" ] } }, { "category": "AWS", "displayName": "Amazon FreeRTOS SHA256-ECDSA", "target": "SHA256-ECDSA", "platformId": "AmazonFreeRTOS-Default", "signingConfiguration": { "encryptionAlgorithmOptions": { "defaultValue": "ECDSA", "allowedValues": [ "ECDSA" ] }, "hashAlgorithmOptions": { "defaultValue": "SHA256", "allowedValues": [ "SHA256" ] } }, "maxSizeInMB": 16, "partner": "AmazonFreeRTOS", "signingImageFormat": { "defaultFormat": "JSONEmbedded", "supportedFormats": [ "JSONEmbedded" ] } } ] }`- 
                    For API details, see [ListSigningPlatforms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-platforms.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-signing-profiles`.

- **AWS CLI**
- 
            
                    **To list all signing profiles**The following `list-signing-profiles`example displays details about all signing profiles for the account.`aws signer list-signing-profiles`Output: `{ "profiles": [ { "platformId": "AmazonFreeRTOS-TI-CC3220SF", "profileName": "MyProfile4", "status": "Active", "signingMaterial": { "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc" } }, { "platformId": "AWSIoTDeviceManagement-SHA256-ECDSA", "profileName": "MyProfile5", "status": "Active", "signingMaterial": { "certificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc" } } ] }`- 
                    For API details, see [ListSigningProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/list-signing-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-signing-profile`.

- **AWS CLI**
- 
            
                    **To create a signing profile**The following `put-signing-profile`example creates a signing profile using the specified certificate and platform.`aws signer put-signing-profile \ --profile-name``MyProfile6`\ --signing-material`certificateArn=arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc`\ --platform`AmazonFreeRTOS-TI-CC3220SF`Output: `{ "arn": "arn:aws:signer:us-west-2:123456789012:/signing-profiles/MyProfile6" }`- 
                    For API details, see [PutSigningProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/put-signing-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-signing-job`.

- **AWS CLI**
- 
            
                    **To start a signing job**The following `start-signing-job`example starts a signing job on the code found at the specified source. It uses the specified profile to do the signing and places the signed code in the specified destination.`aws signer start-signing-job \ --source '``s3={bucketName=signer-source,key=MyCode.rb,version=PNyFaUTgsQh5ZdMCcoCe6pT1gOpgB_M4}`' \ --destination '`s3={bucketName=signer-destination,prefix=signed-}`' \ --profile-name`MyProfile7`The output is the ID of the signing job. `{ "jobId": "2065c468-73e2-4385-a6c9-0123456789abc" }`- 
                    For API details, see [StartSigningJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/start-signing-job.html)in*AWS CLI Command Reference*.
 
-