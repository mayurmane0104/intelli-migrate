# Creating a data source - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-source.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-source.html)

---

| Intended audience: Amazon Quick authors | 

As an analysis author in Amazon Quick, you don't need to understand anything about the infrastructure that you use to connect to your data. You set up a new data source only once.

After a data source is set up, you can access it from its tile in the Quick console. You can use it to create one or more datasets. After a dataset is set up, you can also access the dataset from its tile. By abstracting away the technical details, Amazon Quick Sight simplifies data connections.

###### Note

You don't need to store connection settings for files that you plan to upload
					manually. For more information about file uploads, see [Creating datasets](./creating-data-sets.html).

Before you begin adding a new data-source connection profile to Amazon Quick, first collect the information that you need to connect to the data source. In some cases, you might plan to copy and paste settings from a file. If so, make sure that the file doesn't contain formatting characters (list bullets or numbers) or blank space characters (spaces, tabs). Also make sure that the file doesn't contain nontext "gremlin" characters such as non-ASCII, null (ASCII 0), and control characters.

The following list includes the information to collect the most commonly used settings:

- 
					The data source to connect to. Make sure that you know which source that you need to connect to for reporting. This source might be different than the source that stores, processes, or provides access to the data. For example, let's say that you're a new analyst in a large company. You want to analyze data from your ordering system, which you know uses Oracle. However, you can't directly query the online transaction processing (OLTP) data. A subset of data is extracted and stored in a bucket on Amazon S3, but you don't have access to that either. Your new co-workers explain that they use AWS Glue crawlers to read the files and AWS Lake Formation to access them. With more research, you learn that you need to use an Amazon Athena query as your data source in Amazon Quick Sight. The point here is that it isn't always obvious which type of data source to choose. 
- 
					A descriptive name for the new data source tile. Each new data source connection needs a unique and descriptive name. This name displays on the Amazon Quick Sight list of existing data sources, which is at the bottom of the **Create a Data Set**screen. Use a name that makes it easy to distinguish your data sources from other similar data sources. Your new Amazon Quick Sight data source profile displays both the database software logo and the custom name that you assign.
- 
					The name of the server or instance to connect to. A unique name or other identifier identifies the server connector of the data source on your network. The descriptors vary depending on which one you're connecting to, but it's usually one or more of the following: - 
							Hostname 
- 
							IP address 
- 
							Cluster ID 
- 
							Instance ID 
- 
							Connector 
- 
							Site-based URL 
 
- 
							
- 
					The name of the collection of data that you want to use. The descriptor varies depending on the data source, but it's usually one of the following: - 
							Database 
- 
							Warehouse 
- 
							S3 bucket 
- 
							Catalog 
- 
							Schema 
 In some cases, you might need to include a manifest file or a query. 
- 
							
- 
					The user name that you want Amazon Quick Sight to use. Every time Amazon Quick Sight connects using this data source profile (tile), it uses the user name from the connection settings. In some cases, this might be your personal login. But if you're going to share this with other people, ask the system administrator about creating credentials to use for Amazon Quick Sight connections. 
- 
					What type of connection to use. You can choose a public network or a VPC connection. If you have more than one VPC connection available, identify which one to use to reach your source of data. 
- 
					Additional settings, such as Secure Sockets Layer (SSL) or API tokens, are required by some data sources. 

After you save the connection settings as a data source profile, you can create a dataset by selecting its tile. The connections are stored as data source connection profiles in Amazon Quick Sight.

To view your existing connection profiles, open the Quick start page,
				choose **Data**, choose **Create**, and then
				choose **New Dataset**.

For a list of supported data source connections and examples, see [Connect to your data with integrations and datasets](./connecting-to-data-examples.html).

After you create a data source in Quick Sight, you can [create a
					dataset](https://docs.aws.amazon.com/quicksuite/latest/userguide/creating-data-sets) in Quick Sight that contains data from the connected data
				source. You can also [update data source
					connection](https://docs.aws.amazon.com/quicksuite/latest/userguide/edit-a-data-source) information at any time.