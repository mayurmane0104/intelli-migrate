# Using Starburst with Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/connecting-to-starburst.html](https://docs.aws.amazon.com/quick/latest/userguide/connecting-to-starburst.html)

---

Starburst is a full-featured data lake analytics service built on top of a massively
            parallel processing (MPP) query engine, Trino. Use this section to learn how to connect
            from Amazon Quick Sight to Starburst. All traffic between Quick Sight and Starburst is enabled by
            SSL. If you're connecting to Starburst Galaxy, you can get the necessary connection
            details by logging in to your Starburst Galaxy account, then choose **Partner
                Connect** and then **Quick Sight**. You should be able to
            see information, such as hostname and port. Amazon Quick Sight supports basic username and password
            authentication to Starburst.

Quick Sight offers two ways to connect to Starburst: with your Starburst login credentials or with OAuth client credentials. Use the following sections to learn about both methods of connection.

###### Topics

## Creating an Quick Sight data source connection to Starburst with login credentials

            - 
                    Begin by creating a new dataset. From the left navigation pane, choose **Data**, then choose**Create**, then choose**New Dataset**.
- 
                    Choose the **Starburst**data source card.
- 
                    Select the Starburst product type. Choose **Starburst Enterprise**for on-prem Starburst instances. Choose**Starburst Galaxy**for managed instances.
- 
                    For **Data source name**, enter a descriptive name for your Starburst data source connection. Because you can create many datasets from a connection to Starburst, it's best to keep the name simple.
- 
                    For **Connection type**, select the type of network you're using. Choose**Public network**if your data is shared publicly. Choose**VPC**if your data is inside a VPC. To configure a VPC connection in Amazon Quick Sight, see[Configuring the VPC connection in Amazon Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/vpc-creating-a-connection-in-quicksight.html). This connection type is not available for Starburst Galaxy.
- 
                    For **Database server**enter the hostname specified in your Starburst connection details.
- 
                    For **Catalog**, enter the catalog specified in your Starburst connection details.
- 
                    For **Port**, enter the port specified in your Starburst connection details. Defaults to 443 for Starburst Galaxy.
- 
                    For **Username**and**Password**, enter your Starburst connection credentials.
- 
                    To verify the connection is working, choose **Validate connection**.
- 
                    To finish and create the data source, choose **Create data source**.

###### Note

Connectivity between Amazon Quick Sight and Starburst was validated using Starburst version 420.

After you have successfully created a data source connection between your
                Quick Sight and Starburst accounts, you can begin [Creating datasets](./creating-data-sets.html) that contain
                Starburst data.

