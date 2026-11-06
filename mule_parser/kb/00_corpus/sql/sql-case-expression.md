# SQL CASE Expression

**Source:** [https://www.w3schools.com/sql/sql_case.asp](https://www.w3schools.com/sql/sql_case.asp)

---

# SQL CASE Expression

## The SQL CASE Expression

The `CASE` expression is used to define 
different results based on specified conditions in an SQL statement.

The `CASE` expression goes through the conditions and 
stops at the first match (like an if-then-else statement). So, once a condition is true, it will stop 
processing and return the result. If no conditions are true, it returns 
the value in the `ELSE` clause. If there is no `ELSE` 
clause and no conditions are true, it returns NULL.

## CASE Syntax

```
CASE
  WHEN 
  WHEN 
  WHEN 
  ELSE 
END;
 
```
*condition1* THEN *result1**condition2* THEN *result2**conditionN* THEN *resultN**default_result*## SQL CASE Example

Here we use the `CASE` expression to 
categorize data (Price) and we create a new column (PriceCategory) that shows in 
which price category each product is:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT ProductName, Price,
  CASE
    WHEN Price < 20 THEN 'Low Cost'
    WHEN Price BETWEEN 20 AND 50 THEN 'Medium Cost'
    ELSE 'High Cost'
  END AS PriceCategory
  FROM Products;
 
```
[Try it Yourself »](trymysql.asp?filename=trysql_case)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the SQL `CASE` expression do?