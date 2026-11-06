# SQL NULL Values - IS NULL and IS NOT NULL

**Source:** [https://www.w3schools.com/sql/sql_null_values.asp](https://www.w3schools.com/sql/sql_null_values.asp)

---

# SQL NULL Values

## What is a NULL Value?

If a field in a table is optional, it is possible to insert or update a record without adding any value to this field.
This way, the field will be saved with a `NULL` value.

A `NULL` value represents an unknown, missing, or inapplicable data in a database field. It is not a value itself, but a placeholder to indicate the absence of data.

**Note:** A `NULL` value is different from zero (0) or an empty string (''). A field with a `NULL`
value is one that has been left blank upon record creation.

## How to Test for NULL Values?

It is not possible to test for NULL values with comparison operators, such as =, <, or <>.

We will have to use the `IS NULL` and ```
IS NOT NULL
```
 operators instead.

### IS NULL Syntax

```
  SELECT 
```
*column_names*FROM 

*table_name*

WHERE

*column_name*IS NULL;

### IS NOT NULL Syntax

```
  SELECT 
```
*column_names*FROM 

*table_name*

WHERE

*column_name*IS NOT NULL;

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## The IS NULL Operator

The `IS NULL` operator is used to test for empty values (NULL values).

The following SQL lists all customers with a NULL value in the "Address" field:

### Example[Get your own SQL Server](/sql/sql_server.asp)

```
  SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address 
  IS NULL;
 
```
[Try it Yourself »](trysql.asp?filename=trysql_is_null)

**Tip:** Always use `IS NULL` to look for NULL values.

## The IS NOT NULL Operator

The `IS NOT NULL` operator is used to test for non-empty values (NOT NULL 
values).

The following SQL lists all customers with a value in the "Address" field:

### Example

```
  SELECT CustomerName, ContactName, Address
FROM Customers
WHERE Address 
  IS NOT NULL;
 
```
  [Try it Yourself »](trysql.asp?filename=trysql_is_not_null)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What is a `NULL` value in SQL?

## Video: SQL NULL Values

![SQL Tutorial on YouTube](images/yt_logo_rgb_dark.png) 

        ![SQL Tutorial on YouTube](images/img_sql_null.png)