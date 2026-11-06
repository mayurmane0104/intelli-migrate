# Advanced use cases of dataset parameters - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-advanced-options.html](https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-advanced-options.html)

---

This section covers more advanced options and use cases working with dataset parameters and dropdown controls. Use the following walkthroughs to create dynamic dropdown values with dataset parameters.

## Using multivalue controls with dataset parameters

            When you use dataset parameters that are inserted into the custom SQL of a dataset, the dataset parameters commonly filter data by values from a specific column. If you create a dropdown control and assign the parameter as the value, the dropdown only shows the value that the parameter filtered. The following procedure shows how you can create a control that is mapped to a dataset parameter and shows all unfiltered values.

###### To populate all assigned values in a dropdown control

- 
                    Create a new single–column dataset in SPICE or direct query that includes all unique values from the original dataset. For example, let's say that your original dataset is using the following custom SQL: `select * from all_flights where origin_state_abr = <<$State>>`To create a single–column table with all unique origin states, apply the following custom SQL to the new dataset: `SELECT distinct origin_state_abr FROM all_flights order by origin_state_abr asc`The SQL expression returns all unique states in alphabetic order. The new dataset does not have any dataset parameters. 
- 
                    Enter a **Name**for the new dataset, and then save and publish the dataset. In our example, the new dataset is called`State Codes`.
- 
                    Open the analysis that contains the original dataset, and add the new dataset to the analysis. For information on adding datasets to an existing analysis, see [Adding a dataset to an analysis](./adding-a-data-set-to-an-analysis.html).
- 
                    Navigate to the **Controls**pane and find the dropdown control that you want to edit. Choose the ellipsis (three dots) next to the control, and then choose**Edit**.
- 
                    In the **Format control**that appears on the left, and choose**Link to a dataset field**in the**Values**section.
- 
                    For the **Dataset**dropdown that appears, choose the new dataset that you created. In our example, the`State Codes`dataset is chosen.
- 
                    For the **Field**dropdown that appears, choose the appropriate field. In our example, the`origin_state_abr`field is chosen.

After you finish linking the control to the new dataset, all unique values appear in the control's dropdown. These include the values that are filtered out by the dataset parameter.

## Using controls with Select all options

            By default, when one or more dataset parameters are mapped to an analysis
                parameter and added to a control, the `Select all` option is not
                available. The following procedure shows a workaround that uses the same example
                scenario from the previous section.

###### Note

This walkthrough is for datasets that are small enough to load in direct
                    query. If you have a large dataset and want to use the `Select All`
                    option, it is recommended that you load the dataset into SPICE. However, if you
                    want to use the `Select All` option with dataset parameters, this
                    walkthrough describes a way to do so.

To begin, let's say you have a direct query dataset with custom SQL that
                contains a multivalue parameter called `States`:

```
select * from all_flights
where origin_state_abr in (<<$States>>)
```
###### To use the Select all option in a control that uses dataset parameters

- 
                    In the **Parameters**pane of the analysis, find the dataset parameter that you want to use and choose**Edit**from the ellipsis (three dots) next to the parameter.
- 
                    In the **Edit parameter**window that appears, enter a new default value in the**Static multiple default values**section. In our example, the default value is`All States`. Note that the example uses a leading space character so that the default value appears as the first item in the control.
- 
                    Choose **Update**to update the parameter.
- 
                    Navigate to the dataset that contains the dataset parameter that you're using in the analysis-by-analysis. Edit the custom SQL of the dataset to include a default use case for your new static multiple default values. Using the `All States`example, the SQL expression appears as follows:`select * from public.all_flights where ' All States' in (<<$States>>) or origin_state_abr in (<<$States>>)`If the user chooses `All States`in the control, the new SQL expression returns all unique records. If the user chooses a different value from the control, the query returns values that were filtered by the dataset parameter.

### Using controls with Select all and multivalue options

You can combine the previous `Select all` procedure with the
                    multivalue control method discussed earlier to create dropdown controls that
                    contain a `Select all` value in addition to multiple values that the
                    user can select. This walkthrough assumes that you have followed the previous
                    procedures, that you know how to map dataset parameters to analysis parameters,
                    and that you can create controls in an analysis. For more information on mapping
                    analysis parameters, see [Mapping dataset parameters in new Quick analyses](./dataset-parameters-analysis.html#dataset-parameters-map-to-analysis). For more information
                    on creating controls in an analysis that is using dataset parameters, see [Adding filter controls to mapped analysis parameters](./dataset-parameters-analysis.html#dataset-parameters-analysis-filter-control).

###### To add multiple values to a control with a Select all option and a mapped dataset parameter

- 
                        Open the analysis that has the original dataset with a `Select all`custom SQL expression and a second dataset that includes all possible values of the filtered column that exists in the original dataset.
- 
                        Navigate to the secondary dataset that was created earlier to return all values of a filtered column. Add a custom SQL expression that adds your previously configured `Select all`option to the query. The following example adds the`All States`record to the top of the list of returned values of the dataset:`(Select ' All States' as origin_state_abr) Union All (SELECT distinct origin_state_abr FROM all_flights order by origin_state_abr asc)`
- 
                        Go back to the analysis that the datasets belong to and map the dataset parameter that you are using to the analysis parameter that you created in step 3 of the previous procedure. The analysis parameter and dataset parameter can have the same name. In our example, the analysis parameter is called `States`.
- 
                        Create a new filter control or edit an existing filter control and choose **Hide Select All**to hide the disabled**Select All**option that appears in multivalue controls.

Once you create the control, users can use the same control to select all or multiple values of a filtered column in a dataset.