# Parse Template Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/parse-template-reference](https://docs.mulesoft.com/mule-runtime/latest/parse-template-reference)

---

![A Parse Template showing an error message](_images/parse.png) 

# Parse Template Reference

Parse Template is the Mule component to use for processing a template and obtaining a result. A template is defined as text with embedded Mule expressions that are evaluated and replaced with their result.

You can configure template through an external file reference, or you can embed it in the component definition itself.

## Configuring a Parse Template

- 
In Studio, drag a Parse Template message processor from the palette onto the canvas. 
- 
Configure the fields described in this table: ![A Parse Template showing an error message](_images/parse.png)  Field Value Description **Content**Template String A string to use as a template. Instead of defining the template in an external file, you can use this field to write it inline. It can contain embedded expressions to be evaluated and replaced with their results. **Display Name**Parse Template Customize to display a unique name for the transformer in your application. **Location**filepath Define the location of the file that Mule uses as a template into which to insert values extracted from the message properties or variables. **Target Variable**Variable Name The name of a variable that stores the result of evaluating the expression defined in Target Value. **Target Value**Expression Mule Expression to be evaluated after executing Parse Template. The result of this expression is stored in a variable with the name defined in the Target Variable field. 

If you are using the XML editor in Studio or a Standalone Mule instance:

- 
Add a `parse-template`element to your flow, then configure it according to the tables below.`<parse-template location="users/administrator/desktop/hrweb/confirmation.html" doc:name="Parse Template"/>`xml

Attributes of the `parse-template` element:

| Element Attributes | Value | 
|---|---|
| 
 | A string representing the template to be used where the embedded expressions will be evaluated and replaced by their results. | 
| 
 | Filepath which defines the location of the file that Mule uses as a template into which to insert values extracted from the message properties or variables. | 
| 
 | Customize to display a unique name for the transformer in your application. (Note: Not needed in Mule standalone.) | 
| 
 | The name of a variable where the result of the expression defined in  | 
| 
 | A Mule Expression that will be evaluated after the Parse Template is executed and which result will be stored in a variable with name as defined in the  | 

## Examples

The following examples use Parse Template to load data dynamically into HTML:

### Processing Results of a Database Query Dynamically

This example uses Parse Template in a Mule application that loads employee data from a database into an HTML template. The flow returns the template-built output to the caller.

![A flow showing steps from Listener to Error handling with a Parse Template](_images/parse-template-flow.png) 

#### Input to Parse Template

Assume that you start the flow with a URI that contains a query parameter that identifies the ID of an employee, such as `http://localhost:8081/getEmployee?id=1234`, and that the Select operation returns the following input to Parse Template:

`{ "first_name": "Melba", "last_name": "Roy Mouton", "department": "Computers", "job_title": "Assistant Chief of Research Programs", "start_date": "01/01/2021", "employee_type": "mathematician" }`html

#### Template Content

The template selects fields containing name, department, job title, start date, and employee type values from the input payload.

```
<html>
	<body>
		<table>
			<thead>
				<tr>
					<th>First Name</th>
					<th>Last Name</th>
					<th>Department</th>
					<th>Job Title</th>
					<th>Start Date</th>
					<th>Employee Type</th>
				</tr>
			</thead>
			<tbody>
				<tr>
					<td>#[payload['first_name']]</td>
					<td>#[payload['last_name']]</td>
					<td>#[payload['department']]</td>
					<td>#[payload['job_title']]</td>
					<td>#[payload['start_date']]</td>
					<td>#[payload['employee_type']]</td>
				</tr>
			</tbody>
		</table>
	</body>
</html>
```
html#### Configuration XML

In the Mule configuration XML for the example, Parse Template loads the template file through the setting `location="src/main/resources/responseHtml.template"`.

