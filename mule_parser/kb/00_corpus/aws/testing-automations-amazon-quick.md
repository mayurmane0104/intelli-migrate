# Testing automations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/testing-automations.html](https://docs.aws.amazon.com/quick/latest/userguide/testing-automations.html)

---

Amazon Quick Automate provides comprehensive capabilities for testing your automations. This section describes the tools and features available for validating your automation behavior.

## Test modes

        Choose from two modes to test your automation:

- Run mode - Executes the automation from start to finish without stopping. Any breakpoints in the automation will be ignored. This mode is best for testing the complete flow of your automation. 
- Debug mode - Executes the automation and pauses at any breakpoints you've set or if an exception occurs. This allows you to inspect the automation state, monitor variables, and validate behavior at specific points in your process. 

## Test pane

        The Test pane includes includes two main tabs that help you monitor and control your automation test:

### Setup tab

The Setup tab provides tools for managing your test configuration:

- Breakpoint manager - Lists all breakpoints currently set in your automation. Remove breakpoints directly from this view without returning to the canvas. 
- Test navigation - Quick access links to view: - View runs - See all automation runs from testing 
- View cases - View cases created during testing 
- View tasks - Review any human-in-the-loop tasks generated 
 

### Monitor tab

The Monitor tab displays real-time information about your running automation:

- UI streaming - Watch browser automation actions execute in real-time 
- Variable watcher - Monitor and modify variable values 
- Logs - Track detailed automation progress 

## Test statuses

        During testing, your automation will be in one of these statuses:

- Running - The automation is actively executing actions 
- Paused (breakpoint) - Execution has stopped at a user-defined breakpoint 
- Paused (exception) - Execution has stopped due to an error condition 
- Completed - The automation has finished all steps successfully 
- Failed - The automation encountered an unrecoverable error and stopped 

## Running and debugging

        
         
        
            ### Test automations with inputs and outputs

When you test an automation that has input and output fields defined, Amazon Quick Automate validates the input values and displays both inputs and outputs as expandable cards in the **Monitor** pane alongside the execution logs.

#### Running an automation with inputs from the authoring studio

When you choose **Run** or **Debug** to test an automation with inputs and outputs, the authoring studio (Studio) displays a dynamic input form titled **Provide input values**. Amazon Quick Automate automatically generates this form based on the schema you defined.

The form includes:

- Field names from your schema. 
- Input controls appropriate for each data type (text fields for strings, number inputs for integers, and file upload buttons for files). 
- Required field indicators (marked with an asterisk). 
- Default values pre-populated where you defined them. 
- Client-side validation for data types, required fields, and file size limits (maximum 5 MB for files). 

To run an automation with inputs:

- Open your automation in Studio and choose - **Run**or- **Debug**.
- In the - **Provide input values**form, enter values for each field:- For text and number fields, type the values directly 
- For file fields, choose - **Browse**to select a file from your local machine
- Optional fields can be left blank unless you want to override default values 
 
- Choose - **Start**to begin the automation with your provided inputs.

Amazon Quick Automate performs two layers of validation:

- **Client-side validation**– Checks for blank required fields, correct data types, and file size limits before execution starts
- **Runtime validation**– Validates the complete input payload against your JSON schema during execution

#### Viewing inputs and outputs

After the automation runs, input and output values appear as collapsible cards in the **Monitor** pane:

- **Input card**– Displays at the beginning of the run logs, showing all values you provided when starting the automation
- **Output card**– Displays at the end of the run logs after execution completes, showing all values your automation produced

Both cards are collapsed by default. When you expand them, you can:

- View the complete schema definition and actual values 
- Download any file objects included in the inputs or outputs 
- Copy the structured data as JSON 
- Download the complete payload as a JSON file 

###### Note

If the automation terminates with an error, the output card won't be available.

### Setting breakpoints

Breakpoints allow you to pause your automation at specific points:

To add a breakpoint:

- Hover over an action or step on the canvas 
- Click - **Add breakpoint**
- The breakpoint icon appears on the action or step 

To remove a breakpoint:

- Click - **Remove breakpoint**on the action
- Or use the breakpoint manager in the Setup tab 

###### Note

Set up breakpoints before starting debug mode.

### Debug controls

When your automation is paused, you have several control options:

- Next - Run the next action in your automation and pause again 
- Continue - Resume the run until the next breakpoint is reached 
- Stop - End the current test run 
- Ignore - If paused on an exception, this will clear the exception and continue as if that action was successful. This is useful if the exception is not blocking the rest of your test and you want to continue. 
- Retry - If paused on an exception, this will attempt to run the current action again. This is useful if the issue is temporary or if you want to change the value of a variable and retry with the new value 

### Deactivating steps

To temporarily disable any actions or steps without removing them, you can deactivate them before starting your test. Deactivated actions or steps will be skipped during testing.

- Select the step to deactivate 
- Click the - **Menu options**
- Choose - **Deactivate**
- The step appears grayed out 

To reactivate:

- Select the deactivated step 
- Click the - **Menu options**
- Choose - **Activate**

### Variable watcher

The Variable watcher in the Monitor tab provides visibility to inspect data being used by your automation during the test. To inspect a variable:

- Open the Variable watcher in the Monitor tab while the test is paused 
- Click - **Add**to search and select variables to inspect
- View the current value for the variable 
- Modify values to test different scenarios: - Click the - **pencil icon**next to any variable
- Enter a new value to test 
- Continue the run to proceed with the new value 
 

This feature is particularly useful for:

- Testing different data conditions 
- Validating error handling 
- Simulating edge cases 

## Troubleshooting

        
         
        
            ### Fix with Assistant

When your automation encounters an exception, the Automation Assistant can help identify and resolve issues:

- Click - **Fix with Assistant**when paused at an error
- The Assistant will: - Analyze the error message 
- Review the run logs 
- Check its troubleshooting knowledge base 
- Provide a clear explanation of the issue 
- Suggest potential solutions 
 
- Chat with the Assistant to: - Ask questions about the error 
- Update the automation based on any of the recommended changes 
 

## Test metrics

        After your test completes, Amazon Quick Automate provides comprehensive test metrics to help understand automation performance and validate test coverage. View key metrics about your test run:

- Total running time - How long the test took from start to finish 
- Number of completed cases - Count of cases that finished processing (excluding those created or pending) 
- Average time per case - The processing average time for each completed case 
- Case success rate - Percentage of cases that completed without exceptions 
- Count of tasks created - Number of human-in-the-loop tasks generated during the test 
- Action coverage - Percentage of actions in your automation that executed during the test, helping identify untested paths