# Dashboard Configuration Reference | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/dashboard-config-ref](https://docs.mulesoft.com/monitoring/dashboard-config-ref)

---

- 
`avg_request_count`
- 
`avg_response_count`

# Dashboard Configuration Reference

Anypoint Monitoring provides many predefined values and identifiers for your configurations.

## Date and Time Field Values

Many fields accept time and date interval values in the following format:

| Date and Time Fields | |
|---|---|
| 
 | Week, for example:  | 
| 
 | Day, for example:  | 
| 
 | Hour, for example:  | 
| 
 | Minute, for example:  | 
| 
 | Second, for example:  | 
| 
 | Millisecond, for example:  | 

## Metrics Available to Charts

Metrics are available to basic and advanced mode chart configurations.

### Basic Mode Metrics for Applications

These metrics are available when you configure basic mode chart using the **Application Panel** setting.

Run your Mule app on a supported Mule runtime version. For supported versions, see [Mule Runtime Release Notes](../release-notes/mule-runtime/mule-esb).

| Basic Metrics | Unit | 
|---|---|
| Inbound - Average Request Count by Endpoint | 
 | 
| Inbound - Average Request Count by Flow | 
 | 
| Inbound - Average Response Count by Endpoint | 
 | 
| Inbound - Average Response Count by Flow | 
 | 
| Inbound - Failure Average Request Count by Endpoint | 
 | 
| Inbound - Failure Average Request Count by Flow | 
 | 
| Inbound - Failure Average Response Time by Endpoint | 
 | 
| Inbound - Failure Average Response Time by Flow | 
 | 
| Inbound - Success Average Request Count by Endpoint | 
 | 
| Inbound - Success Average Request Count by Flow | 
 | 
| Inbound - Success Average Response Time by Endpoint | 
 | 
| Inbound - Success Average Response Time by Flow | 
 | 
| JVM - CPU % Utilization | 
 | 
| JVM - CPU Load Average | 
 | 
| JVM - Classes Loaded | 
 | 
| JVM - Classes Loaded Total | 
 | 
| JVM - Classes Unloaded | 
 | 
| JVM - Code Cache Committed | 
 | 
| JVM - Code Cache Init | 
 | 
| JVM - Code Cache Max | 
 | 
| JVM - Code Cache Used | 
 | 
| JVM - Compressed Class Space Committed | 
 | 
| JVM - Compressed Class Space Total | 
 | 
| JVM - Compressed Class Space Used | 
 | 
| JVM - Garbage Collection Count | 
 | 
| JVM - Garbage Collection Time | 
 | 
| JVM - Heap Committed | 
 | 
| JVM - Heap Used | 
 | 
| JVM - JVM Uptime | 
 | 
| JVM - Memory Utilization | 
 | 
| JVM - Metaspace Committed | 
 | 
| JVM - Metaspace Init | 
 | 
| JVM - Metaspace Max | 
 | 
| JVM - Metaspace Used | 
 | 
| JVM - Par Eden Committed | 
 | 
| JVM - Par Eden Init | 
 | 
| JVM - Par Eden Max | 
 | 
| JVM - Par Eden Used | 
 | 
| JVM - Par New Collection Count | 
 | 
| JVM - Par New Collection Time | 
 | 
| JVM - Par Survivor Committed | 
 | 
| JVM - Par Survivor Init | 
 | 
| JVM - Par Survivor Max | 
 | 
| JVM - Par Survivor Used | 
 | 
| JVM - Tenured Gen Committed | 
 | 
| JVM - Tenured Gen Init | 
 | 
| JVM - Tenured Gen Max | 
 | 
| JVM - Tenured Gen Used | 
 | 
| JVM - Thread count - Server | 
 | 
| JVM - Total System Memory | 
 | 
| JVM - Total System Processors | 
 | 
| Outbound - Average Request Count by Endpoint | 
 | 
| Outbound - Average Request Count by Flow | 
 | 
| Outbound - Average Response Time by Endpoint | 
 | 
| Outbound - Average Response Time by Flow | 
 | 
| Outbound - Failure Average Request Count by Endpoint | 
 | 
| Outbound - Failure Average Request Count by Flow | 
 | 
| Outbound - Failure Average Response Time by Endpoint | 
 | 
| Outbound - Failure Average Response Time by Flow | 
 | 
| Outbound - Success Average Request Count by Endpoint | 
 | 
| Outbound - Success Average Request Count by Flow | 
 | 
| Outbound - Success Average Response Time by Endpoint | 
 | 
| Outbound - Success Average Response Time by Flow | 
 | 

### Basic Mode Metrics for APIs

These metrics are available when you configure basic mode chart using the **API Panel** setting.

| Basic Metrics | Unit | 
|---|---|
| Average Response Time by Instance | 
 | 
| Failed Requests by Instance | 
 | 
| Failures by Method | 
 | 
| Failures by Path | 
 | 
| Failures by Response Code | 
 | 
| Policy Violations by Instance | 
 | 
| Policy Violations by Outcome | 
 | 
| Policy Violations by Path | 
 | 
| Policy Violations by Violation ID | 
 | 
| Requests Volume by Instance | 
 | 
| Requests by Client ID | 
 | 
| Requests by Client IP | 
 | 
| Requests by Method | 
 | 
| Requests by Path | 
 | 
| Requests by Performance | 
 | 
| Requests by Response Code | 
 | 
