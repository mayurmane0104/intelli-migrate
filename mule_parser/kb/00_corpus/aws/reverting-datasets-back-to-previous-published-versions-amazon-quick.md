# Reverting datasets back to previous published versions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dataset-versioning.html](https://docs.aws.amazon.com/quick/latest/userguide/dataset-versioning.html)

---

When you save and publish changes to a dataset in Amazon Quick Sight, a new version of the dataset is created. At any time, you can see a list of all the previous published versions of that dataset. You can also preview a specific version in that history, or even revert the dataset back to a previous version, if needed.

The following limitations apply to dataset versioning:

- 
				Only the most recent 1,000 versions of a dataset are shown in the publishing history, and are available for versioning. 
- 
				After you exceed 1,000 published versions, the oldest versions are automatically removed from the publishing history, and the dataset can no longer be reverted back to them. 

Use the following procedure to revert a dataset to a previous published version.

###### To revert a dataset to a previous published version

- 
				From the Quick start page, choose **Data**.
- 
				On the **Data**page, choose a dataset, and then choose**Edit dataset**at upper right.For more information about editing datasets, see [Editing datasets](./edit-a-data-set.html).
- 
				On the dataset preparation page that opens, choose the **Manage**icon in the blue toolbar at upper right, and then choose**Publishing history**.A list of previous published versions appears at right. 
- 
				In the **Publishing history**pane, find the version that you want and choose**Revert**.To preview the version before reverting, choose **Preview**.The dataset is reverted and a confirmation message appears. The **Publishing history**pane also updates to show the active version of the dataset.

## Troubleshooting reverting versions

			Sometimes, the dataset can't be reverted to a specific version for one the following reasons:

- 
					The dataset uses one or more data sources that were deleted. If this error occurs, you can't revert the dataset to a previous version. 
- 
					Reverting would make a calculated field not valid. If this error occurs, you can edit or remove the calculated field, and then save the dataset. Doing this creates a new version of the dataset. 
- 
					One or more columns are missing in the data source. If this error occurs, Quick Sight shows the latest schema from the data source in the preview to reconcile differences between versions. Any calculated field, field name, field type, and filter changes shown in the schema preview are from the version that you want to revert to. You can save this reconciled schema as a new version of the dataset. Or you can return to the active (latest) version by choosing **Preview**on the top (latest) version in the publishing history.