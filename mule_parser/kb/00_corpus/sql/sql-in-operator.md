# SQL IN Operator

**Source:** [https://www.w3schools.com/sql/sql_in.asp](https://www.w3schools.com/sql/sql_in.asp)

---

# SQL IN Operator

## The SQL IN Operator

The `IN` operator is used in the `WHERE` clause to check if a specified column's value matches
any value within a provided list.

The `IN` operator functions as a shorthand for multiple `OR` conditions, making queries shorter and more readable.

The following SQL uses the `IN` operator to select all customers from 
Germany, France, or UK:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT * FROM Customers
  WHERE Country IN ('Germany', 'France', 'UK');
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_in)

The following SQL uses multiple `OR` conditions to select all customers from 
Germany, France, or UK (same result, but longer code):

### Example

```
SELECT * FROM Customers
WHERE Country = 'Germany' OR Country = 'France' OR Country = 'UK';
 
```
## Syntax

```
SELECT 
```
*column_name(s)*

FROM *table_name*

WHERE *column_name* IN (*value1*,* value2*, ...);
 

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## The NOT IN Operator

By using the `NOT IN` operator,
you return all records that are NOT any of the values in the list.

### Example

Return all customers that are NOT from 'Germany', 'France', or 'UK':

```
 SELECT * FROM Customers
  WHERE Country NOT IN ('Germany', 'France', 'UK');
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_not_in2)

## IN (SELECT)

You can also use `IN` with a subquery in the `WHERE` clause.

With a subquery you can return all records from the main query that are present in the result of the subquery.

The following SQL returns all customers who also have an order in the "Orders" table:

### Example

```
SELECT * FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_in2)

## NOT IN (SELECT)

The result in the example above returned 74 records, that means that there are 17 customers that haven't placed any orders.

Let us check if that is correct, by using the `NOT IN` operator.

The following SQL returns all customers who do NOT have any orders in the "Orders" table:

### Example

```
SELECT * FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_in_not)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of the SQL `IN` operator?