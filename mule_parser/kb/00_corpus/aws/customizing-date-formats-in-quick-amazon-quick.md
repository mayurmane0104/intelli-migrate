# Customizing date formats in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/format-visual-date-controls.html](https://docs.aws.amazon.com/quick/latest/userguide/format-visual-date-controls.html)

---

In Quick, you can customize how dates are formatted in your filter and parameter controls. For example, you can specify to format the date in a control as 20-09-2021, or, if you'd rather, as 09-20-2021. You can also specify to shorten the month in your dates (such as September) to three letters (Sep), among other customizations.

Following is a list of tokens you can use to create custom date formats. You can use them in combination with one another to control how dates appear in your controls.

## List of supported tokens for formatting dates

							Use the following tokens to customize the format of dates in Quick.

| Example | Description | Token | 
|---|---|---|
| 0–6 | Numeric representation of a particular day of the week. 0 is Sunday and 6 is Saturday. | 
 | 
| Mo–Su | A 2-character textual representation of a particular day of the week. | 
 | 
| Mon–Sun | A 3-character textual representation of a particular day of the week. | 
 | 
| Monday–Sunday | A textual representation of a particular day of the week. | 
 | 
| 99 or 21 | A 2-digit representation of a year. | 
 | 
| 1999 or 2021 | A full, 4-digit numeric representation of a year. | 
 | 
| 1–12 | Number of a month, without leading zeros. | 
 | 
| 1st, 2nd, to 12th | Number of a month without leading zeros and with an ordinal suffix. | 
 | 
| 01–12 | Number of a month with leading zeros. | 
 | 
| Jan–Dec | A 3-digit textual representation of a month. | 
 | 
| January–December | A full textual representation of a month. | 
 | 
| 1–4 | A numeric representation of a quarter. | 
 | 
| 1st–4th | A numeric representation of a quarter with an ordinal suffix. | 
 | 
| 1–31 | Day of the month without leading zeros. | 
 | 
| 1st, 2nd, to 31st | Day of the month without leading zeros and an ordinal suffix. | 
 | 
| 01–31 | A 2-digit day of the month with leading zeros. | 
 | 
| 1–365 | Day of the year without leading zeros. | 
 | 
| 001–365 | Day of the year with leading zeros. | 
 | 
| 1–53 | Week of the year without leading zeros. | 
 | 
| 1st–53rd | The week of the year without leading zeros and with an ordinal suffix. | 
 | 
| 01–53rd | Week of the year with leading zeros. | 
 | 
| 1–23 | Hours, in 24-hour format, without leading zeros. | 
 | 
| 01–23 | Hours, in 24-hour format, with leading zeros. | 
 | 
| 1–12 | Hours, in 12-hour format, without leading zeros. | 
 | 
| 01–12 | Hours, in 12-hour format, with leading zeros. | 
 | 
| 0–59 | Minutes without leading zeros. | 
 | 
| 00–59 | Minutes with leading zeros. | 
 | 
| 0–59 | Seconds without leading zeros. | 
 | 
| 00–59 | Seconds with leading zeros. | 
 | 
| am or pm | am/pm | 
 | 
| AM or PM | AM/PM | 
 | 
| 1632184215 | Unix timestamp. | 
 | 
| 1632184215000 | Millisecond Unix timestamp. | 
 | 
| Z | Zero UTC offset. | 
 | 

The following date types are not supported.

- 
									Time zones offset with a colon. For example, +07:00. 
- 
									Time zones offset without a colon. For example, +0730. 

### Preset date formats

To quickly customize dates and times to appear as one of the following example formats, you can use the following Quick preset tokens.

| Example | Token | 
|---|---|
| 8:30 PM | 
 | 
| 8:30:25 PM | 
 | 
| August 2 1985 | 
 | 
| Aug 2 1985 | 
 | 
| August 2 1985 08:30 PM | 
 | 
| Aug 2 1985 08:30 PM | 
 | 
| Thursday, August 2 1985 08:30 PM | 
 | 
| Thu, Aug 2 1985 08:30 PM | 
 | 

## Common date formats

							Following are three common date examples and their associated token formats for your quick reference.

| Example | Token Format | 
|---|---|
| Sep 20, 2021 | 
 | 
| 20-09-21 5pm | 
 | 
| Monday, September 20, 2021 17:30:15 | 
 | 

## Adding words to dates

							To include words in your date formats, such as the word "of" in
									*20th of Sep, 2021*, enter backslashes (\)
								before each character in the word. For example, for the 20th of Sep,
								2021 date example, use the following token format: ```
Do \o\f
									MMM, YYYY
```
.

## Example: Customizing the date format in a filter control

							Use the following procedure to learn how to use date token formats to customize dates for a filter control.

###### To learn to customize dates for a filter control with data tokens

- 
									In a Quick analysis, choose the filter control that you want to customize. 
- 
									On the filter control, choose the **Edit control**icon.
- 
									On the **Edit control**page that opens, for**Date format**, enter the custom date format that you want. Use the tokens listed previously in this topic.For example, let's say that you want to customize your dates using the following format: *Sep 3rd, 2020 at 5pm*. To do so, you can enter the following token format:`MMM Do, YYYY \a\t ha`A preview of the date format appears below the input field as you enter each token. 
- 
									Choose **Apply**.The dates in the control update to the format you specified.