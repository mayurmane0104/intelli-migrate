# What is ARC? - Amazon Application Recovery Controller (ARC)

**Source:** [https://docs.aws.amazon.com/r53recovery/latest/dg/index.html](https://docs.aws.amazon.com/r53recovery/latest/dg/index.html)

---

[Aurora provisioned scaling execution block sample policy](https://docs.aws.amazon.com/r53recovery/latest/dg/security_iam_region_switch_aurora_provisioned_scaling.html)

*3 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Amazon Application Recovery Controller (ARC) helps you prepare for and complete faster recovery for applications running on the AWS Global Cloud Infrastructure.

ARC provides the following capabilities:

*Multi-Availability Zone (AZ) recovery*, including zonal
		shift and zonal autoshift, which enable you to recover from single AZ impairments by
		temporarily shifting traffic from an impaired AZ to a healthy AZ.

*Multi-Region recovery*, which includes routing control
		and Region switch for Regional application recovery, and readiness check for application monitoring.

*Zonal shift*

You can use ARC zonal shift to quickly isolate and recover from single Availability Zone (AZ) impairments. Zonal shift temporarily shifts traffic for a supported resource away from an impaired AZ to healthy AZs in the same AWS Region. Starting a zonal shift helps your application recover quickly, for example, from a developer's bad code deployment or from an AWS impairment in a single AZ. Shifting traffic away from the impaired AZ reduces the impact for clients who are using your application in the impaired AZ.

You can start a zonal shift for any supported resource in your account in an AWS Region. Zonal shifts are manual and temporary. When you start a zonal shift, you must specify an
			(extendable) expiration of up to three days. To enable zonal shift for supported resources, refer to [Supported resources](./arc-zonal-shift.resource-types.html).

*Zonal autoshift*

ARC zonal autoshift authorizes AWS to shift traffic away from an impaired AZ for supported resources, on your behalf, to healthy AZs in the same AWS Region. AWS starts a zonal autoshift when internal telemetry indicates that there is an impairment in one AZ in an AWS Region that could potentially impact customers. The internal telemetry incorporates metrics from multiple sources, including the AWS network, and the Amazon EC2 and Elastic Load Balancing services.

Zonal autoshifts are temporary. AWS ends a zonal autoshift when the internal telemetry indicators show that there is no longer an issue or potential issue.

To learn more about these capabilities, see the following chapters:

*Region switch*

Region switch in ARC provides a centralized, automated, and observable solution for multi-Region application recovery. Region switch helps you to plan and coordinate recovery for your applications across AWS Regions, to help ensure business continuity and reduce operational overhead.

You can use Region switch to orchestrate large-scale, complex recovery tasks for your application resources, across multiple AWS account. If an AWS Region becomes impaired, the plans that you create by using Region switch can fail over or switch your resources to another Region, so that your application can continue to operate, in a healthy AWS Region.

*Routing control*

ARC's extremely reliable routing controls enable multi-Region recovery so that your applications can failover Domain Name System DNS traffic across AWS Regions.

If your application is designed to operate out of multiple AWS Regions, you can use
		ARC *routing control* to failover between Regions.
		Routing control enables you to failover traffic from an impaired AWS Region to a healthy
		AWS Region, so that you can ensure that your application maintains availability. Routing
		control includes safety rules, which help protect you from unintended outcomes by imposing
		guardrails that you define. For example, you can impose a safety rule that only one of your
		application replicas, active or standby, is enabled and in use. 

*Readiness check *

ARC readiness check continually monitors AWS resource quotas, capacity, and network routing policies, and can notify you about changes that may affect your ability to failover to a replica application and recover from Region impairment. Continual readiness checks ensure that you can maintain your multi-Region applications in a state that is scaled and configured to handle failover traffic. Readiness check is useful when you first configure ARC, and during normal application operation. Readiness check is not intended to be used in the critical path for failover during an event.

To learn more about these capabilities, see the following chapters:

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

EKS integrates ARC zonal shift, enabling traffic redirection from impaired AZs while Managed Node Groups launch nodes in healthy zones.

Active-active replication distributes data across AWS Regions, enabling low-latency reads/writes, last-writer-wins conflict resolution, near-zero RTO.

ARC zonal shift enables rapid Availability Zone impairment recovery, shifting traffic automatically via autoshift integration.