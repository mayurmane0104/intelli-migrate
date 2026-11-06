# Mule Runtime Engine 4.6.0 Release Notes | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/mule-runtime/mule-4.6.0-release-notes](https://docs.mulesoft.com/release-notes/mule-runtime/mule-4.6.0-release-notes)

---

Connectivity testing of configurations in clustered deployments no longer uses distributed locks, preventing deadlocks.

# Mule Runtime Engine 4.6.0 Release Notes

Mule runtime engine (Mule) is a lightweight integration engine that runs Mule applications and supports domains and policies.

This version of Mule provides important enhancements and fixes. Deploy all your new and existing applications to the latest version to benefit from the improvements.

## June 2026

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.31 includes Runtime Manager agent 2.7.15. See [Runtime Manager Agent 2.7.15 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-15).

### Fixed Issues

Patch release version: 4.6.31

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| W-22248198 | |
| Fatal errors such as  | W-22496803 | 
| Mule no longer hangs during shutdown when a parameter validation exception occurs during flow execution. | W-22248534 | 
| Race conditions in  | W-22343018 | 
| The ObjectStore retrieved from the Registry in  | W-22373641 | 
| SDK parameter validation errors now raise the  | W-22276522 | 
| Race conditions during policy redeployment that caused Mule to stop processing events permanently no longer occur. | W-22343705 | 
| 
 | W-21193046 | 
| Cluster encryption now uses the configured algorithm correctly instead of defaulting to Blowfish. | W-21666905 | 
| The error type in the EE Cache scope is now correctly reported as  | W-21525972 | 
| Large Anypoint Platform authentication failure responses no longer cause excessive log bloat. | W-21882516 | 
| In-memory Object Store partitions now correctly use cluster-wide storage when deployed to a cluster with the Object Store plugin enabled. | W-17714668 | 
| Persistent ObjectStore or Batch data serialized before a patch upgrade now deserializes correctly after upgrading. | W-22623626 | 
| 
 | W-22547971 | 

DataWeave 2.6.27 is bundled with the Mule 4.6.31 release. This patch release addresses these DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The Java bean metadata cache no longer performs unnecessary evictions when processing Java POJOs. A new per-app Java bean cache can be enabled with the  | W-22417507 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## May 2026

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.30 includes Runtime Manager agent 2.7.13. See [Runtime Manager Agent 2.7.13 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-13).

General improvements:

- 
The `diaf`Event Dump now includes two additional`eventContextState`values:`PENDING`and`WAITING_NON_BLOCKING`. See[Mule Troubleshooting Plugin](../../mule-runtime/latest/mule-troubleshooting-plugin)for more information.

### Fixed Issues

Patch release version: 4.6.30

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| Configuration references to configs defined in a parent domain are now properly validated at deployment time, preventing unclear runtime errors. | W-11453332 | 
| Extension operations using  | W-18034452 | 
| The Grizzly HTTP library is upgraded to 2.3.36-MULE-029. | W-21337433 | 
| The plexus-utils library is upgraded to 4.0.3. | W-21774430 | 
| A memory leak in dynamic  | W-22013292 | 
| Deserialization errors no longer occur in Redis-backed Object Stores when accessing cached data created on an earlier Mule runtime version. | W-20880559 | 
| API Gateway contracts for public OAuth clients using PKCE are no longer dropped when the client secret is null. | W-21177224 | 
| The support-tools-installer is removed from the Mule runtime distribution. | W-21842339 | 

DataWeave 2.6.26 is bundled with the Mule 4.6.30 release. This patch release addresses these DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| 
 | W-21614817 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## April 2026

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.29 includes Runtime Manager agent 2.7.11. See [Runtime Manager Agent 2.7.11 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-11).

Feature Flagging Mechanism:

- 
Mule 4.6 incorporates new feature flags. See [Feature Flagging Mechanism](../../mule-runtime/latest/feature-flagging)for a detailed description of each feature flag and configuration instructions.

### Fixed Issues

Patch release version: 4.6.29

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| The c3p0 library is upgraded to 0.12.0. | W-21391116 | 
| The mchange-commons-java library is upgraded to 0.4.0. | W-21391115 | 
| 
 | W-20256082 | 
| Until Successful scopes no longer continue retrying during application shutdown when using flow-ref. | W-20267296 | 
| 
 | W-20791354 | 
| OAuth token storage now correctly uses custom  | W-19811593 | 
| 
 | W-21250126 | 
| Scheduler jobs no longer deadlock during flow shutdown. | W-21263748 | 
| TLS Context can now be initialized during application deployment by using the  | W-20038933 | 

DataWeave 2.6.25 is bundled with the Mule 4.6.29 release. This patch release addresses these DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The Avro library is upgraded to 1.12.1. The Jackson Core library is upgraded to 2.21.1. | W-21415439 | 
| The Jakarta Mail library is upgraded to 2.1.5. | W-21320250 | 
| The range operator now returns null for invalid ranges. | W-21781423 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## March 2026

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.28 includes Runtime Manager agent 2.7.10. See [Runtime Manager Agent 2.7.10 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-10).

