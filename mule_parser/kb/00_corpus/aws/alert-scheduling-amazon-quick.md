# Alert Scheduling - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/threshold-alerts-scheduling.html](https://docs.aws.amazon.com/quick/latest/userguide/threshold-alerts-scheduling.html)

---

When you create an alert, Quick checks your data for any breaches against the thresholds you set based on when your dataset is scheduled to refresh. The information presented in the alert varies based on the visual type that you're creating an alert for. For SPICE datasets, alert rules are checked after a successful refresh of your SPICE dataset. For direct query datasets, alert rules are checked at a random time between 6:00 PM and 8:00 AM in the AWS Region that holds the dataset by default.

If you're a dataset owner, you can set an alert evaluation schedule in the dataset settings. See the following procedure to learn how.

###### To set an alert evaluation schedule for a dataset

- 
					In Quick, choose **Data**in the navigation bar at left.
- 
					Choose the dataset that you want to schedule alert evaluations for. 
- 
					Choose **Set alert schedule**.
- 
					In the **Set alert schedule**page that opens, do the following.- 
							For **Time zone**, choose a time zone.
- 
							For **Repeats**, choose how often you want the data to be evaluated.
- 
							For **Starts**, enter the time that you want the alert evaluation to start.
 
-