# Flow logic steps - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/flow-logic-steps.html](https://docs.aws.amazon.com/quick/latest/userguide/flow-logic-steps.html)

---

Flow logic steps control how your flow runs.

## Reasoning Group

        Reasoning groups give you control over how parts of your flow run using natural language instructions. A reasoning group contains its own set of steps — like an isolated workflow within your larger workflow — that runs based on conditions you define. You can add most step types to a reasoning group, except reasoning groups and research steps. Templates are available to help you get started.

### Loops

You can repeat the steps in a group for each value in a list from a previous step's output. Reference the previous step in your instructions, and the Flows runtime handles the iteration for you. For example, if a previous step returns a list of customer emails, a reasoning group can process each email in turn.

### Conditions

You can run the steps in a group based on natural language conditions that evaluate a previous step's output. For example, "Run if @Customer Priority is HIGH PRIORITY" routes only urgent items through the group's steps.

### Validation

You can check inputs or outputs before proceeding. For example, a reasoning group can verify that a required field is present before passing data to an action step.

For configuration instructions, see [Editing flows](./editing-flows.html). For reasoning group limits, see [Quick Flows limits](./quick-flows-limits.html).