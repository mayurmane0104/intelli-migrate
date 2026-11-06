# AWS Payment Cryptography examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_payment-cryptography_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_payment-cryptography_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Payment Cryptography.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-alias`.

- **AWS CLI**
- 
            
                    **To create an alias for a key**The following `create-alias`example creates an alias for a key.`aws payment-cryptography create-alias \ --alias-name``alias/sampleAlias1`\ --key-arn`arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`Output: `{ "Alias": { "AliasName": "alias/sampleAlias1", "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h" } }`For more information, see [About aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-about.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [CreateAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/create-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-key`.

- **AWS CLI**
- 
            
                    **To create a key**The following `create-key`example generates a 2KEY TDES key you can use to generate and verify CVV/CVV2 values.`aws payment-cryptography create-key \ --exportable \ --key-attributes``KeyAlgorithm=TDES_2KEY,``KeyUsage=TR31_C0_CARD_VERIFICATION_KEY,KeyClass=SYMMETRIC_KEY,``KeyModesOfUse={Generate=true,Verify=true}`Output: `{ "Key": { "CreateTimestamp": "1686800690", "Enabled": true, "Exportable": true, "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h", "KeyAttributes": { "KeyAlgorithm": "TDES_2KEY", "KeyClass": "SYMMETRIC_KEY", "KeyModesOfUse": { "Decrypt": false, "DeriveKey": false, "Encrypt": false, "Generate": true, "NoRestrictions": false, "Sign": false, "Unwrap": false, "Verify": true, "Wrap": false }, "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY" }, "KeyCheckValue": "F2E50F", "KeyCheckValueAlgorithm": "ANSI_X9_24", "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY", "KeyState": "CREATE_COMPLETE", "UsageStartTimestamp": "1686800690" } }`For more information, see [Generating keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/create-keys.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [CreateKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/create-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-alias`.

- **AWS CLI**
- 
            
                    **To delete an alias**The following `delete-alias`example deletes an alias. It does not affect the key.`aws payment-cryptography delete-alias \ --alias-name``alias/sampleAlias1`This command produces no output. For more information, see [About aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-about.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [DeleteAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/delete-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-key`.

- **AWS CLI**
- 
            
                    **To delete a key**The following `delete-key`example schedules a key for deletion after 7 days, which is the default waiting period.`aws payment-cryptography delete-key \ --key-identifier``arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h`Output: `{ "Key": { "CreateTimestamp": "1686801198", "DeletePendingTimestamp": "1687405998", "Enabled": true, "Exportable": true, "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h", "KeyAttributes": { "KeyAlgorithm": "TDES_2KEY", "KeyClass": "SYMMETRIC_KEY", "KeyModesOfUse": { "Decrypt": false, "DeriveKey": false, "Encrypt": false, "Generate": true, "NoRestrictions": false, "Sign": false, "Unwrap": false, "Verify": true, "Wrap": false }, "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY" }, "KeyCheckValue": "F2E50F", "KeyCheckValueAlgorithm": "ANSI_X9_24", "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY", "KeyState": "DELETE_PENDING", "UsageStartTimestamp": "1686801190" } }`For more information, see [Deleting keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-deleting.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [DeleteKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/delete-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `export-key`.

- **AWS CLI**
- 
            
                    **To export a key**The following `export-key`example exports a key.`aws payment-cryptography export-key \ --export-key-identifier``arn:aws:payment-cryptography:us-west-2:123456789012:key/lco3w6agsk7zgu2l`\ --key-material '`{"Tr34KeyBlock": { \ "CertificateAuthorityPublicKeyIdentifier": "arn:aws:payment-cryptography:us-west-2:123456789012:key/ftobshq7pvioc5fx", \ "ExportToken": "export-token-cu4lg26ofcziixny", \ "KeyBlockFormat": "X9_TR34_2012", \ "WrappingKeyCertificate": file://wrapping-key-certificate.pem }}`'Contents of `wrapping-key-certificate.pem`:`LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUV2VENDQXFXZ0F3SUJBZ0lSQU1ZZS8xMXFUK2svVzlRUDJQOElVdWd3RFFZSktvWklodmNOQVFFTkJRQXcKZ1lreEN6QUpCZ05WQkFZVEFsVlRNUmt3RndZRFZRUUtEQkJCVjFNZ1EzSjVjSFJ2WjNKaGNHaDVNU0V3SHdZRApWUVFMREJoQlYxTWdVR0Y1YldWdWRDQkRjbmx3ZEc5bmNtRndhSGt4RVRBUEJnTlZCQWdNQ0ZacGNtZHBibWxoCk1SVXdFd1lEVlFRRERBd3dOelUxTlRZNU5UTTNOVEF4RWpBUUJnTlZCQWNNQ1VGeWJHbHVaM1J2YmpBZUZ3MHkKTXpBMk1UTXhOelV6TVROYUZ3MHlNekEyTWpBeE9EVXpNVEphTUN3eEZUQVRCZ05WQkFNTUREQTNOVFUxTmprMQpNemMxTURFVE1CRUdBMVVFQlJNS09URTFNRGMzTnpRMk9EQ0NBU0l3RFFZSktvWklodmNOQVFFQkJRQURnZ0VQCkFEQ0NBUW9DZ2dFQkFNUjZsVTZ0SFJwcWtCQmI1Z2FFa0FrbVRxNEgwNUQ2UXR2MS9WemhSaThtNVBFMjVtMFIKVnRtZmsxcUEySi94TEROTEl3dHFDR3BIVldOM0JMdFhuSmh2Y1dNNkI0QlRRVXNicENMbG9PYW1jMGF0UXRmeQo0ZUhoWHJoT2lDMFVpR05zeTc5ZlltTkZ3Q3RrSDhvZzJXTEdYNldXNSszRzlTaFZKR3dhbWpNamtlOVo1a0FhCnJKZHk4Y2tsMTFBTS8wQjVZRFR2TU5KVTcyZnVUMlJ5KzVoRmdFTE14aS8vbGE1TnFCQWp5VTY0cmV3eGdVSjAKZ1pVM3lJU2F2UjFwMElNOFNvZzdXUHlkVlNNTitZeTdLMG1OL3lFa3FZTWQxZWxvS1I0OVV3V0hvdzFMcHVzcwpzMDh5a0diWGxsMnBvZ3NvSmZZaFFGWTc4UmRsTU9vY2dOc0NBd0VBQWFOOE1Ib3dDUVlEVlIwVEJBSXdBREFmCkJnTlZIU01FR0RBV2dCU2tDVlVEZzJGZDdPZWpVSUlVRnBvbUpxWG9FREFkQmdOVkhRNEVGZ1FVZU1sRzJ5dkgKamxsQzM2OUV2U3hIcXBBODVkMHdEZ1lEVlIwUEFRSC9CQVFEQWdXZ01CMEdBMVVkSlFRV01CUUdDQ3NHQVFVRgpCd01CQmdnckJnRUZCUWNEQWpBTkJna3Foa2lHOXcwQkFRMEZBQU9DQWdFQURNS2gxbnhYWWtncVkwYmMwVjA1ClNCUTBlcm5vMmsxbXdRQnhpUDBpcUpMdWNFUnF6b0RzOTBJWTN5SjhjMkMzU2kzU1JrVzBmQUhKR0VucTlzblgKbGdGWnRBZmtNbzR4Wllpb1JGZmY1TWdSOUdNaUZNQnVQS2tIeGxKc0R2NllSbnp1Zmkza1lDT1NzeWE4U2tTMQp2M2l2UEpLcTk3aDBBaThoNFQ3clBtN0NNSnYxZ0JTUEF4UVdtdndES2RrTjFsd0VudmtGdzlLZjhqeVpaNjhGCjlmUFV4Z1RvYm1MSmNialZxaFdsQ3U1VE9mSGNPR2RLRURwZE54RE12ODNZZ1ZaWUszclc4UHVxWWIyWFdMR2IKdmFISXh2RGVnOVJwNDByVVpETGVyalptb0gwUWpEZmxCV1RYK0JqU3ZLMm5yUGpzZzJIUC91S1VncVIwQWM5eAo0UjF5YjU2cHh3eU54TUU2NmFTVWNVQ3F1WTloY1Q3eWxWNjc3REVhRHpLTG1abnpMcWdWZU5PaUtzQTMvTi9hCnI2UW56VjNabEtJbCs5aWZwNTVPaTVLMXFyWFkyeVlPL1V2SXBXZjAxcFNFUERHN0hXSllnaGorbXpDRFVkM24KdldBeHBjUXlYRGlybS8wSkRZTWtuYzhjK2Z4QmxQR3ZiT2cwWldOeVUwSVpqRmx3aDVwUnIrMnRkT3lhRkZrNApWNytmMkpRWXdKZWgzWDdQL0N6WldKMlQvbnVzaVZXd0Y2K0hueDQ2ZHVGTzhXSWJZTnJUU1hTQnFEV04vdWpZCjBwYUhwS1poUTJOVnV1M0t3a2JaTDUzRjBRM09EVjcydGtiTHJyajZvOUNGd3JGUFluV0owSWtsemN0d1VtQ24KNjd5TzlSVjVzcC83YlNxTkhYNFRuNmc9Ci0tLS0tRU5EIENFUlRJRklDQVRFEXAMPLE=`Output: `{ "WrappedKey": { "KeyMaterial": "308205A106092A864886F70D010702A08205923082058E020101310D300B06096086480165030402013082031F06092A864886F70D010703A08203100482030C020100318201F4308201F002010030819F308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3037353535363935333735303112301006035504070C0941726C696E67746F6E021100C61EFF5D6A4FE93F5BD40FD8FF0852E8304506092A864886F70D0101073038300D06096086480165030402010500301806092A864886F70D010108300B0609608648016503040201300D06092A864886F70D0101090400048201008B09AFE9DFF1EA4E97F8651B6B3B51A3BFF68B0365F3956AD34A64B015185BB3FFB3DC7D5812B0D21D58436EAEC131F8110389E2A9F22DA146805A4D818BDCD6AA0387284188CEF5691565A849659C117AAD0042DF5D2C290386710B58A8C63A298C99280EB75861B793302F78299DE64853433227F23DBB383A605DA23620546DCA92B2D3CD8B486339D303844D807C2D6AF17CF1ABF191F63ACFF0E0F8A91AA5B22C1A0D9EE663854D1D76CEE37FE3A0113C8577B57F173ECD69FA752A8A1AEF49AB2A62D39F091FF9AA0FD4CB695D084637DBA7EF7DA2E657BBBF0C5FCC355DB37866B7BBD5AE065DC0FD399A8E0FC19C10943D5059507DC822DED6AFA67A3082010D06092A864886F70D0107013081FF06082A864886F70D030704085050B8007C2CE5608081E8DC683EECE2BF1FC1D209D5F6642E01E58DC76FF7926B576CB6884B6723C63DDE91D8E6C75DFC4E94F1CDDA8A3E863BE8A7E1DFCD2115E251675F73388D022A28247ED66D7892AA57800750A5F84313ACC3616449A703D7DFC770F50C816F224FB038E675FB1751916699FD00585C1B2EA19FECEE696611FA65B4E8516210D884E351201A888A47D874B1ACDDF4AE7F6F59D0780A5BE3E788DD6FB4E6AC1B9D966443881E9998A625CFB10A35D943B21A3ABB902CF68AD6F7FE7B0C18FF05B94C10E254017203541AFF71E440A42C8B915A84B341F923EF657280DB7B19F769E29725FF7E5999859C318202553082025102010130819E308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3037353535363935333735303112301006035504070C0941726C696E67746F6E02106BD452CE836B7D2A717B69DB8FAF3679300B0609608648016503040201A0818A301806092A864886F70D010903310B06092A864886F70D010703301C06092A864886F70D010905310F170D3233303631333139303234305A301F06092A864886F70D0107013112041044303131324B30544230304530303030302F06092A864886F70D010904312204209AD3A76A89E2F58433DF669174A6F4D4B6B3D60A8A7341712CB666CA6AE4125E300D06092A864886F70D0101010500048201009BA48B242A227AD05243DBB99ACF6249D626CEF086DAFD8B064592EFF1205CFE6713D5FC373D8CD53AF9A88292E143A4B9C1887792E8E7F6310503B1FD8F0F89F735DFF11CC55114859B902841E4D163D64E19DFAE0151B93590C8D770E47E939DF08242897F9319DC6AB272C26DE2ACC539BF055CE528B139D61B45542FF35D2ABDE34EEF5BE19D1C48679187B455864EDD3D976CDC80070A6A6635DF5A00AF08CBBF309C4D59A4710A531A719562D390394A736E9F2DED502B2F766BA56727DFB0C6A92FD4D2BABC69BDDBD6B17EB376FA9ADD83C2974292447E63F26D168E66A4558ED97E417BDE97837188DB4F414A2219BAC50A8D726CD54C3C1EXAMPLE", "WrappedKeyMaterialFormat": "TR34_KEY_BLOCK" } }`For more information, see [Export keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-export.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [ExportKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/export-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-alias`.

- **AWS CLI**
- 
            
                    **To get an alias**The following `get-alias`example returns the ARN of the key associated with the alias.`aws payment-cryptography get-alias \ --alias-name``alias/sampleAlias1`Output: `{ "Alias": { "AliasName": "alias/sampleAlias1", "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h" } }`For more information, see [About aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-about.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GetAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-alias.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-key`.

- **AWS CLI**
- 
            
                    **To get the metadata of a key**The following `get-key`example returns the metadata of the key associated with the alias. This operation does not return cryptographic material.`aws payment-cryptography get-key \ --key-identifier``alias/sampleAlias1`Output: `{ "Key": { "CreateTimestamp": "1686800690", "DeletePendingTimestamp": "1687405998", "Enabled": true, "Exportable": true, "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/kwapwa6qaifllw2h", "KeyAttributes": { "KeyAlgorithm": "TDES_2KEY", "KeyClass": "SYMMETRIC_KEY", "KeyModesOfUse": { "Decrypt": false, "DeriveKey": false, "Encrypt": false, "Generate": true, "NoRestrictions": false, "Sign": false, "Unwrap": false, "Verify": true, "Wrap": false }, "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY" }, "KeyCheckValue": "F2E50F", "KeyCheckValueAlgorithm": "ANSI_X9_24", "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY", "KeyState": "DELETE_PENDING", "UsageStartTimestamp": "1686801190" } }`For more information, see [Get keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/getkeys.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GetKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-parameters-for-export`.

- **AWS CLI**
- 
            
                    **To initialize the export process**The following `get-parameters-for-export`example generates a key pair, signs the key, and then returns the certificate and certificate root.`aws payment-cryptography get-parameters-for-export \ --signing-key-algorithm``RSA_2048`\ --key-material-type`TR34_KEY_BLOCK`Output: `{ "ExportToken": "export-token-ep5cwyzune7oya53", "ParametersValidUntilTimestamp": "1687415640", "SigningKeyAlgorithm": "RSA_2048", "SigningKeyCertificate": "MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=", "SigningKeyCertificateChain": "NIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=" }`For more information, see [Export keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-export.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GetParametersForExport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-parameters-for-export.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-parameters-for-import`.

- **AWS CLI**
- 
            
                    **To initialize the import process**The following `get-parameters-for-import`example generates a key pair, signs the key, and then returns the certificate and certificate root.`aws payment-cryptography get-parameters-for-import \ --key-material-type``TR34_KEY_BLOCK`\ --wrapping-key-algorithm`RSA_2048`Output: `{ "ImportToken": "import-token-qgmafpaa7nt2kfbb", "ParametersValidUntilTimestamp": "1687415640", "WrappingKeyAlgorithm": "RSA_2048", "WrappingKeyCertificate": "MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=", "WrappingKeyCertificateChain": "NIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=" }`For more information, see [Import keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-import.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GetParametersForImport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-parameters-for-import.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-public-key-certificate`.

- **AWS CLI**
- 
            
                    **To return the public key**The following `get-public-key-certificate`example returns the public key portion of a key pair.`aws payment-cryptography get-public-key-certificate \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`Output: `{ "KeyCertificate": "MIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=", "KeyCertificateChain": "NIICiTCCAfICCQD6m7oRw0uXOjANBgkqhkiG9w0BAQUFADCBiDELMAkGA1UEBhMC VVMxCzAJBgNVBAgTAldBMRAwDgYDVQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6 b24xFDASBgNVBAsTC0lBTSBDb25zb2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAd BgkqhkiG9w0BCQEWEG5vb25lQGFtYXpvbi5jb20wHhcNMTEwNDI1MjA0NTIxWhcN MTIwNDI0MjA0NTIxWjCBiDELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAldBMRAwDgYD VQQHEwdTZWF0dGxlMQ8wDQYDVQQKEwZBbWF6b24xFDASBgNVBAsTC0lBTSBDb25z b2xlMRIwEAYDVQQDEwlUZXN0Q2lsYWMxHzAdBgkqhkiG9w0BCQEWEG5vb25lQGFt YXpvbi5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMaK0dn+a4GmWIWJ 21uUSfwfEvySWtC2XADZ4nB+BLYgVIk60CpiwsZ3G93vUEIO3IyNoH/f0wYK8m9T rDHudUZg3qX4waLG5M43q7Wgc/MbQITxOUSQv7c7ugFFDzQGBzZswY6786m86gpE Ibb3OhjZnzcvQAaRHhdlQWIMm2nrAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAtCu4 nUhVVxYUntneD9+h8Mg9q6q+auNKyExzyLwaxlAoo7TJHidbtS4J5iNmZgXL0Fkb FFBjvSfpJIlJ00zbhNYS5f6GuoEDmFJl0ZxBHjJnyp378OD8uTs7fLvjx79LjSTb NYiytVbZPQUQ5Yaxu2jXnimvw3rrszlaEXAMPLE=" }`For more information, see [Get the public key/certificate associated with a key pair](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys.getpubliccertificate-example.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GetPublicKeyCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/get-public-key-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-key`.

- **AWS CLI**
- 
            
                    **To import a TR-34 key**The following `import-key`example imports a TR-34 key.`aws payment-cryptography import-key \ --key-material='{ "Tr34KeyBlock": {" \ CertificateAuthorityPublicKeyIdentifier": "arn:aws:payment-cryptography:us-west-2:123456789012:key/rmm5wn2q564njnjm", \ "ImportToken": "import-token-5ott6ho5nts7bbcg", \ "KeyBlockFormat": "X9_TR34_2012", \ "SigningKeyCertificate": file://signing-key-certificate.pem, \ "WrappedKeyBlock": file://wrapped-key-block.pem }}'`Contents of `signing-key-certificate.pem`:`LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUV2RENDQXFTZ0F3SUJBZ0lRYWVCK25IbE1WZU1PR1ZiNjU1Q2JzREFOQmdrcWhraUc5dzBCQVEwRkFEQ0IKaVRFTE1Ba0dBMVVFQmhNQ1ZWTXhHVEFYQmdOVkJBb01FRUZYVXlCRGNubHdkRzluY21Gd2FIa3hJVEFmQmdOVgpCQXNNR0VGWFV5QlFZWGx0Wlc1MElFTnllWEIwYjJkeVlYQm9lVEVSTUE4R0ExVUVDQXdJVm1seVoybHVhV0V4CkZUQVRCZ05WQkFNTUREVXlPVEF5TnpRMU5UUTVOVEVTTUJBR0ExVUVCd3dKUVhKc2FXNW5kRzl1TUI0WERUSXoKTURZd09USXlNVEkxTUZvWERUSXpNRFl4TmpJek1USTFNRm93TERFVk1CTUdBMVVFQXd3TU5USTVNREkzTkRVMQpORGsxTVJNd0VRWURWUVFGRXdvek1EVTRNVGszTkRjNE1JSUJJakFOQmdrcWhraUc5dzBCQVFFRkFBT0NBUThBCk1JSUJDZ0tDQVFFQXdMc0dGb0pqOTVJY0UxL1p1OGZxak40SDVHTFJHVGZQSkFyWWJLbjA4WXVrQTE0SjRBSHEKWGR6ZlY5MjcvVTJZTWN2S3FsNlk5SVQwejZhTVBGbDVYemZWNU1YVW5YMlJxYTladU1ndDhGSDJJYWxsMEQ3bgo0V0RjUkg3TERQdEhXZTRaVmh3aExRVEFQa1I2dUxTWC84UDhSN2lrSWpkVkI4SytjVitnbHh0clB1Vkh5TzNxCjhXRUl3a1lYVTFDVjJybHptNklzWjcycjhPcXJWcHNiZEhERENBelJ2YUtPN3hMNU1RUGVFMFcvdkxmRGdrYmoKb2h4VHl6Z3dRSlJFK21tUXdCRmlIeXdaY2F5Y1FZdXdzTktoK0xPWXJpN0ZGM2lRRTJlYlY5Mm4zZER5NDRtcQpUSjFHUWJENndFM3ZHS0xnYXNqMVl0WVNSTk9xNld1UTV3SURBUUFCbzN3d2VqQUpCZ05WSFJNRUFqQUFNQjhHCkExVWRJd1FZTUJhQUZHMVBsWElaUGdETVU0WjVwRTc3dE8xYmV2eDVNQjBHQTFVZERnUVdCQlFwanByQXFoZGMKVmF2dElTRnBBNkswVzJMcmJUQU9CZ05WSFE4QkFmOEVCQU1DQmFBd0hRWURWUjBsQkJZd0ZBWUlLd1lCQlFVSApBd0VHQ0NzR0FRVUZCd01DTUEwR0NTcUdTSWIzRFFFQkRRVUFBNElDQVFCOXVxcFVadU1oK1kzQXhXSklNUkx5Cmlob2gvR0xIanh1aVhxK1IvdFRxbTBNYTA3R2dvbGxhRkdIZzZMei9ELy9ZRDB2UHdYc1dVOE5qY0Vib095aGcKc0hmay9hVGxjRnovZm51MVlkRUpvYUpFdW15bDkwSTBMNyswUmJNYXJScWU0bC9yQlQ4YTM3R0JyQ0x0ZUlyRgorcnp1cmovU1BDM1FiUWkvOVBzWmlieTFKMlFxTzVVRUJncEYreklaVk84dzgwMzVEK1YrUXhsY2RaUGVLS2JnCmI5WHNSeHF3cUZIVUVRM2tybXdVZUZveERlbm91QmxKMVFzOTVXUHBpVk9zYUFvbkJkYUtEbFBaRTlqdG1zZkwKMER3b1lRRy92bHdWN0pIVnNNd0dleml2VGJXaWFNdmZTTkxIMmVZMG9rblhFcHlHcmlWMjczSVFqVU1QTXBMNgpjODh3OUYzcTJnY0x6Nk0ycEFHUTZ0SVBrZ2c3aUZjbk9haGp4Ty9ORFZrS0xxbXZ0eFFlcUk2VDRveWRuWkVWCkdOMjBISStZcFVud09Eem1GL1k5TXZQQXFtdGJka2dZZGRJWExtbU9ORlF1dm4wenp0Tm01NzNTN0NSYWxCNTgKeFhyNm1iak1MQU1tcmZGQmNrU0NYaUZ6Y3gvNHJTRGJtbU9INWM0dGxiNEM3SzF5QU96NWo3OHhWOWNQOTM3SQpwczcrZUFZRkFpYTdzZGpuS3hNUDN4ZVVTM0tNS2FGMzg2TGRYbkRwdTFyczhVRWhPeDhqakt6RWplWU9qV3hLClo5Mjd1Yzd0b2kwZlcvT2tzT3NnWVlybmttSEhyd3p0NXRBc2llcjFyWXFGK2lYa1Y4TzRxSzI0bHc4cXFPanUKS3htVHMzY0NlTmdGNUZhVmhCV1Zjdz09Ci0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0=`Contents of `wrapped-key-block.pem`:`3082059806092A864886F70D010702A082058930820585020101310D300B06096086480165030402013082031606092A864886F70D010703A082030704820303020100318201F3308201EF02010030819E308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3532393032373435353439353112301006035504070C0941726C696E67746F6E021026C5E52507841B72C59D9F0065548DC1304506092A864886F70D0101073038300D06096086480165030402010500301806092A864886F70D010108300B0609608648016503040201300D06092A864886F70D01010904000482010013D3C2E9405CA45A947BA6EA098DD5A83A7E6CFF4E140B141634EBFF9E0F78057B5C22013574BA8C8D8D64B43C391E1D9CDF081B33D15CDE3AB2DB21CAE7380E64B0A09A8C45B8A0F87659638E6E30D4351E9B941EDD384183DA169ADDF71FC64E06487F8750B74B2CD3AB4F8534C024AE04BD7C070CB685A250EB2A8C1EEDEBFA387935466D152E063D3EBEDD6231216EEE5145983C74D755C050D191E6E41DC2BDB09E78CDA203C2767270E3E56C6E24EB1090904462743B054098DE278A18C71577CAE1EC13CF776055224F299DBF1BC96C11F339DEE1A2CD130A275959820FBE5C34C0CB21DB6404F868B348D5A6F8ED8E5DC5BC681F6115BA278879FF8F3082010506092A864886F70D0107013081F706082A864886F70D0307040857F8BFE99B4493AD8081E05DEE59D9E60520DB8A15869BB840F1CC908DAE6CC6F6BE79DDF72DD8EA84F881D7DFB4A186CDC622B29E3F97AEB7C00872D1BB47FE235D9204F80A4D3EF502309ECD967F8F70A2F741738ACE7B7CA0AA2EBB0DACD3126F7831F79AF6DC3C74CEBF7D0947301245F42C59508FBC0318C03F02E37EDF014C4D0170ACC4E992EC7E9B85D95BF87F75FD2E0B938E2D8E807872DE4017F8530D59A48C9F68AF5BEC1B2115D7555C248F980DF28C69619E508317F0C20461AE26CD0D55896FEE71E1EA89F7F9B5DC047F9BD063210E1F09D9566EF2AF6472AD44A8ACC0180AC1995CDE318202553082025102010130819E308189310B300906035504061302555331193017060355040A0C104157532043727970746F6772617068793121301F060355040B0C18415753205061796D656E742043727970746F6772617068793111300F06035504080C0856697267696E69613115301306035504030C0C3532393032373435353439353112301006035504070C0941726C696E67746F6E021069E07E9C794C55E30E1956FAE7909BB0300B0609608648016503040201A0818A301806092A864886F70D010903310B06092A864886F70D010703301C06092A864886F70D010905310F170D3233303630393233333934365A301F06092A864886F70D0107013112041044303131324330544330304530303030302F06092A864886F70D01090431220420D6413C502DC4552B495B9A8449F9A3BF9E6DCB31AD56A1D158DB482BDF06EEAD300D06092A864886F70D010101050004820100313BA7BCDFE6C55F3544A8E7D9973A346DDAD17CC5C506DE72B8B7E490891702E753C445FED78D5477C5E5A2BF63378B2F12CE6C22C1A543BCC41FA978568F65C0171DBF3E438E70FD68DAB52BA1DEB294C4ED92CD6EAA684B4352AF6C53924048931595FC7F1FF642E82B12DBD8B8578DA200DC0CCE2FA075897CDA6D5257C78DC2B515015CC414E78B49075AFF333C7CEAFF81F5EEC44C5C9F6BD32898E6983A7CEA40DD5C0CF9CD51DB3E712ED1C755E0A9DA38286872B46D7119088A76728DC08AECB0F624B34E15349E5B2334900E57885A6461AC6E74B35A3FFF5C010ACE5F15DE9D867A5160D30217997E7DE6319A74F5D55D44A934908A3BC1602D22`Output: `{ "Key": { "CreateTimestamp": "2023-06-09T16:56:27.621000-07:00", "Enabled": true, "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/bzmvgyxdg3sktwxd", "KeyAttributes": { "KeyAlgorithm": "TDES_2KEY", "KeyClass": "SYMMETRIC_KEY", "KeyModesOfUse": { "Decrypt": false, "DeriveKey": false, "Encrypt": false, "Generate": true, "NoRestrictions": false, "Sign": false, "Unwrap": false, "Verify": true, "Wrap": false }, "KeyUsage": "TR31_C0_CARD_VERIFICATION_KEY" }, "KeyCheckValue": "D9B20E", "KeyCheckValueAlgorithm": "ANSI_X9_24", "KeyOrigin": "EXTERNAL", "KeyState": "CREATE_COMPLETE", "UsageStartTimestamp": "2023-06-09T16:56:27.621000-07:00" } }`For more information, see [Import keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-import.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [ImportKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/import-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-aliases`.

- **AWS CLI**
- 
            
                    **To get a list of aliases**The following `list-aliases`example shows all of the aliases in your account in this Region.`aws payment-cryptography list-aliases`Output: `{ "Aliases": [ { "AliasName": "alias/sampleAlias1", "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h" }, { "AliasName": "alias/sampleAlias2", "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h" } ] }`For more information, see [About aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-about.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [ListAliases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/list-aliases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-keys`.

- **AWS CLI**
- 
            
                    **To get a list of keys**The following `list-keys`example shows all of the keys in your account in this Region.`aws payment-cryptography list-keys`Output: `{ "Keys": [ { "CreateTimestamp": "1666506840", "Enabled": false, "Exportable": true, "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h", "KeyAttributes": { "KeyAlgorithm": "TDES_3KEY", "KeyClass": "SYMMETRIC_KEY", "KeyModesOfUse": { "Decrypt": true, "DeriveKey": false, "Encrypt": true, "Generate": false, "NoRestrictions": false, "Sign": false, "Unwrap": true, "Verify": false, "Wrap": true }, "KeyUsage": "TR31_P1_PIN_GENERATION_KEY" }, "KeyCheckValue": "369D", "KeyCheckValueAlgorithm": "ANSI_X9_24", "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY", "KeyState": "CREATE_COMPLETE", "UsageStopTimestamp": "1666938840" } ] }`For more information, see [List keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-about.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [ListKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/list-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To get the list of tags for a key**The following `list-tags-for-resource`example gets the tags for a key.`aws payment-cryptography list-tags-for-resource \ --resource-arn``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`Output: `{ "Tags": [ { "Key": "BIN", "Value": "20151120" }, { "Key": "Project", "Value": "Production" } ] }`For more information, see [Managing key tags with API operations](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/manage-tags-api.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `restore-key`.

- **AWS CLI**
- 
            
                    **To restore a key that is scheduled for deletion**The following `restore-key`example cancels the deletion of a key.`aws payment-cryptography restore-key \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`Output: `{ "Key": { "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h", "KeyAttributes": { "KeyUsage": "TR31_V2_VISA_PIN_VERIFICATION_KEY", "KeyClass": "SYMMETRIC_KEY", "KeyAlgorithm": "TDES_3KEY", "KeyModesOfUse": { "Encrypt": false, "Decrypt": false, "Wrap": false, "Unwrap": false, "Generate": true, "Sign": false, "Verify": true, "DeriveKey": false, "NoRestrictions": false } }, "KeyCheckValue": "", "KeyCheckValueAlgorithm": "ANSI_X9_24", "Enabled": false, "Exportable": true, "KeyState": "CREATE_COMPLETE", "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY", "CreateTimestamp": "1686800690", "UsageStopTimestamp": "1687405998" } }`For more information, see [Deleting keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-deleting.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [RestoreKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/restore-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-key-usage`.

- **AWS CLI**
- 
            
                    **To enable a key**The following `start-key-usage`example enables a key to be used.`aws payment-cryptography start-key-usage \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`Output: `{ "Key": { "CreateTimestamp": "1686800690", "Enabled": true, "Exportable": true, "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh", "KeyAttributes": { "KeyAlgorithm": "TDES_3KEY", "KeyClass": "SYMMETRIC_KEY", "KeyModesOfUse": { "Decrypt": true, "DeriveKey": false, "Encrypt": true, "Generate": false, "NoRestrictions": false, "Sign": false, "Unwrap": true, "Verify": false, "Wrap": true }, "KeyUsage": "TR31_P1_PIN_GENERATION_KEY" }, "KeyCheckValue": "369D", "KeyCheckValueAlgorithm": "ANSI_X9_24", "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY", "KeyState": "CREATE_COMPLETE", "UsageStartTimestamp": "1686800690" } }`For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-enable-disable.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [StartKeyUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/start-key-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-key-usage`.

- **AWS CLI**
- 
            
                    **To disable a key**The following `stop-key-usage`example disables a key.`aws payment-cryptography stop-key-usage \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`Output: `{ "Key": { "CreateTimestamp": "1686800690", "Enabled": true, "Exportable": true, "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/alsuwfxug3pgy6xh", "KeyAttributes": { "KeyAlgorithm": "TDES_3KEY", "KeyClass": "SYMMETRIC_KEY", "KeyModesOfUse": { "Decrypt": true, "DeriveKey": false, "Encrypt": true, "Generate": false, "NoRestrictions": false, "Sign": false, "Unwrap": true, "Verify": false, "Wrap": true }, "KeyUsage": "TR31_P1_PIN_GENERATION_KEY" }, "KeyCheckValue": "369D", "KeyCheckValueAlgorithm": "ANSI_X9_24", "KeyOrigin": "AWS_PAYMENT_CRYPTOGRAPHY", "KeyState": "CREATE_COMPLETE", "UsageStartTimestamp": "1686800690" } }`For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-enable-disable.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [StopKeyUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/stop-key-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a key**The following `tag-resource`example tags a key.`aws payment-cryptography tag-resource \ --resource-arn``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`\ --tags`Key=sampleTag,Value=sampleValue`This command produces no output. For more information, see [Managing key tags](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/manage-tags-api.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a key**The following `untag-resource`example removes a tag from a key.`aws payment-cryptography untag-resource \ --resource-arn``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`\ --tag-keys`sampleTag`This command produces no output. For more information, see [Managing key tags](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/manage-tags-api.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-alias`.

- **AWS CLI**
- 
            
                    **To update an alias**The following `update-alias`example associates the alias with a different key.`aws payment-cryptography update-alias \ --alias-name``alias/sampleAlias1`\ --key-arn`arn:aws:payment-cryptography:us-east-2:123456789012:key/tqv5yij6wtxx64pi`Output: `{ "Alias": { "AliasName": "alias/sampleAlias1", "KeyArn": "arn:aws:payment-cryptography:us-west-2:123456789012:key/tqv5yij6wtxx64pi " } }`For more information, see [About aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/alias-about.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [UpdateAlias](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography/update-alias.html)in*AWS CLI Command Reference*.
 
-