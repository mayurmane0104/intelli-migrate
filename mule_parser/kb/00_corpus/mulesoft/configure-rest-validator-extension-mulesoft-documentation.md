# Configure REST Validator Extension | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/rest-validator-extension](https://docs.mulesoft.com/api-manager/latest/rest-validator-extension)

---

```
<dependency>
		     <groupId>com.mulesoft.anypoint</groupId>
		     <artifactId>mule-rest-validator-extension</artifactId>
		     <version>${restValidatorVersion}</version>
		     <classifier>mule-plugin</classifier>
</dependency>
```
XML# Configure REST Validator Extension

The REST validator extension enables you to perform schema validations that use a RAML or OAS specification against the attributes of a request. Additionally, the extension adds default values to attributes, if they are already not set in the request.

Unless otherwise noted, this documentation applies only to REST validator extension v2.x. To use the REST validator extension in your Mule artifact, such as a Mule runtime engine (Mule) application XML, you must:

## Include Dependencies in Your pom.xml File

You can include the REST validator in your Mule artifact (for example, Mule application XML) by adding the following snippet in the `<dependencies>` section of your `pom.xml` file:

As a best practice, define a Maven property inside the `<properties>` section, with the version of the REST validator that you want to use:

```
<properties>
<restValidatorVersion>2.1.3</restValidatorVersion>
</properties>
```
XML## Add Namespace and Schema to Your Mule Artifact

To use the REST validator operations in your Mule artifact, include the following namespace and schema:

`xmlns:rest-validator="http://www.mulesoft.org/schema/mule/rest-validator" xsi:schemaLocation="http://www.mulesoft.org/schema/mule/rest-validator http://www.mulesoft.org/schema/mule/rest-validator/current/mule-rest-validator.xsd"`text

## Configure the REST Validator Extension

To configure the REST validator extension, add the following syntax in your Mule artifact:

`<rest-validator:config name="validatorConfig" api="${specFile}"/>`

This snippet contains the required attributes for configuration. You can specify [additional attributes](#config-reference) to customize the extension. The following example illustrates how to use attributes deserializing strategies:

```
    <rest-validator:config name="configValidator" api="${specFile}" keepApiBaseUri="true">
        <rest-validator:attributes-deserializing-strategies arrayHeaderDelimiter="COMMA"/>
    </rest-validator:config>
```
XML## Use the REST Validator Operation

After you configure the REST validator, you can start using the validator operation:

**Operation Name**

`validate-request`

**Description**

Validates a request against the specified RAML or OAS specification in the configuration.

**Usage Example**

`<rest-validator:validate-request config-ref="validatorConfig"/>`

**Attributes Description**

The following table lists the attributes and provides their descriptions:

| Attribute | Description | Required? | 
|---|---|---|
| 
 | A DataWeave expression that extracts the attributes to validate. Default value: #[attributes] | No | 
| 
 | A DataWeave expression that extracts the payload to validate. Default value: #[payload] | No | 
| 
 | A REST validator configuration. | Yes | 

**Output**

If the request does not violate the defined schema, the validation ends successfully and the result of the operation does not modify the HTTP request attributes. Conversely, default values are added to the schema validation and the output includes the original and new HTTP request attributes.

**Error Types**

The `validate-request` operation might raise different errors if a problem occurs when retrieving a file or if the validation does not end successfully:

- 
`REST-VALIDATOR:BAD_REQUEST`Error raised when some of the attributes do not match with the schema. The attributes that are considered during the validation include: - 
Form parameters 
- 
Headers 
- 
Query parameters 
- 
URI parameters 
 
- 
- 
`REST-VALIDATOR:METHOD_NOT_ALLOWED`Error raised when the schema does not support a particular method for the required resource. 
- 
`REST-VALIDATOR:RESOURCE_NOT_FOUND`Error raised when the root schema or some related file cannot be retrieved. 

## REST Validator Extension Configuration Reference

The following table describes the attributes that you configure for your validator extension:

| Attribute | Description | Required? | 
|---|---|---|
| 
 | A unique identifier for your configuration. | Yes | 
| 
 | If you are using a version of the REST validator later than 2.0.0, you must use the  | Yes | 
| 
 | The parser used to validate the requests: 
 | No | 
| 
 | Specifies whether you can override the  If you are using a REST validator version that is later than 2.0.0, use the  | No | 
| 
 | Validates whether all the query parameters in the request are defined in the specification file. If some of the parameters are not specified, the validation fails. The default value is  | No | 
| 
 | Validates whether all the required headers defined in the specification are defined in the request. If some of the parameters are not specified, the validation fails. The default value is  | No | 
| 
 | Allows parsing of the HTTP headers that contain an array of values that are separated by commas. | No | 

## REST Validator and APIkit Compatibility Reference

You can share the REST validator (`pom.xml` dependency) across applications by using a domain. However, if some of those applications also have a dependency on APIkit, that version of APIkit in each application must match the one required by the REST validator version that you use in your domain.

Per the following table of compatibilities, for example, if you use the REST validator v2.2.0 in your domain, all your applications using APIkit must import the 1.4.2 version:

| Rest Validator Version | APIkit REST Module Version | 
|---|---|
| 2.2.4 | 1.9.0 | 
| 2.2.3 | 1.8.3 | 
| 2.2.2 | 1.7.0 | 
| 2.2.1 | 1.5.3 | 
| 2.2.0 | 1.4.2 | 
| 2.1.3 | 1.3.17 | 
| 2.1.2 | 1.3.11 | 
| 2.1.1 | 1.3.5 | 
| 2.1.0 | 1.3.5 | 
| 2.0.0 | 1.2.0 | 
| 1.2.0 | 1.1.16 | 
| 1.1.1 | 1.1.1 |