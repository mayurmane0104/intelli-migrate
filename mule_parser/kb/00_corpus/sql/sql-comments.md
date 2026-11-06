# SQL Comments

**Source:** [https://www.w3schools.com/sql/sql_comments.asp](https://www.w3schools.com/sql/sql_comments.asp)

---

# SQL Comments

## SQL Comments

Comments are used to explain SQL code, or to temporarily prevent execution of SQL code (for debugging).

Comments are ignored by the database engine.

SQL supports single-line comments `--`, and multi-line comments ```
/* 
*/
```
.

**Note:** Comments are not supported in Microsoft Access databases.

## SQL Single-line Comments

Single-line comments start with `--` and 
continue to the end of line.

Any text after `--` and to the end of the line will be ignored.

The following example uses a single-line comment as an explanation:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
-- Selects all German 
  customers
SELECT * FROM Customers
WHERE Country = 'Germany';
 
```
[Try it Yourself »](trymysql.asp?filename=trysql_comment_single_1)

The following example uses a single-line comment to comment away the end of a line:

The following example uses a single-line comment to temporarily prevent execution of an SQL statement:

## SQL Multi-line Comments

Multi-line comments start with `/*` and end with 
`*/`.

Any text between `/*` and  
`*/` will be ignored.

The following example uses a multi-line comment as an explanation:

### Example

```
/* Selects all German customers
  from Berlin */
SELECT * FROM Customers
WHERE Country = 'Germany' AND City = 'Berlin';
 
```
[Try it Yourself »](trymysql.asp?filename=trysql_comment_multi_1)

The following example uses a multi-line comment to ignore many SQL statements:

### Example

```
/* SELECT * FROM Customers;
SELECT * FROM Products;
SELECT * FROM Orders;
SELECT * FROM Categories; */
SELECT * FROM Suppliers;
 
```
[Try it Yourself »](trymysql.asp?filename=trysql_comment_multi_2)

To ignore just a part of an SQL code, you can also use multi-line comment:

The following example uses a multi-line comment to ignore part of an SQL statement:

### Example

```
SELECT * FROM Customers WHERE (CustomerName LIKE 'L%'
OR CustomerName LIKE 'R%' /*OR CustomerName LIKE 'S%'
OR CustomerName LIKE 'T%'*/ OR CustomerName LIKE 'W%')
AND Country='USA'
ORDER BY CustomerName; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_comment_part_2)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of comments in SQL?