# Using models with Bedrock - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html](https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models-reference.html)

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

A foundation model is an Artificial Intelligence model with a large number of parameters
        and trained on a massive amount of diverse data. A foundation model can generate a variety
        of responses for a wide range of use cases. Foundation models can generate text or image,
        and can also convert input into *embeddings*. This section provides
        information about the foundation models (FM) that you can use in Amazon Bedrock, such as the
        features that models support and the AWS Regions in which models are available. For
        information about the foundation models that Amazon Bedrock supports, see [Supported foundation models in Amazon Bedrock](./models-supported.html). 

Access to all Amazon Bedrock foundation models is enabled by default. To get started, simply select a model from the model catalog in the Amazon Bedrock console and open it in the playground. For Anthropic models, first-time users may need to submit use case details before they can access the model. Once you have selected a model, you can then use it in the following ways.

[Run inference](./inference.html) by sending prompts to a model
                and generating responses. The [playgrounds](./playgrounds.html)
                offer a user-friendly interface in the AWS Management Console for generating text, images, or
                chats. See the **Output modality** column to determine the
                models you can use in each playground.

The console playgrounds don't support running inference on embeddings models. Use the API to run inference on embeddings models.

[Evaluate models](./evaluation.html) to compare outputs and
                determine the best model for your use-case.

[Set up a knowledge base](./knowledge-base.html) with the help of
                an embeddings model. Then use a text model to generate responses to
                queries.

[Create an agent](./agents.html) and use a model to run inference
                on prompts to carry out orchestration.

[Customize a model](./custom-models.html) by feeding training and
                validation data to adjust model parameters for your use-case. To use a
                customized model, you must purchase [Provisioned Throughput](./prov-throughput.html)
                for it.

[Purchase Provisioned Throughput](./prov-throughput.html) for a model to increase
                throughput for it.

To use a foundation model with the Amazon Bedrock API, you need to determine the appropriate **model ID** to use. Refer to the following table to determine where to find the model ID that you need to use.

| Use case | How to find the model ID | 
|---|---|
| Use a base model | Look up the ID in the [base model IDs chart](./models-supported.html) | 
| Use a cross-Region inference profile | Look up the ID in the [supported inference profiles](./inference-profiles-support.html)page | 
| Purchase Provisioned Throughput for a base model | Look up the ID in the model IDs for Provisioned Throughput chart and use it as the `modelId`in the[CreateProvisionedModelThroughput](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateProvisionedModelThroughput.html)request. | 
| Purchase Provisioned Throughput for a custom model | Use the name of the custom model or its ARN as the `modelId`in the[CreateProvisionedModelThroughput](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateProvisionedModelThroughput.html)request. | 
| Use a provisioned model | After you create a Provisioned Throughput, it returns a `provisionedModelArn`. This ARN is the model ID. | 
| Use a custom model | [Purchase Provisioned Throughput](./prov-throughput.html)for the custom model and use the returned`provisionedModelArn`as the model ID. | 

For example code, see the documentation
        for the feature you are using and also [Code examples for Amazon Bedrock using AWS SDKs](./service_code_examples.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Experiment foundation models, compare outputs, generate images/videos, access shared assets playgrounds.

Setup options configure Bedrock serverless model access, playgrounds, project profiles, IAM roles governance.

Access serverless foundation models, group by modality/provider, evaluate performance, build chat agents via on-demand/cross-region inference.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.