# Setting Up Monitoring for CloudHub Deployments | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/monitoring/configure-monitoring-cloudhub](https://docs.mulesoft.com/monitoring/configure-monitoring-cloudhub)

---

- 
For new and existing Mule apps: - 
Go to **Settings**in Runtime Manager for that app.
- 
Choose the new runtime from the **Runtime Version**selector.If you do not see a supported runtime version in the drop-down menu, scroll down to **Show Old Patch Releases**, click, and select a runtime for your app.
 
- 
- 
For Anypoint CLI deployments: If you are using the Anypoint CLI to deploy your Mule app (for example, through a build pipeline), you need to include the `--runtime`parameter with an appropriate value, for example:anypoint-cli --username="..." --password="..." --organization="Mythical, Inc" --environment="Production" runtime-mgr cloudhub-application deploy --runtime="3.9.4" helloworld ~/demoproj2.zip 
- 
For Maven deployments: If you are using Maven for deployment, you must modify the `<muleVersion>`tag in the`pom.xml`file. For example, you can change`<muleVersion>3.9.3</muleVersion>`to`<muleVersion>3.9.4</muleVersion>`).

# Setting Up Monitoring for CloudHub Deployments

To start monitoring Mule apps that are managed in CloudHub, you must deploy them to a supported version of Mule runtime engine and set the runtime version in your Mule app.

