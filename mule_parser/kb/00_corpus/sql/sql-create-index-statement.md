# SQL CREATE INDEX Statement

**Source:** [https://www.w3schools.com/sql/sql_create_index.asp](https://www.w3schools.com/sql/sql_create_index.asp)

---

# SQL CREATE INDEX Statement

## SQL CREATE INDEX Statement

The `CREATE INDEX` statement is used to create indexes 
on tables in databases, to speed up data retrieval.

The users cannot see the indexes, they are just used to speed up searches/queries.

**Note:** Updating tables with indexes are more time-consuming 
than tables without indexes (because the indexes must also be updated).
So, only create indexes on columns that are frequently searched against.

## Types of Indexes: Non-unique and Unique

There are two types of indexes:

- `CREATE INDEX`- Creates a non-unique index (duplicate values are allowed)
- `CREATE UNIQUE INDEX`- Creates a unique index (duplicate values are not allowed)

### CREATE INDEX Syntax

```
CREATE INDEX 
ON 
```
*index_name**table_name* (*column1*, *column2*, ...); ### CREATE UNIQUE INDEX Syntax

```
CREATE UNIQUE INDEX 
ON 
```
*index_name**table_name* (*column1*, *column2*, ...); **Note:** The syntax for creating indexes varies among different databases. 
Check the syntax for creating indexes in your database!

## CREATE INDEX Example

The following SQL creates a non-unique index named "idx_lastname" on the "LastName" column in the "Persons" table:

```
CREATE INDEX idx_lastname
ON Persons (LastName); 
```
If you want to create an index on a combination of columns, you can list the column names within the parentheses, separated by commas:

```
CREATE INDEX idx_lname_fname
ON Persons (LastName, FirstName); 
```
## DROP INDEX Statement

The `DROP INDEX` statement is used to remove an index.

### SQL Server:

```
DROP INDEX 
```
*table_name*.*index_name*; ### MySQL:

```
ALTER TABLE 
```
*table_name*DROP INDEX *index_name*; ### MS Access:

```
DROP INDEX 
```
*index_name* ON *table_name*; ### DB2/Oracle:

```
DROP INDEX 
```
*index_name*; ## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is the purpose of the SQL `CREATE INDEX` statement?