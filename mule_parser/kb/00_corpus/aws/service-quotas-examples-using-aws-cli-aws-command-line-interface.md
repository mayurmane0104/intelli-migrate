# Service Quotas examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_service-quotas_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_service-quotas_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Service Quotas.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `get-aws-default-service-quota`.

- **AWS CLI**
- 
            
                    **To describe a default service quota**The following `get-aws-default-service-quota`example displays details for the specified quota.`aws service-quotas get-aws-default-service-quota \ --service-code``ec2`\ --quota-code`L-1216C47A`Output: `{ "Quota": { "ServiceCode": "ec2", "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)", "QuotaArn": "arn:aws:servicequotas:us-east-2::ec2/L-1216C47A", "QuotaCode": "L-1216C47A", "QuotaName": "Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances", "Value": 5.0, "Unit": "None", "Adjustable": true, "GlobalQuota": false, "UsageMetric": { "MetricNamespace": "AWS/Usage", "MetricName": "ResourceCount", "MetricDimensions": { "Class": "Standard/OnDemand", "Resource": "vCPU", "Service": "EC2", "Type": "Resource" }, "MetricStatisticRecommendation": "Maximum" } } }`- 
                    For API details, see [GetAwsDefaultServiceQuota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-aws-default-service-quota.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-requested-service-quota-change`.

- **AWS CLI**
- 
            
                    **To describe a service quota increase request**The following `get-requested-service-quota-change`example describes the specified quota increase request.`aws service-quotas get-requested-service-quota-change \ --request-id``d187537d15254312a9609aa51bbf7624u7W49tPO`Output: `{ "RequestedQuota": { "Id": "d187537d15254312a9609aa51bbf7624u7W49tPO", "CaseId": "6780195351", "ServiceCode": "ec2", "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)", "QuotaCode": "L-20F13EBD", "QuotaName": "Running Dedicated c5n Hosts", "DesiredValue": 2.0, "Status": "CASE_OPENED", "Created": 1580446904.067, "LastUpdated": 1580446953.265, "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}", "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:ec2/L-20F13EBD", "GlobalQuota": false, "Unit": "None" } }`- 
                    For API details, see [GetRequestedServiceQuotaChange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-requested-service-quota-change.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-service-quota`.

- **AWS CLI**
- 
            
                    **To describe a service quota**The following `get-service-quota`example displays details about the specified quota.`aws service-quotas get-service-quota \ --service-code``ec2`\ --quota-code`L-1216C47A`Output: `{ "Quota": { "ServiceCode": "ec2", "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)", "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:ec2/L-1216C47A", "QuotaCode": "L-1216C47A", "QuotaName": "Running On-Demand Standard (A, C, D, H, I, M, R, T, Z) instances", "Value": 1920.0, "Unit": "None", "Adjustable": true, "GlobalQuota": false, "UsageMetric": { "MetricNamespace": "AWS/Usage", "MetricName": "ResourceCount", "MetricDimensions": { "Class": "Standard/OnDemand", "Resource": "vCPU", "Service": "EC2", "Type": "Resource" }, "MetricStatisticRecommendation": "Maximum" } } }`- 
                    For API details, see [GetServiceQuota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-service-quota.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-aws-default-service-quotas`.

- **AWS CLI**
- 
            
                    **To list the default quotas for a service**The following `list-aws-default-service-quotas`example lists the default values for the quotas for the specified service.`aws service-quotas list-aws-default-service-quotas \ --service-code``xray`Output: `{ "Quotas": [ { "ServiceCode": "xray", "ServiceName": "AWS X-Ray", "QuotaArn": "arn:aws:servicequotas:us-west-2::xray/L-C6B6F05D", "QuotaCode": "L-C6B6F05D", "QuotaName": "Indexed annotations per trace", "Value": 50.0, "Unit": "None", "Adjustable": false, "GlobalQuota": false }, { "ServiceCode": "xray", "ServiceName": "AWS X-Ray", "QuotaArn": "arn:aws:servicequotas:us-west-2::xray/L-D781C0FD", "QuotaCode": "L-D781C0FD", "QuotaName": "Segment document size", "Value": 64.0, "Unit": "Kilobytes", "Adjustable": false, "GlobalQuota": false }, { "ServiceCode": "xray", "ServiceName": "AWS X-Ray", "QuotaArn": "arn:aws:servicequotas:us-west-2::xray/L-998BFF16", "QuotaCode": "L-998BFF16", "QuotaName": "Trace and service graph retention in days", "Value": 30.0, "Unit": "None", "Adjustable": false, "GlobalQuota": false } ] }`- 
                    For API details, see [ListAwsDefaultServiceQuotas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-aws-default-service-quotas.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-requested-service-quota-change-history-by-quota`.

- **AWS CLI**
- 
            
                    **To list your quota increase requests**The following `list-requested-service-quota-change-history-by-quota`example lists the quota increase requests for the specified quota.`aws service-quotas list-requested-service-quota-change-history-by-quota \ --service-code``ec2`\ --quota-code`L-20F13EBD`Output: `{ "RequestedQuotas": [ { "Id": "d187537d15254312a9609aa51bbf7624u7W49tPO", "CaseId": "6780195351", "ServiceCode": "ec2", "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)", "QuotaCode": "L-20F13EBD", "QuotaName": "Running Dedicated c5n Hosts", "DesiredValue": 2.0, "Status": "CASE_OPENED", "Created": 1580446904.067, "LastUpdated": 1580446953.265, "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}", "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:ec2/L-20F13EBD", "GlobalQuota": false, "Unit": "None" } ] }`- 
                    For API details, see [ListRequestedServiceQuotaChangeHistoryByQuota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-requested-service-quota-change-history-by-quota.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-requested-service-quota-change-history`.

- **AWS CLI**
- 
            
                    **To list your quota increase requests**The following `list-requested-service-quota-change-history`example lists the quota increase requests for the specified service.`aws service-quotas list-requested-service-quota-change-history \ --service-code``ec2`Output: `{ "RequestedQuotas": [ { "Id": "d187537d15254312a9609aa51bbf7624u7W49tPO", "CaseId": "6780195351", "ServiceCode": "ec2", "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)", "QuotaCode": "L-20F13EBD", "QuotaName": "Running Dedicated c5n Hosts", "DesiredValue": 2.0, "Status": "CASE_OPENED", "Created": 1580446904.067, "LastUpdated": 1580446953.265, "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}", "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:ec2/L-20F13EBD", "GlobalQuota": false, "Unit": "None" } ] }`- 
                    For API details, see [ListRequestedServiceQuotaChangeHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-requested-service-quota-change-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-service-quotas`.

- **AWS CLI**
- 
            
                    **To list the quotas for a service**The following `list-service-quotas`example displays details about the quotas for AWS CloudFormation.`aws service-quotas list-service-quotas \ --service-code``cloudformation`Output: `{ "Quotas": [ { "ServiceCode": "cloudformation", "ServiceName": "AWS CloudFormation", "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:cloudformation/L-87D14FB7", "QuotaCode": "L-87D14FB7", "QuotaName": "Output count in CloudFormation template", "Value": 60.0, "Unit": "None", "Adjustable": false, "GlobalQuota": false }, { "ServiceCode": "cloudformation", "ServiceName": "AWS CloudFormation", "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:cloudformation/L-0485CB21", "QuotaCode": "L-0485CB21", "QuotaName": "Stack count", "Value": 200.0, "Unit": "None", "Adjustable": true, "GlobalQuota": false } ] }`- 
                    For API details, see [ListServiceQuotas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-service-quotas.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-services`.

- **AWS CLI**
- 
            
                    **To list the available services**The following command lists the services that are available in Service Quotas. `aws service-quotas list-services`Output: `{ "Services": [ { "ServiceCode": "AWSCloudMap", "ServiceName": "AWS Cloud Map" }, { "ServiceCode": "access-analyzer", "ServiceName": "Access Analyzer" }, { "ServiceCode": "acm", "ServiceName": "AWS Certificate Manager (ACM)" }, ...truncated... { "ServiceCode": "xray", "ServiceName": "AWS X-Ray" } ] }`You can add the `--query`parameter to filter the display to the information that you are interested in. The following example displays only the service codes.`aws service-quotas list-services \ --query``Services[*].ServiceCode`Output: `[ "AWSCloudMap", "access-analyzer", "acm", "acm-pca", "amplify", "apigateway", "application-autoscaling", ...truncated... "xray" ]`- 
                    For API details, see [ListServices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-services.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `request-service-quota-increase`.

- **AWS CLI**
- 
            
                    **To request a service quota increase**The following `request-service-quota-increase`example requests an increase in the specified service quota.`aws service-quotas request-service-quota-increase \ --service-code``ec2`\ --quota-code`L-20F13EBD`\ --desired-value`2`Output: `{ "RequestedQuota": { "Id": "d187537d15254312a9609aa51bbf7624u7W49tPO", "ServiceCode": "ec2", "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)", "QuotaCode": "L-20F13EBD", "QuotaName": "Running Dedicated c5n Hosts", "DesiredValue": 2.0, "Status": "PENDING", "Created": 1580446904.067, "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}", "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:ec2/L-20F13EBD", "GlobalQuota": false, "Unit": "None" } }`- 
                    For API details, see [RequestServiceQuotaIncrease](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html)in*AWS CLI Command Reference*.
 
-