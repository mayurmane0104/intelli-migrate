# SQL Stored Procedures

**Source:** [https://www.w3schools.com/sql/sql_stored_procedures.asp](https://www.w3schools.com/sql/sql_stored_procedures.asp)

---

# SQL Stored Procedures

## What is a Stored Procedure?

A stored procedure is a precompiled SQL code that can be saved and reused.

If you have an SQL query that you write over and over again, save it as a stored procedure, and then just call it to execute it.

A stored procedure can also have parameters, so it can act based on the parameter value(s) that is passed.

## Key Benefits of Stored Procedures

Stored procedures are widely used in database management, and have the following benefits:

- Code Reusability - The same procedure can be called from various applications
- Improved Performance - Stored procedures are precompiled and runs faster
- Database Security - You can set users permission to run a specific procedure (limits direct access to tables)
- Easy Maintenance - When updating a procedure, it automatically updates all its use

## Stored Procedure Syntax (SQL Server)

To create a stored procedure, use the `CREATE PROCEDURE` statement:

```
CREATE PROCEDURE 
  
  
AS
BEGIN
  -- SQL_statements to be executed
  SELECT 
  FROM 
  WHERE 
END;
 
```
*procedure_name**@param1 datatype*,*@param2 datatype**column1*, *column2**table_name**columnN* = *@paramN*;
**Tip:** To see the syntax for MySQL database, look at 
[MySQL Stored Procedures](/mysql/mysql_stored_procedures.asp).

## Execute a Stored Procedure

To run a stored procedure, use the `EXEC` 
statement:

```
EXEC 
```
*procedure_name @param1* = *'value1'*, *@param2* = *'value2'*;
 ## Drop a Stored Procedure

To delete a stored procedure, use the `DROP PROCEDURE` statement:

```
  DROP PROCEDURE 
```
*procedure_name*; **Tip:** To ensure that `DROP PROCEDURE` does not 
return an error, if the procedure is missing, add the `IF EXISTS` clause:

```
  DROP PROCEDURE IF EXISTS 
```
*procedure_name*; ## Demo Database

Below is a selection from the "Customers" table in the Northwind sample database:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 

## Stored Procedure Example

The following SQL creates a stored procedure named "GetCustomersByCity" that can be used to select Customers from a particular City in the "Customers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  CREATE PROCEDURE 
  GetCustomersByCity
  @City nvarchar(50)
AS
BEGIN
  SELECT * FROM Customers
  WHERE 
  City = @City;
END; 
```
Here we execute the stored procedure by passing a city ('London') as a parameter, and the stored procedure returns the relevant details from the "Customers" table:

### Example

```
  EXEC 
  GetCustomersByCity @City = 'London'; 
```
## Stored Procedure With Multiple Parameters

Adding multiple parameters is easy. Just list each parameter and the data type separated by a comma as shown below.

The following SQL creates a stored procedure that selects Customers from a particular City with a particular PostalCode from the "Customers" table:

### Example

```
  CREATE PROCEDURE 
  GetCustomersByCity
  @City nvarchar(50),
  @PostalCode nvarchar(10)
AS
  BEGIN
  SELECT * FROM Customers
  WHERE 
  City = @City AND PostalCode = @PostalCode;
END; 
```
Execute the stored procedure above as follows:

### Example

```
  EXEC 
  GetCustomersByCity @City = 'London', @PostalCode = 'WA1 1DP'; 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of a stored procedure in SQL?