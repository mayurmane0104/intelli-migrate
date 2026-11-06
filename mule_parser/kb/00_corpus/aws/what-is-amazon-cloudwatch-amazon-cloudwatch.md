# What is Amazon CloudWatch? - Amazon CloudWatch

**Source:** [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/index.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/index.html)

---

[SDK and API reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/sdk-api-reference.html)

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

Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time, and offers many tools to give you system-wide observability of your application performance, operational health, and resource utilization.

[Metrics](./working_with_metrics.html) collect and track key performance data at user-defined intervals. [Many AWS services](./aws-services-cloudwatch-metrics.html)  automatically report metrics into CloudWatch, and you can also [publish
				custom metrics](./publishingMetrics.html) in CloudWatch from your applications.

[Dashboards](./CloudWatch_Dashboards.html) offer a unified view of your resources and applications with visualizations of your metrics and logs in a single location. You can also
			[share dashboards](./cloudwatch-dashboard-sharing.html) across accounts and Regions for enhanced operational awareness. CloudWatch provides [curated automatic dashboards](./GettingStarted.html) for many AWS services, 
			so that you don't have to build them yourself.

You can set up [alarms](./CloudWatch_Alarms.html) that continuously monitor CloudWatch metrics against user-defined thresholds. They can automatically alert you to breaches of the thresholds, and
			can also automatically respond to changes in your resources' behavior by [triggering automated actions](./Acting_Alarm_Changes.html).

With [Application Signals](./CloudWatch-Application-Monitoring-Sections.html)
			you can automatically detect and monitor your applications' key performance indicators like latency, error rates, and request rates without manual instrumentation or code changes. Application Signals
		also provides curated dashboards so you can begin monitoring with a minimum of setup.

[CloudWatch Synthetics](./CloudWatch_Synthetics_Canaries.html) complements this by enabling you to proactively monitor your endpoints and APIs through configurable scripts called *canaries* that simulate user behavior and alert you to availability 
			issues or performance degradation before they impact real users. You
			can also use [CloudWatch RUM](./CloudWatch-RUM.html) to gather performance data from real user sessions.

Use [Service Level Objectives (SLOs)](./CloudWatch-ServiceLevelObjectives.html) in CloudWatch to define, track, and alert on specific reliability targets for your applications, helping you maintain service quality commitments by 
			setting error budgets and monitoring SLO compliance over time.

Many AWS services automatically send basic metrics to CloudWatch for free.  [Services that send metrics are listed here](./aws-services-cloudwatch-metrics.html).  Additionally, CloudWatch provides additional monitoring capabilities 
			for several key pieces of AWS infrastructure:

[Database Insights](./Database-Insights.html) allows you to monitor database performance metrics in real time, analyze SQL query performance, and troubleshoot database load issues for 
			AWS database services.

[Lambda Insights](./Lambda-Insights.html) provides system-level metrics for Lambda functions, including memory and CPU utilization tracking, and cold start detection and analysis.

[Container Insights](./ContainerInsights.html) allows you to collect and analyze metrics from containerized applications, 
				on Amazon ECS clusters, Amazon EKS clusters, and self-managed Kubernetes clusters on Amazon EC2.

CloudWatch Logs offers a suite of powerful features for comprehensive log management and analysis. Logs ingested from AWS services and custom applications are stored in 
			[log groups and streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) for easy organization.     
			Use [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) to perform interactive, fast queries on your log data, with a choice of three query languages including SQL and PPL. 
			Use [log anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection) to find unusual patterns in log events in a log group, which can indicate issues. 
				Create [metric filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData)   to extract numerical values from logs and generate CloudWatch metrics, which you can use for alerting and dashboards. 
				Set up [subscription filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions) to process and analyze logs in real-time or route them to other services like Amazon S3 or Firehose.
			

Use the [CloudWatch agent](./Install-CloudWatch-Agent.html) to collect detailed system
			metrics about processes, CPU, memory, disk usage, and network performance from your fleets of Amazon EC2 instances and on-premises servers. 
			You can also collect and monitor custom metrics from your applications, aggregate logs from multiple sources, and configure alarms based on the collected data. 
			You can also use the agent to gather [GPU metrics](./CloudWatch-Agent-NVIDIA-GPU.html). The agent supports both Windows and Linux operating systems and can integrate with Systems Manager for centralized configuration management. 
			 

