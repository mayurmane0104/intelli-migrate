# Tooltips on visual types in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/customizing-visual-tooltips.html](https://docs.aws.amazon.com/quick/latest/userguide/customizing-visual-tooltips.html)

---

When you hover your cursor over any graphical element in an Quick visual, a tooltip appears with information about that specific element. For example, when you hover your cursor over dates in a line chart, a tooltip appears with information about those dates. By default, the fields in the Fields well determine what information displays in tooltips. Tooltips can display up to 10 fields.

You can provide your viewers with additional information about data in your visual, customizing what viewers can see. You can even prevent tooltips from appearing when viewers hover a cursor over an element. To do this, you can customize the tooltips for that visual.

## Customizing tooltips in a visual

			Use the following procedure to customize tooltips in a visual.

###### To customize tooltips in a visual

- 
					On the analysis page, choose the visual that you want to format. 
- 
					On the menu in the upper-right corner of the visual, choose the **Format visual**icon.
- 
					In the **Properties**pane that opens, choose**Tooltip**.
- 
					For **Type**, choose**Detailed tooltip**. A new set of options appear.

###### To show or hide titles in a tooltip

- 
					Choose **Use primary value as title**.Clearing the option hides titles in the tooltip. Selecting the option shows the primary field value as the title in the tooltip. 

###### To show or hide aggregations for fields in the tooltip

- 
					Choose **Show aggregations**.Clearing the option hides the aggregation for fields in the tooltip. Selecting the option shows the aggregation for fields in the tooltip. 

###### To add a field to the tooltip

- 
					Choose **Add field**.
- 
					In the **Add field to tooltip**page that opens, choose**Select field**and then select a field from the list.You can add up to 10 fields to tooltips. 
- 
					(Optional) For **Label**, enter a label for the field. This option creates a custom label for the field in the tooltip.
- 
					(Optional) Depending on whether you add a dimension or a measure, choose how you want the aggregation to display in the tooltip. If you don't select an option, Quick uses the default aggregation. If you add a measure to the tooltip, you can select how you want the field to be aggregated. To do so, choose **Select aggregation**, and then select an aggregation from the list. For more information about the types of aggregations in Quick, see[Changing field aggregation](./changing-field-aggregation.html).
- 
					Choose **Save**.A new field is added to the list of fields in your tooltip. 

###### To remove a field from the tooltip

- 
					Under the **Fields**list, select the field menu for the field that you want to remove (the three dots) and choose**Hide**.

###### To rearrange the order of the fields in the tooltip

- 
					Under the **Fields**list, select the field menu for a field (the three dots) and choose either**Move up**or**Move down**.

###### To customize the label for a field in the tooltip

- 
					Select the field menu for the field that you want to customize (the three dots) and choose **Edit**.
- 
					In the **Edit tooltip field**page that opens, for**Label**, enter the label that you want to appear in the tooltip.
- 
					Choose **Save**.

## Using sheet tooltips in Quick

			Sheet tooltips transform how viewers explore data by providing rich context without disrupting their analysis flow. Instead of navigating away from a visual or opening separate sheets, viewers get instant access to detailed breakdowns, trends, and supporting information, making dashboards more intuitive and reducing the need for multiple sheets.

Sheet tooltips are available on interactive sheets only. They are not supported on paginated reports. You can duplicate a tooltip sheet to another tooltip sheet, or duplicate a tooltip sheet to a regular interactive sheet. Additionally, you can duplicate a visual to a tooltip sheet.

### How sheet tooltips work

When an author creates a sheet tooltip, a tooltip sheet is created and associated with a visual. This tooltip sheet works like a regular sheet. You can add visuals, text boxes, and images to it using a free-form layout. When a viewer hovers over a data point, the tooltip sheet inherits all filters from the source visual and adds an additional filter for the specific data point. For example, if your source visual is filtered to "2025 data" and a viewer hovers over "Electronics," the tooltip shows Electronics data for 2025 only.

Consider a bar chart showing sales by product category. You could create a sheet tooltip that shows a trend line of monthly sales, a KPI of year-over-year growth, and a text box with the category name, all filtered to whichever category the viewer hovers over.

![Animated image showing a sheet tooltip appearing when hovering over data points in a visual.](/images/quick/latest/userguide/images/sheet-tooltip-preview.gif) 

					 
					 
				### Sheet tooltip limits

The following limits apply to sheet tooltips:

- 
						Up to 50 tooltip sheets per analysis 
- 
						Up to 5 visuals per tooltip sheet 
- 
						Up to 5 text boxes per tooltip sheet 
- 
						Up to 5 images per tooltip sheet 
