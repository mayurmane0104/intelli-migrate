# Monitoring performance - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/monitoring-performance.html](https://docs.aws.amazon.com/quick/latest/userguide/monitoring-performance.html)

---

Amazon Quick Automate provides comprehensive monitoring capabilities that help you track performance, audit and troubleshoot your automations. This section describes how to use the performance monitoring features in Amazon Quick Automate.

## Prerequisites

        Before using the Performance dashboard, you need:

- Active automations - At least one automation must be run to see metrics 
- Automation group access - Permission to view the automation groups you want to monitor 

## Automation summary dashboard

        The Automations tab provides high-level metrics and key performance indicators across your automation portfolio.

### Automation summary charts

The dashboard includes three main performance visualizations:

- **Automation Distribution**- Shows the number of deployed automations organized by automation group, helping you understand your automation footprint across the organization
- **Success Rate**- Displays the percentage of cases that completed successfully versus those that encountered exceptions, providing insight into automation reliability
- **Time Savings**- Calculates total hours saved based on successful case completions multiplied by the estimated time savings configured for each automation project

### Automation details table

Each automation is listed with key metrics and status information:

- **Automation name**- Name and version of the deployed automation
- **Latest run**- Most recent execution status and timestamp
- **Case metrics**- Count of cases processed, broken down by:- Successfully completed cases 
- Cases with business exceptions 
- Cases with system exceptions 
 
- **Tasks**- Number of human-in-the-loop tasks created by the automation

## Runs dashboard

        The Runs tab provides detailed visibility into individual automation executions and their outcomes.

### Run statuses

Automations can be in one of these run statuses:

- **Waiting**- The automation is queued and awaiting available system resources to begin execution. This is typically a brief transitional state.
- **In Progress**- The automation is actively executing its configured steps. You can monitor real-time progress through the logs.
- **Completed**- The automation has finished all steps successfully.
- **Failed**- The automation encountered an error it could not recover from and stopped execution. Detailed error information is available in the logs.
- **Stopped**- A user manually interrupted the automation execution using either the Exit or Terminate action.

###### Note

Count of incomplete runs includes Waiting and In Progress.

### Run details table

Each run provides comprehensive execution information through the following columns:

- **Status**- Current run status (as defined in Run Status Types)
- **Automation**- Name of the automation being run
- **Version**- Specific version number of the automation which ran
- **Start time**- When the automation run began
- **End time**- When the automation completed or stopped
- **Duration**- Total running time of the automation
- **Case metrics**- Count of cases processed, broken down by:- Successfully completed cases 
- Cases with business exceptions 
- Cases with system exceptions 
 
- **Tasks**- Number of human-in-the-loop tasks created in the run

###### Note

Data is refreshed when first navigating to the page. Click the refresh button to pull the latest data at any point.

## Cases dashboard

        The Cases tab enables tracking of individual case records through their lifecycle.

### Case charts

The dashboard includes two main performance visualizations:

- **Total cases created**- Shows the number of cases created over time, helping you understand your automation volumes.
- **Top exceptions**- Displays the top 5 exception reasons and the relative count of each, helping you prioritize your optimization efforts to improve success rates.

### Case statuses

Cases can be in one of these processing statuses:

- **Ready**- The case has been created and is waiting to be picked up for processing. This is the initial state of all new cases.
- **In Progress**- The case is actively being processed by the automation. You can monitor real-time progress through the logs.
- **Pending Resolution**- The case is waiting for a human-in-the-loop task to be completed before processing can continue. Cases move back to Ready status after tasks are resolved.
- **Successful**- The case has completed without any exceptions.
- **Failed**- The case encountered one of the following exception types:- **Business Exception**- The case encountered a handled business rule violation and stopped processing. Detailed exception information is available in the logs.
- **System Exception**- The case experienced a technical error and stopped processing. Detailed error information is available in the logs.
 

