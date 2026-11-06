# Building automations - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/building-automations.html](https://docs.aws.amazon.com/quick/latest/userguide/building-automations.html)

---

Amazon Quick Automate provides multiple methods for creating automations to suit different needs and skill levels. This section describes the available creation methods and tools.

## Prerequisites

        Before creating an automation, you need to create a project within a specific automation group. The automation group will control what integrations and credentials are available to you when building that automation. Ensure the required integrations and credentials are set up for any external systems you plan to interact with in your automation.

Once you have created a project, click the **Start building** button to get started.

###### Note

You must have owner permissions to manage integrations and credentials for an automation group.

## Creation methods

        Choose from three approaches to build your automation. If you're new to Amazon Quick Automate, we recommend:

- Start by exploring sample automations 
- Try creating a simple automation using natural language 
- Experiment with manual editing once you're familiar with the basics 

### Using sample automations

Get started quickly by exploring pre-built samples that demonstrate common automation patterns. These samples provide hands-on examples of different automation capabilities and serve as learning resources to help you become familiar with the capabilities of Amazon Quick Automate. To use a sample automation:

- Search to explore different samples by industry. 
- Click on the sample to view an overview of the automation. - If any integrations are required, they will be listed as prerequisites. 
 
- Click - **Start with sample**to open the automation in the canvas.
- You will now be able to view the automation, edit it, and test it. 

### Creating with natural language

The Automation Assistant provides an AI-powered approach to creating automations through:

- Chat interface - Describe your process conversationally in natural language 
- Document upload - Import any documentation that describes your process steps and requirements 

When you provide input through either method, the Automation Assistant will generate your automation through a two-step guided experience:

- **High-level plan**- First, the Assistant analyzes your requirements and generates a high-level automation plan. The plan consists of - **process steps**that logically group the related actions as part of the automation. Each process step initially contains natural language instructions.
- Review and edit the instructions for each process step and then click - **Generate**to create the low-level actions for that step.
 
- **Low-level actions**- Next, the Assistant will build the low-level actions and process logic based on the step instructions. 
- Review and edit the generated actions. Click - **Run**or- **Debug**to begin testing.
 

Best practices for providing natural language inputs:

- Specify the step by step process as if you were training a new hire 
- Include exact details needed to perform each step: - Email address if sending a message 
- File name and location if uploading/downloading a document 
- URL if navigating to a website 
 

### Creating from scratch (blank automation)

Build automations manually using the visual designer interface:

- Navigate to your project summary 
- Click - **Start building**
- Select - **Skip**to access the canvas

The designer interface provides several key components:

- **Canvas**- Visualizes the automation. You can zoom in and out, expand and collapse process steps, and reorder actions on the canvas.
- **Actions panel**- The actions panel has a comprehensive list of all the automation actions made available within your automation group. You can search and filter to find actions organized by category (Agents, Process flow, Web browser, etc.). Drag-and-drop actions onto the canvas to build your automation. You can also click the plus sign found when hovering between actions to add a new action directly in place on the canvas.
- **Properties panel**- Once you add an action or click on an existing one in your process, the properties panel allows you to configure the input and output parameters that control how that action will behave.
- **Settings panel**- Allows you to create and edit runtime configurations and explore the credentials available to your automation.
- **Variables panel**- Displays all the variables used within your automation. Creating a variable is seamless by adding a new reference directly in your automation.

## Runtime configurations and variables

        Runtime configurations allow you to create easily editable settings that are used by your automation. Examples of runtime configurations include:

- Website URLs 
- File names and locations 
- Email configurations like subjects and sender lists 

Variables are used to store and pass information between the actions in your automation when it runs. Add a new variable to you automation by simply providing a new reference name in an output property. Common variable types include:

- String - Plain text (e.g., name, description) 
- Number - Numeric value (e.g., quantity, score) 
- Boolean - True/False value 
- Array - Collection or list of items 
- Object - Key-value pairs 
- File - Documents and media (e.g., PDFs, images) 
- Data table - Spreadsheet-like data with rows and columns 

## Editing automations

        Once you've created your automation, you can modify it using either the Automation Assistant or by directly editing on the canvas.

### Using Automation Assistant

The Automation Assistant helps you make changes through natural language. You can:

- Ask for updates to the entire automation, specific steps or specific actions - Focus the chat on specific steps by selecting them first 
 
- Ask questions and get in-product help and suggestions based on your actual automation 
- Ask for help writing expressions and code based on your needs 

To edit with the Assistant:

