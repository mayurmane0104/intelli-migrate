# Deploying automations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/deploying-automations.html](https://docs.aws.amazon.com/quick/latest/userguide/deploying-automations.html)

---

After you create and test your automations in Amazon Quick Automate, the next step is to **deploy** them so they can run regularly on a trigger. Deployment makes the automation operational and ready for execution. You can add a trigger to a deployed automation to run it at a predefined schedule. Deployment involves configuring runtime settings, assigning users for human-in-the-loop tasks, verifying credentials and integrations.

This section explains each step of the deployment process and how to configure your automation for reliability, security, and optimal performance.

## Prerequisites

        Before deploying your automation, ensure that the following steps are complete:

- **Automation is tested thoroughly**- Validate your automation through end-to-end testing to confirm that all logic, actions, and agent interactions work as expected.
- **Version committed for deployment**- Only committed automation versions can be deployed. Review your changes, finalize the version, and commit it before proceeding.
- **Integrations configured**- If your automation interacts with external applications such as Salesforce or Jira via APIs, make sure all necessary integrations are configured.- Navigate to - **Connections → Integrations**in the left panel to create new integrations.
- Currently, only integrations available under the - **Actions**tab are supported in Amazon Quick Automate.
- Once an integration action is created, associate it with the - **Automation Group**where it will be used.
- The associated actions will then appear in the canvas. During deployment, you can select the appropriate connection to be used by the deployed automation. 
 
- **Credentials configured**- Verify that all credentials required by your automation are correctly set up.

## Deploying an automation

        You can deploy an automation directly from the Canvas by clicking Deploy, or by navigating to the Deployment tab on the automation's landing page. Once you initiate deployment, the system guides you through a series of steps to complete the configuration and release process.

### Release details

On the **Release Details** page, select the version of the automation you want to deploy. Only **committed versions** are available for deployment and will appear in the dropdown list.

### Additional settings

Additional settings include:

- **Runtime configuration**
- **Tasks (for HITL assignments)**
- **Access**

#### Runtime configuration

Runtime configurations are parameters that may differ between environments such as development, testing, and production.

For example, an automation step that sends an email may use your personal email address during testing but should switch to a shared team address in production. Such environment-dependent values can be defined as **runtime configurations** when authoring the automation.

At deployment time, you can review and override these configurations to ensure the automation runs correctly in the intended environment. Runtime parameters can include:

- Email addresses or notification recipients 
- File paths or URLs specific to the environment 

This flexibility helps maintain a single automation definition across environments while adapting key parameters as needed.

#### Tasks

Select the resolver users or user groups for each of the tasks that require human-in-the-loop.

#### Access (Credentials and Connections)

Automations often need to connect to external systems, databases, or services. Amazon Quick Automate provides secure methods for managing credentials and connections without embedding sensitive information within your automation logic.

Connection and credential data are securely stored and encrypted, and made available to workflows at runtime without exposing them to authors or end users. This design ensures strong separation of secrets from automation definitions, improving both security and maintainability.

You can store and use two primary types of credentials:

- **Website credentials**- Used for UI automation steps that require website logins (username and password).
- **Action credentials (Integrations)**- Used for connecting AWS services (e.g. S3) or external systems through configured integrations (e.g., Salesforce, Jira).

At deployment, ensure that the correct credentials and connections are selected so the automation can access all required systems securely and successfully.

## Setting up triggers

        Triggers determine when and how your automations run. You can configure automations to start based on a predefined schedule or invoke them programmatically through the Amazon QuickSight API.

### Schedules

You can configure automations to start based on a predefined schedule. To setup a trigger:

- On the Deployment page, click "Create Trigger" and configure the rules. 
- Select the frequency 
- Select the start date and time (Note that the actual execution will initiate within 15 minutes of the start time selected) 
- Select the end date and time 
- Select the timezone 
- Amazon Quick Automate provided built-in scalability. Select the number of parallel executions of the automation (you can select a maximum of 10 parallel executions per trigger and 50 across all automations within an account. Please reach out to AWS) 
- For complex scheduling needs, you can use cron expressions to define precise running patterns. For example, to run an automation at 2:30 AM every Monday, Wednesday, and Friday, you would use the cron expression: - `30 2 * * 1,3,5`.

### API triggers

