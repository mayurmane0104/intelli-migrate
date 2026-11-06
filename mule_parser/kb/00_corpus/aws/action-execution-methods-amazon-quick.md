# Action execution methods - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/int-actions-execution.html](https://docs.aws.amazon.com/quick/latest/userguide/int-actions-execution.html)

---

Amazon Quick provides multiple ways to execute actions, accommodating different use cases and interaction preferences.

## Chat interface

        You can execute implicit actions in the Amazon Quick chat.

### Implicit actions

Amazon Quick also supports implicit action execution through natural conversation with agents. Using advanced natural language processing, the system can identify when your conversation indicates the need for specific actions. Conversations are analyzed to determine which actions are required to fulfill your request.

A single request might require multiple actions to complete. When this happens, the system handles these actions sequentially, guiding you through each step. For each identified action, the system presents the appropriate form for you to complete. After each action completes, you receive a confirmation before moving on to the next action in the sequence.

For example, if you ask "Create a Jira ticket for this issue and notify the team in Slack," the system would:

- 
                    First present the Jira ticket creation form. 
- 
                    After completing the ticket creation, show the Slack message form. 
- 
                    Complete both actions in sequence. 

Throughout the process, you can track your progress through multiple actions. When all actions complete, the system provides a comprehensive summary showing all executed actions and their outcomes. You can access related documentation if needed and review any error states that may have occurred during the process.