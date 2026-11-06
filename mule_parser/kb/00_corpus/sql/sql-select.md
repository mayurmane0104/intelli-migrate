# SQL SELECT

**Source:** [https://www.w3schools.com/sql/sql_ref_backup_database.asp](https://www.w3schools.com/sql/sql_ref_backup_database.asp)

---

# SQL BACKUP DATABASE Keyword

## BACKUP DATABASE

The `BACKUP DATABASE` command is used in SQL 
Server to create a full back up of an existing SQL database.

The following SQL statement creates a full back up of the existing database "testDB" to the D disk:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak'; 
```
**Tip:** Always back up the database to a different drive than the 
actual database. If you get a disk crash, you will not lose your backup 
file along with the database.

A differential back up only backs up the parts of the database that have changed since the last full database backup.

The following SQL statement creates a differential back up of the database "testDB":

### Example

```
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak'
WITH 
  DIFFERENTIAL; 
```
**Tip:** A differential back up reduces the back up time (since only the changes are backed up).