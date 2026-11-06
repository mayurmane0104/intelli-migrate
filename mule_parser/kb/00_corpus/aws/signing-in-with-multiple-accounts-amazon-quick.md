# Signing in with multiple accounts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/signing-in-multiple-accounts.html](https://docs.aws.amazon.com/quick/latest/userguide/signing-in-multiple-accounts.html)

---

You can sign in to Amazon Quick with multiple accounts at the same time and switch between them as necessary.

###### To sign in to multiple accounts

- 
                Follow the steps at [Signing in to Amazon Quick](./signing-in.html)to sign in to Amazon Quick.
- 
                From the navigation bar, choose your account name to reveal a dropdown menu. 
- 
                Hover over **Switch accounts**. A list of accounts that you've signed in to before appears. Do one of the following:- 
                        To switch to an account, select that account and provide sign-in credentials. 
- 
                        To sign in to a new account, choose **Add another account**. You are prompted to provide sign-in credentials for the account.
 
- 
                        

###### To sign out of an account or all accounts

- 
                From the navigation bar, choose your account name to reveal a dropdown menu. 
- 
                Hover over **Sign out**. You can choose to sign out of your current account or to**Sign out of all accounts**.

## URL structure

            When using multiple accounts, Amazon Quick URLs include the account name to identify which account you're accessing.

### Application URLs

Application URLs follow this structure:

`https://us-east-1.quicksight.aws.amazon.com/sn/account/``ACCOUNT-NAME`/...

Examples:

```
https://us-east-1.quicksight.aws.amazon.com/sn/account/my-account/start/home
https://us-east-1.quicksight.aws.amazon.com/sn/account/my-account/dashboards/1234
```
### Console URLs

Console URLs follow this structure.

**Standard accounts (account alias is the account
                        ID)**

`https://us-east-1.quicksight.aws.amazon.com/sn/console/account/``123456789012`/...

Examples:

```
https://us-east-1.quicksight.aws.amazon.com/sn/console/account/123456789012/admin
https://us-east-1.quicksight.aws.amazon.com/sn/console/account/123456789012/asset-management
```
**Accounts with IAM multi-account access (account alias
                        is the session differentiator)**

`https://us-east-1.quicksight.aws.amazon.com/sn/console/account/``123456789012-abc123`/...

Examples:

```
https://us-east-1.quicksight.aws.amazon.com/sn/console/account/123456789012-abc123/admin
https://us-east-1.quicksight.aws.amazon.com/sn/console/account/123456789012-abc123/asset-management
```
## Key considerations and limitations

            - 
                    The URL structures above enable bookmarking of resources within the Amazon Quick account. 
- 
                    You can simultaneously be signed in to different accounts in different tabs or windows in your browser. 
- 
                    The Amazon Quick URL contains your account name. If you change it to another account name, you are prompted to sign in if you aren't already. 
- 
                    You can sign in to up to five accounts. If you try to sign in to a sixth account, the system automatically signs out and forgets the least recently signed in account. 
- 
                    Multi-account sign-in is not supported for IAM users who access Amazon Quick through IAM-based multi-account federation. 

## IAM SSO federation with multi-account

            For more information about setting up identity federation, see
                    [Initiating sign-on from Quick](./federated-identities-sp-to-idp.html).

### Service Provider (SP) initiated federation

If your account has SSO configuration established in Quick, all login attempts or links that include the account alias provide seamless login. There is no change in behavior for these logins.

### Identity Provider (IdP) initiated federation

**Scenarios with no change in behavior:**

- 
                        If you have enabled IAM multi-account access, all federation links provide seamless login, regardless of whether they include the account alias. 
- 
                        If you have SSO configuration enabled in Quick, all IdP initiated federation or IdP deep links that include the account alias provide seamless login. 
- 
                        If you have never used Quick before or have only ever used one account with Quick and you use IdP federation to access that one account, there is no change in experience. 

**Scenarios with change in behavior:** When you
                    have one or more saved Quick accounts and access any IdP federation
                    link without an account alias, instead of being taken directly to your account,
                    you land on the Quick saved account login page where you can select
                    your session and be taken to your account.

**Recommended configuration:** To ensure seamless
                    IdP federation, include the account alias in all IdP federation links. If you are
                    unable to ensure the account alias in your deep links or you do not have SSO
                    configuration enabled in Quick, include the
                        `sso_login=true` query parameter in your links.

Recommended example start federation URL:

`https://us-east-1.quicksight.aws.amazon.com/sn/account/``ACCOUNT-NAME`/start/home?sso_login=true