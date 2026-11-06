# percentileContOver - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/percentileContOver-function.html](https://docs.aws.amazon.com/quick/latest/userguide/percentileContOver-function.html)

---

The `percentileContOver` function calculates the percentile based on the
			actual numbers in `measure`. It uses the grouping and sorting that are
			applied in the field wells. The result is partitioned by the specified dimension at the
			specified calculation level. 

Use this function to answer the following question: Which actual data points are
			present in this percentile? To return the nearest percentile value that is present in
			your dataset, use `percentileDiscOver`. To return an exact percentile value
			that might not be present in your dataset, use `percentileContOver` instead. 

## Syntax

			`percentileContOver (``measure`,`percentile-n`, [`partition-by, …`] ,`calculation-level`)

## Arguments

			- 
						*measure*
- 
						Specifies a numeric value to use to compute the percentile. The argument must be a measure or metric. Nulls are ignored in the calculation. 
- 
						*percentile-n*
- 
						The percentile value can be any numeric constant 0–100. A percentile value of 50 computes the median value of the measure. 
- 
						*partition-by*
- 
						(Optional) One or more dimensions that you want to partition by, separated by commas. Each field in the list is enclosed in { } (curly braces), if it is more than one word. The entire list is enclosed in [ ] (square brackets). 
- 
						*calculation-level*
- 
						Specifies where to perform the calculation in relation to the order of evaluation. There are three supported calculation levels: - 
								PRE_FILTER 
- 
								PRE_AGG 
- 
								POST_AGG_FILTER (default) – To use this calculation level, specify an aggregation on `measure`, for example`sum(measure)`.
 PRE_FILTER and PRE_AGG are applied before the aggregation occurs in a visualization. For these two calculation levels, you can't specify an aggregation on `measure`in the calculated field expression. To learn more about calculation levels and when they apply, see[Order of evaluation in Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/order-of-evaluation-quicksight.html)and[Using level-aware calculations in Quick](https://docs.aws.amazon.com/quicksight/latest/user/level-aware-calculations.html).
- 
								

## Returns

			The result of the function is a number.

## Example of percentileContOver

			The following example helps explain how percentileContOver works.

###### Example Comparing calculation levels for the median

The following example shows the median for a dimension (category) by using
					different calculation levels with the `percentileContOver` function.
					The percentile is 50. The dataset is filtered by a region field. The code for
					each calculated field is as follows:

- 
						`example = left(`(A simplified example.)`category`, 1 )
- 
						`pre_agg = percentileContOver ( {Revenue} , 50 , [ example ] , PRE_AGG)`
- 
						`pre_filter = percentileContOver ( {Revenue} , 50 , [ example ] , PRE_FILTER)`
- 
						`post_agg_filter = percentileContOver ( sum ( {Revenue} ) , 50 , [ example ], POST_AGG_FILTER )`

`example pre_filter pre_agg post_agg_filter ------------------------------------------------------ 0 106,728 119,667 4,117,579 1 102,898 95,946 2,307,547 2 97,807 93,963 554,570 3 101,043 112,585 2,709,057 4 96,533 99,214 3,598,358 5 106,293 97,296 1,875,648 6 97,118 69,159 1,320,672 7 100,201 90,557 969,807`