# Turning off public sharing settings - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-anyone-no-share.html](https://docs.aws.amazon.com/quick/latest/userguide/share-a-dashboard-grant-access-anyone-no-share.html)

---

You can turn off public sharing settings for dashboards at anytime. You can turn off public sharing for an individual dashboard, or for all dashboards in your account. Visual sharing settings are determined at the dashboard level. If you turn off public sharing settings to a dashboard that holds a visual that you are embedding, users won't be able to access the visual.

The following table describes the different scenarios for when a dashboard is publicly available.

| Account-level public setting | Dashboard-level public setting | Public access | Visual indicators | 
|---|---|---|---|
| Off | Off | Off | None | 
| On | Off | Off | None | 
| On | On | Yes | An orange badge appears on the dashboard and an eye
											icon appears on the dashboard in the
												 | 
| Off | On | No | A grey badge appears on the dashboard and an eye icon
											with a slash appears on the dashboard in the
												 | 

###### To turn off public sharing for a single dashboard

- 
							In Amazon Quick, open the published dashboard that you no longer want to share. You must be the owner or a co-owner of the dashboard. 
- 
							In the published dashboard, choose the **Share**icon at upper-right, and then choose**Share dashboard**.
- 
							In the **Share dashboard**page that opens, toggle off the**Anyone on the internet (public)**switch in the**Enable access for**section at bottom-left.This action will remove public access to the dashboard. It will now only be accessible to users that it has been shared with. 

###### To turn off public sharing settings for all dashboards in a Quick user account

- 
							From the Amazon Quick start page, choose your user icon at upper right of your browser window, and then choose **Manage Quick**.
- 
							In the page that opens, scroll down to the **Permissions**section.
- 
							Choose **Public access to dashboards**at left.
- 
							On the page that opens, toggle off the **Anyone on the internet**switch.When you disable public sharing settings from the **Public sharing**menu, a pop-up will appear asking you to confirm your choice. Select**I have read and acknowledge this change**and then choose**Confirm**to confirm your choice.This action will remove public access to every dashboard on your account. Dashboards that were visible to anyone on the internet will now only be accessible to users that each dashboard has been shared with. Individual dashboards that have their public settings turned on will have a gray badge and the eye icon that appears on the **Dashboards**page will have a strike through it to indicate that the account level public settings are disabled and that the dashboard can't be viewed. It can take up to two minutes for a dashboard's public access to be revoked.

If your session capacity pricing subscription has expired, public sharing settings will be automatically removed across your account. Renew your subscription to restore access to public sharing settings.