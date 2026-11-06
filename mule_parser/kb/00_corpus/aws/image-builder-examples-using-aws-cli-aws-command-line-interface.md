# Image Builder examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_imagebuilder_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_imagebuilder_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Image Builder.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-component`.

- **AWS CLI**
- 
            
                    **To create a component**The following `create-component`example creates a component that uses a JSON document file and references a component document in YAML format that is uploaded to an Amazon S3 bucket.`aws imagebuilder create-component \ --cli-input-json``file://create-component.json`Contents of `create-component.json`:`{ "name": "MyExampleComponent", "semanticVersion": "2019.12.02", "description": "An example component that builds, validates and tests an image", "changeDescription": "Initial version.", "platform": "Windows", "uri": "s3://s3-bucket-name/s3-bucket-path/component.yaml" }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "componentBuildVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/examplecomponent/2019.12.02/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [CreateComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-component.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-distribution-configuration`.

- **AWS CLI**
- 
            
                    **To create a distribution configuration**The following `create-distribution-configuration`example creates a distribution configuration using a JSON file.`aws imagebuilder create-distribution-configuration \ --cli-input-json``file:/create-distribution-configuration.json`Contents of `create-distribution-configuration.json`:`{ "name": "MyExampleDistribution", "description": "Copies AMI to eu-west-1", "distributions": [ { "region": "us-west-2", "amiDistributionConfiguration": { "name": "Name {{imagebuilder:buildDate}}", "description": "An example image name with parameter references", "amiTags": { "KeyName": "{{ssm:parameter_name}}" }, "launchPermission": { "userIds": [ "123456789012" ] } } }, { "region": "eu-west-1", "amiDistributionConfiguration": { "name": "My {{imagebuilder:buildVersion}} image {{imagebuilder:buildDate}}", "amiTags": { "KeyName": "Value" }, "launchPermission": { "userIds": [ "123456789012" ] } } } ] }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [CreateDistributionConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-distribution-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-image-pipeline`.

- **AWS CLI**
- 
            
                    **To create an image pipeline**The following `create-image-pipeline`example creates an image pipeline using a JSON file.`aws imagebuilder create-image-pipeline \ --cli-input-json``file://create-image-pipeline.json`Contents of `create-image-pipeline.json`:`{ "name": "MyWindows2016Pipeline", "description": "Builds Windows 2016 Images", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03", "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution", "imageTestsConfiguration": { "imageTestsEnabled": true, "timeoutMinutes": 60 }, "schedule": { "scheduleExpression": "cron(0 0 * * SUN)", "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE" }, "status": "ENABLED" }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [CreateImagePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-image-recipe`.

- **AWS CLI**
- 
            
                    **To create a recipe**The following `create-image-recipe`example creates an image recipe using a JSON file. Components are installed in the order in which they are specified.`aws imagebuilder create-image-recipe \ --cli-input-json``file://create-image-recipe.json`Contents of `create-image-recipe.json`:`{ "name": "MyBasicRecipe", "description": "This example image recipe creates a Windows 2016 image.", "semanticVersion": "2019.12.03", "components": [ { "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02/1" }, { "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myimportedcomponent/1.0.0/1" } ], "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2016-english-full-base-x86/xxxx.x.x" }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [CreateImageRecipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image-recipe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-image`.

- **AWS CLI**
- 
            
                    **To create an image**The following `create-image`example creates an image.`aws imagebuilder create-image \ --image-recipe-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03`\ --infrastructure-configuration-arn`arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [CreateImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-infrastructure-configuration`.

