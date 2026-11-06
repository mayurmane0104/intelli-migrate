# I can't create or refresh a dataset from an existing Adobe Analytics data source - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-connect-adobe-analytics.html](https://docs.aws.amazon.com/quick/latest/userguide/troubleshoot-connect-adobe-analytics.html)

---

As of May 1, 2022, Quick Sight no longer supports legacy OAuth and version 1.3 and SOAP API operations in Adobe Analytics. If you experience failures while trying to create or refresh a dataset from an existing Adobe Analytics data source, you might have a stale access token.

###### To troubleshoot failures while creating or refreshing a dataset from an existing Adobe Analytics data source

- 
					Open Quick Sight and choose **Data**at left.
- 
					Choose **New**then**Dataset**.
- 
					On the **Create a dataset**page, choose the Adobe Analytics data source that you want to update from the list of existing data sources.
- 
					Choose **Edit data source**.
- 
					On the **Edit Adobe Analytics data source**page that opens, choose**Update data source**to reauthorize the Adobe Analytics connection.
- 
					Try recreating or refreshing the dataset again. The dataset creation or refresh should succeed.