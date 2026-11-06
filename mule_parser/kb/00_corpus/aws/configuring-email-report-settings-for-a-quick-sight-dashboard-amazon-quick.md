# Configuring email report settings for a Quick Sight dashboard - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/email-reports-from-dashboard.html](https://docs.aws.amazon.com/quick/latest/userguide/email-reports-from-dashboard.html)

---

| Applies
                    to:Enterprise Edition | 

In Amazon Quick Enterprise edition, you can email a report from any sheet in a dashboard. You can send reports from interactive dashboards and pixel perfect report sheets. Schedules include settings for when to send them, the contents to include, and who receives the email. You can view a sample report and a list of the datasets used in the report. To set up or change the schedule sent from a dashboard, make sure that you're an owner or co-owner of the dashboard.

If you have access to the dashboard, you can change your subscription options by
				opening your view of the dashboard. For more information on how this works, see
					[Subscribing to email reports in Amazon Quick Sight](./subscribing-to-reports.html).

Scheduling options that are available for an email report include the following:

- 
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

You can customize the title of the report, the optional email subject, and the body text.

Although you can configure the report so that everyone who has access receives a copy, this is not usually the best plan. We recommend limiting automated emails, especially those sent to groups. You can start with a small number of subscribers by choosing specific people from the access list. Verify your company's policy before subscribing anyone to a subscription.

You can directly add people to a report subscription in these ways:

- 
					(Recommended) Choose recipients from the provided access list to specify and maintain a list of people who you want to email reports to. You can use the search box to find people by email or group name. 
- 
					To send reports to all of the dashboard's subscribers, choose **Send email report to all users with access to dashboard**when prompted.

Anyone else who wants to get the emails can open the dashboard and set their own subscription options to either opt in or opt out.

###### Important

When you share the dashboard with new Quick user names or groups, they automatically start receiving the email reports. If you don't want this to happen, you need to edit the report settings each time you add people to the dashboard.

For existing email schedules, you can pause the schedule in Amazon Quick Sight while you make
				changes. In the **Schedules** pane, you can pause or resume a
				scheduled report with the toggle that appears under each report. Pausing a report
				does not delete the report's schedule from Quick Sight.

If your report includes custom visuals, be aware that you can't include images from a private network in an email report, even if you can access the images. If you want to include an image, use a publicly available one.

Before you begin, make sure that you are using Amazon Quick Enterprise edition and that you have shared the dashboard with intended recipients.

###### To create or change an email report

- 
					Open Quick and choose **Dashboards**on the navigation pane at left.
- 
					Open a dashboard to configure its email report. 
- 
					At top right, choose **Schedules**, and then choose**Schedules**.
- 
					Choose **ADD SCHEDULE**.
- 
					In the **New schedule**pane that appears, enter the schedule name. Optionally, add a description for the new schedule.
- 
					In the **Content**tab, toggle the**PDF**,**CSV**, or**Excel**switches to choose the report format. CSV and Excel format are currently supported for pixel perfect reports.
- 
					In the **Sheet**dropdown on the**Content**tab, choose the sheet that you want to schedule a report for.If you choose **CSV**or**Excel**, choose the table or pivot table visuals from any sheet of the dashboard that you want to include in the report. You can select up to 5 visuals for each schedule.If you choose **Excel**, one Excel workbook is generated as a final output.
- 
					In the **Dates**tab, choose the frequency for the report in the**Repeat**dropdown. If you're not sure, choose**Send once (Does not repeat)**.
- 
					For **Start date**, choose the start date and runtime that you want to send the first report on.
- 
					For **Timezone**, choose the time zone from the dropdown.
- 
					In the **Email**tab, for**E-mail subject line**, enter a custom subject line, or leave it blank to use the report title.
- 
					Enter the email addresses of the Quick group name of the users or groups that you want to receive the report. You can also select the **Send to all users with access**box to send the report to everyone that has access to the dashboard in your account.
- 
					For **Email header**, enter the header that you want the emal report to show.
- 
					(Optional) For **E-mail body text**, leave it blank or enter a custom message to display at the beginning of the email.
- 
					(Optional) For PDF attachments, you can choose **Include sheet in email body**to show the first page of the PDF snapshot in the email's body.
- 
					Choose the method of attachment that you want the report to use. The following options are available. - 
							**File attachment**– uploads an attachment of the snapshot to the email. The email size can't exceed 10 MB. This limit includes all attachments.
- 
							**Download link**– adds a link to the email body that users can access to download the snapshot report. When a user chooses the download link, they are prompted to sign in before the report starts to download. The link expires one year after the report is sent.
 
- 
							
- 
					(Optional, recommended) To send a sample of the report before you save changes, choose **Send test report**. This option displays beside the user name of the owner of the dashboard.
- 
					Do one of the following: - 
							(Recommended) Choose **Save**to confirm your entries.
- 
							To immediately send a report, choose **Save and run now**. The report is sent immediately, even if your schedule's start date is in the future.
 
-