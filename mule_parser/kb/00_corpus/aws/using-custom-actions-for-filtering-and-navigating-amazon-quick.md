# Using custom actions for filtering and navigating - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quicksight-actions.html](https://docs.aws.amazon.com/quick/latest/userguide/quicksight-actions.html)

---

To add interactive options for dashboard subscribers (Quick readers), you create custom actions on one or more visuals in your analysis. Enhancing dashboards with custom actions helps people explore data by adding more context from within the dataset. It can make it easier to drill into the details and to find new insights in the same dashboard, a different dashboard, or a different application. You can add up to 10 custom actions to each visual in a dashboard.

Before you begin, it's helpful to do some planning. For example, identify fields that are good candidates for filtering, for opening a different sheet, for opening a URL, or for sending email. For each sheet, identify the widgets that display these fields. Then decide which widgets are going to contain actions. It's also a good idea to create a naming scheme so the names of the actions are consistent throughout the entire analysis. Consistent names make it easier for the person using your analysis to figure out what the action will do, plus they make it easier for you to maintain actions that you might be duplicating throughout the analysis.

Actions only exist on the dashboard widget where you create them and they work in the context of that widget's parent sheet and child fields that it displays. You can create actions only on specific types of widget: visuals and insights. You can't add them to other widgets, for example filter or list controls. Custom actions can only be activated from the widget where you create them.

To activate an action, the person using the analysis can left-click (select) or
            right-click (use the context menu) on a data point. A *data
                point* is an item in the dataset, for example a point on a line chart, a
            cell in a pivot table, a slice on a pie chart, and so on. If the person clicks a visual
            element, the *select* action is activated. This is the
            action that is currently a member of the **On select** category of the
                **Actions** in an analysis. If the person instead right-clicks a
            visual element, they can choose from a list of *menu*
            actions. Any action listed is currently a member of the **Menu option**
            category of the **Actions** in an analysis. The **On
                select** category can contain one and only one member action. 

By default, the first action you create becomes the select action—the one
            activated by left-clicking. To remove an action from the **On select**
            category, change the action's **Activation** setting to **Menu
                option**. After you save that change, you can set a different action's
                **Activation** setting to **Select**. 

You can choose from three **Action types** when you configure an
            action:

- 
                **Filter action**– Filter data included in visual or in the entire sheet. By default, filters are available for all fields in the parent visual. Cascading filters are enabled by default. Filter actions work across multiple datasets by using automatically generated field mappings.If the analysis uses more than one dataset, you can view the automatically generated field mappings for fields that exist in multiple datasets. To do this, choose **View field mapping**at the end of the action settings, while you're editing an action. If you are viewing a list of actions, choose**View field mapping**from the menu for each action. The field mappings appear in a new screen that shows the mapping between the initial dataset and all the other datasets in the visual. If no fields are automatically mapped, a message displays with a link to[Mapping and Joining Fields](./mapping-and-joining-fields.html).
- 
                **Navigation actions**– Enable navigation between different sheets in the same analysis.
- 
                **URL actions**– Open a link to another web page. If you want to open a different dashboard, use a URL action. You can use a URL action to send data points and parameters to other URLs. You can include any available field or parameter.If the URL uses the `mailto`scheme, running the action opens your default email editor.