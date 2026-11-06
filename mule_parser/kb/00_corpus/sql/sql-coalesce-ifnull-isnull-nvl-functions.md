# SQL COALESCE(), IFNULL(), ISNULL(), NVL() Functions

**Source:** [https://www.w3schools.com/sql/sql_isnull.asp](https://www.w3schools.com/sql/sql_isnull.asp)

---

# SQL NULL Functions

## SQL COALESCE(), IFNULL(), ISNULL(), and NVL() Functions

Operations involving NULL values can sometimes lead to unexpected results.

SQL has some built-in functions to handle NULL values, and the most common functions are:

- `COALESCE()`- The preferred standard. (Works in MySQL, SQL Server and Oracle)
- `IFNULL()`- (MySQL)
- `ISNULL()`- (SQL Server)
- `NVL()`- (Oracle)
- `IsNull()`- (MS Access)

**Note:** A `NULL` value represents an unknown or missing data in a database field. It is not a value itself, but a placeholder to indicate the absence of data.

## Demo Database

Assume we have the following "Products" table:

| PId | ProductName | Price | InStock | InOrder | 
|---|---|---|---|---|
| 1 | Jarlsberg | 10.45 | 16 | 15 | 
| 2 | Mascarpone | 32.56 | 23 | null | 
| 3 | Gorgonzola | 15.67 | 9 | 20 | 

The "InOrder" column is optional, and may contain NULL values.

Now look at the following SQL statement:

```
SELECT ProductName, Price * (InStock + InOrder)
FROM Products; 
```
**Note: In the SQL above, if any of the "InOrder" values are NULL, the result will be NULL!**

## The COALESCE() Function

The `COALESCE()` function is the preferred standard for handling potential NULL values.

The `COALESCE()` function returns the first non-NULL value in a list 
of values.

The `COALESCE()` function works in [MySQL](func_mysql_coalesce.asp),
[SQL Server](func_sqlserver_coalesce.asp), and Oracle (not in MS Access).

### Syntax

```
COALESCE(
```
*val1*, *val2*, *....*, *val_n*)
Here we use the ```
COALESCE()
```
 function to replace NULL 
values with 0:

```
SELECT ProductName, Price * (InStock + COALESCE(InOrder, 0))
FROM Products; 
```
## The IFNULL() Function (MySQL)

The MySQL [IFNULL()](func_mysql_ifnull.asp)

### Syntax

```
  IFNULL(
```
*expr*, *alt*)
Here we replace NULL values with 0:

```
SELECT ProductName, Price * (InStock + IFNULL(InOrder, 0))
FROM Products; 
```
## The ISNULL() Function (SQL Server)

The SQL Server [
ISNULL()](func_sqlserver_isnull.asp)

### Syntax

```
  ISNULL(
```
*expr*, *alt*)
Here we replace NULL values with 0:

```
SELECT ProductName, Price * (InStock + ISNULL(InOrder, 0))
FROM Products; 
```
## The NVL() Function (Oracle)

The Oracle `NVL()` function replaces NULL with 
a specified value.

### Syntax

```
NVL(
```
*expr*, *alt*)
Here we replace NULL values with 0:

```
SELECT ProductName, Price * (InStock + NVL(InOrder, 0))
FROM Products; 
```
## The IsNull() Function (MS Access)

The MS Access [
IsNull()](func_msaccess_isnull.asp)

### Syntax

```
  IsNull(
```
*expr*)
The MS Access `IIf()` function returns one 
of two parts, depending on the evaluation of the expression.

### Syntax

```
  IIf(
```
*expr, truepart, falsepart*)
- *expr*- Required. The expression to evaluate
- *truepart*- Value to return if- *expr*is True
- *falsepart*- Value to return if- *expr*is False

Here we replace NULL values with 0:

```
SELECT ProductName, Price * (InStock + IIf(IsNull(InOrder), 0, 
  InOrder))
FROM Products; 
```
## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

In SQL Server, which function can be used to replace `NULL` values with a specified alternative?