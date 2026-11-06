# MS Access MonthName() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_monthname.asp](https://www.w3schools.com/sql/func_msaccess_monthname.asp)

---

# MS Access MonthName() Function

## Definition and Usage

The MonthName() function returns the name of the month based on a number.

## Syntax

```
  MonthName(
```
*number*, *abbreviate*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A value from 1 to 12, that represent the month | 
| abbreviate | Optional. A Boolean value. True = the month name should be abbreviated. False = the month name should not be abbreviated. False is default | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Return the abbreviated name of the month based on a number:

```
SELECT WeekdayName(3, true); 
```
Ad