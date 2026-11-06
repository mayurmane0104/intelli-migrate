# Configuring Permissions | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/start-configure-permissions](https://docs.mulesoft.com/anypoint-code-builder/start-configure-permissions)

---

## Show me how

- 
US cloud (non-EU host): [Anypoint Platform (US)](https://anypoint.mulesoft.com/login/)
- 
EU cloud (EU host): [Anypoint Platform (EU)](https://eu1.anypoint.mulesoft.com/login/)

MuleSoft MCP Support is now available

Create connected experiences with AI

Future of connected AI agents

Go from composability to agent actionability

2.x

Mule 4

1.12

2.x

Configuring Permissions

Configuring Permissions

**Open Beta Release**: The **cloud IDE is in open beta**. Any use of Anypoint Code Builder in its beta state is subject to the applicable beta services terms and conditions, available from the IDE.

    ![Cloud IDE logo cloud IDE](../_/img/logos/deployment-cloud-ide.png) Cloud IDE

    Cloud IDE

    ![Desktop IDE logo desktop IDE](../_/img/logos/deployment-desktop-ide.png) Desktop IDE

    Desktop IDE

Manage user access to Anypoint Code Builder and Anypoint Platform features used by the cloud and desktop IDEs. Use Access Management to grant permissions directly to individual users or assign permissions to teams to which the users belong.

These permissions are required:

Cloud IDE users only:

**Anypoint Code Builder Developer** allows a user to launch Anypoint Code Builder from Anypoint Platform.

Cloud and desktop IDE users:

Set these [Anypoint Exchange permissions](../access-management/permissions-by-product#exchange) so that users can download and publish assets:

**Viewer**

**Creator**

Set these [Runtime Manager permissions](../access-management/permissions-by-product#runtime-manager) to enable services related to CloudHub and CloudHub 2.0, such as deploying applications:

**Read applications**

**Create applications**

**Delete applications**

Set the [Design Center Developer](../access-management/permissions-by-product#design-center) permission so that users can view and create APIs.

For a complete list of permissions, see [Permissions by Product in Anypoint Platform](../access-management/permissions-by-product).

Log in to Anypoint Platform on your US or EU cloud host.

US cloud (non-EU host): [Anypoint Platform (US)](https://anypoint.mulesoft.com/login/)

EU cloud (EU host): [Anypoint Platform (EU)](https://eu1.anypoint.mulesoft.com/login/)

If you do not have an Anypoint Platform account, you can sign up from one of the hosts.

To grant permissions to an individual user:

In Anypoint Platform, navigate to **Access Management**.

For the Anypoint Platform URL, see [Before You Begin](#before-you-begin).

Assign [permissions](#permissions) to the user by following the steps in [Grant Permissions to Users](../access-management/users#grant-user-permissions).

The user can now develop using Anypoint Code Builder.

To grant the permission to a team:

In Anypoint Platform, navigate to **Access Management**.

For the Anypoint Platform URL, see [Before You Begin](#before-you-begin).

If you haven’t started using Teams in Access Management, click **Try New Features** > **Start Using These Features** to [opt in to Teams](../access-management/teams#opt-in-to-teams).

Follow the steps in [Configuring Teams in Anypoint Platform](../access-management/configure-teams):

If necessary, create the team and add users.

Assign [permissions](#permissions) to the team.

The members of the team can now develop using Anypoint Code Builder.