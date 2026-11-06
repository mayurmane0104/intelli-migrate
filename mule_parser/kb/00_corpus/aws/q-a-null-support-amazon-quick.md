# Q&A null support - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-q-and-a-null-support.html](https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-q-and-a-null-support.html)

---

Amazon Quick Sight Q&A has comprehensive support for null value handling, enabling users to create more sophisticated analyses and answer complex business questions. This functionality allows for precise filtering of null values, intuitive queries about missing data, and dynamic chart interactions.

## Add a filter to include or exclude null values

            
            ###### To add a filter to include or exclude null values

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Topics**and then open the topic you want to add a filter to.
- 
                    Choose the **Data**tab.
- 
                    Under **Data Fields**, choose**Add filter**.
- 
                    On the **Filter configuration**page that opens, do the following:- 
                            For **Name**, enter a name for the filter.
- 
                            For **Dataset**, choose a dataset that you want to apply the filter to.
- 
                            For **Field**, choose the field that you want to filter for.
- 
                            For **Null Option**, choose one of the dropdown options:- 
                                    **No null option selected**- No option is selected to filter nulls.
- 
                                    **Include nulls only**- Filter for only nulls on the field selected.
- 
                                    **Exclude nulls only**- Filter for only non nulls on the field selected.
 
- 
                                    
- 
                            (Optional) To specify when the filter is applied, choose **Apply the filter anytime the dataset is used**, and then choose one of the following:- 
                                    **Apply always**- Filter is applied whenever a column from the specified dataset is linked to a question.
- 
                                    **Apply always, unless a question results in an explicit filter from the dataset**- Filter is applied whenever a column from the specified dataset is linked to a question, unless the question contains its own explicit filter for the same field.
 
- 
                                    
- 
                            Choose **Save**.
 
- 
                            

The filter is added to the list of fields in the topic. You can edit the description for it or adjust it when the filter is applied.

## Ask a question on null values

            
            You can use Q&A to directly ask questions about null values, such as:

- 
                    What is the total sales amount for records where the segment is null? 
- 
                    Display accounts without assigned representatives. 
- 
                    List projects with no completion date. 
- 
                    Show inventory items without category assignments. 
- 
                    What percentage of total orders have non null values in the license field by segment? 
- 
                    Which orders do not have a customer assigned? 

## Manage null values in visualizations

            
            After generating visualizations through the Q&A bar, you can interact with the charts using various null value actions, including focusing only on null values or excluding null values. These chart actions help you analyze and filter your data dynamically based on null value presence.

Choose either **Focus only on null** or **Exclude null**
                to appropriately filter the results.

![Data visualization showing 6 unique contact names each associated with 3 segments, displayed in bar chart and table format.](/images/quick/latest/userguide/images/focus-on-null.png) 

                 
                 
            ## Refine query interpretations for null value handling

            
            Once the visualizations are generated based on your query, you can adjust how null values are handled.

- 
                    Locate the **Interpreted as**section below your query.
- 
                    Select the field you wish to modify. 
- 
                    From the dropdown menu, choose **Null Options**to adjust null value handling.

![Analytics dashboard showing total Energy sector sales of 298,474.41 with breakdown by segment.](/images/quick/latest/userguide/images/interpreted-as.png) 

                 
                 
            For categorical fields, empty values are not the same as null values. To convert empty values into nulls:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Topics**and then open the topic you want to add a filter to.
- 
                    Choose the **Data**tab.
- 
                    Choose **Add calculated field**.
- 
                    Enter a name for the **Add name**field.
- 
                    Choose a categorical field and enter an expression to convert empty values to null values: `ifelse({Segment}="",NULL,{Segment})`.
- 
                    Choose **Save**.