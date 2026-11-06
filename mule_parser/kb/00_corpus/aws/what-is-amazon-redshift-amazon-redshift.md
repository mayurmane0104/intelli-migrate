# What is Amazon Redshift? - Amazon Redshift

**Source:** [https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html)

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
      

Welcome to the *Amazon Redshift Management Guide*. Amazon Redshift is a fully managed,
        petabyte-scale data warehouse service in the cloud. Amazon Redshift Serverless lets you access and
        analyze data without all of the configurations of a provisioned data warehouse. Resources
        are automatically provisioned and data warehouse capacity is intelligently scaled to deliver
        fast performance for even the most demanding and unpredictable workloads. You don't incur
        charges when the data warehouse is idle, so you only pay for what you use. You can load data
        and start querying right away in the Amazon Redshift query editor v2 or in your favorite business
        intelligence (BI) tool. Enjoy the best price performance and familiar SQL features in an
        easy-to-use, zero administration environment.

Regardless of the size of the dataset, Amazon Redshift offers fast query performance using the same SQL-based tools and business intelligence applications that you use today.

If you are a first-time user of Amazon Redshift, we recommend that you begin by reading the following sections:

[Service Highlights
                        and Pricing](https://aws.amazon.com/redshift/redshift-serverless) – This product detail page provides the Amazon Redshift
                    value proposition, service highlights, and pricing.

[Get started with Amazon Redshift Serverless data warehouses](https://docs.aws.amazon.com/redshift/latest/gsg/new-user-serverless.html) – This
                    topic walks you through the process of setting up a serverless data warehouse,
                    creating resources, and querying sample data. 

[Amazon Redshift Database Developer Guide](https://docs.aws.amazon.com/redshift/latest/dg/) – If you are a database developer, this guide explains how
                    to design, build, query, and maintain the databases that make up your data
                    warehouse.

If you prefer to manage your Amazon Redshift resources manually, you can create provisioned
            clusters for your data querying needs. For more information, see [Amazon Redshift
                clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html).

As an application developer, you can use the Amazon Redshift API or the AWS Software
            Development Kit (SDK) libraries to manage clusters programmatically. If you use the
            Amazon Redshift API, you must authenticate every HTTP or HTTPS request to the API by signing
            it. For more information about signing requests, go to [Signing an HTTP request](./amazon-redshift-signing-requests.html).

For information about the API, CLI, and SDKs, go to the following links:

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Orchestrate ETL/ELT workflows using Step Functions, Redshift Data API, parallel jobs, Lambda, IAM policies, CloudFormation.

AMS SSP provisions Athena, enabling S3 SQL queries via customer_athena_console_role, requiring AWS Glue catalog athena-query-results bucket.

Automates CloudTrail log queries via Athena, creating/deleting tables using IAM-permitted S3, Glue, Athena actions.

Configure ODBC driver version 1.x connecting Amazon Redshift cluster via third-party SQL clients Linux Windows macOS.

Configure provisioned clusters using RG RA3 nodes, managed storage, VPC security, CloudWatch alarms, reserved nodes.

CREATE TABLE defines distribution styles, sort keys, encoding, IDENTITY columns, temporary tables, constraints.