# Managing users in a Amazon Quick Free or Plus account - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/standalone-users.html](https://docs.aws.amazon.com/quick/latest/userguide/standalone-users.html)

---

In a Amazon Quick Free or Plus account, the account administrator can invite team members by email, monitor user activity, and manage pending invitations. User management is handled directly within the Amazon Quick web application through the Manage Account page.

###### Note

This section applies to Amazon Quick Free and Plus accounts created at [quick.aws.com](https://quick.aws.com). For information about managing
            users in AWS Console–based accounts, see 

[Managing user access inside Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/managing-users.html).

###### Topics

## User limits by plan

        The number of users you can have in your account depends on your plan. For
            specific user limits for each plan, see
            [Amazon Quick pricing](https://aws.amazon.com/quick/pricing/).

For more information about plans, see [Amazon Quick plans and pricing](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-plans.html).

## Navigating to user management

        ###### To access the Users page

- 
                Sign in to Amazon Quick at [quick.aws.com](https://quick.aws.com).
- 
                From the navigation panel, choose your username. 
- 
                Choose **Manage account**.
- 
                In the left navigation, choose **Users**.

The Users page displays two tabs: **Active** and
            **Invited**.

## Managing active users

        The **Active** tab displays all users who have accepted their
            invitation and are currently active in your Amazon Quick account.

### Active users table

The Active users table includes the following columns:

- 
                    **Name**– The user's display name, as set in their AWS Builder ID profile.
- 
                    **Email**– The email address associated with the user's AWS Builder ID.

You can sort the table by either column by choosing the column header. Use the
                **Search users** field to filter the list by name or email.

### Viewing user usage

You can view usage statistics for any active user.

###### To view a user's usage

- 
                    On the **Active**tab, locate the user in the table.
- 
                    In the row for that user, choose the **More options**menu.
- 
                    Choose **See usage**.A dialog opens displaying the user's usage statistics. 
- 
                    Review the usage information. When finished, choose **Close**to dismiss the dialog.

## Inviting new users

        You can invite team members to join your Amazon Quick account by sending them an email invitation. Invited users receive an email with instructions to create an AWS Builder ID (if they don't already have one) and join your Quick account.

###### Note

You can only invite users up to the maximum allowed by your plan. If you
                need to invite more users than your plan allows, consider [upgrading your plan](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-upgrade.html).

###### To invite new users

- 
                On the Users page, choose **Invite**.The Invite dialog opens. 
- 
                In the **Enter email addresses**field, type the email address of the person you want to invite.
- 
                Press **Enter**. The email address appears as a chip (bubble) in the field, confirming it has been accepted.
- 
                (Optional) Repeat the previous steps to add additional email addresses. You can also enter multiple email addresses separated by commas. 
- 
                Choose **Send invitations**.Amazon Quick sends an invitation email to each address. The invitations appear in the **Invited**tab.

###### Tip

You can invite multiple users at once by entering several email addresses
                before choosing **Send invitations**. Each email address must be
                confirmed as a chip in the field before sending.

## Managing invited users

        The **Invited** tab displays all pending invitations that have not
            yet been accepted.

### Invited users table

The Invited users table includes the following columns:

- 
                    **Email**– The email address the invitation was sent to.
- 
                    **Invitation Status**– The current status of the invitation (for example,*Pending*).

You can sort the table by either column. Use the **Search
                    invitations** field to filter the list.

### Resending or canceling invitations

You can resend an invitation if the original email was not received, or cancel an invitation to revoke access before it is accepted.

###### To resend an invitation

- 
                    On the **Invited**tab, locate the invitation in the table.
- 
                    In the row for that invitation, choose the **More options**menu.
- 
                    Choose **Resend**.Amazon Quick sends a new invitation email to the address. 

###### To cancel an invitation

- 
                    On the **Invited**tab, locate the invitation in the table.
- 
                    In the row for that invitation, choose the **More options**menu.
- 
                    Choose **Cancel**.The invitation is revoked. The recipient will no longer be able to use the invitation link to join your account. 

###### Important

Canceling an invitation does not affect users who have already accepted and
                    are active in your account. To remove an active user, use the options
                    available on the **Active** tab.