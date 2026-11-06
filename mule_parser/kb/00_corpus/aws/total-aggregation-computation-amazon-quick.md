# Total aggregation computation - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/total-aggregation-function.html](https://docs.aws.amazon.com/quick/latest/userguide/total-aggregation-function.html)

---

The total aggregation computation creates a grand total of the value. For example, you can create a computation to find the total revenue.

To use this function, you need at least one dimension in the
						**Time** field well and at least one measure in the
						**Values** field well. 

## Parameters

					- *name*
- 
								A unique descriptive name that you assign or change. A name is assigned if you don't create your own. You can edit this later. 
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

- 
							`categoryField`– The category field.- 
									**name**
 
- 
									
- 
							`metricField`– From the**Values**field well.- 
									**name**
- 
									**aggregationFunction****SUM**,**AVG**, and so on).
 
- 
									
- 
							`totalAggregate`– The total value of the metric aggregation.- 
									**value**
- 
									**formattedValue**
- 
									**formattedAbsoluteValue**
 
-