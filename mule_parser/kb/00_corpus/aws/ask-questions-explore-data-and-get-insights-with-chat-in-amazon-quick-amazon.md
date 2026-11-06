# Ask questions, explore data, and get insights with chat in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/using-quick-chat.html](https://docs.aws.amazon.com/quick/latest/userguide/using-quick-chat.html)

---

You can use Amazon Quick chat to ask questions, interact with your Quick resources, and accomplish tasks using multiple agentic worflows using natural language. When you ask a question, Quick chat analyzes the data it has access to to generate comprehensive responses.

Quick chat provides you with the following capabilities.

###### Topics

## Welcome message

        When you log in, Amazon Quick chat displays a welcome message.

## Suggested prompts

        To help you get started on interacting with your resources in chat, Amazon Quick displays suggested prompts you can use to learn more about Amazon Quick features. Use these to get started on your tasks. Once you select a prompt, Amazon Quick guides you step-by-step through the information it needs from you to complete the task.

###### Note

Suggested prompts are system generated for the system agent; you can't customize them. For custom agents, suggested prompts can be created and customized by the agent builder or owner.

## Expand and collapse modes

        To help enhance your productivity and streamline your chat interactions, Amazon Quick offers two separate chat window display modes:

- 
                **Collapse mode**– The default chat window display. Use for easy access to chat from within all Amazon Quick contexts.
- 
                **Expand mode**– Access chat in an expanded view. Use this mode to work in the chat window without any distractions.

You can open up the chat interface at any time by selecting the chat bubble icon from the top right navigation menu. You can also exit out of the chat at any time by selecting the cancel icon from the top navigation menu.

## Agent picker

        Chat agents in Amazon Quick are conversational assistants that help users explore
            data, analyze information, and take actions. You can pick any agent you've created to
            use during chat, or use the system agent **My Assistant** for your
            conversations.

To learn more about agents, see [Working with agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html).

## Scoping response generation to specific data

        When you use Amazon Quick, you can define what data you want your chat responses generated from using data filters. Data filters enable you to customize your chat's expertise area. The data available to your agent depends on whether it is bound to specific Amazon Quick knowledge and integrations, or if it's unbounded (not connected to specific Amazon Quick resources).

By default, an agent has knowledge of all your Amazon Quick resources and its underlying large language model (LLM). While using chat, you can select between the following knowledge modes:

- 
                **All data and apps**– Amazon Quick will use all available knowledge sources (including spaces, dashboards, datasets, topics, knowledge bases, action integrations, and LLM knowledge) to generate a response to your prompts.
- 
                **General knowledge**– Amazon Quick will only use LLM knowledge to generate responses to your prompts. It won't use any knowlegde from Amazon Quick resources.
- 
                **Specific data and apps**– Chat with a specific or multiple spaces, dashboards, datasets, topics, knowledge bases, or actions. To choose specific resources, select**Choose resource**.

An agent with pre-defined knowledge, on the other hand, only has knowledge of existing Amazon Quick resources already linked to it, and its underlying LLM knowledge. While chatting with an agent with pre-defined knowledge, you get the following knowledge modes:

- 
                **Pre-defined knowledge**– Amazon Quick will use only the Amazon Quick resource knowledge linked to the agent, and LLM knowledge, to generate responses. You can't change this setting.
- 
                **Additional data and apps**– Chat with a specific or multiple spaces, dashboards, datasets, topics, or knowledge bases and actions. To choose specific resources, select**Choose resource**.

## Chatting with datasets

        You can chat with your datasets in Amazon Quick to ask questions and get insights
            from your data using natural language. To get started, you need to first create a
            dataset. For more information, see [Creating
                datasets](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sets.html).

Amazon Quick chat supports the following dataset types:

- 
                SPICE datasets 
- 
                Direct Query datasets against Amazon Redshift, Athena, Aurora PostgreSQL, and Amazon S3 Tables 

###### Note

Direct Query datasets against other data sources are not yet supported for chat.

For SPICE datasets, the size limit of 2 TB and 2 billion rows applies when chatting with the dataset.

## Web search

        Amazon Quick comes with built-in web search capability. Amazon Quick chat automatically searches both your connected data sources and the web, providing comprehensive answers from either or both sources as needed. You can turn web search off for any query by clicking the globe icon in the chat panel. Any content retrieved from the web is appropriately cited in the final response.

###### Note

Web search is available to users only if it has been enabled by admin.

## Upload files and chat

        You can upload documents into Amazon Quick chat and ask Amazon Quick chat to summarize or analyze data based on the content of the uploaded documents.

When you start a new conversation, you can upload new files, choose from a saved list of recent documents, or drag and drop files directly into the conversation.

You can upload up to 20 files at one time with the following size limits:

- 
                10 MB for images ( `.jpeg`,`.png`)
- 
                10 MB for spreadsheet files ( `.csv`,`.xls`,`.xlsx`)
