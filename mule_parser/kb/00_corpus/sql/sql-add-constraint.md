# SQL ADD CONSTRAINT

**Source:** [https://www.w3schools.com/sql/sql_ref_add_constraint.asp](https://www.w3schools.com/sql/sql_ref_add_constraint.asp)

---

# SQL ADD CONSTRAINT Keyword

## ADD CONSTRAINT

The `ADD CONSTRAINT` command is used to create 
a constraint after a table is already created.

The following SQL adds a constraint named "PK_Person" that is a PRIMARY KEY constraint on multiple columns (ID and LastName):

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
ALTER TABLE Persons
ADD CONSTRAINT PK_Person PRIMARY KEY (ID,LastName);
 
```