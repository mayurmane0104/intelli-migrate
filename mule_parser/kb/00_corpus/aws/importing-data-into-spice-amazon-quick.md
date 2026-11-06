# Importing data into SPICE - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/spice.html](https://docs.aws.amazon.com/quick/latest/userguide/spice.html)

---

When you import data into a dataset rather than using a direct SQL query, it becomes
				*SPICE data* because of how it's
			stored. *SPICE (Super-fast, Parallel, In-memory
					Calculation Engine)* is the robust in-memory engine that
			Amazon Quick Sight uses. It's engineered to rapidly perform advanced calculations and serve data.
			In Enterprise edition, data stored in SPICE is encrypted at rest.

When you create or edit a dataset, you choose to use either SPICE or a
			direct query, unless the dataset contains uploaded files. Importing (also called
				*ingesting*) your data into SPICE can save time
			and money:

- 
				Your analytical queries process faster. 
- 
				You don't need to wait for a direct query to process. 
- 
				Data stored in SPICE can be reused multiple times without incurring additional costs. If you use a data source that charges per query, you're charged for querying the data when you first create the dataset and later when you refresh the dataset. 

SPICE capacity is allocated separately for each AWS Region. Default
				SPICE capacity is automatically allocated to your home AWS Region.
			For each AWS account, SPICE capacity is shared by all the people using
			Quick Sight in a single AWS Region. The other AWS Regions have no
				SPICE capacity unless you choose to purchase some. Quick Sight
			administrators can view how much SPICE
			capacity you have in each AWS Region and how much of it is currently in use. A
			Quick Sight administrator can purchase more SPICE capacity or release
			unused SPICE capacity as needed. For more information, see [Configure SPICE memory capacity](./managing-spice-capacity.html).

## Estimating the size of SPICE datasets

			The size of a dataset in SPICE relative to your Quick
				account's SPICE capacity is called *logical
					size*. A dataset's logical size isn't the same as the size
				of the dataset's source file or table. The computation of a dataset's
				logical size occurs after all the data type transformations and calculated columns
				are defined during data preparation. These fields are materialized in
					SPICE in a way that enhances query performance. Any changes you
				make in an analysis have no effect on the logical size of the data in
					SPICE. Only changes that are saved in the dataset apply to
					SPICE capacity.

The logical size of a SPICE dataset depends on the data types of the dataset fields and the number of rows in the dataset. The three types of SPICE data are decimals, dates, and strings. You can transform a field's data type during the data preparation phase to fit your data visualization needs. For example, the file you want to import might contain all strings (text). But for these to be used in a meaningful way in an analysis, you prepare the data by changing the data types to their proper form. Fields containing prices can be changed from strings to decimals, and fields containing dates can be changed from strings to dates. You can also create calculated fields and exclude fields that you don't need from the source table. When you are finished preparing your dataset and all transformations are complete, you can estimate the logical size of the final schema.

###### Note

Geospatial data types use metadata to interpret the physical data type. Latitude and longitude are numeric. All other geospatial categories are strings.

In the formula below, decimals and dates are calculated as 8 bytes per cell with 4 extra bytes for auxillary. Strings are calculated based on the text's length in UTF-8 encoding plus 24 bytes for auxillary. String data types require more space because of the extra indexing required by SPICE to provide high query performance.

`Logical dataset size in bytes = (Number of Numeric cells * (12 bytes per cell)) + (Number of Date cells * (12 bytes per cell)) + SUM ((24 bytes + UTF-8 encoded length) per Text cell)`

The formula above should only be used to estimate the size of a single dataset in SPICE. The SPICE capacity usage is the total size of all datasets in an account in a specific region. Quick Sight does not recommend that you use this formula to estimate the total SPICE capacity that your Quick Sight account is using.