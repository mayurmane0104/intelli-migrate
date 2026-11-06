# Using Amazon Augmented AI for Human Review - Amazon SageMaker AI

**Source:** [https://docs.aws.amazon.com/sagemaker/latest/dg/use-augmented-ai-a2i-human-review-loops.html?icmpid=docs_a2i_lp](https://docs.aws.amazon.com/sagemaker/latest/dg/use-augmented-ai-a2i-human-review-loops.html?icmpid=docs_a2i_lp)

---

[Disaggregated Prefill and Decode for HyperPod inference](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-dpd.html)

*13 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

When you use AI applications such as Amazon Rekognition, Amazon Textract, or your custom machine learning (ML) models, you can use Amazon Augmented AI to get human review of low-confidence predictions or random prediction samples.

Amazon Augmented AI (Amazon A2I) is a service that brings human review of ML predictions to all developers by removing the heavy lifting associated with building human review systems or managing large numbers of human reviewers.

Many ML applications require humans to review low-confidence predictions to ensure the
    results are correct. For example, extracting information from scanned mortgage application forms
    can require human review due to low-quality scans or poor handwriting. Building human review
    systems can be time-consuming and expensive because it involves implementing complex processes
    or *workflows*, writing custom software to manage review tasks
    and results, and managing large groups of reviewers.

Amazon A2I streamlines building and managing human reviews for ML applications. Amazon A2I provides built-in human review workflows for common ML use cases, such as content moderation and text extraction from documents. You can also create your own workflows for ML models built on SageMaker AI or any other tools. Using Amazon A2I, you can allow human reviewers to step in when a model is unable to make a high-confidence prediction or to audit its predictions on an ongoing basis.

The following examples demonstrate how you can use Amazon A2I to integrate a human review
      loop into your ML application. For each of these examples, you can find a Jupyter Notebook
      that demonstrates that workflow in [Use Cases and Examples Using Amazon A2I](./a2i-task-types-general.html). 

**Use Amazon A2I with Amazon Textract** – Have humans
        review important key-value pairs in single-page documents or have Amazon Textract randomly sample
        and send documents from your dataset to humans for review. 

**Use Amazon A2I with Amazon Rekognition** – Have humans review
        unsafe images for explicit adult or violent content if Amazon Rekognition returns a low-confidence score,
        or have Amazon Rekognition randomly sample and send images from your dataset to humans for review.

**Use Amazon A2I to review real-time ML inferences**
        – Use Amazon A2I to review real-time, low-confidence inferences made by a model
        deployed to a SageMaker AI hosted endpoint and incrementally train your model using Amazon A2I
        output data.

**Use Amazon A2I with Amazon Comprehend** – Have humans review
        Amazon Comprehend inferences about text data such as sentiment analysis, text syntax, and entity
        detection.

**Use Amazon A2I with Amazon Transcribe** – Have humans review
        Amazon Transcribe transcriptions of video or audio files. Use the results of transcription human review
        loops to create a custom vocabulary and improve future transcriptions of similar video or
        audio content.

**Use Amazon A2I with Amazon Translate** – Have humans review
        low-confidence translations returned from Amazon Translate.

**Use Amazon A2I to review tabular data** – Use
        Amazon A2I to integrate a human review loop into an ML application that uses tabular
        data.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Amazon A2I enables human review workflows integrating Textract, Rekognition, Comprehend, Translate via SageMaker Jupyter Notebooks.

Fully managed ML service enables building, training, deploying models; renamed SageMaker AI December 2024.

Administrators configure unified AWS data, AI, ML analytics platform managing users, access, governance, generative AI development.

SageMaker built-in algorithms support tabular, text, image, time-series supervised unsupervised ML tasks.