# Create, customize, and deploy AI-powered chat agents in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-agents.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-agents.html)

---

Chat agents in Amazon Quick help users explore data, analyze information, and take actions. Users can interact with chat agents using the Quick chat interface. Chat agents provide assistance through open-ended conversations supported by specific goals, sources of knowledge, and any connected tools. Chat agents can evolve from simple question-answering interfaces to more advanced functions that orchestrate complex workflows.

You can use chat agents to:

- 
            Generate content and provide answers through natural language conversations 
- 
            Analyze and summarize information from connected spaces, dashboards, topics, datasets, and uploaded files 
- 
            Invoke actions to perform predefined steps for consistent, repeatable outcomes 

###### Note

To learn more about chatting using chat agents, see [Using
                Amazon Quick chat](https://docs.aws.amazon.com/quicksuite/latest/userguide/using-quick-chat.html).

###### Topics

## Chat agent types

        Amazon Quick supports two types of chat agents:

- 
                **System chat agent**– This chat agent ("My assistant") is automatically available to all users by default. The system chat agent serves as a base planner with no inherent data or actions of its own—it dynamically accesses resources available to each user during chat time, allowing it to be tailored to individual user permissions and available content. Admin users control system chat agent settings by assigning specific users as owners so they can customize its persona and other settings.The system chat agent is enabled with all chat capabilities, including file upload functionality, LLM knowledge access, toxicity and other guardrails, web search. It also includes chat data scoping mechanisms that provide access to spaces, topics, dashboards, knowledge bases, and actions based on user permissions. 
- 
                **Custom chat agents**– These chat agents can be created and customized to specific use cases by users with chat agent creation capabilities in Amazon Quick, and shared with anyone. Admins can choose to restrict specific users and groups from creating custom chat agents, while still allowing users to use chat agents via chat. Chat agents return responses scoped to content that their invoking users have permissions to.

Custom chat agents can interact with Amazon Quick resources in the following ways:

- 
                **Preconfigured with resources**– These chat agents use only the configured resources (for example, spaces as knowledge sources, action connectors as tools) when looking for answers or orchestrating actions as their defeault behavior. While chatting, users can attach additional resources as per their need or invoke actions directly. For example, chat agents configured with only spaces containing files can't take actions by default unless users explicitly invoke them. Similarly, chat agents configured with only actions rely on LLM knowledge unless users attach a space or dashboard for enterprise-specific answers. However, users may attach additional spaces or directly invoke other actions they may have access to within the chat interface.
- 
                **Not opinionated at build time**– These chat agents are not initially configured with resources when they are built (spaces, or action connectors, or both). Chat determines the resource boundary for the chat agent. For example, if no space is configured for the chat agent, chat will default to all spaces or LLM knowledge until the user makes a change. If no action connectors are configured for the chat agent, during chat, all actions a user has access to will be available to the agent until user makes a resource selection that doesn't include actions.User resource selection during chat affects chat agent behavior. If a user selects a space, the chat agent will only answer with data within that space and take actions available within that space (if it is not opinionated at build time). If a user selects a dashboard, topic, or knowledge base, the chat agent will only answer from that source and not take any actions since the focus is changed to a specific data source. Users are expected to select all relevant resources within chat for comprehensive assistance. ###### NoteThe system chat agent is an unopinionated chat agent by design. If you want chat agents to access all actions irrespective of data focus, configure chat agents with action connectors. 

## Amazon Quick user interaction with chat agents

        The following table shows what you can do with chat agents in the admin console versus
            as a Amazon Quick user. For more information on which roles can access these features,
            refer to the [Amazon Quick
                pricing](https://aws.amazon.com/quicksuite/pricing/) document.

| Access Level | Capabilities | 
|---|---|
| Admin Console | 
 | 
| Amazon Quick user | 
 | 

## Amazon Quick user permissions for chat agents

        What you can do with a chat agent also depends on the permissions you're assigned for it. There are two permission types that users can be assigned:

- 
                **Owner**– Owners can edit, share, and delete the chat agent.
- 
                **Viewer**– Viewers can view and use the chat agent.

###### Note

If you don't have access to a linked resource as either a viewer or owner, resources added to the chat agent by another owner appear as "Resource unavailable". You can delete these resources as an owner, but you cannot list or add them because resource-level sharing is required.

Quick admins must give users the permission to create chat agents. For
            information on which roles can create chat agents, refer to the [Amazon Quick pricing](https://aws.amazon.com/quicksuite/pricing/)
            documentation. For information on how to provide access to these features, see 

[Custom permissions](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html)in the Quick Admin Guide.

The following table outlines how user permissions determine what you can do with a Amazon Quick chat agent:

| Permissions type | Permissions | 
|---|---|
| Owners | 
 | 
| Viewers | 
 | 

## Custom permissions for chat agents

        By default, Amazon Quick enables all new features available for the Amazon Quick
            account, so that users can access them immediately based on their subscription. You can
            use [custom permissions](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html) to restrict specific features. As an
            admin, when you create a custom permissions profile, you can create two types of
            restrictions for chat agents:

- 
                You can completely disable all chat agent functionality for users, including chatting with the default agent, chatting with custom agents, and creating new agents. This can be done by restricting the **Chat agent**capability.
- 
                You can also specifically restrict the ability to create agents without impacting chat with agents. This can be done by creating a custom permission profile and restricting only the feature **Create chat agents**.

###### Note

If you want your users to be able to chat using the system agent but don't want them to create chat agents, restrict their chat agent creation abilities only.

Agent permissions in Amazon Quick can be configured in various combinations to meet your organization's needs. To help you understand how to configure permissions, the following section provides a use-case driven approach that groups common scenarios:

| Use case scenario | What users can do | 
|---|---|
| Agent with all capabilities(No restrictions on chat agents, spaces, knowledge bases, actions, or flows) | 
 | 
| Chat-only access to
                                agents(Agent capabilities enabled, but chat agent creation restricted) | 
 | 
| Limited access to other
                                capabilities(Chat agents enabled, but specific capabilities restricted) | 
 | 
| No chat agent access(Agent capabilities completely restricted) | 
 |