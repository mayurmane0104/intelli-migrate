# Creating a dataset using an existing data source - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-existing.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-existing.html)

---

After you make an initial connection to a Salesforce, AWS data store, or other
			database data source, Amazon Quick saves the connection information. It adds the data source to
			the **FROM EXISTING DATA SOURCES** section of the **Create a
				Data Set** page. You can use these existing data sources to create new
			datasets without respecifying connection information.

## Creating a dataset using an existing Amazon S3 data source

			Use the following procedure to create a dataset using an existing Amazon S3 data source.

###### To create a dataset using an existing S3 data source

- 
					On the Amazon Quick start page, choose **Data**.
- 
					Choose **Create**then choose**New dataset**.
- 
					Choose the Amazon S3 data source to use. 
- 
					To prepare the data before creating the dataset, choose **Edit/Preview data**. To create an analysis using the data as-is, choose**Visualize**.

## Creating a dataset using an existing Amazon Athena data source

			To create a dataset using an existing Amazon Athena data source, use the following procedure.

###### To create a dataset from an existing Athena connection profile

- 
					On the Amazon Quick start page, choose **Data**.
- 
					Choose **Create**then choose**New data set**.Choose the connection profile icon for the existing data source that you want to use. Connection profiles are labeled with the data source icon and the name provided by the person who created the connection. 
- 
					Choose **Create data set**.Amazon Quick creates a connection profile for this data source based only on the Athena workgroup. The database and table aren't saved. 
- 
					On the **Choose your table**screen, do one of the following:- 
							To write a SQL query, choose **Use custom SQL**.
- 
							To choose a database and table, first select your database from the **Database**list. Next, choose a table from the list that appears for your database.
 
- 
							

## Create a dataset using an existing Salesforce data source

			Use the following procedure to create a dataset using an existing Salesforce data source.

###### To create a dataset using an existing Salesforce data source

- 
					On the Amazon Quick start page, choose **Data**.
- 
					Choose **Create**then choose**New data set**.
- 
					Choose the Salesforce data source to use. 
- 
					Choose **Create Data Set**.
- 
					Choose one of the following: - 
							**Custom SQL**On the next screen, you can choose to write a query with the **Use custom SQL**option. Doing this opens a screen named**Enter custom SQL query**, where you can enter a name for your query, and then enter the SQL. For best results, compose the query in a SQL editor, and then paste it into this window. After you name and enter the query, you can choose**Edit/Preview data**or**Confirm query**. Choose**Edit/Preview data**to immediately go to data preparation. Choose**Confirm query**to validate the SQL and make sure that there are no errors.
- 
							**Choose tables**To connect to specific tables, for **Data elements: contain your data**, choose**Select**and then choose either**REPORT**or**OBJECT**.To prepare the data before creating an analysis, choose **Edit/Preview data**to open data preparation. Use this option if you want to join to more tables.Otherwise, after choosing a table, choose **Select**.
 
- 
							
- 
					On the next screen, choose one of the following options: - 
							To create a dataset and an analysis using the data as-is, choose **Visualize**.###### NoteIf you don't have enough [SPICE](./spice.html)capacity, choose**Edit/Preview data**. In data preparation, you can remove fields from the dataset to decrease its size or apply a filter that reduces the number of rows returned. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
- 
							To prepare the data before creating an analysis, choose **Edit/Preview data**to open data preparation for the selected report or object. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
 
- 
							

## Creating a dataset using an existing database data source

			Use the following procedure to create a dataset using an existing database data source.

###### To create a dataset using an existing database data source

- 
					On the Amazon Quick start page, choose **Data**.
- 
					Choose **Create**then choose**New data set**.
- 
					Choose the database data source to use, and then choose **Create Data Set**.
- 
					Choose one of the following: - 
							**Custom SQL**On the next screen, you can choose to write a query with the **Use custom SQL**option. Doing this opens a screen named**Enter custom SQL query**, where you can enter a name for your query, and then enter the SQL. For best results, compose the query in a SQL editor, and then paste it into this window. After you name and enter the query, you can choose**Edit/Preview data**or**Confirm query**. Choose**Edit/Preview data**to immediately go to data preparation. Choose**Confirm query**to validate the SQL and make sure that there are no errors.
- 
							**Choose tables**To connect to specific tables, for **Schema: contain sets of tables**, choose**Select**and then choose a schema. In some cases where there is only a single schema in the database, that schema is automatically chosen, and the schema selection option isn't displayed.To prepare the data before creating an analysis, choose **Edit/Preview data**to open data preparation. Use this option if you want to join to more tables.Otherwise, after choosing a table, choose **Select**.
 
- 
							
- 
					Choose one of the following options: - 
							Prepare the data before creating an analysis. To do this, choose **Edit/Preview data**to open data preparation for the selected table. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
- 
							Create a dataset and an analysis using the table data as-is and import the dataset data into [SPICE](./spice.html)for improved performance (recommended). To do this, check the SPICE indicator to see if you have enough space.If you have enough SPICE capacity, choose **Import to SPICE for quicker analytics**, and then create an analysis by choosing**Visualize**.###### NoteIf you want to use SPICE and you don't have enough space, choose **Edit/Preview data**. In data preparation, you can remove fields from the dataset to decrease its size. You can also apply a filter or write a SQL query that reduces the number of rows or columns returned. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
- 
							Create a dataset and an analysis using the table data as-is and have the data queried directly from the database. To do this, choose the **Directly query your data**option. Then create an analysis by choosing**Visualize**.
 
-