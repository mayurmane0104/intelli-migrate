# SQL OR

**Source:** [https://www.w3schools.com/sql/sql_ref_or.asp](https://www.w3schools.com/sql/sql_ref_or.asp)

---

# SQL OR Keyword

## OR

The `OR` command is used with WHERE to include 
rows where either condition is true.

The following SQL statement selects all fields from "Customers" where city is "Berlin" OR city is "München":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT * FROM Customers
  WHERE City='Berlin' OR City='München';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_where_or)

Ad