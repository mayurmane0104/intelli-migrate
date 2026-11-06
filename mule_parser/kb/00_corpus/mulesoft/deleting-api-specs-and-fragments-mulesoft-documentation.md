# Deleting API Specs and Fragments | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/des-delete-api-projects](https://docs.mulesoft.com/anypoint-code-builder/des-delete-api-projects)

---

## Show me how

- 
US cloud (non-EU host): [Anypoint Platform (US)](https://anypoint.mulesoft.com/login/)
- 
EU cloud (EU host): [Anypoint Platform (EU)](https://eu1.anypoint.mulesoft.com/login/)

Deleting API specs and fragments varies depending on the project creation date and project hosting.

To delete a design project hosted locally on Anypoint Code Builder, delete the entire project folder.

To delete a design project hosted on US cloud or EU cloud with an API spec imported from MuleSoft VCS, you must delete the project from MuleSoft VCS by accessing Design Center.

To delete a design project created with versions of Anypoint Code Builder released prior to February 2024 that required storage of the spec in the MuleSoft VCS, you must delete the project from MuleSoft VCS by accessing Design Center.

To delete a project hosted on JP cloud or CA cloud, you must use an Anypoint CLI command.

| You must delete the previous project to reuse the project name for a new design project in Anypoint Code Builder. | 

To delete an API project (API spec or API spec fragment) from Anypoint Code Builder:

In the Explorer view, right-click on the folder and select **File** > **Open Folder**.

Locate the folder for the project to delete.

Right-click and select to delete the folder.

API design projects [imported to Anypoint Code Builder from Design Center](des-create-api-specs#import-spec) or created in Anypoint Code Builder before the February 2024 release automatically connect to MuleSoft VCS, which enables you to sync with a corresponding design project.

Design project names must be unique. To create a new design project with a name already used in Anypoint Code Builder, you must delete the existing project from the IDE.

To delete an API project (API spec or API spec fragment) from Anypoint Code Builder:

In Anypoint Code Builder, [delete the spec](#delete-spec).

To delete a design project from Design Center:

Navigate to Anypoint Platform and log in using your credentials.

US cloud (non-EU host): [Anypoint Platform (US)](https://anypoint.mulesoft.com/login/)

EU cloud (EU host): [Anypoint Platform (EU)](https://eu1.anypoint.mulesoft.com/login/)

Select **Design Center** from the navigation panel.

Select **API Projects** from the navigation panel.

Select the project and click the ![](_images/icon-dc-delete-project.png) (

 (**Delete Project**) icon.

To delete a design project by using Anypoint CLI:

Run this command:

designcenter:project:delete [flags] <name>

For more information, see [delete design projects using Anypoint CLI](../anypoint-cli/latest/design-center#designcenter-project-delete).