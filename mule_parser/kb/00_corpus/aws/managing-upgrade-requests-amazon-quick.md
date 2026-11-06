# Managing upgrade requests - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/managing-upgrade-requests.html](https://docs.aws.amazon.com/quick/latest/userguide/managing-upgrade-requests.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators and Amazon Quick administrators | 

As an administrator, you can view and manage user license upgrade requests through the Amazon Quick admin console. This section describes how to approve, deny, or verify upgrade requests based on your organization's identity management setup.

## Viewing upgrade requests

        
        To view pending upgrade requests, navigate to the User upgrades section in the admin console. The requests table displays the username, current role, requested role, request date, and available actions for each pending request.

###### To view upgrade requests

- 
                Sign in to the Amazon Quick console as an administrator. 
- 
                Choose **Manage Amazon Quick**from the top right corner.
- 
                Navigate to the **User upgrades**section.
- 
                Review the pending requests in the table. 

## Processing upgrade requests

        
        The process for handling upgrade requests varies depending on your organization's identity management setup.

### Processing requests for IdP identity type

For organizations using Identity Provider (IdP) authentication, administrators can directly approve or deny requests.

###### To process IdP upgrade requests

- 
                    In the upgrade requests table, choose **View details**for the request you want to process.
- 
                    Review the request details in the modal that opens. 
- 
                    Choose one of the following options: - 
                            **Approve**— Grants the requested license upgrade immediately
- 
                            **Deny**— Rejects the upgrade request
 
- 
                            
- 
                    Confirm your selection. The system displays a success message and removes the processed request from the pending list. 

### Processing requests for IAM Identity Center and Active Directory identity types

For organizations using IAM Identity Center or Active Directory, administrators must add users to the appropriate groups before verifying the upgrade.

###### To process IAM Identity Center and Active Directory upgrade requests

- 
                    In the upgrade requests table, choose **View details**for the request you want to process.
- 
                    Note the required group name(s) displayed in the modal. 
- 
                    Navigate to your IAM Identity Center or Active Directory management console. 
- 
                    Add the user to the required group for the requested license tier. 
- 
                    Return to the Amazon Quick admin console and choose **Verify**.
- 
                    The system checks the user's group membership and completes the upgrade if verification succeeds. 

Alternatively, you can choose **Deny** to reject the upgrade request without making any group changes.

## Understanding upgrade request statuses

        
        Upgrade requests can have the following statuses:

- 
                **Pending**— Request is awaiting administrator action
- 
                **Approved**— Request has been approved and the user's license has been upgraded
- 
                **Denied**— Request has been rejected by an administrator
- 
                **Verified**— For IAM Identity Center/AD setups, the user has been added to the required group and the upgrade is complete