- 
                50 MB for other supported formats 

Supported file types include:

- 
                Word ( `.docx`)
- 
                Excel ( `.xls`,`.xlsx`)
- 
                PowerPoint ( `.ppt`,`.pptx`)
- 
                PDF ( `.pdf`)
- 
                images ( `.jpeg`,`.png`)
- 
                text files ( `.csv`,`.txt`,`.rtf`,`.md`)
- 
                Outlook ( `.msg`)
- 
                structured data files ( `.json`,`.yaml`,`.xml`,`.vtt`, and common code files)

The total parsed content for all files combined has to be under 665,000 characters.

###### Note

If your files exceed the file count and character count limits, you can upload
                them to a [space](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-spaces.html) instead.

Documents uploaded through the chat interface are deleted with the associated conversation after 90 days of inactivity.

###### Note

Audio and video files are not supported as file uploads.

## Actions

        Amazon Quick actions boost productivity by allowing you to perform relevant tasks in supported third-party services from your Amazon Quick chat interface, like sending an email using Microsoft Outlook, or creating a PagerDuty incident. You can invoke any actions configured and available to you from your Amazon Quick chat interface. To select an action, use the action application from the data scoping filter and select the third party application you want to perform actions in. Then, choose the action you want to perform from the available actions. The system checks if you have authorization to perform the action before performing it.

To learn more about actions, see [Actions in Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/action-integrations.html).

## Flows

        Use Amazon Quick flows to create shortcuts for everyday, repetitive tasks you perform while chatting in Amazon Quick. For example, if you find yourself using Amazon Quick chat to create and copy edit product launch descriptions, you can use Amazon Quick flows to generate an application that takes your draft content as input, and generates a polished draft—after content, style, and grammar review—as output.

You can run a flow directly from chat within a conversation. Within a single conversation, you can talk to a chat agent as well as run a flow.

To learn more about flows, see [Flows in Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-amazon-quick-flows.html).

## Memory and response personalization

        Memory in Amazon Quick chat helps personalize your conversations by remembering your preferences, context, and past interactions. Chat agents can reference this stored information to provide more personalized and contextually relevant responses without you needing to repeat information in every conversation, enabling more relevant and tailored responses over time.

When you interact with chat agents in Amazon Quick, you can provide your preferences including:

- 
                Response style and format 
- 
                Frequently accessed Dashboards, Spaces, integrations, and other Amazon Quick assets 
- 
                Context about your role and responsibilities 
- 
                Common tasks and workflows you perform 

This information is securely stored and fetched to enhance your future interactions with chat agents. Memories are specific to you and are not shared with other users. To get the most value from memory in chat, follow the best practices below:

- 
                **Be explicit about your preferences**– Clearly state your preferences, priorities, and context when you want the chat agent to remember them. For example, "I prefer reports in table format" or "I work on the marketing team".
- 
                **Provide relevant context**– Share information about your role, responsibilities, and common tasks to help chat agents understand your needs better.
- 
                **Update your preferences**– As your priorities change, inform the chat agent about updates to ensure the stored information remains current and relevant.
- 
                **Review and refine**– If responses don't align with your expectations, provide feedback and clarify your preferences to improve future interactions.

You maintain control over your memory data. You can review chat memory by going to **Conversation History** and clicking on **View Memories**.

###### Note

Chat memory has the following limitations:

- 
                    Chat memory isn't supported for accounts configured with [AWS KMS customer managed keys](https://docs.aws.amazon.com/quicksuite/latest/userguide/customer-managed-keys.html).

## Source citations

        Amazon Quick chat responses provide in-text source citations in a numbered list. To view the source for a response, choose the number at the end of the sentence. The dialog box shows the title, URL, and a snippet from the source that was used to generate the response. Choose the URL to view the source document.

To view the full list of sources, choose **Sources** at the end of
            the response. You can use the source list to fact-check the response, or for deeper
            analysis. 

## Copy responses

        You can copy and save the responses for later review and analysis. To copy a response, choose the copy icon at the end of the response.

## Provide feedback

        You can provide direct feedback about the responses you received from Amazon Quick chat by using the thumbs-up or thumbs-down button. Your feedback is used to help address technical issues in the web experience.

If you select the thumbs-down button, you can choose from the following feedback options:

- 
                **Inaccurate, not factually correct**
- 
                **Incomplete answer**
- 
                **Didn't understand my question**
- 
                **Issue with sources**
- 
                **Too wordy**
- 
                **Offensive or unsafe language**
- 
                **Other**

You can also copy conversation details from the feedback window for further troubleshooting.

## Artifact panel

        An *artifact* in Amazon Quick is defined as any Amazon Quick
            generated content produced using Amazon Quick's underlying large language model's (LLM)
            generative capabilities, for example: contracts, email drafts, social media posts,
            tables, interactive charts, code blocks, or any Amazon Quick visuals.