Feature Flagging Mechanism:

- 
Mule 4.6 incorporates new feature flags. See [Feature Flagging Mechanism](../../mule-runtime/latest/feature-flagging)for a detailed description of each feature flag and configuration instructions.

### Fixed Issues

Patch release version: 4.6.28

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| When the  | W-20890587 | 
| When the  | W-20890613 | 
| Extensions no longer export  | W-21001749 | 
| Public flows now stop concurrently during graceful shutdown. | W-21228085 | 
| Deadlocks no longer occur during log reconfiguration when policies are applied. | W-21231834 | 
| When the  | W-21232374 | 
| The  | W-17689958 | 
| When the  | W-21215761 | 
| The tika-core library is upgraded to 3.2.3. | W-21179465 | 
| The  | W-20633888 | 
| APIkit flows that use non-default names and are mapped through the  | W-18668900 | 

DataWeave 2.6.24 is bundled with the Mule 4.6.28 release. This patch release addresses these DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The Array range selector operator no longer experiences performance degradation. | W-20220578 | 
| Concurrent access to  | W-21045501 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## February 2026

### Patch 4.6.27

- 
This patch update reverts the fixes for these Mule issues: W-20618734 and W-20628990. 

### Patch 4.6.26

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.26 includes Runtime Manager agent 2.7.9. See [Runtime Manager Agent 2.7.9 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-9).

### Fixed Issues

Patch release version: 4.6.26

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| JDK Flight Recorder (JFR) is now disabled by default. | W-19990145 | 
| The Abstract Syntax Tree (AST) file of applications using the until-successful component is now leveraged by Mule runtime instead of parsing the configuration XML files. | W-20283146 | 
| Mule application unresponsiveness no longer occurs after a policy that uses the until-successful component is undeployed or redeployed. | W-20628990 | 
| Implemented minor improvements to Mule classloading structures to enhance efficiency and stability. | W-20028988 | 
| Thread Context Classloader (TCCL) is no longer wrongly set to the connector after an operation policy  | W-20618734 | 
| Fastutil is now replaced with fastutil-core. | W-20729870 | 

There is no DataWeave update for this version.

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## January 2026

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.25 includes Runtime Manager agent 2.7.9. See [Runtime Manager Agent 2.7.9 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-9).

MUnit:

- 
MUnit version 3.6.3 is now required. See [MUnit 3.6.3 Release Notes](../munit/munit-3.6.3-release-notes).

General improvements:

- 
You can now view deployment information in the `diaf`file. See[Mule Troubleshooting Plugin](../../mule-runtime/latest/mule-troubleshooting-plugin)for more information.

### Fixed Issues

Patch release version: 4.6.25

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| Batch jobs no longer hang when errors occur in steps that use try scopes with global error handlers. | W-17738563 | 
| Design-time operations on primary content parameters with non-Java types now work correctly. | W-20187776 | 
| Logging information is now improved during graceful shutdown. | W-20278970 | 
| A deadlock between Log4j Mule log support during application initialization no longer occurs. | W-20419795 | 
| MUnit tests no longer fail intermittently when running on Java 17. | W-17044721 | 
| Batch processing no longer fails with serialization error when LDAP action throws an error in Java 17. | W-19524600 | 
| Dynamic configurations now work correctly during initialization when using  | W-18835469 | 

DataWeave 2.6.22 is bundled with the Mule 4.6.25 release. This patch release addresses these DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The stream reader now processes input with multi-byte characters correctly. | W-20016549 | 
| The org.apache.commons:commons-text library is upgraded to 1.14.0. | W-20618375 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## November 2025

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.24 includes Runtime Manager agent 2.7.8. See [Runtime Manager Agent 2.7.8 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-8).

General improvements:

- 
You can now view CPU usage information in the `diaf`file. See[Mule Troubleshooting Plugin](../../mule-runtime/latest/mule-troubleshooting-plugin)for more information.

### Fixed Issues

Patch release version: 4.6.24

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| OpenTelemetry current API sampling decisions now propagate correctly through  | W-19784910 | 
| 
 | W-15196888 | 
| 
 | W-18563387 | 
| MDC information is now properly preserved when using loggers inside custom Java code invoked from a DataWeave script. | W-18912999 | 
| Batch queuestore files now clean up correctly in rare load failure scenarios such as out-of-memory errors. | W-17935223 | 
| Builds no longer fail when running tests from an extension that uses Mule SDK with Java 8 through Java 17. | W-18964335 | 
| The until-successful scope now properly honors the graceful shutdown timeout. In versions earlier than 4.11.0, you must enable this behavior using these system properties:  | W-19340663 | 
| Hashing now uses  | W-18584560 | 
| 
 | W-19340663 | 
| Mule applications that use TLS KeyStore configurations no longer fail to deploy with “NO MODEL RESOLVED” warnings and  | W-16565012 | 
| Mule Troubleshooting Plugin executions no longer fail when the IP address changes. | W-19802474 | 

