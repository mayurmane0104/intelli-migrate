# Adding a Scanner for LangChain LangSmith | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/adding-langsmith-scanner](https://docs.mulesoft.com/exchange/adding-langsmith-scanner)

---

# Adding a Scanner for LangChain LangSmith

Add a scanner to discover, import, and sync agents from LangSmith into Exchange. Then you can govern the agents and consume them in other applications.

## Before You Begin

Before adding the scanner, verify that you have these:

- 
Exchange Administrator permission 
- 
Plus plan (or higher) workspace in LangSmith 
- 
LangSmith API key for the workspace 
- 
LangSmith workspace ID 

## Add a Scanner for LangChain LangSmith

- 
Verify that you are in the business group where you want to add the scanner. 
- 
From the sidebar in Exchange, click **Scanners**.
- 
Enter a name for the scanner. 
- 
From **Scanner Run Configuration**, complete these fields or options:**Field/Option****Value****Run Schedule**Select a frequency and time. **Sync Review**Select an option: **Auto-resolve**or**Ask to review**.
- 
From **Connection Configuration**, complete these fields:**Field****Value****Provider**Select **LangChain**.**Platform**Select **LangSmith**.**Service Type****Agents**is selected by default.**Authentication Method****Access Keys**selected by default.**LangSmith API Key**Enter the API key. **Workspace ID**Enter the workspace ID. **Region**Select the region for your workspace: US or EU. Default is the US region. 
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