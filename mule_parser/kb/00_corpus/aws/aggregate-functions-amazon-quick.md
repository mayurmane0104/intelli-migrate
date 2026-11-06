# Aggregate functions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/calculated-field-aggregations.html](https://docs.aws.amazon.com/quick/latest/userguide/calculated-field-aggregations.html)

---

Aggregate functions are only available during analysis and visualization. Each of these functions returns values grouped by the chosen dimension or dimensions. For each aggregation, there is also a conditional aggregation. These perform the same type of aggregation, based on a condition.

When a calculated field formula contains an aggregation, it becomes a custom aggregation. To make sure that your data is accurately displayed, Amazon Quick applies the following rules:

- 
			Custom aggregations can't contain nested aggregate functions. For example, this formula doesn't work: `sum(avg(x)/avg(y))`. However, nesting nonaggregated functions inside or outside aggregate functions does work. For example,`ceil(avg(x))`works. So does`avg(ceil(x))`.
- 
			Custom aggregations can't contain both aggregated and nonaggregated fields, in any combination. For example, this formula doesn't work: `Sum(sales)+quantity`.
- 
			Filter groups can't contain both aggregated and nonaggregated fields. 
- 
			Custom aggregations can't be converted to a dimension. They also can't be dropped into the field well as a dimension. 
- 
			In a pivot table, custom aggregations can't be added to table calculations. 
- 
			Scatter plots with custom aggregations need at least one dimension under **Group/Color**in the field wells.

For more information about supported functions and operators, see [Calculated field function and operator reference for Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/calculated-field-reference.html). 

The aggregate functions for calculated fields in Quick include the following.