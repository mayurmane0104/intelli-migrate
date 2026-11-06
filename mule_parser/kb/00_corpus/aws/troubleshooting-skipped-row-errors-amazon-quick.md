# Troubleshooting skipped row errors - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-skipped-rows.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshooting-skipped-rows.html)

---

When you import data, Amazon Quick Sight previews a portion of your data. If it can't interpret a row for any reason, Quick Sight skips the row. In some cases, the import will fail. When this happens, Quick Sight returns an error message that explains the failure.

Fortunately, there's a limited number of things that can go wrong. Some issues can be avoided by being aware of examples like the following:

- 
				Make sure that there is no inconsistency between the field data type and the field data, for example occasional string data in a field with a numeric data type. Here are a few examples that can be difficult to detect when scanning the contents of a table: - 
						`''`– Using an empty string to indicate a missing value
- 
						`'NULL'`– Using the word "null" to indicate a missing value
- 
						`$1000`– Including a dollar sign in a currency value turns it into a string
- 
						`'O'Brien'`– Using punctuation to mark a string that itself contains the same punctuation.
 However, this type of error isn't always this easy to find, especially if you have a lot of data, or if your data is typed in by hand. For example, some customer service or sales applications involve entering information verbally provided by customers. The person who originally typed in the data might have put it in the wrong field. They might add, or forget to add, a character or digit. For example, they might enter a date of "0/10/12020" or enter someone's gender in a field meant for age. 
- 
						
- 
				Make sure that your imported file is correctly processed with or without a header. If there is a header row, make sure that you choose the **Contains header**upload option.
- 
				Make sure that the data doesn't exceed one or more of the [Data source quotas](./data-source-limits.html).
- 
				Make sure that the data is compatible with the [Supported data types and values](./supported-data-types-and-values.html).
- 
				Make sure that your calculated fields contain data that works with the calculation, rather than being incompatible with or excluded by the function in the calculated field. For example, if you have a calculated field in your dataset that uses [parseDate](./parseDate-function.html), Quick Sight skips rows where that field doesn't contain a valid date.

Quick Sight provides a detailed list of the errors that occur when the SPICE engine attempts to ingest data. When a saved dataset reports skipped rows, you can view the errors so you can take action to fix the issues.

###### To view errors for rows that were skipped during SPICE ingestion (data import)

- 
				Choose **Data**at left. In the**Datasets**tab, choose the problematic dataset to open it.
- 
				On the dataset details page that opens, choose the **Refresh**tab.SPICE ingestion history is shown at bottom. 
- 
				For the ingestion with the error, choose **View error summary**. This link is located under the**Status**column.
- 
				Examine the **File import log**that opens. It displays the following sections:- 
						**Summary**– Provides a percentage score of how many rows were skipped out of the total number of rows in the import. For example, if there are 864 rows skipped out of a total of 1,728, the score is 50.00%.
- 
						**Skipped Rows**– Provides the row count, field name, and error message for each set of similar skipped rows.
- 
						**Troubleshooting**– Provides a link to download a file that contains error information.
 
- 
						
- 
				Under **Troubleshooting**, choose**Download error rows file**.The error file has a row for each error. The file is named `error-report_123_fe8.csv`, where`123_fe8`is replaced with a unique identifying string. The file contains the following columns:- 
						
						**ERROR_TYPE**– The type or error code for the error that occurred when importing this row. You can look up this error in the[SPICE ingestion error codes](./errors-spice-ingestion.html)section that follows this procedure.
- 
						**COLUMN_NAME**– The name of the column in your data that caused the error.
- 
						All the columns from your imported row – The remaining columns duplicate the entire row of data. If a row has more than one error, it can appear multiple times in this file. 
 
- 
						
						
- 
				Choose **Edit data set**to make changes to your dataset. You can filter the data, omit fields, change data types, adjust existing calculated fields, and add calculated fields that validate the data.
- 
				After you've made changes indicated by the error codes, import the data again. If more SPICE ingestion errors appear in the log, step through this procedure again to fix all remaining errors. 

###### Tip

If you can't solve the data issues in a reasonable amount of time by using the dataset editor, consult the administrators or developers who own the data. In the long run, it's more cost-effective to cleanse the data closer to its source, rather than adding exception processing while you're preparing the data for analysis. By fixing it at the source, you avoid a situation where multiple people fix the errors in different ways, resulting in different reporting results later on.

###### To practice troubleshooting skipped rows

- 
				Extract the files into a folder that you can use to upload the sample .csv file into Quick Sight. The zip file contains the following two text files: - 
						`sample dataset - data ingestion error.csv`– A sample .csv file that contains issues that cause skipped rows. You can try to import the file yourself to see how the error process works.
- 
						`sample data ingestion error file`– A sample error file generated during SPICE ingestion while importing the sample .csv file into Quick Sight.
 
- 
						
- 
				Import the data by following these steps: - 
						Choose **Data**,**Datasets**tab,**New**,**Dataset**.
- 
						Choose **Upload a file**.
- 
						Find and choose the file named `sample dataset - data ingestion error.csv`.
- 
						Choose **Upload a file**,**Edit settings and prepare data**.
- 
						Choose **Save**to exit.
 
- 
						
- 
				Choose your dataset to view its information, then choose **View error summary**. Examine the errors and the data to help you resolve the issues.