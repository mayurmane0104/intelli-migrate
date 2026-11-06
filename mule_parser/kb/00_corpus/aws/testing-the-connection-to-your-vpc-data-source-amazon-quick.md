# Testing the connection to your VPC data source - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/vpc-creating-a-quicksight-data-source-profile.html](https://docs.aws.amazon.com/quick/latest/userguide/vpc-creating-a-quicksight-data-source-profile.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick administrators and authors | 

To test whether you can connect to your data source through an existing Quick VPC connection, use the following procedure.

Before you begin, collect the information you need to connect. If you plan to copy and paste settings from a file, make sure that it doesn't contain any of the following: formatting (list bullets or numbers), blank space (spaces, tabs), or invisible "gremlin" (non-ASCII, null (ASCII 0), or control) characters.

- 
                On the Amazon Quick start page, choose **Manage data**.
- 
                On the **Datasets**page, choose**New data set**.
- 
                In the **FROM NEW DATA SOURCES**section of the**Create a data set**page, choose a supported data source that you want to connect to. For a list of data sources that support VPC, see[Identify the data sources to use](https://docs.aws.amazon.com/quicksight/latest/user/vpc-finding-setup-information.html#vpc-data-sources).Your data source instance must use the same VPC that you used to create the VPC connection. Also, the associated security group must be properly configured. For more information, see [Setting up a VPC to use with Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/vpc-setup-for-quicksight.html).
- 
                Enter the connection information for the data source. The fields for the data source are sometimes displayed in different order depending on which data source you choose. For more information, see [Creating a data source](https://docs.aws.amazon.com/quicksight/latest/user/create-a-data-source.html).- 
                        For **Data source name**, enter a descriptive name for the new data source. This name appears beside the data source logo on a tile on the**Create a data set**page. For testing purposes, name it`"VPC test-"`followed by the database name or location, whichever is unique.
- 
                        For **Connection Type**, choose the name of the VPC connection that has a route to your data source. If the correct VPC is missing from the list, ask a Amazon Quick administrator to verify that the VPC connection is correct in Amazon Quick. If it looks correct, ask a system administrator to verify that the data source and VPC are set up for this purpose.
- 
                        The name or other identifier for the server or instance to connect to. The descriptors vary depending on which one you're connecting to, but it's usually one or more of the following: hostname, IP address, cluster ID, instance ID, connector, or site based URL. 
- 
                        **Database name**shows the default database for the**Instance ID**cluster or instance. If you want to use a different database on that cluster or instance, enter its name.
- 
                        The name of the collection of data that you want to use. The descriptor varies depending on the provider, but it's usually one of the following: database, warehouse, or catalog. In this topic, we use the word "database" as a generic term. 
- 
                        For **Credentials**, enter a username and password to use for everyone who connects from Amazon Quick using this data source. The username must have permissions to do the following:- 
                                Access the target database. 
- 
                                Read (perform a `SELECT`statement on) all of the tables that you want to use in that database.
 
- 
                                
 
- 
                        
- 
                Choose **Validate connection**to verify your connection information is correct. If your connection doesn't validate, correct the connection information and try again. If the information looks correct but doesn't validate, do one or all of the following:- 
                        Contact your data source administrator to verify your connection settings. 
- 
                        Contact your Amazon Quick administrator to verify the settings in the Amazon Quick VPC connection. 
- 
                        Contact your AWS administrator to verify that the VPC is correctly configured for use with Amazon Quick. 
 
- 
                        
- 
                After the connection validates, choose **Create data source**to save the connection profile. Or, choose**Cancel**if you don't need to save it (recommended) after testing is complete.