# Using Quick action connectors in dashboard visuals - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/action-connectors-in-dashboard-visuals.html](https://docs.aws.amazon.com/quick/latest/userguide/action-connectors-in-dashboard-visuals.html)

---

## Prerequisites

			
			
			Before you begin, make sure to 
				[create at least one action connector](./builtin-services-integration.html).

The connector must meet these requirements:

- 
					Uses the **User Auth**authentication method
- 
					Uses one of the following integrations: - 
							Atlassian Jira Cloud 
- 
							Microsoft Outlook 
- 
							Microsoft Teams 
- 
							Salesforce 
- 
							ServiceNow 
- 
							Slack 
 
- 
							

## Enable Quick actions on a dashboard to use action connectors

			
			
			###### To enable Quick actions on a dashboard to use action connectors

- 
					If a dashboard exists, go to the source analysis of the dashboard. Otherwise, [create a new analysis](./quickstart-createanalysis.html).
- 
					Choose **Publish**.
- 
					Choose between **New Dashboard**or**Replace existing dashboard**.
- 
					Choose the **Enable Quick actions**checkbox under**Dashboard options**.
- 
					Choose **Publish dashboard**.

## Use action connectors on a visual

			
			
			###### To use action connectors on a visual

- 
					Open a dashboard with the **Enable Quick actions**publishing option turned on.
- 
					Hover over a visual. 
- 
					Choose the lightening bolt icon. 
- 
					A menu appears with a list of all supported action connectors and actions. 
- 
					Choose the desired action from the list. 
- 
					If you have not used the connector before, or if your previous login credentials have expired, an authentication modal will appear. Log in with appropriate credentials for your organization. 
- 
					An **Action**form appears in the right pane.
- 
					Enter all the information you need to include with the action. 
- 
					Some fields allow the inclusion of autofill values. Choose **Autofill**to open the menu. Choose the values you need and they will be added to your entered text.- 
							**Today’s date**: Injects today’s date
- 
							**Visual name**: Injects visual name
- 
							**All**: Injects both of the above
 
- 
							
- 
					Some actions support the ability to include an attachment. You can optionally attach an image of the visual with these actions by selecting the **Visual image**checkbox.
- 
					Select the action button at the bottom of the form to invoke the action. 

## Security and customizations

			
			
			**Custom Permissions/Capability Customization**

- **Actions**capability: You cannot see or use actions if your user or role is restricted the permission to use the Actions capability

To learn more about custom permissions, see 
				[Creating a custom permissions profile in Amazon Quick](./create-custom-permissions-profile.html).

**Row Level Security (RLS) / Column Level Security (CLS)**

- You cannot see or use actions on visuals that are based on datasets that use RLS or CLS. 

To learn more about RLS, see 
				[Using row-level security in Amazon Quick](./row-level-security.html).

To learn more about CLS, see 
				[Using column-level security to restrict access to a dataset](./row-level-security.html).

**Dashboard publishing options**

- 
					Enable Quick actions - You cannot see or use actions on any visuals of a dashboard that was published with the - **Enable Quick actions**publishing option disabled.
 

To learn more about dashboard publishing options, see 
				[Publishing dashboards](./creating-a-dashboard.html).

## Limitations

			
			
			**Visual Image attachment support**

The following visual types do not support image attachments:

- 
					High charts (when HTML is used) 
- 
					ML Insights (when HTML is used) 
- 
					Textbox and insights (when HTML is used) 
- 
					Custom content 

###### Note

For these visuals, the **Visual image** checkbox will not appear on the UI.