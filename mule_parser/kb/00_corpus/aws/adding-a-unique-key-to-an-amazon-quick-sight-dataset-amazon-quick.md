# Adding a unique key to an Amazon Quick Sight dataset - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/set-unique-key.html](https://docs.aws.amazon.com/quick/latest/userguide/set-unique-key.html)

---

Quick authors can configure a unique key column to a Quick Sight dataset during data preparation. This unique key acts as a global sorting key for the dataset and optimizes query generation for table visuals. When a user creates a table visual in Quick Sight and adds the unique key column to the value field well,data is sorted from left to right up to the unique key column. All columns to the right of the unique key column are ignored in the sort order. Tables that don't contain a unique key are sorted based on the order that the columns appear in the dataset.

The following limitations apply to unique keys:

- 
				Unique keys are only supported for unaggregated tables. 
- 
				If a dataset column is used for column level security (CLS), the column can't also be used as the unique key. 

Use the following procedure to designate a unique key for a dataset in Amazon Quick Sight.

###### To set up a unique key

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
				Choose **Data**.
- 
				Perform one of the following actions: - 
						Navigate to the dataset that you want to add a unique key to, choose the ellpisis (three dots) next to the dataset, and then choose **Edit**.
- 
						Choose **New**then**Dataset**. Choose the dataset that you want to add and then choose**Edit data source**. For more information about creating new datasets in Amazon Quick Sight, see[Creating datasets](./creating-data-sets.html).
 
- 
						
- 
				The data preparation page for the dataset opens. Navigate to the **Fields**pane and locate the field that you want to set as the unique key.
- 
				Choose the ellipsis (three dots) next to the field name, and then choose **Set as unique key**.

After you create a unique key, a key icon appears next to the field to show that the
			field is now the unique key for the dataset. When you save and publish the dataset, the
			unique key configuration is applied to the dataset and to all dashboards and analyses
			that are created with that dataset. To remove a unique key from a dataset, navigate to
			the data preparation page for the dataset, choose the ellipsis next to the unique key
			field, and then choose **Remove as unique key**. After you remove a
			unique key from a dataset, you can designate a different field as the unique key.