# AWS AppConfig examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_appconfig_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_appconfig_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS AppConfig.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-application`.

- **AWS CLI**
- 
            
                    **To create an application**The following `create-application`example creates an application in AWS AppConfig.`aws appconfig create-application \ --name``"example-application"`\ --description`"An application used for creating an example."`Output: `{ "Description": "An application used for creating an example.", "Id": "339ohji", "Name": "example-application" }`For more information, see [Step 1: Creating an AWS AppConfig application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [CreateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-configuration-profile`.

- **AWS CLI**
- 
            
                    **To create a configuration profile**The following `create-configuration-profile`example creates a configuration profile using a configuration stored in Parameter Store, a capability of Systems Manager.`aws appconfig create-configuration-profile \ --application-id``"339ohji"`\ --name`"Example-Configuration-Profile"`\ --location-uri`"ssm-parameter://Example-Parameter"`\ --retrieval-role-arn`"arn:aws:iam::111122223333:role/Example-App-Config-Role"`Output: `{ "ApplicationId": "339ohji", "Description": null, "Id": "ur8hx2f", "LocationUri": "ssm-parameter://Example-Parameter", "Name": "Example-Configuration-Profile", "RetrievalRoleArn": "arn:aws:iam::111122223333:role/Example-App-Config-Role", "Type": null, "Validators": null }`For more information, see [Step 3: Creating a configuration and a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [CreateConfigurationProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-configuration-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-environment`.

- **AWS CLI**
- 
            
                    **To create an environment**The following `create-environment`example creates an AWS AppConfig environment named Example-Environment using the application you created using create-application.`aws appconfig create-environment \ --application-id``"339ohji"`\ --name`"Example-Environment"`Output: `{ "ApplicationId": "339ohji", "Description": null, "Id": "54j1r29", "Monitors": null, "Name": "Example-Environment", "State": "ReadyForDeployment" }`For more information, see [Step 2: Creating an environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [CreateEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-extension-association`.

- **AWS CLI**
- 
            
                    **To create an extension association**The following `create-extension-association`example creates a new extension association in AWS AppConfig.`aws appconfig create-extension-association \ --region``us-west-2`\ --extension-identifier`S3-backup-extension`\ --resource-identifier`"arn:aws:appconfig:us-west-2:123456789012:application/Finance"`\ --parameters`S3bucket=FinanceConfigurationBackup`Output: `{ "Id": "a1b2c3d4", "ExtensionArn": "arn:aws:appconfig:us-west-2:123456789012:extension/S3-backup-extension/1", "ResourceArn": "arn:aws:appconfig:us-west-2:123456789012:application/Finance", "Parameters": { "S3bucket": "FinanceConfigurationBackup" }, "ExtensionVersionNumber": 1 }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [CreateExtensionAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-extension-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-extension`.

- **AWS CLI**
- 
            
                    **To create an extension**The following `create-extension`example creates a new extension in AWS AppConfig.`aws appconfig create-extension \ --region``us-west-2`\ --name`S3-backup-extension`\ --actions`PRE_CREATE_HOSTED_CONFIGURATION_VERSION=[{Name=S3backup,Uri=arn:aws:lambda:us-west-2:123456789012:function:s3backupfunction,RoleArn=arn:aws:iam::123456789012:role/appconfigextensionrole}]`\ --parameters`S3bucket={Required=true}`Output: `{ "Id": "1A2B3C4D", "Name": "S3-backup-extension", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2:123456789012:extension/1A2B3C4D/1", "Actions": { "PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [ { "Name": "S3backup", "Uri": "arn:aws:lambda:us-west-2:123456789012:function:s3backupfunction", "RoleArn": "arn:aws:iam::123456789012:role/appconfigextensionrole" } ] }, "Parameters": { "S3bucket": { "Required": true } } }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [CreateExtension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-extension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-hosted-configuration-version`.

- **AWS CLI**
- 
            
                    **To create a hosted configuration version**The following `create-hosted-configuration-version`example creates a new configuration in the AWS AppConfig hosted configuration store. The configuration content must first be converted to base64.`aws appconfig create-hosted-configuration-version \ --application-id``"339ohji"`\ --configuration-profile-id`"ur8hx2f"`\ --content`eyAiTmFtZSI6ICJFeGFtcGxlQXBwbGljYXRpb24iLCAiSWQiOiBFeGFtcGxlSUQsICJSYW5rIjogNyB9`\ --content-type`"application/json"`\`configuration_version_output_file`Contents of `configuration_version_output_file`:`{ "Name": "ExampleApplication", "Id": ExampleID, "Rank": 7 }`Output: `{ "ApplicationId": "339ohji", "ConfigurationProfileId": "ur8hx2f", "VersionNumber": "1", "ContentType": "application/json" }`For more information, see [About the AWS AppConfig hosted configuration store](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-about-hosted-store)in the*AWS Appconfig User Guide*.- 
                    For API details, see [CreateHostedConfigurationVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-hosted-configuration-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-application`.

- **AWS CLI**
- 
            
                    **To delete an application**The following `delete-application`example deletes the specified application.`aws appconfig delete-application \ --application-id``339ohji`This command produces no output. For more information, see [Step 1: Creating an AWS AppConfig application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [DeleteApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-configuration-profile`.

- **AWS CLI**
- 
            
                    **To delete a configuration profile**The following `delete-configuration-profile`example deletes the specified configuration profile.`aws appconfig delete-configuration-profile \ --application-id``339ohji`\ --configuration-profile-id`ur8hx2f`This command produces no output. For more information, see [Step 3: Creating a configuration and a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [DeleteConfigurationProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-configuration-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-deployment-strategy`.

- **AWS CLI**
- 
            
                    **To delete a deployment strategy**The following `delete-deployment-strategy`example deletes the specified deployment strategy.`aws appconfig delete-deployment-strategy \ --deployment-strategy-id``1225qzk`This command produces no output. For more information, see [Step 4: Creating a deployment strategy](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [DeleteDeploymentStrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-deployment-strategy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-environment`.

- **AWS CLI**
- 
            
                    **To delete an environment**The following `delete-environment`example deletes the specified application environment.`aws appconfig delete-environment \ --application-id``339ohji`\ --environment-id`54j1r29`This command produces no output. For more information, see [Step 2: Creating an environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [DeleteEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-extension-association`.

- **AWS CLI**
- 
            
                    **To delete an extension association**The following `delete-extension-association`example deletes an extension association from AWS AppConfig.`aws appconfig delete-extension-association \ --region``us-west-2`\ --extension-association-id`a1b2c3d4`This command produces no output. For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [DeleteExtensionAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-extension-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-extension`.

- **AWS CLI**
- 
            
                    **To delete an extension**The following `delete-extension`example deletes an extension from AWS AppConfig.`aws appconfig delete-extension \ --region``us-west-2`\ --extension-identifier`S3-backup-extension`This command produces no output. For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [DeleteExtension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-extension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-hosted-configuration-version`.

- **AWS CLI**
- 
            
                    **To delete a hosted configuration version**The following `delete-hosted-configuration-version`example deletes a configuration version hosted in the AWS AppConfig hosted configuration store.`aws appconfig delete-hosted-configuration-version \ --application-id``339ohji`\ --configuration-profile-id`ur8hx2f`\ --version-number`1`Output:: This command produces no output. For more information, see [Step 3: Creating a configuration and a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [DeleteHostedConfigurationVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-hosted-configuration-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-application`.

- **AWS CLI**
- 
            
                    **To list details of an application**The following `get-application`example lists the details of the specified application.`aws appconfig get-application \ --application-id``339ohji`Output: `{ "Description": "An application used for creating an example.", "Id": "339ohji", "Name": "example-application" }`For more information, see [How AWS AppConfig works](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html#learn-more-appconfig-how-it-works)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-configuration-profile`.

- **AWS CLI**
- 
            
                    **To retrieve configuration profile details**The following `get-configuration-profile`example returns the details of the specified configuration profile.`aws appconfig get-configuration-profile \ --application-id``339ohji`\ --configuration-profile-id`ur8hx2f`Output: `{ "ApplicationId": "339ohji", "Id": "ur8hx2f", "Name": "Example-Configuration-Profile", "LocationUri": "ssm-parameter://Example-Parameter", "RetrievalRoleArn": "arn:aws:iam::111122223333:role/Example-App-Config-Role" }`For more information, see [Step 3: Creating a configuration and a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetConfigurationProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-configuration-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-configuration`.

- **AWS CLI**
- 
            
                    **To retrieve configuration details**The following `get-configuration`example returns the configuration details of the example application. On subsequent calls to get-configuration use the`client-configuration-version`parameter to only update the configuration of your application if the version has changed. Only updating the configuration when the version has changed avoids excess charges incurred by calling get-configuration.`aws appconfig get-configuration \ --application``"example-application"`\ --environment`"Example-Environment"`\ --configuration`"Example-Configuration-Profile"`\ --client-id`"test-id"`\`configuration-output-file`Contents of `configuration-output-file`:`{ "Name": "ExampleApplication", "Id": ExampleID, "Rank": 7 }`Output: `{ "ConfigurationVersion": "1", "ContentType": "application/json" }`For more information, see [Step 6: Receiving the configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-retrieving-the-configuration.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment-strategy`.

- **AWS CLI**
- 
            
                    **To retrieve details of a deployment strategy**The following `get-deployment-strategy`example lists the details of the specified deployment strategy.`aws appconfig get-deployment-strategy \ --deployment-strategy-id``1225qzk`Output: `{ "Id": "1225qzk", "Name": "Example-Deployment", "DeploymentDurationInMinutes": 15, "GrowthType": "LINEAR", "GrowthFactor": 25.0, "FinalBakeTimeInMinutes": 0, "ReplicateTo": "SSM_DOCUMENT" }`For more information, see [Step 4: Creating a deployment strategy](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetDeploymentStrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-deployment-strategy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment`.

- **AWS CLI**
- 
            
                    **To retrieve deployment details**The following `get-deployment`example lists details of the deployment to the application in the specified environment and deployment.`aws appconfig get-deployment \ --application-id``339ohji`\ --environment-id`54j1r29`\ --deployment-number`1`Output: `{ "ApplicationId": "339ohji", "EnvironmentId": "54j1r29", "DeploymentStrategyId": "1225qzk", "ConfigurationProfileId": "ur8hx2f", "DeploymentNumber": 1, "ConfigurationName": "Example-Configuration-Profile", "ConfigurationLocationUri": "ssm-parameter://Example-Parameter", "ConfigurationVersion": "1", "DeploymentDurationInMinutes": 15, "GrowthType": "LINEAR", "GrowthFactor": 25.0, "FinalBakeTimeInMinutes": 0, "State": "COMPLETE", "EventLog": [ { "EventType": "DEPLOYMENT_COMPLETED", "TriggeredBy": "APPCONFIG", "Description": "Deployment completed", "OccurredAt": "2021-09-17T21:59:03.888000+00:00" }, { "EventType": "BAKE_TIME_STARTED", "TriggeredBy": "APPCONFIG", "Description": "Deployment bake time started", "OccurredAt": "2021-09-17T21:58:57.722000+00:00" }, { "EventType": "PERCENTAGE_UPDATED", "TriggeredBy": "APPCONFIG", "Description": "Configuration available to 100.00% of clients", "OccurredAt": "2021-09-17T21:55:56.816000+00:00" }, { "EventType": "PERCENTAGE_UPDATED", "TriggeredBy": "APPCONFIG", "Description": "Configuration available to 75.00% of clients", "OccurredAt": "2021-09-17T21:52:56.567000+00:00" }, { "EventType": "PERCENTAGE_UPDATED", "TriggeredBy": "APPCONFIG", "Description": "Configuration available to 50.00% of clients", "OccurredAt": "2021-09-17T21:49:55.737000+00:00" }, { "EventType": "PERCENTAGE_UPDATED", "TriggeredBy": "APPCONFIG", "Description": "Configuration available to 25.00% of clients", "OccurredAt": "2021-09-17T21:46:55.187000+00:00" }, { "EventType": "DEPLOYMENT_STARTED", "TriggeredBy": "USER", "Description": "Deployment started", "OccurredAt": "2021-09-17T21:43:54.205000+00:00" } ], "PercentageComplete": 100.0, "StartedAt": "2021-09-17T21:43:54.205000+00:00", "CompletedAt": "2021-09-17T21:59:03.888000+00:00" }`For more information, see [Step 5: Deploying a configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-environment`.

- **AWS CLI**
- 
            
                    **To retrieve environment details**The following `get-environment`example returns the details and state of the specified environment.`aws appconfig get-environment \ --application-id``339ohji`\ --environment-id`54j1r29`Output: `{ "ApplicationId": "339ohji", "Id": "54j1r29", "Name": "Example-Environment", "State": "ReadyForDeployment" }`For more information, see [Step 2: Creating an environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-extension-association`.

- **AWS CLI**
- 
            
                    **To get extension association details**The following `get-extension-association`example displays information about an extension association.`aws appconfig get-extension-association \ --region``us-west-2`\ --extension-association-id`a1b2c3d4`Output: `{ "Id": "a1b2c3d4", "ExtensionArn": "arn:aws:appconfig:us-west-2:123456789012:extension/S3-backup-extension/1", "ResourceArn": "arn:aws:appconfig:us-west-2:123456789012:application/Finance", "Parameters": { "S3bucket": "FinanceConfigurationBackup" }, "ExtensionVersionNumber": 1 }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetExtensionAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-extension-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-extension`.

- **AWS CLI**
- 
            
                    **To get extension details**The following `get-extension`example displays information about an extension.`aws appconfig get-extension \ --region``us-west-2`\ --extension-identifier`S3-backup-extension`Output: `{ "Id": "1A2B3C4D", "Name": "S3-backup-extension", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2:123456789012:extension/S3-backup-extension/1", "Actions": { "PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [ { "Name": "S3backup", "Uri": "arn:aws:lambda:us-west-2:123456789012:function:S3backupfunction", "RoleArn": "arn:aws:iam::123456789012:role/appconfigextensionrole" } ] }, "Parameters": { "S3bucket": { "Required": true } } }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetExtension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-extension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-hosted-configuration-version`.

- **AWS CLI**
- 
            
                    **To retrieve hosted configuration details**The following `get-hosted-configuration-version`example retrieves the configuration details of the AWS AppConfig hosted configuration.`aws appconfig get-hosted-configuration-version \ --application-id``339ohji`\ --configuration-profile-id`ur8hx2f`\ --version-number`1`\`hosted-configuration-version-output`Contents of `hosted-configuration-version-output`:`{ "Name": "ExampleApplication", "Id": ExampleID, "Rank": 7 }`Output: `{ "ApplicationId": "339ohji", "ConfigurationProfileId": "ur8hx2f", "VersionNumber": "1", "ContentType": "application/json" }`For more information, see [About the AWS AppConfig hosted configuration store](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-about-hosted-store)in the*AWS AppConfig User Guide*.- 
                    For API details, see [GetHostedConfigurationVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-hosted-configuration-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-applications`.

- **AWS CLI**
- 
            
                    **To list the available applications**The following `list-applications`example lists the available applications in your AWS account.`aws appconfig list-applications`Output: `{ "Items": [ { "Id": "339ohji", "Name": "test-application", "Description": "An application used for creating an example." }, { "Id": "rwalwu7", "Name": "Test-Application" } ] }`For more information, see [Step 1: Creating an AWS AppConfig application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-applications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-configuration-profiles`.

- **AWS CLI**
- 
            
                    **To list the available configuration profiles**The following `list-configuration-profiles`example lists the available configuration profiles for the specified application.`aws appconfig list-configuration-profiles \ --application-id``339ohji`Output: `{ "Items": [ { "ApplicationId": "339ohji", "Id": "ur8hx2f", "Name": "Example-Configuration-Profile", "LocationUri": "ssm-parameter://Example-Parameter" } ] }`For more information, see [Step 3: Creating a configuration and a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListConfigurationProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-configuration-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployment-strategies`.

- **AWS CLI**
- 
            
                    **To list the available deployment strategies**The following `list-deployment-strategies`example lists the available deployment strategies in your AWS account.`aws appconfig list-deployment-strategies`Output: `{ "Items": [ { "Id": "1225qzk", "Name": "Example-Deployment", "DeploymentDurationInMinutes": 15, "GrowthType": "LINEAR", "GrowthFactor": 25.0, "FinalBakeTimeInMinutes": 0, "ReplicateTo": "SSM_DOCUMENT" }, { "Id": "AppConfig.AllAtOnce", "Name": "AppConfig.AllAtOnce", "Description": "Quick", "DeploymentDurationInMinutes": 0, "GrowthType": "LINEAR", "GrowthFactor": 100.0, "FinalBakeTimeInMinutes": 10, "ReplicateTo": "NONE" }, { "Id": "AppConfig.Linear50PercentEvery30Seconds", "Name": "AppConfig.Linear50PercentEvery30Seconds", "Description": "Test/Demo", "DeploymentDurationInMinutes": 1, "GrowthType": "LINEAR", "GrowthFactor": 50.0, "FinalBakeTimeInMinutes": 1, "ReplicateTo": "NONE" }, { "Id": "AppConfig.Canary10Percent20Minutes", "Name": "AppConfig.Canary10Percent20Minutes", "Description": "AWS Recommended", "DeploymentDurationInMinutes": 20, "GrowthType": "EXPONENTIAL", "GrowthFactor": 10.0, "FinalBakeTimeInMinutes": 10, "ReplicateTo": "NONE" } ] }`For more information, see [Step 4: Creating a deployment strategy](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListDeploymentStrategies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-deployment-strategies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-deployments`.

- **AWS CLI**
- 
            
                    **To list the available deployments**The following `list-deployments`example lists the available deployments in your AWS account for the specified application and environment.`aws appconfig list-deployments \ --application-id``339ohji`\ --environment-id`54j1r29`Output: `{ "Items": [ { "DeploymentNumber": 1, "ConfigurationName": "Example-Configuration-Profile", "ConfigurationVersion": "1", "DeploymentDurationInMinutes": 15, "GrowthType": "LINEAR", "GrowthFactor": 25.0, "FinalBakeTimeInMinutes": 0, "State": "COMPLETE", "PercentageComplete": 100.0, "StartedAt": "2021-09-17T21:43:54.205000+00:00", "CompletedAt": "2021-09-17T21:59:03.888000+00:00" } ] }`For more information, see [Step 5: Deploying a configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-environments`.

- **AWS CLI**
- 
            
                    **To list the available environments**The following `list-environments`example lists the available environments in your AWS account for the specified application.`aws appconfig list-environments \ --application-id``339ohji`Output: `{ "Items": [ { "ApplicationId": "339ohji", "Id": "54j1r29", "Name": "Example-Environment", "State": "ReadyForDeployment" } ] }`For more information, see [Step 2: Creating an environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-environments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-extension-associations`.

- **AWS CLI**
- 
            
                    **To list all AWS AppConfig extension associations in your AWS account for an AWS Region**The following `list-extension-associations`example lists all AWS AppConfig extension associations for the current AWS account in a specific AWS Region.`aws appconfig list-extension-associations \ --region``us-west-2`Output: `{ "Items": [ { "Id": "a1b2c3d4", "ExtensionArn": "arn:aws:appconfig:us-west-2:123456789012:extension/S3-backup-extension/1", "ResourceArn": "arn:aws:appconfig:us-west-2:123456789012:application/Finance" } ] }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListExtensionAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-extension-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-extensions`.

- **AWS CLI**
- 
            
                    **To list all AWS AppConfig extensions in your AWS account for an AWS Region**The following `list-extensions`example lists all AWS AppConfig extensions for the current AWS account in a specific AWS Region. The command returns custom and AWS authored extensions.`aws appconfig list-extensions \ --region``us-west-2`Output: `{ "Items": [ { "Id": "1A2B3C4D", "Name": "S3-backup-extension", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2:123456789012:extension/1A2B3C4D/1" }, { "Id": "AWS.AppConfig.FeatureFlags", "Name": "AppConfig Feature Flags Helper", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.FeatureFlags/1", "Description": "Validates AppConfig feature flag data automatically against a JSON schema that includes structure and constraints. Also transforms feature flag data prior to sending to the client. This extension is automatically associated to configuration profiles with type \"AWS.AppConfig.FeatureFlags\"." }, { "Id": "AWS.AppConfig.JiraIntegration", "Name": "AppConfig integration with Atlassian Jira", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.JiraIntegration/1", "Description": "Exports feature flag data from AWS AppConfig into Jira. The lifecycle of each feature flag in AppConfig is tracked in Jira as an individual issue. Customers can see in Jira when flags are updated, turned on or off. Works in conjunction with the AppConfig app in the Atlassian Marketplace and is automatically associated to configuration profiles configured within that app." }, { "Id": "AWS.AppConfig.DeploymentNotificationsToEventBridge", "Name": "AppConfig deployment events to Amazon EventBridge", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.DeploymentNotificationsToEventBridge/1", "Description": "Sends events to Amazon EventBridge when a deployment of configuration data in AppConfig is started, completed, or rolled back. Can be associated to the following resources in AppConfig: Application, Environment, Configuration Profile." }, { "Id": "AWS.AppConfig.DeploymentNotificationsToSqs", "Name": "AppConfig deployment events to Amazon SQS", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2::extension/AWS.AppConfig.DeploymentNotificationsToSqs/1", "Description": "Sends messages to the configured Amazon SQS queue when a deployment of configuration data in AppConfig is started, completed, or rolled back. Can be associated to the following resources in AppConfig: Application, Environment, Configuration Profile." }, { "Id": "AWS.AppConfig.DeploymentNotificationsToSns", "Name": "AppConfig deployment events to Amazon SNS", "VersionNumber": 1, "Description": "Sends events to the configured Amazon SNS topic when a deployment of configuration data in AppConfig is started, completed, or rolled back. Can be associated to the following resources in AppConfig: Application, Environment, Configuration Profile." } ] }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListExtensions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-extensions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-hosted-configuration-versions`.

- **AWS CLI**
- 
            
                    **To list the available hosted configuration versions**The following `list-hosted-configuration-versions`example lists the configurations versions hosted in the AWS AppConfig hosted configuration store for the specified application and configuration profile.`aws appconfig list-hosted-configuration-versions \ --application-id``339ohji`\ --configuration-profile-id`ur8hx2f`Output: `{ "Items": [ { "ApplicationId": "339ohji", "ConfigurationProfileId": "ur8hx2f", "VersionNumber": 1, "ContentType": "application/json" } ] }`For more information, see [About the AWS AppConfig hosted configuration store](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html#appconfig-creating-configuration-and-profile-about-hosted-store)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListHostedConfigurationVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-hosted-configuration-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags of an application**The following `list-tags-for-resource`example lists the tags of a specified application.`aws appconfig list-tags-for-resource \ --resource-arn``arn:aws:appconfig:us-east-1:682428703967:application/339ohji`Output: `{ "Tags": { "group1": "1" } }`For more information, see [Step 1: Creating an AWS AppConfig application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-deployment`.

- **AWS CLI**
- 
            
                    **To start a configuration deployment**The following `start-deployment`example starts a deployment to the application using the specified environment, deployment strategy, and configuration profile.`aws appconfig start-deployment \ --application-id``339ohji`\ --environment-id`54j1r29`\ --deployment-strategy-id`1225qzk`\ --configuration-profile-id`ur8hx2f`\ --configuration-version`1`Output: `{ "ApplicationId": "339ohji", "EnvironmentId": "54j1r29", "DeploymentStrategyId": "1225qzk", "ConfigurationProfileId": "ur8hx2f", "DeploymentNumber": 1, "ConfigurationName": "Example-Configuration-Profile", "ConfigurationLocationUri": "ssm-parameter://Example-Parameter", "ConfigurationVersion": "1", "DeploymentDurationInMinutes": 15, "GrowthType": "LINEAR", "GrowthFactor": 25.0, "FinalBakeTimeInMinutes": 0, "State": "DEPLOYING", "EventLog": [ { "EventType": "DEPLOYMENT_STARTED", "TriggeredBy": "USER", "Description": "Deployment started", "OccurredAt": "2021-09-17T21:43:54.205000+00:00" } ], "PercentageComplete": 0.0, "StartedAt": "2021-09-17T21:43:54.205000+00:00" }`For more information, see [Step 5: Deploying a configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [StartDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/start-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-deployment`.

- **AWS CLI**
- 
            
                    **To stop configuration deployment**The following `stop-deployment`example stops the deployment of an application configuration to the specified environment.`aws appconfig stop-deployment \ --application-id``339ohji`\ --environment-id`54j1r29`\ --deployment-number`2`Output: `{ "DeploymentNumber": 0, "DeploymentDurationInMinutes": 0, "GrowthFactor": 0.0, "FinalBakeTimeInMinutes": 0, "PercentageComplete": 0.0 }`For more information, see [Step 5: Deploying a configuration](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-deploying.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [StopDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/stop-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag an application**The following `tag-resource`example tags an application resource.`aws appconfig tag-resource \ --resource-arn``arn:aws:appconfig:us-east-1:682428703967:application/339ohji`\ --tags '`{"group1" : "1"}`'This command produces no output. For more information, see [Step 1: Creating an AWS AppConfig application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from an application**The following `untag-resource`example removes the group1 tag from the specified application.`aws appconfig untag-resource \ --resource-arn``arn:aws:appconfig:us-east-1:111122223333:application/339ohji`\ --tag-keys '`["group1"]`'This command produces no output. For more information, see [Step 1: Creating an AWS AppConfig application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-application`.

- **AWS CLI**
- 
            
                    **To update an application**The following `update-application`example updates the name of the specified application.`aws appconfig update-application \ --application-id``339ohji`\ --name`"Example-Application"`Output: `{ "Id": "339ohji", "Name": "Example-Application", "Description": "An application used for creating an example." }`For more information, see [Step 1: Creating an AWS AppConfig application](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-application.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [UpdateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-configuration-profile`.

- **AWS CLI**
- 
            
                    **To update a configuration profile**The following `update-configuration-profile`example updates the description of the specified configuration profile.`aws appconfig update-configuration-profile \ --application-id``339ohji`\ --configuration-profile-id`ur8hx2f`\ --description`"Configuration profile used for examples."`Output: `{ "ApplicationId": "339ohji", "Id": "ur8hx2f", "Name": "Example-Configuration-Profile", "Description": "Configuration profile used for examples.", "LocationUri": "ssm-parameter://Example-Parameter", "RetrievalRoleArn": "arn:aws:iam::111122223333:role/Example-App-Config-Role" }`For more information, see [Step 3: Creating a configuration and a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [UpdateConfigurationProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-configuration-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-deployment-strategy`.

- **AWS CLI**
- 
            
                    **To update a deployment strategy**The following `update-deployment-strategy`example updates final bake time to 20 minutes in the specified deployment strategy.`aws appconfig update-deployment-strategy \ --deployment-strategy-id``1225qzk`\ --final-bake-time-in-minutes`20`Output: `{ "Id": "1225qzk", "Name": "Example-Deployment", "DeploymentDurationInMinutes": 15, "GrowthType": "LINEAR", "GrowthFactor": 25.0, "FinalBakeTimeInMinutes": 20, "ReplicateTo": "SSM_DOCUMENT" }`For more information, see [Step 4: Creating a deployment strategy](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [UpdateDeploymentStrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-deployment-strategy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-environment`.

- **AWS CLI**
- 
            
                    **To update an environment**The following `update-environment`example updates an environment's description.`aws appconfig update-environment \ --application-id``339ohji`\ --environment-id`54j1r29`\ --description`"An environment for examples."`Output: `{ "ApplicationId": "339ohji", "Id": "54j1r29", "Name": "Example-Environment", "Description": "An environment for examples.", "State": "RolledBack" }`For more information, see [Step 2: Creating an environment](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-environment.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [UpdateEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-environment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-extension-association`.

- **AWS CLI**
- 
            
                    **To update an AWS AppConfig extension association**The following `update-extension-association`example adds a new parameter value to an extension association in AWS AppConfig.`aws appconfig update-extension-association \ --region``us-west-2`\ --extension-association-id`a1b2c3d4`\ --parameters`S3bucket=FinanceMobileApp`Output: `{ "Id": "a1b2c3d4", "ExtensionArn": "arn:aws:appconfig:us-west-2:123456789012:extension/S3-backup-extension/1", "ResourceArn": "arn:aws:appconfig:us-west-2:123456789012:application/Finance", "Parameters": { "S3bucket": "FinanceMobileApp" }, "ExtensionVersionNumber": 1 }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [UpdateExtensionAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-extension-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-extension`.

- **AWS CLI**
- 
            
                    **To update an AWS AppConfig extension**The following `update-extension`example adds an additional parameter Key to an extension in AWS AppConfig.`aws appconfig update-extension \ --region``us-west-2`\ --extension-identifier`S3-backup-extension`\ --parameters`S3bucket={Required=true},CampaignID={Required=false}`Output: `{ "Id": "1A2B3C4D", "Name": "S3-backup-extension", "VersionNumber": 1, "Arn": "arn:aws:appconfig:us-west-2:123456789012:extension/1A2B3C4D/1", "Actions": { "PRE_CREATE_HOSTED_CONFIGURATION_VERSION": [ { "Name": "S3backup", "Uri": "arn:aws:lambda:us-west-2:123456789012:function:S3backupfunction", "RoleArn": "arn:aws:iam::123456789012:role/appconfigextensionrole" } ] }, "Parameters": { "CampaignID": { "Required": false }, "S3bucket": { "Required": true } } }`For more information, see [Working with AWS AppConfig extensions](https://docs.aws.amazon.com/appconfig/latest/userguide/working-with-appconfig-extensions.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [UpdateExtension](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-extension.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `validate-configuration`.

- **AWS CLI**
- 
            
                    **To validate a configuration**The following `validate-configuration`example uses the validators in a configuration profile to validate a configuration.`aws appconfig validate-configuration \ --application-id``abc1234`\ --configuration-profile-id`ur8hx2f`\ --configuration-version`1`The command produces no output. For more information, see [Step 3: Creating a configuration and a configuration profile](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-and-profile.html)in the*AWS AppConfig User Guide*.- 
                    For API details, see [ValidateConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/validate-configuration.html)in*AWS CLI Command Reference*.
 
-