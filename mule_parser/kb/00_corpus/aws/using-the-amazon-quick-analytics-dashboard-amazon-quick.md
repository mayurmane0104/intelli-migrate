# Using the Amazon Quick analytics dashboard - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/incident-response-logging-and-monitoring-quick-suite.html](https://docs.aws.amazon.com/quick/latest/userguide/incident-response-logging-and-monitoring-quick-suite.html)

---

Analytics in Amazon Quick provides insights into how users interact with your instance across all features and capabilities. The analytics dashboard delivers the data-driven insights you need to make informed decisions about security, performance, and user experience.

###### Note

The analytics dashboard is only available for IAM administrators.

The Amazon Quick analytics system captures detailed usage metrics from chat conversations, space interactions, flow executions, action invocations, research activities, automations, and custom agent usage. This comprehensive data collection enables you to understand not just what users are doing, but how effectively they're leveraging Quick to accomplish their goals while maintaining security and compliance standards.

You can use analytics to:

- 
            Monitor user adoption and engagement across all Quick features 
- 
            Identify potential issues and monitor system health through available analytics 
- 
            Analyze user feedback and satisfaction trends to improve the user experience 
- 
            Understand resource utilization patterns and identify your most valuable content 
- 
            Make data-driven decisions about feature deployment, training needs, and resource allocation 
- 
            Monitor security-related events such as blocked messages and failed queries 

###### Topics

## Analytics access and permissions

        Access to analytics in Amazon Quick is controlled by user roles and permissions to ensure data security and privacy. Currently, only IAM administrators have access to the analytics dashboard.

To access the analytics dashboard, you need the following permission:
                `quicksight:QuickSuiteUsageMetrics`

| User type | Analytics capabilities | 
|---|---|
| IAM administrators | 
 | 

## Analytics dashboard overview

        The Amazon Quick analytics dashboard is organized into several key sections that provide different perspectives on your instance usage and security events:

### Dashboard filters and controls

The analytics dashboard provides filtering options to focus on specific data:

- 
                    **Agent filter**– Select from two available options: "All Agents" to see aggregate data across all agents, or "My Assistant (System Agent)" to view system agent metrics
- 
                    **Date range picker**– Choose different time periods to analyze trends and patterns

### Active user metrics

Track how users interact with your Amazon Quick instance over time.

This section displays user activity metrics including:

- 
                    **Active users**– Daily, weekly, and monthly active user counts with trend comparisons
- 
                    **Usage trends**– Growth patterns and engagement changes over time
- 
                    **Feature adoption**– Usage distribution across chat, spaces, flows, and other features

Use these metrics to understand user adoption patterns and identify engagement opportunities.

### Chat agent and asset metrics

Monitor chat usage patterns and user feedback to understand engagement with conversational features and identify areas for improvement.

#### Conversation analytics

This section provides insights into chat usage including:

- 
                        **Total conversations**– Number of chat sessions initiated
- 
                        **Total queries**– Number of messages sent by users
- 
                        **Average queries per user**– Engagement depth metrics
- 
                        **Average queries per conversation**– Conversation length patterns displayed in a time-series chart showing trends over months
- 
                        **Conversations, queries, and active users chart**– Interactive line chart displaying total conversations, total queries, and active users trends over time with monthly granularity

These metrics help optimize chat experiences and identify usage trends.

#### User feedback analytics

Track user satisfaction to continuously improve system quality.

This section displays user feedback data including:

- 
                        **Positive feedback**– Thumbs up interactions and trends
- 
                        **Negative feedback analysis**– Thumbs down interactions with detailed reasons and breakdown by category
- 
                        **Customer feedback trend chart**– Time-series visualization showing positive vs. negative feedback patterns over months
- 
                        **Query scope selection chart**– Analytics showing how users select different query scopes, with breakdowns by "All Resources Selected", "No Resources Selected", and "Specific Resources"
- 
                        **Feedback trends**– Satisfaction changes over time with 3-month historical data
- 
                        **Thumbs down details**– View specific queries that received negative feedback, including the full conversation context and user-provided reasons
- 
                        **Thumbs down reason breakdown**– Detailed categorization of negative feedback reasons to identify common issues and improvement areas

Leverage feedback data to enhance user satisfaction and system performance.

#### Query issue analysis

Identify and resolve query problems to improve system performance.

The query issue analysis section helps you identify and resolve problems:

- 
                        **Issue percentage breakdown**– View the percentage of queries that failed by issue type
- 
                        **Failed query details**– See the actual query text from users, ordered by most recent, with issue type classification
- 
                        **Unanswered queries section**– Dedicated analytics for queries that received no response, helping identify system gaps and user needs
