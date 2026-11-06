# Ifelse - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/ifelse-function.html](https://docs.aws.amazon.com/quick/latest/userguide/ifelse-function.html)

---

`ifelse` evaluates a set of *if*,
					*then* expression pairings, and returns the value of the
					*then* argument for the first *if*
				argument that evaluates to true. If none of the *if* arguments
				evaluate to true, then the value of the *else* argument is
				returned.

## Syntax

				`ifelse(``if-expression-1`,`then-expression-1`[,`if-expression-n`,`then-expression-n`...],`else-expression`)

## Arguments

				`ifelse` requires one or more
						*if*,*then* expression pairings, and
					requires exactly one expression for the *else* argument. 

- 
							*if-expression*
- 
							The expression to be evaluated as true or not. It can be a field name like `address1`, a literal value like`'Unknown'`, or another function like`toString(salesAmount)`. An example is`isNotNull(FieldName)`.If you use multiple AND and OR operators in the `if`argument, enclose statements in parentheses to identify processing order. For example, the following`if`argument returns records with a month of 1, 2, or 5 and a year of 2000.`ifelse((month = 5 OR month < 3) AND year = 2000, 'yes', 'no')`The next `if`argument uses the same operators, but returns records with a month of 5 and any year, or with a month of 1 or 2 and a year of 2000.`ifelse(month = 5 OR (month < 3 AND year = 2000), 'yes', 'no')`
- 
							*then-expression*
- 
							The expression to return if its *if*argument is evaluated as true. It can be a field name like`address1`, a literal value like`'Unknown'`, or a call to another function. The expression must have the same data type as the other`then`arguments and the`else`argument.
- 
							*else-expression*
- 
							The expression to return if none of the *if*arguments evaluate as true. It can be a field name like`address1`, a literal value like`'Unknown'`, or another function like`toString(salesAmount)`. The expression must have the same data type as all of the`then`arguments.

## Return type

				`ifelse` returns a value of the same data type as the values in
						*then-expression*. All data returned
						*then* and *else* expressions must be of the same data type or be converted
					to the same data type. 

## Examples

				The following example generates a column of aliases for field
						`country`.

