# Using dataset parameters in Quick analyses - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-analysis.html](https://docs.aws.amazon.com/quick/latest/userguide/dataset-parameters-analysis.html)

---

Once you create a dataset parameter, after you add the dataset to an analysis, map the dataset parameter to a new or existing analysis parameter. After you map a dataset parameter to an analysis parameter, you can use them with filters, controls, and any other analysis parameter feature.

You can manage your dataset parameters in the **Parameters** pane of
            the analysis that is using the dataset that the parameters belong to. In the
                **Dataset Parameters** section of the
                **Parameters** pane, you can choose to see only the unmapped
            dataset parameters (default). Alternatively, you can choose to see all mapped and
            unmapped dataset parameters by choosing **ALL** from the
                **Viewing** dropdown.

## Mapping dataset parameters in new Quick analyses

            When you create a new analysis from a dataset that contains parameters, you need
                to map the dataset parameters to the analysis before you can use them. This is also
                true when you add a dataset with parameters to an analysis. You can view all
                unmapped parameters in an analysis in the **Parameters** pane of
                the analysis. Alternatively, choose **VIEW** in the notification
                message that appears in the top right of the page when you create the analysis or
                add the dataset.

###### To map a dataset parameter to an analysis parameter

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose the analysis that you want to change. 
- 
                    Choose the **Parameters**icon to open the**Parameters**pane.
- 
                    Choose the ellipsis (three dots) next to the dataset parameter that you want to map, choose **Map Parameter**, and then choose the analysis parameter that you want to map your dataset parameter to.If your analysis doesn't have any analysis parameters, you can choose **Map parameter**and**Create new**to create an analysis parameter that is automatically mapped to the dataset parameter upon creation.- 
                            (Optional) In the **Create new parameter**pop-up that appears, for**Name**, enter a name for the new analysis parameter.
- 
                            (Optional) For **Static default value**, choose the static default value that you want the parameter to have.
- 
                            (Optional) Choose **Set a dynamic default**to set a dynamic default for the new parameter.
- 
                            In the **Mapped dataset parameters**table, you will see the dataset parameter that you are mapping to the new analysis parameter. You can add other dataset parameters to this analysis parameter by choosing the**ADD DATASET PARAMETER**dropdown and then choosing the parameter that you want to map. You can unmap a dataset parameter by choosing the**Remove**button next to the dataset parameter that you want to remove.
 For more information on creating analysis parameters, see [Setting up parameters in Amazon Quick](./parameters-set-up.html).
- 
                            

When you map a dataset parameter to an analysis parameter, the analysis parameter represents the dataset parameter wherever it is used in the analysis.

You can also map and unmap dataset parameters to analysis parameters in the
                    **Edit parameter** window. To open the **Edit
                    parameter** window, navigate to the **Parameters**
                pane, choose the ellipsis (three dots) next to the analysis parameter that you want
                to change, and then choose **Edit parameter**. You can add other
                dataset parameters to this analysis parameter by choosing the **ADD DATASET
                    PARAMETER** dropdown and then choosing the parameter that you want to
                map. You can unmap a dataset parameter by choosing the **Remove**
                button next to the dataset parameter that you want to remove. You can also remove
                all mapped dataset parameters by choosing **REMOVE ALL**. When you
                are done making changes, choose **Update**.

When you delete an analysis parameter, all dataset parameters are unmapped from
                the analysis and appear in the **UNMAPPED** section of the
                    **Parameters** pane. You can only map a dataset parameter to
                one analysis parameter at a time. To map a dataset parameter to a different analysis
                parameter, unmap the dataset parameter and then map it to the new analysis
                parameter.

## Adding filter controls to mapped analysis parameters

            After you map a dataset parameter to an analysis parameter in Quick, you can create filter controls for filters, actions, calculated fields, titles, descriptions, and URLs.

###### To add a control to a mapped parameter

- 
                    In the **Parameters**pane of the analysis page, choose the ellipsis (three dots) next to the mapped analysis parameter that you want, and then choose**Add control**.
- 
                    In the **Add control**window that appears, enter the**Name**that you want and choose the**Style**that you want the control to have. For single value controls, choose between`Dropdown`,`List`, and`Text field`. For multivalue controls, choose`Dropdown`.
- 
                    Choose **Add**to create the control.