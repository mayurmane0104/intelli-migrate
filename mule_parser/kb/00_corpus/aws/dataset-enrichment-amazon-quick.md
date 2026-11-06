# Dataset Enrichment - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dataset-enrichment.html](https://docs.aws.amazon.com/quick/latest/userguide/dataset-enrichment.html)

---

Dataset Enrichment is a capability in Amazon Quick Sight that enables dataset authors to add rich semantic metadata to their datasets. By providing descriptions, custom instructions, and structured metadata, you ensure that both human consumers and AI-powered agents understand what a dataset represents and how to use it.

## Dataset Enrichment overview

            Dataset Enrichment enables authors and author pros to annotate datasets with semantic context at both the dataset level and the column level. This metadata connects raw data with business context. It serves two audiences:

- 
                    **Dataset Consumers (other Authors, Reader Pros)**– Gain better business context about what each dataset contains, its purpose, and appropriate use cases.
- 
                    **AI Agents**– Receive richer contextual information to generate more accurate queries and interpretations when answering questions through Dataset Q&A.

## Dataset Enrichment components

             
                ### Dataset-level enrichment

###### Important

Do not add sensitive information to the
                        **Dataset Description** or **Custom Instructions** fields. This information is
                        visible to all dataset viewers.

- **Dataset Description**
- 
                            A business-level summary of what the dataset represents, its scope, and intended use. This description is visible to all dataset consumers in the UI, helping them quickly understand the dataset's purpose. Maximum length: 5,000 characters. 
- **Custom Instructions**
- 
                            Free-form text instructions specifically consumed by AI agents. These instructions guide the AI on how to interpret, query, and reason about the dataset. Maximum length: 5,000 characters. 
- **File Upload**
- 
                            You can upload a single file in YAML, JSON, or TXT format containing catalog-grade semantic metadata exported from third-party tools (for example, Databricks, dbt, or Alation). This enables hundreds of column definitions, business rules, and metric calculations to be ingested in a single upload – eliminating manual column-by-column entry. Maximum length: 50,000 characters. 

### Column-level enrichment

- **Folders**
- 
                            Organize columns into logical groupings for easier navigation and understanding. 
- **Column Description**
- 
                            A human-readable description of what each column represents, its valid values, and business meaning. Maximum length: 500 characters. 
- **Additional Notes**
- 
                            Supplementary context for each column, such as data quality considerations, related tables, or common analysis patterns. Maximum length: 2,000 characters. 

## Benefits of Dataset Enrichment

            - 
                    **More accurate AI-powered Dataset Q&A**– Richer semantic context helps AI agents generate more precise SQL queries and interpretations, leading to significantly better answers.
- 
                    **Better understanding for consumers**– Descriptions and metadata help all users across the organization understand what datasets contain and how to use them correctly.
- 
                    **Scale metadata from external catalogs**– File Upload allows authors to bring in rich metadata from third-party catalog tools in a single operation, rather than manually entering definitions column by column.

## Permissions and requirements

            Authors and author pros with Enterprise licenses can enrich any dataset they own or manage.

## Accessing Dataset Enrichment

            To access Dataset Enrichment, complete the following steps.

- 
                    Save your dataset in the data preparation experience. 
- 
                    Choose the **Output**tab.
- 
                    Enter the **Dataset Description**and**Custom Instructions**, or upload a semantic metadata file.

## Writing effective custom instructions

            Custom Instructions are the most impactful component of Dataset Enrichment. They directly guide AI agents on how to interpret and query a dataset. The following are examples of effective and ineffective custom instructions.

### Good custom instructions

**Example 1 – Revenue Dataset**

```
This dataset contains net revenue after returns and discounts, calculated
on an accrual basis. Revenue is recognized at the point of sale for retail
transactions and upon delivery confirmation for B2B orders. All figures are
in USD. The 'revenue' column specifically excludes taxes, shipping fees,
and promotional credits. For year-over-year comparisons, use the
'fiscal_year' field rather than 'calendar_year' as our fiscal year runs
April–March.
```
Why it's effective:

