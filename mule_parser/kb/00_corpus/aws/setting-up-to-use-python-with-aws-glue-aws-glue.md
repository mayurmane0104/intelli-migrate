# Setting up to use Python with AWS Glue - AWS Glue

**Source:** [https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-setup.html](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-setup.html)

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

Use Python to develop your ETL scripts for Spark jobs. The supported Python versions for ETL
    jobs depend on the AWS Glue version of the job. For more information on AWS Glue versions, see the
      [Glue version job property](./add-job.html#glue-version-table).

Follow these steps to install Python and to be able to invoke the AWS Glue APIs.

If you don't already have Python installed, download and install it from the [Python.org download page](https://www.python.org/downloads/).

Install the AWS Command Line Interface (AWS CLI) as documented in the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/installing.html).

The AWS CLI is not directly necessary for using Python. However, installing and configuring it is a convenient way to set up AWS with your account credentials and verify that they work.

Install the AWS SDK for Python (Boto 3), as documented in the [Boto3
          Quickstart](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
        .

Boto 3 resource APIs are not yet available for AWS Glue. Currently, only the Boto 3 client APIs can be used.

For more information about Boto 3, see [AWS SDK for Python (Boto3) Getting Started](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

You can find Python code examples and utilities for AWS Glue in the [AWS Glue samples repository](https://github.com/awslabs/aws-glue-samples) on the
    GitHub website.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

New-GLUEJob cmdlet creates Glue jobs via CreateJob API using DefaultArguments hashtable for Python Scala scripts.

PowerShell New-GLUEJob cmdlet creates AWS Glue jobs using Python scripts, hashtable parameters via CreateJob API.

New-GLUEJob cmdlet creates AWS Glue jobs using Python scripts, hashtable DefaultArguments, and CreateJob API parameters.

Serverless ETL pipelines, automated crawlers, visual canvas, sensitive data detection, centralized catalog management.

AWS Glue DynamicFrame enables ETL transforms, resolves choice types, relationalizes nested schemas, unnests DynamoDB JSON structures PySpark.

ETL workflows leverage Data Catalog metadata, crawlers, dynamic frames, triggers, DPU workers, visual editor transformations.