DataWeave 2.6.20 is bundled with the Mule 4.6.24 release. This patch release addresses these DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The Apache Commons Lang dependency is removed from the distribution. | W-19803454 | 
| Materialization errors no longer occur when running functions. | W-19884071 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## October 2025

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.23 includes Runtime Manager agent 2.7.7. See [Runtime Manager Agent 2.7.7 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-7).

Mule Troubleshooting Plugin:

- 
Mule 4.6.23 introduces the Mule Troubleshooting plugin, which generates a structured diagnostic archive (DIAF) to simplify troubleshooting, consolidate runtime metrics, and provide consistent data for MuleSoft Support. It works across all deployment models and helps investigate performance issues, application errors, and scheduler activity. See [Mule Troubleshooting Plugin](../../mule-runtime/latest/mule-troubleshooting-plugin)for more information.

### Fixed Issues

Patch release version: 4.6.23

This patch update addresses these Mule issues:

| Issue Resolution | ID | 
|---|---|
| The org.springframework library is upgraded to 5.3.45. | W-18603096 | 
| Memory leaks no longer occur when a reconnection is configured in a Mule domain and referenced from multiple applications. | W-17857080 | 
| 
 | W-18667744 | 
| Fork-join routers no longer create unnecessary schedules when the timeout is set to infinite. | W-18347293 | 
| Potential deadlocks during deployment no longer occur when using some custom Log4j appenders. | W-19675881 | 
| This release reverts the changes introduced in W-17340911. | W-17340911 | 
| Cookies now propagate correctly across multiple redirect scenarios. | W-18971065 | 
| Batch queuestore files now clean up correctly in rare load failure scenarios, such as out of memory errors. | W-17935223 | 
| Gatekeeper deadlock errors no longer occur during race conditions among contract downloads and policy application. | W-19407164 | 

DataWeave 2.6.19 is bundled with the Mule 4.6.23 release. This patch release addresses these DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The  | W-19168279 | 
| 
 | W-19477334 | 
| Module compilation performance is improved when running concurrently. | W-19376546 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## September 2025

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.22 includes Runtime Manager agent 2.7.7. See [Runtime Manager Agent 2.7.7 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-7).

### Fixed Issues

Patch release version: 4.6.22

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| TLS configuration for FIPS-140-2 is now upgraded. | W-16315176 | 
| Applications using Scheduler component in a strict FIPS-140-2 environment no longer fail to deploy due to the unavailability of the MD5 algorithm. | W-19319437 | 
| OAuth token is now refreshed when used through  | W-19248279 | 

There is no DataWeave update for this version.

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## August 2025

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.21 includes Runtime Manager agent 2.7.6. See [Runtime Manager Agent 2.7.6 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-6).

General improvements:

- 
License Delivery Update: Starting with Mule 4.6.21, Enterprise licenses are now provided either as a single `license.lic`file or as a`.zip`that contains both FIPS and non-FIPS licenses. See[FIPS 140-2 Compliance Support](../../mule-runtime/latest/fips-140-2-compliance-support)for details.

General improvements:

