# Integrating Amazon SageMaker AI models with Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sagemaker-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/sagemaker-integration.html)

---

###### Note

You don't need any technical experience in machine learning (ML) to author analyses and dashboards that use the ML-powered features in Amazon Quick Sight.

You can augment your Amazon Quick Enterprise edition data with Amazon SageMaker AI machine learning
        models. You can run inferences on data stored in SPICE imported from any data
        source supported by Quick. For a full list of supported data sources, see [Supported data sources](./supported-data-sources.html). 

Using Quick with SageMaker AI models can save the time that you might otherwise spend managing data movement and writing code. The results are useful both for evaluating the model and—when you're satisfied with the results—for sharing with decision-makers. You can begin immediately after the model is built. Doing this surfaces your data scientists' prebuilt models, and enables you to apply the data science to your datasets. Then you can share these insights in your predictive dashboards. With the Quick serverless approach, the process scales seamlessly, so you don't need to worry about inference or query capacity.

Amazon Quick supports SageMaker AI models that use regression and classification algorithms. You can apply this feature to get predictions for just about any business use case. Some examples include predicting the likelihood of customer churn, employee attrition, scoring sales leads, and assessing credit risks. To use Quick to provide predictions, the SageMaker AI model data for both input and output must be in tabular format. In multiclass or multilabel classification use cases, each output column has to contain a single value. Quick doesn’t support multiple values inside a single column.

###### Topics

## How SageMaker AI integration works

        In general, the process works like this:

- 
                An Amazon Quick administrator adds permissions for Quick to access SageMaker AI. To do this, open **Security & Permissions**settings from the**Manage Quick**page. Go to**Quick access to AWS services**, and add SageMaker AI.When you add these permissions, Quick is added to an AWS Identity and Access Management (IAM) role that provides access to list all the SageMaker AI models in your AWS account. It also provides permissions to run SageMaker AI jobs that have names that are prefixed with `quicksight-auto-generated-`.
- 
                We recommend that you connect to an SageMaker AI model that has an inference pipeline, because it automatically performs data preprocessing. For more information, see [Deploy an Inference Pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html)in the*SageMaker AI Developer Guide.*
- 
                After you identify the data and the pretrained model that you want to use together, the owner of the model creates and provides a schema file. This JSON file is a contract with SageMaker AI. It provides metadata about the fields, data types, column order, output, and settings that the model expects. The optional settings component provides the instance size and count of the compute instances to use for the job. If you're the data scientist who built the model, create this schema file using the format documented following. If you're a consumer of the model, get the schema file from the owner of the model. 
- 
                In Quick, you begin by creating a new dataset with the data that you want to make predictions on. If you're uploading a file, you can add the SageMaker AI model on the upload settings screen. Otherwise, add the model on the data preparation page. Before you proceed, verify the mappings between the dataset and the model. 
