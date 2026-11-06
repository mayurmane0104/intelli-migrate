# Automate tasks in your application using AI agents - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

---

[Gemma 4 E2B](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-google-gemma-4-e2b.html)

*12 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Amazon Bedrock Agents offers you the ability to build and configure autonomous agents in your application. An agent helps your end-users complete actions based on organization data and user input. Agents orchestrate interactions between foundation models (FMs), data sources, software applications, and user conversations. In addition, agents automatically call APIs to take actions and invoke knowledge bases to supplement information for these actions. By integrating agents, you can accelerate your development effort to deliver generative artificial intelligence (generative AI) applications.

With agents, you can automate tasks for your customers and answer questions for them. For example, you can create an agent that helps customers process insurance claims or an agent that helps customers make travel reservations. You don't have to provision capacity, manage infrastructure, or write custom code. Amazon Bedrock manages prompt engineering, memory, monitoring, encryption, user permissions, and API invocation.

Agents perform the following tasks:

Extend foundation models to understand user requests and break down the tasks that the agent must perform into smaller steps.

Collect additional information from a user through natural conversation.

Take actions to fulfill a customer's request by making API calls to your company systems.

Augment performance and accuracy by querying data sources.

To use an agent, you perform the following steps:

(Optional) Create a knowledge base to store your private data in that database. For more information, see [Retrieve data and generate AI responses with Amazon Bedrock Knowledge Bases](./knowledge-base.html).

Configure an agent for your use case and add at least one of the following components:

At least one action group that the agent can perform. To
                        learn how to define the action group and how it's handled by the agent, see [Use action groups to define actions for your agent to perform](./agents-action-create.html).

Associate a knowledge base with the agent to augment the agent's performance. For
                        more information, see [Augment response generation for your agent with knowledge base](./agents-kb-add.html).

(Optional) To customize the agent's behavior to your specific use-case, modify
                prompt templates for the pre-processing, orchestration, knowledge base response
                generation, and post-processing steps that the agent performs. For more information,
                see [Enhance agent's accuracy using advanced prompt templates in Amazon Bedrock](./advanced-prompts.html).

Test your agent in the Amazon Bedrock console or through API calls to the
                    `TSTALIASID`. Modify the configurations as necessary. Use traces to
                examine your agent's reasoning process at each step of its orchestration. For more
                information, see [Test and troubleshoot agent behavior](./agents-test.html) and [Track agent's step-by-step reasoning process using trace](./trace-events.html).

When you have sufficiently modified your agent and it's ready to be deployed to
                your application, create an alias to point to a version of your agent. For more
                information, see [Deploy and use an Amazon Bedrock agent in your application](./agents-deploy.html).

Set up your application to make API calls to your agent alias.

Iterate on your agent and create more versions and aliases as necessary.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Strands native Bedrock support accelerates Nova AI agent builds, automating tasks via AgentCore deployment at scale.

SDK Python Boto3 actions manage Bedrock agents, knowledge bases, flows, prompts, Step Functions orchestration.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.