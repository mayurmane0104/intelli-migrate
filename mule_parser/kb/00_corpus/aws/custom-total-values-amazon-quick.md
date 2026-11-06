# Custom total values - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/tables-pivot-tables-custom-totals.html](https://docs.aws.amazon.com/quick/latest/userguide/tables-pivot-tables-custom-totals.html)

---

Quick authors can define the total and subtotal aggregations for their table or pivot table visuals from the field wells. For tables,the custom total menu is only available if totals are toggled on for the visual.

###### To change the aggregation of a total or subtotal

- 
					Navigate to the analysis that you want to change, and choose the table or pivot table visual whose total you want to define. 
- 
					Choose the field that you want to change from the field wells. 
- 
					Choose **Total**, and then choose the aggregation that you want. The following options are available.- 
							**Default**– The total calculation uses the same aggregation as the metric field.
- 
							**Sum**– Calculates the sum of the data in the visual.
- 
							**Average**– Calculates the average of the data in the visual.
- 
							**Min**– Calculates the minimum value of the data in the visual.
- 
							**Max**– Calculates the maximum value of the data in the visual.
- 
							**None (HIDE)**– Totals are not calculated. When you choose this option, the total and subtotal cells in the visual are left blank. If the outer dimension is sorted with the metric field that calculates the total or subtotal, the dimension is sorted alphabetically. When you change the value from**None (HIDE)**to another value, the outer dimension is sorted by the subtotals that are calculated with the specified aggregation type.
 
- 
							

The following limitations apply to custom totals.

- 
					Conditional formatting is not supported for custom totals. 
- 
					Total aggregations aren't supported for string columns. Total aggregations include **Min**,**Max**,**Sum**, and**Average**.
- 
					Date columns are incompatible with **Average**and**Sum**total aggregation functions.