# Repairing custom actions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/repairing-custom-actions.html](https://docs.aws.amazon.com/quick/latest/userguide/repairing-custom-actions.html)

---

For a custom action to work, every field and parameter it references must be active in the parent widget. If a field is missing from the source widget, or if a parameter is missing from the analysis, the action for that field or parameter becomes unavailable. Menu actions are no longer included in the context menu. Select actions no longer respond to attempts to interact. However, in all other ways, the widget continues to function. No error displays to your users. You can fix broken filter actions and URL actions by adding the missing fields back to the broken visual or insight.

The following procedure explains how to fix an action that broke because someone removed a field or parameter without updating the action. These steps provide basic guidance how to fix this issue. However, use your own judgment on how or if you should make changes to the analysis. If you're not sure, it's better to ask a Amazon Quick administrator for assistance before you change anything. For example, there might be a way to restore a previous version of the analysis, which might be safer if you aren't sure what happened to it.

###### To remove a field from a broken action

- 
                    From the start page, choose **Analyses**. Then choose the analysis to fix.
- 
                    Choose the visual or insight where the action no longer works. Make sure that it's highlighted on the sheet. 
- 
                    Choose **Actions**from the Menu options dropdown in the upper right corner.
- 
                    Locate the action you want to fix and choose **Edit**.
- 
                    If the action type is **Filter action**, and you see an error that says*the field used by this action was removed*, check the settings for**Filter scope**.**Selected fields**can only display fields that are in the visual. To disable selected fields that are removed, choose one of the following:- 
                            Change the **Filter scope**setting to**All fields**. Doing this enables the widget to filter on every field.
- 
                            If you want to use a list of **Selected fields**, verify the list of fields. If you need to include another field, you need to add it to the visual first.
 
- 
                            
- 
                    If the action type is **Navigation action**, follow the guidance on the error message, which reflects the type of change that caused the error.
- 
                    If the action type is **URL action**, check the**URL**setting for variables marked with double angle brackets (`<<FIELD-OR-$PARAMETER>`). Open the list of available variables by choosing the plus icon. Remove any fields or parameters that aren't in the list. Be sure you also remove the matching*URL parameter*and it's separator (`?`for the first URL parameter, or`&`for subsequent parameters). The following examples show (in**bold**) which part is removed if you were removing the field named`Product`from the visual.`https://www.example.com/examplefunction`**?q=<<Product>**`https://www.example.com/examplefunction?`**q=<<Product>&**uact=<<$CSN>`https://www.example.com/examplefunction?pass=yes&q=`**<<Product>+**<<City>&oq=**<<Product>+**<<City>&uact=<<$CSN>Make sure to test the new URL. 
- 
                    (Optional) To delete the action, scroll to the end and choose **Delete**.
- 
                    When you are finished, confirm your changes to the action. Scroll to the bottom of the **Action**pane and choose**Save**.If the error also exists in an associated dashboard, share and publish the dashboard again to propagate the fix.