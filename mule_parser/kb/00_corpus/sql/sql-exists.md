# SQL EXISTS

**Source:** [https://www.w3schools.com/sql/sql_ref_exists.asp](https://www.w3schools.com/sql/sql_ref_exists.asp)

---

# SQL EXISTS Keyword

## EXISTS

The `EXISTS` command tests for the existence of any record in a subquery, 
and returns true if the subquery returns one or more records.

The following SQL lists the suppliers with a product price less than 20:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM 
  Products WHERE SupplierId = Suppliers.supplierId AND Price < 20); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_exists)

The following SQL lists the suppliers with a product price equal to 22:

### Example

```
  SELECT SupplierName
FROM Suppliers
WHERE EXISTS (SELECT ProductName FROM 
  Products WHERE SupplierId = Suppliers.supplierId AND Price = 22); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_exists2)

Ad