`ifelse(country = "United States", "US", country = "China", "CN", country = "India", "IN", "Others") `For such use cases evaluating each value in a field against a list of
					literals, and returns the result corresponding to the first matching value.,
					function switch is recommended to simplify your work. The previous example can
					be rewritten to the following statement using [switch](https://docs.aws.amazon.com/quicksight/latest/user/switch-function.html):

`switch(country,"United States","US","China","CN","India","IN","Others")`The following example categorizes sales per customer into human-readable levels.

`ifelse(salesPerCustomer < 1000, “VERY_LOW”, salesPerCustomer < 10000, “LOW”, salesPerCustomer < 100000, “MEDIUM”, “HIGH”)`The following example uses AND, OR, and NOT to compare multiple expressions
					using conditional operators to tag top customers NOT in Washington or Oregon
					with a special promotion, who made more than 10 orders. If no values are
					returned, the value `'n/a'` is used.

`ifelse(( (NOT (State = 'WA' OR State =  'OR')) AND Orders > 10),  'Special Promotion XYZ',  'n/a')`The following examples use only OR to generate a new column that contains the
					name of continent that corresponds to each `country`.

`ifelse(country = "United States" OR country = "Canada", "North America", country = "China" OR country = "India" OR country = "Japan", "Asia", "Others")`The previous example can be simplified as shown in the next example. The
					following example uses `ifelse` and [in](https://docs.aws.amazon.com/quicksight/latest/user/in-function.html) to create a value in a new column for any row
					where the tested value is in a literal list. You could use `ifelse`
					with [notIn](https://docs.aws.amazon.com/quicksight/latest/user/notIn-function.html) as well.

`ifelse(in(country,["United States", "Canada"]), "North America", in(country,["China","Japan","India"]),"Asia","Others")`Authors are able to save a literal list in a multivalue parameter and use it
					in the [in](https://docs.aws.amazon.com/quicksight/latest/user/in-function.html) or [notIn](https://docs.aws.amazon.com/quicksight/latest/user/notIn-function.html) functions. The following example is an
					equivalent of the previous example, except that the literal lists are stored in
					two multivalue parameters. 

`ifelse(in(country,${NorthAmericaCountryParam}), "North America", in(country,${AsiaCountryParam}),"Asia", "Others") `The following example assigns a group to a sales record based on the sales
					total. The structure of each `if-then` phrase mimics the behavior of
						*between*, a keyword that doesn't currently
					work in calculated field expressions. For example, the result of the comparison
						`salesTotal >= 0 AND salesTotal < 500` returns the same
					values as the SQL comparison `salesTotal between 0 and 499`.

`ifelse(salesTotal >= 0 AND salesTotal < 500, 'Group 1', salesTotal >= 500 AND salesTotal < 1000, 'Group 2', 'Group 3')`The following example tests for a NULL value by using `coalesce` to
					return the first non-NULL value. Instead of needing to remember the meaning of a
					NULL in a date field, you can use a readable description instead. If the
					disconnect date is NULL, the example returns the suspend date, unless both of
					those are NULL. Then `coalesce(DiscoDate, SuspendDate, '12/31/2491')`
					returns `'12/31/2491'`. The return value must match the other data
					types. This date might seem like an unusual value, but a date in the 25th
					century reasonably simulates the "end of time," defined as the highest
					date in a data mart. 

`ifelse (  (coalesce(DiscoDate, SuspendDate, '12/31/2491') = '12/31/2491'),  'Active subscriber', 'Inactive subscriber')`The following shows a more complex example in a more readable format, just to
					show that you don't need to compress your code all into one long line. This
					example provides for multiple comparisons of the value a survey result. It
					handles potential NULL values for this field and categorizes two acceptable
					ranges. It also labels one range that needs more testing and another that's not
					valid (out of range). For all remaining values, it applies the `else`
					condition, and labels the row as needing a retest three years after the date on
					that row. 

```
ifelse
( 
    isNull({SurveyResult}), 'Untested',  
    {SurveyResult}=1, 'Range 1', 
    {SurveyResult}=2, 'Range 2', 
    {SurveyResult}=3, 'Need more testing',
    {SurveyResult}=99, 'Out of Range',
    concat  
    (
        'Retest by ', 
        toString    
        (
           addDateTime(3, "YYYY", {Date}) 
        )
    )
) 
```
The following example assigns a "manually" created region name to a group of
					states. It also uses spacing and comments, wrapped in `/* */`, to
					make it easier to maintain the code. 

```
ifelse 
(    /* NE REGION*/
     locate('New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire',{State}) > 0,
    'Northeast',
     /* SE REGION*/
     locate('Georgia, Alabama, South Carolina, Louisiana',{State}) > 0,
    'Southeast',
    'Other Region'
)
```
The logic for the region tagging breaks down as follows:

- 
						We list the states that we want for each region, enclosing each list in quotation marks to make each list a string, as follows: - 
								`'New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire'`
- 
								`'Georgia, Alabama, South Carolina, Louisiana'`
- 
								You can add more sets, or use countries, cities, provinces, or What3Words if you want. 
 
- 
								
- 
						We ask if the value for `State`(for each row) is found in the list, by using the`locate`function to return a nonzero value if the state is found in the list, as follows.`locate('New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire',{State}) and locate('Georgia, Alabama, South Carolina, Louisiana',{State})`
- 
						The `locate`function returns a number instead of a`TRUE`or`FALSE`, but`ifelse`requires the`TRUE`/`FALSE`Boolean value. To get around this, we can compare the result of`locate`to a number. If the state is in the list, the return value is greater than zero.- 
								Ask if the state is present. `locate('New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire',{State}) > 0`
- 
								If it's present the region, label it as the specific region, in this case a Northeast region. `/*The if expression:*/ locate('New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire',{State}) > 0, /*The then expression:*/ 'Northeast',`
 
- 
								
- 
						Because we have states that aren't in a list, and because `ifelse`requires a single`else`expression, we provide`'Other Region'`as the label for the leftover states.`/*The if expression:*/ locate('New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire',{State}) > 0, /*The then expression:*/ 'Northeast', /*The else expression:*/ 'Other Region'`
- 
						We wrap all that in the `ifelse( )`function to get the final version. The following example leaves out the Southeast region states that were in the original. You can add them back in place of the`<insert more regions here>`If you want to add more regions, you can construct more copies of those two lines and alter the list of states to suit your purpose. You can change the region name to something that suits you, and change the field name from `State`to anything that you need.`ifelse ( /*The if expression:*/ locate('New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire',{State}) > 0, /*The then expression:*/ 'Northeast', /*``<insert more regions here>`*/ /*The else expression:*/ 'Other Region' )###### NoteThere are other ways to do the initial comparison for the if expression. For example, suppose that you pose the question "What states are not missing from this list?" rather than "Which states are on the list?" If you do, you might phrase it differently. You might compare the locate statement to zero to find values that are missing from the list, and then use the NOT operator to classify them as "not missing," as follows. `/*The if expression:*/ NOT (locate('New York, New Jersey, Connecticut, Vermont, Maine, Rhode Island, New Hampshire',{State}) = 0),`Both versions are correct. The version that you choose should make the most sense to you and your team, so you can maintain it easily. If all the options seem equal, choose the simplest.