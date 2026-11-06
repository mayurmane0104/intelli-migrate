# Use the narrative expression editor - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-narratives-expression-editor-step-by-step.html](https://docs.aws.amazon.com/quick/latest/userguide/using-narratives-expression-editor-step-by-step.html)

---

The following walkthrough shows an example of how to customize a narrative. For this example, we use a period over period computation type.

- 
					Begin with an existing analysis. Add a **period over period**insight to it. The easiest way to do this is to choose the + icon, then**Add insight**, then choose a type of insight from the list. To learn what type of computational insights you can add as autonarratives, see[Insights that include autonarratives](./auto-narratives.html).After you choose a type of insight, choose **Select**to create the widget. To create an empty narrative, close this screen without choosing a template. To follow this example, choose**Period over period**.If you had a visual selected when you added the insight, the field wells have preconfigured fields for the date, metric, and category. These come from the visualization that you chose when you created the insight. You can customize the fields as needed. You can only customize a narrative for a new or existing insight (text-based) widget. You can't add one to an existing visual (chart based), because it's a different type of widget. 
- 
					Edit the narrative in the expressions editor by choosing the on-visual menu, then choosing **Customize narrative**.In this context, **Computations**are predefined calculations (period-over-period, period-to-date, growth rate, max, min, top movers, and so on) that you can reference in your template to describe your data. Currently, Amazon Quick Sight supports 13 different types of computations that you can add to your insight. In this example,**PeriodOverPeriod**is added by default because we chose the**Period Over Period**template from the suggested insights panel.
- 
					Choose **Add computation**at bottom right to add a new computation, and then choose one from the list. For this walkthrough, choose**Growth rate**, and then choose**Next**.
- 
					Configure the computation by choosing the number of periods that you want to compute over. The default is four, and that works for our example. Optionally, you can change the name of the computation at the top of the screen. However, for our purposes, leave the name unchanged. ###### NoteThe computation names that you create are unique within the insight. You can reference multiple computations of the same type in your narrative template. For example, suppose that you have two metrics, sales revenue and units sold. You can create growth rate computations for each metric if they have different names. However, anomaly computations aren't compatible with any other computation type in the same widget. Anomaly detection must exist in an insight by itself. To use other computations in the same analysis, put them into insights separate from anomalies. To proceed, choose **Add**.
- 
					Expand **Computations**on the right. The computations that are part of the narrative display in the list. In this case, it's**PeriodOverPeriod**and**GrowthRate**.
- 
					In the workspace, add the following text after the final period: `Compounded growth rate for the last`, then add a space.
- 
					Next, to add the computation leave your cursor after the space after the word **last**. On the right, under**GrowthRate**, choose the expression named**timePeriods**(click only once to add it).Doing this inserts the expression **GrowthRate.timePeriods**, which is the number of periods you set in the configuration for**GrowthRate**.
- 
					Complete the sentence with `days is`(a space before and afterwards), and add the expression**GrowthRate.compoundedGrowthRate.formattedValue**, followed by a period (`.`). Choose the expression from the list, rather than typing it in. However, you can edit the contents of the expression after you add it.![Expression editor with open expressions list.](/images/quick/latest/userguide/images/narrative-add-expression.png)  ###### NoteThe **formattedValue**expression returns a string that is formatted based on the formatting applied for the metric on the field. To perform metric math, use**value**instead, which returns the raw value as an integer or decimal.
- 
					Add a conditional statement and formatting. Place your cursor at the end of the template, after the `formattedValue`expression. Add a space if necessary. On the**Edit narrative**menu bar, choose**Insert code**, and then choose**Inline IF**from the list. An expression block opens.
- 
					With the expression block open, choose **GrowthRate**,**compoundedGrowthRate**,**value**from the expression list. Enter`>0`at the end of the expression. Choose**Save**. Don't move your cursor yet.A prompt appears for the conditional content; enter `better than expected!`Then select the text you just entered, and use the formatting toolbar at the top to turn it green and bold.
- 
					Add another expression block for the case when the growth rate wasn't that great by repeating the previous step. But this time, make it `<0`and enter the text`worse than expected`. Make it red instead of green.
- 
					Choose **Save**. The customized narrative that we just created should look similar to the following.![Customized narrative.](/images/quick/latest/userguide/images/narrative-example-result.png)  

The expression editor provides you with a sophisticated tool to customize your narratives. You can also reference the parameters you create for your analysis or dashboard, and use a set of built-in functions for further customization.

###### Tip

To create an empty narrative, add an insight using the **+**
					icon and then **Add insights**. But instead of choosing a
					template, simply close the screen. 

The best way to get started with customizing narratives is to use the existing templates to learn the syntax.