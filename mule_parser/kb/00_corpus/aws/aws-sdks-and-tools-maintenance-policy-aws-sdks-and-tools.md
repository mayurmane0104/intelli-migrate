# AWS SDKs and Tools maintenance policy - AWS SDKs and Tools

**Source:** [https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html](https://docs.aws.amazon.com/sdkref/latest/guide/maint-policy.html)

---

[Enabling hybrid post-quantum TLS](https://docs.aws.amazon.com/sdkref/latest/guide/pqtls-details.html)

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

This document outlines the maintenance policy for AWS Software Development Kits (SDKs) and Tools, including Mobile and IoT SDKs, and their underlying dependencies. AWS regularly provides the AWS SDKs and Tools with updates that may contain support for new or updated AWS APIs, new features, enhancements, bug fixes, security patches, or documentation updates. Updates may also address changes with dependencies, language runtimes, and operating systems. AWS SDK releases are published to package managers (e.g. Maven, NuGet, PyPI), and are available as source code on GitHub.

We recommend users to stay up-to-date with SDK releases to keep up with the latest features, security updates, and underlying dependencies. Continued use of an unsupported SDK version is not recommended and is done at the user's discretion.

The AWS SDK release versions are in the form of X.Y.Z where X represents the major version. Increasing the major version of an SDK indicates that this SDK underwent significant and substantial changes to support new idioms and patterns in the language. Major versions are introduced when public interfaces (e.g. classes, methods, types, etc.), behaviors, or semantics have changed. Applications need to be updated in order for them to work with the newest SDK version. It is important to update major versions carefully and in accordance with the upgrade guidelines provided by AWS.

The lifecycle for major SDKs and Tools versions consists of 5 phases, which are outlined below.

*Developer Preview (Phase 0) -* During this phase, SDKs are
                    not supported, should not be used in production environments, and are meant for
                    early access and feedback purposes only. It is possible for future releases to
                    introduce breaking changes. Once AWS identifies a release to be a stable
                    product, it may mark it as a Release Candidate. Release Candidates are ready for
                    GA release unless significant bugs emerge, and will receive full AWS
                    support.

*General Availability (GA) (Phase 1) -* During this phase,
                    SDKs are fully supported. AWS will provide regular SDK releases that include
                    support for new services, API updates for existing services, as well as bug and
                    security fixes. For Tools, AWS will provide regular releases that include new
                    feature updates and bug fixes. AWS will support the GA version of an SDK for
                        *at least 24 months*.

*Maintenance Announcement (Phase 2) -* AWS will make a
                    public announcement at least 6 months before an SDK enters maintenance mode.
                    During this period, the SDK will continue to be fully supported. Typically,
                    maintenance mode is announced at the same time as the next major version is
                    transitioned to GA.

*Maintenance (Phase 3) -* During the maintenance mode, AWS
                    limits SDK releases to address critical bug fixes and security issues only. An
                    SDK will not receive API updates for new or existing services, or be updated to
                    support new regions. Maintenance mode has a *default duration of 12
                        months*, unless otherwise specified.

*End-of-Support (Phase 4) -* When an SDK reaches end-of
                    support, it will no longer receive updates or releases. Previously published
                    releases will continue to be available via public package managers and the code
                    will remain on GitHub. The GitHub repository may be archived. Use of an SDK
                    which has reached end-of-support is done at the user's discretion. We recommend
                    users upgrade to the new major version.

*The following is a visual illustration of the SDK major version lifecycle.
                Please note that the timelines shown below are illustrative and not
                binding.*

Most AWS SDKs have underlying dependencies, such as language runtimes, operating systems, or third party libraries and frameworks. These dependencies are typically tied to the language community or the vendor who owns that particular component. Each community or vendor publishes their own end-of-support schedule for their product.

The following terms are used to classify underlying third party dependencies:

*Operating System (OS):* Examples include Amazon Linux AMI,
                    Amazon Linux 2, Windows 2008, Windows 2012, Windows 2016, etc.

*Language Runtime: * Examples include Java 7, Java 8,
                    Java 11, .NET Core, .NET Standard, .NET PCL, etc.

*Third party Library / Framework:* Examples include
                    OpenSSL, .NET Framework 4.5, Java EE, etc.

Our policy is to continue supporting SDK dependencies for at least 6 months after the community or vendor ends support for the dependency. This policy, however, could vary depending on the specific dependency.

AWS reserves the right to stop support for an underlying dependency without increasing the major SDK version

Maintenance announcements are communicated in several ways:

An email announcement is sent to affected accounts, announcing our plans to end support for the specific SDK version. The email will outline the path to end-of-support, specify the campaign timelines, and provide upgrade guidance.

AWS SDK documentation, such as API reference documentation, user guides, SDK product marketing pages, and GitHub readme(s) are updated to indicate the campaign timeline and provide guidance on upgrading affected applications.

An AWS blog post is published that outlines the path to end-of-support, as well as reiterates the campaign timelines.

Deprecation warnings are added to the SDKs, outlining the path to end-of-support and linking to the SDK documentation.

To see the list of available major versions of AWS SDKs and Tools and where they are
            in their maintenance lifecycle, see [AWS SDKs and Tools version lifecycle](./version-support-matrix.html).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.