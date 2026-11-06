# App Runner examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_apprunner_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_apprunner_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with App Runner.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-custom-domain`.

- **AWS CLI**
- 
            
                    **To associate a domain name and the www subdomain with a service**The following `associate-custom-domain`example associates a custom domain name that you control with an App Runner service. The domain name is the root domain`example.com`, including the special-case subdomain`www.example.com`.`aws apprunner associate-custom-domain \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "DomainName": "example.com", "EnableWWWSubdomain": true }`Output: `{ "CustomDomain": { "CertificateValidationRecords": [ { "Name": "_70d3f50a94f7c72dc28784cf55db2f6b.example.com", "Status": "PENDING_VALIDATION", "Type": "CNAME", "Value": "_1270c137383c6307b6832db02504c4b0.bsgbmzkfwj.acm-validations.aws." }, { "Name": "_287870d3f50a94f7c72dc4cf55db2f6b.www.example.com", "Status": "PENDING_VALIDATION", "Type": "CNAME", "Value": "_832db01270c137383c6307b62504c4b0.mzkbsgbfwj.acm-validations.aws." } ], "DomainName": "example.com", "EnableWWWSubdomain": true, "Status": "CREATING" }, "DNSTarget": "psbqam834h.us-east-1.awsapprunner.com", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`- 
                    For API details, see [AssociateCustomDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/associate-custom-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-auto-scaling-configuration`.

- **AWS CLI**
- 
            
                    **To create a high availability auto scaling configuration**The following `create-auto-scaling-configuration`example creates an auto scaling configuration optimized for high availability by setting`MinSize`to 5. With this configuration, App Runner attempts to spread your service instances over the most Availability Zones possible, up to five, depending on the AWS Region.The call returns an `AutoScalingConfiguration`object with the other settings set to their defaults. In the example, this is the first call to create a configuration named`high-availability`. The revision is set to 1, and it's the latest revision.`aws apprunner create-auto-scaling-configuration \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "AutoScalingConfigurationName": "high-availability", "MinSize": 5 }`Output: `{ "AutoScalingConfiguration": { "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1/2f50e7656d7819fead0f59672e68042e", "AutoScalingConfigurationName": "high-availability", "AutoScalingConfigurationRevision": 1, "CreatedAt": "2020-11-03T00:29:17Z", "Latest": true, "Status": "ACTIVE", "MaxConcurrency": 100, "MaxSize": 50, "MinSize": 5 } }`- 
                    For API details, see [CreateAutoScalingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-auto-scaling-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-connection`.

