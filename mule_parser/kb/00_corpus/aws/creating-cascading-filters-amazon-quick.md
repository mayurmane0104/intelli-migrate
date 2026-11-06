# Creating cascading filters - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/use-a-cascading-filter.html](https://docs.aws.amazon.com/quick/latest/userguide/use-a-cascading-filter.html)

---

The idea behind cascading any action, such as a filter, is that choices in the higher
			levels of a hierarchy affect the lower levels of a hierarchy. The term
				*cascading* comes from the way that a cascade waterfall flows
			from one tier to the next. 

To set up cascading filters, you need a trigger point where the filter is activated, and target points where the filter is applied. In Quick, the trigger and target points are included in visuals.

To create a cascading filter, you set up an action, not a filter. This approach is
			because you need to define how the cascading filter is activated, which fields are
			involved, and which visuals are filtered when someone activates it. For more
			information, including step-by-step instructions, see [Using custom actions for filtering and navigating](./quicksight-actions.html).

There are two other ways to activate a filter across multiple visuals:

- 
				For a filter that is activated from a widget on a dashboard – The widget is called a *sheet control,*which is a custom menu that you can add to the top of your analysis or dashboard. The most common sheet control is a drop-down list, which displays a list of options to choose from when you open it. To add one of these to your analysis, create a parameter, add a control to the parameter, and then add a filter that uses the parameter. For more information, see[Setting up parameters in Amazon Quick](./parameters-set-up.html),[Using a control with a parameter in Amazon Quick](./parameters-controls.html), and[Adding filter controls to analysis sheets](./filter-controls.html).
- 
				For a filter that always applies to multiple visuals – This is a regular filter, except that you set its scope to apply to multiple (or all) visuals. This type of filter doesn't really cascade, because there is no trigger point. It always filters all the visuals that it's configured to filter. To add this type of filter to your analysis, create or edit a filter and then choose its scope: **Single visual**,**Single sheet**, or**Cross sheets**. Note the option to**Apply cross-datasets**. If this box is checked, then the filter will be applied to all visuals from different datasets that are applicable on all sheets in the filter scope. For more information, see[Filters](./cross-sheet-filters.html#filters).