- **AWS CLI**
- 
            
                    **To create an infrastructure configuration**The following `create-infrastructure-configuration`example creates an infrastructure configuration using a JSON file.`aws imagebuilder create-infrastructure-configuration \ --cli-input-json``file://create-infrastructure-configuration.json`Contents of `create-infrastructure-configuration.json`:`{ "name": "MyExampleInfrastructure", "description": "An example that will retain instances of failed builds", "instanceTypes": [ "m5.large", "m5.xlarge" ], "instanceProfileName": "EC2InstanceProfileForImageBuilder", "securityGroupIds": [ "sg-a1b2c3d4" ], "subnetId": "subnet-a1b2c3d4", "logging": { "s3Logs": { "s3BucketName": "bucket-name", "s3KeyPrefix": "bucket-path" } }, "keyPair": "key-pair-name", "terminateInstanceOnFailure": false, "snsTopicArn": "arn:aws:sns:us-west-2:123456789012:sns-topic-name" }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [CreateInfrastructureConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/create-infrastructure-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-component`.

- **AWS CLI**
- 
            
                    **To delete a component**The following `delete-component`example deletes a component build version by specifying its ARN.`aws imagebuilder delete-component \ --component-build-version-arn``arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02/1`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "componentBuildVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [DeleteComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-component.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-image-pipeline`.

