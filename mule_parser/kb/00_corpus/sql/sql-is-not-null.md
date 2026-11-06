# SQL IS NOT NULL

**Source:** [https://www.w3schools.com/sql/sql_ref_is_not_null.asp](https://www.w3schools.com/sql/sql_ref_is_not_null.asp)

---

# SQL IS NOT NULL Keyword

## IS NOT NULL

The `IS NOT NULL` command is used to test for 
non-empty values (NOT NULL values).

The following SQL lists all customers with a value in the "Address" field:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address 
  IS NOT NULL;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_is_not_null)

Ad