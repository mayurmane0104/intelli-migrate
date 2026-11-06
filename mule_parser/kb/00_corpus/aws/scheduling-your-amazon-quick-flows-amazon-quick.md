# Scheduling your Amazon Quick Flows - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/schedules-in-quick-flows.html](https://docs.aws.amazon.com/quick/latest/userguide/schedules-in-quick-flows.html)

---

Schedules let you automate recurring flow runs without manual intervention. You can schedule flows you have created or flows that have been shared with you. All schedules are private to you and cannot be shared with other users.

Common uses include generating recurring reports, summarizing open items from external services, or preparing daily meeting briefings.

## Creating a schedule

        - Open your flow in Run mode. 
- Choose the scheduling icon. 
- Choose - **Create schedule**.
- Configure your schedule: - **Schedule name**— A unique name for the schedule.
- **Description**— Optional. Details about the schedule's purpose.
- **Repeat configuration**— Choose from suggestions or configure custom recurrence (daily, weekly, or monthly) with start date, optional end date, and time zone.
 
- Choose - **Next**.
- Provide default inputs for each scheduled run. 
- Choose - **Next**.
- Configure action permissions: - Turn on - **Run with no confirmation**to automatically submit action forms during scheduled runs.
- Turn off to review and confirm each action manually. 
 
- Choose - **Save**.

###### Note

Action permissions only appear if the flow contains action steps. Automatic form submission is enabled by default for write actions. User confirmation is recommended to help avoid AI prediction errors.

## Managing schedules

        You can manage schedules from two places:

- **From the flow**— Open the flow, choose the scheduling icon, and edit, pause, duplicate, view runs, or delete a schedule.
- **From the Flows library**— Choose the- **My schedules**tab to see all your schedules across all flows with their status, frequency, last run, and associated flow name.

## Schedule history

        All manual and scheduled runs appear in the flow run history. You can filter by all runs, scheduled runs, or failed runs. History is retained for 30 days.

Visual indicators help distinguish run types:

- Schedule run tag for scheduled runs 
- Orange dot for un-viewed completed runs 
- Running tag for in-progress runs 
- Failed tag for failed runs 

###### Note

You cannot view an ongoing scheduled run until it completes.

## Notifications

        You receive email notifications when:

- A scheduled run completes successfully (with a link to the results) 
- A run requires your input to continue 
- A run requires authentication for a third-party application 
- A flow with your schedules is unshared from you (schedules are archived) 
- A flow with your schedules is deleted 
- A flow with your schedules is updated with a new version (schedules continue with the updated version) 

## Authentication for action connectors

        Ensure your authentication for action connectors is current before scheduling. If authentication expires before a scheduled run, you receive an email notification. To verify, run the flow manually or visit the action connector page in Quick to sign in.