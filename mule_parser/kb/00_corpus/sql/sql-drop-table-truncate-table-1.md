# SQL DROP TABLE, TRUNCATE TABLE

**Source:** [https://www.w3schools.com/sql/sql_ref_truncate_table.asp](https://www.w3schools.com/sql/sql_ref_truncate_table.asp)

---

# SQL DROP TABLE and TRUNCATE TABLE Keywords

## DROP TABLE

The `DROP TABLE` command deletes a table in 
the database.

The following SQL deletes the table "Shippers":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  DROP TABLE Shippers;
 
```
**Note****:** Be careful before deleting a table. Deleting a table results in loss of all information stored in the table!

## TRUNCATE TABLE

The `TRUNCATE TABLE` command deletes the data inside a table, but 
not the table itself.

The following SQL truncates the table "Categories":

### Example

```
  TRUNCATE TABLE Categories;
 
```
Ad