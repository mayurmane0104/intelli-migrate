# Consuming pixel perfect reports in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/qs-reports-consume-reports.html](https://docs.aws.amazon.com/quick/latest/userguide/qs-reports-consume-reports.html)

---

When an Amazon Quick author publishes and then sends a scheduled pixel perfect report,
            Quick will generate and save a snapshot of the report that is sent out.
            Whenever you go to view the pixel perfect report's dashboard, you will see the
            generated snapshot of the most recently sent report. If you try to view your
            report's dashboard but you haven't sent an email report yet, you are prompted to
            schedule your first report to see the dashboard snapshot. For more information on
            scheduling an email report, see [Scheduling and sending Quick Sight reports by email](./sending-reports.html).

If a Quick author has set up a prompted report for a Quick Sight
            pixel perfect report, Quick readers can use the prompt to schedule their own
            on-demand reports for themselves. For more information about reader-generated reports,
            see [Creating a reader generated report in Amazon Quick Sight](./reader-scheduling.html). For more
            information about prompts for pixel perfect reports, see [Setting up prompts for paginated reports](./paginated-reports-prompts.html).

Users can't interact with a published pixel perfect report the same way they can interact with a published interactive sheet. Unlike interactive sheets, pixel perfect reports generate static snapshots of data that is presented in groups of visuals or text boxes. These static snapshots are generated at the time that the report is sent, so that the audience can see the latest version of the data in the report. Pixel perfect reports are especially useful for generating invoices or weekly business reviews. Users can then compare the current pixel perfect reports with reports that were generated in the past to better track their business data.

## Viewing a report's snapshot history

            Every time you send out a scheduled pixel perfect report, Amazon Quick saves a copy of the generated snapshot that is sent out for your reference. You can view these snapshots at any time in the Quick console.

###### To view a report's snapshot history

- 
                    From the Quick homepage, choose **Dashboards**, and then choose the dashboard whose snapshot history you want to see.
- 
                    Choose the **Scheduling**icon in the top right toolbar, and then choose**Recent snapshots**.
- 
                    In the **Recent snapshots**pane that appears on the right, choose the snapshot to view, and then choose the download button next to the file that you want to download.