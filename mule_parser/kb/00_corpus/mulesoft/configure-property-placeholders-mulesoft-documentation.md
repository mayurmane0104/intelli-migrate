# Configure Property Placeholders | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/mule-app-properties-to-configure](https://docs.mulesoft.com/mule-runtime/latest/mule-app-properties-to-configure)

---

```
http:
  path: "/service"
  port: "10000"
  host: "my-api.cloudhub.io"
```
yaml# Configure Property Placeholders

Instead of using static values for your Mule application configurations, such as connections, you can create a `.yaml` or a `.properties` file to contain your properties and then reference the properties from your application.

Configuring a properties file improves the organization and maintainability of your applications.

In a `.yaml` file, the properties take this form:

In a `.properties` file, the properties take this form:

http.path=/service http.port=10000 http.host=my-api.cloudhub.io

## Create and Configure your Properties File

- 
In Studio, go to the **Package Explorer**view and right-click the`/src/main/resources`folder in your project.
- 
Select **New**>**File**:![A Mule project structure with various source and test directories](_images/mruntime-properties-new-file.png) 
- 
Choose a name for your file and set the extension to `.yaml`, or`.properties`if you prefer to use this format.
- 
Edit the file to define the properties and values you need. 
- 
Add the properties file to your Mule application. - 
From Studio: - 
Open the **Global Elements**tab, and click the**Create**button.
- 
Search for the element called Configuration Properties and click **OK**.
- 
Click on the **…**button and navigate to your`.yaml`or`.properties`file.
 
- 
- 
From the XML Editor: - 
Include a `<configuration-properties>`element inside`<mule>`, and set its`file`parameter with your properties file name. For example:`<mule> <configuration-properties file="myConfiguration.yaml" doc:name="Configuration properties" doc:id="872422be-3571-4a52-a383-a2b0e16859d7" />` ... </mule>`xml
 
- 
 
- 

## Use the Properties in your Application

Once you have configured your properties file and added it to your project, you can reference its attributes by using a syntax like this: `${propertyContainer.propertyName}`.

Based on the examples configured in the previous section, to use the `path` and `port` values the syntax is `${http.path}` and `${http.port}` respectively.

For example, you can configure your Global HTTP Request configuration to use the values defined in the properties file.

- 
From Studio: 

![HTTP Request configuration settings showing fields for URL, host, port, and connection settings](_images/mruntime-properties-file.png) 

- 
From the XML Editor `<http:request-config name="HTTP_Request_config" doc:name="HTTP Request configuration" doc:id="7120494c-0540-4ad1-a118-f5b6db3f1456" basePath="${http.path}" > <http:request-connection host="${http.host}" port="${http.port}" /> </http:request-config>`xml

When the application is deployed, the property values are computed from the different possible sources and statically replace the placeholders as if they were written directly in the source code.

Based on the previous example, the configuration looks like this:

```
<http:request-config
  name="HTTP_Request_config"
  doc:name="HTTP Request
  configuration" doc:id="7120494c-0540-4ad1-a118-f5b6db3f1456"
  basePath="/service" >
		<http:request-connection
      host="my-api.cloudhub.io"
      port="10000" />
</http:request-config>
```
xmlThere is no escaping special characters based on the context. The resulting values need to be valid in the context from which they are referenced.

Consider the following example, which contains a DataWeave script:

```
<ee:transform>
  <ee:message>
    <ee:set-payload>
      <![CDATA[
        %dw 2.0
        output application/json
        ---
        {
          "message": "${message}",
        }
      ]]>
    </ee:set-payload>
  </ee:message>
</ee:transform>
```
xmlThe contents of the `.properties` file:

message=I love $

After property replacements take place, the application looks like this:

```
<ee:transform>
  <ee:message>
    <ee:set-payload>
      <![CDATA[
        %dw 2.0
        output application/json
        ---
        {
          "message": "I love $",
        }
      ]]>
    </ee:set-payload>
  </ee:message>
</ee:transform>
```
xmlThe output is an invalid DataWeave script because the dollar sign ($) has a special meaning and needs to be escaped. See [Dataweave - Escaping Special Characters](../../dataweave/latest/dataweave-types#escape-chars-string). Remember the property placeholders are replaced before the DataWeave script is parsed.

To solve conflicts, you can escape the value in the properties file:

message=I love \$

Or use DataWeave [p function](../../dataweave/latest/dw-mule-functions-p) instead of a property placeholder:

```
<ee:transform>
  <ee:message>
    <ee:set-payload>
      <![CDATA[
        %dw 2.0
        output application/json
        ---
        {
          "message": Mule::p("message"),
        }
      ]]>
    </ee:set-payload>
  </ee:message>
</ee:transform>
```
xmlThe property is evaluated when the script is executed and the script remains syntactically valid at the moment of parsing.