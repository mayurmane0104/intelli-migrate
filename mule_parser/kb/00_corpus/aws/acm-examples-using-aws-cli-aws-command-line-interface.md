# ACM examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_acm_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_acm_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with ACM.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `add-tags-to-certificate`.

- **AWS CLI**
- 
            
                    **To add tags to an existing ACM Certificate**The following `add-tags-to-certificate`command adds two tags to the specified certificate. Use a space to separate multiple tags:`aws acm add-tags-to-certificate --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`--tags`Key=Admin,Value=Alice``Key=Purpose,Value=Website`- 
                    For API details, see [AddTagsToCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/add-tags-to-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-certificate`.

- **AWS CLI**
- 
            
                    **To delete an ACM certificate from your account**The following `delete-certificate`command deletes the certificate with the specified ARN:`aws acm delete-certificate --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`- 
                    For API details, see [DeleteCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/delete-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-certificate`.

- **AWS CLI**
- 
            
                    **To retrieve the fields contained in an ACM certificate**The following `describe-certificate`command retrieves all of the fields for the certificate with the specified ARN:`aws acm describe-certificate --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`Output similar to the following is displayed: `{ "Certificate": { "CertificateArn": "arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012", "CreatedAt": 1446835267.0, "DomainName": "www.example.com", "DomainValidationOptions": [ { "DomainName": "www.example.com", "ValidationDomain": "www.example.com", "ValidationEmails": [ "hostmaster@example.com", "admin@example.com", "owner@example.com.whoisprivacyservice.org", "tech@example.com.whoisprivacyservice.org", "admin@example.com.whoisprivacyservice.org", "postmaster@example.com", "webmaster@example.com", "administrator@example.com" ] }, { "DomainName": "www.example.net", "ValidationDomain": "www.example.net", "ValidationEmails": [ "postmaster@example.net", "admin@example.net", "owner@example.net.whoisprivacyservice.org", "tech@example.net.whoisprivacyservice.org", "admin@example.net.whoisprivacyservice.org", "hostmaster@example.net", "administrator@example.net", "webmaster@example.net" ] } ], "InUseBy": [], "IssuedAt": 1446835815.0, "Issuer": "Amazon", "KeyAlgorithm": "RSA-2048", "NotAfter": 1478433600.0, "NotBefore": 1446768000.0, "Serial": "0f:ac:b0:a3:8d:ea:65:52:2d:7d:01:3a:39:36:db:d6", "SignatureAlgorithm": "SHA256WITHRSA", "Status": "ISSUED", "Subject": "CN=www.example.com", "SubjectAlternativeNames": [ "www.example.com", "www.example.net" ] } }`- 
                    For API details, see [DescribeCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/describe-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `export-certificate`.

- **AWS CLI**
- 
            
                    **To export a private certificate issued by a private CA.**The following `export-certificate`command exports a private certificate, certificate chain, and private key to your display:`aws acm export-certificate --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`--passphrase`file://path-to-passphrase-file`To export the certificate, chain, and private key to a local file, use the following command: `aws acm export-certificate --certificate-arn``arn:aws:acm:region:sccount:certificate/12345678-1234-1234-1234-123456789012`--passphrase`file://path-to-passphrase-file``>`c:\temp\export.txt- 
                    For API details, see [ExportCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/export-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-certificate`.

- **AWS CLI**
- 
            
                    **To retrieve an ACM certificate**The following `get-certificate`command retrieves the certificate for the specified ARN and the certificate chain:`aws acm get-certificate --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`Output similar to the following is displayed: `{ "Certificate": "-----BEGIN CERTIFICATE----- MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END CERTIFICATE-----", "CertificateChain": "-----BEGIN CERTIFICATE----- MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END CERTIFICATE-----", "-----BEGIN CERTIFICATE----- MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END CERTIFICATE-----", "-----BEGIN CERTIFICATE----- MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE= -----END CERTIFICATE-----" }`- 
                    For API details, see [GetCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/get-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-certificate`.

- **AWS CLI**
- 
            
                    **To import a certificate into ACM.**The following `import-certificate`command imports a certificate into ACM. Replace the file names with your own:`aws acm import-certificate --certificate``file://Certificate.pem`--certificate-chain`file://CertificateChain.pem`--private-key`file://PrivateKey.pem`- 
                    For API details, see [ImportCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/import-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-certificates`.

- **AWS CLI**
- 
            
                    **To list the ACM certificates for an AWS account**The following `list-certificates`command lists the ARNs of the certificates in your account:`aws acm list-certificates`The preceding command produces output similar to the following: `{ "CertificateSummaryList": [ { "CertificateArn": "arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012", "DomainName": "www.example.com" }, { "CertificateArn": "arn:aws:acm:region:account:certificate/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee", "DomainName": "www.example.net" } ] }`You can decide how many certificates you want to display each time you call `list-certificates`. For example, if you have four certificates and you want to display no more than two at a time, set the`max-items`argument to 2 as in the following example:`aws acm list-certificates --max-items``2`Two certificate ARNs and a `NextToken`value will be displayed:`"CertificateSummaryList": [ { "CertificateArn": "arn:aws:acm:region:account: \ certificate/12345678-1234-1234-1234-123456789012", "DomainName": "www.example.com" }, { "CertificateArn": "arn:aws:acm:region:account: \ certificate/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee", "DomainName": "www.example.net" } ], "NextToken": "9f4d9f69-275a-41fe-b58e-2b837bd9ba48"`To display the next two certificates in your account, set this `NextToken`value in your next call:`aws acm list-certificates --max-items``2`--next-token`9f4d9f69-275a-41fe-b58e-2b837bd9ba48`You can filter your output by using the `certificate-statuses`argument. The following command displays certificates that have a PENDING_VALIDATION status:`aws acm list-certificates --certificate-statuses``PENDING_VALIDATION`You can also filter your output by using the `includes`argument. The following command displays certificates filtered on the following properties. The certificates to be displayed:`- Specify that the RSA algorithm and a 2048 bit key are used to generate key pairs. - Contain a Key Usage extension that specifies that the certificates can be used to create digital signatures. - Contain an Extended Key Usage extension that specifies that the certificates can be used for code signing. aws acm list-certificates --max-items 10 --includes extendedKeyUsage=CODE_SIGNING,keyUsage=DIGITAL_SIGNATURE,keyTypes=RSA_2048`- 
                    For API details, see [ListCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-certificate`.

- **AWS CLI**
- 
            
                    **To list the tags applied to an ACM Certificate**The following `list-tags-for-certificate`command lists the tags applied to a certificate in your account:`aws acm list-tags-for-certificate --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`The preceding command produces output similar to the following: `{ "Tags": [ { "Value": "Website", "Key": "Purpose" }, { "Value": "Alice", "Key": "Admin" } ] }`- 
                    For API details, see [ListTagsForCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/list-tags-for-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `remove-tags-from-certificate`.

- **AWS CLI**
- 
            
                    **To remove a tag from an ACM Certificate**The following `remove-tags-from-certificate`command removes two tags from the specified certificate. Use a space to separate multiple tags:`aws acm remove-tags-from-certificate --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`--tags`Key=Admin,Value=Alice``Key=Purpose,Value=Website`- 
                    For API details, see [RemoveTagsFromCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/remove-tags-from-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `request-certificate`.

- **AWS CLI**
- 
            
                    **To request a new ACM certificate**The following `request-certificate`command requests a new certificate for the www.example.com domain using DNS validation:`aws acm request-certificate --domain-name``www.example.com`--validation-method`DNS`You can enter an idempotency token to distinguish between calls to `request-certificate`:`aws acm request-certificate --domain-name``www.example.com`--validation-method`DNS`--idempotency-token`91adc45q`You can enter one or more subject alternative names to request a certificate that will protect more than one apex domain: `aws acm request-certificate --domain-name``example.com`--validation-method`DNS`--idempotency-token`91adc45q`--subject-alternative-names`www.example.net`You can enter an alternative name that can also be used to reach your website: `aws acm request-certificate --domain-name``example.com`--validation-method`DNS`--idempotency-token`91adc45q`--subject-alternative-names`www.example.com`You can use an asterisk (*) as a wildcard to create a certificate for several subdomains in the same domain: `aws acm request-certificate --domain-name``example.com`--validation-method`DNS`--idempotency-token`91adc45q`--subject-alternative-names`*.example.com`You can also enter multiple alternative names: `aws acm request-certificate --domain-name``example.com`--validation-method`DNS`--subject-alternative-names`b.example.com``c.example.com``d.example.com`If you are using email for validation, you can enter domain validation options to specify the domain to which the validation email will be sent: `aws acm request-certificate --domain-name``example.com`--validation-method`EMAIL`--subject-alternative-names`www.example.com`--domain-validation-options`DomainName=example.com,ValidationDomain=example.com`The following command opts out of certificate transparency logging when you request a new certificate: `aws acm request-certificate --domain-name``www.example.com`--validation-method`DNS`--options`CertificateTransparencyLoggingPreference=DISABLED`--idempotency-token`184627`- 
                    For API details, see [RequestCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/request-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `resend-validation-email`.

- **AWS CLI**
- 
            
                    **To resend validation email for your ACM certificate request**The following `resend-validation-email`command tells the Amazon certificate authority to send validation email to the appropriate addresses:`aws acm resend-validation-email --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`--domain`www.example.com`--validation-domain`example.com`- 
                    For API details, see [ResendValidationEmail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/resend-validation-email.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-certificate-options`.

- **AWS CLI**
- 
            
                    **To update the certificate options**The following `update-certificate-options`command opts out of certificate transparency logging:`aws acm update-certificate-options --certificate-arn``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012`--options`CertificateTransparencyLoggingPreference=DISABLED`- 
                    For API details, see [UpdateCertificateOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm/update-certificate-options.html)in*AWS CLI Command Reference*.
 
-