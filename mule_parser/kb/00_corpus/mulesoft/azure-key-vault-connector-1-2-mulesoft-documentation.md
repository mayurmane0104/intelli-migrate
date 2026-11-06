# Azure Key Vault Connector 1.2 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/azure-key-vault-connector/latest](https://docs.mulesoft.com/azure-key-vault-connector/latest)

---

# Azure Key Vault Connector 1.2

Anypoint Connector for Azure Key Vault (Azure Key Vault Connector) enables you to retrieve secrets, keys, or certificates, and encrypt or decrypt content.

For information about compatibility and fixed issues, refer to the Azure Key Vault Connector Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The Azure Key Vault Secrets API 
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
Credentials to access the Azure Key Vault target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases for the Connector

Some common use cases for Azure Key Vault Connector include:

- 
Authenticating to Azure Key Vault via Client Secret Credential to access Key Vault secrets without exposing sensitive credentials in code, thus improving resilience and security 
- 
Enabling other applications in a Mule flow to have access to encrypt and decrypt operations using Azure Key Vault keys to avoid key rotations 
- 
Authenticating to other database and HTTP connectors in a more secure and automated way to fetch and use credentials to access other endpoints 
- 
Retrieving a certificate and saving the certificate into a file 

## Connection Types

Azure Key Vault connections use the Connection authentication type, which uses a client ID, client secret, and cryptography client cache.

## Environment Variables

When setting **Use Azure Default Credential** to `True`, you must set one of the following environment variables `AZURE_CLIENT_ID`, `AZURE_CLIENT_SECRET`, or `AZURE_TENANT_ID`. Refer to [Setting environment variables](../../mule-runtime/latest/setting-environment-variables) documentation for details.

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)