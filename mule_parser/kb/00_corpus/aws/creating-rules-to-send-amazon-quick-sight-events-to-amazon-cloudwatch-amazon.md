# Creating rules to send Amazon Quick Sight events to Amazon CloudWatch - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/events-send-cloudwatch.html](https://docs.aws.amazon.com/quick/latest/userguide/events-send-cloudwatch.html)

---

You can write simple rules to indicate which Amazon Quick Sight events interest you and which
            automated actions to take when an event matches a rule. For example, you can configure
            Amazon Quick Sight to send events to Amazon CloudWatch whenever a Amazon Quick Sight asset is placed in a folder. For
            more information, see the [Amazon EventBridge user
            guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

- Sign in to the AWS Management Console and open the CloudWatch console at - [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).
- 
                Under **Events**in the navigation pane, choose**Rules**.
- 
                Choose **Create rule**.
- 
                Enter a name and description for the rule. The rule name must be unique within this Region. For example, enter `QuickSightAssetChangeRuleCloudWatch`.
- 
                Choose **default**Event bus.
- 
                Choose **Rule with an event pattern**, and then choose**Next**.
- 
                For **Event source**, choose**AWS events or EventBridge partner events**.
- 
                In the **Creation method**section, choose**Custom pattern (JSON editor)**.
- 
                In the **Event pattern**text box, enter the following snippet and choose**Next**.`{ "source": ["aws.quicksight"] }`Alternatively, you can create the rule that only subscribes to a subset of event types in Amazon Quick Sight. For example, the following rule will only triggered when an asset is added to or removed from a folder with id `77e307e8-b41b-472a-90e8-fe3f471537be`.`{ "source": ["aws.quicksight"], "detail-type": ["QuickSight Folder Membership Updated"], "detail": { "folderId": "77e307e8-b41b-472a-90e8-fe3f471537be" } }`
- 
                For **Targets**, choose**AWS service**>**CloudWatch log group.**
- 
                Choose from an existing log group or create a new one by entering a new log group name. 
- 
                Optionally, you can add another target for this rule. 
- 
                In **Configure tags**, choose**Next**.
- 
                Choose **Create rule**.

For more information, see [Creating Amazon EventBridge rule that
                reacts To events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the Amazon EventBridge user guide.