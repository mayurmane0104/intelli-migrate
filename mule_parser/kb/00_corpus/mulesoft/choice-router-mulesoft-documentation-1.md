# Choice Router | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/choice-router-concept](https://docs.mulesoft.com/mule-runtime/latest/choice-router-concept)

---

![A choice router schematic showing multiple options, one being the default](_images/component-choice-schematic.png) 

# Choice Router

The Choice router dynamically routes messages through a flow according to a set of DataWeave expressions that evaluate message content. Each expression is associated with a different routing option. The effect is to add conditional processing to a flow, similar to an `if`/`then`/`else` code block in most programming languages.

Only one of the routes in the Choice router executes, meaning that the first expression that evaluates to `true` triggers that route’s execution and the others are not checked. If none of the expressions are `true`, then the default route executes.

![A choice router schematic showing multiple options, one being the default](_images/component-choice-schematic.png) 

## Configuration

To configure the Choice router, specify one or more conditions to evaluate, and the message processors that execute when any condition evaluates to `true`. Additionally, configure a default route that executes when none of the defined conditions are `true`.

### Anypoint Studio Configuration

To configure the Choice router in Studio, follow these steps:

![A flow showing the configuration of a Choice component in Studio](_images/mruntime-choice-configuration-studio.png)


- 
Drag the **Choice**component to any point of the flow.
- 
Click **When**, inside the Choice router, and configure the**Expression**value in the properties window to specify the condition to evaluate.
- 
Drag message processors inside **When**to specify the processors to execute when the condition is met.
- 
Drag message processors inside **Default**to specify the processors to execute when none of the defined conditions are met.

### XML Configuration

Following is the basic XML structure for a Choice router:

```
<choice doc:name="Choice">
  <when expression=${expressionToEvaluate}> 
```
**(1)**
  	<!-- Message processors --> **(2)**
  </when>
  <otherwise>
    <!-- Message processors--> **(3)**
  </otherwise>
</choice>xml| 1 | The `expression`attribute has the condition to evaluate. | 
| 2 | Add any number of message processors to execute if `expression`evaluates to`true`. | 
| 3 | Add any number of message processors to execute if none of the conditions evaluates to `true`. | 

## Adding Routes to the Choice Router

By default, the Choice router has one route option that executes when the configured DataWeave expression evaluates to `true`, and a default route that executes when none of the expressions in the existing routes are `true`. Add more routes when you need to evaluate more than one condition and then execute different operations depending on which condition is met.

### Add Routes by Dragging Components in Studio

From **Mule Palette** in Anypoint Studio, click any component and drag it into the Choice router, where you see a vertical black line:

![A flow showing a content-based routing configuration](_images/mruntime-choice-add-route.png)


### Add Routes by Editing the XML

You can also add additional route options to a Choice router by modifying the XML configuration file:

- 
In Studio, right-click the Choice router and select **Go to XML…**.
- 
Inside the `<choice>`element, add a`<when>`element:`<!--Content based routing example flow --> <flow name="content-based-routingFlow"> <http:listener config-ref="HTTP_Listener_config" path="/" doc:name="Listener"/> <set-variable variableName="language" value="#[attributes.queryParams.language]" doc:name="Set Variable" /> <!-- Choice router block--> <choice doc:name="Choice" > <when expression="#[vars.language == 'Spanish']" > <set-payload value="Hola!" doc:name="Reply in Spanish" /> </when> <when expression="#[vars.language == 'French']" > <set-payload value="Bonjour!" doc:name="Reply in French" /> </when> <!-- This is the new route option added in this step --> <when> </when> <otherwise> <flow-ref name="reply-in-default-languageSub_Flow" doc:name="reply-in-default-languageSub_Flow" /> </otherwise> </choice> <logger level="INFO" doc:name="Log the reply" message='#["The reply $(payload) means hello in $(vars.language)" ]'/> </flow>`xml

After adding a new `<when>` element, the new route option shows in the Message Flow view:
![A flow for a new content-based routing path](_images/mruntime-choice-new-route.png)


## Example Project

You can use Anypoint Studio to download the example project *Content-Based Routing* from Anypoint Exchange. This project presents a working example of a flow that uses the Choice router.

