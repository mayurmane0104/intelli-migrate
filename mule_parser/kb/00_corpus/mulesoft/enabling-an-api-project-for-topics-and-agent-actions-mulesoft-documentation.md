# Enabling an API Project for Topics and Agent Actions | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/ai-enabling-api-project-topic-center](https://docs.mulesoft.com/anypoint-code-builder/ai-enabling-api-project-topic-center)

---

![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png) 

# Enabling an API Project for Topics and Agent Actions

Use MuleSoft for Agentforce: Topic Center (also known as Topic Center) to enable API specifications for topics and agents, which can then be synced to API Catalog in Salesforce. You can then augment agent functionality by assigning topics to Agentforce agents in Agent Builder.

Use the Topic Center visual editor to:

- 
Enable the API specifications for topics and agents. 
- 
Apply governance rules to validate that your API is ready to generate agent actions and topics in Salesforce. 
- 
Add metadata to make your topic and action-enabled APIs available in Salesforce using Salesforce API Catalog. 

Topics are bundles of actions and sets of instructions Agentforce agents use to complete tasks. Actions are tasks that the agent can do, and instructions help the agent understand how to use actions.

Topic Center makes your API operations available as agent actions and topics. Agents perform common tasks autonomously, such as updating records, searching and summarizing data, and securely taking action in various systems. Agents are reusable across any set of topics and can contain multiple topics.

| The MuleSoft for Agentforce Extension Pack (beta) must not be installed at the same time as the Anypoint Code Builder Extension Pack* in Visual Studio Code. The extensions conflict with each other and can’t run concurrently. Make sure you only install the extension you plan to use. | 

## Before You Begin