```
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:db="http://www.mulesoft.org/schema/mule/db"
      xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core
       http://www.mulesoft.org/schema/mule/core/current/mule.xsd
       http://www.mulesoft.org/schema/mule/db
       http://www.mulesoft.org/schema/mule/db/current/mule-db.xsd
       http://www.mulesoft.org/schema/mule/http
       http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd
       http://www.mulesoft.org/schema/mule/ee/core
       http://www.mulesoft.org/schema/mule/ee/core/current/mule-ee.xsd">
    <db:config name="Database_Config" doc:name="Database Config" >
        <db:my-sql-connection host="localhost" port="3306" user="user"
          password="pw" database="MySQL_Data_Source" />
    </db:config>
    <http:listener-config name="HTTP_Listener_config" doc:name="HTTP Listener config">
        <http:listener-connection host="localhost" port="8081" />
    </http:listener-config>
    <flow name="exampleTemplateFlow1" >
        <http:listener doc:name="Listener" config-ref="HTTP_Listener_config"
          path="/getEmployee"/>
        <db:select doc:name="Select" config-ref="Database_Config">
            <ee:repeatable-file-store-iterable />
            <db:sql >SELECT * FROM Employees WHERE id=#[attributes.queryParams['id']]</db:sql>
        </db:select>
        <parse-template doc:name="Parse Template"
          location="src/main/resources/responseHtml.template"/>
    </flow>
</mule>
```
xml#### Output of the Template

