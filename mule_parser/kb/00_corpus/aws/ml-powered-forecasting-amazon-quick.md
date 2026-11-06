# ML-powered forecasting - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/forecast-function.html](https://docs.aws.amazon.com/quick/latest/userguide/forecast-function.html)

---

The ML-powered forecast computation forecasts future metrics based on patterns of previous metrics by seasonality. For example, you can create a computation to forecast total revenue for the next six months.

To use this function, you need at least one dimension in the
						**Time** field well. 

For more information about working with forecasts, see [Forecasting and creating what-if scenarios with Amazon Quick Sight](./forecasts-and-whatifs.html).

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
- *Periods forward*
- 
								The number of time periods in the future that you want to forecast. Ranges from 1 to 1,000. 
- *Periods backward*
- 
								The number of time periods in the past that you want to base your forecast on. Ranges from 0 to 1,000. 
- *Seasonality*
- 
								The number of seasons included in the calendar year. The default setting, **automatic**detects this for you. Ranges from 1 to 180.

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
							`metricValue`– The value in the metric dimension.- 
									**value**
- 
									**formattedValue**
- 
									**formattedAbsoluteValue**
 
- 
									
- 
							`timeValue`– The value in the date dimension.- 
									**value**
- 
									**formattedValue**
 
- 
									
- 
							**relativePeriodsToForecast**