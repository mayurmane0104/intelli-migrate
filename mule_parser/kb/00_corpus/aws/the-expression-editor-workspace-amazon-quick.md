# The expression editor workspace - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-narratives-expression-editor-menus.html](https://docs.aws.amazon.com/quick/latest/userguide/using-narratives-expression-editor-menus.html)

---

Use the expression editor to customize a narrative to best fit your business
				needs. The information below provides an overview of the expression editor workspace
				and lists all menu options that can be configured for your narrative. For a
				walkthrough that shows you how to create a custom narrative, see [Use the narrative expression editor](./using-narratives-expression-editor-step-by-step.html).

On the right side of the screen, there's a list of items that you can add to the narrative:

- 
					**Computations**– Use this to choose from the computations that are available in this insight. You can expand this list.
- 
					**Parameters**– Use this to choose from the parameters that exist in your analysis. You can expand this list.
- 
					**Functions**– Use this to choose from functions that you can add to a narrative. You can expand this list.
- 
					**Add computation**– Use this button to create another computation. New computations appear in the**Computations**list, ready to add to the insight.

At the bottom of the narrative expression editor, there's a preview of the narrative that updates as you work. This area also shows an alert if you introduce an error into the narrative or if the narrative is empty. To see a preview of ML-powered insights like anomaly detection or forecasting, run your insight calculation at least once before customizing the narrative.

Editing tools are located across the top of the screen. They offer the following options:

- 
					**Insert code**– You can insert the following code blocks from this menu:- 
							**Expressions**– Add a free-form expression.
- 
							**Inline IF**– Add an IF statement that displays inline with the existing block of text.
- 
							**Inline FOR**– Add a FOR statement that displays inline with the existing block of text.
- 
							**Block IF**– Add an IF statement that displays in a separate block of text.
- 
							**Block FOR**– Add a FOR statement that displays in a separate block of text.
 The IF and FOR statements enable you to create content that is conditionally formatted. For example, you might add a **block IF**statement, then configure it to compare an integer to a value from a calculation. To do this, you use the following steps, also demonstrated in[Use the narrative expression editor](./using-narratives-expression-editor-step-by-step.html):- 
							Open the calculations menu at right, and choose one of the blue highlighted items from one of the calculations. Doing this adds the item to the narrative. 
- 
							Click once on the item to open it. 
- 
							Enter the comparison that you want to make. The expression looks something like this: `PeriodOverPeriod.currentMetricValue.value>0`.
- 
							Save this expression in the pop-up editor, which prompts you for **Conditional content**.
- 
							Enter what you want to display in the insight, and format it as you want it to appear. Or if you prefer, you can add an image or a URL—or add a URL to an image. 
 
- 
							
- 
					**Paragraph**– This menu offers options for changes to the font size:- 
							**H1 Large header**
- 
							H2 Header 
- 
							H3 Small header 
- 
							¶1 Large paragraph 
- 
							¶2 Paragraph 
- 
							¶3 Small paragraph 
 
- 
							
- 
					**Font**– Use this menu tray to choose options for text formatting. These include bold, italic, underline, strikethrough, foreground color of the text (the letters themselves), and background color of the text. Choose the icon to turn on an option; choose it again to toggle the option off.
- 
					**Formatting**– Use this menu tray to choose options for paragraph formatting, including bulleted list, left justify, center, and right justify. Choose the icon to turn on an option, choose it again to toggle the option off.
- 
					**Image**– Use this icon add an image URL. The image displays in your insight, provided the link is accessible. You can resize images. To display an image based on a condition, put the image inside an IF block.
- 
					**URL**– Use this icon to add a static or dynamic URL. You can also add URLs to images. For example, you can add traffic light indicator images to an insight for an executive dashboard, with links to a new sheet for red, amber, and green conditions.