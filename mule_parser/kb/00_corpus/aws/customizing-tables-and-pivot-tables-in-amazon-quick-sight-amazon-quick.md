# Customizing tables and pivot tables in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/customizing-tables-pivot-tables.html](https://docs.aws.amazon.com/quick/latest/userguide/customizing-tables-pivot-tables.html)

---

Reader customization for tables and pivot tables is enabled by default. You can change the visual to fit your analysis needs without requesting updates from the dashboard author. Your customizations are private – other readers of the same dashboard don't see your changes unless you share them.

###### For dashboard authors

To disable reader customization, choose **Format Visual**,
                    choose **Interactions**, and then turn off **Reader
                    Customization**. Republish the dashboard for the change to take
                    effect.

You can customize tables and pivot tables in the following ways:

- 
                    **Sort columns**– Organize data in ascending or descending order.
- 
                    **Reorder columns**– Rearrange columns to reflect the order that matters most to you.
- 
                    **Hide and show columns**– Focus on relevant data by hiding columns you don't need, and show them again when you do.
- 
                    **Freeze columns**– Keep important columns visible while scrolling horizontally through large datasets.
- 
                    **Add and remove fields**– Include additional fields from the dataset or remove fields you don't need.
- 
                    **Change aggregations**– Modify how a measure is aggregated (for example, change from*Sum*to*Average*).
- 
                    **Modify formatting**– Adjust field formatting directly in the dashboard view.

###### Note

Reader customization is supported for tables and pivot tables only. Other visual types don't support reader-level customization at this time.

## Sorting columns

                To sort data in a table or pivot table, choose the column header that you want to sort by. Choose it again to toggle between ascending and descending order.

## Reordering columns

                To rearrange columns, choose the column header menu and then choose
                        **Move left** or **Move right**.

## Hiding and showing columns

                To hide a column, choose the column header menu and then choose
                        **Hide**.

To show hidden columns, choose any column header menu and then choose
                        **Show all hidden fields**.

## Freezing columns

                To freeze a column so that it stays in place while you scroll horizontally,
                    choose the column header menu and then choose **Freeze
                        column**.

This is useful for keeping key identifiers, such as region names or account numbers, visible while you review a wide table.

## Adding and removing fields

                If the author has made additional fields available for customization, you can add or remove them from the visual.

###### To add or remove fields

- 
                        On the table or pivot table, choose **Customize**.
- 
                        In the field list, select the fields you want to add (for example, *City*,*Profit*, or*Quantity*).
- 
                        To remove a field, clear its selection in the field list. 

The available fields are determined by the author. By default, you can add back, remove, hide, show, reorder, and change aggregations for the fields that are already in the visual. Authors can extend this list to include additional fields from the underlying dataset.

## Changing aggregations

                After you add or select a measure field, you can change its aggregation type.
                    For example, you can change *Order Date* to aggregate by
                        **Quarter**, or change
                        *Quantity* from **Sum** to
                        **Average**.

To change an aggregation, choose the field in the customization panel and then select a different aggregation type.

## Resetting to the default view

                To discard all of your customizations and return to the author's original
                    configuration, choose any column header menu and then choose **Reset
                        visual**.

## Saving your customizations

                Your customizations are saved automatically. When you return to the dashboard, your personalized view is preserved – you don't need to reapply settings each time you open the dashboard.

## Sharing customized views

                You can share your customized view with other readers in the following ways:

- 
                        **Share this view**– Generate a link that preserves your current filters, column selections, and ordering. Other users who open the link see the same view. This is useful for ad-hoc collaboration.
- 
                        **Bookmarks**– Save your customizations as a bookmark for recurring use. Bookmarks capture visual customizations and applied filters, so you can return to your preferred view at any time. Bookmarks can be private or shared across teams.

## Exporting customized views

                You can schedule and export your customized table or pivot table in the following formats:

- 
                        PDF 
- 
                        CSV 
- 
                        Excel 

This is useful for sharing data with stakeholders who don't have Amazon Quick Sight access or for offline analysis.

## Embedding behavior

                When tables and pivot tables are embedded in an application, customization availability and persistence depend on the embedding method.

- 
                        **Visual embedding (registered or anonymous users)**– You can customize the visual. Customizations are not persisted – the original dashboard is displayed when the page reloads.
- 
                        **Dashboard embedding for registered users**– You can customize the visual. If state persistence is enabled through embedding options, your customized view is preserved on reload. If state persistence is not enabled, the original dashboard is displayed.
- 
                        **Dashboard embedding for anonymous users**– You can customize the visual. Customizations are not persisted – the original dashboard is displayed when the page reloads.

The `createSharedView` SDK function supports generating a shared
                    view from a customized embedded dashboard.

## Limitations

                - 
                        Reader customization is supported for tables and pivot tables only. Other visual types, such as bar charts, line charts, and KPIs, don't support reader-level customization. 
- 
                        The fields available for readers to add or remove are controlled by the dashboard author. If you need access to a field that isn't available, contact the dashboard author.