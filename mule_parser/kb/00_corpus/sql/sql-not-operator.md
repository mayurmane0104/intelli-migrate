# SQL NOT Operator

**Source:** [https://www.w3schools.com/sql/sql_not.asp](https://www.w3schools.com/sql/sql_not.asp)

---

# SQL NOT Operator

## The NOT Operator

The `NOT` operator is used in the `WHERE` 
clause to return all records that DO NOT match the specified criteria. It reverses the result of a condition from true to false and vice-versa. 

The following SQL selects all customers that are NOT from Spain:

### Example[Get your own SQL Server](/sql/sql_server.asp)

Select only the customers that are NOT from Spain:

```
 SELECT * FROM Customers
 WHERE NOT Country = 'Spain';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not)

In the example above, the `NOT` operator is used in combination with the
`=` operator.

The `NOT` operator is also used in combination with other operators to exclude data, such as:

-  `NOT LIKE`
-  `NOT BETWEEN`
-  `NOT IN`
-  `IS NOT NULL`
-  `NOT EXISTS`

## NOT Syntax

```
SELECT 
```
*column1*,* column2, ...*

FROM *table_name*

WHERE NOT *condition*;
 

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## The NOT LIKE Operator

The `NOT LIKE` operator is used in the `WHERE` clause to exclude rows that match a specified character pattern.

There are two wildcards often used in conjunction with the `NOT LIKE` operator:

- A percent sign `%`- represents zero, one, or multiple characters
- A underscore sign `_`- represents a single character

The following SQL selects all customers that do NOT start with the letter "A":

### Example

Select customers that does not start with the letter 'A':

```
 SELECT * FROM Customers
 WHERE CustomerName NOT LIKE 'A%';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not_like)

## The NOT BETWEEN Operator

The `NOT BETWEEN` operator is used in the `WHERE` clause to select rows where a value falls outside a specified inclusive range.

The `NOT BETWEEN` operator can be used with numeric, text, or date values.

The following SQL selects all customers with a CustomerID NOT between 10 and 60:

### Example

Select customers with a customerID not between 10 and 60:

```
 SELECT * FROM Customers
 WHERE CustomerID NOT BETWEEN 10 AND 60;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not_between2)

## The NOT IN Operator

The `NOT IN` operator is used in the `WHERE`
clause to exclude rows that match any value in a specified list or a subquery result set.

The following SQL selects all customers with City NOT IN "Paris" or "London":

### Example

Select customers that are not from Paris or London:

```
 SELECT * FROM Customers
 WHERE City NOT IN ('Paris', 'London');
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not_in)

## NOT Greater Than

In SQL, the "NOT Greater Than" condition is most often expressed with the standard greater than or equal to (>=) operator.

The following SQL selects all customers with a CustomerID not greater than 50:

### Example

Select customers with a CustomerId not greater than 50:

```
 SELECT * FROM Customers
 WHERE NOT CustomerID > 50;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not_gt)

## NOT Less Than

In SQL, the "NOT Less Than" condition is most often expressed with the standard less than or equal to (<=) operator.

The following SQL selects all customers with a CustomerID not less than 50:

### Example

Select customers with a CustomerID not less than 50:

```
 SELECT * FROM Customers
 WHERE NOT CustomerId < 50;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not_lt)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of the SQL `NOT` operator?

## Video: SQL NOT Operator

![SQL Tutorial on YouTube](images/yt_logo_rgb_dark.png) 

        ![SQL Tutorial on YouTube](images/img_sql_not.png)