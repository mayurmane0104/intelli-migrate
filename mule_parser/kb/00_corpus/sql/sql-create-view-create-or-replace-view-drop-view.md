# SQL CREATE VIEW, CREATE OR REPLACE VIEW, DROP VIEW

**Source:** [https://www.w3schools.com/sql/sql_ref_view.asp](https://www.w3schools.com/sql/sql_ref_view.asp)

---

# SQL VIEW Keyword

## CREATE VIEW

In SQL, a view is a virtual table based on the result set of an SQL statement.

The `CREATE VIEW` command creates a view.

The following SQL creates a view that selects all customers from Brazil:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
CREATE VIEW [Brazil 
  Customers] AS
SELECT 
  CustomerName, ContactName
FROM Customers
WHERE 
  Country = "Brazil"; 
```
## Query The View

We can query the view above as follows:

### Example

```
SELECT * FROM [Brazil 
  Customers]; 
```
## CREATE OR REPLACE VIEW

The `CREATE OR REPLACE VIEW` command updates a view.

The following SQL adds the "City" column to the "Brazil Customers" view:

### Example

```
CREATE OR REPLACE VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = "Brazil"; 
```
## DROP VIEW

The `DROP VIEW` command deletes a view.

The following SQL drops the "Brazil Customers" view:

### Example

```
DROP VIEW [Brazil Customers]; 
```
Ad