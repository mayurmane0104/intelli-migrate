# Simulating Data in REST APIs | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/ex2-to-simulate-api-data](https://docs.mulesoft.com/exchange/ex2-to-simulate-api-data)

---

![API Console showing the mocking service](_images/exchange-rest-api-mocking-service.png) 

# Simulating Data in REST APIs

Exchange lets you provide simulated data for testing OAS or RAML REST APIs. The simulated data is provided in the mocking service feature.

The following example shows how the mocking service simulates the data for a REST API:

- 
In the API console that appears on the right side of an asset detail screen. The mocking service lets you add simulated data to an API function and test the API with the data. ![API Console showing the mocking service](_images/exchange-rest-api-mocking-service.png)  This page shows two URLs. The URL on the left is also used in Design Center and is public. The URL on the right is used only in Exchange and requires authentication. 
- 
Listed as an instance with each version of an API. ![A table of patch versions for 1.0 with mocking instances](_images/exchange-patch-version-mocking.png)  
- 
Listed on the **API instances**page that also lists the mocking service URL.![A table of API instances, their corresponding environments, URLs, and visibility](_images/ex2-api-instances.png)  

## Accept Simulated Data in an API

- 
From Design Center > API Specification, provide example data that the implementation returns. Alternatively, you can develop an OAS (Swagger) specification from a text editor and add the example data there. 
- 
In the REST specification provide an HTTP status code for a successful API call. 

## Test a REST API With Simulated Data

- 
In Exchange, click a REST API. 
- 
Click a function such as **GET**.
- 
In the API console on the right of the screen, click **Send**to send simulated data to the API.Exchange sends the data and lists the response, which in this example returns the HTTP 200 OK status to indicate success, and lists the data that is sent from the API using the simulated data.