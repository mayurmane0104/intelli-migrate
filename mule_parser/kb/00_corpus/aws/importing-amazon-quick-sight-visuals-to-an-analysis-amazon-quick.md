# Importing Amazon Quick Sight visuals to an analysis - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/import-visuals.html](https://docs.aws.amazon.com/quick/latest/userguide/import-visuals.html)

---

Quick Sight authors can import Quick Sight visuals from one analysis or dashboard to a new analysis that has access privileges. When you import a visual from a Quick Sight analysis or dashboard to another Quick Sight analysis, the following dependencies are imported along with the visual.

- 
                    Datasets associated with the visual 
- 
                    All parameters that are configured to the visual 
- 
                    Calculated fields that are configured to the visual 
- 
                    Filter definitions 
- 
                    Visual properties 
- 
                    Conditional formatting rules 

Use the following sections to learn more about importing Quick Sight visuals.

## Considerations

                Before you import a visual, review the following limitations.

- 
                        The Quick Sight author that wants to import a visual must have ownership privileges to the analysis that they want to import the visual to 
- 
                        Filter controls can't be imported 
- 
                        Importing visuals from multiple sheets at a time is not supported 
- 
                        Some user configurations including filter configurations that are maintained against bookmarks and alerts are not supported 

## Import a visual

                Use the following procedure to import a visual from a source dashboard or analysis to a different analysis.

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                        Open the analysis that you want to import a visual to. 
- 
                        Choose **File**, and then choose**Import**. Alternatively, you can choose the**Import**icon in the**ADD**toolbar.
- 
                        The **Asset explorer**modal opens. A list of all eligible source analyses and dashboards that you can access are displayed. Choose the artifact that you want to import a visual from, and then choose**LOAD**. Alternatively, enter the name of the source artifact that contains the visual that you want to import in the**Find source to insert**search bar. Choose the artifact that you want, and then choose**LOAD**.
- 
                        In the **Select visuals to import**page that opens, choose the sheet that contains the visuals that you want to import, and then choose the visuals that you want to import. You can only import visuals from one sheet at a time. When you have chosen all visuals that you want to import, choose**IMPORT**.

After a successful import job, the imported visuals are added to the destination analysis. The imported visuals retain the original properties that were configured to them in the source dashboard or analysis. Imported visuals inherit the theme-level properties from the theme that is applied to the destination analysis.