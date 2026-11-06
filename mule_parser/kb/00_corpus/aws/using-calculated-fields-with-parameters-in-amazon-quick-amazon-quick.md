# Using calculated fields with parameters in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/parameters-calculated-fields.html](https://docs.aws.amazon.com/quick/latest/userguide/parameters-calculated-fields.html)

---

You can pass the value of a parameter to a calculated field in an analysis. When
                you create a calculation, you can choose existing parameters from the list of
                parameters under **Parameter list**. You can't create a
                calculated field that contains a multivalued parameter—those with a
                multiselect drop-down control.

For the formula, you can use any of the available functions. You can pass the
                viewer's selection from the parameter control, to the `ifElse`
                function. In return, you get a metric. The following shows an example. 

```
ifelse(
${KPIMetric} = 'Sales',sum({Weighted Revenue}),
${KPIMetric} = 'Forecast',sum({Forecasted Monthly Revenue}),
${KPIMetric} = '# Active', distinct_count(ActiveItem),
NULL
)
```
The preceding example creates a metric (a decimal) that you can use in a field well. Then, when a user chooses a value from the parameter control, the visual updates to reflect their selection.