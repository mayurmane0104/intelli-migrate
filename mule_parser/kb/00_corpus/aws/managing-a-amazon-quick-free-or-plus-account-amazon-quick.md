# Managing a Amazon Quick Free or Plus account - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/standalone-admin.html](https://docs.aws.amazon.com/quick/latest/userguide/standalone-admin.html)

---

Amazon Quick Free and Plus accounts – created through the direct signup process at
        [quick.aws.com](https://quick.aws.com) – include a built-in
        administration interface for managing your account, users, assets, billing, and support.
        This interface is accessible directly within the Amazon Quick web application, without
        requiring access to the AWS Management Console.

###### Note

This section applies to Amazon Quick Free and Plus accounts only. If your organization
            accesses Amazon Quick through the AWS Management Console, see [Administering Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/qsysadmin.html) for information about managing your account
            using IAM, IAM Identity Center, and other AWS services.

###### Topics

## Account administration overview

        When you create a Amazon Quick Free or Plus account at quick.aws.com, the person who
            completes the signup process is automatically assigned the **administrator** role. As the account administrator, you have full access
            to all account management capabilities, including user management, asset oversight,
            plan and billing configuration, and support resources.

Free and Plus account administration is organized into the following sections:

| Section | Description | 
|---|---|
| Users | Invite team members, manage active users, view usage
                            statistics, and manage pending invitations. For more information, see [Managing users in a Amazon Quick Free or Plus
                                account](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-users.html). | 
| Assets | View and manage all account resources including chat agents,
                            spaces, automations, and built-in tools. For more information, see [Managing assets in a Amazon Quick Free or Plus
                                account](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-assets.html). | 
| Plan and billing | View your current plan, estimated charges, payment methods,
                            and billing history. Upgrade or change your plan. For more
                            information, see [Plan and billing for Amazon Quick Free and Plus
                                accounts](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-billing.html). | 
| Support | Access AWS Support resources for help with your Amazon Quick account. | 

## Accessing the Manage Account page

        ###### To access account administration

- 
                Sign in to Amazon Quick at [quick.aws.com](https://quick.aws.com).
- 
                From the navigation panel, choose your username (displayed with your initials and name). 
- 
                From the profile menu, choose **Manage account**.The Manage Account page opens, displaying an overview dashboard with a summary of your account sections. 

## Manage Account page layout

        The Manage Account page uses a left-side navigation panel with the following sections:

- 
                **Manage account**– The overview dashboard. Displays a summary card for each section, including a user count and a**Manage**link that navigates directly to the Users page.
- 
                **Users**– Manage active users and pending invitations. See[Managing users](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-users.html).
- 
                **Assets**– View and manage account resources. See[Managing assets](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-assets.html).
- 
                **Plan and billing**– Opens the plan and billing settings page in a new browser tab. See[Plan and billing](https://docs.aws.amazon.com/quicksuite/latest/userguide/standalone-billing.html).
- 
                **Support**– Opens the AWS Support portal in a new browser tab for submitting support requests.

## Free and Plus vs. AWS Console administration

        The following table summarizes the key differences between Free and Plus account administration and AWS Console–based administration.

| Feature | Free or Plus account (quick.aws.com) | AWS Console account | 
|---|---|---|
| Identity provider | Email or social login | IAM Identity Center, IAM, or federated identity | 
| Admin interface | Built-in Quick web UI (Manage Account page) | AWS Management Console | 
| User management | Email-based invitations | IAM Identity Center groups, IAM users | 
| Billing | Billing portal (account.global.app.aws) | AWS Billing and Cost Management console | 
| Plans | Free, Plus | Standard AWS subscription pricing | 
| Account creation | Automatic (AWS account created behind the scenes) | Manual AWS account setup required | 

###### Note

Regardless of how your Amazon Quick account was created, all product features – including chat, chat agents, spaces, research, automations, Amazon Quick Sight, integrations, and extensions – function identically. The differences are limited to account setup, identity management, and billing.