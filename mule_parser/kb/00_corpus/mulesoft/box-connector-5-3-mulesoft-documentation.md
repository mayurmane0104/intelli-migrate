# Box Connector 5.3 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/box-connector/latest](https://docs.mulesoft.com/box-connector/latest)

---

# Box Connector 5.3

Box is an online file sharing and content management service for businesses. Anypoint Connector for Box (Box Connector) is a RAML-based connector that provides synchronization of data and automation of processes between Box and third party CRMs, CMS, mobile, and social applications. Because this is a RAML-based connector, it only uses REST calls to interact with the Box 2.0 API and supports only a subset of available API services.

## Before You Begin

Before creating an app, you must have access to the Box target resource and Anypoint Platform. You must also understand how to create a Mule app using Anypoint Studio.

You should be familiar with the use of the Box 2.0 API, Mule, Anypoint Connectors, Anypoint Studio, Mule concepts, elements in a Mule flow, and global elements.

To use this connector you need the following:

- 
A developer account or other valid Box instance. 
- 
MuleSoft Enterprise License and necessary entitlements. 

## Connection Types

Box Connector uses the following authentication types:

- 
JWT 
 Server-side authentication using a keypair. For more information about configuring Box Connector with JWT, refer to[JWT Authentication](box-connector-config-topics#jwt).
- 
Oauth2security 
 Access tokens provided by the authorization server.

## Next Step

After you complete the prerequisites, you are ready to create an app with [Anypoint Studio](box-connector-studio).

## See Also

- 
[Use Exchange to Discover Connectors, Templates, and Examples](../../connectors/introduction/intro-use-exchange)
- 
[Box Connector on Exchange](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-box-connector/)
- 
[Salesforce Help](https://help.salesforce.com)