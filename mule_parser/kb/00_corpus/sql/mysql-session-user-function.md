# MySQL SESSION_USER() Function

**Source:** [https://www.w3schools.com/sql/func_mysql_session_user.asp](https://www.w3schools.com/sql/func_mysql_session_user.asp)

---

# MySQL SESSION_USER() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the current user name and host name for the MySQL connection:

```
  SELECT SESSION_USER(); 
```
[Try it Yourself »](trymysql.asp?filename=trysql_func_mysql_session_user)

## Definition and Usage

The SESSION_USER() function returns the current user name and host name for the MySQL connection.

**Note:** This function is equal to the
[SYSTEM_USER()](func_mysql_system_user.asp) and the [USER()](func_mysql_user.asp) function.

## Syntax

```
  SESSION_USER()
```
## Technical Details

| Works in: | From MySQL 4.0 | 
|---|

Ad