- **AWS CLI**
- 
            
                    **To delete an image pipeline**The following `delete-image-pipeline`example deletes an image pipeline by specifying its ARN.`aws imagebuilder delete-image-pipeline \ --image-pipeline-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/my-example-pipeline`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [DeleteImagePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-image-recipe`.

- **AWS CLI**
- 
            
                    **To delete an image recipe**The following `delete-image-recipe`example deletes an image recipe by specifying its ARN.`aws imagebuilder delete-image-recipe \ --image-recipe-arn``arn:aws:imagebuilder:us-east-1:123456789012:image-recipe/mybasicrecipe/2019.12.03`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [DeleteImageRecipe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image-recipe.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-image`.

- **AWS CLI**
- 
            
                    **To delete an image**The following `delete-image`example deletes an image build version by specifying its ARN.`aws imagebuilder delete-image \ --image-build-version-arn``arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image/2019.12.02/1`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [DeleteImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-infrastructure-configuration`.

- **AWS CLI**
- 
            
                    **To delete an infrastructure configuration**The following `delete-infrastructure-configuration`example deletes an image pipeline by specifying its ARN.`aws imagebuilder delete-infrastructure-configuration \ --infrastructure-configuration-arn``arn:aws:imagebuilder:us-east-1:123456789012:infrastructure-configuration/myexampleinfrastructure`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [DeleteInfrastructureConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/delete-infrastructure-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-component-policy`.

- **AWS CLI**
- 
            
                    **To get component policy details**The following `get-component-policy`example lists the details of a component policy by specifying its ARN.`aws imagebuilder get-component-policy \ --component-arn``arn:aws:imagebuilder:us-west-2:123456789012:component/my-example-component/2019.12.03/1`Output: `{ "Policy": "{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetComponent", "imagebuilder:ListComponents" ], "Resource": [ "arn:aws:imagebuilder:us-west-2:123456789012:component/my-example-component/2019.12.03/1" ] } ] }" }`For more information, see Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI <https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html>`__ in the *EC2 Image Builder Users Guide*.- 
                    For API details, see [GetComponentPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-component-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-component`.

- **AWS CLI**
- 
            
                    **To get component details**The following `get-component`example lists the details of a component by specifying its ARN.`aws imagebuilder get-component \ --component-build-version-arn``arn:aws:imagebuilder:us-west-2:123456789012:component/component-name/1.0.0/1`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "component": { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:component/component-name/1.0.0/1", "name": "component-name", "version": "1.0.0", "type": "TEST", "platform": "Linux", "owner": "123456789012", "data": "name: HelloWorldTestingDocument\ndescription: This is hello world testing document.\nschemaVersion: 1.0\n\nphases:\n - name: test\n steps:\n - name: HelloWorldStep\n action: ExecuteBash\n inputs:\n commands:\n - echo \"Hello World! Test.\"\n", "encrypted": true, "dateCreated": "2020-01-27T20:43:30.306Z", "tags": {} } }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [GetComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-component.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-distribution-configuration`.

- **AWS CLI**
- 
            
                    **To get the details of a distribution configuration**The following `get-distribution-configuration`example displays the details of a distribution configuration by specifying its ARN.`aws imagebuilder get-distribution-configuration \ --distribution-configuration-arn``arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "distributionConfiguration": { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution", "name": "MyExampleDistribution", "description": "Copies AMI to eu-west-1 and exports to S3", "distributions": [ { "region": "us-west-2", "amiDistributionConfiguration": { "name": "Name {{imagebuilder:buildDate}}", "description": "An example image name with parameter references", "amiTags": { "KeyName": "{{ssm:parameter_name}}" }, "launchPermission": { "userIds": [ "123456789012" ] } } }, { "region": "eu-west-1", "amiDistributionConfiguration": { "name": "My {{imagebuilder:buildVersion}} image {{imagebuilder:buildDate}}", "amiTags": { "KeyName": "Value" }, "launchPermission": { "userIds": [ "123456789012" ] } } } ], "dateCreated": "2020-02-19T18:40:10.529Z", "tags": {} } }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [GetDistributionConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-distribution-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image-pipeline`.

- **AWS CLI**
- 
            
                    **To get image pipeline details**The following `get-image-pipeline`example lists the details of an image pipeline by specifying its ARN.`aws imagebuilder get-image-pipeline \ --image-pipeline-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imagePipeline": { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline", "name": "MyWindows2016Pipeline", "description": "Builds Windows 2016 Images", "platform": "Windows", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03", "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution", "imageTestsConfiguration": { "imageTestsEnabled": true, "timeoutMinutes": 60 }, "schedule": { "scheduleExpression": "cron(0 0 * * SUN)", "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE" }, "status": "ENABLED", "dateCreated": "2020-02-19T19:04:01.253Z", "dateUpdated": "2020-02-19T19:04:01.253Z", "tags": {} } }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [GetImagePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image-policy`.

- **AWS CLI**
- 
            
                    **To get image policy details**The following `get-image-policy`example lists the details of an image policy by specifying its ARN.`aws imagebuilder get-image-policy \ --image-arn``arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image/2019.12.03/1`Output: `{ "Policy": "{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetImage", "imagebuilder:ListImages" ], "Resource": [ "arn:aws:imagebuilder:us-west-2:123456789012:image/my-example-image/2019.12.03/1" ] } ] }" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [GetImagePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image-recipe-policy`.

- **AWS CLI**
- 
            
                    **To get image recipe policy details**The following `get-image-recipe-policy`example lists the details of an image recipe policy by specifying its ARN.`aws imagebuilder get-image-recipe-policy \ --image-recipe-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/my-example-image-recipe/2019.12.03/1`Output: `{ "Policy": "{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetImageRecipe", "imagebuilder:ListImageRecipes" ], "Resource": [ "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/my-example-image-recipe/2019.12.03/1" ] } ] }" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [GetImageRecipePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image-recipe-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image`.

- **AWS CLI**
- 
            
                    **To get image details**The following `get-image`example lists the details of an image by specifying its ARN.`aws imagebuilder get-image \ --image-build-version-arn``arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "image": { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1", "name": "MyBasicRecipe", "version": "2019.12.03/1", "platform": "Windows", "state": { "status": "BUILDING" }, "imageRecipe": { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03", "name": "MyBasicRecipe", "description": "This example image recipe creates a Windows 2016 image.", "platform": "Windows", "version": "2019.12.03", "components": [ { "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02/1" }, { "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myimportedcomponent/1.0.0/1" } ], "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2016-english-full-base-x86/2019.12.17/1", "dateCreated": "2020-02-14T19:46:16.904Z", "tags": {} }, "infrastructureConfiguration": { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "name": "MyExampleInfrastructure", "description": "An example that will retain instances of failed builds", "instanceTypes": [ "m5.large", "m5.xlarge" ], "instanceProfileName": "EC2InstanceProfileForImageFactory", "securityGroupIds": [ "sg-a1b2c3d4" ], "subnetId": "subnet-a1b2c3d4", "logging": { "s3Logs": { "s3BucketName": "bucket-name", "s3KeyPrefix": "bucket-path" } }, "keyPair": "Sam", "terminateInstanceOnFailure": false, "snsTopicArn": "arn:aws:sns:us-west-2:123456789012:sns-name", "dateCreated": "2020-02-14T21:21:05.098Z", "tags": {} }, "imageTestsConfiguration": { "imageTestsEnabled": true, "timeoutMinutes": 720 }, "dateCreated": "2020-02-14T23:14:13.597Z", "outputResources": { "amis": [] }, "tags": {} } }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [GetImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-infrastructure-configuration`.

- **AWS CLI**
- 
            
                    **To get infrastructure configuration details**The following `get-infrastructure-configuration`example lists the details of an infrastructure configuration by specifying its ARN.`aws imagebuilder get-infrastructure-configuration \ --infrastructure-configuration-arn``arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "infrastructureConfiguration": { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "name": "MyExampleInfrastructure", "description": "An example that will retain instances of failed builds", "instanceTypes": [ "m5.large", "m5.xlarge" ], "instanceProfileName": "EC2InstanceProfileForImageBuilder", "securityGroupIds": [ "sg-a48c95ef" ], "subnetId": "subnet-a48c95ef", "logging": { "s3Logs": { "s3BucketName": "bucket-name", "s3KeyPrefix": "bucket-path" } }, "keyPair": "Name", "terminateInstanceOnFailure": false, "snsTopicArn": "arn:aws:sns:us-west-2:123456789012:sns-name", "dateCreated": "2020-02-19T19:11:51.858Z", "tags": {} } }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [GetInfrastructureConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/get-infrastructure-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-component`.

- **AWS CLI**
- 
            
                    **To import a component**The following `import-component`example imports a preexisting script using a JSON file.`aws imagebuilder import-component \ --cli-input-json``file://import-component.json`Contents of `import-component.json`:`{ "name": "MyImportedComponent", "semanticVersion": "1.0.0", "description": "An example of how to import a component", "changeDescription": "First commit message.", "format": "SHELL", "platform": "Windows", "type": "BUILD", "uri": "s3://s3-bucket-name/s3-bucket-path/component.yaml" }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "componentBuildVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myimportedcomponent/1.0.0/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ImportComponent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/import-component.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-component-build-versions`.

- **AWS CLI**
- 
            
                    **To list component build versions**The following `list-component-build-versions`example lists the component build versions with a specific semantic version.`aws imagebuilder list-component-build-versions --component-version-arn``arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "componentSummaryList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:component/myexamplecomponent/2019.12.02/1", "name": "MyExampleComponent", "version": "2019.12.02", "platform": "Windows", "type": "BUILD", "owner": "123456789012", "description": "An example component that builds, validates and tests an image", "changeDescription": "Initial version.", "dateCreated": "2020-02-19T18:53:45.940Z", "tags": { "KeyName": "KeyValue" } } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListComponentBuildVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-component-build-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-components`.

- **AWS CLI**
- 
            
                    **To list all of the component semantic versions**The following `list-components`example lists all of the component semantic versions to which you have access. You can optionally filter on whether to list components owned by you, by Amazon, or that have been shared with you by other accounts.`aws imagebuilder list-components`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "componentVersionList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:component/component-name/1.0.0", "name": "component-name", "version": "1.0.0", "platform": "Linux", "type": "TEST", "owner": "123456789012", "dateCreated": "2020-01-27T20:43:30.306Z" } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListComponents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-components.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-distribution-configurations`.

- **AWS CLI**
- 
            
                    **To list distributions**The following `list-distribution-configurations`example lists all of your distributions.`aws imagebuilder list-distribution-configurations`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "distributionConfigurationSummaryList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution", "name": "MyExampleDistribution", "description": "Copies AMI to eu-west-1 and exports to S3", "dateCreated": "2020-02-19T18:40:10.529Z", "tags": { "KeyName": "KeyValue" } } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListDistributionConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-distribution-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-image-build-versions`.

- **AWS CLI**
- 
            
                    **To list image build versions**The following `list-image-build-versions`example lists all of the image build versions with a semantic version.`aws imagebuilder list-image-build-versions \ --image-version-arn``arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imageSummaryList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/7", "name": "MyBasicRecipe", "version": "2019.12.03/7", "platform": "Windows", "state": { "status": "FAILED", "reason": "Can't start SSM Automation for arn arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/7 during building. Parameter \"iamInstanceProfileName\" has a null value." }, "owner": "123456789012", "dateCreated": "2020-02-19T18:56:11.511Z", "outputResources": { "amis": [] }, "tags": {} }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/6", "name": "MyBasicRecipe", "version": "2019.12.03/6", "platform": "Windows", "state": { "status": "FAILED", "reason": "An internal error has occurred." }, "owner": "123456789012", "dateCreated": "2020-02-18T22:49:08.142Z", "outputResources": { "amis": [ { "region": "us-west-2", "image": "ami-a1b2c3d4567890ab", "name": "MyBasicRecipe 2020-02-18T22-49-38.704Z", "description": "This example image recipe creates a Windows 2016 image." }, { "region": "us-west-2", "image": "ami-a1b2c3d4567890ab", "name": "Name 2020-02-18T22-49-08.131Z", "description": "Copies AMI to eu-west-2 and exports to S3" }, { "region": "eu-west-2", "image": "ami-a1b2c3d4567890ab", "name": "My 6 image 2020-02-18T22-49-08.131Z", "description": "Copies AMI to eu-west-2 and exports to S3" } ] }, "tags": {} }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/5", "name": "MyBasicRecipe", "version": "2019.12.03/5", "platform": "Windows", "state": { "status": "AVAILABLE" }, "owner": "123456789012", "dateCreated": "2020-02-18T16:51:48.403Z", "outputResources": { "amis": [ { "region": "us-west-2", "image": "ami-a1b2c3d4567890ab", "name": "MyBasicRecipe 2020-02-18T16-52-18.965Z", "description": "This example image recipe creates a Windows 2016 image." } ] }, "tags": {} }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/4", "name": "MyBasicRecipe", "version": "2019.12.03/4", "platform": "Windows", "state": { "status": "AVAILABLE" }, "owner": "123456789012", "dateCreated": "2020-02-18T16:50:01.827Z", "outputResources": { "amis": [ { "region": "us-west-2", "image": "ami-a1b2c3d4567890ab", "name": "MyBasicRecipe 2020-02-18T16-50-32.280Z", "description": "This example image recipe creates a Windows 2016 image." } ] }, "tags": {} }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/3", "name": "MyBasicRecipe", "version": "2019.12.03/3", "platform": "Windows", "state": { "status": "AVAILABLE" }, "owner": "123456789012", "dateCreated": "2020-02-14T23:14:13.597Z", "outputResources": { "amis": [ { "region": "us-west-2", "image": "ami-a1b2c3d4567890ab", "name": "MyBasicRecipe 2020-02-14T23-14-44.243Z", "description": "This example image recipe creates a Windows 2016 image." } ] }, "tags": {} }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/2", "name": "MyBasicRecipe", "version": "2019.12.03/2", "platform": "Windows", "state": { "status": "FAILED", "reason": "SSM execution 'a1b2c3d4-5678-90ab-cdef-EXAMPLE11111' failed with status = 'Failed' and failure message = 'Step fails when it is verifying the command has completed. Command a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 returns unexpected invocation result: \n{Status=[Failed], ResponseCode=[1], Output=[\n----------ERROR-------\nfailed to run commands: exit status 1], OutputPayload=[{\"Status\":\"Failed\",\"ResponseCode\":1,\"Output\":\"\\n----------ERROR-------\\nfailed to run commands: exit status 1\",\"CommandId\":\"a1b2c3d4-5678-90ab-cdef-EXAMPLE11111\"}], CommandId=[a1b2c3d4-5678-90ab-cdef-EXAMPLE11111]}. Please refer to Automation Service Troubleshooting Guide for more diagnosis details.'" }, "owner": "123456789012", "dateCreated": "2020-02-14T22:57:42.593Z", "outputResources": { "amis": [] }, "tags": {} } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListImageBuildVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-build-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-image-pipeline-images`.

- **AWS CLI**
- 
            
                    **To list image pipeline pipeline images**The following `list-image-pipeline-images`example lists all images that were created by a specific image pipeline.`aws imagebuilder list-image-pipeline-images \ --image-pipeline-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imagePipelineList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline", "name": "MyWindows2016Pipeline", "description": "Builds Windows 2016 Images", "platform": "Windows", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03", "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution", "imageTestsConfiguration": { "imageTestsEnabled": true, "timeoutMinutes": 60 }, "schedule": { "scheduleExpression": "cron(0 0 * * SUN)", "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE" }, "status": "ENABLED", "dateCreated": "2020-02-19T19:04:01.253Z", "dateUpdated": "2020-02-19T19:04:01.253Z", "tags": { "KeyName": "KeyValue" } }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/sam", "name": "PipelineName", "platform": "Linux", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/recipe-name-a1b2c3d45678/1.0.0", "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/infrastructureconfiguration-name-a1b2c3d45678", "imageTestsConfiguration": { "imageTestsEnabled": true, "timeoutMinutes": 720 }, "status": "ENABLED", "dateCreated": "2019-12-16T18:19:02.068Z", "dateUpdated": "2019-12-16T18:19:02.068Z", "tags": { "KeyName": "KeyValue" } } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListImagePipelineImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-pipeline-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-image-recipes`.

- **AWS CLI**
- 
            
                    **To list image recipes**The following `list-image-recipes`example lists all of your image recipes.`aws imagebuilder list-image-recipes`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imageRecipeSummaryList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03", "name": "MyBasicRecipe", "platform": "Windows", "owner": "123456789012", "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/windows-server-2016-english-full-base-x86/2019.x.x", "dateCreated": "2020-02-19T18:54:25.975Z", "tags": { "KeyName": "KeyValue" } }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/recipe-name-a1b2c3d45678/1.0.0", "name": "recipe-name-a1b2c3d45678", "platform": "Linux", "owner": "123456789012", "parentImage": "arn:aws:imagebuilder:us-west-2:aws:image/amazon-linux-2-x86/2019.11.21", "dateCreated": "2019-12-16T18:19:00.120Z", "tags": { "KeyName": "KeyValue" } } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListImageRecipes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-image-recipes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-images`.

- **AWS CLI**
- 
            
                    **To list images**The following `list-images`example lists all of the semantic versions you have access to.`aws imagebuilder list-images`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imageVersionList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03", "name": "MyBasicRecipe", "version": "2019.12.03", "platform": "Windows", "owner": "123456789012", "dateCreated": "2020-02-14T21:29:18.810Z" } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-infrastructure-configurations`.

- **AWS CLI**
- 
            
                    **To list infrastructure configurations**The following `list-infrastructure-configurations`example lists all of your infrastructure configurations.`aws imagebuilder list-infrastructure-configurations`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "infrastructureConfigurationSummaryList": [ { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "name": "MyExampleInfrastructure", "description": "An example that will retain instances of failed builds", "dateCreated": "2020-02-19T19:11:51.858Z", "tags": {} }, { "arn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/infrastructureconfiguration-name-a1b2c3d45678", "name": "infrastructureConfiguration-name-a1b2c3d45678", "dateCreated": "2019-12-16T18:19:01.038Z", "tags": { "KeyName": "KeyValue" } } ] }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListInfrastructureConfigurations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-infrastructure-configurations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a specific resource**The following `list-tags-for-resource`example lists all of the tags for a specific resource.`aws imagebuilder list-tags-for-resource \ --resource-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline`Output: `{ "tags": { "KeyName": "KeyValue" } }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-component-policy`.

