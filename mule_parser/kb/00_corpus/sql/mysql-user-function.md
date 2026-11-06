# MySQL USER() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_user.asp](https://www.w3schools.com/sql/func_mysql_user.asp)

---

# MySQL USER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the current user name and host name for the MySQL connection:

```
  SELECT USER(); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_user)

## Definition and Usage

The USER() function returns the current user name and host name for the MySQL connection.

**Note:** This function is equal to the
[SESSION_USER()](func_mysql_session_user.asp) function and the
[SYSTEM_USER()](func_mysql_system_user.asp) function.

**Tip:** Also look at the [
CURRENT_USER()](func_mysql_current_user.asp) function.

## Syntax

```
  USER()
```
## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad