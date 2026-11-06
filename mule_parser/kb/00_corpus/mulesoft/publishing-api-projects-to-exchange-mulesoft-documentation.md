# Publishing API Projects to Exchange | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/des-publish-api-spec-to-exchange](https://docs.mulesoft.com/anypoint-code-builder/des-publish-api-spec-to-exchange)

---

![Publish API Project to Exchange icon](_images/icon-publish-to-exchange.png) 

# Publishing API Projects to Exchange

Publish your API project to Anypoint Exchange so that other team members can find and use it.

## Before You Begin

Before publishing an API project:

- 
Have some familiarity with [business groups](../access-management/business-groups).When you publish your API spec to Exchange from Anypoint Code Builder, the IDE requests the name of the business group. 

## Publish an API Project to Exchange

To publish your API project to Exchange:

- 
Log in to your Anypoint Platform account. 
- 
In **Explorer**, open your API project and click the Publish API Project to Exchange icon.![Publish API Project to Exchange icon](_images/icon-publish-to-exchange.png)  If you don’t open the project, you can also right-click the API specification and select **Publish API Project to Exchange**.Alternatively: - 
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
Enter `publish`and select the following command:`MuleSoft: Publish API Project to Exchange`command
 
- 
- 
If prompted, click **Allow**, and follow the prompts to sign in to Anypoint Platform.
- 
Confirm or change each item in **Publish API Project to Exchange**:- 
**Asset Version**
- 
**API Version**If the API project has never been published to Exchange, the default version is `1.0.0`.The API version isn’t required for API fragments. 
- 
**Business Group**If you selected a business group when you created the API project, this field isn’t shown in the form. You can view and update the business by expanding **Project Metadata**.
 
- 
- 
Optionally, expand **Project Metadata**and click**API Project Properties**to update metadata for the API project, such as updating the asset name and ID and adding tags and categories, updating the business group, and so on. For more information, see[Add Metadata to the API Project](ai-enabling-api-project-topic-center#add-metadata).- 
After you complete your updates, click **Apply**.
 
- 
- 
In the banner click **Sync centralized governance rulesets and run validation**to ensure the API project conforms to the applied rulesets.This step is optional, but it’s recommended as a best practice. You must be logged in to your Anypoint Platform account and have a business group defined in the API project metadata to validate rulesets. ![Publish API Project to Exchange form with banner to sync centralized rulesets](_images/des-publish-api-project.png)  
- 
Click **Publish**.When publishing is complete, you see a message that the API specification successfully published to Exchange. If the API project has errors, you must fix the errors before you can publish to Exchange. Errors are listed in the **Problems**tab. Click the Publish API Project to Exchange icon to bring the**Problems**tab into focus.
- 
Click **View Asset**to see the published asset in Exchange.
- 
When prompted to implement the API, select one of the following: - 
**No**to avoid scaffolding the API specification into your integration.
- 
**Yes**to scaffold the API specification into a new project.## Show me how- 
In the field that opens, provide a name for your implementation project. 
- 
Navigate to a directory for your project, and click **Select target folder**.
- 
Select a Mule runtime (Mule) version for your project. 
- 
Select a supported Java version for Mule. 
- 
After the scaffolding process completes, view the scaffolded interface for your project from the `src/main/mule`directory in the Explorer.If the scaffold fails, see [Implementation Errors](troubleshoot-implementation-errors).You can also open your new project’s `mule-artifact.json`file from the Explorer to check the Mule and Java versions, for example:`{ "minMuleVersion": "4.6.2", "javaSpecificationVersions": [ "11" ] }`XMLThe `mule-artifact.json`file is located at the root level of the project directory.
 
- 
 
- 

## Locate Your API in Exchange

After publishing your API specification, you can find it in Anypoint Exchange:

- 
Navigate to Anypoint Platform and log in using your credentials. ## Show me how- 
US cloud (non-EU host): [Anypoint Platform (US)](https://anypoint.mulesoft.com/login/)
- 
EU cloud (EU host): [Anypoint Platform (EU)](https://eu1.anypoint.mulesoft.com/login/)
 
- 
- 
Navigate to Anypoint Exchange. ## Show me how- 
US cloud (non-EU host): [Exchange (US)](https://anypoint.mulesoft.com/exchange/)
- 
EU cloud (EU host): [Exchange (EU)](https://eu1.anypoint.mulesoft.com/exchange/)
 Your API specification appears as an asset in your organization, for example: ![API specification in Exchange](_images/des-api-exchange.png)  
- 

You can select the API, navigate through its summary, and see all the endpoints you defined in the previous tasks. You can also generate documentation for REST APIs without documentation on the asset details page in Exchange. For more information, see [Generating API Documentation with Einstein Generative AI](https://docs.mulesoft.com/exchange/generating-documentation-with-ai).

## Publish a GraphQL API Spec to Exchange

To publish a GraphQL API specification to Exchange:

- 
Navigate to Anypoint Platform and log in using your credentials. ## Show me how- 
US cloud (non-EU host): [Anypoint Platform (US)](https://anypoint.mulesoft.com/login/)
- 
EU cloud (EU host): [Anypoint Platform (EU)](https://eu1.anypoint.mulesoft.com/login/)
 
- 
- 
Navigate to Anypoint Exchange. ## Show me how- 
US cloud (non-EU host): [Exchange (US)](https://anypoint.mulesoft.com/exchange/)
- 
EU cloud (EU host): [Exchange (EU)](https://eu1.anypoint.mulesoft.com/exchange/)
 
- 
- 
Click **Publish new asset**:![Publish new asset button in Exchange](_images/des-publish-asset-exchange.png)  
- 
Complete the **Publish a new asset**form:![Publish a new asset form on Exchange](_images/des-graphql-publish-exchange.png)  - 
For **Name**, type a name for your asset.
- 
For **Asset types**, select**GraphQL API**.
- 
For **Method**, select**Upload a GraphQL API Schema**.
- 
For **File upload**, click**Choose file**and browse for your`.graphql`schema file.
- 
Click **Advanced**to change the version number.
- 
For **Lifecycle state**, select**Stable**.
 
- 
- 
Click **Publish**.

Your GraphQL API spec is now available on Exchange, for example:

!["GraphQL API spec on Exchange](_images/des-graphql-asset-exchange.png)