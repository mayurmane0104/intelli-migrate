# Mapping and joining fields - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/mapping-and-joining-fields.html](https://docs.aws.amazon.com/quick/latest/userguide/mapping-and-joining-fields.html)

---

When you are using different datasets together in Quick Sight, you can simplify the process of mapping fields or joining tables during the data preparation stage. You should already be verifying that your fields have the correct data type and an appropriate field name. However, if you already know which datasets are going to be used together, you can take a couple of extra steps to make your work easier later on.

## Mapping fields

			Quick Sight can automatically map fields between datasets in the same analysis. The following tips can help make it easier for Quick Sight to automatically map fields between datasets, for example if you are creating a filter action across datasets:

- 
					Matching field names – Field names must match exactly, with no differences in case, spacing, or punctuation. You can rename fields that describe the same data, so an automatic mapping is accurate. 
- 
					Matching data types – Fields must have the same data type for automatic mapping. You can change the data types while you are preparing the data. This step also gives you the opportunity to discover whether you need to filter out any data that isn't the correct data type. 
- 
					Using calculated fields – You can use calculated fields to create a matching field, and give it the correct name and data type for automatic mapping. 

###### Note

After an automatic mapping exists, you can rename a field without breaking the field mapping. However, if you change the data type, the mapping is broken.

For more information on field mapping for filter actions across datasets, see
					[Creating and editing custom actions in Amazon Quick Sight](./custom-actions.html).

## Joining fields

			You can create joins between data from different data sources, including files or databases. The following tips can help make it easier for you to join data from different files or data sources:

- 
					Similar field names – It is simpler to join fields when you can see what should match; for example, **Order ID**and**order-id**seem as if they should be the same. But if one is a work order, and the other is a purchase order, then the fields are probably different data. If possible, make sure that the files and tables that you want to join have field names making it clear what data they contain.
- 
					Matching data types – Fields must have the same data type before you can join on them. Make sure that the files and tables that you want to join having matching data types in join fields. You can't use a calculated field for a join. Also, you can't join two existing datasets. You create the joined dataset by directly accessing the source data. 

For more information on joining data across data sources, see [Joining data](./joining-data.html).