# Setting Up Integration Intelligence | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/integration-intelligence-setup](https://docs.mulesoft.com/monitoring/integration-intelligence-setup)

---

![Salesforce admin flow for setting up Integration Intelligence](../access-management/_images/ii-salesforce-admin-flow.png) 

# Setting Up Integration Intelligence

[Advanced and Titanium tiers](/monitoring/#billing)

Integration Intelligence enhances monitoring, analysis, and troubleshooting of MuleSoft integrations through AI-powered capabilities.

## Before You Begin

Before enabling Integration Intelligence in your Anypoint Platform organization, you must have:

- 
An Anypoint Platform Integration Advanced or legacy Titanium package. 
- 
Salesforce Enterprise, Performance, or Unlimited edition. 
- 
A Tableau Next license. 
- 
Administrative access to an Anypoint Platform organization that isn’t a trial organization and isn’t expired. 
- 
Administrative access to a Salesforce organization. 
- 
[A tenant relationship](../access-management/trusted-salesforce-org)between your Anypoint Platform organization and a trusted Salesforce organization established.The connected Salesforce organization must have Data 360 and Tableau Next enabled. For more information, see [Tableau Next Setup Guide](https://help.tableau.com/current/online/en-us/tableau_next_setup_guide.htm).
- 
Agentforce enabled in the connected Salesforce organization and your Anypoint Platform organization. For more information, see [Enabling or Disabling Agentforce for Anypoint Platform](../access-management/enabling-agentforce).
- 
To avoid installation failures while testing through your Salesforce sandbox organization, make sure that your Single source of truth (SSOT) package version is v1.120 or later. For more information, see [Verify the SSOT Package Version in Data Cloud](https://help.salesforce.com/s/articleView?id=ind.cg_tpm_data_cloud_verify_ssot.htm&type=5).

## Integration Intelligence High-Level Flow

After the Anypoint Platform organization administrator establishes a connection between the Anypoint Platform organization and the Salesforce organization, the Salesforce admin sets up Integration Intelligence in the Salesforce organization.

This diagram shows the high-level flow for the Salesforce and Anypoint Platform organization administrators to set up Integration Intelligence in the Salesforce org.

![Salesforce admin flow for setting up Integration Intelligence](../access-management/_images/ii-salesforce-admin-flow.png) 

- 
Log in to your Salesforce organization. 
- 
In Salesforce Setup, enter `MuleSoft`in the**Quick Find**box, then select**MuleSoft > Integration Intelligence**.
- 
On the **Integration Intelligence Setup Assistant**page, follow the setup steps in order:
- 
The Anypoint Platform organization administrator now completes the setup steps to enable Integration Intelligence in Anypoint Platform. 
- 
After the Anypoint Platform organization administrator completes the setup steps in Anypoint Platform, the Salesforce admin completes the rest of the Integration Intelligence setup in the Salesforce org. - 
[Enable Seamless Login](#enable-seamless-login)for Anypoint Platform users to access Tableau Next dashboards in Salesforce.
 
- 

## Set up Salesforce Data 360

Connect your Salesforce organization to Data 360. Data 360 is the storage and processing layer for Integration Intelligence. It ingests MuleSoft telemetry data from your selected business group into a Data 360 data space.

- 
In the **Data Cloud**section, click**Setup**.For information about setting up Data 360, see [Get Started with Data 360](https://help.salesforce.com/s/articleView?id=data.c360_a_product_considerations.htm&type=5).

## Complete the Connection with Anypoint Platform

Complete the connection between your Salesforce organization and Anypoint Platform so Salesforce can ingest MuleSoft telemetry data from your selected business group into Data 360.

- 
From **Setup**, in the Quick Find box, enter`MuleSoft`, and then select**MuleSoft > Anypoint Platform Setup**.
- 
On the **MuleSoft Anypoint Platform Setup**page, click**Complete the Connection**.
- 
Copy your Salesforce org tenant key. The format for the Salesforce tenant key is `cloud/env/org-id`.
- 
Sign in to Anypoint Platform using an account that has the root Organization Administrator permission. 
- 
Select **Access Management**from the image::access-management::gear.svg["gear icon",20] menu.
- 
Select **Salesforce**.
- 
Click **Add Salesforce Org**.
- 
In **Add the Salesforce Org**, paste the Salesforce org tenant key, and click**Add**.
- 
Enter the name of the Salesforce org in **Name Used in Anypoint Platform**, and click**Add**.Anypoint Platform generates and provides the organization key (or tenant key) in the format `cloud/env/org-id`.
- 
Click **Copy**to copy the Anypoint Platform organization key.
- 
Return to the **MuleSoft Anypoint Platform Setup**page in the Salesforce organization.
- 
Enter the Anypoint Platform organization key in **Anypoint Platform Organization ID**, and then click**Connect**.You return to the **MuleSoft Anypoint Platform Setup**page. The page shows the connected Anypoint Platform organization details.

## Enable Telemetry Data

Enable telemetry data to stream logs and metrics from your Mule apps and APIs into the selected Data 360 data space.

- 
In Salesforce Setup, in the **Quick Find**box, enter`MuleSoft`, then select**MuleSoft Observability**.
- 
In **MuleSoft Observability**, switch**Telemetry Data Ingestion for Integration Intelligence**to**Active**.
- 
Return to Anypoint Platform **Access Management > Salesforce**.
- 
In **Capability enablement**for the connected Salesforce organization, switch**You can’t bring telemetry data into Salesforce Data Cloud**to**Enabled**.
- 
In **Enable Telemetry Data Ingestion**, select the business group that contains the apps that will send telemetry data to Data 360, and then click**Next**.The business group you select for data ingestion can’t be changed after you save the settings. 
- 
In **Select Applications**, select the environment.A list of applications in the selected environment appears. The application selection list includes specific versions of Mule on CloudHub 2.0 and Runtime Fabric. The list of selectable apps isn’t inclusive of all the apps in the selected business groups. For other deployments (CloudHub, Mule Gateway, Omni Gateway), or some earlier versions of Mule, telemetry data ingestion is automatically enabled and excluded from the selection list. 
- 
Select the applications to ingest telemetry data for, and click **Enable Data Ingestion**.You can search for applications by name and you can also select **Show only applications available for selection**to filter the list and show only applications that use the latest runtime versions.The settings are saved. Any subsequent changes made to Integration Intelligence in Access Management are automatically shared with the connected Salesforce organization. For example, turning off the Integration Intelligence feature in Anypoint Platform disables: - 
Trust with the connected Salesforce organization. Turning it back on restores trust and enables data ingestion for the selected business group. 
- 
Seamless login for Anypoint Platform users to access Tableau Next dashboards in Salesforce. Turning it back on restores seamless login. 
 
- 

## Enable Seamless Login for Anypoint Platform Users

The Salesforce admin enables seamless login for Anypoint Platform users to access Tableau Next dashboards in Salesforce without needing to create new credentials or perform additional login steps.

- 
If you aren’t logged in, log in to Salesforce. 
- 
In Salesforce Setup, enter `MuleSoft`in the**Quick Find**box, then select**MuleSoft > Anypoint Platform Setup**.
- 
Switch the **Enable Seamless Login from Anypoint Platform**option to**Enabled**.This option is available after the Anypoint Platform organization administrator completes all their setup steps in Anypoint Platform. If you don’t see the option, contact your Anypoint Platform organization administrator. 

## Install Integration Intelligence

The Salesforce admin installs Integration Intelligence in the Salesforce org.

| This step is available only after the Anypoint organization administrator completes all the Anypoint Platform setup steps. | 

- 
In Salesforce Setup, enter `MuleSoft`in the**Quick Find**box, then select**MuleSoft > Integration Intelligence Setup Assistant**.
- 
In **Install Integration Intelligence**, click**Setup**.The setup steps appear. If a step isn’t complete, click **Setup**to complete it. All the steps must be completed before you can install Integration Intelligence.
- 
Select **Setup**for**Install Integration Intelligence**.
- 
In **Data Space**, select the data space to use for Integration Intelligence.This is the data space where your observability data will be stored and processed and must match the data space where telemetry data is ingested. 
- 
Click **Next**.
- 
In **App Details**, enter a name and description for the Integration Intelligence app, and then click**OK**.After the Integration Intelligence app is successfully installed, you see a **Success**status and the name of the app is shown on a tab in the**Integration Intelligence Setup**page.

## Next Steps

[Use dashboards](integration-intelligence-dashboards) in the Salesforce ecosystem to monitor Mule app and API metrics, and get insights into related business data.