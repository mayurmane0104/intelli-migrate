# Creating and managing groups in Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/creating-quicksight-groups.html](https://docs.aws.amazon.com/quick/latest/userguide/creating-quicksight-groups.html)

---

| Intended audience: System administrators | 

| Applies
                    to:Enterprise Edition | 

###### Note

If your Amazon Quick account is integrated with IAM Identity Center (recommended), groups are not managed in the Quick application. Instead, groups are managed in IAM Identity Center or in the third-party identity provider that you configured in IAM Identity Center. Groups are synced automatically between Quick and IAM Identity Center.

Admins with IAM credentials who have access to the Quick console can
        organize sets of users into groups that make it easier to manage access and security. For
        example, you can create a group of users that you can share Amazon Quick assets with all at
        once. You can create and manage groups using the Amazon Quick console or the AWS Command Line Interface
        (AWS CLI). You can create up to 10,000 groups in a namespace. If you want to create more than
        10,000 groups in a namespace, contact [AWS
            Support](https://aws.amazon.com//contact-us/).

Use the topics below to create, and modify groups with in the Amazon Quick console or with the Amazon Quick APIs.

###### Topics

## Create a group with the Amazon Quick console

        Use the following procedure to create a group in the Quick console.

###### To create a user group in the Amazon Quick console:

- 
                On the Amazon Quick start page, choose **Manage Quick**, and then choose**Manage groups**.
- 
                Choose **NEW GROUP**.
- 
                On the **Create new group**page, enter the name and description of the new group in the corresponding boxes.
- 
                When you're finished, choose **Create**to create the new group.

###### Note

You can't delete a group from the Amazon Quick console, but you can delete a group
                with the AWS CLI. For more information on deleting a Amazon Quick group with the
                AWS CLI, see [Create and manage groups with the AWS CLI](https://docs.aws.amazon.com/quicksight/latest/user/creating-groups-cli.html).

## Change a group description with the Amazon Quick console

        After you have created a new group, you can't change the group's title but you can change the group's description.

###### To change the description of a group:

- 
                On the Amazon Quick start page, choose **Manage Quick**, and then choose**Manage groups**.
- 
                Choose the group that you want to change, and then choose the **Edit**link next to the group description.
- 
                In the **Edit description**box that appears, enter the new description and choose**Save**.

## Manage group membership in the Amazon Quick console

        After you create a group, you can add and remove users from the **Manage
                groups** page. You can't add a user to a group if you haven't added the
            user to your account. For more information on adding users to your Amazon Quick account,
            see [Managing user access inside Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/managing-users.html).

###### To add a user to a group

- 
                On the Amazon Quick start page, choose **Manage Quick**, and then choose**Manage groups**.
- 
                Choose the group that you want to add a user to, and choose **ADD USER**at the page's upper right.
- 
                Enter the user name or email of the user that you want to add, and choose the correct user for **Search users**.

###### To remove a user from a group:

- 
                On the Amazon Quick start page, choose **Manage Quick**, and then choose**Manage groups**.
- 
                Choose the group that you want to remove a user from. 
- 
                Find the user that you want to remove and choose **Remove**.

Choosing **remove** automatically removes the selected user from the
            group.

You can also search for a group member by entering the user's full user name into the search bar on the right-hand side of the group's page.

## Create and manage groups with the AWS CLI

        Before you begin, make sure that you have the AWS CLI installed. For more information,
            see [Installing
                the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) in the *AWS CLI User Guide.
            *

Use the following procedure to create an Quick user group.

- 
                Open a terminal window. If you are using Microsoft Windows, open a command prompt. 
- 
                Enter the following command at the prompt to create a group. Substitute the correct values for your parameters. `aws quicksight create-group --aws-account-id=``111122223333`--namespace=`default`--group-name="`Sales-Management`" --description="`Sales Management - Forecasting`"You might find it easier to create the command in a text editor before entering it at the prompt. For more information on `create-group`and other available commands, see the[Amazon Quick API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).
- 
                Verify that the group exists by using a command similar to one of the following. The following command lists all groups. `aws quicksight list-groups --aws-account-id``111122223333`--namespace`default`The following command describes a specific group. `aws quicksight describe-group --aws-account-id``11112222333`--namespace`default`--group-name`Sales`The following command searches for groups in a specified Amazon Quick namespace. `aws quicksight search-groups --region``us-west-2`--aws-account-id`11112222333`--namespace`default`--filters "[{\"Operator\": \"StartsWith\", \"Name\": \"GROUP_NAME\", \"Value\": \"Mar\"}]"
- 
                Add a member to the new group by using a command similar to the following. `aws quicksight create-group-membership --aws-account-id``111122223333`--namespace`default`--group-name`Sales`--member-name`Pat`The following command determines if a user is a member of a specified group. `aws quicksight describe-group-membership --region``us-west-2`--aws-account-id`11112222333`--namespace`default`--group-name`Marketing-East`--member-name`user`

Enter the following command at the prompt to delete a group. Substitute the correct values for your parameters.

`aws quicksight delete-group --aws-account-id``111122223333`--namespace`default`--group-name`Marketing-East`

You might find it easier to create the command in a text editor before entering it at
            the prompt. For more information on `delete-group` and other available
            commands, see the [Amazon Quick API
                reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).