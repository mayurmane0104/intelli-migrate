# Configure API Autodiscovery for Local Testing | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/int-configure-api-autodiscovery-local](https://docs.mulesoft.com/anypoint-code-builder/int-configure-api-autodiscovery-local)

---

`<api-gateway:autodiscovery apiId="${api.instance.id}" flowRef="<YOUR_MAIN_FLOW_NAME>" />`xml# Configure API Autodiscovery for Local Testing

Configure **API Autodiscovery** to connect your local Mule application to an API instance in [API Manager](../api-manager/latest/latest-overview-concept). This setup enables local policy testing before you deploy the application.

## Before You Begin

Ensure you have:

- 
An active API instance in API Manager 

## Get the API ID

- 
In Anypoint Platform, open **API Manager**.
- 
In **API Administration**, select your API instance.
- 
On the API summary page, copy the **API Instance ID**.

## Add the Autodiscovery Element

In your Mule app, add the autodiscovery element in your flow definitions. Use a property reference for `apiId` so you can load the value through configuration:

## Configure Local Credentials

For local execution in Anypoint Code Builder, provide your environment credentials through `config.yaml` or through Mule runtime arguments in VS Code settings. Avoid hardcoding secrets in Mule XML files.

Set these properties:

- 
`anypoint.platform.client_id`
- 
`anypoint.platform.client_secret`

Example `config.yaml`:

```
api.instance.id: "<YOUR_API_ID>"
anypoint.platform.client_id: "<YOUR_ENV_CLIENT_ID>"
anypoint.platform.client_secret: "<YOUR_ENV_CLIENT_SECRET>"
```
yamlExample Mule runtime arguments:

`-M-Danypoint.platform.client_id=<YOUR_ENV_CLIENT_ID> -M-Danypoint.platform.client_secret=<YOUR_ENV_CLIENT_SECRET>`text

To add these values in Anypoint Code Builder:

- 
Open the **Settings**tab.## Show me how- 
From the Anypoint Code Builder panel, click the ![](_images/icon-settings-gear.png) (gear) icon. (gear) icon.
- 
From the activity bar, click the ![](_images/icon-settings-gear.png) (gear) icon, select (gear) icon, select**Settings**, and search for`mule`in the**Settings**tab.
- 
Provide the command `MuleSoft: Open ACB Settings`in the[Command Palette](start-use-command-palette).
 
- 
- 
In the **Settings**tab, find**Mule › Runtime: Default Arguments**.
- 
Append the client ID and client secret arguments to the end of the existing arguments. 

Append the placeholder values with your client ID and client secret.