# Replacing datasets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/replacing-data-sets.html](https://docs.aws.amazon.com/quick/latest/userguide/replacing-data-sets.html)

---

In an analysis, you can add, edit, replace, or remove datasets. Use this section to learn how to replace your dataset.

When you replace a dataset, the new dataset should have similar columns, if you expect the visual to work the way you designed it. Replacing the dataset also clears the undo and redo history for the analysis. This means you can't use the undo and redo buttons on the application bar to navigate your changes. So, when you decide to change the dataset, your analysis design should be somewhat stable—not in the middle of an editing phase.

###### To replace a dataset

- 
					On the analysis page, navigate to the **Data**pane and expand the**Dataset**dropdown.
- 
					Choose **Manage datasets**.
- 
					Choose the ellipsis (three dots) next to the dataset that you want to replace, and then choose **Replace**.
- 
					In the **Select replacement dataset**page, choose a dataset from the list, and then choose**Select**.###### NoteReplacing a dataset clears the undo and redo history for this analysis. 

The dataset is replaced with the new one. The field list and visuals are updated with the new dataset.

At this point, you can choose to add a new dataset, edit the new dataset, or
				replace it with a different one. Choose **Close** to exit. 

## If your new dataset doesn't match

				In some cases, the selected replacement dataset doesn't contain all of the fields and hierarchies used by the visuals, filters, parameters, and calculated fields in your analysis. If so, you receive a warning from Quick Sight that shows a list of mismatched or missing columns.

If this happens, you can update the field mapping between the two datasets.

###### To update the field mapping

- 
						In the **Mismatch in replacement dataset**page, choose**Update field mapping**.
- 
						In the **Update field mapping**page, choose the drop-down menu for the field(s) you want to map and choose a field from the list to map it to.If the field is missing from the new dataset, choose **Ignore this field**.
- 
						Choose **Confirm**to confirm your updates.
- 
						Choose **Close**to close the page and return to your analysis.

The dataset is replaced with the new one. The fields list and visuals are updated with the new dataset.

Any visuals that were using a field that's now missing from the new dataset update to blank. You can readd fields to the visual or remove the visual from your analysis.

If you change your mind after replacing the dataset, you can still recover. Let's say you replace the dataset and then find that it's too difficult to change your analysis to match the new dataset. You can undo any changes you made to your analysis. You can then replace the new dataset with the original one, or with a dataset that more closely matches the requirements of the analysis.