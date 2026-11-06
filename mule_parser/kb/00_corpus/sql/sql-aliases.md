# SQL Aliases

**Source:** [https://www.w3schools.com/sql/sql_alias.asp](https://www.w3schools.com/sql/sql_alias.asp)

---

# SQL Aliases

## SQL Aliases

An alias is created with the `AS` keyword, and 
is often used to make a column name more readable.

An alias only exists for the duration of that query.

## Alias for Columns

The following SQL creates two aliases, one for the CustomerID column and one for the CustomerName column:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT CustomerID AS ID, CustomerName AS Customer
 FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_column0)

## Syntax

Alias for column:

```
 SELECT 
```
*column_name* AS *alias_name*

 FROM *table_name;* 

Alias for table:

```
 SELECT 
```
*column_name(s)*

 FROM *table_name *AS *alias_name;*
 

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## Aliases with Spaces

If you want your alias to contain one or more spaces, like "My Great Products", surround the aliasname with square brackets or double quotes:

### Example

Using [square brackets] for aliases with space characters:

```
 SELECT ProductName AS [My Great Products]
 FROM Products; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_brackets)

OR:

### Example

Using "double quotes" for aliases with space characters:

```
 SELECT ProductName AS "My Great Products"
 FROM Products; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_quotes)

**Note:** Some database systems allows both [] and "", and some only allows one of them.

## Concatenate Columns

The following SQL creates an alias named "Address" that combine four columns (Address, PostalCode, City and Country):

### Example

```
  SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country 
  AS Address
 FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_column2)

**Note:** To get the SQL statement above to work in MySQL use the following:

### MySQL Example

```
SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers; 
```
[Try it Yourself »](trymysql.asp?filename=trysql_select_alias_mysql_concat)

**Note:** To get the SQL statement above to work in Oracle use the following:

### Oracle Example

```
  SELECT CustomerName, (Address || ', ' || PostalCode || ' ' || City || ', ' || 
  Country) AS Address
FROM Customers; 
```
## Alias for Tables

The same rules applies when you want to use an alias for a table.

### Example

Refer to the Customers table as Persons instead:

```
 SELECT * FROM Customers AS Persons;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_table_persons)

It might seem useless to use aliases on tables, but when you are joining tables, it makes sense.

In the following example, c is the alias for customers and o is for orders, making the query shorter and easier to read:

### Example

```
SELECT c.CustomerName, o.OrderID
FROM customers AS c
JOIN orders AS o ON c.customerID = o.customerID;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_table)

You will learn more about [SQL Joins](sql_join.asp) in the next chapters.

Aliases are useful when:

- There are more than one table involved in a query
- Functions are used in the query
- Column names are long or not very readable
- Two or more columns are combined together

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

Which SQL statement creates an alias for the CustomerID column as 'ID'?