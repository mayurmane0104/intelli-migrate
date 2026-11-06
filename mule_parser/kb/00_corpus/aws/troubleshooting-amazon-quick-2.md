# Troubleshooting - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/desktop-troubleshooting.html](https://docs.aws.amazon.com/quick/latest/userguide/desktop-troubleshooting.html)

---

The following sections describe common issues you might encounter when using the Amazon Quick desktop application and how to resolve them.

## Installation and launch issues

        - macOS displays an "unidentified developer" warning
- 
                    If macOS prevents you from opening the Amazon Quick desktop application because it's from an unidentified developer, use the following procedure to allow it. - Open - **System Settings**on your Mac.
- Choose - **Privacy & Security**.
- Scroll to the Security section and choose - **Open Anyway**next to the message about Quick.
- Confirm that you want to open the application. 
 ###### NoteOn first launch, your operating system might prompt you to confirm that you want to open the application. Choose **Open**to continue.
- The application doesn't launch
- 
                    If the Amazon Quick desktop application doesn't launch, try the following steps. - Restart your computer and try opening the application again. 
- Verify that your operating system meets the minimum requirements. 
- Check that you have sufficient disk space available. 
- If the issue persists, delete the - `~/.quickwork/`directory (macOS) or- `%USERPROFILE%\.quickwork\`directory (Windows) and reinstall the application.
 ###### WarningDeleting the `~/.quickwork/`(macOS) or`%USERPROFILE%\.quickwork\`(Windows) directory removes all local data, including conversations, knowledge graph, memory, and saved credentials. Use this step only as a last resort.

## Connection issues

        - Slack or Outlook connection fails
- 
                    If a connection to Slack or Microsoft Outlook fails, try the following steps. - Disconnect the service in - **Settings**>- **Capabilities**>- **Connections**.
- Reconnect the service by choosing - **Sign in**and completing the authentication flow.
- Verify that your account has the required permissions in the third-party service. 
- Check that your internet connection is active and stable. 
 
- Microsoft Teams connection fails
- 
                    If a connection to Microsoft Teams fails, follow the same steps as for Slack or Outlook. Verify that your organization's administrator has not restricted third-party application access. 
- Connection shows "Not synced" status
- 
                    If a connection shows a "Not synced" status, try the following steps. - Verify that you have an active internet connection. 
- Disconnect and reconnect the service in - **Settings**>- **Capabilities**>- **Connections**.
- If the issue persists, the third-party service might be experiencing an outage. Check the service's status page. 
 
- Google Workspace connections fail
- 
                    If connections to Google services (Gmail, Google Calendar, Google Drive, Google Docs, Google Sheets, Google Slides, Google Meet, or Google Analytics) fail, verify the following. - Your Google account is not restricted by your organization's admin policies. 
- You have granted the required OAuth permissions during the sign-in flow. 
- You are signing in with the correct Google account. 
 

## Performance issues

        - Slow responses
- 
                    If Quick responses are slow, try the following steps. - Switch to the - **Fast**AI model mode for quicker responses. Choose the model selector in the chat input area and select- **Fast**.
- Reduce the - **thinking effort**level. Lower thinking effort (Off or Low) produces faster responses.
- Close unused applications to free up system resources. 
- Check your internet connection speed. AI model requests require a network connection to API Gateway. 
 
- High memory usage
- 
                    If the Amazon Quick desktop application uses excessive memory, try the following steps. - Reduce the number of folders indexed in - **Settings**>- **My computer**. Disable- **Semantic search**for folders that don't require it, as semantic search uses more resources than keyword search.
- Lower the - **Max parallel tasks**slider in- **Settings**>- **Customization**>- **Performance**. The default value is 50. Reducing this value limits the number of concurrent background operations.
- Restart the application to clear cached data. 
- Adjust search indexing limits in - **Settings**>- **My computer**>- **Search indexing**. Lower the- **Storage limit**,- **Max file size for indexing**, or- **Max folder size for indexing**sliders.
 ###### NoteSearch indexing automatically pauses when free disk space falls below 8.0 GiB. 

## File access issues

        - Quick can't find a file
- 
                    If Quick can't find a file you reference in chat, verify the following. - The file's parent folder is added in - **Settings**>- **My computer**>- **Local folders**. Quick can only access files in folders you explicitly grant access to, with the exception of system temporary directories, which are always accessible. On Windows, these are- `C:\TEMP`,- `C:\TMP`,- `\TEMP`, and- `\TMP`. On macOS and Linux, these are- `/tmp`,- `/var/tmp`, and- `/usr/tmp`.
- Choose - **+ Add folder**to grant access to additional folders.
- After adding a folder, Quick can immediately read files in it. Indexing for search happens in the background. 
 
- Search returns no results
- 
                    If file search returns no results, try the following steps. - Verify that - **Keyword search**is toggled on for the folder in- **Settings**>- **My computer**>- **Local folders**. Expand the folder to see its indexing toggles.
- Check the indexing status. A - **Ready**status with file and entry counts confirms indexing is complete.
- If you recently added a new folder, wait for indexing to complete. The status shows progress. 
- Check that the file is not larger than the - **Max file size for indexing**limit in- **Settings**>- **My computer**>- **Search indexing**. Files larger than this limit are skipped during indexing but are still available to the agent through direct file access.
- For broader search, enable - **Semantic search**on the folder to allow natural language queries.
 

## Browser automation issues

        - Browser automation doesn't work
- 
                    If Quick can't browse web pages, try the following steps. - Verify that - **Browser Automation**is enabled in- **Settings**>- **Capabilities**>- **System**.
- If using "Use my Chrome" mode, verify the setup in - **Settings**>- **Customization**>- **Browser**. Open Chrome and navigate to- `chrome://inspect/#remote-debugging`. Choose- **Enable remote debugging**. Return to Quick and choose- **Test Connection**to verify the connection.
- If using the default mode, Quick launches a separate Chrome instance with a copy of your profile. Ensure Chrome is installed on your system. 
 

