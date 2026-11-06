# Filtering Search Results | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/imp-filter-search-results](https://docs.mulesoft.com/anypoint-code-builder/imp-filter-search-results)

---

![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png) 

# Filtering Search Results

When implementing an API, use the advanced search filters to find API specifications in Exchange.

To search for an API using the search filters:

- 
In the activity bar of the IDE, click the ![](_images/icon-ms-logo.png) ( (**Anypoint Code Builder**) icon.![Anypoint Code Builder icon highlighted in the activity bar](_images/anypoint-code-builder-view.png)  
- 
From **Create**, click**Implement an API**:![Implement an API in the Create menu](_images/implement-api-option-mat.png)  
- 
Select **Show Filters**to display the search filters:![Implement API specification screen with the Show filters label highlighted](_images/imp-api-filters.png)  Anypoint Code Builder supports the following filters for your API assets: - 
Tag Keyword or term that describes a specific search. 
- 
Type The list of asset types depends on which types are available in a business group, such as: - 
GraphQL API A schema definition that contains the object types and definitions used to interact with the API through the GraphQL specification. GraphQL enables you to query an API that supports this language in a much more flexible way than REST. 
- 
REST APIs RAML or OAS files that specify APIs referenced by an HTTP Request connector to expose metadata. 
- 
gRPC API Protocol Buffers (Protobuf) specifications that define gRPC services and methods. Select this type to narrow results when implementing a gRPC API from Exchange. 
 
- 
- 
Category/Industry Specific groupings of assets set by the administrator of a business group or an organization owner. 
- 
Organization Business groups for which you have permission to view their assets. The search filters display the business group from which to retrieve your API in the **Organization**column:![Implement API specification screen with the Organization column highlighted](_images/imp-api-business-group.png)  
 
- 
- 
Click **Add Asset**to add the selected API specification to the Mule application project.