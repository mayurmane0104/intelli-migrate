# Customize your model to improve its performance for your use case - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)

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

Model customization is the process of providing training data to a model to improve its performance for specific use-cases. You can customize Amazon Bedrock foundation models to improve their performance and create a better customer experience. Amazon Bedrock currently provides the following customization methods.

**Supervised fine-tuning**

Provide *labeled* data to train a model to improve performance on specific tasks. By providing a training dataset of labeled examples, the model learns to associate what types of outputs should be generated for certain types of inputs. The model parameters are adjusted in the process and the model's performance is improved for the tasks represented by the training dataset.

For more information about using supervised fine-tuning, see [Customize a model with fine-tuning in Amazon Bedrock](./custom-model-fine-tuning.html).

**Reinforcement fine-tuning**

Reinforcement fine-tuning improves foundation model alignment with your specific use case through feedback-based learning. Instead of providing labeled input-output pairs, you define reward functions that evaluate response quality. The model learns iteratively by receiving feedback scores from these reward functions.

You can upload your training prompt datasets or provide existing Bedrock invocation logs. You can define reward functions using AWS Lambda to evaluate response quality. Amazon Bedrock automates the training workflow and provides real-time metrics to monitor model learning progress.

For more information about using reinforcement fine-tuning, 
                see [Customize a model with reinforcement fine-tuning in Amazon Bedrock](./reinforcement-fine-tuning.html).

**Distillation**

Use distillation to transfer knowledge from a larger more intelligent model (known as teacher) to a smaller, faster, and cost-efficient model (known as student). Amazon Bedrock automates the distillation process by using the latest data synthesis techniques to generate diverse, high-quality responses from the teacher model, and fine-tunes the student model.

To use distillation, you select a teacher model whose accuracy you want to achieve for your use case, and a student model to fine-tune. Then, you provide use case-specific prompts as input data. Amazon Bedrock generates responses from the teacher model for the given prompts, and then uses the responses to fine-tune the student model. You can optionally provide labeled input data as prompt-response pairs.

For more information about using distillation see [Customize a model with distillation in Amazon Bedrock](./model-distillation.html).

For information about model customization quotas, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html) in the AWS General Reference.

You are charged for model training based on the number of
            tokens processed by the model (number of tokens in training data corpus × number of
            epochs) and model storage charged per month per model. For more information, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

AWS SDK PHP examples invoke LLMs Amazon Bedrock: Nova, Titan images, Claude, Stable Diffusion XL.

SDK Go V2 invokes Bedrock foundation models, including Titan Image Generator, Nova, Claude Converse API, real-time streams.

Redshift ML integrates SageMaker AI Autopilot & Bedrock LLMs, enabling churn prediction, sentiment analysis via SQL.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.