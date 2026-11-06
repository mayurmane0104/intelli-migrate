# Conditional formatting on visual types in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/conditional-formatting-for-visuals.html](https://docs.aws.amazon.com/quick/latest/userguide/conditional-formatting-for-visuals.html)

---

In some visual types, you can add conditional formatting to highlight some of your data. The conditional formatting options currently supported include changing text or background color and using symbolic icons. You can use icons from the provided set, or you can use Unicode icons instead.

Conditional formatting is available on the following visuals:

- 
				Gauge charts 
- 
				Key performance indicators (KPIs) 
- 
				Pivot tables 
- 
				Tables 

For tables and pivot tables, you can set multiple conditions for fields or supported aggregations, along with format options to apply to a target cell. For KPIs and gauge charts, you can format the primary value based on conditions that are applied to any dimension in the dataset. For gauge charts, you can also format the foreground color of the arc based on conditions.

###### To use conditional formatting on a visual

- 
				On the analysis page, choose the visual that you want to format. 
- 
				On the visual, open the context menu on the down icon at the upper-right. Then choose **Conditional formatting**.Options for formatting display on the left. Choose one of the following: - 
						**For pivot tables**– Begin by choosing a measure that you want to use. You can set conditional formatting on one or more fields. The selection is limited to the measures that are in the**Values**field well.
- 
						**For tables**– Begin by choosing a field that you want to use. You can set conditional formatting on one or more fields. You can also choose to apply formatting to the entire row. Formatting the entire row adds an option to**Apply on top**, which applies the row formatting in addition to formatting added by other conditions.
- 
						**For KPIs**– Apply formatting to the primary value or the progress bar or both.
 
- 
						
- 
				For the remaining steps in this procedure, choose the features that you want to use. Not all options are available for all visuals. 
- 
				(Optional) Choose **Add background color**to set a background color. If a background color is already added, choose**Background**.- 
						**Fill type**– The background color can be**Solid**or**Gradient**. If you choose to use a gradient, additional color options display, enabling you to choose a minimum and maximum value for the gradient scale. The minimum value defaults to the lowest value, and the maximum value defaults to the highest value.
- 
						**Format field based on**– The field to use when applying the format.
- 
						**Aggregation**– The aggregation to use (displays only the available aggregations).
- 
						**Condition**– The comparison operator to use, for example "greater than".
- 
						**Value**– The value to use.
- 
						**Color**– The color to use.
- 
						**Additional options:**In pivot tables, you can set what you want to format by choosing options from the context menu (**…**):**Values**,**Subtotals**, and**Totals**.
 
- 
						
- 
				(Optional) Choose **Add text color**to set a text color. If a text color is already added, choose**Text**.- 
						**Format field based on**– The field or item to use when applying the format.
- 
						**Aggregation**– The aggregation to use (displays only the available aggregations). This option applies to tables and pivot tables.
- 
						**Condition**– The comparison operator to use, for example "greater than".
- 
						**Value**– The value to use.
- 
						**Color**– The color to use.
- 
						**Additional options:**In tables and pivot tables, you can set what you want to format by choosing options from the context menu (**…**):**Values**,**Subtotals**, and**Totals**.
 
- 
						
- 
				(Optional) Choose **Add icons**to set an icon or icon set. If an icon is already added, choose**Icon**.- 
						**Format field based on**– The field or item to use when applying the format.
- 
						**Aggregation**– The aggregation to use (displays only the available aggregations). This option applies to tables and pivot tables.
- 
						**Icon set**– The icon set to apply to field in**Format field based on**. This option applies to tables and pivot tables.
- 
						**Reverse colors**– Reverses the colors of the icons for tables and pivot tables.
- 
						**Custom conditions**– Provides more icon options for tables and pivot tables.
- 
						**Condition**– The comparison operator to use.
- 
						**Value**– The value to use.
- 
						**Icon**– The icon to use. To choose an icon set, use the**Icon**symbol to choose the icons to use. Choose from the provided icon sets. In some cases, you can add your own. To use your own icon, choose**Use custom Unicode icon**. Paste in the Unicode glyph that you want to use as an icon. Choose**Apply**to save or choose**Cancel**to exit icon setup.
- 
						**Color**– The color to use.
- 
						**Show icon only**– Replaces the value with the icon for tables and pivot tables.
- 
						**Additional options:**- 
								In tables and pivot tables, you can set what you want to format by choosing options from the context menu ( **…**):**Values**,**Subtotals**, and**Totals**.
- 
								In pivot tables, enabling **Custom conditions**activates preset conditional formatting that you can keep, add to, or overwrite with your own settings.
 
- 
								
 
- 
						
- 
				(Optional) Choose **Add foreground color**to set the foreground color of a KPI progress bar. If a foreground color is already added, choose**Foreground**.- 
						**Format field based on**– The field to use when applying the format.
- 
						**Condition**– The comparison operator to use.
- 
						**Value**– The value to use.
- 
						**Color**– The color to use.
 
- 
						
- 
				When you are finished configuring conditional formatting, choose one or more of the following: - 
						To save your work, choose **Apply**.
- 
						To cancel selections and return to the previous panel, choose **Cancel**.
- 
						To close the settings panel, choose **Close**.
- 
						To reset all settings on this panel, choose **Clear**.
 
-