Amazon Quick stores any artifacts it generates as responses during chat in an artifact
            panel. You can access any artifacts created during your chat by selecting **View
                more** from below the artifact in chat.

You can download artifacts as text, CSV, code files, Word documents, Excel spreadsheets, PowerPoint presentations, PDFs, and infographics. Saving artifacts to a Space is not currently supported.

For more information about creating and downloading documents and visuals, see
                [Document and visual creation with Amazon Quick](./document-and-visual-creation.html).

## Conversation management

        Amazon Quick stores conversations for up to 90 days, and you can access them in the left navigation pane. You can perform the following tasks to manage your conversations:

- 
                **Start new conversation**– Choose**+**from the chat controls menu to start a new conversation.
- 
                **View conversation history**– Choose the clock icon to view all conversation history for the last 90 days. You can filter conversation history to specific agents.

###### Note

Searching, saving, renaming, and sharing conversations with other users is not supported.

## Response events

        For every natural language prompt Amazon Quick chat receives, it generates real-time
            processing steps while the request is being fulfilled. These steps can be viewed as part
            of **Response events** during response generation, and are also
            accessible once Amazon Quick has finished generating a response. Response events vary
            based on the chat interaction you're having (whether you're chatting with a file you've
            uploaded or with a Amazon Quick resource) and capture any rewrites to your response
            before it's finalized. A response event also includes the system generated identifiers
            for your conversation—you can copy and save the information for
            troubleshooting..

## Explanations

        When you chat with dashboards and datasets, each answer includes an Explanation that shows how the model arrived at each numerical claim, including the data sources, assumptions, filters, calculations, and SQL queries that the model used. Instead of manually verifying each answer by finding the original source and re-creating the logic, you can directly see the model's assumptions at the click of a button.

When you open an Explanation, you can see the following components:

- 
                **Found data in**– Displays the dashboards, sheets, or datasets where the insight came from.
- 
                **Filters**– Lists dashboard filter values that were used to arrive at the answer.
- 
                **Assumptions**– Unpacks any large language model (LLM)-derived definitions from either the data directly or from world knowledge.
- 
                **Calculation explained**– Shows any calculations that the model performed to arrive at the answer, presented in both natural language and as a math formula.
- 
                **Generated SQL**(datasets only) – Displays the specific SQL query that produced each numerical claim.

For more information and examples, see
            [Amazon Quick chat explanations](./chat-explanations.html).

## Contextual awareness

        Amazon Quick chat is context aware. It registers the Amazon Quick resource you're interacting with and scopes your chat automatically to the resource. This way, when you start chatting, the resource you're interacting with is already included as a knowledge source for your chat.

If you navigate to a specific Amazon Quick resource during an on-going chat, and that
            resource supports chat, Amazon Quick chat will automatically register your new context
            and ask you whether you want to chat with the specific resource you have navigated to.
            If you want to continue chatting in the mode you're in, you can choose to
                **Ignore** the message. Or you can choose **Yes**
            to focus your chat on the specific resource you're interacting with. If you do so,
            Amazon Quick automatically scopes your chat interactions to the resource in
            context.

## Managing your preferences in Amazon Quick

        User Preferences in Amazon Quick gives you control over how Quick looks, feels, and works for you. You can customize your chat experience, set a default chat agent, personalize how Quick interacts with you, and manage your memories — all from a single settings modal.

### Customizing your chat experience

You can set your default chat panel to open in either expanded or collapsed mode. By default, Quick automatically remembers your last used setting. For example, if you expand the chat panel during a session, Quick updates your default so the panel opens expanded the next time you return. You can also manually set your preferred default at any time from the Preferences modal.

### Setting your default chat agent

You can choose a preferred chat agent that greets you each time you open Quick. In addition to selecting a default agent, you can pre-select a default knowledge scope for My Assistant. The available knowledge scope options are:

- 
                    **All data and apps**– Quick searches across all your connected data sources and applications.
- 
                    **General knowledge**– Quick responds using general knowledge only, without searching your connected data.
- 
                    **Specific data and apps**– Quick searches only the data sources and applications you specify.

Your selected agent and knowledge scope are applied automatically each time you start a new conversation.

### Personalizing your experience

You can let Quick know what to call you and share your area of focus at work. Quick uses this context to personalize responses and make your experience more relevant to your role and responsibilities.

### Managing your memories

You can view and manage your memories directly from Preferences. Memories are insights that Quick learns from your conversations to personalize future interactions. From the Memories section, you can:

- 
                    View all saved memories. 
- 
                    Search for specific memories. 
- 
                    Delete individual memories. 
- 
                    Delete all memories at once. 

### Accessing User Preferences

To access and configure your preferences:

- 
                    Go to the top-right corner of the Amazon Quick homepage. 
- 
                    Choose your account name. 
- 
                    Select **Preferences**from the dropdown menu.
- 
                    Make your changes across any of the available sections. 
- 
                    Choose **Save**to apply your changes, or choose**Cancel**to discard them.