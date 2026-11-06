# SQL NOT

**Source:** [https://www.w3schools.com/sql/sql_ref_not.asp](https://www.w3schools.com/sql/sql_ref_not.asp)

---

# SQL NOT Keyword

## NOT

The `NOT` command is used with WHERE to only 
include rows where a condition is not true.

The following SQL statement selects all fields from "Customers" where country is NOT "Germany":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT * FROM Customers
 WHERE 
  NOT Country='Germany';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_where_not)

Ad