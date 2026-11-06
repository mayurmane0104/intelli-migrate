# AWS Serverless Application Repository examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_serverlessapplicationrepository_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_serverlessapplicationrepository_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Serverless Application Repository.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `put-application-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To share an application publicly**The following `put-application-policy`shares an application publicly, so anyone can find and deploy your application in the AWS Serverless Application Repository.`aws serverlessrepo put-application-policy \ --application-id``arn:aws:serverlessrepo:us-east-1:123456789012:applications/my-test-application`\ --statements Principals='*',Actions=DeployOutput: `{ "Statements": [ { "Actions": [ "Deploy" ], "Principals": [ "" ], "StatementId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" } ] }`**Example 2:**To share an application privatelyThe following `put-application-policy`shares an application privately, so only specific AWS accounts can find and deploy your application in the AWS Serverless Application Repository.`aws serverlessrepo put-application-policy \ --application-id``arn:aws:serverlessrepo:us-east-1:123456789012:applications/my-test-application`\ --statements`Principals=111111111111,222222222222,Actions=Deploy`Output: `{ "Statements": [ { "Actions": [ "Deploy" ], "Principals": [ "111111111111", "222222222222" ], "StatementId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" } ] }`For more information, see [Sharing an Application Through the Console](https://docs.aws.amazon.com/serverlessrepo/latest/devguide/serverlessrepo-how-to-publish.html#share-application)in the*AWS Serverless Application Repository Developer Guide*- 
                    For API details, see [PutApplicationPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/put-application-policy.html)in*AWS CLI Command Reference*.
 
-