- Click - **Build with Assistant**in the toolbar
- Describe the changes you want to make 
- Review and confirm the suggested modifications - The chat includes a summary of changes. Click - **Reject changes**to revert to the previous version.
 
- Test the updated automation 

### Editing on canvas

Make changes directly in the visual designer:

- Select the step or action to modify 
- Use the properties panel to adjust settings 
- Rearrange steps using drag-and-drop 

###### Note

Every action has a menu of options with common actions like duplicating the action or deleting it.

**Best practices for editing:**

- Make incremental changes 
- Test after each significant modification 

###### Note

Changes are saved automatically to the live version. If you want to deploy those changes, commit and deploy the updated version.

###### Tip

If you encounter issues while building:

- Use the Automation Assistant to get help 
- Check the action documentation for specific requirements 

## Automation inputs and outputs

        Define input and output schemas to create reusable, parameterized automations in Amazon Quick Automate. By defining input and output schemas using the Start and End nodes, you can transform static automations into reusable workflows that accept different data each time they run. Instead of hardcoding values, you define typed input parameters that are provided at runtime and structured output values that are captured when the automation completes. Inputs and outputs work across all invocation methods: manual runs, API calls, and scheduled triggers.

Key benefits of using inputs and outputs:

- **Reusability**– Run the same automation with different data without modifying the automation itself.
- **Type safety**– Amazon Quick Automate validates input data against the schema before execution starts, which prevents invalid data from running.
- **API integration**– Auto-generated schemas enable programmatic discovery and integration with external systems.
- **Observability**– Structured outputs are captured as execution artifacts for audit and review.

### Supported data types

The following data types are supported for input and output fields:

- **Text**– Plain text values (e.g., text1, text2)
- **Number**– Numeric values including decimals (e.g., 3.14, 100)
- **Boolean**– True or false values
- **File**– File objects with a maximum size of 5 MB

### Start and End nodes

Every automation includes a Start node and an End node, which are blank by default. You can edit these nodes to create a schema, use the inputs in the automation, and update the output data to return from the automation. The Start node receives input data at runtime, while End nodes (including End Process nodes) collect output data during execution and return it as structured artifacts when the automation completes.

#### Start

The Start node is the entry point that accepts input parameters when the automation is triggered. It is blank by default.

Properties:

- **Input format**– Defines the schema for input parameters that the automation accepts. Edit using the Input schema editor described in Defining input and output schemas.
- **Input variable**– Variable that stores the input values for the automation as defined in the input format and supplied by the user.

#### End

The End node is the termination point that collects and returns output values when the automation completes successfully. You can set the output values from variables in the automation using the properties of the End node. Your automation can have multiple End nodes (End process) based on the structure of the automation.

Properties:

- **Output format**– Defines the schema for output parameters that the automation returns. Choose- **Edit**and add or modify the schema using the Output schema editor described in Defining input and output schemas.
- **Output data**– Maps values from variables in your automation to the output fields that you defined. For each output variable that you create in the End node (Output schema), specify which automation variable contains the data that you want to return. Use the- **Edit output data**editor to configure these mappings in the- **Output Value**field.

### Defining input and output schemas

Schemas define the structure of data that your automation accepts as input and produces as output. The authoring studio provides a visual form builder for defining input and output schemas directly on the automation canvas.

To define an input schema:

- Open your automation in Amazon Quick Automate. 
- Choose the - **Start**node on the canvas to open the schema editor. You can also open the schema editor from the properties pane. To do this, choose the- **Start**node, and then choose- **Edit**in- **Input format**in the properties pane.
- Choose - **+Add field**to add an input field.
- For each input field, configure the following properties: - **Name**– A unique identifier for the field.
- **Type**– The type of data the field accepts. For more information, see Supported data types.
- **Required**– Whether the field must be provided when running the automation.
- **Default value**(Optional) – This option is active only if the- **Required**field is cleared. Default values appear pre-populated in the input form when you run a test or trigger the automation.
- **Description**– A description of what the field represents.
 
- Choose - **Save**to store the schema with your automation.

To define an output schema:

- Choose an - **End**node on the canvas to open the Output schema editor. You can also open the schema editor from the properties pane. To do this, choose the- **End**node, and then choose- **Edit**in- **Output format**in the properties pane.
- Choose - **+Add field**to add an output field.
- For each output field, configure the following properties: - **Name**– A unique identifier for the field.
- **Type**– The type of data for the output.
- **Description**– A description of what the output represents.
 
- Choose - **Save**.

###### Note

You can define inputs from the Start node and outputs from any End node. If your automation has multiple End nodes, adding or modifying the schema of one End node modifies all End node schemas.

