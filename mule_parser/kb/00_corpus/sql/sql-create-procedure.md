# SQL CREATE PROCEDURE

**Source:** [https://www.w3schools.com/sql/sql_ref_create_procedure.asp](https://www.w3schools.com/sql/sql_ref_create_procedure.asp)

---

# SQL CREATE PROCEDURE Keyword

## CREATE PROCEDURE

The `CREATE PROCEDURE` command is used to 
create a stored procedure.

A stored procedure is a prepared SQL code that you can save, so the code can be reused over and over again.

The following SQL creates a stored procedure named "SelectAllCustomers" that selects all records from the "Customers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;
 
```
Execute the stored procedure above as follows:

### Example

```
  EXEC SelectAllCustomers;
 
```
Ad