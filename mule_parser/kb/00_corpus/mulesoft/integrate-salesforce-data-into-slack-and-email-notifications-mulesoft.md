# Integrate Salesforce Data into Slack and Email Notifications | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/tut-slack-create-escalation-api](https://docs.mulesoft.com/anypoint-code-builder/tut-slack-create-escalation-api)

---

![Create an App in Slack](_images/slack-create-app.png) 

# Integrate Salesforce Data into Slack and Email Notifications

Create an integration that notifies you through email or Slack when a new case is created in Salesforce.

The integration that you build contains a flow with the following logic:

- 
The creation of a new case in Salesforce triggers your flow. 
- 
If the case is escalated, your application sends an email to the regional leader including the case number, origin, reason, priority, and status. 
- 
If the case is not escalated, your application sends a message to a Slack channel with the same information. 

## Before You Begin

Before you begin, ensure you:

- 
Set up your MuleSoft environment. See [Getting Started with Anypoint Code Builder](start-acb)for more information.
- 
Set up a Salesforce demo environment. - 
[Sign up for a developer organization](https://www.salesforce.com/products/free-trial/developer/).
- 
[Create a developer security token](https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm&type=5).
 
- 
- 
Have a personal or business Gmail account. 
- 
Have a personal or business Slack account. 

### Set Up Your Slack Workspace

- 
Navigate to [Slack](https://slack.com/)and log in using your organization credentials.If your work organization restricts users from creating new workspaces, log in using your personal email account. 
- 
Create a new Workspace called **Integration Test**.
- 
Skip the step to invite new users and type a brief description of your Workspace, for example, **This is a test Workspace**.
- 
Navigate to [Your Apps](https://api.slack.com/apps)and click**Create an App**:![Create an App in Slack](_images/slack-create-app.png)  
- 
Select **From scratch**.
- 
Name your app **OAuth for Anypoint Code Builder**, and select your**Integration Test**workspace.
- 
Click **Generate**:![Generate a configuration token in Slack](_images/generate-token.png)  
- 
Click **Create App**:![Name your app and select a workspace in Slack](_images/slack-create-app-workspace.png)  
- 
Click **Install App**:![Install an app in Slack](_images/slack-install-app.png)  
- 
Click **Permission scope**:![Click permission scope in Slack](_images/slack-install-permission-scope.png)  
- 
Scroll down to the **Scopes**section and, under**Bot Token Scopes**, select**Add an OAuth Scope**, and select**chat:write.public**:![Add OAuth scope in Slack](_images/slack-bot-permissions-chat-write.png)  
- 
Select **Add scopes**when prompted to add other necessary scopes for`chat:write.public`.
- 
Scroll up to the **OAuth Tokens for Your Workspace**and select**Install to Workspace**.
- 
Click **Allow**:![Allow OAuth access to workspace](_images/slack-allow-install-app-workspace.png)  
- 
Under **Bot User OAuth Token**, click**Copy**and save it on a safe location.![Copy OAuth token for Bot User](_images/slack-copy-oauth-token.png)  You use this token to connect to your Slack workspace from Anypoint Code Builder: 
- 
Create a new public channel called "this-is-a-test" in your **Integration Test**workspace.
- 
Add the OAuth for Anypoint Code Builder app to the `this-is-a-test`channel.

### Set up an App Password for Your Email

Later in this tutorial, you configure the Email Connector to send emails to your configured email account. To avoid using your email password, follow [Google instructions](https://support.google.com/accounts/answer/185833?visit_id=637917932546436561-2352829986&p=InvalidSecondFactor&rd=1) to configure an App password.

| The Gmail account must have 2-factor authentication enabled to configure an App password. | 

## Create an Integration

- 
Navigate to Anypoint Code Builder. 
- 
Open the Command Palette. ## Show me how- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
In the desktop IDE, select **View**>**Command Palette**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Command Palette**.
 
- 
- 
Provide the following command: `MuleSoft: Develop an Integration`command
- 
Provide integration project properties to the **Develop an Integration**form:![Develop an Integration form](_images/int-create-integration-scratch.png)  - 
Under **Project Name**, provide the name**New Case Salesforce**.
- 
Under **Project Location**, click**Browse**, and then select your home directory.
- 
Under **Create**, select**Empty Project**.
- 
Select a **Mule runtime**and**Java**version.You can select from locally available Mule runtime and Java versions. The dropdown shows only the Mule runtime versions that are installed on your local disk, including bundled Mule runtime versions that are available immediately after installation. The IDE saves your version settings to the project’s `mule-artifact.json`file. Bundled Mule runtime versions enable instant project opening and design. To install additional Mule runtime versions, use the`MuleSoft: Install Runtime`command. For information about version support and automated Mule patch updates, see[Mule and Java version support](acb-release-notes#versions-mule-jdk). To set default Mule runtime and Java versions for the projects you create, see[Version Settings for Mule, Java, and Connectors](int-versions).
 
- 
- 
Click **Create Project**.Projects open instantly using the bundled Mule runtime versions. The IDE provides a notification only if you must download a specific Mule runtime version or Java version for running or debugging your application. The Mule runtime versions download to `${user.home}/AnypointCodeBuilder/runtimes`, and the selected Java version downloads to`${user.home}/AnypointCodeBuilder/java`.
- 
Proceed to [Create a Configuration File for Slack and Salesforce](tut-slack-create-config-files-sfdc)to create configuration files for connectors.

[Create a Configuration File for Slack and Salesforce](tut-slack-create-config-files-sfdc)