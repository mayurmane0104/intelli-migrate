# Increase model invocation capacity with Provisioned Throughput in Amazon Bedrock - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html)

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

**Throughput** refers to the number and rate of inputs and
        outputs that a model processes and returns. You can purchase **Provisioned Throughput** to provision a higher level of throughput for a model at a fixed cost.
        If you customized a model, you must purchase Provisioned Throughput to be able to use it.

You're billed hourly for a Provisioned Throughput that you purchase. For detailed information about pricing,
        see [Amazon Bedrock Pricing](https://aws.amazon.com/bedrock/pricing). The price per hour
        depends on the following factors:

The model that you choose (for custom models, pricing is the same as the base model that it was customized from).

The number of Model Units (MUs) that you specify for the Provisioned Throughput. An MU delivers a specific throughput level for the specified model. The throughput level of an MU specifies the following:

The number of input tokens that an MU can process across all requests within a span of one minute.

The number of output tokens that an MU can generate across all requests within a span of one minute.

For more information about what an MU specifies, pricing per MU, and to request limit increases, contact your AWS account manager.

The duration of time you commit to keeping the Provisioned Throughput. The longer the commitment duration, the more discounted the hourly price becomes. You can choose between the following levels of commitment:

No commitment – You can delete the Provisioned Throughput at any time.

1 month – You can't delete the Provisioned Throughput until the one month commitment term is over.

6 months – You can't delete the Provisioned Throughput until the six month commitment term is over.

Billing continues until you delete the Provisioned Throughput.

The following steps outline the process of setting up and using Provisioned Throughput.

Determine the number of MUs you wish to purchase for a Provisioned Throughput and the amount of time for which you want to commit to using the Provisioned Throughput.

Purchase Provisioned Throughput for a base or custom model.

After the provisioned model is created, you can use it to [run model inference](./inference.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Reserve ALB LCUs regionally via historic estimates or manual input; charges apply until terminated.

Reserve NLB throughput capacity converting Mbps to LCUs at 1 LCU per 2.2 Mbps across availability zones.

Purchase Provisioned Throughput custom model via CreateProvisionedModelThroughput, use ARN invoke guaranteed capacity.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.