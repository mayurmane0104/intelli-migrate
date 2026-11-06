# Amazon Quick Microsoft Word extension user guide - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/legacy-word-extension-user-guide.html](https://docs.aws.amazon.com/quick/latest/userguide/legacy-word-extension-user-guide.html)

---

As a user, you can access Amazon Quick directly within Microsoft Word to get AI-powered assistance without leaving your workspace. The extension integrates seamlessly into your Microsoft Word environment, providing instant access to knowledge bases and intelligent responses.

###### Topics

## Add the Quick Microsoft Word extension

                Install the Amazon Quick app in your Microsoft Word workspace to enable AI-powered assistance. This one-time setup makes Amazon Quick accessible throughout your Microsoft Word environment.

- 
                        Open Microsoft Word for the web or the desktop application. 
- 
                        Navigate to **Insert**>**Get Add-ins**.
- 
                        Search for **Amazon Quick**in the**Office Add-ins**store.
- 
                        Select **Add**to install the Quick add-in.
- 
                        Once the add-in is installed, you can use your Quick **Add-In**.

## Access Quick in your Microsoft Word home menu at any time

                Once you've added Quick to your Microsoft Word environment, you can access it conveniently through the home menu for quick assistance without interrupting your document workflow. The home menu provides persistent access to Quick while you work with documents.

## Microsoft Word extension use cases

                With Quick integrated into Microsoft Word, you can search and access your organization's knowledge bases directly from your documents. This allows you to find relevant information, get answers to questions, and enhance your content without leaving Microsoft Word.

###### Get summaries and insights from your documents

- 
                        Open the Quick add-in from the ribbon or side panel in your Microsoft Word document. 
- 
                        Select the **summarize**shortcut from the ribbon, or ask any question about the document content in the side panel.
- 
                        Quick will analyze your document and provide relevant summaries or insights based on your request. 

###### Generate and improve document content

- 
                        Navigate to the location in your document where you want to add or improve content. 
- 
                        Open the Quick add-in and select the **generate content**or**improve writing**shortcut.
- 
                        Describe what you need, and Quick will generate suggestions that match your document's style and context. 

###### Review and enhance selected text

- 
                        Select the text you want to review or improve in your document. 
- 
                        Open the Quick side panel and use quick prompts such as **explain in simple terms**or**simplify writing**.
- 
                        Quick will provide suggestions for improving clarity, grammar, and style based on your selected content. 

###### Incorporate Quick's company knowledge and general knowledge into your docs

- 
                        Open the Quick side panel while working on your document. 
- 
                        Ask questions about your organization's knowledge bases and spaces to find relevant information for your document. 
- 
                        Use the **insert text**or**replace selection**buttons to insert Quick's response into your document.

**Perform actions in external applications**

- 
                        Open the Quick side panel in your Microsoft Word document. 
- 
                        Ask Quick to perform an action in an external application using [action connectors](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-connectors.html)configured by your organization.

## Amazon Quick Microsoft Word extension usage guidelines

                As a user, you are responsible for keeping company information safe. The following guidance helps you use Amazon Quick apps securely while maintaining data privacy and compliance.

### Conversation retention policy and accuracy

Quick automatically deletes conversations and related files after 30 days of inactivity. Microsoft Word conversation retention follows your company's specific history rules, and Microsoft Word retention periods may exceed Quick's 30-day limit.

Users can review past conversations and attachments. To start fresh, begin
                        a new conversation by selecting **New chat**. However,
                        users need to visit the Amazon Quick chat instance to manage their
                        conversations.

###### Note

Conversation history is not currently available in Microsoft Word. To manage your conversations, use the Quick chat instance.

### Security considerations

When you use Amazon Quick with document content, remember that responses reflect individual user permissions and content may include information not accessible to all document recipients. It may generate responses that contain sensitive data that can't be publicly shared.

To protect your organization's data, carefully evaluate document usage and plan deployment with data privacy in mind. Amazon Quick maintains strict data privacy by not using customer data for service improvements, not using customer data to enhance language models, and not indexing Microsoft Word documents into your company's Quick instance.

No document is read when the side panel is closed, and no data or document content is sent to Quick unless you explicitly send a prompt to the extension.

Quick uses generative AI, so double check responses before
                        using them. Usage of the Quick extension for Microsoft
                            Word is subject to the AWS Responsible AI Policy. [AWS
                            Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/)

### Microsoft Word extension known limitations

The following are known limitations of the Amazon Quick Microsoft Word extension:

- 
                            The Microsoft Word extension can't generate visuals from structured data. 
- 
                            Web search isn't supported in the Microsoft Word extension. 
- 
                            You can't review your conversation history in the Microsoft Word extension at this time. To review and manage your conversation history, visit your Amazon Quick chat instance. 
- 
                            The Microsoft Word extension doesn't support [flows](https://docs.aws.amazon.com/quicksuite/latest/userguide/flows.html).
- 
                            The Microsoft Word extension supports up to 19 uploaded files and your Microsoft Word document. For more information on file upload limits, see [Upload files and chat](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-quick-chat.html#file-uploads).
- 
                            The Microsoft Word extension doesn't support filtering during chat based on **Recently used**agents. Users will have access to the full list of available agents and can pick agents they want to use.
- 
                            The Microsoft Word extension doesn't support the **Actions**menu, so you can't invoke actions explicitly. However, implicit actions are supported. For more information about explicit and implicit actions, see[Using Actions in Chat](https://docs.aws.amazon.com/quicksuite/latest/userguide/int-actions-execution.html).