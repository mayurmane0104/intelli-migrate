# Adding a Scanner for Google Apigee | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/exchange/adding-apigee-scanner](https://docs.mulesoft.com/exchange/adding-apigee-scanner)

---

# Adding a Scanner for Google Apigee

Add a scanner to discover, import, and sync APIs from Google Apigee into Anypoint Exchange. Once imported, you can apply governance rulesets and publish them to your developer portal.

## Before You Begin

Before adding the scanner, verify that you have the permission, context, and these Google Apigee credentials:

- 
Exchange Administrator permission 
- 
Apigee Read-only Admin permission 
- 
Google Cloud Platform (GCP) project ID 
- 
Service account email 
- 
Private key 

## Add a Scanner for Google Apigee

- 
Verify that you are in the business group where you want to add the scanner. 
- 
From the sidebar in Exchange, click **Scanners**.
- 
Enter a name for the scanner. 
- 
From **Scanner Run Configuration**, complete these fields or options:**Field/Option****Value****Run Schedule**Select a frequency and local time. **Sync Review**Select an option: Auto-resolve or Ask to review. 
- 
From **Connection Configuration**, complete these fields:**Field****Value****Provider**Select **Google**.**Platform**Select **Google Apigee**.**Service Type****REST APIs**selected by default.**Authentication Method****Service Account**selected by default.**GCP Project ID**Enter the Google Cloud Platform project ID. **Service Account Email**Enter the service account email. **Private Key**Enter the private key. 
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