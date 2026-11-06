# Adding an ML insight to detect outliers and key drivers - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-adding-anomaly-insights.html](https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-adding-anomaly-insights.html)

---

You can add an ML insight that detects *anomalies*, which are outliers that seem significant. To get
					started, you create for your insight a widget, also known as an *autonarrative*. As you configure your options, you
					can view a limited screenshot of your insight in the
						**Preview** pane at screen right.

In your insight widget, you can add up to five dimension fields that are not
					calculated fields. In the field wells, values for
						**Categories** represent the dimensional values that
					Amazon Quick Sight uses to split the metric. For example, let's say that you are
					analyzing revenue across all product categories and product SKUs. There are 10
					product categories, each with 10 product SKUs. Amazon Quick Sight splits the metric by the
					100 unique combinations and runs anomaly detection on each combination for the
					split.

The following procedure shows how to do this, and also how to add contribution
					analysis to detect the key drivers that are causing each anomaly. You can add
					contribution analysis later, as described in [Using contribution analysis for key drivers](./anomaly-detection-adding-key-drivers.html).

###### To set up outlier analysis, including key drivers

- 
						Open your analysis and in the toolbar, choose **Insights**, then**Add**. From the list, choose**Anomaly detection**and**Select**.
- 
						Follow the screen prompt on the new widget, which tells you to choose fields for the insight. Add at least one date, one measure, and one dimension. 
- 
						Choose **Get started**on the widget. The configuration screen appears.
- 
						Under **Compute options**, choose values for the following options.- 
								For **Combinations to be analysed**, choose one of the following options:- 
										**Hierarchical**Choose this option if you want to analyze the fields hierarchically. For example, if you chose a date (T), a measure (N), and three dimension categories (C1, C2, and C3), Quick Sight analyses the fields hierarchically, as shown following. `T-N, T-C1-N, T-C1-C2-N, T-C1-C2-C3-N`
- 
										**Exact**Choose this option if you want to analyze only the exact combination of fields in the Category field well, as they are listed. For example, if you chose a date (T), a measure (N), and three dimension categories (C1, C2, and C3), Quick Sight analyses only the exact combination of category fields in the order they are listed, as shown following. `T-C1-C2-C3-N`
- 
										**All**Choose this option if you want to analyze all field combinations in the Category field well. For example, if you chose a date (T), a measure (N), and three dimension categories (C1, C2, and C3), Quick Sight analyses all combinations of fields, as shown following. `T-N, T-C1-N, T-C1-C2-N, T-C1-C2-C3-N, T-C1-C3-N, T-C2-N, T-C2-C3-N, T-C3-N`
 If you chose a date and a measure only, Quick Sight analyses the fields by date and then by measure. In the **Fields to be analyzed**section, you can see a list of fields from the field wells for reference.
- 
										
- 
								For **Name**, enter a descriptive alphanumeric name with no spaces, or choose the default value. This provides a name for the computation.If you plan on editing the narrative that automatically displays on the widget, you can use the name to identify this widget's calculation. Customize the name if you plan to edit the autonarrative and if you have other similar calculations in your analysis. 
 
- 
								
- 
						In the **Display options**section, choose the following options to customize what is displayed in your insight widget. You can still explore all your results, no matter what you display.- 
								**Maximum number of anomalies to show**– The number of outliers you want to display in the narrative widget.
- 
								**Severity**– The minimum level of severity for anomalies that you want to display in the insight widget.A *level of severity*is a range of anomaly scores that is characterized by the lowest actual anomaly score included in the range. All anomalies that score higher are included in the range. If you set severity to**Low**, the insight displays all of the anomalies that rank between low and very high. If you set the severity to**Very high**, the insight displays only the anomalies that have the highest anomaly scores.You can use the following options: - 
										**Very high**
- 
										**High and above**
- 
										**Medium and above**
- 
										**Low and above**
 
- 
										
- 
								**Direction**– The direction on the x-axis or y-axis that you want to identify as anomalous. You can choose from the following:- 
										**Higher than expected**to identify higher values as anomalies.
- 
										**Lower than expected**to identify lower values as anomalies.
- 
										**[ALL]**to identify all anomalous values, high and low (default setting).
 
- 
										
- 
								**Delta**– Enter a custom value to use to identify anomalies. Any amount higher than the threshold value counts as an anomaly. The values here change how the insight works in your analysis. In this section, you can set the following:- 
										**Absolute value**– The actual value to use. For example, suppose this is 48. Amazon Quick Sight then identifies values as anomalous when the difference between a value and the expected value is greater than 48.
- 
										**Percentage**– The percentage threshold to use. For example, suppose this is 12.5%. Amazon Quick Sight then identifies values as anomalous when the difference between a value and the expected value is greater than 12.5%.
 
- 
										
- 
								**Sort by**– Choose a sort method for your results. Some methods are based on the anomaly score that Amazon Quick Sight generates. Amazon Quick Sight gives higher scores to data points that look anomalous. You can use any of the following options:- 
										**Weighted anomaly score**– The anomaly score multiplied by the log of the absolute value of the difference between the actual value and the expected value. This score is always a positive number.
- 
										**Anomaly score**– The actual anomaly score assigned to this data point.
- 
										**Weighted difference from expected value**– The anomaly score multiplied by the difference between the actual value and the expected value (default).
- 
										**Difference from expected value**– The actual difference between the actual value and the expected value (that is, actual−expected).
- 
										**Actual value**– The actual value with no formula applied.
 
- 
										
 
- 
								
- 
						In the **Schedule options**section, set the schedule for automatically running the insight recalculation. The schedule runs only for published dashboards. In the analysis, you can run it manually as needed. Scheduling includes the following settings:- 
								**Occurrence**– How often that you want the recalculation to run: every hour, every day, every week, or every month.
- 
								**Start schedule on**– The date and time to start running this schedule.
- 
								**Timezone**– The time zone that the schedule runs in. To view a list, delete the current entry.
 
- 
								
- 
						In the **Top contributors**section, set Amazon Quick Sight to analyze the key drivers when an outlier (anomaly) is detected.For example, Amazon Quick Sight can show the top customers that contributed to a spike in sales in the US for home improvement products. You can add up to four dimensions from your dataset. These include dimensions that you didn't add to the field wells of this insight widget. For a list of dimensions available for contribution analysis, choose **Select fields**.
- 
						Choose **Save**to confirm your choices. Choose**Cancel**to exit without saving.
- 
						From the insight widget, choose **Run now**to run the anomaly detection and view your insight.

The amount of time that anomaly detecton takes to complete varies depending on how many unique data points you are analyzing. The process can take a few minutes for a minimum number of points, or it can take many hours.

While it's running in the background, you can do other work in your analysis.
					Make sure to wait for it to complete before you change the configuration, edit
					the narrative, or open the **Explore anomalies** page for this
					insight.

The insight widget needs to run at least once before you can see results. If you think the status might be out of date, you can refresh the page. The insight can have the following states.

| Appears on the Page | Status | 
|---|---|
| Run nowbutton | The job has not yet started. | 
| Message about Analyzing for
									anomalies | The job is currently running. | 
| Narrative about the detected anomalies (outliers) | The job has run successfully. The message says when this widget's calculation was last updated. | 
| Alert icon with an exclamation point ( !) | This icon indicates there was an error during the last run.
									If the narrative also displays, you can still use Explore anomaliesto use data from the
									previous successful run. |