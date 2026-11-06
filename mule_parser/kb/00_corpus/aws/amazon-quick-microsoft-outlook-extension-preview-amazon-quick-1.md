# Amazon Quick Microsoft Outlook extension (Preview) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/outlook-extension-guide.html](https://docs.aws.amazon.com/quick/latest/userguide/outlook-extension-guide.html)

---

###### Note

This extension is currently available as a preview. During the preview period, the extension is fully functional for end users and production workloads. Administrative features such as centralized deployment controls and usage monitoring are being developed and will be available when the extension becomes generally available. Functionality and features may change during the preview period. We recommend using this extension instead of the legacy Microsoft Outlook extension for new deployments.

The Amazon Quick extension for Outlook helps you manage your entire inbox using natural language. You can summarize unread messages, organize your inbox, schedule meetings, and draft responses, all without leaving Outlook.

You can search for Amazon Quick in the Microsoft Outlook app store
            or visit the [Quick
                for Outlook Microsoft store page](https://marketplace.microsoft.com/en-us/product/WA200010695) to add the extension.

Key capabilities include:

- 
                **Inbox management:**Summarize and prioritize your unread emails, search for specific emails or discussions using natural language queries, and organize your inbox by moving emails to folders, flagging messages for follow-up, and more.
- 
                **Calendar and meeting management:**Summarize your calendar, find optimal meeting times with coworkers, and schedule meetings using natural language instructions.
- 
                **Email summaries and replies:**Open the Quick side panel to ask questions about an email thread in focus or generate a contextual reply.
- 
                **Enterprise knowledge integration:**Use Quick's knowledge sources to draft contextual responses to emails or to perform inbox and calendar tasks.
- 
                **External actions:**Perform actions in third-party applications using your configured[action connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html)or apps directly from Outlook.

###### Important

- 
                    The Amazon Quick Outlook extension uses generative AI to create and execute code within your Outlook application sandbox. AI can make mistakes and perform inaccurate actions within your Outlook mailbox. No email or content is read when the side panel is closed, and no data is sent to Amazon Quick unless you explicitly send a prompt. 
- 
                    Amazon Quick does not use your user data for service improvement or for training its underlying large language models (LLMs). 

###### Note

Some features, such as inbox prioritization, calendar management, and email
                organization, require Microsoft Graph API permissions that must be
                granted by your administrator. If you are unable to perform these tasks, contact
                your administrator to ensure the required Graph API permissions have been approved
                for your organization. For more information, see [Microsoft Outlook extension permissions](./outlook-extension.html#outlook-permissions) in the admin guide.

## Amazon Quick Microsoft Outlook extension usage guidelines

            As a user, you are responsible for keeping company information safe. The following guidance helps you use Amazon Quick apps securely while maintaining data privacy and compliance.

### Conversation retention and accuracy

Each conversation is stored for 30 days. You can review and manage your conversation history by choosing the conversation history button in the Outlook extension.

Amazon Quick uses generative AI. You should review responses for accuracy.

Usage of the Amazon Quick extension for Microsoft Outlook is
                    subject to the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

### Security considerations

When you use Amazon Quick with email content, remember that responses reflect individual user permissions and content may include information not accessible to all email recipients. It may generate responses that contain sensitive data that can't be publicly shared.

To protect your organization's data, carefully evaluate email usage and plan deployment with data privacy in mind. Amazon Quick maintains strict data privacy by not using customer data for service improvements, not using customer data to enhance language models, and not indexing Microsoft Outlook conversations into your company's Amazon Quick instance.

## Sample prompts

            The following prompts demonstrate common ways to use Quick within Outlook. You can adapt these to your specific needs.

- 
                    "Summarize all unread emails and highlight any that need urgent responses today." 
- 
                    "Draft a follow-up email to [contact name] referencing the key points from this thread." 
- 
                    "Schedule a 30-minute meeting with the contacts in this email thread for next week." 
- 
                    "Find all emails discussing [project name] and create a summary of action items." 
- 
                    "Using data from my Quick space, draft a status update email for the leadership team on our quarterly metrics." 

###### Tip

For best results, be specific in your prompts. Include names, dates, and goals. You can also reference your Quick spaces, dashboards, and knowledge bases for personalized results.