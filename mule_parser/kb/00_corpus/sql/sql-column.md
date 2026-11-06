# SQL COLUMN

**Source:** [https://www.w3schools.com/sql/sql_ref_column.asp](https://www.w3schools.com/sql/sql_ref_column.asp)

---

# SQL COLUMN Keyword

## ALTER COLUMN

The `ALTER COLUMN` command is used to change the data type of a column in a table.

The following SQL changes the data type of the column named "BirthDate" in the "Employees" table to type year:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  ALTER TABLE Employees
ALTER COLUMN BirthDate 
  year;
 
```
## DROP COLUMN

The `DROP COLUMN` command is used to delete a column in an 
existing table.

The following SQL deletes the "ContactName" column from the "Customers" table:

### Example

```
  ALTER TABLE Customers
DROP COLUMN ContactName;
 
```
Ad