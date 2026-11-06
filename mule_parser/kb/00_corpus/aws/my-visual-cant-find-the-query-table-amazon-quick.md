# My visual can’t find the query table - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-dataset-changed-tables.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-dataset-changed-tables.html)

---

In this case, the visuals in your analysis aren't working as expected. The error
				message says `"Amazon Quick Sight can’t find the query table."`

The most common cause of this error is that your data source schema changed. For
				example, it's possible a table name changed from `x_table` to
					`y_table`.

Depending on how the dataset accesses the data source, choose one of the following.

- 
					If the dataset is based on custom SQL, do one or more of the following: - 
							Edit the dataset. 
- 
							Edit the SQL statement. For example, if the table name changed from `x_table`to`y_table`, you can update the FROM clause in the SQL statement to refer to the new table instead.
 When you're done, choose **Save & visualize**, then choose each visual and readd the fields as needed.
- 
							
- 
					If the dataset isn't based on custom SQL, do the following: - 
							Create a new dataset using the new table, `y_table`for example.
- 
							Open your analysis. 
- 
							Replace the original dataset with the newly created dataset. If there are no column changes, all the visuals should work after you replace the dataset. For more information, see [Replacing datasets](./replacing-data-sets.html).
 
-