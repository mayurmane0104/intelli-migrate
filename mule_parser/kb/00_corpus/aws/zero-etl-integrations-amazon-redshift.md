# Zero-ETL integrations - Amazon Redshift

**Source:** [https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.html)

---

[Use SHOW commands](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-show-commands.html)

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

         Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198. 
  Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
  [
          blog post
        ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/).
      

         Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198. 
  Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
  [
          blog post
        ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/).
      

Zero-ETL integration is a fully managed solution that makes transactional and operational data available in Amazon Redshift from multiple operational and transactional sources. With this solution, you can configure an integration from your source to an Amazon Redshift data warehouse. You don't need to maintain an extract, transform, and load (ETL) pipeline. We take care of the ETL for you by automating the creation and management of data replication from the data source to the Amazon Redshift cluster or Redshift Serverless namespace. You can continue to update and query your source data while simultaneously using Amazon Redshift for analytic workloads, such as reporting and dashboards.

With zero-ETL integration you have fresher data for analytics, AI/ML, and reporting. You get more accurate and timely insights for use cases like business dashboards, optimized gaming experience, data quality monitoring, and customer behavior analysis. You can make data-driven predictions with more confidence, improve customer experiences, and promote data-driven insights across the business.

The following sources are currently supported for zero-ETL integrations:

Amazon Aurora MySQL (AMS)

Amazon Aurora PostgreSQL (APG)

Amazon DynamoDB

Amazon RDS for MySQL

Amazon RDS for Oracle

Amazon RDS for PostgreSQL

Oracle Database@AWS

Applications including Salesforce, Salesforce Marketing Cloud Account Engagement, SAP, ServiceNow, Instagram ads, Meta ads, and Zendesk

Self-Managed MySQL, PostgreSQL, SQL Server, and Oracle

To create a zero-ETL integration, you specify an integration source and an Amazon Redshift data warehouse as the target. After an initial data load, the integration replicates data from the source to the target data warehouse. The data becomes available in Amazon Redshift. You control the encryption of your data when you create the integration source, when you create the zero-ETL integration, and when you create the Amazon Redshift data warehouse. The integration monitors the health of the data pipeline and recovers from issues when possible. You can create integrations from sources of the same type into a single Amazon Redshift data warehouse to derive holistic insights across multiple applications.

With the data in Amazon Redshift, you can use analytics that Amazon Redshift provides. For example, built-in machine learning (ML), materialized views, data sharing, and direct access to multiple data stores and data lakes. For data engineers, zero-ETL integration provides access to time-sensitive data that otherwise can get delayed by intermittent errors in complex data pipelines. You can run analytical queries and ML models on transactional data to derive timely insights for time-sensitive events and business decisions.

You can create an Amazon Redshift event notification subscription so you can be notified when an event
    occurs for a given zero-ETL integration. To view the list of integration-related event notifications, see
      [Zero-ETL integration event notifications with Amazon EventBridge](./integration-event-notifications.html). The simplest way to create a subscription
    is with the Amazon SNS console. For information on creating an Amazon SNS topic and subscribing to it, see
      [Getting started with
      Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/GettingStarted.html) in the *Amazon Simple Notification Service Developer Guide*.

As you get started with zero-ETL integrations, consider the following concepts:

A source database is the database from where data is replicated into Amazon Redshift.

A target data warehouse is the Amazon Redshift provisioned cluster or Redshift Serverless workgroup where data is replicated to.

A destination database is the database that you create from a zero-ETL integration in the target data warehouse.

For information about system tables and views you can use to monitor your zero-ETL integrations, see
      [Monitoring zero-ETL integrations with Amazon Redshift system views](./zero-etl-monitoring.html#zero-etl-monitoring-sysviews). 

For a list of AWS Regions that each source for zero-ETL integrations supports, see [Supported Regions for zero-ETL integrations](./zero-etl-using.regions.html).

For pricing information for zero-ETL integrations, see the appropriate pricing page:

For more information about zero-ETL integration sources, see the following topics:

For Aurora zero-ETL integrations, see [Benefits](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html#zero-etl.benefits),
          [Key
          concepts](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html#zero-etl.concepts), [Limitations](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html#zero-etl.reqs-lims), [Quotas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html#zero-etl.quotas), and
          [Supported
          Regions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/zero-etl.html#zero-etl.regions) of zero-ETL integrations in the *Amazon Aurora User Guide*. 

For RDS zero-ETL integrations, see [Benefits](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html#zero-etl.benefits), [Key
          concepts](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html#zero-etl.concepts), [Limitations](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html#zero-etl.reqs-lims),
          [Quotas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html#zero-etl.quotas), and [Supported Regions](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/zero-etl.html#zero-etl.regions)
        of zero-ETL integrations in the *Amazon RDS User Guide*. 

For DynamoDB zero-ETL integrations, see [DynamoDB
          zero-ETL integration with Amazon Redshift](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/RedshiftforDynamoDB-zero-etl.html) in the *Amazon DynamoDB Developer Guide*. 

For zero-ETL integrations with applicatons, see [Zero-ETL integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html) in the
          *AWS Glue Developer Guide*. 

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Monitor Aurora zero-ETL integrations via Redshift system tables, CloudWatch metrics, EventBridge events, RDS console.

Monitor RDS zero-ETL integrations via Redshift system tables, CloudWatch metrics, EventBridge events.

Create Redshift destination database via integration ID, enabling zero-ETL active-state data replication from Aurora PostgreSQL sources.

Configure ODBC driver version 1.x connecting Amazon Redshift cluster via third-party SQL clients Linux Windows macOS.

Configure provisioned clusters using RG RA3 nodes, managed storage, VPC security, CloudWatch alarms, reserved nodes.

CREATE TABLE defines distribution styles, sort keys, encoding, IDENTITY columns, temporary tables, constraints.