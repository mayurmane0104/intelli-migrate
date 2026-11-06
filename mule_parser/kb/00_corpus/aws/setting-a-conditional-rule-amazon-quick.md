# Setting a conditional rule - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/setting-a-conditional-rule.title.html](https://docs.aws.amazon.com/quick/latest/userguide/setting-a-conditional-rule.title.html)

---

When you set up a conditional rule, you create a conditional statement that
                    will hide or show a visual when a specific condition is met. You can currently
                    create conditional rules that hide or show a visual. If you want to create a
                    conditional rule that makes a hidden visual appear, choose **Hide this
                        visual by default** in the **Rules** menu of the
                        **Properties** pane. 

###### Note

Before you begin, make a parameter and a corresponding parameter control
                        to base your new conditional rule on. Supported parameters are string
                        parameters and number parameters. For more information about parameters and
                        parameter controls, see [Parameters in Amazon Quick](./parameters-in-quicksight.html).

###### To set a conditional rule

- 
                        From the Quick homepage, choose **Analyses**, and then choose the analysis you want to customize.
- 
                        Choose the visual that you want to add a rule to. 
- 
                        On the menu in the upper-right hand side of the visual, choose **Properties**.
- 
                        In the **Properties**pane that appears on the left, choose**Interactions**, and then choose**Rules**.
- 
                        Choose **ADD RULE**.
- 
                        In the first menu in the **Add rule**pane, choose the parameter you want.
- 
                        In the second menu in the **Add rule**pane, choose which condition you want. For string parameters, supported conditions are**Equals**,**Starts with**,**Contains**, and**Does not equal**. For number parameters, supported conditions are**Equals**,**Starts with**,**Contains**, and**Does not equal**.
- 
                        Enter the value you want the conditional rule to meet. ###### NoteValues are case-sensitive. 
- 
                        Choose **Add rule**to apply the new conditional rule to the visual. To cancel the rule, choose**Cancel**.

Conditional rules can also be edited and deleted.

###### To edit a conditional rule

- 
                        On the menu in the upper-right hand side of the visual, choose **Properties**.
- 
                        In the **Properties**pane that appears on the left, choose**Interactions**, and then choose**Rules**.
- 
                        Choose the menu icon on the right-hand side of the rule you want to edit, and choose **Edit**.
- 
                        Make the changes that you want and choose **Save**.

###### To delete a conditional rule

- 
                        On the menu in the upper-right hand side of the visual, choose **Properties**.
- 
                        In the **Properties**pane that appears on the left, choose**Interactions**, and then choose**Rules**.
- 
                        Choose the menu icon on the right-hand side of the rule you want to edit and choose **Delete**.