# Adding numeric filters - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/add-a-numeric-filter-data-prep.html](https://docs.aws.amazon.com/quick/latest/userguide/add-a-numeric-filter-data-prep.html)

---

Fields with decimal or int data types are considered numeric fields. You create
			filters on numeric fields by specifying a comparison type, for example **Greater
				than** or **Between**, and a comparison value or values as
			appropriate to the comparison type. Comparison values must be positive integers and
			can't contain commas.

You can use the following comparison types in numeric filters:

- 
				Equals 
- 
				Does not equal 
- 
				Greater than 
- 
				Greater than or equal to 
- 
				Less than 
- 
				Less than or equal to 
- 
				Between 

###### Note

To use a top and bottom filter for numeric data (analyses only), first change the
				field from a measure to a dimension. Doing this converts the data to text. Then you
				can use a text filter. For more information, see [Adding text filters](./add-a-text-filter-data-prep.html).

In analyses, for datasets based on database queries, you can also optionally apply an
			aggregate function to the comparison value or values, for example
				**Sum** or **Average**. 

You can use the following aggregate functions in numeric filters:

- 
				Average 
- 
				Count 
- 
				Count distinct 
- 
				Max 
- 
				Median 
- 
				Min 
- 
				Percentile 
- 
				Standard deviation 
- 
				Standard deviation - population 
- 
				Sum 
- 
				Variance 
- 
				Variance - population 

## Creating numeric filters

			Use the following procedure to create a numeric field filter.

###### To create a numeric field filter

- 
					Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
					In the **Filters**pane, choose the new filter to expand it.
- 
					(Optional) For **Aggregation**, choose an aggregation. No aggregation is applied by default. This option is available only when creating numeric filters in an analysis.
- 
					For **Filter condition**, choose a comparison type.
- 
					Do one of the following: - 
							If you chose a comparison type other than **Between**, enter a comparison value.If you chose a comparison type of **Between**, enter the beginning of the value range in**Minimum value**and the end of the value range in**Maximum value**.
- 
							(Analyses only) To use an existing parameter, enable **Use parameters**, then choose your parameter from the list.For parameters to appear in this list, create your parameters first. Usually, you create a parameter, add a control for it, and then add a filter for it. For more information, see [Parameters in Amazon Quick](./parameters-in-quicksight.html). The values display alphabetically in the control, unless there are more than 1,000 distinct values. Then the control displays a search box instead. Each time you search for the value that you want to use, it initiates a new query. If the results contain more than 1,000 values, you can scroll through the values with pagination.
 
- 
							
- 
					(Analyses only) For **Null options**choose**Exclude nulls**,**Include nulls**, or**Nulls only**.
- 
					When finished, choose **Apply**.