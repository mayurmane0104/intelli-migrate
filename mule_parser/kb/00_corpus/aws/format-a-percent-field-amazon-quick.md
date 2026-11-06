# Format a percent field - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/format-a-percent-field.html](https://docs.aws.amazon.com/quick/latest/userguide/format-a-percent-field.html)

---

When you format a percent field, you can choose the number of decimal
						places from a list of common options. Or you can open the **Format
							data** pane and manually format the field. Manually formatting
						the field enables you to choose which separators to use. It also enables you
						to choose the number of decimal places to show and how to display negative
						numbers.

Changing a field format changes it for all visuals in the analysis, but does not change it in the underlying dataset.

If you want to choose the number of decimal places for a percent field
						from a list of common options, you can access such a list in several ways.
						You can access it from the **Field list** pane, an
						on-visual editor, or a visual field well.

###### To change a percent field's number of decimal places by choosing a list option

- 
							Choose one of the following options: - 
									In the **Field list**pane, choose the selector icon to the right of the number field that you want to format.
- 
									On any visual that contains an on-visual editor associated with the percent field that you want to format, choose that on-visual editor. Expand the **Field wells**pane, and then choose the field well associated with the number field that you want to change.
 
- 
									
- 
							Choose **Format**, and then choose the number of decimal places that you want. The following quick formats are offered for percent fields:- 
									Display the value with two decimal places. 
- 
									Display the value with one decimal place. 
- 
									Display the value with no decimal places. 
 
- 
									

###### To manually change a percent field's format

- 
							Choose one of the following options: - 
									In the **Field list**pane, choose the selector icon to the right of the number field that you want to format.
- 
									On any visual that contains an on-visual editor associated with the number field that you want to format, choose that on-visual editor. Expand the **Field wells**pane, and then choose the field well associated with the number field that you want to change.
 
- 
									
- 
							Choose **Format**, and then choose**More Formatting Options**.The **Format data**pane opens.
- 
							Expand the **Separators**section and choose from the following options:- 
									Under **Decimal**, choose a dot or a comma for the decimal separator. A dot is the default. If you choose a comma instead, use a dot or a space as the thousands separator.
- 
									Under **Thousands**, select or clear**Enabled**to indicate whether you want to use a thousands separator.**Enabled**is selected by default.
- 
									If you are using a thousands separator, choose whether to use a comma, dot, or space for the separator. A comma is the default. If you choose a dot instead, use a comma as the decimal separator. 
 
- 
									
- 
							Expand the **Decimal Places**section and choose from the following options:- 
									Choose **Auto**to have Amazon Quick automatically determine the appropriate number of decimal places, or choose**Custom**to specify a number of decimal places.**Auto**is the default.
- 
									If you chose **Custom**, enter the number of decimal places to use. Field values are rounded to the decimal places specified. For example, if you specify two decimal places, the value 6.728 is rounded to 6.73.
 
- 
									
- 
							Expand the **Negatives**section and choose whether to display a negative value by using a minus sign or by enclosing it in parentheses. Using a minus sign is the default.
- 
							Expand the **Null values**section and choose whether to display null values as`null`or as a custom value. Using`null`is the default.###### NoteWhen using a table or pivot table, null values only display for fields that are placed in the **Rows**,**Columns**, or**Group by**field wells. Null values for fields in the**Values**field well appear empty in the table or pivot table.