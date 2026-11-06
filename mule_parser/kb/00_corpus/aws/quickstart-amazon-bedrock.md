# Quickstart - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html)

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

In this section, we will show you how to get started with Amazon Bedrock within a few minutes. We will use the OpenAI-compatible APIs: [Responses API](./bedrock-mantle.html) and [Chat Completions API](./inference-chat-completions.html), the Anthropic-native [Messages API](./model-parameters-anthropic-claude-messages.html), and the [Invoke](./inference-invoke.html) and [Converse API](./conversation-inference.html) to show you how run an inference request. See [Build](./build.html) for list of complete APIs.

**Step 1 - AWS Account:** If you have an AWS account already, skip this step and go to step 2. If you are new to AWS, sign up for an [AWS account](https://portal.aws.amazon.com/billing/signup) and follow instructions.

**Step 2 - API key:** Once you have an AWS account, you can create a short-term API key to authenticate your requests to Amazon Bedrock. To do that, go to the [Amazon Bedrock service in AWS Console](https://console.aws.amazon.com/bedrock/home#/api-keys/short-term/create) and generate a short-term key. For production applications, use 

**Step 3 - Get the SDK:** To use this getting started guide, you must have Python already installed. Then install the relevant software depending on the APIs you are using.

`pip install boto3 anthropic``pip install boto3 openai``pip install boto3``pip install boto3 anthropic`**Step 4 - Set environment variables:** Configure your environment to use the API key for authentication.

```
ANTHROPIC_API_KEY="<provide your Bedrock API key>"
ANTHROPIC_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/anthropic"
```
```
OPENAI_API_KEY="<provide your Bedrock API key>"
OPENAI_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/v1"
```
`AWS_BEARER_TOKEN_BEDROCK="<provide your Bedrock API key>"````
ANTHROPIC_API_KEY="<provide your Bedrock API key>"
ANTHROPIC_BASE_URL="https://bedrock-mantle.<your-region>.api.aws/anthropic"
```
**Step 5 - Run your first inference request:** Amazon Bedrock supports [100+ foundation models](./models.html). Choose a model, and then use the following Python code to run your first inference request. Save the file as `bedrock-first-request.py`

```
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="anthropic.claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
)
print(response)
```
```
from openai import OpenAI
client = OpenAI()
response = client.responses.create(
    model="openai.gpt-oss-120b",
    input="Can you explain the features of Amazon Bedrock?"
    )
print(response)
```
```
from openai import OpenAI
client = OpenAI()
response = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
    )
print(response)
```
```
import boto3
client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='anthropic.claude-opus-4-7',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```
```
import json
import boto3
client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='anthropic.claude-opus-4-7',
    body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
 )
 print(json.loads(response['body'].read()))
```
```
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="anthropic.claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
)
print(response)
```
Execute the code with Python by using the command:

`python3 bedrock-first-request.py`You should see the output of your inference request.

To learn more about using other APIs and endpoints, please refer to [Build](./build.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Amazon Location API keys authenticate anonymous users via console, requiring geo-maps and geo-places actions plus expiration or referrer protection.

Configure Kustomer API key, meet minimum requirements, connect AWS Glue Studio transfer data supported destinations.

Configure Jira basic authentication connecting Amazon Q via API token, username, Jira URL credentials.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.