# Custom chat agents - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/custom-agents.html](https://docs.aws.amazon.com/quick/latest/userguide/custom-agents.html)

---

Custom chat agents enable Amazon Quick users to create tailored conversational interfaces for specific business needs. Unlike the system chat agent, which is available to all users with chat permissions by default, custom chat agents can be selectively shared and configured by authorized users.

Users with chat agent creation capabilities can customize the chat agent's personality, response style, and capabilities through a natural language interface, or through the agent builder configuration flow. These users can also configure these chat agents with specific knowledge sources (like spaces) and workflows (like actions) while maintaining control over sharing and access permissions for each of those resources separately. Or, chat agents can be left unlinked for general purpose use which allows end users to use the agent with all or some of their resources.

Quick admins must give users the permission to create chat agents. For
            information on which roles can create chat agents, refer to the [Amazon Quick pricing](https://aws.amazon.com/quicksuite/pricing/)
            documentation. For information on how to provide or restrict access to these features,
            see 

[Custom permissions](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html)in the Quick Admin Guide.

###### Topics

## Create and preview custom chat agents

            You can create custom chat agents in Amazon Quick from the **Chat
                    agents** menu on the Amazon Quick home page. You can preview and test
                your chat agent as you build it. When you create a custom chat agent, you are
                assigned as its owner by default. The following procedure outlines how to create a
                custom chat agent.

###### To create a custom chat agent using a natural language prompt

- 
                                Log in to the Amazon Quick console. 
- 
                                From the left navigation menu, select **Chat agents**, and then select**Create chat agent**.
- 
                                In **New chat agent**, do the following:- 
                                        In the text input box, enter a natural language description for what kind of chat agent you want to create. This is the prompt Amazon Quick will use you create your chat agent. You can use the suggested sample instructions on the page to create your chat agent as well. 
- 
                                        Then, select **Generate**. Selecting**Generate**takes the instruction or goal provided and expands it into chat agent instructions and configurations. It also scans the user's available resources (spaces and action connectors) and finds the most relevant matches based on the chat agent intent provided. The expanded builder UI is opened with these configurations for the user to review, customize, test, and launch.
 
- 
                                        
- 
                                On the **Configure chat agent**page, make sure your chat agent has the right settings and customize your chat agent further. Click on**Update preview**to ensure all changes are saved before you try out the chat agent in preview.
- 
                                When you're ready, select **Launch chat agent**to publish your custom chat agent to the chat agent library and use it in chat.###### Note- 
                                            Until you select **Launch chat agent**, your chat agent is not available in the chat agent library. If you exit the creation process without launching, the preview version will be deleted and the chat agent won't be saved.
- 
                                            When you launch a chat agent, it remains private by default. The chat agent only becomes available in other users' libraries after you share it. Once shared, subsequent edits and launches will publish changes to the same chat agent for all users who have access. 
 
- 
                                            

## Share custom chat agents

            When you create a chat agent, you are assigned as its owner by default. You can choose to share a chat agent you own with other Amazon Quick users using the following permissions:

- 
                    *Owner*permissions – User can edit, share, use, and delete the chat agent.
- 
                    *Viewer*permissions – User can view and use the chat agent.

You can also define access permissions for a chat agent globally, granting all users access to a chat agent and then defining more granular access permissions for specific users and groups.

The following procedure shows you how to share and assign permissions to chat agents.

###### To share custom chat agents

- 
                    Log in to the Amazon Quick console. 
- 
                    From the left navigation menu, select **Chat agents**
- 
                    Then, from the **Actions**column for the chat agent you want to share, select the menu icon, and then select**Share**.
- 
                    In the **Share chat agent**modal that opens, enter the user or group name you want to share the chat agent with. When the user or group name appears, select it. Repeat the action for all groups or users you want to share the chat agent with. The modal displays the users and groups you're adding.
- 
                    Assign permissions and access information for each user or group you're sharing your chat agent with using the dropdown next to the user or group name. You can assign one of two roles: - 
                            **Owner**– User can edit, share, and delete the chat agent.
- 
                            **Viewer**– User can view and use the chat agent.
 
- 
                            
- 
                    Select **Share**.

## Embed custom chat agents

            You can embed a custom chat agent in an external website or application so that users can interact with it outside of the Amazon Quick console. To embed a chat agent, you must first allow the hosting domain in the Amazon Quick admin settings, and then generate the embed code from the chat agent's share options.

Embedding a chat agent involves two steps:

- 
                    **Allow the hosting domain**– A Amazon Quick admin must add the domain (and optionally its subdomains) where the embedded chat agent will be hosted to the domain allow list.
- 
                    **Generate the embed code**– The chat agent owner or an authorized user generates the embed code from the chat agent's share options.

### Allow a domain for embedded chat agents

Before you can embed a chat agent on an external website, a Amazon Quick admin must add the hosting domain to the allow list. You must be a Amazon Quick admin to complete this procedure. This ensures that only approved domains can host embedded chat agents.

###### To allow a domain for embedding

- 
                        Log in to the Amazon Quick console. 
- 
                        Choose the profile icon. 
- 
                        Choose **Manage account**.
- 
                        In the navigation pane under **Security**, choose**Manage domains**.
- 
                        In the **Domain**field, enter the domain name where you want to host the embedded chat agent (for example,`https://example.com`).
- 
                        (Optional) Select **Include subdomains**to allow embedded chat agents on all subdomains of the specified domain.
- 
                        Choose **Add**.

The domain now appears in the list of allowed domains. You can edit or delete existing domains by choosing the edit or delete icons next to each domain in the list.

### Generate the embed code for a chat agent

After you allow the hosting domain, you can generate the embed code for a chat agent.

###### To generate the embed code for a chat agent

- 
                        Log in to the Amazon Quick console. 
- 
                        From the navigation pane, choose **Chat agents**.
- 
                        From the **Actions**column for the chat agent you want to embed, choose the menu icon, and then choose**Edit**.
- 
                        In the chat agent editor, choose **Share**.
- 
                        In the share options, choose **Share via embed**.
- 
                        Copy the provided embed code and paste it into the HTML of your website or application where you want the chat agent to appear. 

The embedded chat agent is now available on your website. Users who visit the page can interact with the chat agent directly.

## Update custom chat agents

            You can update custom chat agents in Amazon Quick from the
                    **Agents** menu on the Amazon Quick home page. The following
                procedure outlines how to do so.

###### Note

You can preview how your chat agent customizations updates perform, as you are
                    configuring the chat agent, in the preview chat interface. Make sure to select
                        **Update preview** before testing a change. Once all
                    changes are tested in preview, select **Launch** to publish the
                    changes to the chat agent currently in use.

###### To update a custom chat agent

- 
                    Log in to the Amazon Quick console. 
- 
                    From the left navigation menu, select **Chat agents**
- 
                    Then, from the **Actions**column for the chat agent you want to share, select the menu icon, and then select**Edit**. This creates a preview version of your chat agent to update and test before publishing.
- 
                    In the **Edit agent**, update your chat agent settings, and then select**Launch**.

## Manage access to a custom chat agent

            If you're the owner of a chat agent, you can choose to change the user access permissions for a chat agent. You can also remove user and group access to a chat chat agent. The following procedure shows how.

###### To manage access to custom chat agents

- 
                    Log in to the Amazon Quick console. 
- 
                    From the left navigation menu, select **Chat agents**
- 
                    Then, from the **Actions**column for the chat agent you want to share, select the menu icon, and then select**Share**.
- 
                    In the **Share chat agent**modal that opens, select the user and group you want to change permissions for. When the user or group name appears, select it and change the permissions. Repeat the action for all groups or users you want to change permissions for. The modal displays the users and group permissions you're changing. You can take the following three actions:- 
                            Change to **Owner**– User can edit, share, and delete the chat agent.
- 
                            Change to **Viewer**– User can view and use the chat agent.
- 
                            **Remove access**– Remove user or group access to a chat agent.
 ###### NoteYou can also define access permissions to a chat agent globally, granting all users access to a chat agent and then defining more granular access permissions for specific users and groups. To do so, choose **Settings**and then use**Global settings**to turn this feature on or off.
- 
                            
- 
                    Select **Share**.

## View chat agents

            You can view a list of the chat agents you have created or have access to. The following procedure shows how.

###### To view custom chat agents

- 
                    Log in to the Amazon Quick console. 
- 
                    From the left navigation menu, select **Chat agents**
- 
                    The chat agents you have created or have access to will be displayed on the **Chat agents**home page.

## View chat agent details

            You can view the details of chat agents that are either created by you or shared with you, including all spaces and actions attached to each chat agent.

###### To view chat agent details

- 
                    Log in to the Amazon Quick console. 
- 
                    From the left navigation menu, select **Chat agents**
- 
                    Then, from the list of chat agents, from the **Name**column, click on the name of the chat agent you want to view details for. A detail modal will open.###### NoteYou can also view chat agent details by navigating to the **Actions**column for the chat agent you want to share, selecting the menu icon, and then selecting**View chat agent details**.
- 
                    In the chat agent details modal that opens, you will see the following details: - 
                            **Description**– The description for the chat agent.
- 
                            **Instruction summary**– A summary of the instructions defined for the chat agent.
- 
                            **Created by**– Details on whether the chat agent was created by you or someone else.
- 
                            **Last modified**– The time the chat agent was last modified.
- 
                            Under **Capabilities**:- 
                                    **Knowledge**– The knowledge sources the chat agent is either attached to or has access to. If your chat agent is linked to a space, you'll be able to see which space it is linked to.
- 
                                    **Actions**– The actions that the chat agent is attached or has access to. You can also view this by clicking on**info**next to the agent name in the chat UI agent selector.
 
- 
                                    
 
- 
                            

## Duplicate custom chat agents

            You can duplicate existing custom chat agents without building a chat agent from
                scratch. Users can duplicate chat chat agents from the list page using the
                    **Duplicate** action button. When you duplicate a chat agent,
                Amazon Quick creates a new chat agent with name format "[Original name] (copy)",
                which you can edit. All fields and configurations from the original chat agent are
                copied to the new version of the chat agent. Once duplicated, you can assign custom
                user access permissions to the duplicated chat agent and share it.

The following procedure outlines how to duplicate chat agents.

###### To duplicate custom chat agents

- 
                    Log in to the Amazon Quick console. 
- 
                    From the left navigation menu, select **Chat agents**
- 
                    Then, from the **Actions**column for the chat agent you want to share, select the menu icon, and then select**Duplicate**.You will be redirected to a chat agent duplication modal with prepopulated fields. 
- 
                    Make any changes you need to, including adding the right user and group permissions, and linking it to the assets you want and then select **Launch**to launch your duplicated chat agent.

## Delete chat agents

            You can delete a Amazon Quick chat agent you own. The following procedure shows you how.

###### To delete a custom chat agent

- 
                    Log in to the Amazon Quick console. 
- 
                    From the left navigation menu, select **Chat agents**
- 
                    Then, from the **Actions**column for the chat agent you want to share, select the menu icon, and then select**Delete**.