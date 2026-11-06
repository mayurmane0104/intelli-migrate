# SQL SELECT TOP, LIMIT, ROWNUM

**Source:** [https://www.w3schools.com/sql/sql_ref_limit.asp](https://www.w3schools.com/sql/sql_ref_limit.asp)

---

# SQL SELECT TOP, LIMIT and ROWNUM Keywords

## SELECT TOP, LIMIT and ROWNUM

The `LIMIT`, `SELECT TOP` 
or `ROWNUM` command is used to specify the number of records to return.

**Note:** SQL Server uses ```
SELECT TOP
```
. MySQL 
uses `LIMIT`, and Oracle uses ```
ROWNUM
```
.

The following SQL statement selects the first three records from the "Customers" table (SQL SERVER):

The following SQL statement shows the equivalent example using the LIMIT clause (MySQL):

The following SQL statement shows the equivalent example using ROWNUM (Oracle):

### Example

```
SELECT * FROM Customers
WHERE ROWNUM  <= 3;
 
```
Ad