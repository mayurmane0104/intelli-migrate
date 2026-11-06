# AWS Payment Cryptography Data Plane examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_payment-cryptography-data_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_payment-cryptography-data_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS Payment Cryptography Data Plane.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `decrypt-data`.

- **AWS CLI**
- 
            
                    **To decrypt ciphertext**The following `decrypt-data`example decrypts ciphertext data using a symmetric key. For this operation, the key must have`KeyModesOfUse`set to`Decrypt`and`KeyUsage`set to`TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY`.`aws payment-cryptography-data decrypt-data \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`\ --cipher-text`33612AB9D6929C3A828EB6030082B2BD`\ --decryption-attributes '`Symmetric={Mode=CBC}`'Output: `{ "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h", "KeyCheckValue": "71D7AE", "PlainText": "31323334313233343132333431323334" }`For more information, see [Decrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/decrypt-data.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [DecryptData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/decrypt-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `encrypt-data`.

- **AWS CLI**
- 
            
                    **To encrypt data**The following `encrypt-data`example encrypts plaintext data using a symmetric key. For this operation, the key must have`KeyModesOfUse`set to`Encrypt`and`KeyUsage`set to`TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY`.`aws payment-cryptography-data encrypt-data \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`\ --plain-text`31323334313233343132333431323334`\ --encryption-attributes '`Symmetric={Mode=CBC}`'Output: `{ "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h", "KeyCheckValue": "71D7AE", "CipherText": "33612AB9D6929C3A828EB6030082B2BD" }`For more information, see [Encrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/encrypt-data.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [EncryptData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/encrypt-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-card-validation-data`.

- **AWS CLI**
- 
            
                    **To generate a CVV**The following `generate-card-validation-data`example generates a CVV/CVV2.`aws payment-cryptography-data generate-card-validation-data \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`\ --primary-account-number=171234567890123 \ --generation-attributes`CardVerificationValue2={CardExpiryDate=0123}`Output: `{ "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h", "KeyCheckValue": "CADDA1", "ValidationData": "801" }`For more information, see [Generate card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-card-data.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GenerateCardValidationData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-card-validation-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-mac`.

- **AWS CLI**
- 
            
                    **To generate a MAC**The following `generate-card-validation-data`example generates a Hash-Based Message Authentication Code (HMAC) for card data authentication using the algorithm HMAC_SHA256 and an HMAC encryption key. The key must have`KeyUsage`set to`TR31_M7_HMAC_KEY`and`KeyModesOfUse`to`Generate`.`aws payment-cryptography-data generate-mac \ --key-identifier``arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h`\ --message-data`"3b313038383439303031303733393431353d32343038323236303030373030303f33"`\ --generation-attributes`Algorithm=HMAC_SHA256`Output: `{ "KeyArn": "arn:aws:payment-cryptography:us-east-2:123456789012:key/kwapwa6qaifllw2h, "KeyCheckValue": "2976E7", "Mac": "ED87F26E961C6D0DDB78DA5038AA2BDDEA0DCE03E5B5E96BDDD494F4A7AA470C" }`For more information, see [Generate MAC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-mac.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GenerateMac](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-mac.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-pin-data`.

- **AWS CLI**
- 
            
                    **To generate a PIN**The following `generate-card-validation-data`example generate a new random PIN using the Visa PIN scheme.`aws payment-cryptography-data generate-pin-data \ --generation-key-identifier``arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2`\ --encryption-key-identifier`arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt`\ --primary-account-number`171234567890123`\ --pin-block-format`ISO_FORMAT_0`\ --generation-attributes`VisaPin={PinVerificationKeyIndex=1}`Output: `{ "GenerationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2", "GenerationKeyCheckValue": "7F2363", "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt", "EncryptionKeyCheckValue": "7CC9E2", "EncryptedPinBlock": "AC17DC148BDA645E", "PinData": { "VerificationValue": "5507" } }`For more information, see [Generate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/generate-pin-data.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [GeneratePinData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/generate-pin-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `re-encrypt-data`.

- **AWS CLI**
- 
            
                    **To re-encrypt data with a different key**The following `re-encrypt-data`example decrypts cipher text that was encrypted using an AES symmetric key and re-encrypts it using a Derived Unique Key Per Transaction (DUKPT) key.`aws payment-cryptography-data re-encrypt-data \ --incoming-key-identifier``arn:aws:payment-cryptography:us-west-2:111122223333:key/hyvv7ymboitd4vfy`\ --outgoing-key-identifier`arn:aws:payment-cryptography:us-west-2:111122223333:key/jl6ythkcvzesbxen`\ --cipher-text`4D2B0BDBA192D5AEFEAA5B3EC28E4A65383C313FFA25140101560F75FE1B99F27192A90980AB9334`\ --incoming-encryption-attributes`"Dukpt={Mode=ECB,KeySerialNumber=0123456789111111}"`\ --outgoing-encryption-attributes '`{"Symmetric": {"Mode": "ECB"}}`'Output: `{ "CipherText": "F94959DA30EEFF0C035483C6067667CF6796E3C1AD28C2B61F9CFEB772A8DD41C0D6822931E0D3B1", "KeyArn": "arn:aws:payment-cryptography:us-west-2:111122223333:key/jl6ythkcvzesbxen", "KeyCheckValue": "2E8CD9" }`For more information, see [Encrypt and decrypt data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/crypto-ops.encryptdecrypt.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [ReEncryptData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/re-encrypt-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `translate-pin-data`.

- **AWS CLI**
- 
            
                    **To translate PIN data**The following `translate-pin-data`example translates a PIN from PEK TDES encryption using ISO 0 PIN block to an AES ISO 4 PIN Block using the DUKPT algorithm.`aws payment-cryptography-data translate-pin-data \ --encrypted-pin-block``"AC17DC148BDA645E"`\ --incoming-translation-attributes=IsoFormat0='{PrimaryAccountNumber=171234567890123}' \ --incoming-key-identifier`arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt`\ --outgoing-key-identifier`arn:aws:payment-cryptography:us-east-2:111122223333:key/4pmyquwjs3yj4vwe`\ --outgoing-translation-attributes IsoFormat4="{PrimaryAccountNumber=171234567890123}" \ --outgoing-dukpt-attributes KeySerialNumber="FFFF9876543210E00008"Output: `{ "PinBlock": "1F4209C670E49F83E75CC72E81B787D9", "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt "KeyCheckValue": "7CC9E2" }`For more information, see [Translate PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/translate-pin-data.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [TranslatePinData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/translate-pin-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-auth-request-cryptogram`.

- **AWS CLI**
- 
            
                    **To verify an auth request**The following `verify-auth-request-cryptogram`example verifies an Authorization Request Cryptogram (ARQC).`aws payment-cryptography-data verify-auth-request-cryptogram \ --auth-request-cryptogram``F6E1BD1E6037FB3E`\ --auth-response-attributes '`{"ArpcMethod1": {"AuthResponseCode": "1111"}}`' \ --key-identifier`arn:aws:payment-cryptography:us-west-2:111122223333:key/pboipdfzd4mdklya`\ --major-key-derivation-mode`"EMV_OPTION_A"`\ --session-key-derivation-attributes '`{"EmvCommon": {"ApplicationTransactionCounter": "1234","PanSequenceNumber": "01","PrimaryAccountNumber": "471234567890123"}}`' \ --transaction-data`"123456789ABCDEF"`Output: `{ "AuthResponseValue": "D899B8C6FBF971AA", "KeyArn": "arn:aws:payment-cryptography:us-west-2:111122223333:key/pboipdfzd4mdklya", "KeyCheckValue": "985792" }`For more information, see [Verify auth request (ARQC) cryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/data-operations.verifyauthrequestcryptogram.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [VerifyAuthRequestCryptogram](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-auth-request-cryptogram.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-card-validation-data`.

- **AWS CLI**
- 
            
                    **To validate a CVV**The following `verify-card-validation-data`example validates a CVV/CVV2 for a PAN.`aws payment-cryptography-data verify-card-validation-data \ --key-identifier``arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi`\ --primary-account-number=171234567890123 \ --verification-attributes`CardVerificationValue2={CardExpiryDate=0123}`\ --validation-data`801`Output: `{ "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/tqv5yij6wtxx64pi", "KeyCheckValue": "CADDA1" }`For more information, see [Verify card data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-card-data.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [VerifyCardValidationData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-card-validation-data.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-mac`.

- **AWS CLI**
- 
            
                    **To verify a MAC**The following `verify-mac`example verifies a Hash-Based Message Authentication Code (HMAC) for card data authentication using the algorithm HMAC_SHA256 and an HMAC encryption key.`aws payment-cryptography-data verify-mac \ --key-identifier``arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6`\ --message-data`"3b343038383439303031303733393431353d32343038323236303030373030303f33"`\ --verification-attributes='Algorithm=HMAC_SHA256' \ --mac`ED87F26E961C6D0DDB78DA5038AA2BDDEA0DCE03E5B5E96BDDD494F4A7AA470C`Output: `{ "KeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/qnobl5lghrzunce6, "KeyCheckValue": "2976E7", }`For more information, see [Verify MAC](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-mac.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [VerifyMac](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-mac.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-pin-data`.

- **AWS CLI**
- 
            
                    **To verify a PIN**The following `verify-pin-data`example validates a PIN for a PAN.`aws payment-cryptography-data verify-pin-data \ --verification-key-identifier``arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2`\ --encryption-key-identifier`arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt`\ --primary-account-number`171234567890123`\ --pin-block-format`ISO_FORMAT_0`\ --verification-attributes VisaPin="{PinVerificationKeyIndex=1,VerificationValue=5507}" \ --encrypted-pin-block`AC17DC148BDA645E`Output: `{ "VerificationKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/37y2tsl45p5zjbh2", "VerificationKeyCheckValue": "7F2363", "EncryptionKeyArn": "arn:aws:payment-cryptography:us-east-2:111122223333:key/ivi5ksfsuplneuyt", "EncryptionKeyCheckValue": "7CC9E2", }`For more information, see [Verify PIN data](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/verify-pin-data.html)in the*AWS Payment Cryptography User Guide*.- 
                    For API details, see [VerifyPinData](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/payment-cryptography-data/verify-pin-data.html)in*AWS CLI Command Reference*.
 
-