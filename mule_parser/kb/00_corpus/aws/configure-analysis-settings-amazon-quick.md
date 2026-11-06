# Configure analysis settings - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/analysis-settings.html](https://docs.aws.amazon.com/quick/latest/userguide/analysis-settings.html)

---

Amazon Quick authors can use the Analysis settings menu to configure the refresh and
            date time settings of an analysis. To access the Analysis Settings menu, choose
                **Edit**, and then choose **Analysis Settings**.
            The following settings can be configured in the Analysis settings menu:

###### Refresh settings

- 
                **Reload visuals every time I switch sheets**– Use this setting to reload every visual in a Quick Sight analysis whenever the user switches to a different sheet in the analysis.
- 
                **Update visuals manually**– Use this setting to only update applicable visuals in an analysis when the user applies their changes. When this setting is toggled on, the analysis loads the visuals blank by default because the queries won't be fired until the user selects the**UPDATE VISUALS**button located in the toolbar or on the impacted visuals. The**UPDATE VISUALS**button confirms that the user is finished with the filter and control choices that they want to apply to the affected visuals. The image below shows the**UPDATE VISUALS**button.When **Update visuals manually**is toggled on, authors can still add visuals, edit visuals, and edit control selections, but the affected visuals won't update until the author applies the new changes. This allows authors to build analyses without increasing their database load and gives better control over which values are loaded in an analysis.

###### Date and time settings

- 
                **Convert time zone**– Use this setting to convert all date field related visualizations, filters, and parameters to reflect the chosen time zone. All daylight savings adjustments are made automatically. For more information about time zone configuration, see[Customize date and time values of an analysis](./analysis-date-time.html).
- 
                **Start of the week**– Use this setting to choose the week start day for an analysis.

###### Interactivity

- 
                Use this setting to highlight specific data points across visuals in a sheet. When you select or hover over a data point on a visual, related data across other visuals will stand out, while unrelated data is dimmed. Highlighting allows you to understand correlations, spot patterns, trends, and outliers, and facilitate stronger, more informed analyses. Select either **On selection**or**On hover**to turn highlighting on, or**No highlight**to turn it off.
- 
                To customize highlighting on a per-sheet level see [Adding and managing sheets](./working-with-multiple-sheets.html).