# Data preparation limits - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/data-preparation-limits.html](https://docs.aws.amazon.com/quick/latest/userguide/data-preparation-limits.html)

---

Amazon Quick Sight's data preparation experience is designed to handle enterprise-scale datasets while maintaining optimal performance. The following limits ensure reliable functionality.

## Dataset size limits (SPICE)

            
            - 
                    **Output size**: Up to 2TB or 2 billion rows
- 
                    **Total input size**: Combined input sources cannot exceed 2TB
- 
                    **Secondary tables size**: Combined size is limited to 20GB

###### Note

Primary tables are those with maxiumum size in a workflow; all others are secondary.

## Workflow structure limits

            
            - 
                    **Maximum steps**: Up to 256 transformation steps per workflow
- 
                    **Source tables**: Maximum 32 import steps per workflow
- 
                    **Output columns**: Up to 2048 columns at any step in the workflow and final output table with 2000 columns
- 
                    **Divergent paths**: Maximum 5 paths from a single step (SPICE only, not applicable for DirectQuery)
- 
                    **Dataset as a source**: Up to 10 levels for both SPICE and DirectQuery

These limits are designed to balance flexibility with performance, enabling complex data transformations while ensuring optimal analysis capabilities.