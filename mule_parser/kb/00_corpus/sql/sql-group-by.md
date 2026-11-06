# SQL GROUP BY

**Source:** [https://www.w3schools.com/sql/sql_ref_group_by.asp](https://www.w3schools.com/sql/sql_ref_group_by.asp)

---

# SQL GROUP BY Keyword

## GROUP BY

The `GROUP BY` command is used to group the result set (used with aggregate functions: COUNT, MAX, MIN, SUM, 
AVG).

The following SQL lists the number of customers in each country:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_groupby)

The following SQL lists the number of customers in each country, sorted high to low:

### Example

```
  SELECT COUNT(CustomerID), Country
FROM Customers
GROUP BY Country
  ORDER BY COUNT(CustomerID) DESC;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_groupby_orderby)

Ad