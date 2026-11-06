# SQL BETWEEN Operator

**Source:** [https://www.w3schools.com/sql/sql_between.asp](https://www.w3schools.com/sql/sql_between.asp)

---

# SQL BETWEEN Operator

## The SQL BETWEEN Operator

The `BETWEEN` operator is used in the `WHERE` clause to select values within a specified range.

The range is **inclusive** - the beginning and end values of the range are included in the results.

The values can be numbers, text, or dates.

### Example[Get your own SQL Server](/sql/sql_server.asp)

Select all products with a price between 10 and 20:

```
 SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_between)

## Syntax

```
SELECT 
```
*column_name(s)*

FROM *table_name*

WHERE *column_name *BETWEEN *value1* AND *value2;* 

## Demo Database

Below is a selection from the [ Products](trysql.asp?filename=trysql_products) table used in the examples:

| ProductID | ProductName | SupplierID | CategoryID | Unit | Price | 
|---|---|---|---|---|---|
| 1 | Chais | 1 | 1 | 10 boxes x 20 bags | 18.00 | 
| 2 | Chang | 1 | 1 | 24 - 12 oz bottles | 19.00 | 
| 3 | Aniseed Syrup | 1 | 2 | 12 - 550 ml bottles | 10.00 | 
| 4 | Chef Anton's Cajun Seasoning | 2 | 2 | 48 - 6 oz jars | 22.00 | 
| 5 | Chef Anton's Gumbo Mix | 2 | 2 | 36 boxes | 21.35 | 

## NOT BETWEEN

The `NOT BETWEEN` operator is used in the `WHERE` clause to select values outside a specified range.

The following SQL returns all products with a price NOT between 10 and 20:

## BETWEEN with IN

The following SQL returns all products with a price between 10 and 20. In addition, the CategoryID must be either 1, 2 or 3:

### Example

```
 SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID IN (1,2,3);
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_between_in)

## BETWEEN Text Values

The following SQL selects all products with a ProductName alphabetically between 'Geitost' and 'Louisiana Hot Spiced Okra':

### Example

```
 SELECT * FROM Products
 WHERE ProductName BETWEEN 'Geitost' AND 'Louisiana Hot Spiced Okra'
 ORDER BY ProductName;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_between_text)

## NOT BETWEEN Text Values

The following SQL selects all products with a ProductName NOT between 'Geitost' and 'Louisiana Hot Spiced Okra':

### Example

```
 SELECT * FROM Products
WHERE ProductName NOT BETWEEN 'Geitost' AND 
  'Louisiana Hot Spiced Okra'
ORDER BY ProductName;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not_between_text)

## BETWEEN Dates

The `BETWEEN` operator is useful for filtering records within a specific date or time period.
Ensure the date format matches the database (e.g. 'YYYY-MM-DD').

The following SQL selects all orders placed in July, 1996:

### Example

```
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
 
```
[Try it Yourself »](trymysql.asp?filename=trysql_select_between_date2)

## Sample Table

Below is a selection from the [ Orders](trysql.asp?filename=trysql_orders) table used in the example 
above:

| OrderID | CustomerID | EmployeeID | OrderDate | ShipperID | 
|---|---|---|---|---|
| 10248 | 90 | 5 | 1996-07-04 | 3 | 
| 10249 | 81 | 6 | 1996-07-05 | 1 | 
| 10250 | 34 | 4 | 1996-07-08 | 2 | 
| 10251 | 84 | 3 | 1996-07-08 | 1 | 
| 10252 | 76 | 4 | 1996-07-09 | 2 | 

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

Which SQL statement selects all products with a price between 10 and 20?