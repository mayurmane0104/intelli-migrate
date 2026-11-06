# Refreshing data in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/refreshing-data.html](https://docs.aws.amazon.com/quick/latest/userguide/refreshing-data.html)

---

When refreshing data, Amazon Quick Sight handles datasets differently depending on the connection properties and the storage location of the data.

If Quick Sight connects to the data store by using a direct query, the data automatically refreshes when you open an associated dataset, analysis, or dashboard. Filter controls are refreshed automatically every 24 hours.

To refresh SPICE datasets, Quick Sight must independently authenticate
		using stored credentials to connect to the data. Quick Sight can't refresh manually
		uploaded data—even from S3 buckets, even though it's stored in
		SPICE—because Quick Sight doesn't store its connection and location
		metadata. If you want to automatically refresh data that's stored in an S3 bucket, create a
		dataset by using the **S3** data source card.

For files that you manually uploaded to SPICE, you refresh these manually
		by importing the file again. If you want to reuse the name of the original dataset for the
		new file, first rename or delete the original dataset. Then give the preferred name to the
		new dataset. Also, check that the field names are the same name and data type. Open your
		analysis, and replace the original dataset with the new dataset. For more information, see
			[Replacing datasets](./replacing-data-sets.html).

You can refresh your [SPICE](./spice.html) datasets at any
		time. Refreshing imports the data into SPICE again, so the data includes any
		changes since the last import.

For Amazon Quick Sight Standard Edition, you can do a full refresh of your SPICE data at any time. For Amazon Quick Sight Enterprise Edition, you can do a full refresh or an incremental refresh (SQL-based data sources only) at any time.

###### Note

If your dataset uses CustomSQL, refreshing incrementally might not benefit you. If the SQL query is complex, your database may not be able to optimize the filter with the look-back window. This can cause the query that pulls in the data to take longer than a full refresh. We recommend that you try reducing query execution time by refactoring the custom SQL. Note that results might vary depending on the type of optimization you make.

You can refresh SPICE data by using any of the following approaches:

- 
			You can use the options on **Datasets**page.
- 
			You can refresh a dataset while editing a dataset. 
- 
			You can schedule refreshes in the dataset settings. 
- 
			You can use the [CreateIngestion](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateIngestion.html)API operation to refresh the data.

When you create or edit a SPICE dataset, you can enable email notifications
		about data loading status. This option notifies the owners of the dataset if the data fails
		to load or refresh. To turn on notifications, select the **Email owners when a
			refresh fails** option that appears on the **Finish data set
			creation** screen. This option isn't available for datasets that you create by
		using **Upload a File** on the datasets page. 

In the following topics, you can find an explanation of different approaches to refreshing and working with SPICE data.