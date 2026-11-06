# Build an end-to-end generative AI workflow with Amazon Bedrock Flows - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)

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

Amazon Bedrock Flows offers the ability for you to use supported foundation models (FMs) to build workflows by linking prompts, foundational models, and other AWS services to create end-to-end solutions.

With flows, you can quickly build complex generative AI workflows using a visual builder, easily integrate with Amazon Bedrock offerings such as FMs, knowledge bases, and other AWS services such as AWS Lambda by transferring data between them, and deploying immutable workflows to move from testing to production in few clicks.

Refer to the following resources for more information about Amazon Bedrock Flows:

Pricing for Amazon Bedrock Flows is dependent on the resources that you use. For example, if you invoke a flow with a prompt node that uses an Amazon Titan model, you'll be charged for invoking that model. For more information, see [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing/).

To see quotas for flows, see [Amazon Bedrock endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/bedrock.html) in the AWS General Reference.

The following are some example tasks that you can build a flow for in Amazon Bedrock:

**Create and send an email invite** – Create a flow connecting a prompt node, knowledge base node, and Lambda function node. Provide the following prompt to generate an email body: `Send invite to John Smith’s extended team for in-person documentation read for an hour at 2PM EST next Tuesday`. After processing the prompt, the flow queries a knowledge base to look up the email addresses of John Smith's extended team, and then sends the input to a Lambda function to send the invite to all the team members in the list.

**Troubleshoot using the error message and the ID of the resource that is causing the error** – The flow looks up the possible causes of the error from a documentation knowledge base, pulls system logs and other relevant information about the resource, and updates the faulty configurations and values for the resource.

**Generate reports** – Build a flow to generate metrics for top products. The flow looks for the sales metrics in a
                database, aggregates the metrics, generates a summary report for top product
                purchases, and publishes the report on the specified portal.

**Ingest data from a specified dataset** – Provide a prompt such as the following: ```
Start ingesting new datasets added after 3/31 and report
                    failures
```
. The flow starts preparing data for ingestion and keeps
                reporting on the status. After the data preparation is complete, the flow starts the
                ingestion process filtering the failed data. After data ingestion is complete, the
                flow summarizes the failures and publishes a failure report.

Flows for Amazon Bedrock makes it easy for you link foundation models (FMs), prompts, and other AWS services to quickly create, test, and run your flows. You can manage flows using the visual builder in the Amazon Bedrock console or through the APIs.

The general steps for creating, testing, and deploying a flow are as follows:

Specify a flow name, description, and appropriate IAM permissions.

Design your flow by deciding the nodes you want to use.

Create or define all the resources you require for each node. For example, if you are planning to use an AWS Lambda function, define the functions you need for the node to complete its task.

Add nodes to your flow, configure them, and create connections between the nodes by linking the output of a node to the input of another node in the flow.

Prepare the flow, so that the latest changes apply to the *working draft* of the flow, a version of the flow that you can use to iteratively test and update your flow

Test the flow by invoking it with sample inputs to see the outputs it yields.

When you're satisfied with a flow's configuration, you can create a snapshot of it by publishing a *version*. The version preserves flow definition as it exists at the time of the creation. Versions are immutable because they act as a snapshot of the flow at the time it was created.

Create an alias that points to the version of your flow that you want to use in your application.

Set up your application to make `InvokeFlow` requests to the alias. If you need to revert to an older version or upgrade to a newer one, you can change the routing configuration of the alias.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Build generative AI workflows linking prompts, models, knowledge bases using drag-and-drop nodes, conditions, export options.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.