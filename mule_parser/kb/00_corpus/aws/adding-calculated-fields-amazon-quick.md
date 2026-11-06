# Adding calculated fields - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/adding-a-calculated-field-analysis.html](https://docs.aws.amazon.com/quick/latest/userguide/adding-a-calculated-field-analysis.html)

---

Create calculated fields to transform your data by using one or more of the following:

You can add calculated fields to a dataset during data preparation or from the analysis page. When you add a calculated field to a dataset during data preparation, it's available to all analyses that use that dataset. When you add a calculated field to a dataset in an analysis, it's available only in that analysis.

Analyses support both single-row operations and aggregate operations. Single-row operations are those that supply a (potentially) different result for every row. Aggregate operations supply results that are always the same for entire sets of rows. For example, if you use a simple string function with no conditions, it changes every row. If you use an aggregate function, it applies to all the rows in a group. If you ask for the total sales amount for the US, the same number applies to the entire set. If you ask for data on a particular state, the total sales amount changes to reflect your new grouping. It still provides one result for the entire set.

By creating the aggregated calculated field within the analysis, you can then drill down into the data. The value of that aggregated field is recalculated appropriately for each level. This type of aggregation isn't possible during dataset preparation.

For example, let's say that you want to figure out the percentage of profit for each
			country, region, and state. You can add a calculated field to your analysis,
				`(sum(salesAmount - cost)) / sum(salesAmount)`. This field is then
			calculated for each country, region, and state, at the time your analyst drills down
			into the geography.

###### Topics

## Adding calculated fields to an analysis

			When you add a dataset to an analysis, every calculated field that exists in the dataset is added to the analysis. You can add additional calculated fields at the analysis level to create calculated fields that are available only in that analysis.

###### To add a calculated field to an analysis

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
					Open the analysis that you want to change. 
- 
					In the **Data**pane, choose**Add**at top left, and then choose**+ CALCULATED FIELD**.- 
							In the calculations editor that opens, do the following: 
- 
							Enter a name for the calculated field. 
- 
							Enter a formula using fields from your dataset, functions, and operators. 
 
- 
							
- 
					When finished, choose **Save**.

For more information about how to create formulas using the available functions in
				Quick Sight, see [Calculated field function and operator reference for Amazon Quick](./calculated-field-reference.html).

## Adding calculated fields to a dataset

			Amazon Quick Sight authors can genreate calculated fields during the data preparation phase of a dataset's creation. When you create a calculated field for a dataset, the field becomes a new column in the dataset. All analyses that use the dataset inherit the dataset's calculated fields.

If the calculated field operates at the row level and the dataset is stored in SPICE, Quick Sight computes and materializes the result in SPICE. If the calculated field relies on an aggregation function, Quick Sight retains the formula and performs the calculation when the analysis is generated. This type of calculated field is called an unmaterialized calculated field.

###### To add or edit a calculated field for a dataset

- 
					Open the dataset that you want to work with. For more information, see [Editing datasets](./edit-a-data-set.html).
- 
					On the data prep page, do one of the following: - 
							To create a new field, choose **Add calculated field**at left.
- 
							To edit an existing calculated field, choose it from **Calculated fields**at left, then choose**Edit**from the context (right-click) menu.
 
- 
							
- 
					In the calculation editor, enter a descriptive name for **Add title**to name the new calculated field. This name appears in the field list in the dataset, so it should look similar to the other fields. For this example, we name the field`Total Sales This Year`.
- 
					(Optional) Add a comment, for example to explain what the expression does, by enclosing text in slashes and asterisks. `/* Calculates sales per year for this year*/`
- 
					Identify the metrics, functions, and other items to use. For this example, we need to identify the following: - 
							The metric to use 
- 
							Functions: `ifelse`and`datediff`
 We want to build a statement like "If the sale happened during this year, show the total sales, and otherwise show 0." To add the `ifelse`function, open the**Functions**list. Choose**All**to close the list of all functions. Now you should see the function groups:**Aggregate**,**Conditional**,**Date**, and so on.Choose **Conditional**, and then double-click on`ifelse`to add it to the workspace.`ifelse()`
