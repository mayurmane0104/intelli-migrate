# Creating datasets using new data sources - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/creating-data-sets-new.html](https://docs.aws.amazon.com/quick/latest/userguide/creating-data-sets-new.html)

---

When you create a dataset based on an AWS service like Amazon RDS, Amazon Redshift, or Amazon EC2, data transfer charges might apply when consuming data from that source. Those charges might also vary depending on whether that AWS resource is in the home AWS Region that you chose for your Amazon Quick account. For details on pricing, see the pricing page for the service in question.

When creating a new database dataset, you can select one table, join several tables,
			or create a SQL query to retrieve the data that you want. You can also change whether
			the dataset uses a direct query or instead stores data in [SPICE](./spice.html).

###### To create a new dataset

- 
				To create a dataset, choose **New data set**on the**Data**page. You can then create a dataset based on an existing dataset or data source, or connect to a new data source and base the dataset on that.
- 
				Provide connection information to the data source: - 
						For local text or Microsoft Excel files, you can simply identify the file location and upload the file. 
- 
						For Amazon S3, provide a manifest identifying the files or buckets that you want to use, and also the import settings for the target files. 
- 
						For Amazon Athena, all Athena databases for your AWS account are returned. No additional credentials are required. 
- 
						For Salesforce, provide credentials to connect with. 
- 
						For Amazon Redshift, Amazon RDS, Amazon EC2, or other database data sources, provide information about the server and database that host the data. Also provide valid credentials for that database instance. 
 
-