# Creating a dataset using an existing dataset in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-dataset-existing-dataset.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-dataset-existing-dataset.html)

---

After you create a dataset in Amazon Quick, you can create additional datasets using it as a source. When you do this, any data preparation that the parent dataset contains, such as any joins or calculated fields, is kept. You can add additional preparation to the data in the new child datasets, such as joining new data and filtering data. You can also set up your own data refresh schedule for the child dataset and track the dashboards and analyses that use it.

Child datasets that are created using a dataset with RLS rules active as a source inherit the parent dataset's RLS rules. Users who are creating a child dataset from a larger parent dataset can only see the data that they have access to in the parent dataset. Then, you can add more RLS rules to the new child dataset in addition to the inherited RLS rules to further manage who can access the data that is in the new dataset. You can only create child datasets from datasets with RLS rules active in Direct Query.

Creating datasets from existing Quick datasets has the following advantages:

- 
				**Central management of datasets**– Data engineers can easily scale to the needs of multiple teams within their organization. To do this, they can develop and maintain a few general-purpose datasets that describe the organization's main data models.
- 
				**Reduction of data source management**– Business analysts (BAs) often spend lots of time and effort requesting access to databases, managing database credentials, finding the right tables, and managing Quick data refresh schedules. Building new datasets from existing datasets means that BAs don't have to start from scratch with raw data from databases. They can start with curated data.
- 
				**Predefined key metrics**– By creating datasets from existing datasets, data engineers can centrally define and maintain critical data definitions across their company's many organizations. Examples might be sales growth and net marginal return. With this feature, data engineers can also distribute changes to those definitions. This approach means that their business analysts can get started with visualizing the right data more quickly and reliably.
- 
				**Flexibility to customize data**– By creating datasets from existing datasets, business analysts get more flexibility to customize datasets for their own business needs. They can avoid worry about disrupting data for other teams.

For example, let's say that you're part of an ecommerce central team of five data engineers. You and your team has access to sales, orders, cancellations, and returns data in a database. You have created a Quick dataset by joining 18 other dimension tables through a schema. A key metric that your team has created is the calculated field, order product sales (OPS). Its definition is: OPS = product quantity x price.

Your team serves over 100 business analysts across 10 different teams in eight countries. These are the Coupons team, the Outbound Marketing team, the Mobile Platform team, and the Recommendations team. All of these teams use the OPS metric as a base to analyze their own business line.

Rather than manually creating and maintaining hundreds of unconnected datasets, your team reuses datasets to create multiple levels of datasets for teams across the organization. Doing this centralizes data management and allows each team to customize the data for their own needs. At the same time, this syncs updates to the data, such as updates to metric definitions, and maintains row-level and column-level security. For example, individual teams in your organization can use the centralized datasets. They can then combine them with the data specific to their team to create new datasets and build analyses on top of them.

Along with using the key OPS metric, other teams in your organization can reuse column
			metadata from the centralized datasets that you created. For example, the Data
			Engineering team can define metadata, such as *name*,
				*description*, *data type*, and
				*folders*, in a centralized dataset. All subsequent teams can use
			it.

###### Note

Amazon Quick supports creating up to two additional levels of datasets from a single dataset.

For example, from a parent dataset, you can create a child dataset and then a grandchild dataset for a total of three dataset levels.

## Creating a dataset from an existing dataset

			Use the following procedure to create a dataset from an existing dataset.

###### To create a dataset from an existing dataset

- 
					From the Quick start page, choose **Data**in the pane at left.
- 
					Choose **Create**then choose the dataset that you want to use to create a new dataset.
- 
					On the page that opens for that dataset, choose the drop-down menu for **Use in analysis**, and then choose**Use in dataset**.The data preparation page opens and preloads everything from the parent dataset, including calculated fields, joins, and security settings. 
- 
					On the data preparation page that opens, for **Query mode**at bottom left, choose how you want the dataset to pull in changes and updates from the original, parent dataset. You can choose the following options:- 
							**Direct query**– This is the default query mode. If you choose this option, the data for this dataset automatically refreshes when you open an associated dataset, analysis, or dashboard. However, the following limitations apply:- 
									If the parent dataset allows direct querying, you can use direct query mode in the child dataset. 
- 
									If you have multiple parent datasets in a join, you can choose direct query mode for your child dataset only if all the parents are from the same underlying data source. For example, the same Amazon Redshift connection. 
- 
									Direct query is supported for a single SPICE parent dataset. It is not supported for multiple SPICE parent datasets in a join. 
 
- 
									
- 
							**SPICE**– If you choose this option, you can set up a schedule for your new dataset to sync with the parent dataset. For more information about creating SPICE refresh schedules for datasets, see[Refreshing SPICE data](./refreshing-imported-data.html).
 
- 
							
- 
					(Optional) Prepare your data for analysis. For more information about preparing data, see [Preparing data in Amazon Quick Sight](./preparing-data.html).
- 
					(Optional) Set up row-level or column-level security (RLS/CLS) to restrict access to the dataset. For more information about setting up RLS, see [Using row-level security with user-based rules to restrict access to a dataset](./restrict-access-to-a-data-set-using-row-level-security.html). For more information about setting up CLS, see[Using column-level security to restrict access to a dataset](./restrict-access-to-a-data-set-using-column-level-security.html).###### NoteYou can set up RLS/CLS on child datasets only. RLS/CLS on parent datasets is not supported. 
- 
					When you're finished, choose **Save & publish**to save your changes and publish the new child dataset. Or choose**Publish & visualize**to publish the new child dataset and begin visualizing your data.