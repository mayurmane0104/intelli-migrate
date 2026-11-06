# Create and manage membership permissions for Quick Sight shared folders - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/sharing-folders.html](https://docs.aws.amazon.com/quick/latest/userguide/sharing-folders.html)

---

**Shared folders (unrestricted)**

To create a shared folder and to share the folder with one or more groups in the
            Quick console, you must be an Amazon QuickSight administrator. You can also
            create a shared folder with the `CreateFolder` API operation. Use the
            following procedure to share or modify the membership permissions of a shared
            folder.

- 
                From the left navigation, choose **Folders**then**Shared Folders**. Find the folder that you want to share or manage permissions for.
- 
                To open the actions menu for that folder's row, choose the ellipsis (three dots). 
- 
                Choose **Share**.
- 
                In the **Share folder**modal, add the groups and users with whom you want to share the contents of the folder.
- 
                For each user and group that you add, choose a permission level from the **Permissions**menu in that row.
- 
                To update the permission type for an existing user, choose **Manage folder access**.
- 
                When you're done setting user and group permissions for the folder, choose **Share**. Users are not notified that they now have access to the folder.

**Restricted shared folders**
        

Restricted shared folders can only be created with the `CreateFolder` API
            operation. The following example creates a restricted shared folder.

`aws quicksight create-folder \ --aws-account-id``AWSACCOUNTID`\ --region`us-east-1`\ --folder-id`example-folder-name`\ --folder-type RESTRICTED \ --name`"Example Folder"`\

After you create a restricted shared folder, assign folder contributor and viewer
            permissions with a `UpdateFolderPermissions` API call. The following example
            updates the permissions of a restricted shared folder to grant contributor permissions
            to a user.

`aws quicksight update-folder-permissions \ --aws-account-id``AWSACCOUNTID`\ --region`us-east-1`\ --folder-id`example-folder-name`\ --grant-permissions Principal=arn:aws:quicksight::`us-east- 1`::`AWSACCOUNTID`:user/default/:username,Actions=quicksight:CreateFolder ,quicksight:DescribeFolder, \ quicksight:CreateFolderMembership,quicksight:DeleteFolderMembership,qu icksight:DescribeFolderPermissions \

The permissions that you pass to the user depend on the type of folder role that you want to grant them. Use the following lists to determine which permissions are needed for the user that you want to grant folder access to.

###### Folder owner

- 
                quicksight:CreateFolder 
- 
                quicksight:DescribeFolder 
- 
                quicksight:UpdateFolder 
- 
                quicksight:DeleteFolder 
- 
                quicksight:CreateFolderMembership 
- 
                quicksight:DeleteFolderMembership 
- 
                quicksight:DescribeFolderPermissions 
- 
                quicksight:UpdateFolderPermissions 

###### Folder contributor

- 
                quicksight:CreateFolder 
- 
                quicksight:DescribeFolder 
- 
                quicksight:CreateFolderMembership 
- 
                quicksight:DeleteFolderMembership 
- 
                quicksight:DescribeFolderPermissions 

###### Folder viewer

- 
                quicksight:DescribeFolder 

After you create a shared folder, you can begin using the folder in Quick Sight.

You can also use the Quick Sight APIs to create special scaled folders that can be
            shared with up to 3000 namespaces. To learn more about creating a scaled folder, see
                [Creating Quick Sight scaled folders with the Quick Sight APIs](./folders-scaled.html).