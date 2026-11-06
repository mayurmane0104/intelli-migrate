# Feature Flagging Mechanism | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/feature-flagging](https://docs.mulesoft.com/mule-runtime/latest/feature-flagging)

---

```
{
  "minMuleVersion": "4.1.0"
}
```
# Feature Flagging Mechanism

Mule runtime engine incorporates a feature flagging mechanism that enables Mule applications to change the behavior of the Mule instance depending on the required minimum Mule version. This feature ensures backward compatibility because it allows Mule applications to continue working on later Mule runtime versions, while new Mule applications can benefit from the latest bug fixes implemented in the Mule instance.

The feature flagging mechanism is automatic. For each Mule application deployed to a Mule instance, Mule determines which features are enabled or disabled based on the application’s minimum Mule version configured in the application descriptor file (`mule-artifact.json`) of the Mule app.

By default, Mule runtime engine disables any new features or bug fixes that aren’t backward compatible with Mule applications running in earlier Mule versions. However, it is possible to manage the feature flags configured for each Mule application or all applications running in the same Mule instance.

## Configure Feature Flags for a Mule Application

To configure feature flags for a Mule application, change the `minMuleVersion` value in the `mule-artifact.json` file of your app. This configuration instructs the Mule instance to run this application implementing all features and bug fixes that were released to that particular version and disabling features and bug fixes that are active by default in later Mule versions.

For example, you can run a Mule application in Mule 4.5.0 instructing the Mule instance to apply only the features that don’t change core functionality up to Mule 4.1.0:

`mule-artifact.json` file## Configure Feature Flags for the Mule Instance

An alternative way to configure feature flags is by using system properties. In this case, you can enable or disable each one of the available feature flags. However, configuring feature flags through system properties applies the changes at the Mule instance level, so all applications deployed to this Mule instance behave according to the configured feature flags.

Note that this configuration is compatible with on-premise deployments only because you cannot configure system properties in other deployment targets.

For example, you can configure a Mule 4.5.0 instance to enable and disable specific features for all applications running on this instance:

`wrapper.conf` file… wrapper.java.additional.999=-DHONOUR_RESERVED_PROPERTIES_PROPERTY=true wrapper.java.additional.1000=-DCOMPUTE_CONNECTION_ERRORS_IN_STATS_PROPERTY=false

## Feature Flags Reference

The following table shows the available feature flags, a description of their functionality, the Mule version in which the flag became available, the earlier minor version releases that enable the flag by default, and the issue ID in which the change was implemented:

| Feature Flag | Description | 
|---|---|
| 
 | When enabled, batch aggregators with fixed size aggregators commit only when a full block is processed. 
 
 
 
 
 
 | 
| 
 | When enabled, connection errors are computed as part of alerts triggering. 
 
 
 
 
 
 | 
| 
 | When enabled, the default error handler added by the Runtime doesn’t roll back a transaction if it doesn’t correspond to have this roll back made. 
 
 
 
 
 
 | 
| 
 | When enabled, DataWeave removes implicit inputs when a variable with the same name is declared at the root level. 
 
 
 
 
 
 | 
| 
 | When enabled, Mule manages extensions imported by a policy in complete isolation from the extensions imported by the Mule application. Also, validations prevent the use of explicit configurations that the application declared as part of the policy initialization. 
 
 
 
 
 
 | 
| 
 | When enabled, the Runtime profiling capabilities become available. 
 
 
 
 
 
 | 
| 
 | When enabled, the Mule XML DSL parser fails when deploying an application that declares a schema that cannot be located. Otherwise, the parser fails if the application also makes use of the namespace to which such a schema is bound. 
 
 
 
 
 
 | 
| 
 | When enabled, profiling consumers implemented by the Runtime are enabled by default. 
 
 
 
 
 
 | 
| 
 | When enabled, DataWeave correctly handles internal exceptions while splitting a payload, preventing subsequent serialization errors. 
 
 
 
 
 
 | 
| 
 | When enabled, reserved properties such as  
 
 
 
 
 
 | 
| 
 | When enabled, the operation policy’s error resolution is ignored. Therefore, the error mappings of the processor on which the policy is applied are set successfully. 
 
 
 
 
 
 | 
| 
 | When enabled, AbstractForkJoinRouter-based processors, such as Parallel For Each and Scatter-Gather routers, now show detailed error information for their failed routes. 
 
 
 
 
 
 | 
| 
 | When enabled, if the items to iterate over on a parallel-foreach scope are messages (such as the output of an operation that returns Result objects), they are flattened in a way that is consistent with what the foreach scope does. 
 
 
 
 
 
 | 
| 
 | When enabled, the Set Variable component creates a variable even if its value is  
 
 
 
 
 
 | 
| 
 | When enabled, extensions are only able to load exported resources from the deployable artifacts (application, policy, domain). 
 
 
 
 
 
 | 
| 
 | When enabled, managed cursor iterators transformed to strings show the representation of the elements instead of generic value  
 
 
 
 
 
 | 
| 
 | When enabled, error suppression occurs. This feature prevents components such as the Web Service Consumer connector and the Until Successful scope from reporting errors outside their namespaces. Example of an error log extract for a connectivity error at the Web Service Consumer (HTTP:CONNECTIVITY is being suppressed): Error type : WSC:INVALID_WSDL Caused by : HTTP:CONNECTIVITY Suppressed errors are treated as underlying causes that can also be matched by On Error handlers. 
 
 
 
 
 
 | 
