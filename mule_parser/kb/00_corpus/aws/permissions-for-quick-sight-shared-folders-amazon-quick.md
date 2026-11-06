# Permissions for Quick Sight shared folders - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/folders-security.html](https://docs.aws.amazon.com/quick/latest/userguide/folders-security.html)

---

Shared folders have three permission levels. To set folder-level permissions for a
            user or group, see [Create and manage membership permissions for Quick Sight shared folders](./sharing-folders.html).

- 
                **Owners**- The folder*owner*owns everything (folders, analyses, dashboards, datasets, data sources, topics) inside of the folder. They can create, edit, and delete the assets in the folder, modify permissions on the folder and its assets, and delete the folder entirely. The owner role is not supported for restricted shared folders.
- 
                **Contributors**- A*contributor*can create, edit, and delete assets in a folder just like an owner. They can't delete the folder or modify permissions on the folder or on assets where they have contributor access that they inherited from the folder.
- 
                **Viewers**- A*viewer*can only view the assets (folders, dashboards, datasets, data sources, topics) in the folder. A viewer can't edit or share those assets.

The following rules also apply to security for shared folders:

- 
                Quick readers' sharing status for a folder gets shared with the folder. However, a reader gets only read access to folders, and only dashboard access to visuals. 
- 
                AWS security is enforced on every object within a folder. The folder applies the same type of security to the assets of whoever the folder is shared with according to their access level (admin, author, or reader). 
- 
                The *top-level folder*is the root folder of any subfolders. When a subfolder is shared at any level, the person whom the folder was shared with sees the root folder in the top-level folders view.
- 
                The folder permission is the permission on the current folder, combined with permissions of all the folders leading to the root folder. 
- 
                A *shared asset*inherits its permission from the folder. A shared asset is created when an asset that belongs to the folder owner is added to a shared folder.
- 
                If you own an unrestricted shared folder, you can transfer ownership of the folder to another Quick admin. 
- 
                The owner role is not supported for restricted folders. The contributor role is assigned to authors that create and edit assets within the restricted folders. Folder contributors can't manage the permissions of the restricted folder or its assets. 
- 
                The correct IAM permissions are required to update the permissions of a restricted shared folder with the `UpdateFolderPermissions`API.

To create and manage permissions of a shared folder, see [Create and manage membership permissions for Quick Sight shared folders](./sharing-folders.html).