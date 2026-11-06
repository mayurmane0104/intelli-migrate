# SQL OR Operator

**Source:** [https://www.w3schools.com/sql/sql_or.asp](https://www.w3schools.com/sql/sql_or.asp)

---

# SQL OR Operator

## The SQL OR Operator

The `WHERE` clause can contain one or more `OR` operators.

The `OR` operator is used to filter records based on more than one condition.

**Note: **The `OR` operator displays a record if **any** of the conditions are TRUE.

The following SQL selects all customers from Germany OR Spain:

### Example[Get your own SQL Server](/sql/sql_server.asp)

Select all customers where Country is "Germany" OR "Spain":

```
 SELECT *
 FROM Customers
 WHERE Country = 'Germany' OR Country = 'Spain';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_or)

## OR Syntax

```
SELECT 
```
*column1*,* column2, ...*

FROM *table_name*

WHERE *condition1* OR *condition2* OR *condition3 ...*;
 

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## At Least One Condition Must Be True

The following SQL selects all customers where City is "Berlin", OR CustomerName starts with the letter "G", OR Country is "Norway":

### Example

```
 SELECT * FROM Customers
 WHERE City = 'Berlin'
 OR CustomerName LIKE 'G%'
 OR Country = 'Norway'; 
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_where_or_or)

## AND vs. OR

The `AND` operator displays a record if **all** the conditions are TRUE.

The `OR` operator displays a record if **any** of the conditions are TRUE.

## Combining AND and OR

You can also combine `AND` and `OR` operators.

The following SQL selects all customers from Spain that starts with a "G" or an "R" (make sure to use parenthesis to get the correct result):

### Example

Select all Spanish customers that starts with either "G" or "R":

```
 SELECT * FROM Customers
 WHERE Country = 'Spain'
 AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%'); 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_and_or)

Without parenthesis, the SQL above will return all customers from Spain that starts with a 
"G", *plus*
all customers that starts with an "R", regardless of the country value:

### Example

```
 SELECT * FROM Customers
 WHERE Country = 'Spain'
 AND CustomerName LIKE 'G%' OR CustomerName LIKE 'R%'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_and_or2)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of the SQL `OR` operator?