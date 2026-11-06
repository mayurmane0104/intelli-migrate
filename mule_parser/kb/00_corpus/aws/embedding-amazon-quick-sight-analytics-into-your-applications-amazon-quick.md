# Embedding Amazon Quick Sight analytics into your applications - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedding-overview.html](https://docs.aws.amazon.com/quick/latest/userguide/embedding-overview.html)

---

| Applies
                    to:Enterprise Edition | 

To embed analytics, you can run the Amazon Quick Sight embedding API to generate the embed code. Alternatively for dashboards, you can copy an embed code when you share the dashboard in Amazon Quick Sight. Each option is described below.

## 1-click embedding for registered users

            When you share a dashboard with registered users in your account, you can copy an embed code for the dashboard and paste it into your internal application's HTML.

Using 1-click enterprise embedding is best for when you want to embed a Amazon Quick Sight dashboard in an internal application that users need to authenticate in to. When you copy the embed code, you get a static embed code that doesn't change.

For more information, see [Embedding Amazon Quick Sight visuals and dashboards for registered users with a 1-click embed code](./embedded-analytics-1-click.html).

## Embedding with the Amazon Quick Sight APIs

            Embedding with the Amazon Quick Sight API is best for when you want to embed the Amazon Quick Sight experience in an internal application that users must authenticate in to, or an external application that anyone can access. When you use the embedding API operations to generate an embed code, you get a one-time code.

For more information, see [Embedding with the Amazon Quick Sight APIs](./embedded-analytics-api.html).