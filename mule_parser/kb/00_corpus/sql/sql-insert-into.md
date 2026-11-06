# SQL INSERT INTO

**Source:** [https://www.w3schools.com/sql/sql_ref_insert_into.asp](https://www.w3schools.com/sql/sql_ref_insert_into.asp)

---

# SQL INSERT INTO Keyword

## INSERT INTO

The `INSERT INTO` command is used to insert new rows in a table.

The following SQL inserts a new record in the "Customers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');
 
```
The following SQL will insert a new record, but only insert data in the "CustomerName", "City", and "Country" columns (CustomerID will be updated automatically):

### Example

```
INSERT INTO Customers (CustomerName, City, Country)
VALUES ('Cardinal', 'Stavanger', 'Norway');
 
```
Ad