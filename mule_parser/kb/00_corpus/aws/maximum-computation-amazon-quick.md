# Maximum computation - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/maximum-function.html](https://docs.aws.amazon.com/quick/latest/userguide/maximum-function.html)

---

The maximum computation finds the maximum dimension by value. For example, you can create a computation to find the month with the highest revenue.

To use this function, you need at least one dimension in the
						**Time** field well. 

## Parameters

					- *name*
- 
								A unique descriptive name that you assign or change. A name is assigned if you don't create your own. You can edit this later. 
- *Date*
- 
								The date dimension that you want to rank. 
- *Value*
- 
								The aggregated measure that the computation is based on. 

## Computation outputs

					Each function generates a set of output parameters. You can add these outputs to the autonarrative to customize what it displays. You can also add your own custom text.

To locate the output parameters, open the
							**Computations** tab on the right, and locate the
						computation that you want to use. The names of the computations come from
						the name you provide when you create the insight. Choose the output
						parameter by clicking on it only once. If you click twice, you add the same
						output twice. Items displayed in **bold** can
						be used in the narrative. 

###### Note

These are the same output parameters as the ones that are returned by the minimum computation.

- 
							`timeField`– From the**Time**field well.- 
									**name**
- 
									**timeGranularity****DAY**,**YEAR**, and so on).
 
- 
									
- 
							`metricField`– From the**Values**field well.- 
									**name**
- 
									**aggregationFunction****SUM**,**AVG**, and so on).
 
- 
									
- 
							`metricValue`– The value in the metric dimension.- 
									**value**
- 
									**formattedValue**
- 
									**formattedAbsoluteValue**
 
- 
									
- 
							`timeValue`– The value in the datetime dimension.- 
									**value**
- 
									**formattedValue**
 
-