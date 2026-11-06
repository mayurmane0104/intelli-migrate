# SQL BACKUP DATABASE Statement

**Source:** [https://www.w3schools.com/sql/sql_backup_db.asp](https://www.w3schools.com/sql/sql_backup_db.asp)

---

# SQL BACKUP DATABASE Statement

## The BACKUP DATABASE Statement

The `BACKUP DATABASE` statement is used in SQL Server to create a full backup of an existing SQL database.

### Syntax

```
BACKUP DATABASE 
TO DISK = '
```
*databasename**filepath*';  
## BACKUP DATABASE Example

The following SQL creates a full backup of the existing database "testDB" to the D drive:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak'; 
```
**Tip:** Always place the backup database in a different drive than the 
original database! If you get a disk crash, you will not lose your backup 
file along with the database.

## The BACKUP WITH DIFFERENTIAL Statement

A differential backup only captures the data that has changed since the last full backup.

A differential backup requires at least one prior full backup!

### Syntax

```
BACKUP DATABASE 
TO DISK = '
WITH 
  DIFFERENTIAL; 
```
*databasename**filepath*'
## BACKUP WITH DIFFERENTIAL Example

The following SQL creates a differential backup of the database "testDB":

### Example

```
BACKUP DATABASE testDB
TO DISK = 'D:\backups\testDB.bak'
WITH 
  DIFFERENTIAL; 
```
**Tip:** A differential backup reduces the backup time (since only the changes are backed up).

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

Which SQL statement creates a full backup of a database named 'myDB'?