### Using input values from the start node

When your automation has an input schema defined at the Start node, you can access those input values throughout your workflow using the `inputs` dictionary. The runtime automatically validates and populates this dictionary with the values provided when the automation runs.

```
# Access required input fields
value = inputs["field_name"]
# Example usage
customer_id = inputs["customer_id"]  # Retrieves a required string input
```
### Setting output values in the End node

The End node defines which values from your automation are returned as outputs. You configure this using the **Output Data** property, which provides two interaction modes for setting output values in the editor. Toggle between the modes by choosing the code icon (`</>`) next to the **Output value** field.

Two modes for setting outputs:

- **Variable Selection Mode (Dropdown)**– The default interface displays a dropdown list of all available variables in your automation. Select the variable that you want to assign to each output field.
- **Expression Mode (Code)**– Choose the code icon (- `</>`) next to any output value field to switch to expression mode. This mode allows you to enter custom expressions, perform calculations, access nested data, or set literal values.

### Defining schemas with the Build with Assistant

Build with Assistant can create or modify input and output schemas directly. Describe your input and output requirements in natural language, and the assistant generates the schema definition for you. Any changes that the assistant makes automatically sync with the Studio visual form builder.

### Considerations

Keep the following in mind when you use automation inputs and outputs:

- Input and output schemas are optional. Existing automations without schemas continue to work unchanged. 
- File inputs have a maximum size of 5 MB. For larger files, pass the file location (such as an Amazon S3 path) as a text input instead. 
- Input and output values are stored with each execution run for observability and audit purposes. 
- When you update a schema, you must redeploy the automation for the changes to take effect on deployed runs. Test runs always use the latest draft schema. 

You can use the input and output values in the following ways:

- Testing and running the automation from the canvas. For more information, see - [Testing automations](https://docs.aws.amazon.com/quicksuite/latest/userguide/testing-automations.html#running-and-debugging).
- Manually triggering deployed automations. For more information, see - [Deploying automations](https://docs.aws.amazon.com/quicksuite/latest/userguide/deploying-automations.html#deploy-run-inputs-outputs).
- Scheduled triggers for deployed automations. For more information, see - [Deploying automations](https://docs.aws.amazon.com/quicksuite/latest/userguide/deploying-automations.html#deploy-run-inputs-outputs).

## Managing automation versions

        Amazon Quick Automate provides version control capabilities to help you track and maintain the history of updates to your automations and easily restore previous versions.

### Key concepts

- **Live version**- The current working copy of your automation that you can edit in the canvas. Changes are auto-saved to the live version as you edit.
- **Committed versions**- Read-only snapshots of your automation which can be deployed. Commit a new version of your automation to keep track of significant updates and be able to revert back if needed.
- **Deployed versions**- Committed versions can be deployed and activated to run on a schedule.

###### Note

Each version maintains its own runtime configuration values. Changes to the Live version's runtime settings don't affect previously committed or deployed versions.

### Committing versions

To commit a version:

- Click - **Commit**in the canvas toolbar
- Add a descriptive note explaining your changes 
- Choose how to increment the version number: - Minor version (e.g., 1.05 → 1.06) for smaller updates (default) 
- Major version (e.g., 1.0 → 2.0) for significant changes 
 
- Click - **Commit**

###### Important

You cannot commit a version if the automation has any validation errors. Resolve all errors before attempting to commit.

When you commit a version:

- The committed version becomes a read-only snapshot 
- The current runtime configuration is saved with the committed version 
- A new Live version is created based on that snapshot to continue editing 

###### Important

Only committed versions can be deployed. The Live version must be committed first before it can be made deployed.

### Viewing versions

View versions in two places:

- **Version dropdown in canvas**- Defaulted to the Live version. Choose any previous version from the dropdown to view in read-only mode on the canvas.
- **Versions tab**- Found within Project details. Shows a complete version history including version number, when the version was committed, the user that committed the version, and any version notes. Click on the actions menu to view version details or deploy the version.

### Restoring previous versions

To restore a previous version and continue editing it as the Live version:

- Select the version from the version dropdown above canvas 
- Choose - **Restore live version**
- The selected version replaces your current Live version 
- Continue editing the Live version to make any needed adjustments 
- Commit as a new version to take a snapshot or deploy the updates 

###### Note

Restoring a version creates a new working copy but doesn't delete any version history.

### Best practices

- Add clear version notes to track the purpose of changes 
- Commit versions after significant updates 
- Test changes before committing 
- Review runtime configuration before committing