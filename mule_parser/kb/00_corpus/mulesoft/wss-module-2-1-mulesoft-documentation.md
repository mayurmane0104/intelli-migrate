# WSS Module 2.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/wss-module/latest](https://docs.mulesoft.com/wss-module/latest)

---

# WSS Module 2.1

WSS Module enables you to process and validate an inbound SOAP request against a given Web Service Security (WSS) extension configuration to, for example, validate the request’s signature, perform an LDAP authentication, or decrypt the inbound message. WSS Module also enables you to sign your response by adding a WSS header to it, or to encrypt your outbound message.

In version 2.1, the module upgrades the default hashing algorithm from SHA-1 to SHA-256 to enhance cryptographic security and align with FIPS 140-3 approved standards.

For information about compatibility and fixed issues, see the WSS Module Release Notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
The WSS Module API 
- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Studio 

Before creating an app, you must have access to:

- 
The WSS Module target resource 
- 
Anypoint Platform 
- 
Anypoint Studio or Anypoint Code Builder 
- 
Web Services Security (WSS) extension for SOAP 

## Common Use Cases for the Connector

WSS Module enables you to validate WSS headers in inbound SOAP requests to your application to:

- 
Decrypt a SOAP envelope according to the encryption information 
- 
Validate a signature 
- 
Verify the freshness of the message using `timestamp`information
- 
Verify the `Username`and`Password`credentials of`UsernameToken`
- 
Verify the `LDAP`credentials of`UsernameToken`
- 
Determine whether `UsernameToken`is expired
- 
Determine whether a SAML assertion expired 
- 
Verify the signature of a SAML assertion. 
- 
Verify that a SAML assertion has a specific confirmation method. 

Using WSS Module, you can also add WSS headers to your outbound SOAP response to:

- 
Encrypt some or all of your SOAP message content 
- 
Sign your SOAP message 

See the [WSS Module Examples](wss-examples) section for detailed examples.

## Audience

- 
New user To create your Mule app, see: - 
[Studio Configuration](wss-studio)to help extend your understanding of WSS Module.
- 
[Examples](wss-examples), with use case information for the connector
 
- 
- 
Advanced user Read the following: 
- 
[Examples](wss-examples), with use case information for the connector
 

## Next Step

After you complete the prerequisites and experiment with templates and examples, you are ready to create an app and configure the connector using [Anypoint Studio](wss-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[WSS Module on Exchange](https://www.mulesoft.com/exchange/?search=wss-module&type=connector)
- 
[Salesforce Help](https://help.salesforce.com)