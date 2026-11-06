# Step 1. Prerequisites for Building an API-Led Solution | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/api-led-prerequisites](https://docs.mulesoft.com/general/api-led-prerequisites)

---

# Step 1. Prerequisites for Building an API-Led Solution

Set up your environment before starting the tutorial. You need an Anypoint Platform account, Anypoint Code Builder, and a REST client such as Postman. Specific permissions are also required for deployment and, optionally, for AI-assisted API design with MuleSoft Vibes.

- 
Username and password for your Anypoint Platform organization. If you don’t have Anypoint Platform yet, create a Trial organization on Anypoint Platform. [Create a Trial organization](https://anypoint.mulesoft.com/login/#/signup)
- 
[Download and install Visual Studio Code](https://code.visualstudio.com/download)
- 
To test REST requests, obtain a client such as Postman or Advanced REST Client if you don’t already have one. This tutorial uses Postman. [Install Postman](https://www.postman.com/downloads/)Depending on your platform, you might need to install a different client. 
- 
Required permissions: - 
**Anypoint Code Builder Developer**Allows API spec creation 
- 
**Exchange Contributor**Enables publishing assets to Exchange 
- 
**Create Applications**Allows deployment of applications to CloudHub 2.0 
 
- 
- 
Optional permissions (for MuleSoft Vibes AI features): **MuleSoft Vibes**requires Agentforce to be enabled in Access Management. See[Enabling or Disabling Agentforce for Anypoint Platform](../access-management/enabling-agentforce).- 
**Mule Developer Generative AI User**Enables MuleSoft Vibes features for AI-generated API specs. If you don’t have this permission, you can still complete the tutorial by manually creating your API spec. 
 
- 

## Install Anypoint Code Builder

Install the Anypoint Extension Pack in Visual Studio Code to set up Anypoint Code Builder for desktop development.

- 
Open Visual Studio Code. 
- 
Select **View > Extensions**and search for the**Anypoint Extension Pack**.To avoid installation errors, don’t install the individual Anypoint Code Builder extensions that are also available separately from Anypoint Extension Pack in Visual Studio Marketplace. 
- 
Select **Install**.Make sure that the Anypoint extensions update automatically by right-clicking each extension to see if **Auto Update All (From Publisher)**is selected. If it’s not, select**Auto Update**for each extension.
- 
If you have an Anypoint Platform account running in the EU cloud, change the **Mule: Control Plane**setting to**EU cloud**:- 
Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows/Linux) to open the Command Palette. 
- 
Type **Preferences: Open Settings**and select it.
- 
Search for **Mule: Control Plane**.
- 
Change the value to **EU cloud**.If an Anypoint Platform session is active in any of your browsers when you install the Anypoint Extension Pack, the extension pack uses that session to sign in to Anypoint Platform from the IDE. You can log out or sign in from the status bar in the IDE. 
 
- 

## CloudHub 2.0 Setup

For CloudHub 2.0 deployments, you need:

- 
A CloudHub 2.0 Shared Space in your organization. Anypoint Platform trial accounts include a default Shared Space. See [About Shared Spaces](../cloudhub-2/ch2-shared-space-about).
- 
At least one environment (such as Sandbox or Development) configured for CloudHub 2.0 deployments. 

## Helpful Hints

- 
Use two browser windows: one to read instructions and one to perform the tasks. 
- 
In Anypoint Code Builder, enable auto-save to avoid losing work ( **File > Auto Save**).
- 
Bookmark the [Anypoint Platform](https://anypoint.mulesoft.com)login page.

## What’s Next

With your environment ready, the next step is designing your API spec.

[Step 2. Design an API Specification](api-led-design)