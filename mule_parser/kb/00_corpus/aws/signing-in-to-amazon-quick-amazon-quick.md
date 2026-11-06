# Signing in to Amazon Quick - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/signing-in.html](https://docs.aws.amazon.com/quick/latest/userguide/signing-in.html)

---

You can sign in to Amazon Quick multiple ways, depending on what your Quick administrator has set up. You can sign in to Quick using AWS root, AWS Identity and Access Management (IAM), corporate Active Directory, or your native Quick credentials. If your Quick account is integrated with an identity provider such as Okta, the following procedures don't apply to you.

If you're a Quick administrator, make sure to allow-list the following domains within your organization's network.

| User type | Domain or domains to allow-list | 
|---|---|
| Users who sign in directly through Quick and Active Directory users | 
 | 
| AWS root user | 
 | 
| IAM users | 
 | 

###### Important

We strongly recommend that you don't use the AWS root user for your everyday tasks,
            even the administrative ones. Instead, adhere to the best practice of using the root
            user only to create your first IAM user. Then securely lock away the root user
            credentials and use them to perform only a few account and service management tasks. For
            more information, see [AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html) in the
                *IAM User Guide*.

## Signing in through the AWS Console

        Use the following procedure to sign in to Quick through the AWS Management Console.

###### To sign in to Quick

- 
                For **Quick account name**, enter your account name. This is the name that was created when the Quick account was created in AWS.If you were invited to the Quick account by email, you can find the account name inside of that email. If you don't have the email that invited you to Quick, ask the Quick administrator in your organization for the information that you need. You can also find your Quick account name by choosing the profile icon on the Quick console menu. In some cases, you might not have access to your Quick account or have an administrator who can provide this information, or both. If so, contact AWS Support and open a ticket that includes your AWS customer ID. 
- 
                For **Username**, enter your Quick user name. User names that contain a semicolon (;) aren't supported. Choose one of the following:- 
                        For organizational users – The user name is provided by your administrator. Your account can be based on IAM credentials or your email address if it's a root email address. Or it can be used as the user name to invite you into the Quick account. If you received an invitation email from another Quick user, it indicates what type of credentials to use. 
- 
                        For individual users – The user name that you created for yourself. This is usually the IAM credentials that you created. 
 
- 
                        

The remaining steps vary depending on the user type you sign in as (directly through Quick or as an Active Directory user, AWS root user, or IAM user). For more information, see the following sections.

### Finishing Quick sign-in as a Quick or Active Directory user

If you're signing in directly through Quick or are using your
                corporate Active Directory credentials, you're redirected to `signin.aws`
                after you enter your account name and user name. Use the following procedure to
                finish signing in.

###### To finish signing in to Quick if you sign in directly through Quick or use Active Directory credentials

- 
                    For **Password**, enter your password.Passwords are case-sensitive and must be 8–64 characters in length. They must also contain each of the following: - 
                            Lowercase letters (a–z) 
- 
                            Uppercase letters (A–Z) 
- 
                            Numbers (0–9) 
- 
                            Nonalphanumeric characters (~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/) 
 
- 
                            
- 
                    If your account is multi-factor authentication enabled, enter the multi-factor authentication code that you receive for **MFA code**.
- 
                    Choose **Sign in**.

### Finishing Quick sign-in as an AWS root user

If you're signing in as an AWS root user, you're redirected to signin.aws.amazon.com (or amazon.com) to complete the sign-in process. Your user name is prefilled. Use the following procedure to finish signing in.

###### To finish signing in as an AWS root user

- 
                    Choose **Next**.
- 
                    For **password**, enter your password. For more information about root user passwords, see[Changing the AWS account root user password](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_change-root.html)in the*IAM User Guide*.
- 
                    Choose **Sign in**.

### Finishing Quick sign-in as an IAM user

If you're signing in as an IAM user, you're redirected to signin.aws.amazon.com (or amazon.com) to complete the sign-in process. Your user name is prefilled. Use the following procedure to finish signing in.

###### To finish signing in as an IAM user

- 
                    For **Password**, enter your password. For more information about IAM user passwords, see[Default password policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html#default-policy-details)in the*IAM User Guide*.
- 
                    Choose **Sign in**.

If your sign-in process happens automatically and you need to use a different account, use a private or incognito browser window. Doing this prevents the browser from reusing cached settings.

###### Note

If you're not sure which type of account you have: if you signed up at [quick.aws.com](https://quick.aws.com) and use an email/password to sign
            in, you have a Free or Plus account. If you sign in through the AWS Management Console or your
            organization's single sign-on portal, you have an AWS Console account.