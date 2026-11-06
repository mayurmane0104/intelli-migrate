# MySQL CURRENT_USER() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_current_user.asp](https://www.w3schools.com/sql/func_mysql_current_user.asp)

---

# MySQL CURRENT_USER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the user name and host name for the MySQL account:

```
  SELECT CURRENT_USER(); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_current_user)

## Definition and Usage

The CURRENT_USER() function returns the user name and host name for the MySQL account that the server used to authenticate the current client.

The result is returned as a string in the UTF8 character set.

**Tip:** See also the [USER()](func_mysql_user.asp) 
function.

## Syntax

```
  CURRENT_USER()
```
## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad