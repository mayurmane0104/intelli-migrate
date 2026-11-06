# SQL UNION ALL

**Source:** [https://www.w3schools.com/sql/sql_ref_union_all.asp](https://www.w3schools.com/sql/sql_ref_union_all.asp)

---

# SQL UNION ALL Keyword

## UNION ALL

The `UNION ALL` command combines the result set of two or more SELECT statements (allows 
duplicate values).

The following SQL statement returns the cities (duplicate values also) from both the "Customers" and the "Suppliers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT City FROM Customers
UNION ALL
SELECT City FROM Suppliers
 ORDER BY City;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_union_all)

Ad