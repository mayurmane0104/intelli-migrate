# Improve Q&A accuracy with custom instructions - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-improve-qa-accuracy-with-custom-instructions.html](https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-improve-qa-accuracy-with-custom-instructions.html)

---

Custom Instructions enables Authors to curate Amazon Q's responses to questions by adding domain-specific knowledge that can’t be captured through a topic’s metadata settings, such as synonyms or semantic types. By providing these metadata descriptions or custom instructions, Authors can guide Amazon Q to align its responses with distinct definitions, preferences, and expert knowledge—ensuring more accurate, relevant, and tailored answers that are better suited for their business needs.

Use the following table to understand when and how to apply different types of metadata to improve Q&A answer accuracy. Each metadata type plays a unique role in clarifying context, resolving ambiguity, and ensuring that answers are aligned with business rules or domain-specific terminology.

| Metadata Type | When to Use | How it Improves Answer Accuracy | 
|---|---|---|
| Field-Level Description | When the Q&A system needs to understand ambiguous or
                                domain-specific column names (for example,  | Clarifies field semantics so the model can answer more precisely
                                (for example, interpreting  | 
| Topic-Level Description | When users may ask broad or ambiguous questions and Amazon Q needs more context about the topic's overall purpose (for example, sales performance vs. clinical trial data). | Helps disambiguate general terms and steer answers toward the right domain (for example, sales vs. marketing). | 
| Dataset Description | When users have access to multiple datasets and the Q&A system needs to identify which one best fits the question. | Enables dataset selection logic by providing context about each dataset's purpose and content. | 
| Topic-Level Custom Instructions | When a topic has specific business rules, timeframes, or definitions (for example, fiscal year ≢ calendar year). | Applies custom logic or definitions (for example, defining Q1 as August-October) to tailor answers appropriately. | 

## Adding field-level descriptions

            ###### To add field-level descriptions:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Topics**and then open the topic you want to add descriptions for.
- 
                    From the topic details page, select the **Data**tab then choose the**Data Fields**sub-tab.
- 
                    Add a description to improve answer accuracy for each included field. This is especially important for field names that contain bespoke corporate knowledge to understand. 

 If you have multiple date fields, for example, clear descriptions can help Amazon Q
                distinguish between them and choose the most relevant one based on the user’s
                question. In the sample below, an Author added descriptions for **Solution
                    Create** and **Topic Create**, which enables Amazon Q to
                more accurately select the appropriate date field in context. 

![solution create description](/images/quick/latest/userguide/images/solution_create.png) 

                 
                 
            ![topic create description](/images/quick/latest/userguide/images/topic_create.png) 

                 
                 
            ## Adding topic-level descriptions

            ###### To add topic-level descriptions:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Topics**and then open the topic you want to add descriptions for.
- 
                    From the topic details page, select the **Summary**tab.
- 
                    Under **Topic Details**, add a description to provide more context about the topic's overall purpose.

## Adding dataset descriptions

            ###### To add dataset descriptions:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Topics**and then open the topic you want to add descriptions for.
- 
                    From the topic details page, select the **Data**tab then choose the**Datasets**sub-tab.
- 
                    Add a description to help improve dataset selection logic. 

## Adding topic-level custom instructions

            ###### To add custom instructions:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Topics**and then open the topic you want to add descriptions for.
- 
                    From the topics details page, select the **Custom Instructions**tab.
- 
                    Add topic-level guidance to help the chat better understand the context, terminology, or intent that is specific to the selected topic. This can include disambiguation tips, field relationships, definitions for terms that can’t be captured in a calculated field or topic filter, or instructions for customizing relative date ranges. 

## Best practices for writing custom instructions

            **Match cell values precisely**

- 
                    Use the exact cell value from the database, including casing and formatting. 
- 
                    If the value is ambiguous, reference its source column to clarify. 

Examples:

- 
                    Instead of: " *AMZ are Amazon customers*"Use: " *AMZ are 'Amazon.com, Inc.' customers*"
- 
                    Instead of: " *ETPs are enterprise customers*"Use: " *ETPs are customers from the enterprise Segment*"

**Be specific and quantitative**

Avoid vague language—be clear about filters, thresholds, and source columns.

Example:

- 
                    Instead of: " *Filter large customers when talking about sales*"Use: " *Filter customers where Annual Revenue > $1M when talking about sales*"

**Use formatting for clarity, not function**

Spacing and line breaks do not affect model behavior, but help authors read and maintain instructions more easily.

**Understand what custom instructions cannot do**

Custom instructions improve the understanding of your business context, but they do not add new capabilities. These instructions will not:

- 
                    Change chart type selections 
- 
                    Perform calculations or fill nulls 
- 
                    Create new fields 
- 
                    Control formatting, colors, or legends 
- 
                    Alter the narrative or number/type of visuals 

## Adding field-level descriptions in data preparation for dashboard-based Q&A

            In addition to Topic-based descriptions, you can create field-level definitions to
                enhance [Dashboard Q&A](./dashboard-qa.html) functionality. Adding
                specific definitions to individual fields during the data preparation phase improves
                the answer accuracy when users ask questions about particular dashboard
                elements.

###### To add field-level descriptions for dashboard-based Q&A:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    Choose **Data**, open a dataset that you have access to, and select**EDIT DATASET**.
- 
                    For each relevant field, choose the three-dot menu and select **Edit name & description**.
- 
                    Add a description to enhance answers for dashboard-related questions. 
- 
                    Choose **Apply**to save your changes.