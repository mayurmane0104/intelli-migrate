# SQL ORDER BY Keyword

**Source:** [https://www.w3schools.com/sql/sql_orderby.asp](https://www.w3schools.com/sql/sql_orderby.asp)

---

# SQL ORDER BY Keyword

## The SQL ORDER BY

The `ORDER BY` keyword is used to sort the result-set in ascending or 
descending order.

The `ORDER BY` keyword sorts the result-set in ascending order 
(ASC) by default.

### Example[Get your own SQL Server](/sql/sql_server.asp)

Sort the products from lowest to highest price:

```
 SELECT * FROM Products
 ORDER BY Price;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_orderby_price)

## ORDER BY Syntax

```
SELECT 
```
*column1*,* column2, ...*

FROM *table_name*

ORDER BY *column1, column2, ... *ASC|DESC;
 

## Demo Database

Below is a selection from the [ Products](trysql.asp?filename=trysql_products) table used in the examples:

| ProductID | ProductName | SupplierID | CategoryID | Unit | Price | 
|---|---|---|---|---|---|
| 1 | Chais | 1 | 1 | 10 boxes x 20 bags | 18 | 
| 2 | Chang | 1 | 1 | 24 - 12 oz bottles | 19 | 
| 3 | Aniseed Syrup | 1 | 2 | 12 - 550 ml bottles | 10 | 
| 4 | Chef Anton's Cajun Seasoning | 2 | 2 | 48 - 6 oz jars | 22 | 
| 5 | Chef Anton's Gumbo Mix | 2 | 2 | 36 boxes | 21.35 | 

## ORDER BY DESC

 To sort the records in descending order, use the ```
DESC
```
 keyword.

### Example

Sort the products from highest to lowest price:

```
 SELECT * FROM Products
 ORDER BY Price DESC; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_orderby_price_desc)

## Order Alphabetically

For string values, the `ORDER BY` keyword will 
sort the values in the column alphabetically:

### Example

Sort the ProductName column in alphabetically order:

```
 SELECT * FROM Products
 ORDER BY ProductName; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_orderby_name)

## Alphabetically DESC

To sort the text values in a column in a descending order, use the `DESC` keyword:

### Example

Sort the ProductName column in descending alphabetically order:

```
 SELECT * FROM Products
 ORDER BY ProductName DESC; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_orderby_name_desc)

## ORDER BY Several Columns

The following SQL statement selects all customers from the "Customers" table - and sorts it by the "Country" and the "CustomerName" column.

This means that it sorts it first by Country, and if some records have the same Country, it sorts them by CustomerName:

## Combine ASC and DESC

The following SQL statement selects all customers from the "Customers" table, and sorts it ASCENDING by the "Country" and DESCENDING by the "CustomerName" column:

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the purpose of the SQL `ORDER BY` keyword?

## Video: SQL ORDER BY Keyword

![SQL Tutorial on YouTube](images/yt_logo_rgb_dark.png) 

        ![SQL Tutorial on YouTube](images/img_sql_order_by.png)