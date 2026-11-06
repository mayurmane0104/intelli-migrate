# Creating New GitHub Repositories Synchronized from an Existing Projects | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/design-center/design-ghs-new-repo-existing-project](https://docs.mulesoft.com/design-center/design-ghs-new-repo-existing-project)

---

# Creating New GitHub Repositories Synchronized from an Existing Projects

You can create a new GitHub repository and synchronize it with an existing API Designer project.

## Before You Begin

Before you synchronize a new repository and a project, ensure you have:

- 
The Design Center Developer permission within Anypoint Platform 
- 
[Installed and authorized](design-ghs-install-authorize)the GitHub Synchronization application
- 
Signed into GitHub 

## Synchronize A New Repository and A Project

- 
In the Design Center **Projects**list, click the table row containing a project to synchronize with GitHub.
- 
In the details panel, click the **Sync with GitHub**button.
- 
In the **Enable Sync with GitHub**dialog, select an organization from the**GitHub Organization**list dropdown.The **GitHub Organization**list remains empty if the GitHub Synchronization application is not installed. See[Install and Authorize the MuleSoft GitHub Synchronization Application](design-ghs-install-authorize).
- 
Specify a name for the new repository. 
- 
Click **Sync**.You are navigated to the Design Center **Projects**page. A**Sync Status**indicator appears in the**Details**pane along with buttons that enable you to manage a GitHub repository and disable synchronizing.