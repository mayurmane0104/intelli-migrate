# Manage topic permissions through dashboards in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-manage-topic-permissions.html](https://docs.aws.amazon.com/quick/latest/userguide/gen-bi-manage-topic-permissions.html)

---

Quick enables Authors to manage permissions for dashboards and their linked topics from a single location. When sharing dashboards with Q&A enabled, Authors can control topic viewer access directly from a dashboard's sharing preferences, eliminating the need to manage permissions in multiple locations.

###### To enable Q&A on a dashboard with a linked topic:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Open the analysis of the dashboard with Q&A enabled and topic linked that you want to publish. 
- 
                Choose **Publish**.
- 
                Check the **Allow data Q&A**check box.
- 
                Choose **MANAGE Q&A**and select**Use a linked topic for Build visual and Q&A**.
- 
                Select the desired linked topic from the dropdown menu. 
- 
                Choose **APPLY CHANGES**, then choose**Publish dashboard**.

###### To conveniently manage topic access from a dashboard:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Open the dashboard with a linked topic that you are a co-owner of. 
- 
                Select the share icon and choose **Share dashboard**.
- 
                In the row of your selected user, flip on/off the **Share as "topic viewer"**toggle to grant/revoke viewer access to the linked topic.
- 
                In the row of your selected shared folder, flip on/off the **Add topic to folder**toggle to add/remove the linked topic to/from the shared folder.

###### To share the dashboard and its linked topic to all users and groups:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Open the dashboard with a linked topic that you are a co-owner of. 
- 
                Select the share icon and choose **Share dashboard**.
- 
                On the bottom-left of the panel, under **Auto-share linked topic for**, flip the**All dashboard users and groups**toggle on. This will grant viewer access to the linked topic when the dashboared is shared. Flip the toggle off to cancel this behavior.

After the dashboard with a linked topic has been shared, users will immediately be
            able to ask questions about their data. Navigate to **Ask a question about
                <topic name>** at the top of the dashboard to start asking
            questions.