- **AWS CLI**
- 
            
                    **To create a GitHub connection**The following `create-connection`example creates a connection to a private GitHub code repository. The connection status after a successful call is`PENDING_HANDSHAKE`. This is because an authentication handshake with the provider still hasn't happened. Complete the handshake using the App Runner console.`aws apprunner create-connection \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ConnectionName": "my-github-connection", "ProviderType": "GITHUB" }`Output: `{ "Connection": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection", "ConnectionName": "my-github-connection", "Status": "PENDING_HANDSHAKE", "CreatedAt": "2020-11-03T00:32:51Z", "ProviderType": "GITHUB" } }`For more information, see [Managing App Runner connections](https://docs.aws.amazon.com/apprunner/latest/dg/manage-connections.html)in the*AWS App Runner Developer Guide*.- 
                    For API details, see [CreateConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-service`.

- **AWS CLI**
- 
            
                    **Example 1: To create a source code repository service**The following `create-service`example creates an App Runner service based on a Python source code repository.`aws apprunner create-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceName": "python-app", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" }, "CodeConfiguration": { "ConfigurationSource": "API", "CodeConfigurationValues": { "Runtime": "PYTHON_3", "BuildCommand": "pip install -r requirements.txt", "StartCommand": "python server.py", "Port": "8080", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ] } } } }, "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } }`Output: `{ "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "Service": { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-20T19:05:25Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "CodeConfiguration": { "CodeConfigurationValues": { "BuildCommand": "pip install -r requirements.txt", "Port": "8080", "Runtime": "PYTHON_3", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ], "StartCommand": "python server.py" }, "ConfigurationSource": "Api" }, "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" } } }, "Status": "OPERATION_IN_PROGRESS", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } } }`**Example 2: To create a source code repository service**The following `create-service`example creates an App Runner service based on a Python source code repository.`aws apprunner create-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceName": "python-app", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" }, "CodeConfiguration": { "ConfigurationSource": "API", "CodeConfigurationValues": { "Runtime": "PYTHON_3", "BuildCommand": "pip install -r requirements.txt", "StartCommand": "python server.py", "Port": "8080", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ] } } } }, "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } }`Output: `{ "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "Service": { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-20T19:05:25Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "CodeConfiguration": { "CodeConfigurationValues": { "BuildCommand": "pip install -r requirements.txt", "Port": "8080", "Runtime": "PYTHON_3", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ], "StartCommand": "python server.py" }, "ConfigurationSource": "Api" }, "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" } } }, "Status": "OPERATION_IN_PROGRESS", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } } }`**Example 3: To create a source image repository service**The following `create-service`example creates an App Runner service based on an image stored in Elastic Container Registry (ECR).`aws apprunner create-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceName": "golang-container-app", "SourceConfiguration": { "AuthenticationConfiguration": { "AccessRoleArn": "arn:aws:iam::123456789012:role/my-ecr-role" }, "AutoDeploymentsEnabled": true, "ImageRepository": { "ImageIdentifier": "123456789012.dkr.ecr.us-east-1.amazonaws.com/golang-app:latest", "ImageConfiguration": { "Port": "8080", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ] }, "ImageRepositoryType": "ECR" } }, "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } }`Output: `{ "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "Service": { "CreatedAt": "2020-11-06T23:15:30Z", "UpdatedAt": "2020-11-06T23:15:30Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/golang-container-app/51728f8a20ce46d39b25398a6c8e9d1a", "ServiceId": "51728f8a20ce46d39b25398a6c8e9d1a", "ServiceName": "golang-container-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "AccessRoleArn": "arn:aws:iam::123456789012:role/my-ecr-role" }, "AutoDeploymentsEnabled": true, "ImageRepository": { "ImageIdentifier": "123456789012.dkr.ecr.us-east-1.amazonaws.com/golang-app:latest", "ImageConfiguration": { "Port": "8080", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ] }, "ImageRepositoryType": "ECR" } }, "Status": "OPERATION_IN_PROGRESS", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } } }`- 
                    For API details, see [CreateService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/create-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-auto-scaling-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To delete the latest active revision of an auto scaling configuration**The following `delete-auto-scaling-configuration`example deletes the latest active revision of an App Runner auto scaling configuration. To delete the latest active revision, specify an Amazon Resource Name (ARN) that ends with the configuration name, without the revision component.In the example, two revisions exist before this action. Therefore, revision 2 (the latest) is deleted. However, it now shows `"Latest": false`, because, after being deleted, it isn't the latest active revision anymore.`aws apprunner delete-auto-scaling-configuration \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability" }`Output: `{ "AutoScalingConfiguration": { "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/e76562f50d78042e819fead0f59672e6", "AutoScalingConfigurationName": "high-availability", "AutoScalingConfigurationRevision": 2, "CreatedAt": "2021-02-25T17:42:59Z", "DeletedAt": "2021-03-02T08:07:06Z", "Latest": false, "Status": "INACTIVE", "MaxConcurrency": 30, "MaxSize": 90, "MinSize": 5 } }`**Example 2: To delete a specific revision of an auto scaling configuration**The following `delete-auto-scaling-configuration`example deletes a specific revision of an App Runner auto scaling configuration. To delete a specific revision, specify an ARN that includes the revision number.In the example, several revisions exist before this action. The action deletes revision `1`.`aws apprunner delete-auto-scaling-configuration \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1" }`Output: `{ "AutoScalingConfiguration": { "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1/2f50e7656d7819fead0f59672e68042e", "AutoScalingConfigurationName": "high-availability", "AutoScalingConfigurationRevision": 1, "CreatedAt": "2020-11-03T00:29:17Z", "DeletedAt": "2021-03-02T08:07:06Z", "Latest": false, "Status": "INACTIVE", "MaxConcurrency": 100, "MaxSize": 50, "MinSize": 5 } }`- 
                    For API details, see [DeleteAutoScalingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/delete-auto-scaling-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-connection`.

