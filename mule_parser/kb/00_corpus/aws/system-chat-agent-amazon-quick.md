# System chat agent - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/default-assistant.html](https://docs.aws.amazon.com/quick/latest/userguide/default-assistant.html)

---

The Amazon Quick system chat agent is automatically created when you sign up for Quick. It serves as the primary interface for all users to interact with their data and perform various tasks within the Quick environment. It comes equipped with default guardrails.

Ownership of the system chat agent is managed by the Quick admin. Admins
            can disable chatting with chat agents including the system chat agent using [custom permissions](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html). If enabled, users with non-admin
            roles (authors and readers) can view, list, invoke, and use the Quick chat
            chat agent. Its responses are filtered based on user permissions to assets.

The Quick system chat agent is set to use all chat features out of the box with minimal customization required. While these features are also available to custom chat agents, they must be configured during chat agent creation. The system chat agent includes:

- 
                Default persona as the Quick assistant, with professional tone and response style 
- 
                File upload in chat capability enabled 
- 
                Large language model (LLM) knowledge chat enabled 
- 
                Uses default guardrails configured for chat in admin console 
- 
                Access to all spaces, topics, dashboards, knowledge bases, and actions based on user permissions 
- 
                Web search capabilities 

To learn how to customize a system chat agent as an Admin owner, see [Managing
                chat agent customization](https://docs.aws.amazon.com/quicksuite/latest/userguide/manage-agent.html). To learn how to control access to the system chat
            chat agent, see [Manage assets](https://docs.aws.amazon.com/quicksuite/latest/userguide/manage-qs-assets.html).