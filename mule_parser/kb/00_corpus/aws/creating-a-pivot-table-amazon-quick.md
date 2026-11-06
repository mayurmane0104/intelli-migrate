# Creating a pivot table - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-pivot-table.html](https://docs.aws.amazon.com/quick/latest/userguide/create-pivot-table.html)

---

Use the following procedure to create a pivot table.

###### To create a pivot table

- 
					On the analysis page, choose the **Visualize**icon on the tool bar.
- 
					On the **Visuals**pane, choose**+ Add**, and then choose the pivot table icon.
- 
					From the **Fields list**pane, choose the fields that you want to include. Amazon Quick automatically places these into the field wells.To change the placement of a field, drag it to the appropriate field wells. Typically, you use dimension or measure fields as indicated by the target field well. If you choose to use a dimension field as a measure, the **Count**aggregate function is automatically applied to it to create a numeric value.- 
							To create a single-measure pivot table, drag a dimension to the **Rows**field well, a dimension to the**Columns**field well, and a measure to the**Values**field well.
- 
							To create a multi-measure pivot table, drag a dimension to the **Rows**field well, a dimension to the**Columns**field well, and two or more measures to the**Values**field well.
- 
							To create a clustered pivot table, drag one or more dimensions to the **Rows**field well, one or more dimensions to the**Columns**field well, and a measure to the**Values**field well.
 You can also select multiple fields for all of the pivot table field wells if you want to. Doing this combines the multi-measure and clustered pivot table approaches. 
- 
							

###### Note

To view roll-ups for calculated fields, make sure that you are using
					aggregates. For example, a calculated field with ```
field-1 / field-2
					
```
doesn't display a summary when rolled up. However,
						`sum(field-1) / sum(field-2) `does display a roll-up summary.
				

## Choosing a layout

				When you create a pivot table in Amazon Quick, you can further customize the
					way your data is presented with Tabular and Hierarchy layout options. For pivot
					tables that use a tabular layout, each row field is displayed in its own column.
					For pivot tables that use a hierarchy layout, all row fields are displayed in a
					single column. Indentation is used to differentiate row headers of different
					fields. To change the layout of a pivot table visual, open the **Format
						visual** menu of the pivot table that you want to change and choose
					the layout option that you want from the **Pivot options**
					section.

Depending on the layout that you choose for your pivot table visual, different
					formatting options are available. For more information about formatting
					differences between tabular and hierarchy pivot tables, see [Table and pivot table formatting options in Quick](./format-tables-pivot-tables.html).