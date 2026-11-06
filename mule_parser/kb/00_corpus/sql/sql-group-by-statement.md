# SQL GROUP BY Statement

**Source:** [https://www.w3schools.com/sql/sql_groupby.asp](https://www.w3schools.com/sql/sql_groupby.asp)

---

# SQL GROUP BY Statement

## The SQL GROUP BY Statement

The `GROUP BY` statement is used to group rows that have the same values into summary rows, like "Find the number of customers in each country".

The `GROUP BY` statement is almost always used in conjunction with aggregate functions, like `COUNT()`,
`MAX()`, `MIN()`, `SUM()`, `AVG()`,
to perform calculations on each group.

### GROUP BY Syntax

```
SELECT 
FROM 
WHERE 
GROUP BY 
ORDER BY 
```
*column1, aggregate_function(column2), column3, ...**table_name**condition**column1*, *column3**column_name*;
 ## Demo Database

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## SQL GROUP BY Examples

The following SQL returns the number of customers in each country:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT Country, COUNT(CustomerID) AS [Number of Customers]
FROM Customers
GROUP BY Country;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_groupby)

The following SQL returns the number of customers in each country, sorted from high to low:

### Example

```
  SELECT Country, COUNT(CustomerID) AS [Number of Customers]
  FROM Customers
  GROUP BY Country
  ORDER BY COUNT(CustomerID) DESC;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_groupby_orderby)

## Demo Database

Below is a selection from the "Orders" table in the Northwind sample database:

| OrderID | CustomerID | EmployeeID | OrderDate | ShipperID | 
|---|---|---|---|---|
| 10248 | 90 | 5 | 1996-07-04 | 3 | 
| 10249 | 81 | 6 | 1996-07-05 | 1 | 
| 10250 | 34 | 4 | 1996-07-08 | 2 | 

And a selection from the "Shippers" table:

| ShipperID | ShipperName | 
|---|---|
| 1 | Speedy Express | 
| 2 | United Package | 
| 3 | Federal Shipping | 

## GROUP BY With JOIN Example

The following SQL returns the number of orders sent by each shipper:

### Example

```
  SELECT Shippers.ShipperName, COUNT(Orders.OrderID) AS NumberOfOrders
FROM 
  Orders
LEFT JOIN Shippers
ON Orders.ShipperID = Shippers.ShipperID
  GROUP BY ShipperName;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_groupby1)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

Which aggregate functions are commonly used with the `GROUP BY` statement?