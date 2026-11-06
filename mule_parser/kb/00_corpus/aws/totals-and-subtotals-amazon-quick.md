# Totals and subtotals - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/format-tables-pivot-tables-totals.html](https://docs.aws.amazon.com/quick/latest/userguide/format-tables-pivot-tables-totals.html)

---

On tables and pivot tables, you can configure the display of totals or subtotals. Tables can display totals at the top or the bottom of the visual. Pivot tables can display totals and subtotals on rows and columns.

## Add totals and subtotals to tables and pivot tables in Quick

				You can add total columns to your table and pivot table visuals. You can also add subtotal columns to your pivot table visuals.

###### To display or hide totals and subtotals for a pivot table

- 
						To display totals, open the **Properties**pane and choose**Total**.- 
								To show totals for rows, toggle the **ROWS**switch on. Totals are displayed on the bottom row of the visual. Choose**Pin totals**to keep the totals visible as you scroll through the table.
- 
								To show totals for columns, toggle the **COLUMNS**switch on. Totals are displayed on the last column of the visual.
 
- 
								
- 
						To display totals, open the **Properties**pane and choose**Subtotal**.- 
								To show subtotals for rows, toggle the **ROWS**switch on. Totals are displayed on the bottom row of the visual.
- 
								To show subtotals for columns, toggle the **COLUMNS**switch on.
- 
								For **Level**, choose one of the following:- 
										Choose **Last**to only show the subtotal of the last field in the chart's hierarchy. This is the default option.
- 
										Choose **All**to show subtotals for every field.
- 
										Choose **Custom**to customize which fields show subtotals.
 
- 
										
 
- 
								

After you add row totals to your table or pivot table visual, you can also choose to position the totals at the top or bottom of the visual. You can also change the position of column totals in pivot tables.

###### To position row or column totals in a table or pivot table

- 
						In the **Properties**pane, choose**Total**.
- 
						(Optional) For **Rows**, choose**Show totals**.
- 
						(Optional) For **Columns**, choose**Show totals**.
- 
						(Optional) In the **Rows**menu, open the**Position**dropdown and choose the position that you want the totals to be displayed. Choose**Top**to position totals at the top of the table, or**Bottom**to position totals at the bottom of the table.
- 
						(Optional) In the **Columns**menu, open the**Position**dropdown and choose the position that you want the totals to be displayed. Choose**Left**to position totals at the left of the table, or**Right**to position totals at the right of the table.

You can't change the position of the subtotals of a pivot table visual. If your pivot table uses a hierarchy layout, the subtotal rows are positioned at the top of the table. Tabular pivot table subtotals are displayed at the bottom of the table.

## Customize labels for totals and subtotals

				You can rename the totals in table and pivot table visuals to provide better context for account readers. By default, the totals and subtotals appear without a label.

###### To rename totals in a table or pivot table visual

- 
						In the **Properties**pane, choose**Total**or**Subtotal**.
- 
						For **Label**, enter a word or short phrase that you want displayed for the total.In pivot tables, you can also add labels to column totals and subtotals. To do so, enter a word or short phrase for **Label**in the**Columns**section.
- 
						(Optional) For tabular pivot tables, you can also add group names to subtotals. To add a group name to row subtotals, choose the **Plus (+)**icon next to the**Label**field to add the group name parameter that you want. You can also enter a word or short phrase to this field.

You can also make changes to the text size and font color of the total and subtotal labels of your table and pivot table visuals.

###### To format totals and subtotals text

- 
						In the **Properties**pane, choose**Total**or**Subtotal**.
- 
						For **Text**, do one or more of the following.- 
								To change the color of the total or subtotal text, choose the color swatch underneath **Text styling**, and then choose the color that you want the table text to be.
- 
								To change the font or font size of the total or subtotal text, open the **Font**or**Font size**dropdown and choose the font or font size that you want.
- 
								To bold, italicize, or underline the total or subtotal text, choose the appropriate icon from the style bar. 
 In pivot tables, you can also add format text for column totals and subtotals. To do so, repeat the above steps in the **Columns**section.
- 
								

## Totals and subtotals background color

				###### To customize the background color for totals and subtotals

- 
						In the **Properties**pane, choose**Total**or**Subtotal**.
- 
						For **Background**, choose the background color icon, and then choose a color. You can choose one of the provided colors, reset the background color to the default color, or create a custom color.In pivot tables, you can also add background colors for column totals and subtotals. To do so, choose a the background color icon for **Background**in the**Columns**section.

## Totals and subtotals borders

				###### To customize the borders for totals and subtotals

- 
						In the **Properties**pane, choose**Total**or**Subtotal**.
- 
						For **Borders**, do one or more of the following:- 
								To customize the type of border that you want, choose a border type icon. You can choose no borders, horizontal borders only, vertical borders only, or all borders. 
- 
								To customize the border thickness, choose a border thickness. 
- 
								To customize the border color, choose the border color icon, and then choose a color. You can choose one of the provided colors, reset the border color to the default color, or create a custom color. 
 In pivot tables, you can also add borders for column totals and subtotals. To do so, repeat the above steps in the **Columns**section.
- 
								

## Applying totals and subtotals styling to cells

				In pivot tables, you can apply any text, background color, and border styling
					you apply to totals to cells in that same column or row. Row subtotals appear
					differently depending on the layout that your pivot table uses. For tabular
					pivot tables, explicit subtotal headers appear on the visual. For hierarchy
					pivot tables, explicit subtotal headers do not appear. Instead, authors apply
					subtotal styling to individual fields from the **Format
						visual** menu. Collapsed headers cannot be styled as
					subtotals.

###### To apply totals and subtotals styling to cells

- 
						In the **Properties**pane, choose**Total**or**Subtotal**.
- 
						For **Apply styling to**, choose the visual that you want to apply subtotal styling to. You can choose from the following options.- 
								**None**– Removes styling options from all cells.
- 
								**Headers only**– Aplies styling options to all headers in the pivot table.
- 
								**Cells only**– Applies styling options to all cells that aren't headers in the pivot table.
- 
								**Headers and cells**– Applies styling options to all cells in the pivot table.
 
-