# Mule Troubleshooting Plugin | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/mule-troubleshooting-plugin](https://docs.mulesoft.com/mule-runtime/latest/mule-troubleshooting-plugin)

---

```
➜  mule-enterprise-standalone-4.6.23 ./tools/diag help
Mule Troubleshooting Tool
=========================
Usage: ./diag [options] [command] [command-options]
Commands:
  diaf                    Generate a complete Mule diagnostic dump (default)
  help                    Show this help message
  <operation-name>        Execute a specific troubleshooting operation
Global Options:
  --stdout                Output the diagnostic dump to standard output
  --output <path>         Specify custom output directory or file path
  --extended              Enable extended mode (includes heap dump)
  --debug                 Enable debug mode with remote debugging on port 5005
Examples:
  ./diag                          # Generate diagnostic dump to logs directory
  ./diag --stdout                 # Output diagnostic dump to stdout
  ./diag --extended               # Include heap dump in diagnostic
  ./diag --output /tmp/mule.zip   # Save to specific file
  ./diag --output /tmp/           # Save to specific directory
  ./diag <operation-name>         # Execute specific operation
Output:
  By default, the tool creates a ZIP file containing:
  - mule_dump_<timestamp>.diaf    # Diagnostic information
  - thread_dump_<timestamp>.txt   # Thread dump
  - heap_dump_<timestamp>.hprof   # Heap dump (if --extended is used)
  The ZIP file is saved to the 'logs' directory by default.
```
bash# Mule Troubleshooting Plugin

Use the Mule Troubleshooting plugin to generate structured diagnostic information, simplify troubleshooting, and provide consistent data for Mule runtime support.

The Mule Troubleshooting plugin provides a unified way to collect diagnostic data from Mule runtime environments. It generates a structured diagnostic archive called the Diagnostic Information Analysis File (DIAF), which consolidates Mule runtime information, application metrics, and system data into a single, standardized output.

This Java-based plugin provides an extensible, environment-agnostic solution that simplifies troubleshooting for Mule runtime engineers, MuleSoft Support teams, customers running self-service diagnostics, and AI-assisted analysis.

## Before You Begin

Before using the plugin, make sure that you have these prerequisites:

- 
Supported Mule runtime distributions include version 4.10 and later, or LTS versions 4.9 (with patch 4.9.10 or later) and 4.6 (with patch 4.6.23 or later). 
- 
Java 8 or later, matching the Mule runtime version requirements. 
- 
Access to the `$MULE_HOME`directory. The CLI script`diag`automatically locates the Mule home directory.

The plugin works out-of-the-box in the Standalone, CloudHub, and CloudHub 2.0 deployment models without installing additional dependencies. For details about CloudHub 2.0 diagnostics, see [Generating Apps Diagnostics and Analyzing with Einstein](../../cloudhub-2/ch2-view-diag).

## Using the Mule Troubleshooting Plugin

Run this command from your Mule runtime installation at `$MULE_HOME/tools/diag` to generate the DIAF and a thread dump. By default, the tool saves the files unzipped in the `logs` directory of the distribution.

Use the `./diag --extended` command to generate a heap dump. Use `./diag --output some/dir/name/` to create the directories if they don’t exist and save unzipped files there. Use `./diag --output some/dir/name` (without a trailing `/`) to create a ZIP file at that path containing all output files.

On Windows, run `diag.bat`. The `--stdout` option isn’t supported.

The plugin’s help output lists the available commands and options.

## Understanding Diagnostic Information Analysis File (DIAF)

The Diagnostic Information Analysis File (DIAF) organizes all diagnostic data collected by the Mule Troubleshooting plugin into structured sections. Use this reference to understand the content of each section:

### Title

This section shows the report generation timestamp.

| Field | Description | 
|---|---|
| Report Generation Timestamp | The report generation time, expressed in the local time zone. | 

### Basic Information

This section shows details about the environment where the Mule runtime instance is running.

| Field | Description | 
|---|---|
| Mule Product/version | The product (CE/EE), version, and build number of the Mule runtime. Formatted as  | 
| 
 | Absolute path to  | 
