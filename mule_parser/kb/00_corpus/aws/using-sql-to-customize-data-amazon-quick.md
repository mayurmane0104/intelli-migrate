# Using SQL to customize data - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/adding-a-SQL-query.html](https://docs.aws.amazon.com/quick/latest/userguide/adding-a-SQL-query.html)

---

When you create a dataset or prepare your data for use in an analysis, you can customize the data in the query editor.

The query editor is made up of multiple components, as follows:

- 
				**Query mode**– At the top left, you can choose between direct query or SPICE query modes:- 
						**Direct query**– To run the SELECT statement directly against the database
- 
						**SPICE**– To run the SELECT statement against data that was previously stored in memory
 
- 
						
- 
				**Fields**– Use this section to disable fields you want to remove from the final dataset. You can add calculated fields in this section, and augment your data with SageMaker AI
- 
				**Query archive**– Use this section to find previous version of your SQL queries.
- 
				**Filters**– Use this section to add, edit, or remove filters.
- 
				**Schema explorer**– This section only appears while you are editing SQL. You can use it to explore your schemas, tables, fields, and data types.
- 
				**SQL editor**– Use this to edit your SQL. The SQL editor, which offers syntax highlighting, basic autocomplete, autoindent, and line numbering. You can specify a SQL query only for datasets that come from data sources compatible with SQL. Your SQL must conform to the target database requirements regarding syntax, capitalization, command termination, and so on. If you prefer, you can instead paste SQL from another editor.
- 
				**Data workspace**– When the SQL editor is closed, the data workspace displays at top right with a grid background. Here you can see a graphical representation of your data objects, including queries, tables, files, and joins created in the join editor.To view details about each table, use the data source options menu and choose **Table details**or**Edit SQL Query**. Details display for table name and alias, schema, data source name, and data source type. For upload settings on a file, choose**Configure upload settings**from the data source options menu to view or change the following settings:- 
						Format – the file format, CSV, CUSTOM, CLF, and so on 
- 
						The starting row – the row to start with 
- 
						The text qualifier – double quote or single quote 
- 
						Header – indicates if the file includes a header row 
 
- 
						
- 
				**Preview rows**– A preview of the sampled rows appear at bottom right when the join configuration editor isn't in use.
- 
				**Join configuration**editor – The join editor opens when you have more than one data object in the data workspace. To edit a join, you select the join icon between two tables (or files). Choose a join type and the fields to join on, by using the join configuration panel at the bottom of the screen. Then choose**Apply**to create the join. You must complete all joins before you can save your work.

To add more queries, tables, or files, use the **Add data** option
			above the workspace. 

## Creating a basic SQL query

			Use the following procedure to connect to a data source by using a custom SQL query.

###### To create a basic SQL query

- 
					Create a new data source and validate the connection. 
- 
					Fill in the options necessary to connection, however you don't need to select a schema or a table. 
- 
					Choose **Use custom SQL**.
- 
					(Optional) You can enter your query in the SQL editor, or continue on to the next step to use the full-screen version. To enter it now, create a name for the query. Then type or paste a SQL query into the editor. The SQL editor offers syntax highlighting, basic autocomplete, autoindent, and line numbering. (Optional) Choose **Confirm query**to validate it and view settings for direct query, SPICE memory, and SageMaker AI settings.
- 
					Choose **Edit/Preview data**. The full query editor appears with the SQL editor displayed. The query is processed and a sample of the query results displays in the data preview pane. You can make changes to the SQL and confirm them by choosing**Apply**. When you are done with the SQL, choose**Close**to continue.
- 
					At the top, enter a name for the dataset. Then choose **Save & visualize**.

### Modifying existing queries

###### To update a SQL query

- 
						Open the dataset that you want to work with. 
- 
						In the workspace with the grid, locate the box-shaped object that represents the existing query. 
- 
						Open the options menu on the query object and choose **Edit SQL query**. If this option doesn't appear in the list, the query object isn't based on SQL.To view previous versions of queries, open the **Query archive**at left.