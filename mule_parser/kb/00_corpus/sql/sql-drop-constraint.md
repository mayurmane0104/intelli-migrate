# SQL DROP CONSTRAINT

**Source:** [https://www.w3schools.com/sql/sql_ref_drop_constraint.asp](https://www.w3schools.com/sql/sql_ref_drop_constraint.asp)

---

# SQL DROP CONSTRAINT Keyword

## DROP CONSTRAINT

The `DROP CONSTRAINT` command is used to delete 
a UNIQUE, PRIMARY KEY, FOREIGN KEY, or CHECK constraint.

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
Ad

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