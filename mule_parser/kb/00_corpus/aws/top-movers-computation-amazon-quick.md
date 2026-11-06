# Top movers computation - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/top-movers-function.html](https://docs.aws.amazon.com/quick/latest/userguide/top-movers-function.html)

---

The top movers computation counts the requested number of categories by date that rank in the top of the autonarrative's dataset. For example, you can create a computation to find the top products by sales revenue for a time period.

To use this function, you need at least one dimension in the
						**Time** field well and at least one dimension in the
						**Categories** field well. 

## Parameters

					- *name*
- 
								A unique descriptive name that you assign or change. A name is assigned if you don't create your own. You can edit this later. 
- *Category*
- 
								The category dimension you want to rank. 
- *Value*
- 
								The aggregated measure that the computation is based on. 
- *Number of results*
- 
								The number of top ranking items you want to find. 

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

These are the same output parameters as the ones that are returned by the bottom movers computation.

- 
							`timeField`– From the**Time**field well.- 
									**name**
- 
									**timeGranularity****DAY**,**YEAR**, and so on).
 
- 
									
- 
							`categoryField`– From the**Categories**field well.- 
									**name**
 
- 
									
- 
							`metricField`– From the**Values**field well.- 
									**name**
- 
									**aggregationFunction****SUM**,**AVG**, and so on).
 
- 
									
- 
							`startTimeValue`– The value in the date dimension.- 
									**value**
- 
									**formattedValue**
 
- 
									
- 
							`endTimeValue`– The value in the date dimension.- 
									**value**
- 
									**formattedValue**
 
- 
									
- 
							**itemsCount**
- 
							**items**- 
									`categoryField`– The category field.- 
											**value**
- 
											**formattedValue**`NULL`'. If the field is empty, it displays '`(empty)`'.
 
- 
											
- 
									`currentMetricValue`– The current value for the metric field.- 
											**value**
- 
											**formattedValue**
- 
											**formattedAbsoluteValue**
 
- 
											
- 
									`previousMetricValue`– The previous value for the metric field.- 
											**value**
- 
											**formattedValue**
- 
											**formattedAbsoluteValue**
 
- 
											
- 
									`percentDifference`– The percent difference between the current and previous values of the metric field.- 
											**value**
- 
											**formattedValue**
- 
											**formattedAbsoluteValue**
 
- 
											
- 
									`absoluteDifference`– The absolute difference between the current and previous values of the metric field.- 
											**value**
- 
											**formattedValue**
- 
											**formattedAbsoluteValue**
 
- 
											
 
-