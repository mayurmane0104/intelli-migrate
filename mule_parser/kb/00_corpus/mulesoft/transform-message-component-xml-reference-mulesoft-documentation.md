# Transform Message Component XML Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/transform-dataweave-xml-reference](https://docs.mulesoft.com/mule-runtime/latest/transform-dataweave-xml-reference)

---

```
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      ...
      xsi:schemaLocation="
      ...
      http://www.mulesoft.org/schema/mule/ee/core
      http://www.mulesoft.org/schema/mule/ee/core/current/mule-ee.xsd">
</mule>
```
xml# Transform Message Component XML Reference

Instead of using the Studio UI to include DataWeave language in your Mule projects, you can also create and configure a 'Transform Message' component entirely through XML, either from the XML tab in Studio or from an external editor.

Note that if you use the UI to create and configure the element, the corresponding XML configuration is created automatically in the XML editor.

## Namespace and Schema Location

At the very start of your Mule Project, you must include the following dependencies:

Note that Studio automatically adds these dependencies when you drag and drop the Transform component to your canvas.

## <ee:transform/>

The `<ee:transform>` element is the top-level XML tag for the Transform component.

| `<ee:transform>`Attributes | Description | 
|---|---|
| 
 | Defines the name of the element as it appears in the Studio canvas. | 
| 
 | Refers to  | 

## Adding DataWeave Scripts to the Transform Component

You can either type your DataWeave code into your XML using `CDATA` within a [Transformations](#transformations) element, or you can reference an external `.dwl` file.

This example that writes a DataWeave script inline within a `<dw:set-payload>` transformation element:

```
<ee:transform doc:id="747f74d4-cb66-4f8e-8222-24784e6863ae"
  doc:name="Transform" doc:timestamp="1510861248434">
    <ee:message>
        <ee:set-payload>
          <![CDATA[%dw 2.0
            output application/json
            ---
            {
              // YOUR DW SCRIPT
            }
          ]]>
       </ee:set-payload>
    </ee:message>
</ee:transform>
```
xmlHere is same example, calling an external `.dwl` file:

```
<ee:transform doc:id="747f74d4-cb66-4f8e-8222-24784e6863ae"
  doc:name="Transform" doc:timestamp="1510861248434" doc:mode="immediate">
    <ee:message>
      <ee:set-payload resource="transform.dwl" />
    </ee:message>
</ee:transform>
```
xmlThe default location for these files is in the `src/main/resources` folder in your project.

## Transformations

A single Transform component element (`<ee:transform/>`) can specify content for all parts of the Mule Event:

- 
`<ee:message/>`can contain`<ee:set-payload/>`and`<ee:set-attributes/>`.
- 
`<ee:variables/>`can contain one or more`<ee:set-variable/>`elements.

```
<ee:transform doc:id="747f74d4-cb66-4f8e-8222-24784e6863ae"
  doc:name="Transform" doc:timestamp="1510861248434">
    <ee:message>
        <ee:set-payload resource="transform.dwl" />
        <ee:set-attributes resource="myattributes.dwl" />
    </ee:message>
    <ee:variables>
        <ee:set-variable variableName="myVar" resource="myvar.dwl"/>
    </ee:variables>
</ee:transform>
```
xmlThe child elements contain some of the same attributes.

| Attributes | Description | 
|---|---|
| 
 | Points to a  | 
| 
 | For output variables only, defines the name of the variable. | 

## Full XML Sample

Here is an example that creates transformations for the payload, an attribute, and a variable.

```
<ee:transform doc:id="747f74d4-cb66-4f8e-8222-24784e6863ae"
  doc:name="Transform" doc:timestamp="1510861248434">
    <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
output application/json
---
(payload map (value0, index0) -> {
id: value0.id,
username: value0.username,
address: {
street: value0.address.street
},
website: value0.website
})]]></ee:set-payload>
        <ee:set-attributes><![CDATA[%dw 2.0
output application/json
---
{
reasonPhrase: attributes.reasonPhrase
}]]></ee:set-attributes>
    </ee:message>
    <ee:variables>
        <ee:set-variable variableName="myVar"><![CDATA[%dw 2.0
output application/json
---
{
a: payload[0].phone
}]]></ee:set-variable>
    </ee:variables>
</ee:transform>
```
xml