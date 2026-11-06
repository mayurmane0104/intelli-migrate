# Human-in-the-loop task center - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/hitl-task-center.html](https://docs.aws.amazon.com/quick/latest/userguide/hitl-task-center.html)

---

Human-in-the-loop (HITL) tasks enable you to incorporate human judgment at critical points in your automated processes. The Task Center provides a centralized interface for managing HITL tasks. Users can review, resolve, and track tasks that require human intervention.

## Overview

        The Task center displays tasks requiring human attention and provides metrics on task processing.

### Task metrics

The dashboard shows key performance indicators:

- **Open tasks**- Total number of tasks awaiting completion
- **Critical tasks**- Count of high-priority tasks requiring attention
- **Overdue tasks**- Number of tasks past their due date

### Task details table

Each task provides comprehensive information through the following columns:

- **Title**- Brief description of what needs to be done
- **Status**- Current task state (Open, Completed, Archived)
- **Due date**- When the task should be completed (includes overdue warning)
- **Severity**- Task priority (Low, Moderate, Critical)
- **Assignee**- User or group responsible for the task
- **Creation time**- When the task was created
- **Completion time**- When the task resolution was submitted by a user

### Prerequisites

Before working with tasks, you need:

- Task permissions - Access granted through automation deployment settings 
- Active automations - At least one automation with HITL tasks must be run 

## Types of tasks

        
         
        
            ### Chat tasks

Interactive conversations where AI agents gather input through natural language. To participate in a chat task:

- Select the task 
- Review the conversation history 
- Respond to agent questions in the chat interface 
- The agent will close the task once it has sufficient information 

###### Note

Chat tasks are closed automatically by the AI agent. You can archive unresolvable tasks, which the agent will treat as exceptions.

### Form tasks

Tasks requiring structured input through form fields. To complete a form task:

- Select the task 
- Fill in the required form fields 
- Click Submit when finished 

###### Note

Enable "Automatically open next task" to streamline processing multiple tasks. Use "Save as Draft" to preserve partial progress.

## Managing tasks

        
         
        
            ### Task statuses

Tasks can be in one of these states:

- Open - Awaiting human input 
- Completed - Successfully submitted 
- Archived - Removed from active view 

### Task actions

Manage tasks through these available actions:

- Submit - Complete a form task 
- Save as Draft - Preserve partial form progress 
- Archive - Remove task from active view 
- Unarchive - Restore archived task 

###### Note

Only Open tasks can be archived.

### Task assignment

Distribute work by assigning tasks:

- Select a task 
- Click the assignee field 
- Search for and select users or groups 
- Click Remove assignee to clear assignment 

###### Note

Users must have appropriate permissions to be assigned tasks.

### Related information

Access connected resources through the Sources menu:

- Case - View related case details (if applicable) 
- Automation - See the automation that created the task 

###### Note

Source access requires appropriate permissions.

### Search and filtering

Locate specific tasks using:

- Search - Find tasks by title 
- Filters: - Status 
- Due date 
- Severity 
- Assignee 
- Creation date 
 

###### Note

Click refresh to update task data at any time.

### Environment selection

Switch between viewing tasks from:

- Test - Tasks from automation testing 
- Deployed - Tasks from deployed automations