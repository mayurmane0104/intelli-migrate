# Inserting dataset parameters into custom SQL - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-insert-parameter.html](https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-insert-parameter.html)

---

You can insert dataset parameters into the custom SQL of a dataset in direct query
            mode by referencing it with `<<$parameter_name>>` in the SQL statement.
            At runtime, dashboard users can enter filter control values that are associated with a
            dataset parameter. Then, they can see the results in the dashboard visuals after the
            values propagate to the SQL query. You can use parameters to create basic filters based
            on customer input in `where` clauses. Alternatively, you could add ```
case
                when
```
 or `if else` clauses to dynamically change the logic of the
            SQL query based on a parameter's input.

For example, say you want to add a `WHERE` clause to your custom SQL that
            filters data based on an end user's Region name. In this case, you create a single
            value parameter called `RegionName`:

```
SELECT *
FROM transactions
WHERE region = <<$RegionName>>
```
You can also let users provide multiple values to the parameter:

```
SELECT *
FROM transactions
WHERE region in (<<$RegionNames>>)
```
In the following more complex example, a dataset author refers to two dataset parameters twice based on a user's first and last names that can be selected in a dashboard filter control:

```
SELECT Region, Country, OrderDate, Sales
FROM transactions
WHERE region=
(Case
WHEN <<$UserFIRSTNAME>> In 
    (select firstname from user where region='region1') 
    and <<$UserLASTNAME>> In 
    (select lastname from user where region='region1') 
    THEN 'region1'
WHEN <<$UserFIRSTNAME>> In 
    (select firstname from user where region='region2') 
    and <<$UserLASTNAME>> In 
    (select lastname from user where region='region2') 
    THEN 'region2'
ELSE 'region3'
END)
```
You can also use parameters in `SELECT` clauses to create new columns in a
            dataset from user input:

```
SELECT Region, Country, date, 
    (case 
    WHEN <<$RegionName>>='EU'
    THEN sum(sales) * 0.93   --convert US dollar to euro
    WHEN <<$RegionName>>='CAN'
    THEN sum(sales) * 0.78   --convert US dollar to Canadian Dollar
    ELSE sum(sales) -- US dollar
    END
    ) as "Sales"
FROM transactions
WHERE region = <<$RegionName>>
```
To create a custom SQL query or to edit an existing query before adding a dataset
            parameter, see [Using SQL to customize data](./adding-a-SQL-query.html).

When you apply custom SQL with a dataset parameter,
                `<<$parameter_name>>` is used as a placeholder value. When a user
            chooses one of the parameter values from a control, Quick replaces the placeholder
            with the values that the user selects on the dashboard.

In the following example, the user enters a new custom SQL query that filters data by state:

```
select * from all_flights
where origin_state_abr = <<$State>>
```
The default value of the parameter is applied to the SQL query and the results appear
            in the **Preview pane**.