- **AWS CLI**
- 
            
                    **To delete a connection**The following `delete-connection`example deletes an App Runner connection. The connection status after a successful call is`DELETED`. This is because the connection is no longer available.`aws apprunner delete-connection \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection" }`Output: `{ "Connection": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection", "ConnectionName": "my-github-connection", "Status": "DELETED", "CreatedAt": "2020-11-03T00:32:51Z", "ProviderType": "GITHUB" } }`- 
                    For API details, see [DeleteConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/delete-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-service`.

- **AWS CLI**
- 
            
                    **To delete a service**The following `delete-service`example deletes an App Runner service.`aws apprunner delete-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`Output: `{ "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "Service": { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-20T19:05:25Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "CodeConfiguration": { "CodeConfigurationValues": { "BuildCommand": "pip install -r requirements.txt", "Port": "8080", "Runtime": "PYTHON_3", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ], "StartCommand": "python server.py" }, "ConfigurationSource": "Api" }, "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" } } }, "Status": "OPERATION_IN_PROGRESS", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } } }`- 
                    For API details, see [DeleteService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/delete-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-auto-scaling-configuration`.

- **AWS CLI**
- 
            
                    **Example 1: To describe the latest active revision of an auto scaling configuration**The following `describe-auto-scaling-configuration`example gets a description of the latest active revision of an App Runner auto scaling configuration. To describe the latest active revision, specify an ARN that ends with the configuration name, without the revision component.In the example, two revisions exist. Therefore, revision `2`(the latest) is described. The resulting object shows`"Latest": true`.`aws apprunner describe-auto-scaling-configuration \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability" }`Output: `{ "AutoScalingConfiguration": { "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/e76562f50d78042e819fead0f59672e6", "AutoScalingConfigurationName": "high-availability", "AutoScalingConfigurationRevision": 2, "CreatedAt": "2021-02-25T17:42:59Z", "Latest": true, "Status": "ACTIVE", "MaxConcurrency": 30, "MaxSize": 90, "MinSize": 5 } }`**Example 2: To describe a specific revision of an auto scaling configuration**The following `describe-auto-scaling-configuration`example get a description of a specific revision of an App Runner auto scaling configuration. To describe a specific revision, specify an ARN that includes the revision number.In the example, several revisions exist and revision `1`is queried. The resulting object shows`"Latest": false`.`aws apprunner describe-auto-scaling-configuration \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1" }`Output: `{ "AutoScalingConfiguration": { "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/1/2f50e7656d7819fead0f59672e68042e", "AutoScalingConfigurationName": "high-availability", "AutoScalingConfigurationRevision": 1, "CreatedAt": "2020-11-03T00:29:17Z", "Latest": false, "Status": "ACTIVE", "MaxConcurrency": 100, "MaxSize": 50, "MinSize": 5 } }`- 
                    For API details, see [DescribeAutoScalingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/describe-auto-scaling-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-custom-domains`.

- **AWS CLI**
- 
            
                    **To get descriptions of custom domain names associated with a service**The following `describe-custom-domains`example get descriptions and status of the custom domain names associated with an App Runner service.`aws apprunner describe-custom-domains \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "DomainName": "example.com", "EnableWWWSubdomain": true }`Output: `{ "CustomDomains": [ { "CertificateValidationRecords": [ { "Name": "_70d3f50a94f7c72dc28784cf55db2f6b.example.com", "Status": "PENDING_VALIDATION", "Type": "CNAME", "Value": "_1270c137383c6307b6832db02504c4b0.bsgbmzkfwj.acm-validations.aws." }, { "Name": "_287870d3f50a94f7c72dc4cf55db2f6b.www.example.com", "Status": "PENDING_VALIDATION", "Type": "CNAME", "Value": "_832db01270c137383c6307b62504c4b0.mzkbsgbfwj.acm-validations.aws." } ], "DomainName": "example.com", "EnableWWWSubdomain": true, "Status": "PENDING_CERTIFICATE_DNS_VALIDATION" }, { "CertificateValidationRecords": [ { "Name": "_a94f784c70d3f507c72dc28f55db2f6b.deals.example.com", "Status": "SUCCESS", "Type": "CNAME", "Value": "_2db02504c1270c137383c6307b6834b0.bsgbmzkfwj.acm-validations.aws." } ], "DomainName": "deals.example.com", "EnableWWWSubdomain": false, "Status": "ACTIVE" } ], "DNSTarget": "psbqam834h.us-east-1.awsapprunner.com", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`- 
                    For API details, see [DescribeCustomDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/describe-custom-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-service`.

- **AWS CLI**
- 
            
                    **To describe a service**The following `describe-service`example gets a description of an App Runner service.`aws apprunner describe-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`Output: `{ "Service": { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-20T19:05:25Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "CodeConfiguration": { "CodeConfigurationValues": { "BuildCommand": "pip install -r requirements.txt", "Port": "8080", "Runtime": "PYTHON_3", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ], "StartCommand": "python server.py" }, "ConfigurationSource": "Api" }, "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" } } }, "Status": "RUNNING", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } } }`- 
                    For API details, see [DescribeService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/describe-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-custom-domain`.

