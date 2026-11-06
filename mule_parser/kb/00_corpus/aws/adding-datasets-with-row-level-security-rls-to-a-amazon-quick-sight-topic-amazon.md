# Adding datasets with row-level security (RLS) to a Amazon Quick Sight topic - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topics-data-rls.html](https://docs.aws.amazon.com/quick/latest/userguide/topics-data-rls.html)

---

You can add datasets that contain row-level security (RLS) to topics. All fields in a topic respect the RLS rules applied to your dataset. For example, if a user asks, "show me sales by region," the data that is returned is based on the user's access to the underlying data. So, if they're only allowed to see the East region, only data for the East region appears in the answer.

RLS rules are applied to automatic suggestions when users are asking questions. As users enter questions, only the values that they have access to are suggested to them. If a user enters a question about a dimensional value that they don't have access to, they do not get an answer for that value. For example, suppose that the same user is entering the question, "show me sales in the West region." In this case, they do not get a suggestion or an answer for it, even if they ask, because they don't have RLS access to that region.

By default, Quick Sight allows users to ask questions regarding fields based on the user's permissions in RLS. Continue to use this option if your field contains sensitive data that you want to restrict access to. If your fields don't contain sensitive information and you want all users to see the information in suggestions, then you can choose to allow questions for all values in the field.

###### To allow questions for all fields

- 
                    From the Quick homepage, choose **Data**.
- 
                    Under the **Datasets**tab, choose the dataset that you added RLS to, and then choose**Edit dataset**.For more information about adding RLS to a dataset, see [Using row-level security in Amazon Quick](./row-level-security.html).
- 
                    On the data preparation page, choose the field menu (the three dots) for a field that you want to allow , and then choose **Row level security**.
- 
                    On the **Row level security for Quick**page that opens, choose**Allow users to ask questions regarding all values on this field**.
- 
                    Choose **Apply**.
- 
                    When finished editing the dataset, choose **Save & publish**in the blue toolbar at upper right.
- 
                    Add the dataset to your topic. For more information, see the previous section, [Adding datasets to a topic in Amazon Quick Sight](./topics-data-add.html).

If you currently allow users to ask questions regarding all values, but want to
                implement the dataset's RLS rules to protect sensitive information, then repeat
                steps 1–4 and choose **Allow users to ask questions regarding this
                    field based on their permissions**. When you are done, refresh the
                dataset in your topic. For more information, see [Refreshing datasets in a Quick Sight topic](./topics-data-refresh.html).