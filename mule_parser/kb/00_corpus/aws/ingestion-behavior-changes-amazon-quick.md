# Ingestion behavior changes - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/ingestion-behavior-changes.html](https://docs.aws.amazon.com/quick/latest/userguide/ingestion-behavior-changes.html)

---

The new data preparation experience introduces an important change in how data quality issues are handled during SPICE ingestion. This change significantly impacts data completeness and transparency in your datasets.

In the legacy experience, when encountering data type inconsistencies (such as incorrect date formats or 
        [similar issues](./errors-spice-ingestion.html)), the entire row containing problematic cells is skipped 
        during ingestion. This approach results in fewer rows in the final dataset, potentially obscuring data quality issues.

The new experience takes a more granular approach to data inconsistencies. When encountering problematic cells, only the inconsistent values are converted to null values while retaining the entire row. This preservation ensures that related data in other columns remains accessible for analysis.

**Impact on dataset quality**

Datasets created in the new experience will typically contain more rows than their legacy counterparts when the source data contains inconsistencies. This enhanced approach offers several benefits:

- 
                Improved data completeness by retaining all rows 
- 
                Greater transparency in identifying data quality issues 
- 
                Better visibility of problematic values for remediation 
- 
                Preservation of related data in unaffected columns 

This change enables analysts to identify and address data quality issues more effectively, rather than having problematic rows silently omitted from the dataset.