# Using Snowflake with Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/connecting-to-snowflake.html](https://docs.aws.amazon.com/quick/latest/userguide/connecting-to-snowflake.html)

---

Snowflake is an AI data cloud platform that provides data solutions from data
            warehousing and collaboration to data science and generative AI. Snowflake is an [AWS
                Partner](https://partners.amazonaws.com/partners/001E000000d8qQcIAI/Snowflake) with multiple AWS accreditations that include AWS ISV
            Competencies in Generative AI, Machine Learning, Data and Analytics, and Retail.

Amazon Quick Sight offers two ways to connect to Snowflake: with your Snowflake login credentials or with OAuth client credentials. Use the following sections to learn about both methods of connection.

###### Topics

## Creating an Quick Sight data source connection to Snowflake with login credentials

            Use this section to learn how to create a connection between Quick Sight and Snowflake with your Snowflake login credentials. All traffic between Quick Sight and Snowflake is enabled by SSL.

###### To create a connection between Quick Sight and Snowflake

- 
	Open the [Quick console](https://quicksight.aws.amazon.com/).
- 
                    From the left navigation pane, choose **Data**, then choose**Create**, then choose**New Dataset**.
- 
                    Choose the **Snowflake**data source card.
- 
                    In the pop up that appears, enter the following information: - 
                            For **Data source name**, enter a descriptive name for your Snowflake data source connection. Because you can create many datasets from a connection to Snowflake, it's bets to keep the name simple.
- 
                            For **Connection type**, choose the type of network that you're using. Choose**Public network**if your data is shared publicly. Choose**VPC**if your data is located inside a VPC. To configure a VPC connection in Quick Sight, see[Managing VPC connection in Amazon Quick](./vpc-creating-a-connection-in-quicksight.html).
- 
                            For **Database server**enter the hostname specified in your Snowflake connection details.
 
- 
                            
- 
                    For **Database name and Warehouse**, enter the respective Snowflake database and wearehouse that you want to connect.
- 
                    For **Username**and**Password**, enter your Snowflake credentials.

After you have successfully created a data source connection between your
                Quick Sight and Snowflake accounts, you can begin [Creating datasets](./creating-data-sets.html) that contain
                Snowflake data.

## Creating an Quick Sight data source connection to Snowflake with OAuth client credentials

            You can use OAuth client credentials to connect your Quick Sight
                account with Snowflake through the [Quick Sight
                    APIs](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html). *OAuth* is a standard
                authorization protocol that is often utilized for applications that have advanced
                security requirements. When you connect to Snowflake with OAuth client credentials,
                you can create datasets that contain Snowflake data with the Quick Sight APIs and
                in the Quick Sight UI. For more information about configuring OAuth
                in Snowflake, see [Snowflake OAuth overview](https://docs.snowflake.com/en/user-guide/oauth-snowflake-overview).

Quick Sight supports the `client credentials`
                OAuth grant type. OAuth client credentials is used to
                obtain an access token for machine-to-machine communication. This method is suitable
                for scenarios where a client needs to access resources that are hosted on a server
                without the involvement of a user.

In the client credentials flow of OAuth 2.0, there are several client authentication mechanisms that can be used to authenticate the client application with the authorization server. Quick Sight supports client credentials based OAuth for Snowflake for the following two mechanisms:

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

OAuth client credentials are meant for machine-to-machine use cases and are
                    not designed to be interactive. To create a datasource connection between
                    Quick Sight and Snowflake, create a new secret in Secrets Manager that contains your
                    credentials for the OAuth client app. The secret ARN that is
                    created with the new secret can be used to create datasets that contain
                    Snowflake data in Quick Sight. For more information about using Secrets Manager keys in
                    Quick Sight, see [Using AWS Secrets Manager secrets instead of database credentials in Quick](./secrets-manager-integration.html).

The credentials that you need to store in Secrets Manager are determined by the OAuth mechanism that you use. The following key/value pairs are required for X509-based OAuth secrets:

- 
                        `username`: The Snowflake account username to be used when connecting to Snowflake
- 
                        `client_id`: The OAuth client ID
- 
                        `client_private_key`: The OAuth client private key
- 
                        `client_public_key`: The OAuth client certificate public key and its encrypted algorithm (for example,`{"alg": "RS256", "kid", "cert_kid"}`)

The following key/value pairs are required for token-based OAuth secrets:

- 
                        `username`: The Snowflake account username to be used when connecting to Snowflake
- 
                        `client_id`: The OAuth client ID
- 
                        `client_secret`: the OAuth client secret

### Creating a Snowflake OAuth connection with the Quick Sight APIs

After you create a secret in Secrets Manager that contains your Snowflake OAuth credentials and have connected your Quick account to Secrets Manager, you can establish a data source connection between Quick Sight and Snowflake with the Quick Sight APIs and SDK. The following example creates a Snowflake data source connection using token OAuth client credentials.

```
{
    "AwsAccountId": "
```
`AWSACCOUNTID`",
    "DataSourceId": "`UNIQUEDATASOURCEID`",
    "Name": "`NAME`",
    "Type": "SNOWFLAKE",
    "DataSourceParameters": {
        "SnowflakeParameters": {
            "Host": "`HOSTNAME`",
            "Database": "`DATABASENAME`",
            "Warehouse": "`WAREHOUSENAME`",
            "AuthenticationType": "TOKEN",
            "DatabaseAccessControlRole": "`snowflake-db-access-role-name`",
            "OAuthParameters": {
              "TokenProviderUrl": "`oauth-access-token-endpoint`", 
              "OAuthScope": "`oauth-scope`",
              "IdentityProviderResourceUri" : "`resource-uri`",
              "IdentityProviderVpcConnectionProperties" : {
                "VpcConnectionArn": "`IdP-VPC-connection-ARN`" 
             }
        }
    },
    "VpcConnectionProperties": {
        "VpcConnectionArn": "`VPC-connection-ARN-for-Snowflake`"
    }
    "Credentials": {
        "SecretArn": "`oauth-client-secret-ARN`"
    }
}For more information about the CreateDatasource API operation, see [CreateDataSource](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CreateDataSource.html).

Once the connection between Quick Sight and Snowflake is established and a
                    data source is created with the Quick Sight APIs or SDK, the new data source is
                    displayed in Quick Sight. Quick Sight authors can use this data source to
                    create datasets that contain Snowflake data. Tables are displayed based on the
                    role used in the `DatabaseAccessControlRole` parameter that is passed
                    in a `CreateDataSource` API call. If this parameter is not defined
                    when the data source connection is created, the default Snowflake role is
                    used.

After you have successfully created a data source connection between your
                    Quick Sight and Snowflake accounts, you can begin [Creating datasets](./creating-data-sets.html) that
                    contain Snowflake data.