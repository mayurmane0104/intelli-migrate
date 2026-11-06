# Administrator configuration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/administrator-configuration.html](https://docs.aws.amazon.com/quick/latest/userguide/administrator-configuration.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators and Amazon Quick administrators | 

As a Amazon Quick administrator, you can configure various settings for user-driven license upgrades, including enabling the feature, setting approval policies, and configuring custom permissions profiles.

## Enabling user-driven upgrades

        
        Before users can request license upgrades, you must enable the user-driven upgrade feature in your Amazon Quick account settings.

### Access Administrator Settings

- 
                    Log in to your Amazon Quick administrator account 
- 
                    Navigate to the 'Manage Account' section of the console 
- 
                    Check for User upgrades Section 
- 
                    Use the toggle button to Enable/Disable - Automatically approve upgrades 

### Configuring approval settings

Administrators can configure three types of upgrade governance:

- 
                    **Turned off altogether**— Users cannot request upgrades
- 
                    **Admin Approval**(default for IAM Identity Center and AD) — Users can request upgrades that require administrator approval
- 
                    **User Driven Upgrades**(default for IdP) — Users can upgrade automatically without approval

## Creating a custom permissions profile for Amazon Quick account that is integrated with IAM Identity Center or Active Directory

        
        Amazon Quick account administrators can use the following procedure to create a custom permissions profile for an Amazon Quick account that is integrated with IAM Identity Center or Active Directory.

### To create a custom permissions profile for an Amazon Quick account that is integrated with IAM Identity Center or Active Directory

- 
                    Sign in to the [AWS Management Console](https://console.aws.amazon.com/).
- 
                    Open Amazon Quick. 
- 
                    The Amazon Quick Admin console opens. Choose **Custom Permissions**.
- 
                    The **Manage custom permissions**page opens. Choose one of the following options.
- 
                    To create a new custom permissions profile, choose **Create**.
- 
                    To edit or view an existing custom permissions profile, choose the ellipses (three dots) next to the profile that you want, and then choose **Edit**.
- 
                    If you want to create or update a custom permissions profile, make selections for the following items. 
- 
                    For **Name**, enter a name for the custom permissions profile.
- 
                    For **Restrictions**, choose "Allow users to upgrade or request upgrades" under "User Upgrades". Choose any other options that you want to deny. Any option that you don't choose is allowed.
- 
                    Choose **Create**or**Update**to confirm your choices. To go back without making any changes, choose**Back**.
- 
                    Once you are done making changes, record the name of the custom permissions profile. Provide the name of the custom permissions profile to API users so that they can apply the custom permissions profile to roles or users. 

## Creating a custom permissions profile for an Amazon Quick account that uses Amazon Quick managed users

        
        Amazon Quick account administrators can use the following procedure to create a custom permissions profile for an Amazon Quick account that uses Amazon Quick managed users.

### To create a custom permissions profile for Amazon Quick managed users

- 
                    Open the [Amazon Quick console](https://quicksight.aws.amazon.com/).
- 
                    From any page in the Amazon Quick console, choose **Manage Amazon Quick**at the top right corner.
- 
                    Only Amazon Quick administrators have access to the **Manage Amazon Quick**menu option. If you don't have access to the**Manage Amazon Quick**menu, contact your Amazon Quick administrator for assistance.
- 
                    Choose **Custom permissions**. You can also choose the**Manage users**section and then choose**Manage custom permissions**.
- 
                    The **Manage custom permissions**page opens. Choose one of the following options.
- 
                    To create a new custom permissions profile, choose **Create**.
- 
                    To edit or view an existing custom permissions profile, choose the ellipses (three dots) next to the profile that you want, and then choose **Edit**.
- 
                    If you want to create or update a custom permissions profile, make selections for the following items. 
- 
                    For **Name**, enter a name for the custom permissions profile.
- 
                    For **Restrictions**, choose "Allow users to upgrade or request upgrades" under "User Upgrades". Choose any other options that you want to deny. Any option that you don't choose is allowed.
- 
                    Choose **Create**or**Update**to confirm your choices. To go back without making any changes, choose**Back**.
- 
                    Once you are done making changes, record the name of the custom permissions profile. Provide the name of the custom permissions profile to API users so that they can apply the custom permissions profile to roles or users. 

## Applying custom permissions profiles

        
         
            ### Apply a custom permissions profile to an Amazon Quick role with the Amazon Quick API

For more information, see [Apply custom permissions profile to role](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-role.html#customizing-permissions-to-the-quicksight-console-apply-role).

### Apply a custom permissions profile to a user with the Amazon Quick API

For more information, see [Apply custom permissions profile to user](https://docs.aws.amazon.com/quicksight/latest/user/customizing-permissions-to-the-quicksight-console-apply-iam-user.html#customizing-permissions-to-the-quicksight-console-apply-iam-user).

### Apply a custom permissions profile to an account

For more information, see [Apply custom permissions profile to account](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html#customizing-permissions-to-the-quicksight-console-apply-account).

### Apply a custom permissions profile to an account using the Amazon Quick APIs

For more information, see [Apply custom permissions profile using APIs](https://docs.aws.amazon.com/quicksuite/latest/userguide/create-custom-permissions-profile.html#customizing-permissions-to-the-quicksight-console-apply-account-with-apis).