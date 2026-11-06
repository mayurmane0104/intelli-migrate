# SQL Self Join

**Source:** [https://www.w3schools.com/sql/sql_join_self.asp](https://www.w3schools.com/sql/sql_join_self.asp)

---

# SQL Self Join

## SQL Self Join

A self join is a regular join, but the table is joined with itself.

### Self Join Syntax

```
SELECT 
FROM 
  WHERE 
```
*column_name(s)**table1 T1, table1 T2**condition*;
 *T1* and *T2* are different table aliases for the same table.

## Demo Database

Below is a selection from the "Customers" table:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 

Ad

## SQL Self Join Example

The following SQL statement matches customers that are from the same city:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT A.CustomerName AS CustomerName1, B.CustomerName AS CustomerName2, 
  A.City
FROM Customers A, Customers B
WHERE A.CustomerID <> B.CustomerID
  AND A.City = B.City 
ORDER BY A.City;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_join_self)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the purpose of a self join in SQL?