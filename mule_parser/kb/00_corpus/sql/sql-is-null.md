# SQL IS NULL

**Source:** [https://www.w3schools.com/sql/sql_ref_is_null.asp](https://www.w3schools.com/sql/sql_ref_is_null.asp)

---

# SQL IS NULL Keyword

## IS NULL

The `IS NULL` command is used to test for 
empty values (NULL values).

The following SQL lists all customers with a NULL value in the "Address" field:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address 
  IS NULL;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_is_null)

**Note:** A NULL value is 
different from a zero value or a field that contains spaces. A field with a NULL 
value is one that has been left blank during record creation!

**Tip:** Always use IS NULL to look for NULL values.

Ad