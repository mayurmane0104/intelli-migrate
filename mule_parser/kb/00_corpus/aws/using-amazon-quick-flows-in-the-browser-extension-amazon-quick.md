# Using Amazon Quick Flows in the browser extension - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/flows-in-browser-extension.html](https://docs.aws.amazon.com/quick/latest/userguide/flows-in-browser-extension.html)

---

Amazon Quick Flows in the browser extension enables you to run pre-defined workflows directly within your web browsing context. You can invoke flows that you've created or that have been shared with you, pass web page content as input, and execute multi-step workflows without leaving your browser.

When you use flows in the browser extension, you can:

- 
            Invoke flows explicitly from the browser extension interface. 
- 
            Pass web pages as context to your flows. 
- 
            View flow execution history in your browser extension. 

## Prerequisites

        Before using flows in the browser extension, ensure you have:

- 
                Appropriate permissions to execute flows in your Amazon Quick account. 

## Invoking flows

        You can invoke flows from the browser extension to run workflows on the web pages you're viewing.

**To invoke a flow in the browser extension:**

- 
                Open the Amazon Quick browser extension. 
- 
                In the chat interface, choose the **Flows**icon.
- 
                Select a flow from the list or use the search bar to search through your flows. 
- 
                The flow begins execution in the browser extension chat. 
- 
                When prompted, select the tab you want to include as context and choose **Confirm**.

When a flow is active, the browser extension displays a progress tracker showing the current step. The dropdown menu on the progress tracker shows all steps in the flow.

## Flow execution process

        Once a flow is invoked in your browser extension, you interact with the flow through natural language chat as follows:

- 
                You're greeted with a summary of its capabilities. 
- 
                You're prompted for required inputs through chat messages. 
- 
                The extension displays outputs and results in the chat interface. 
- 
                The extension shows a progress tracker indicating completed and remaining steps. 

To view flow capabilities, see the [flows documentation](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-flows.html).

## Flow execution history

        All flow executions in the browser extension are recorded in your conversation history. You can view past executions and resume incomplete flows. To view flow execution history:

- 
                In the browser extension, go to menu and choose the **Conversation history**icon.
- 
                Select a conversation that includes a flow execution. 
- 
                The conversation displays the flow execution details, including all inputs and outputs. 

If you closed the browser extension while a flow was running, you can resume the flow by selecting it from your history.

## Stopping flow execution

        You can stop a flow at any time during execution. To stop a running flow:

- 
                While the flow is running, choose the **End**button in the progress tracker.
- 
                The flow stops at the current step and you can continue your conversation with your My Assistant or Chat agent.