# Turn on the Dashboard Q&A experience in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/dashboard-qa.html](https://docs.aws.amazon.com/quick/latest/userguide/dashboard-qa.html)

---

Quick allows any Author to enable Q&A directly from their dashboards
            in one click without the need to create a Topic in Quick Sight. To do this, publish
            your dashboard and check the **Allow data Q&A** checkbox from the
            dashboard publishing menu. When you turn on dashboard Q&A, you can choose which
            datasets to use for dashboard Q&A to ensure that your end users get the answers they
            need.

Dashboard Q&A queries all rows and columns in the included datasets - beyond what is visible in the
            dashboard. To protect sensitive or confidential data, enable 
            [row-level security (RLS)](./row-level-security.html) and/or 
            [column-level security (CLS)](./restrict-access-to-a-data-set-using-column-level-security.html).
        

The following table compares feature availability between dashboard Q&A and topic Q&A.

| Q&A feature | Dashboard Q&A | Topic Q&A | 
|---|---|---|
| Allows users in all roles to ask and answer questions of data |  |  | 
| Allows author and admin roles to enable data Q&A on dashboards |  |  | 
| Suported in Quick console embedding |  |  | 
| Ability to add reviewed answers |  |  | 
| Ability to customize Q&A-specific metadata |  |  | 
| Ability to support autocomplete for data values |  |  | 

Use the procedure below to enable dashboard Q&A on a Quick Sight dashboard.

###### To enable dashboard Q&A on a dashboard

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                Open the analysis that the dashboard that you want to publish with Q&A enabled. 
- 
                Choose **Publish**.
- 
                Check the **Allow data Q&A**check box.
- 
                (Optional) Choose **MANAGE Q&A**to choose which datasets you want to include in the dashboard Q&A experience. By default, all datasets that are used by the dashboard are included.
- 
                Choose **APPLY CHANGES**, and then choose**Publish dashboard**.

After you publish a dashboard with the dashboard Q&A experience enabled, users can
            ask questions about their data with the **Ask a question about this
                dashboard** input at the top of the dashboard.

Quick allows any user to ask questions on dashboards that have dashboard Q&A enabled. However, dashboard Q&A is a feature that incurs the associated enablement fee. Quick admins can disable this feature at the account level at any time. Use the following procedure to disable dashboard Q&A across an entire Quick account.

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
             Choose the user icon in the top right, and then choose **Manage Quick**.
- 
             Choose **Security & permissions**.
- 
             Navigate to the Amazon Q section, and then choose **Manage**.
- 
             Toggle **Manage Dashboard Q&A**off.

When you toggle **Manage Dashboard Q&A** off, dashboard Q&A
            is removed from any dashboards that have dashboard Q&A enabled. If your
            Quick account does not have Pro users or topics, this action stops the Amazon Q
            enablement fee from billing your Quick account. This setting does not impact
            Pro users or existing topics in Quick. For more information about opting out
            of Generative BI, see [Opting out of Generative BI](./generative-bi-opt-out.html).