| Slow Requests | 
 | 

The retention period for basic mode metrics for APIs is two hours.

These metrics are available if you use basic mode for APIs using the **API Analytics Panel** setting (deprecated):

| Basic Metrics | Unit | 
|---|---|
| Requests by HTTP Policy Violation | 
 | 
| Requests by HTTP Respond Code | 
 | 
| Requests by Method | 
 | 
| Requests by Instance | 
 | 

### Advanced Mode Metrics for Applications

These metrics are available when you use **Advanced** mode for apps:

| Metric | Key (From clause) | Available Field Values (Select clause) | 
|---|---|---|
| Application Inbound Metrics | 
 | |
| Application Outbound Metrics | 
 | 
 | 
| Application Statistics | 
 | 
 | 
| Disk Statistics | 
 | 
 | 
| Eden Space | 
 | N/A | 
| JVM ClassLoader | 
 | 
 | 
| JVM CPU | 
 | 
 | 
| JVM Garbage Collection | 
 | 
 | 
| JVM Garbage Collection | 
 | 
 | 
| JVM Heap Total Memory | 
 | 
 | 
| JVM Memory “Code Cache” | 
 | 
 | 
| JVM Memory Compressed | 
 | 
 | 
| JVM Memory Metaspace | 
 | 
 | 
| JVM Memory (Par Eden Space) | 
 | 
 | 
| JVM Memory (Survivor Space) | 
 | 
 | 
| JVM Memory (Tenured Generation) | 
 | 
 | 
| JVM Runtime | 
 | 
 | 
| JVM Thread Count | 
 | 
 | 
| Operating System | 
 | 
 | 
| Survivor Space | 
 | N/A | 

### Advanced Mode Metrics for APIs

These metrics are available if you use advanced mode for APIs using the **API Panel** setting:

| Metric | Key (From clause) | Available Field Values (Select clause) | 
|---|---|---|
| API Client IP | 
 | 
 | 
| API Path | 
 | 
 | 
| API Summary | 
 | 
 | 

## Markdown Syntax Support

Some Anypoint Monitoring fields, such as text graph fields in a custom dashboard, accept Markdown. Markdown is a lightweight syntax for styling all forms of writing. For information about the Markdown syntax, see [Markdown](https://en.wikipedia.org/wiki/Markdown).

## HTML Support

Some Anypoint Monitoring fields, such as Text graph fields in a custom dashboard, accept HTML elements (or tags).

### HTML Titles

```
<h1>Title 1</h1>
<h2>Title 2</h2>
<h3>Title 3</h3>
```
html### HTML Emphasis

```
<i>This text will be italic</i><br>
<em>This will also be italic</em><br>
<b>This text will be bold</b><br>
<strong>This will also be bold</strong><br>
<br>
<em>You <b>can</b> combine them</em><br>
```
html### HTML Lists

```
<ul>
<li>Item 1</li>
<li>Item 2 is <b>bold</b></li>
  <ul>
      <li>Item 2a</li>
      <li>Item 2b</li>
  </ul>
</ul>
```
html```
<ol type="1">
<li>Item 1</li>
<li>Item 2</li>
<li>Item 3</li>
  <ol>
    <li>Item 3a</li>
    <li>Item 3b</li>
   </ol>
</ol>
```
html### Images

`<img src="https://www.mycompany.com/content/dam/usa/logo/m_logo.png" alt="MyCompany's Logo" height="50" width="50">`html### Links

`<a href="https://www.mycompany.com/us/en-us.html">Visit mycompany.com!</a>`html### Blockquotes

```
As John F. Kennedy said:
<blockquote>
  And so, my fellow Americans, ask not what your
  country can do for you -- ask what you can do
  for your country.
</blockquote>
```
html### Code and Preformatted Text

- 
Code: `<code>A piece of computer code</code>`
- 
Preformatted text: Pre Tag Example`<pre> Text in a pre element is displayed in a fixed-width font, and it preserves both spaces and line breaks </pre>`html

### Tables

```
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr>
    <td>Jill</td>
    <td>Smith</td>
    <td>50</td>
  </tr>
  <tr>
    <td>Eve</td>
    <td>Jackson</td>
    <td>94</td>
  </tr>
</table>
```
html### Strikethrough

```
<p> You can use the <strike>strike tag</strike>.</p>
<p>You can also use <del> (<del>del</del>) and <s> (<s>s</s>).</p>
```
html### HTML Style Attribute

```
<h1 style="color:blue; text-align:center;">A heading</h1>
<h2 style="font-family:verdana; color:red">A heading</h2>
<p style="font-family:courier; color:green; font-size:300%;">A paragraph.</p>
```
html### Embedded Styling

It is possible to render the entire HTML page with embedded styling.

```
<!DOCTYPE html>
<html>
<head>
<style>
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    overflow: hidden;
    background-color: #333333;
}
li {
    float: left;
}
li a {
    display: block;
    color: white;
    text-align: center;
    padding: 16px;
    text-decoration: none;
}
li a:hover {
    background-color: #111111;
}
</style>
</head>
<body>
<ul>
  <li><a href="#home">Home</a></li>
  <li><a href="#news">News</a></li>
  <li><a href="#contact">Contact</a></li>
  <li><a href="#about">About</a></li>
</ul>
</body>
</html>
<hr/>
<p>© 2004 Foo Corporation</p>
```
htmlNote that you can use HTML entities like `©` for copyright.