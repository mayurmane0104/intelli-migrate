# Project Loading Errors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-loading-errors](https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-loading-errors)

---

- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+u 
- 
Windows: Ctrl+Shift+u 
 
- 
- 
In the desktop IDE, select **View**>**Output**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Output**.

# Project Loading Errors

Errors sometimes occur when you open or start a project in Anypoint Code Builder.

## Loading Error in the Canvas

A **Loading…** error in the graphical UI (canvas) often occurs under these conditions:

- 
When importing a project due to a missing dependency 

To check for a missing dependency:

- 
Open the Output panel. ## Show me how
- 
Select Mule DX Server from the dropdown list. 
- 
Search for an error caused by the missing dependency, similar to this one: Caused by: org.eclipse.aether.transfer.ArtifactNotFoundException: Failure to find org.mule.examples:accelerator-common-config-module:jar:mule-plugin:1.1.0 in https://repo.maven.apache.org/maven2/ was cached in the local repository, resolution will not be reattempted until the update interval of central has elapsed or updates are forced 
- 
If you find a missing dependency, log in to Anypoint Platform. The canvas loads after all dependencies load. When a browser extension is interfering with the UI loading process, you see: ![Loading error in the UI](_images/troubleshoot-loading-error.png)  

To address this issue, try:

- 
Disabling browser extensions and reloading the application 
- 
Using another browser that is not using extensions 

## UI Canvas Renders Without Configured Flows or Subflows

If the UI for an application that is already configured with a flow or subflow treats your application as a new project, prompting you with the question **How do you want to start building your project?** and **Build a flow** and **Build a sub flow** creation options, make sure that your application is open from its *root* directory or from a multi-root workspace.

![Start Screen Building a Mule Application](_images/acb-start-flow-subflow-ui.png) 

Visual Studio Code treats an open directory as a workspace. For the project to load into a workspace, the root directory of the project must be the top-level directory in the Explorer view, or the project must belong to a [multi-root workspace](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces).

- 
Open the Command Palette. ## Show me how- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
In the desktop IDE, select **View**>**Command Palette**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Command Palette**.
 
- 
- 
Provide this command: `File: Open Folder...`command
- 
Navigate to the *root*directory for your project.The root is the top-level folder that Anypoint Code Builder generates when it creates a project. Do not navigate to the project’s parent or ancestor directory or to one of its child or descendant directories. 

See also [Importing Projects into the IDE](int-import-mule-project) and [Working with Workspaces](start-workspaces).

## Mule DX API Component Was Not Installed

The error indicates that some Anypoint Code Builder dependencies have not finished loading. This issue typically occurs when you click **Design an API** and is often accompanied by the notification **Extracting Mule runtime: This operation may take a while…**. The extraction process can take several minutes, particularly after you install or update Anypoint Extension Pack on the desktop IDE.

- 
Wait for the error **Mule DX API Component was not installed**to disappear.
- 
Retry your action. 

To monitor the progress of backend processes:

- 
Open the Output panel. ## Show me how- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+u 
- 
Windows: Ctrl+Shift+u 
 
- 
- 
In the desktop IDE, select **View**>**Output**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Output**.
 
- 
- 
Select **Mule DX Server**from the dropdown list in the panel. To see scaffolding errors only, select**Mule DX Server: Scaffolding**from the list.

## Dependency Resolution Error

The error `There was an issue solving the dependencies for the asset` occurs when a dependency is missing. Usually, the appears after you import or open an integration or implementation project that is missing one or more dependencies for a connector operation.

To address this issue and avoid other errors, try logging in to Anypoint Platform from the IDE, and wait for the project to finish loading before attempting to resolve any missing dependencies that remain.