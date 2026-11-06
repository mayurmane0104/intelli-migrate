# Using dataset parameters in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters.html](https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters.html)

---

In Amazon Quick, authors can use dataset parameters in direct query to dynamically customize
        their datasets and apply reusable logic to their datasets. A *dataset
            parameter* is a parameter created at the dataset level. It's consumed by an
        analysis parameter through controls, calculated fields, filters, actions, URLs, titles, and
        descriptions. For more information on analysis parameters, see [Parameters in Amazon Quick](./parameters-in-quicksight.html). The
        following list describes three actions that can be performed with dataset parameters:

- 
            **Custom SQL in direct query**– Dataset owners can insert dataset parameters into the custom SQL of a direct query dataset. When these parameters are applied to a filter control in a Quick analysis, users can filter their custom data faster and more efficiently.
- 
            **Repeatable variables**– Static values that appear in multiple locations in the dataset page can be modified in one action using custom dataset parameters.
- 
            **Move calculated fields to datasets**– Quick authors can copy calculated fields with parameters in an analysis and migrate them to the dataset level. This protects calculated fields at the analysis level from being accidentally modified and calculated fields be shared across multiple analyses.

In some situations, dataset parameters improve filter control performance for direct query datasets that require complex custom SQL and simplify business logic at the dataset level.

###### Topics

## Dataset parameter limitations

        This section covers known limitations that you might encounter when working with dataset parameters in Amazon Quick.

- 
                When dashboard readers schedule emailed reports, selected controls don't propagate to the dataset parameters that are included in the report that's attached to the email. Instead, the default values of the parameters are used. 
- 
                Dataset parameters can't be inserted into custom SQL of datasets stored in SPICE. 
- 
                Dynamic defaults can only be configured on the analysis page of the analysis that is using the dataset. You can't configure a dynamic default at the dataset level. 
- 
                The **Select all**option is not supported on multivalue controls of analysis parameters that are mapped to dataset parameters.
- 
                Cascading controls are not supported for dataset parameters. 
- 
                Dataset parameters can only be used by dataset filters when the dataset is using direct query. 
- 
                In a custom SQL query, only 128 dataset parameters can be used.