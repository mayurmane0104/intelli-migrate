# Creating Quick Sight scaled folders with the Quick Sight APIs - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/folders-scaled.html](https://docs.aws.amazon.com/quick/latest/userguide/folders-scaled.html)

---

You can use the Amazon Quick Sight APIs to create special scaled folders that can be shared with
            up to 3000 namespaces. Each namespace that is added to a folder can contain up to 100
            principals. A *principal* is a user or a group of users. After you
            create a scaled folder and add the principals that you want, any QuickSight asset can be
            added to the folder. It can then be shared to every principal in the namespaces that the
            folder principals are assigned to. This streamlines the process to share Quick Sight
            assets with thousands of users.

Scaled folders can only be created with the Quick Sight APIs. When you create a
            scaled folder, you can share the folder with up to 100 principals that are in the same
            namespace. You can add principals that belong to a different namespace with an
                `UpdateFolderPermissions` API call. After the folder is created, you can
            add and remove assets from the folder with the Quick Sight APIs or the
            Quick console.

Each Amazon Quick Sight account holds up 100 scaled folders. You can add up to 100 assets to a
            scaled folder. If you want to share a scaled folder with more than 3000 namespaces,
            contact [AWS support](https://aws.amazon.com/contact-us/).

## Examples

            The following examples show how to create a scaled folder with the Quick Sight APIs.

**Prerequisites**

Before you begin, verify that you have an AWS Identity and Access Management role that grants the API user access to call the Quick Sight API operations. The following example shows an IAM policy that you can add to an existing IAM role to create, delete, or modify a scaled folder. With the sample policy, users can add dashboards, analyses, and datasets to a scaled folder.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Action": [ "quicksight:CreateFolder", "quicksight:CreateFolderMembership", "quicksight:DeleteFolderMembership", "quicksight:DeleteFolder", "quicksight:DescribeFolderPermissions", "quicksight:DescribeFolderResolvedPermissions", "quicksight:UpdateFolderPermissions", "quicksight:UpdateDashboardPermissions", "quicksight:UpdateAnalysisPermissions", "quicksight:UpdateDataSetPermissions" ], "Resource": "*" } ] }`

The following example creates a scaled folder.

`aws quicksight create-folder \ --aws-account-id "``AWSACCOUNTID`" \ --region "`us-east-1`" \ --name "`eastcoast-users`" \ --sharing-model "`NAMESPACE`" \ --folder-id "`eastcoast-users`"

After you create a scaled folder, share the folder with a principal in your account. You can only grant or revoke permissions to users and groups that are within the same namespace in each API call. The following example shares a scaled folder with a user in the same account that the folder exists in.

```
aws quicksight update-folder-permissions \
--aws-account-id "
```
`AWSACCOUNTID`" \
--region "`us-east-1`" \
--folder-id "`eastcoast-users`" \
--grant-permissions \
    '[
        {"Actions":
            ["quicksight:DescribeFolder",
            "quicksight:UpdateFolder",
            "quicksight:DeleteFolder",
            "quicksight:DescribeFolderPermissions",
            "quicksight:UpdateFolderPermissions",
            "quicksight:CreateFolderMembership",
            "quicksight:DeleteFolderMembership",
            "quicksight:CreateFolder"
            ],
        "Principal":"arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:user/default/`my-user`"
        }
    ]'After you share the folder with a new principal, validate the new folder
                permissions with a `describe-folder-permissions` API call.

`aws quicksight describe-folder-permissions \ --aws-account-id "``AWSACCOUNTID`" \ --region "`us-east-1`" \ --folder-id "`eastcoast-users`" \ --namespace "`default`"

After you validate the new folder permissions, create a subfolder within the scaled folder. The subfolder inherits the permissions of the scaled folder that it's created in.

`aws quicksight create-folder \ --aws-account-id "``AWSACCOUNTID`" \ --region "`us-east-1`" \ --name "`new-york-users`" \ --sharing-model "`NAMESPACE`" \ --folder-id "`new-york-users`" \ --parent-folder-arn "arn:aws:quicksight:`us-east-1`:`AWSACCOUNTID`:folder/`eastcoast-users`"

The following example validates the inherited permissions of the new subfolder.

`aws quicksight describe-folder-resolved-permissions \ --aws-account-id "``AWSACCOUNTID`" \ --region "`us-east-1`" \ --folder-id "`new-york-users`" \ --namespace "`default`"

After you validate the permissions of the subfolder, add the Quick Sight asset that you want to share to the folder. After you add the asset to the subfolder, the asset is shared with every principal that the subfolder is shared with. The following example adds a dashboard to a subfolder.

```
aws quicksight create-folder-membership \
--aws-account-id "
```
`AWSACCOUNTID`" \
--folder-id "`new-york-users`" \
--member-id "`my-dashboard`" \
--member-type "`DASHBOARD`" \
--region "`us-east-1`"