- 
						Tooltip sheets use free-form layout only 
- 
						Layer map visuals are not allowed on tooltip sheets 
- 
						Maximum size of a tooltip sheet is 640px wide by 720px tall 

### Creating a sheet tooltip

Use the following procedure to create a sheet tooltip for a visual.

###### To create a tooltip sheet

- 
						On the analysis page, choose the visual that you want to add a sheet tooltip to. 
- 
						On the menu in the upper-right corner of the visual, choose the **Format visual**icon.
- 
						In the **Properties**pane that opens, choose**Interactions**>**Tooltip**.
- 
						For **Type**, choose**Sheet tooltip**.![The Properties pane showing the Sheet tooltip option selected in the Type dropdown.](/images/quick/latest/userguide/images/sheet-tooltip-properties-pane.png)  
- 
						Choose **Create tooltip sheet**. You will automatically navigate to a tooltip sheet editing experience. A tooltip name is auto-generated and you can edit it by choosing the tab title.
- 
						Add visuals, text boxes, or images to the tooltip sheet. Arrange them using the free-form layout. 
- 
						When you are finished, return to the source sheet by choosing the **Back**button located to the left of the sheet tooltip title. To preview the tooltip, hover over any data points in the visual.

### Assigning a tooltip sheet to a visual

When you select **Sheet tooltip** as the tooltip type in the
					**Properties** pane, a control appears that lets you select all
					tooltip sheets available in the analysis. You can assign one tooltip sheet to
					multiple visuals or create separate tooltip sheets for each visual.

If you would like to apply the same tooltip sheet to another visual, you can
					do this by assigning one tooltip sheet to multiple visuals in the
					**Interactions** > **Tooltip** accordion
					in the **Properties** pane.

### Editing a tooltip sheet

Use the following procedure to edit an existing sheet tooltip.

###### To edit a tooltip sheet

- 
						Choose any visual where a sheet tooltip is enabled. 
- 
						Open the **Properties**pane and navigate to**Interactions**>**Tooltip**.
- 
						In the **Tooltip**accordion, select the tooltip that you would like to edit and choose the edit icon next to the tooltip sheet name to navigate to it.
- 
						Make your changes to the visuals, text boxes, or images on the tooltip sheet. ![Animated image showing how to edit a tooltip sheet.](/images/quick/latest/userguide/images/sheet-tooltip-editing.gif)  

### Switching between tooltip types

You can switch a visual's tooltip between basic, detailed, and sheet tooltip types at any time.

###### To change the tooltip type

- 
						Choose the visual that you want to update. 
- 
						Open the **Properties**pane, choose**Interactions**, and then choose**Tooltip**.
- 
						For **Type**, select the tooltip type that you want:**Basic tooltip**,**Detailed tooltip**, or**Sheet tooltip**.

###### Note

Switching away from a sheet tooltip preserves your work. You can always switch back without losing your tooltip sheet design.

### Sheet tooltip considerations

Keep the following in mind when working with sheet tooltips:

- 
						Tables and pivot tables support sheet tooltips but not basic or detailed tooltips. 
- 
						Visuals in a tooltip sheet do not support context menus, on-visual menus, or custom actions. 
- 
						[Using custom actions for filtering and navigating](./quicksight-actions.html)on visuals in a tooltip sheet are not supported when the sheet is rendered as a tooltip.
- 
						Sheet tooltips support filters, cross-sheet filtering, and parameters. Filter controls are not supported. 
- 
						Sheet descriptions are not displayed on tooltip sheets. 
- 
						Cross-sheet filters cannot be scoped to tooltip sheets. 
- 
						An analysis must contain at least one regular interactive sheet. An analysis cannot consist of only tooltip sheets. 
- 
						Layer map visuals cannot be placed inside a tooltip sheet. 
- 
						Tooltips on tooltip sheets are not supported. 
- 
						Sheet tooltips are not supported on the following chart types: Sankey, Waterfall, KPI, Radar, Wordcloud, Custom content, and Highcharts. 

These limits ensure tooltip sheets load quickly and maintain a focused, scannable experience for viewers. For more complex analysis, consider using drill-down actions or separate detail sheets.

## Hiding tooltips in a visual

			If you don't want tooltips to appear when you hover your cursor over data in a visual, you can hide them.

###### To hide tooltips in a visual

- 
					On the analysis page, choose the visual that you want to format. 
- 
					On the menu in the upper-right corner of the visual, choose the **Format visual**icon.
- 
					In the **Properties**pane that opens, choose**Tooltip**.
- 
					Choose **Show tooltip**.Clearing the option hides tooltips for the visual. Selecting the option shows them.