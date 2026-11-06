# Sync reports and observability - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sync-reports-observability.html](https://docs.aws.amazon.com/quick/latest/userguide/sync-reports-observability.html)

---

With Amazon Quick, you can view sync schedules, sync activity logs, and detailed sync reports for every knowledge base. If your knowledge base has document-level access control (ACL) enabled, you can also verify individual document permissions.

## Sync schedules and activity

        To view sync schedules and activity, open a knowledge base and choose the
            **Sync schedules** tab.

- Sync schedule
- 
                    Displays the configured sync frequency and timing. The table shows the occurrence (for example, Daily), the start time for the next scheduled sync, and the email notification status. You can add or modify sync schedules. To receive email notifications for sync failures, turn on **Email on sync failure**.
- Sync activity
- 
                    Displays a historical log of all past syncs. You can filter by time frame (for example, Last 90 days) and sync status (for example, All, Completed, Failed). 

The following table describes the sync activity columns:

| Column | Description | 
|---|---|
| Start time | The date and time the sync began. | 
| Sync status | The outcome of the sync: Queued (waiting to run), Completed (all items processed), Completed with issues (some items were skipped or failed), or Failed. | 
| Duration | How long the sync took to complete. | 
| Total items scanned | The number of items processed during the sync. | 
| Type | Whether the sync was Scheduled (automatic) or Manual
                            (initiated by choosing the Sync nowbutton). | 
| Sync report | A View reportlink that opens the detailed sync report
                            for that run. | 

###### Tip

To start a sync on demand, choose **Sync now** on the
                knowledge base detail page.

## Review sync reports

        To view detailed results for a specific sync, open a knowledge base and
            choose the **Sync reports** tab.

Use the **Select sync** dropdown to choose the sync run
            you want to inspect.

### Overview

The overview section provides a summary of the selected sync. The following table describes the overview fields:

| Field | Description | 
|---|---|
| Sync status | The overall outcome (for example, Completed, Completed with issues). | 
| Sync type | Whether the sync was Scheduled or Manual. | 
| Sync duration | Total time elapsed for the sync. | 
| Sync start time | When the sync began. | 
| Sync end time | When the sync finished. | 

### Sync items

The sync items section shows all items that were processed during the sync, organized into the following categories:

- Available items
- 
                        Items that are present and indexed in the knowledge base after the sync: - 
                                **Unmodified**– Items already indexed that have not changed since the last sync.
- 
                                **Modified**– Previously indexed items that were updated and re-indexed.
- 
                                **Added**– New items indexed for the first time.
 
- 
                                
- Unavailable items
- 
                        Items that are not available in the knowledge base after the sync: - 
                                **Skipped**– Items filtered out (for example, empty files, unsupported formats, or items outside the date filter range).
- 
                                **Failed**– Items that could not be processed because of an error.
- 
                                **Deleted**– Items previously indexed that have been removed from the source.
 
- 
                                

### Filter and inspect individual items

The **All items** tab displays the complete list of
                items that were processed during the sync. You can narrow the results by using the
                following filters:

| Filter | Description | 
|---|---|
| Filter by status | Filter items by their sync status (for example, Added, Modified, Unmodified, Skipped, Failed, Deleted). | 
| Filter by error type | Filter failed or skipped items by their specific error type. | 
| Filter by item title | Search for a specific item by name. | 

After you set your filters, choose **Apply
                    filters** to update the results.

The following table describes the sync item columns:

| Column | Description | 
|---|---|
| Item Title | The name of the file, page, or item. | 
| Item Status | The sync status for this item. | 
| Error type | The category of error, if applicable. | 
| Error message | A detailed description of why the item failed or was skipped. | 

### Download report

To export the full sync results for offline analysis, choose
                **Download detailed report (.csv)** in the Sync items section. The CSV file includes all items with
                their status, error type, and error message.

## Check document access (ACL verification)

        If your knowledge base has document-level access control (ACL) enabled, you can verify whether a specific user has access to a particular document. Use this feature to troubleshoot when users cannot see documents that you expect them to access, or to confirm that sensitive documents are properly restricted.

###### Note

ACL verification is available for admin-managed SharePoint and Google Drive knowledge bases with ACL management enabled. Amazon S3 knowledge bases with document-level ACLs are not included in this feature. Because the ACL configuration files are customer-managed, you can verify them directly in Amazon S3.

- 
                Open the knowledge base and choose the **Sync reports**tab.
- 
                In the sync items list, choose the actions menu ( **⋮**) for an item.
- 
                Choose **View Access Details**.

The **Access Details** panel shows:

- 
                The document name, status, and last synced timestamp. 
- 
                **Permission Checker**– Enter a user's email address and choose**Check Access**to verify whether that user can access the document.
- 
                **Users and group membership**– Lists all users and groups with access to the document.

The following table describes the permission checker results:

| Result | Meaning | 
|---|---|
| User has access | The user's identity matches the document's ACL. They see this document in Quick responses. | 
| [user] does not have access to this document | The user is not in the document's ACL. Quick does not surface this document for them. | 
| No access control list found | The ACL was not crawled for this document. Either ACL management is not enabled, or the required permissions are not configured correctly. | 

If you see "No access control list found", take the following steps:

- 
                Verify that ACL management is enabled in the knowledge base settings. 
- 
                Confirm the app registration has the required ACL permissions for your data source. 
- 
                Run a full sync after you fix the permissions.