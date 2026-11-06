# Limitations of apps in Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/apps-limitations.html](https://docs.aws.amazon.com/quick/latest/userguide/apps-limitations.html)

---

The following limitations apply to apps in Amazon Quick in its current release.

## Limits

        | Resource | Limit | 
|---|---|
| Dashboard visuals per app | 8 | 
| Visual minimum size | 100 × 100 pixels | 
| Storage value size | 350 KB per item | 
| Storage key length | 255 characters | 
| Table name length | 255 characters | 

## Building experience

        - 
                **Content policy violations**— Prompts occasionally trigger security guardrails as false positives. When this happens, the agent cannot process further prompts in the current session. Close the editor and wait 15 to 20 minutes for the session to time out, then reopen the app.
- 
                **Agent memory in long conversations**— The agent's accuracy decreases as the conversation grows longer. For complex applications, consider building in phases.
- 
                **No image upload from agent chat**— You cannot upload screenshots or reference images to the agent.
- 
                **No investigation-only mode**— The agent executes code changes with every instruction. To have the agent investigate without making changes, explicitly say "Investigate but do not write code yet."
- 
                **Network sensitivity**— The editor uses a WebSocket for real-time streaming. Unstable connections can cause prompts to fail silently.

## Sharing and access

        - 
                **Subscription requirement**— Only users with Author, Professional, Author Pro, Enterprise, or Admin Pro subscriptions can view apps.
- 
                **No external access**— Users must have a Amazon Quick account to view an app. External access is not supported.

## Portability

        - 
                **No code export**— You cannot download the source code of an app.
- 
                **Duplication**— You can duplicate an app to create a copy.

## Integration limitations

        - 
                **No direct Quick Flows integration**— Use a space as an intermediary.
- 
                **No standalone agent embedding**— You can create a new agent instance backed by a space.
- 
                **No integration removal**— You cannot remove a registered integration from an app through the settings UI.

## Sandbox restrictions

        For detailed information about sandbox restrictions, see
            [Sandbox restrictions](./security-sandbox-apps.html#apps-sandbox-restrictions). Key
            restrictions include:

- 
                **No direct link navigation**— Users must use Cmd+Click or Ctrl+Click.
- 
                **No external images**— CSP blocks loading images from external URLs.
- 
                **No built-in app analytics**— As a workaround, you can ask the agent to implement a view counter using shared app storage.