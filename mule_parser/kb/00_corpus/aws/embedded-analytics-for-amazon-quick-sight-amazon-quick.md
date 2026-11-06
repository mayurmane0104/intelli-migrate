# Embedded analytics for Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics.html)

---

###### Important

Amazon Quick Sight has new API operations for embedding analytics:
                `GenerateEmbedUrlForAnonymousUser` and
                `GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
                `GetSessionEmbedUrl` API operations to embed dashboards and the
            Amazon Quick Sight console, but they don't contain the latest embedding capabilities. For
            more information about embedding using the old API operations, see [Embedding analytics using the GetDashboardEmbedURL and GetSessionEmbedURL API operations](./embedded-analytics-deprecated.html).

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

With Amazon Quick Sight embedded analytics, you can seamlessly integrate data-driven experiences into your software applications. You can style the embedded components to match your brand. This capability brings the power of Amazon Quick Sight to your end users, where they can analyze and interact with data without ever leaving the application. Improving the user experience by reducing cognitive complexity gives users a better opportunity for deeper understanding and effectiveness.

Amazon Quick Sight supports embedding for these elements:

- 
            Amazon Quick Sight console (full authoring experience for registered users ) 
- 
            Amazon Quick Sight dashboards and visuals (for registered users, anonymous users, public end users) 
- 
            Amazon Quick Sight Q search bar (for registered users and anonymous users) 

With an embedded Amazon Quick Sight console, you embed the full Amazon Quick Sight experience. Doing this makes it possible to use Amazon Quick Sight authoring tools as part of your application, rather than in the context of the AWS Management Console or a standalone website. Users of an embedded Amazon Quick Sight console need to be registered as Amazon Quick Sight authors or admins in your AWS account. They also need to be authenticated into the same AWS account, using any of the Amazon Quick Sight-supported authentication methods.

With an embedded Amazon Quick Sight dashboard or visual, readers get the same functionality and interactivity as they do in a published dashboard or visual. To use an embedded dashboard or visual, readers (viewers) can include any of the following:

- 
            Amazon Quick Sight users authenticated in your AWS account by any method supported by Amazon Quick Sight. 
- 
            Unauthenticated visitors to a website or application – This option requires session packs with capacity pricing . For information about subscription types, see [Understanding Amazon Quick Sight subscriptions and roles](https://docs.aws.amazon.com/quicksight/latest/user/user-types.html#subscription-role-mapping).
- 
            Multiple end users viewing a display on monitors or large screens by programmatic access. 

If your app also resides in AWS, the app doesn't need to reside on the same AWS account as the Amazon Quick Sight subscription. However, the app needs to be able to assume the AWS Identity and Access Management (IAM) role that you use for the API calls.

Before you can embed content, make sure that you're using Amazon Quick Sight Enterprise edition in the AWS account where you plan to use embedding.

Amazon Quick Sight embedding is available in all supported AWS Regions.