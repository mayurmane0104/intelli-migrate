# Amazon SES examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ses_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ses_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon SES.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-identity`.

- **AWS CLI**
- 
            
                    **To delete an identity**The following example uses the `delete-identity`command to delete an identity from the list of identities verified with Amazon SES:`aws ses delete-identity --identity``user@example.com`For more information about verified identities, see Verifying Email Addresses and Domains in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [DeleteIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-identity-dkim-attributes`.

- **AWS CLI**
- 
            
                    **To get the Amazon SES Easy DKIM attributes for a list of identities**The following example uses the `get-identity-dkim-attributes`command to retrieve the Amazon SES Easy DKIM attributes for a list of identities:`aws ses get-identity-dkim-attributes --identities``"example.com"``"user@example.com"`Output: `{ "DkimAttributes": { "example.com": { "DkimTokens": [ "EXAMPLEjcs5xoyqytjsotsijas7236gr", "EXAMPLEjr76cvoc6mysspnioorxsn6ep", "EXAMPLEkbmkqkhlm2lyz77ppkulerm4k" ], "DkimEnabled": true, "DkimVerificationStatus": "Success" }, "user@example.com": { "DkimEnabled": false, "DkimVerificationStatus": "NotStarted" } } }`If you call this command with an identity that you have never submitted for verification, that identity won't appear in the output. For more information about Easy DKIM, see Easy DKIM in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [GetIdentityDkimAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-dkim-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-identity-notification-attributes`.

- **AWS CLI**
- 
            
                    **To get the Amazon SES notification attributes for a list of identities**The following example uses the `get-identity-notification-attributes`command to retrieve the Amazon SES notification attributes for a list of identities:`aws ses get-identity-notification-attributes --identities``"user1@example.com"``"user2@example.com"`Output: `{ "NotificationAttributes": { "user1@example.com": { "ForwardingEnabled": false, "ComplaintTopic": "arn:aws:sns:us-east-1:EXAMPLE65304:MyTopic", "BounceTopic": "arn:aws:sns:us-east-1:EXAMPLE65304:MyTopic", "DeliveryTopic": "arn:aws:sns:us-east-1:EXAMPLE65304:MyTopic" }, "user2@example.com": { "ForwardingEnabled": true } } }`This command returns the status of email feedback forwarding and, if applicable, the Amazon Resource Names (ARNs) of the Amazon SNS topics that bounce, complaint, and delivery notifications are sent to. If you call this command with an identity that you have never submitted for verification, that identity won't appear in the output. For more information about notifications, see Using Notifications With Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [GetIdentityNotificationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-notification-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-identity-verification-attributes`.

- **AWS CLI**
- 
            
                    **To get the Amazon SES verification status for a list of identities**The following example uses the `get-identity-verification-attributes`command to retrieve the Amazon SES verification status for a list of identities:`aws ses get-identity-verification-attributes --identities``"user1@example.com"``"user2@example.com"`Output: `{ "VerificationAttributes": { "user1@example.com": { "VerificationStatus": "Success" }, "user2@example.com": { "VerificationStatus": "Pending" } } }`If you call this command with an identity that you have never submitted for verification, that identity won't appear in the output. For more information about verified identities, see Verifying Email Addresses and Domains in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [GetIdentityVerificationAttributes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-identity-verification-attributes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-send-quota`.

- **AWS CLI**
- 
            
                    **To get your Amazon SES sending limits**The following example uses the `get-send-quota`command to return your Amazon SES sending limits:`aws ses get-send-quota`Output: `{ "Max24HourSend": 200.0, "SentLast24Hours": 1.0, "MaxSendRate": 1.0 }`Max24HourSend is your sending quota, which is the maximum number of emails that you can send in a 24-hour period. The sending quota reflects a rolling time period. Every time you try to send an email, Amazon SES checks how many emails you sent in the previous 24 hours. As long as the total number of emails that you have sent is less than your quota, your send request will be accepted and your email will be sent. SentLast24Hours is the number of emails that you have sent in the previous 24 hours. MaxSendRate is the maximum number of emails that you can send per second. Note that sending limits are based on recipients rather than on messages. For example, an email that has 10 recipients counts as 10 against your sending quota. For more information, see Managing Your Amazon SES Sending Limits in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [GetSendQuota](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-send-quota.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-send-statistics`.

- **AWS CLI**
- 
            
                    **To get your Amazon SES sending statistics**The following example uses the `get-send-statistics`command to return your Amazon SES sending statistics`aws ses get-send-statistics`Output: `{ "SendDataPoints": [ { "Complaints": 0, "Timestamp": "2013-06-12T19:32:00Z", "DeliveryAttempts": 2, "Bounces": 0, "Rejects": 0 }, { "Complaints": 0, "Timestamp": "2013-06-12T00:47:00Z", "DeliveryAttempts": 1, "Bounces": 0, "Rejects": 0 } ] }`The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute interval. In this example, there are only two data points because the only emails that the user sent in the last two weeks fell within two 15-minute intervals. For more information, see Monitoring Your Amazon SES Usage Statistics in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [GetSendStatistics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-send-statistics.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-identities`.

- **AWS CLI**
- 
            
                    **To list all identities (email addresses and domains) for a specific AWS account**The following example uses the `list-identities`command to list all identities that have been submitted for verification with Amazon SES:`aws ses list-identities`Output: `{ "Identities": [ "user@example.com", "example.com" ] }`The list that is returned contains all identities regardless of verification status (verified, pending verification, failure, etc.). In this example, email addresses *and*domains are returned because we did not specify the identity-type parameter.For more information about verification, see Verifying Email Addresses and Domains in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [ListIdentities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-identities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-email`.

- **AWS CLI**
- 
            
                    **To send a formatted email using Amazon SES**The following example uses the `send-email`command to send a formatted email:`aws ses send-email --from``sender@example.com`--destination`file://destination.json`--message`file://message.json`Output: `{ "MessageId": "EXAMPLEf3a5efcd1-51adec81-d2a4-4e3f-9fe2-5d85c1b23783-000000" }`The destination and the message are JSON data structures saved in .json files in the current directory. These files are as follows: `destination.json`:`{ "ToAddresses": ["recipient1@example.com", "recipient2@example.com"], "CcAddresses": ["recipient3@example.com"], "BccAddresses": [] }``message.json`:`{ "Subject": { "Data": "Test email sent using the AWS CLI", "Charset": "UTF-8" }, "Body": { "Text": { "Data": "This is the message body in text format.", "Charset": "UTF-8" }, "Html": { "Data": "This message body contains HTML formatting. It can, for example, contain links like this one: <a class=\"ulink\" href=\"http://docs.aws.amazon.com/ses/latest/DeveloperGuide\" target=\"_blank\">Amazon SES Developer Guide</a>.", "Charset": "UTF-8" } } }`Replace the sender and recipient email addresses with the ones you want to use. Note that the sender's email address must be verified with Amazon SES. Until you are granted production access to Amazon SES, you must also verify the email address of each recipient unless the recipient is the Amazon SES mailbox simulator. For more information on verification, see Verifying Email Addresses and Domains in Amazon SES in the *Amazon Simple Email Service Developer Guide*.The Message ID in the output indicates that the call to send-email was successful. If you don't receive the email, check your Junk box. For more information on sending formatted email, see Sending Formatted Email Using the Amazon SES API in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [SendEmail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-email.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `send-raw-email`.

- **AWS CLI**
- 
            
                    **To send a raw email using Amazon SES**The following example uses the `send-raw-email`command to send an email with a TXT attachment:`aws ses send-raw-email --raw-message``file://message.json`Output: `{ "MessageId": "EXAMPLEf3f73d99b-c63fb06f-d263-41f8-a0fb-d0dc67d56c07-000000" }`The raw message is a JSON data structure saved in a file named `message.json`in the current directory. It contains the following:`{ "Data": "From: sender@example.com\nTo: recipient@example.com\nSubject: Test email sent using the AWS CLI (contains an attachment)\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; boundary=\"NextPart\"\n\n--NextPart\nContent-Type: text/plain\n\nThis is the message body.\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename=\"attachment.txt\"\n\nThis is the text in the attachment.\n\n--NextPart--" }`As you can see, "Data" is one long string that contains the entire raw email content in MIME format, including an attachment called attachment.txt. Replace sender@example.com and recipient@example.com with the addresses you want to use. Note that the sender's email address must be verified with Amazon SES. Until you are granted production access to Amazon SES, you must also verify the email address of the recipient unless the recipient is the Amazon SES mailbox simulator. For more information on verification, see Verifying Email Addresses and Domains in Amazon SES in the *Amazon Simple Email Service Developer Guide*.The Message ID in the output indicates that the call to send-raw-email was successful. If you don't receive the email, check your Junk box. For more information on sending raw email, see Sending Raw Email Using the Amazon SES API in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [SendRawEmail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-raw-email.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-identity-dkim-enabled`.

- **AWS CLI**
- 
            
                    **To enable or disable Easy DKIM for an Amazon SES verified identity**The following example uses the `set-identity-dkim-enabled`command to disable DKIM for a verified email address:`aws ses set-identity-dkim-enabled --identity``user@example.com`--no-dkim-enabledFor more information about Easy DKIM, see Easy DKIM in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [SetIdentityDkimEnabled](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/set-identity-dkim-enabled.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-identity-feedback-forwarding-enabled`.

- **AWS CLI**
- 
            
                    **To enable or disable bounce and complaint email feedback forwarding for an Amazon SES verified identity**The following example uses the `set-identity-feedback-forwarding-enabled`command to enable a verified email address to receive bounce and complaint notifications by email:`aws ses set-identity-feedback-forwarding-enabled --identity``user@example.com`--forwarding-enabledYou are required to receive bounce and complaint notifications via either Amazon SNS or email feedback forwarding, so you can only disable email feedback forwarding if you select an Amazon SNS topic for both bounce and complaint notifications. For more information about notifications, see Using Notifications With Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [SetIdentityFeedbackForwardingEnabled](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/set-identity-feedback-forwarding-enabled.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-identity-notification-topic`.

- **AWS CLI**
- 
            
                    **To set the Amazon SNS topic to which Amazon SES will publish bounce, complaint, and/or delivery notifications for a verified identity**The following example uses the `set-identity-notification-topic`command to specify the Amazon SNS topic to which a verified email address will receive bounce notifications:`aws ses set-identity-notification-topic --identity``user@example.com`--notification-type`Bounce`--sns-topic`arn:aws:sns:us-east-1:EXAMPLE65304:MyTopic`For more information about notifications, see Using Notifications With Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [SetIdentityNotificationTopic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/set-identity-notification-topic.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-domain-dkim`.

- **AWS CLI**
- 
            
                    **To generate a verified domain's DKIM tokens for DKIM signing with Amazon SES**The following example uses the `verify-domain-dkim`command to generate DKIM tokens for a domain that has been verified with Amazon SES:`aws ses verify-domain-dkim --domain``example.com`Output: `{ "DkimTokens": [ "EXAMPLEq76owjnks3lnluwg65scbemvw", "EXAMPLEi3dnsj67hstzaj673klariwx2", "EXAMPLEwfbtcukvimehexktmdtaz6naj" ] }`To set up DKIM, you must use the returned DKIM tokens to update your domain's DNS settings with CNAME records that point to DKIM public keys hosted by Amazon SES. For more information, see Easy DKIM in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [VerifyDomainDkim](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/verify-domain-dkim.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-domain-identity`.

- **AWS CLI**
- 
            
                    **To verify a domain with Amazon SES**The following example uses the `verify-domain-identity`command to verify a domain:`aws ses verify-domain-identity --domain``example.com`Output: `{ "VerificationToken": "eoEmxw+YaYhb3h3iVJHuXMJXqeu1q1/wwmvjuEXAMPLE" }`To complete domain verification, you must add a TXT record with the returned verification token to your domain's DNS settings. For more information, see Verifying Domains in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [VerifyDomainIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/verify-domain-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-email-identity`.

- **AWS CLI**
- 
            
                    **To verify an email address with Amazon SES**The following example uses the `verify-email-identity`command to verify an email address:`aws ses verify-email-identity --email-address``user@example.com`Before you can send an email using Amazon SES, you must verify the address or domain that you are sending the email from to prove that you own it. If you do not have production access yet, you also need to verify any email addresses that you send emails to except for email addresses provided by the Amazon SES mailbox simulator. After verify-email-identity is called, the email address will receive a verification email. The user must click on the link in the email to complete the verification process. For more information, see Verifying Email Addresses in Amazon SES in the *Amazon Simple Email Service Developer Guide*.- 
                    For API details, see [VerifyEmailIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/verify-email-identity.html)in*AWS CLI Command Reference*.
 
-