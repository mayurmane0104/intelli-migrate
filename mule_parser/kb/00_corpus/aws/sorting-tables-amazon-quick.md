# Sorting tables - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/table-sort.html](https://docs.aws.amazon.com/quick/latest/userguide/table-sort.html)

---

In Amazon Quick, you can sort values in a table by fields in the columns headers
				of the table or with the **Sort visual** tool. You can sort up to
				10 columns in a single table. Quick can also use an off-visual sort You
				can sort columns in an **Ascending** or a
					**Descending** order. The following image shows the
					**Sort visual** icon and pop over.

![The Sort visual icon and the Sort visual pop over that it opens.](/images/quick/latest/userguide/images/table-sort-icon.png) 

				 
				 
			## Single column sort options

				Quick Authors can access single column sort options from the field
					wells, the column headers, or from the **Sort visual** menu.
					Use the procedure below to use set up a single column sort on a table in
					Quick.

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
						Open the analysis that you want to work in and navigate to the table that you want to sort. 
- 
						Choose the header of the column that you want to sort. 
- 
						For **Sort by**, choose the arrow icon, and then choose the field that you want to sort by.

You can also set up a single column sort in the **Sort
						visual** menu. To access the sort visual menu, choose the
						**Sort visual** icon in the on-visual menu. In the
						**Sort visual** menu, choose the field that you want to
					sort by, and then choose if you want the sort in an ascending or descending
					order. By default, new sorts are sorted in an ascending order. When you are
					finished, choose **APPLY**.

Tables that use single column sorting are sorted one column at a time. When a user chooses a new column to sort by, the previous sort order is overridden.

To make changes to a single column sort, open the **Sort
						visual** menu annd use the dropdown menus to choose a new field or
					sort order. When you are finished with your changes, choose
						**APPLY**.

To reset a table to its original state, open the **Sort
						visual** menu and choose **RESET**.

## Multi column sort options

				Quick authors can access multi column sort options from the
						**Sort visual** menu. Use the procedure below to set up a
					multi column sort for a table.

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
						Open the analysis that you want to work in and navigate to the table that you want to sort. 
- 
						Choose the **Sort visual**icon to open the**Sort visual**menu.- 
								Alternatively, choose a header that you want to sort. 
- 
								For **Sort by**, choose the arrow icon, and then choose**Multiple fields**.
 
- 
								
- 
						In the **Sort visual**menu that opens, choose a field from the**Sort by**dropdown, and then choose whether you want the field sorted in an ascending or descending order.
- 
						To add another sort, choose **ADD SORT**, and repeat the workflow from Step 4. You can add up to 10 sorts to each table.
- 
						When you are finished, choose **APPLY**.

Columns are sorted in the order that they are added to the **Sort
						visual** menu. To change the order that columns are sorted by, open
					the **Sort visual** menu and use the **Sort
						by** dropdowns to reorder the sorts. When you are finished, choose
						**APPLY** to apply the new sort order to the table.

To reset a table to its original state, open the **Sort
						visual** menu and choose **RESET**.

## Off visual sort options

				Quick authors can configure an off-visual sort to sort the values in a table by a field and aggregation that is a part of the dataset that the table uses but not in one of the table's field wells. One off-field sort can be configured to a single table at a time.

Use the procedure below to configure an off-visual sort.

###### To add an off-visual sort to a table

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
						Open the analysis that you want to work in and navigate to the table that you want to sort. 
- 
						Choose the header of any column in the table. 
- 
						For **Sort by**, choose the arrow icon, and then choose**Off-visual field**.
- 
						In the **Off-visual field**pane that appears, open the**Sort by**dropdown menu and choose the field that you want to sort.
- 
						For **Aggregation**open the dropdown menu and choose the aggregation that you want to use.
- 
						For **Sort order**, choose if you want the sort to be in an ascending or descending order.
- 
						When you are finished, choose **Apply**.

After a off-visual sort is applied to a table, the sort is shown in the
						**Sort visual** menu. The sort order of a table that
					contains an off-visual sort depends on the sort configuration of the table when
					the off-visual sort is added. If an off-visual sort is added to a table that
					already has a single or multi column sort configured, the off-visual sort
					overrides all other sorts. If the off-visual sort is applied before single or
					multi column sorts, you can add and reorder more sorts to the table.