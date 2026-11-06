# Interacting with flows in runtime mode - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/interacting-with-flows-in-runtime-mode.html](https://docs.aws.amazon.com/quick/latest/userguide/interacting-with-flows-in-runtime-mode.html)

---

When you open a flow, you select **Run mode** to execute it. There are three ways to start a flow.

## Starting a flow with structured input

        If the flow has input steps, enter the required information and choose **Start**. The flow runs through each step in sequence and displays the results.

## Starting a flow with conversational runtime

        You can supply the flow input (optional) and ask the agent to start the flow through the chat panel. The agent collects any additional inputs, runs the steps, and presents results within the conversation. You can ask follow-up questions or refine outputs as the flow runs.

## Starting a flow from a chat agent

        You can run a flow directly from a chat agent conversation:

- Choose the Flows menu in the chat footer. 
- Select the flow you want to run. 
- Follow the prompts to execute it. 
- When finished, choose - **End**to return to your chat agent conversation.

Details from your conversation can automatically populate the text input to your flow. When the flow completes, the output is shared with the calling agent.

## Progress tracker

        The progress tracker shows the status of each step as the flow runs.

## Resuming runs from history

        You can view and resume previous flow runs from the flow's history. Open the flow and choose the history icon to view previous runs.