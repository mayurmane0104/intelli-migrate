# SQL CREATE UNIQUE INDEX

**Source:** [https://www.w3schools.com/sql/sql_ref_create_unique_index.asp](https://www.w3schools.com/sql/sql_ref_create_unique_index.asp)

---

# SQL CREATE UNIQUE INDEX Keyword

## CREATE UNIQUE INDEX

The `CREATE UNIQUE INDEX` command creates a unique index on a table (no duplicate values 
allowed)

Indexes are used to retrieve data from the database very fast. The users cannot see the indexes, they are just used to speed up searches/queries.

The following SQL creates an index named "uidx_pid" on the "PersonID" column in the "Persons" table:

```
CREATE UNIQUE INDEX uidx_pid
ON Persons (PersonID); 
```
**Note:** The syntax for creating indexes varies among different databases. Therefore: Check the syntax for creating indexes in your database.

**Note:** Updating a table with indexes takes more time than updating a table without (because the indexes also need an update).
So, only create indexes on columns that will be frequently searched against.