# What is Amazon Athena? - Amazon Athena

**Source:** [https://docs.aws.amazon.com/athena/latest/ug/what-is.html](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

---

[Browser SSO OIDC credentials](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-browser-sso-oidc.html)

*5 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Amazon Athena is an interactive query service that makes it easy to analyze data directly in
        Amazon Simple Storage Service (Amazon S3) using standard [SQL](./ddl-sql-reference.html). With a few actions in the AWS Management Console, you
        can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc
        queries and get results in seconds.

For more information, see [Get started](./getting-started.html).

Amazon Athena also makes it easy to interactively run data analytics using Apache Spark
        without having to plan for, configure, or manage resources. When you run Apache Spark
        applications on Athena, you submit Spark code for processing and receive the results
        directly. Use the simplified notebook experience in Amazon Athena console to develop Apache
        Spark applications using Python or [Use Athena Spark APIs](./notebooks-spark-api-list.html).

For more information, see [Get started with Apache Spark on Amazon Athena](./notebooks-spark-getting-started.html).

Athena SQL and Apache Spark on Amazon Athena are serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. Athena scales automatically—running queries in parallel—so results are fast, even with large datasets and complex queries.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

AMS SSP provisions Athena via RFC, enabling serverless SQL queries on large-scale S3 datasets using customer_athena_console_role.

EMR Studio enables Athena SQL queries, AWS Glue Data Catalog browsing, query history, workgroups trusted identity propagation.

AMS SSP provisions Athena, enabling S3 SQL queries via customer_athena_console_role, requiring AWS Glue catalog athena-query-results bucket.

Athena engine version 3 upgrade introduces breaking changes: timestamp precision serialization errors, deprecated Iceberg time travel clauses, CHAR VARCHAR coercion workarounds.

Tutorial covers querying data, creating tables, S3 bucket setup, named queries, keyboard shortcuts, typeahead, data sources.

Athena enables infrastructure-free ad hoc SQL queries on S3 data, integrating AWS Glue Data Catalog metadata.