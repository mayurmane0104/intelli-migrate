# Editing datasets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/edit-a-data-set.html](https://docs.aws.amazon.com/quick/latest/userguide/edit-a-data-set.html)

---

You can edit an existing dataset to perform data preparation. For more information
			about Quick Sight data preparation functionality, see [Preparing data in Amazon Quick Sight](./preparing-data.html).

You can open a dataset for editing from the **Datasets** page, or
			from the analysis page. Editing a dataset from either location modifies the dataset for
			all analyses that use it.

## Things to consider when editing datasets

			In two situations, changes to a dataset might cause concern. One is if you deliberately edit the dataset. The other is if your data source has changed so much that it affects the analyses based on it.

###### Important

Analyses that are in production usage should be protected so they continue to function correctly.

We recommend the following when you're dealing with data changes:

- 
					Document your data sources and datasets, and the visuals that rely upon them. Documentation should include screenshots, fields used, placement in field wells, filters, sorts, calculations, colors, formatting, and so on. Record everything that you need to recreate the visual. You can also track which Quick Sight resources use a dataset in the dataset management options. For more information, see [Tracking dashboards and analyses that use a dataset](./track-analytics-that-use-dataset.html).
- 
					When you edit a dataset, try not to make changes that might break existing visuals. For example, don't remove columns that are being used in a visual. If you must remove a column, create a calculated column in its place. The replacement column should have the same name and data type as the original. 
- 
					If your data source or dataset changes in your source database, adapt your visual to accommodate the change, as described previously. Or you can try to adapt the source database. For example, you might create a view of the source table (document). Then if the table changes, you can adjust the view to include or exclude columns (attributes), change data types, fill null values, and so on. Or, in another circumstance, if your dataset is based on a slow SQL query, you might create a table to hold the results of the query. If you can't sufficiently adapt the source of the data, recreate the visuals based on your documentation of the analysis. 
- 
					If you no longer have access to a data source, your analyses based on that source are empty. The visuals that you created still exist, but they can't display until they have some data to show. This result can happen if permissions are changed by your administrator. 
- 
					If you remove the dataset a visual is based on, you might need to recreate it from your documentation. You can edit the visual and select a new dataset to use with it. If you need to consistently use a new file to replace an older one, store your data in a location that is consistently available. For example, you might store your .csv file in Amazon S3 and create an S3 dataset to use for your visuals. For more information on access files stored in S3, see [Creating a dataset using Amazon S3 files](./create-a-data-set-s3.html).Or you can import the data into a table, and base your visual on a query. This way, the data structures don't change, even if the data contained in them changes. 
- 
					To centralize data management, consider creating general, multiple-purpose datasets that others can use to create their own datasets from. For more information, see [Creating a dataset using an existing dataset in Amazon Quick](./create-a-dataset-existing-dataset.html).

## Editing a dataset from the Datasets page

			- 
					From the Quick start page, choose **Data**at left.
- 
					On the **Data**page that opens, choose the dataset that you want to edit, and then choose**Edit dataset**at upper right.The data preparation page opens. For more information about the types of edits you can make to datasets, see [Preparing data in Amazon Quick Sight](./preparing-data.html).

## Editing a dataset in an analysis

			Use the following procedure to edit a dataset from the analysis page.

###### To edit a dataset from the analysis page

- 
					In your analysis, choose the pencil icon at the top of the **Fields list**pane.
- 
					In **Data sets in this analysis**page that opens, choose the three dots at right of the dataset that you want to edit, and then choose**Edit**.The dataset opens in the data preparation page.For more information about the types of edits you can make to datasets, see [Preparing data in Amazon Quick Sight](./preparing-data.html).