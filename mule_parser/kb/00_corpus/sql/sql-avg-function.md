# SQL AVG() Function

**Source:** [https://www.w3schools.com/sql/sql_avg.asp](https://www.w3schools.com/sql/sql_avg.asp)

---

# SQL AVG() Function

## The SQL AVG() Function

The `AVG()` function returns the average value of a numeric column.

The `AVG()` function ignores NULL values in the column.

### Example[Get your own SQL Server](/sql/sql_server.asp)

Find the average price of all products:

```
  SELECT AVG(Price)
FROM Products;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_avg)

**Note:** NULL values are ignored.

## AVG() Syntax

```
  SELECT AVG(
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

## Add a WHERE Clause

You can add a `WHERE` clause to specify conditions:

### Example

Return the average price of products in category 1:

```
  SELECT AVG(Price)
FROM Products
WHERE CategoryID = 1;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_avg_where)

## Use an Alias

Give the AVG column a name by using the `AS` keyword.

### Example

Name the column "average price":

```
SELECT AVG(Price) AS [average price]
FROM Products;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_avg_as)

## Higher Than Average

To list all records with a higher price than average, we can use the
`AVG()` function in a sub query:

### Example

Return all products with a higher price than the average price:

```
  SELECT * FROM Products
WHERE Price > 
  (SELECT AVG(Price) FROM Products); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_avg2)

## Use AVG() with GROUP BY

Here we use the `AVG()` function and the
`GROUP BY` clause, to return the average price 
for EACH category in the "Products" table:

### Example

```
  SELECT AVG(Price) AS AveragePrice, CategoryID
FROM Products
GROUP BY CategoryID;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_avg_groupby)

You will learn more about the
[GROUP BY](sql_groupby.asp)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the SQL `AVG()` function do?