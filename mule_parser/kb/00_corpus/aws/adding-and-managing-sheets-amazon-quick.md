# Adding and managing sheets - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-multiple-sheets.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-multiple-sheets.html)

---

A *sheet* is a set of visuals that are viewed together in a single
			page. When you create an analysis, you place visuals in the workspace on a sheet. You
			can imagine this as a sheet from a newspaper, except that it is filled with data
			visualizations. You can add more sheets, and make them work separately or together in
			your analysis. 

The top sheet, also called the default sheet, is the one on the far left. This sheet displays on top in an analysis or dashboard. Each analysis can contain up to 20 sheets.

You can share analyses and publish dashboards with multiple sheets. You can also schedule email reports for any combination of sheets in an analysis.

When you create a new analysis or a new sheet in an existing analysis, you choose
			whether to make the new sheet an **Interactive sheet** or a
				**Pixel perfect report**. This way, you can have analyses for
			interactive sheets only, analyses for pixel perfect reports only, or you can have an
			analysis that includes both interactive sheets and pixel perfect reports.

An *Interactive Sheet* is a collection of data expressed in visuals
			that users can interact with when the sheet is published to a dashboard. Amazon Quick
			authors can add different controls and filters to their interactive sheets. Dashboard
			viewers can use these to gain detailed information from the published data. For more
			information on interactive sheets, see [Working with interactive sheets in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-interactive-sheets.html).

A *Paginated Report* is a collection of tables, charts, and visuals
			that are used to convey business critical information, such as daily transaction
			summaries or weekly business reports. In order to create pixel perfect reports in
			Quick Sight, add the **Pixel perfect reporting Add-on** to your
			Quick account. To get the **Pixel perfect reporting Add-on**
			and start working with pixel perfect reports, see [Working
				with pixel perfect reports in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/working-with-reports.html).

Use the following list of actions to work with sheets:

- 
				To add a new sheet, choose the plus sign (+) to the right of the sheet tabs, choose the type of sheet that you want, and then choose **ADD**.
- 
				To rename a sheet, choose the name of the sheet and start typing. **Rename**is also available from the sheet menu.
- 
				To duplicate a sheet, choose the name of the sheet, then choose **Duplicate**from the sheet menu. You can only duplicate a sheet if**Autosave**is turned on.
- 
				To duplicate an interactive sheet and convert it to a pixel perfect report, choose the name of the sheet, then choose **Duplicate to report**from the sheet menu. You can't convert a pixel perfect report to an interactive sheet.
- 
				To delete a sheet, choose the name of the sheet, then choose **Delete**from the sheet menu. You can't delete the sheet if it's the only sheet in the analysis.
- 
				To change the order of the sheets, choose the name of the sheet and drag it to a new position. 
- 
				To copy a visual to a new sheet, choose **Duplicate visual to**from the on-visual menu. Then choose the target sheet. Filters exist only on the sheet that you create them on. To duplicate filters, recreate them on the target sheet.
- 
				To highlight specific data points across visuals in a sheet, go to the **Sheets**tab and select**Layout Settings**. Under the**Interactivity**section, select either**On selection**or**On hover**to turn highlighting on, or**No highlight**to turn it off. By default, sheet highlighting follows the same settings as analysis highlighting.When you select or hover over a data point on a visual, related data across other visuals will stand out, while unrelated data is dimmed. Highlighting allows you to understand correlations, spot patterns, trends, and outliers, and facilitate stronger, more informed analyses. 

You can use the parameter controls on the top sheet to control multiple sheets. To do this, open each sheet that you want to work with the parameter. Then add a filter that uses the same parameter used in the control on the top sheet. Or, if you want a new sheet to operate independently, you can add parameters and parameter controls to it that are separate from those on the top sheet.