# SQL Wildcard Characters

**Source:** [https://www.w3schools.com/sql/sql_wildcards.asp](https://www.w3schools.com/sql/sql_wildcards.asp)

---

# SQL Wildcards

## SQL Wildcard Characters

A wildcard character is used to substitute one or more characters in a string.

Wildcard characters are used with the ```
```
 
operator. The [LIKE](sql_like.asp)`LIKE` operator is used in a ```
WHERE
```
 clause to search for a specified pattern in a column.

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return all customers that starts with the letter 'a':

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE 'a%';  
```
  [Try it Yourself »](trysql.asp?filename=trysql_select_wildcard_a)

## Wildcard Characters

| Symbol | Description | 
|---|---|
| % | Represents zero or more characters | 
| _ | Represents a single character | 
| [] | Represents any single character within the brackets * | 
| ^ | Represents any character not in the brackets * | 
| - | Represents any single character within the specified range * | 
| {} | Represents any escaped character ** | 

* Not supported in PostgreSQL and MySQL databases.

** Supported only in Oracle databases.

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## Using the % Wildcard

The `%` wildcard represents any number of characters, even zero characters.

### Example

Return all customers that ends with the pattern 'es':

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE '%es';
 
```
  [Try it Yourself »](trysql.asp?filename=trysql_select_wildcard_endswith)

### Example

Return all customers that *contains* the pattern 'mer':

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE '%mer%';
 
```
  [Try it Yourself »](trysql.asp?filename=trysql_select_wildcard_contains)

## Using the _ Wildcard

The `_` wildcard represents a single character.

It can be any character or number, but each `_` represents one, and only one, character.

### Example

Return all customers with a `City` starting with any character, followed by "ondon":

```
 SELECT * FROM Customers
 WHERE City LIKE '_ondon';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_wildcard_underscore)

### Example

Return all customers with a `City` starting with "L", followed by any 
3 characters, ending with "on":

```
 SELECT * FROM Customers
 WHERE City LIKE 'L___on';
 
```
  [Try it Yourself »](trysql.asp?filename=trysql_select_wildcard_3_underscores)

## Using the [] Wildcard

The `[]` wildcard returns a result if *any*
of the characters inside gets a match.

### Example

Return all customers starting with either "b", "s", or "p":

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE '[bsp]%';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_wildcard_charlist)

## Using the - Wildcard

The `-` wildcard allows you to specify a range 
of characters inside the `[]` wildcard.

### Example

Return all customers starting with "a", "b", "c", "d", "e" or "f":

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE '[a-f]%';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_wildcard_charlist2)

## Combine Wildcards

Any wildcard, like `%` and `_` 
, can be used in combination with other 
wildcards.

### Example

Return all customers that starts with "a" and are at least 3 characters in length:

```
 SELECT * FROM Customers
  WHERE CustomerName LIKE 'a__%'; 
```
  [Try it Yourself »](trysql.asp?filename=trysql_select_like_start_least)

### Example

Return all customers that have "r" in the second position:

```
 SELECT * FROM Customers
  WHERE CustomerName LIKE '_r%';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_underscore)

## Without Wildcard

If no wildcard is specified, the phrase has to have an exact match to return a result.

### Example

Return all customers from Spain:

```
 SELECT * FROM Customers
  WHERE Country 
  LIKE 'Spain';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_spain)

## Microsoft Access Wildcards

The Microsoft Access Database has some other wildcards:

| Symbol | Description | Example | 
|---|---|---|
| * | Represents zero or more characters | bl* finds bl, black, blue, and blob | 
| ? | Represents a single character | h?t finds hot, hat, and hit | 
| [] | Represents any single character within the brackets | h[oa]t finds hot and hat, but not hit | 
| ! | Represents any character not in the brackets | h[!oa]t finds hit, but not hot and hat | 
| - | Represents any single character within the specified range | c[a-b]t finds cat and cbt | 
| # | Represents any single numeric character | 2#5 finds 205, 215, 225, 235, 245, 255, 265, 275, 285, and 295 | 

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the `%` wildcard represent in SQL?