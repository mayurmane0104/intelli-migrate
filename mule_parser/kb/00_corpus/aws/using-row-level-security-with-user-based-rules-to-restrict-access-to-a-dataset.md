# Using row-level security with user-based rules to restrict access to a dataset - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/restrict-access-to-a-data-set-using-row-level-security.html](https://docs.aws.amazon.com/quick/latest/userguide/restrict-access-to-a-data-set-using-row-level-security.html)

---

| Applies
                    to:Enterprise Edition | 

In the Enterprise edition of Amazon Quick, you can restrict access to a dataset by configuring row-level security (RLS) on it. You can do this before or after you have shared the dataset. When you share a dataset with RLS with dataset owners, they can still see all the data. When you share it with readers, however, they can only see the data restricted by the permission dataset rules. By adding row-level security, you can further control their access.

###### Note

When applying SPICE datasets to row-level security, each field in the dataset can
				contain up to 2,047 Unicode characters. Fields that contain more than this quota are
				truncated during ingestion. To learn more about SPICE data quotas, see [SPICE quotas for imported data](./data-source-limits.html#spice-limits).

To do this, you create a query or file with one column for user or group identification. You can use either
			`UserName` and `GroupName`, or alternatively `UserARN` and `GroupARN`. You
			can think of this as *adding a rule* for that user or
			group. Then you can add one column to the query or file for each field that you want to
			grant or restrict access to. For each user or group name that you add, you add the
			values for each field. You can use NULL (no value) to mean all values. To see examples
			of dataset rules, see [Creating dataset rules for row-level security](#create-data-set-rules-for-row-level-security).

To apply the dataset rules, you add the rules as a permissions dataset to your dataset. Keep in mind the following points:

- 
				The permissions dataset can't contain duplicate values. Duplicates are ignored when evaluating how to apply the rules. 
- 
				Each user or group specified can see only the rows that *match*the field values in the dataset rules.
- 
				If you add a rule for a user or group and leave all other columns with no value (NULL), you grant them access to all the data. 
- 
				If you don't add a rule for a user or group, that user or group can't see any of the data. 
- 
				The full set of rule records that are applied per user must not exceed 999. This limitation applies to the total number of rules that are directly assigned to a username, plus any rules that are assigned to the user through group names. 
- 
				If a field includes a comma (,) Amazon Quick treats each word separated from another by a comma as an individual value in the filter. For example, in `('AWS', 'INC')`,`AWS,INC`is considered as two strings:`AWS`and`INC`. To filter with`AWS,INC`, wrap the string with double quotation marks in the permissions dataset.If the restricted dataset is a SPICE dataset, the number of filter values applied per user can't exceed 192,000 for each restricted field. This applies to the total number of filter values that are directly assigned to a username, plus any filter values that are assigned to the user through group names. If the restricted dataset is a direct query dataset, the number of filter values applied per user varies from data sources. Exceeding the filter value limit may cause the visual rendering to fail. We recommend adding an additional column to your restricted dataset to divide the rows into groups based on the original restricted column so that the filter list can be shortened. 

Amazon Quick treats spaces as literal values. If you have a space in a field that you are restricting, the dataset rule applies to those rows. Amazon Quick treats both NULLs and blanks (empty strings "") as "no value". A NULL is an empty field value.

Depending on what data source your dataset is coming from, you can configure a direct query to access a table of permissions. Terms with spaces inside them don't need to be delimited with quotes. If you use a direct query, you can easily change the query in the original data source.

Or you can upload dataset rules from a text file or spreadsheet. If you are using a comma-separated value (CSV) file, don't include any spaces on the given line. Terms with spaces inside them need to be delimited with quotation marks. If you use dataset rules that are file-based, apply any changes by overwriting the existing rules in the dataset's permissions settings.

Datasets that are restricted are marked with the word **RESTRICTED**
			in the **Data** screen.

Child datasets that are created from a parent dataset that has RLS rules active retain the same RLS rules that the parent dataset has. You can add more RLS rules to the child dataset, but you can't remove the RLS rules that the dataset inherits from the parent dataset.

Child datasets that are created from a parent dataset that has RLS rules active can only be created with Direct Query. Child datasets that inherit the parent dataset's RLS rules aren't supported in SPICE.

Row-level security works only for fields containing textual data (string, char, varchar, and so on). It doesn't currently work for dates or numeric fields. Anomaly detection is not supported for datasets that use row-level security (RLS).

## Creating dataset rules for row-level security

			Use the following procedure to create a permissions file or query to use as dataset rules.

###### To create a permissions files or query to use as dataset rules

- 
					Create a file or a query that contains the dataset rules (permissions) for row-level security. It doesn't matter what order the fields are in. However, all the fields are case-sensitive. Make sure that they exactly match the field names and values. The structure should look similar to one of the following. Make sure that you have at least one field that identifies either users or groups. You can include both, but only one is required, and only one is used at a time. The field that you use for users or groups can have any name you choose. ###### NoteIf you are specifying groups, use only Amazon Quick groups or Microsoft AD groups. The following example shows a table with groups. GroupName Sales region Segment EMEA-Sales EMEA Enterprise, SMB, Startup US-Sales US Enterprise US-Sales US SMB, Startup US-Sales US Startup APAC-Sales APAC Enterprise, SMB Corporate-Reporting APAC-Sales APAC Enterprise, Startup The following example shows a table with usernames. UserName Sales region Segment AlejandroRosalez EMEA Enterprise, SMB, Startup MarthaRivera US Enterprise NikhilJayashankar US SMB, Startup PauloSantos US Startup SaanviSarkar APAC Enterprise, SMB sales-tps@example.com ZhangWei APAC Enterprise, Startup The following example shows a table with user and group Amazon Resource Names (ARNs). UserARN GroupARN Sales region `arn:aws:quicksight:us-east-1:123456789012:user/default/Bob``arn:aws:quicksight:us-east-1:123456789012:group/default/group-1`APAC `arn:aws:quicksight:us-east-1:123456789012:user/default/Sam``arn:aws:quicksight:us-east-1:123456789012:group/default/group-2`US Or if you use a .csv file, the structure should look similar to one of the following. `UserName,SalesRegion,Segment AlejandroRosalez,EMEA,"Enterprise,SMB,Startup" MarthaRivera,US,Enterprise NikhilJayashankars,US,SMB PauloSantos,US,Startup SaanviSarkar,APAC,"SMB,Startup" sales-tps@example.com,"","" ZhangWei,APAC-Sales,"Enterprise,Startup"``GroupName,SalesRegion,Segment EMEA-Sales,EMEA,"Enterprise,SMB,Startup" US-Sales,US,Enterprise US-Sales,US,SMB US-Sales,US,Startup APAC-Sales,APAC,"SMB,Startup" Corporate-Reporting,"","" APAC-Sales,APAC,"Enterprise,Startup"``UserARN,GroupARN,SalesRegion arn:aws:quicksight:us-east-1:123456789012:user/Bob,arn:aws:quicksight:us-east-1:123456789012:group/group-1,APAC arn:aws:quicksight:us-east-1:123456789012:user/Sam,arn:aws:quicksight:us-east-1:123456789012:group/group-2,US`Following is a SQL example. `/* for users*/ select User as UserName, SalesRegion, Segment from tps-permissions; /* for groups*/ select Group as GroupName, SalesRegion, Segment from tps-permissions;`
- 
					Create a dataset for the dataset rules. To make sure that you can easily find it, give it a meaningful name, for example `Permissions-Sales-Pipeline`.

## Rules Dataset flagging for row-level security

			Use the following procedure to appropriately flag a dataset as a rules dataset.

Rules Dataset is a flag that distinguishes permission datasets used for row-level
				security from regular datasets. If a permissions dataset was applied to a regular
				dataset before March 31, 2025, it will have a Rules Dataset flag in the
					**Dataset** landing page. 

If a permissions dataset was not applied to a regular dataset by March 31, 2025, it will be categorized as a regular dataset. To use it as a rules dataset, duplicate the permissions dataset and flag it as a rules dataset on the console when creating the dataset. Select EDIT DATASET and under the options, choose DUPLICATE AS RULES DATASET.

To successfully duplicate it as a rules dataset, ensure the original dataset has: 1. Required user metadata or group metadata column(s) and 2. Only string type columns.

To create a new rules dataset on the console, select NEW RULES DATASET under the
				NEW DATASET dropdown. When creating a rules dataset programmatically, add the
				following parameter: [UseAs: RLS_RULES](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSet.html#API_CreateDataSet_RequestSyntax). This is an optional parameter that is only used to
				create a rules dataset. Once a dataset has been created, either through the console
				or programmatically, and flagged as either a rules dataset or a regular dataset, it
				cannot be changed.

Once datasets are flagged as rules datasets, Amazon Quick will apply strict SPICE ingestion rules on them. To ensure data integrity, SPICE ingestions for rules datasets will fail if there are invalid rows or cells exceeding length limits. You must fix the ingestion issues in order to re-initiate a successful ingestion. Strict ingestion rules are only applicable to rules datasets. Regular datasets will not have dataset ingestion failures when there are skipped rows or string truncations.

## Applying row-level security

			Use the following procedure to apply row-level security (RLS) by using a file or query as a dataset that contains the rules for permissions.

###### To apply row-level security by using a file or query

- 
					Confirm that you have added your rules as a new dataset. If you added them, but don't see them under the list of datasets, refresh the screen. 
- 
					On the **Data**page, choose the dataset
- 
					On the dataset details page that opens, for **Row-level security**, choose**Set up**.
- 
					On the **Set up row-level security**page that opens, choose**User-based rules**.
- 
					From the list of datasets that appears, choose your permissions dataset. If your permissions dataset doesn't appear on this screen, return to your datasets, and refresh the page. 
- 
					For **Permissions policy**choose**Grant access to dataset**. Each dataset has only one active permissions dataset. If you try to add a second permissions dataset, it overwrites the existing one.###### ImportantSome restrictions apply to NULL and empty string values when working with row-level security: - 
								If your dataset has NULL values or empty strings ("") in the restricted fields, these rows are ignored when the restrictions are applied. 
- 
								Inside the permissions dataset, NULL values and empty strings are treated the same. For more information, see the following table. 
- 
								To prevent accidentally exposing sensitive information, Amazon Quick skips empty RLS rules that grant access to everyone. An *empty RLS rule*occurs when all columns of a row have no value. Quick RLS treats NULL, empty strings (""), or empty comma separated strings (for example ",,,") as no value.- 
										After skipping empty rules, other nonempty RLS rules still apply. 
- 
										If a permission dataset has only empty rules and all of them were skipped, no one will have access to any data restricted by this permission dataset. 
 
- 
										
 Rules for UserName, GroupName, SalesRegion, Segment Granted access AlejandroRosalez,EMEA-Sales,EMEA,"Enterprise,SMB,Startup" Sees all EMEA Enterprise, SMB, and Startup sales-tps@example.com,Corporate-Reporting,"","" Sees all rows User or group has no entry Sees no rows “”,“”,“”,“” Skipped; sees no rows if all other rules are empty. NULL,“”,“”,NULL Skipped; sees no rows if all other rules are empty. Anyone whom you shared your dashboard with can see all the data in it, unless the dataset is restricted by dataset rules. 
- 
								
- 
					Choose **Apply dataset**to save your changes. Then, on the**Save data set rules?**page, choose**Apply and activate**. Changes in permissions apply immediately to existing users.
- 
					(Optional) To remove permissions, first remove the dataset rules from the dataset. Make certain that the dataset rules are removed. Then, choose the permissions dataset and choose **Remove data set**.To overwrite permissions, choose a new permissions dataset and apply it. You can reuse the same dataset name. However, make sure to apply the new permissions in the **Permissions**screen to make these permissions active. SQL queries dynamically update, so these can be managed outside of Amazon Quick. For queries, the permissions are updated when the direct query cache is automatically refreshed.

If you delete a file-based permissions dataset before you remove it from the
				target dataset, restricted users can't access the dataset. While the dataset is in
				this state, it remains marked as **RESTRICTED**. However, when you
				view **Permissions** for that dataset, you can see that it has no
				selected dataset rules. 

To fix this, specify new dataset rules. Creating a dataset with the same name is
				not enough to fix this. You must choose the new permissions dataset on the
					**Permissions** screen. This restriction doesn't apply to
				direct SQL queries.