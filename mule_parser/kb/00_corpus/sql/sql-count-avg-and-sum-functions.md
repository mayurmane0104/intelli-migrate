# SQL COUNT(), AVG() and SUM() Functions

**Source:** [https://www.w3schools.com/sql/sql_count_avg_sum.asp](https://www.w3schools.com/sql/sql_count_avg_sum.asp)

---

# SQL COUNT(), AVG() and SUM() Functions

## The SQL COUNT(), AVG() and SUM() Functions

The `COUNT()` function returns the number of rows that matches a specified criterion.

### COUNT() Syntax

```
SELECT COUNT(
FROM 
WHERE 
```
*column_name*)*table_name**condition*; The `AVG()` function returns the average value of a numeric column. 

### AVG() Syntax

```
SELECT AVG(
FROM 
WHERE 
```
*column_name*)*table_name**condition*; The `SUM()` function returns the total sum of a numeric column. 

### SUM() Syntax

```
SELECT SUM(
FROM 
WHERE 
```
*column_name*)*table_name**condition*; ## Demo Database

Below is a selection from the "Products" table in the Northwind sample database:

| ProductID | ProductName | SupplierID | CategoryID | Unit | Price | 
|---|---|---|---|---|---|
| 1 | Chais | 1 | 1 | 10 boxes x 20 bags | 18 | 
| 2 | Chang | 1 | 1 | 24 - 12 oz bottles | 19 | 
| 3 | Aniseed Syrup | 1 | 2 | 12 - 550 ml bottles | 10 | 
| 4 | Chef Anton's Cajun Seasoning | 2 | 2 | 48 - 6 oz jars | 22 | 
| 5 | Chef Anton's Gumbo Mix | 2 | 2 | 36 boxes | 21.35 | 

## COUNT() Example

The following SQL statement finds the number of products:

**Note:** NULL values are not counted.

## AVG() Example

The following SQL statement finds the average price of all products:

**Note:** NULL values are ignored.

## Demo Database

Below is a selection from the "OrderDetails" table in the Northwind sample database:

| OrderDetailID | OrderID | ProductID | Quantity | 
|---|---|---|---|
| 1 | 10248 | 11 | 12 | 
| 2 | 10248 | 42 | 10 | 
| 3 | 10248 | 72 | 5 | 
| 4 | 10249 | 14 | 9 | 
| 5 | 10249 | 51 | 40 | 

## SUM() Example

The following SQL statement finds the sum of the "Quantity" fields in the "OrderDetails" table:

**Note:** NULL values are ignored.