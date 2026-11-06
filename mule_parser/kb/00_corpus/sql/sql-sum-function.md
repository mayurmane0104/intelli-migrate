# SQL SUM() Function

**Source:** [https://www.w3schools.com/sql/sql_sum.asp](https://www.w3schools.com/sql/sql_sum.asp)

---

# SQL SUM() Function

## The SQL SUM() Function

The `SUM()` function is used to calculate the total sum of values within a numeric column.

The `SUM()` function ignores NULL values in the column.

The following SQL returns the sum of the Quantity field in the "OrderDetails" table:

## SUM() Syntax

```
SELECT SUM(
```
*column_name*)

FROM *table_name*

WHERE *condition*; 

## Demo Database

Below is a selection from the [ OrderDetails](trysql.asp?filename=trysql_orderdetails) table used in the examples:

| OrderDetailID | OrderID | ProductID | Quantity | 
|---|---|---|---|
| 1 | 10248 | 11 | 12 | 
| 2 | 10248 | 42 | 10 | 
| 3 | 10248 | 72 | 5 | 
| 4 | 10249 | 14 | 9 | 
| 5 | 10249 | 51 | 40 | 

## Add a WHERE Clause

You can add a `WHERE` clause to specify conditions.

The following SQL returns the sum of the Quantity field for the product with ProductID = 11, in the "OrderDetails" table:

## Use an Alias

Give the summarized column a name by using the `AS` keyword.

## Use SUM() with GROUP BY

Here we use the `SUM()` function and the
`GROUP BY` clause, to return the Quantity
for EACH OrderID in the "OrderDetails" table:

### Example

```
  SELECT OrderID, SUM(Quantity) AS [Total Quantity]
FROM OrderDetails
  GROUP BY OrderID;  
```
[Try it Yourself »](trysql.asp?filename=trysql_select_sum_groupby)

You will learn more about the
[GROUP BY](sql_groupby.asp)

## SUM() With an Expression

The parameter inside the `SUM()` function can also be an expression.

If we assume that each product in the "OrderDetails" table costs 10 dollars, we can find the total earnings in dollars by multiply each quantity with 10:

### Example

Use an expression inside the `SUM()` function:

```
SELECT SUM(Quantity * 10)
FROM OrderDetails; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_sum2)

We can also join the "OrderDetails" table with the "Products" table to find the actual price, instead of assuming it is 10 dollars:

### Example

Join `OrderDetails` with 
`Products`, and use `SUM()` to find the total amount:

```
SELECT SUM(Price * Quantity)
FROM OrderDetails
LEFT JOIN Products ON OrderDetails.ProductID = Products.ProductID; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_sum3)

You will learn more about [Joins](sql_join.asp) later in this tutorial.

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the SQL `SUM()` function do?