- 
Establish [a tenant relationship](../access-management/trusted-salesforce-org)between your Anypoint Platform organization and a trusted Salesforce organization that has agent entitlements.
- 
Verify that [API Catalog is enabled](../access-management/enabling-api-catalog)for the connected Salesforce organization.
- 
Verify that you have the [required permissions](start-configure-permissions):- 
[Anypoint Exchange permissions](../access-management/permissions-by-product#exchange)so that users can download and publish assets:- 
**Viewer**
- 
**Creator**
 
- 
- 
[Runtime Manager permissions](../access-management/permissions-by-product#runtime-manager)to enable services related to CloudHub and CloudHub 2.0, such as deploying applications:- 
**Read applications**
- 
**Create applications**
- 
**Delete applications**
 
- 
- 
[Design Center Developer](../access-management/permissions-by-product#design-center)permission so that users can view and create APIs.
 
- 
- 
In **Anypoint Platform → API Governance**, make sure you[opt in to govern APIs by version](../api-governance/get-started).
- 
Understand the basics of designing API specs. See the [Tutorials](tutorials)for details.
- 
Have some familiarity with [business groups](../access-management/business-groups).

## Create an API Specification Project for Agent Actions and Topics

- 
In the activity bar of the IDE, click the ![](_images/icon-ms-logo.png) ( (**Anypoint Code Builder**) icon.![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png)  
- 
From **Create**, click**Design an API**:![*Design an API* link highlighted in the *Create* section](_images/design-api-1.png)  
- 
Select **Enable this API for Agent Topics and Actions**.
- 
Complete the **API Specification**form:Field Name Field Value **Project Name**Unique name for your project. This name is used as the API spec title in Exchange, the name of the spec file, and the name of the project’s root directory. For example, if the project name is *Agent Example*, the spec file name is`agent-example`.To reuse an existing project name, you must delete the project that is already using the name first. See [Deleting API Specs and Fragments](des-delete-api-projects).**Project Location**Your home directory or another directory you create. Don’t create the project within another project directory. **API Type**Select **REST API**.**API Specification Language**Select **OAS 3.0 (YAML)**or**OAS 3.0 (JSON)**.Only OAS 3.0 is supported for topics and actions. **Business Group**Select the business group the API will belong to. The business group is required for API governance and syncing centralized rulesets. When you publish your API spec to Exchange from Anypoint Code Builder, the IDE requests the name of the business group. 
- 
Click **Create Project**.If prompted, trust the authors of the files in the folder. The Agent Topics configuration panel opens. 
- 
In the Agent Topics configuration panel, configure agent topic metadata and instructions, and click **Apply**.
- 
Continue designing your API spec. As you enter elements, use [auto-complete](start-discover-ui#auto-complete)(or press Ctrl+Space) to display available options within the context.

## Add Metadata to the API Project

- 
In **Explorer**, right-click the API specification and select**Open API Project Properties**.The **API Project Properties**tab opens and is auto-populated with:- 
**Asset Version**The asset version for your API project must follow the semantic versioning model. For more information, see [Asset Versions](../exchange/asset-versions).
- 
**API Version**The major version for the API. 
- 
**Business Group**Select the Anypoint Platform business group this API will be available in. 
- 
**Asset ID**
- 
**Asset Name**
- 
**Tags**
- 
**Categories**These properties are used when you publish your API specification to Exchange. Tags and categories help users filter search results when they search Anypoint Exchange. The `sf-api-catalog`and`sf-api-topic`tags are applied automatically when you enable the API for agent actions and topics.![API Project Properties tab with sf-api-catalog and sf-api-topic tags applied](_images/ai-topic-center-api-project-properties.png)  You can edit any of the fields. 
 
- 
- 
If you make any changes to the API project properties, click **Apply**.

## Configure Topics

Configure your topic in the **Agent Topics** configuration panel:

- 
Click the **#**icon to open the**Agent Topics**configuration panel if it’s not already open.
- 
Configure these fields for topics: Field Name Description Example **Topic Label**Enter a unique name for the topic. Sales Agent **Classification Description**Enter one to three plain text sentences. An agent uses this description to determine when to use a topic in a conversation. When a user enters a message, the agent identifies the user’s intent, compares it to the topic name and classification description, and uses the best matching topic. These are some examples of classification descriptions: Answers questions about business policies, procedures, or products. Interacts with the user to draft or revise content. Answers questions related to a user’s order status, return status, or making a return. **Scope**The scope defines exactly what the agent can and can’t do for a given topic. The scope is most effective when it narrowly defines the agent’s job for a given topic as it helps limit the agent so it doesn’t try to respond outside the desired job or scope you want the topic to include. These are some examples of scope descriptions: Your job is to only handle tasks related to setting a closing strategy to close deals. This may include answering product-related pricing questions, briefing users on customer sentiment based on conversations, suggesting a close plan to help users close deals, or giving advice based on video and voice calls. Your job is to only educate the user with their reservation questions and only handle changing upcoming or existing reservations by resending the reservation confirmation email. You aren’t able to make new reservations. **Instructions**Plain text instructions help an agent make decisions about how to use the actions in a topic for different use cases. Each instruction is a single topic-specific guideline, usually phrased as “Always…”, “Never…”, “If x, then y…”, or “As a first step,…”. Instructions are nondeterministic, so they shouldn’t include sensitive or deterministic business rules. These are some examples of instructions: Always clarify what type of mobile device (iOS or Android) before using the Answer Questions with Knowledge function to retrieve troubleshooting information. Never ask the user for an ID. Instead, use the name or ask for the name of the record to use IdentifyRecordByName to get the ID to call other actions. If a user asks about the status of their order or order confirmation, ask if they have their order number or their email. If a user doesn’t have their email or order number, ask if they’d like to escalate to an agent or create a case. 

## Configure Actions

Create agent actions using a schema to define the required metadata. As you enter elements, use [auto-complete](start-discover-ui#auto-complete) (or press Ctrl+Space) to display available options within the context.

To enable an API for agent topics and actions, you must annotate at least one operation to use as an agent with `x-sfdc/agent/action/publishAsAgentAction` and set the value to `true`.

| Extension | Description | Default Value | 
|---|---|---|
| x-sfdc/agent/action/publishAsAgentAction | Required. Set this attribute to  | false | 
| x-sfdc/privacy/isPii | Optional. Set this attribute to  | false | 
| x-sfdc/agent/action/isUserInput | Required. Set this attribute to  | false | 
| x-sfdc/agent/action/isDisplayable | Required. Set this attribute to  | false | 

Adding agent metadata in a schema that’s defined using `$ref` isn’t supported. The metadata must be defined inside the schema, for example:

`... (Inside response, request body, etc..) schema: $ref: '#/components/schemas/Pet' ... components: schemas: Pet: x-sfdc: agent: action: isDisplayable: true required: - name - photoUrls properties: id: type: integer format: int64 example: 10 name: type: string example: doggie status: type: string description: pet status in the store enum: - available - pending - sold`openai

## Topic and Agent Governance Rulesets

To make sure your API is ready to generate agent actions and topics in Salesforce, the **SF API Topic and Action Enablement** centralized ruleset is added to your topic-enabled API project automatically.

- 
Optionally, [add additional rulesets](des-govern-api#add-rulesets)that are required for your project.
- 
[Validate the governance rulesets](des-govern-api).If you remove the `sf-api-catalog`and`sf-api-topic`tags from your API project, the topic and action rulesets are automatically removed.

## Publish the API spec to Exchange

After you validate your API specification rulesets, [publish your API specification to Exchange](des-publish-api-spec-to-exchange).

After you publish your API to Exchange and create an active API instance in API Manager, it is available for use in API Catalog. For more information, see [API Catalog](https://help.salesforce.com/s/articleView?id=platform.api_catalog.htm).

## Disable the API Specification for Topics

- 
In **Explorer**, right-click the API specification and select**Open API Project Properties**.
- 
Deselect **Enable this API for Agent Topic and Actions**, and click**Apply**.

The `sf-api-catalog` and `sf-api-topic` tags and the **SF API Topic and Action Enablement** ruleset are removed from the API project.

## See Also

- 
[What are Agents](https://help.salesforce.com/s/articleView?id=sf.copilot_overview.htm&type=5)
- 
[The Building Blocks of Agents](https://help.salesforce.com/s/articleView?id=sf.copilot_building_blocks.htm&type=5)
- 
[Agent Topics](https://help.salesforce.com/s/articleView?id=sf.copilot_topics.htm&type=5)