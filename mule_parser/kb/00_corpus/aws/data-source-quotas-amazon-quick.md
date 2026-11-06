# Data source quotas - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/data-source-limits.html](https://docs.aws.amazon.com/quick/latest/userguide/data-source-limits.html)

---

Data sources that you use with Amazon Quick Sight must conform to the following quotas.

## SPICE quotas for imported data

			When you create a new dataset in Amazon Quick Sight, [SPICE](./spice.html) limits the number of rows you can add to a
				dataset. You can ingest data into SPICE from a query or from a file.
				Each file can have up to 2,000 columns. Each column name can have up to 127 Unicode
				characters. Each field can have up to 2,047 Unicode characters.If you use the new data preparation experience to create your SPICE dataset, each field can have up to 65,534 Unicode characters. 

To retrieve a subset of data from a larger set, you can deselect columns or apply filters to reduce the size of the data. If you are importing from Amazon S3, each manifest can specify up to 1,000 files.

Quotas for SPICE are as follows:

- 
					2,047 Unicode characters for each field. (65,534 Unicode characters with new data preparation experience) 
- 
					127 Unicode characters for each column name 
- 
					2,000 columns for each file 
- 
					1,000 files for each manifest 
- 
					For Standard edition, 25 million (25,000,000) rows or 25 GB for each dataset 
- 
					For Enterprise edition, 2 billion (2,000,000,000) rows or 2 TB for each dataset 

All quotas apply to SPICE datasets with row-level security, as well.

In rare cases, if you're ingesting large rows into SPICE, you might reach the quota for gigabytes per dataset before you reach the quota on rows. The size is based on the SPICE capacity the data occupies after ingestion into SPICE.

## Quotas for direct SQL queries

			If you aren't importing data into SPICE, different quotas apply for space and time. For operations such as connecting, sampling data for a dataset, and generating visuals, timeouts can occur. In some cases, these are timeout quotas set by the source database engine. In other cases, such as visualizing, Amazon Quick Sight generates a timeout after 2 minutes.

However, not all database drivers react to the 2-minute timeout, for example Amazon Redshift.
				In these cases, the query runs for as long as it takes for the response to return,
				which can result in long-running queries on your database. When this happens, you
				can cancel the query from the database server to free up database resources. Follow
				the instructions for your database server about how to do this. For example, for
				more information on how to cancel queries in Amazon Redshift, see [Canceling a query in
					Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/cancel_query.html), and [Implementing workload management in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-implementing-workload-management.html) in the
					*Amazon Redshift Database Developer Guide*.

Each result set from a direct query can have up to 2,000 columns. Each column name
				can have up to 127 Unicode characters. If you want to retrieve data from a larger
				table, you can use one of several methods to reduce the size of the data. You can
				deselect columns, or apply filters. In a SQL query, you can also use predicates,
				such as `WHERE`, `HAVING`. If your visuals time out during a
				direct query, you can simplify your query to optimize execution time or you can
				import the data into SPICE. 

Quotas for queries are as follows:

- 
					127 Unicode characters for each column name. 
- 
					2,000 columns for each dataset. 
- 
					2-minute quota for generating a visual, or an optional dataset sample. 
- 
					Data source timeout quotas apply (varies for each database engine).