# What you can build with apps in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/what-you-can-build.html](https://docs.aws.amazon.com/quick/latest/userguide/what-you-can-build.html)

---

You can build complete web applications with apps in Quick, not just static documents or simple forms. Your apps run in the browser, respond to user interaction, and connect to live data.

## User interfaces

        The agent generates responsive layouts using standard web components: navigation menus, tabs, cards, tables, charts, forms, modals, and buttons. You can describe the layout you want in natural language, or let the agent choose a layout based on the purpose you describe. Applications can include multiple views or sections, and the agent can implement navigation between them.

Role-based views are possible. If you tell the agent which users should see which content (for example, by alias or role), it can build conditional visibility into the interface using the user identity API available in the sandbox.

## Data storage

        Every app has access to built-in app storage, a key-value system that requires no external setup. There are two modes: private storage (scoped to the individual user, invisible to others) and shared storage (visible to everyone who accesses the app). Built-in storage scales to support large numbers of records.

You can also store and retrieve data through external systems using action connectors
            or through Amazon Quick spaces. For more information, see
            [Working with data in apps in Quick](./working-with-data-apps.html).

## AI inference

        With apps in Quick, you can apply AI reasoning to features within your app. Common use cases include summarizing submitted text, classifying data into categories, generating recommendations, and answering natural language questions based on connected data.

AI inference supports two modes:

- 
                **Free-form text**— Generate summaries, creative writing, chat responses, and any unstructured text output.
- 
                **Structured output**— Extract structured data, classify inputs, and parse information into JSON. Uses tool-use patterns to guarantee valid, typed responses.

Available models range from fast (for simple tasks), to balanced (general purpose), to most capable (for complex reasoning). For
            more information about AI inference, see
            [Handling write approvals when AI inference is active](./working-with-data-apps.html#apps-write-approvals).

## Embedded visuals

        With apps in Quick, you can embed live, interactive visuals from your Amazon Quick Sight dashboards directly in the app. Charts, tables, KPIs, and graphs update in real time with your data.

Each embedded visual must represent a unique dashboard, sheet, and visual combination. You can embed up to 8 visuals per app, with a minimum size of 100×100 pixels per visual. Embedded visuals are fully interactive and support filters, tooltips, and drill-downs. Viewers see visuals based on their Quick access permissions.

## Embedded chat experiences

        You can add a conversational chat interface to your app by connecting a Amazon Quick space as a knowledge base. The app creates its own agent instance that answers questions based on the documents and data in that space. This is useful for building knowledge portals, FAQ tools, or help desks within an app.

###### Important

You cannot currently embed a standalone chat agent that was created separately in Amazon Quick. The app's embedded agent is a new instance backed by the space you connect.

## File handling

        With apps in Quick, you can generate files for download through the secure bridge API. Supported
            file types include CSV, JSON, plain text, HTML, XML, and Markdown. Apps can also
            read files from Amazon Quick spaces and display their contents. For more information
            about bridge API restrictions, see
            [Sandbox restrictions](./security-sandbox-apps.html#apps-sandbox-restrictions).

###### Important

Direct browser APIs for file creation are blocked by the sandbox. All downloads must go through the secure download utility provided by the platform.