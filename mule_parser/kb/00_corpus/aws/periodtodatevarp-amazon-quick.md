# periodToDateVarP - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/periodToDateVarP-function.html](https://docs.aws.amazon.com/quick/latest/userguide/periodToDateVarP-function.html)

---

The `periodToDateVarP` function calculates the population variance of the
			set of numbers in the specified measure for a given time granularity (for instance, a
			quarter) up to a point in time, relevant to that period.

## Syntax

			`periodToDateVarP(`measure, dateTime, period, endDate (optional))

## Arguments

			- 
						*measure*
- 
						The argument must be a field. Null values are omitted from the results. Literal values don't work. 
- 
						*dateTime*
- 
						The Date dimension over which you're computing PeriodToDate aggregations. 
- 
						*period*
- 
						The time period across which you're computing the computation. Granularity of `YEAR`means`YearToDate`computation,`Quarter`means`QuarterToDate`, and so on. Valid granularities include`YEAR`,`QUARTER`,`MONTH`,`WEEK`,`DAY`,`HOUR`,`MINUTE`, and`SECONDS`.
- 
						*endDate*
- 
						(Optional) The date dimension that you're ending computing periodToDate aggregations. It defaults to `now()`if omitted.

## Example

			The following example calculates the week-to-date minimum fare amount per payment type, for the week of 06-30-21. For simplicity in the example, we filtered out only a single payment. 06-30-21 is Wednesday. Quick begins the week on Sundays. In our example, that is 06-27-21.

`periodToDateVarP(fare_amount, pickUpDatetime, WEEK, parseDate("06-30-2021", "MM-dd-yyyy"))`![This is an image of the results from the example calculation.](/images/quick/latest/userguide/images/PTDVarPResults.png)