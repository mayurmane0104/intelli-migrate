# Add Instance Alerts in API Manager (Mule Gateway) | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/add-api-alert-task](https://docs.mulesoft.com/api-manager/latest/add-api-alert-task)

---

# Add Instance Alerts in API Manager (Mule Gateway)

Instance alerts in API Manager email recipients when request volume, response codes, response times, or other conditions cross thresholds you set for an API instance on Mule Gateway.
You name each alert, set severity, choose from [alert types](using-api-alerts), configure time ranges as sliding windows, and specify email recipients.
Policy Violation alerts are unavailable for [automated policies](../../gateway/latest/policies-automated-overview), and Omni Gateway instances use [a separate alert workflow](../../gateway/latest/flex-use-api-alerts).

| This task applies to Mule Gateway runtimes only. To add alerts to instances that use Omni Gateway as their runtime, see [Using Omni Gateway API Alerts](../../gateway/latest/flex-use-api-alerts). | 

## Configure an Instance Alert

To add an alert to a Mule Gateway instance:

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
In **API Administration**, click the instance to which to add an alert.
- 
Click **Alerts**>**Add alert**.
- 
Specify the alert options: - 
**Name**:Type an alert name, for example `trial-alert`.If adding multiple alerts to the same environment, the alerts must have unique names. 
- 
**Enabled**:The default option is **Enabled**.You can delete an alert anytime if not required. 
- 
**Severity**:Select a severity for the alert, for example, **Info**.
- 
**Alert type**:Select the type of alert to create, (for example, **Request Count**) and provide appropriate alert configuration values. For information about alert types, see[Instance Alerts](using-api-alerts#api-alerts).In the **For at least**and**consecutive period(s) of**fields, enter a value in the range of 1 - 999999999 to specify the time interval as a[sliding window](https://www.techopedia.com/definition/869/sliding-window).
 
- 
- 
Select **Recipients**.Specify which email addresses receive the email notification. 
- 
Click **Create Alert**.