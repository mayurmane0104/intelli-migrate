# My visual can’t find missing columns - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-dataset-changed-columns.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-dataset-changed-columns.html)

---

The visuals in my analysis aren't working as expected. The error message says
					`"The column(s) used in this visual do not exist."`

The most common cause of this error is that your data source schema changed. For
				example, it's possible a column name changed from `a_column` to
					`b_column`.

Depending on how your dataset accesses the data source, choose one of the following.

- 
					If the dataset is based on custom SQL, do one or more of the following: - 
							Edit the dataset. 
- 
							Edit the SQL statement. For example, if the table name changed from `a_column`to`b_column`, you can update the SQL statement to create an alias:`SELECT b_column as a_column`. By using the alias to maintain the same field name in the dataset, you avoid having to add the column to your visuals as a new entity.
 When you're done, choose **Save & visualize**.
- 
							
- 
					If the dataset isn't based on custom SQL, do one or more of the following: - 
							Edit the dataset. 
- 
							For fields that now have different names, rename them in the dataset. You can use the field names from your original dataset. Then open your analysis and add the renamed fields to the affected visuals. 
 When you're done, choose **Save & visualize**.
-