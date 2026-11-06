# Revoke and Delete API Contracts | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/remove-client-app-latest-task](https://docs.mulesoft.com/api-manager/latest/remove-client-app-latest-task)

---

# Revoke and Delete API Contracts

As the Organization Administrator of the root organization, you can revoke or delete a contract that is providing an application access to your API. When you revoke a contract, you can restore the contract at any time.

Deleting a contract deletes the approved contract from Anypoint Exchange. Revoking a contract blocks the client application from accessing the API. When you revoke a contract, you can either restore or delete the contract anytime. Before you delete a contract, you must first revoke it.

To delete a contract with an application:

- 
Navigate to **Anypoint Platform**>**API Manager**.
- 
In **API Administration**, click the name of the API instance for which you want to revoke access.
- 
Click the `<api version>:<api instance or label>`link, for example,`v1:16046365`.
- 
Click **Contracts**.
- 
For the application for which you want to revoke access, click **Revoke**.The **Restore**and**Delete**options appear.
- 
To delete the contract, click **Delete**.