| 
 | When enabled, error types validations are enforced even for error handlers/components that aren’t referenced. 
 
 
 
 
 
 | 
| 
 | When enabled, if an application accesses a native library, the rest of its declared native libraries are also loaded. This prevents errors like  
 
 
 
 
 
 | 
| 
 | When enabled, internal exceptions are rethrown instead of throwing a general  
 
 
 
 
 
 | 
| 
 | When this property is set to true, DataWeave retains a mixed-content structure instead of grouping text with mixed content into a single text field. 
 
 
 
 
 
 | 
| 
 | When enabled, error types validations are enforced, even for error handlers/components that aren’t being referenced. This feature isn’t configurable by system property. 
 
 
 
 
 
 | 
| 
 | When enabled, Mule trims whitespaces from parameter values defined at the attribute level in the DSL. 
 
 
 
 
 
 | 
| 
 | When enabled, Mule trims whitespaces from CDATA text parameter of pojos in the DSL. 
 
 
 
 
 
 | 
| 
 | When enabled, expression validations are enforced for  
 
 
 
 
 
 | 
| 
 | When enabled, expression validations are enforced for all DataWeave expressions. 
 
 
 
 
 
 | 
| 
 | When enabled, profiling consumers implemented by Mule are enabled by default. 
 
 
 
 
 
 | 
| 
 | When enabled,  
 
 
 
 
 
 
 
 | 
| 
 | When enabled,  
 
 
 
 
 
 | 
| 
 | When enabled, the application model is validated with the region classloader. When disabled, it is validated with the application classloader. 
 
 
 
 
 
 | 
| 
 | When enabled, error suppression happens. This affects, for example, the Web Service Consumer connector and the Until Successful scope that always reports errors from their corresponding namespaces (MULE and WSC). Suppressed errors are treated as underlying causes. 
 
 
 
 
 
 | 
| 
 | When enabled, the 'foreach' router generates an  
 
 
 
 
 
 | 
| 
 | When enabled, the insecure TLS configuration is honored even if there are fields of the TrustStore configured. 
 
 
 
 
 
 | 
| 
 | When enabled, flux sinks are cached using index as part of the key. If a sink is already in use, a new sink is created. 
 
 
 
 
 
 | 
| 
 | When enabled, a new (Source) Policy Context is created for the execution of parallel scopes: ParallelForeach, ScatterGather, and Async. 
 
 
 
 
 
 | 
| 
 | When enabled, the trace ID and span ID are added to the MDC when available. 
 
 
 
 
 
 | 
| 
 | When enabled, the  
 
 
 
 
 
 | 
| 
 | When enabled, MBeans isn’t registered for  
 
 
 
 
 
 | 
| 
 | When enabled, the Scheduler doesn’t log exceptions. 
 
 
 
 
 
 | 
| 
 | When enabled, an error is thrown when a local or XA transaction reach timeout. This error can be handled using error handling. 
 
 
 
 
 
 | 
| 
 | When enabled, implicit configuration for the XML SDK isn’t created. 
 
 
 
 
 
 | 
| 
 | When enabled, the MDC context resets after XML SDK operation is executed. 
 
 
 
 
 
 | 
| 
 | When enabled,  
 
 
 
 
 
 | 
| 
 | When enabled, the root element of  
 
 
 
 
 
 | 
| 
 | When enabled, flows honor the state configured in  
 
 
 
 
 
 | 
| 
 | When enabled, body contents aren’t sent on NTLM type 1 requests. This saves resources by not sending a payload that is never consumed (the server rejects the payload until the dance is completed). 
 
 
 
 
 
 | 
| 
 | When enabled, the processors that perform fork and join work (currently, Scatter-Gather and Parallel For Each routers) complete the child event contexts when a timeout occurs. 
 
 
 
 
 
 | 
| 
 | When enabled, the  
 
 
 
 
 
 | 
| 
 | When disabled, dynamic resolution of notification handling doesn’t occur after the Mule artifact is initialized. This can cause race conditions that affect monitoring metrics. 
 
 
 
 
 
 | 
| 
 | When enabled, the encrypted payload is encoded in hexadecimal format when no Expression ID is specified. 
 
 
 
 
 
 | 
| 
 | When enabled, events cancelled during a forceful shutdown raise a  
 
 
 
 
 
 | 
| 
 | When enabled, events aren’t retried if a  
 
 
 
 
 
 | 
| 
 | When enabled, batch processing uses batch errors instead of step exceptions. The DataWeave exception-based bindings  
 
 
 
 
 
 | 
| 
 | When enabled, the  
 
 
 
 
 
 | 
| 
 | When enabled, policies use the object store implementation configured for the application. This enables alternative implementations, such as Object Store v2, to be used by policies. 
 
 
 
 
 
 | 
| 
 | When enabled, inline TLS contexts invoke their lifecycle initialization method, ensuring inline TLS contexts are fully initialized before use. 
 
 
 
 
 
 | 
| 
 | When enabled, all Mule flows are stopped in parallel rather than sequentially when a Mule application is stopped. This prevents delays caused by in-flight events in one flow from delaying the shutdown of other flows. 
 
 
 
 
 
 | 
| 
 | When enabled,  
 
 
 
 
 
 |