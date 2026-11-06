# SQL DEFAULT Constraint

**Source:** [https://www.w3schools.com/sql/sql_default.asp](https://www.w3schools.com/sql/sql_default.asp)

---

# SQL DEFAULT Constraint

## SQL DEFAULT Constraint

The `DEFAULT` constraint is used to 
automatically insert a default value for a column, 
if no value is specified.

The default value will be added to all new records (if no other value is specified).

## DEFAULT Constraint on CREATE TABLE

The following SQL sets a `DEFAULT` value for the "City" column 
upon creation of the "Persons" table:

```
CREATE TABLE Persons
(
    ID int PRIMARY KEY,
   
LastName varchar(255) NOT NULL,
   
FirstName varchar(255),
   
Age int,
   
City varchar(255) DEFAULT 'Sandnes'
); 
```
The `DEFAULT` constraint can also be used to insert system values, by using functions like ```
```
 to insert the current date:[CURRENT_DATE()](func_mysql_current_date.asp)

### MySQL:

```
CREATE TABLE Orders
(
    ID int PRIMARY KEY,
   
OrderNumber int NOT NULL,
   
OrderDate date DEFAULT CURRENT_DATE()
); 
```
### SQL Server:

To achieve the same result in SQL Server use the following SQL (to insert the current date):

```
CREATE TABLE Orders
(
    ID int PRIMARY KEY,
   
OrderNumber int NOT NULL,
   
OrderDate date DEFAULT CAST(GETDATE() AS date)
); 
```
## DEFAULT Constraint on ALTER TABLE

To define a `DEFAULT` constraint on the "City" column when the table is already created, use the following SQL:

### MySQL:

```
ALTER TABLE Persons
ALTER City SET DEFAULT 'Sandnes'; 
```
### SQL Server:

```
ALTER TABLE Persons
ADD CONSTRAINT df_City DEFAULT 'Sandnes' FOR City; 
```
### MS Access:

```
ALTER TABLE Persons
ALTER COLUMN City SET DEFAULT 'Sandnes'; 
```
### Oracle:

```
ALTER TABLE Persons
MODIFY City DEFAULT 'Sandnes'; 
```
## Drop a DEFAULT Constraint

To drop a `DEFAULT` constraint, use the following SQL:

### MySQL:

```
ALTER TABLE Persons
ALTER City DROP DEFAULT; 
```
### SQL Server:

```
ALTER TABLE Persons
  DROP CONSTRAINT df_City; 
```
### MS Access:

```
ALTER TABLE Persons
ALTER COLUMN City DROP DEFAULT; 
```
### Oracle:

```
ALTER TABLE Persons
  MODIFY (City DEFAULT NULL); 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of the SQL `DEFAULT` constraint?