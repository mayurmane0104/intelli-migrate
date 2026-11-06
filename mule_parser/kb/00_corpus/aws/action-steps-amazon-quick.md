# Action steps - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/action-steps-in-flows.html](https://docs.aws.amazon.com/quick/latest/userguide/action-steps-in-flows.html)

---

Action steps let your flows perform read or write operations in connected applications. The available operations depend on the action integrations that you have configured or that have been shared with you. For prerequisites, authentication methods, and available integrations, see [Working with integrations](./working-with-integrations.html).

## Action parameters

        Some actions require or accept parameters such as filters or specific input values. To determine which parameters an action accepts, you can ask Quick — for example, "What parameters does list emails accept when filtering emails?"

Parameters can be:

- Supplied directly in the prompt (for example, "List emails with subject containing 'quarterly report'") 
- Referenced from a previous step using @ references (for example, a user input step that collects a search term) 
- Acquired dynamically during flow execution based on the flow context 

## Working with list results

        When you use an action that returns a list of items (for example, listing emails or tickets), the results may not include every item or every detail. This is because many applications return results in batches rather than all at once, and Quick retrieves only the first batch to keep your flow fast and responsive.

If you need the full details for each item in a list, you can use a reasoning group to go through the results one at a time and retrieve the complete information for each. For example, you might list your open support tickets in one step, then use a reasoning group to get the full details of each ticket.

When doing this, be mindful of how many items you are processing. A large number of items means more steps to run, which increases the time your flow takes to complete and the amount of data in your results. Where possible, use filters in your initial list action to narrow down the results before processing them.

For configuration instructions, see [Editing flows](./editing-flows.html).