CloudHub 2.0: Anypoint Monitoring is enabled by default for Mule apps deployed to CloudHub 2.0.
For path normalization configuration in CloudHub 2.0 and CloudHub, see [Normalize API Paths](#normalize-path).

## Supported Versions of Mule Deployed to CloudHub

Run your Mule app on a supported Mule runtime version. For supported versions, see [Mule Runtime Release Notes](../release-notes/mule-runtime/mule-esb).

If you are not running a supported Mule runtime version, update the version in Runtime Manager.

## Show me how

[Logging in Anypoint Monitoring](logs) is available only if your organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform.

## Enable Monitoring by Default for New Apps

If you want your Mule apps to be monitored by default when you deploy them to CloudHub, configure this feature in Anypoint Monitoring before you deploy your apps. If your organization has the Anypoint Integration Advanced package or a Titanium subscription to Anypoint Platform, this feature is enabled by default.

To configure automatic monitoring for each Mule app as it is deployed to CloudHub:

- 
Log in to Anypoint Platform with a user account that has [permission to access Anypoint Monitoring content](am-permissions).
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
In the sidebar, click **Settings**:
- 
Select **CloudHub**.
- 
Select **Enable Anypoint Monitoring for newly deployed CloudHub applications**.

If you deployed Mule apps to CloudHub before you enabled this feature, you must enable monitoring for those apps manually. This feature does not retroactively enable monitoring for previously deployed apps.

## Enable Monitoring for Apps Previously Deployed to CloudHub

You can enable monitoring for Mule apps running on non-AM versions of Mule in the Anypoint Monitoring **Settings** page, the application’s **Settings** page, or by using the Anypoint CLI for continuous integration and delivery (CI/CD).

For supported versions of Mule, see [Configure Anypoint Monitoring for Mule Apps](#).

### Enable Monitoring for an App in Monitoring Settings

Use the **Settings** page in Anypoint Monitoring to enable or disable monitoring for apps deployed to CloudHub and running on Mule:

- 
Log in to Anypoint Platform with a user account that has [permission to access Anypoint Monitoring content](am-permissions).
- 
Navigate to Anypoint Monitoring: Click **Monitoring**from the Anypoint Platform home page or from the**Runtimes**menu in the header.
- 
In the sidebar, click **Settings**:
- 
Select **CloudHub**.
- 
In the **Environment**list, select the environment where the application is running.A list of running applications is shown for the selected environment. You can search for a specific application using the **List of resources**search box.
- 
Next to the application, click **Enable**to enable monitoring for the application.

### Enable Monitoring for an App in Runtime Manager Settings

Enable monitoring for Mule apps running on supported versions of Mule by adding a property to an application deployed to CloudHub:

- 
Log in to Anypoint Platform. 
- 
Navigate to **Runtime Manager**.
- 
In the list of applications, select the application for which you want to enable monitoring. The application must be deployed to CloudHub and running on a supported version of Mule. 
- 
In the navigation menu, click **Settings**.
- 
Click **Properties**, and add the following property to the**Text**view:
 `anypoint.platform.config.analytics.agent.enabled=true`
- 
Click **Apply Changes**.

### Enable Monitoring using the Anypoint CLI

Use the Anypoint CLI and set the following property during your CI/CD deployment:
`anypoint.platform.config.analytics.agent.enabled=true`

## Performance Impact

Enabling Anypoint Monitoring can impact CPU utilization and memory utilization, which varies depending upon specific application behavior, such as inbound and outbound call rates. For a typical application, expected CPU utilization impact is less than 5%. For an accurate impact analysis specific to your application, test and estimate any performance impact in your pre-production environment prior to enabling monitoring in your production environment.

## Normalize API Paths

Proper path normalization helps to ensure correct counting of requests to inbound HTTP endpoints in Runtime Manager and Anypoint Monitoring dashboards. Normalization enables charts in these dashboards to ignore insignificant differences, typically from dynamic variables, between URLs that make requests to the same endpoint.

For inbound HTTP endpoints, you can rely on the [default path normalization](#normalization-default) or configure a [custom normalization pattern](#normalization-custom) with the `anypoint.platform.config.analytics.endpoint.patterns` property.

Supported deployment types:

- 
CloudHub 
- 
CloudHub 2.0 
- 
Hybrid 
- 
Runtime Fabric 

### Default Path Normalization

The default path normalization process follows these substitution patterns for:

- 
Digits: Replace any part of the path containing a digit with `X`. For example,`/booking/abc123/pax/A1B2C4`becomes`/booking/X/pax/X`.
- 
Uppercase segments: Replace any part of the path containing uppercase characters but no lower case characters with `X`. For example,`/booking/ABC/pax/A1B2C4`becomes`/booking/X/pax/X`.

Parts that contain a mix of upper case and lower case characters remain the same. For example, `/booking/abc123/pax/PAisdf` remains `/booking/X/pax/PAisdf`.

### Configure a Custom Path Normalization Pattern

To override the default behavior, you can configure `anypoint.platform.config.analytics.endpoint.patterns` on a running Mule app in Runtime Manager or when deploying a new application:

- 
Log in to your Anypoint Platform account and select **Runtime Manager**.
- 
Either click **Deploy Application**for a new deployment, or select an existing application and click**Manage Application**.
- 
Navigate to the **Properties**tab in the**Settings**section.
- 
Under **New Key**, add`anypoint.platform.config.analytics.endpoint.patterns`.
- 
Under **New Value**, add the pattern for your dynamic endpoint, for example,`/api/V1/proc/payments/{paymentId}/cancel`.
- 
Click **Apply Changes**.

By defining an explicit pattern, you can ensure consistent normalization of dynamic endpoints. All incoming requests matching the pattern are correctly normalized to a single endpoint.

For example, provide a pattern that identifies the variable part.

For variables, you can use:

- 
`{}`with an empty string
- 
`{string}`with a string value

For example, assume property values that follow these patterns:

- 
`/v1/payments/{paymentId}/cancel`(single property)
- 
`/v1/order/{orderId},/v1/order/{}/cancel`(multiple properties separated by`,`)

These incoming requests match one of the defined patterns:

- 
`/v1/order/jAXjh`
- 
`/v1/payments/CAjjAXjh/cancel`
- 
`/v1/order/jAXjh/cancel`

Normalized results for the example requests:

- 
`/v1/payments/X/cancel`
- 
`/v1/order/X`
- 
`/v1/order/X/cancel`