For detailed information about case handling and orchestration patterns, see [Orchestration actions](https://docs.aws.amazon.com/actions-orchestration.html).

## Search and filtering

        The Performance dashboard includes search and filtering capabilities available across all monitoring views to help you find specific information. Filter by:

- Time range 
- Status 
- Automation group 
- Automation 

###### Note

You can also search on the cases page by reference name or exception reason.

### Environment selection

Switch between viewing metrics from:

- Test - Data from automation testing in development environment 
- Deployed - Data from deployed automations 

###### Note

Your selected environment applies across all dashboard tabs until changed.

## CloudWatch

        Amazon CloudWatch provides monitoring and observability capabilities for your automations in Amazon Quick Automate. This section explains the metrics available in CloudWatch, how to view the metrics, and how to set up alarms for these metrics.

### Prerequisites

#### IAM roles and permissions

To grant CloudWatch access following least-privilege principles:

- Create an IAM role or group, preferably using AWS IAM Identity Center. 
- Attach the AWS managed policy CloudWatchFullAccess for full monitoring and alarm capabilities. 
- Optionally, add CloudWatchLogsReadOnlyAccess for log querying without deletion permissions. 
- Assign users to this role or group to enable CloudWatch operations without broader administrative access. 

For detailed step-by-step instructions, see [Getting setup in CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html) and [CloudWatch permissions guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/auth-and-access-control-cw.html).

#### Accessing CloudWatch

- Navigate to the AWS Management Console. 
- Enter CloudWatch in the services search bar. 
- Choose CloudWatch from the results to open the CloudWatch console. 

### Accessing CloudWatch metrics for Amazon Quick Automate

- Open the CloudWatch console. 
- In the left navigation pane, choose - **Metrics**,- **All metrics**.
- Choose the service namespace - **QuickSight**.
- Choose the relevant dimensions, - **AutomationGroupId**or- **AutomationId**, to view the metrics.
- Use the search bar to search or filter by metric name or dimension. 

For more detailed information, see the [CloudWatch metrics documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html).

### Available metrics

Amazon Quick Automate publishes metrics to CloudWatch under the **QuickSight** namespace. Metrics are grouped by either **AutomationId** or **AutomationGroupId** dimensions.

###### Note

CloudWatch is a Regional service. To view metrics, ensure that you are in the same AWS Region where your automations run.

#### AutomationId metrics

These metrics track individual automation performance:

- **FailedAutomationRunCount**- The total number of automation runs that failed during execution. Use this metric to identify problematic automations that require attention or debugging.
- **SuccessfulAutomationRunCount**- The total number of automation runs that completed successfully. Use this metric to track automation reliability and success rates.
- **AutomationRunDuration**- The time taken for each automation run to complete. Use this metric to identify performance bottlenecks and optimize automation efficiency.
- **StoppedAutomationRunCount**- The number of automation runs that were manually stopped or terminated before completion. This can indicate user intervention or system-initiated stops.
- **TotalAutomationRunCount**- The aggregate count of all automation runs, regardless of status. Use this metric to monitor overall automation activity and usage patterns.

#### AutomationGroupId metrics

These metrics provide a broader view across all cases:

- **TotalCaseCount**- The total number of cases processed by the automation system. Use this metric to track overall workload volume.
- **CompletedCaseCount**- The number of cases that were successfully processed and completed. Use this metric to measure throughput and productivity.
- **FailedCaseCount**- The number of cases that failed during processing. Use this metric to identify systemic issues or patterns in failures.
- **CaseDuration**- The time taken to process cases from start to completion. Use this metric to assess overall system performance and identify opportunities for optimization.

#### Finding AutomationId and AutomationGroupId

To find the AutomationId and AutomationGroupId for your automation:

- Sign in to Amazon Quick Automate. 
- In the left navigation pane, choose - **Automations**.
- Choose the automation group that contains your automation. 
- Choose the automation name to open the automation. 
- Choose the - **Deployments**tab.
- Choose the - **Actions (⋮)**and- **View deployment details**to get the- **Automation ID**and- **Group ID**at the top just below the heading Deployment Details.

#### Setting up CloudWatch alarms

Use these metrics to monitor the health of your automations or set up alarms in CloudWatch. For example, you can create alarms for the following conditions:

- More than five automation runs fail within a specified period. 
- More than 10 cases fail within a specified period. 
- Case duration exceeds 30 minutes. 

For more information about creating alarms, see [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create-Alarms.html).