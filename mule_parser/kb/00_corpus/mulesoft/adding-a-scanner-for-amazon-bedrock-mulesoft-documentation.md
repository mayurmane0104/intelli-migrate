# Adding a Scanner for Amazon Bedrock | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/adding-amazon-bedrock-scanner](https://docs.mulesoft.com/exchange/adding-amazon-bedrock-scanner)

---

# Adding a Scanner for Amazon Bedrock

Add a scanner to discover, import, and sync agents from Amazon Bedrock into Exchange. Then you can govern the agents and consume them in other applications.

## Before You Begin

Before adding the scanner, verify that you have the permission, context, and these Amazon Bedrock credentials:

- 
Exchange Administrator permission 
- 
Knowledge about the Amazon Web Services region where the agents are deployed. 
- 
Amazon Bedrock access key ID 
- 
Amazon Bedrock secret access key 
- 
Ensure you have these Amazon Bedrock permissions: - 
bedrock:ListAgents 
- 
bedrock:GetAgent 
- 
bedrock:ListAgentAliases 
- 
bedrock:GetAgentAlias 
- 
bedrock:ListAgentVersions 
- 
bedrock:GetAgentVersion 
 
- 
- 
To make sure the scanner discovers the agent, assign an alias and link that alias to a version. The scanner ignores agents without an invocable URL. 

## Add a Scanner for Amazon Bedrock

- 
Verify that you are in the business group where you want to add the scanner. 
- 
From the sidebar in Exchange, click **Scanners**.
- 
Enter a name for the scanner. 
- 
From **Scanner Run Configuration**, complete these fields or options:**Field/Option****Value****Run Schedule**Select a frequency and time. **Sync Review**Select Auto-resolve. 
- 
From **Connection Configuration**, complete these fields:**Field****Value****Provider**Select **Amazon**.**Platform**Select **AWS Bedrock**.**Authentication Method**Select **Access key**.**Access Key ID**Enter the access key ID. **Secret Access Key**Enter the secret access key. **AWS Region**Select a region. 
- 
Click **Test Connection**.If the connection fails, review the **Connection Configuration**settings. Update the settings, and then test the connection again.
- 
To send email notifications: - 
Select **Advanced Settings**and turn on**Send Email Notifications**.
- 
Enter an email address. 
 
- 
- 
Click **Add Scanner**.