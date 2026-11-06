# SQL MIN() Function

**Source:** [https://www.w3schools.com/sql/sql_min_max.asp](https://www.w3schools.com/sql/sql_min_max.asp)

---

# SQL MIN() Function

## The SQL MIN() Function

The `MIN()` function returns the smallest value of the selected column.

The `MIN()` function works with numeric, string, and date data types.

### MIN() Example[Get your own SQL Server](/sql/sql_server.asp)

Return the lowest price in the Price column, in the "Products" table:

```
  SELECT MIN(Price)
FROM Products;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_min)

## MIN() Syntax

```
SELECT MIN(
```
*column_name*)

FROM *table_name*

WHERE *condition*; 

## Demo Database

Below is a selection from the [ Products](trysql.asp?filename=trysql_products) table used in the examples:

| ProductID | ProductName | SupplierID | CategoryID | Unit | Price | 
|---|---|---|---|---|---|
| 1 | Chais | 1 | 1 | 10 boxes x 20 bags | 18.00 | 
| 2 | Chang | 1 | 1 | 24 - 12 oz bottles | 19.00 | 
| 3 | Aniseed Syrup | 1 | 2 | 12 - 550 ml bottles | 10.00 | 
| 4 | Chef Anton's Cajun Seasoning | 2 | 2 | 48 - 6 oz jars | 22.00 | 
| 5 | Chef Anton's Gumbo Mix | 2 | 2 | 36 boxes | 21.35 | 

## Set Column Name (Alias)

When using `MIN()`, the returned column will not have a 
name.

Use the 
`AS` keyword to give the column a descriptive name:

## Use MIN() with Date Column

The following SQL returns the earliest BirthDate in the BirthDate column, in the [ Employees](trysql.asp?filename=trysql_employees) table:

## Use MIN() with GROUP BY

Here we use the `MIN()` function and the
`GROUP BY` clause, to return the smallest price 
for each category in the Products table:

### Example

```
  SELECT MIN(Price) AS SmallestPrice, CategoryID
FROM Products
GROUP BY CategoryID;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_min_groupby)

You will learn more about the
[GROUP BY](sql_groupby.asp)