# Zero-ETL integrations - AWS Glue

**Source:** [https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html)

---

[Using Amazon S3 Express One Zone with AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-s3-express.html)

*22 May 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

[Zero-ETL](https://aws.amazon.com/what-is/zero-etl/) is a set of fully managed integrations by AWS that minimizes the need to build ETL data pipelines for common ingestion and replication use cases. It makes data available in Lakehouse architecture of Amazon SageMaker and Amazon Redshift from multiple operational, transactional, and application sources. Currently AWS Glue Zero-ETL supports DynamoDB, Oracle Database@AWS and SaaS sources like Salesforce, SAP, Zendesk as sources. With zero-ETL integration, you have fresher data for analytics, AI/ML, and reporting. You get more accurate and timely insights for use cases like business dashboards, optimized gaming experience, data quality monitoring, and customer behavior analysis. You can make data-driven predictions with more confidence, improve customer experiences, and promote data-driven insights across the business.

Amazon Redshift is a fast, fully managed, petabyte-scale data warehouse service that makes it simple and cost-effective to efficiently analyze all your data using your existing business intelligence tools.

Lakehouse architecture of Amazon SageMaker unifies all your data across Amazon Simple Storage Service (Amazon S3) data lakes and Amazon Redshift data warehouses, helping you build powerful analytics and AI/ML applications on a single copy of data. Lakehouse architecture of Amazon SageMaker gives you the flexibility to access and query your data in-place with all Apache Iceberg compatible tools and engines. With SageMaker Lakehouse, you also have the flexibility to access and query your data in-place with Apache Iceberg compatible tools and engines. Additionally, you can secure your data with integrated, fine-grained access controls, that are enforced across all your data in all analytic tools and engines. Define permissions once and confidently share data across your organization.

Zero-ETL integrations in AWS Glue simplify data ingestion and replication from AWS data services and third-party applications to AWS destinations.

AWS services supported as zero-ETL sources in AWS Glue include:

Amazon DynamoDB

Oracle at AWS, ODB

Third-party applications supported as zero-ETL sources in AWS Glue include:

Facebook Ads

Instagram Ads

Salesforce

Salesforce Marketing Cloud Account Engagement

SAP OData

ServiceNow

Zendesk

Zoho CRM

Self-managed databases supported as zero-ETL sources in AWS Glue include:

Oracle

SQL Server

MySQL

PostgreSQL

For more information about zero-ETL integrations from self-managed sources, see [AWS zero-ETL integration for self-managed database sources](https://docs.aws.amazon.com/dms/latest/userguide/zero-etl.html).

AWS services supported by Zero-ETL targets in AWS Glue include:

General purpose Amazon S3 bucket via Lakehouse architecture of Amazon SageMaker

Amazon S3 Tables via Lakehouse architecture of Amazon SageMaker

Redshift Managed Storage via Lakehouse architecture of Amazon SageMaker

Amazon Redshift Datawarehouse

For self-managed database sources, you can replicate data only to an Amazon Redshift data warehouse. Other targets are not supported.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

AWS Glue serverless integration replicates SAP data via OData, enabling ETL pipelines, Zero-ETL replication, scalable Spark compute.

Fully managed zero-ETL replication automates transactional data pipelines, enabling multi-source analytics Amazon Redshift.

Serverless ETL pipelines, automated crawlers, visual canvas, sensitive data detection, centralized catalog management.

AWS Glue DynamicFrame enables ETL transforms, resolves choice types, relationalizes nested schemas, unnests DynamoDB JSON structures PySpark.

ETL workflows leverage Data Catalog metadata, crawlers, dynamic frames, triggers, DPU workers, visual editor transformations.