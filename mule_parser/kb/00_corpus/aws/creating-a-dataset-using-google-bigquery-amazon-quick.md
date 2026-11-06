# Creating a dataset using Google BigQuery - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quicksight-google-big-query.html](https://docs.aws.amazon.com/quick/latest/userguide/quicksight-google-big-query.html)

---

###### Note

When Quick Sight uses and transfers information that is received from
                    Google APIs, it adheres to the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy).

Google BigQuery is a fully managed serverless data warehouse that customers use to manage and analyze their data. Google BigQuery customers use SQL to query their data without any infrastructure management.

## Creating a data source connection with Google BigQuery

            **Prerequisites**

Before you start, make sure that you have the following. These are all required to create a data source connection with Google BigQuery:

- 
                    **Project ID**– The project ID that is associated with your Google account. To find this, navigate to the Google Cloud console and choose the name of the project that you want to connect to Quick Sight. Copy the project ID that appears in the new window and record it for later use.
- 
                    **Dataset Region**– The Google region that the Google BigQuery project exists in. To find the dataset region, navigate to the Google BigQuery console and choose**Explorer**. Locate and expand the project that you want to connect to, then choose the dataset that you want to use. The dataset region appears in the pop-up that opens.
- 
                    **Google account login credentials**– The login credentials for your Google account. If you don't have this information, contact your Google account administrator.
- 
                    **Google BigQuery Permissions**– To connect your Google account with Quick Sight, make sure that your Google account has the following permissions:- 
                            `BigQuery Job User`at the`Project`level.
- 
                            `BigQuery Data Viewer`at the`Dataset`or`Table`level.
- 
                            `BigQuery Metadata Viewer`at the`Project`level.
 
- 
                            

For information about how to retrieve the previous prerequisite information, see
                    [Unlock the power of unified business intelligence with Google Cloud
                        BigQuery and Quick Sight](https://aws.amazon.com/blogs/business-intelligence/unlock-the-power-of-unified-business-intelligence-with-google-cloud-bigquery-and-amazon-quicksight/).

Use the following procedure to connect your Quick account with your Google BigQuery data source.

###### To create a new connection to a Google BigQuery data source from Quick Sight

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    From the left navigation pane, choose **Data**.
- 
                    Choose **Create**then choose**New Dataset**
- 
                    Choose the **Google BigQuery**tile.
- 
                    Add the data source details that you recorded in the prerequisites section earlier: - 
                            **Data source name**– A name for the data source.
- 
                            **Project ID**– A Google Platform project ID. This field is case sensitive.
- 
                            **Dataset Region**– The Google cloud platform dataset region of the project that you want to connect to.
 
- 
                            
- 
                    Choose **Sign in**.
- 
                    In the new window that opens, enter the login credentials for the Google account that you want to connect to. 
- 
                    Choose **Continue**to grant Quick Sight access to Google BigQuery.
- 
                    After you create the new data source connection, continue to [Step 4](#gbq-step-4)in the following procedure.

## Adding a new Quick Sight dataset for Google BigQuery

            After you create a data source connection with Google BigQuery, you can create Google BigQuery datasets for analysis. Datasets that use Google BigQuery can only be stored in SPICE.

###### To create a dataset using Google BigQuery

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    From the start page, choose **Data**.
- 
                    Choose **Create**, then**New Dataset**
- 
                    Choose the **Google BigQuery**tile, and then choose**Create dataset**.
- 
                    
                    For **Tables**, do one of the following:- 
                            Choose the table that you want to use. 
- 
                            Choose **Use custom SQL**to use your own personal SQL statement. For more information about using custom SQL in Quick Sight, see[Using SQL to customize data](./adding-a-SQL-query.html).
 
- 
                            
- 
                    Choose **Edit/Preview**.
- 
                    (Optional) In the **Data prep**page that opens, you can add customizations to your data with calculated fields, filters, and joins.
- 
                    When you are finished making changes, choose **Save**to save and close the dataset.