## Creating an Quick Sight data source connection to Starburst with OAuth client credentials

            You can use OAuth client credentials to connect your Quick Sight
                account with Starburst through the [Quick Sight
                    APIs](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html). *OAuth* is a standard
                authorization protocol that is often utilized for applications that have advanced
                security requirements. When you connect to Starburst with OAuth
                client credentials, you can create datasets that contain Starburst data with the
                Quick Sight APIs and in the Quick Sight UI. For more information about configuring
                    OAuth in Starburst, see [OAuth
                    2.0 authentication](https://docs.starburst.io/latest/security/oauth2.html).

Quick Sight supports the `client credentials`
                OAuth grant type. OAuth client credentials is used to
                obtain an access token for machine-to-machine communication. This method is suitable
                for scenarios where a client needs to access resources that are hosted on a server
                without the involvement of a user.

In the client credentials flow of OAuth 2.0, there are several client authentication mechanisms that can be used to authenticate the client application with the authorization server. Quick Sight supports client credentials based OAuth for Starburst for the following two mechanisms:

- 
                    **Token (Client secrets-based OAuth)**: The secret-based client authentication mechanism is used with the client credentials to grant flow in order to authenticate with authorization server. This authentication scheme requires the`client_id`and`client_secret`of the OAuth client app to be stored in Secrets Manager.
- 
                    **X509 (Client private key JWT-based OAuth)**: The X509 certificate key-based solution provides an additional security layer to the OAuth mechanism with client certificates that are used to authenticate instead of client secrets. This method is primarily used by private clients who use this method to authenticate with the authorization server with strong trust between the two services.

Quick Sight has validated OAuth connections with the following Identity providers:

- 
                    OKTA 
- 
                    PingFederate 

### Storing OAuth credentials in Secrets Manager

OAuth client credentials are meant for machine-to-machine use
                    cases and are not designed to be interactive. To create a datasource connection
                    between Quick Sight and Starburst, create a new secret in Secrets Manager that contains
                    your credentials for the OAuth client app. The secret ARN that is
                    created with the new secret can be used to create datasets that contain
                    Starburst data in Quick Sight. For more information about using Secrets Manager keys in
                    Quick Sight, see [Using AWS Secrets Manager secrets instead of database credentials in Quick](./secrets-manager-integration.html).

The credentials that you need to store in Secrets Manager are determined by the OAuth mechanism that you use. The following key/value pairs are required for X509-based OAuth secrets:

- 
                        `username`: The Starburst account username to be used when connecting to Starburst
- 
                        `client_id`: The OAuth client ID
- 
                        `client_private_key`: The OAuth client private key
- 
                        `client_public_key`: The OAuth client certificate public key and its encrypted algorithm (for example,`{"alg": "RS256", "kid", "cert_kid"}`)

The following key/value pairs are required for token-based OAuth secrets:

- 
                        `username`: The Starburst account username to be used when connecting to Starburst
- 
                        `client_id`: The OAuth client ID
- 
                        `client_secret`: the OAuth client secret

### Creating a Starburst OAuth connection with the Quick Sight APIs

After you create a secret in Secrets Manager that contains your Starburst OAuth credentials and have connected your Quick account to Secrets Manager, you can establish a data source connection between Quick Sight and Starburst with the Quick Sight APIs and SDK. The following example creates a Starburst data source connection using token OAuth client credentials.

```
{
    "AwsAccountId": "
```
`AWSACCOUNTID`",
    "DataSourceId": "`DATASOURCEID`",
    "Name": "`NAME`",
    "Type": "STARBURST",
    "DataSourceParameters": {
        "StarburstParameters": {
            "Host": "`STARBURST_HOST_NAME`",
            "Port": "`STARBURST_PORT`",
            "Catalog": "`STARBURST_CATALOG`",
            "ProductType": "`STARBURST_PRODUCT_TYPE`",     
            "AuthenticationType": "TOKEN",
            "DatabaseAccessControlRole": "`starburst-db-access-role-name`",
            "OAuthParameters": {
              "TokenProviderUrl": "`oauth-access-token-endpoint`", 
              "OAuthScope": "oauth-scope",
              "IdentityProviderResourceUri" : "`resource-uri`",
              "IdentityProviderVpcConnectionProperties" : {
                "VpcConnectionArn": "`IdP-VPC-connection-ARN`"
            }
        }
    },
    "VpcConnectionProperties": {
        "VpcConnectionArn": "`VPC-connection-ARN-for-Starburst`"
    },
    "Credentials": {
        "SecretArn": "`oauth-client-secret-ARN`"
    }
}For more information about the CreateDatasource API operation, see [CreateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html).

Once the connection between Quick Sight and Starburst is established and a
                    data source is created with the Quick Sight APIs or SDK, the new data source is
                    displayed in Quick Sight. Quick Sight authors can use this data source to
                    create datasets that contain Starburst data. Tables are displayed based on the
                    role used in the `DatabaseAccessControlRole` parameter that is passed
                    in a `CreateDataSource` API call. If this parameter is not defined
                    when the data source connection is created, the default Starburst role is
                    used.

After you have successfully created a data source connection between your
                    Quick Sight and Starburst accounts, you can begin [Creating datasets](./creating-data-sets.html) that
                    contain Starburst data.