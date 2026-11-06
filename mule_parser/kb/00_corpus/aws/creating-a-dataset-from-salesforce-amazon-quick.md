# Creating a dataset from Salesforce - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-salesforce.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-salesforce.html)

---

Use the following procedure to create a dataset by connecting to Salesforce and selecting a report or object to provide data.

###### To create a dataset using Salesforce from a report or object

- 
                Check [Data source quotas](./data-source-limits.html)to make sure that your target report or object doesn't exceed data source quotas.
- 
                On the Quick start page, choose **Data**.
- 
                On the **Data**page, choose**Create**then**New dataset**.
- 
                Choose the **Salesforce**icon.
- 
                Enter a name for the data source and then choose **Create data source**.
- 
                On the Salesforce login page, enter your Salesforce credentials. 
- 
                For **Data elements: contain your data**, choose**Select**and then choose either**REPORT**or**OBJECT**.###### NoteJoined reports aren't supported as Quick Sight data sources. 
- 
                Choose one of the following options: - 
                        To prepare the data before creating an analysis, choose **Edit/Preview data**to open data preparation. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
- 
                        Otherwise, choose a report or object and then choose **Select**.
 
- 
                        
- 
                Choose one of the following options: - 
                        To create a dataset and an analysis using the data as-is, choose **Visualize**.###### NoteIf you don't have enough [SPICE](./spice.html)capacity, choose**Edit/Preview data**. In data preparation, you can remove fields from the dataset to decrease its size or apply a filter that reduces the number of rows returned. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
- 
                        To prepare the data before creating an analysis, choose **Edit/Preview data**to open data preparation for the selected report or object. For more information about data preparation, see[Preparing dataset examples](./preparing-data-sets.html).
 
- 
                        

###### Note

The Salesforce connector is not supported in embedded console deployments where users authenticate through namespace isolation. The OAuth authentication flow requires direct Amazon Quick Sight console access to complete the sign-in process.