The Automation Job APIs enable you to programmatically start and monitor automation jobs from external applications. You can use these APIs to invoke deployed automations with custom input payloads and retrieve execution results through the AWS SDK and AWS CLI.

The Automation Job APIs include two operations:

- **StartAutomationJob**– Starts a new job for a deployed automation with an optional input payload.
- **DescribeAutomationJob**– Retrieves the status, timestamps, and optional input and output payloads for a specified job.

These APIs are part of the Amazon QuickSight service namespace. You access them through the `quicksight` namespace in the AWS SDK and AWS CLI.

For more information about AWS SDKs and toolkits, see the [AWS Getting Started Resource Center](https://aws.amazon.com/getting-started/tools-sdks/).

#### Prerequisites

Before you call the Automation Job APIs, complete the following setup steps.

##### Find your automation identifiers

To call the Automation Job APIs, you need the following identifiers:

- **AWS account ID**– Your 12-digit AWS account ID.
- **Automation group ID**– The unique ID of the automation group that contains your automation.
- **Automation ID**– The unique ID of the automation you want to invoke.

You can find the automation group ID and automation ID in the Deployments section when you open any automation and have a deployed version.

**To find your identifiers**

- Sign in to Amazon Quick Automate. 
- In the left navigation pane, choose - **Automations**.
- Choose the automation group that contains your automation. 
- Choose the automation name to open the automation editor. 
- Choose the - **Deployments**tab.
- Choose the - **Actions (⋮)**and- **View deployment details**to get the- **Automation ID**and- **Group ID**at the top just below the heading Deployment Details.

##### Configure IAM permissions

The Automation Job APIs require IAM permissions attached to your IAM identity (user, role, or group). Each operation requires a separate permission.

**Permission for StartAutomationJob**

Attach a policy that grants the `quicksight:StartAutomationJob` action. Scope the resource ARN to the specific automation that you want to allow.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowStartAutomationJob",
            "Effect": "Allow",
            "Action": [
                "quicksight:StartAutomationJob"
            ],
            "Resource": [
                "arn:aws:quicksight:us-west-2:111122223333:automation-group/EXAMPLE-GROUP-ID/automation/EXAMPLE-AUTOMATION-ID"
            ]
        }
    ]
}
```
**Permission for DescribeAutomationJob**

Attach a policy that grants the `quicksight:DescribeAutomationJob` action. The resource ARN for this operation includes the job ID segment. To allow describing any job under an automation, use a wildcard (*) for the job segment.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowDescribeAutomationJob",
            "Effect": "Allow",
            "Action": [
                "quicksight:DescribeAutomationJob"
            ],
            "Resource": [
                "arn:aws:quicksight:us-west-2:111122223333:automation-group/EXAMPLE-GROUP-ID/automation/EXAMPLE-AUTOMATION-ID"
            ]
        }
    ]
}
```
AWS recommends scoping each permission to the most specific resource ARN possible to follow the principle of least privilege. For more information, see the following:

##### Deploy your automation

The StartAutomationJob API targets deployed automations only. You must commit and deploy your automation in the Amazon Quick Automate console before you can invoke it through the API.

#### StartAutomationJob

Starts a new job for a deployed automation. The operation is asynchronous — Amazon Quick Automate accepts the request, queues the job, and returns a **JobId** immediately. The automation runs in the background. If the automation has an input schema defined, Amazon Quick Automate validates the **InputPayload** against the schema before accepting the job. An invalid payload results in an **InvalidParameterValueException**.

##### Request syntax

`POST /accounts/``AwsAccountId`/automation-groups/`AutomationGroupId`/automations/`AutomationId`/jobs HTTP/1.1 Content-type: application/json { "InputPayload": "string" }

##### Request parameters

- **AwsAccountId**(String, required) – Your AWS account ID (12 digits).
- **AutomationGroupId**(String, required) – The ID of the automation group (UUID).
- **AutomationId**(String, required) – The ID of the automation to run (UUID).
- **InputPayload**(String, optional) – Input for the job as a JSON string.

##### Response elements

- **Arn**(String) – ARN of the automation job.
- **JobId**(String) – ID of the started job. Use this with- `DescribeAutomationJob`to track status.
- **Status**(Integer) – HTTP status code of the response.
- **RequestId**(String) – AWS request ID.

