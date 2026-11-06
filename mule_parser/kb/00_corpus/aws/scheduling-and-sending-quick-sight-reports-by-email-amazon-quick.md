# Scheduling and sending Quick Sight reports by email - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sending-reports.html](https://docs.aws.amazon.com/quick/latest/userguide/sending-reports.html)

---

###### Important

Amazon Quick Sight in the Europe (Spain) (eu-south-2) region uses an internal email service (Amazon SES) in the Europe (Ireland) (eu-west-1) to send emails to Quick Sight users. Customer data that's included in scheduled reports, alerts, and other features are passed by email from Europe (Spain) to Europe (Ireland) before it reaches Quick Sight users.

As a privacy protection measure, the following features that send customer data in emails have been limited or disabled by default.

- 
					File attachments and sheet previews in Scheduled Report emails. The [download link option](https://docs.aws.amazon.com/quicksuite/latest/userguide/email-reports-from-dashboard)is the default.
- 
					Emails that use threshold alerts. 
- 
					Anomaly detection alerts. 

For more information about AWS privacy features, see [Privacy Features of AWS
				Services](https://aws.amazon.com/compliance/privacy-features/).

In Enterprise edition, you can send a dashboard in report form either once or on a schedule (daily, weekly, monthly, or yearly). You can email the reports to users or groups who share your Amazon Quick subscription. To receive email reports, the users or group members must meet the following conditions:

- 
				They are part of your Quick subscription. 
- 
				You already shared the dashboard with them. 
- 
				Amazon Quick Sight can't send scheduled emails to more than 5,000 members. 

Amazon Quick Sight generates a custom email snapshot for each user or group based on their data permissions, which are defined in the dashboard. Row Level Security (RLS), Column Level Security (CLS) and Dynamic Default Parameters for email reports works for both scheduled and ad hoc (one-time) emails.

Quick authors can run scheduled reports with the **Report
				now** button in the Quick console or with the [ StartDashboardSnapshotJobSchedule](https://docs.aws.amazon.com//quicksight/latest/APIReference/API_StartDashboardSnapshotJobSchedule.html) API.

Subscribers who are readers see an option for **Reports**
			on the dashboard when an email report is available for that dashboard. They can use the
				**Schedules** menu to subscribe to or unsubscribe from the emails.
			For more information, see [Subscribing to email reports in Amazon Quick Sight](./subscribing-to-reports.html).

You can create up to five schedules for each dashboard.

Quick Sight dashboard viewers can also schedule their own reports for themselves from
			a Quick Sight dashboard. For more information about reader generated reports, see [Creating a reader generated report in Amazon Quick Sight](./reader-scheduling.html).

Use the following topics to learn more about email report settings and report billing.