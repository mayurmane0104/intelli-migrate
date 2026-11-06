# Using level-aware calculations in Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/level-aware-calculations.html](https://docs.aws.amazon.com/quick/latest/userguide/level-aware-calculations.html)

---

| Applies
                    to:Enterprise Edition and Standard Edition | 

With *Level-aware calculations* (LAC) you can specify the level of
			granularity that you want to compute window functions or aggregate functions. There are
			two types of LAC functions: level-aware calculation - aggregate (LAC-A) functions, and
			level-aware calculation - window (LAC-W) functions.

## Level-aware calculation - aggregate (LAC-A) functions

			With LAC-A functions, you can specify at what level to group the computation. By
				adding one argument into an existing aggregate function, such as ```
sum() , max()
					, count()
```
, you can define any group-by level that you want for the
				aggregation. The level added can be any dimension independent of the dimensions
				added to the visual. For example:

`sum(measure,[group_field_A])`To use LAC-A functions, type them directly in the calculation editor by adding the intended aggregation levels as the second argument between brackets. Following is an example of an aggregate function and a LAC-A function, for comparison.

- 
					Aggregate function: `sum({sales})`
- 
					LAC-A function: `sum({sales}, [{Country},{Product}])`

The LAC-A results are computed with the specified level in the brackets ```
[
					]
```
, can be used as operand of an aggregate function. The group-by level of
				the aggregate function is visual level, with **Group by** fields
				added to the field well of the visual. 

In addition to creating a static LAC group key in the bracket `[ ]`,
				you can make it dynamically adapted to visual group-by fields, by putting a
				parameter `$visualDimensions` in the bracket. This is a system-provided
				parameter, in contrast to user-defined parameter. The
					`[$visualDimensions]`parameter represents the fields added to the
					**Group by** field well in current visual. The following
				examples show how to dynamically add group keys to the visual dimensions or remove
				group keys from visual dimensions

- 
					LAC-A with dynamic-added group key : `sum({sales}, [${visualDimensions},{Country},{Products}])`It calculates, before the visual level aggregation is calculated, the sum of sales, grouping by `country`,`products`, and any other fields in the**Group by**field well .
- 
					LAC-A with dynamic-removed group key : `sum({sales}, [${visualDimensions},!{Country},!{Products}])`It calculates, before visual level aggregation is calculated, the sum of sales, grouping by the fields in the visual's **Group by**field well, except`country`and`product`.

You can specify added group key or removed group key in on LAC expression, but not both.

LAC-A functions are supported for the following aggregate functions:

### LAC-A examples

You can do the following with LAC-A functions:

- 
						Run calculations that are independent of the levels in the visual. For example, if you have the following calculation, the sales numbers are aggregated only at the country level, but not across other dimensions (Region or Product) in the visual. `sum({Sales},[{Country}])`
- 
						Run calculations for the dimensions that are not in the visual. For example, if you have the following function, you can calculate the average total country sales by region. `sum({Sales},[{Country}])`Though Country is not included in the visual, the LAC-A function first aggregates the sales at the Country level and then the visual level calculation generates the average number for each region. If the LAC-A function isn't used to specify the level, the average sales are calculated at the lowest granular level (the base level of the dataset) for each region (showing in the sales column). 
- 
						Use LAC-A combined with other aggregate functions and LAC-W functions. There are two ways you can nest LAC-A functions with other functions. - 
								You can write a nested syntax when you create a calculation. For example, the LAC-A function can be nested with a LAC-W function to calculate the total sales by country of each product's average price: `sum(avgOver({Sales},[{Product}],PRE_AGG),[{Country}])`
