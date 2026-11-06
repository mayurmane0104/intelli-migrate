# SQL LIKE

**Source:** [https://www.w3schools.com/sql/sql_ref_like.asp](https://www.w3schools.com/sql/sql_ref_like.asp)

---

# SQL LIKE Keyword

## LIKE

The `LIKE` command is used in a WHERE clause 
to search for a specified pattern in a column.

You can use two wildcards with `LIKE`: 

- % - Represents zero, one, or multiple characters
- _ - Represents a single character (MS Access uses a question mark (?) instead)

The following SQL selects all customers with a CustomerName starting with "a":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE 'a%'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like)

The following SQL selects all customers with a CustomerName ending with "a":

The following SQL selects all customers with a CustomerName that have "or" in any position:

The following SQL statement selects all customers with a CustomerName that starts with "a" and are at least 3 characters in length:

Ad