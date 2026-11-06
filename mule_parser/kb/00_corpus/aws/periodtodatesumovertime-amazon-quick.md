# periodToDateSumOverTime - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/periodToDateSumOverTime-function.html](https://docs.aws.amazon.com/quick/latest/userguide/periodToDateSumOverTime-function.html)

---

The `periodToDateSumOverTime` function calculates the sum of a measure for
			a given time granularity (for instance, a quarter) up to a point in time.

## Syntax

			`periodToDateSumOverTime(`measure, dateTime, period)

## Arguments

			- 
						*measure*
- 
						An aggregated measure that you want to do the calculation 
- 
						*dateTime*
- 
						The date dimension over which you're computing PeriodOverTime calculations. 
- 
						*period*
- 
						(Optional) The time period across which you're computing the computation. Granularity of `YEAR`means`YearToDate`computation,`Quarter`means`QuarterToDate`, and so on. Valid granularities include`YEAR`,`QUARTER`,`MONTH`,`WEEK`,`DAY`,`HOUR`,`MINUTE`, and`SECONDS`.The default value is the visual's date dimension granularity. 

## Example

			The following function returns the total fare amount month over month.

`periodToDateSumOverTime(sum({fare_amount}), pickupDatetime, MONTH)`![This is an image of the results of the example calculation with illustrations.](/images/quick/latest/userguide/images/PTDSumOverTime-example-results.png)