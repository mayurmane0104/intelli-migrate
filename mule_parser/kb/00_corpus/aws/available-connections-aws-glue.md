# Available connections - AWS Glue

**Source:** [https://docs.aws.amazon.com/glue/latest/dg/available-connections.html](https://docs.aws.amazon.com/glue/latest/dg/available-connections.html)

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

AWS Glue supports the following connection types:

Adobe Analytics

Adobe Marketo Engage

Amazon Aurora (supported if the native JDBC driver is being used. Not all driver features can be leveraged)

Amazon DocumentDB

Amazon DynamoDB

Amazon OpenSearch Service, for use with AWS Glue for Spark.

Amazon Redshift

Asana

Azure Cosmos, for use of Azure Cosmos DB for NoSQL with AWS Glue ETL jobs

Azure SQL, for use with AWS Glue for Spark.

Blackbaud

CircleCI

Datadog

Docusign Monitor

Domo

Dynatrace

Facebook Ads

Facebook Page Insights

Freshdesk

Freshsales

Google Ads

Google Analytics 4

Google BigQuery, for use with AWS Glue for Spark.

Google Search Console

Google Sheets

HubSpot

Instagram Ads

Intercom

JDBC

Jira Cloud

Kafka

Kustomer

Mailchimp

Microsoft Dynamics 365 CRM

Microsoft Teams

Mixpanel

Monday

MongoDB

MongoDB Atlas

Okta

Oracle NetSuite

Paypal

Pendo

Pipedrive

Productboard

QuickBooks

REST API (requires connection type setup, see [REST API Connections](https://docs.aws.amazon.com/glue/latest/dg/rest-api-connections.html))

Salesforce

Salesforce Commerce Cloud

Salesforce Marketing Cloud

Salesforce Marketing Cloud Account Engagement (previously Salesforce Pardot)

SAP HANA, for use with AWS Glue for Spark.

SAP OData

SendGrid

ServiceNow

Slack

Smartsheet

Snapchat Ads

Stripe

Snowflake, for use with AWS Glue for Spark.

Teradata Vantage, when using AWS Glue for Spark.

Twilio

Vertica, for use with AWS Glue for Spark.

WooCommerce

Zendesk

Zoho CRM

Zoom Meetings

Various Amazon Relational Database Service (Amazon RDS) offerings.

Network (designates a connection to a data source that is in an Amazon Virtual Private Cloud (Amazon VPC))

With AWS Glue Studio, you can also create a connection for a *connector*. A connector is an optional code package that assists with
            accessing data stores in AWS Glue Studio. For more information, see [Using connectors and connections with
                AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html)
        

For information about how to connect to on-premises databases, see [How to access and analyze on-premises data stores using
            AWS Glue](https://aws.amazon.com/blogs/big-data/how-to-access-and-analyze-on-premises-data-stores-using-aws-glue/) at the AWS Big Data Blog website.

To create a connection with VPC configuration while using a custom IAM role, it must have the following VPC access actions:

secretsmanager:GetSecretValue

secretsmanager:PutSecretValue

secretsmanager:DescribeSecret

ec2:CreateNetworkInterface

ec2:DeleteNetworkInterface

ec2:DescribeNetworkInterfaces

ec2:DescribeSubnets

You can't edit connections through the AWS Glue console if you created a v2 connection using AWS Glue APIs:

Amazon DocumentDB

Amazon Aurora

MariaDB

MongoDB Atlas

MongoDB

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Unified data connections enable federated queries, ETL reuse, OAuth2 auth, metadata browse across AWS services.

Connect Domo Amazon AppFlow transferring datasets client ID secret supported destinations integration setup.

Execute SQL queries JupyterLab extension; store results pandas DataFrames; use dynamic parameters; install Snowflake dependencies SageMaker distribution.

Serverless ETL pipelines, automated crawlers, visual canvas, sensitive data detection, centralized catalog management.

AWS Glue DynamicFrame enables ETL transforms, resolves choice types, relationalizes nested schemas, unnests DynamoDB JSON structures PySpark.

ETL workflows leverage Data Catalog metadata, crawlers, dynamic frames, triggers, DPU workers, visual editor transformations.