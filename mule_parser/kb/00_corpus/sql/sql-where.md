# SQL WHERE

**Source:** [https://www.w3schools.com/sql/sql_ref_where.asp](https://www.w3schools.com/sql/sql_ref_where.asp)

---

# SQL WHERE Keyword

## SELECT

The `WHERE` command filters a result set to include only records that fulfill a specified condition.

The following SQL statement selects all the customers from "Mexico" in the "Customers" table:

SQL requires single quotes around text values (most database systems will also allow double quotes).

However, numeric fields should not be enclosed in quotes:

**Note:** The WHERE clause is not only used in SELECT statement, it is also used in UPDATE,
DELETE statement, etc.!

The following operators can be used in the WHERE clause:

| Operator | Description | 
|---|---|
| = | Equal | 
| <> | Not equal. Note:In some versions of SQL this operator may be written as != | 
| > | Greater than | 
| < | Less than | 
| >= | Greater than or equal | 
| <= | Less than or equal | 
| BETWEEN | Between a certain range | 
| LIKE | Search for a pattern | 
| IN | To specify multiple possible values for a column |