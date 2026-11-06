# Configure Slack Integration | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/tut-slack-configure-integration](https://docs.mulesoft.com/anypoint-code-builder/tut-slack-configure-integration)

---

![A workflow with the *Temporary Logger* component highlighted, both in the flow canvas UI and in the code view](_images/delete-temporary-logger-slack.png) 

# Configure Slack Integration

With your email and Salesforce integration complete, you can now configure your Slack integration to send a Slack message for a new case that is not escalated.

## Before You Begin

Complete these procedures:

- 
[Integrate Salesforce Data into Slack and Email Notifications](tut-slack-create-escalation-api).
- 
[Create a Configuration File for Slack and Salesforce](tut-slack-create-config-files-sfdc)and configure your Salesforce integration.

## Add a Slack Action

- 
In Anypoint Code Builder, open your `new-case-salesforce.xml`file and delete**Temporary Logger**from the**Not Escalated**route of the Choice router:![A workflow with the *Temporary Logger* component highlighted, both in the flow canvas UI and in the code view](_images/delete-temporary-logger-slack.png)  `<logger doc:name="Temporary Logger" message='#["Please look into this new Case: " ++ payload]'/>`XML
- 
Click the ![](_images/icon-plus.png) ( (**Add component**) icon after the**Not Escalated**route of the Choice router:![A flow in the canvas UI with the *Add Component* button highlighted](_images/add-slack-action-example-canvas.png)  
- 
Click the ![](_images/icon-search-exchange.png) ( (**Search in Exchange**) icon, type`Slack`, and select**Slack Connector**:![A list of search results with the Slack connector highlighted](_images/add-slack-connector-canvas-exchange.png)  
- 
Select the **Chat: Post Message**operation from the Slack section:![A list of search results containing Slack connector components](_images/select-post-message-operation.png)  
- 
Configure the Slack operation using the following code sample: `<slack:post-message channel="this-is-a-test" config-ref="Slack_Config" doc:name="Send Case to Slack">`**(1)**<slack:message ><![CDATA[#["Please handle this case. " ++ payload]]]></slack:message> </slack:post-message>XML**1**Set the `channel`field to the channel name that you set earlier in the tutorial.

## Configure the Slack Connection

- 
In Anypoint Code Builder, open your `new-case-salesforce.xml`file, and add a new line under your`<email:smtp-config/>`element.
- 
Type `slack:`and select**slack:config**.
- 
Add the following configuration to your `<slack:config/>`element:`<slack:config name="Slack_Config" doc:name="Slack Config"> <slack:token-connection token="${slack.token}" /> </slack:config>`XML

## Test Your Mule Application

- 
To expedite the test, remove the breakpoint next to your Logger component. 
- 
Select **Run**>**Start Debugging (F5)**.
- 
After your application deploys successfully, log in to your Salesforce account. 
- 
From **App Launcher**, select**Service**:![The Setup menu with the App Launcher button icon highlighted](_images/salesforce-select-service.png)  
- 
Select **Cases**>**New Case**:![The Service navigation bar with the *New Case* button highlighted in the Cases section](_images/salesfroce-create-new-case.png)  
- 
Ensure that the **Status**of the new case is**New**.
- 
After a few seconds, ensure that your configured Slack channel received a message with the information configured in the case: `Please handle this case. Case Number: 00001030, Origin: Phone, Case Type: , Priority: Medium, Status: New`

[Add a Condition to Your Flow Logic](tut-slack-add-condition-to-your-flow)