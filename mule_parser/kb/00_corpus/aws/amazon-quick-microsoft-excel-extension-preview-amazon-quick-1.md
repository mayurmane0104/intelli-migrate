# Amazon Quick Microsoft Excel extension (Preview) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/excel-extension-guide.html](https://docs.aws.amazon.com/quick/latest/userguide/excel-extension-guide.html)

---

###### Note

This extension is currently available as a preview. During the preview period, the extension is fully functional for end users and production workloads. Administrative features such as centralized deployment controls and usage monitoring are being developed and will be available when the extension becomes generally available. Functionality and features may change during the preview period.

The Amazon Quick extension for Excel helps you work with data faster by automating data cleaning, analysis, and visualization tasks while integrating with your enterprise data sources.

You can search for Amazon Quick in the Microsoft Excel app store
            or visit the [Quick
                for Excel Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010611) to add the extension.

Key capabilities include:

- 
                **Data import and preparation:**Pull data from Quick dashboards, structured datasets, spaces, and uploaded files directly into your spreadsheet. Identify inconsistencies and clean data automatically, and apply formatting and templates based on your data and objectives.
- 
                **Spreadsheet debugging:**Ask Quick to explain calculations behind cells or tables, debug and fix formula errors, and highlight anomalies and inconsistencies in your data.
- 
                **Data analysis and insights:**Automatically analyze patterns and trends, create pivot tables and charts with natural language prompts, and perform sensitivity analysis and scenario planning.
- 
                **Spreadsheet automation:**Apply filters, transformations, and conditional formatting using prompts, and generate appropriate templates based on your content and objectives.
- 
                **Enterprise knowledge integration:**Choose an agent or a space to respond from and incorporate relevant information from your organization's knowledge into your spreadsheets. Integrate data from Quick dashboards, spaces, and knowledge bases.
- 
                **External actions:**Perform actions in third-party applications using your configured[action connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html)or apps directly from Excel.

###### Important

- 
                    The Amazon Quick Excel extension uses generative AI to create and execute code within your Excel application sandbox. AI can make mistakes and perform inaccurate actions within your Excel workbook. No spreadsheet data is read when the side panel is closed, and no data is sent to Amazon Quick unless you explicitly send a prompt. 
- 
                    Amazon Quick does not use your user data for service improvement or for training its underlying large language models (LLMs). 

## Amazon Quick Microsoft Excel extension usage guidelines

            As a user, you are responsible for keeping company information safe. The following guidance helps you use Amazon Quick apps securely while maintaining data privacy and compliance.

### Conversation retention and accuracy

Each conversation is stored for 30 days. You can review and manage your conversation history by choosing the conversation history button in the Excel extension.

Amazon Quick uses generative AI. You should review responses for accuracy.

Usage of the Amazon Quick extension for Microsoft Excel is
                    subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

### Security considerations

To protect your organization's data, carefully evaluate usage and plan deployment with data privacy in mind. Amazon Quick maintains strict data privacy by not using customer data for service improvements, not using customer data to enhance language models, and not indexing Microsoft Excel conversations into your company's Amazon Quick instance.

## Sample prompts

            The following prompts demonstrate common ways to use Quick within Excel. You can adapt these to your specific needs.

- 
                    "Import data from my Quick dashboard and identify which items are trending above or below target." 
- 
                    "Create a pivot table showing totals by category and region." 
- 
                    "Generate a chart comparing this quarter's performance to last quarter." 
- 
                    "Explain the formula in cell D5 and suggest a more efficient approach." 
- 
                    "Apply conditional formatting to highlight any values that exceed the threshold by more than 10%." 

###### Tip

For best results, be specific in your prompts. Include names, dates, and goals. You can also reference your Quick spaces, dashboards, and knowledge bases for personalized results.