- **AWS CLI**
- 
            
                    **To apply a resource policy to a component**The following `put-component-policy`command applies a resource policy to a build component to enable cross-account sharing of build components. We recommend you use the RAM CLI command`create-resource-share`. If you use the EC2 Image Builder CLI command`put-component-policy`, you must also use the RAM CLI command`promote-resource-share-create-from-policy`in order for the resource to be visible to all principals with whom the resource is shared.`aws imagebuilder put-component-policy \ --component-arn``arn:aws:imagebuilder:us-west-2:123456789012:component/examplecomponent/2019.12.02/1`\ --policy '`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetComponent", "imagebuilder:ListComponents" ], "Resource": [ "arn:aws:imagebuilder:us-west-2:123456789012:component/examplecomponent/2019.12.02/1" ] } ] }`'Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "componentArn": "arn:aws:imagebuilder:us-west-2:123456789012:component/examplecomponent/2019.12.02/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [PutComponentPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/put-component-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-image-policy`.

- **AWS CLI**
- 
            
                    **To apply a resource policy to an image**The following `put-image-policy`command applies a resource policy to an image to enable cross-account sharing of images. We recommend you use the RAM CLI command create-resource-share. If you use the EC2 Image Builder CLI command put-image-policy, you must also use the RAM CLI command promote-resource-share-create-from-policy in order for the resource to be visible to all principals with whom the resource is shared.`aws imagebuilder put-image-policy \ --image-arn``arn:aws:imagebuilder:us-west-2:123456789012:image/example-image/2019.12.02/1`\ --policy '`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetImage", "imagebuilder:ListImages" ], "Resource": [ "arn:aws:imagebuilder:us-west-2:123456789012:image/example-image/2019.12.02/1" ] } ] }`'Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imageArn": "arn:aws:imagebuilder:us-west-2:123456789012:image/example-image/2019.12.02/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [PutImagePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/put-image-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-image-recipe-policy`.

- **AWS CLI**
- 
            
                    **To apply a resource policy to an image recipe**The following `put-image-recipe-policy`command applies a resource policy to an image recipe to enable cross-account sharing of image recipes. We recommend that you use the RAM CLI command`create-resource-share`. If you use the EC2 Image Builder CLI command`put-image-recipe-policy`, you must also use the RAM CLI command`promote-resource-share-create-from-policy`in order for the resource to be visible to all principals with whom the resource is shared.`aws imagebuilder put-image-recipe-policy \ --image-recipe-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/example-image-recipe/2019.12.02`\ --policy '`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": [ "123456789012" ] }, "Action": [ "imagebuilder:GetImageRecipe", "imagebuilder:ListImageRecipes" ], "Resource": [ "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/example-image-recipe/2019.12.02" ] } ] }`'Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/example-image-recipe/2019.12.02/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [PutImageRecipePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/put-image-recipe-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-image-pipeline-execution`.

- **AWS CLI**
- 
            
                    **To start an image pipeline manually**The following `start-image-pipeline-execution`example manually starts an image pipeline.`aws imagebuilder start-image-pipeline-execution \ --image-pipeline-arn``arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "clientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "imageBuildVersionArn": "arn:aws:imagebuilder:us-west-2:123456789012:image/mybasicrecipe/2019.12.03/1" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [StartImagePipelineExecution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/start-image-pipeline-execution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example adds and tags a resource to EC2 Image Builder using a JSON file.`aws imagebuilder tag-resource \ --cli-input-json``file://tag-resource.json`Contents of `tag-resource.json`:`{ "resourceArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline", "tags": { "KeyName: "KeyValue" } }`This command produces no output. For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resource`example removes a tag from a resource using a JSON file.`aws imagebuilder untag-resource \ --cli-input-json``file://tag-resource.json`Contents of `untag-resource.json`:`{ "resourceArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline", "tagKeys": [ "KeyName" ] }`This command produces no output. For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-distribution-configuration`.

- **AWS CLI**
- 
            
                    **To update a distribution configuration**The following `update-distribution-configuration`example updates a distribution configuration using a JSON file.`aws imagebuilder update-distribution-configuration \ --cli-input-json``file://update-distribution-configuration.json`Contents of `update-distribution-configuration.json`:`{ "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution", "description": "Copies AMI to eu-west-2 and exports to S3", "distributions": [ { "region": "us-west-2", "amiDistributionConfiguration": { "name": "Name {{imagebuilder:buildDate}}", "description": "An example image name with parameter references" } }, { "region": "eu-west-2", "amiDistributionConfiguration": { "name": "My {{imagebuilder:buildVersion}} image {{imagebuilder:buildDate}}" } } ] }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [UpdateDistributionConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-distribution-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-image-pipeline`.

- **AWS CLI**
- 
            
                    **To update an image pipeline**The following `update-image-pipeline`example updates an image pipeline using a JSON file.`aws imagebuilder update-image-pipeline \ --cli-input-json``file://update-image-pipeline.json`Contents of `update-image-pipeline.json`:`{ "imagePipelineArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-pipeline/mywindows2016pipeline", "imageRecipeArn": "arn:aws:imagebuilder:us-west-2:123456789012:image-recipe/mybasicrecipe/2019.12.03", "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "distributionConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:distribution-configuration/myexampledistribution", "imageTestsConfiguration": { "imageTestsEnabled": true, "timeoutMinutes": 120 }, "schedule": { "scheduleExpression": "cron(0 0 * * MON)", "pipelineExecutionStartCondition": "EXPRESSION_MATCH_AND_DEPENDENCY_UPDATES_AVAILABLE" }, "status": "DISABLED" }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [UpdateImagePipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-image-pipeline.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-infrastructure-configuration`.

- **AWS CLI**
- 
            
                    **To update an infrastructure configuration**The following `update-infrastructure-configuration`example updates an infrastructure configuration using a JSON file.`aws imagebuilder update-infrastructure-configuration \ --cli-input-json``file:/update-infrastructure-configuration.json`Contents of `update-infrastructure-configuration.json`:`{ "infrastructureConfigurationArn": "arn:aws:imagebuilder:us-west-2:123456789012:infrastructure-configuration/myexampleinfrastructure", "description": "An example that will terminate instances of failed builds", "instanceTypes": [ "m5.large", "m5.2xlarge" ], "instanceProfileName": "EC2InstanceProfileForImageFactory", "securityGroupIds": [ "sg-a48c95ef" ], "subnetId": "subnet-a48c95ef", "logging": { "s3Logs": { "s3BucketName": "bucket-name", "s3KeyPrefix": "bucket-path" } }, "terminateInstanceOnFailure": true, "snsTopicArn": "arn:aws:sns:us-west-2:123456789012:sns-name" }`Output: `{ "requestId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }`For more information, see [Setting Up and Managing an EC2 Image Builder Image Pipeline Using the AWS CLI](https://docs.aws.amazon.com/imagebuilder/latest/userguide/managing-image-builder-cli.html)in the*EC2 Image Builder Users Guide*.- 
                    For API details, see [UpdateInfrastructureConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/update-infrastructure-configuration.html)in*AWS CLI Command Reference*.
 
-