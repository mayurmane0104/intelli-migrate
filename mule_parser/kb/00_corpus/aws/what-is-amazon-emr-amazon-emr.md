# What is Amazon EMR? - Amazon EMR

**Source:** [https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html)

---

[S3 path-based access using Lake Formation for Amazon EMR Spark](https://docs.aws.amazon.com/emr/latest/ManagementGuide/lake-formation-path-based-credential-vending.html)

*12 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Amazon EMR, which was previously called Amazon Elastic MapReduce, is a managed cluster platform that
		simplifies running big data frameworks, such as [Apache Hadoop](https://aws.amazon.com/elasticmapreduce/details/hadoop) and 

If you are a first-time user of Amazon EMR, we recommend that you begin by reading the following, in addition to this section:

[Amazon EMR](https://aws.amazon.com/elasticmapreduce/) – This
				service page provides Amazon EMR highlights, product details, and pricing
				information.

[Tutorial: Getting started with Amazon EMR](./emr-gs.html) – This tutorial gets you
				started using Amazon EMR quickly.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Serverless runtime auto-manages capacity, pre-initializes workers, simplifies analytics job execution AWS resources.

Launch EMR cluster, submit PySpark job processing food inspection data, store results S3, terminate cluster.

EMR clusters cycle through lifecycle states, processing data via sequential steps across primary, core, task nodes.