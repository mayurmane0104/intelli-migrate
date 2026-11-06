# WorkSpaces examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_workspaces_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_workspaces_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with WorkSpaces.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-tags`.

- **AWS CLI**
- 
            
                    **To add tags to a WorkSpace**The following `create-tags`example adds the specified tags to the specified WorkSpace.`aws workspaces create-tags \ --resource-id``ws-dk1xzr417`\ --tags`Key=Department,Value=Finance`This command produces no output. For more information, see [Tag WorkSpaces resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [CreateTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-workspaces`.

- **AWS CLI**
- 
            
                    **Example 1: To create an AlwaysOn WorkSpace**The following `create-workspaces`example creates an AlwaysOn WorkSpace for the specified user, using the specified directory and bundle.`aws workspaces create-workspaces \ --workspaces``DirectoryId=d-926722edaf,UserName=Mateo,BundleId=wsb-0zsvgp8fc`Output: `{ "FailedRequests": [], "PendingRequests": [ { "WorkspaceId": "ws-kcqms853t", "DirectoryId": "d-926722edaf", "UserName": "Mateo", "State": "PENDING", "BundleId": "wsb-0zsvgp8fc" } ] }`**Example 2: To create an AutoStop WorkSpace**The following `create-workspaces`example creates an AutoStop WorkSpace for the specified user, using the specified directory and bundle.`aws workspaces create-workspaces \ --workspaces``DirectoryId=d-926722edaf,UserName=Mary,BundleId=wsb-0zsvgp8fc,WorkspaceProperties={RunningMode=AUTO_STOP}`Output: `{ "FailedRequests": [], "PendingRequests": [ { "WorkspaceId": "ws-dk1xzr417", "DirectoryId": "d-926722edaf", "UserName": "Mary", "State": "PENDING", "BundleId": "wsb-0zsvgp8fc" } ] }`**Example 3: To create a user-decoupled WorkSpace**The following `create-workspaces`example creates a user-decoupled WorkSpace by setting the username to`[UNDEFINED]`, and specifying a WorkSpace name, directory ID, and bundle ID.`aws workspaces create-workspaces \ --workspaces DirectoryId=d-926722edaf,UserName='"[UNDEFINED]"',WorkspaceName=MaryWorkspace1,BundleId=wsb-0zsvgp8fc,WorkspaceProperties={RunningMode=ALWAYS_ON}`Output: `{ "FailedRequests": [], "PendingRequests": [ { "WorkspaceId": "ws-abcd1234", "DirectoryId": "d-926722edaf", "UserName": "[UNDEFINED]", "State": "PENDING", "BundleId": "wsb-0zsvgp8fc", "WorkspaceName": "MaryWorkspace1" } ] }`For more information, see [Launch a virtual desktop](https://docs.aws.amazon.com/workspaces/latest/adminguide/launch-workspaces-tutorials.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [CreateWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/create-workspaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-tags`.

- **AWS CLI**
- 
            
                    **To delete a tag from a WorkSpace**The following `delete-tags`example deletes the specified tag from the specified WorkSpace.`aws workspaces delete-tags \ --resource-id``ws-dk1xzr417`\ --tag-keys`Department`This command produces no output. For more information, see [Tag WorkSpaces resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/delete-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `deregister-workspace-directory`.

- **AWS CLI**
- 
            
                    **To deregister a directory**The following `deregister-workspace-directory`example deregisters the specified directory.`aws workspaces deregister-workspace-directory \ --directory-id``d-926722edaf`This command produces no output. For more information, see [Register a directory with WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [DeregisterWorkspaceDirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/deregister-workspace-directory.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-tags`.

- **AWS CLI**
- 
            
                    **To describe the tags for a WorkSpace**The following `describe-tags`example describes the tags for the specified WorkSpace.`aws workspaces describe-tags \ --resource-id``ws-dk1xzr417`Output: `{ "TagList": [ { "Key": "Department", "Value": "Finance" } ] }`For more information, see [Tag WorkSpaces resources](https://docs.aws.amazon.com/workspaces/latest/adminguide/tag-workspaces-resources.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [DescribeTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-workspace-bundles`.

- **AWS CLI**
- 
            
                    **To list the bundles provided by Amazon**The following `describe-workspace-bundles`example lists the names and IDs of the bundles provided by Amazon, in table format and sorted by name.`aws workspaces describe-workspace-bundles \ --owner``AMAZON`\ --query`"Bundles[*].[Name, BundleId]"`Output: `[ [ "Standard with Amazon Linux 2", "wsb-clj85qzj1" ], [ "Performance with Windows 10 (Server 2016 based)", "wsb-gm4d5tx2v" ], [ "PowerPro with Windows 7", "wsb-1pzkp0bx4" ], [ "Power with Amazon Linux 2", "wsb-2bs6k5lgn" ], [ "Graphics with Windows 10 (Server 2019 based)", "wsb-03gyjnfyy" ], ... ]`For more information, see [WorkSpaces bundles and images](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-bundles.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [DescribeWorkspaceBundles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-bundles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-workspace-directories`.

- **AWS CLI**
- 
            
                    **To describe a registered directory**The following `describe-workspace-directories`example describes the specified registered directory.`aws workspaces describe-workspace-directories \ --directory-ids``d-926722edaf`Output: `{ "Directories": [ { "DirectoryId": "d-926722edaf", "Alias": "d-926722edaf", "DirectoryName": "example.com", "RegistrationCode": "WSpdx+9RJ8JT", "SubnetIds": [ "subnet-9d19c4c6", "subnet-500d5819" ], "DnsIpAddresses": [ "172.16.1.140", "172.16.0.30" ], "CustomerUserName": "Administrator", "IamRoleId": "arn:aws:iam::123456789012:role/workspaces_DefaultRole", "DirectoryType": "SIMPLE_AD", "WorkspaceSecurityGroupId": "sg-0d89e927e5645d7c5", "State": "REGISTERED", "WorkspaceCreationProperties": { "EnableInternetAccess": false, "UserEnabledAsLocalAdministrator": true, "EnableMaintenanceMode": true }, "WorkspaceAccessProperties": { "DeviceTypeWindows": "ALLOW", "DeviceTypeOsx": "ALLOW", "DeviceTypeWeb": "DENY", "DeviceTypeIos": "ALLOW", "DeviceTypeAndroid": "ALLOW", "DeviceTypeChromeOs": "ALLOW", "DeviceTypeZeroClient": "ALLOW", "DeviceTypeLinux": "DENY" }, "Tenancy": "SHARED", "SelfservicePermissions": { "RestartWorkspace": "ENABLED", "IncreaseVolumeSize": "DISABLED", "ChangeComputeType": "DISABLED", "SwitchRunningMode": "DISABLED", "RebuildWorkspace": "DISABLED" } } ] }`For more information, see [Manage directories for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/manage-workspaces-directory.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [DescribeWorkspaceDirectories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspace-directories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-workspaces-connection-status`.

- **AWS CLI**
- 
            
                    **To describe the connection status of a WorkSpace**The following `describe-workspaces-connection-status`example describes the connection status of the specified WorkSpace.`aws workspaces describe-workspaces-connection-status \ --workspace-ids``ws-dk1xzr417`Output: `{ "WorkspacesConnectionStatus": [ { "WorkspaceId": "ws-dk1xzr417", "ConnectionState": "CONNECTED", "ConnectionStateCheckTimestamp": 1662526214.744 } ] }`For more information, see [Administer your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-workspaces.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [DescribeWorkspacesConnectionStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces-connection-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-workspaces`.

- **AWS CLI**
- 
            
                    **To describe a WorkSpace**The following `describe-workspaces`example describes the specified WorkSpace.`aws workspaces describe-workspaces \ --workspace-ids``ws-dk1xzr417`Output: `{ "Workspaces": [ { "WorkspaceId": "ws-dk1xzr417", "DirectoryId": "d-926722edaf", "UserName": "Mary", "IpAddress": "172.16.0.175", "State": "STOPPED", "BundleId": "wsb-0zsvgp8fc", "SubnetId": "subnet-500d5819", "ComputerName": "WSAMZN-RBSLTTD9", "WorkspaceProperties": { "RunningMode": "AUTO_STOP", "RunningModeAutoStopTimeoutInMinutes": 60, "RootVolumeSizeGib": 80, "UserVolumeSizeGib": 10, "ComputeTypeName": "VALUE" }, "ModificationStates": [] } ] }`For more information, see [Administer your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/administer-workspaces.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [DescribeWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-workspaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `migrate-workspace`.

- **AWS CLI**
- 
            
                    **To migrate a WorkSpace**The following `migrate-workspace`example migrates the specified WorkSpace to the specified bundle.`aws workspaces migrate-workspace \ --source-workspace-id``ws-dk1xzr417`\ --bundle-id`wsb-j4dky1gs4`Output: `{ "SourceWorkspaceId": "ws-dk1xzr417", "TargetWorkspaceId": "ws-x5h1lbkp5" }`For more information, see [Migrate a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/migrate-workspaces.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [MigrateWorkspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/migrate-workspace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-workspace-creation-properties`.

- **AWS CLI**
- 
            
                    **To modify a WorkSpace creation property of a directory**The following `modify-workspace-creation-properties`example enables the`EnableInternetAccess`property for the specified directory. This enables automatic assignment of public IP addresses for the WorkSpaces created for the directory.`aws workspaces modify-workspace-creation-properties \ --resource-id``d-926722edaf`\ --workspace-creation-properties`EnableInternetAccess=true`This command produces no output. For more information, see [Update directory details for your WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/update-directory-details.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [ModifyWorkspaceCreationProperties](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-creation-properties.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-workspace-properties`.

- **AWS CLI**
- 
            
                    **To modify the running mode of a WorkSpace**The following `modify-workspace-properties`example sets the running mode of the specified WorkSpace to`AUTO_STOP`.`aws workspaces modify-workspace-properties \ --workspace-id``ws-dk1xzr417`\ --workspace-properties`RunningMode=AUTO_STOP`This command produces no output. For more information, see [Modify a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [ModifyWorkspaceProperties](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-properties.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `modify-workspace-state`.

- **AWS CLI**
- 
            
                    **To modify the state of a WorkSpace**The following `modify-workspace-state`example sets the state of the specified WorkSpace to`ADMIN_MAINTENANCE`.`aws workspaces modify-workspace-state \ --workspace-id``ws-dk1xzr417`\ --workspace-state`ADMIN_MAINTENANCE`This command produces no output. For more information, see [WorkSpace maintenance](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspace-maintenance.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [ModifyWorkspaceState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/modify-workspace-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reboot-workspaces`.

- **AWS CLI**
- 
            
                    **To reboot a WorkSpace**The following `reboot-workspaces`example reboots the specified WorkSpace.`aws workspaces reboot-workspaces \ --reboot-workspace-requests``ws-dk1xzr417`Output: `{ "FailedRequests": [] }`For more information, see [Reboot a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/reboot-workspaces.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [RebootWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/reboot-workspaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `rebuild-workspaces`.

- **AWS CLI**
- 
            
                    **To rebuild a WorkSpace**The following `rebuild-workspaces`example rebuilds the specified WorkSpace.`aws workspaces rebuild-workspaces \ --rebuild-workspace-requests``ws-dk1xzr417`Output: `{ "FailedRequests": [] }`For more information, see [Rebuild a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/rebuild-workspace.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [RebuildWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/rebuild-workspaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-workspace-directory`.

- **AWS CLI**
- 
            
                    **To register a directory**The following `register-workspace-directory`example registers the specified directory for use with Amazon WorkSpaces.`aws workspaces register-workspace-directory \ --directory-id``d-926722edaf`This command produces no output. For more information, see [Register an existing AWS Directory Service directory with WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/register-deregister-directory.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [RegisterWorkspaceDirectory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/register-workspace-directory.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-workspace`.

- **AWS CLI**
- 
            
                    **To restore a WorkSpace**The following `restore-workspace`example restores the specified WorkSpace.`aws workspaces restore-workspace \ --workspace-id``ws-dk1xzr417`This command produces no output. For more information, see [Restore a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/restore-workspace.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [RestoreWorkspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/restore-workspace.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-workspaces`.

- **AWS CLI**
- 
            
                    **To start an AutoStop WorkSpace**The following `start-workspaces`example starts the specified WorkSpace. The WorkSpace must have a running mode of`AutoStop`.`aws workspaces start-workspaces \ --start-workspace-requests``WorkspaceId=ws-dk1xzr417`Output: `{ "FailedRequests": [] }`For more information, see [Stop and start an AutoStop WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html#stop-start-workspace)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [StartWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/start-workspaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-workspaces`.

- **AWS CLI**
- 
            
                    **To stop an AutoStop WorkSpace**The following `stop-workspaces`example stops the specified WorkSpace. The WorkSpace must have a running mode of`AutoStop`.`aws workspaces stop-workspaces \ --stop-workspace-requests``WorkspaceId=ws-dk1xzr417`Output: `{ "FailedRequests": [] }`For more information, see [Stop and start an AutoStop WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/running-mode.html#stop-start-workspace)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [StopWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/stop-workspaces.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `terminate-workspaces`.

- **AWS CLI**
- 
            
                    **To terminate a WorkSpace**The following `terminate-workspaces`example terminates the specified workspace.`aws workspaces terminate-workspaces \ --terminate-workspace-requests``ws-dk1xzr417`Output: `{ "FailedRequests": [] }`For more information, see [Delete a WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/delete-workspaces.html)in the*Amazon WorkSpaces Administration Guide*.- 
                    For API details, see [TerminateWorkspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/terminate-workspaces.html)in*AWS CLI Command Reference*.
 
-