# Orchestration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/actions-orchestration.html](https://docs.aws.amazon.com/quick/latest/userguide/actions-orchestration.html)

---

Orchestration enables you to automate complex end-to-end processes, coordinating automated tasks with human decisions where needed. The orchestration capabilities in Amazon Quick Automate include case management for tracking work items and human-in-the-loop integration for incorporating human judgment.

## Case management

        Cases track individual items of work for your automation to process such as a new claim, an IT support ticket, a customer complaint, or a new invoice. Each case has:

- A unique reference name (e.g., "Order-12345") 
- A case type for grouping related work (e.g., "Sales orders") 
- Custom data stored as key-value pairs 
- A defined lifecycle with status tracking and an audit trail 
- Associated human-in-the-loop tasks if applicable 

### Case status lifecycle

To track the progress of work through your automation, cases follow a defined lifecycle with specific status transitions:

- `Ready`- The case has been created and is waiting to be picked up for processing. This is the initial state of all new cases.
- `In Progress`- The case is actively being processed by the automation. You can monitor real-time progress through the logs.
- `Pending Resolution`- The case is waiting for a human-in-the-loop task to be completed before processing can continue. Cases automatically move back to Ready status after tasks are resolved.
- `Successful`- The case has completed all processing steps without any exceptions.
- `Failed`- The case encountered one of the following exception types:- Business Exception - The case encountered a handled business rule violation and stopped processing. Detailed exception information is available in the logs. 
- System Exception - The case experienced a technical error and stopped processing. Detailed error information is available in the logs. 
 

### Actions

Amazon Quick Automate provides the following actions to create, process, and manage cases throughout their lifecycle.

- Create new case
- 
                        Creates a single case to track work. Each case has a reference name (e.g., "Order-12345") and stores custom data as key-value pairs. Cases are grouped by type (e.g., "Sales orders") for organization and reporting. Properties: - `Title`(optional) - Action name shown in the process visualization (e.g., "Create sales order case")
- `Reference name`(required) - Business identifier used for searching and tracking cases in monitoring dashboards (e.g., "Order-12345")
- `Case type`(required) - Label that groups related cases by business purpose. Provides organization and metric tracking (e.g., "Sales orders", "Support tickets")
- `Custom data`(required) - Additional case information stored as key-value pairs. This data is visible to users and can be retrieved, updated, or appended to during case processing (e.g., {"Product": "ABC-12345", "Qty": "100", "Priority": "High"})
 
- Create multiple cases
- 
                        Bulk creates cases from a data table. Each row becomes a new case, inheriting the specified case type and using a designated column for reference names. All other columns become custom data fields. Properties: - `Title`(optional) - Action name shown in the process visualization (e.g., "Create cases from invoice batch")
- `Case type`(required) - Label that groups related cases by business purpose (e.g., "Invoice processing")
- `Cases data table`(required) - Data table where each row creates a new case. All columns are stored as custom data (e.g., cases_table)
- `Reference column name`(required) - Name of the column containing the reference name identifier for each case (e.g., "Invoice number")
 
- Process cases
- 
                        Loops through cases in 'Ready' status. Automatically manages case status by moving cases to 'In Progress' during processing and marking them as successful or failed based on completion. When adding actions inside the Process cases loop, uncaught exceptions are handled for you, marking the case as failed with the associated error details and moving to the next case. The action also provides access to case data during processing. Properties: - `Title`(optional) - Action name shown in the process visualization (e.g., "Process pending invoices")
- `Case type`(required) - Type of cases to process (e.g., "Invoice processing")
- `Current case`(output) - Variable containing the case being processed in each loop. Access case data using current_case["custom_data"]["key_name"]
 
- Update case data
- 
                        Saves changes to case information during processing. Can add new fields or modify existing data. Only available while a case is 'In Progress'. Used to track processing results and manage case lifecycle. Properties: - `Title`(optional) - Action name shown in the process visualization (e.g., "Update case status")
- `Case ID`(required) - Unique identifier of the case to update (e.g., current_case["case_id"])
- `Data to update`(required) - New or modified information to store as key-value pairs (e.g., {"Status": "Approved", "ProcessedDate": "2024-01-20"})
- `Updated case`(output) - Variable containing the modified case. Access updated data using updated_case["custom_data"]["key_name"]
 
