# Filtering data at runtime for Amazon Quick Sight embedded dashboards and visuals - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedding-runtime-filtering.html](https://docs.aws.amazon.com/quick/latest/userguide/embedding-runtime-filtering.html)

---

You can use filter methods in the Amazon Quick Sight embedding SDK to leverage the power of Amazon Quick Sight filters within your software as a service (SaaS) application at runtime. Runtime filters allow business owners to integrate their application with their embedded Amazon Quick Sight dashboards and visuals. To accomplish this, create customized filter controls in your application and apply filter presets based on data from your application. Then, developers can personalize filter configurations for end users at runtime.

Developers can create, query, update, and remove Amazon Quick Sight filters on an
                embedded dashboard or visual from their application with the Amazon Quick Sight
                Embedding SDK. Create Amazon Quick Sight filter objects in your application with the
                    [FilterGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterGroup.html)
                data model and apply them to embedded dashboards and visuals using the filter
                methods. For more information about using the Amazon Quick Sight Embedding SDK, see
                the [amazon-quicksight-embedding-sdk](https://github.com/awslabs/amazon-quicksight-embedding-sdk) on GitHub.

**Prerequisites**

Before you can get started, make sure that you are using the Amazon Quick Sight Embedding SDK version 2.5.0 or higher.

## Terminology and concepts

                The following terminology can be useful when working with embedded runtime filtering.

- 
                        *Filter group*– A group of individual filters. Filters that are located within a`FilterGroup`are OR-ed with each other. Filters within a[FilterGroup](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FilterGroup.html)are applied to the same sheets or visuals.
- 
                        *Filter*– A single filter. The filter can be a category, numeric, or datetime filter type. For more information on filters, see[Filter](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Filter.html).

## Setting up

                Before you begin, make sure that you have the following assets and information prepared.

- 
                        The sheet ID of the sheet that you want to scope the `FilterGroup`to. This can be obtained with the`getSheets`method in the Embedding SDK.
- 
                        The dataset and column identifier of the dataset that you want to filter. This can be obtained through the [DescribeDashboardDefinition](https://docs.aws.amazon.com/APIReference/API_DescribeDashboardDefinition.html)API operation.Depending on the column type that you use, there might be restrictions on the types of filters that can be added to an embedded asset. For more information on filter restrictions, see [Filter](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_Filter.html).
- 
                        The visual ID of the visual that you want to scope the `FilterGroup`to, if applicable. This can be obtained by using the`getSheetVisuals`method in the Embedding SDK.In addition to the `getSheetVisuals`method, the`FilterGroup`that you add can only be scoped to the currently selected sheet.

To use this feature, you must already have a dashboard or visual embedded into
                    your application through the Amazon Quick Sight Embedding SDK. For more
                    information about using the Amazon Quick Sight Embedding SDK, see the [amazon-quicksight-embedding-sdk](https://github.com/awslabs/amazon-quicksight-embedding-sdk) on GitHub.

## SDK method interface

                **Dashboard embedding getter methods**

The following table describes different dashboard embedding getter methods that developers can use.

| Method | Description | 
|---|---|
| 
 | Returns all FilterGroups that are currently scoped to the sheet that is supplied in the parameter. | 
| 
 | Returns all  | 

If the sheet that is supplied in the parameter is not the currently selected sheet of the embedded dashboard, the above methods return an error.

**Visual embedding getter methods**

The following table describes different visual embedding getter methods that developers can use.

| Method | Description | 
|---|---|
| 
 | Returns all  | 

**Setter methods**

The following table describes different setter methods that developers can use for dashboard or visual embedding.

| Method | Description | 
|---|---|
| 
 | Adds and applies the supplied
                                             | 
| 
 | Updates the  | 
| 
 | Removes the supplied FilterGroups from the dashboard and
                                        returns a  | 

The `FilterGroup` that is supplied must be scoped to the embedded
                    sheet or visual that is currently selected.