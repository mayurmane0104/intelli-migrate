# MS Access WeekdayName() Function

**Source:** [https://www.w3schools.com/sql/func_msaccess_weekdayname.asp](https://www.w3schools.com/sql/func_msaccess_weekdayname.asp)

---

# MS Access WeekdayName() Function

## Definition and Usage

The WeekdayName() function returns the weekday name based on a number.

## Syntax

```
  WeekdayName(
```
*number*, *abbreviate*, *firstdayofweek*)
## Parameter Values

| Parameter | Description | 
|---|---|
| number | Required. A value from 1 to 7, that represent the day of the week | 
| abbreviate | Optional. A Boolean value. True = the weekday name should be abbreviated. False = the weekday name should not be abbreviated. False is default | 
| firstdayofweek | Optional. Specifies the first day of the week. 
    Can be one of the following values: 
 | 

## Technical Details

| Works in: | From Access 2000 | 
|---|

## More Examples

### Example

Return the abbreviated weekday name based on a number:

```
SELECT WeekdayName(3, true); 
```
### Example

Return the abbreviated weekday name based on a number, and let Monday be the first day of week:

```
 SELECT WeekdayName(3, true, 2); 
```