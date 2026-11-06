# AI response steps - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/ai-response-steps.html](https://docs.aws.amazon.com/quick/latest/userguide/ai-response-steps.html)

---

AI response steps generate content using AI models. Amazon Quick Flows provides the following AI response step types.

## Chat agent

        Amazon Quick Flows allows you to use your chat agents to generate outputs from configured spaces or take action with configured action integrations, all within a workflow step.

Chat agents contain domain-specific knowledge, custom instructions, and connected tools. When you integrate a chat agent into a flow, you can automatically apply this specialized knowledge across multiple workflows without recreating it. For example, if you built a sales assistant chat agent that understands product details and follows brand guidelines, you can embed it in your outreach flow to ensure consistent communication at scale.

For configuration instructions, see [Editing flows](./editing-flows.html).

###### Note

The chat agent step is a single-turn interaction. The agent responds to the task you instruct it to do, but does not support a back-and-forth conversation within the same step.

## Research

        The research step invokes Amazon Quick Research to generate research reports within your flow. This lets you embed research directly into multi-step workflows — for example, creating account plans, conducting policy reviews, researching patent prior art, or generating industry reports.

For full details about Quick Research capabilities and limitations, see [Using Amazon Quick Research](./using-amazon-quick-research.html). For configuration instructions, see [Editing flows](./editing-flows.html).

You can reference the research output in later steps — for example, to send a summary over email to your team.

## Web search

        The web search step lets your flows retrieve current information from the internet. This is useful when you need to access real-time data, verify facts, or gather information from public sources beyond your organization's internal knowledge base.

Write a prompt describing what to search for. The search results can be referenced by later steps in your flow using @ references.

For configuration instructions, see [Editing flows](./editing-flows.html).

###### Note

Search results may vary over time as internet content changes. Some content may not be accessible through web search.

## General knowledge

        The General knowledge step generates text responses using Amazon Bedrock models. Instead of selecting a specific model, you choose a response preference, and Amazon Quick Flows automatically selects the most appropriate model based on your preference and the requirements of your flow.

Choose from:

- **Fast responses**— Optimized for speed across image, video, and text inputs.
- **Versatility and performance**— Balanced capabilities for diverse tasks.

Optionally adjust the creativity slider to control the randomness of the response.

If you do not see response preferences, verify that your administrator has enabled "Enable bedrock model usage in General knowledge step for output refinement" in the Custom Permissions page.

For configuration instructions, see [Editing flows](./editing-flows.html).

## UI agent

        The UI agent step (Preview) lets your flows interact with public websites that do not require a login. The agent can autonomously navigate websites, click, type, read data, and produce structured outputs — all described in natural language.

**Writing effective instructions**

- Be clear and specific about the task you want performed. 
- Use single, complete URLs (for example, "Go to https://example.com/reports"). 
- Add constraints to narrow the scope (for example, "only look at the pricing section"). 
- Specify when the agent should stop (for example, "stop after finding the first matching result"). 
- Define the output format if needed (for example, "return the data as a bulleted list"). 

For configuration instructions, see [Editing flows](./editing-flows.html).

###### Note

UI agent is currently in Preview. Some websites implement anti-automation measures such as CAPTCHA challenges that may limit UI agent capabilities. Websites that require login are not currently supported.

## Create Image

        The Create Image step generates AI images from text prompts. You can configure creativity level, exclude terms, and image seed in the advanced settings.

For configuration instructions, see [Editing flows](./editing-flows.html).