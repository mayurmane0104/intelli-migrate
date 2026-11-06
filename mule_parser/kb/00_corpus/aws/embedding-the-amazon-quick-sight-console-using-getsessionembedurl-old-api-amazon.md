# Embedding the Amazon Quick Sight console using GetSessionEmbedUrl (old API) - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get.html)

---

###### Important

Amazon Quick Sight has new APIs for embedding analytics:
                    `GenerateEmbedUrlForAnonymousUser` and
                    `GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
                    `GetSessionEmbedUrl` APIs to embed dashboards and the
                Amazon Quick Sight console, but they do not contain the latest embedding
                capabilities. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your applications](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html).

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

In the following sections, you can find detailed information on how to provide the
            Amazon Quick Sight console experience in a custom-branded authoring portal for registered
            users using the `GetSessionEmbedUrl` API.