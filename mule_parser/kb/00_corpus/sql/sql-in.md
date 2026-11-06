# SQL IN

**Source:** [https://www.w3schools.com/sql/sql_ref_in.asp](https://www.w3schools.com/sql/sql_ref_in.asp)

---

# SQL IN Keyword

## IN

The `IN` operator is used in the `WHERE` clause to check if a specified column's value matches
any value within a provided list.

The `IN` operator functions as a shorthand for multiple `OR` conditions, making queries shorter and more readable.

The following SQL uses the `IN` operator to select all customers from 
Germany, France, or UK:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT * FROM Customers
  WHERE Country IN ('Germany', 'France', 'UK');
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_in)

The following SQL selects all customers that are NOT located in "Germany", "France" or "UK":

The following SQL selects all customers that are from the same countries as the suppliers: