# Enabling executive summaries in embedded dashboards - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-genbi-executive-summaries-dashboard.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-genbi-executive-summaries-dashboard.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

You can enable executive summaries in your embedded dashboards. When enabled, registered
        users can generate executive summaries that provide a summary of all insights that
        Amazon Quick Sight has generated for the dashboard. Executive summaries make it easier for
        readers to find key insights and information about a dashboard. For more information about
        how users generate an executive summary of a dashboard, see [Generate
            an executive summary of an Amazon Quick Sight dashboard](https://docs.aws.amazon.com/quicksight/latest/user/use-executive-summaries.html).

###### Note

Executive summaries are only available in embedded dashboards for registered users, and cannot be enabled in embedded dashboards for anonymous or unregistered users.

###### To enable executive summaries in embedded dashboards for registered users

- 
            Follow the steps in [Embedding Amazon Quick Sight dashboards for registered users](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-dashboards-for-authenticated-users.html)to embed a dashboard with the following changes:- 
                    When generating the URL in Step 2, set `Enabled: true`in the`ExecutiveSummary`parameter in the[GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html)or[GenerateEmbedUrlForRegisteredUserWithIdentity](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUserWithIdentity.html)as shown in the following example:`ExperienceConfiguration: { Dashboard: { InitialDashboardId:``dashboard_id`, FeatureConfigurations: { AmazonQInQuickSight: { ExecutiveSummary: { Enabled: true } } } } } }
- 
                    When embedding the dashboard URL with the Amazon Quick Sight Embedding SDK in Step 3, set `executiveSummary: true`in`contentOptions`, as shown in the following example:`const contentOptions = { toolbarOptions: { executiveSummary: true } };`
 
-