# Construct and store reusable prompts with Prompt management in Amazon Bedrock - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html)

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

Amazon Bedrock provides you the ability to create, edit, and save your own prompts using Prompt management so that you can save time by applying the same prompt to different workflows. When you create a prompt, you can select a model to run inference on it and modify the inference parameters to use. You can include variables in the prompt so that you can adjust the prompt for different use cases.

When you test your prompt, you have the option of comparing different variants of the prompt and choosing the variant that yields outputs that are best-suited for your use case. While iterating on your prompt, you can save versions of it. You integrate a prompt into your application with the help of [Amazon Bedrock Flows](./flows.html).

The following is the general workflow for using Prompt management:

Create a prompt in Prompt management that you want to reuse across different use cases. Include variables to provide flexibility in the model prompt.

Choose a model, inference profile, or agent to run inference on the prompt and modify the inference configurations as necessary.

Fill in test values for the variables and run the prompt. You can create variants of your prompt and compare the outputs of different variants to choose the best one for your use case.

Integrate the prompt into your application in one of the following ways:

Specify the prompt when [running model inference](./inference.html).

Add a prompt node to a [flow](./flows.html) and specify the prompt.

The following list introduces you to the basic concepts of Prompt management:

**Prompt** – An input provided to a model to guide it to generate an appropriate response or output.

**Variable** – A placeholder that you can include in the prompt. You can include values for each variable when testing the prompt or when you invoke the model at runtime.

**Prompt variant** – An alternative configuration of the prompt, including its message or the model or inference configurations used. You can create different variants of a prompt, test them, and save the variant that you want to keep.

**Prompt builder** – A tool in the Amazon Bedrock console that lets you create, edit, and test prompts and their variants in a visual interface.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Save reusable Amazon Q Developer chat prompts library, insert across projects via IDE integration.

Deleting Amazon Bedrock prompts checks app dependencies, removes draft versions, requiring SSO/IAM access via Asset gallery.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.