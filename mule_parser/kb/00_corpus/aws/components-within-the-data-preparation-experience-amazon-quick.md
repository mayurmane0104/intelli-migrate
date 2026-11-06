# Components within the data preparation experience - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/data-prep-components.html](https://docs.aws.amazon.com/quick/latest/userguide/data-prep-components.html)

---

Amazon Quick Sight's data preparation experience has the following core components.

## Workflow

			
			A workflow in Quick Sight's data preparation experience represents a sequential series of data transformation steps that guide your dataset from its raw state to an analysis-ready form. These workflows are designed for reusability, enabling analysts to leverage and build upon existing work while maintaining consistent data transformation standards throughout the organization.

While workflows can accommodate multiple paths through various Inputs or through Divergence (detailed in subsequent sections), they must ultimately converge into a single output table. This unified structure ensures data consistency and streamlined analysis capabilities.

## Transformation

			
			A transformation is a specific data manipulation operation that changes the structure, format, or content of your data. Quick Sight's data preparation experience offers various transformation types including Join, Filter, Aggregate, Pivot, Unpivot, Append, and Calculated Columns. Each transformation type serves a distinct purpose in reshaping your data to meet analytical requirements. These transformations are implemented as individual steps within your workflow.

## Step

			
			A step is a collection of homogeneous transformations of the same type applied within your workflow. Each step contains one or more related operations of the same transformation category. For example, a Rename step can include multiple column renaming operations, and a Filter step can contain multiple filtering conditions–all managed as a single unit in your workflow.

Most steps can include multiple operations, with two notable exceptions: Join and Append steps are limited to two input tables per step. To join or append more than two tables, you can create additional Join or Append steps in sequence.

Steps are displayed in order, with each step building upon the results of previous steps, allowing you to track the progressive transformation of your data. To rename or delete a step, select it and choose the three-dot menu.

## Connector

			
			The connector links two steps with an arrow indicating the workflow direction. You can delete a connector by selecting it and pressing the delete key. To add a step between two existing steps, simply delete the connector, add the new step, and reconnect the steps by dragging your mouse between them.

## Configure pane

			
			The **Configuation pane** is the interactive area where you define parameters and settings for a selected step. 
			When you select a step in your workflow, this pane displays relevant options for that specific transformation type. 
			For example, when configuring a Join step, you can select join type, matching columns, and other join-specific 
			settings. The **Configuation pane**'s point-and-click interface eliminates the need for SQL knowledge.

## Preview pane

			
			The **Preview pane** displays a real-time sample of your data as it appears after applying the current 
			transformation step. This immediate visual feedback helps you verify that each transformation produces the 
			expected results before proceeding to the next step. The **Preview pane** updates dynamically as you modify step 
			configurations, enabling iterative refinement of data transformations with confidence.

These components work together to create an intuitive, visual data preparation experience that makes complex data transformations accessible to business users without requiring technical expertise.