- 
							
- 
					Place your cursor inside the parenthesis in the workspace, and add three blank lines. `ifelse( )`
- 
					With your cursor on the first blank line, find the `dateDiff`function. It's listed for**Functions**under**Dates**. You can also find it by entering`date`for**Search functions**. The`dateDiff`function returns all functions that have`date`**Dates**; for example, the`now`function is missing from the search results.Double-click on `dateDiff`to add it to the first blank line of the`ifelse`statement.`ifelse( dateDiff() )`Add the parameters that `dateDiff`uses. Place your cursor inside the`dateDiff`parentheses to begin to add`date1`,`date2`, and`period`:- 
							For `date1`: The first parameter is the field that has the date in it. Find it under**Fields**, and add it to the workspace by double-clicking it or entering its name.
- 
							For `date2`, add a comma, then choose`truncDate()`for**Functions**. Inside its parenthesis, add period and date, like this:`truncDate( "YYYY", now() )`
- 
							For `period`: Add a comma after`date2`and enter`YYYY`. This is the period for the year. To see a list of all the supported periods, find`dateDiff`in the**Functions**list, and open the documentation by choosing**Learn more**. If you're already viewing the documentation, as you are now, see[dateDiff](./dateDiff-function.html).
 Add a few spaces for readability, if you like. Your expression should look like the following. `ifelse( dateDiff( {Date}, truncDate( "YYYY", now() ) ,"YYYY" ) )`
- 
							
- 
					Specify the return value. For our example, the first parameter in `ifelse`needs to return a value of`TRUE`or`FALSE`. Because we want the current year, and we're comparing it to this year, we specify that the`dateDiff`statement should return`0`. The`if`part of the`ifelse`evaluates as true for rows where there is no difference between the year of the sale and the current year.`dateDiff( {Date}, truncDate( "YYYY", now() ) ,"YYYY" ) =``0`To create a field for `TotalSales`for last year, you can change`0`to`1`.Another way to do the same thing is to use `addDateTime`instead of`truncDate`. Then for each previous year, you change the first parameter for`addDateTime`to represent each year. For this, you use`-1`for last year,`-2`for the year before that, and so on. If you use`addDateTime`, you leave the`dateDiff`function`= 0`for each year.`dateDiff( {Discharge Date},``addDateTime(-1, "YYYY", now() )`,"YYYY" ) = 0 /* Last year */
- 
					Move your cursor to the first blank line, just under `dateDiff`. Add a comma.For the `then`part of the`ifelse`statement, we need to choose the measure (metric) that contains the sales amount,`TotalSales`.To choose a field, open the **Fields**list and double-click a field to add it to the screen. Or you can enter the name. Add curly braces`{ }`around names that contain spaces. It's likely that your metric has a different name. You can know which field is a metric by the number sign in front of it (**#**).Your expression should look like the following now. `ifelse( dateDiff( {Date}, truncDate( "YYYY", now() ) ,"YYYY" ) = 0 ,{TotalSales} )`
- 
					Add an `else`clause. The`ifelse`function doesn't require one, but we want to add it. For reporting purposes, you usually don't want to have any null values, because sometimes rows with nulls are omitted.We set the else part of the ifelse to `0`. The result is that this field is`0`for rows that contain sales from previous years.To do this, on the blank line add a comma and then a `0`. If you added the comment at the beginning, your finished`ifelse`expression should look like the following.`/* Calculates sales per year for this year*/ ifelse( dateDiff( {Date}, truncDate( "YYYY", now() ) ,"YYYY" ) = 0 ,{TotalSales} ,0 )`
- 
					Save your work by choosing **Save**at upper right.If there are errors in your expression, the editor displays an error message at the bottom. Check your expression for a red squiggly line, then hover your cursor over that line to see what the error message is. Common errors include missing punctuation, missing parameters, misspellings, and invalid data types. To avoid making any changes, choose **Cancel**.

