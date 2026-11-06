# SQL INSERT INTO SELECT Statement

**Source:** [https://www.w3schools.com/sql/sql_insert_into_select.asp](https://www.w3schools.com/sql/sql_insert_into_select.asp)

---

# SQL INSERT INTO SELECT Statement

## The SQL INSERT INTO SELECT Statement

The `INSERT INTO SELECT` statement is used to copy data from 
an existing table and 
insert it into another existing table.

The `INSERT INTO SELECT` statement requires that 
the data types in source and target tables match.

**Note:** The existing records in the target table are unaffected.

### INSERT INTO SELECT Syntax

Copy all columns from one table to another table:

```
INSERT INTO 
SELECT * FROM 
WHERE 
```
*target_table**source_table**condition*;
 **Note:** If you omit the column names, the number and order of 
columns in the source and target tables must be exactly the same!

Copy only some columns from one table to another table:

```
INSERT INTO 
SELECT 
FROM 
WHERE 
```
*target_table *(*column1*, *column2*, *column3*, ...)*column1*, *column2*, *column3*, ...*source_table**condition*;
 ## Demo Database

Below is a selection from the "Customers" table:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 

And a selection from the "Suppliers" table:

| SupplierID | SupplierName | ContactName | Address | City | Postal Code | Country | 
|---|---|---|---|---|---|---|
| 1 | Exotic Liquid | Charlotte Cooper | 49 Gilbert St. | Londona | EC1 4SD | UK | 
| 2 | New Orleans Cajun Delights | Shelley Burke | P.O. Box 78934 | New Orleans | 70117 | USA | 
| 3 | Grandma Kelly's Homestead | Regina Murphy | 707 Oxford Rd. | Ann Arbor | 48104 | USA | 

## SQL INSERT INTO SELECT Examples

### Example[Get your own SQL Server](/sql/sql_server.asp)

Copy "Suppliers" into "Customers" (the columns that are not filled with data, will contain NULL):

```
 INSERT INTO Customers (CustomerName, 
  City, Country)
 SELECT SupplierName, City, Country FROM Suppliers;
 
```
### Example

Copy "Suppliers" into "Customers" (copy all columns):

```
  INSERT INTO Customers
SELECT * FROM Suppliers;
 
```
### Example

Copy only the German suppliers into "Customers":

```
 INSERT INTO Customers (CustomerName, 
  City, Country)
 SELECT SupplierName, City, Country FROM Suppliers
WHERE Country='Germany';
 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the purpose of the SQL `INSERT INTO SELECT` statement?