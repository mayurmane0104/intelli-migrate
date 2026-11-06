# Informatica Business 360 Connector 1.0 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/informatica-b360-connector/latest](https://docs.mulesoft.com/informatica-b360-connector/latest)

---

# Informatica Business 360 Connector 1.0

| Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. | 

Anypoint Connector for Informatica Business 360 (Informatica Business 360 Connector) enables Mule applications to integrate with the Informatica Business 360 (MDM) REST API. Use this connector to manage master data records, perform searches, run ML-based fuzzy matching, and discover business object metadata, all from within your Mule flows.

For information about compatibility and fixed issues, refer to the Informatica Business 360 Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Informatica Business 360 Connector’s API 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Code Builder or Anypoint Studio 

Before creating an app, you must have:

- 
Credentials to access the Informatica Business 360 target resource 
- 
Anypoint Platform 
- 
The latest versions of Anypoint Code Builder or Anypoint Studio 
- 
Access to an Informatica Business 360 (MDM) environment with valid credentials 
- 
At least one business entity configured in your B360 tenant (for example, `c360.person`)

## Supported Authentication Methods

This connector supports two Informatica API authentication versions:

| Method | Description | 
|---|---|
| Basic Auth V3 | Authenticates via the V3 login endpoint ( | 
| Basic Auth V2 | Authenticates via the V2 login endpoint ( | 

## Key Capabilities

- 
Entity CRUD Operations Create, read, update (full and partial via JSON patch), delete, and restore business entity records such as persons, organizations, and custom entity types. 
- 
Search with Automatic Pagination Perform full-text or field-based searches across entity records. The connector handles pagination transparently, fetching pages on demand as your flow iterates over results. 
- 
ML-Based Fuzzy Matching Find similar records using Informatica’s match engine. Search Match V1 matches against source records using blocking fields defined in the match model. 
- 
Metadata Discovery The connector dynamically retrieves available business entity types and source systems from the B360 tenant. Anypoint Studio and Anypoint Code Builder display dynamic dropdowns for object types and source systems. 
- 
Dynamic Input and Output Metadata The connector dynamically resolves input and output schemas at design time based on the selected business object type, providing field-level autocompletion in Anypoint Studio and Anypoint Code Builder. Dynamic input and output metadata for the operation is cached and is automatically refreshed once every 10 minutes. 
- 
Automatic Session Management The connector manages the session token lifecycle automatically, including proactive refresh before the 30-minute expiration window and transparent retry on 401 (Unauthorized) responses. 
- 
Error Handling Hierarchy Structured error types ( `CLIENT_ERROR`,`SERVER_ERROR`,`CONNECTIVITY`) with specific subtypes (`NOT_FOUND`,`BAD_REQUEST`,`RATE_LIMITED`, etc.) enable precise error handling in your flows.
- 
Debug Logging When the connector logger is set to `DEBUG`level, HTTP request and response details are logged automatically with sensitive data masked. No separate configuration is required.

## Connection Management

The connector uses a cached connection model (`CachedConnectionProvider`), meaning a single connection is shared across all operations within a Mule app. The session token is proactively refreshed on a configurable interval (default: 25 minutes) to avoid mid-request expiration.

If a request receives a 401 (Unauthorized) response, the connector automatically refreshes the session token and retries the request once before propagating the error.

## Next Step

After you complete the prerequisites, you’re ready to create an app and configure the connector using [Anypoint Studio](informatica-b360-connector-studio) or [Anypoint Code Builder](informatica-b360-connector-acb).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)