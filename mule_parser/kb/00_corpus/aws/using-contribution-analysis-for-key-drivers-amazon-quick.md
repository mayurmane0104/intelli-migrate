# Using contribution analysis for key drivers - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-adding-key-drivers.html](https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-adding-key-drivers.html)

---

Amazon Quick Sight can identify the dimensions (categories) that contribute to outliers in measures (metrics) between two points in time. The key driver that contributes to an outlier helps you to answer the question: What happened to cause this anomaly?

If you are already using anomaly detection without contribution analysis, you can enable the existing ML insight to find key drivers. Use the following procedure to add contribution analysis and identify the key drivers behind outliers. Your insight for anomaly detection needs to include a time field and at least one aggregated metric (SUM, AVERAGE, or COUNT). You can include multiple categories (dimension fields) if you wish, but you can also run contribution analysis without specifying any category or dimension field.

You can also use this procedure to change or remove fields as key drivers in your anomaly detection.

###### To add contribution analysis to identify key drivers

- 
						Open your analysis and locate an existing ML insight for anomaly detection. Select the insight widget to highlight it. 
- 
						Choose **Menu Options**(**…**) from the menu on the visual.
- 
						Choose **Configure anomaly**to edit the settings.
- 
						The **Contribution analysis (optional)**setting allows Amazon Quick Sight to analyze the key drivers when an outlier (anomaly) is detected. For example, Amazon Quick Sight can show you the top customers that contributed to a spike in sales in the US for home improvement products. You can add up to four dimensions from your dataset, including dimensions that you didn't add to the field wells of this insight widget.To view a list of dimensions available for contribution analysis, choose **Select fields**.If you want to change the fields you're using as key drivers, change the fields that are enabled in this list. If you disable all of them, Quick Sight won't perform any contribution analysis in this insight. 
- 
						To save your changes, scroll to the bottom of the configuration options, and choose **Save**. To exit without saving, choose**Cancel**. To completely remove these settings, choose**Delete**.