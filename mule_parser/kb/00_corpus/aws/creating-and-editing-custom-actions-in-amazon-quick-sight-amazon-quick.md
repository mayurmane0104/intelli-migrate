# Creating and editing custom actions in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/custom-actions.html](https://docs.aws.amazon.com/quick/latest/userguide/custom-actions.html)

---

You create one action for each task that you want to be able to add to a visual. The actions you create become part of the functionality of each visual or insight.

The following table defines when to use each type of action.

| Action to perform | Type of action | 
|---|---|
| Add or customize an interactive filter action, including one-click filters | Filter action | 
| Open another sheet in the same dashboard | Navigation action | 
| Open a sheet in a different dashboard in the same AWS account | URL action | 
| Open a URL ( | URL action | 
| Send an email ( | URL action | 

You can set the following attributes and options for a custom action:

- 
                    **Action name**– This is a descriptive name that you choose for the action. By default, actions are named`Action 1`,`Action 2`, and so on. If your custom action is activated from a context menu, this name displays in the menu when you right-click on a data point.To make the action name dynamic, you can parameterize it. Use the plus icon near the action name header to display a list of available variables. Variables are enclosed in angle brackets `<< >>`. Parameters are prefixed with a`$`, for example`<<$parameterName>>`. Field names have no prefix, for example`<<fieldName>>`.
- 
                    **Activation**– Available options are**Select**or**Menu option**. To use an action, you can*select*the data point (left-click) or navigate to the*menu option*in the context menu (right-click). Navigation actions and URL actions listed in the middle of the context menu, just above**Color**options. Actions that are activated by menu are also available from the legend on a visual.
- 
                    **Action type**– The type of action that you want. Settings that are specific to an action type only display after you choose the action type.- 
                            **Filter action**settings include the following:- 
                                    **Filter scope**– The fields to filter on. To filter on all fields, choose**All fields**. Otherwise, choose**Select fields**and then turn off the items you don't want to target.The default is **All fields**.
- 
                                    **Target visuals**– The dashboard widgets to target. To apply the filter to all of them, choose**All visuals**. Otherwise, choose**Select visuals**and then turn off the items you don't want to target. When you apply a filter action to other visuals, the effect is called*cascading filters*.The default is **All visuals**.A cascading filter applies all the visuals that are set up in the **Target visuals**section of a specific filter action. Amazon Quick Sight initially evaluates your visuals and preconfigures the settings for you. But you can change the defaults if you wish to do so. You can set up multiple cascading filters on multiple visuals in the same sheet or analysis. When you are using the analysis or dashboard, you can use multiple cascading filters at the same time, although you activate each of these one at a time.A filter action requires at least one target visual, because a filter action requires a source and a target. To filter only the current visual, create a regular filter instead by choosing **Filter**at left.
 
- 
                                    
- 
                            **Navigation action**settings include the following:- 
                                    **Target sheet**– The sheet to target.
- 
                                    **Parameters**– The parameters to send to the target sheet. Choose the plus icon to add an existing parameter.
 
- 
                                    
- 
                            **URL action**settings include the following:- 
                                    **URL**– The URL to open. URL actions can be deep links into another application. Valid URL schemes include`https`,`http`, and`mailto`.
- 
                                    **+**(Values)`$`. The parameters on both the sending and the receiving end must match in name and data type.
- 
                                    **Open in**– Where to open the URL. You can choose**New browser tab**,**Same browser tab**, or**New browser window**.
 
- 
                                    
 
- 
                            

Some types of actions enable you to include values from parameters or fields that
                are available in the visual or insight. You can type these in manually or choose
                    **+** to select from a list. For the custom action to work,
                every field and parameter it references must be actively in use in the parent
                widget.

Use the following procedure to create, view, or edit a custom action in an analysis.

###### To create, view, or edit a custom action

- 
                    With your analysis open, choose **Actions**from the**Menu options**dropdown in the upper right corner.The existing actions, if any, display by activation type. To turn an existing action on or off, use the box to the right of the action's name. 
- 
                    (Optional) To edit or view an existing action, choose the menu icon next to the name of the action. To edit the action, choose **Edit**.To delete it, choose **Delete**.
- 
                    To create a new action, choose either one of the following: - 
                            The add icon near the **Actions**heading
- 
                            The **Define a custom action**button
 
- 
                            
- 
                    For **Action name**, define an action name. To make the action name dynamic, use the plus icon to add parameter or field values.
- 
                    For **Activation**, choose how the action runs.
- 
                    For **Action type**, choose the action type you want to use.
- 
                    For a **Filter action**, do the following:- 
                            For **Filter scope**, choose the scope of the filter.
- 
                            For **Target visuals**, choose how far the filter cascades
 
- 
                            
- 
                    For a **Navigation action**, do the following:- 
                            For **Target sheet**, choose the target sheet.
- 
                            For **Parameters**, choose the plus icon near the**Parameters**heading, select a parameter, and then choose a parameter value. You can choose all values, enter custom values, or select specific fields.
 
- 
                            
- 
                    For a **URL action**, do the following:- 
                            For **URL**, enter the hyperlink.
- 
                            Choose the plus icon near the **URL**heading. Then, add variables from the list.
- 
                            For **Open in**, choose how to open the URL.
 
- 
                            
- 
                    After you are finished with the action, choose one of the following at the bottom of the **Actions**panel (you might need to scroll down):- 
                            **Save**– Save your selections, and create the custom action.
- 
                            **Close**– Close this custom action and discard your changes.
- 
                            **Delete**– Delete this action.
 
-