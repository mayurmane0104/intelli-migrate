# What is IPAM? - Amazon Virtual Private Cloud

**Source:** [https://docs.aws.amazon.com/vpc/latest/ipam/index.html](https://docs.aws.amazon.com/vpc/latest/ipam/index.html)

---

[Modify an IPAM pool allocation](https://docs.aws.amazon.com/vpc/latest/ipam/modify-alloc-ipam.html)

*19 May 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

Amazon VPC IP Address Manager (IPAM) is a VPC feature that makes it easier for you to plan, track, and monitor IP addresses for your AWS workloads. You can use IPAM automated workflows to more efficiently manage IP addresses.

You can use IPAM to do the following:

Organize IP address space into routing and security domains

Monitor IP address space that's in use and monitor resources that are using space against business rules

View the history of IP address assignments in your organization

Automatically allocate CIDRs to VPCs using specific business rules

Troubleshoot network connectivity issues

Enable cross-region and cross-account sharing of your Bring Your Own IP (BYOIP) addresses

Provision Amazon-provided contiguous IPv6 CIDR blocks to pools for VPC creation

This guide consists of the following sections:

[How IPAM works](./how-it-works-ipam.html): IPAM concepts and
                terminology.

[Getting started with IPAM](./getting-started-ipam.html): Steps to enable
                company-wide IP address management with AWS Organizations, create an IPAM, and
                plan IP address usage.

[Managing IP address space in IPAM](./managing-ip-space-ipam.html): Steps to
                manage your IPAM, scopes, pools, and allocations.

[Tracking IP address usage in IPAM](./tracking-ip-addresses-ipam.html): Steps
                to monitor and track IP address usage with IPAM.

[Tutorials for Amazon VPC IP Address Manager](./tutorials-ipam.html): Detailed step-by-step
                tutorials for creating an IPAM and pools, allocating VPC CIDRs, and bringing your
                own public IP address CIDRs to IPAM.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Configure IPAM integration: AWS Organizations, external accounts, or single account setup to monitor CIDR networking resources.

Integrate IPAM with Organizations to monitor IP usage, share pools, delegate admin accounts via EnableIpamOrganizationAdminAccount API.

Launch AWS resources isolated virtual networks; configure subnets, gateways, peering, routing, IPv4/IPv6 addressing.

Public/private NAT gateways enable private subnet outbound connectivity, using Elastic IPs or VPC routing.

VPC peering enables private IP routing across accounts and Regions, supporting file sharing and geographic redundancy.