# AWS service action connectors - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/builtin-services-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/builtin-services-integration.html)

---

With AWS service action connectors in Amazon Quick, you can create action connectors that interact directly with AWS services like Amazon Bedrock, Amazon Textract, and Amazon Comprehend. These connectors enable automated workflows that leverage AWS AI and machine learning capabilities.

## What you can do

        
        AWS service action connectors enable you to integrate powerful AWS capabilities into your automated workflows. For example, you can use Amazon Bedrock to generate content with foundation models, Amazon Textract to extract text and data from documents, or Amazon Comprehend to analyze sentiment and extract insights from text. These action connectors allow you to build sophisticated automation workflows that combine multiple AWS services for document processing, content generation, and data analysis—all while maintaining security through IAM role-based authentication.

###### Note

AWS services action connectors can only be used with Amazon Quick Automate because they require an IAM identity for authentication. These connectors are created through the admin console and provide direct access to AWS service APIs.

## Supported AWS services

        
        Amazon Quick supports the following AWS services for action connectors:

- 
                **Amazon Bedrock Agent**- Invoke Bedrock agents for complex AI workflows.
- 
                **Amazon Bedrock Runtime**- Access foundation models for text generation and conversation.
- 
                **Amazon Bedrock Data Automation**- Automate data processing workflows with AI.
- 
                **Amazon Comprehend**- Analyze text for sentiment, entities, and key phrases.
- 
                **Amazon Comprehend Medical**- Extract medical information from healthcare text.
- 
                **Amazon Textract**- Extract text and data from documents and images.
- 
                **Amazon S3**- Manage objects and buckets in S3.

## Before you begin

        
        Before you set up an AWS service action connectors, make sure you have the following:

- 
                AWS account with access to the desired AWS services. 
- 
                IAM role with appropriate permissions for the AWS services you want to use. 
- 
                Amazon Quick Admin access to create action connectors. 
- 
                Amazon Quick Automate access to use the action connectors in workflows. 

## Prepare IAM role and permissions

        
        Before setting up the action connectors in Amazon Quick, prepare your IAM role with the necessary permissions for the AWS services you want to use.

### Required IAM permissions

Configure your IAM role with the appropriate permissions based on the AWS services you plan to use. Make sure your IAM role includes a trust policy that allows Amazon Quick to assume the role for executing actions.

### IAM Role for Resource Access

First, you will need to create an IAM role that will be used by Amazon Quick to call the AWS service needed in your Amazon Quick Automate workflow.

- 
                    Log in to the AWS Console of the AWS account where the Amazon Quick subscription resides. 
- 
                    Open IAM and create a new IAM role. 
- 
                    Give it all the permissions for the AWS service you want to invoke via action connectors. For example, you can assign a managed policy like `AmazonS3FullAccess`if you need to invoke Amazon S3.
- 
                    In the trust relationship, give the assume role permission to `quicksight.amazonaws.com`. This allows Amazon Quick to assume this role and call AWS services on your behalf.
- 
                    Once the Customer Role is created, take a note of the IAM role ARN. 

Example trust policy:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "quicksight.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
## Create AWS services action connector

        
        After preparing your IAM role and permissions, follow these steps to set up AWS Actions in Quick Suite.

###### Note

You need administrative access to Amazon Quick Suite to perform the following steps. See documentation on [Configure Amazon Quick subscriptions](./managing-qbs-subscriptions.html) to learn more.

### Steps to create a new AWS integration

- 
                    Choose the **profile icon**, then select**Manage Quick Suite**.
- 
                    Select **AWS actions**under the**Permissions**section.
- 
                    Choose **New Action**to create a new AWS integration.
- 
                    Choose one of the **supported AWS services**.
- 
                    Select **Next**to review available actions for this service.
- 
                    Select **Next**to configure the connection details:- 
                            **Name**– Enter a descriptive name for your integration.
- 
                            **Description**– Optionally, add notes about how this integration will be used.
- 
                            **Role ARN**– Enter the ARN of the IAM role to be used for this AWS service.
 
- 
                            
- 
                    Select **Next**to share the integration with users and/or user groups.- 
                            Provide **Owner access**for any users who need to edit, share, and delete the integration.###### NoteOwner access is required to add integrations to Automation Groups in order to give access within Quick Automate. 
- 
                            Provide **User access**for any users who need to invoke actions across Quick Suite.For a list of integrations supported in various Quick Suite capabilities, see [Action connector compatibility matrix](./action-connector-apis-supported-types.html#action-connector-compatibility-matrix).
 
- 
                            
- 
                    Select **Add**to finish creating the integration.See [Integration workflows](./integration-workflows.html)to learn more.

## Next steps

        
        After creating your action integration, you can:

- 
                Share the integration with additional users or groups as needed. 
- 
                Add the integration to an **Automation Group**in order to use it in Quick Automate. See[Setup tasks](./getting-started-quick-automate.html#automate-setup-tasks)for more details.
- 
                Monitor the integration's usage and performance through the admin console. 
- 
                Update the integration's configuration or permissions as requirements change.