- 
When running Mule runtime in FIPS security mode with clustering enabled, the encryption key defined in `mule.cluster.network.encryption.key`must have a length of 16, 24, or 32 bytes. See[Enable Clustering in FIPS Mode](../../mule-runtime/latest/mule-high-availability-ha-clusters#cluster_fips)for details.

### Fixed Issues

Patch release version: 4.6.21

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Silent errors and hangs no longer occur when a component fails to start within a foreach/subflow combination. | W-18589595 | 
| An incorrect error level message no longer shows during deployment when using APIKit with no flow mappings. | W-19004884 | 
| Performance degradation no longer occurs when using repeatable streaming. | W-19175330 | 

DataWeave 2.6.17 is bundled with the Mule 4.6.21 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| A  | W-18981240 | 
| The  | W-18990604 | 
| DataWeave runtime types are now correctly written when outputting Java. | W-18942349 | 
| Access to multipart content raw value no longer reads the part content. | W-18892158 | 
| The  | W-18850597 | 
| The  | W-18851259 | 
| The  | W-17204482 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## July 2025

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.20 includes Runtime Manager agent 2.7.5. See [Runtime Manager Agent 2.7.5 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-5).

### Fixed Issues

Patch release version: 4.6.20

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Schedulers are no longer triggered during graceful shutdown. | W-17981248 | 
| The commons-beanutils:commons-beanutils library is upgraded to v1.11.0. | W-18687846 | 
| The com.google.code.gson:gson library is upgraded to v2.12.1. | W-17896347 | 
| Repeatable streams now make data available before the buffer is full. To enable this behavior, set the system property  | W-18716253 | 
| Serialization now works correctly with API Gateway internal classes. | W-18475283 | 
| The W-17340911 fix, which resolved loader constraint violation errors related to  | W-18327141 | 

DataWeave 2.6.16 is bundled with the Mule 4.6.20 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Reading a CSV file inside a MultiPart body now works correctly when performed more than once. | W-17167283 | 
| XML encoding detection now works correctly when the declaration header is missing. | W-18853667 | 
| The  | W-17204482 | 
| Unicode characters now render correctly at the beginning of the string when using the DataWeave  | W-14855645 | 
| The Apache POI library is now upgraded. | W-18253747 | 
| Experimental warning messages are no longer logged on DataWeave SDK files. | W-16384926 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## June 2025

### Patch 4.6.19

- 
This patch update reverts the fixes for the following Mule issue: W-17703164 

### Patch 4.6.18

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.18 includes Runtime Manager agent 2.7.4. See [Runtime Manager Agent 2.7.4 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-4).

### Fixed Issues

Patch release version: 4.6.18

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Loader constraint violation errors no longer occur when  | W-17340911 | 
| Serialization of result objects with Kryo no longer fails with  | W-17774685 | 
| Class loading no longer results in deadlocks caused by a race condition. | W-18388443 | 
| Spring Framework artifacts are replaced with vendor-supported equivalents to improve long-term compatibility. | W-18462316 | 
| A serialization exception no longer occurs when using caching scope. | W-17703164 | 

DataWeave 2.6.15 is bundled with the Mule 4.6.18 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The performance of the  | W-18439576 | 
| Reading a CSV file inside a MultiPart body now works correctly when performed more than once. | W-17147598 | 
| A memory leak of the binding context no longer occurs when using the  | W-18472194 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## May 2025

### Patch 4.6.17

The May patch update 4.6.17 addresses a regression in the previous May patch update, 4.6.16, and includes the fixes in the patch.

Patch release version: 4.6.17

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Cluster discovery mechanism now works as expected on Runtime Fabric, CloudHub 2.0, and Anypoint Platform PCE environments, ensuring that schedulers are executed only on the primary node. | W-18528551 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

### Patch 4.6.16

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.16 includes Runtime Manager agent 2.7.2. See [Runtime Manager Agent 2.7.2 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-2).

### Fixed Issues

Patch release version: 4.6.16

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Parallel For Each events no longer randomly timeout after a  | W-17980769 | 
| The error message "Couldn’t parse instance of ReentrantReadWriteLock" in ReentrantReadWriteLockSerializer no longer occurs. | W-18057570 | 
| Parameters field isn’t serialized in  | W-17703164 | 
| Connectivity tests in MTS are now fixed for Java 17. | W-18075077 | 
| Exceptions no longer occur when using WebSocket close codes outside a predefined subset. The code now correctly handles all standard or custom WebSocket close codes. | W-17846088 | 
| The  | W-16263266 | 
| org.glassfish:jakarta.json was removed form the distribution. | W-17896357 | 
| xerces-j is upgraded to 2.12.2. | W-16980865 | 
| raml-parser is upgraded to v1.0.44-17. | W-17750714 | 

DataWeave 2.6.14 is bundled with the Mule 4.6.16 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Materialization issues no longer occur when using CSV content inside variables. | W-17167283 | 
| A compatibility flag is now added to address the different results produced by calling  | W-18020856 | 
| An unnecessary import is now removed from  | W-17670504 | 
| DataWeave no longer returns a format error on  | W-18118138 | 
| Overflowing no longer occurs while reading large file on multipart format. | W-17644871 | 
| Performance issues no longer occur when using the Mule API Java class Message in DataWeave scripts. | W-18034217 | 
| DataWeave now preserves trailing zeroes of single-element sum. | W-17283050 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## April 2025

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.15 includes Runtime Manager agent 2.7.2. See [Runtime Manager Agent 2.7.2 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.7.x-release-notes#2-7-2).

Enterprise Edition License:

- 
The command `mule -verifyLicenseDetails [path_to_license]`that verifies the license before installing it is now added. See[Verify or Remove Enterprise Edition License](../../mule-runtime/latest/installing-an-enterprise-license#verify-or-remove-enterprise-edition-license).

### Fixed Issues

Patch release version: 4.6.15

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| 
 | W-16980865 | 
| Error type in raise-error is now correctly resolved when defined with a static property. | W-17339304 | 
| 
 | W-17844603 | 
| You can now use the  | W-17340620 | 
| 
 | W-17896358 | 

There is no DataWeave update for this version.

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## March 2025

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.14 includes Runtime Manager agent 2.6.7. See [Runtime Manager Agent 2.6.7 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.6.x-release-notes#2-6-7).

Feature Flagging Mechanism:

- 
Mule 4.6 incorporates new feature flags. See [Feature Flagging Mechanism](../../mule-runtime/latest/feature-flagging)for a detailed description of each feature flag and configuration instructions.

### Fixed Issues

Patch release version: 4.6.14

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Resources are now properly released after a timeout when using the Scatter-Gather or Parallel For Each routers. The  | W-16941297 | 
| 
 | W-16629236 | 
| 
 | W-17667949 | 
| Performance degradation no longer occurs when the  | W-17627284 | 
| A race condition introduced by W-17048606 no longer occurs, where the last part of the response body was truncated when  | W-17617940 | 
| Serialization using Object Store V2 with OAuth2 Provider now works as expected. | W-16673760 | 
| Performance during cache scope execution is now improved. | W-17671126 | 

DataWeave 2.6.12 is bundled with the Mule 4.6.14 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The Flat File Module now supports YAML files with nested depth greater than 50. | W-17495145 | 
| 
 | W-16918194 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## February 2025

### Patch 4.6.13

The February patch update 4.6.13 addresses a regression in the previous February patch update, 4.6.12, and includes the fixes in the patch.

Patch release version: 4.6.13

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| 
 | W-17801971 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

### Patch 4.6.12

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.12 includes Runtime Manager agent 2.6.7. See [Runtime Manager Agent 2.6.7 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.6.x-release-notes#2-6-7).

### Fixed Issues

Patch release version: 4.6.12

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| 
 | W-17395302 | 
| The optimization to avoid sending body contents on NTLM type 1 requests added in W-17107281 is now controlled by the feature flag  | W-17216089 | 
| A  | W-17430963 | 
| A corner case has been fixed and Anypoint Monitoring dashboard now correctly shows all metrics. | W-16828516 | 
| Kryo serialization issue no longer occurs in Java 17 when running with distributed cluster using authentication, caching policy, and persistent Object Store. | W-16912085 | 
| Transactions initiated before a  | W-17453707 | 
| API metrics are now properly sent. | W-17529530 | 

DataWeave 2.6.11 is bundled with the Mule 4.6.12 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The Java reflection lookup strategy is now improved for bean instances. | W-17624594 | 
| Compatibility flags created with Mule runtime 4.4 can now be used with older Mule runtime versions. | W-17372664 | 
| The deconstruct pattern now works as expected when using append on empty objects combined. | W-16823030 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## January 2025

### Patch 4.6.11

- 
This patch update reverts the fixes for the following Mule issues: W-17107281 and W-17048606. 
- 
This patch update reverts the fixes for the following DataWeave issues: W-16823030, W-17206423, and W-17372664. 

### Patch 4.6.10

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.10 includes Runtime Manager agent 2.6.7. See [Runtime Manager Agent 2.6.7 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.6.x-release-notes#2-6-7).

### Fixed Issues

Patch release version: 4.6.10

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Windows no longer throws  | W-17050930 | 
| 
 | W-16517561 | 
| Unnecessary internal blocking operations no longer occur when handling large streamed HTTP responses. | W-17048606 | 
| Body content is no longer sent on Type 1 requests during NTLM authentication. | W-17107281 | 
| Deploying applications that contain XML SDK connectors no longer causes application class loader memory leak. | W-16814280 | 
| An infinite loop no longer ocurrs when a redelivery policy is exhausted in a source configured with Transactions and contains an On Error Propagate. | W-17403761 | 
| 
 | W-17008722 | 
| A memory leak no longer occurs when using  | W-16789548 | 
| 
 | W-11866494 | 
| A serialization error no longer occurs in Java 17 when using clustering mode or Object Store v2. | W-17218707 | 
| 
 | W-17089503 | 
| All transactions running within a global Error Handler are now committed as expected. | W-16619771 | 

DataWeave 2.6.10 is bundled with the Mule 4.6.10 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Compatibility flags created with Mule runtime 4.4 can now be used with older Mule runtime versions. | W-17372664 | 
| The deconstruct pattern now works as expected when using append on empty objects combined. | W-16823030 | 
| The Java reflection lookup strategy is now improved for bean instances. | W-17206423 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## November 2024

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.9 includes Runtime Manager agent 2.6.6. See [Runtime Manager Agent 2.6.6 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.6.x-release-notes#2-6-6).

### Fixed Issues

Patch release version: 4.6.9

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Memory leak in  | W-16823349 | 
| A batch serialization error no longer occurs in Java 17 when one of the steps throws  | W-16546951 | 
| A deadlock no longer occurs when consuming the payload in the completion callback of the HTTP client  | W-16640190 | 
| 
 | W-16712841 | 
| Log4j2 monorepo is upgraded to 2.24.1. | W-16889265 | 
| The  | W-16843119 | 

DataWeave 2.6.9 is bundled with the Mule 4.6.9 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| The  | W-17030593 | 
| Apache POI folder used for temporal files is no longer deleted. | W-16899674 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## October 2024

### What’s New

Runtime Manager agent:

- 
This release of Mule runtime 4.6.8 includes Runtime Manager agent 2.6.6. See [Runtime Manager Agent 2.6.6 Release Notes](../runtime-manager-agent/runtime-manager-agent-2.6.x-release-notes#2-6-6).

### Fixed Issues

Patch release version: 4.6.8

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Spring Core is upgraded to 5.3.39. | W-16519084 | 
| The  | W-12228892 | 
| Web Service Consumer Connector and RosettaNet Connector no longer fails when there is an HTTP TLS transport configuration. | W-16288302 | 
| 
 | W-16237424 | 
| Kryo serialization now works as expected with  | W-16533466 | 
| Kryo serialization now works as expected when executing the Rate Limit policy in Java17. | W-16843706 | 
| Fatal errors no longer occur when loading native libraries in Java 17. | W-16787783 | 
| 
 | W-16595277 | 
| When the feature flag  | W-16169887 | 
| Logging for the Analytics  | W-16624763 | 
| 
 | W-16734361 | 
| Race condition now causes an infinite loop in Grizzly AHC. | W-16599945 | 

DataWeave 2.6.8 is bundled with the Mule 4.6.8 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| DataWeave descendant selector performance is now improved. | W-16343577 | 
| Streaming capability for arguments at  | W-16125755 | 
| Input/output  | W-16161736 | 
| Access error for Java 17 encapsulation errors is now improved. | W-15705596 | 
| Coercion error is now caught inside  | W-15323897 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## September 2024

### What’s New

- 
`cxfVersion`is upgraded to 3.5.9.
- 
JaCoCo is upgraded to 0.8.11. 
- 
Maven JAR Plugin is upgraded to 3.3.0. 

### Fixed Issues

Patch release version: 4.6.7

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| 
 | W-15643200 | 
| Properties files are now located in the  | W-16404468 | 
| 
 | W-16343071 | 
| Debug logs for custom policies containing a custom extension/connector now work correctly. | W-15286605 | 
| The process of unloading native libraries in Windows OS running on Java 8 and Java 11 is now improved. | W-16375439 | 
| 
 | W-16436783 | 
| JaCoCo is upgraded to 0.8.11. | W-14866639 | 
| 
 | W-14580541 | 
| Policies with minimum Mule version 4.4.0 now use the flow name as part of the artifact name, when the feature flag  | W-16169887 | 
| 
 | W-16540685 | 
| API Gateway pollers are no longer initialized when the API Gateway is started in offline mode. | W-16093885 | 
| Race condition no longer causes byte buffer disposal errors when deploying policies. | W-16450677 | 

DataWeave 2.6.7 is bundled with the Mule 4.6.7 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| DataWeave now preserves MimeType properties correctly. | W-16161736 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## August 2024

Patch release version: 4.6.6

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Loaded native libraries are now copied into a separate temporary folder to avoid issues while redeploying applications in Windows OS. | W-15894519 | 
| Parameter resolution error handling is no longer affected when the parameterized operation is inside a dynamically referenced subflow. | W-15923581 | 
| The OAuth token invalidation status is now communicated to other nodes in a cluster when a token is invalidated on one node. | W-15154658 | 
| Flows now honour the state configured in  | W-15750334 | 
| Mule runtime startup no longer fails when  | W-15346051 | 
| A serialization exception is no longer thrown when a Batch Step fails with a  | W-15808825 | 
| 
 | W-15832941 | 
| Jars in  | W-16010357 | 
| Serialization now works as expected with Batch Job and Salesforce BulkOperationResult in Java 17. | W-16105403 | 
| Batch module no longer fails with a  | W-16124318 | 
| Deploying a policy no longer fails while using a mule directory with whitespaces. | W-15440100 | 
| 
 | W-15595791 | 
| 
 | W-15734679 | 
| API Gateway initialization no longer fails if quorum isn’t reached in cluster mode. | W-15951155 | 
| Hard timeout for platform requests is now available by setting up the  | W-16141554 | 

DataWeave 2.6.6 is bundled with the Mule 4.6.6 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Argument materialization is now improved at the  | W-15323897 | 
| Streaming capability is now enabled for arguments of  | W-16125755 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## July 2024

Patch release version: 4.6.5

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| The  | W-15397610 | 
| The redeployment of an app with a domain using a Groovy component no longer throws the  | W-15750766 | 
| Batch job instance queue store files are removed after completion. | W-15546969 | 
| Cache scope with multiple computations no longer occurs if events arrive concurrently for an absent key. | W-14604517 | 
| Tanuki wrapper configuration is now enabled for AArch64. | W-15839796 | 
| MDC context is reset after the XML SDK operation is executed. | W-15206528 | 
| MUnit tests no longer fail with  | W-14998254 | 
| Maven plugin versions are updated to be compatible with Maven 3.9. | W-15554914 | 
| JRuby dependency is upgraded to 9.4.7.0. | W-15757000 | 
| Deploying a policy in Windows no longer fails in folders containing whitespaces. | W-16112611 | 
| Open Telemetry tracing support is now added to policies. | W-15633203 | 
| Kerberos is now enabled for proxy authentication against Anypoint Platform for Gateway capabilities. | W-15642605 | 
| Default stronger validations for policies are now added after applying the property  | W-15769926 | 
| Logging for Gateway Analytics initialization is now improved. | W-15904845 | 
| Handling of connection errors with API platform is now improved. | W-15809377 | 
| Default gatekeeping for APIs that fail when doing a rollback is now added using the property  | W-15427352 | 

DataWeave 2.6.5 is bundled with the Mule 4.6.5 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Enforced Java accessibility restrictions only for Mule apps with DataWeave language level version 2.6 and later and executing with Java 17 and later. | W-15832793 | 
| Materialization issues no longer occur with schema properties. | W-15839190 | 
| The Flat File module now adds the  | W-15571377 | 
| The Flat File module now adds the  | W-15973636 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## June 2024

Patch release version: 4.6.4

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Applications configured with OAuth and running on Java 17 are now correctly serialized. | W-15425364 | 
| You can now see the number of flows considered for UBP and what those flows are when the application starts. | W-14401338 | 
| 
 | W-14821825 | 
| The version in the  | W-15228973 | 
| Events with statistics are now correctly serialized for applications running on Java 17. | W-15542604 | 
| The exception  | W-15617764 | 
| DataWeave compiled expressions cache is no longer overpopulated when using nested templates. | W-15782010 | 
| Batch job serialization now works as expected when running on Java 17. | W-15345812 | 
| Tracing variables inside XML operations are no longer propagated to the flows. | W-15206528 | 
| 
 | W-15628361 | 
| 
 | W-15677894 | 
| Resiliency is now improved on policy application and updates. | W-15426519 | 

DataWeave 2.6.4 is bundled with the Mule 4.6.4 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| A  | W-14589732 | 
| The Excel writer now generates XLSX files using ZIP specification 2.0. | W-15534640 | 
| When comparing a  | W-15478713 | 
| Access error messages for Java 17 encapsulation errors are now improved. | W-15705596 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## May 2024

Patch release version: 4.6.3

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Client, policy, and API names are now shown when logging Analytics events. | W-15294568 | 
| When upgrading a policy, templates are now downloaded before the previous version is removed. | W-15212679 | 
| When applying a policy that initially failed but was later applied successfully, the retry initiated by the gateway no longer causes an exception error. | W-15186491 | 
| Joda-Time is upgraded to v2.12.7. | W-15511864 | 
| Apache CXF is upgraded to version 3.5.8. | W-15293232 | 
| Getting metadata from a XSD with  | W-15193303 | 

DataWeave 2.6.3 is bundled with the Mule 4.6.3 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| 
 | W-15006840 | 
| Performance degradation no longer occurs when an array is concatenated. | W-15399854 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## April 2024

Patch release version: 4.6.2

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| 
 | W-15159880 | 
| Hazelcast is upgraded to 5.2.5. | W-15274674 | 
| Spring is upgraded to 5.3.33. | W-15260752 | 
| GraalJS is upgraded to 22.3.5. | W-15284493 | 
| MUnit tests using tracing module and "Set logging variable" now work as expected. | W-14773408 | 
| Using  | W-15081363 | 
| Template parser validation is now improved. | W-15141905 | 

DataWeave 2.6.2 is bundled with the Mule 4.6.2 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Inconsistent behavior no longer occurs between in-memory and streaming XML parsers for deciding document encoding. | W-15110015 | 
| Streaming for DataWeave-based data formats like  | W-15262860 | 
| The Excel reader no longer reads furigana characters. | W-14991276 | 
| Coercion of the third parameter on the ternary function executor now works as expected. | W-15061008 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## March 2024

Patch release version: 4.6.1

This patch update addresses the following Mule issues:

| Issue Resolution | ID | 
|---|---|
| Performance is now improved for certain For Each scenarios. | W-14678431 | 
| HTTP Request Connector no longer throws  | W-14686211 | 
| Disabling the  | W-14954677 | 
| Multi-step batch jobs can now be correctly resumed and finished after being stopped. | W-14726677 | 
| The error message is now improved for exceptions that occur when loading an extension because of Java version incompatibility. | W-14934626 | 
| The error message  | W-14559071 | 
| Transactions' timeout is now honored. When a transaction times out, it is rolled back, and an error is thrown that can be handled with error handling. To enable this, activate the  | W-14128870 | 
| Memory leaks no longer occur when using the  | W-14479158 | 
| Java JDK  | W-14645134 | 

DataWeave 2.6.1 is bundled with the Mule 4.6.1 release. This patch release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Performance is now improved when coercing addition and subtraction operations. | W-14927555 | 

For guidance with the patching process, see [Apply Patch Updates](patching-mule-versions#apply_patch_updates).

## February 6, 2024

### What’s New

The 4.6.0 version of Mule runtime introduces the following enhancements:

Java adoption:

- 
MuleSoft is adopting Java’s long-term support (LTS) release cadence, beginning with Mule runtime 4.6, which adds support for Java 17 LTS. See [Java Adoption](java-adoption).The maximum supported version for running your applications is Java 17 for Mule runtime 4.6.x and later. During the packaging of your app, all code, including third-party dependencies, **must**be compiled for Java 8.
- 
Java 17 manages memory differently than Java 8. See [Application Performance](../../general/java-support#application-performance).
- 
Mule runtime classes are now modularized per the Java module system introduced back in Java 9 (also known as JPMS or Project Jigsaw). Reflective introspection of Mule runtime classes is now limited. To maintain backward compatibility, reflective access to classes defined within the scope of your applications and domains remains open to access. 
- 
Java EE libraries are now removed from Mule runtime for Java 17. 

Mule Gateway improvements:

- 
You can now upgrade your policies and API proxies to Java 17. See [Upgrading Policies](../../general/java-support#policies)and[Upgrading API Proxies](../../general/java-support#api-proxies).
- 
Mule Gateway now supports API analytics event logging. To enable event logging, see [Log Analytics Event Data](../../mule-gateway/mule-gateway-metrics#log-analytics-event-data).
- 
Mule Gateway now supports automatically deleting cached policy files. To enable this feature, see [Cached Policy Assets Deletion](../../mule-gateway/policies-policy-overview#cached-policy-assets-deletion).

Mule SDK improvements:

- 
Mule SDK (Java SDK and XML SDK) now support Java 17. See [Upgrading Custom Connectors](../../general/java-support#custom-connectors).
- 
Java SDK now includes the new `@JavaVersionSupport`annotation. See[Supported Java Version Concept](../../general/customer-connector-upgrade#release-your-custom-connector).
- 
XML SDK now supports TLS. See [XML SDK TLS Support](../../mule-sdk/latest/xml-sdk#xml-sdk-tls).

General improvements:

- 
The Joda-Time library is upgraded to version 2.12.5. 
- 
The GraalJS library is upgraded to 22.3.3. 

### DataWeave Features

The 2.6.0 version of DataWeave introduces these new features and enhancements:

Extended format support:

- 
DataWeave now supports Java 17. See [Java Format](../../dataweave/latest/dataweave-formats-java).
- 
Mule expression language service are now modularized. 

### Fixed Issues

The release addresses the following Mule issues and incorporates all patch updates from the 4.5.0 Mule release through January 2023:

| Issue Resolution | ID | 
|---|---|
| 
 | W-13913357 | 
| The Joda-Time library is upgraded to version 2.12.5. | W-13913362 | 
| The GraalJS library is upgraded to 22.3.3. | W-13961780 | 
| MUnit no longer fails with apps using Anypoint Connector for DotNet (DotNet Connector). | W-14747448 | 
| 
 | W-14748090 | 
| Timeout is not considered for local transactions and rollbacks are silently executed. | W-14608096 | 
| MediaType cache now has a maximum size to prevent leaks. | W-14490182 | 
| DataWeave now uses objects as part of the Mule API. | W-14185880 | 
| License installation no longer fails with  | W-14542349 | 
| Legacy properties builder no longer reevaluates from root resolver placeholders. | W-14616618 | 
| 
 | W-12082402 | 
| HTTP Redirect no longer works on Mule runtime 4.x on HTTP Post. | W-14619216 | 
| Race condition no longer results in  | W-14543363 | 
| Container of the Embedded Runtime no longer stops if it wasn’t created. | W-14321634 | 
| Unnecessary MBeans for JMX management are no longer registered. | W-12422473 | 
| Internal dependency graph is now generated only once for all validations. | W-12421187 | 
| Extension model parsing no longer fails for extensions with dependencies declared as  | W-14646484 | 

DataWeave 2.6.0 is bundled with the Mule 4.6.0 release. This release addresses the following DataWeave issues:

| Issue Resolution | ID | 
|---|---|
| Caching now works correctly when coercing for addition and subtraction operations. | W-14591653 | 
| 
 | W-14514837 | 
| The  | W-14315728 | 

### Bundled Components

- 
DataWeave version 2.6.0 
- 
Runtime Manager Agent plugin version 2.6.0 

### Upgrade

If you are upgrading to this version of Mule from an earlier Mule 4.x version, see [Mule Upgrades and Patch Updates](mule-esb#mule-upgrades).

To ensure optimal performance with this version of Mule and avoid unexpected issues, update these modules and extensions to their latest version at the time of this release:

| Module or Extension | Version | 
|---|---|
| APIkit for Mule 4 | 1.10.1 | 
| APIkit for OData | 2.2.1 | 
| APIkit for OData 4 | 1.3.4 | 
| APIkit for SOAP | 1.4.1 | 
| APIkit for GraphQL | 1.0.0 | 
| Spring module | 1.3.11 | 
| MUnit plugin | 3.1.0 | 

### Considerations for Mule Extension Developers

If you update the version of your parent `pom.xml` file to 1.4.0 or later when you build a Mule extension, ensure that the dependencies in your `pom.xml` file do not override dependencies defined in the parent `pom.xml` file, and declare only the dependencies you need. If you need to declare a dependency that is already declared in the parent `pom.xml` file, do not specify a version so it uses the version from the parent `pom.xml` file.

## See Also

- 
[Salesforce Help](https://help.salesforce.com)
- 
[MuleSoft Services](https://www.mulesoft.com/support-and-services)