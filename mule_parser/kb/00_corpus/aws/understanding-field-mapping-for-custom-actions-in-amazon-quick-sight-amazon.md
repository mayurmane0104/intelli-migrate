# Understanding field mapping for custom actions in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quicksight-actions-field-mapping.html](https://docs.aws.amazon.com/quick/latest/userguide/quicksight-actions-field-mapping.html)

---

Automated field mapping is based on identical fields. Fields with the same name and data type map automatically across datasets. Their field names and data types must be an exact match. This works similar to a join, except that it is automatically generated based on names and data types for every matching field. If you are missing fields, you can create them by using calculated fields in the dataset that's missing a field. If you don't want to have some of the fields mapped to each other, you can rename or remove them from the dataset.

It's important to make sure that all target fields are mapped if they are
                enabled for use with a filter action (in the **Filter scope**).
                Doing this allows filtering to apply automatically. If some target fields
                aren't mapped, the automatic filtering doesn't work.

Mapping is generated only when you create or save a custom action. So after every change that affects the mapping, make sure to return to it and save it again. When you create an action, mapping is based on the fields as they exist at that point. When you save an action, any mapped fields that you renamed since you created the custom action stay mapped. However, if you alter the data type of a mapped field, the mapping is removed.

If your mapping is missing some fields, you can do one of the following to fix it:

- 
                    Only target the mapped fields, by removing the unmapped fields from the **Filter scope.**
- 
                    Remove the visual in question from the target visuals. 
- 
                    Create calculated fields to supply the missing fields for the mapping, and then save your custom action. 
- 
                    Edit the dataset and rename the fields or change their data types, and then save your custom action. 
- 
                    Edit the dataset and rename the fields or change their data types, and then resave your custom action. 

###### Note

The information that displays on the mapping screen shows the configuration from the most recent time you saved it. To refresh or update the view, save the action again.

If you add or edit datasets, they aren't automatically mapped or remapped. This causes the filtering to work incorrectly. For example, suppose that you add a new dataset, then create visuals for it. The new visuals won't respond to filter actions, because there is no field mapping to connect them. When you make changes, remember to save your custom actions again to redo the field mappings.

If you remove a parameterized field or any other targeted field from the source visual, the action that uses it breaks. The action for the missing field either doesn't work when you select a data point, or it's hidden from the context menu.

For information about preparing your dataset for automated field mapping, see
                    [Mapping fields](./mapping-and-joining-fields.html#mapping-and-joining-fields-automatic).