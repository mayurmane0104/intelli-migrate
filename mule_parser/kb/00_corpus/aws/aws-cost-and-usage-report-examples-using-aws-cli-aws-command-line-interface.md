# AWS Cost and Usage Report examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cost-and-usage-report-service_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cost-and-usage-report-service_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Cost and Usage Report.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-report-definition`.

- **AWS CLI**
- 
            
                    **To delete an AWS Cost and Usage Report**This example deletes an AWS Cost and Usage Report. Command: `aws cur --region``us-east-1``delete-report-definition`--report-name`"ExampleReport"`- 
                    For API details, see [DeleteReportDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/delete-report-definition.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-report-definitions`.

- **AWS CLI**
- 
            
                    **To retrieve a list of AWS Cost and Usage Reports**This example describes a list of AWS Cost and Usage Reports owned by an account. Command: `aws cur --region``us-east-1``describe-report-definitions`--max-items`5`Output: `{ "ReportDefinitions": [ { "ReportName": "ExampleReport", "Compression": "ZIP", "S3Region": "us-east-1", "Format": "textORcsv", "S3Prefix": "exampleprefix", "S3Bucket": "example-s3-bucket", "TimeUnit": "DAILY", "AdditionalArtifacts": [ "REDSHIFT", "QUICKSIGHT" ], "AdditionalSchemaElements": [ "RESOURCES" ] } ] }`- 
                    For API details, see [DescribeReportDefinitions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/describe-report-definitions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-report-definition`.

- **AWS CLI**
- 
            
                    **To create an AWS Cost and Usage Reports**The following `put-report-definition`example creates a daily AWS Cost and Usage Report that you can upload into Amazon Redshift or Amazon QuickSight.`aws cur put-report-definition --report-definition``file://report-definition.json`Contents of `report-definition.json`:`{ "ReportName": "ExampleReport", "TimeUnit": "DAILY", "Format": "textORcsv", "Compression": "ZIP", "AdditionalSchemaElements": [ "RESOURCES" ], "S3Bucket": "example-s3-bucket", "S3Prefix": "exampleprefix", "S3Region": "us-east-1", "AdditionalArtifacts": [ "REDSHIFT", "QUICKSIGHT" ] }`- 
                    For API details, see [PutReportDefinition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/put-report-definition.html)in*AWS CLI Command Reference*.
 
-