# SQL WHERE Clause

**Source:** [https://www.w3schools.com/sql/sql_where.asp](https://www.w3schools.com/sql/sql_where.asp)

---

# SQL WHERE Clause

## The SQL WHERE Clause

The `WHERE` clause is used to filter records.

The `WHERE` clause is used to extract only those records that fulfill a specific 
condition.

### Example[Get your own SQL Server](/sql/sql_server.asp)

Here we select all customers from **Mexico**:

```
SELECT * FROM Customers
WHERE Country = 'Mexico'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_where)

## WHERE Syntax

```
SELECT 
```
*column1*,* column2, ...*

FROM *table_name*

WHERE *condition*;
 

**Note:** The `WHERE` clause is not only used in ```
SELECT
```
 statements, it is also used in `UPDATE`,
`DELETE`, etc.

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## Text Fields vs. Numeric Fields

SQL requires single quotes around text values (most database systems will also allow double quotes).

However, numeric fields should not be enclosed in quotes:

## Operators in The WHERE Clause

You can use other operators than the ```
=
```
 operator to filter the search.

### Example

Select all customers with a CustomerID greater than 80:

```
 SELECT * FROM Customers
 WHERE CustomerID > 80; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_where_gt)

The following operators can be used in the `WHERE` clause:

| Operator | Description | Example | 
|---|---|---|
| = | Equal | [Try it](trysql.asp?filename=trysql_op_equal_to) | 
| > | Greater than | [Try it](trysql.asp?filename=trysql_op_greater_than) | 
| < | Less than | [Try it](trysql.asp?filename=trysql_op_less_than) | 
| >= | Greater than or equal | [Try it](trysql.asp?filename=trysql_op_greater_than2) | 
| <= | Less than or equal | [Try it](trysql.asp?filename=trysql_op_less_than2) | 
| <> | Not equal. Note:In some versions of SQL this operator may be written as != | [Try it](trysql.asp?filename=trysql_op_not_equal_to) | 
| BETWEEN | Between a certain range | [Try it](trysql.asp?filename=trysql_op_between) | 
| LIKE | Search for a pattern | [Try it](trysql.asp?filename=trysql_op_like) | 
| IN | To specify multiple possible values for a column | [Try it](trysql.asp?filename=trysql_op_in) | 

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the purpose of the SQL `WHERE` clause?

## Video: SQL WHERE Clause

![SQL Tutorial on YouTube](images/yt_logo_rgb_dark.png) 

        ![SQL Tutorial on YouTube](images/img_sql_where.png)