# Chat agent customization in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/manage-agent.html](https://docs.aws.amazon.com/quick/latest/userguide/manage-agent.html)

---

When a user account subscribes to Quick, the service automatically creates a system default chat agent. This agent powers the default chat experience, allowing Amazon Quick users to leverage all chat functionalities (such as uploading files to chat, using large language model (LLM) parametric knowledge, and answering from their enterprise data) out of the box. The system default chat agent can be updated in the Amazon Quick agent section by a select set of users who are designated as owners for the agent by the admin.

All chat agents (including system and custom) as well as flows are also equipped with guardrails and safety controls to ensure responsible use. Any agent or flow that you chat with will use these default guardrails powering the chat interactions:

- 
            **Prompt leak protection**– Automatically enabled to prevent prompt injection and other LLM-breaking attacks.
- 
            **Prompt safety**– Protects against common security threats like malicious instructions, instructions to ignore guardrails, and others.
- 
            **Blocked words and phrases**– Protects against inappropriate content including insults, hate speech, sexual content, violence, and misconduct, for both chat requests and responses.

As an admin, you can define blocked phrases for all Amazon Quick chat agents. If you do, Amazon Quick ensures that chat agent and flows responses across your Amazon Quick instance don't include these words or phrases. No blocked words or phrases are assigned to your chat agent or flows by default. You can choose up to 50 words or phrases to block.

Admins can also configure whether URLs in chat responses appear as clickable hyperlinks or plain text. This setting applies across all chat agents and flows in your instance, allowing you to control how links are presented to users.

###### Note

Admins can also control permissions for whether users can create and use chat agents
            and flows. For instructions on how to do that, see [Custom permissions](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html).

The following sections outline how to edit the system default agent and add blocked words for chat to influence all agent responses and flows.

###### Topics

## Grant user permissions to edit system default chat agent

        The system default chat agent can be edited by users the admin designates as owners to this agent in the admin console. The following procedure shows you how to grant admin permissions to a user so that they can edit the system default agent.

###### To grant permissions to edit system default agent

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**from the Amazon Quick admin console.
- 
                From the admin console left navigation menu, select **Account**, and then select**Manage assets**.
- 
                In **Manage assets**, select**Chat agents**.
- 
                Select **My Assistant**from the list of chat agents shown. Then, from the**Actions**menu, select**Share**.
- 
                In the **Share assets**modal, use the**User or Group**search bar to find the user or group you want to designate as owners for the system agent.
- 
                Then, from **Permissions**, choose**Owner**. Then, select**Share**.

## Edit system chat agent settings

        To customize your system chat agent, users designated as owners need to login to
            Amazon Quick and visit the agent library page. Admins can directly access this page by
            clicking on the **Go to agent** link in admin console under
                **Chat agent customization**. Once in Amazon Quick, follow these
            steps to edit your system default chat agent's properties. You can preview and test how
            your system agent works as you configure it.

###### To update system chat agent settings

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**from the Amazon Quick admin console.
- 
                From the admin console left navigation menu, select **Customization**, and then select**Chat agent customization**.
- 
                In **Chat agent customization**, in**System chat agent**, select**Go to chat agent**.
- 
                In the **My Assistant**page, in**Configure chat agent**, customize the following sections:- 
                        In **Chat agent persona**, configure your chat agent's personality, identity, tone, and response style. For detailed information about agent customization options, see[Working with chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html)in the*Amazon Quick User Guide*.###### NoteThis agent powers default chat interactions across all users of this account with chat feature access. Ensure that your instructions (e.g. identity and response style) work well for all users of this account. 
- 
                        In **Reference documents**, upload files that remain active in your chat agent's memory to guide all interactions. For detailed information about file upload options, see[Working with chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html)in the*Amazon Quick User Guide*.###### NoteSince this agent is meant for broad use, this is a place to upload enterprise-level response templates and guides. The system default agent isn't linked to specific knowledge sources, actions, or spaces to ensure it works for all users regardless of their access permissions. This setting can't be changed. 
 
- 
                        
- 
                In **Customization**, configure details to help recognize the chat agent. For detailed information about customization options, see[Working with chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html)in the*Amazon Quick User Guide*.

## Configure clickable external links in chat responses

        Admins can configure whether URLs in chat agent responses appear as clickable hyperlinks. The following procedure shows you how to enable clickable hyperlinks for all chat agents in your Amazon Quick instance.

###### To enable clickable external links

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**from the Amazon Quick admin console.
- From the admin console left navigation menu, select - **Customization**, and then select- **Chat agent customization**.
- 
                Under **Clickable external links**, turn the toggle on.

## Adding blocked words and phrases for chat agents

        Default guardrails and admin provided blocked words serve as general settings that all chat agents and flows consider when the user chats with them. Admin configured blocked words are filtered out from responses in both chat agents and flows within your Amazon Quick instance.

To learn more about chat agents, see [Working with chat agents](https://docs.aws.amazon.com/quicksuite/latest/userguide/working-with-agents.html) in the *Amazon Quick User
                Guide*.

###### To assign blocked words and phrases for all chat agents

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**.
- 
                From the left navigation menu, select **Customization**, and then select**Chat agent customization**.
- 
                In **Chat agent customizations**, for**Guardrails and safety controls**, do the following:- 
                        **Add blocked words and phrases**– Select**Add**to add blocked words and phrases. You can add upto 50 words and phrases.
 
- 
                        

## Edit blocked words and phrases for chat agents and flows

        To edit blocked words and phrases added to chat agents and flows, use the following procedure.

###### To edit blocked words and phrases for all chat agents and flows

- 
                Log in to the Amazon Quick console. 
- 
                Select **Manage Quick**.
- 
                From the left navigation menu, select **Customization**, and then select**Chat agent customization**.
- 
                In **Chat agent customization**, for**Guardrails and safety controls**, do the following:- 
                        **Add blocked words and phrases**– Select**Remove**to remove existing blocked words and phrases. Or, select**Add**to add new ones. You can add upto 50 words and phrases.
 
-