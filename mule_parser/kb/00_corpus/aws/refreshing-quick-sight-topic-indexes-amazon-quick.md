# Refreshing Quick Sight topic indexes - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topics-index.html](https://docs.aws.amazon.com/quick/latest/userguide/topics-index.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick administrators and authors | 

When you create a topic, Quick Sight creates, stores, and maintains an index with definitions for data in that topic. This index isn't exposed to Quick Sight authors. It's not a copy of the datasets included in a topic either. Metrics are not indexed. For example, measures stored as integers are not indexed.

The topic index is an index of unique string values for fields included in a topic. This index is used to generate correct answers, provide autocomplete suggestions when someone asks a question, and suggest mappings of terms to columns or data values.

To refresh a topic index, refresh the datasets in the topic. You can manually refresh
            all datasets in a topic or refresh an individual dataset. You can also view dataset
            refresh history to monitor past refreshes, and set a recurring refresh schedule for
            every dataset in the topic. For SPICE datasets, you can sync the topic
            index refresh schedule with the SPICE refresh schedule. For more
            information about setting SPICE refresh schedules, see [Refreshing a dataset on a schedule](./refreshing-imported-data.html#schedule-data-refresh).

###### Note

Currently, hourly refresh schedules aren't supported. You can set a refresh schedule to refresh datasets in a topic up to once a day.

We recommend that you update topic indexes regularly to ensure that the latest definitions and values are recorded. Updating a topic index takes approximately 15 to 30 minutes, depending on the number and size of datasets included in the topic.

###### To refresh a topic index

- 
                On the Quick start page, choose **Topics**.
- 
                On the **Topics**page that opens, open the topic that you want to refresh.The topic opens to the **Summary**tab, which shows the datasets that are included in the topic at page bottom. It also shows when the last time the topic was refreshed at upper right.
- 
                Choose **Refreshed**at upper right to refresh the topic index, and then choose**Refresh data**. Doing this manually refreshes all datasets in the topic.For more information about refreshing individual datasets in a topic, see [Refreshing datasets in a Quick Sight topic](./topics-data-refresh.html).