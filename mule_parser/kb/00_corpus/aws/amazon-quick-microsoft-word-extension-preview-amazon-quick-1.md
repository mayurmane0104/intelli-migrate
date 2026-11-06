# Amazon Quick Microsoft Word extension (Preview) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/word-extension-guide.html](https://docs.aws.amazon.com/quick/latest/userguide/word-extension-guide.html)

---

###### Note

This extension is currently available as a preview. During the preview period, the extension is fully functional for end users and production workloads. Administrative features such as centralized deployment controls and usage monitoring are being developed and will be available when the extension becomes generally available. Functionality and features may change during the preview period. We recommend using this extension instead of the legacy Microsoft Word extension for new deployments.

The Amazon Quick extension for Word helps you create professional documents faster by working directly in your document to generate, edit, and review content using natural language instructions.

You can search for Amazon Quick in the Microsoft Word app store
            or visit the [Quick
                for Word Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010615) to add the extension.

Key capabilities include:

- 
                **Content generation and editing:**Generate formatted content including headings, tables, and styled text using plain language instructions. Go from a blank page to a review-ready draft without manually formatting. Quick works directly in the document itself, automatically applying proper formatting and structure.
- 
                **Document review with track changes:**Ask Quick to review your document and suggest edits based on any criteria or Quick data of your choice. Suggestions appear in Word's built-in track changes and comments, so you stay in control of what gets accepted.
- 
                **Style and formatting matching:**Quick automatically matches your document's existing style, structure, and formatting. Attach reference documents or templates to apply specific formatting standards.
- 
                **Enterprise knowledge integration:**Include relevant information from your Quick knowledge sources directly into your document.
- 
                **External actions:**Perform actions in third-party applications using your configured[action connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html)or apps directly from Word.

###### Important

- 
                    The Amazon Quick Word extension uses generative AI to create and execute code within your Word application sandbox. AI can make mistakes and perform inaccurate actions within your Word document. No document content is read when the side panel is closed, and no data is sent to Amazon Quick unless you explicitly send a prompt. 
- 
                    Amazon Quick does not use your user data for service improvement or for training its underlying large language models (LLMs). 

## Amazon Quick Microsoft Word extension usage guidelines

            As a user, you are responsible for keeping company information safe. The following guidance helps you use Amazon Quick apps securely while maintaining data privacy and compliance.

### Conversation retention and accuracy

Each conversation is stored for 30 days. You can review and manage your conversation history by choosing the conversation history button in the Word extension.

Amazon Quick uses generative AI. You should review responses for accuracy.

Usage of the Amazon Quick extension for Microsoft Word is
                    subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

### Security considerations

To protect your organization's data, carefully evaluate usage and plan deployment with data privacy in mind. Amazon Quick maintains strict data privacy by not using customer data for service improvements, not using customer data to enhance language models, and not indexing Microsoft Word conversations into your company's Amazon Quick instance.

## Sample prompts

            The following prompts demonstrate common ways to use Quick within Word. You can adapt these to your specific needs.

- 
                    "Create a project proposal including an executive summary, timeline, and budget section, pulling data from my Quick space." 
- 
                    "Review this document with Track Changes enabled and suggest edits to improve clarity and tone." 
- 
                    "Read the comments in this document and address each piece of feedback, making the requested changes directly." 
- 
                    "Generate a one-page executive summary of this report highlighting the key findings." 
- 
                    "Add a competitive comparison table to this document using data from my Quick dashboard." 

###### Tip

For best results, be specific in your prompts. Include names, dates, and goals. You can attach reference documents or templates to guide formatting and style.