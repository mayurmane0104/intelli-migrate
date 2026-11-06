# Tips for building effective apps - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/tips-best-practices-apps.html](https://docs.aws.amazon.com/quick/latest/userguide/tips-best-practices-apps.html)

---

These tips come from patterns observed in successful app-building sessions.

- 
            **Start with a detailed first prompt**— The first prompt sets the foundation. Including the purpose, audience, data model, and integration needs in your initial description gives the agent a clear starting point and reduces rework.
- 
            **Make changes one at a time**— The agent produces more reliable results with focused, single-purpose instructions than with broad requests that modify many things at once.
- 
            **Provide context about your goals**— When you explain why you want a change, not just what you want, the agent can make better implementation choices.
- 
            **Investigate before changing**— The agent executes code changes with every instruction. If you want to explore options without modifying the app, explicitly say so: "Investigate the current data flow but do not write any code yet."
- 
            **Note stable version numbers**— After completing a working feature, note the current version. If subsequent changes cause problems, you can restore the stable version immediately using the version selector.
- 
            **Add a debug panel for complex apps**— For apps with significant logic, a debug panel that logs storage operations, integration calls, and state changes makes it easier to track down problems. You can make the panel visible only to yourself based on your user alias.
- 
            **Specify roles when your app has different user types**— If different people should see different things, include that in your instructions.
- 
            **Use structured AI output**— When you need data in a specific format (JSON, categories), use structured output mode instead of asking for free-form text. It guarantees valid, parseable responses.
- 
            **Scope storage thoughtfully**— Use private storage for user-specific data and shared storage for collaborative features. Keep table names descriptive.
- 
            **Approve integrations deliberately**— Review each integration approval carefully. Only approve connectors and spaces your app actually needs.