## Scheduled agent issues

        - A scheduled agent didn't run
- 
                    Scheduled agents run locally on your computer. If an agent didn't run at its scheduled time, verify the following. - Your computer was turned on and awake at the scheduled time. 
- The Amazon Quick desktop application was running. 
- The agent is enabled. Check the toggle in - **Settings**>- **Capabilities**>- **Scheduled tasks**, or open the- **Agents**panel from the top bar.
- Your internet connection was active. Agents that access connected services or AI models require a network connection. 
 ###### ImportantIf your computer is off or the application is closed when an agent is scheduled to run, the agent does not run until the next scheduled time. 
- Agent produces unexpected results
- 
                    If a scheduled agent produces unexpected results, try the following steps. - Open - **Settings**>- **Capabilities**>- **Scheduled tasks**and select the agent.
- Review the - **Prompt**tab to verify the agent's instructions are correct.
- Check the - **Capabilities**tab to verify the correct MCP servers are attached.
- Consider changing the - **Model**in the- **Overview**tab. Use- **Balanced**or- **Smart**for more complex agent tasks.
- Choose the - **Run**button (play icon) to manually trigger the agent and observe the results.
 

## MCP server issues

        - MCP server fails to connect
- 
                    If an MCP server fails to connect, try the following steps based on the connection type. **Local MCP server:**- Verify that the command is correct and the executable is installed on your system. 
- Check that the arguments are space-separated and correctly formatted. 
- Increase the - **Timeout**value if the server takes longer than 30 seconds to start (configurable from 5 to 300 seconds).
- Verify that any required - **Environment variables**are correctly set.
 **Remote MCP server:**- Verify that the URL is correct and the server is running. 
- If authentication is required, verify the - **Token**value is a valid bearer token.
- Check your network connection and any firewall settings. 
 **Imported MCP server:**- Verify that the config file path is correct. 
- Ensure the source application (Kiro, Claude Code, AIM, and so on) is properly installed. 
 

## Exporting diagnostics

        If you need to share diagnostic information for troubleshooting, you can export diagnostic logs from the application.

- Open - **Settings**>- **Customization**.
- Scroll to the - **Troubleshooting**section.
- Select a time range from the dropdown (for example, - **Last 2 hours**).
- Choose - **Export Diagnostics**to save diagnostic logs to your desktop.

## Resetting the application

        If other troubleshooting steps don't resolve your issue, you can reset the application by clearing all data.

###### Warning

This action is irreversible. It removes all Quick data, including conversations, cached messages, knowledge graph, saved credentials, and user preferences. The application quits after cleanup.

- Open - **Settings**>- **Customization**.
- Scroll to the - **Danger zone**section.
- Choose - **Clear all data**.
- Confirm the action. 
- To fully uninstall on macOS, drag - `Amazon Quick.app`to Trash. On Windows, open- **Settings**>- **Apps**>- **Installed apps**, find Amazon Quick, and choose- **Uninstall**.

## Getting additional help

        If the preceding troubleshooting steps don't resolve your issue, you can use the following resources.

- **Export diagnostics**and share them with your support team.
- **Developer menu**– Choose the connection status dot (green dot in the top-right corner) to access Mission Control, Metrics overlay, Debug panel, and Memory panel for advanced diagnostics.
- Contact your organization's IT administrator for enterprise account issues. 
- Visit the Amazon Quick documentation for the latest guidance.