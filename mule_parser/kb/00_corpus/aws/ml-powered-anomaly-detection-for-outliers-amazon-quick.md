# ML-powered anomaly detection for outliers - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-function.html](https://docs.aws.amazon.com/quick/latest/userguide/anomaly-detection-function.html)

---

The ML-powered anomaly detection computation searches your data for outliers. For example, you can detect the top three outliers for total sales on January 3, 2019. If you enable contribution analysis, you can also detect the key drivers for each outlier.

To use this function, you need at least one dimension in the
						**Time** field well, at least one measure in the
						**Values** field well, and at least one dimension in the
						**Categories** field well. The configuration screen
					provides an option to analyze the contribution of other fields as key drivers,
					even if those fields aren't in the field wells.

For more information, see [Detecting outliers with ML-powered anomaly detection](./anomaly-detection.html).

###### Note

You can't add ML-powered anomaly detection to another computation, and you can't add another computation to an anomaly detection.

## Computation outputs

					Each function generates a set of output parameters. You can add these outputs to the autonarrative to customize what it displays. You can also add your own custom text.

To locate the output parameters, open the
							**Computations** tab on the right, and locate the
						computation that you want to use. The names of the computations come from
						the name that you provide when you create the insight. Choose the output
						parameter by clicking on it only once. If you click twice, you add the same
						output twice. You can use items displayed in ** bold monospace font** following in the
						narrative. 

- 
							`timeField`– From the**Time**field well.- 
									**name**
- 
									**timeGranularity****DAY**,**YEAR**, and so on).
 
- 
									
- 
							**categoryFields****Categories**field well.- 
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
									`timeValue`– The values in the date dimension.- 
											**value**
- 
											**formattedValue**
 
- 
											
- 
									**categoryName**
- 
									**direction**`HIGH`or`LOW`.`HIGH`means "higher than expected."`LOW`means "lower than expected."When iterating on items, `AnomalyDetection.items[index].direction`can contain either`HIGH`or`LOW`. For example,`AnomalyDetection.items[index].direction='HIGH'`or`AnomalyDetection.items[index].direction=LOW`.`AnomalyDetection.direction`can have an empty string for`ALL`. An example is`AnomalyDetection.direction=''`.
- 
									`actualValue`– The metric's actual value at the point of the anomaly or outlier.- 
											**value**
- 
											**formattedValue**
- 
											**formattedAbsoluteValue**
 
- 
											
- 
									`expectedValue`– The metric's expected value at the point of the anomaly (outlier).- 
											**value**
- 
											**formattedValue**
- 
											**formattedAbsoluteValue**
 
- 
											
 
-