| 
 | Absolute path to  | 
| 
 | All system properties starting with  | 
| Java Version | Version of the JVM running the Mule runtime. | 
| Java Vendor | Vendor of the JVM running the Mule runtime. | 
| Java VM Name | Full name of the JVM running the Mule runtime. | 
| 
 | Location of the JVM running the Mule runtime. | 
| OS Name | Name of the OS running the Mule runtime. | 
| OS Version | Version of the OS running the Mule runtime. | 
| OS Arch | Architecture of the OS (for example,  | 
| Running Time | The total time the Mule runtime has been running. | 
| PID | Process ID of the JVM running the Mule runtime. | 
| Report Millis Time | Report generation time in milliseconds since epoch ( | 
| Report Nano Time | Report generation time in nanoseconds ( | 
| 
 | Amount of used memory in the JVM. | 
| 
 | Amount of available memory in the JVM. | 
| 
 | Total amount of memory in the JVM. | 
| 
 | Maximum amount of memory the JVM attempts to use. | 
| 
 | Percentage of used memory compared to the total allocated memory. | 
| 
 | Percentage of used memory compared to the maximum available memory. | 
| 
 | The number of processors available to the JVM process. | 
| 
 | Percentage of recent CPU usage for the JVM process; negative value if unavailable. | 
| 
 | Percentage of recent CPU usage for the whole system; negative value if unavailable. | 
| 
 | System load average for the last minute; negative value if unavailable. | 

### Statistics

This section shows detailed statistics information about deployed Mule applications and their performance metrics. Metrics reflect the runtime state since the last start or redeployment. They reset after redeployments and don’t capture complete historical data. Note that this information represents a snapshot, or point in time, of the runtime behavior and can differ from the information in the Anypoint Platform usage report, which reflects a period of time.

Set the `mule.enable.statistics` system property to collect General Application Metrics and Flow Statistics.

#### Flow Summary Statistics

| Field | Description | 
|---|---|
| Private Flows Declared | Total number of private flows declared in the application. A private flow doesn’t contain a  | 
| Private Flows Active | Number of private flows that are currently in a started state. | 
| Trigger Flows Declared | Total number of trigger flows declared in the application. A trigger flow contains a MessageSource. | 
| Trigger Flows Active | Number of trigger flows currently in a started state. | 
| API Kit Flows Declared | Total number of APIkit flows declared in the application. An APIkit router uses an APIkit flow, but the flow doesn’t contain a  | 
| API Kit Flows Active | Number of APIkit flows currently in a started state. | 

#### General Application Metrics

| Field | Description | 
|---|---|
| Events Received | Number of events received by the application or flow. | 
| Events Processed | Number of events processed by the application or flow. | 
| Messages Dispatched | Total number of messages dispatched from message sources within the application. | 
| Execution Errors | Number of execution errors encountered. | 
| Fatal Errors | Number of fatal errors that cause the application to fail or stop processing. | 
| Connection Errors | Number of connection-related errors that occur. | 
| Average Processing Time | Average time (in milliseconds) required to process an event. | 
| Min Processing Time | Minimum time (in milliseconds) required to process an event. | 
| Max Processing Time | Maximum time (in milliseconds) required to process an event. | 
| Total Processing Time | Cumulative time (in milliseconds) spent processing all events. | 

#### Flow Statistics

| Field | Description | 
|---|---|
| Events Received | Total number of events received by the application since it started. | 
| Events Processed | Total number of events successfully processed by the application. | 
| Messages Dispatched | Total number of messages dispatched from message sources within the application. | 
| Execution Errors | Number of execution errors that occur during event processing. | 
| Fatal Errors | Number of fatal errors that cause the application to fail or stop processing. | 
| Connection Errors | Number of connection-related errors that occur. | 
| Average Processing Time | Average time (in milliseconds) required to process an event. | 

### Alerts

This section shows alerts for known Mule runtime issues. The report lists how many times each alert triggers during the last 1, 5, 15, and 60 minutes along with the context of the alert at the time of triggering. Some alerts, like the backpressure alert, trigger multiple times with the same context, so the plugin shows the context once and indicates how many times it happens to avoid flooding the report. Alerts that don’t trigger in any of the time intervals aren’t included in the report.

| Field | Description | 
|---|---|
| 
 | The runtime generated  | 
| Reactor discarded event | A discarded event is one that a component explicitly filters in a flow. This cuts the processing of such an event, causing the execution to hang. The context shows the correlation ID of each discarded event. | 
| Reactor dropped event | A dropped event doesn’t pass to the following component in a flow through a reactor chain and doesn’t complete. Its symptom is that the event is “hanged”. The alert doesn’t show context because the event dump provides the information. | 
| Reactor dropped error | A dropped error doesn’t pass to the corresponding error handler in a flow through a reactor chain, and so doesn’t complete. Its symptom is that the event is “hanged” when an error occurs. The context shows the string representation of each dropped error. | 
| Not consumed stream | A stream that is garbage collected before being completely consumed can provoke leaks on certain conditions (the most common one is connections from a DB connection pool that remain taken until the data is fully read). The context shows the originating location of the components that generated the streams. | 
| Backpressure triggered | Backpressure is the mechanism that rejects incoming events that exceed the current capacity. This happens because of a spike of incoming events or a longer than usual processing time of the flows. A common sign is when backpressure triggers on systems that have a CPU and memory capacity. The context shows the flow or component that exceeded capacity and the reason for backpressure. | 
| XA recovery start error | Triggered if recovery of an XA connection fails to start. The context shows the unique name (including the configuration name) of the connection for which recovery fails. | 
| Async logger ringbuffer full | When a log appender writes logs slower than the log entries are generated, the logger ringbuffer fills up. When full, threads attempting to log either wait for space in the ringbuffer or log synchronously, depending on the configuration. In either case, a thread that shouldn’t block or wait does so, causing performance issues in the Mule runtime. No context is available for this alert because it always means the same, the buffer is full. | 
| Event dispatched after flow stop | If a source dispatches an event after the flow stops, the graceful shutdown period extends unnecessarily. The context shows the connector that owns the flow’s source, and a thread dump helps you identify why the source doesn’t finish stopping. | 
| OTel export queue full | If OpenTelemetry export queues fill up, Mule runtime either drops the exceeding spans and logs or blocks the thread that tries to add them to the export queue until space is available. Dropping these resources results in missing data, while blocking threads can cause performance issues. System logs specify which spans or logs were affected and whether they were dropped or blocked. | 

| The report provides hints about potential issues. For details on a specific alert, query the log. This report isn’t intended to replace the log for detailed analysis. | 

### Event Dump

This section shows a hierarchical listing of in-flight events. For each event hierarchy executing through a flow in Mule has at least one entry in the report. For each child context for the event, a nested entry appears, sorted in a stack order: children on top, parents on bottom. If an event is dropped, the legend `DROPPED` appears next to it.

| Field | Description | 
|---|---|
| 
 | A unique identifier for the event. For child events, it has the ID of the parent event context as prefix. | 
| 
 | How long the event has been running. For child events, this time refers to the execution of this child context. The format is “mm:ss”. | 
| 
 | 
 | 
| 
 | 
 
 | 
| 
 | Identifier of the component (for example,  | 
| 
 | Unique identifier of a component within a Mule application. The first part is the flow or policy name, followed by the index and chains that nests the component. | 
| 
 | Name of the Mule configuration file that contains the component. | 
| 
 | Line number in the Mule configuration file that contains the component. | 
| 
 | Duration in milliseconds the event spends at the  | 

### Schedulers

This section shows the status and metrics of schedulers provided by the scheduler service, which the Mule runtime manages internally, not the [source components](scheduler-concept) themselves. For Mule runtime instances with multiple deployed applications, entries are grouped by application.

| Field | Description | 
|---|---|
| 
 | Name assigned to the scheduler when created, showing where in the code it happened. | 
| 
 | Type of tasks the scheduler runs: 
 | 
| 
 | A shutdown scheduler doesn’t accept new tasks. Tasks still running are allowed a graceful period to complete. | 
| 
 | A terminated scheduler is shut down and all in progress tasks are completed or forcefully terminated after a graceful shutdown period. | 
| 
 | Number of tasks currently executing by the scheduler. | 
| 
 | Number of tasks waiting in a queue. Not shown if there’s no queue, the queue size can’t be queried, or no tasks are queued. | 
| 
 | Number of tasks rejected because the scheduler is at capacity. Shows rejections in the last 1, 5, 15, and 60 minutes. If there aren’t any in those intervals, the alert isn’t shown. | 
| 
 | Number of tasks throttled because the scheduler is at capacity. Shows throttles in the last 1, 5, 15, and 60 minutes. If there aren’t any in those intervals, the alert isn’t shown. | 

### CPU Usage

This section shows the CPU usage for each thread in the Mule runtime process. Use it to identify high CPU consumption that can affect application performance. The data is sorted by current CPU usage to highlight the most active threads.

| Field | Description | 
|---|---|
| 
 | Unique identifier of the thread within the Mule runtime process. | 
| 
 | Percentage of CPU consumed by the thread during the last three-second sampling interval, calculated like the Linux top command. This metric provides a short-term view of CPU activity instead of a lifetime average. | 
| 
 | Name of the thread as reported by the JVM. | 
| 
 | Current execution state of the thread (for example,  | 
| 
 | Total CPU time the thread consumed during the most recent three-second measurement interval, in milliseconds. | 
| 
 | Total CPU time the thread has consumed since the Mule runtime process started, in milliseconds. | 

### Deployments

This section shows the status and metadata of all artifacts currently deployed in the Mule runtime instance: applications, domains, policy templates, and policies applied to applications. It also shows undeployed artifacts still present in memory, which can indicate possible leaks.

#### Applications

For each application, the report includes this information:

| Field | Description | 
|---|---|
| Artifact Name | Name of the application. | 
| Artifact Type | 
 | 
| State | Current state of the application: 
 | 
| Domain | Name of the domain the application uses. Shown only if the application uses a non-default domain. | 
| Policies | List of policy IDs applied to the application. Shown only if the application has policies. | 
| Plugins | List of all plugins available in the application’s deployment. | 
| Time since Last State Update | Timestamp of the most recent state update, formatted as  | 
| Feature Flags | List of all enabled feature flags for the application, sorted alphabetically. Shown only for  | 

#### Domains

For each domain (excluding the default domain), the report includes this information:

| Field | Description | 
|---|---|
| Artifact Name | Name of the domain. | 
| Artifact Type | 
 | 
| State | Current state of the domain: 
 | 
| Plugins | List of all plugins available in the domain’s deployment. | 
| Time since Last State Update | Timestamp of the most recent state update, formatted as  | 

#### Policy Templates

Policy templates appear as separate top-level entries. Each entry represents a unique policy template used by one or more applications.

| Field | Description | 
|---|---|
| Template Name/ID | Name or identifier of the policy template. | 
| Artifact Type | 
 | 
| Version | Version of the policy template. | 
| Plugins | List of all plugins available in the policy template. | 

## Considerations

- 
DIAF provides investigation hints. Check the logs for complete details. 
- 
Heap dumps can contain sensitive data. Enable the `--extended`option only in secure environments.
- 
In Mule runtime instances with multiple applications, DIAF sections are grouped by application. 
- 
Use DIAF for initial troubleshooting before collecting heap or thread dumps manually. 
- 
Correlate events in the event dump section with logs by using the `eventId`for deeper analysis.
- 
Collect scheduled diagnostics during maintenance windows in production environments. 
- 
To verify if all the hosts defined in your deployable artifacts (domains, applications, policies) support TLS 1.2 and 1.3 connectivity, enable the `mule.extractConnectionData.enable`system property. On UNIX, the tool generates`<ORIGINAL_CSV_NAME>_tls_results.csv`along with DIAF output. Enable the`mule.extractConnectionData.silentErrors`system property to log errors without failing deployment. Not available for Windows.