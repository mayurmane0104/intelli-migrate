# Working with threads in an Amazon Quick Sight scenario - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/scenarios-threads.html](https://docs.aws.amazon.com/quick/latest/userguide/scenarios-threads.html)

---

After you create a scenario in Quick Sight, the data that Amazon Q generates is
            presented in *threads* and *blocks*. A thread is a
            vertical chain of prompts and responses. A block is a single prompt and response pair.
            Each thread can contain up to 15 blocks, and each scenario can contain up to 50 blocks
            total across multiple threads.

When a new thread is created, a list of Amazon Q-generated prompts appears inside of a new block. When you choose one of the prompts to drill down on, Amazon Q analyzes the data that is relevant to the chosen prompt and returns a summary of all data findings, forecasts, and conclusions that can be drawn from the analysis.

To continue the thread and dive deeper into the prompt, choose the plus sign
                (**+**) located below the block to create a new block that contains
            a new list of generated prompts that factor in the findings from the previous block. To
            start a new thread that analyzes a different aspect of the data, choose the plus sign
                (**+**) above any block in the scenario to create a new thread. 

Blocks can be collapsed, duplicated, or deleted from a scenario, as long as the block that you want to change has finished loading. Use the following procedures to make changes to a scenario block.

###### To collapse, duplicate, or delete a block

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Choose **Scenarios**from the options pane, and then choose the scenario that you want to change.
- 
                Navigate to the block that you want to change and choose the ellipsis (…) in the top right of the block. 
- 
                Perform one of the following actions: - 
                        To collapse the block, choose **Collapse**. To expand a collapsed block, choose the ellipsis in the top right of the block, and then choose**Expand**.
- 
                        To duplicate the block, choose **Duplicate**. The block is duplicated and placed in a new thread next to the original block.
- 
                        To delete the block, choose **Delete**.
 
- 
                        

You can also modify the prompt of a block to better match your use case. Use the following procedure to modify a block prompt.

###### To modify the prompt of a block

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Choose **Scenarios**from the options pane, and then choose the scenario that you want to change.
- 
                Navigate to the block that you want to change and choose **Modify block**.
- 
                In the **Modify block**popup that appears, enter a new description for the block, and then choose**Apply**.

After you modify a prompt, Amazon Q analyzes the data and returns a new generated analysis that reflects the changes that were made to the prompt.