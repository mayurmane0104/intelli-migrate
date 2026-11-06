# Functions by category - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/functions-by-category.html](https://docs.aws.amazon.com/quick/latest/userguide/functions-by-category.html)

---

In this section, you can find a list of the functions available in Amazon Quick, sorted by category.

###### Topics

## Aggregate functions

			The aggregate functions for calculated fields in Amazon Quick include the following. These are only available during analysis and visualization. Each of these functions returns values grouped by the chosen dimension or dimensions. For each aggregation, there is also a conditional aggregation. These perform the same type of aggregation, based on a condition.

- 
					[avg](https://docs.aws.amazon.com/quicksight/latest/user/avg-function.html)averages the set of numbers in the specified measure, grouped by the chosen dimension or dimensions.
- 
					[avgIf](https://docs.aws.amazon.com/quicksight/latest/user/avgIf-function.html)calculates the average based on a conditional statement.
- 
					[count](https://docs.aws.amazon.com/quicksight/latest/user/count-function.html)calculates the number of values in a dimension or measure, grouped by the chosen dimension or dimensions.
- 
					[countIf](https://docs.aws.amazon.com/quicksight/latest/user/countIf-function.html)calculates the count based on a conditional statement.
- 
					[distinct_count](https://docs.aws.amazon.com/quicksight/latest/user/distinct_count-function.html)calculates the number of distinct values in a dimension or measure, grouped by the chosen dimension or dimensions.
- 
					[distinct_countIf](https://docs.aws.amazon.com/quicksight/latest/user/distinct_countIf-function.html)calculates the distinct count based on a conditional statement.
- 
					[max](https://docs.aws.amazon.com/quicksight/latest/user/max-function.html)returns the maximum value of the specified measure, grouped by the chosen dimension or dimensions.
- 
					[maxIf](https://docs.aws.amazon.com/quicksight/latest/user/maxIf-function.html)calculates the maximum based on a conditional statement.
- 
					[median](https://docs.aws.amazon.com/quicksight/latest/user/median-function.html)returns the median value of the specified measure, grouped by the chosen dimension or dimensions.
- 
					[medianIf](https://docs.aws.amazon.com/quicksight/latest/user/medianIf-function.html)calculates the median based on a conditional statement.
- 
					[min](https://docs.aws.amazon.com/quicksight/latest/user/min-function.html)returns the minimum value of the specified measure, grouped by the chosen dimension or dimensions.
- 
					[minIf](https://docs.aws.amazon.com/quicksight/latest/user/minIf-function.html)calculates the minimum based on a conditional statement.
- 
					[percentile](https://docs.aws.amazon.com/quicksight/latest/user/percentile-function.html)(alias of`percentileDisc`) computes the*n*th percentile of the specified measure, grouped by the chosen dimension or dimensions.
- 
					[percentileCont](https://docs.aws.amazon.com/quicksight/latest/user/percentileCont-function.html)calculates the*n*th percentile based on a continuous distribution of the numbers of the specified measure, grouped by the chosen dimension or dimensions.
- 
					[percentileDisc (percentile)](https://docs.aws.amazon.com/quicksight/latest/user/percentileDisc-function.html)calculates the*n*th percentile based on the actual numbers of the specified measure, grouped by the chosen dimension or dimensions.
- 
					[periodToDateAvg](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateAvg-function.html)averages the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateCount](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateCount-function.html)calculates the number of values in a dimension or measure for a given time granularity (for instance, Quarter) up to a point in time including duplicates.
- 
					[periodToDateMax](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMax-function.html)returns the maximum value of the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateMedian](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMedian-function.html)returns the median value of the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateMin](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMin-function.html)returns the minimum value of the specified measure or date for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDatePercentile](https://docs.aws.amazon.com/quicksight/latest/user/periodToDatePercentile-function.html)calculates the percentile based on the actual numbers in measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDatePercentileCont](https://docs.aws.amazon.com/quicksight/latest/user/periodToDatePercentileCont-function.html)calculates percentile based on a continuous distribution of the numbers in the measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateStDev](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateStDev-function.html)calculates the standard deviation of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time based on a sample.
- 
					[periodToDateStDevP](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateStDevP-function.html)calculates the population standard deviation of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time based on a sample.
- 
					[periodToDateSum](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateSum-function.html)adds the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateVar](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateVar-function.html)calculates the sample variance of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateVarP](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateVarP-function.html)calculates the population variance of the set of numbers in the specified measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[stdev](https://docs.aws.amazon.com/quicksight/latest/user/stdev-function.html)) calculates the standard deviation of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a sample.
- 
					[stdevIf](https://docs.aws.amazon.com/quicksight/latest/user/stdevIf-function.html)calculates the sample standard deviation based on a conditional statement.
- 
					[stdevp](https://docs.aws.amazon.com/quicksight/latest/user/stdevp-function.html)calculates the standard deviation of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a biased population.
- 
					[stdevpIf](https://docs.aws.amazon.com/quicksight/latest/user/stdevpIf-function.html)calculates the population deviation based on a conditional statement.
- 
					[var](https://docs.aws.amazon.com/quicksight/latest/user/var-function.html)) calculates the variance of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a sample.
- 
					[varIf](https://docs.aws.amazon.com/quicksight/latest/user/varIf-function.html)calculates the sample variance based on a conditional statement.
- 
					[varp](https://docs.aws.amazon.com/quicksight/latest/user/varp-function.html)) calculates the variance of the set of numbers in the specified measure, grouped by the chosen dimension or dimensions, based on a biased population.
- 
					[varpIf](https://docs.aws.amazon.com/quicksight/latest/user/varpIf-function.html)calculates the population variance based on a conditional statement.
- 
					[sum](https://docs.aws.amazon.com/quicksight/latest/user/sum-function.html)) adds the set of numbers in the specified measure, grouped by the chosen dimension or dimensions.
- 
					[sumIf](https://docs.aws.amazon.com/quicksight/latest/user/sumIf-function.html)) calculates the sum based on a conditional statement.

## Conditional functions

			The conditional functions for calculated fields in Amazon Quick include the following:

- 
					[Coalesce](https://docs.aws.amazon.com/quicksight/latest/user/coalesce-function.html)returns the value of the first argument that is not null.
- 
					[Ifelse](https://docs.aws.amazon.com/quicksight/latest/user/ifelse-function.html)evaluates a set of*if*,*then*expression pairings, and returns the value of the*then*argument for the first*if*argument that evaluates to true.
- 
					[in](https://docs.aws.amazon.com/quicksight/latest/user/in-function.html)evaluates an expression to see if it is in a given list of values.
- 
					[isNotNull](https://docs.aws.amazon.com/quicksight/latest/user/isNotNull-function.html)evaluates an expression to see if it is not null.
- 
					[isNull](https://docs.aws.amazon.com/quicksight/latest/user/isNull-function.html)evaluates an expression to see if it is null. If the expression is null,`isNull`returns true, and otherwise it returns false.
- 
					[notIn](https://docs.aws.amazon.com/quicksight/latest/user/notIn-function.html)evaluates an expression to see if it is not in a given list of values.
- 
					[nullIf](https://docs.aws.amazon.com/quicksight/latest/user/nullIf-function.html)compares two expressions. If they are equal, the function returns null. If they are not equal, the function returns the first expression.
- 
					[switch](https://docs.aws.amazon.com/quicksight/latest/user/switch-function.html)returns an expression that matches the first label equal to the condition expression.

## Date functions

			The date functions for calculated fields in Amazon Quick include the following:

- 
					[addDateTime](https://docs.aws.amazon.com/quicksight/latest/user/addDateTime-function.html)adds or subtracts a unit of time to the date or time provided.
- 
					[addWorkDays](https://docs.aws.amazon.com/quicksight/latest/user/addWorkDays-function.html)adds or subtracts the given number of work days to the date or time provided.
- 
					[dateDiff](https://docs.aws.amazon.com/quicksight/latest/user/dateDiff-function.html)returns the difference in days between two date fields.
- 
					[epochDate](https://docs.aws.amazon.com/quicksight/latest/user/epochDate-function.html)converts an epoch date into a standard date.
- 
					[Extract](https://docs.aws.amazon.com/quicksight/latest/user/extract-function.html)returns a specified portion of a date value.
- 
					[formatDate](https://docs.aws.amazon.com/quicksight/latest/user/formatDate-function.html)formats a date using a pattern you specify.
- 
					[isWorkDay](https://docs.aws.amazon.com/quicksight/latest/user/isWorkDay-function.html)returns TRUE if a given date-time value is a work or business day.
- 
					[netWorkDays](https://docs.aws.amazon.com/quicksight/latest/user/netWorkDays-function.html)returns the number of working days between the provided two date values.
- 
					[Now](https://docs.aws.amazon.com/quicksight/latest/user/now-function.html)returns the current date and time, using either settings for a database, or UTC for file and Salesforce.
- 
					[truncDate](https://docs.aws.amazon.com/quicksight/latest/user/truncDate-function.html)returns a date value that represents a specified portion of a date.

## Numeric functions

			The numeric functions for calculated fields in Amazon Quick include the following:

- 
					[Ceil](https://docs.aws.amazon.com/quicksight/latest/user/ceil-function.html)rounds a decimal value to the next highest integer.
- 
					[decimalToInt](https://docs.aws.amazon.com/quicksight/latest/user/decimalToInt-function.html)converts a decimal value to an integer.
- 
					[Floor](https://docs.aws.amazon.com/quicksight/latest/user/floor-function.html)decrements a decimal value to the next lowest integer.
- 
					[intToDecimal](https://docs.aws.amazon.com/quicksight/latest/user/intToDecimal-function.html)converts an integer value to a decimal.
- 
					[Round](https://docs.aws.amazon.com/quicksight/latest/user/round-function.html)rounds a decimal value to the closest integer or, if scale is specified, to the closest decimal place.

## Mathematical functions

			The mathematical functions for calculated fields in Amazon Quick include the following:

- 
					[Mod](https://docs.aws.amazon.com/quicksight/latest/user/mod-function.html)(`number`,`divisor`)
- 
					[Log](https://docs.aws.amazon.com/quicksight/latest/user/log-function.html)(`expression`)
- 
					[Ln](https://docs.aws.amazon.com/quicksight/latest/user/ln-function.html)(`expression`)
- 
					[Abs](https://docs.aws.amazon.com/quicksight/latest/user/abs-function.html)(`expression`)
- 
					[Sqrt](https://docs.aws.amazon.com/quicksight/latest/user/sqrt-function.html)(`expression`)
- 
					[Exp](https://docs.aws.amazon.com/quicksight/latest/user/exp-function.html)(`expression`)*e*raised to the power of a given expression.

## String functions

			The string (text) functions for calculated fields in Amazon Quick include the following:

- 
					[Concat](https://docs.aws.amazon.com/quicksight/latest/user/concat-function.html)concatenates two or more strings.
- 
					[contains](https://docs.aws.amazon.com/quicksight/latest/user/contains-function.html)checks if an expression contains a substring.
- 
					[endsWith](https://docs.aws.amazon.com/quicksight/latest/user/endsWith-function.html)checks if the expression ends with the substring specified.
- 
					[Left](https://docs.aws.amazon.com/quicksight/latest/user/left-function.html)returns the specified number of leftmost characters from a string.
- 
					[Locate](https://docs.aws.amazon.com/quicksight/latest/user/locate-function.html)locates a substring within another string, and returns the number of characters before the substring.
- 
					[Ltrim](https://docs.aws.amazon.com/quicksight/latest/user/ltrim-function.html)removes preceding blank space from a string.
- 
					[parseDate](https://docs.aws.amazon.com/quicksight/latest/user/parseDate-function.html)parses a string to determine if it contains a date value, and returns the date if found.
- 
					[parseDecimal](https://docs.aws.amazon.com/quicksight/latest/user/parseDecimal-function.html)parses a string to determine if it contains a decimal value.
- 
					[parseInt](https://docs.aws.amazon.com/quicksight/latest/user/parseInt-function.html)parses a string to determine if it contains an integer value.
- 
					[parseJson](https://docs.aws.amazon.com/quicksight/latest/user/parseJson-function.html)parses values from a native JSON or from a JSON object in a text field.
- 
					[Replace](https://docs.aws.amazon.com/quicksight/latest/user/replace-function.html)replaces part of a string with a new string.
- 
					[Right](https://docs.aws.amazon.com/quicksight/latest/user/right-function.html)returns the specified number of rightmost characters from a string.
- 
					[Rtrim](https://docs.aws.amazon.com/quicksight/latest/user/rtrim-function.html)removes following blank space from a string.
- 
					[Split](https://docs.aws.amazon.com/quicksight/latest/user/split-function.html)splits a string into an array of substrings, based on a delimiter that you choose, and returns the item specified by the position.
- 
					[startsWith](https://docs.aws.amazon.com/quicksight/latest/user/startsWith-function.html)checks if the expression starts with the substring specified.
- 
					[Strlen](https://docs.aws.amazon.com/quicksight/latest/user/strlen-function.html)returns the number of characters in a string.
- 
					[Substring](https://docs.aws.amazon.com/quicksight/latest/user/substring-function.html)returns the specified number of characters in a string, starting at the specified location.
- 
					[toLower](https://docs.aws.amazon.com/quicksight/latest/user/toLower-function.html)formats a string in all lowercase.
- 
					[toString](https://docs.aws.amazon.com/quicksight/latest/user/toString-function.html)formats the input expression as a string.
- 
					[toUpper](https://docs.aws.amazon.com/quicksight/latest/user/toUpper-function.html)formats a string in all uppercase.
- 
					[trim](https://docs.aws.amazon.com/quicksight/latest/user/trim-function.html)removes both preceding and following blank space from a string.

## Table calculations

			Table calculations form a group of functions that provide context in an analysis. They provide support for enriched aggregated analysis. By using these calculations, you can address common business scenarios such as calculating percentage of total, running sum, difference, common baseline, and rank.

When you are analyzing data in a specific visual, you can apply table calculations to the current set of data to discover how dimensions influence measures or each other. Visualized data is your result set based on your current dataset, with all the filters, field selections, and customizations applied. To see exactly what this result set is, you can export your visual to a file. A table calculation function performs operations on the data to reveal relationships between fields.

**Lookup-based functions**

- 
					[difference](https://docs.aws.amazon.com/quicksight/latest/user/difference-function.html)calculates the difference between a measure based on one set of partitions and sorts, and a measure based on another.
- 
					[lag](https://docs.aws.amazon.com/quicksight/latest/user/lag-function.html)calculates the lag (previous) value for a measure.
- 
					[lead](https://docs.aws.amazon.com/quicksight/latest/user/lead-function.html)calculates the lead (following) value for a measure.
- 
					[percentDifference](https://docs.aws.amazon.com/quicksight/latest/user/percentDifference-function.html)calculates the percentage difference between the current value and a comparison value.

**Over functions**

- 
					[avgOver](https://docs.aws.amazon.com/quicksight/latest/user/avgOver-function.html)calculates the average of a measure over one or more dimensions.
- 
					[countOver](https://docs.aws.amazon.com/quicksight/latest/user/countOver-function.html)calculates the count of a field over one or more dimensions.
- 
					[distinctCountOver](https://docs.aws.amazon.com/quicksight/latest/user/distinctCountOver-function.html)calculates the distinct count of the operand partitioned by the specified attributes at a specified level.
- 
					[maxOver](https://docs.aws.amazon.com/quicksight/latest/user/maxOver-function.html)calculates the maximum of a measure over one or more dimensions.
- 
					[minOver](https://docs.aws.amazon.com/quicksight/latest/user/minOver-function.html)the minimum of a measure over one or more dimensions.
- 
					[percentileOver](https://docs.aws.amazon.com/quicksight/latest/user/percentileOver-function.html)(alias of`percentileDiscOver`) calculates the*n*th percentile of a measure partitioned by a list of dimensions.
- 
					[percentileContOver](https://docs.aws.amazon.com/quicksight/latest/user/percentileContOver-function.html)calculates the*n*th percentile based on a continuous distribution of the numbers of a measure partitioned by a list of dimensions.
- 
					[percentileDiscOver](https://docs.aws.amazon.com/quicksight/latest/user/percentileDiscOver-function.html)calculates the*n*th percentile based on the actual numbers of a measure partitioned by a list of dimensions.
- 
					[percentOfTotal](https://docs.aws.amazon.com/quicksight/latest/user/percentOfTotal-function.html)calculates the percentage that a measure contributes to the total.
- 
					[periodOverPeriodDifference](https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodDifference-function.html)calculates the difference of a measure over two different time periods as specified by period granularity and offset.
- 
					[periodOverPeriodLastValue](https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodLastValue-function.html)calculates the last (previous) value of a measure from a previous time period as specified by period granularity and offset.
- 
					[periodOverPeriodPercentDifference](https://docs.aws.amazon.com/quicksight/latest/user/periodOverPeriodPercentDifference-function.html)calculates the percent difference of a measure over two different time periods as specified by period granularity and offset.
- 
					[periodToDateAvgOverTime](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateAvgOverTime-function.html)calculates the average of a measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateCountOverTime](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateCountOverTime-function.html)calculates the count of a dimension or measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateMaxOverTime](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMaxOverTime-function.html)calculates the maximum of a measure or date for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateMinOverTime](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateMinOverTime-function.html)calculates the minimum of a measure or date for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[periodToDateSumOverTime](https://docs.aws.amazon.com/quicksight/latest/user/periodToDateSumOverTime-function.html)calculates the sum of a measure for a given time granularity (for instance, a quarter) up to a point in time.
- 
					[sumOver](https://docs.aws.amazon.com/quicksight/latest/user/sumOver-function.html)calculates the sum of a measure over one or more dimensions.
- 
					[stdevOver](https://docs.aws.amazon.com/quicksight/latest/user/stdevOver-function.html)calculates the standard deviation of the specified measure, partitioned by the chosen attribute or attributes, based on a sample.
- 
					[stdevpOver](https://docs.aws.amazon.com/quicksight/latest/user/stdevpOver-function.html)calculates the standard deviation of the specified measure, partitioned by the chosen attribute or attributes, based on a biased population.
- 
					[varOver](https://docs.aws.amazon.com/quicksight/latest/user/varOver-function.html)calculates the variance of the specified measure, partitioned by the chosen attribute or attributes, based on a sample.
- 
					[varpOver](https://docs.aws.amazon.com/quicksight/latest/user/varpOver-function.html)calculates the variance of the specified measure, partitioned by the chosen attribute or attributes, based on a biased population.

**Ranking functions**

- 
					[rank](https://docs.aws.amazon.com/quicksight/latest/user/rank-function.html)calculates the rank of a measure or a dimension.
- 
					[denseRank](https://docs.aws.amazon.com/quicksight/latest/user/denseRank-function.html)calculates the rank of a measure or a dimension, ignoring duplicates.
- 
					[percentileRank](https://docs.aws.amazon.com/quicksight/latest/user/percentileRank-function.html)calculates the rank of a measure or a dimension, based on percentile.

**Running functions**

- 
					[runningAvg](https://docs.aws.amazon.com/quicksight/latest/user/runningAvg-function.html)calculates a running average for a measure.
- 
					[runningCount](https://docs.aws.amazon.com/quicksight/latest/user/runningCount-function.html)calculates a running count for a measure.
- 
					[runningMax](https://docs.aws.amazon.com/quicksight/latest/user/runningMax-function.html)calculates a running maximum for a measure.
- 
					[runningMin](https://docs.aws.amazon.com/quicksight/latest/user/runningMin-function.html)calculates a running minimum for a measure.
- 
					[runningSum](https://docs.aws.amazon.com/quicksight/latest/user/runningSum-function.html)calculates a running sum for a measure.

**Window functions**

- 
					[firstValue](https://docs.aws.amazon.com/quicksight/latest/user/firstValue-function.html)calculates the first value of the aggregated measure or dimension partitioned and sorted by specified attributes.
- 
					[lastValue](https://docs.aws.amazon.com/quicksight/latest/user/lastValue-function.html)calculates the last value of the aggregated measure or dimension partitioned and sorted by specified attributes.
- 
					[windowAvg](https://docs.aws.amazon.com/quicksight/latest/user/windowAvg-function.html)calculates the average of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
- 
					[windowCount](https://docs.aws.amazon.com/quicksight/latest/user/windowCount-function.html)calculates the count of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
- 
					[windowMax](https://docs.aws.amazon.com/quicksight/latest/user/windowMax-function.html)calculates the maximum of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
- 
					[windowMin](https://docs.aws.amazon.com/quicksight/latest/user/windowMin-function.html)calculates the minimum of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.
- 
					[windowSum](https://docs.aws.amazon.com/quicksight/latest/user/windowSum-function.html)calculates the sum of the aggregated measure in a custom window that is partitioned and sorted by specified attributes.