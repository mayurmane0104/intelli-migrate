# Period to date computation - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/period-to-date-function.html](https://docs.aws.amazon.com/quick/latest/userguide/period-to-date-function.html)

---

The period to date computation evaluates values for a specified period to date. For example, you can create a computation to find out how much you've earned in year-to-date sales.

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
- *Time granularity*
- 
								The date granularity that you want to use for the computation, for example year to date. 

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
							`previousMetricValue`– The previous value in the metric dimension.- 
									**value**
- 
									**formattedValue**
- 
									**formattedAbsoluteValue**
 
- 
									
- 
							`previousTimeValue`– The previous value in the datetime dimension.- 
									**value**
- 
									**formattedValue**
 
- 
									
- 
							`currentMetricValue`– The current value in the metric dimension.- 
									**value**
- 
									**formattedValue**
- 
									**formattedAbsoluteValue**
 
- 
									
- 
							`currentTimeValue`– The current value in the datetime dimension.- 
									**value**
- 
									**formattedValue**
 
- 
									
- 
							**periodGranularity****MONTH**,**YEAR**, and so on).
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
									

## Example

					###### To create a Period to date computation

- 
							In the analysis that you want to change, choose **Add insight**.
- 
							For **Computation type**, choose**Period to date**, and then choose**Select**.
- 
							In the new insight that you created, add the time dimenstion and value dimension fields that you want to compare. In the screenshot below, `Order Date`and`Sales (Sum)`are added to the insight. With these two fields selected, Quick Sight shows the year to date sales of the latest month and the percentage difference compared with the previous month.![Field wells showing Order Date in Time section and Sales (Sum) in Values section.](/images/quick/latest/userguide/images/periodOverPeriod1.png)  
- 
							(Optional) To further customize the insight, open the on-visual menu and choose **Customize narrative**. In the**Edit narative**window that appears, drag and drop the fields that you need from the**Computations**list, and then choose**Save**.