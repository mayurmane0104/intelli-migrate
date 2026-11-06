# Refreshing datasets in a Quick Sight topic - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topics-data-refresh.html](https://docs.aws.amazon.com/quick/latest/userguide/topics-data-refresh.html)

---

When you add a dataset to a topic, you can specify how often you want that dataset to refresh. When you refresh datasets in a topic, the index is refreshed for that topic with any new and updated information.

Your datasets aren't replicated when you add them to a topic. An index of unique string values is created and metrics are not indexed. For example, measures stored as integers are not indexed. Questions asked always fetch the latest sales metrics based on data in your dataset.

For more information about refreshing the topic index, see [Refreshing Quick Sight topic indexes](./topics-index.html)

You can set a refresh schedule for a dataset in a topic, or refresh the dataset manually. You can also see when the data was last refreshed.

###### To set a refresh schedule for a topic dataset

- 
                    Open the topic that you want to change. 
- 
                    On the **Summary**page, choose**Data**. Then, under**Datasets**, expand the dataset that you want to set a refresh schedule for.
- 
                    Choose **Add schedule**, and then do one of the following in the**Add refresh schedule**page that opens.- 
                            If the dataset is a SPICE dataset, select **Refresh topic when dataset is imported into SPICE**.Currently, hourly refresh SPICE datasets aren't supported. SPICE datasets that are set to refresh every hour are automatically converted to a daily refresh. For more information about setting refresh schedules for SPICE datasets, see [Refreshing SPICE data](./refreshing-imported-data.html).
- 
                            If the dataset is a direct query dataset, do the following: - 
                                    For **Timezone**, choose a time zone.
- 
                                    For **Repeats**, choose how often you want the refresh to happen. You can choose to refresh the dataset daily, weekly, or monthly.
- 
                                    For **Refresh time**, enter the time that you want the refresh to start.
- 
                                    For **Start first refresh on**, choose a date that you want start refreshing the dataset on.
 
- 
                                    
 
- 
                            
- 
                    Choose **Save**.

###### To manually refresh a dataset

- 
                    On the topic **Summary**page, choose**Data**. Then, under**Datasets**, choose the dataset that you want to refresh.
- 
                    Choose **Refresh now**.

###### To view refresh history for a dataset

- 
                    On the topic **Summary**page, choose**Data**. Then, under**Datasets**, choose the dataset that you want to see refresh history for.
- 
                    Choose **View history**.The **Update history**page opens with a list of the times the dataset was refreshed.