# SQL DELETE

**Source:** [https://www.w3schools.com/sql/sql_ref_delete.asp](https://www.w3schools.com/sql/sql_ref_delete.asp)

---

# SQL DELETE Keyword

## DELETE

The `DELETE` command is used to delete 
existing records in a table.

The following SQL statement deletes the customer "Alfreds Futterkiste" from the "Customers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 DELETE FROM Customers
 WHERE CustomerName='Alfreds Futterkiste';
 
```
**Note:** Be careful when deleting records in a table! Notice the WHERE clause in the 
DELETE statement.
The WHERE clause specifies which record(s) should be deleted. If 
you omit the WHERE clause, all records in the table will be deleted!

It is possible to delete all rows in a table without deleting the table. This means that the table structure, attributes, and indexes will be intact:

The following SQL statement deletes all rows in the "Customers" table, without deleting the table. This means that the table structure, attributes, and indexes will be intact:

### Example

```
  DELETE FROM Customers;
 
```