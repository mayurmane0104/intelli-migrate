# Managing your Anypoint Platform Account | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/access-management/managing-your-account](https://docs.mulesoft.com/access-management/managing-your-account)

---

# Managing your Anypoint Platform Account

Create a new Anypoint Platform account, sign in to an existing Anypoint Platform organization through an invitation, use your current account to access a new organization, and set up a new account within an existing organization. You can also sign in to Anypoint Platform using single sign-on and allowlist URLs for uninterrupted access.

## Create an Anypoint Platform Account

- 
Go to [the signup page](https://anypoint.mulesoft.com/login/signup).
- 
Enter your information in the form: - 
**Email**You can use the same email address for multiple Anypoint Platform accounts, but each account must have a unique username so you can manage all your Anypoint Platform accounts under a single email address. 
- 
**Username**Must be at least three characters and contain only: - 
Alphanumeric characters 
- 
Dashes 
- 
Underscores 
 
- 
- 
**Phone Number**Phone number with area code. 
- 
**Password**Must be between 8 and 64 characters in length with at least one uppercase letter, one lowercase letter, and one number. Your password can contain only: - 
Upper and lower case characters 
- 
Numbers 
- 
Non-alphanumeric symbols 
 
- 
- 
**Company**Must be at least two characters in length. If you were invited to join an existing organization, the company name is already set. Anypoint Platform creates a new root organization (business group) using the company name you entered and makes you the administrator of that organization. An Anypoint Platform account is associated with only one root organization. 
 
- 
- 
Click the terms of service link to read the Anypoint Platform Trial License agreement, then check the box to agree to the terms of service. 
- 
Click the **I’m not a Robot**CAPTCHA checkmark and wait for validation.You might be prompted to perform a small test before proceeding. Google’s reCaptcha verification service autodetects your browser’s language. 
- 
Click **Accept and create account**.

## Join an Existing Organization

To join an existing Anypoint Platform organization or create a new account in an existing organization, ask the organization administrator for an invitation. When the administrator responds with an email invitation, you must click the included link within one week.

- 
Click the link you received in the Anypoint Platform invitation email. You must use the email address the invitation email was sent to to sign up for an account with that organization. 
- 
Enter your information in the form. If your email address is associated with more than one Anypoint Platform account, after clicking the link in the invitation select either: 
- 
Agree to the terms of service and privacy policy, then click **Accept and create account in <org>**.

| You can’t create a new account within an existing organization without an email invitation. | 

## Use an Existing Account

You can use an existing account to join an existing organization after you receive an invitation. For example, if you’re invited to join the **MuleSoft** Organization, and you have three different Anypoint Platform accounts:

- 
Member An account not associated with any organization. 
- 
Admin An account with the organization administrator role associated to a different organization. 
- 
Owner An organization owner account for a different organization. 

After clicking the link in the invitation, you have one week to choose the account to use to join the organization.

| If the account you want to use is already associated with another root organization, an exclamation mark is shown next to your account. Additional steps are needed before migrating the account to a new organization. | 

## Sign in to Anypoint Platform

- 
Navigate to the Anypoint Platform signin screen. 
- 
Enter your username and password. 
- 
Click **Sign in**.

| If Anypoint Platform rejects your valid credentials, your organization uses an [external identity provider](external-identity)to initiate the sign-in process. Navigate to your external identity provider to sign in, or[enter your organization’s domain name](#use-CustomDomainLogin)before reentering your credentials. | 

## Sign in to Anypoint Platform Using Single Sign-on

If your organization uses [Single Sign-on](external-identity), provide your organization’s domain name as part of the sign-in process.

- 
Navigate to the Anypoint Platform signin screen. 
- 
Click **Use custom domain**.
- 
Enter your organization’s domain name. If you don’t know your organization’s domain name, a member of your organization can provide the organization domain name, which is accessible in their user profile. 
- 
Click **Continue**.You’re redirected to your identity provider. 

## Allowlist URLs to Sign in to and Use Anypoint Platform

To make sure your sessions aren’t blocked or interrupted by your organization’s firewall or proxy if you use a restricted environment, such as a virtual machine, or have proxy requirements preventing you from signing in to Anypoint Platform, add these URLs to your allowlists:

- 
`https://*.mulesoft.com/*`
- 
`https://*.salesforce.com/*`
- 
`https://app.launchdarkly.com/*`
- 
`https://clientstream.launchdarkly.com/*`
- 
`https://www.gstatic.com/recaptcha/*`
- 
`https://www.google.com/recaptcha/*`
- 
[https://npmcdn.com/*](https://npmcdn.com/*)
- 
[https://cdnjs.cloudflare.com/*](https://cdnjs.cloudflare.com/*)
- 
[https://fast.appcues.com/*](https://fast.appcues.com/*)

## Use an Unassociated Account

When an organization administrator deletes an account from the organization, the deleted account is *unattached*.

You can use an unattached account to join the **MuleSoft** organization with no further configurations needed. Select the account, enter its corresponding password, and click **Sign in**.

## Use an Organization Administrator Account

If your account is an organization administrator for a different organization (or business group within that organization), your username is shown with an exclamation mark next to it.

You can use this account to join **MuleSoft**, however all existing references from this account to the existing organization are lost.

After selecting this account and entering the password associated with it, you’re asked to confirm your decision. If you proceed:

- 
If there are other members in the business group you’re leaving, the organization administrator of the parent organization is automatically assigned as the organization administrator for the business group. 
- 
If there are no other members, the business group is deleted. 

## Account Associated as an Organization Owner

A common scenario is to create an account that’s not associated with any existing organization. This automatically assigns your account to a new organization and makes your account an organization owner.

After selecting this account, entering its corresponding password, and clicking the **Sign in** button, if there are no other members in the organization you own:

- 
You get a warning that all associations to the existing organization will be lost. 
- 
The organization you’re leaving will be deleted. 

However, if the organization your account owns has other members, Anypoint Platform won’t allow you to migrate to **MuleSoft**.

To free your account from the organization you own, open a support ticket at [https://help.salesforce.com](https://help.salesforce.com). Provide this information:

- 
The username of another user within the organization you own to promote to owner 
- 
The organization name and organization ID of the organization 

After support confirms the migration is complete, you can use your account to join MuleSoft.

| If you have a trial account at no additional cost and want to migrate your username to a new organization, another organization administrator in your current organization must delete your organization owner account from the organization associated with your trial account. | 

## Link Your Anypoint Platform Profiles

When you sign in to Anypoint Platform for the first time using an external identity provider (IdP), Anypoint Platform locates potential user accounts that match the email address associated with your IdP profile. Your options for linking profiles vary based on whether the profiles use the Anypoint identity provider (IdP) or an external IdP that uses single sign-on (SSO). Anypoint Platform supports:

- 
Linking an SSO signin to a local profile by using credentials (signin managed by Anypoint IdP) 
- 
Linking an SSO signin to another SSO signin that uses a different IdP to sign in 
- 
Linking an SSO signin to multiple other profiles that each use different IdPs to sign in 

Anypoint Platform doesn’t support linking multiple profiles that use the same IdP. The IdP must be an OpenID Connect (OIDC) provider. You can link up to 25 user profiles. This feature is available only if an [organization administrator has enabled it](external-identity-index#enable-profile-linking).

### Link a New SSO Signin to Existing Profiles

When you attempt to sign in using SSO for the first time and there are additional user profiles that share the same email address but use different identity providers (IdPs) to sign in, you are prompted to link the profiles. You cannot link profiles that use the same IdP.

- 
In the Anypoint Platform signin page, click **Sign in with <your identity provider>**.
- 
If prompted, enter your credentials for your IdP. 
 If your SSO credentials share an email address with additional profiles in the same organization, you are prompted to select one of the profiles and sign in with those credentials to link your profiles.
- 
In the **Link your Account**page, select the profile you want to link.
 You can hover over each profile to see which identity provider it uses.
- 
Click **Link Accounts**.
- 
Enter your credentials for the profile you chose. You can now view your linked profile in the **Logged In Via**section of your user profile.

## Update User Information

- 
Sign in to Anypoint Platform. 
- 
In the Anypoint Platform navigation bar, click the circle icon with the initials associated with your Anypoint Platform account and select your name. 

You can modify your contact information, change your password, and see a list of the permissions assigned to your account.

### Manage Sensitive Account Information

For enhanced security, Access Management might prompt you to reauthenticate before you can modify your email address.

Access Management prompts you to reauthenticate when:

- 
More than 30 minutes have elapsed since you entered your password, Access Management prompts you to reenter your password. 
- 
You have multifactor authentication (MFA) enabled and more than eight hours have elapsed since you entered your password and used MFA, Access Management prompts you to reenter your password and confirm the signin using MFA. 

Each time you sign in or reauthenticate, the timer resets. If less than 30 minutes have elapsed since you signed in, Access Management does not prompt for your password again.

Connected apps and clients are exempt from reauthentication. If you have a script that makes an API call to change your email address, update it to accommodate reauthentication if necessary.

### Verify Your Email Address

As of October 10, 2022, non-SSO users must verify their Anypoint Platform email addresses. If you haven’t verified your email address, an email verification request prompt appears each time you sign in. You can verify your email using the sign in prompt, or you can verify your email in your user profile. SSO users can’t verify their email addresses through Anypoint Platform and don’t receive verification prompts.

- 
Sign in to Anypoint Platform. 
- 
In the Anypoint Platform navigation bar, click the circle icon with the initials associated with your Anypoint Platform account and select your name. 
- 
Click the **Contact Info**tab.
- 
In the **Email**section, click**Verify Email**.
- 
Enter the verification code you received at your Anypoint Platform account’s email address. The verification email can take a few minutes to arrive. If you don’t see the email in your inbox after several minutes, check your Spam folder. 
- 
Click **Confirm**.

## Change Your Account Email Address

You can change the email address that you use to sign in to your Anypoint Platform account.

| SSO users can’t change their account email address through Anypoint Platform. | 

- 
Sign in to Anypoint Platform. 
- 
In the Anypoint Platform navigation bar, click the circle icon with the initials associated with your Anypoint Platform account and select your name. 
- 
Click the **Contact Info**tab.
- 
In the **Email**row, click the pencil icon.
- 
Enter your new email address. 
- 
Click **Save Changes**.
- 
If you’re signed in to Anypoint Platform for more than 30 minutes, reenter your password to reauthenticate. 
- 
Enter the verification code you received at the new email address you entered. 
- 
Click **Confirm**.The email address you entered is now your primary email address for Anypoint Platform. 

## Reset Your Password

When you reset your password, your new password must be between 8 and 64 characters in length with at least one uppercase letter, one lowercase letter, and one number. Your password must contain only ASCII-standard characters. You can’t reuse any of your previous three passwords.

- 
Navigate to the Anypoint Platform signin page. 
- 
Click the **Forgot your username or password**link.
- 
In the **Forgot your credentials**form, enter your username.A link to create a new password is emailed to you. 
- 
Click the reset password link in the email. 
- 
In the **Reset your password**form, enter a new password and click**Reset Password**.

## Forgot User Name

- 
Navigate to the Anypoint Platform signin page. 
- 
Click the **Forgot your username or password**link.
- 
In the **Forgot your credentials**form, enter the email address you used for your Anypoint Platform account, then click**Request credentials**.You receive an email from Anypoint Platform with a list of user names associated with your email address. 

## Upgrade Your Account

To upgrade your Anypoint Platform trial account to an enterprise license, contact your account representative or [the MuleSoft sales team](https://www.mulesoft.com/contact).

## Known Issue: Account Creation

When you attempt to create an account from an email invitation to join an organization, and you use a username that already exists (even in a different organization), an error appears, erroneously stating your credentials are invalid. This error occurs when a username already exists, even if it is under a different organization. If the username already belongs to you, you can move the username from your previous organization to the organization that sent you the email invitation.