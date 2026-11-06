# Making inference requests - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html](https://docs.aws.amazon.com/bedrock/latest/userguide/inference.html)

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

Inference is the process of generating an output from an input provided to a model. Before you can send an inference request to Amazon Bedrock, you need to allow your role to perform the model invocation API actions. This depends on the endpoint you are using.

`bedrock-mantle` endpoint

If your role has the `AmazonBedrockMantleInferenceAccess` AWS managed policy attached, you can skip this section. Otherwise, attach the following permissions to allow inference via the `bedrock-mantle` endpoint (Responses API, Chat Completions, Messages API):

```
{
    "Version": "2012-10-17", 
    "Statement": [
        {
            "Sid": "MantleInferencePermissions",
            "Effect": "Allow",
            "Action": [
                "bedrock-mantle:CreateInference",
                "bedrock-mantle:GetProject",
                "bedrock-mantle:ListProjects",
                "bedrock-mantle:ListTagsForResources"
            ],
            "Resource": "*"
        }
    ]
}
```
`bedrock-runtime` endpoint

If your role has the [AmazonBedrockFullAccess](./security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonBedrockFullAccess) AWS managed policy attached, you can skip this section. Otherwise, attach the following permissions to allow inference via the `bedrock-runtime` endpoint (Converse and Invoke APIs):

```
{
    "Version": "2012-10-17", 
    "Statement": [
        {
            "Sid": "ModelInvocationPermissions",
            "Effect": "Allow",
            "Action": [
                "bedrock:InvokeModel",
                "bedrock:InvokeModelWithResponseStream",
                "bedrock:GetInferenceProfile",
                "bedrock:ListInferenceProfiles",
                "bedrock:RenderPrompt",
                "bedrock:GetCustomModel",
                "bedrock:ListCustomModels",
                "bedrock:GetImportedModel",
                "bedrock:ListImportedModels",
                "bedrock:GetProvisionedModelThroughput",
                "bedrock:ListProvisionedModelThroughputs",
                "bedrock:GetGuardrail",
                "bedrock:ListGuardrails",
                "bedrock:ApplyGuardrail"
            ],
            "Resource": "*"
        }
    ]
}
```
For a detailed breakdown of each permission, see [Prerequisites for running model inference](./inference-prereq.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.