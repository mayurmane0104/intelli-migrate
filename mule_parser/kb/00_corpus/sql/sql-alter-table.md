# SQL ALTER TABLE

**Source:** [https://www.w3schools.com/sql/sql_ref_alter_table.asp](https://www.w3schools.com/sql/sql_ref_alter_table.asp)

---

# SQL ALTER TABLE Keyword

## ALTER TABLE

The `ALTER TABLE` command adds, deletes, or 
modifies columns in a table.

The `ALTER TABLE` command also adds and 
deletes various constraints in a table.

The following SQL adds an "Email" column to the "Customers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  ALTER TABLE Customers
ADD Email varchar(255);
 
```
The following SQL deletes the "Email" column from the "Customers" table:

### Example

```
  ALTER TABLE Customers
DROP COLUMN Email;
 
```
Ad