# Granting everyone in your Amazon Quick account access to a dashboard with the Quick Sight API - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-everyone-api.html](https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-everyone-api.html)

---

| Intended audience: Amazon Quick developers | 

Alternatively, you can grant everyone in your account access to the dashboard
					with the Quick Sight API using the `UpdateDashboardPermissions`
					operation. 

The following example API request illustrates how to do so using an AWS CLI
					command. It grants link permissions on the dashboard in your account, and allows
					the following operations: `DescribeDashboard`,
						`QueryDashboard` and `ListDashboard`.

`aws quicksight update-dashboard-permissions \ --aws-account-id``account-id`\ --region`aws-directory-region`\ --dashboard-id`dashboard-id`\ --grant-link-permissions Principal="arn:aws:quicksight:`aws-directory-region`:`account-id`:namespace/default", Actions="quicksight:DescribeDashboard, quicksight:QueryDashboard, quicksight:ListDashboardVersions"

The response for the preceding request looks similar to the following.

```
{
		"Status": 200,
		"DashboardArn": "arn:aws:quicksight:AWSDIRECTORYREGION:ACCOUNTID:dashboard/
		DASHBOARDID",
		"DashboardId": "DASHBOARDID",
		"LinkSharingConfiguration": {
			"Permissions": [
				{
					"Actions": [
						"quicksight:DescribeDashboard",
						"quicksight:ListDashboardVersions",
						"quicksight:QueryDashboard"
					],
					"Principal": "arn:aws:quicksight:AWSDIRECTORYREGION:ACCOUNTID:namespace/default"
				}
			]
		},
		"Permissions": [
			// other dashboard permissions here
		],
		"RequestId": "REQUESTID"
	}
```
You can also prevent all users in your account from accessing the dashboard using the same API operation. The following example request illustrates how by using a CLI command.

`aws quicksight update-dashboard-permissions \ --aws-account-id``account-id`\ --region`aws-directory-region`\ --dashboard-id`dashboard-id`\ --revoke-link-permissions Principal="arn:aws:quicksight:`aws-directory-region`:`account-id`:namespace/default", Actions="quicksight:DescribeDashboard, quicksight:QueryDashboard, quicksight:ListDashboardVersions"

For more information, see [UpdateDashboardPermissions](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateDashboardPermissions.html) in the
						*Amazon Quick API Reference*.

When all users in a Quick user account are granted access to the
					dashboard, the following snippet is added to AWS CloudTrail log as part of the
						`eventName`
					`UpdateDashboardAccess`, and the `eventCategory`
					`Management`.

```
"linkPermissionPolicies": 
	[
		{
			"principal": "arn:aws:quicksight:AWSDIRECTORYREGION:ACCOUNTID:
							namespace/default",
			"actions": 
			[
				"quicksight:DescribeDashboard",
				"quicksight:ListDashboardVersions",
				"quicksight:QueryDashboard"
			]
		}
	]
```