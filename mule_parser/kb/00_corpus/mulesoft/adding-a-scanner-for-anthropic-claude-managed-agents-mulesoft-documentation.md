# Adding a Scanner for Anthropic Claude Managed Agents | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/adding-claude-scanner](https://docs.mulesoft.com/exchange/adding-claude-scanner)

---

# Adding a Scanner for Anthropic Claude Managed Agents

Add a scanner to discover, import, and sync agents from Claude Managed Agents into Exchange. Then you can govern the agents and consume them in other applications.

## Before You Begin

Before adding the scanner, verify that you have these:

- 
Exchange Administrator permission 
- 
Paid Anthropic account 
- 
Claude API key 

## Add a Scanner for Anthropic Claude Managed Agents

- 
Verify that you are in the business group where you want to add the scanner. 
- 
From the sidebar in Exchange, click **Scanners**.
- 
Enter a name for the scanner. 
- 
From **Scanner Run Configuration**, complete these fields or options:**Field/Option****Value****Run Schedule**Select a frequency and time. **Sync Review**Select an option: **Auto-resolve**or**Ask to review**.
- 
From **Connection Configuration**, complete these fields:**Field****Value****Provider**Select **Anthropic**.**Platform**Select **Anthropic Claude**.**Service Type****Agents**selected by default.**Authentication Method**Select **Access Keys**.**API Key**Enter the API key. 
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