![A flow for content-based routing including payload settings and error handling](_images/mruntime-choice-example.png) 

To download and open this example project:

- 
Click the Exchange icon ( ![](_images/mruntime-exchange-icon.png) ) in Anypoint Studio. ) in Anypoint Studio.
- 
In the left panel, click **All assets**.
- 
In the window that opens, log in to Anypoint Exchange and search for the example project Content-Based Routing. 
- 
Click the Open icon ( ![](_images/mruntime-open-exchange-icon.png) ). ).

### Behavior of the Example Project

When you run the project as a Mule application, the application performs the following actions:

- 
Listens for messages. 
- 
Passes messages to a Set Variable component that sets the variable `language`to the language that is passed in the message by the parameter`language`.
- 
Uses a Choice router to find out whether each message contains a `language`attribute. The presence and value of this attribute determine how the Choice router routes the message:- 
If the value is `French`, the router routes the message to a Set Payload component that is named*Reply in French*. This latter component returns the message`Bonjour!`to the requester.
- 
If the value is `Spanish`, the router routes the message to a Set Payload component that is named*Reply in Spanish*. This latter component returns the message`Hola!`to the requester.
- 
If the message contains no `language`attribute, the router routes the message to the default path, which is a subflow that:
 
- 
- 
Logs the message "No language specified. Using English as a default." to the console 
- 
Sets the value of `language`to`English`.
- 
Returns the message `Hello!`.

The example project demonstrates that, when you are planning to route messages in a flow by using a Choice router, there are four aspects to planning that you need to consider:

- 
The content that the Choice router evaluates to determine how it routes messages 
- 
The number of routes 
- 
The default routing option 
- 
The processing that the flow performs for each routing option 

## Example XML

Following is the XML code for the Choice router example:

```
<mule xmlns:http="http://www.mulesoft.org/schema/mule/http" xmlns="http://www.mulesoft.org/schema/mule/core"
	xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
	xmlns:spring="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans-current.xsd
http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd
http://www.mulesoft.org/schema/mule/http http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd">
	<http:listener-config name="HTTP_Listener_config" doc:name="HTTP Listener config" >
		<http:listener-connection host="0.0.0.0" port="8081" />
	</http:listener-config>
	<flow name="content-based-routingFlow" >
		<http:listener config-ref="HTTP_Listener_config" path="/" doc:name="Listener" />
		<set-variable variableName="language" value="#[attributes.queryParams.language]" doc:name="Set Variable" />
    <!-- START OF CHOICE BLOCK-->
		<choice doc:name="Choice" >
			<when expression="#[vars.language == 'Spanish']" >
				<set-payload value="Hola!" doc:name="Reply in Spanish" />
			</when>
			<when expression="#[vars.language == 'French']" >
				<set-payload value="Bonjour!" doc:name="Reply in French" />
			</when>
			<otherwise>
				<flow-ref name="reply-in-default-languageSub_Flow" doc:name="reply-in-default-languageSub_Flow" />
			</otherwise>
		</choice>
    <!-- END OF CHOICE BLOCK-->
		<logger level="INFO" doc:name="Log the reply" message='#["The reply $(payload) means hello in $(vars.language)" ]'/>
	</flow>
  <sub-flow name="reply-in-default-languageSub_Flow" >
		<logger level="INFO" doc:name="Logger" message="No language specified. Using English as a default. "/>
		<set-variable variableName="language" value="English" doc:name="Set Language to English" />
		<set-payload value="Hello!" doc:name="Reply in English" />
	</sub-flow>
</mule>
```
xml## Choice Router XML Reference

A Choice flow control component contains these elements:

- 
A single root element `<choice>`
- 
A `<when>`child element for each routing option, each with an expression to match
- 
Optionally, an `<otherwise>`child element of Choice that handles all cases where none of the expressions on the`<when>`elements evaluate to`true`
- 
Components that are conditionally executed under each of the choices are defined as child elements of the `when`and`otherwise`elements

### Properties of <choice>

| Property | Description | 
|---|---|
| Business Events | For activating the Business Events feature:  | 

### Properties of <when>

| Property | Description | 
|---|---|
| Expression ( | Expression in DataWeave language to evaluate input.  |