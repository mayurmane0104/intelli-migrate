# Scheduler Endpoint (Trigger) | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/scheduler-concept](https://docs.mulesoft.com/mule-runtime/latest/scheduler-concept)

---

![A scheduler component set up in a Mule flow example with multiple processors](_images/scheduler-component-ex.png) 

# Scheduler Endpoint (Trigger)

Automate recurring tasks by executing flows at specific times or intervals. Use fixed frequencies to run flows every few seconds, minutes, or hours, or create complex schedules with cron expressions for specific days and times. Configure time zones to ensure flows execute at the correct local time for your use case.

Consider this when adding a Scheduler to your Mule application:

- 
Schedulers use the same time zone as the machine on which Mule is running. However, if an application is running in CloudHub, the Scheduler conforms to the UTC time zone, regardless of the geographic region in which the application is running. To set a different time zone for the Scheduler, see `timeZone`in[Cron (](#props_cron_expressions).`<cron/>`)
- 
The `disallowConcurrentExecution`property prevents the Scheduler from triggering the execution of the flow while a previously-triggered execution is running.
- 
If [back-pressure](execution-engine#backpressure)occurs because no resources are available at the time of the scheduled trigger, Mule skips that execution.
- 
In a Mule runtime engine cluster or multi-worker CloudHub deployment, the Scheduler executes only on the primary node (that is, only in one Mule instance). 

## Architecture

Like other Mule event source components, a Scheduler is the first component in a Mule flow.

![A scheduler component set up in a Mule flow example with multiple processors](_images/scheduler-component-ex.png) 

The XML for the Scheduler consists of these elements:

- 
`<scheduler />`: Top-level element of the Scheduler.
- 
`<scheduling-strategy />`: Second-level element that accepts one of these children:- 
`<fixed-frequency />`: For common scheduling frequencies, such as every second.
- 
`<cron />`: For[cron expressions](#cron_expressions)and time zone settings.
 
- 

The Scheduler sets a scheduling strategy at a fixed frequency or an interval based on a cron expression. For example:

- 
The fixed frequency setting in this Scheduler executes every fifteen seconds: `<flow name="ex-fixed-frequency-flow" > <scheduler doc:name="Scheduler"> <scheduling-strategy> <fixed-frequency frequency="15" timeUnit="SECONDS" /> </scheduling-strategy> </scheduler> <!-- One or more processors here. --> </flow>`xml
- 
The cron expression in this Scheduler triggers the generation of a Mule message in a new execution of the flow every fifteen seconds: `<flow name="ex-cron-expression-flow" > <scheduler doc:name="Scheduler" > <scheduling-strategy > <cron expression='0/15 * * * * ? '/> </scheduling-strategy> </scheduler> <!-- One or more processors here. --> </flow>`xml

At least one processor must follow the Scheduler. Processors include Mule components and connector operations, such as an HTTP Request operation or Transform Message component. Failure to provide a processor produces a `MuleRuntimeException` and causes the deployment of the Mule application to fail with this ERROR message in the logs (edited for readability):

`ERROR ...MuleRuntimeException ... The content of element 'flow' is not complete. One of '{"http://www.mulesoft.org/schema/mule/core":abstract-message-processor, "http://www.mulesoft.org/schema/mule/core":abstract-mixed-content-message-processor}' is expected.`logs

For Scheduler attributes, see [Reference](#reference).

## Reference

The Scheduler elements accept attributes for configuring the execution interval and concurrency.

### Scheduler (`<scheduler/>`)

By default, the Scheduler does not wait for one execution of a given flow to complete before executing another instance of the flow at the configured cadence. You can change this behavior by setting the `disallowConcurrentExecution="true"` attribute directly in the configuration XML.

| Attribute XML | Description | 
|---|---|
| 
 | When this attribute is set to  | 

In this example, the Scheduler skips its execution if the flow takes longer to complete than the fixed frequency of 10 milliseconds:

```
<flow name="scheduler-disallowConcurrentExecution-ex" >
  <scheduler doc:name="Scheduler" disallowConcurrentExecution="true" >
    <scheduling-strategy>
      <fixed-frequency frequency="10" timeUnit="MILLISECONDS"/>
    </scheduling-strategy>
  </scheduler>
  <!-- processors here -->
</flow>
```
xmlEach time a Scheduler skips its execution, Mule logs an `Execution skipped` message, for example (edited for readability):

`INFO 2022-11-09 15:15:43,082 ... ...scheduler.DefaultSchedulerMessageSource: Flow 'scheduler-disallowConcurrentExecution-ex' is already running and 'disallowConcurrentExecution' is set to 'true'. Execution skipped. INFO 2022-11-09 15:15:43,083 ... ...scheduler.DefaultSchedulerMessageSource: Flow 'scheduler-disallowConcurrentExecution-ex' is already running and 'disallowConcurrentExecution' is set to 'true'. Execution skipped.`logs

### Fixed Frequency (`<fixed-frequency/>`)

The fixed frequency scheduling strategy accepts these attributes:

| Attribute | XML | Default | Description | 
|---|---|---|---|
| 
 | 
 | 
 | The frequency at which the Scheduler triggers the flow given the  | 
| 
 | 
 | 
 | The amount of time to delay execution of the Scheduler for the first time after the application starts. This property uses the same  | 
| 
 | 
 | 
 | One of these time units for the values of  
 | 

This strategy delays executes the Scheduler every 10 seconds after an initial 10 second delay:

```
<scheduler doc:name="Scheduler" >
  <scheduling-strategy >
    <fixed-frequency frequency="10" timeUnit="SECONDS" startDelay="10"/>
  </scheduling-strategy>
</scheduler>
```
xml### Cron (`<cron/>`)

For more complex scheduling strategies, you can use a cron expression.

| Attribute | XML | Description | 
|---|---|---|
| 
 | 
 | A cron expression for triggering the Scheduler. There is no default cron expression. For guidance with expressions, see  | 
| 
 | 
 | Time zone passed as a system property, or in a machine’s operating system.  | 

This example uses a cron expression to trigger the flow at 12:00 every day in the `America/Los_Angeles` time zone.

```
<flow name="componentsFlow">
  <scheduler>
    <scheduling-strategy>
      <cron expression="0 0 12 * * ?" timeZone="America/Los_Angeles"/>
    </scheduling-strategy>
  </scheduler>
  <logger message="my message"/>
</flow>
```
xml## Cron Expressions

Cron is a widely used standard for describing time and date information. The Cron Expression (`<cron expression />` scheduling strategy (`<scheduling-strategy >`) is useful for triggering a flow at intervals not available through the Fixed Frequency scheduling strategy.

The Scheduler keeps track of every second and creates a Mule event when the Quartz Cron expression matches your time-date setting. You can trigger the event just once or at regular intervals.

A date-time expression consists of six required settings and can include the optional year setting. Specify the settings in this order:

- 
Seconds ( `0`-`59`)
- 
Minutes ( `0`-`59`)
- 
Hours ( `0`-`23`)
- 
Day of month ( `1`-`31`)
- 
Month ( `1`-`12`or`JAN`-`DEC`)
- 
Day of the week ( `1`-`7`or`SUN`-`SAT`)
- 
Year (empty or a 4-digit year between `1970`-`2199`, for example,`2019`)

The Scheduler supports Quartz Cron expressions. Here are a few examples:

| Expression | Behavior | 
|---|---|
| 
 | Run every 2 seconds of the day, every day. | 
| 
 | Run at 10:15 a.m., every day.  | 
| 
 | Run at 10:15 a.m., every day during the year 2019. | 
| 
 | Run every minute starting at 2pm and ending at 2:59pm, every day. | 
| 
 | Run every 5 minutes starting at 2pm and ending at 2:55pm, every day | 
| 
 | Run the first second of the first minute of the first hour, on the first and seventh day, every month. | 

The Scheduler component also supports Quartz Scheduler special characters:

- 
`*`: All values.
- 
`?`: No specific value.
- 
`-`: Range of values, for example,`1-3`.
- 
`,`: Additional values, for example,`1,7`.
- 
`/`: Incremental values, for example,`1/7`.
- 
`L`: Last day of the week or month, or last specific day of the month (such as`7L`for the last Saturday of the month).
- 
`W`: Weekday, which is valid in the day-of-month field and must follow a specific day. For example,`15W`for the weekday nearest to the 15th of the month.
- 
`#`: "nth" day of the month. For example,`#3`is the third day of the month.

See [CronExpression](https://www.quartz-scheduler.org/api/2.3.0/org/quartz/CronExpression.html) for more information.

This example logs the message "hello" every second:

```
<flow name="cronFlow" >
  <scheduler doc:name="Scheduler" >
    <scheduling-strategy >
      <cron expression="* * * * * ?" />
    </scheduling-strategy>
  </scheduler>
  <logger level="INFO" doc:name="Logger" message='"hello"'/>
</flow>
```
XMLNote that there are several free online tools that can help you build Cron expressions.

## Examples in Anypoint Exchange

The examples in [Anypoint Exchange](https://www.mulesoft.com/exchange/) show use cases for a Scheduler component:

- 
*Data Sync Using Watermarking and Batch*
- 
*Import Contacts into Microsoft Dynamics CRM*
- 
*Import Leads into Salesforce*
- 
*Importing a CSV File into mongoDB*
- 
*Importing an Email Attachment Using the IMAP Connector*
- 
*Salesforce to MySQL Database Using Batch Processing*
- 
*Sending a CSV File Through Email Using SMTP*

To download and open the project from Anypoint Studio, see [Import a Mule Project from Exchange](../../studio/import-project-exchange).

## Debugging in Anypoint Studio

In Anypoint Studio [debug mode](../../studio/visual-debugger-concept), the Mule application disables the triggering of events. You can manually execute the Scheduler component when debugging by clicking the green arrow icon in Studio that appears at the bottom of the component, for example:

![A scheduler component in a flow example with process and error handling](_images/scheduler-component-debug-ex.png)