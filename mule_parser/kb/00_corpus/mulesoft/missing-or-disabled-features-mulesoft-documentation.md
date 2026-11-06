# Missing or Disabled Features | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-missing-features](https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-missing-features)

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

# Missing or Disabled Features

Some Anypoint Code Builder features can be disabled or hidden based on settings in the IDE.

For any features that aren’t working as expected, first [check for problems and issues](troubleshooting#check-logs).

## MuleSoft Icon Missing from the Activity Bar

If the MuleSoft icon (see [Discovering the UI](start-discover-ui)) is missing from the Activity Bar, check for and address common causes.

### Enable Anypoint Code Builder in the Activity Bar

The Activity Bar allows you to enable or disable icons.

- 
In the IDE, right-click the Activity Bar. 
- 
Check for **Anypoint Code Builder**:- 
If **Anypoint Code Builder**is disabled, click**Anypoint Code Builder**to add the icon to the Activity Bar.
- 
If **Anypoint Code Builder**is not present, see[Check for Anypoint Extension Pack Installation](troubleshooting#check-extension-pack). If the Anypoint Extension Pack is installed,[Check for Restricted Mode](#check-trusted).
 
- 

### Check for Restricted Mode

If your project or workspace is in restricted mode, the MuleSoft icon does not appear in the Activity Bar.

To determine whether your project or workspace is trusted or in restricted mode:

- 
Open the Command Palette. ## Show me how
- 
Provide the following command to launch the **Workspace Trust**tab:`Workspace: Manage Workspace Trust`commandIf the **Workspace Trust**tab says**You are in Restricted Mode**, you can click**Trust**or**Trust Parent**.![VS Code indicating that a project or workspace is in restricted mode](_images/acb-restricted-mode.png) 
- 
After trusting, check for the MuleSoft icon in the Activity Bar. 

For more information about trust settings in the IDE, see [Trusting a workspace](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) in the VS Code documentation.

### Modify Trust Settings

To modify your trust settings in the IDE:

- 
Provide the following command to launch the **Workspace Trust**tab:`Workspace: Configure Workspace Trust Settings`command
- 
Review and adjust the workspace settings, as needed. 

## Incomplete Flow or Corrupted XML

If a flow lacks a component or contains only a trigger, such as an HTTP Listener operation or the Scheduler, an error similar to the following appears in the **Problems** panel and from the code editor:

```
The content of element 'flow' is not complete. One of
'{"http://www.mulesoft.org/schema/mule/core":abstract-message-processor,
"http://www.mulesoft.org/schema/mule/core":abstract-mixed-content-message-processor}'
is expected.(cvc-complex-type.2.4.b)
```
To address this issue, add processing components or connector operations to your flow, such as a Logger or HTTP Request operation.
For reference documentation on specific connector and component configurations, see [Anypoint Code Builder Components and Commands Reference](acb-reference).

This error can also occur if XML tags in the configuration file are corrupted or not properly closed. If you’ve already added components and the error persists, check the configuration XML for unclosed tags. To prevent XML corruption, save your work frequently and use source control management (SCM) to back up your projects.