- 
                        **Full conversation context**– Click on any failed query to see the complete conversation leading up to the issue
- 
                        **Issue trends**– Track how query issues change over time to identify patterns

Use this analysis to proactively address system issues and improve user experience.

### Asset creation and usage

Monitor resource utilization to optimize content and feature adoption.

This section provides insights into resource utilization including:

- 
                    **Assets created**– New spaces, agents, flows, actions, research, and automations
- 
                    **Assets used**– Active resource engagement
- 
                    **Number of users by asset type chart**– Horizontal bar chart showing user distribution across different asset types including Actions, Automations, Chat, Custom Agents, Flows, Research, and Spaces
- 
                    **Most used assets**– Most popular content and tools (spaces, agents, actions, flows, research)

Use these insights to guide content strategy and resource allocation decisions.

### Automations, flows, and research agent hours usage

Monitor agent hours usage to manage subscription limits and optimize resource allocation across different subscription tiers.

This section includes the following tabs:

- 
                    **Automation and Flows Agent hours**– Provides insights into agent hours consumed by automations and flows
- 
                    **Research Agent hours**– Provides insights into agent hours consumed by research activities

Agent hours consumption metrics include:

- 
                    **Total Professional hours**– Agent hours consumed by Professional tier users
- 
                    **Total Enterprise hours**– Agent hours consumed by Enterprise tier users
- 
                    **Additional hours**– Overage hours used beyond included monthly allocations
- 
                    **Hours used by subscription type chart**– Horizontal bar chart showing user distribution by percentage of included hours consumed (25-49%, 50-74%, 75-99%, >100%) for both Enterprise (4hrs/mo) and Professional (2hrs/mo) tiers
- 
                    **Additional agent hours used by week**– Weekly trend chart showing additional hours consumed by Enterprise users after exceeding their included hours

Use these metrics to understand user adoption patterns and identify engagement opportunities.

## Accessing the analytics dashboard

        You can access the analytics dashboard from the Amazon Quick console if you have the appropriate permissions.

###### To access the analytics dashboard

- 
                Log in to the Amazon Quick console. 
- 
                From the left navigation menu, select **Analytics**, and then select**Amazon Quick Usage Metrics**.The analytics dashboard opens, displaying an overview of your instance usage and available analytics. 
- 
                Use the date picker to specify the time interval for the graphs. You can choose from the following preset intervals: - 
                        **Last week**– This interval starts from the previous Sunday at 00:00 and goes until the following Sunday at 00:00 in the UTC time zone.
- 
                        **This week**– This interval starts on Monday at 00:00 and goes until 00:00 today as per the timezone relevant for the primary region of the Amazon Quick account.
- 
                        **Last month**– This interval begins on the 1st day of the last month at 00:00 and ends on the first day of this month at 00:00 in the UTC time zone.
- 
                        **This month**– This interval begins on the 1st day of this month at 00:00 and goes until 00:00 today in the UTC time zone.
 
- 
                        

###### Note

If you don't see the Analytics option in the navigation menu, contact your instance administrator to request access.

## Understanding analytics metrics

        The analytics dashboard displays various metrics that help you understand usage patterns, performance, and security events. The following sections explain key metrics in detail.

### User activity metrics

User activity metrics help you understand how many people are actively using your Amazon Quick instance:

- 
                    **Daily active users**– Number of unique users who sent at least one message in a given day
- 
                    **Weekly active users**– Number of unique users who sent at least one message in the current week starting from Monday
- 
                    **Monthly active users**– Number of unique users who sent at least one message in the current month starting from the 1st day of the month

###### Note

Active user metrics are based on chat interactions and may not reflect all types of Quick usage.

### Security monitoring metrics

Security monitoring metrics help you track potential security issues and policy enforcement:

- 
                    **Blocked messages**– Messages blocked by guardrails for safety, policy, or content violations
- 
                    **Failed messages**– Messages that encountered errors, with specific error codes for troubleshooting

## Analytics limitations

        The following limitations apply to Amazon Quick analytics:

- 
                Analytics primarily covers chat interactions and may not capture all types of Quick usage 
- 
                Data processing may have a delay of up to 24 hours 
- 
                Historical data availability depends on when analytics was first enabled 
- 
                Some metrics may be aggregated to protect individual user privacy 
- 
                Analytics data retention follows your instance's data retention policies 
- 
                Detailed query and response data is only available to instance administrators 

###### Note

For comprehensive monitoring beyond chat interactions, consider using CloudWatch metrics
                and logs in conjunction with the analytics dashboard. For more information, see
                    [Monitoring Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/monitoring-quicksight.html).