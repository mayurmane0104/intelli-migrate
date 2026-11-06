# Snowball Edge examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_snowball_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_snowball_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Snowball Edge.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `get-snowball-usage`.

- **AWS CLI**
- 
            
                    **To get information about the Snowball service limit for your account**The following `get-snowball-usage`example displays information about the Snowball service limit for your account, and also the number of Snowballs your account has in use.`aws snowball get-snowball-usage`Output: `{ "SnowballLimit": 1, "SnowballsInUse": 0 }`FOR more information, see [AWS Snowball Edge Limits](https://docs.aws.amazon.com/snowball/latest/developer-guide/limits.html)in the*AWS Snowball Developer Guide*.- 
                    For API details, see [GetSnowballUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/get-snowball-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-jobs`.

- **AWS CLI**
- 
            
                    **To list the current Snowball jobs in your account**The following `list-jobs`example displays an array of`JobListEntry`objects. In this example, a single job is listed.`aws snowball list-jobs`Output: `{ "JobListEntries": [ { "CreationDate": 2016-09-27T14:50Z, "Description": "Important Photos 2016-08-11", "IsMaster": TRUE, "JobId": "ABCd1e324fe-022f-488e-a98b-3b0566063db1", "JobState": "Complete", "JobType": "IMPORT", "SnowballType": "EDGE" } ] }`For more information, see [Jobs for AWS Snowball Edge devices](https://docs.aws.amazon.com/snowball/latest/developer-guide/jobs.html)in the*AWS Snowball Developer Guide*.- 
                    For API details, see [ListJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snowball/list-jobs.html)in*AWS CLI Command Reference*.
 
-