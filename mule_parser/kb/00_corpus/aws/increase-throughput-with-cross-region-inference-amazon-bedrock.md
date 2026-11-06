# Increase throughput with cross-Region inference - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)

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

With cross-Region inference, you can choose either a cross-Region inference profile tied to a specific geography (such as US or EU), or you can choose a global inference profile. When you choose an inference profile tied to a specific geography, Amazon Bedrock automatically selects the optimal commercial AWS Region within that geography to process your inference request. With global inference profiles, Amazon Bedrock automatically selects the optimal commercial AWS Region to process the request, which optimizes available resources and increases model throughput.

Both types of cross-Region inference work through [inference profiles](./inference-profiles.html), which define a foundation model (FM) and the AWS Regions
        to which requests can be routed. When running model inference in on-demand mode, your
        requests might be restricted by service quotas or during peak usage times. Cross-Region
        inference enables you to seamlessly manage unplanned traffic bursts by using compute
        across different AWS Regions.

You can also increase throughput for a model by purchasing [Provisioned Throughput](./prov-throughput.html). Inference profiles currently don't support Provisioned Throughput.

To see the Regions and models with which you can use inference profiles to run
        cross-Region inference, refer to [Supported Regions and models for inference profiles](./inference-profiles-support.html).

Amazon Bedrock provides two types of cross-Region inference profiles, each designed for different use cases and compliance requirements:

| Feature | Geographic Cross-Region Inference | Global Cross-Region Inference | Recommendation | 
|---|---|---|---|
| Data residency | Within geographic boundaries (US, EU, APAC, etc.) | Any supported AWS commercial Region worldwide | Choose Geographic for compliance requirements | 
| Throughput | Higher than single-region | Highest available | Choose Global for maximum performance | 
| Cost | Standard pricing | Approximately 10% savings | Choose Global for cost optimization | 
| SCP requirements | Allow all destination Regions in profile | Allow `"aws:RequestedRegion": "unspecified"` | Configure based on your organizational policies | 
| Best suited for | Organizations with data residency regulations | Organizations prioritizing cost and performance | Assess your compliance and performance needs | 

Choose Geographic cross-Region inference when you have data residency requirements and need to ensure data processing remains within specific geographic boundaries. Choose Global cross-Region inference when you want maximum throughput and cost savings without geographic restrictions.

Note the following information about cross-Region inference:

There's no additional routing cost for using cross-Region inference. The price
                    is calculated based on the Region from which you call an inference profile. For
                    information about pricing, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

Cross-Region inference can route requests to AWS Regions that are not manually enabled in your AWS account. Manual Region enablement is not required for cross-Region inference to function.

All data transmitted during cross-Region operations remains on the AWS network and does not traverse the public internet. Data is encrypted in transit between AWS Regions.

All cross-Region inference requests are logged in CloudTrail in your source Region.
                    Look for the `additionalEventData.inferenceRegion` field to identify
                    where requests were processed.

AWS Services powered by Amazon Bedrock may also use CRIS. See service-specific documentation for more details.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

AgentCore routes inference across regions, balancing compute availability while maintaining geography-bounded data residency compliance.

Cross-region inference routes requests within geographic boundaries; data encrypted transit, logged CloudTrail.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.