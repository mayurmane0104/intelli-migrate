# Features not supported in the new data preparation experience - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/unsupported-features.html](https://docs.aws.amazon.com/quick/latest/userguide/unsupported-features.html)

---

While the new data preparation experience offers enhanced capabilities, some features from the legacy experience are not yet supported. This section outlines these features and provides guidance for handling affected workflows.

When using unsupported data sources, Amazon Quick Sight automatically defaults to the legacy experience. For other unsupported 
        features, select **Switch to legacy experience** in the top right corner of the data preparation page. 
        Rules Datasets created in the legacy experience remain compatible with both legacy and new experience datasets.

## Unsupported data sources

            The following data sources are currently available only in the legacy experience.

| Data Source | Details | 
|---|---|
| Salesforce | Automatically defaults to legacy experience | 
| Google Sheets | Automatically defaults to legacy experience | 
| S3 Analytics | 
 | 

## Other unsupported features

            The following features are currently available only in the legacy experience.

| Feature Category | Unsupported features | 
|---|---|
| Dataset Management | |
| Data Types | |
| Configuration Options | 
 | 
| Parent dataset selection from legacy experience | Parent and child datasets must exist in the same experience environment. You cannot use a legacy experience dataset as a parent for a new experience dataset. | 

## Future development

            
        	Amazon Quick Sight plans to implement these features in the new data preparation experience in the future. This approach ensures that the initial launch for the new data preparation experience prioritizes:

**Enhanced capabilities**

- 
        			Visual transformation workflows 
- 
        			Improved process transparency 
- 
        			Advanced preparation techniques through Divergence 
- 
        			Powerful new features like Append, Aggregate, and Pivot 

**Flexible adoption**

Users can choose between experiences before publishing datasets, ensuring uninterrupted workflows while teams transition at their own pace. This approach allows immediate access to new capabilities while maintaining support for specialized requirements through the legacy experience.