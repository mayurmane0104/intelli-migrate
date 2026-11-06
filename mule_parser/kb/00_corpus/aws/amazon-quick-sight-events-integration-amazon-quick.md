# Amazon Quick Sight events integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/events-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/events-integration.html)

---

With Amazon EventBridge, you can respond automatically to events in Amazon Quick Sight such as new dashboard creation or updates. These events are delivered to EventBridge in near real time. As a developer, you can write simple rules to indicate which events are of interest, and what actions to take when an event matches a rule. By using events, you can complete use cases such as continuous backup and deployment.

###### Topics

## Supported events

        Amazon Quick Sight currently supports the following events.

| Asset type | Action | Event detail type | Event detail | 
|---|---|---|---|
| Dashboard | Create | Amazon Quick Sight Dashboard Creation Successful |  | 
| Dashboard | Create | Amazon Quick Sight Dashboard Creation Failed |  | 
| Dashboard | Create | Amazon Quick Sight Dashboard Permissons Updated |  | 
| Dashboard | Update | Amazon Quick Sight Dashboard Update Successful |  | 
| Dashboard | Update | Amazon Quick Sight Dashboard Update Failed |  | 
| Dashboard | Update | Amazon Quick Sight Dashboard Permissons Updated |  | 
| Dashboard | Publish | Amazon Quick Sight Dashboard Published Version Updated |  | 
| Dashboard | Delete | Amazon Quick Sight Dashboard Deleted |  | 
| Analysis | Create | Amazon Quick Sight Analysis Creation Successful |  | 
| Analysis | Create | Amazon Quick Sight Analysis Creation Failed |  | 
| Analysis | Create | Amazon Quick Sight Analysis Permissons Updated |  | 
| Analysis | Delete | Amazon Quick Sight Analysis Deleted |  | 
| Analysis | Update | Amazon Quick Sight Analysis update successful |  | 
| Analysis | Update | Amazon Quick Sight Analysis update failed |  | 
| Analysis | Update | Amazon Quick Sight Analysis Permissons Updated |  | 
| VPC connection | Create | Amazon Quick Sight VPC Connection Creation Successful |  | 
| VPC connection | Create | Amazon Quick Sight VPC Connection Creation Failed |  | 
| VPC connection | Update | Amazon Quick Sight VPC Connection Update Successful |  | 
| VPC connection | Update | Amazon Quick Sight VPC Connection Update Failed |  | 
| VPC connection | Delete | Amazon Quick Sight VPC Connection Deletion Successful |  | 
| VPC connection | Delete | Amazon Quick Sight VPC Connection Deletion Failed |  | 
| Folder | Create | Amazon Quick Sight Folder Created |  | 
| Folder | Create | Amazon Quick Sight Folder Permissions Updated |  | 
| Folder | Update | Amazon Quick Sight Folder Updated |  | 
| Folder | Update | Amazon Quick Sight Folder Permissions Updated |  | 
| Folder | Delete | Amazon Quick Sight Folder Deleted |  | 
| Folder | Membership update | Amazon Quick Sight Folder Membership Updated |  | 
| Dataset | Create | Amazon Quick Sight Dataset Created |  | 
| Dataset | Create | Amazon Quick Sight Dataset Permissions Updated |  | 
| Dataset | Update | Amazon Quick Sight Dataset Updated |  | 
| Dataset | Update | Amazon Quick Sight Dataset Permissions Updated |  | 
| Dataset | Delete | Amazon Quick Sight Dataset Deleted |  | 
| DataSource | Create | Amazon Quick Sight DataSource Creation Successful |  | 
| DataSource | Create | Amazon Quick Sight DataSource Creation Failed |  | 
| DataSource | Create | Amazon Quick Sight DataSource Permissions Updated |  | 
| DataSource | Update | Amazon Quick Sight DataSource Update Successful |  | 
| DataSource | Update | Amazon Quick Sight DataSource Update Failed |  | 
| DataSource | Update | Amazon Quick Sight DataSource Permissions Updated |  | 
| DataSource | Delete | Amazon Quick Sight DataSource Deleted |  | 
| Theme | Create | Amazon Quick Sight Theme Creation Successful |  | 
| Theme | Create | Amazon Quick Sight Theme Creation Failed |  | 
| Theme | Create | Amazon Quick Sight Theme Permissions Updated |  | 
| Theme | Update | Amazon Quick Sight Theme Update Successful |  | 
| Theme | Update | Amazon Quick Sight Theme Update Failed |  | 
| Theme | Update | Amazon Quick Sight Theme Permissions Updated |  | 
| Theme | Delete | Amazon Quick Sight Theme deleted |  | 
| Theme | Alias Create | Amazon Quick Sight Theme Alias Created |  | 
| Theme | Alias Update | Amazon Quick Sight Alias Updated |  | 
| Theme | Alias Delete | Amazon Quick Sight Theme Alias Deleted |  | 

## Example event payload

        All events follow the standard EventBridge [object
            structure](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-events-structure.html). The detail field is a JSON object that contains more information
            about the event.

```
{
  "version": "0",
  "id": "3acb26c8-397c-4c89-a80a-ce672a864c55",
  "detail-type": "QuickSight Dashboard Creation Successful",
  "source": "aws.quicksight",
  "account": "123456789012",
  "time": "2023-10-30T22:06:31Z",
  "region": "us-east-1",
  "resources": ["arn:aws:quicksight:us-east-1:123456789012:dashboard/6fdbc328-ebbd-457f-aa02-9780173afc83"],
  "detail": {
    "dashboardId": "6fdbc328-ebbd-457f-aa02-9780173afc83",
    "versionNumber": 1
  }
}
```