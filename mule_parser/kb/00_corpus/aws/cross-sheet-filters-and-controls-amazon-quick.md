# Cross-sheet filters and controls - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/cross-sheet-filters.html](https://docs.aws.amazon.com/quick/latest/userguide/cross-sheet-filters.html)

---

Cross-sheet filters and controls are filters that are scoped to either your entire analysis or dashboard or multiple sheets within your analysis and dashboard.

## Filters

			###### Creating a Cross-Sheet Filter

- 
					Once you have [Added a filter](https://docs.aws.amazon.com/quicksight/latest/user/add-a-filter-data-prep.html#add-a-filter-data-prep-analyses), you update the scope of the filter to cross-sheet. By default, this applies to all of the the sheets in your analysis.
- 
					If the **Apply cross-datasets**box is checked, then the filter will be applied to all visuals from up to 100 different datasets that are applicable to all sheets in the filter scope.
- 
					If you want to customize the sheets that it is applied to, then choose the Cross-sheet icon. You can then view the sheets the filter is currently applied to or toggle on the custom select sheets. 
- 
					When you enable **Custom select sheets**, you can select which sheets to apply the filter to.
- 
					Follow the steps at [Editing filters in analyses](https://docs.aws.amazon.com/quicksight/latest/user/edit-a-filter-data-prep.html#edit-a-filter-data-prep-analyses). Your changes will be applied to all of the filters for all of the sheets you have selected. This includes newly added sheets if the filter is scoped to your entire analysis.

**Removing a Cross-Sheet Filter**

**Deleting**

If you have no controls created from these filters, see [Deleting filters in analyses](https://docs.aws.amazon.com/quicksight/latest/user/delete-a-filter-data-prep.html#delete-a-filter-data-prep-analyses).

If you have controls created then:

- 
					Follow the instructions at [Deleting filters in analyses](https://docs.aws.amazon.com/quicksight/latest/user/delete-a-filter-data-prep.html#delete-a-filter-data-prep-analyses).
- 
					If you choose **Delete Filter and Controls**, the controls will be deleted from all pages. This may impact the layout of your analysis. Alternatively, you can remove these controls individually.

**Downscoping**

If you want to remove a cross-sheet filter, you can also do this by changing the filter scope:

- 
					Follow the instructions at [Editing filters in analyses](https://docs.aws.amazon.com/quicksight/latest/user/edit-a-filter-data-prep.html#edit-a-filter-data-prep-analyses)to get to the filter.
- 
					One of the edits you can make is changing the scope. You can switch to **Single sheet**or**Single visual**. You can also remove a sheet from the Cross-sheet selection.Or the custom sheet selection: ![This is an image of Delete Filter in Quick Sight.](/images/quick/latest/userguide/images/cross-sheet-7.png)  
- 
					If there are controls, you will see a modal to warn you that you will be bulk-removing controls from any of the sheets where the filter no longer applies and this can impact your layout. You can also remove the controls individually. For more information, see [Removing a Cross-Sheet Control](#cross-sheet-removing-control).
- 
					If you add controls to the **Top of all sheets in filter scope**then new sheets will by default be added with this new control if the filter is scoped to your entire analysis.

## Controls

			 
				### Creating a Cross-Sheet Control

**New filter control**

- 
						Create a cross-sheet filter. For more information, see [Filters](#filters).
- 
						From the three-dot menu, you can see an option that says **Add control**. Hovering over this, you will see three options:- 
								**Top of all sheets in filter scope**
- 
								**Top of this sheet**
- 
								**Inside this sheet**
 If you want to add to multiple-sheets within the sheets themselves, you can do that sheet-by-sheet. Or you can add to the top and then use the option on each control to **Move to sheet**. For more information, see[Editing a Cross-Sheet Control](#cross-sheet-controls-editing-control).
- 
								

**Increasing Scope of Existing Control**

- 
						Navigate to the existing filter in the analysis 
- 
						Change the scope of what sheets this filter is **Applied to**to**Cross-sheet**.
- 
						If there is already a control created from the filter, you will see a modal, which if you check the box will bulk-add controls to the top of all the sheets in the filter scope. This will not impact the position of the already created control if it is on the sheet. 

### Editing a Cross-Sheet Control

- 
						Go to the cross-sheet control and select the three-dot menu if the control is pinned to the top or the edit pencil icon if the control is on the sheet. You will be presented with the following options: - 
								**Go to filter**(which directs you to the cross-sheet filter for you to edit or review
- 
								**Move to sheet**(which moves the control into the analysis pane)
- 
								**Reset**
- 
								**Refresh**
- 
								**Edit**
- 
								**Remove**
 
- 
								
- 
						Choose **Edit**. This brings up the**Format Control**pane on the right side of your analysis.
- 
						You can then edit your control. The top section labeled **Cross-sheet settings**will apply to all controls, whereas any settings outside of this section are not applicable to all controls and only to the specific control you’re editing. For instance,**Relevant value**is not a cross-sheet control setting.
- 
						You can also see the sheets that this control is on as well as the location (Top or Sheet) that the control is on for each sheet. You can do this by choosing **Sheets(8)**.

### Removing a Cross-Sheet Control

You can remove controls in two places. First, from the control:

- 
						Go to the cross-sheet control and select the three-dot menu if the control is pinned to the top or the edit pencil icon if the control is on the sheet. You will be presented with the following options: - 
								**Go to filter**(which directs you to the cross-sheet filter for you to edit or review
- 
								**Move to sheet**(which moves the control into the analysis pane)
- 
								**Reset**
- 
								**Refresh**
- 
								**Edit**
- 
								**Remove**
 
- 
								
- 
						Choose **Remove**

Second, you can remove controls from the filter:

- 
						Choose the three-dot menu on the cross-sheet filter that the cross-sheet controls are created from. You will see that instead of an option to **Add control**there is now an option to**Manage control**.
- 
						Hover over **Manage control**. You will be presented with the following options:- 
								**Move inside this sheet**
- 
								**Top of this sheet**
 These options are applicable to just the control on the sheet, depending on where the current control is. If you don’t have controls on all of the sheets within the filter scope, you will get the option to **Add to top of all sheets in filter scope**. This will not move sheet controls to the top of the sheet if you have already added them to the sheet in the analysis. You will also get the option to**Remove from this sheet**or**Remove from all sheets**.
-