- Search cases
- 
                        Retrieves cases for reporting and analysis. Filter by case type, status, or reference name. Returns results as a data table containing case information and custom data. Properties: - `Title`(optional) - Action name shown in the process visualization (e.g., "Find overdue cases")
- `Case type`(required) - Type of cases to search (e.g., "Support tickets")
- `Filter by status`(optional) - Filter for cases based on their current status (e.g., "Pending Resolution")
- `Filter by reference name`(optional) - Filter for cases with a specific reference name (e.g., "Ticket-12345")
- `Maximum results`(optional) - Limits the number of cases to return. Leave empty to return all cases up to 10,000 (e.g., 100)
- `Search results`(output) - Variable name that will store the data table of cases retrieved by the search (e.g., cases_table)
 

## Human-in-the-Loop (HITL)

        While many decisions can be automated, some scenarios require human judgment. Amazon Quick Automate's HITL capabilities allow you to seamlessly incorporate human decision-making into your automated processes. There are two ways to create HITL tasks:

- Using the Create user task action 
- Using HITL chat through a Custom agent 

### Create user task

Creates a task for human input. Tasks appear in a list for users to review, make decisions, or provide information. Tasks can only be created when in a case processing loop while the case is in progress. Creating a task moves the case to 'Pending task' status and the automation continues with the next case. Once the task is resolved, the case returns to 'Ready' status for further processing. Properties:

- `Title`(required) - Subject line that appears in the user's task list. Should clearly describe what needs to be done (e.g., "Review loan application", "Approve expense report")
- `Description`(required) - Detailed instructions and context provided to users completing the task (e.g., "Please review the attached application details and either approve or reject based on the following criteria...")
- `Form`(required) - Interface for collecting structured input from users
- `Severity`(required) - Priority level to help users triage tasks:- Critical - Urgent attention required, highest priority 
- Moderate - Normal priority (default) 
- Low - Non-urgent task 
 
- `Due in`(required):- Number - Quantity of time units (e.g., 24) 
- Unit - Hours or Days 
 
- `Case ID`(required) - Unique identifier of the case this task is for (e.g., current_case["case_id"])

###### Important

When creating a HITL task:

- The Process cases loop automatically updates the case status to Pending Resolution and moves on to the next case 
- Do not add actions after creating a task inside the Process cases loop as they won't execute for the current case 

#### Building forms

When creating a HITL task, you can build custom forms to collect exactly the information needed from human reviewers. The following components are available for form design:

- Text field - Single or multi-line text input for collecting user inputs (e.g., "Please provide reason for rejection in detail") 
- Dropdown - Selection from predefined options (e.g., ["Approve", "Reject", "Escalate"]) 
- Date/time picker - Calendar-based input 
- Media - Display images or documents for review 
- Display text - Read-only information to provide context (e.g., case details, policy references) 

### HITL chat

For scenarios requiring more dynamic interaction, Amazon Quick Automate also supports HITL chat through Custom agents. This enables natural language conversation between the agent and human reviewer. The agent can create a HITL tasks when it needs human input. The case will remain In progress while the agent chats with the human reviewer. Once sufficient input is provided, the agent will continue.

```
# Example agent prompt for HITL chat
"""
Review the data and if any values are outside normal ranges,
create a HITL task for human review. Include the specific
values and acceptable ranges in the task description.
"""
```
###### Note

HITL chat tasks will be given a default severity (Moderate) and due in (24 hours).

### Task resolution and case re-entry

After a human completes a HITL task, your automation needs to handle the case's return to processing. Understanding how to work with task resolution data is key to implementing effective human-in-the-loop workflows. When a task is resolved:

- The associated case automatically returns to Ready status 
- The case becomes available for processing again through Process cases 
- The latest_task_resolution field contains all form inputs and decisions 

Example checking for HITL resolution and handling the case accordingly:

```
# Example handling HITL resolution
if current_case["latest_task_resolution"]:
    # Handle case returning from HITL
    resolution_data = current_case["latest_task_resolution"]["form_data"]
    if resolution_data["decision"] == "Approve":
        # Process approved case
    else:
        # Handle rejected case
else:
    # First time processing this case
```
Best practices for handling HITL resolution:

- Always check latest_task_resolution when processing cases 
- Structure your logic to handle both new cases and those returning from HITL 
- Consider implementing different processing paths based on human decisions 
- Include error handling for missing or invalid resolution data