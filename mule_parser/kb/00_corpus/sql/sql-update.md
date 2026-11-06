# SQL UPDATE

**Source:** [https://www.w3schools.com/sql/sql_ref_update.asp](https://www.w3schools.com/sql/sql_ref_update.asp)

---

# SQL UPDATE Keyword

## UPDATE

The `UPDATE` command is used to update existing rows in a table.

The following SQL statement updates the first customer (CustomerID = 1) with a new contact person *and* 
a new city.

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 UPDATE Customers
 SET ContactName = 'Alfred Schmidt', City= 'Frankfurt'
 WHERE CustomerID = 1;
 
```
The following SQL statement will update the contactname to "Juan" for all records where country is "Mexico":

### Example

```
UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';
 
```
**Note:** Be careful when updating records in a table! Notice the WHERE clause in the 
UPDATE statement.
The WHERE clause specifies which record(s) that should be updated. If 
you omit the WHERE clause, all records in the table will be updated!