# Service roles - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-sr.html](https://docs.aws.amazon.com/bedrock/latest/userguide/security-iam-sr.html)

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

Amazon Bedrock uses [IAM service roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) for some features to let Amazon Bedrock carry out tasks on your behalf.

The console automatically creates service roles for supported features.

You can also create a custom service role and customize the attached permissions to your specific use-case. If you use the console, you can select this role instead of letting Amazon Bedrock create one for you.

To set up the custom service role, you carry out the following general steps.

Create the role by following the steps at [Creating a role to delegate permissions to an AWS service](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html).

Attach a **trust policy**.

Attach the relevant **identity-based permissions**.

When setting the `iam:PassRole` permission, make sure that a user can't pass
            a role where the role has more permissions than you want the user to have. For example,
            Alice might not be allowed to perform `bedrock:InvokeModel` on a custom
            model. If Alice can pass a role to Amazon Bedrock to create an evaluation of that custom
            model, the service could invoke that model on behalf of Alice while running the
            job.

Refer to the following links for more information about IAM concepts that are relevant to setting service role permissions.

Select a topic to learn more about service roles for a specific feature.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

IAM console creates MediaConvert service role; assign permissions, set boundary, ensure unique role name.

IAM roles delegate permissions create manage invoke guardrails filter content third-party models via ApplyGuardrail API.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.