# Build predictive models with SageMaker AI Canvas - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sagemaker-canvas-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/sagemaker-canvas-integration.html)

---

Amazon Quick authors can export data into SageMaker AI Canvas to build ML models that can be sent back to Quick. Authors can use these ML models to augment their datasets with predictive analytics that can be used to build analyses and dashboards.

**Prerequisites**

- 
                A Quick account that's integrated with IAM Identity Center. If your Quick account isn't integrated with IAM Identity Center, create a new Quick account and choose **Use IAM Identity Center enabled application**as the identity provider.- 
                        For more information on IAM Identity Center, see [Getting started](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html).
- 
                        To learn more about integrating your Quick with IAM Identity Center, see [Configure your Amazon Quick account with IAM Identity Center](./setting-up-sso.html#sec-identity-management-identity-center).
- 
                        To import assets from an existing Quick account to a new Quick account that's integrated with IAM Identity Center, see [Asset bundle operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/asset-bundle-ops.html).
 
- 
                        
- 
                A new SageMaker AI domain that is integrated with IAM Identity Center. For more information about onboarding to SageMaker AI Domain with IAM Identity Center, see [Onboard to SageMaker AI Domain using IAM Identity Center](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-sso-users.html).

###### Topics

## Build a predictive model in SageMaker AI Canvas from Amazon Quick Sight

            ###### To build a predictive model in SageMaker AI Canvas

- 
                    Log in to Amazon Quick and navigate to the tabular table or pivot table that you want to create a predictive model for. 
- 
                    Open the on-visual menu and choose **Build a predictive model**.
- 
                    In the **Build a predictive model in SageMaker AI Canvas**pop up that appears, review the information presented and then choose**EXPORT DATA TO SAGEMAKER CANVAS**.
- 
                    In the **Exports**pane that appears, choose**GO TO SAGEMAKER CANVAS**when the export is completed to go to the SageMaker AI Canvas console.
- 
                    In SageMaker AI Canvas, create a predictive model with the data that you exported from Quick Sight. You can choose to follow a guided tour that helps you create the predictive model, or you can skip the tour and work at your own pace. For more information about creating a predictive model in SageMaker AI Canvas, see [Build a model](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-build-model-how-to.html#canvas-build-model-numeric-categorical).
- 
                    Send the predictive model back to Quick Sight. For more information about sending a model from SageMaker AI Canvas to Amazon Quick Sight, see [Send your model to Amazon Quick Sight](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-send-model-to-quicksight.html).

## Create a dataset with a SageMaker AI Canvas model

            After you create a predictive model in SageMaker AI Canvas and send it back to Quick Sight, use the new model to create a new dataset or apply it to an existing dataset.

###### To add a predictive field to a dataset

- 
                    Open the Quick console, choose **Data**at left, and choose the**Datasets**tab.
- 
                    Upload a new dataset or choose an existing dataset. 
- 
                    Choose **Edit**.
- 
                    On the dataset' data prep page, choose **ADD**, and then choose**Add predictive field**to open the**Augment with SageMaker AI**modal.
- 
                    For **Model**, choose the model that you sent to Quick Sight from SageMaker AI Canvas. The schema file automatically populates in the**Advanced settings**pane. Review the inputs, and then choose**Next**.
- 
                    On the **Review outputs**pane, enter a field name and description for a colum to be targeted by the model that you created in SageMaker AI Canvas.
- 
                    When you are finished, choose **Prepare data**.
- 
                    After you choose **Prepare data**, you are redirected to the dataset page. To publish the new dataset, choose,**Publish & Visuallize**.

When you publish a new dataset that uses a model from SageMaker AI Canvas, the data is imported into SPICE and a batch inference job begins in SageMaker AI. It can take up to 10 minutes for these processes to complete.

## Considerations

            The following limitations apply to the creation of SageMaker AI Canvas models with Quick Sight data.

- 
                    The **Build a predictive model**option that is used to send data to SageMaker AI Canvas is only available on table and tabular pivot table visuals. The table or pivot table visual must have between 2 and 1,000 fields and at least 500 rows.
- 
                    Datasets that contain integer or geographic data types will experience schema mapping errors when you add a predictive field to the dataset. To resolve this issue, remove the integer or geographic data types from the dataset or convert them to a new data type.