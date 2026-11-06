# SQL INSERT INTO SELECT

**Source:** [https://www.w3schools.com/sql/sql_ref_insert_into_select.asp](https://www.w3schools.com/sql/sql_ref_insert_into_select.asp)

---

# SQL INSERT INTO SELECT Keyword

## INSERT INTO SELECT

The `INSERT INTO SELECT` command copies data 
from one table and inserts it into another table.

The following SQL copies "Suppliers" into "Customers" (the columns that are not filled with data, will contain NULL):

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 INSERT INTO Customers (CustomerName, 
  City, Country)
 SELECT SupplierName, City, Country FROM Suppliers;
 
```
The following SQL copies "Suppliers" into "Customers" (fill all columns):

### Example

```
  INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, 
  Country)
SELECT SupplierName, ContactName, Address, City, PostalCode, 
  Country FROM Suppliers;
 
```
The following SQL copies only the German suppliers into "Customers":

### Example

```
 INSERT INTO Customers (CustomerName, 
  City, Country)
 SELECT SupplierName, City, Country FROM Suppliers
WHERE Country='Germany';
 
```
Ad