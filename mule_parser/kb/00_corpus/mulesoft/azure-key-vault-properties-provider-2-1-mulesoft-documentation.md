# Azure Key Vault Properties Provider 2.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/azure-key-vault-properties-provider-connector/latest](https://docs.mulesoft.com/azure-key-vault-properties-provider-connector/latest)

---

![Example of a connector using Azure Key Vault Properties Provider in configuration window](_images/properties-provider-example.png) 

# Azure Key Vault Properties Provider 2.1

Azure Key Vault Properties Provider is a configuration that enables you to retrieve your secrets from a secure Azure cloud service before your Mule app runs.

For information about compatibility and fixed issues, refer to the Azure Key Vault Properties Provider Release Notes.

## Before You Begin

To use this properties provider, you must be familiar with:

- 
The Azure Key Vault API 
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
Mule Enterprise Edition 
- 
Credentials to access the Azure Key Vault target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 

## Common Use Cases for the Properties Provider

With Azure Key Vault Properties Provider, secrets can be retrieved in the pre-runtime phase, which means secrets are populated before the Mule app is deployed.

## Connection Types

Connectors can use the Azure Key Vault Properties Provider in their configuration. In the configuration, use the `${azure-key-vault-properties-provider::secret::yourSecret}` structure to retrieve a secret from Azure Key Vault. Here is an example:

![Example of a connector using Azure Key Vault Properties Provider in configuration window](_images/properties-provider-example.png) 

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Salesforce Help](https://help.salesforce.com)