###### To add a parameter value to a calculated field

- 
					You can reference parameters in calculated fields. By adding the parameter to your expression, you add the current value of that parameter. 
- 
					To add a parameter, open the **Parameters**list, and select the parameter whose value you want to include.
- 
					
					(Optional) To manually add a parameter to the expression, type the name of the parameter. Then enclosed it in curly braces `{}`, and prefix it with a`$`, for example`${parameterName}`.

You can change the data type of any field in your dataset, including the types of calculated fields. You can only choose data types that match the data that's in the field.

###### To change the data type of a calculated field

- 
					For **Calculated fields**(at left), choose the field that you want to change, then choose**Change data type**from the context (right-click) menu.

Unlike the other fields in the dataset, calculated fields can't be disabled. Instead, delete them.

###### To delete a calculated field

- 
					For **Calculated fields**(at left), choose the field that you want to change, then choose**Delete**from the context (right-click) menu.

## Handling decimal values in calculated fields

			When your dataset uses Direct Query mode, the calculation of the decimal data type is determined by the behavior of the source engine that the dataset originates from. In some particular cases, Quick Sight applies special handlings to determine the output calculation's data type.

When your dataset uses SPICE query mode and a calculated field is materialized, the data type of the result is contingent on the specific function operators and the data type of the input. The tables below show the expected bahavior for some numeric calculated fields.

**Unary operators**

The following table shows which data type is output based on the operator you use
				and the data type of the value that you input. For example, if you input an integer
				to an `abs` calculation, the output value's data type is
				integer.

| Operator | Input type | Output type | 
|---|---|---|
| `abs` | Decimal-fixed | Decimal-fixed | 
| Int | Int | |
| Decimal-float | Decimal-float | |
| `ceil` | Decimal-fixed | Int | 
| Int | Int | |
| Decimal-float | Int | |
| `exp` | Decimal-fixed | Decimal-float | 
| Int | Decimal-float | |
| Decimal-float | Decimal-float | |
| `floor` | Decimal-fixed | Int | 
| Int | Int | |
| Decimal-float | Int | |
| `ln` | Decimal-fixed | Decimal-float | 
| Int | Decimal-float | |
| Decimal-float | Decimal-float | |
| `log` | Decimal-fixed | Decimal-float | 
| Int | Decimal-float | |
| Decimal-float | Decimal-float | |
| `round` | Decimal-fixed | Decimal-fixed | 
| Int | Decimal-fixed | |
| Decimal-float | Decimal-fixed | |
| `sqrt` | Decimal-fixed | Decimal-float | 
| Int | Decimal-float | |
| Decimal-float | Decimal-float | 

**Binary operators**

The following tables show which data type is output based on the data types of the two values that you input. For example, for an arithmetic operator, if you provide two integer data types, the result of the calculation output as an integer.

For basic operators (+, -, *):

| Integer | Decimal-fixed | Decimal-float | |
|---|---|---|---|
| 
 | Integer | Decimal-fixed | Decimal-float | 
| 
 | Decimal-fixed | Decimal-fixed | Decimal-float | 
| 
 | Decimal-float | Decimal-float | Decimal-float | 

For division operators (/):

| Integer | Decimal-fixed | Decimal-float | |
|---|---|---|---|
| 
 | Decimal-float | Decimal-float | Decimal-float | 
| 
 | Decimal-float | Decimal-fixed | Decimal-float | 
| 
 | Decimal-float | Decimal-float | Decimal-float | 

For exponential and mod operators (^, %):

| Integer | Decimal-fixed | Decimal-float | |
|---|---|---|---|
| 
 | Decimal-float | Decimal-float | Decimal-float | 
| 
 | Decimal-float | Decimal-float | Decimal-float | 
| 
 | Decimal-float | Decimal-float | Decimal-float |