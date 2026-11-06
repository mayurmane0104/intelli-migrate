# Designing a gRPC API Specification with Anypoint Code Builder | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/des-design-grpc-api-spec](https://docs.mulesoft.com/anypoint-code-builder/des-design-grpc-api-spec)

---

**Project Name**

# Designing a gRPC API Specification with Anypoint Code Builder

Anypoint Code Builder supports designing gRPC API specifications using Protocol Buffers 3 (Protobuf 3). Create and edit `.proto` files, import reusable Protobuf libraries from Anypoint Exchange, and use syntax highlighting and validation. gRPC uses HTTP/2 and supports four RPC patterns:

- 
Unary 
- 
Client streaming 
- 
Server streaming 
- 
Bidirectional streaming 

You author service and message definitions in `.proto` files and can reuse shared types by importing Protobuf fragments (libraries) from Exchange.

## Before You Begin

- 
Understand the basics of gRPC and Protocol Buffers (Protobuf 3). See [Introduction to gRPC](https://grpc.io/docs/what-is-grpc/introduction/)and the[Protocol Buffers 3 Language Guide](https://protobuf.dev/programming-guide/proto3/).
- 
Have some familiarity with [Anypoint Platform Business Groups](../access-management/business-groups).

## Create a New gRPC API Specification Project

To create a gRPC API spec project in Anypoint Code Builder:

- 
In the activity bar of the IDE, click the ![](_images/icon-ms-logo.png) ( (**Anypoint Code Builder**) icon.
- 
From **Create**, click**Design an API**:
- 
Complete the **API Specification**form:Field Name Field Value Unique name for your project. This name is used as the API spec title in Exchange, the name of the spec file, and the name of the project’s root directory. To reuse an existing project name, you must delete the project that is already using the name first. See [Deleting API Specs and Fragments](des-delete-api-projects).**Project Location**Your home directory or another directory you create. Don’t create the project within another project directory. **API Type**The type of API spec to create. Select **gRPC API**to create a gRPC project.**API Specification Language**The language for the API specification. Select **Protobuf 3**for gRPC API projects.
- 
Click **Create Project**.If prompted, trust the authors of the files in the folder. When the project is ready, the API project opens with a default `.proto`file in the Editor view.
- 
Continue designing your gRPC API spec. As you enter elements, use [auto-complete](start-discover-ui#auto-complete)(or press Ctrl+Space) to display available options within the context.

## Organize gRPC API Projects and Dependencies

A new gRPC API project includes a root `.proto` file (for example, `main.proto` or a file named after your project) that defines your service and messages.

Edit the main `.proto` file to define `service`, `rpc`, and `message` blocks. To reuse shared types, add new `.proto` files in the same project and import them. You can also add a Protobuf fragment as a dependency from Exchange and import it in your specification.

## Publish a gRPC Fragment to Exchange

Publish reusable `.proto` definitions as a fragment to Anypoint Exchange so other gRPC API specifications can import them as dependencies.

A fragment contains shared definitions such as `message` or `enum` blocks.

### Publish the Fragment

To publish a gRPC fragment to Exchange:

- 
Ensure that you’re logged in to Anypoint Platform. 
- 
Open the project that contains your reusable `.proto`files.
- 
From the IDE, select the publish action. 
- 
When prompted: - 
Select the business group. 
- 
Provide the asset name and version. 
- 
Add any required metadata. 
 
- 
- 
Confirm the publication. 

After publishing, the fragment appears in Exchange as an API Fragment asset and can be added as a dependency to other gRPC API specification projects.

To use the fragment in another gRPC API specification:

- 
Add the fragment as a dependency from Exchange. 
- 
Import the corresponding `.proto`file in your main specification.
- 
Validate that all references resolve correctly. 

## Import a Protobuf Library from Anypoint Exchange

Import reusable Protobuf libraries (fragments) from Anypoint Exchange and add them as dependencies to your gRPC API project. You can reuse messages and services across multiple specifications.

To use a Protobuf fragment published to Exchange:

- 
Ensure you’re logged in to Anypoint Platform. 
- 
Open your gRPC API project. 
- 
Open the Command Palette (Cmd+Shift+P on macOS or Ctrl+Shift+P on Windows). 
- 
Select **MuleSoft: Add Fragment dependency from Exchange**.
- 
Search for the Protobuf fragment you need and select the version to add. 
- 
After the dependency is added, the library is available under the project. 
- 
In your main `.proto`file, use`import`to reference the library’s package and message or service definitions. For example:`syntax = "proto3"; import "path/to/library.proto"; service MyService { rpc GetOrder(OrderRequest) returns (OrderResponse); }`protobuf
- 
Save the spec. Anypoint Code Builder resolves the dependency and validates references. You can reuse messages and services from the imported library across your gRPC specs. 

## Define Technical Details for gRPC Specifications

Specify RPC communication patterns in your service definitions and use built-in validation to verify your Protobuf specification.

### Declare Communication Patterns for gRPC Services

Anypoint Code Builder and Mule runtime support all four gRPC RPC patterns:

- 
**Unary**– Single request, single response.
- 
**Client streaming**– Client sends a stream of messages; server returns a single response.
- 
**Server streaming**– Client sends a single request; server returns a stream of messages.
- 
**Bidirectional streaming**– Both client and server send and receive streams of messages.

Define these in your `.proto` file using the appropriate `rpc` declarations and stream modifiers.

### Verify Specification Accuracy with Syntax Validation

Anypoint Code Builder provides syntax highlighting and validation for Protobuf 3 specifications. Validation is performed using the API Modeling Framework (AMF) parser, so you get inline feedback and error reporting as you edit your `.proto` files. Use the editor and the [output panel](start-open-output-panel) to track validation and scaffolding status.