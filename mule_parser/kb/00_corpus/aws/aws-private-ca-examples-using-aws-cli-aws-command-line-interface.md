# AWS Private CA examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_acm-pca_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_acm-pca_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Private CA.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-certificate-authority-audit-report`.

- **AWS CLI**
- 
            
                    **To create a certificate authority audit report**The following `create-certificate-authority-audit-report`command creates an audit report for the private CA identified by the ARN.`aws acm-pca create-certificate-authority-audit-report --certificate-authority-arn``arn:aws:acm-pca:us-east-1:accountid:certificate-authority/12345678-1234-1234-1234-123456789012`--s3-bucket-name`your-bucket-name`--audit-report-response-format`JSON`- 
                    For API details, see [CreateCertificateAuthorityAuditReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority-audit-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-certificate-authority`.

- **AWS CLI**
- 
            
                    **To create a private certificate authority**The following `create-certificate-authority`command creates a private certificate authority in your AWS account.`aws acm-pca create-certificate-authority --certificate-authority-configuration file://C:\ca_config.txt --revocation-configuration file://C:\revoke_config.txt --certificate-authority-type``"SUBORDINATE"`--idempotency-token`98256344`- 
                    For API details, see [CreateCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/create-certificate-authority.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-certificate-authority`.

- **AWS CLI**
- 
            
                    **To delete a private certificate authority**The following `delete-certificate-authority`command deletes the certificate authority identified by the ARN.`aws acm-pca delete-certificate-authority --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`- 
                    For API details, see [DeleteCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/delete-certificate-authority.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-certificate-authority-audit-report`.

- **AWS CLI**
- 
            
                    **To describe an audit report for a certificate authority**The following `describe-certificate-authority-audit-report`command lists information about the specified audit report for the CA identified by the ARN.`aws acm-pca describe-certificate-authority-audit-report --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/99999999-8888-7777-6666-555555555555`--audit-report-id`11111111-2222-3333-4444-555555555555`- 
                    For API details, see [DescribeCertificateAuthorityAuditReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority-audit-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-certificate-authority`.

- **AWS CLI**
- 
            
                    **To describe a private certificate authority**The following `describe-certificate-authority`command lists information about the private CA identified by the ARN.`aws acm-pca describe-certificate-authority --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`- 
                    For API details, see [DescribeCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/describe-certificate-authority.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-certificate-authority-certificate`.

- **AWS CLI**
- 
            
                    **To retrieve a certificate authority (CA) certificate**The following `get-certificate-authority-certificate`command retrieves the certificate and certificate chain for the private CA specified by the ARN.`aws acm-pca get-certificate-authority-certificate --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`--output`text`- 
                    For API details, see [GetCertificateAuthorityCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-certificate-authority-csr`.

- **AWS CLI**
- 
            
                    **To retrieve the certificate signing request for a certificate authority**The following `get-certificate-authority-csr`command retrieves the CSR for the private CA specified by the ARN.`aws acm-pca get-certificate-authority-csr --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`--output`text`- 
                    For API details, see [GetCertificateAuthorityCsr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate-authority-csr.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-certificate`.

- **AWS CLI**
- 
            
                    **To retrieve an issued certificate**The following `get-certificate`example retrieves a certificate from the specified private CA.`aws acm-pca get-certificate \ --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`\ --certificate-arn`arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012/certificate/6707447683a9b7f4055627ffd55cebcc`\ --output`text`Output: `-----BEGIN CERTIFICATE----- MIIEDzCCAvegAwIBAgIRAJuJ8f6ZVYL7gG/rS3qvrZMwDQYJKoZIhvcNAQELBQAw cTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xEDAOBgNVBAcMB1Nl ....certificate body truncated for brevity.... tKCSglgZZrd4FdLw1EkGm+UVXnodwMtJEQyy3oTfZjURPIyyaqskTu/KSS7YDjK0 KQNy73D6LtmdOEbAyq10XiDxqY41lvKHJ1eZrPaBmYNABxU= -----END CERTIFICATE---- -----BEGIN CERTIFICATE----- MIIDrzCCApegAwIBAgIRAOskdzLvcj1eShkoyEE693AwDQYJKoZIhvcNAQELBQAw cTELMAkGA1UEBhMCVVMxEzARBgNVBAgMCldhc2hpbmd0b24xEDAOBgNVBAcMB1Nl ...certificate body truncated for brevity.... kdRGB6P2hpxstDOUIwAoCbhoaWwfA4ybJznf+jOQhAziNlRdKQRR8nODWpKt7H9w dJ5nxsTk/fniJz86Ddtp6n8s82wYdkN3cVffeK72A9aTCOU= -----END CERTIFICATE-----`The first part of the output is the certificate itself. The second part is the certificate chain that chains to the root CA certificate. Note that when you use the `--output text`option, a`TAB`character is inserted between the two certificate pieces (that is the cause of the indented text). If you intend to take this output and parse the certificates with other tools, you might need to remove the`TAB`character so it is processed correctly.- 
                    For API details, see [GetCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/get-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-certificate-authority-certificate`.

- **AWS CLI**
- 
            
                    **To import your certificate authority certificate into ACM PCA**The following `import-certificate-authority-certificate`command imports the signed private CA certificate for the CA specified by the ARN into ACM PCA.`aws acm-pca import-certificate-authority-certificate --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`--certificate file://C:\ca_cert.pem --certificate-chain file://C:\ca_cert_chain.pem- 
                    For API details, see [ImportCertificateAuthorityCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/import-certificate-authority-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `issue-certificate`.

- **AWS CLI**
- 
            
                    **To issue a private certificate**The following `issue-certificate`command uses the private CA specified by the ARN to issue a private certificate.`aws acm-pca issue-certificate --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`--csr file://C:\cert_1.csr --signing-algorithm`"SHA256WITHRSA"`--validity Value=365,Type="DAYS" --idempotency-token`1234`- 
                    For API details, see [IssueCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/issue-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-certificate-authorities`.

- **AWS CLI**
- 
            
                    **To list your private certificate authorities**The following `list-certificate-authorities`command lists information about all of the private CAs in your account.`aws acm-pca list-certificate-authorities --max-results``10`- 
                    For API details, see [ListCertificateAuthorities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-certificate-authorities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags`.

- **AWS CLI**
- 
            
                    **To list the tags for your certificate authority**The following `list-tags`command lists the tags associated with the private CA specified by the ARN.`aws acm-pca list-tags --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/123455678-1234-1234-1234-123456789012`--max-results`10`- 
                    For API details, see [ListTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/list-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `revoke-certificate`.

- **AWS CLI**
- 
            
                    **To revoke a private certificate**The following `revoke-certificate`command revokes a private certificate from the CA identified by the ARN.`aws acm-pca revoke-certificate --certificate-authority-arn``arn:aws:acm-pca:us-west-2:1234567890:certificate-authority/12345678-1234-1234-1234-123456789012`--certificate-serial`67:07:44:76:83:a9:b7:f4:05:56:27:ff:d5:5c:eb:cc`--revocation-reason`"KEY_COMPROMISE"`- 
                    For API details, see [RevokeCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/revoke-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-certificate-authority`.

- **AWS CLI**
- 
            
                    **To attach tags to a private certificate authority**The following `tag-certificate-authority`command attaches one or more tags to your private CA.`aws acm-pca tag-certificate-authority --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`--tags`Key=Admin,Value=Alice`- 
                    For API details, see [TagCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/tag-certificate-authority.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-certificate-authority`.

- **AWS CLI**
- 
            
                    **To remove one or more tags from your private certificate authority**The following `untag-certificate-authority`command removes tags from the private CA identified by the ARN.`aws acm-pca untag-certificate-authority --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-123456789012`--tags`Key=Purpose,Value=Website`- 
                    For API details, see [UntagCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/untag-certificate-authority.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-certificate-authority`.

- **AWS CLI**
- 
            
                    **To update the configuration of your private certificate authority**The following `update-certificate-authority`command updates the status and configuration of the private CA identified by the ARN.`aws acm-pca update-certificate-authority --certificate-authority-arn``arn:aws:acm-pca:us-west-2:123456789012:certificate-authority/12345678-1234-1234-1234-1232456789012`--revocation-configuration file://C:\revoke_config.txt --status`"DISABLED"`- 
                    For API details, see [UpdateCertificateAuthority](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/acm-pca/update-certificate-authority.html)in*AWS CLI Command Reference*.
 
-