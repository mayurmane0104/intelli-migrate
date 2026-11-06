# Managing mobile settings - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/manage-mobile-settings.html](https://docs.aws.amazon.com/quick/latest/userguide/manage-mobile-settings.html)

---

Mobile settings allow Amazon Quick admins to enhance data security and maintain compliance standards for users accessing Quick through mobile devices. These settings apply to all users accessing Quick through the mobile application.

###### To access mobile settings:

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
            Choose the user icon at the top right, and then choose **Manage Amazon Quick**.
- 
            Under the **Security**section, choose**Mobile settings**.
- 
            Choose settings to enhance your data security on mobile devices: - 
                    **Require use of biometrics or PIN to unlock device**- Check the box to enable this security requirement. When enabled, users must use fingerprint recognition, Face ID, device PINs, or other biometric authentication methods supported by their device to access Amazon Quick.
- 
                    **Require devices to use the latest version of the mobile operating system**- Check the box to enable this security requirement. When enabled, users must keep their mobile devices' operating systems up to date to access Amazon Quick.
 
- 
                    
- 
            To manage how long users can remain logged in on mobile devices: - 
                    Locate the **Current session lifetime for all devices**setting.
- 
                    Select the desired duration from the dropdown menu. The maximum session lifetime depends on your identity provider: - 
                            **IAM Identity Center**: Maximum session lifetime is 7 days.
- 
                            **All other identity providers**: Maximum session lifetime is 30 days (default).
 The minimum session lifetime for all identity providers is 12 hours. 
- 
                            
- 
                    Choose **Update**to apply your changes.
 
- 
                    

## Best practices

        - 
                Regularly review and update mobile security settings to align with your organization's security policies 
- 
                Set an appropriate session lifetime that balances security with user convenience 
- 
                Enable biometric/PIN requirements for additional security, especially when dealing with sensitive data 
- 
                Keep operating system requirements enabled to ensure devices have the latest security updates 
- 
                Communicate changes in mobile settings to your users before implementation