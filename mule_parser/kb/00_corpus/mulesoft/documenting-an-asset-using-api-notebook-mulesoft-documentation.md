# Documenting an Asset Using API Notebook | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/to-use-api-notebook](https://docs.mulesoft.com/exchange/to-use-api-notebook)

---

```
```notebook
// Authenticate client
API.authenticate(myclient);
```
```
javascript# Documenting an Asset Using API Notebook

API Notebook lets you document an API’s functionality with explanations that accompany code windows. Users can change the code and execute it by clicking the Play button in each code block. You can create a new API Notebook from the Exchange editor and use JavaScript code in the code blocks.

Use API Designer in Anypoint Platform to improve and test your RAML, OAS, or AsyncAPI API specification, and to publish the API specification to Anypoint Exchange.

| An OAS specification is converted into RAML so you can follow the RAML conventions in API Notebook. Also, the RAMl specification is converted when you upload an OAS. | 

- 
Click the asset to view details. 
- 
Click **Edit documentation**and click the API Notebook icon![API Notebook icon in the editor](_images/ex2-api-notebook-icon.png) in the editor. in the editor.
- 
Add a description for the asset. 
- 
In the Visual editor, the API Notebook icon creates a panel where you can add JavaScript code items. Enter the first letter of the function you want to add and Notebook lists the available functions starting with that letter. If you are using Markdown, each notebook entry is enclosed in a block of 3 tick marks, for example: 

## API Notebook Program Flow for External APIs

If you are accessing an external API such as the Instagram API, fetch the client using the Anypoint Asset
Portal Service at the `https://anypoint.mulesoft.com/exchange/api/v1/health` URL.

The fetch code is:

`fetch('https://anypoint.mulesoft.com/exchange/api/v1/health').then((res) => res.json())`javascriptEnable users to authenticate with the API:

`// Authenticate Instagram. // This asks you to authenticate with your personal account. // Don't worry, we have no idea who you are. API.authenticate(instagramApi);`text

You can then construct your notebook to use the API.

## API Notebook Program Flow for API Manager APIs

- 
Create a client in the notebook to initialize access to your API using the API.createClient function. Syntax: `API.createClient('CLIENT_NAME', 'URL_TO_API_MANAGER_API');`
- 
Authenticate the client with Anypoint Platform using the API.authenticate function. Syntax: `API.authenticate(CLIENT_NAME);`
- 
Create your notebook based on the functionality in your REST API. Each function is based on the names of your RAML descriptor blocks. For example, for the `getdetails`client and with a block called`/info`, to document the GET call, the function description in the notebook is:`getdetails.info.get();`You can add extra parameters to function call with an array, for example: `me.function.post[{ orgId: 'myorg'}) …]`
- 
Test the API in Exchange by setting elements in the code blocks and clicking Play. Ensure all code blocks work without causing errors in the code. 

| The create and authentication calls must be in separate notebook calls:  | 

## Create API Instance

After creating your API Notebook you can optionally create an API instance to control whether the notebook is private or public. By setting the notebook’s instance to private, others in your organization can review it. When you are ready, you can set the API instance to make the API Notebook public. See [Configuring Instances](to-configure-api-settings) for more information about API instances.

| API Notebooks are independent of the use of an API instance. If you don’t use a base URI in your RAML, or use an API instance, you can use the mocking service to generate test data. | 

## API Notebook Security

API notebooks run plain JavaScript in the browser. To ensure sensitive data does not leak, API Notebook disables certain JavaScript functionality:

- 
All global functions, including `alert`and`prompt`
- 
All global variables, including `window`,`document`,`localStorage`, and`XMLHttpRequest`

## See Also

- 
https://docs.mulesoft.com/design-center/v/1.0/upload-raml-task[Upload an Existing RAML File to Exchange].