[CloudWatch cross-account observability](./CloudWatch-Cross-Account-Methods.html) lets you 
			set up a central monitoring account to monitor and troubleshoot applications that span multiple accounts. 
			From the central account, you can view metrics, logs, and traces from source 
			accounts across your organization. This centralized approach enables you to create cross-account dashboards, 
			set up alarms that watch metrics from multiple accounts, and perform root-cause analysis across account 
			boundaries. With CloudWatch cross-account observability, you can link source accounts either individually or 
			link them automatically through AWS Organizations.

Amazon CloudWatch provides native OTLP endpoints for ingesting metrics, logs, and traces
			using the OpenTelemetry standard. You can collect telemetry using any
			OpenTelemetry-compatible SDK or collector and send it directly to CloudWatch without
			proprietary agents or format conversion. CloudWatch also supports PromQL for querying
			OpenTelemetry metrics. This open-standards approach lets you use the same
			instrumentation to send data to CloudWatch and third-party destinations, and query
			application and AWS infrastructure telemetry together. For more information, see
				[OpenTelemetry](./CloudWatch-OpenTelemetry-Sections.html).

CloudWatch offers a catalog of readily available configurations to help you quickly implement monitoring for various AWS services and common workloads, such as [Java Virtual Machines (JVM)](./Solution-JVM-On-EC2.html), [NVIDIA GPU](./Solution-NVIDIA-GPU-On-EC2.html), [Apache Kafka](./Solution-Kafka-On-EC2.html), 
			[Apache Tomcat](./Solution-Tomcat-On-EC2.html), and 
			[NGINX](./Solution-NGINX-On-EC2.html). These solutions provide focused guidance, including instructions for installing and configuring the CloudWatch agent, deploying pre-defined custom dashboards, and setting up related alarms. 

CloudWatch provides comprehensive network and internet monitoring capabilities through CloudWatch Network Monitoring.

[Internet Monitor](./CloudWatch-InternetMonitor.html) uses AWS global networking data to analyze 
			internet performance and availability between your applications and end users. With an internet monitor, 
			you can identify or get notifications for increased latency or regional disruptions that impact your customers. 
			Internet monitors work by analyzing your VPC flow logs to provide automated insights about network traffic 
			patterns and performance. You can also get suggestions for how to optimize application performance for your 
			clients. 

[Network Flow Monitor](./CloudWatch-NetworkFlowMonitor.html) displays network performance 
			information gathered by lightweight software agents that you install on your instances. Using a flow monitor, 
			you can quickly visualize packet loss and latency of your network connections over a time frame that 
			you specify. Each monitor also generates a network health indicator (NHI), which tells you whether there 
			were AWS network issues for the network flows tracked by your monitor during the time period that you're 
			evaluating. 

When you connect by using Direct Connect, you can use synthetic monitors in [Network Synthetic Monitor](./what-is-network-monitor.html) to proactively monitor network connectivity 
			by running synthetic tests between a VPC and on-premises endpoints. When you create a synthetic monitor, you 
			specify probes by providing a VPC subnet and on-premises IP addresses. AWS creates and manages the 
			infrastructure in the background that is required to perform round-trip time and packet loss measurements 
			with the probes. These tests detect issues with connectivity, DNS, and latency before they impact your 
			applications, so that you can take action to improve your end users’ experience. 

For complete information about CloudWatch pricing, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/). 

For information that can help you analyze your bill and possibly optimize and reduce costs, 
			see [Analyzing, optimizing, and reducing CloudWatch costs](./cloudwatch_billing.html).

The following related resources can help you as you work with this service.

| Resource | Description | 
|---|---|
| The FAQ covers the top questions developers have asked about this product. | |
| A central starting point to find documentation, code examples, release notes, and other information to help you build innovative applications with AWS. | |
| The console allows you to perform most of the functions of Amazon CloudWatch and various other AWS offerings without programming. | |
| Community-based forum for developers to discuss technical questions related to Amazon CloudWatch. | |
| The hub for creating and managing your AWS Support cases. Also includes links to other helpful resources, such as forums, technical FAQs, service health status, and AWS Trusted Advisor. | |
| The primary web page for information about Amazon CloudWatch. | |
| A central contact point for inquiries concerning AWS billing, account, events, abuse, etc. | 

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Monitor EMR clusters via CloudWatch, Ganglia, logs, Spark History Server, YARN timeline server.

Monitor WorkSpaces via CloudWatch, EventBridge, CloudTrail, Internet Monitor, S3 logs.

Collects metrics, logs, traces from EC2, on-premises servers via StatsD, collectd, OpenTelemetry, X-Ray SDKs.

Monitor, store, access logs; query, mask sensitive data; centralize cross-account; protect retention.

JSON config file defines agent, metrics, logs, traces sections enabling custom metrics, Windows Event Log collection, cross-account IAM roles.