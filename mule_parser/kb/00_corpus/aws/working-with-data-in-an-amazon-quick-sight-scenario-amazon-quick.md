# Working with data in an Amazon Quick Sight scenario - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/scenarios-data.html](https://docs.aws.amazon.com/quick/latest/userguide/scenarios-data.html)

---

When you create a scenario in Amazon Quick Sight, you can preview and modify the data that the scenario uses to generate summaries. Use the following sections to learn about the ways Quick users can interact with data in a scenario.

## Adding more data to a scenario

            After you create a scenario in Amazon Quick Sight, you can add more data to the scenario at any time. Use the following procedure to add data to an Amazon Quick Sight scenario.

###### To add data to an existing Amazon Quick Sight scenario

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Scenarios**from the options pane, and then choose the scenario that you want to add more data to.
- 
                    Choose the **Data Source**icon in the actions bar to open the**Data**pane.
- 
                    Perform one of the following actions: - 
                            To add Quick Sight data to the scenario, choose **Find Data**, and then choose the dataset or dashboard visuals that you want to add to the scenario. After you have selected all of the Quick Sight data that you want to add to the scenario, choose**Add**.
- 
                            To upload a file from your computer to the scenario, choose **Upload File**.
 The following limits apply to the data that is added to a scenario: - 
                            You can add up to 10 data sources to a scenario. 
- 
                            Up to 20 visuals can be selected from a dashboard at a time. 
- 
                            Uploaded files must be in `.xlsx`or`.csv`format and can't exceed 1 GB.
- 
                            Data sources can have up to 200 columns. 
 
- 
                            

After you add new data to a scenario, Amazon Q includes the data in all new analyses.

## Editing data in a preview

            When you choose data from a Quick Sight dashboard to be used in a scenario, a preview of the data is generated for review before it's added to the analysis. If needed, the following changes can be made to dashboard data in the preview state:

- 
                    **Filters**– If you only want to analyze a subset of the available data or if you need to reduce the number of rows that are included in the scenario, you can apply filters to the data.
- 
                    **Sort**– If the available data exceeds 1 million rows and you want to prioritize the retention of the values in a specific column, you can sort the data to fit your needs.

## Editing data in a snapshot

            When you add dashboard or external data to a scenario, Quick Sight creates a
                snapshot of the data sources to be reviewed. To see a snapshot of the data used in a
                scenario, choose the **Data Source** icon in the actions bar. This
                opens the **Data** pane, and then you can choose the data snapshot
                that you want to review.

You can perform the following actions on a data snapshot:

- 
                    To update the title of the data snapshot, choose the pencil icon next to the title and enter a new title for the snapshot. 
- 
                    Choose the **Filter**icon to filter the data that is used in the scenario. This option can be used if you want the scenario to only use a subset of the data that is added to the scenario.
- 
                    Choose the **Sort**icon to sort the data that is used in the scenario. This option can be used to prioritize the retention of specific columns if the data exceeds 1 million rows.
- 
                    Choose the **Fields list**icon to choose which fields are included in the scenario. This option can be used to control which columns are used in the scenario.

When you are finished updating the scenario data, close the
                    **Data** pane.