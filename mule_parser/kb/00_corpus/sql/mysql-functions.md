# MySQL Functions

**Source:** [https://www.w3schools.com/sql/sql_ref_mysql.asp](https://www.w3schools.com/sql/sql_ref_mysql.asp)

---

# MySQL Functions

MySQL has many built-in functions.

This reference contains string, numeric, date, and some advanced functions in MySQL.

## MySQL String Functions

| Function | Description | 
|---|---|
| [ASCII](func_mysql_ascii.asp) | Returns the ASCII value for the specific character | 
| [CHAR_LENGTH](func_mysql_char_length.asp) | Returns the length of a string (in characters) | 
| [CHARACTER_LENGTH](func_mysql_character_length.asp) | Returns the length of a string (in characters) | 
| [CONCAT](func_mysql_concat.asp) | Adds two or more expressions together | 
| [CONCAT_WS](func_mysql_concat_ws.asp) | Adds two or more expressions together with a separator | 
| [FIELD](func_mysql_field.asp) | Returns the index position of a value in a list of values | 
| [FIND_IN_SET](func_mysql_find_in_set.asp) | Returns the position of a string within a list of strings | 
| [FORMAT](func_mysql_format.asp) | Formats a number to a format like "#,###,###.##", rounded to a specified number of decimal places | 
| [INSERT](func_mysql_insert.asp) | Inserts a string within a string at the specified position and for a certain number of characters | 
| [INSTR](func_mysql_instr.asp) | Returns the position of the first occurrence of a string in another string | 
| [LCASE](func_mysql_lcase.asp) | Converts a string to lower-case | 
| [LEFT](func_mysql_left.asp) | Extracts a number of characters from a string (starting from left) | 
| [LENGTH](func_mysql_length.asp) | Returns the length of a string (in bytes) | 
| [LOCATE](func_mysql_locate.asp) | Returns the position of the first occurrence of a substring in a string | 
| [LOWER](func_mysql_lower.asp) | Converts a string to lower-case | 
| [LPAD](func_mysql_lpad.asp) | Left-pads a string with another string, to a certain length | 
| [LTRIM](func_mysql_ltrim.asp) | Removes leading spaces from a string | 
| [MID](func_mysql_mid.asp) | Extracts a substring from a string (starting at any position) | 
| [POSITION](func_mysql_position.asp) | Returns the position of the first occurrence of a substring in a string | 
| [REPEAT](func_mysql_repeat.asp) | Repeats a string as many times as specified | 
| [REPLACE](func_mysql_replace.asp) | Replaces all occurrences of a substring within a string, with a new substring | 
| [REVERSE](func_mysql_reverse.asp) | Reverses a string and returns the result | 
| [RIGHT](func_mysql_right.asp) | Extracts a number of characters from a string (starting from right) | 
| [RPAD](func_mysql_rpad.asp) | Right-pads a string with another string, to a certain length | 
| [RTRIM](func_mysql_rtrim.asp) | Removes trailing spaces from a string | 
| [SPACE](func_mysql_space.asp) | Returns a string of the specified number of space characters | 
| [STRCMP](func_mysql_strcmp.asp) | Compares two strings | 
| [SUBSTR](func_mysql_substr.asp) | Extracts a substring from a string (starting at any position) | 
| [SUBSTRING](func_mysql_substring.asp) | Extracts a substring from a string (starting at any position) | 
| [SUBSTRING_INDEX](func_mysql_substring_index.asp) | Returns a substring of a string before a specified number of delimiter occurs | 
| [TRIM](func_mysql_trim.asp) | Removes leading and trailing spaces from a string | 
| [UCASE](func_mysql_ucase.asp) | Converts a string to upper-case | 
| [UPPER](func_mysql_upper.asp) | Converts a string to upper-case | 

## MySQL Numeric Functions

| Function | Description | 
|---|---|
| [ABS](func_mysql_abs.asp) | Returns the absolute value of a number | 
| [ACOS](func_mysql_acos.asp) | Returns the arc cosine of a number | 
| [ASIN](func_mysql_asin.asp) | Returns the arc sine of a number | 
| [ATAN](func_mysql_atan.asp) | Returns the arc tangent of one or two numbers | 
| [ATAN2](func_mysql_atan2.asp) | Returns the arc tangent of two numbers | 
| [AVG](func_mysql_avg.asp) | Returns the average value of an expression | 
| [CEIL](func_mysql_ceil.asp) | Returns the smallest integer value that is >= to a number | 
| [CEILING](func_mysql_ceiling.asp) | Returns the smallest integer value that is >= to a number | 
| [COS](func_mysql_cos.asp) | Returns the cosine of a number | 
| [COT](func_mysql_cot.asp) | Returns the cotangent of a number | 
| [COUNT](func_mysql_count.asp) | Returns the number of records returned by a select query | 
| [DEGREES](func_mysql_degrees.asp) | Converts a value in radians to degrees | 
| [DIV](func_mysql_div.asp) | Used for integer division | 
| [EXP](func_mysql_exp.asp) | Returns e raised to the power of a specified number | 
| [FLOOR](func_mysql_floor.asp) | Returns the largest integer value that is <= to a number | 
| [GREATEST](func_mysql_greatest.asp) | Returns the greatest value of the list of arguments | 
| [LEAST](func_mysql_least.asp) | Returns the smallest value of the list of arguments | 
| [LN](func_mysql_ln.asp) | Returns the natural logarithm of a number | 
| [LOG](func_mysql_log.asp) | Returns the natural logarithm of a number, or the logarithm of a number to a specified base | 
| [LOG10](func_mysql_log10.asp) | Returns the natural logarithm of a number to base 10 | 
| [LOG2](func_mysql_log2.asp) | Returns the natural logarithm of a number to base 2 | 
| [MAX](func_mysql_max.asp) | Returns the maximum value in a set of values | 
| [MIN](func_mysql_min.asp) | Returns the minimum value in a set of values | 
| [MOD](func_mysql_mod.asp) | Returns the remainder of a number divided by another number | 
| [PI](func_mysql_pi.asp) | Returns the value of PI | 
| [POW](func_mysql_pow.asp) | Returns the value of a number raised to the power of another number | 
| [POWER](func_mysql_power.asp) | Returns the value of a number raised to the power of another number | 
| [RADIANS](func_mysql_radians.asp) | Converts a degree value into radians | 
| [RAND](func_mysql_rand.asp) | Returns a random number | 
| [ROUND](func_mysql_round.asp) | Rounds a number to a specified number of decimal places | 
| [SIGN](func_mysql_sign.asp) | Returns the sign of a number | 
| [SIN](func_mysql_sin.asp) | Returns the sine of a number | 
| [SQRT](func_mysql_sqrt.asp) | Returns the square root of a number | 
| [SUM](func_mysql_sum.asp) | Calculates the sum of a set of values | 
| [TAN](func_mysql_tan.asp) | Returns the tangent of a number | 
| [TRUNCATE](func_mysql_truncate.asp) | Truncates a number to the specified number of decimal places | 

## MySQL Date Functions

| Function | Description | 
|---|---|
| [ADDDATE](func_mysql_adddate.asp) | Adds a time/date interval to a date and then returns the date | 
| [ADDTIME](func_mysql_addtime.asp) | Adds a time interval to a time/datetime and then returns the time/datetime | 
| [CURDATE](func_mysql_curdate.asp) | Returns the current date | 
| [CURRENT_DATE](func_mysql_current_date.asp) | Returns the current date | 
| [CURRENT_TIME](func_mysql_current_time.asp) | Returns the current time | 
| [CURRENT_TIMESTAMP](func_mysql_current_timestamp.asp) | Returns the current date and time | 
| [CURTIME](func_mysql_curtime.asp) | Returns the current time | 
| [DATE](func_mysql_date.asp) | Extracts the date part from a datetime expression | 
| [DATEDIFF](func_mysql_datediff.asp) | Returns the number of days between two date values | 
| [DATE_ADD](func_mysql_date_add.asp) | Adds a time/date interval to a date and then returns the date | 
| [DATE_FORMAT](func_mysql_date_format.asp) | Formats a date | 
| [DATE_SUB](func_mysql_date_sub.asp) | Subtracts a time/date interval from a date and then returns the date | 
| [DAY](func_mysql_day.asp) | Returns the day of the month for a given date | 
| [DAYNAME](func_mysql_dayname.asp) | Returns the weekday name for a given date | 
| [DAYOFMONTH](func_mysql_dayofmonth.asp) | Returns the day of the month for a given date | 
| [DAYOFWEEK](func_mysql_dayofweek.asp) | Returns the weekday index for a given date | 
| [DAYOFYEAR](func_mysql_dayofyear.asp) | Returns the day of the year for a given date | 
| [EXTRACT](func_mysql_extract.asp) | Extracts a part from a given date | 
| [FROM_DAYS](func_mysql_from_days.asp) | Returns a date from a numeric datevalue | 
| [HOUR](func_mysql_hour.asp) | Returns the hour part for a given date | 
| [LAST_DAY](func_mysql_last_day.asp) | Extracts the last day of the month for a given date | 
| [LOCALTIME](func_mysql_localtime.asp) | Returns the current date and time | 
| [LOCALTIMESTAMP](func_mysql_localtimestamp.asp) | Returns the current date and time | 
| [MAKEDATE](func_mysql_makedate.asp) | Creates and returns a date based on a year and a number of days value | 
| [MAKETIME](func_mysql_maketime.asp) | Creates and returns a time based on an hour, minute, and second value | 
| [MICROSECOND](func_mysql_microsecond.asp) | Returns the microsecond part of a time/datetime | 
| [MINUTE](func_mysql_minute.asp) | Returns the minute part of a time/datetime | 
| [MONTH](func_mysql_month.asp) | Returns the month part for a given date | 
| [MONTHNAME](func_mysql_monthname.asp) | Returns the name of the month for a given date | 
| [NOW](func_mysql_now.asp) | Returns the current date and time | 
| [PERIOD_ADD](func_mysql_period_add.asp) | Adds a specified number of months to a period | 
| [PERIOD_DIFF](func_mysql_period_diff.asp) | Returns the difference between two periods | 
| [QUARTER](func_mysql_quarter.asp) | Returns the quarter of the year for a given date value | 
| [SECOND](func_mysql_second.asp) | Returns the seconds part of a time/datetime | 
| [SEC_TO_TIME](func_mysql_sec_to_time.asp) | Returns a time value based on the specified seconds | 
| [STR_TO_DATE](func_mysql_str_to_date.asp) | Returns a date based on a string and a format | 
| [SUBDATE](func_mysql_subdate.asp) | Subtracts a time/date interval from a date and then returns the date | 
| [SUBTIME](func_mysql_subtime.asp) | Subtracts a time interval from a datetime and then returns the time/datetime | 
| [SYSDATE](func_mysql_sysdate.asp) | Returns the current date and time | 
| [TIME](func_mysql_time.asp) | Extracts the time part from a given time/datetime | 
| [TIME_FORMAT](func_mysql_time_format.asp) | Formats a time by a specified format | 
| [TIME_TO_SEC](func_mysql_time_to_sec.asp) | Converts a time value into seconds | 
| [TIMEDIFF](func_mysql_timediff.asp) | Returns the difference between two time/datetime expressions | 
| [TIMESTAMP](func_mysql_timestamp.asp) | Returns a datetime value based on a date or datetime value | 
| [TO_DAYS](func_mysql_to_days.asp) | Returns the number of days between a date and date "0000-00-00" | 
| [WEEK](func_mysql_week.asp) | Returns the week number for a given date | 
| [WEEKDAY](func_mysql_weekday.asp) | Returns the weekday number for a given date | 
| [WEEKOFYEAR](func_mysql_weekofyear.asp) | Returns the week number for a given date | 
| [YEAR](func_mysql_year.asp) | Returns the year part for a given date | 
| [YEARWEEK](func_mysql_yearweek.asp) | Returns the year and week number for a given date | 

## MySQL Advanced Functions

| Function | Description | 
|---|---|
| [BIN](func_mysql_bin.asp) | Returns a binary representation of a number | 
| [BINARY](func_mysql_binary.asp) | Converts a value to a binary string | 
| [CASE](func_mysql_case.asp) | Goes through conditions and return a value when the first condition is met | 
| [CAST](func_mysql_cast.asp) | Converts a value (of any type) into a specified datatype | 
| [COALESCE](func_mysql_coalesce.asp) | Returns the first non-null value in a list | 
| [CONNECTION_ID](func_mysql_connection_id.asp) | Returns the unique connection ID for the current connection | 
| [CONV](func_mysql_conv.asp) | Converts a number from one numeric base system to another | 
| [CONVERT](func_mysql_convert.asp) | Converts a value into the specified datatype or character set | 
| [CURRENT_USER](func_mysql_current_user.asp) | Returns the user name and host name for the MySQL account that the server used to authenticate the current client | 
| [DATABASE](func_mysql_database.asp) | Returns the name of the current database | 
| [IF](func_mysql_if.asp) | Returns a value if a condition is TRUE, or another value if a condition is FALSE | 
| [IFNULL](func_mysql_ifnull.asp) | Return a specified value if the expression is NULL, otherwise return the expression | 
| [ISNULL](func_mysql_isnull.asp) | Returns 1 or 0 depending on whether an expression is NULL | 
| [LAST_INSERT_ID](func_mysql_last_insert_id.asp) | Returns the AUTO_INCREMENT id of the last row that has been inserted in a table | 
| [NULLIF](func_mysql_nullif.asp) | Compares two expressions and returns NULL if they are equal. Otherwise, the first expression is returned | 
| [SESSION_USER](func_mysql_session_user.asp) | Returns the current MySQL user name and host name | 
| [SYSTEM_USER](func_mysql_system_user.asp) | Returns the current MySQL user name and host name | 
| [USER](func_mysql_user.asp) | Returns the current MySQL user name and host name | 
| [VERSION](func_mysql_version.asp) | Returns the current version of the MySQL database |