# SQL CREATE VIEW

**Source:** [https://www.w3schools.com/sql/sql_ref_create_view.asp](https://www.w3schools.com/sql/sql_ref_create_view.asp)

---

# SQL CREATE VIEW Keyword

## CREATE VIEW

The `CREATE VIEW` command creates a view.

A view is a virtual table based on the result set of an SQL statement.

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
SELECT * FROM [Brazil Customers]; 
```
Ad