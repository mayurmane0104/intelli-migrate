# Granting everyone in your Amazon Quick Sight account access to a dashboard - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-everyone.html](https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-everyone.html)

---

Alternatively, you can share your Amazon Quick Sight dashboard with everyone in your account. When you do this, everyone in your account can access the dashboard, even if they weren't granted access individually and assigned permissions. They can access the dashboard if they have a link to it (shared by you) or if it's embedded.

Sharing the dashboard with everyone in your account doesn't affect email
					reports. For example, suppose that you choose to share the dashboard with
					everyone in your account. Suppose also that you choose **Send email
						report to all users with access to dashboard** when setting up an
					email report for the same dashboard. In this case, the email report is sent only
					to people who have access to the dashboard. They receive access either through
					someone explicitly sharing it with them, through groups, or through shared
					folders.

###### To grant everyone in your account access to a dashboard

- 
						Open the published dashboard and choose **Share**at upper right. Then choose**Share dashboard**.
- 
						In the **Share dashboard**page that opens, for**Enable access for**at bottom left, toggle on**Everyone in this account**. Accounts that sign in with an Active Directory can't access the**Everyone in this account**switch. Accounts that use Active Directory can enable this setting with an`UpdateDashboardPermissions`API call. For more information on`UpdateDashboardPermissions`, see[UpdateDashboardPermissions](https://docs.aws.amazon.com//quicksight/latest/APIReference/API_UpdateDashboardPermissions.html)in the*Amazon Quick Sight API Reference*.
- 
						(Optional) Toggle on **Discoverable in Quick Sight**.When you share a dashboard with everyone in the account, owners can also choose to make the dashboard discoverable in Quick Sight. A dashboard that's discoverable appears in everyone's list of dashboards on the **Dashboards**page. When this option is turned on, everyone in the account can see and search for the dashboard. When this option is turned off, they can only access the dashboard if they have a link or if it's embedded. The dashboard doesn't appear on the**Dashboards**page, and users can't search for it.