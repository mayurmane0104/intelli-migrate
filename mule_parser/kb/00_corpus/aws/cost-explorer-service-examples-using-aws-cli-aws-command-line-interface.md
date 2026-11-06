# Cost Explorer Service examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cost-explorer_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cost-explorer_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Cost Explorer Service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `get-cost-and-usage`.

- **AWS CLI**
- 
            
                    **To retrieve the S3 usage of an account for the month of September 2017**The following `get-cost-and-usage`example retrieves the S3 usage of an account for the month of September 2017.`aws ce get-cost-and-usage \ --time-period``Start=2017-09-01,End=2017-10-01`\ --granularity`MONTHLY`\ --metrics`"BlendedCost"``"UnblendedCost"``"UsageQuantity"`\ --group-by`Type=DIMENSION,Key=SERVICE``Type=TAG,Key=Environment`\ --filter`file://filters.json`Contents of `filters.json`:`{ "Dimensions": { "Key": "SERVICE", "Values": [ "Amazon Simple Storage Service" ] } }`Output: `{ "GroupDefinitions": [ { "Type": "DIMENSION", "Key": "SERVICE" }, { "Type": "TAG", "Key": "Environment" } ], "ResultsByTime": [ { "Estimated": false, "TimePeriod": { "Start": "2017-09-01", "End": "2017-10-01" }, "Total": {}, "Groups": [ { "Keys": [ "Amazon Simple Storage Service", "Environment$" ], "Metrics": { "BlendedCost": { "Amount": "40.3527508453", "Unit": "USD" }, "UnblendedCost": { "Amount": "40.3543773134", "Unit": "USD" }, "UsageQuantity": { "Amount": "9312771.098461578", "Unit": "N/A" } } }, { "Keys": [ "Amazon Simple Storage Service", "Environment$Dev" ], "Metrics": { "BlendedCost": { "Amount": "0.2682364644", "Unit": "USD" }, "UnblendedCost": { "Amount": "0.2682364644", "Unit": "USD" }, "UsageQuantity": { "Amount": "22403.4395271182", "Unit": "N/A" } } } ] } ] }`- 
                    For API details, see [GetCostAndUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-cost-and-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-dimension-values`.

- **AWS CLI**
- 
            
                    **To retrieve the tags for the dimension SERVICE, with a value of "Elastic"**This example retrieves the tags for the dimension SERVICE, with a value of "Elastic" for January 01 2017 through May 18 2017. Command: `aws ce get-dimension-values --search-string``Elastic`--time-period`Start=2017-01-01,End=2017-05-18`--dimension`SERVICE`Output: `{ "TotalSize": 6, "DimensionValues": [ { "Attributes": {}, "Value": "Amazon ElastiCache" }, { "Attributes": {}, "Value": "EC2 - Other" }, { "Attributes": {}, "Value": "Amazon Elastic Compute Cloud - Compute" }, { "Attributes": {}, "Value": "Amazon Elastic Load Balancing" }, { "Attributes": {}, "Value": "Amazon Elastic MapReduce" }, { "Attributes": {}, "Value": "Amazon Elasticsearch Service" } ], "ReturnSize": 6 }`- 
                    For API details, see [GetDimensionValues](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-dimension-values.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reservation-coverage`.

- **AWS CLI**
- 
            
                    **To retrieve the reservation coverage for EC2 t2.nano instances in the us-east-1 region**This example retrieves the reservation coverage for EC2 t2.nano instances in the us-east-1 region for July-September of 2017. Command: `aws ce get-reservation-coverage --time-period``Start=2017-07-01,End=2017-10-01`--group-by`Type=Dimension,Key=REGION`--filter`file://filters.json`filters.json: `{ "And": [ { "Dimensions": { "Key": "INSTANCE_TYPE", "Values": [ "t2.nano" ] }, "Dimensions": { "Key": "REGION", "Values": [ "us-east-1" ] } } ] }`Output: `{ "TotalSize": 6, "DimensionValues": [ { "Attributes": {}, "Value": "Amazon ElastiCache" }, { "Attributes": {}, "Value": "EC2 - Other" }, { "Attributes": {}, "Value": "Amazon Elastic Compute Cloud - Compute" }, { "Attributes": {}, "Value": "Amazon Elastic Load Balancing" }, { "Attributes": {}, "Value": "Amazon Elastic MapReduce" }, { "Attributes": {}, "Value": "Amazon Elasticsearch Service" } ], "ReturnSize": 6 }`- 
                    For API details, see [GetReservationCoverage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-coverage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reservation-purchase-recommendation`.

- **AWS CLI**
- 
            
                    **To retrieve the reservation recommendations for Partial Upfront EC2 RIs with a three year term**The following `get-reservation-purchase-recommendation`example retrieves recommendations for Partial Upfront EC2 instances with a three-year term, based on the last 60 days of EC2 usage.`aws ce get-reservation-purchase-recommendation \ --service``"Amazon Redshift"`\ --lookback-period-in-days`SIXTY_DAYS`\ --term-in-years`THREE_YEARS`\ --payment-option`PARTIAL_UPFRONT`Output: `{ "Recommendations": [], "Metadata": { "GenerationTimestamp": "2018-08-08T15:20:57Z", "RecommendationId": "00d59dde-a1ad-473f-8ff2-iexample3330b" } }`- 
                    For API details, see [GetReservationPurchaseRecommendation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-purchase-recommendation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reservation-utilization`.

- **AWS CLI**
- 
            
                    **To retrieve the reservation utilization for your account**The following `get-reservation-utilization`example retrieves the RI utilization for all t2.nano instance types from 2018-03-01 to 2018-08-01 for the account.`aws ce get-reservation-utilization \ --time-period``Start=2018-03-01,End=2018-08-01`\ --filter`file://filters.json`Contents of `filters.json`:`{ "Dimensions": { "Key": "INSTANCE_TYPE", "Values": [ "t2.nano" ] } }`Output: `{ "Total": { "TotalAmortizedFee": "0", "UtilizationPercentage": "0", "PurchasedHours": "0", "NetRISavings": "0", "TotalActualHours": "0", "AmortizedRecurringFee": "0", "UnusedHours": "0", "TotalPotentialRISavings": "0", "OnDemandCostOfRIHoursUsed": "0", "AmortizedUpfrontFee": "0" }, "UtilizationsByTime": [] }`- 
                    For API details, see [GetReservationUtilization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-reservation-utilization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-tags`.

- **AWS CLI**
- 
            
                    **To retrieve keys and values for a cost allocation tag**This example retrieves all cost allocation tags with a key of "Project" and a value that contains "secretProject". Command: `aws ce get-tags --search-string``secretProject`--time-period`Start=2017-01-01,End=2017-05-18`--tag-key`Project`Output: `{ "ReturnSize": 2, "Tags": [ "secretProject1", "secretProject2" ], "TotalSize": 2 }`- 
                    For API details, see [GetTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/get-tags.html)in*AWS CLI Command Reference*.
 
-