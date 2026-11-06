# SQL DROP

**Source:** [https://www.w3schools.com/sql/sql_ref_drop.asp](https://www.w3schools.com/sql/sql_ref_drop.asp)

---

# SQL DROP Keyword

## DROP COLUMN

The `DROP COLUMN` command is used to delete a column in an existing table.

The following SQL deletes the "ContactName" column from the "Customers" table:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  ALTER TABLE Customers
DROP COLUMN ContactName;
 
```
## DROP a UNIQUE Constraint

To drop a UNIQUE constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
DROP CONSTRAINT UC_Person; 
```
**MySQL:**

```
ALTER TABLE Persons
DROP INDEX UC_Person; 
```
## DROP a PRIMARY KEY Constraint

To drop a PRIMARY KEY constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
DROP CONSTRAINT PK_Person; 
```
**MySQL:**

```
ALTER TABLE Persons
DROP PRIMARY KEY; 
```
## DROP a FOREIGN KEY Constraint

To drop a FOREIGN KEY constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Orders
DROP CONSTRAINT FK_PersonOrder; 
```
**MySQL:**

```
ALTER TABLE Orders
DROP FOREIGN KEY FK_PersonOrder; 
```
## DROP a CHECK Constraint

To drop a CHECK constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
DROP CONSTRAINT CHK_PersonAge; 
```
**MySQL:**

```
ALTER TABLE Persons
DROP CHECK CHK_PersonAge; 
```
## DROP DEFAULT

The `DROP DEFAULT` command is used to delete 
a DEFAULT constraint.

To drop a DEFAULT constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
ALTER COLUMN City DROP DEFAULT; 
```
**MySQL:**

```
ALTER TABLE Persons
ALTER City DROP DEFAULT; 
```
## DROP INDEX

The `DROP INDEX` command is used to delete an 
index in a table.

**MS Access:**

```
DROP INDEX 
```
*index_name* ON *table_name*; **SQL Server:**

```
DROP INDEX 
```
*table_name*.*index_name*; **DB2/Oracle:**

```
DROP INDEX 
```
*index_name*; **MySQL:**

```
ALTER TABLE 
```
*table_name*DROP INDEX *index_name*; ## DROP DATABASE

The `DROP DATABASE` command is used is to 
delete an existing SQL database.

The following SQL drops a database named "testDB":

### Example

```
  DROP DATABASE testDB; 
```
**Note:** Be careful before dropping a database. Deleting 
a database will result in loss of complete information stored in the database!

## DROP TABLE

The `DROP TABLE` command deletes a table in 
the database.

The following SQL deletes the table "Shippers":

### Example

```
  DROP TABLE Shippers;
 
```
**Note****:** Be careful before deleting a table. Deleting a 
table results in loss of all information stored in the table!

## DROP VIEW

The `DROP VIEW` command deletes a view.

The following SQL drops the "Brazil Customers" view:

### Example

```
DROP VIEW [Brazil Customers]; 
```