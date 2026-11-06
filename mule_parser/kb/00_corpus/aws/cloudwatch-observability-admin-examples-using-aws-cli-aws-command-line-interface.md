# CloudWatch Observability Admin examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_observabilityadmin_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_observabilityadmin_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudWatch Observability Admin.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `get-telemetry-evaluation-status-for-organization`.

- **AWS CLI**
- 
            
                    **To get telemetry onboarding status for the organization**The following `get-telemetry-evaluation-status-for-organization`example returns the current onboarding status of the telemetry config feature for the organization.`aws observabilityadmin get-telemetry-evaluation-status-for-organization`Output: `{ "Status": "RUNNING" }`For more information, see [Auditing CloudWatch telemetry configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetTelemetryEvaluationStatusForOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/get-telemetry-evaluation-status-for-organization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-telemetry-evaluation-status`.

- **AWS CLI**
- 
            
                    **To get telemetry onboarding status for the account**The following `get-telemetry-evaluation-status`example returns the current onboarding status of the telemetry config feature in the specified account.`aws observabilityadmin get-telemetry-evaluation-status`Output: `{ "Status": "RUNNING" }`For more information, see [Auditing CloudWatch telemetry configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [GetTelemetryEvaluationStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/get-telemetry-evaluation-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-telemetry-for-organization`.

- **AWS CLI**
- 
            
                    **To retrieve the telemetry configurations for the organization**The following `list-resource-telemetry-for-organization`example returns a list of telemetry configurations in the organization for AWS resources supported by telemetry config.`aws observabilityadmin list-resource-telemetry-for-organization \ --resource-types``AWS::EC2::Instance`Output: `{ "TelemetryConfigurations": [ { "AccountIdentifier": "111111111111", "TelemetryConfigurationState": { "Logs": "NotApplicable", "Metrics": "Disabled", "Traces": "NotApplicable" }, "ResourceType": "AWS::EC2::Instance", "ResourceIdentifier": "i-a166400b", "ResourceTags": { "Name": "dev" }, "LastUpdateTimeStamp": 1733168548521 }, { "AccountIdentifier": "222222222222", "TelemetryConfigurationState": { "Logs": "NotApplicable", "Metrics": "Disabled", "Traces": "NotApplicable" }, "ResourceType": "AWS::EC2::Instance", "ResourceIdentifier": "i-b188560f", "ResourceTags": { "Name": "apache" }, "LastUpdateTimeStamp": 1732744260182 } ] }`For more information, see [Auditing CloudWatch telemetry configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListResourceTelemetryForOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/list-resource-telemetry-for-organization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-resource-telemetry`.

- **AWS CLI**
- 
            
                    **To retrieve the telemetry configurations for the account**The following `list-resource-telemetry`example returns a list of telemetry configurations for AWS resources supported by telemetry config in the specified account.`aws observabilityadmin list-resource-telemetry \ --resource-types``AWS::EC2::Instance`Output: `{ "TelemetryConfigurations": [ { "AccountIdentifier": "111111111111", "TelemetryConfigurationState": { "Logs": "NotApplicable", "Metrics": "Disabled", "Traces": "NotApplicable" }, "ResourceType": "AWS::EC2::Instance", "ResourceIdentifier": "i-0e979d278b040f856", "ResourceTags": { "Name": "apache" }, "LastUpdateTimeStamp": 1732744260182 } ] }`For more information, see [Auditing CloudWatch telemetry configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [ListResourceTelemetry](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/list-resource-telemetry.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-telemetry-evaluation-for-organization`.

- **AWS CLI**
- 
            
                    **To enable the telemetry config feature**The following `start-telemetry-evaluation-for-organization`example enables the telemetry config feature for the organization.`aws observabilityadmin start-telemetry-evaluation-for-organization`This command produces no output. For more information, see [Turning on CloudWatch telemetry auditing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-on.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StartTelemetryEvaluationForOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/start-telemetry-evaluation-for-organization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-telemetry-evaluation`.

- **AWS CLI**
- 
            
                    **To enable the telemetry config feature**The following `start-telemetry-evaluation`example enables the telemetry config feature in the specified account.`aws observabilityadmin start-telemetry-evaluation`This command produces no output. For more information, see [Turning on CloudWatch telemetry auditing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-on.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StartTelemetryEvaluation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/start-telemetry-evaluation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-telemetry-evaluation-for-organization`.

- **AWS CLI**
- 
            
                    **To disable the telemetry config feature**The following `stop-telemetry-evaluation-for-organization`example disables the telemetry config feature for the organization.`aws observabilityadmin stop-telemetry-evaluation-for-organization`This command produces no output. For more information, see [Turning off CloudWatch telemetry auditing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-off.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StopTelemetryEvaluationForOrganization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/stop-telemetry-evaluation-for-organization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-telemetry-evaluation`.

- **AWS CLI**
- 
            
                    **To disable the telemetry config feature**The following `stop-telemetry-evaluation`example disables the telemetry config feature in the specified account.`aws observabilityadmin stop-telemetry-evaluation`This command produces no output. For more information, see [Turning off CloudWatch telemetry auditing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-off.html)in the*Amazon CloudWatch User Guide*.- 
                    For API details, see [StopTelemetryEvaluation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/observabilityadmin/stop-telemetry-evaluation.html)in*AWS CLI Command Reference*.
 
-