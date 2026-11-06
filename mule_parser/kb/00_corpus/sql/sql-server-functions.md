# SQL Server Functions

**Source:** [https://www.w3schools.com/sql/sql_ref_sqlserver.asp](https://www.w3schools.com/sql/sql_ref_sqlserver.asp)

---

# SQL Server Functions

SQL Server has many built-in functions.

This reference contains string, numeric, date, conversion, and some advanced functions in SQL Server.

## SQL Server String Functions

| Function | Description | 
|---|---|
| [ASCII](func_sqlserver_ascii.asp) | Returns the ASCII value for the specific character | 
| [CHAR](func_sqlserver_char.asp) | Returns the character based on the ASCII code | 
| [CHARINDEX](func_sqlserver_charindex.asp) | Returns the position of a substring in a string | 
| [CONCAT](func_sqlserver_concat.asp) | Adds two or more strings together | 
| [Concat with +](func_sqlserver_concat_with_plus.asp) | Adds two or more strings together | 
| [CONCAT_WS](func_sqlserver_concat_ws.asp) | Adds two or more strings together with a separator | 
| [DATALENGTH](func_sqlserver_datalength.asp) | Returns the number of bytes used to represent an expression | 
| [DIFFERENCE](func_sqlserver_difference.asp) | Compares two SOUNDEX values, and returns an integer value | 
| [FORMAT](func_sqlserver_format.asp) | Formats a value with the specified format | 
| [LEFT](func_sqlserver_left.asp) | Extracts a number of characters from a string (starting from left) | 
| [LEN](func_sqlserver_len.asp) | Returns the length of a string | 
| [LOWER](func_sqlserver_lower.asp) | Converts a string to lower-case | 
| [LTRIM](func_sqlserver_ltrim.asp) | Removes leading spaces from a string | 
| [NCHAR](func_sqlserver_nchar.asp) | Returns the Unicode character based on the number code | 
| [PATINDEX](func_sqlserver_patindex.asp) | Returns the position of a pattern in a string | 
| [QUOTENAME](func_sqlserver_quotename.asp) | Returns a Unicode string with delimiters added to make the string a valid SQL Server delimited identifier | 
| [REPLACE](func_sqlserver_replace.asp) | Replaces all occurrences of a substring within a string, with a new substring | 
| [REPLICATE](func_sqlserver_replicate.asp) | Repeats a string a specified number of times | 
| [REVERSE](func_sqlserver_reverse.asp) | Reverses a string and returns the result | 
| [RIGHT](func_sqlserver_right.asp) | Extracts a number of characters from a string (starting from right) | 
| [RTRIM](func_sqlserver_rtrim.asp) | Removes trailing spaces from a string | 
| [SOUNDEX](func_sqlserver_soundex.asp) | Returns a four-character code to evaluate the similarity of two strings | 
| [SPACE](func_sqlserver_space.asp) | Returns a string of the specified number of space characters | 
| [STR](func_sqlserver_str.asp) | Returns a number as string | 
| [STUFF](func_sqlserver_stuff.asp) | Deletes a part of a string and then inserts another part into the string, starting at a specified position | 
| [SUBSTRING](func_sqlserver_substring.asp) | Extracts some characters from a string | 
| [TRANSLATE](func_sqlserver_translate.asp) | Returns the string from the first argument after the characters specified in the second argument are translated into the characters specified in the third argument. | 
| [TRIM](func_sqlserver_trim.asp) | Removes leading and trailing spaces (or other specified characters) from a string | 
| [UNICODE](func_sqlserver_unicode.asp) | Returns the Unicode value for the first character of the input expression | 
| [UPPER](func_sqlserver_upper.asp) | Converts a string to upper-case | 

Ad

## SQL Server Math/Numeric Functions

| Function | Description | 
|---|---|
| [ABS](func_sqlserver_abs.asp) | Returns the absolute value of a number | 
| [ACOS](func_sqlserver_acos.asp) | Returns the arc cosine of a number | 
| [ASIN](func_sqlserver_asin.asp) | Returns the arc sine of a number | 
| [ATAN](func_sqlserver_atan.asp) | Returns the arc tangent of a number | 
| [ATN2](func_sqlserver_atn2.asp) | Returns the arc tangent of two numbers | 
| [AVG](func_sqlserver_avg.asp) | Returns the average value of an expression | 
| [CEILING](func_sqlserver_ceiling.asp) | Returns the smallest integer value that is >= a number | 
| [COUNT](func_sqlserver_count.asp) | Returns the number of records returned by a select query | 
| [COS](func_sqlserver_cos.asp) | Returns the cosine of a number | 
| [COT](func_sqlserver_cot.asp) | Returns the cotangent of a number | 
| [DEGREES](func_sqlserver_degrees.asp) | Converts a value in radians to degrees | 
| [EXP](func_sqlserver_exp.asp) | Returns e raised to the power of a specified number | 
| [FLOOR](func_sqlserver_floor.asp) | Returns the largest integer value that is <= to a number | 
| [LOG](func_sqlserver_log.asp) | Returns the natural logarithm of a number, or the logarithm of a number to a specified base | 
| [LOG10](func_sqlserver_log10.asp) | Returns the natural logarithm of a number to base 10 | 
| [MAX](func_sqlserver_max.asp) | Returns the maximum value in a set of values | 
| [MIN](func_sqlserver_min.asp) | Returns the minimum value in a set of values | 
| [PI](func_sqlserver_pi.asp) | Returns the value of PI | 
| [POWER](func_sqlserver_power.asp) | Returns the value of a number raised to the power of another number | 
| [RADIANS](func_sqlserver_radians.asp) | Converts a degree value into radians | 
| [RAND](func_sqlserver_rand.asp) | Returns a random number | 
| [ROUND](func_sqlserver_round.asp) | Rounds a number to a specified number of decimal places | 
| [SIGN](func_sqlserver_sign.asp) | Returns the sign of a number | 
| [SIN](func_sqlserver_sin.asp) | Returns the sine of a number | 
| [SQRT](func_sqlserver_sqrt.asp) | Returns the square root of a number | 
| [SQUARE](func_sqlserver_square.asp) | Returns the square of a number | 
| [SUM](func_sqlserver_sum.asp) | Calculates the sum of a set of values | 
| [TAN](func_sqlserver_tan.asp) | Returns the tangent of a number | 

## SQL Server Date Functions

| Function | Description | 
|---|---|
| [CURRENT_TIMESTAMP](func_sqlserver_current_timestamp.asp) | Returns the current date and time | 
| [DATEADD](func_sqlserver_dateadd.asp) | Adds a time/date interval to a date and then returns the date | 
| [DATEDIFF](func_sqlserver_datediff.asp) | Returns the difference between two dates | 
| [DATEFROMPARTS](func_sqlserver_datefromparts.asp) | Returns a date from the specified parts (year, month, and day values) | 
| [DATENAME](func_sqlserver_datename.asp) | Returns a specified part of a date (as string) | 
| [DATEPART](func_sqlserver_datepart.asp) | Returns a specified part of a date (as integer) | 
| [DAY](func_sqlserver_day.asp) | Returns the day of the month for a specified date | 
| [GETDATE](func_sqlserver_getdate.asp) | Returns the current database system date and time | 
| [GETUTCDATE](func_sqlserver_getutcdate.asp) | Returns the current database system UTC date and time | 
| [ISDATE](func_sqlserver_isdate.asp) | Checks an expression and returns 1 if it is a valid date, otherwise 0 | 
| [MONTH](func_sqlserver_month.asp) | Returns the month part for a specified date (a number from 1 to 12) | 
| [SYSDATETIME](func_sqlserver_sysdatetime.asp) | Returns the date and time of the SQL Server | 
| [YEAR](func_sqlserver_year.asp) | Returns the year part for a specified date | 

## SQL Server Advanced Functions

| Function | Description | 
|---|---|
| [CAST](func_sqlserver_cast.asp) | Converts a value (of any type) into a specified datatype | 
| [COALESCE](func_sqlserver_coalesce.asp) | Returns the first non-null value in a list | 
| [CONVERT](func_sqlserver_convert.asp) | Converts a value (of any type) into a specified datatype | 
| [CURRENT_USER](func_sqlserver_current_user.asp) | Returns the name of the current user in the SQL Server database | 
| [IIF](func_sqlserver_iif.asp) | Returns a value if a condition is TRUE, or another value if a condition is FALSE | 
| [ISNULL](func_sqlserver_isnull.asp) | Return a specified value if the expression is NULL, otherwise return the expression | 
| [ISNUMERIC](func_sqlserver_isnumeric.asp) | Tests whether an expression is numeric | 
| [NULLIF](func_sqlserver_nullif.asp) | Returns NULL if two expressions are equal | 
| [SESSION_USER](func_sqlserver_session_user.asp) | Returns the name of the current user in the SQL Server database | 
| [SESSIONPROPERTY](func_sqlserver_sessionproperty.asp) | Returns the session settings for a specified option | 
| [SYSTEM_USER](func_sqlserver_system_user.asp) | Returns the login name for the current user | 
| [USER_NAME](func_sqlserver_user_name.asp) | Returns the database user name based on the specified id |