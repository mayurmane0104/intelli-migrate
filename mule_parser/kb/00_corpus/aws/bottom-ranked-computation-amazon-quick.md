# Bottom ranked computation - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/bottom-ranked-function.html](https://docs.aws.amazon.com/quick/latest/userguide/bottom-ranked-function.html)

---

The bottom ranked computation calculates the requested number of categories by value that rank in the bottom of the autonarrative's dataset. For example, you can create a computation to find the bottom three states by sales revenue.

To use this function, you need at least one dimension in the
						**Categories** field well. 

## Parameters

					- *name*
- 
								A unique descriptive name that you assign or change. A name is assigned if you don't create your own. You can edit this later. 
- *Category*
- 
								The category dimension that you want to rank. 
- *Value*
- 
								The aggregated measure that the computation is based on. 
- *Number of results*
- 
								The number of ranked results that you want to display. 

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

These are the same output parameters as the ones that are returned by the top ranked computation.

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
							**itemsCount**
- 
							**items**- 
									`categoryField`– The category field.- 
											**value**
- 
											**formattedValue**`NULL`'. If the field is empty, it displays '`(empty)`'.
 
- 
											
- 
									`metricValue`– The metric field.- 
											**value**
- 
											**formattedValue**
- 
											**formattedAbsoluteValue**
 
- 
											
 
- 
									

## Example

					The following screenshot shows the default configuration for the bottom-ranked computation.

![Default configuration for the bottom-ranked computation.](/images/quick/latest/userguide/images/bottom-ranked-computation.png)