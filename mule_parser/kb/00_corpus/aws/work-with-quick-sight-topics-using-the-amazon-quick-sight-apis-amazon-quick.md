# Work with Quick Sight topics using the Amazon Quick Sight APIs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topics-cli.html](https://docs.aws.amazon.com/quick/latest/userguide/topics-cli.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

Use this section to learn how to work with Quick Sight topics using the Amazon Quick Sight command line interface (CLI).

**Prerequisites**

Before you begin, make sure that you have an AWS Identity and Access Management (IAM) role that grants the CLI user access to call the Quick Sight API operations. The following table shows which permissions must be added to the IAM policy to use specific API operations. To use all of the topic API operations, add all of the permissions listed in the table.

| API operation | IAM policy | 
|---|---|
| 
 | 
 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 
| 
 | 
 | 

The following example shows an IAM policy that allows a user to use the
                `ListTopics` API operation.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "quicksight:ListTopics" ], "Resource": "*" } ] }`

After you configure the permissions to create Quick Sight topics with the Quick Sight APIs, use the following topics to create and work with Quick Sight topic APIs.