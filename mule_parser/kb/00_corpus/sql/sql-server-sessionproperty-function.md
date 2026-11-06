# SQL Server SESSIONPROPERTY() Function

**Source:** [https://www.w3schools.com/sql/func_sqlserver_sessionproperty.asp](https://www.w3schools.com/sql/func_sqlserver_sessionproperty.asp)

---

# SQL Server SESSIONPROPERTY() Function

### Example[Get your own SQL Server](/sql/sql_server.asp)

Return the session settings for a specified option:

```
  SELECT SESSIONPROPERTY('ANSI_NULLS'); 
```
## Definition and Usage

The SESSIONPROPERTY() function returns the session settings for a specified option.

## Syntax

```
  SESSIONPROPERTY(
```
*option*)
## Parameter Values

| Parameter | Description | 
|---|---|
| option | Required. The option to retrieve the session settings for. Can be one of 
    the following values: 
 | 

## Technical Details

| Works in: | SQL Server (starting with 2008), Azure SQL Database | 
|---|

Ad