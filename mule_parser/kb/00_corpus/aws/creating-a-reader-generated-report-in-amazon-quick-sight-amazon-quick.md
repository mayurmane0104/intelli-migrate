# Creating a reader generated report in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/reader-scheduling.html](https://docs.aws.amazon.com/quick/latest/userguide/reader-scheduling.html)

---

If a Amazon Quick author has set up a prompted report for a Quick Sight pixel perfect
            report, Quick Sight dashboard viewers can use the prompt to schedule their own reports
            for themselves. For more information about prompts for pixel perfect reports, see [Setting up prompts for paginated reports](./paginated-reports-prompts.html).

Use the following sections to learn how to create and modify a reader generated report.

###### Topics

## Creating a reader generated report

            Use the following procedure to create a reader generated report.

###### To create a reader generated report

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Open the dashboard that you want to create a report for. 
- 
                    Choose the **Scheduling**at the top of the dashboard page.
- 
                    The scheduling pane opens. To add a new report schedule, choose **Add**. If you do not see the**Add**button, the dashboard does not contain a pixel perfect sheet, or your Quick account does not have the Pixel perfect reports add on. For more information about the paginater reports add on, see[Getting started](./qs-reports-getting-started.html).
- 
                    For **Schedule name**, enter a name for the new schedule. The schedule name can be up to 100 chatacters long.
- 
                    For **Description**, choose the view option that you want the report to use. You can choose from the following views:- 
                            **Custom view**– The current view of the dashboard.
- 
                            **Original view**– The author published view of the dashboard.
 
- 
                            
- 
                    For **Content**, choose the pixel perfect report sheet that you want to generate a PDF report for.
- 
                    For **Dates**, choose the frequency at which you want to receive the report. Scheduling options that are available for an email report include the following:- 
                            **Once (Does not repeat)**– Sends the report only once at the date and time that you choose.
- 
                            **Daily**– Repeats daily at the time that you choose.
- 
                            **Weekly**– Repeats each week on the same day or days at the time that you choose. You can also use this option to send reports in weekly intervals, such as every other week or every three weeks.
- 
                            **Monthly**– Repeats each month on the same day of the month at the time that you choose. You can also use this option to send reports on specific days of the month, such as the second Wednesday or the last Friday of each month.
- 
                            **Yearly**– Repeats each year on the same day of the month or months selected at the time that you choose. You can also use this option to send reports on specific days or sets of days in selected months. For example, you can configure a report to be sent on the first Monday of January, March, and September, or on July 14th, or on the second day of February, April, and June each year.
- 
                            **Custom**– Configure your own scheduled report that best fits your business needs.
 The scheduled report is sent within 1 hour from the specified time. Delays may occur during peak hours. 
- 
                            
- 
                    In the **Email**tab, for**E-mail subject line**, enter a custom subject line, or leave it blank to use the report title.
- 
                    Enter the email addresses of the Quick group name of the users or groups that you want to receive the report. 
- 
                    For **Email header**, enter the header that you want the emal report to show.
- 
                    (Optional) For **E-mail body text**, leave it blank or enter a custom message to display at the beginning of the email.
- 
                    (Optional, recommended) To send a sample of the report before you save changes, choose **Send test report**.
- 
                    Do one of the following: - 
                            (Recommended) Choose **Save**to confirm your entries.
- 
                            To immediately send a report, choose **Save and run now**. The report is sent immediately, even if your schedule's start date is in the future.
 
- 
                            

After you save a report schedule, the schedule appears in the
                    **Schedules** pane. Reader generated reports are only available
                to the user that created them and can't be shared.

## Loading a saved view of a Quick Sight reader generated report

            Amazon Quick readers can use the **Schedules** pane to load a
                saved view of any scheduled pixel perfect report thay have created or received. Use the
                following procedure to load a saved review of a scheduled report.

###### To load a saved view of a scheduled report

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Open the dashboard that contains the report that you want to change. 
- 
                    Choose the **Scheduling**at the top of the dashboard page.
- 
                    The scheduling pane opens. Locate the schedule that you want to change and choose the ellipsis (three dots) icon next to the report to open the schedule menu, and then choose **Details**.
- 
                    Choose **Load saved view**. The saved view of the dashboard that was used for the selected schedule is rendered. All filter values that were active when the dashboard snapshot was taken are applied to the dashboard. When a saved view of a dashboard is loaded, the reader's current view of the dashboard is lost.

## Updating the view of a scheduled reader generated report

            After a Amazon Quick reader has created a report in Quick Sight, they can use the
                    **Schedules** pane to update the dashboard view that is used in
                the scheduled report. Use the following procedure to update the dashboard view of a
                scheduled report.

###### To change the dashboard view of a scheduled report

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Open the dashboard that contains the report that you want to change. 
- 
                    Choose the **Scheduling**at the top of the dashboard page.
- 
                    The scheduling pane opens. Locate the schedule that you want to change and choose the ellipsis (three dots) icon next to the report to open the schedule menu, and then choose **Details**.
- 
                    Choose **Load saved view**. The saved view of the dashboard that was used for the selected schedule is rendered. All filter values that were active when the dashboard snapshot was taken are applied to the dashboard. When a saved view of a dashboard is loaded, the reader's current view of the dashboard is lost.
- 
                    Update the dashboard filters that you want to change. 
- 
                    Choose the **Scheduling**at the top of the dashboard page.
- 
                    The scheduling pane opens. Locate the schedule that you want to change and choose the ellipsis (three dots) icon next to the report to open the schedule menu, and then choose **Edit**.
- 
                    Navigate to the **Dashboard view**section, and then choose**Custom view**. The new filter values that you updated are applied to the dashboard report.
- 
                    Choose **Save**to update the schedule.

## Updating a reader generated report schedule

            After they create a reader generated report, Amazon Quick readers can use the
                    **Schedules** pane to make a report schedule active or
                inactive. Use the following procedure to update active status of a reader generated
                report schedule.

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Open the dashboard that contains the report that you want to change. 
- 
                    Choose the **Scheduling**at the top of the dashboard page to open the**Schedules**pane.
- 
                    Choose **Schedules**.
- 
                    Navigate to the **My schedules**section and find the schedule that you want to update.
- 
                    Use the toggle to set the report schedule to **Active**or**Inactive**.
- 
                    When you are finished making changes to the report schedule, close the **Schedules**pane.