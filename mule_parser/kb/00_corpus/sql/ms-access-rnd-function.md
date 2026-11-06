# MS Access Rnd Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_rnd.asp](https://www.w3schools.com/sql/func_msaccess_rnd.asp)

---

# MS Access Rnd Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return one random number between 1 and 10, and another random number between 100 and 499:

```
  SELECT Int((10 - 1 + 1) * Rnd + 1) AS RandNumBetween1and10,
Int((499 - 100 
  + 1) * Rnd + 100) AS RandNumBetween100and499; 
```
[Try it Yourself »](trysql.asp?filename=trysql_func_ms_rnd&ss=-1)

## Definition and Usage

The Rnd function returns a random number.

**Note:** If you do not call the 
[Randomize()](func_msaccess_randomize.asp) function before 
calling the Rnd function, the Rnd function may return the same random number each time!

## Syntax

To return a random integer less than 1, but greater than or equal to zero:

```
  Rnd
```
To return a random integer in a given range, use this formula:

```
  Int((
```
*upperbound* - *lowerbound* + 1) * Rnd + *lowerbound*)
## Parameter Values

| Parameter | Description | 
|---|---|
| upperbound | Required. The highest allowed value for the random number | 
| lowerbound | Required. The lowest allowed value for the random number | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

Ad