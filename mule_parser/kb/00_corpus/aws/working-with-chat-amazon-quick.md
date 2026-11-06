# Working with chat - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-chat-desktop.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-chat-desktop.html)

---

Chat is the primary way you interact with Amazon Quick on desktop. You can ask questions, get help with tasks, analyze files, create documents, generate visualizations, and work with your connected services through natural language. The following sections describe the chat features available in the Amazon Quick desktop application.

## AI models

        Amazon Quick on desktop provides multiple AI model modes that you can choose from based on your task. You can switch between modes by using the model selector in the chat input area.

The following table describes the available AI model modes.

| Mode | Description | Best for | 
|---|---|---|
| Fast | Cheapest and fastest model. Responses are generated quickly with the lowest latency. | Quick questions and simple tasks where speed matters more than depth. | 
| Balanced | Balances performance and speed. Provides good quality responses with moderate latency. | Most tasks, including writing assistance, summarization, and general day-to-day work. | 
| Smart | Highest quality responses. Uses the most capable model available with longer response times. | Complex analysis, nuanced writing, detailed reasoning, and tasks that require high accuracy. | 
| Auto | Automatically selects the best model based on the complexity of your request. | When you don't want to choose a model and prefer Quick to decide for each message. | 

### Thinking effort

You can control the thinking effort independently from the model mode. Thinking effort determines how much reasoning the model applies before responding. Higher thinking effort enables deeper reasoning for complex code, strategic planning, and analysis.

The following thinking effort levels are available.

| Level | Description | 
|---|---|
| Off | No extended reasoning. The model responds directly. | 
| Low | Minimal reasoning before responding. | 
| Med | Moderate reasoning. Good balance for most tasks. | 
| High | Extended reasoning for complex problems. | 
| Max | Maximum reasoning depth. Available only on Smart mode. | 

You can set thinking effort on **Balanced** and
                **Smart** modes. The
                **Max** level is available only on Smart mode. To
                change the thinking effort, choose the model selector in the chat input area and
                adjust the thinking effort picker.

## Conversations

        Amazon Quick on desktop persists your conversation history locally on your machine. You can organize, search, and manage your conversations using the following features.

- 
                **Folders**– Organize your conversations into folders for easy access.
- 
                **Pinning**– Pin important conversations to keep them at the top of your chat history.
- 
                **Search**– Search across all your conversations, artifacts, and connected data sources using the search icon next to**Recents**in the sidebar.
- 
                **Thread routing**– Route related discussions to organized threads for structured conversations.

Your conversation history appears in the **Recents**
            section of the sidebar, organized by date.

## Voice input and talkback

        You can use your microphone to interact with Quick instead of typing. Amazon Quick on desktop supports two voice modes.

| Mode | Icon | Description | 
|---|---|---|
| Dictation | Microphone | Converts your speech to text in the chat input field. You can review and edit the text before sending it. | 
| Talkback | Waveform | Converts your speech to text and Quick reads its response aloud. This creates a hands-free conversational experience. | 

To configure voice settings, go to **Settings** >
            **Customization** >
            **Voice**. The following voice settings are
            available.

- 
                **Microphone**– Select which microphone device to use for dictation. Defaults to your system default.
- 
                **Voice selection**– Choose the voice Quick uses for talkback responses. For example,*Matthew · Male · US English*.
- 
                **Speed**– Adjust the playback speed of talkback responses using the speed slider. For example, 1.20×.
- 
                **Live mode**– When enabled, the microphone stays on while the assistant speaks. Say three or more words to interrupt and take your turn. This creates a more natural conversational flow.

###### Tip

You can turn on or turn off voice input from
                **Settings** >
                **Customization** >
                **Voice** using the master toggle. When talkback is
                enabled, a waveform icon appears in the chat input area.

## Plan mode

        For complex multi-step tasks, you can use plan mode. When you activate plan mode, Quick breaks your request into a structured plan with individual steps before executing. You can review and modify the plan before Quick proceeds with each step.

Plan mode is useful for tasks such as the following.

- 
                Multi-file document generation 
- 
                Complex data analysis workflows 
- 
                Multi-step research projects 
- 
                Large-scale code refactoring 

## Deep analysis

        Deep analysis provides structured, multi-track research with parallel investigation. When you start a deep analysis, Quick breaks your question into multiple research tracks and investigates them simultaneously. The results are compiled into a comprehensive report with findings from each track.

