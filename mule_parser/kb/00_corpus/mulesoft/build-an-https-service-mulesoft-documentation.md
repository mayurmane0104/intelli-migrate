# Build an HTTPS Service | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/build-an-https-service](https://docs.mulesoft.com/mule-runtime/latest/build-an-https-service)

---

`keytool -genkeypair -keystore keystore.jks -dname "CN=localhost, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown" -keypass password -storepass password -keyalg RSA -sigalg SHA1withRSA -keysize 2048 -alias mule -ext SAN=DNS:localhost,IP:127.0.0.1 -validity 9999`text

# Build an HTTPS Service

To help you ensure data confidentiality, you can deploy your Mule app using an HTTPS-based service. Learn how to build:

- 
An HTTPS service to deploy your application to CloudHub 
- 
HTTPS services using API Manager proxies 

Additionally, learn how to configure HTTP request and response headers.

If you need to deploy your app locally, see [TLS Configuration](tls-configuration).

## Prerequisites

Before you begin, build a service (such as a simple "Hello World" service) and deploy it.

Learn how to design and develop an API using our [Build an API from Start to Finish](../../general/api-led-overview) tutorial.

## Build an HTTPS Service

Modify your service to HTTPS to deploy your app to CloudHub:

- 
Generate a `keystore.jks`file using the JDK`keytool`utility on the command line. You must also specify the hostname on the command line to generate a self-signed certificate.For example, the following command with hostname `SAN=DNS:localhost,IP:127.0.0.1`creates a`keystore.jks`file:
- 
Add the generated `keystore.jks`file to your Anypoint Studio Mule app folder in`src/main/resources`.
- 
Configure the HTTP Listener in your Mule app, specifying: - 
Any host IP addresses you want to use with the HTTPS scheme for the value of `host`
- 
A value for `${https.port} variable for the value of `port`
 
- 

```
...
<http:listener-config name="HTTPS_Listener_Configuration" protocol="HTTPS" host="0.0.0.0" port="${https.port}">
     <tls:context>
         <tls:key-store path="keystore.jks" keyPassword="${keystore.password}" password="${password}"/>
     </tls:context>
 </http:listener-config>
...
```
xml- 
Include a `config-ref`reference to the HTTPS global listener configuration.

```
<flow name="httpsserviceFlow">
    <http:listener config-ref="HTTPS_Listener_Configuration" path="hello"/>
</flow>
```
xml- 
Configure the HTTP Requester using the TLS configuration required to enable HTTPS requests to external addresses: `... <http:request-config name="HTTP_Request_Configuration" protocol="HTTPS" host="0.0.0.0" port="${https.port}" > <tls:context> <tls:key-store path="keystore.jks" password="${password}" keyPassword="${keystore.password}" /> </tls:context> </http:request-config> ...`xml

- 
Include a `config-ref`reference to the HTTPS global request configuration:`<flow name="httpsserviceFlow"> <http:request config-ref="HTTP_Request_Configuration" path="some-path" method="GET" host="0.0.0.0" port="${https.port}"/> </flow>`xmlYour application is now ready to be deployed on CloudHub. You can access your endpoint using the HTTPS address: for example, `https://yourdomain.cloudhub.io`

## Configure Services Under API Manager Proxies

If you are prompted to download a proxy from API Manager and need to configure it for HTTPS, follow the same steps that you used in Anypoint Connector for HTTP to configure the HTTP Requester. The HTTP Listener configuration is provided as a template.

To complete the configuration:

- 
Import the proxy project into Anypoint Studio. 
- 
Select the **Configuration XML**tab for your proxy flow.The parser detects an error because the flow references an HTTPS Connector that is commented out. 
- 
Uncomment the `http:listener-config`block.
- 
Add the `keystore`values:`path`,`password`, and`keyPassword`:`<tls:context name="tls-context-config"> <tls:key-store path="keystore.jks" password="${password}" keyPassword="${keystore.password}"/> </tls:context>`xml- 
You can use external properties. 
- 
The value of `path`cannot include`src/main/resources`.Your configuration should look similar to the following: `<?xml version="1.0" encoding="UTF-8"?> <mule xmlns:api-platform-gw="http://www.mulesoft.org/schema/mule/api-platform-gw" xmlns:tls="http://www.mulesoft.org/schema/mule/tls" xmlns:http="http://www.mulesoft.org/schema/mule/http" xmlns="http://www.mulesoft.org/schema/mule/core" xmlns:doc="http://www.mulesoft.org/schema/mule/documentation" xmlns:spring="http://www.springframework.org/schema/beans" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation=" http://www.mulesoft.org/schema/mule/api-platform-gw http://www.mulesoft.org/schema/mule/api-platform-gw/current/mule-api-platform-gw.xsd http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-current.xsd http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd http://www.mulesoft.org/schema/mule/http http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd http://www.mulesoft.org/schema/mule/tls http://www.mulesoft.org/schema/mule/tls/current/mule-tls.xsd"> <configuration defaultProcessingStrategy="non-blocking" /> <expression-language:property-placeholder location="config.properties" /> <api-platform-gw:api apiName="![p['api.name']]" version="![p['api.version']]" flowRef="proxy"> </api-platform-gw:api> <http:listener-config name="https-lc-0.0.0.0-8082" host="0.0.0.0" port="![p['proxy.port']]" protocol="HTTPS"> <tls:context name="tls-context-config"> <tls:key-store path="keystore.jks" password="${password}" keyPassword="${keystore.password}"/> </tls:context> </http:listener-config> ...`xml
 
- 

## Configure HTTP Request and Response Headers

You can change the maximum values for the server response headers, server request headers, and client request headers by modifying the following system properties in the `wrapper.conf` file:

| Name | Property | Description | Default Value | 
|---|---|---|---|
| Server Response Headers | 
 | Maximum amount of headers allowed on a response sent from the HTTP server. | 
 | 
| Server Request Headers | 
 | Maximum amount of headers allowed on a request sent to the HTTP server. | 
 | 
| Client Request Headers | 
 | Maximum amount of headers allowed on a request sent by the HTTP client. | 
 | 

There is no Max Client Response Header system property as there is no maximum limit for client HTTP response headers.