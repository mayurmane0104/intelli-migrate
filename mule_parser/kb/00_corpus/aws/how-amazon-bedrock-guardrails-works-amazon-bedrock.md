# How Amazon Bedrock Guardrails works - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-how.html)

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

Amazon Bedrock Guardrails helps keep your generative AI applications safe by evaluating both user inputs and model responses.

You can configure guardrails for your applications based on the following considerations:

An account can have multiple guardrails, each with a different configuration and customized to a specific use case.

A guardrail is a combination of multiple policies configured for prompts and response including; content filters, denied topics, sensitive information filters, word filters, and image content filters.

A guardrail can be configured with a single policy, or a combination of multiple policies.

A guardrail can be used with any text or image foundation model (FM) by referencing the guardrail during the model inference.

You can use guardrails with Amazon Bedrock Agents and Amazon Bedrock Knowledge Bases.

When using a guardrail in the `InvokeModel`,
                `InvokeModelWithResponseStream`, `Converse`, or
                `ConverseStream` operations, it works as follows during the inference
            call. (How this works depends on how you configure your policies to handle inputs and
            outputs.)

The input is evaluated against the configured policies specified in the guardrail. Furthermore, for improved latency, the input is evaluated in parallel for each configured policy.

If the input evaluation results in a guardrail intervention, a configured
                        *blocked message* response is returned and the foundation
                    model inference is discarded.

If the input evaluation succeeds, the model response is then subsequently evaluated against the configured policies in the guardrail.

If the response results in a guardrail intervention or violation, it will be
                    overridden with *pre-configured blocked messaging* or
                        *masking* of the sensitive information based on your
                    policy configuration.

If the response's evaluation succeeds, the response is returned to the application without any modifications.

For information on Amazon Bedrock Guardrails pricing, see the [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

Charges for Amazon Bedrock Guardrails are incurred only for the policies configured in the guardrail.
                The price for each policy type is available at [ Amazon Bedrock
                Pricing](https://aws.amazon.com/bedrock/pricing/).

If a guardrail blocks the input prompt, you're charged for the guardrail evaluation. There are no charges for foundation model inference calls.

If a guardrail blocks the model response, you're charged for guardrail's evaluation of the input prompt and the model response. In this case, you're charged for the foundation model inference calls, in addition to the model response that was generated before the guardrail's evaluation.

If a guardrail doesn't block the input prompt and the model response, you're charged for guardrail's evaluation of the prompt and the model response, in addition to the foundation model inference.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Bedrock policy syntax defines guardrail enforcement, content tagging, model scope, ARN versioning, member permissions.

Bedrock Guardrails streaming supports synchronous buffered scanning or asynchronous low-latency filtering via streamProcessingMode, balancing moderation accuracy latency.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.