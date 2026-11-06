# SQL AS

**Source:** [https://www.w3schools.com/sql/sql_ref_as.asp](https://www.w3schools.com/sql/sql_ref_as.asp)

---

# SQL AS Keyword

## AS

The `AS` command is used to rename a column or table with an alias.

An alias only exists for the duration of the query.

## Alias for Columns

The following SQL statement creates two aliases, one for the CustomerID column and one for the CustomerName column:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT CustomerID AS ID, CustomerName AS Customer
 FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_column0)

The following SQL statement creates two aliases. Notice that it requires double quotation marks or square brackets if the alias name contains spaces:

### Example

```
 SELECT CustomerName AS Customer, ContactName AS [Contact Person]
 FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_column)

The following SQL statement creates an alias named "Address" that combine four columns (Address, PostalCode, City and Country):

### Example

```
  SELECT CustomerName, Address + ', ' + PostalCode + ' ' + City + ', ' + Country 
  AS Address
 FROM Customers; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_column2)

**Note:** To get the SQL statement above to work in MySQL use the following:

```
SELECT CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers; 
```
## Alias for Tables

The following SQL statement selects all the orders from the customer with CustomerID=4 (Around the Horn). We use the "Customers" and "Orders" tables, and give them the table aliases of "c" and "o" respectively (Here we use aliases to make the SQL shorter):

### Example

```
 SELECT o.OrderID, o.OrderDate, c.CustomerName
FROM Customers AS c, Orders AS o
WHERE c.CustomerName="Around the Horn" AND c.CustomerID=o.CustomerID;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_alias_table)