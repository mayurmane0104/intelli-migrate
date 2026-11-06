# Refreshing visuals in Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/refreshing-visuals.html](https://docs.aws.amazon.com/quick/latest/userguide/refreshing-visuals.html)

---

When you work in an Quick Sight analysis or dashboard, visuals refresh and reload when you change something that affects them, such as updating a parameter or filter control. If you switch to a new sheet after a parameter or filter changes, only the visuals affected by the change refresh on the new sheet. Otherwise, visuals update every 30 minutes when you switch sheets. This is the default behavior for all analyses and dashboards.

If you want to refresh all visuals when you switch sheets, regardless of a change, you can do so for each analysis that you create.

###### To refresh all visuals each time that you switch sheets in an analysis

- 
                    In Amazon Quick, open the analysis. 
- 
                    In the analysis, choose **Edit > Analysis Settings**.
- 
                    In the **Analysis Settings**pane that opens, for**Refresh Options**, toggle on**Reload visuals each time I switch sheets**.
- 
                    Choose **Apply**.