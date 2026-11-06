# SQL NOT NULL

**Source:** [https://www.w3schools.com/sql/sql_ref_not_null.asp](https://www.w3schools.com/sql/sql_ref_not_null.asp)

---

# SQL NOT NULL Keyword

## NOT NULL

The `NOT NULL` constraint enforces a column to 
not accept NULL values, which means that you cannot insert or update a record without adding a value to this field.

The following SQL ensures that the "ID", "LastName", and "FirstName" columns will NOT accept NULL values:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  CREATE TABLE Persons (
    ID int NOT NULL,
    
  LastName varchar(255) NOT NULL,
    FirstName varchar(255) 
  NOT NULL,
    Age int
);  
```
The following SQL creates a NOT NULL constraint on the "Age" column when the "Persons" table is already created:

```
ALTER TABLE Persons
MODIFY Age int NOT NULL; 
```
Ad