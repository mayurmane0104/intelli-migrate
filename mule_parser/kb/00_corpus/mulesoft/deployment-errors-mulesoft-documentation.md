# Deployment Errors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-deploy-errors](https://docs.mulesoft.com/anypoint-code-builder/troubleshoot-deploy-errors)

---

# Deployment Errors

In Anypoint Code Builder, the error `Failed to deploy to CloudHub: 400` occurs when you deploy a Mule application to CloudHub if the root organization or business group to which you are deploying lacks a sufficient vCore allocation.

To address this isssue, increase the vCore allocation to the root organization or business group in the **Sandbox** environment:

- 
To reallocate resources, see [Redistribute Resources Between Existing Business Groups](../access-management/business-groups#redistribute-resources).
- 
To manage environments, see [Anypoint Platform Environments](../access-management/environments). For additional help, contact your organization administrator for Anypoint Platform.