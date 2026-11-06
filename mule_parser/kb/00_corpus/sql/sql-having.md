# SQL HAVING

**Source:** [https://www.w3schools.com/sql/sql_ref_having.asp](https://www.w3schools.com/sql/sql_ref_having.asp)

---

# SQL HAVING Keyword

## HAVING

The `HAVING` command is used instead of WHERE with aggregate functions.

The following SQL lists the number of customers in each country. Only include countries with more than 5 customers:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
  HAVING COUNT(CustomerID) > 5;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_having)

The following SQL lists the number of customers in each country, sorted high to low (Only include countries with more than 5 customers):

### Example

```
  SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
HAVING COUNT(CustomerID) 
  > 5
  ORDER BY COUNT(CustomerID) DESC;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_having_orderby)

Ad