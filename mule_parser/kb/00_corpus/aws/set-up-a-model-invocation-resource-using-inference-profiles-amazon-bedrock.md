# Set up a model invocation resource using inference profiles - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles.html)

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

*Inference profiles* are a resource in Amazon Bedrock that define a model and one or more Regions to which the inference profile can route model invocation requests. You can use inference profiles for the following tasks:

**Track usage metrics** – Set up CloudWatch logs and submit model invocation requests with an application inference profile to collect usage metrics for model invocation. You can examine these metrics when you view information about the inference profile and use them to inform your decisions. For more information about how to set up CloudWatch logs, see [Monitor model invocation using CloudWatch Logs and Amazon S3](./model-invocation-logging.html).

**Use tags to monitor costs** – Attach tags to an application inference profile to track costs when you submit on-demand model invocation requests. For more information on how to use tags for cost allocation, see [Organizing and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the AWS Billing user guide.

**Cross-Region inference** – Increase your throughput by using an inference profile that includes multiple AWS Regions. The inference profile will distribute model invocation requests across these Regions to increase throughput and performance. For more information about cross-Region inference, see [Increase throughput with cross-Region inference](./cross-region-inference.html).

Amazon Bedrock offers the following types of inference profiles:

**Cross Region (system-defined) inference profiles** – Inference profiles that are predefined in Amazon Bedrock and include multiple Regions to which requests for a model can be routed.

**Application inference profiles** – Inference profiles that a user creates to track costs and model usage. You can create an inference profile that routes model invocation requests to one Region or to multiple Regions:

To create an inference profile that tracks costs and usage for a model in one Region, specify the foundation model in the Region to which you want the inference profile to route requests.

To create an inference profile that tracks costs and usage for a model across multiple Regions, specify the cross Region (system-defined) inference profile that defines the model and Regions to which you want the inference profile to route requests.

You can use inference profiles with the following features to route requests to multiple Regions and to track usage and cost for invocation requests made with these features:

Model inference – Use an inference profile when running model invocation by choosing an inference profile in a playground in the Amazon Bedrock console, or by specifying the ARN of the inference profile when calling the [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html), [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html), [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html), and [ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html) operations. For more information, see [Making inference requests](./inference.html).

Knowledge base vector embedding and response generation – Use an inference profile when generating a response after querying a knowledge base or when parsing non-textual information in a data source. For more information, see [Test your knowledge base with queries and responses](./knowledge-base-test.html) and [Parsing options for your data source](./kb-advanced-parsing.html).

Model evaluation – You can submit an inference profile as a model to evaluate when submitting a model evaluation job. For more information, see [Evaluate the performance of Amazon Bedrock resources](./evaluation.html).

Prompt management – You can use an inference profile when generating a response for a prompt you created in Prompt management. For more information, see [Construct and store reusable prompts with Prompt management in Amazon Bedrock](./prompt-management.html)

Flows – You can use an inference profile when generating a response for a prompt you define inline in a prompt node in a flow. For more information, see [Build an end-to-end generative AI workflow with Amazon Bedrock Flows](./flows.html).

The price for using an inference profile is calculated based on the price of the model in the Region from which you call the inference profile. For information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

For more details about the throughput that a cross-Region inference profile can offer, see [Increase throughput with cross-Region inference](./cross-region-inference.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Invoke models via inference profiles, routing requests across Regions tracking costs using ARNs in modelId fields.

Configure API Gateway request validation via SAM RequestModel, validating body, path parameters, query strings, headers.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.