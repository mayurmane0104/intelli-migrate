# Using SPICE data in an analysis - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/spice-in-an-analysis.html](https://docs.aws.amazon.com/quick/latest/userguide/spice-in-an-analysis.html)

---

When you use stored data to create an analysis, a data import indicator appears next
			to the dataset list at the top of the **Fields list** pane. When you
			first open the analysis and the dataset is importing, a spinner icon appears.

After the SPICE import is complete, the indicator displays the percentage of rows that were successfully imported. A message also appears at the top of the visualization pane to provide counts of the rows imported and skipped.

If any rows were skipped, you can choose **View summary** in this
			message bar to see details about why those rows failed to import. To edit the dataset
			and resolve the issues that led to skipped rows, choose **Edit data
				set**. For more information about common causes for skipped rows, see [Troubleshooting skipped row errors](./troubleshooting-skipped-rows.html).

If an import fails altogether, the data import indicator appears as an exclamation
			point icon, and an **Import failed** message is displayed.