- 
								When adding a LAC-A function into a visual, the calculation can be further nested with visual-level aggregate functions that you selected in the fields well. For more information about changing the aggregation of fields in the visual, see [Changing or adding aggregation to a field by using a field well](./changing-field-aggregation.html#change-field-aggregation-field-wells).
 
- 
								

### LAC-A limitations

The following limitations apply to LAC-A functions:

- 
						LAC-A functions are supported for all additive and non-additive aggregate functions, such as `sum()`,`count()`, and`percentile()`. LAC-A functions are not supported for conditional aggregate functions that end with "if", such as`sumif()`and`countif()`, nor for period aggregate functions that start with "periodToDate", such as`periodToDateSum()`and`periodToDateMax()`.
- 
						Row-level and column-level totals are not currently supported for for LAC-A functions in tables and pivot tables. When you add row-level or column-level totals to the chart, the total number will show as blank. Other non-LAC dimensions are not impacted. 
- 
						Nested LAC-A functions are not currently supported. A limited capability of LAC-A functions nested with regular aggregate functions and LAC-W functions are supported. For example, the following functions are valid: - 
								`Aggregation(LAC-A())`. For example:`max(sum({sales}, [{country}]))`
- 
								`LAC-A(LAC-W())`. For example:`sum(sumOver({Sales},[{Product}],PRE_AGG), [{Country}])`
 The following functions are not valid: - 
								`LAC-A(Aggregation())`. For example:`sum(max({sales}), [{country}])`
- 
								`LAC-A(LAC-A())`. For example:`sum(max({sales}, [{country}]),[category])`
- 
								`LAC-W(LAC-A())`. For example:`sumOver(sum({Sales},[{Product}]),[{Country}],PRE_AGG)`
 
- 
								

## Level-aware calculation - window (LAC-W) functions

			With LAC-W functions, you can specify the window or partition to compute the
				calculation. LAC-W functions are a group of window functions, such as
					`sumover()`, `(maxover)`, `denseRank`, that you
				can run at the prefilter or preaggregate level. For example:
					`sumOver(measure,[partition_field_A],pre_agg)`.

LAC-W functions used to be called level aware aggregations (LAA).

LAC-W functions help you to answer the following types of questions:

- 
					How many of my customers made only 1 purchase order? Or 10? Or 50? We want the visual to use the count as a dimension rather than a metric in the visual. 
- 
					What are the total sales per market segment for customers whose lifetime spend is greater than $100,000? The visual should only show the market segment and the total sales for each. 
- 
					How much is the contribution of each industry to the entire company's profit (percent of total)? We want to be able to filter the visual to show some of the industries, and how they contribute to the total sales for the displayed industries. However, we also want to see each industry's percent of total sales for the entire company (including industries that are filtered out). 
- 
					What are the total sales in each category as compared to the industry average? The industry average should include all of the categories, even after filtering. 
- 
					How are my customers grouped into cumulative spending ranges? We want to use the grouping as a dimension rather than a metric. 

For more complex questions, you can inject a calculation or filter before
				Quick Sight gets to a specific point in its evaluation of your settings. To
				directly influence your results, you add a calculation level keyword to a table
				calculation. For more information on how Quick Sight evaluates queries, see [Order of evaluation in Amazon Quick Sight](./order-of-evaluation-quicksight.html).

The following calculation levels are supported for LAC-W functions:

- 
					`PRE_FILTER`– Before applying filters from the analysis, Quick Sight evaluates prefilter calculations. Then it applies any filters that are configured on these prefilter calculations.
- 
					`PRE_AGG`– Before computing display-level aggregations, Quick Sight performs preaggregate calculations. Then it applies any filters that are configured on these preaggregate calculations. This work happens before applying top and bottom*N*filters.

You can use the `PRE_FILTER` or `PRE_AGG` keyword as a
				parameter in the following table calculation functions. When you specify a
				calculation level, you use an unaggregated measure in the function. For example, you
				can use `countOver({ORDER ID}, [{Customer ID}], PRE_AGG)`. By using
					`PRE_AGG`, you specify that the `countOver` executes at
				the preaggregate level. 

By default, the first parameter for each function must be an aggregated measure.
				If you use either `PRE_FILTER` or `PRE_AGG`, you use a
				nonaggregated measure for the first parameter. 

For LAC-W functions, the visual aggregation defaults to `MIN` to
				eliminate duplicates. To change the aggregation, open the field's context
				(right-click) menu, and then choose a different aggregation.

For examples of when and how to use LAC-W functions in real life scenarios, see
				the following post in the AWS Big Data Blog: [Create advanced insights using Level Aware Aggregations in Amazon
					QuickSight.](https://aws.amazon.com/jp/blogs/big-data/create-advanced-insights-using-level-aware-aggregations-in-amazon-quicksight/)