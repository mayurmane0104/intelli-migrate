# SQL LIKE Operator

**Source:** [https://www.w3schools.com/sql/sql_like.asp](https://www.w3schools.com/sql/sql_like.asp)

---

# SQL LIKE Operator

## The SQL LIKE Operator

The `LIKE` operator is used in a ```
WHERE
```
 clause to search for a specified pattern within a column's text 
data.

There are two wildcards often used in conjunction with the ```
LIKE
```
 operator:

- A percent sign `%`- represents zero, one, or multiple characters
- A underscore sign `_`- represents a single character

The following SQL selects all customers that starts with the letter "a":

### Example[Get your own SQL Server](/sql/sql_server.asp)

Select all customers that starts with the letter "a":

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE 'a%'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like)

## Syntax

```
SELECT 
```
*column1, column2, ...*

FROM *table_name*

WHERE *columnN* LIKE *pattern*; 

## Demo Database

Below is a selection from the [ Customers](trysql.asp?filename=trysql_customers) table used in the examples:

| CustomerID | CustomerName | ContactName | Address | City | PostalCode | Country | 
|---|---|---|---|---|---|---|
| 1 | Alfreds Futterkiste | Maria Anders | Obere Str. 57 | Berlin | 12209 | Germany | 
| 2 | Ana Trujillo Emparedados y helados | Ana Trujillo | Avda. de la Constitución 2222 | México D.F. | 05021 | Mexico | 
| 3 | Antonio Moreno Taquería | Antonio Moreno | Mataderos 2312 | México D.F. | 05023 | Mexico | 
| 4 | Around the Horn | Thomas Hardy | 120 Hanover Sq. | London | WA1 1DP | UK | 
| 5 | Berglunds snabbköp | Christina Berglund | Berguvsvägen 8 | Luleå | S-958 22 | Sweden | 

## The % Wildcard

The `%` wildcard represents any number of characters, even zero characters.

### Example

Return all customers from a City that *contains* the character 
sequence 'on':

```
 SELECT * FROM Customers
 WHERE city LIKE '%on%'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_l)

## The _ Wildcard

The `_` wildcard represents one single character.

It can be any character or number, but each `_` represents one, and only one, character.

### Example

Return all customers from a City that starts with 'l' followed by one wildcard character, then 'nd' and then two wildcard characters:

```
 SELECT * FROM Customers
 WHERE city LIKE 'l_nd__'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_london)

## Starts With

To return records that starts with a specific letter or phrase, add the `%` at the end of the letter or phrase.

### Example

Return all customers that starts with 'La':

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE 'La%'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_la)

**Tip:** You can also combine any number of conditions using ```
AND
```
 or `OR` operators.

### Example

Return all customers that starts with 'a' or starts with 'b':

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE 'a%' OR CustomerName LIKE 'b%';  
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_ending2)

## Ends With

To return records that ends with a specific letter or phrase, add the `%` at the beginning of the letter or phrase.

### Example

Return all customers that ends with 'a':

```
 SELECT * FROM Customers
 WHERE CustomerName LIKE '%a';  
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_ending)

**Tip:** You can also combine "starts with" and "ends with":

### Example

Return all customers that starts with "b" and ends with "s":

```
 SELECT * FROM Customers
  WHERE CustomerName LIKE 'b%s'; 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_startend)

## Contains

To return records that contains a specific letter or phrase, add the 
`%` both before and after the letter or phrase.

### Example

Return all customers that contains the phrase 'or'

```
 SELECT * FROM Customers
  WHERE CustomerName LIKE '%or%';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_pattern)

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

## Without Wildcards

If no wildcard is specified, the phrase has to have an exact match to return a result.

### Example

Return all customers from Spain:

```
 SELECT * FROM Customers
  WHERE Country 
  LIKE 'Spain';
 
```
[Try it Yourself »](trysql.asp?filename=trysql_select_like_spain)

## Exercise?**What is this?**

Test your skills by answering a few questions about the topics of this page

What does the SQL `LIKE` operator do?