##### Errors

- **AccessDeniedException**– Insufficient permissions or invalid credentials.
- **InvalidParameterValueException**– One or more parameters has a value that isn't valid.
- **ResourceNotFoundException**– Automation group or automation not found.
- **LimitExceededException**– A limit is exceeded.
- **ThrottlingException**– Request was throttled.
- **InternalFailureException**– Internal service error.

For more details, see the [API reference guide for StartAutomationJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_StartAutomationJob.html).

#### DescribeAutomationJob

Retrieves the status and details of a specified automation job, including execution timestamps and optional input and output payloads. Use this operation to poll for job completion after calling **StartAutomationJob**.

The response does not include input and output payloads by default. Set the **IncludeInputPayload** and **IncludeOutputPayload** query parameters to `true` to request them. Amazon Quick Automate returns the output payload only when all of the following conditions are met:

- **IncludeOutputPayload**is- `true`.
- **JobStatus**is- `SUCCEEDED`.
- The automation produced output values. 

##### Request syntax

`GET /accounts/``AwsAccountId`/automation-groups/`AutomationGroupId`/automations/`AutomationId`/jobs/`JobId`?IncludeInputPayload=`boolean`&IncludeOutputPayload=`boolean`HTTP/1.1

##### Request parameters

- **AwsAccountId**(String, required) – Your AWS account ID (12 digits).
- **AutomationGroupId**(String, required) – The ID of the automation group (UUID).
- **AutomationId**(String, required) – The ID of the automation (UUID).
- **JobId**(String, required) – The ID of the job returned by- `StartAutomationJob`(UUID).
- **IncludeInputPayload**(Boolean, optional) – Include the input payload in the response. Default:- `false`.
- **IncludeOutputPayload**(Boolean, optional) – Include the output payload in the response. Default:- `false`.

##### Response fields

- **Arn**(String) – ARN of the automation job.
- **CreatedAt**(Timestamp) – When the job was created (epoch seconds).
- **StartedAt**(Timestamp) – When the job started running (epoch seconds).
- **EndedAt**(Timestamp) – When the job finished (epoch seconds).
- **JobStatus**(String) –- `QUEUED`,- `RUNNING`,- `SUCCEEDED`,- `FAILED`, or- `STOPPED`.
- **InputPayload**(String) – The input payload. Omitted from response unless- `IncludeInputPayload`is- `true`.
- **OutputPayload**(String) – The output payload. Omitted from response unless- `IncludeOutputPayload`is- `true`.
- **RequestId**(String) – AWS request ID.

##### Errors

- **AccessDeniedException**– Insufficient permissions or invalid credentials.
- **InvalidParameterValueException**– One or more parameters has a value that isn't valid.
- **ResourceNotFoundException**– Job, automation, or automation group not found.
- **ThrottlingException**– Request was throttled.
- **InternalFailureException**– Internal service error.

For more details, see the [API reference guide for DescribeAutomationJob](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeAutomationJob.html).

## Run automations with API triggers using input and output

        You can include input values as a JSON payload when you start an automation job through the API. Amazon Quick Automate validates the payload against the automation's input schema before execution begins, and returns structured output values when the job completes.

### Prerequisites

Before you run an automation with API triggers, make sure the following are in place:

- The automation is deployed. 
- The automation has an input schema defined in the Start node. 
- You have the automation group ID and automation ID. 

### Sending input values through the API

To include input values, pass a JSON payload in the **StartAutomationJob** request using the **InputPayload** parameter.

```
Sample Request
POST /accounts/123456789012/automation-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/automations/11111111-2222-3333-4444-555555555555/jobs
{
    "InputPayload": "{\"customer_id\":\"C-98765\",\"threshold\":100,\"region\":\"us-east-1\"}"
}
Sample Response
{
    "Arn": "arn:aws:quicksight:us-west-2:123456789012:automation-group/a1b2c3d4-e5f6-7890-abcd-ef1234567890/automation/11111111-2222-3333-4444-555555555555/job/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "JobId": "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "Status": 200,
    "RequestId": "req-12345678-abcd-efgh-ijkl-123456789012"
}
```
###### Note

The `InputPayload` value must be a JSON-serialized string that contains the input field values matching your automation's input schema.

### Retrieving output values through the API

