# Create repeating sections - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/qs-reports-repeat-sections.html](https://docs.aws.amazon.com/quick/latest/userguide/qs-reports-repeat-sections.html)

---

Use repeating sections to create duplicates of specific sections of a report to show one or more-dimension values. The data in the repeating section is sliced to match the dimensions of the section. Repeating sections can be replicated at scale to decrease the amount of time it takes to build reports.

Use the following procedures to create and configure a repeating section in a report.

###### To define a repeating section

- 
                        Navigate to the section that you want to add a repeating behavior to and choose the **Edit repeating section**(triple panel).
- 
                        In the **Edit section**pane that opens, choose**ADD DIMENSION**, and then choose the dimension that you want to add.
- 
                        To add additional dimensions, repeat Step 2. You can add up to 3 dimensions in each repeating section configuration. 

**Considerations for repeating sections**

The following limits apply to repeating sections.

- 
                        Insight visuals aren't supported for repeating sections. 
- 
                        Repeating sections dimensions that are only from the last dataset that was selected for use in the analysis. 

After you create a repeating section, you can define sorting and limits to the repeating section configuration. You can also use text boxes to add system parameters to repeating sections.