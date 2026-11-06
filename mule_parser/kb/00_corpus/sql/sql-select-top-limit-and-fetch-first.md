# SQL SELECT TOP, LIMIT and FETCH FIRST

**Source:** [https://www.w3schools.com/sql/sql_top.asp](https://www.w3schools.com/sql/sql_top.asp)

---

# SQL SELECT TOP, LIMIT and FETCH FIRST

## The SQL SELECT TOP Clause

The `SELECT TOP` clause is used to limit the number of records to return.

The `SELECT TOP` clause is useful on large tables with thousands of 
records. Returning a large number of records can impact performance.

The following SQL selects only the first 3 records of the "Customers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

Select only the first 3 records of the Customers table:

```
 SELECT TOP 3 * FROM Customers;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_top)

**Note:** Not all database systems support the ```
SELECT TOP
```
 clause. MySQL 
supports the `LIMIT` clause to select a limited number of records, while Oracle uses ```
FETCH FIRST 
```
.*n* ROWS ONLY

### Syntax for SQL Server / MS Access

```
SELECT TOP 
```
*number*|*percent* *column_name(s)*

FROM *table_name*WHERE 

*condition*;

### Syntax for MySQL

```
SELECT 
```
*column_name(s)*

FROM *table_name*WHERE 

*condition*

LIMIT

*number*;

### Syntax for Oracle 12+

```
SELECT 
```
*column_name(s)*

FROM *table_name*ORDER BY 

*column_name(s)*

FETCH FIRST

*number*ROWS ONLY;

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## MySQL - The LIMIT Clause

The following SQL shows the equivalent example for MySQL:

### Example

Select the first 3 records of the Customers table:

```
 SELECT * FROM Customers
LIMIT 3; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_select_limit)

## Oracle - The FETCH FIRST Clause

The following SQL shows the equivalent example for Oracle:

### Example

Select the first 3 records of the Customers table:

```
SELECT * FROM Customers
FETCH FIRST 3 ROWS ONLY; 
```
## SQL TOP PERCENT Example

Here we will use the `SELECT TOP` clause with the percent syntax.

The following SQL selects the first 50% of the records from the "Customers" table (for SQL Server/MS Access):

The following SQL shows the equivalent example for Oracle:

### Example

```
SELECT * FROM Customers
FETCH FIRST 50 PERCENT ROWS ONLY;
 
```
## SELECT TOP with WHERE

The following SQL selects the first three records from the "Customers" table, where Country is "Germany" (for SQL Server/MS Access):

The following SQL shows the equivalent example for MySQL:

The following SQL shows the equivalent example for Oracle:

### Example

```
SELECT * FROM Customers
WHERE Country = 'Germany'
FETCH FIRST 3 ROWS ONLY;
 
```
## SELECT TOP and ORDER BY

Add the `ORDER BY` keyword when you want to sort the result, and return the first 3 records of the sorted result.

For SQL Server and MS Access:

### Example

Sort the result reverse alphabetically by CustomerName, and return the first 3 records:

```
SELECT TOP 3 * FROM Customers
ORDER BY CustomerName DESC;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_top_orderby)

The following SQL shows the equivalent example for MySQL:

The following SQL shows the equivalent example for Oracle:

### Example

```
SELECT * FROM Customers
ORDER BY CustomerName DESC
FETCH FIRST 3 ROWS ONLY;
 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What would the following query do in SQL Server?`SELECT TOP 5 * FROM Customers;`