Deep analysis is useful for the following tasks.

- 
                Market research and competitive analysis 
- 
                Technical topic deep dives 
- 
                Strategic planning and investigation 
- 
                Multi-angle problem exploration 

To start a deep analysis, ask Quick to perform a deep analysis, research, or comprehensive investigation on a topic. Quick automatically identifies the best research tracks and begins parallel investigation.

## Attachments and file uploads

        You can attach files directly to your chat messages for Quick to analyze, summarize, or reference. The Amazon Quick desktop application supports common file types including documents, spreadsheets, presentations, images, PDFs, code files, and more.

To attach a file, use one of the following methods.

- 
                Choose the **+**(attachment) icon in the chat input area.
- 
                Drag and drop a file directly into the chat window. 

When you attach a file, Quick can read, analyze, and reference the file contents in its responses.

###### Note

For local files, Quick can also access files directly from your
                granted folders without uploading. Reference a file by name or path in your
                message, and Quick reads it from disk. To grant folder access, go to
                **Settings** >
                **My computer** >
                **Local folders**.

## Web search

        You can turn on web search to allow Quick to search the internet for up-to-date information when responding to your messages. When web search is active, Quick can retrieve current information from the web to supplement its responses.

To toggle web search, choose the **web search** icon in
            the chat input area. When web search is active, Quick includes citations
            from the web sources it references in its responses.

## Quick Web Spaces

        You can attach Quick Web Spaces to your conversations to give Quick access to shared team knowledge. Spaces contain curated collections of information that your team maintains in the Quick web application.

When you attach a Space to a conversation, Quick can reference the content in that Space when responding to your messages. This is useful when you need answers grounded in your team's shared context, such as the following.

- 
                Project documentation 
- 
                Company policies and procedures 
- 
                Domain-specific knowledge bases 
- 
                Team wikis and reference materials 

To attach a Space, choose the **Spaces** icon in the
            chat input area and select the Space you want to use.

## Document creation

        Amazon Quick on desktop can generate documents in multiple formats directly from
            your chat conversations. You can ask Quick to create presentations,
            reports, spreadsheets, and other documents by describing what you need. For
            detailed information about supported formats, editing, and best practices, see
            [Document and visual creation with Amazon Quick](./document-and-visual-creation.html).

The following table describes the supported document formats.

| Format | Extension | Capabilities | 
|---|---|---|
| PowerPoint | .pptx | Multi-slide layouts, charts, images, speaker notes | 
| Word | .docx | Formatted text, tables, charts, images, headers and footers | 
| Excel | .xlsx | Formulas, charts, conditional formatting, multiple sheets | 
| Headers, footers, tables, images, page layouts | ||
| Markdown | .md | Reports with embedded SVG visualizations, tables, code blocks | 
| HTML | .html | Interactive dashboards, charts, forms, styled layouts | 

To create a document, describe what you need in chat. For example:

- 
                "Create a PowerPoint presentation about our Q2 results" 
- 
                "Generate an Excel spreadsheet with a sales forecast template" 
- 
                "Write a PDF report summarizing this data" 

### Data visualizations

Quick can generate interactive data visualizations using Highcharts. You can ask Quick to create charts, graphs, and dashboards from your data. The visualizations are rendered as interactive HTML artifacts that you can explore, save, and share.

Supported visualization types include the following.

- 
                    Bar, line, area, and pie charts 
- 
                    Scatter plots and heatmaps 
- 
                    Multi-series and combined charts 
- 
                    Interactive dashboards with filters 

### Image generation

Quick can generate and edit images using Amazon Nova Canvas. You can describe the image you want, and Quick generates it directly in your conversation.

The following image capabilities are available.

| Capability | Description | 
|---|---|
| Generate | Create new images from a text description. | 
| Edit | Modify existing images based on instructions. | 
| Remove background | Remove the background from an image. | 
| Variations | Generate variations of an existing image. | 
| Outpaint | Extend an image beyond its original boundaries. | 

Generated images appear as artifacts that you can save to your local machine.

### Saving artifacts

When Quick generates a document, visualization, or image, it appears
                as an artifact in your conversation. You can save artifacts to your local machine
                or to your **My Stuff** library for later use.

To save an artifact, choose the save icon on the artifact and select a destination. Artifacts saved to My Stuff are accessible from the sidebar and can be reused across conversations.