- **AWS CLI**
- 
            
                    **To disassociate a domain name from a service**The following `disassociate-custom-domain`example disassociates the domain`example.com`from an App Runner service. The call also disassociates the subdomain`www.example.com`that was associated together with the root domain.`aws apprunner disassociate-custom-domain \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "DomainName": "example.com" }`Output: `{ "CustomDomain": { "CertificateValidationRecords": [ { "Name": "_70d3f50a94f7c72dc28784cf55db2f6b.example.com", "Status": "PENDING_VALIDATION", "Type": "CNAME", "Value": "_1270c137383c6307b6832db02504c4b0.bsgbmzkfwj.acm-validations.aws." }, { "Name": "_287870d3f50a94f7c72dc4cf55db2f6b.www.example.com", "Status": "PENDING_VALIDATION", "Type": "CNAME", "Value": "_832db01270c137383c6307b62504c4b0.mzkbsgbfwj.acm-validations.aws." } ], "DomainName": "example.com", "EnableWWWSubdomain": true, "Status": "DELETING" }, "DNSTarget": "psbqam834h.us-east-1.awsapprunner.com", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`- 
                    For API details, see [DisassociateCustomDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/disassociate-custom-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-auto-scaling-configurations`.

- **AWS CLI**
- 
            
                    **To get a paginated listing of App Runner auto scaling configurations**The following `list-auto-scaling-configurations`example lists all App Runner auto scaling configurations in your AWS account. Up to five auto scaling configurations are listed in each response.`AutoScalingConfigurationName`and`LatestOnly`aren't specified. Their defaults cause the latest revision of all active configurations to be listed.In this example, the response includes two results and there aren't additional ones, so no `NextToken`is returned.`aws apprunner list-auto-scaling-configurations \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "MaxResults": 5 }`Output: `{ "AutoScalingConfigurationSummaryList": [ { "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/2/e76562f50d78042e819fead0f59672e6", "AutoScalingConfigurationName": "high-availability", "AutoScalingConfigurationRevision": 2 }, { "AutoScalingConfigurationArn": "arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/low-cost/1/50d7804e7656fead0f59672e62f2e819", "AutoScalingConfigurationName": "low-cost", "AutoScalingConfigurationRevision": 1 } ] }`- 
                    For API details, see [ListAutoScalingConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-auto-scaling-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-connections`.

