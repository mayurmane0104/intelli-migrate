# Approval review - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/approval-review.html](https://docs.aws.amazon.com/quick/latest/userguide/approval-review.html)

---

When approval review is enabled, users must submit their flows for review before they can be shared. This gives administrators oversight of what flows are available in the organization.

## How approvals work

            When approval review is enabled, sharing a flow follows a three-stage cycle:

- **Submitted**— The flow is waiting for review. You can view it and check the status, but cannot edit it. You can withdraw the request if needed.
- **Rejected**— The flow was not approved. You can view the reviewer's feedback, update your draft, and resubmit.
- **Approved**— The flow is shared with your intended audience. Any future changes require a new approval cycle.

## Who can review flows

            Users with Amazon Quick Enterprise subscriptions (Author Pro or Admin Pro roles) can review and approve flows. Users with Amazon Quick Professional subscriptions cannot review flows.

Reviewers can:

- View all submitted flows in the - **Pending approval**tab
- Approve or reject flows individually or in bulk 
- Provide feedback when rejecting a flow 

## Submitting a flow for approval

            - Complete and test your flow. 
- Choose - **Share**and specify who should have access.
- Choose - **Submit for review**.
- Monitor the approval status in the - **Pending approval**tab.

If your flow is rejected, review the feedback, update your draft, and resubmit.

## Enabling and disabling approval review

            Administrators control approval review through the Custom Permissions page.

**When enabled:**

- All future flow sharing requires approval. 
- Existing shared flows remain accessible. 
- Users can still create and edit flows in draft mode. 

**When disabled:**

- All pending approval requests are automatically rejected. 
- Users can share flows immediately without approval. 
- Previously approved flows remain shared. 

## Approval states reference

            | State | Can edit? | Visible to users? | Available actions | 
|---|---|---|---|
| Draft | Yes | No | Submit for approval | 
| Submitted | No | No | View status, withdraw request | 
| Rejected | Yes | No | Update and resubmit | 
| Approved | No | Yes | Create new draft for changes |