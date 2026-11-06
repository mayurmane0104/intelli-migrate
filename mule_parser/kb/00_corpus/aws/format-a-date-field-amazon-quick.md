# Format a date field - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/format-a-date-field.html](https://docs.aws.amazon.com/quick/latest/userguide/format-a-date-field.html)

---

When you format a date field, you can choose a list of common formatting
						options. Or you can open the **Format data** pane to choose
						from a list of common formats, or specify custom formatting for the date and
						time values.

Changing a field format changes it for all visuals in the analysis that use that dataset, but does not change it in the dataset itself.

If you want to format a date field by choosing from a list of common
						options, you can access such a list in several ways. You can access it from
						the **Field list** pane, a visual on-visual editor, or a
						visual field well.

###### To change a date field's format by choosing a list option

- 
							Choose one of the following options: - 
									In the **Field list**pane, choose the selector icon to the right of the number field that you want to format.
- 
									On any visual that contains an on-visual editor associated with the number field that you want to format, choose that on-visual editor. Expand the **Field wells**pane, and then choose the field well associated with the number field that you want to change.
 
- 
									
- 
							Choose **Format**, and then choose the format that you want. The following quick formatting options are offered for date fields:- 
									Show the month, day, year, and time. 
- 
									Show the month, day, and year. 
- 
									Show the month and year. 
- 
									Show the year. 
 
- 
									

###### To manually change a date field's format

- 
							Choose one of the following options: - 
									In the **Field list**pane, choose the selector icon to the right of the number field that you want to format.
- 
									On any visual that contains an on-visual editor associated with the number field that you want to format, choose that on-visual editor. Expand the **Field wells**pane, and then choose the field well associated with the number field that you want to change.
 
- 
									
- 
							Choose **Format**, and then choose**More Formatting Options**.The **Format data**pane opens.
- 
							Expand the **Date**section. Choose an existing date format, or choose**Custom**and specify a format pattern in the**Custom**section lower down in the**Format data**pane. If you choose**Custom**for the**Date**section, you must also choose**Custom**for the following**Time**section. The pattern that you specify in the**Custom**section must include any date and time formatting that you want.The default selection is **Custom**, with a default format pattern of MMM D, YYYY h:mma, for example Sep 20, 2022 5:30pm.
- 
							Expand the **Time**section. Choose an existing time format, or choose**Custom**and specify a format pattern in the**Custom**section lower down in the**Format data**pane. If you choose**Custom**for the**Time**section, you must also choose**Custom**for the preceding**Date**section. The pattern that you specify in the**Custom**section must include any date and time formatting that you want.The default selection is **Custom**, with a default format pattern of MMM D, YYYY h:mma, for example Sep 20, 2022 5:30pm.
- 
							If you chose **Custom**in the**Date**and**Time**sections, expand the**Custom**section and specify the format pattern that you want, using the format pattern syntax specified in[Moment.js Display Format](https://momentjs.com/docs/#/displaying/)in the Moment.js JavaScript documentation.###### NoteThe time zone related display token `Z`from the Moment.js library is supported in Quick, but the`z`token is not.If you chose something other than **Custom**in the**Date**and**Time**sections,**Custom**is populated with the format pattern that reflects your selections. For example, if you chose Jun 21, 2016 in the**Date**section and 17:00:00pm in the**Time**section, the**Custom**section shows the format pattern MMM D, YYYY H:mm:ssa.
- 
							(Optional) Expand the **Custom**section and use**Preview**to verify your specified format.
- 
							Expand the **Null values**section and choose whether to display null values as`null`or as a custom value. Using`null`is the default.