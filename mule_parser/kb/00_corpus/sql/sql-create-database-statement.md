# SQL CREATE DATABASE Statement

**Source:** [https://www.w3schools.com/sql/sql_create_db.asp](https://www.w3schools.com/sql/sql_create_db.asp)

---

# SQL CREATE DATABASE Statement

## The SQL CREATE DATABASE Statement

The `CREATE DATABASE` statement is used to create a new SQL database.

**Tip:** You need administrative privileges to create a new database. 

### Syntax

```
CREATE DATABASE 
```
*database_name*; 
## CREATE DATABASE Example

The following SQL statement creates a database called "testDB":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
CREATE DATABASE testDB;
 
```
## Show Databases

Once a database is created, you can check it in the list of databases with the following SQL command:

### Syntax for SQL Server

```
SELECT name FROM sys.databases; 
```
### Syntax for MySQL

```
SHOW DATABASES;
 
```
Ad

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the purpose of the SQL `CREATE DATABASE` statement?