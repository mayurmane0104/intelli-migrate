# Implementing APIs | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/imp-implementing-apis](https://docs.mulesoft.com/anypoint-code-builder/imp-implementing-apis)

---

# Implementing APIs

Use Anypoint Code Builder to start an API implementation by importing and scaffolding an API spec into an interface that you implement and integrate within a Mule app.

Anypoint Code Builder supports automated scaffolding of OAS, RAML, AsyncAPI, GraphQL, and gRPC APIs,
*except for* APIs that reference OAS or JSON schema fragment dependencies from Exchange.

The methods for implementing APIs using Anypoint Code Builder are:

- 
[Scaffold an API from a spec in Exchange](imp-implement-api-specs#scaffold-new-integration)and create a new implementation project.
- 
[Import an API spec](imp-implement-api-specs#import-spec-into-project)from Exchange to scaffold the API in an existing integration project.
- 
[Implement a gRPC API spec](imp-implement-grpc-api-spec)by scaffolding a gRPC (Protobuf) specification from Exchange or a local design project.
- 
[Scaffold an API](imp-implement-local-apis)into an implementation project without first publishing it to Anypoint Exchange, enabling iterative design and implementation.

After scaffolding an API specification into an interface, you are ready to develop, test, and deploy your Mule app as described in [Developing Integrations](int-developing-integrations). For the ordered topics from API design through deployment, see [Take Your API Specification from Design Through Deployment](tutorials#modular-learning-paths).

## Source Control for Implementation Projects

Use source control management (SCM) to store and share your design, integration, and implementation projects.
For source control options, see [Controlling Source Files](start-scm).