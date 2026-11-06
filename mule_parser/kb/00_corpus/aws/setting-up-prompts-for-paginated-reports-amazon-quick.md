# Setting up prompts for paginated reports - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/paginated-reports-prompts.html](https://docs.aws.amazon.com/quick/latest/userguide/paginated-reports-prompts.html)

---

Amazon Quick authors can create prompts on pixel-perfect reports to allow
                dashboard users to filter data in on-demand and scheduled reports.
                    *Prompts* behave the same way a filter or control behaves in
                an interactive sheet.

###### To define a prompt in a pixel perfect report

- 
                    On a pixel perfect sheet, define a filter control or a parameter control. For more information on filter controls to sheets, see [Adding filter controls to analysis sheets](./filter-controls.html). For more information on parameter controls, see[Using a control with a parameter in Amazon Quick](./parameters-controls.html).
- 
                    In the new filter or parameter, choose the prompt values that you want. The new prompts are immediately reflected on the sheet. 
- 
                    To export the report with the new prompts, choose **File**, and then choose**Export to PDF**.

Prompts can't be moved to the sheet itself. Instead, they are displayed on the top panel.

After a prompt is created for a pixel-perfect report and is published as a
                dashboard, Quick authors can use the new prompt to configure and
                schedule reports that are sent to Quick dashboard viewers. Dashboard
                viewers can also use these prompts to create their own scheduled reports. For more
                information about reader generated reports, see [Creating a reader generated report in Amazon Quick Sight](./reader-scheduling.html).