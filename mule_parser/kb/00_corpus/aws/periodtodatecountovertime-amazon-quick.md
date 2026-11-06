# periodToDateCountOverTime - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/periodToDateCountOverTime-function.html](https://docs.aws.amazon.com/quick/latest/userguide/periodToDateCountOverTime-function.html)

---

The `periodToDateCountOverTime` function calculates the count of a
			dimension or measure for a given time granularity (for instance, a quarter) up to a
			point in time.

## Syntax

			`periodToDateCountOverTime(`measure, dateTime, period)

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

			The following example calculates the count of vendors month over month.

`periodToDateCountOverTime(count(vendorid), pickupDatetime, MONTH)`![This is an image of the results of the example calculation with illustrations.](/images/quick/latest/userguide/images/PTDCountOverTimeResults.png)