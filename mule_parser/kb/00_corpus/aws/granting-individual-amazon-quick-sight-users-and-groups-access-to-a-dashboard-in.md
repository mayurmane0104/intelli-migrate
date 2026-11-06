# Granting individual Amazon Quick Sight users and groups access to a dashboard in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-users.html](https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-users.html)

---

Use the following procedure to grant access to a dashboard.

###### To grant users or groups access to a dashboard

- 
						Open the published dashboard and choose **Share**at upper right. Then choose**Share dashboard**.
- 
						In the **Share dashboard**page that opens, do the following:- 
								For **Invite users and groups to dashboard**at left, enter a user email or group name in the search box.Any users or groups that match your query appear in a list below the search box. Only active users and groups appear in the list. 
- 
								For the user or group that you want to grant access to the dashboard, choose **Add**. Then choose the level of permissions that you want them to have.You can select **Viewer**or**Co-owner**, depending on the user's Quick role. The available permissions for each role are as follows:- 
										**Readers**– Quick readers can only be granted**Viewer**access to dashboards. They can view, export, and print the dashboard, but they can't save the dashboard as an analysis. They can view, filter, and sort the dashboard data. They can also use any controls or custom actions that are on the dashboard. Any changes that they make to the dashboard exist only while they are viewing it, and aren't saved after they close the dashboard.
- 
										**Authors**– Quick authors can be granted**Viewer**or**Co-owner**access to dashboards.- 
												Authors with Viewer access can view, export, and print the dashboard. They can view, filter, and sort the dashboard data. They can also use any controls or custom actions that are on the dashboard. Any changes that they make to the dashboard exist only while they are viewing it, and aren't saved after they close the dashboard. However, they can save the dashboard as an analysis, unless the dashboard owner specifies otherwise. This privilege grants them read-only access to the datasets so that they can create new analyses from them. The owner has the option to provide them with the same permissions to the analysis. If the owner wants them also to edit and share the datasets, the owner can set that up inside the analysis. 
- 
												Authors with Co-owner access can view, export, and print the dashboard. They can also edit, share, and delete it. They can also save the dashboard as an analysis, unless the dashboard owner specifies otherwise. This privilege grants them read-only access to the datasets so that they can create new analyses from them. The owner has the option to provide them with the same permissions to the analysis. If the owner wants them to also edit and share the datasets, the owner can set that up inside the analysis. 
 
- 
												
- 
										**Groups**– Quick groups can only be granted**Viewer**access to dashboards. They can view, export, and print the dashboard, but they can't save the dashboard as an analysis.
 After you add a user or group to the dashboard, you can see information about them in the **Manage permissions**section, under**Users & Groups**. You can see their user name, email, permission level, and "save as" privileges.To allow a user or group to save the dashboard as an analysis, turn on **Allow "save as"**in the**Save as Analysis**column.
- 
										
- 
								To add more users to the dashboard, enter another user email or group name in the search box and repeat steps A and B. 
 
-