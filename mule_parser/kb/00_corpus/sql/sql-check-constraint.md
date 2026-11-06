# SQL CHECK Constraint

**Source:** [https://www.w3schools.com/sql/sql_check.asp](https://www.w3schools.com/sql/sql_check.asp)

---

# SQL CHECK Constraint

## SQL CHECK Constraint

The `CHECK` constraint is used to ensure that 
the values in a column satisfies a specific condition.

The `CHECK` constraint evaluates the data to 
TRUE or FALSE. If the data evaluates to TRUE, the operation is ok. If the data 
evaluates to FALSE, the entire INSERT or UPDATE operation is aborted, and an 
error is raised.

## CHECK Constraint on CREATE TABLE

The following SQL creates a `CHECK` constraint on the "Age" column 
upon creation of the "Persons" table.

Here, the `CHECK` constraint ensures that the 
"Age" column must have a value of 18, or above:

```
CREATE TABLE Persons
(
    ID int PRIMARY KEY,
   
LastName varchar(255) NOT NULL,
   
FirstName varchar(255),
   
Age int CHECK (Age >= 18)
); 
```
### Naming a CHECK Constraint

To name a `CHECK` constraint, and to define a ```
CHECK
```
 constraint on multiple columns, use the following SQL syntax:

```
CREATE TABLE Persons
(
    ID int PRIMARY KEY,
   
LastName varchar(255) NOT NULL,
   
FirstName varchar(255),
   
Age int,
   
City varchar(255),
   
CONSTRAINT chk_PersonAge CHECK (Age >= 18 AND City = 'Sandnes')
); 
```
## CHECK Constraint on ALTER TABLE

To create a `CHECK` constraint on the "Age" column when the table is already created, use the following SQL:

```
ALTER TABLE Persons
ADD CHECK (Age >= 18); 
```
### Naming a CHECK Constraint

To name a `CHECK` constraint, and to define a ```
CHECK
```
 constraint on multiple columns, use the following SQL syntax:

```
ALTER TABLE Persons
ADD CONSTRAINT chk_PersonAge CHECK (Age >= 18 AND City = 'Sandnes'); 
```
## Drop a CHECK Constraint

To drop a `CHECK` constraint, use the following SQL:

### SQL Server / Oracle / MS Access:

```
ALTER TABLE Persons
DROP CONSTRAINT chk_PersonAge; 
```
### MySQL:

```
ALTER TABLE Persons
DROP CHECK chk_PersonAge; 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the primary purpose of the SQL `CHECK` constraint?