# SQL UNION

**Source:** [https://www.w3schools.com/sql/sql_ref_union.asp](https://www.w3schools.com/sql/sql_ref_union.asp)

---

# SQL UNION Keyword

## UNION

The `UNION` command combines the result set of two or more SELECT statements (only 
distinct values)

The following SQL statement returns the cities (only distinct values) from both the "Customers" and the "Suppliers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT City FROM Customers
UNION
SELECT City FROM Suppliers
ORDER BY City;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_union)

Ad