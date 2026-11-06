# Embedding with the Amazon Quick Sight APIs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-api.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-api.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

There are only a few steps involved in the actual process of embedding analytics using the Amazon Quick Sight APIs.

Before you begin, make sure to have the following items in place:

- 
                Set up the required IAM permissions for the caller identity used by your application that will use the AWS SDK to make API calls. For example, grant permission to allow the `quicksight:GenerateEmbedUrlForAnonymousUser`or`quicksight:GenerateEmbedUrlForRegisteredUser`action.
- 
                To embed for registered users, share Amazon Quick Sight assets with them beforehand. For new authenticating users, know how to grant access to the assets. One way to do this is by adding all the assets to a Amazon Quick Sight folder. If you prefer to use the Amazon Quick Sight API, use the `DescribeDashboardPermissions`and`UpdateDashboardPermissions`API operations. For more information, see[DescribeDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeDashboardPermissions.html)or[UpdateDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPermissions.html)in the*Amazon Quick API Reference*. If you want to share the dashboard with all users in a namespace or group, you can share the dashboard with`namespace`or`group`.
- 
                If you're embedding dashboards, make sure to have the ID of the dashboards you want to embed. The dashboard ID is the code in the URL of the dashboard. You can also get it from the dashboard URL. 
- 
                A Amazon Quick Sight administrator must explicitly enable domains where you plan to embed your Amazon Quick Sight analytics. You can do this by using the **Manage Amazon Quick Sight**,**Domains and Embedding**from the profile menu, or you can use the`AllowedDomains`parameter of a`GenerateEmbedUrlForAnonymousUser`or`GenerateEmbedUrlForRegisteredUser`API call.This option is only visible to Amazon Quick Sight administrators. You can also add subdomains as part of a domain. For more information, see [Allow listing domains at runtime with the Amazon Quick API](./manage-domains.html#embedding-run-time).All domains in your static allow list (such as development, staging, and production) must be explicitly allowed, and they must use HTTPS. You can add up to 100 domains to the allow list. You can add domains at runtime with Amazon Quick Sight API operations. 

After all the prerequisites are complete, embedding Amazon Quick Sight involves the following steps, which are explained in greater detail later:

- 
                For authentication, use your application server to authenticate the user. After authentication in your server, generate the embedded dashboard URL using the AWS SDK that you need. 
- 
                In your web portal or application, embed Amazon Quick Sight using the generated URL. To simplify this process, you can use the Amazon Quick Sight Embedding SDK, available on [NPMJS](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk)and[GitHub](https://github.com/awslabs/amazon-quicksight-embedding-sdk). This customized JavaScript SDK is designed to help you efficiently integrate Amazon Quick Sight into your application pages, set defaults, connect controls, get callbacks, and handle errors.

You can use AWS CloudTrail auditing logs to get information about the number of embedded dashboards, users of an embedded experience, and access rates.

###### Topics

- [Embedding Amazon Quick Sight dashboards with the Amazon Quick Sight API](./embedding-dashboards.html)
- [Embedding Amazon Quick Sight visuals with the Amazon Quick Sight APIs](./embedding-visuals.html)
- [Embedding the full functionality of the Amazon Quick Sight console for registered users](./embedded-analytics-full-console-for-authenticated-users.html)
- [Embedding the Amazon Q in Amazon Quick Sight Generative Q&A experience](./embedding-gen-bi.html)
- [Embedding analytics using the GetDashboardEmbedURL and GetSessionEmbedURL API operations](./embedded-analytics-deprecated.html)