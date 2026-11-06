# Obtaining the Client Credentials of a Registered Client Application | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/access-client-app-id-task](https://docs.mulesoft.com/api-manager/latest/access-client-app-id-task)

---

# Obtaining the Client Credentials of a Registered Client Application

As the owner of a [registered client application](../../exchange/to-request-access), you are occasionally required to provide your client ID and client secret when accessing an API, after a contract is created between your application and an API.

You are required to provide the client ID and client secret credentials depending on the policies applied to that API. For example, if the API owner has applied the Client ID Enforcement policy, you must provide your application’s client ID and, optionally, its client secret to access the API.

You must have the Organization Administrator privileges of the root organization, or must be the owner of the client application to access the credentials.

To obtain the credentials of a client application:

- 
Go to **Anypoint Platform**>**API Manager**.
- 
Click **Client Applications**.
- 
From the details pane, click the application for which you want to view the client credentials. The client ID and client secret credentials for the selected application appear in the window. 
- 
Alternatively, if you need to obtain only the client ID of the registered client application, select the correct version of the API and click **Contracts**.As an Application Owner, if you do not have access to API Manager, you can view the [application credentials](../../exchange/about-my-applications)in Exchange.
- 
To view the details, click the specific API contract.