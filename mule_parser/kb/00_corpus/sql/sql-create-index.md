# SQL CREATE INDEX

**Source:** [https://www.w3schools.com/sql/sql_ref_create_index.asp](https://www.w3schools.com/sql/sql_ref_create_index.asp)

---

# SQL CREATE INDEX Keyword

## CREATE INDEX

The `CREATE INDEX` command is used to 
create indexes in tables (allows duplicate values).

Indexes are used to retrieve data from the database very fast. The users cannot see the indexes, they are just used to speed up searches/queries.

The following SQL creates an index named "idx_lastname" on the "LastName" column in the "Persons" table:

```
CREATE INDEX idx_lastname
ON Persons (LastName); 
```
If you want to create an index on a combination of columns, you can list the column names within the parentheses, separated by commas:

```
CREATE INDEX idx_pname
ON Persons (LastName, FirstName); 
```
**Note:** The syntax for creating indexes varies among different databases. Therefore: Check the syntax for creating indexes in your database.

**Note:** Updating a table with indexes takes more time than updating a table without (because the indexes also need an update).
So, only create indexes on columns that will be frequently searched against.