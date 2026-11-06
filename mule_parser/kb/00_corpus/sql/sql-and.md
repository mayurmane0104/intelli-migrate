# SQL AND

**Source:** [https://www.w3schools.com/sql/sql_ref_and.asp](https://www.w3schools.com/sql/sql_ref_and.asp)

---

# SQL AND Keyword

## AND

The `AND` command is used with WHERE to only include rows where both conditions is true.

The following SQL statement selects all fields from "Customers" where country is "Germany" AND city is "Berlin":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT * FROM Customers
 WHERE Country='Germany'
 AND City='Berlin';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_where_and)

Ad