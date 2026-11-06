# What is AWS Lambda? - AWS Lambda

**Source:** [https://docs.aws.amazon.com/lambda/latest/dg/index.html](https://docs.aws.amazon.com/lambda/latest/dg/index.html)

---

[Tag propagation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-managed-instances-tag-propagation.html)

*10 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Join Serverless experts for free hands-on workshops to learn how to build Serverless 
      applications with best practices. [Click here](https://aws-experience.com/amer/smb/events/series/Get-Hands-On-With-Serverless?trk=188abe3e-9f94-4e84-aefb-398d944ad567%26sc_channel%3Del) to sign up.

AWS Lambda is a compute service that runs code without the need to manage servers. Your code runs, scaling up and down automatically, with pay-per-use pricing. 
    To get started, see [Create your first function](./getting-started.html).

You can use Lambda for:

**File processing**: Process files automatically when uploaded to Amazon Simple Storage Service. See [file processing examples](./example-apps.html#examples-apps-file) for details.

**Long-running workflows:** Use [durable Lambda functions](./durable-functions.html) to build stateful, multi-step workflows that can run for up to one year. Perfect for order processing, approval workflows, human-in-the-loop processes, and complex data pipelines that need to remember their progress.

**Database operations and integration examples**: Respond to database changes and automate data workflows. See [database examples](./example-apps.html#examples-apps-database) for details.

**Scheduled and periodic tasks**: Run automated operations on a regular schedule using EventBridge. See [scheduled task examples](./example-apps.html#examples-apps-scheduled) for details.

**Stream processing**: Process real-time data streams for analytics and monitoring. See [Kinesis Data Streams](./with-kinesis.html) for details.

**Web applications**: Build scalable web apps that automatically adjust to demand.

**Mobile backends**: Create secure API backends for mobile and web applications.

**IoT backends**: Handle web, mobile, IoT, and third-party API requests. See [IoT](./services-iot.html) for details.

For pricing information, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

[Lambda functions](./lambda-functions-chapter.html)
      run for up to 15 minutes and are ideal for event-driven tasks like processing API requests, handling
      file uploads, or responding to database changes. [Durable functions](./durable-functions.html)
      extend this model for workloads that need to run longer and survive interruptions. They can execute for
      up to one year, automatically checkpointing their progress so they resume reliably after failures. Use
      durable functions when you need multi-step workflows, human-in-the-loop approvals, or coordination
      across services over extended periods.

When using Lambda, you are responsible only for your code. Lambda runs your code on a high-availability compute infrastructure and manages all the computing resources, including server and operating system maintenance, capacity provisioning, automatic scaling, and logging.

Because Lambda is a serverless, event-driven compute service, it uses a different programming paradigm than traditional web applications. The following model illustrates how Lambda works:

You write and organize your code in [Lambda functions](./concepts-basics.html#gettingstarted-concepts-function), which are the basic building blocks you use to create a Lambda application.

You control security and access through [Lambda permissions](./lambda-permissions.html), using [execution roles](./lambda-intro-execution-role.html) to manage what AWS services your functions can interact with and what resource policies can interact with your code.

Event sources and AWS services [trigger](./concepts-event-driven-architectures.html) your Lambda functions, passing event data in JSON format, which your functions process (this includes event source mappings).

[Lambda runs your code](./concepts-how-lambda-runs-code.html) with language-specific runtimes (like Node.js and Python) in execution environments that package your runtime, layers, and extensions.

To learn how to build **serverless solutions**, check out the [Serverless Developer Guide](https://docs.aws.amazon.com/serverless/latest/devguide/).

**Configure, control, and deploy secure applications:**

[Environment variables](./configuration-envvars.html) modify application behavior without new code deployments.

[Versions](./configuration-versions.html) safely test new features while maintaining stable production environments.

[Layers](./chapter-layers.html) optimize code reuse and maintenance by sharing common components across multiple functions.

[Code signing](./configuration-codesigning.html) enforce security compliance by ensuring only approved code reaches production systems.

**Scale and perform reliably:**

[Concurrency and scaling controls](./lambda-concurrency.html) precisely manage application responsiveness and resource utilization during traffic spikes.

[SnapStart](./snapstart.html) significantly reduce cold start times. Lambda SnapStart can provide as low as sub-second startup performance, typically with no changes to your function code.

[Response streaming](./configuration-response-streaming.html) optimize function performance by delivering large payloads incrementally for real-time processing.

[Container images](./images-create.html) package functions with complex dependencies using container workflows.

**Connect and integrate seamlessly:**

[VPC networks](./configuration-vpc.html) secure sensitive resources and internal services.

[File systems](./configuration-filesystem.html) integration that shares persistent data and manage stateful operations across function invocations.

[Function URLs](./urls-configuration.html) create public-facing APIs and endpoints without additional services.

[Extensions](./lambda-extensions.html) augment functions with monitoring, security, and operational tools.

For information on how Lambda works, see [How Lambda works](./concepts-basics.html).

To start using Lambda, see [Create your first Lambda function](./getting-started.html). 

For a list of example applications, see [Getting started with example applications and patterns](./example-apps.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Customize CloudFront content delivery using Lambda@Edge functions to reduce latency via edge computing.

Lambda runtime deprecation policy outlines supported runtimes, deprecation dates, AL2023 upgrades, notifications, management controls.

Configure Lambda environment variables customize function behavior, encrypt secrets, manage reserved runtime variables securely.

Lambda SQS event source mapping enables batch processing, provisioned polling, partial batch responses, idempotent functions.