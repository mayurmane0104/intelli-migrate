# Column not found when using Athena with Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-column-not-found.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-athena-column-not-found.html)

---

You can receive a "`column not found`" error if the columns in an
				analysis are missing from the Athena data source. 

In Amazon Quick Sight, open your analysis. On the **Visualize** tab, choose
					**Choose dataset**, **Edit analysis data
					sets**. 

On the **Data sets in this analysis** screen, choose
					**Edit** near your dataset to refresh the dataset. Amazon Quick Sight
				caches the schema for two minutes. So it can take two minutes before the latest
				changes display. 

To investigate how the column was lost in the first place, you can go to the Athena
				console ([https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home)) and check the query history to find queries that edited
				the table.

If this error happened when you were editing a custom SQL query in preview, verify that the name of the column in the query, and check for any other syntax errors. For example, check that the column name isn't enclosed in single quotation marks, which are reserved for strings.

If you still have the issue, verify that your tables, columns, and queries comply
				with Athena requirements. For more information, see [Names
					for Tables, Databases, and Columns](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html) and [Troubleshooting](https://docs.aws.amazon.com/athena/latest/ug/troubleshooting.html) in the *Athena User
					Guide*.