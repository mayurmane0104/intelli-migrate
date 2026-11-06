# Evaluate the performance of Amazon Bedrock resources - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)

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

Use Amazon Bedrock evaluations to evaluate the performance and effectiveness of Amazon Bedrock models and knowledge bases, as well as models and Retrieval Augmented Generation (RAG) sources outside of Amazon Bedrock. Amazon Bedrock can compute performance metrics such as the semantic robustness of a model and the correctness of a knowledge base in retrieving information and generating responses. For model evaluations, you can also use a team of human workers to rate and provide their input for the evaluation.

Automatic evaluations, including evaluations that use Large Language Models (LLMs), produce computed scores and metrics that help you assess the effectiveness of a model and knowledge base. Human-based evaluations use a team of people who provide their ratings and preferences in relation to certain metrics.

Programmatic model evaluation jobs allow you to quickly evaluate a model's ability to perform a task. You can either provide your own custom prompt dataset that you've tailored to a specific use case, or you can use an available built-in dataset.

Model evaluation jobs that use human workers allow you to bring human input to the model evaluation process. They can be employees of your company or a group of subject-matter experts from your industry.

Model evaluation jobs that use a judge model allow you to quickly evaluate a model's responses via using a second LLM. The second LLM scores the response and provides an explanation for each response.

LLM-based evaluations compute performance metrics for the knowledge base. The metrics reveal if a RAG source or Amazon Bedrock Knowledge Base is able to retrieve highly relevant information and generate useful, appropriate responses. You provide a dataset that contains the prompts or user queries for evaluating how a knowledge base retrieves information and generates responses for those given queries. The dataset must also include ‘ground truth’ or the expected retrieved texts and responses for the queries so that the evaluation can check if your knowledge base is aligned with what’s expected.

Use the following topic to learn more about creating your first model evaluation job.

Model evaluation jobs support using the following types of Amazon Bedrock models:

Foundation models

Amazon Bedrock Marketplace models

Customized foundation models

Imported foundation models

Prompt routers

Models that you have purchased Provisioned Throughput

[Creating an automatic model evaluation job in Amazon Bedrock](./evaluation-automatic.html)

[Creating a model evaluation job that use human workers in Amazon Bedrock](./evaluation-human.html)

[Evaluate the performance of RAG sources using Amazon Bedrock evaluations](./evaluation-kb.html)

[Required Cross Origin Resource Sharing (CORS) permissions on S3 buckets](./model-evaluation-security-cors.html)

[Review model evaluation job reports and metrics in Amazon Bedrock](./model-evaluation-report.html)

[Data management and encryption in Amazon Bedrock evaluation job](./evaluation-data-management.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Evaluate Amazon Bedrock foundation models via automatic jobs measuring semantic robustness, text generation, scores, metrics.

Configure, submit, evaluate models via SageMaker Unified Studio using metrics toxicity, accuracy, robustness.

SageMaker evaluation supports MMLU BBH benchmarks, LLM-as-Judge via Bedrock, custom scorers, PRIME MATH PRIME CODE built-in scoring.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.