# Troubleshooting | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/troubleshooting](https://docs.mulesoft.com/anypoint-code-builder/troubleshooting)

---

- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
In the desktop IDE, select **View**>**Command Palette**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Command Palette**.

# Troubleshooting

Troubleshoot errors and warnings you encounter when using Anypoint Code Builder.

- 
For other issues and workarounds, see [Known Issues](acb-release-notes#known-issues)in the Anypoint Code Builder Release Notes.

For tasks that support the troubleshooting process, see:

## Check for Problems and Issues

When you don’t know how to resolve an issue, the first step is to check for and review problems, console output, and logs. Error messages and logs list underlying issues that can help you understand what went wrong and what requires attention.

- 
To view centralized errors and warnings, open the **ACB Logs**panel. See[View Errors and Warnings in ACB Logs](start-open-output-panel#acb-logs).
- 
To view detailed logs for in-depth investigation, use the **Output**panel. See[View Detailed Logs in the Output Panel](start-open-output-panel#output-panel).
- 
To view problems, open the **Problems**tab by pressing Cmd+Shift+m (Mac) or Ctrl+Shift+m (Windows).

## Export Troubleshooting Information

If the MuleSoft support team requests troubleshooting information about your project, export a compressed file that contains your project’s workspace folders, logs, and information about environment variables, CPU, operating system, and system properties.

- 
Open the Command Palette. ## Show me how
- 
Provide this command: `MuleSoft: Export Troubleshooting Information`command
- 
When you receive a notification about the information that the command extracts, click **Continue**.When the process is complete, the IDE shows this message: Collecting information...: Generating compressed file 
- 
Click **Open folder**to locate the file.The command places the file in your home directory. The filename has the prefix `acb-troubleshooting`, for example,`/Users/me/acb-troubleshooting-w9ffppmq.tar.gz`.
- 
Provide a copy of the file to the support team. 

## Manage Your Cloud IDE Instance

Manage your cloud IDE instance directly from the Anypoint Code Builder in Anypoint Platform.

![Cloud IDE management page](_images/web-ide-management-central-page.png) 

| 1 | Version and IDE Details:Shows the version of your Anypoint Code Builder cloud IDE instance. You can hover over  
 | ||
| 2 | Reboot: Button for rebooting your cloud IDE instance. | ||
| 3 | Delete: Button for deleting your cloud IDE instance.
 | 

## Check for Anypoint Extension Pack Installation

To determine whether Anypoint Code Builder extensions are installed in the desktop IDE, check for the **Anypoint Extension Pack** in the **Extensions: Marketplace** panel of the IDE:

- 
In the Activity Bar, click the Extensions icon to open the **Extensions: Marketplace**panel.To find this icon, see [Discovering the UI](start-discover-ui).
- 
In the panel’s search field, type *Anypoint*to locate**Anypoint Extension Pack**in the list of installed extensions.- 
If the extension pack is *not*installed, follow the installation steps at[Set up the Desktop IDE](start-acb#set-up-desktop).
- 
If the extension pack is installed but the MuleSoft icon is not present in the Activity Bar, see [MuleSoft Icon Missing from Activity Bar](troubleshoot-missing-features#missing-mulesoft-icon)to display the icon.
 
- 

## Folder Permission Error

Some high-level folders in the cloud IDE are protected and not available for your projects. Examples include `/home`, `/`, and `.config`. Attempts to create an integration, implementation, or design project in a protected folder produces the following error:

EACCES: permission denied, mkdir '/home/XXXX/.vscode'

To avoid this error, create and import your projects within your `/home/` folder or in a subdirectory that you create under this folder. The cloud IDE automatically provides the folder with your username.*your-user-name*/

Also avoid creating your projects under `/home/AnypointCodeBuilder`, which is intended for downloads of Mule and Java versions.

## Disable Components to Isolate Issues

When debugging a flow, you can disable (comment out) individual components directly in the canvas. This allows you to isolate and test parts of your logic without removing or rewriting anything. For example:

- 
Temporarily disable a Transform or Logger to test a different path. 
- 
Comment out an entire flow or error handler to simplify the execution logic. 
- 
Disable MUnit test processors to troubleshoot specific assertions. 

To disable a component:

- 
Right-click it in the canvas. 
- 
Select **Disable Component**.

Disabled components are unavailable in the canvas and are ignored at runtime. In the code editor, the block is wrapped in an XML comment.

Once the issue is resolved, you can re-enable the component or use Delete to remove disabled items.

## View Error Messages and Warnings in the Canvas

Anypoint Code Builder shows validation issues directly in the canvas to help you resolve problems faster. Hover over a component to see a tooltip listing errors and warnings, along with affected field names.

The configuration sidebar also displays validation messages at the node level.

Field-level errors appear inline during component configuration.

Hover over a component with a red dot to view error details in the canvas.

## Perform a Clean Reinstallation

If you experience persistent issues that other troubleshooting steps don’t resolve, perform a clean reinstallation of Anypoint Extension Pack:

- 
Close VS Code completely. 
- 
Uninstall Anypoint Extension Pack: - 
Open VS Code. 
- 
From the Activity Bar, open the **Extensions**panel.
- 
Find and select **Anypoint Extension Pack**.
- 
Click **Uninstall**.
- 
Close VS Code. 
 
- 
- 
Delete the `anypoint-code-builder`folder from your user directory:- 
Mac: `~/AnypointCodeBuilder`
- 
Windows: `C:\Users\<username>\AnypointCodeBuilder`
 
- 
- 
Optionally, delete cached extension data from the VS Code extensions folder: - 
Mac: `~/.vscode/extensions/`
- 
Windows: `C:\Users\<username>\.vscode\extensions\`Remove any folders starting with `salesforce.mule-dx-`or`mulesoftinc.mule-dx-`.
 
- 
- 
Reopen VS Code and reinstall Anypoint Extension Pack from the Extensions Marketplace. 

| This procedure removes downloaded Mule runtime versions and Java versions. You can re-download them after reinstalling. |