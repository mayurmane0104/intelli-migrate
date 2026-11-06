# Setting up parameters in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/parameters-set-up.html](https://docs.aws.amazon.com/quick/latest/userguide/parameters-set-up.html)

---

Use the following procedure to create or edit a basic parameter.

###### To create or edit a basic parameter

- 
                Choose an analysis to work with, then decide which field you want to parameterize. 
- 
                Choose the **Parameters**icon from the icon list at the top of the page.
- 
                Add a new parameter by choosing the plus sign ( **+ Add**) near the top of the pane.Edit an existing parameter by first choosing the `v`-shaped icon near the parameter name and then choosing**Edit parameter**.
- 
                For **Name**, enter an alphanumeric value for the parameter.
- 
                For **Data type**, choose**String**,**Number**,**Integer**, or**Datetime**, and then complete the following steps.- 
                        If you choose **String**,**Number**, or**Integer**, do the following:- 
                                For **Values**, choose**Single value**or**Multiple values**.Choose the single value option for parameters that can contain only one value. Choose multiple values for parameters that can contain one or more values. Multivalue parameters can't be `datetime`data types. They also don't support dynamic default values.To switch an existing parameter between single and multiple values, delete and recreate the parameter. 
- 
                                (Optional) For **Static default value**or**Static multiple default values**, enter one or more values.This type of static value is used during the first page load if a dynamic default value or URL parameter isn't provided. 
- 
                                (Optional) Choose **Show as blank by default**.Select this option to show the default value for multivalue lists as blank. This option only applies to multivalue parameters. 
 
- 
                                
- 
                        If you choose **Datetime**, do the following:- 
                                For **Time granularity**, choose**Day**,**Hour**,**Minute**, or**Second**.
- 
                                For **Default date**, select either**Fixed date**or**Relative date**, and then do the following:- 
                                        If you select **Fixed date**, enter a date and time by using the date and time picker.
- 
                                        If you select **Relative date**, choose a rolling date. You can choose**Today**,**Yesterday**, or you can specify the**Filter condition**(start of or end of),**Range**(this, previous, or next), and**Period**(year, quarter, month, week, or day).
 
- 
                                        
 
- 
                                
 
- 
                        
- 
                (Optional) Choose **Set a dynamic default**to create a default that is user-specific.A *dynamic default*is a per-user default value for the first page load of the dashboard. Use a dynamic default to create a personalized view for each user.Calculated fields can't be used as dynamic defaults. Dynamic defaults don't prevent a user from selecting a different value. If you want to secure the data, you can add row-level locking. For more information, see [Using row-level security with user-based rules to restrict access to a dataset](./restrict-access-to-a-data-set-using-row-level-security.html).This option only appears if you choose a single value parameter. Multivalue parameters can't have dynamic defaults. ###### NoteIf you choose a multivalue parameter, the screen changes to remove the default options. Instead, you see a box with the text **Enter values you want to use for this control**. You can enter multiple values in this box, each on a single line. These values are used as the default selected values in the parameter control. The values here are unioned with what you choose to enter for the parameter control. For more information on parameter controls, see[Parameter Controls](./parameters-controls.html).
- 
                (Optional) Set a reserved value to determine the value of the **Select all**value. The*reserved value*of a parameter is the value that is assigned to a parameter when you choose**Select all**as its value. When you set up a specific reserved value for your parameter, that value is no longer considered a valid parameter value in your dataset. The reserved value can't be used in any*parameter consumers*, such as filters, controls, and calculated fields, and custom actions. Also, it does not appear in the parameter control list. You can choose from**Recommended value**,**Null**, and**Custom value**.**Recommended value**is the default. If you choose**Recommended value**, the reserved value is set to the following values based on the value type:- 
                        Strings: `"ALL_VALUES"`
- 
                        Numbers: `"Long.MIN_VALUE"-9,223,372,036,854,775,808`
- 
                        "Integers: `Int.MIN_VALUE"-2147483648`
 To set a reserved value in your new parameter, choose the **Advanced settings**dropdown list in either the**Create a new parameter**page or the**Edit parameter**page and select the value that you want.
- 
                        
- 
                Choose **Create**or**Update**to complete creating or updating the parameter.

After you create a parameter, you can use it in a variety of ways. You can create a control (such as a button) so that you can choose a value for your parameter. For more information, see the following sections.