- **AWS CLI**
- 
            
                    **Example 1: To list all connections**The following `list-connections`example lists all App Runner connections in the AWS account.`aws apprunner list-connections`Output: `{ "ConnectionSummaryList": [ { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection", "ConnectionName": "my-github-connection", "Status": "AVAILABLE", "CreatedAt": "2020-11-03T00:32:51Z", "ProviderType": "GITHUB" }, { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-org-connection", "ConnectionName": "my-github-org-connection", "Status": "AVAILABLE", "CreatedAt": "2020-11-03T02:54:17Z", "ProviderType": "GITHUB" } ] }`**Example 2: To list a connection by name**The following `list-connections`example lists a connection by its name.`aws apprunner list-connections \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ConnectionName": "my-github-org-connection" }`Output: `{ "ConnectionSummaryList": [ { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-org-connection", "ConnectionName": "my-github-org-connection", "Status": "AVAILABLE", "CreatedAt": "2020-11-03T02:54:17Z", "ProviderType": "GITHUB" } ] }`- 
                    For API details, see [ListConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-operations`.

- **AWS CLI**
- 
            
                    **To list operations that occurred on a servicee**The following `list-operations`example lists all operations that occurred on an App Runner service so far. In this example, the service is new and only a single operation of type`CREATE_SERVICE`has occurred.`aws apprunner list-operations \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`Output: `{ "OperationSummaryList": [ { "EndedAt": 1606156217, "Id": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "StartedAt": 1606156014, "Status": "SUCCEEDED", "TargetArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "Type": "CREATE_SERVICE", "UpdatedAt": 1606156217 } ] }`- 
                    For API details, see [ListOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-services`.

- **AWS CLI**
- 
            
                    **To get a paginated listing of App Runner services**The following `list-services`example lists all App Runner services in the AWS account. Up to two services are listed in each response. This example shows the first request. The response includes two results and a token that can be used in the next request. When a subsequent response doesn't include a token, all services have been listed.`aws apprunner list-services \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "MaxResults": 2 }`Output: `{ "NextToken": "eyJDdXN0b21lckFjY291bnRJZCI6IjI3MDIwNTQwMjg0NSIsIlNlcnZpY2VTdGF0dXNDb2RlIjoiUFJPVklTSU9OSU5HIiwiSGFzaEtleSI6IjI3MDIwNTQwMjg0NSNhYjhmOTRjZmUyOWE0NjBmYjg3NjBhZmQyZWU4NzU1NSJ9", "ServiceSummaryList": [ { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-23T12:41:37Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "Status": "RUNNING" }, { "CreatedAt": "2020-11-06T23:15:30Z", "UpdatedAt": "2020-11-23T13:21:22Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/golang-container-app/ab8f94cfe29a460fb8760afd2ee87555", "ServiceId": "ab8f94cfe29a460fb8760afd2ee87555", "ServiceName": "golang-container-app", "ServiceUrl": "e2m8rrrx33.us-east-1.awsapprunner.com", "Status": "RUNNING" } ] }`- 
                    For API details, see [ListServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags associated with an App Runner service**The following `list-tags-for-resource`example lists all the tags that are associated with an App Runner service.`aws apprunner list-tags-for-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ResourceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`Output: `{ "Tags": [ { "Key": "Department", "Value": "Retail" }, { "Key": "CustomerId", "Value": "56439872357912" } ] }`- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `pause-service`.

- **AWS CLI**
- 
            
                    **To pause a service**The following `pause-service`example pauses an App Runner service.`aws apprunner pause-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`Output: `{ "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "Service": { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-23T12:41:37Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "CodeConfiguration": { "CodeConfigurationValues": { "BuildCommand": "pip install -r requirements.txt", "Port": "8080", "Runtime": "PYTHON_3", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ], "StartCommand": "python server.py" }, "ConfigurationSource": "Api" }, "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" } } }, "Status": "OPERATION_IN_PROGRESS", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } } }`- 
                    For API details, see [PauseService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/pause-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resume-service`.

- **AWS CLI**
- 
            
                    **To resume a service**The following `resume-service`example resumes an App Runner service.`aws apprunner resume-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`Output: `{ "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "Service": { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-23T12:41:37Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "CodeConfiguration": { "CodeConfigurationValues": { "BuildCommand": "pip install -r requirements.txt", "Port": "8080", "Runtime": "PYTHON_3", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ], "StartCommand": "python server.py" }, "ConfigurationSource": "Api" }, "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" } } }, "Status": "OPERATION_IN_PROGRESS", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "3 GB" } } }`- 
                    For API details, see [ResumeService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/resume-service.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-deployment`.

- **AWS CLI**
- 
            
                    **To initiate a manual deployment**The following `start-deployment`example performs a manual deployment to an App Runner service.`aws apprunner start-deployment \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa" }`Output: `{ "OperationId": "853a7d5b-fc9f-4730-831b-fd8037ab832a" }`- 
                    For API details, see [StartDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/start-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to an App Runner service**The following `tag-resource`example adds two tags to an App Runner service.`aws apprunner tag-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ResourceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "Tags": [ { "Key": "Department", "Value": "Retail" }, { "Key": "CustomerId", "Value": "56439872357912" } ] }`This command produces no output. - 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from an App Runner service**The following `untag-resource`example removes two tags from an App Runner service.`aws apprunner untag-resource \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ResourceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "TagKeys": [ "Department", "CustomerId" ] }`This command produces no output. - 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-service`.

- **AWS CLI**
- 
            
                    **To update memory size**The following `update-service`example updates the memory size of instances (scaling units) of an App Runner service to 2048 MiB.When the call succeeds, App Runner starts an asynchronous update process. The `Service`structure that's returned by the call reflects the new memory value that's being applied by this call.`aws apprunner update-service \ --cli-input-json``file://input.json`Contents of `input.json`:`{ "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "InstanceConfiguration": { "Memory": "4 GB" } }`Output: `{ "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf", "Service": { "CreatedAt": "2020-11-20T19:05:25Z", "UpdatedAt": "2020-11-23T12:41:37Z", "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa", "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa", "ServiceName": "python-app", "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com", "SourceConfiguration": { "AuthenticationConfiguration": { "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e" }, "AutoDeploymentsEnabled": true, "CodeRepository": { "CodeConfiguration": { "CodeConfigurationValues": { "BuildCommand": "pip install -r requirements.txt", "Port": "8080", "Runtime": "PYTHON_3", "RuntimeEnvironmentVariables": [ { "NAME": "Jane" } ], "StartCommand": "python server.py" }, "ConfigurationSource": "Api" }, "RepositoryUrl": "https://github.com/my-account/python-hello", "SourceCodeVersion": { "Type": "BRANCH", "Value": "main" } } }, "Status": "OPERATION_IN_PROGRESS", "InstanceConfiguration": { "Cpu": "1 vCPU", "Memory": "4 GB" } } }`- 
                    For API details, see [UpdateService](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/update-service.html)in*AWS CLI Command Reference*.
 
-