# Troubleshooting apps in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/apps-troubleshooting.html](https://docs.aws.amazon.com/quick/latest/userguide/apps-troubleshooting.html)

---

This section describes common issues and how to resolve them.

## Recovering from content policy violations

        If you receive the error "This request could not be processed due to content policy violations":

- 
                Close the apps in Quick editor. 
- 
                Wait 15 to 20 minutes for the session to reset. 
- 
                Reopen the app. 
- 
                Try a simpler, more focused prompt. 

All prompts in the same session after a violation continue to fail until the session resets.

## Recovering from a broken app

        If an app stops loading or displays errors after an edit:

- 
                Use the version selector to restore a previous working version. 
- 
                If the editor is not accessible, close the browser tab, wait 15 to 20 minutes, and reopen. 
- 
                In a fresh session, try: "Review all app code. Check the existing code against the actual types and interfaces exported by the runtime library. Fix any issues." 
- 
                If an integration change caused the issue, try: "The prior issue impacting integrations has been resolved. Please try again." 

## Fixing connector authentication issues

        If you see a "Sign in to connectors" dialog with no sign-in option, one or more integrations were not properly registered during app creation. In the editor, ask the agent to retry registering each affected connector individually. After successful re-registration, publish the updated app.

## Debugging complex apps

        You can ask the agent to add a debug panel that logs storage operations, integration calls, and state changes. Make the panel visible only to yourself (based on your user alias) to keep it hidden from end users.

## File export not working

        If an export feature does not work, ask the agent: "Use the
            `downloadFile` function from the runtime library to handle the file export."
            The sandbox blocks direct browser APIs for file creation. For more information, see
            [Sandbox restrictions](./security-sandbox-apps.html#apps-sandbox-restrictions).