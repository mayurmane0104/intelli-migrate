# Route 53 domain registration examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_route-53-domains_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_route-53-domains_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Route 53 domain registration.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `check-domain-availability`.

- **AWS CLI**
- 
            
                    **To determine whether you can register a domain name with Route 53**The following `check-domain-availability`command returns information about whether the domain name`example.com`is available to be registered using Route 53.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains check-domain-availability \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "Availability": "UNAVAILABLE" }`Route 53 supports a large number of top-level domains (TLDs), such as `.com`and`.jp`, but we don't support all available TLDs. If you check the availability of a domain and Route 53 doesn't support the TLD,`check-domain-availability`returns the following message.`An error occurred (UnsupportedTLD) when calling the CheckDomainAvailability operation: <top-level domain> tld is not supported.`For a list of the TLDs that you can use when registering a domain with Route 53, see [Domains That You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html)in the*Amazon Route 53 Developer Guide*. For more information about registering domains with Amazon Route 53, see[Registering a New Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [CheckDomainAvailability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/check-domain-availability.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `check-domain-transferability`.

- **AWS CLI**
- 
            
                    **To determine whether a domain can be transferred to Route 53**The following `check-domain-transferability`command returns information about whether you can transfer the domain name`example.com`to Route 53.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains check-domain-transferability \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "Transferability": { "Transferable": "UNTRANSFERABLE" } }`For more information, see [Transferring Registration for a Domain to Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [CheckDomainTransferability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/check-domain-transferability.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-tags-for-domain`.

- **AWS CLI**
- 
            
                    **To delete tags for a domain**The following `delete-tags-for-domain`command deletes three tags from the specified domain. Note that you specify only the tag key, not the tag value.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains delete-tags-for-domain \ --region``us-east-1`\ --domain-name`example.com`\ --tags-to-delete`accounting-key``hr-key``engineering-key`This command produces no output. To confirm that the tags were deleted, you can run [list-tags-for-domain](https://docs.aws.amazon.com/cli/latest/reference/route53domains/list-tags-for-domain.html). For more information, see[Tagging Amazon Route 53 Resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tagging-resources.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [DeleteTagsForDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/delete-tags-for-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-domain-auto-renew`.

- **AWS CLI**
- 
            
                    **To disable automatic renewal of a domain**The following `disable-domain-auto-renew`command configures Route 53 to*not*automatically renew the domain`example.com`before registration for the domain expires.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains disable-domain-auto-renew \ --region``us-east-1`\ --domain-name`example.com`This command produces no output. To confirm that the setting was changed, you can run [get-domain-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-domain-detail.html). If automatic renewal is disabled, the value of`AutoRenew`is`False`. For more information about automatic renewal, see Renewing Registration for a Domain <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [DisableDomainAutoRenew](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/disable-domain-auto-renew.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disable-domain-transfer-lock`.

- **AWS CLI**
- 
            
                    **To disable the transfer lock on a domain**The following `disable-domain-transfer-lock`command removes the transfer lock on the domain`example.com`so that the domain can be transferred to another registrar. This command changes the`clientTransferProhibited`status.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains disable-domain-transfer-lock \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "OperationId": "3f28e0ac-126a-4113-9048-cc930example" }`To confirm that the transfer lock has been changed, you can run [get-domain-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-domain-detail.html). When the transfer lock is disabled, the value of`StatusList`does*not*include`clientTransferProhibited`.For more information about the transfer process, see [Transferring a Domain from Amazon Route 53 to Another Registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-from-route-53.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [DisableDomainTransferLock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/disable-domain-transfer-lock.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-domain-auto-renew`.

- **AWS CLI**
- 
            
                    **To enable automatic renewal of a domain**The following `enable-domain-auto-renew`command configures Route 53 to automatically renew the domain`example.com`before registration for the domain expires.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains enable-domain-auto-renew \ --region``us-east-1`\ --domain-name`example.com`This command produces no output. To confirm that the setting was changed, you can run [get-domain-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-domain-detail.html). If automatic renewal is enabled, the value of`AutoRenew`is`True`.For more information about automatic renewal, see Renewing Registration for a Domain <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html in the *Amazon Route 53 Developer Guide*.- 
                    For API details, see [EnableDomainAutoRenew](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/enable-domain-auto-renew.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `enable-domain-transfer-lock`.

- **AWS CLI**
- 
            
                    **To enable the transfer lock on a domain**The following `enable-domain-transfer-lock`command locks the specified domain so that it can't be transferred to another registrar. This command changes the`clientTransferProhibited`status.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains enable-domain-transfer-lock \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "OperationId": "3f28e0ac-126a-4113-9048-cc930example" }`To confirm that the transfer lock has been changed, you can run [get-domain-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-domain-detail.html). When the transfer lock is enabled, the value of`StatusList`includes`clientTransferProhibited`.For more information about the transfer process, see [Transferring a Domain from Amazon Route 53 to Another Registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-from-route-53.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [EnableDomainTransferLock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/enable-domain-transfer-lock.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-contact-reachability-status`.

- **AWS CLI**
- 
            
                    **To determine whether the registrant contact has responded to a confirmation email**The following `get-contact-reachability-status`command returns information about whether the registrant contact for the specified domain has responded to a confirmation email.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains get-contact-reachability-status \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "domainName": "example.com", "status": "DONE" }`For more information, see [Resending Authorization and Confirmation Emails](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-click-email-link.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [GetContactReachabilityStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-contact-reachability-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-detail`.

- **AWS CLI**
- 
            
                    **To get detailed information about a specified domain**The following `get-domain-detail`command displays detailed information about the specified domain.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains get-domain-detail \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "DomainName": "example.com", "Nameservers": [ { "Name": "ns-2048.awsdns-64.com", "GlueIps": [] }, { "Name": "ns-2049.awsdns-65.net", "GlueIps": [] }, { "Name": "ns-2050.awsdns-66.org", "GlueIps": [] }, { "Name": "ns-2051.awsdns-67.co.uk", "GlueIps": [] } ], "AutoRenew": true, "AdminContact": { "FirstName": "Saanvi", "LastName": "Sarkar", "ContactType": "COMPANY", "OrganizationName": "Example", "AddressLine1": "123 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "ssarkar@example.com", "ExtraParams": [] }, "RegistrantContact": { "FirstName": "Alejandro", "LastName": "Rosalez", "ContactType": "COMPANY", "OrganizationName": "Example", "AddressLine1": "123 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "arosalez@example.com", "ExtraParams": [] }, "TechContact": { "FirstName": "Wang", "LastName": "Xiulan", "ContactType": "COMPANY", "OrganizationName": "Example", "AddressLine1": "123 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "wxiulan@example.com", "ExtraParams": [] }, "AdminPrivacy": true, "RegistrantPrivacy": true, "TechPrivacy": true, "RegistrarName": "Amazon Registrar, Inc.", "WhoIsServer": "whois.registrar.amazon", "RegistrarUrl": "http://registrar.amazon.com", "AbuseContactEmail": "abuse@registrar.amazon.com", "AbuseContactPhone": "+1.2062661000", "CreationDate": 1444934889.601, "ExpirationDate": 1602787689.0, "StatusList": [ "clientTransferProhibited" ] }`- 
                    For API details, see [GetDomainDetail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-domain-detail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-suggestions`.

- **AWS CLI**
- 
            
                    **To get a list of suggested domain names**The following `get-domain-suggestions`command displays a list of suggested domain names based on the domain name`example.com`. The response includes only domain names that are available. This command runs only in the`us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains get-domain-suggestions \ --region``us-east-1`\ --domain-name`example.com`\ --suggestion-count`10`\ --only-availableOutput: `{ "SuggestionsList": [ { "DomainName": "egzaampal.com", "Availability": "AVAILABLE" }, { "DomainName": "examplelaw.com", "Availability": "AVAILABLE" }, { "DomainName": "examplehouse.net", "Availability": "AVAILABLE" }, { "DomainName": "homeexample.net", "Availability": "AVAILABLE" }, { "DomainName": "examplelist.com", "Availability": "AVAILABLE" }, { "DomainName": "examplenews.net", "Availability": "AVAILABLE" }, { "DomainName": "officeexample.com", "Availability": "AVAILABLE" }, { "DomainName": "exampleworld.com", "Availability": "AVAILABLE" }, { "DomainName": "exampleart.com", "Availability": "AVAILABLE" } ] }`- 
                    For API details, see [GetDomainSuggestions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-domain-suggestions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-operation-detail`.

- **AWS CLI**
- 
            
                    **To get the current status of an operation**Some domain registration operations operate asynchronously and return a response before they finish. These operations return an operation ID that you can use to get the current status. The following `get-operation-detail`command returns the status of the specified operation.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains get-operation-detail \ --region``us-east-1`\ --operation-id`edbd8d63-7fe7-4343-9bc5-54033example`Output: `{ "OperationId": "edbd8d63-7fe7-4343-9bc5-54033example", "Status": "SUCCESSFUL", "DomainName": "example.com", "Type": "DOMAIN_LOCK", "SubmittedDate": 1573749367.864 }`- 
                    For API details, see [GetOperationDetail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/get-operation-detail.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-domains`.

- **AWS CLI**
- 
            
                    **To list the domains that are registered with the current AWS account**The following `list-domains`command lists summary information about the domains that are registered with the current AWS account.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains list-domains --region``us-east-1`Output: `{ "Domains": [ { "DomainName": "example.com", "AutoRenew": true, "TransferLock": true, "Expiry": 1602712345.0 }, { "DomainName": "example.net", "AutoRenew": true, "TransferLock": true, "Expiry": 1602723456.0 }, { "DomainName": "example.org", "AutoRenew": true, "TransferLock": true, "Expiry": 1602734567.0 } ] }`- 
                    For API details, see [ListDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-operations`.

- **AWS CLI**
- 
            
                    **To list the status of operations that return an operation ID**Some domain registration operations run asynchronously and return a response before they finish. These operations return an operation ID that you can use to get the current status. The following `list-operations`command lists summary information, including the status, about the current domain-registration operations.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains list-operations --region``us-east-1`Output: `{ "Operations": [ { "OperationId": "aab9822f-1da0-4bf3-8a15-fd4e0example", "Status": "SUCCESSFUL", "Type": "DOMAIN_LOCK", "SubmittedDate": 1455321739.986 }, { "OperationId": "c24379ed-76be-42f8-bdad-9379bexample", "Status": "SUCCESSFUL", "Type": "UPDATE_NAMESERVER", "SubmittedDate": 1468960475.109 }, { "OperationId": "f47e1297-ef9e-4c2b-ae1e-a5fcbexample", "Status": "SUCCESSFUL", "Type": "RENEW_DOMAIN", "SubmittedDate": 1473561835.943 }, { "OperationId": "75584f23-b15f-459e-aed7-dc6f5example", "Status": "SUCCESSFUL", "Type": "UPDATE_DOMAIN_CONTACT", "SubmittedDate": 1547501003.41 } ] }`The output includes all the operations that return an operation ID and that you have performed on all the domains that you have ever registered using the current AWS account. If you want to get only the operations that you submitted after a specified date, you can include the `submitted-since`parameter and specify a date in Unix format and Coordinated Universal Time (UTC). The following command gets the status of all operations that were submitted after 12:00 am UTC on January 1, 2020.`aws route53domains list-operations \ --submitted-since``1577836800`- 
                    For API details, see [ListOperations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-operations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-domain`.

- **AWS CLI**
- 
            
                    **To list tags for a domain**The following `list-tags-for-domain`command lists the tags that are currently associated with the specified domain.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains list-tags-for-domain \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "TagList": [ { "Key": "key1", "Value": "value1" }, { "Key": "key2", "Value": "value2" } ] }`For more information, see [Tagging Amazon Route 53 Resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tagging-resources.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ListTagsForDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-tags-for-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `register-domain`.

- **AWS CLI**
- 
            
                    **To register a domain**The following `register-domain`command registers a domain, retrieving all parameter values from a JSON-formatted file.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains register-domain \ --region``us-east-1`\ --cli-input-json`file://register-domain.json`Contents of `register-domain.json`:`{ "DomainName": "example.com", "DurationInYears": 1, "AutoRenew": true, "AdminContact": { "FirstName": "Martha", "LastName": "Rivera", "ContactType": "PERSON", "OrganizationName": "Example", "AddressLine1": "1 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "mrivera@example.com" }, "RegistrantContact": { "FirstName": "Li", "LastName": "Juan", "ContactType": "PERSON", "OrganizationName": "Example", "AddressLine1": "1 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "ljuan@example.com" }, "TechContact": { "FirstName": "Mateo", "LastName": "Jackson", "ContactType": "PERSON", "OrganizationName": "Example", "AddressLine1": "1 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "mjackson@example.com" }, "PrivacyProtectAdminContact": true, "PrivacyProtectRegistrantContact": true, "PrivacyProtectTechContact": true }`Output: `{ "OperationId": "b114c44a-9330-47d1-a6e8-a0b11example" }`To confirm that the operation succeeded, you can run `get-operation-detail`. For more information, see[get-operation-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-operation-detail.html).For more information, see [Registering a New Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html)in the*Amazon Route 53 Developer Guide*.For information about which top-level domains (TLDs) require values for `ExtraParams`and what the valid values are, see[ExtraParam](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ExtraParam.html)in the*Amazon Route 53 API Reference*.- 
                    For API details, see [RegisterDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/register-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `renew-domain`.

- **AWS CLI**
- 
            
                    **To renew a domain**The following `renew-domain`command renews the specified domain for five years. To get the value for`current-expiry-year`, use the`get-domain-detail`command, and convert the value of`ExpirationDate`from Unix format.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains renew-domain \ --region``us-east-1`\ --domain-name`example.com`\ --duration-in-years`5`\ --current-expiry-year`2020`Output: `{ "OperationId": "3f28e0ac-126a-4113-9048-cc930example" }`To confirm that the operation succeeded, you can run `get-operation-detail`. For more information, see[get-operation-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-operation-detail.html).The registry for each top-level domain (TLD), such as .com or .org, controls the maximum number of years that you can renew a domain for. To get the maximum renewal period for your domain, see the "Registration and Renewal Period" section for your TLD in [Domains That You Can Register with Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar-tld-list.html)in the*Amazon Route 53 Developer Guide*.For more information, see [Renewing Registration for a Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-renew.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [RenewDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/renew-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resend-contact-reachability-email`.

- **AWS CLI**
- 
            
                    **To resend the confirmation email to the current email address for the registrant contact**The following `resend-contact-reachability-email`command resends the confirmation email to the current email address for the registrant contact for the example.com domain.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains resend-contact-reachability-email \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "domainName": "example.com", "emailAddress": "moliveira@example.com", "isAlreadyVerified": true }`If the value of `isAlreadyVerified`is`true`, as in this example, the registrant contact has already confirmed that the specified email address is reachable.For more information, see [Resending Authorization and Confirmation Emails](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-click-email-link.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [ResendContactReachabilityEmail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/resend-contact-reachability-email.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `retrieve-domain-auth-code`.

- **AWS CLI**
- 
            
                    **To get the authorization code for a domain so you can transfer the domain to another registrar**The following `retrieve-domain-auth-code`command gets the current authorization code for the example.com domain. You give this value to another domain registrar when you want to transfer the domain to that registrar.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains retrieve-domain-auth-code \ --region``us-east-1`\ --domain-name`example.com`Output: `{ "AuthCode": ")o!v3dJeXampLe" }`For more information, see [Transferring a Domain from Amazon Route 53 to Another Registrar](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-from-route-53.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [RetrieveDomainAuthCode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/retrieve-domain-auth-code.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `transfer-domain`.

- **AWS CLI**
- 
            
                    **To transfer a domain to Amazon Route 53**The following `transfer-domain`command transfers a domain to Route 53, with the parameters provided by the JSON-formatted file`C:\temp\transfer-domain.json`.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains transfer-domain \ --region``us-east-1`\ --cli-input-json file://C:\temp\transfer-domain.jsonContents of `transfer-domain.json`:`{ "DomainName": "example.com", "DurationInYears": 1, "Nameservers": [ { "Name": "ns-2048.awsdns-64.com" }, { "Name": "ns-2049.awsdns-65.net" }, { "Name": "ns-2050.awsdns-66.org" }, { "Name": "ns-2051.awsdns-67.co.uk" } ], "AuthCode": ")o!v3dJeXampLe", "AutoRenew": true, "AdminContact": { "FirstName": "Martha", "LastName": "Rivera", "ContactType": "PERSON", "OrganizationName": "Example", "AddressLine1": "1 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "mrivera@example.com" }, "RegistrantContact": { "FirstName": "Li", "LastName": "Juan", "ContactType": "PERSON", "OrganizationName": "Example", "AddressLine1": "1 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "ljuan@example.com" }, "TechContact": { "FirstName": "Mateo", "LastName": "Jackson", "ContactType": "PERSON", "OrganizationName": "Example", "AddressLine1": "1 Main Street", "City": "Anytown", "State": "WA", "CountryCode": "US", "ZipCode": "98101", "PhoneNumber": "+1.8005551212", "Email": "mjackson@example.com" }, "PrivacyProtectAdminContact": true, "PrivacyProtectRegistrantContact": true, "PrivacyProtectTechContact": true }`Output: `{ "OperationId": "b114c44a-9330-47d1-a6e8-a0b11example" }`To confirm that the operation succeeded, you can run `get-operation-detail`. For more information, see[get-operation-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-operation-detail.html).For more information, see [Transferring Registration for a Domain to Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-transfer-to-route-53.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [TransferDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/transfer-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-domain-contact-privacy`.

- **AWS CLI**
- 
            
                    **To update the privacy settings for the contacts for a domain**The following `update-domain-contact-privacy`command turns off privacy protection for the administrative contact for the example.com domain. This command runs only in the`us-east-1`Region.If your default region is set to `us-east-1`, you can omit the`region`parameter.`aws route53domains update-domain-contact-privacy \ --region``us-east-1`\ --domain-name`example.com`\ --no-admin-privacyOutput: `{ "OperationId": "b3a219e9-d801-4244-b533-b7256example" }`To confirm that the operation succeeded, you can run `get-operation-detail`. For more information, see[get-operation-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-operation-detail.html).For more information, see [Enabling or Disabling Privacy Protection for Contact Information for a Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-privacy-protection.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateDomainContactPrivacy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-domain-contact-privacy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-domain-contact`.

- **AWS CLI**
- 
            
                    **To update the contact information for a domain**The following `update-domain-contact`command updates the contact information for a domain, getting the parameters from the JSON-formatted file`C:\temp\update-domain-contact.json`.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains update-domain-contact \ --region``us-east-1`\ --cli-input-json file://C:\temp\update-domain-contact.jsonContents of `update-domain-contact.json`:`{ "AdminContact": { "AddressLine1": "101 Main Street", "AddressLine2": "Suite 1a", "City": "Seattle", "ContactType": "COMPANY", "CountryCode": "US", "Email": "w.xiulan@example.com", "FirstName": "Wang", "LastName": "Xiulan", "OrganizationName": "Example", "PhoneNumber": "+1.8005551212", "State": "WA", "ZipCode": "98101" }, "DomainName": "example.com", "RegistrantContact": { "AddressLine1": "101 Main Street", "AddressLine2": "Suite 1a", "City": "Seattle", "ContactType": "COMPANY", "CountryCode": "US", "Email": "w.xiulan@example.com", "FirstName": "Wang", "LastName": "Xiulan", "OrganizationName": "Example", "PhoneNumber": "+1.8005551212", "State": "WA", "ZipCode": "98101" }, "TechContact": { "AddressLine1": "101 Main Street", "AddressLine2": "Suite 1a", "City": "Seattle", "ContactType": "COMPANY", "CountryCode": "US", "Email": "w.xiulan@example.com", "FirstName": "Wang", "LastName": "Xiulan", "OrganizationName": "Example", "PhoneNumber": "+1.8005551212", "State": "WA", "ZipCode": "98101" } }`Output: `{ "OperationId": "b3a219e9-d801-4244-b533-b7256example" }`To confirm that the operation succeeded, you can run [get-domain-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-domain-detail.html). For more information, see[Updating Contact Information for a Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-update-contacts.html#domain-update-contacts-basic)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateDomainContact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-domain-contact.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-domain-nameservers`.

- **AWS CLI**
- 
            
                    **To update the name servers for a domain**The following `update-domain-nameservers`command updates the name servers for a domain.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains update-domain-nameservers \ --region``us-east-1`\ --domain-name`example.com`\ --nameservers`Name=ns-1.awsdns-01.org``Name=ns-2.awsdns-02.co.uk``Name=ns-3.awsdns-03.net``Name=ns-4.awsdns-04.com`Output: `{ "OperationId": "f1691ec4-0e7a-489e-82e0-b19d3example" }`To confirm that the operation succeeded, you can run [get-domain-detail](https://docs.aws.amazon.com/cli/latest/reference/route53domains/get-domain-detail.html).For more information, see [Adding or Changing Name Servers and Glue Records for a Domain](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-name-servers-glue-records.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateDomainNameservers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-domain-nameservers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-tags-for-domain`.

- **AWS CLI**
- 
            
                    **To add or update tags for a domain**The following `update-tags-for-domain`command adds or updates two keys and the corresponding values for the example.com domain. To update the value for a key, just include the key and the new value. You can add or update tags in only one domain at a time.This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains update-tags-for-domain \ --region``us-east-1`\ --domain-name`example.com`\ --tags-to-update`"Key=key1,Value=value1"``"Key=key2,Value=value2"`This command produces no output. To confirm that the tags were added or updated, you can run [list-tags-for-domain](https://docs.aws.amazon.com/cli/latest/reference/route53domains/list-tags-for-domain.html).For more information, see [Tagging Amazon Route 53 Resources](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/tagging-resources.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [UpdateTagsForDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/update-tags-for-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `view-billing`.

- **AWS CLI**
- 
            
                    **To get billing information for domain registration charges for the current AWS account**The following `view-billing`command returns all the domain-related billing records for the current account for the period from January 1, 2018 (1514764800 in Unix time) and midnight on December 31, 2019 (1577836800 in Unix time).This command runs only in the `us-east-1`Region. If your default region is set to`us-east-1`, you can omit the`region`parameter.`aws route53domains view-billing \ --region``us-east-1`\ --start-time`1514764800`\ --end-time`1577836800`Output: `{ "BillingRecords": [ { "DomainName": "example.com", "Operation": "RENEW_DOMAIN", "InvoiceId": "149962827", "BillDate": 1536618063.181, "Price": 12.0 }, { "DomainName": "example.com", "Operation": "RENEW_DOMAIN", "InvoiceId": "290913289", "BillDate": 1568162630.884, "Price": 12.0 } ] }`For more information, see [ViewBilling](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ViewBilling.html)in the*Amazon Route 53 API Reference*.- 
                    For API details, see [ViewBilling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/view-billing.html)in*AWS CLI Command Reference*.
 
-