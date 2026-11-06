# Authentication Errors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-authentication-errors](https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-authentication-errors)

---

Failed to authenticate to git remote

# Authentication Errors

In Anypoint Code Builder, authentication errors sometimes occur when you attempt to perform actions that require a connection to Anypoint Platform or to services that the cloud and desktop IDEs rely on.

## Failed to Authenticate to Git

All commands that involve `git` actions, such as publishing to Exchange and committing changes to an API specification, require authentication with the correct Anypoint Platform host cloud. If authentication fails, the action throws this VS Code error:

To address this issue, cancel the error notification, and ensure that your IDE is set to the correct region for your project and that you are logged in to Anypoint Platform.