# What is covered in the AWS SDKs and Tools Reference Guide - AWS SDKs and Tools

**Source:** [https://docs.aws.amazon.com/credref/latest/refdocs/index.html](https://docs.aws.amazon.com/credref/latest/refdocs/index.html)

---

[Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html)

*29 May 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Many SDKs and tools share some common functionality, either through shared design specifications or through a shared library.

This guide includes information regarding:

[Globally configuring AWS SDKs and tools](./creds-config-files.html) –
                How to use the shared `config` and `credentials` files or environment variables to configure your AWS SDKs and
                tools. 

[Authentication and access using AWS SDKs and tools](./access.html) – Establish how your code
                or tool authenticates with AWS when you develop with AWS services.

[AWS SDKs and tools settings reference](./settings-reference.html) –
                Reference for all standardized settings available for authentication and
                configuration.

[AWS Common Runtime (CRT) libraries](./common-runtime.html) – Overview
                of the shared AWS Common Runtime (CRT) libraries that are available to almost all SDKs.

[AWS SDKs and Tools maintenance policy](./maint-policy.html) covers the maintenance
                policy and versioning for AWS Software Development Kits (SDKs) and tools,
                including Mobile and Internet of Things (IoT) SDKs, and their underlying
                dependencies.

This AWS SDKs and Tools Reference Guide is intended to be a base of information that is applicable to multiple SDKs and tools. The specific guide for the SDK or tool that you are using should be used in addition to any information presented here. The following are the SDK and tools which have relevant sections of material in this guide:

| If you are using: | This guide's relevant sections for you are: | 
|---|---|
| 
 | [AWS SDKs and Tools maintenance policy](./maint-policy.html) | 
| 
 | |
| 
 
 
 
 | 

For an overview of tools that can help you develop applications on AWS, see
                    [Tools to Build on AWS](https://aws.amazon.com/tools/). 

For information on support, see the [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/). 

For AWS terminology, see the [AWS
                    glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html) in the *AWS Glossary
                    Reference*.

Amazon Q Developer is a generative AI-powered conversational assistant that can help you to understand, build, extend, and operate AWS applications. To accelerate your building
            on AWS, the model that powers Amazon Q is augmented with high-quality AWS content to produce more complete, actionable, and referenced answers. For more information, see [What is Amazon Q Developer?](https://docs.aws.amazon.com/amazonq/latest/aws-builder-use-ug/what-is.html) in the *Amazon Q Developer User Guide*.
            

AWS Integrated Development Environment (IDE) Toolkits are plugins and extensions
                that enable access to AWS services in your IDE. Amazon Q IDE plugins and extensions
                enable generative AI assistance in your IDE. For detailed information about each of
                the IDE Toolkits, see the Toolkit User Guides in the preceding table. To learn more
                about using Amazon Q in your IDE, see the [Using Amazon Q in the IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE.html)
                topic in the *Amazon Q* developer guide.

AWS IDE Toolkits and Amazon Q may collect and store client-side telemetry data to inform decisions regarding future AWS Toolkit and Amazon Q releases. The data collected quantifies your usage of the AWS Toolkit and Amazon Q.

To learn more about the telemetry data collected across all of the AWS IDE
                Toolkits and Amazon Q, see the [commonDefinitions.json](https://github.com/aws/aws-toolkit-common/blob/main/telemetry/definitions/commonDefinitions.json) document in the
                    

`aws-toolkit-common` Github repository.For detailed information about the telemetry data collected by each of the AWS IDE Toolkits and Amazon Q extensions, reference the resource documents in the following AWS Toolkit GitHub repositories:

 Certain AWS services that are accessible in the AWS Toolkits may collect
                additional client-side telemetry data. For detailed information about the type of
                data collected by each individual AWS service, see the [AWS Documentation](https://docs.aws.amazon.com/) topic for the
                specific service you're interested in. 

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.