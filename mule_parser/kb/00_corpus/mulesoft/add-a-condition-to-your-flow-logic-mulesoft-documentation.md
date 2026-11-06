# Add a Condition to Your Flow Logic | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/tut-slack-add-condition-to-your-flow](https://docs.mulesoft.com/anypoint-code-builder/tut-slack-add-condition-to-your-flow)

---

![A flow diagram with the Add Component button icon highlighted](_images/add-choice-router-slack-escalation-canvas.png) 

# Add a Condition to Your Flow Logic

In this section of the tutorial, you learn how to add a condition to your flow to send an email to the regional leader if the Salesforce case is escalated, otherwise your Mule application sends a message to Slack.

## Before You Begin

Complete these procedures:

- 
[Integrate Salesforce Data into Slack and Email Notifications](tut-slack-create-escalation-api).
- 
[Create a Configuration File for Slack and Salesforce](tut-slack-create-config-files-sfdc)and configure your Salesforce integration.

## Define the Behavior for When the Case Is Escalated

Use a Choice router to define behaviors based on specific conditions. In this case, choose to send an email if the case is escalated.

- 
In Anypoint Code Builder, open your `new-case-salesforce.xml`file.
- 
Click the ![](_images/icon-plus.png) ( (**Add component**) icon for the Logger component:![A flow diagram with the Add Component button icon highlighted](_images/add-choice-router-slack-escalation-canvas.png)  
- 
Type `choice`and select**Choice**under**Flow Control**:
- 
Add the `<when/>`and`<otherwise/>`elements:![Search result for 'when', with resulting highlighted text reading 'mule:when'](_images/sync-api-choice-when.png)  `<choice doc:name="Choice"> <when doc:name="When" > </when> <otherwise doc:name="Otherwise" > </otherwise> </choice>`XMLFor better readability of your Mule flow, update the name of the `<choice/>`,`<when/>`, and`<otherwise/>`elements:`<choice doc:name="Is Case Escalated?"> <when doc:name="Escalated" > </when> <otherwise doc:name="Not Escalated" > </otherwise> </choice>`XML
- 
Define the `when`branch to execute if the variable`casestatus`equals`Escalated`:`<choice doc:name="Is Case Escalated?"> <when doc:name="Escalated" expression='#[vars.casestatus == "Escalated"]'> </when> <otherwise doc:name="Not Escalated" > </otherwise> </choice>`XML

## Add an Email Connector

To configure the `<when/>` element, you must first configure operations from the Anypoint Connector for Email (Email Connector):

- 
In Anypoint Code Builder, open your `new-case-salesforce.xml`file, and add a new line under your`<salesforce:sfdc-config/>`element.
- 
Type `smtp`and select**email:smtp-config**:`<email:smtp-config name="Email_SMTP"> <email:smtps-connection host="${email.host}" user="${email.username}" password="${email.password}"> <tls:context> <tls:trust-store insecure="true" /> </tls:context> </email:smtps-connection> </email:smtp-config>`XML
- 
Click the ![](_images/icon-plus.png) ( (**Add component**) icon after the**Escalated**section:![A Choice flow with the Escalated Add Component button icon highlighted](_images/add-email-operation-slack-integration-canvas.png)  
- 
Type `send`and select**Send**from the**Email**section:![A list of components in the search results section, with Send highlighted](_images/send-email-slack-integration-canvas.png)  
- 
Configure `send`using the following code sample:`<email:send config-ref="Email_SMTP" doc:name="Send Escalation Email" subject='#["Case " ++ vars.casenumber ++ " was escalated"]'> <email:to-addresses> <email:to-address value="${email.username}" /> </email:to-addresses> <email:body contentType="text/html" > <email:content ><![CDATA[#["Please handle this case. " ++ payload]]]></email:content> </email:body> </email:send>`XML
- 
To be able to test the application, temporarily add a `<logger/>`element inside your`<otherwise/>`element:`<logger doc:name="Temporary Logger" message='#["Please look into this new Case: " ++ payload]'/>`XML
- 
Examine your full Choice router configuration: `<choice doc:name="Is Case Escalated?"> <when doc:name="Escalated" expression='#[vars.casestatus == "Escalated"]'> <email:send config-ref="Email_SMTP" doc:name="Send Escalation Email" subject='#["Case " ++ vars.casenumber ++ " was escalated"]'> <email:to-addresses> <email:to-address value="${email.username}" /> </email:to-addresses> <email:body contentType="text/html" > <email:content ><![CDATA[#["Please handle this case. " ++ payload]]]></email:content> </email:body> </email:send> </when> <otherwise doc:name="Not Escalated" > <logger doc:name="Temporary Logger" message='#["Please look into this new Case: " ++ payload]'/> </otherwise> </choice>`XML

## Test Your Mule Application

- 
To expedite the test, remove the breakpoint for your Logger component. 
- 
Select **Run**>**Start Debugging (F5)**.
- 
After your application deploys successfully, log in to your Salesforce account. 
- 
From **App Launcher**, select**Service**:![The Setup menu with Home and Service options highlighted](_images/salesforce-select-service.png)  
- 
Select **Cases**>**New Case**:![The Service navigation bar with the New Case button highlighted in the Cases section](_images/salesfroce-create-new-case.png)  
- 
Ensure that the **Status**of the new case is**Escalated**.
- 
After a few seconds, ensure that your configured email account received an email with the information configured in the case: `Please handle this case. Case Number: 00001030, Origin: Phone, Case Type: , Priority: Medium, Status: Escalated`
- 
Proceed to [Configure Slack Integration](tut-slack-configure-integration)to learn how to configure the Slack message for any case that was not escalated.

[Extract Payload Information to Variables](tut-slack-extract-payload-information)

[Configure Slack Integration](tut-slack-configure-integration)