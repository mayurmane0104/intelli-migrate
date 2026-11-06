# Using KPIs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/kpi.html](https://docs.aws.amazon.com/quick/latest/userguide/kpi.html)

---

Use a key performance indicator (KPI) to visualize a comparison between a key value and its target value.

A KPI displays a value comparison, the two values being compared, and a visual that provides context to the data that's displayed. You can choose from a set of predesigned layouts to suit your business needs. The following image shows an example of a KPI visual that uses a sparkline.

- 
				Choose **Add (+)**drop down in the**Visuals pane.**
- 
				Choose the KPI icon from Visual types menu. 

## KPI features

			To understand the features supported by the KPI visual type in Amazon Quick, use the following table.

| Feature | Supported? | Comments | For more information | 
|---|---|---|---|
| Changing the title display | Yes | [Titles and subtitles on visual types in Quick](./customizing-a-visual-title.html) | |
| Removing the title | Yes | You can choose not to display a title. | |
| Changing comparison method | Yes | By default, Amazon Quick automatically chooses a method. The settings are auto, difference, percent, and difference as percent. | |
| Changing the primary value displayed | Yes | You can choose comparison (default) or actual. | |
| Displaying or removing the progress bar | Yes | You can format the visual to either display (default) or not display a progress bar. | 

For more information on KPI formatting options, see [KPI options](./KPI-options.html).

## Creating a KPI

			Use the following procedure to create a KPI.

###### To create a KPI

- 
					Create a new analysis for your dataset. 
- 
					In the **Visual types**pane, choose the KPI icon.
- 
					From the **Fields list**pane, drag the fields that you want to use to the appropriate field wells. You must use measure fields as indicated by the target field well. If you choose to use a dimension field as a measure, the**Count**aggregate function is automatically applied to it to create a numeric value.To create a KPI, drag a measure to the **Value**field well. To compare that value to a target value, drag a different measure to the**Target value**field well.
- 
					(Optional) Choose formatting options by selecting the on-visual menu at the upper-right corner of the visual, then choosing **Format visual**.

## Changing a KPI's layout

			Use the following procedure to change the layout for a KPI.

###### To change the layout of a KPI

- 
					Navigate to the KPI visual that you want to change and choose **KPI layouts**.
- 
					In the **KPI Layouts**pane, choose the KPI layout that you want to use.