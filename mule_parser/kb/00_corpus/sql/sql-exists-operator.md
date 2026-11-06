# SQL EXISTS Operator

**Source:** [https://www.w3schools.com/sql/sql_exists.asp](https://www.w3schools.com/sql/sql_exists.asp)

---

# SQL EXISTS Operator

## The SQL EXISTS Operator

The `EXISTS` operator is used in a `WHERE` clause
to check whether a subquery returns any rows.

The `EXISTS` operator evaluates to TRUE if the subquery returns at least one row, and FALSE otherwise.

### EXISTS Syntax

```
  SELECT 
  FROM 
  WHERE 
  EXISTS (
```
*column_name(s)**table_name**subquery*); ## Demo Database

Below is a selection from the "Products" table in the Northwind sample database:

| ProductID | ProductName | SupplierID | CategoryID | Unit | Price | 
|---|---|---|---|---|---|
| 1 | Chais | 1 | 1 | 10 boxes x 20 bags | 18.00 | 
| 2 | Chang | 1 | 1 | 24 - 12 oz bottles | 19.00 | 
| 3 | Aniseed Syrup | 1 | 2 | 12 - 550 ml bottles | 10.00 | 
| 4 | Chef Anton's Cajun Seasoning | 2 | 2 | 48 - 6 oz jars | 22.00 | 
| 5 | Chef Anton's Gumbo Mix | 2 | 2 | 36 boxes | 21.35 | 

And a selection from the "Suppliers" table:

| SupplierID | SupplierName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Exotic Liquid | Charlotte Cooper | 49 Gilbert St. | London | EC1 4SD | UK | 
| 2 | New Orleans Cajun Delights | Shelley Burke | P.O. Box 78934 | New Orleans | 70117 | USA | 
| 3 | Grandma Kelly's Homestead | Regina Murphy | 707 Oxford Rd. | Ann Arbor | 48104 | USA | 
| 4 | Tokyo Traders | Yoshi Nagase | 9-8 Sekimai Musashino-shi | Tokyo | 100 | Japan | 

## SQL EXISTS Examples

The following SQL checks if any suppliers has a product with a price lower than 10. If the subquery evaluates to TRUE; list the suppliers with a product price less than 10:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT SupplierName
FROM Suppliers
WHERE EXISTS (
  SELECT ProductName
  FROM 
  Products
  WHERE Products.SupplierID = Suppliers.supplierID AND Price < 
  10
); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_exists)

The following SQL checks if any suppliers has a product with a price equal to 22. If the subquery evaluates to TRUE; list the suppliers with a product price equal to 22:

### Example

```
  SELECT SupplierName
FROM Suppliers
WHERE EXISTS (
  SELECT ProductName
  FROM 
  Products
  WHERE Products.SupplierID = Suppliers.supplierID AND Price = 22
); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_exists2)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the SQL `EXISTS` operator do?