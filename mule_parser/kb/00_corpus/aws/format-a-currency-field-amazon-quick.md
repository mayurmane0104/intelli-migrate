# Format a currency field - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/format-a-currency-field.html](https://docs.aws.amazon.com/quick/latest/userguide/format-a-currency-field.html)

---

When you format a currency field, you can either choose the currency
						symbol from a list of common options, or open the **Format
							data** pane and manually format the field. Manually formatting
						the field allows you to choose which symbol to use, which separators to use,
						the number of decimal places to show, which units to use, and how to display
						negative numbers.

Changing a field format changes it for all visuals in the analysis, but does not change it in the underlying dataset.

If you want to choose the symbol for a currency field from a list of
						common options, you can access such a list in several ways. You can access
						it from the **Field list** pane, an on-visual editor, or a
						visual field well.

###### To select a currency field's symbol by choosing a list option

- 
							Choose one of the following options: - 
									In the **Field list**pane, choose the selector icon to the right of the number field that you want to format.
- 
									On any visual that contains an on-visual editor associated with the currency field that you want to format, choose that on-visual editor. Expand the **Field wells**pane, and then choose the field well associated with the number field that you want to change.
 
- 
									
- 
							Choose **Format**, and then choose the currency field that you want:- 
									Display in dollars ($). 
- 
									Display in pounds (£). 
- 
									Display in euros (€). 
- 
									Display in yen or yuan (¥). 
 
- 
									

###### To manually change a currency field's format

- 
							Choose one of the following options: - 
									In the **Field list**pane, choose the selector icon to the right of the number field that you want to format.
- 
									On any visual that contains an on-visual editor associated with the number field that you want to format, choose that on-visual editor. Expand the **Field wells**pane, and then choose the field well associated with the number field that you want to change.
 
- 
									
- 
							Choose **Format**, and then choose**More Formatting Options**.The **Format data**pane opens.
- 
							Expand the **Symbol**section and choose from the following options:- 
									Display in dollars ($). This is the default. 
- 
									Display in pounds (£). 
- 
									Display in euros (€). 
- 
									Display in yen or yuan (¥). 
 
- 
									
- 
							Expand the **Separators**section and choose from the following options:- 
									Under **Decimal**, choose a dot or a comma for the decimal separator. A dot is the default. If you choose a comma instead, use a dot or a space as the thousands separator.
- 
									Under **Thousands**, select or clear**Enabled**to indicate whether you want to use a thousands separator.**Enabled**is selected by default.
- 
									If you are using a thousands separator, choose whether to use a comma, dot, or space for the separator. A comma is the default. If you choose a dot instead, use a comma as the decimal separator. 
 
- 
									
- 
							Expand the **Decimal Places**section and choose the number of decimal places to use. The default is 2. Field values are rounded to the decimal places specified. For example, if you specify two decimal places, the value 6.728 is rounded to 6.73.
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
									If you want to use a custom prefix or suffix, specify it in the **Prefix**or**Suffix**box. Using a custom suffix is a good way to specify a currency suffix outside of those already offered by Amazon Quick. You can specify both. You can also specify a custom prefix in addition to the suffix added by selecting a unit.
 
- 
									
- 
							Expand the **Negatives**section and choose whether to display a negative value by using a minus sign or by enclosing it in parentheses. Using a minus sign is the default.
- 
							Expand the **Null values**section and choose whether to display null values as`null`or as a custom value. Using`null`is the default.###### NoteWhen using a table or pivot table, null values only display for fields that are placed in the **Rows**,**Columns**, or**Group by**field wells. Null values for fields in the**Values**field well appear empty in the table or pivot table.