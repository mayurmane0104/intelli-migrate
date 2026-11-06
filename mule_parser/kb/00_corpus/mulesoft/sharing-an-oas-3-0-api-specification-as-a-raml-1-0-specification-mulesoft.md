# Sharing an OAS 3.0 API Specification as a RAML 1.0 Specification | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/design-center/design-share-oas3-as-raml](https://docs.mulesoft.com/design-center/design-share-oas3-as-raml)

---

# Sharing an OAS 3.0 API Specification as a RAML 1.0 Specification

You can share an OAS 3.0 API specification in Anypoint Exchange as a RAML API specification. Other developers can then download the RAML version for use in Anypoint Studio or third-party IDEs or for implementation with API Manager.

- 
Import the OAS 3.0 API specification into API Designer. 
- 
Click the three dots next to the filename in the **Files**pane and select**Duplicate**.
- 
In the **Duplicate As**dialog, select**RAML**.
- 
Set the root file of the project to the RAML version of the API specification. 
- 
Publish the project to Anypoint Exchange. 

| If you want to share an OAS 3.0 specification in OAS 2, download your OAS 3.0 specification from API Designer as-is and then convert it to OAS 2.0 by using a tool such as APIMatic transformer. |