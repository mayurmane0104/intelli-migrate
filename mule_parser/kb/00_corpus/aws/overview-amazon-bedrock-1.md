# Overview - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/index.html](https://docs.aws.amazon.com/bedrock/latest/userguide/index.html)

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

Amazon Bedrock is a fully managed service that provides secure, enterprise-grade access to [high-performing foundation models](./models.html) from leading AI companies, enabling you to build and scale generative AI applications.

Read the [Quickstart](./getting-started.html) to write your first API call using Amazon Bedrock in under five minutes.

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
Bedrock supports [100+ foundation models](./models.html) from industry-leading providers, including Amazon, Anthropic, DeepSeek, Moonshot AI, MiniMax, and OpenAI.

| ![Amazon logo with curved arrow from A to Z forming a smile.](/images/bedrock/latest/userguide/images/what-is/nova2pro.png)  
 | ![Orange rounded square icon with white radial loading spinner design.](/images/bedrock/latest/userguide/images/models/claude.png)  
 | ![](/images/bedrock/latest/userguide/images/what-is/deepseek.png)  
 | ![Spherical icon with horizontal stripes or segments across its surface.](/images/bedrock/latest/userguide/images/what-is/kimik2.5.png)  
 | ![Red waveform icon representing audio or voice activity.](/images/bedrock/latest/userguide/images/what-is/minimax2.1.png)  
 | ![](/images/bedrock/latest/userguide/images/models/openai.png)  
 | 

**OpenAI GPT-5.5 and GPT-5.4 now available in Amazon Bedrock**: OpenAI's frontier models for complex professional work, agentic coding, reasoning, and long-running tasks are now available through the Responses API on Amazon Bedrock. See the [GPT-5.5](./model-card-openai-gpt-55.html) and [GPT-5.4](./model-card-openai-gpt-54.html) model cards for details.

** Claude Opus 4.7 now available in Amazon Bedrock**: Anthropic's most capable Opus model to date, delivering improvements across agentic coding, professional work, and long-running tasks.

** Claude Mythos Preview (Gated Research Preview)**: Anthropic's most advanced AI model with state-of-the-art capabilities across cybersecurity, software coding, and complex reasoning tasks. Available in gated preview in US East (N. Virginia).

** Cost allocation by IAM user and role**: Amazon Bedrock now supports cost allocation by IAM principal in AWS Cost and Usage Report 2.0 and Cost Explorer, enabling customers to attribute model inference costs across users, teams, and projects.

| ![Cloud icon with bidirectional arrows indicating sync or data transfer.](/images/bedrock/latest/userguide/images/what-is/apis.jpg)  | Explore the  | 
| ![Wrench and screwdriver icon on purple background.](/images/bedrock/latest/userguide/images/what-is/build.jpg)  | Build using the  | 
| ![](/images/bedrock/latest/userguide/images/what-is/customize.png)  | Customize your models to improve performance and quality.  | 

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Swift SDK examples: Bedrock Runtime actions—Nova Canvas images, Reel videos, Claude, Llama Converse API.

Java 2.x SDK examples retrieve foundation model details via synchronous asynchronous clients.

SDK Swift examples: Converse API messaging, real-time streams, image/video generation Nova, Claude, Llama.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.

Automate tasks configuring AI agents, action groups, knowledge bases, aliases accelerating generative AI development.