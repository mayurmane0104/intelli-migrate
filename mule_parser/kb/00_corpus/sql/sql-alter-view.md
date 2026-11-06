# SQL ALTER VIEW

**Source:** [https://www.w3schools.com/sql/sql_ref_alter_view.asp](https://www.w3schools.com/sql/sql_ref_alter_view.asp)

---

# SQL ALTER VIEW Keyword

## ALTER VIEW

In SQL Server, a view can be updated with the `ALTER VIEW` command.

The following SQL adds the "City" column to the "Brazil Customers" view:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  ALTER VIEW [Brazil Customers] AS
SELECT CustomerName, ContactName, City
FROM Customers
WHERE Country = "Brazil"; 
```
## Query The View

We can query the view above as follows:

### Example

```
SELECT * FROM [Brazil 
  Customers]; 
```