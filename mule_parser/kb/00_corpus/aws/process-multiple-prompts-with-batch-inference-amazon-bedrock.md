# Process multiple prompts with batch inference - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)

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

With batch inference, you can submit multiple prompts and generate responses asynchronously. You can format your input data by using either the `InvokeModel` or `Converse` API format. Batch inference helps you process a large number of requests efficiently by sending a single request and generating the responses in an Amazon S3 bucket. After defining model inputs in files you create, you upload the files to an S3 bucket. You then submit a batch inference request and specify the S3 bucket. After the job is complete, you can retrieve the output files from S3. You can use batch inference to improve the performance of model inference on large datasets.

Batch inference isn't supported for provisioned models.

Batch inference does not support tool calling (function calling) or structured output (`response_format`). Each record in the input JSONL file is processed independently without multi-turn interaction, so features that require back-and-forth exchanges between the model and client are not available.

See the following resources for general information about batch inference:

To see pricing for batch inference, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

To see quotas for batch inference, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html) in the AWS General Reference.

To receive notifications when batch inference jobs complete or change state instead of polling, see [Monitor Amazon Bedrock job state changes using Amazon EventBridge](./monitoring-eventbridge.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

SageMaker batch transforms run inference pipelines combining SparkML XGBoost models using S3 input output data.

Python Boto3 SDK examples manage transcription jobs, custom vocabularies, audio S3 uploads boost accuracy.

Java SDK examples demonstrate ListTranscriptionJobs, StartTranscriptionJob, PCM file, microphone streaming transcription.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.