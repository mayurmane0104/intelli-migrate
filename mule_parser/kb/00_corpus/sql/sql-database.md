# SQL DATABASE

**Source:** [https://www.w3schools.com/sql/sql_ref_database.asp](https://www.w3schools.com/sql/sql_ref_database.asp)

---

# SQL DATABASE Keyword

## CREATE DATABASE

The `CREATE DATABASE` command is used is to 
create a new SQL database.

The following SQL creates a database called "testDB":

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
CREATE DATABASE testDB;
 
```
**Tip:** Make sure you have admin privilege before creating any database. Once a 
database is created, you can check it in the list of databases with the 
following SQL command: SHOW DATABASES;

## DROP DATABASE

The `DROP DATABASE` command is used is to 
delete an existing SQL database.

The following SQL drops a database named "testDB":

### Example

```
  DROP DATABASE testDB; 
```
**Note:** Be careful before dropping a database. Deleting 
a database will result in loss of complete information stored in the database!