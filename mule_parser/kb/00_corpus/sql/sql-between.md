# SQL BETWEEN

**Source:** [https://www.w3schools.com/sql/sql_ref_between.asp](https://www.w3schools.com/sql/sql_ref_between.asp)

---

# SQL BETWEEN Keyword

## BETWEEN

The `BETWEEN` command is used to select values 
within a given range. The values can be numbers, text, or dates.

The `BETWEEN` command is inclusive: begin and end values are included. 

The following SQL statement selects all products with a price BETWEEN 10 and 20:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_between)

To display the products outside the range of the previous example, use NOT BETWEEN:

The following SQL statement selects all products with a ProductName BETWEEN 'Carnarvon Tigers' and 'Mozzarella di Giovanni':

### Example

```
 SELECT * FROM Products
WHERE ProductName BETWEEN 'Carnarvon Tigers' AND 'Mozzarella 
  di Giovanni'
ORDER BY ProductName;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_between_text)

Ad