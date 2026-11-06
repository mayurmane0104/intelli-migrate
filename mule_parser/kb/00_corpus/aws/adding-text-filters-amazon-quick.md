# Adding text filters - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/add-a-text-filter-data-prep.html](https://docs.aws.amazon.com/quick/latest/userguide/add-a-text-filter-data-prep.html)

---

When you add a filter using a text field, you can create the following types of text filters:

- 
				**Filter list**(Analyses only) – This option creates a filter that you can use to select one or more field values to include or exclude from all the available values in the field. For more information about creating this type of text filter, see[Filtering text field values by a list (analyses only)](#text-filter-list).
- 
				**Custom filter list**– With this option, you can enter one or more field values to filter on, and whether you want to include or exclude records that contain those values. The values that you enter must match the actual field values exactly for the filter to be applied to a given record. For more information about creating this type of text filter, see[Filtering text field values by a custom list](#add-text-custom-filter-list-data-prep).
- 
				**Custom filter**– With this option, you enter a single value that the field value must match in some way. You can specify that the field value must equal, not equal, starts with, ends with, contains, or does not contain the value you specify. If you choose an equal comparison, the specified value and actual field value must match exactly in order for the filter to be applied to a given record. For more information about creating this type of text filter, see[Filtering a single text field value](#add-text-filter-custom-list-data-prep).
- 
				**Top and bottom filter**(Analyses only) – You can use this option to show the top or bottom*n*value of one field ranked by the values in another field. For example, you might show the top five salespeople based on revenue. You can also use a parameter to allow dashboard users to dynamically choose how many top or bottom ranking values to show. For more information about creating top and bottom filters, see[Filtering a text field by a top or bottom value (analyses only)](#add-text-filter-top-and-bottom).

## Filtering text field values by a list (analyses only)

			In analyses, you can filter a text field by selecting values to include or exclude from a list of all value in the field.

###### To filter a text field by including and excluding values

- 
					Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
					In the **Filters**pane, choose the new filter to expand it.
- 
					For **Filter type**, choose**Filter list**.
- 
					For **Filter condition**, choose**Include**or**Exclude**.
- 
					Choose the field values that you want to filter on. To do this, select the check box in front of each value. If there are too many values to choose from, enter a search term into the box above the checklist and choose **Search**. Search terms are case-insensitive and wildcards aren't supported. Any field value that contains the search term is returned. For example, searching on L returns al, AL, la, and LA.The values display alphabetically in the control, unless there are more than 1,000 distinct values. Then the control displays a search box instead. Each time that you search for the value that you want to use, it starts a new query. If the results contain more than 1,000 values, you can scroll through the values with pagination. 
- 
					When finished, choose **Apply**.

## Filtering text field values by a custom list

			You can specify one or more field values to filter on, and whether you want to include or exclude records that contain those values. The specified value and actual field value must match exactly for the filter to be applied to a given record.

###### To filter text field values by a custom list

- 
					Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
					In the **Filters**pane, choose the new filter to expand it.
- 
					For **Filter type**, choose**Custom filter list**.
- 
					For **Filter condition**, choose**Include**or**Exclude**.
- 
					For **List**, enter a value in the text box. The value must match an existing field value exactly.
- 
					(Optional) To add additional values, enter them in the text box, one per line. 
- 
					For **Null options**choose**Exclude nulls**,**Include nulls**, or**Nulls only**.
- 
					When finished, choose **Apply**.

## Filtering a single text field value

			With the **Custom filter** filter type, you specify a single
				value that the field value must equal or not equal, or must match partially. If you
				choose an equal comparison, the specified value and actual field value must match
				exactly for the filter to be applied to a given record.

###### To filter a text field by a single value

- 
					Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
					In the **Filters**pane, choose the new filter to expand it.
- 
					For **Filter type**, choose**Custom filter**.
- 
					For **Filter condition**, choose one of the following:- 
							**Equals**– When you choose this option, the values included or excluded in the field must match the value that you enter exactly.
- 
							**Does not equal**– When you choose this option, the values included or excluded in the field must match the value that you enter exactly.
- 
							**Starts with**– When you choose this option, the values included or excluded in the field must start with the value that you enter.
- 
							**Ends with**– When you choose this option, the values included or excluded in the field must start with the value that you enter.
- 
							**Contains**– When you choose this option, the values included or excluded in the field must contain the whole value that you enter.
- 
							**Does not contain**– When you choose this option, the values included or excluded in the field must not contain any part of the value that you enter.
 ###### NoteComparison types are case-sensitive. 
- 
							
- 
					Do one of the following: - 
							For **Value**, enter a literal value.
- 
							Select **Use parameters**to use an existing parameter, and then choose a parameter from the list.For parameters to appear in this list, create your parameters first. Usually, you create a parameter, add a control for it, and then add a filter for it. For more information, see [Parameters in Amazon Quick](./parameters-in-quicksight.html).The values display alphabetically in the control, unless there are more than 1,000 distinct values. Then the control displays a search box instead. Each time that you search for the value that you want to use, it starts a new query. If the results contain more than 1,000 values, you can scroll through the values with pagination. 
 
- 
							
- 
					For **Null options**choose**Exclude nulls**,**Include nulls**, or**Nulls only**.
- 
					When finished, choose **Apply**.

## Filtering a text field by a top or bottom value (analyses only)

			You can use a **Top and bottom filter** to show the top or bottom
					*n* value of one field ranked by the values in
				another field. For example, you might show the top five salespeople based on
				revenue. You can also use a parameter to allow dashboard users to dynamically choose
				how many top or bottom ranking values to show.

###### To create a top and bottom text filter

- 
					Create a new filter using a text field. For more information about creating filters, see [Adding filters](./add-a-filter-data-prep.html).
- 
					In the **Filters**pane, choose the new filter to expand it.
- 
					For **Filter type**, choose**Top and bottom filter**.
- 
					Choose **Top**or**Bottom**.
- 
					For **Show top**integer (or**Show bottom**integer), do one of the following:- 
							Enter the number of top or bottom items to show. 
- 
							To use a parameter for the number of top or bottom items to show, select **Use parameters**. Then choose an existing integer parameter.For example, let's say that you want to show the top three salespersons by default. However, you want the dashboard viewer to be able to choose whether to show 1–10 top salespersons. In this case, take the following actions: - 
									Create an integer parameter with a default value. 
- 
									To link the number of displayed items to a parameter control, create a control for the integer parameter. Then you make the control a slider with a step size of 1, a minimum value of 1, and a maximum value of 10. 
- 
									To make the control work, link it to a filter by creating a top and bottom filter on `Salesperson`by`Weighted Revenue`, enable**Use parameters**, and choose your integer parameter.
 
- 
									
 
- 
							
- 
					For **By**, choose a field to base the ranking on. If you want to show the top five salespeople per revenue, choose the revenue field. You can also set the aggregate that you want to perform on the field.
- 
					(Optional) Choose **Tie breaker**and then choose another field to add one or more aggregations as tie breakers. This is useful, in the case of this example, when there are more than five results returned for the top five salespeople per revenue. This situation can happen if multiple salespeople have the same revenue amount.To remove a tie breaker, use the delete icon. 
- 
					When finished, choose **Apply**.