- 
                After the data is imported into the dataset, the output fields contain the data returned from SageMaker AI. You use these fields just as you use other fields, within the guidelines described in [Usage guidelines](#sagemaker-usage-guidelines).When you run SageMaker AI integration, Quick passes a request to SageMaker AI to run batch transform jobs with inference pipelines. Quick starts provisions and deployment of the instances needed in your AWS account. When processing is complete, these instances are shut down and terminated. The compute capacity incurs costs only when it's processing models. To make it easier for you to identify them, Quick names all its SageMaker AI jobs with the prefix `quicksight-auto-generated-`.
- 
                The output of the inference is stored in SPICE and appended to the dataset. As soon as the inference is complete, you can use the dataset to create visualizations and dashboards using the prediction data. 
- 
                The data refresh starts every time you save the dataset. You can start the data refresh process manually by refreshing the SPICE dataset, or you can schedule it to run at a regular interval. During each data refresh, the system automatically calls SageMaker AI batch transform to update the output fields with new data. You can use the Amazon Quick Sight SPICE ingestion API operations to control the data refresh process. For more information about using these API operations, see the [Amazon Quick Sight API Reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/qs-api-overview.html).

## Costs incurred (no additional costs with integration itself)

        Using this feature doesn't require an additional fee in itself. Your costs include the following:

- 
                The cost of model deployment through SageMaker AI, which is incurred only when the model is running. Saving a dataset—after either creating or editing it—or refreshing its data starts the data ingestion process. This process includes calling SageMaker AI if the dataset has inferred fields. Costs are incurred in the same AWS account where your Quick subscription is. 
- 
                Your Quick subscription costs are as follows: - 
                        The cost of storing your data in the in-memory calculation engine in Quick (SPICE). If you are adding new data to SPICE, you might need to purchase enough SPICE capacity to accommodate it. 
- 
                        Quick subscriptions for the authors or admins who build the datasets. 
- 
                        Pay-per-session charges for viewers (readers) to access interactive dashboards. 
 
- 
                        

## Usage guidelines

        In Amazon Quick, the following usage guidelines apply to this Enterprise edition feature:

- 
                The processing of the model occurs in SPICE. Therefore, it can only apply to datasets that are stored in SPICE. The process currently supports up to 500 million rows per dataset. 
- 
                Only Quick admins or authors can augment datasets with ML models. Readers can only view the results when they are part of a dashboard. 
- 
                Each dataset can work with one and only one ML model. 
- 
                Output fields can't be used to calculate new fields. 
- 
                Datasets can't be filtered by fields that are integrated with the model. In other words, if your dataset field is currently mapped to the ML model, you can't filter on that field. 

In SageMaker AI, the following usage guidelines apply to a pretrained model that you use with Amazon Quick Sight:

- 
                When you create the model, associate it with the Amazon Resource Name (ARN) for the appropriate IAM role. The IAM role for the SageMaker AI model needs to have access to the Amazon S3 bucket that Amazon Quick Sight uses. 
- 
                Make sure that your model supports .csv files for both input and output. Make sure that your data is in a tabular format. 
- 
                Provide a schema file that contains metadata about the model, including the list of input and output fields. Currently, you must create this schema file manually. 
- 
                Consider the amount of time that it takes to complete your inference, which depends on a number of factors. These include the complexity of the model, the amount of data, and the compute capacity defined. Completing the inference can take several minutes to several hours. Amazon Quick Sight caps all data ingestion and inferencing jobs to a maximum of 10 hours. To reduce the time it takes to perform an inference, consider increasing the instance size or the number of instances. 
- 
                Currently, you can use only batch transforms for integration with SageMaker AI, not real-time data. You can't use an SageMaker AI endpoint. 

## Defining the schema file

        Before you use an SageMaker AI model with Quick Sight data, create the JSON schema file that contains the metadata that Amazon Quick Sight needs to process the model. The Amazon Quick author or admin uploads the schema file when configuring the dataset.

The schema fields are defined as follows. All fields are required unless specified in the following description. Attributes are case-sensitive.

- 
                    *inputContentType*
- 
                    The content type that this SageMaker AI model expects for the input data. The only supported value for this is `"text/csv"`. Quick Sight doesn't include any of the header names that you add to the input file.
- 
                    *outputContentType*
- 
                    The content type of the output that is produced by the SageMaker AI model that you want to use. The only supported value for this is `"text/csv"`.
- 
                    *input*
- 
                    A list of features that the model expects in the input data. Quick Sight produces the input data in exactly the same order. This list contains the following attributes: - 
                            *name*– The name of the column. If possible, make this the same as the name of the corresponding column in the QuickSight dataset. This attribute is limited to 100 characters.
- 
                            *type*– The data type of this column. This attribute takes the values`"INTEGER"`,`"STRING"`, and`"DECIMAL"`.
- 
                            *nullable*– (Optional) The nullability of the field. The default value is`true`. If you set`nullable`to`false`, Quick Sight drops rows that don't contain this value before calling SageMaker AI. Doing this helps avoid causing SageMaker AI to fail on missing required data.
 
- 
                            
- 
                    *output*
- 
                    A list of output columns that the SageMaker AI model produces. Quick Sight expects these fields in exactly the same order. This list contains the following attributes: - 
                            *name*– This name becomes the default name for the corresponding new column that's created in Quick Sight. You can override the name specified here in Quick Sight. This attribute is limited to 100 characters.
- 
                            *type*– The data type of this column. This attribute takes the values`"INTEGER"`,`"STRING"`, and`"DECIMAL"`.
 
- 
                            
- 
                    *instanceTypes*
- 
                    A list of the ML instance types that SageMaker AI can provision to run the transform job. The list is provided to the Amazon Quick user to choose from. This list is limited to the types supported by SageMaker AI. For more information on supported types, see [TransformResources](https://docs.aws.amazon.com/sagemaker/latest/dg/API_TransformResources.html)in the*SageMaker AI Developer Guide.*
- 
                    *defaultInstanceType*
- 
                    (Optional) The instance type that is presented as the default option in the SageMaker AI wizard in Quick Sight. Include this instance type in `instanceTypes`.
- 
                    *instanceCount*
- 
                    (Optional) The instance count defines how many of the selected instances for SageMaker AI to provision to run the transform job. This value must be a positive integer. 
- 
                    *description*
- 
                    This field provides a place for the person who owns the SageMaker AI model to communicate with the person who is using this model in Quick Sight. Use this field to provide hints about successfully using this model. For example, this field can contain information about selecting an effective instance type to choose from the list in `instanceTypes`, based on the size of dataset. This field is limited to 1,000 characters.
- 
                    *version*
- 
                    The version of the schema, for example " `1.0"`.

The following example shows the structure of the JSON in the schema file.

```
{
        "inputContentType": "CSV",
        "outputContentType": "CSV",
        "input": [
            {
                "name": "buying",
                "type": "STRING"
            },
            {
                "name": "maint",
                "type": "STRING"
            },
            {
                "name": "doors",
                "type": "INTEGER"
            },
            {
                "name": "persons",
                "type": "INTEGER"
            },
            {
                "name": "lug_boot",
                "type": "STRING"
            },
            {
                "name": "safety",
                "type": "STRING"
            }
        ],
        "output": [
            {
                "name": "Acceptability",
                "type": "STRING"
            }
        ],
        "description": "Use ml.m4.xlarge instance for small datasets, and ml.m4.4xlarge for datasets over 10 GB",
        "version": "1.0",
        "instanceCount": 1,
        "instanceTypes": [
            "ml.m4.xlarge",
            "ml.m4.4xlarge"
        ],
        "defaultInstanceType": "ml.m4.xlarge"
    }
```
The structure of the schema file is related to the kind of model that is used in examples provided by SageMaker AI.

## Adding a SageMaker AI model to your Quick Sight dataset

        Using the following procedure, you can add a pretrained SageMaker AI model to your dataset, so that you can use predictive data in analyses and dashboards.

Before you begin, have the following items available:

- 
                The data that you want to use to build the dataset. 
- 
                The name of the SageMaker AI model that you want to use to augment the dataset. 
- 
                The schema of the model. This schema includes field name mappings and data types. It's helpful if it also contains recommended settings for instance type and number of instances to use. 

###### To augment your Amazon Quick Sight dataset with SageMaker AI

- 
                Create a new dataset from the start page by choosing **Datasets**, and then choose**New dataset**.You can also edit an existing dataset. 
- 
                Choose **Augment with SageMaker**on the data preparation screen.
- 
                For **Select your model**, choose the following settings:- 
                        **Model**– Choose the SageMaker AI model to use to infer fields.
- 
                        **Name**– Provide a descriptive name for the model.
- 
                        **Schema**– Upload the JSON schema file provided for the model.
- 
                        **Advanced settings**– QuickSight recommends the selected defaults based on your dataset. You can use specific runtime settings to balance the speed and cost of your job. To do this, enter the SageMaker AI ML instance types for**Instance type**and number of instances for**Count**.
 Choose **Next**to continue.
- 
                        
- 
                For **Review inputs**, review the fields that are mapped to your dataset. Quick Sight attempts to automatically map the fields in your schema to the fields in your dataset. You can make changes here if the mapping needs adjustment.Choose **Next**to continue.
- 
                For **Review outputs**, view the fields that are added to your dataset.Choose **Save and prepare data**to confirm your choices.
- 
                To refresh the data, choose the dataset to view details. Then either choose **Refresh Now**to manually refresh the data, or choose**Schedule refresh**to set up a regular refresh interval. During each data refresh, the system automatically runs the SageMaker AI batch transform job to update the output fields with new data.