The [example](#template) returns template-built output. The output is HTML with the selected employee data.

```
<html>
  <body>
    <table>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Department</th>
          <th>Job Title</th>
          <th>Start Date</th>
          <th>Employee Type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>"Melba"</td>
          <td>"Roy Mouton"</td>
          <td>"Computers"</td>
          <td>"Assistant Chief of Research Programs"</td>
          <td>"01/01/2021"</td>
          <td>"mathematician"</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
```
xml### Dynamically Generating Data in HTML Rows

The example uses Parse Template on employee records that are represented as an array of objects.

![A flow including a Listener, Set Payload, Parse Template, and Logger](_images/parse-template-flow2.png) 

#### Input to Parse Template

Assume that Parse Template component receives the following payload from Set Payload:

`{ Employee: [ { "first_name" : "Melba", "last_name" : "Roy Mouton", "department" : "Computers", "job_title" : "Assistant Chief of Research Programs", "start_date" : "01/01/2021", "employee_type" : "mathematician" }, { "first_name" : "Annie", "last_name" : "Easley", "department" : "Software Development", "job_title" : "Technical Lead", "start_date" : "06/02/2020", "employee_type" : "Rocket Scientist" } ] }`html

#### Template Content

The following template uses a DataWeave script to iterate over the input array and construct an HTML row for each object in the array:

```
<html>
	<body>
		<table>
			<thead>
				<tr>
					<th>First Name</th>
					<th>Last Name</th>
					<th>Department</th>
					<th>Job Title</th>
					<th>Start Date</th>
					<th>Employee Type</th>
				</tr>
			</thead>
			<tbody>
#[%dw 2.0
output application/java
---
payload.*Employee[0] map ((item) ->
	"<tr><td><span>" ++ (item.first_name default "") ++ "</span></td><td><span>"
	++ (item.last_name default "") ++ "</span></td><td><span>"
	++ (item.department default "") ++ "</span></td><td><span>"
	++ (item.job_title default "") ++ "</span></td><td><span>"
	++ (item.start_date default "") ++ "</span></td><td><span>"
	++ (item.employee_type default "") ++ "</span></td></tr>")
	joinBy ""]
			</tbody>
		</table>
	</body>
</html>
```
html#### Configuration XML

In the Mule configuration XML, Parse Template loads the template file through the setting, `location="/path/to/my.template"`.

```
<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
      xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core
      http://www.mulesoft.org/schema/mule/core/current/mule.xsd
      http://www.mulesoft.org/schema/mule/http
      http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd
      http://www.mulesoft.org/schema/mule/ee/core
      http://www.mulesoft.org/schema/mule/ee/core/current/mule-ee.xsd">
	<http:listener-config name="HTTP_Listener_config" doc:name="HTTP Listener
   config" >
		<http:listener-connection host="0.0.0.0" port="8081" />
	</http:listener-config>
	<flow name="exampleTemplateFlow" >
		<http:listener doc:name="Listener" config-ref="HTTP_Listener_config" path="/parseit"/>
		<set-payload doc:name="Set Payload" value='#[{
	Employee: [
			{
				"first_name" : "Melba",
				"last_name" : "Roy Mouton",
				"department" : "Computers",
				"job_title" : "Assistant Chief of Research Programs",
				"start_date" : "01/01/2021",
				"employee_type" : "mathematician"
			},
			{
				"first_name" : "Annie",
				"last_name" : "Easley",
				"department" : "Software Development",
				"job_title" : "Technical Lead",
				"start_date" : "06/02/2020",
				"employee_type" : "Rocket Scientist"
			}
	]
}]'/>
		<parse-template doc:name="Parse Template" location="/path/to/my.template">
		</parse-template>
		<logger level="INFO" doc:name="Logger" message="#[payload]"/>
	</flow>
</mule>
```
xml#### Output of the Template

The [example](#template2) returns template-built output. The output is HTML with the dynamically produced rows and data from the objects in the array.

```
<html>
  <body>
    <table>
      <thead>
        <tr>
          <th>First Name</th>
          <th>Last Name</th>
          <th>Department</th>
          <th>Job Title</th>
          <th>Start Date</th>
          <th>Employee Type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span>Melba</span></td>
          <td><span>Roy Mouton</span></td>
          <td><span>Computers</span></td>
          <td><span>Assistant Chief of Research Programs</span></td>
          <td><span>01/01/2021</span></td>
          <td><span>mathematician</span></td>
        </tr>
        <tr>
          <td><span>Annie</span></td>
          <td><span>Easley</span></td>
          <td><span>Software Development</span></td>
          <td><span>Technical Lead</span></td>
          <td><span>06/02/2020</span></td>
          <td><span>Rocket Scientist</span></td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
```
xml## Special Characters

Parse Template supports the use of expressions within a template and the use of literals within these expressions. The template recognizes certain special characters, such as the sequence `\#[` and quotations marks. You can escape such characters to treat them as regular characters.

- 
`#[an-expression]`:Within a template, use the characters `#[]`to designate an expression. For example, a template can contain expressions within HTML elements, such as`<td>#[upper("mulesoft")]</td>`, which resolves to`<td>MULESOFT</td>`. Empty expressions (`#[]`) return an error, but empty strings, such as`#['']`or`#[""]`are valid expressions.
- 
Sub-expressions: To resolve a sub-expression that is surrounded by quotation marks, surround the sub-expression with another `#[]`. For example, the four elements in the template snippet below contain the same sub-expression (`upper("world")`), either inside or outside of quotation marks. The first two return the same results. The last two do not process`upper("world")`because the sub-expression is inside the quotation marks but not surrounded by another`#[]`.Parse Template Snippet:`<td>#['hello #[upper("world")]']</td> <td>#['hello ' ++ upper("world")]</td> <td>#['hello upper("world")']</td> <td>#['hello ++ upper("world")']</td>`XMLOutput Values:`<td>hello WORLD</td> <td>hello WORLD</td> <td>hello upper("world")</td> <td>hello ++ upper("world")</td>`XML
- 
Escape character ( `\`):Parse Template uses the character sequence `#[`to identify where an expression begins. To avoid this behavior and treat that sequence as literal characters, escape it with`\`. For example,`<td>#[</td>`returns`<td>#[</td>`.In addition, expressions can contain strings with special characters that you want to treat as regular characters. To escape any special characters within a string that is embedded inside an expression, append `\`to the character. Examples of special characters include the sequence`#[`, quotations marks (`'`or`"`), apostrophes (`'`), and`$`. It is not necessary to escape`\#`or`[`unless they are adjacent to one another in the string, with the`\#`preceding the`[`.Parse Template Snippet:`<td>\#[</td> <td>#['abcd\#[-1234' ++ now() as String ++ '.log']</td> <td>'abc'def'</td> <td>#['abc\'def']</td> <td>"xyz"xyz"</td> <td>#["xyz\"xyz"]</td> <td>#["abc\$DEF\#ghi\[JKL]"]</td>`XMLOutput Values:`<td>#[</td> <td>abcd#[-12342020-07-06T17:20:10.683-07:00.log</td> <td>'abc'def'</td> <td>abc'def</td> <td>"xyz"xyz"</td> <td>xyz"xyz</td> <td>abc$DEF#ghi[JKL]</td>`XMLFor more information, see [Escape Special Characters](../../dataweave/latest/dataweave-language-introduction#escape-special-characters).