You can retrieve output values by calling the **DescribeAutomationJob** API. To include input and output payloads in the response, set the **includeInputPayload** and **includeOutputPayload** query parameters to `true`.

The response includes the **OutputPayload** field only when the automation completes successfully.

```
Sample Request
GET /accounts/123456789012/automation-groups/a1b2c3d4-e5f6-7890-abcd-ef1234567890/automations/11111111-2222-3333-4444-555555555555/jobs/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee?includeInputPayload=true&includeOutputPayload=true
Sample Response
{
    "Arn": "arn:aws:quicksight:us-west-2:123456789012:automation-group/a1b2c3d4-e5f6-7890-abcd-ef1234567890/automation/11111111-2222-3333-4444-555555555555/job/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
    "JobStatus": "SUCCEEDED",
    "CreatedAt": "2026-03-11T09:59:50Z",
    "StartedAt": "2026-03-11T10:00:00Z",
    "EndedAt": "2026-03-11T10:05:00Z",
    "InputPayload": "{\"customer_id\":\"C-98765\",\"threshold\":100,\"region\":\"us-east-1\"}",
    "OutputPayload": "{\"result\":\"success\",\"records_processed\":42,\"summary\":{\"passed\":40,\"failed\":2}}",
    "RequestId": "req-12345678-abcd-efgh-ijkl-123456789012"
}
```
###### Note

The **OutputPayload** field is available only after the automation completes successfully (when **JobStatus** is `SUCCEEDED`). If the automation fails or is still running, the response does not include the **OutputPayload** field.

## Deploy and run automations with inputs and outputs

        This section describes how to deploy automations that use input and output schemas, run them manually or on a schedule, and view run results.

### View schema information before deployment

Before deploying an automation, you must commit it to create a version. For more information, see [maintaining automation versions](https://docs.aws.amazon.com/quicksuite/latest/userguide/building-automations.html#managing-automation-versions).

After you commit an automation with input or output schemas, you can view the schema details in the **Data model** section of the version details page. This section displays the complete field definitions for both inputs and outputs.

### Deploy automations with input and output schemas

When you deploy an automation that has input or output schemas defined, the deployment dialog box displays schema information in the **Data model** section, including:

- Input and output field definitions (name, data type, description, required or optional status, and default values). 
- Copyable JSON schemas for inputs and outputs that API callers can use for integration. 

###### Important

The schema is frozen at deployment time along with the automation code. If you update the schema after deployment, you must redeploy the automation for the changes to take effect.

To complete the deployment, review the schema information and choose **Deploy**.

### Run deployed automations manually

To start a deployed automation with inputs, complete the following steps:

- On the deployment page, choose the - **Actions**menu (⋮).
- Choose - **Run now**.
- In the - **Provide input values**dialog box, enter values for each input field.
- Choose - **Start**to start the automation run.

The input form is identical to the one you use when you test in Studio.

### Run automations with scheduled triggers

For scheduled triggers, you provide input values when you create or edit the trigger. The stored values are passed to the automation each time the trigger fires.

You can do the following:

- Create multiple triggers with different input values for the same automation 
- Edit input values for a trigger without redeploying the automation 

To configure inputs for a scheduled trigger, complete the following steps:

- Navigate to the deployment page for your automation. 
- Choose - **Create Trigger**.
- In - **Step 1: Set Trigger**, configure the schedule.
- In - **Step 2: Define Run**, enter values for each input field in the auto-generated form.
- Choose - **Next**, review your configuration, and choose- **Create Trigger**.

###### Note

If you create a trigger with a specific schema version and later deploy the automation with an updated schema, you must modify the trigger. The trigger becomes incompatible when the schema version changes and the automation runs will fail.

### Viewing inputs and outputs for deployed runs

After an automation run completes (whether started manually or by a scheduled trigger), input and output values are available as structured artifacts in the logs panel on the **Runs** page.

The artifacts appear as dedicated cards:

- **Input artifact**– Displays at the top of the logs panel
- **Output artifact**– Displays at the bottom of the logs panel (only available if the automation completes successfully)

Both cards are collapsed by default. When you expand them, you can:

- View the complete schema and actual values 
- Download any file objects included in the inputs or outputs 
- Copy the structured data as JSON 
- Download the complete payload as a JSON file