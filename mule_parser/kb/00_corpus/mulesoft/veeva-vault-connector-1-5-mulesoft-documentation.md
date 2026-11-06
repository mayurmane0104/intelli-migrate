# Veeva Vault Connector 1.5 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/veevavault-connector/latest](https://docs.mulesoft.com/veevavault-connector/latest)

---

# Veeva Vault Connector 1.5

Anypoint Connector for Veeva Vault (Veeva Vault Connector) enables you to connect Mule flows to the Veeva Vault platform using the Veeva Vault REST API.

Depending on the operations you configure, this connector works with the [Veeva Vault REST, bulk, and streaming APIs](https://developer.veevavault.com/api/19.1/#authentication). Each API call uses a JSON request or a CSV request and returns JSON input stream responses over an HTTPS connection. All required request headers, error handling, and HTTPS connection configurations are built into the connector.

For information about compatibility and fixed issues, see the Veeva Vault Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
Veeva Vault 
- 
[Vault Query Language (VQL)](https://developer.veevavault.com/vql/#introduction-to-vault-queries)
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have:

- 
Credentials to access the Veeva Vault target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases for the Connector

You can use Veeva Vault Connector in Mule applications as an outbound connector with CRUD (create, retrieve, update, delete), query, export, and Spark validator operations on the following Veeva Vault objects:

- 
Documents 
 Create, retrieve, update, delete, export
- 
Document Renditions 
 Create, retrieve, delete
- 
Vault Object 
 Create, retrieve, update, delete
- 
Picklists 
 Retrieve
- 
Audit Trail 
 Retrieve
- 
Query 
 Use a VQL query to query on documents, Vault objects, and workflows
- 
Spark validator 
 Validate and verify the Spark message with a signature that is triggered from Veeva Vault
- 
Invoke Rest API 
 Invoke[Veeva Vault Rest APIs](https://developer.veevavault.com/api/20.1/#documents)in which a specific connector operation does not already exist. To maintain[API rate limits](https://developer.veevavault.com/docs/#api-rate-limits), use bulk APIs instead of single APIs.

## Connection Types

Veeva Vault connections use the Basic authentication type, which uses credentials to connect to a Veeva Vault instance and perform operations.

For information about configuring authentication types, see [Configure a Global Element for the Connector](veevavault-connector-studio#configure-global-element).

## Exchange Templates and Examples

[Anypoint Exchange](https://www.mulesoft.com/exchange/) provides templates
that you can use as starting points for your apps, as well as examples that illustrate a complete solution.

The following templates are available for Veeva Vault Connector:

- 
[File System to Veeva Vault](https://anypoint.mulesoft.com/exchange/org.mule.examples/filesystem-to-veeva-vault-template/)
- 
[Veeva Vault to File System](https://anypoint.mulesoft.com/exchange/org.mule.examples/veevavault-connector-project-templates/)
- 
[Spark Message End-to-End Solution](https://anypoint.mulesoft.com/exchange/org.mule.examples/spark-message-solution-template/)

## Next Step

After you complete the prerequisites, you are ready to create an app and configure the connector using [Anypoint Studio](veevavault-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)