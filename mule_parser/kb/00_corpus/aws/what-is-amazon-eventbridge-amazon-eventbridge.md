# What Is Amazon EventBridge? - Amazon EventBridge

**Source:** [https://docs.aws.amazon.com/eventbridge/latest/userguide/index.html](https://docs.aws.amazon.com/eventbridge/latest/userguide/index.html)

---

[Agent setup guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-agent-setup-guide.html)

*2 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. Event-driven architecture is a style of building loosely-coupled software systems that work together by emitting and responding to events. Event-driven architecture can help you boost agility and build reliable, scalable applications.

EventBridge provides simple and consistent ways to ingest, filter, transform, and deliver events so you can build applications quickly.

EventBridge includes two ways to process and deliver events: *event buses* and
      *pipes*.

[Event buses](./eb-event-bus.html) are routers that receive [events](./eb-events.html) and
      delivers them to zero or more targets. Use EventBridge to route events from sources such as home-grown applications, AWS services, and
      third-party software to consumer applications across your organization.

Event buses are well-suited for routing events from many sources to many targets, with optional transformation of events prior to delivery to a target.

[Pipes](./eb-pipes.html) EventBridge Pipes is intended for point-to-point integrations;
      each pipe receives events from a single source for processing and delivery to a single
      target. Pipes also include support for advanced transformations and enrichment of events
      prior to delivery to a target.

Pipes and event buses are often used together. A common use case is to create a pipe with an event bus as its target; the pipe sends events to the event bus, which then sends those events on to multiple targets. For example, you could create a pipe with a DynamoDB stream for a source, and an event bus as the target. The pipe receives events from the DynamoDB stream and sends them to the event bus, which then sends them on to multiple targets according to the rules you've specified on the event bus.

In addition, EventBridge provides [EventBridge Scheduler](./using-eventbridge-scheduler.html), a serverless scheduler that allows you to create, run, and manage
    tasks from one central, managed service. With EventBridge Scheduler, you can create schedules
    using cron and rate expressions for recurring patterns, or configure one-time invocations. You
    can set up flexible time windows for delivery, define retry limits, and set the maximum
    retention time for failed API invocations.

To get started with AWS, you need an AWS account. For  information about creating an AWS account, see 
    [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) 
    in the *AWS Account Management Reference Guide*.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

AWS CLI examples demonstrate creating, deleting, listing, tagging, updating, managing EventBridge Pipes.

EventBridge Pipes connect SQS queues to AWS services, enabling point-to-point integrations with filtering, enrichment, transformations.

AWS CLI examples demonstrate creating, managing, tagging, listing EventBridge Pipes with SQS source and CloudWatch targets.

Legacy scheduled rules use cron rate expressions; migrate EventBridge Scheduler scalable target management.

Filter events using patterns matching source, type, attributes; prevent infinite loops; test via Sandbox.

AWS services generate EventBridge events sent default event bus; JSON structure defines top-level fields.