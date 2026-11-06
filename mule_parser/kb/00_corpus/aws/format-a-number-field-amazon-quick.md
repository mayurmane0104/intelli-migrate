# Format a number field - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/format-a-number-field.html](https://docs.aws.amazon.com/quick/latest/userguide/format-a-number-field.html)

---

When you format a number field, you can choose the decimal place and
						thousand separator format from a list of common options. Or you can open the
							**Format Data** pane and manually format the field.
						Manually formatting the field enables you to choose which separators to use
						and the number of decimal places to show. It also enables you to choose
						which units to use, and how to display negative numbers.

Changing a field format changes it for all visuals in the analysis, but does not change it in the underlying dataset.

If you want to format a number field by choosing from a list of common
						options, you can access such a list from the **Field list**
						pane, an on-visual editor, or a visual field well.

**To change a number field's format by choosing a list
							option:**

- 
							Choose one of the following options: - 
									In the **Field list**pane, choose the selector icon to the right of the number field that you want to format.
- 
									On any visual that contains an on-visual editor associated with the number field that you want to format, choose that on-visual editor. Expand the **Field wells**pane, and then choose the field well associated with the number field that you want to change.
 
- 
									
- 
							Choose **Format**, and then choose the format that you want. The following quick formatting options are offered for number fields:- 
									Use commas to separate groups of thousands and use a decimal point to show the fractional part of the number, for example 1,234.56. 
- 
									Use a decimal point to show the fractional part of the number, for example 1234.56. 
- 
									Show the number as an integer and use commas to separate groups of thousands, for example 1,234. 
- 
									Show the number as an integer, for example 1234. 
 
- 
									

**To manually change a number field's
							format:**

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
							Expand the **Units**section and choose from the following options:- 
									Choose the unit to use. Choosing a unit adds the appropriate suffix to the number value. For example, if you choose **Thousands**, a field value of 1234 displays as 1.234K.The unit options are as follows: - 
											No unit suffix. This is the default. 
- 
											Thousands (K) 
- 
											Millions (M) 
- 
											Billions (B) 
- 
											Trillions (T) 
 
- 
											
- 
									If you want to use a custom prefix or suffix, specify it in the **Prefix**or**Suffix**box. You can specify both. You can also specify a custom prefix in addition to the suffix added by selecting a unit.
 
- 
									
- 
							Expand the **Negatives**section and choose whether to display a negative value by using a minus sign or by enclosing it in parentheses. Using a minus sign is the default.
- 
							Expand the **Null values**section and choose whether to display null values as`null`or as a custom value. Using`null`is the default.###### NoteWhen using a table or pivot table, null values only display for fields that are placed in the **Rows**,**Columns**, or**Group by**field wells. Null values for fields in the**Values**field well appear empty in the table or pivot table.