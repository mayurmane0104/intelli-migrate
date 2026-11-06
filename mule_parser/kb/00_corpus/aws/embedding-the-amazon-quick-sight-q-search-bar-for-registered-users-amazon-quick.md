# Embedding the Amazon Quick Sight Q search bar for registered users - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-q-search-bar-for-authenticated-users.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-q-search-bar-for-authenticated-users.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

###### Note

The embedded Amazon Quick Sight Q search bar provides the classic Amazon Quick Sight
                Q&A experience. Amazon Quick Sight integrates with Amazon Q Business to launch a new
                Generative Q&A experience. Developers are recommended to use the new Generative Q&A experience. For more information on the
                embedded Generative Q&A experience, see [Embedding the Amazon Q in Amazon Quick Sight
                Generative Q&A experience](https://docs.aws.amazon.com/quicksight/latest/user/embedding-gen-bi.html).

In the following sections, you can find detailed information about how to set up an embedded Amazon Quick Sight Q search bar for registered users of Amazon Quick Sight.

###### Topics

## Step 1: Set up permissions

            ###### Note

The embedded Amazon Quick Sight Q search bar provides the classic
                    Amazon Quick Sight Q&A experience. Amazon Quick Sight integrates with
                    Amazon Q Business to launch a new Generative Q&A experience. Developers are recommended to use the new
                    Generative Q&A experience. For more information on the embedded Generative Q&A experience, see [Embedding the Amazon Q in Amazon Quick Sight Generative Q&A experience](https://docs.aws.amazon.com/quicksight/latest/user/embedding-gen-bi.html).

In the following section, you can find how to set up permissions for your backend application or web server to embed the Q search bar. This task requires administrative access to AWS Identity and Access Management (IAM).

Each user who accesses a dashboard assumes a role that gives them Amazon Quick Sight access and permissions to the dashboard. To make this possible, create an IAM role in your AWS account. Associate an IAM policy with the role to provide permissions to any user who assumes it. The IAM role needs to provide permissions to retrieve embedding URLs for a specific user pool.

With the help of the wildcard character ***, you can grant the
                permissions to generate a URL for all users in a specific namespace. Or you can
                grant permissions to generate a URL for a subset of users in specific namespaces.
                For this, you add `quicksight:GenerateEmbedUrlForRegisteredUser`.

You can create a condition in your IAM policy that limits the domains that
                developers can list in the `AllowedDomains` parameter of a
                    `GenerateEmbedUrlForRegisteredUser` API operation. The
                    `AllowedDomains` parameter is an optional parameter. It grants
                developers the option to override the static domains that are configured in the
                    **Manage Amazon Quick Sight** menu and instead list up to three
                domains or subdomains that can access a generated URL. This URL is then embedded in
                a developer's website. Only the domains that are listed in the parameter can access
                the embedded Q search bar. Without this condition, developers can list any domain on
                the internet in the `AllowedDomains` parameter. 

To limit the domains that developers can use with this parameter, add an
                    `AllowedEmbeddingDomains` condition to your IAM policy. For more
                information about the `AllowedDomains` parameter, see [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com//quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html) in the *Amazon Quick Sight API Reference*.

###### Security best practice for IAM condition operators

Improperly configured IAM condition operators can allow unauthorized access to your embedded Quick resources through URL variations. When using the `quicksight:AllowedEmbeddingDomains` condition key in your IAM policies, use condition operators that either allow specific domains or deny all domains that are not specifically allowed. For more information about IAM condition operators, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the IAM User Guide.

Many different URL variations can point to the same resource. For example, the following URLs all resolve to the same content:

- `https://example.com`
- `https://example.com/`
- `https://Example.com`

If your policy uses operators that do not account for these URL variations, an attacker can bypass your restrictions by providing equivalent URL variations.

You must validate that your IAM policy uses appropriate condition operators to prevent bypass vulnerabilities and ensure that only your intended domains can access your embedded resources.

The following sample policy provides these permissions.

Also, if you're creating first-time users who will be Amazon Quick Sight readers, make
                sure to add the `quicksight:RegisterUser` permission in the
                policy.

The following sample policy provides permission to retrieve an embedding URL for first-time users who are to be Amazon Quick Sight readers.

Finally, your application's IAM identity must have a trust policy associated with it to allow access to the role that you just created. This means that when a user accesses your application, your application can assume the role on the user's behalf and provision the user in Amazon Quick Sight.

The following example shows a sample trust policy.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Sid": "AllowLambdaFunctionsToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "lambda.amazonaws.com" }, "Action": "sts:AssumeRole" }, { "Sid": "AllowEC2InstancesToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }`

For more information regarding trust policies for OpenID Connect or Security
                Assertion Markup Language (SAML) authentication, see the following sections of the
                    *IAM User Guide:*

## Step 2: Generate the URL with the authentication code attached

            ###### Note

The embedded Amazon Quick Sight Q search bar provides the classic
                    Amazon Quick Sight Q&A experience. Amazon Quick Sight integrates with
                    Amazon Q Business to launch a new Generative Q&A experience. Developers are recommended to use the new
                    Generative Q&A experience. For more information on the embedded Generative Q&A experience, see [Embedding the Amazon Q in Amazon Quick Sight Generative Q&A experience](https://docs.aws.amazon.com/quicksight/latest/user/embedding-gen-bi.html).

In the following section, you can find how to authenticate your user and get the embeddable Q topic URL on your application server. If you plan to embed the Q bar for IAM or Amazon Quick Sight identity types, share the Q topic with the users.

When a user accesses your app, the app assumes the IAM role on the user's behalf. Then the app adds the user to Amazon Quick Sight, if that user doesn't already exist. Next, it passes an identifier as the unique role session ID.

Performing the described steps ensures that each viewer of the Q topic is uniquely provisioned in Amazon Quick Sight. It also enforces per-user settings, such as the row-level security and dynamic defaults for parameters.

The following examples perform the IAM authentication on the user's behalf. This code runs on your app server.

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
        import com.amazonaws.auth.AWSCredentialsProvider;
        import com.amazonaws.regions.Regions;
        import com.amazonaws.services.quicksight.AmazonQuickSight;
        import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
import com.amazonaws.services.quicksight.model.GenerateEmbedUrlForRegisteredUserRequest;
import com.amazonaws.services.quicksight.model.GenerateEmbedUrlForRegisteredUserResult;
import com.amazonaws.services.quicksight.model.RegisteredUserEmbeddingExperienceConfiguration;
import com.amazonaws.services.quicksight.model.RegisteredUserQSearchBarEmbeddingConfiguration;
        /**
 * Class to call QuickSight AWS SDK to get url for embedding the Q search bar.
        */
public class RegisteredUserQSearchBarEmbeddingConfiguration {
            private final AmazonQuickSight quickSightClient;
    public RegisteredUserQSearchBarEmbeddingConfiguration() {
        this.quickSightClient = AmazonQuickSightClientBuilder
                    .standard()
                    .withRegion(Regions.US_EAST_1.getName())
                    .withCredentials(new AWSCredentialsProvider() {
                            @Override
                            public AWSCredentials getCredentials() {
                                // provide actual IAM access key and secret key here
                                return new BasicAWSCredentials("access-key", "secret-key");
                            }
                            @Override
                            public void refresh() {
                            }
                        }
                    )
                    .build();
            }
    public String getQuicksightEmbedUrl(
            final String accountId, // AWS Account ID
            final String topicId, // Topic ID to embed
            final List<String> allowedDomains, // Runtime allowed domain for embedding
            final String userArn // Registered user arn to use for embedding. Refer to Get Embed Url section in developer portal to find how to get user arn for a QuickSight user.
            ) throws Exception {
        final RegisteredUserEmbeddingExperienceConfiguration experienceConfiguration = new RegisteredUserEmbeddingExperienceConfiguration()
                .withQSearchBar(new RegisteredUserQSearchBarEmbeddingConfiguration().withInitialTopicId(topicId));
        final GenerateEmbedUrlForRegisteredUserRequest generateEmbedUrlForRegisteredUserRequest = new GenerateEmbedUrlForRegisteredUserRequest();
        generateEmbedUrlForRegisteredUserRequest.setAwsAccountId(accountId);
        generateEmbedUrlForRegisteredUserRequest.setUserArn(userArn);
        generateEmbedUrlForRegisteredUserRequest.setAllowedDomains(allowedDomains);
        generateEmbedUrlForRegisteredUserRequest.setExperienceConfiguration(QSearchBar);
        final GenerateEmbedUrlForRegisteredUserResult generateEmbedUrlForRegisteredUserResult = quickSightClient.generateEmbedUrlForRegisteredUser(generateEmbedUrlForRegisteredUserRequest);
        return generateEmbedUrlForRegisteredUserResult.getEmbedUrl();
            }
        }
```
```
global.fetch = require('node-fetch');
const AWS = require('aws-sdk');
function generateEmbedUrlForRegisteredUser(
    accountId,
    topicId, // Topic ID to embed
    openIdToken, // Cognito-based token
    userArn, // registered user arn
    roleArn, // IAM user role to use for embedding
    sessionName, // Session name for the roleArn assume role
    allowedDomains, // Runtime allowed domain for embedding
    getEmbedUrlCallback, // GetEmbedUrl success callback method
    errorCallback // GetEmbedUrl error callback method
    ) {
    const stsClient = new AWS.STS();
    let stsParams = {
        RoleSessionName: sessionName,
        WebIdentityToken: openIdToken,
        RoleArn: roleArn
        }
    
    stsClient.assumeRoleWithWebIdentity(stsParams, function(err, data) {
        if (err) {
            console.log('Error assuming role');
            console.log(err, err.stack);
            errorCallback(err);
        } else {
            const getQSearchBarParams = {
        "AwsAccountId": accountId,
                "ExperienceConfiguration": {
                    "QSearchBar": {
                        "InitialTopicId": topicId
                    }
                },
                "UserArn": userArn,
        "AllowedDomains": allowedDomains,
        "SessionLifetimeInMinutes": 600
    };
            const quicksightGetQSearchBar = new AWS.QuickSight({
        region: process.env.AWS_REGION,
                credentials: {
                    accessKeyId: data.Credentials.AccessKeyId,
                    secretAccessKey: data.Credentials.SecretAccessKey,
                    sessionToken: data.Credentials.SessionToken,
                    expiration: data.Credentials.Expiration
                }
    });
            quicksightGetQSearchBar.generateEmbedUrlForRegisteredUser(getQSearchBarParams, function(err, data) {
        if (err) {
            console.log(err, err.stack);
            errorCallback(err);
        } else {
            const result = {
                "statusCode": 200,
                "headers": {
                            "Access-Control-Allow-Origin": "*", // Use your website domain to secure access to GetEmbedUrl API
                    "Access-Control-Allow-Headers": "Content-Type"
                },
                "body": JSON.stringify(data),
                "isBase64Encoded": false
            }
                    getEmbedUrlCallback(result);
                }
            });
        }
    });
}
```
```
import json
import boto3
from botocore.exceptions import ClientError
sts = boto3.client('sts')
# Function to generate embedded URL  
# accountId: AWS account ID
# topicId: Topic ID to embed
# userArn: arn of registered user
# allowedDomains: Runtime allowed domain for embedding
# roleArn: IAM user role to use for embedding
# sessionName: session name for the roleArn assume role
def getEmbeddingURL(accountId, topicId, userArn, allowedDomains, roleArn, sessionName):
    try:
        assumedRole = sts.assume_role(
            RoleArn = roleArn,
            RoleSessionName = sessionName,
        )
    except ClientError as e:
        return "Error assuming role: " + str(e)
    else: 
        assumedRoleSession = boto3.Session(
            aws_access_key_id = assumedRole['Credentials']['AccessKeyId'],
            aws_secret_access_key = assumedRole['Credentials']['SecretAccessKey'],
            aws_session_token = assumedRole['Credentials']['SessionToken'],
        )
        try:
            quicksightClient = assumedRoleSession.client('quicksight', region_name='us-west-2')
            response = quicksightClient.generate_embed_url_for_registered_user(
                AwsAccountId=accountId,
                ExperienceConfiguration = {
                    "QSearchBar": {
                        "InitialTopicId": topicId
                    }
                },
                UserArn = userArn,
                AllowedDomains = allowedDomains,
                SessionLifetimeInMinutes = 600
            )
            
            return {
                'statusCode': 200,
                'headers': {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type"},
                'body': json.dumps(response),
                'isBase64Encoded':  bool('false')
            }
        except ClientError as e:
            return "Error generating embedding url: " + str(e)
```
The following example shows the JavaScript (Node.js) that you can use on the app server to generate the URL for the embedded dashboard. You can use this URL in your website or app to display the dashboard.

###### Example

```
const AWS = require('aws-sdk');
const https = require('https');
var quicksightClient = new AWS.Service({
    apiConfig: require('./quicksight-2018-04-01.min.json'),
    region: 'us-east-1',
});
quicksightClient.generateEmbedUrlForRegisteredUser({
    'AwsAccountId': '111122223333',
    'ExperienceConfiguration': { 
        'QSearchBar': {
            'InitialTopicId': 'U4zJMVZ2n2stZflc8Ou3iKySEb3BEV6f'
        }
    },
    'UserArn': 'REGISTERED_USER_ARN',
    'AllowedDomains': allowedDomains,
    'SessionLifetimeInMinutes': 100
}, function(err, data) {
    console.log('Errors: ');
    console.log(err);
    console.log('Response: ');
    console.log(data);
});
```
###### Example

```
//The URL returned is over 900 characters. For this example, we've shortened the string for
//readability and added ellipsis to indicate that it's incomplete.
    { 
        Status: 200,
        EmbedUrl: "https://quicksightdomain/embed/12345/dashboards/67890/sheets/12345/visuals/67890...",
        RequestId: '7bee030e-f191-45c4-97fe-d9faf0e03713' 
    }
```
The following example shows the .NET/C# code that you can use on the app server to generate the URL for the embedded Q search bar. You can use this URL in your website or app to display the Q search bar.

###### Example

```
using System;
using Amazon.QuickSight;
using Amazon.QuickSight.Model;
namespace GenerateDashboardEmbedUrlForRegisteredUser
{
    class Program
    {
        static void Main(string[] args)
        {
            var quicksightClient = new AmazonQuickSightClient(
                AccessKey,
                SecretAccessKey,
                SessionToken,
                Amazon.RegionEndpoint.USEast1);
            try
            {
                RegisteredUserQSearchBarEmbeddingConfiguration registeredUserQSearchBarEmbeddingConfiguration
                    = new RegisteredUserQSearchBarEmbeddingConfiguration
                    {
                        InitialTopicId = "U4zJMVZ2n2stZflc8Ou3iKySEb3BEV6f"
                    };
                RegisteredUserEmbeddingExperienceConfiguration registeredUserEmbeddingExperienceConfiguration
                    = new RegisteredUserEmbeddingExperienceConfiguration
                    {
                        QSearchBar = registeredUserQSearchBarEmbeddingConfiguration
                    }; 
                
                Console.WriteLine(
                    quicksightClient.GenerateEmbedUrlForRegisteredUserAsync(new GenerateEmbedUrlForRegisteredUserRequest
                    {
                        AwsAccountId = "111122223333",
                        ExperienceConfiguration = registeredUserEmbeddingExperienceConfiguration,
                        UserArn = "REGISTERED_USER_ARN",
                        AllowedDomains = allowedDomains,
                        SessionLifetimeInMinutes = 100
                    }).Result.EmbedUrl
                );
            } catch (Exception ex) {
                Console.WriteLine(ex.Message);
            }
        }
    }
}
```
To assume the role, choose one of the following AWS Security Token Service (AWS STS) API operations:

- 
                            [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)– Use this operation when you are using an IAM identity to assume the role.
- 
                            [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)– Use this operation when you are using a web identity provider to authenticate your user.
- 
                            [AssumeRoleWithSaml](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)– Use this operation when you are using SAML to authenticate your users.

The following example shows the CLI command to set the IAM role. The
                        role needs to have permissions enabled for
                            `quicksight:GenerateEmbedUrlForRegisteredUser`. If you are
                        taking a just-in-time approach to add users when they use a topic in the Q
                        search bar, the role also needs permissions enabled for
                            `quicksight:RegisterUser`.

`aws sts assume-role \ --role-arn "``arn:aws:iam::111122223333:role/embedding_quicksight_q_search_bar_role`" \ --role-session-name`john.doe@example.com`

The `assume-role` operation returns three output parameters:
                        the access key, the secret key, and the session token. 

###### Note

If you get an `ExpiredToken` error when calling the
                                `AssumeRole` operation, this is probably because the
                            previous `SESSION TOKEN` is still in the environment
                            variables. Clear this by setting the following variables:

- 
                                *AWS_ACCESS_KEY_ID*
- 
                                *AWS_SECRET_ACCESS_KEY*
- 
                                *AWS_SESSION_TOKEN*

The following example shows how to set these three parameters in the CLI.
                        For a Microsoft Windows machine, use `set` instead of
                            `export`.

`export AWS_ACCESS_KEY_ID = "``access_key_from_assume_role`" export AWS_SECRET_ACCESS_KEY = "`secret_key_from_assume_role`" export AWS_SESSION_TOKEN = "`session_token_from_assume_role`"

Running these commands sets the role session ID of the user visiting your
                        website to
                            `embedding_quicksight_q_search_bar_role/john.doe@example.com`.
                        The role session ID is made up of the role name from `role-arn`
                        and the `role-session-name` value. Using the unique role session
                        ID for each user ensures that appropriate permissions are set for each user.
                        It also prevents any throttling of user access. *Throttling* is a security feature that prevents the same user
                        from accessing Amazon Quick Sight from multiple locations. 

The role session ID also becomes the user name in Amazon Quick Sight. You can use this pattern to provision your users in Amazon Quick Sight ahead of time, or to provision them the first time that they access the Q search bar.

The following example shows the CLI command that you can use to provision
                        a user. For more information about [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html), [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html), and other Amazon Quick Sight API operations, see
                        the [Amazon Quick Sight API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).

`aws quicksight register-user \ --aws-account-id``111122223333`\ --namespace default \ --identity-type`IAM`\ --iam-arn "`arn:aws:iam::111122223333:role/embedding_quicksight_q_search_bar_role`" \ --user-role`READER`\ --user-name`jhnd`\ --session-name "`john.doe@example.com`" \ --email`john.doe@example.com`\ --region`us-east-1`\ --custom-permissions-name`TeamA1`

If the user is authenticated through Microsoft AD, you don't need to use
                            `RegisterUser` to set them up. Instead, they should be
                        automatically subscribed the first time that they access Amazon Quick Sight.
                        For Microsoft AD users, you can use `DescribeUser` to get the
                        user Amazon Resource Name (ARN).

The first time a user accesses Amazon Quick Sight, you can also add this user to the group that the dashboard is shared with. The following example shows the CLI command to add a user to a group.

`aws quicksight create-group-membership \ --aws-account-id=``111122223333`\ --namespace=default \ --group-name=`financeusers`\ --member-name="`embedding_quicksight_q_search_bar_role/john.doe@example.com`"

You now have a user of your app who is also a user of Amazon Quick Sight, and who has access to the dashboard.

Finally, to get a signed URL for the dashboard, call
                            `generate-embed-url-for-registered-user` from the app server.
                        This returns the embeddable dashboard URL. The following example shows how
                        to generate the URL for an embedded dashboard using a server-side call for
                        users authenticated through AWS Managed Microsoft AD or single sign-on (IAM Identity Center).

`aws quicksight generate-embed-url-for-registered-user \ --aws-account-id``111122223333`\ --session-lifetime-in-minutes`600`\ --user-arn`arn:aws:quicksight:us-east-1:111122223333:user/default/embedding_quicksight_q_search_bar_role/embeddingsession`--allowed-domains '["`domain1`","`domain2`"]' \ --experience-configuration QSearchBar={InitialTopicId=`U4zJMVZ2n2stZflc8Ou3iKySEb3BEV6f`}

For more information about using this operation, see [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html). You can
                        use this and other API operations in your own code.

## Step 3: Embed the Q search bar URL

            ###### Note

The embedded Amazon Quick Sight Q search bar provides the classic
                    Amazon Quick Sight Q&A experience. Amazon Quick Sight integrates with
                    Amazon Q Business to launch a new Generative Q&A experience. Developers are recommended to use the new
                    Generative Q&A experience. For more information on the embedded Generative Q&A experience, see [Embedding the Amazon Q in Amazon Quick Sight Generative Q&A experience](https://docs.aws.amazon.com/quicksight/latest/user/embedding-gen-bi.html).

In the following section, you can find how to embed the Q search bar URL from step
                3 in your website or application page. You do this with the [Amazon Quick Sight embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) (JavaScript). With the SDK, you can do
                the following: 

- 
                    Place the Q search bar on an HTML page. 
- 
                    Pass parameters into the Q search bar. 
- 
                    Handle error states with messages that are customized to your application. 

To generate the URL that you can embed in your app, call the
                    `GenerateEmbedUrlForRegisteredUser` API operation. This URL is valid
                for 5 minutes, and the resulting session is valid for up to 10 hours. The API
                operation provides the URL with an `auth_code` value that enables a
                single-sign on session. 

The following shows an example response from
                    `generate-embed-url-for-registered-user`.

`//The URL returned is over 900 characters. For this example, we've shortened the string for //readability and added ellipsis to indicate that it's incomplete. { "Status": "200", "EmbedUrl": "https://``quicksightdomain`/embedding/12345/q/search...", "RequestId": "7bee030e-f191-45c4-97fe-d9faf0e03713" }

Embed the Q search bar in your webpage by using the [Amazon Quick Sight embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) or by adding this URL into an iframe.
                If you set a fixed height and width number (in pixels), Amazon Quick Sight uses those
                and doesn't change your visual as your window resizes. If you set a relative
                percent height and width, Amazon Quick Sight provides a responsive layout that is
                modified as your window size changes. 

To do this, make sure that the domain to host the embedded Q search bar is on the
                    *allow list*, the list of approved domains for
                your Amazon Quick Sight subscription. This requirement protects your data by keeping
                unapproved domains from hosting embedded dashboards. For more information about
                adding domains for an embedded Q search bar, see [Managing domains and embedding](https://docs.aws.amazon.com/quicksight/latest/user/manage-qs-domains-and-embedding.html).

When you use the Amazon Quick Sight Embedding SDK, the Q search bar on your page is dynamically resized based on the state. By using the Amazon Quick Sight Embedding SDK, you can also control parameters within the Q search bar and receive callbacks in terms of page load completion and errors.

The following example shows how to use the generated URL. This code is generated on your app server.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Q Search Bar Embedding Example</title>
        <script src="https://unpkg.com/amazon-quicksight-embedding-sdk@2.0.0/dist/quicksight-embedding-js-sdk.min.js"></script>
        <script type="text/javascript">
            const embedQSearchBar = async() => {    
                const {
                    createEmbeddingContext,
                } = QuickSightEmbedding;
                const embeddingContext = await createEmbeddingContext({
                    onChange: (changeEvent, metadata) => {
                        console.log('Context received a change', changeEvent, metadata);
                    },
                });
                const frameOptions = {
                    url: "<YOUR_EMBED_URL>", // replace this value with the url generated via embedding API
                    container: '#experience-container',
                    height: "700px",
                    width: "1000px",
                    onChange: (changeEvent, metadata) => {
                        switch (changeEvent.eventName) {
                            case 'FRAME_MOUNTED': {
                                console.log("Do something when the experience frame is mounted.");
                                break;
                            }
                            case 'FRAME_LOADED': {
                                console.log("Do something when the experience frame is loaded.");
                                break;
                            }
                        }
                    },
                };
                const contentOptions = {
                    hideTopicName: false, 
                    theme: '<YOUR_THEME_ID>',
                    allowTopicSelection: true,
                    onMessage: async (messageEvent, experienceMetadata) => {
                        switch (messageEvent.eventName) {
                            case 'Q_SEARCH_OPENED': {
                                console.log("Do something when Q Search content expanded");
                                break;
                            }
                            case 'Q_SEARCH_CLOSED': {
                                console.log("Do something when Q Search content collapsed");
                                break;
                            }
                            case 'Q_SEARCH_SIZE_CHANGED': {
                                console.log("Do something when Q Search size changed");
                                break;
                            }
                            case 'CONTENT_LOADED': {
                                console.log("Do something when the Q Search is loaded.");
                                break;
                            }
                            case 'ERROR_OCCURRED': {
                                console.log("Do something when the Q Search fails loading.");
                                break;
                            }
                        }
                    }
                };
                const embeddedDashboardExperience = await embeddingContext.embedQSearchBar(frameOptions, contentOptions);
            };
        </script>
    </head>
    <body onload="embedQSearchBar()">
        <div id="experience-container"></div>
    </body>
</html>
```
```
<!DOCTYPE html>
<html>
    <head>
        <title>QuickSight Q Search Bar Embedding</title>
        <script src="https://unpkg.com/amazon-quicksight-embedding-sdk@1.18.0/dist/quicksight-embedding-js-sdk.min.js"></script>
        <script type="text/javascript">
            var session
            function onError(payload) {
                console.log("Do something when the session fails loading");
            }
            function onOpen() {
                console.log("Do something when the Q search bar opens");
            }
            function onClose() {
                console.log("Do something when the Q search bar closes");
            }
            function embedQSearchBar() {
                var containerDiv = document.getElementById("embeddingContainer");
                var options = {
                    url: "https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/dashboardId?isauthcode=true&identityprovider=quicksight&code=authcode", // replace this dummy url with the one generated via embedding API
                    container: containerDiv,
                    width: "
```
`1000px`",
                    locale: "`en-US`",
                    qSearchBarOptions: {
                        expandCallback: onOpen,
                        collapseCallback: onClose,
                        iconDisabled: false,
                        topicNameDisabled: false, 
                        themeId: '`bdb844d0-0fe9-4d9d-b520-0fe602d93639`',
                        allowTopicSelection: true
                    }
                };
                session = QuickSightEmbedding.embedQSearchBar(options);
                session.on("error", onError);
            }
            function onCountryChange(obj) {
                session.setParameters({country: obj.value});
            }
        </script>
    </head>
    <body onload="embedQSearchBar()">
        <div id="embeddingContainer"></div>
    </body>
</html>For this example to work, make sure to use the Amazon Quick Sight Embedding SDK to load the embedded dashboard on your website using JavaScript. To get your copy, do one of the following:

- 
                    Download the [Amazon Quick Sight embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk#step-3-create-the-quicksight-session-object)from GitHub. This repository is maintained by a group of Amazon Quick Sight developers.
- 
                    Download the latest embedding SDK version from [https://www.npmjs.com/package/amazon-quicksight-embedding-sdk](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk).
- 
                    If you use `npm`for JavaScript dependencies, download and install it by running the following command.`npm install amazon-quicksight-embedding-sdk`

## Optional Amazon Quick Sight Q search bar embedding functionalities

            ###### Note

The embedded Amazon Quick Sight Q search bar provides the classic
                    Amazon Quick Sight Q&A experience. Amazon Quick Sight integrates with
                    Amazon Q Business to launch a new Generative Q&A experience. Developers are recommended to use the new
                    Generative Q&A experience. For more information on the embedded Generative Q&A experience, see [Embedding the Amazon Q in Amazon Quick Sight Generative Q&A experience](https://docs.aws.amazon.com/quicksight/latest/user/embedding-gen-bi.html).

The following optional functionalities are available for the embedded Q search bar using the embedding SDK.

### Invoke Q search bar actions

The following options are only supported for Q search bar embedding.

- 
                        Set a Q search bar question — This feature sends a question to the Q search bar and immediately queries the question. It also automatically opens the Q popover. `qBar.setQBarQuestion('``show me monthly revenue`');
- 
                        Close the Q popover — This feature closes the Q popover and returns the iframe to the original Q search bar size. `qBar.closeQPopover();`

For more information, see the [Amazon Quick Sight embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk).