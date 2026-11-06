# SQL SELECT DISTINCT Statement

**Source:** [https://www.w3schools.com/sql/sql_distinct.asp](https://www.w3schools.com/sql/sql_distinct.asp)

---

# SQL SELECT DISTINCT Statement

## The SQL SELECT DISTINCT Statement

The `SELECT DISTINCT` statement is used to return only distinct 
(unique) values.

In a table, a column may contain several duplicate values - and sometimes you want to list only the unique values.

### Example[Get your own SQL Server](/sql/sql_server.asp)

Select all the distinct (unique) countries from the "Customers" table:

```
SELECT DISTINCT Country FROM Customers;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_distinct)

## SELECT DISTINCT Syntax

```
 SELECT DISTINCT 
```
*column1*,* column2, ...*

 FROM *table_name*;
 

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## SELECT Example Without DISTINCT

If you omit the `DISTINCT` keyword, the SQL statement 
returns the "Country" value from all the records of the "Customers" table:

## Count Distinct Values

By using the  
`COUNT()` function with the
`DISTINCT` keyword, we can count the number of 
unique countries.

### Example

```
  SELECT COUNT(DISTINCT Country) FROM Customers;
 
```
**Note:** The COUNT(DISTINCT *column_name*) is not supported in Microsoft Access databases.

Here is a workaround for MS Access:

### Example

```
  SELECT Count(*) AS DistinctCountries
FROM (SELECT DISTINCT Country FROM Customers);
 
```
You will learn more about the 
`COUNT()` function later in this tutorial.

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

Which of the following SQL statements would return a list of all unique countries from a table named 'Customers'?

## Video: SQL SELECT DISTINCT Statement

![SQL Tutorial on YouTube](images/yt_logo_rgb_dark.png) 

        ![SQL Tutorial on YouTube](images/img_sql_select_distinct.png)