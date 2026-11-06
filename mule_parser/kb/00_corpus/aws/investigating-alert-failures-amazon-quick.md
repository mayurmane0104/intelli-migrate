# Investigating Alert Failures - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/threshold-alerts-failures.html](https://docs.aws.amazon.com/quick/latest/userguide/threshold-alerts-failures.html)

---

When an alert fails, Quick sends you an email notification about the failure. Alerts can fail for many reasons, including the following:

- 
					The dataset the alert is using was deleted. 
- 
					The owner of the alert lost permissions to the dataset or to certain rows or columns in the dataset. 
- 
					The owner of the alert lost access to the dashboard. 
- 
					There is no data for the data tracked by the alert. 

When a failure occurs, Quick sends you a notification and disables the alert if the reason for the failure isn't likely to be fixed. For example, if the alert fails due to the loss of access to a dashboard, or if the dashboard was deleted. Otherwise, Quick attempts to check your data for threshold breaches again. After four failures, Quick turns off the alert and notifies you that the alert is turned off. If the alert can be checked again, Quick sends you a notification.

To investigate why an alert failed, check that you still have access to the dashboard. Also check that you have permissions to the correct dataset and to the correct rows and columns in the dataset. If you have lost access or permissions, contact the dashboard owner. If you have the necessary access and permissions, you might need to edit your alert to avoid future alert failures.