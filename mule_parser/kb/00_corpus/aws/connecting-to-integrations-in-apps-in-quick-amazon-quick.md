# Connecting to integrations in apps in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/connecting-integrations-apps.html](https://docs.aws.amazon.com/quick/latest/userguide/connecting-integrations-apps.html)

---

You can connect your apps in Quick apps to external services and data sources through the
        integration framework in Amazon Quick. The same integration model used elsewhere in
        Quick applies in apps in Quick. The agent registers integrations
        on your app, and you and your users authorize them. For more information about integrations,
        see [Work with integrations in Amazon Quick](./working-with-integrations.html).

## Prerequisites

        Before you connect integrations, confirm the following:

- 
                You have an active Amazon Quick account with Author Pro or higher access. 
- 
                Your administrator has enabled the connectors you plan to use. 

## Integration types

        Quick organizes integrations into two categories:

- 
                **Knowledge integrations**— Connect to data sources that the system can search and reason over. In apps in Quick, this is most commonly a Amazon Quick space used as a knowledge base for an embedded chat experience.
- 
                **Action integrations**— Connect to external applications and services where your app can read data, write data, or perform operations. Examples include Microsoft Outlook, SharePoint, OneDrive, Slack, Jira, and Asana. Quick provides over 100 pre-built action connectors. You can also create custom connectors using REST API, OpenAPI, or MCP specifications.

## Authentication models

        Action integrations support two authentication models:

- 
                **User authentication**— The integration uses the credentials of the individual end user. Every user must have their own access to the connected resource.
- 
                **Service authentication**— The integration uses a service-level credential configured by an administrator. All users of the app share that access. Not all connectors support service authentication.

## Adding an integration to your app

        You do not need to set up integrations manually. To add an integration:

- 
                Ask the agent to use a specific service in your instructions. For example: "Connect to my Outlook calendar and display my meetings for this week." 
- 
                Authorize the integration when the agent prompts you. 
- 
                Verify that the integration appears in the Assets view. 

When other users open the published app, they authorize their own credentials for each registered integration on first use.

## How apps in Quick works with other Quick capabilities

        Apps in Quick connects to several other capabilities within Amazon Quick:

- 
                **Amazon Quick spaces**— An app can read files from a space, write new files to it, and use a space as the knowledge base for an embedded chat experience. For more information, see[Organize, collaborate, and share resources with spaces in Amazon Quick](./working-with-spaces.html).
- 
                **Amazon Quick Flows**— There is no direct integration between apps in Quick and Quick Flows. Use a space as a shared data layer instead. A flow processes data and saves its output to a space. The app reads from that space and displays the results. For more information, see[Using Amazon Quick automations](./using-amazon-quick-automations.html).

## Integration tips

        - 
                **Outlook and OneDrive**— These connectors do not reliably resolve the`me`alias in API calls. Instruct the agent to use the user identity API to retrieve the current user's information instead.
- 
                **Slack**— The Slack connector's API schema does not include all available Slack API operations. Provide specific details about the Slack API operations you need, such as the channel ID and message format.
- 
                **Integration removal**— You cannot currently remove a registered integration from an app through the settings UI. As a workaround, ask the agent to remove references to the integration in the app code.