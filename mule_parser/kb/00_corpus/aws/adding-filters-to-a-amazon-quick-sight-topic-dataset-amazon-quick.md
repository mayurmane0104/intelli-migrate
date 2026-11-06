# Adding filters to a Amazon Quick Sight topic dataset - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/topics-data-filters.html](https://docs.aws.amazon.com/quick/latest/userguide/topics-data-filters.html)

---

Sometimes your business users (readers) might ask questions that contain terms
                that map to multiple cells of values in the data. For example, let's say one of
                your readers asks, "Show me weekly sales trend in the west."
                    *West* in this instance refers to both the
                    `Northwest` and `Southwest` values in the
                    `Region` field, and requires the data to be filtered to generate an
                answer. You can add filters to a topic to support requests like these.

###### To add a filter to a topic

- 
                    Open the topic that you want to add a filter to. 
- 
                    In the topic, choose the **Data**tab.
- 
                    For **Actions**, choose**Add filter**.
- 
                    In the **Filter configuration**page that opens, do the following:- 
                            For **Name**, enter a friendly name for the filter.
- 
                            For **Dataset**, choose a dataset that you want to apply the filter to.
- 
                            For **Field**, choose the field that you want to filter.Depending on the type of field you choose, you're offered different filtering options. - 
                                    If you chose a text field (for example, `Region`), do the following:- 
                                            For **Filter type**, choose the type of filter that you want.For more information about filter text fields, see [Adding text filters](./add-a-text-filter-data-prep.html).
- 
                                            For **Rule**, choose a rule.
- 
                                            For **Value**, enter one or more values.
 
- 
                                            
- 
                                    If you chose a date field (for example, `Date`), do the following:- 
                                            For **Filter type**, choose the type of filter that you want, and then enter the date or dates that you want to apply the filter to.For more information about filtering dates, see [Adding date filters](./add-a-date-filter2.html).
 
- 
                                            
- 
                                    If you chose a numeric field (for example, `Compensation`), do the following:- 
                                            For **Aggregation**, choose how you want to aggregate the filtered values.
- 
                                            For **Rule**, choose a rule for the filter, and then enter a value for that rule.
 For more information about filtering numeric fields, see [Adding numeric filters](./add-a-numeric-filter-data-prep.html).
- 
                                            
 
- 
                                    
- 
                            (Optional) To specify when the filter is applied, choose **Apply the filter anytime the dataset is used**, and then choose one of the following:- 
                                    **Apply always**– When you choose this option, the filter is applied whenever any column from the dataset you specified is linked to a question.
- 
                                    **Apply always, unless a question results in an explicit filter from the dataset**– When you choose this option, the filter is applied whenever any column from the dataset you specified is linked to a question. However, if the question mentions an explicit filter on the same field, the filter isn't applied.
 
- 
                                    
- 
                            When finished, choose **Save**.The filter is added to the list of fields in the topic. You can edit the description for it or adjust when the filter is applied. 
 
-