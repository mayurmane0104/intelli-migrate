# MySQL CAST() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_cast.asp](https://www.w3schools.com/sql/func_mysql_cast.asp)

---

# MySQL CAST() Function

Convert a value to a DATE datatype:

  SELECT 
  CAST("2017-08-29" AS DATE); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_cast)
 

## Definition and Usage

The CAST() function converts a value (of any type) into the specified datatype.

**Tip:** See also the [CONVERT()](func_mysql_convert.asp) 
function.

## Syntax

  CAST(*value* AS *datatype*)

## Parameter Values

    | Parameter | Description | 
  
  
    | *value* | Required. The value to convert | 
  
    | *datatype* | Required. The datatype to convert to. Can be one of the following: 
 
    | Value | Description |  
    | DATE | Converts *value*to DATE. Format: "YYYY-MM-DD" |  
    | DATETIME | Converts *value*to DATETIME. Format: "YYYY-MM-DD HH:MM:SS" |  
    | DECIMAL | Converts *value*to DECIMAL. Use the optional M and D parameters 
    to specify the maximum number of digits (M) and the number of digits 
    following the decimal point (D). |  
    | TIME | Converts *value*to TIME. Format: "HH:MM:SS" |  
    | CHAR | Converts *value*to CHAR (a fixed length string) |  
    | NCHAR | Converts *value*to NCHAR (like CHAR, but produces a string with 
    the national character set) |  
    | SIGNED | Converts *value*to SIGNED (a signed 64-bit integer) |  
    | UNSIGNED | Converts *value*to UNSIGNED (an unsigned 64-bit integer) |  
    | BINARY | Converts *value*to BINARY (a binary string) |  | 
  



## Technical Details


## More Examples

### Example

Convert a value to a CHAR datatype:

SELECT CAST(150 AS CHAR); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_cast2)
 
### Example

Convert a value to a TIME datatype:

SELECT CAST("14:06:10" AS TIME); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_cast3)
 
### Example

Convert a value to a SIGNED datatype:

SELECT CAST(5-10 AS SIGNED); 

[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_cast4)