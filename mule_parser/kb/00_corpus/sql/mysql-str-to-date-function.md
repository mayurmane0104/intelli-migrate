# MySQL STR_TO_DATE() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_str_to_date.asp](https://www.w3schools.com/sql/func_mysql_str_to_date.asp)

---

# MySQL STR_TO_DATE() Function

Return a date based on a string and a format:

  SELECT 
  STR_TO_DATE("August 10 2017", "%M %d %Y"); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_str_to_date)
 

## Definition and Usage

The STR_TO_DATE() function returns a date based on a string and a format.

## Syntax

  STR_TO_DATE(*string*, *format*)

  
## Parameter Values

    | Parameter | Description | 
  
  
    | *string* | Required. The string to be formatted to a date | 
  
    | *format* | Required. The format to use. Can be one or a 
    combination of the following 
    values: 
 
    | Format | Description |  
    | %a | Abbreviated weekday name (Sun to Sat) |  
    | %b | Abbreviated month name (Jan to Dec) |  
    | %c | Numeric month name (0 to 12) |  
    | %D | Day of the month as a numeric value, followed by suffix (1st, 2nd, 3rd, 
    ...) |  
    | %d | Day of the month as a numeric value (01 to 31) |  
    | %e | Day of the month as a numeric value (0 to 31) |  
    | %f | Microseconds (000000 to 999999) |  
    | %H | Hour (00 to 23) |  
    | %h | Hour (00 to 12) |  
    | %I | Hour (00 to 12) |  
    | %i | Minutes (00 to 59) |  
    | %j | Day of the year (001 to 366) |  
    | %k | Hour (0 to 23) |  
    | %l | Hour (1 to 12) |  
    | %M | Month name in full (January to December) |  
    | %m | Month name as a numeric value (01 to 12) |  
    | %p | AM or PM |  
    | %r | Time in 12 hour AM or PM format (hh:mm:ss AM/PM) |  
    | %S | Seconds (00 to 59) |  
    | %s | Seconds (00 to 59) |  
    | %T | Time in 24 hour format (hh:mm:ss) |  
    | %U | Week where Sunday is the first day of the week (00 to 53) |  
    | %u | Week where Monday is the first day of the week (00 to 53) |  
    | %V | Week where Sunday is the first day of the week (01 to 53). Used with %X |  
    | %v | Week where Monday is the first day of the week (01 to 53). Used with %X |  
    | %W | Weekday name in full (Sunday to Saturday) |  
    | %w | Day of the week where Sunday=0 and Saturday=6 |  
    | %X | Year for the week where Sunday is the first day of the week. Used with 
    %V |  
    | %x | Year for the week where Monday is the first day of the week. Used with 
    %V |  
    | %Y | Year as a numeric, 4-digit value |  
    | %y | Year as a numeric, 2-digit value |  | 



## Technical Details


## More Examples

### Example

Return a date based on a string and a format:

  SELECT STR_TO_DATE("August,5,2017", "%M %e %Y"); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_str_to_date2)
 
### Example

Return a date based on a string and a format:

  SELECT STR_TO_DATE("Monday, August 14, 2017", "%W %M %e %Y"); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_str_to_date3)
 
### Example

Return a date based on a string and a format:

  SELECT STR_TO_DATE("2017,8,14 10,40,10", "%Y,%m,%d %h,%i,%s"); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_str_to_date4)