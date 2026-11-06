# EventBridge examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_eventbridge_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_eventbridge_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with EventBridge.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-rule`.

- **AWS CLI**
- 
            
                    **To delete a CloudWatch Events rule**This example deletes the rule named EC2InstanceStateChanges: `aws events delete-rule --name``"EC2InstanceStateChanges"`- 
                    For API details, see [DeleteRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-rule`.

- **AWS CLI**
- 
            
                    **To display information about a CloudWatch Events rule**This example displays information about the rule named DailyLambdaFunction: `aws events describe-rule --name``"DailyLambdaFunction"`- 
                    For API details, see [DescribeRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/describe-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-rule`.

- **AWS CLI**
- 
            
                    **To disable a CloudWatch Events rule**This example disables the rule named DailyLambdaFunction. The rule is not deleted: `aws events disable-rule --name``"DailyLambdaFunction"`- 
                    For API details, see [DisableRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/disable-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-rule`.

- **AWS CLI**
- 
            
                    **To enable a CloudWatch Events rule**This example enables the rule named DailyLambdaFunction, which had been previously disabled: `aws events enable-rule --name``"DailyLambdaFunction"`- 
                    For API details, see [EnableRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/enable-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-rule-names-by-target`.

- **AWS CLI**
- 
            
                    **To display all the rules that have a specified target**This example displays all rules that have the Lambda function named "MyFunctionName" as the target: `aws events list-rule-names-by-target --target-arn``"arn:aws:lambda:us-east-1:123456789012:function:MyFunctionName"`- 
                    For API details, see [ListRuleNamesByTarget](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rule-names-by-target.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-rules`.

- **AWS CLI**
- 
            
                    **To display a list of all CloudWatch Events rules**This example displays all CloudWatch Events rules in the region: `aws events list-rules`**To display a list of CloudWatch Events rules beginning with a certain string.**This example displays all CloudWatch Events rules in the region that have a name starting with "Daily": `aws events list-rules --name-prefix``"Daily"`- 
                    For API details, see [ListRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-targets-by-rule`.

- **AWS CLI**
- 
            
                    **To display all the targets for a CloudWatch Events rule**This example displays all the targets of the rule named DailyLambdaFunction: `aws events list-targets-by-rule --rule``"DailyLambdaFunction"`- 
                    For API details, see [ListTargetsByRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-targets-by-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-events`.

- **AWS CLI**
- 
            
                    **To send a custom event to CloudWatch Events**This example sends a custom event to CloudWatch Events. The event is contained within the putevents.json file: `aws events put-events --entries``file://putevents.json`Here are the contents of the putevents.json file: `[ { "Source": "com.mycompany.myapp", "Detail": "{ \"key1\": \"value1\", \"key2\": \"value2\" }", "Resources": [ "resource1", "resource2" ], "DetailType": "myDetailType" }, { "Source": "com.mycompany.myapp", "Detail": "{ \"key1\": \"value3\", \"key2\": \"value4\" }", "Resources": [ "resource1", "resource2" ], "DetailType": "myDetailType" } ]`- 
                    For API details, see [PutEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-rule`.

- **AWS CLI**
- 
            
                    **To create CloudWatch Events rules**This example creates a rule that triggers every day at 9:00am (UTC). If you use put-targets to add a Lambda function as a target of this rule, you could run the Lambda function every day at the specified time: `aws events put-rule --name``"DailyLambdaFunction"`--schedule-expression`"cron(0 9 * * ? *)"`This example creates a rule that triggers when any EC2 instance in the region changes state: `aws events put-rule --name``"EC2InstanceStateChanges"`--event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"]}" --role-arn`"arn:aws:iam::123456789012:role/MyRoleForThisRule"`This example creates a rule that triggers when any EC2 instance in the region is stopped or terminated: `aws events put-rule --name``"EC2InstanceStateChangeStopOrTerminate"`--event-pattern "{\"source\":[\"aws.ec2\"],\"detail-type\":[\"EC2 Instance State-change Notification\"],\"detail\":{\"state\":[\"stopped\",\"terminated\"]}}" --role-arn`"arn:aws:iam::123456789012:role/MyRoleForThisRule"`- 
                    For API details, see [PutRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-targets`.

- **AWS CLI**
- 
            
                    **To add targets for CloudWatch Events rules**This example adds a Lambda function as the target of a rule: `aws events put-targets --rule``DailyLambdaFunction`--targets "Id"="1","Arn"="arn:aws:lambda:us-east-1:123456789012:function:MyFunctionName"This example sets an Amazon Kinesis stream as the target, so that events caught by this rule are relayed to the stream: `aws events put-targets --rule``EC2InstanceStateChanges`--targets "Id"="1","Arn"="arn:aws:kinesis:us-east-1:123456789012:stream/MyStream","RoleArn"="arn:aws:iam::123456789012:role/MyRoleForThisRule"This example sets two Amazon Kinesis streams as targets for one rule: `aws events put-targets --rule``DailyLambdaFunction`--targets "Id"="Target1","Arn"="arn:aws:kinesis:us-east-1:379642911888:stream/MyStream1","RoleArn"="arn:aws:iam::379642911888:role/ MyRoleToAccessLambda" "Id"="Target2"," Arn"="arn:aws:kinesis:us-east-1:379642911888:stream/MyStream2","RoleArn"="arn:aws:iam::379642911888:role/MyRoleToAccessLambda"- 
                    For API details, see [PutTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-targets`.

- **AWS CLI**
- 
            
                    **To remove a target for an event**This example removes the Amazon Kinesis stream named MyStream1 from being a target of the rule DailyLambdaFunction. When DailyLambdaFunction was created, this stream was set as a target with an ID of Target1: `aws events remove-targets --rule``"DailyLambdaFunction"`--ids`"Target1"`- 
                    For API details, see [RemoveTargets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/remove-targets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-event-pattern`.

- **AWS CLI**
- 
            
                    **To check whether an event pattern matches a specified event**This example tests whether the pattern "source:com.mycompany.myapp" matches the specified event. In this example, the output would be "true": `aws events test-event-pattern --event-pattern "{\"source\":[\"com.mycompany.myapp\"]}" --event "{\"id\":\"1\",\"source\":\"com.mycompany.myapp\",\"detail-type\":\"myDetailType\",\"account\":\"123456789012\",\"region\":\"us-east-1\",\"time\":\"2017-04-11T20:11:04Z\"}"`- 
                    For API details, see [TestEventPattern](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/test-event-pattern.html)in*AWS CLI Command Reference*.
 
-