- 
                        Clarifies ambiguous terms (net vs. gross revenue) 
- 
                        Defines calculation methodology 
- 
                        Specifies currency and exclusions 
- 
                        Provides guidance on how to use specific fields correctly 

**Example 2 – Customer Dataset**

```
Customer status definitions: 'Active' = purchased within last 12 months;
'Dormant' = 12–24 months since last purchase; 'Churned' = 24+ months
inactive. The 'customer_segment' field uses RFM analysis (Recency,
Frequency, Monetary). 'Lifetime_value' is calculated as total historical
spend, not predictive LTV. When analyzing customer counts, always filter
out 'is_test_account = true' to exclude internal test data.
```
Why it's effective:

- 
                        Defines business logic and thresholds 
- 
                        Explains acronyms and methodologies 
- 
                        Warns about data quality considerations 
- 
                        Guides proper filtering for accurate analysis 

### Ineffective custom instructions

**Example – Customer Dataset**

```
Contains customer information including names, addresses, purchase history,
and other details. Use this for customer analysis.
```
Why it's ineffective:

- 
                        Describes what is already obvious from column names 
- 
                        Provides no business context or definitions 
- 
                        Offers no guidance on data quality, calculations, or proper usage 
- 
                        Does not help the AI distinguish between similar concepts 

### Key principles for writing good custom instructions

- 
                        **Clarify ambiguities**– Define terms that can have multiple interpretations.
- 
                        **Explain business logic**– Document calculations, thresholds, and categorizations.
- 
                        **Provide context**– Include units, time periods, currencies, and scope.
- 
                        **Guide usage**– Explain which fields to use for specific analyses.
- 
                        **Warn about edge cases**– Note data quality issues, test records, or special cases.
- 
                        **Be specific**– Use concrete examples and precise language.

## Two approaches to semantic enrichment

             
                ### Manual UI-based annotation

Dataset authors directly add dataset and column descriptions and custom instructions through the Quick Sight interface. Quick Sight displays descriptions prominently in the UI, helping all users understand dataset content, column definitions, and appropriate use cases.

### File upload from external catalogs

Dataset authors can export semantic metadata from external catalogs and attach a file per dataset in YAML, JSON, or TXT format through the API or UI. While this information is used by AI models rather than displayed in the UI, it enables catalog-grade metadata at scale.

## The consumption layer: Dataset Q&A

            Dataset Q&A is the consumption layer that uses Dataset Enrichment metadata. It enables users to ask open-ended, natural language questions directly against the datasets they have access to – without needing pre-built dashboards or manually configured topics.

The AI agent uses enriched context in the following ways:

- 
                    **Asset discovery**– The agent uses dataset descriptions and semantic metadata to identify the right dataset for the user's question.
- 
                    **Text-to-SQL generation**– Custom instructions, column descriptions, and uploaded metadata guide the AI in generating more accurate SQL queries.
- 
                    **Governed responses**– All responses respect Row-Level Security (RLS) and Column-Level Security (CLS) rules.

Without enrichment, the AI agent only has column names and data types to work with – which are often ambiguous. With enrichment, the agent receives the full business context needed to:

- 
                    Disambiguate similar fields and concepts 
- 
                    Apply correct calculations and filters 
- 
                    Understand business-specific thresholds and categorizations 
- 
                    Exclude test data and handle edge cases appropriately 

After you add semantic context to a dataset, users can reference the dataset in Q&A and query it through chat. The AI agent consumes the added metadata to deliver more accurate responses.

## Summary

            Dataset Enrichment adds semantic metadata to datasets for AI-powered analysis. By investing a few minutes in adding descriptions, custom instructions, and metadata files, dataset authors can improve the accuracy of AI-powered Q&A while making their datasets more understandable and accessible to every consumer across the organization.