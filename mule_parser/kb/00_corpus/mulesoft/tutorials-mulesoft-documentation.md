# Tutorials | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/tutorials](https://docs.mulesoft.com/anypoint-code-builder/tutorials)

---

# Tutorials

Learn how to design, implement, integrate, and deploy APIs with Anypoint Code Builder. Work through these numbered product topics to move from API specification design to a deployed Mule application. For end-to-end walkthroughs that focus on one scenario each, see [Hands-On Tutorials](#hands-on-tutorials).

## Take Your API Specification from Design Through Deployment

The following topics guide you step by step from API specification design in the IDE to publishing the contract on Anypoint Exchange, building and configuring integration flows, importing and scaffolding the API into a Mule interface, and deploying the application to CloudHub or CloudHub 2.0.

- 
[Designing API Specs and Fragments](des-designing-api-specs)for supported languages and the overall design workflow.
- 
[Creating and Importing API Specifications](des-create-api-specs), including the API Console and mocking service.
- 
Optionally [Creating and Using API Spec Fragments](des-create-api-fragments)for reusable types and examples from Anypoint Exchange.
- 
[Publishing API Projects to Exchange](des-publish-api-spec-to-exchange)so your team can discover and implement the contract.
- 
[Creating Integrations](int-create-integrations)and[Configuring Components](int-configure-components)in your flows.
- 
[Using DataWeave Expressions and Transformations](int-configure-dw-expressions)to map, reshape, or validate data between connectors, processors, and your API layer.
- 
[Implementing OAS, RAML, AsyncAPI, and GraphQL APIs](imp-implement-api-specs)Import your API specification from Exchange, scaffold it into an interface in your project, then wire flows to your implementation. 
- 
[Developing Integrations](int-developing-integrations), including[Debugging Mule Applications](int-debug-mule-apps)and[Deploying Mule Apps to CloudHub and CloudHub 2.0](int-deploy-mule-apps).

## Hands-On Tutorials

Each linked tutorial is a self-contained walkthrough that applies Anypoint Code Builder to one integration style, API technology, or connector story from start to finish.

- 
[Iteratively Design and Implement an API Specification](tut-local-api-specification):Scaffold an API specification into an interface to implement within your IDE, and sync changes to the specification with the interface without first publishing to Anypoint Exchange. For example, after adding a new endpoint to your API specification, you can re-scaffold the change into the interface to add a flow for that endpoint to the interface’s configuration XML file. 
- 
Implement a GraphQL API that you publish to Exchange. 
- 
[Integrate Salesforce Data into Slack and Email Notifications](tut-slack-create-escalation-api):Create an integration that notifies you through email or Slack when a new case is created in Salesforce.