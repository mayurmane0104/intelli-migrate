# SQL DROP DEFAULT

**Source:** [https://www.w3schools.com/sql/sql_ref_drop_default.asp](https://www.w3schools.com/sql/sql_ref_drop_default.asp)

---

# SQL DROP DEFAULT Keyword

## DROP DEFAULT

The `DROP DEFAULT` command is used to delete 
a DEFAULT constraint.

To drop a DEFAULT constraint, use the following SQL:

**SQL Server / Oracle / MS Access:**

```
ALTER TABLE Persons
ALTER COLUMN City DROP DEFAULT; 
```
**MySQL:**

```
ALTER TABLE Persons
ALTER City DROP DEFAULT; 
```
Ad