# Publishing dashboards - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/creating-a-dashboard.html](https://docs.aws.amazon.com/quick/latest/userguide/creating-a-dashboard.html)

---

When you publish an analysis, that analysis becomes a dashboard that can be shared and interacted with by users of your Amazon Quick account or, in some cases, with anonymous users that aren't on your account. You can choose to publish one sheet of an analysis, all sheets in the analysis, or any other combination of sheets that you want. When you publish an interactive sheet, that sheet becomes an interactive dashboard that users can interact with. When you publish a pixel perfect report sheet, the sheet becomes a pixel perfect report that generates and saves a snapshot of the report's data when you schedule a report in Amazon Quick Sight. You can publish a dashboard that contains any combination of interactive sheets and pixel perfect reports from the same analysis.

For more information about scheduling a report, see [Scheduling and sending Quick Sight reports by email](./sending-reports.html) .

For more information about viewing a report's snapshots, see [Consuming pixel perfect reports in Amazon Quick Sight](./qs-reports-consume-reports.html).

Use the following procedure to publish and optionally share a dashboard. You can also use this procedure to rename a published dashboard. A renamed dashboard retains its security and emailed report settings.

- 
				Open the analysis that you want to use. Choose **Publish**.
- 
				Do one of the following: - 
						To create a new dashboard, choose **New dashboard**, and then type a dashboard name.
- 
						To replace an existing dashboard, do one of the following. Replacing a dashboard updates it without altering security or emailed report settings. - 
								To update it with your changes, choose **Replace an existing dashboard**and then choose a dashboard from the list.
- 
								To rename it, choose **Replace an existing dashboard**, choose a dashboard from the list, and then select the pencil icon. Enter a new name to rename the existing dashboard and click the checkmark or press enter to confirm. When you publish a dashboard after renaming, it also saves any changes you made to the analysis. Changes to the analysis or dashboard are not persisted until you**Publish**. An initial version of a dashboard must be published in order to rename it.
 
- 
								
 
- 
						
- 
				(Optional) Choose the sheets that you want to publish in the **SHEETS**dropdown. When you select sheets to add to the new dashboard, the dropdown shows how many sheets are selected for publishing. The default option is**ALL SHEETS SELECTED**.If you are replacing an existing dashboard, the sheets that are already published to the existing dashboard are pre-selected in the dropdown, unless you are publishing from an analysis you have not previously published from. You can make changes to this by selecting or de-selecting sheets from the dropdown list. 
- 
				(Optional) Add comments on the changes you have made in the notes section, which is available to view under [Version History](./publishing-a-previous-dashboard-version.html).
- 
				(Optional) To allow dashboard readers to share data stories, choose **Allow sharing data stories**. For more information about data stories, see[Working with data stories in Amazon Quick Sight](./working-with-stories.html).
- 
				(Optional) Open **More Settings**. These options are only available if at least one sheet in the new dashboard is an interactive sheet.###### NoteThis is a scrollable window. Scroll down in the **Publish a dashboard**window to view all available options.There are some options that you can turn off to simplify the experience for this dashboard, as follows: - 
						For **Dashboard options**:- 
								Leave **Expand on-sheet controls by default**cleared to show a simplified view. This is disabled by default. To show the controls by default, turn on this option.
- 
								Clear **Enable advanced filtering on the left pane**to remove the ability for dashboard viewers to filter the data themselves. If they create their own filters, the filters exist only while the user is viewing the dashboard. Filters can't be saved or reused.
- 
								Clear **Enable on-hover tooltip**to turn off tooltips.
 
- 
								
- 
						For **Visual options**:- 
								Clear **Enable visual menu**, to turn off the on-visual menu entirely.
- 
								Clear **Enable download options**if your dashboard viewers don't need to be able to download data from the visuals in the dashboard. The CSV file includes only what is currently visible in the visual at the time they download it. The viewer downloads data by using the on-visual menu on each individual visual.
- 
								Clear **Enable maximize visual option**to turn off the ability to enlarge visuals to fill the screen.
 
- 
								
- 
						For **Data point options**:- 
								Clear **Enable drill up/down**if your dashboard doesn't offer drillable field hierarchies.
- 
								Clear **Enable on-click tooltip**to turn off tooltips that appear when the reader chooses (clicks on) a data point.
- 
								Clear **Enable sort options**to turn off sorting controls.
 
- 
								
 
- 
						
- 
				Choose **Publish dashboard**.If you renamed the existing dashboard, the top of the screen refreshes to show the new name. 
- 
				(Optional) Do one of the following: - 
						To publish a dashboard without sharing, choose **x**at the upper right of the**Share dashboard with users**screen when it appears. You can always share the dashboard later by choosing**File>Share**from the application bar.
- 
						To share the dashboard, follow the procedure in [Sharing Amazon Quick Sight dashboards](./sharing-a-dashboard.html).
 After you complete these steps, you complete creating and sharing the dashboard. Subscribers of the dashboard receive email that contains a link to the dashboard. Groups don't receive invitation emails. 
-