# SQL CREATE OR REPLACE VIEW

**Source:** [https://www.w3schools.com/sql/sql_ref_create_or_replace_view.asp](https://www.w3schools.com/sql/sql_ref_create_or_replace_view.asp)

---

# SQL CREATE OR REPLACE VIEW Keyword

## CREATE OR REPLACE VIEW

In MySQL and Oracle, a view can be updated with the `CREATE OR REPLACE VIEW` command.

The following SQL adds the "City" column to the "Brazil Customers" view:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
CREATE OR REPLACE VIEW [Brazil Customers] AS
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
Ad