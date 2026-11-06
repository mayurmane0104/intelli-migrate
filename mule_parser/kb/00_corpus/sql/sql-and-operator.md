# SQL AND Operator

**Source:** [https://www.w3schools.com/sql/sql_and.asp](https://www.w3schools.com/sql/sql_and.asp)

---

# SQL AND Operator

## The SQL AND Operator

The `WHERE` clause can contain one or many ```
AND
```
 operators.

The `AND` operator is used to filter records 
based on more than one condition.

**Note:** The `AND` operator displays a record if **all** the conditions are TRUE.

The following SQL selects all customers from Spain that starts with the letter 'G':

### Example[Get your own SQL Server](/sql/sql_server.asp)

Select all customers where Country is "Spain" AND CustomerName starts with the letter 'G':
```
 SELECT *
 FROM Customers
 WHERE Country = 'Spain' AND CustomerName LIKE 'G%';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_and)

## AND Syntax

```
SELECT 
```
*column1*,* column2, ...*

FROM *table_name*

WHERE *condition1* AND *condition2* AND *condition3 ...*; 

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## All Conditions Must Be True

The following SQL selects all customers where Country is "Brazil" AND City is "Rio de Janeiro" AND CustomerID is higher than 50:

### Example

```
  SELECT * FROM Customers
WHERE Country = 'Brazil'
AND City = 'Rio de 
  Janeiro'
AND CustomerID > 50;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_where_and_and)

## AND vs. OR

The `AND` operator displays a record if 
**all** the conditions are TRUE.

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

Without parenthesis, the SQL above will return all customers from Spain that starts with a "G", *plus*
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

True or False:

The `AND` operator is used to filter records based on more than one condition.

## Video: SQL AND Operator

![SQL Tutorial on YouTube](images/yt_logo_rgb_dark.png) 

        ![SQL Tutorial on YouTube](images/img_sql_and.png)