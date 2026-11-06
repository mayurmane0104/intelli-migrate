# Adding dataset parameters to filters - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-dataset-filters.html](https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-dataset-filters.html)

---

For datasets in direct query mode, dataset authors can use dataset parameters in filters without custom SQL. Dataset parameters can't be added to filters if the dataset is in SPICE.

###### To add a dataset parameter to a filter

- 
                Open the dataset page of the dataset that you want to create a filter for. Choose **Filters**on the left, and then choose**Add filter**.
- 
                Enter the name that you want the filter to have and choose the field that you want filtered in the dropdown. 
- 
                After you create the new filter, navigate to the filter in the **Filters**pane, choose the ellipsis (three dots) next to the filter, and then choose**Edit**.
- 
                For **Filter type**, choose**Custom filter**.
- 
                For **Filter condition**, choose the condition that you want.
- 
                Select the **Use parameter**box and choose the dataset parameter that you want the filter to use.
- 
                When you are finished making changes, choose **Apply**.