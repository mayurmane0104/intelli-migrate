# Embedding Amazon Quick Sight dashboards for registered users - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-dashboards-for-authenticated-users.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-dashboards-for-authenticated-users.html)

---

###### Important

Amazon Quick Sight has new API operations for embedding analytics:
                    `GenerateEmbedUrlForAnonymousUser` and
                    `GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
                    `GetSessionEmbedUrl` API operations to embed dashboards and the
                Amazon Quick Sight console, but they don't contain the latest embedding capabilities.
                For more information about embedding using the old API operations, see [Embedding analytics using the
                        GetDashboardEmbedURL and GetSessionEmbedURL
                    API operations](https://docs.aws.amazon.com/quicksight/latest/user/embedded-analytics-deprecated.html).

| Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

In the following sections, you can find detailed information about how to set up embedded Amazon Quick Sight dashboards for registered users of Amazon Quick Sight.

###### Topics

## Step 1: Set up permissions

            In the following section, you can find out how to set up permissions for the backend application or web server. This task requires administrative access to IAM.

Each user who accesses a dashboard assumes a role that gives them
                Amazon Quick Sight access and permissions to the dashboard. To make this possible,
                create an IAM role in your AWS account. Associate an IAM policy with the role
                to provide permissions to any user who assumes it. The IAM role needs to provide
                permissions to retrieve embedding URLs for a specific user pool. With the help of
                the wildcard character ***, you can grant the permissions to
                generate a URL for all users in a specific namespace, or for a subset of users in
                specific namespaces. For this, you add
                    `quicksight:GenerateEmbedUrlForRegisteredUser`.

You can create a condition in your IAM policy that limits the domains that
                developers can list in the `AllowedDomains` parameter of a
                    `GenerateEmbedUrlForRegisteredUser` API operation. The
                    `AllowedDomains` parameter is an optional parameter. It grants you as
                a developer the option to override the static domains that are configured in the
                    **Manage Amazon Quick Sight** menu. Instead, you can list up to
                three domains or subdomains that can access the generated URL. This URL is then
                embedded in the website that you create. Only the domains that are listed in the
                parameter can access the embedded visual. Without this condition, you can list any
                domain on the internet in the `AllowedDomains` parameter. 

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

Additionally, if you are creating first-time users who will be Amazon Quick Sight
                readers, make sure to add the `quicksight:RegisterUser` permission in the
                policy.

The following sample policy provides permission to retrieve an embedding URL for first-time users who are to be Amazon Quick Sight readers.

Finally, your application's IAM identity must have a trust policy associated with it to allow access to the role that you just created. This means that when a user accesses your application, your application can assume the role on the user's behalf and provision the user in Amazon Quick Sight. The following example shows a sample trust policy.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Sid": "AllowLambdaFunctionsToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "lambda.amazonaws.com" }, "Action": "sts:AssumeRole" }, { "Sid": "AllowEC2InstancesToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }`

For more information regarding trust policies for OpenID Connect or SAML
                authentication, see the following sections of the *IAM User
                    Guide: *

## Step 2: Generate the URL with the authentication code attached

            In the following section, you can find out how to authenticate your user and get the embeddable dashboard URL on your application server. If you plan to embed dashboards for IAM or Amazon Quick Sight identity types, share the dashboard with the users.

When a user accesses your app, the app assumes the IAM role on the user's behalf. Then it adds the user to Amazon Quick Sight, if that user doesn't already exist. Next, it passes an identifier as the unique role session ID.

Performing these steps ensures that each viewer of the dashboard is uniquely provisioned in Amazon Quick Sight. It also enforces per-user settings, such as the row-level security and dynamic defaults for parameters.

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
    import com.amazonaws.services.quicksight.model.RegisteredUserDashboardEmbeddingConfiguration;
    /**
    * Class to call QuickSight AWS SDK to get url for dashboard embedding.
    */
    public class GetQuicksightEmbedUrlRegisteredUserDashboardEmbedding {
        private final AmazonQuickSight quickSightClient;
        public GetQuicksightEmbedUrlRegisteredUserDashboardEmbedding() {
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
                        public void refresh() {}
                        }
                    )
                    .build();
        }
        public String getQuicksightEmbedUrl(
                final String accountId, // AWS Account ID
                final String dashboardId, // Dashboard ID to embed
                final List<String> allowedDomains, // Runtime allowed domain for embedding
                final String userArn // Registered user arn to use for embedding. Refer to Get Embed Url section in developer portal to find out how to get user arn for a QuickSight user.
        ) throws Exception {
            final RegisteredUserEmbeddingExperienceConfiguration experienceConfiguration = new RegisteredUserEmbeddingExperienceConfiguration()
                    .withDashboard(new RegisteredUserDashboardEmbeddingConfiguration().withInitialDashboardId(dashboardId));
            final GenerateEmbedUrlForRegisteredUserRequest generateEmbedUrlForRegisteredUserRequest = new GenerateEmbedUrlForRegisteredUserRequest();
            generateEmbedUrlForRegisteredUserRequest.setAwsAccountId(accountId);
            generateEmbedUrlForRegisteredUserRequest.setUserArn(userArn);
            generateEmbedUrlForRegisteredUserRequest.setAllowedDomains(allowedDomains);
            generateEmbedUrlForRegisteredUserRequest.setExperienceConfiguration(experienceConfiguration);
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
        dashboardId,
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
                const getDashboardParams = {
                    "AwsAccountId": accountId,
                    "ExperienceConfiguration": {
                        "Dashboard": {
                            "InitialDashboardId": dashboardId
                        }
                    },
                    "UserArn": userArn,
                    "AllowedDomains": allowedDomains,
                    "SessionLifetimeInMinutes": 600
                };
                const quicksightClient = new AWS.QuickSight({
                    region: process.env.AWS_REGION,
                    credentials: {
                        accessKeyId: data.Credentials.AccessKeyId,
                        secretAccessKey: data.Credentials.SecretAccessKey,
                        sessionToken: data.Credentials.SessionToken,
                        expiration: data.Credentials.Expiration
                    }
                });
                quicksightClient.generateEmbedUrlForRegisteredUser(getDashboardParams, function(err, data) {
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
# dashboardId: Dashboard ID to embed
# userArn: arn of registered user
# allowedDomains: Runtime allowed domain for embedding
# roleArn: IAM user role to use for embedding
# sessionName: session name for the roleArn assume role
def getEmbeddingURL(accountId, dashboardId, userArn, allowedDomains, roleArn, sessionName):
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
                    "Dashboard": {
                        "InitialDashboardId": dashboardId
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
            'Dashboard': {
                'InitialDashboardId': '1c1fe111-e2d2-3b30-44ef-a0e111111cde'
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

`//The URL returned is over 900 characters. For this example, we've shortened the string for //readability and added ellipsis to indicate that it's incomplete. { Status: 200, EmbedUrl: 'https://``quicksightdomain`/embed/12345/dashboards/67890...' RequestId: '7bee030e-f191-45c4-97fe-d9faf0e03713' }

The following example shows the .NET/C# code that you can use on the app server to generate the URL for the embedded dashboard. You can use this URL in your website or app to display the dashboard.

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
                    RegisteredUserDashboardEmbeddingConfiguration registeredUserDashboardEmbeddingConfiguration
                        = new RegisteredUserDashboardEmbeddingConfiguration
                        {
                            InitialDashboardId = "dashboardId"
                        };
                    RegisteredUserEmbeddingExperienceConfiguration registeredUserEmbeddingExperienceConfiguration
                        = new RegisteredUserEmbeddingExperienceConfiguration
                        {
                            Dashboard = registeredUserDashboardEmbeddingConfiguration
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
                            [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)– Use this operation when you're using an IAM identity to assume the role.
- 
                            [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)– Use this operation when you're using a web identity provider to authenticate your user.
- 
                            [AssumeRoleWithSaml](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)– Use this operation when you're using SAML to authenticate your users.

The following example shows the CLI command to set the IAM role. The
                        role needs to have permissions enabled for
                            `quicksight:GenerateEmbedUrlForRegisteredUser`. If you are
                        taking a just-in-time approach to add users when they first open a
                        dashboard, the role also needs permissions enabled for
                            `quicksight:RegisterUser`.

`aws sts assume-role \ --role-arn "``arn:aws:iam::111122223333:role/embedding_quicksight_dashboard_role`" \ --role-session-name`john.doe@example.com`

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
                        If you're using a Microsoft Windows machine, use `set` instead of
                            `export`.

`export AWS_ACCESS_KEY_ID = "``access_key_from_assume_role`" export AWS_SECRET_ACCESS_KEY = "`secret_key_from_assume_role`" export AWS_SESSION_TOKEN = "`session_token_from_assume_role`"

Running these commands sets the role session ID of the user visiting your
                        website to
                            `embedding_quicksight_dashboard_role/john.doe@example.com`.
                        The role session ID is made up of the role name from `role-arn`
                        and the `role-session-name` value. Using the unique role session
                        ID for each user ensures that appropriate permissions are set for each user.
                        It also prevents any throttling of user access. *Throttling* is a security feature that prevents the same user
                        from accessing Amazon Quick Sight from multiple locations. 

The role session ID also becomes the user name in Amazon Quick Sight. You can use this pattern to provision your users in Amazon Quick Sight ahead of time, or to provision them the first time they access the dashboard.

The following example shows the CLI command that you can use to provision
                        a user. For more information about [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html), [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html), and other Amazon Quick Sight API operations, see
                        the [Amazon Quick Sight API Reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).

`aws quicksight register-user \ --aws-account-id``111122223333`\ --namespace`default`\ --identity-type`IAM`\ --iam-arn "`arn:aws:iam::111122223333:role/embedding_quicksight_dashboard_role`" \ --user-role`READER`\ --user-name`jhnd`\ --session-name "`john.doe@example.com`" \ --email`john.doe@example.com`\ --region`us-east-1`\ --custom-permissions-name`TeamA1`

If your user is authenticated through Microsoft AD, you don't need to use
                            `RegisterUser` to set them up. Instead, they should be
                        automatically subscribed the first time they access Amazon Quick Sight. For
                        Microsoft AD users, you can use `DescribeUser` to get the user
                        ARN.

The first time a user accesses Amazon Quick Sight, you can also add this user to the group that the dashboard is shared with. The following example shows the CLI command to add a user to a group.

`aws quicksight create-group-membership \ --aws-account-id=``111122223333`\ --namespace=default \ --group-name=`financeusers`\ --member-name="`embedding_quicksight_dashboard_role/john.doe@example.com`"

You now have a user of your app who is also a user of Amazon Quick Sight, and who has access to the dashboard.

Finally, to get a signed URL for the dashboard, call
                            `generate-embed-url-for-registered-user` from the app server.
                        This returns the embeddable dashboard URL. The following example shows how
                        to generate the URL for an embedded dashboard using a server-side call for
                        users authenticated through AWS Managed Microsoft AD or single sign-on (IAM Identity Center).

`aws quicksight generate-embed-url-for-registered-user \ --aws-account-id``111122223333`\ --session-lifetime-in-minutes`600`\ --user-arn`arn:aws:quicksight:us-east-1:111122223333:user/default/embedding_quicksight_visual_role/embeddingsession`\ --allowed-domains '["`domain1`","`domain2`"]' \ --experience-configuration Dashboard={InitialDashboardId=`1a1ac2b2-3fc3-4b44-5e5d-c6db6778df89`}

For more information about using this operation, see [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html). You can
                        use this and other API operations in your own code.

## Step 3: Embed the dashboard URL

            In the following section, you can find out how you can use the [Amazon Quick Sight Embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) (JavaScript) to embed the dashboard URL
                from step 3 in your website or application page. With the SDK, you can do the
                following: 

- 
                    Place the dashboard on an HTML page. 
- 
                    Pass parameters into the dashboard. 
- 
                    Handle error states with messages that are customized to your application. 

Call the `GenerateEmbedUrlForRegisteredUser` API operation to generate
                the URL that you can embed in your app. This URL is valid for 5 minutes, and the
                resulting session is valid for up to 10 hours. The API operation provides the URL
                with an `auth_code` that enables a single-sign on session. 

The following shows an example response from
                    `generate-embed-url-for-registered-user`.

`//The URL returned is over 900 characters. For this example, we've shortened the string for //readability and added ellipsis to indicate that it's incomplete. { "Status": "200", "EmbedUrl": "https://``quicksightdomain`/embed/12345/dashboards/67890..", "RequestId": "7bee030e-f191-45c4-97fe-d9faf0e03713" }

Embed this dashboard in your webpage by using the [Amazon Quick Sight Embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) or by adding this URL into an iframe.
                If you set a fixed height and width number (in pixels), Amazon Quick Sight uses those
                and doesn't change your visual as your window resizes. If you set a relative
                percent height and width, Amazon Quick Sight provides a responsive layout that is
                modified as your window size changes. By using the Amazon Quick Sight Embedding SDK,
                you can also control parameters within the dashboard and receive callbacks in terms
                of page load completion and errors. 

The domain that is going to host embedded dashboards must be on the *allow list*, the list of approved domains for your
                    Quick subscription. This requirement protects your data by keeping
                unapproved domains from hosting embedded dashboards. For more information about
                adding domains for embedded dashboards, see [Allow
                    listing domains at runtime with the Amazon Quick Sight API](https://docs.aws.amazon.com/quicksight/latest/user/embedding-run-time.html).

The following example shows how to use the generated URL. This code is generated on your app server.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Dashboard Embedding Example</title>
        <script src="https://unpkg.com/amazon-quicksight-embedding-sdk@2.0.0/dist/quicksight-embedding-js-sdk.min.js"></script>
        <script type="text/javascript">
            const embedDashboard = async() => {
                const {
                    createEmbeddingContext,
                } = QuickSightEmbedding;
                const embeddingContext = await createEmbeddingContext({
                    onChange: (changeEvent, metadata) => {
                        console.log('Context received a change', changeEvent, metadata);
                    },
                });
                const frameOptions = {
                    url: '<YOUR_EMBED_URL>',
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
                    parameters: [
                        {
                            Name: 'country',
                            Values: [
                                'United States'
                            ],
                        },
                        {
                            Name: 'states',
                            Values: [
                                'California',
                                'Washington'
                            ]
                        }
                    ],
                    locale: "en-US",
                    sheetOptions: {
                        initialSheetId: '<YOUR_SHEETID>',
                        singleSheet: false,                        
                        emitSizeChangedEventOnSheetChange: false,
                    },
                    toolbarOptions: {
                        export: false,
                        undoRedo: false,
                        reset: false
                    },
                    attributionOptions: {
                        overlayContent: false,
                    },
                    onMessage: async (messageEvent, experienceMetadata) => {
                        switch (messageEvent.eventName) {
                            case 'CONTENT_LOADED': {
                                console.log("All visuals are loaded. The title of the document:", messageEvent.message.title);
                                break;
                            }
                            case 'ERROR_OCCURRED': {
                                console.log("Error occurred while rendering the experience. Error code:", messageEvent.message.errorCode);
                                break;
                            }
                            case 'PARAMETERS_CHANGED': {
                                console.log("Parameters changed. Changed parameters:", messageEvent.message.changedParameters);
                                break;
                            }
                            case 'SELECTED_SHEET_CHANGED': {
                                console.log("Selected sheet changed. Selected sheet:", messageEvent.message.selectedSheet);
                                break;
                            }
                            case 'SIZE_CHANGED': {
                                console.log("Size changed. New dimensions:", messageEvent.message);
                                break;
                            }
                            case 'MODAL_OPENED': {
                                window.scrollTo({
                                    top: 0 // iframe top position
                                });
                                break;
                            }
                        }
                    },
                };
                const embeddedDashboardExperience = await embeddingContext.embedDashboard(frameOptions, contentOptions);
                const selectCountryElement = document.getElementById('country');
                selectCountryElement.addEventListener('change', (event) => {
                    embeddedDashboardExperience.setParameters([
                        {
                            Name: 'country',
                            Values: event.target.value
                        }
                    ]);
                });
            };
        </script>
    </head>
    <body onload="embedDashboard()">
        <span>
            <label for="country">Country</label>
            <select id="country" name="country">
                <option value="United States">United States</option>
                <option value="Mexico">Mexico</option>
                <option value="Canada">Canada</option>
            </select>
        </span>
        <div id="experience-container"></div>
    </body>
</html>
```
```
<!DOCTYPE html>
<html>
    <head>
        <title>Basic Embed</title>
        <script src="https://unpkg.com/amazon-quicksight-embedding-sdk@1.0.15/dist/quicksight-embedding-js-sdk.min.js"></script>
        <script type="text/javascript">
            var dashboard
            function onDashboardLoad(payload) {
                console.log("Do something when the dashboard is fully loaded.");
            }
            function onError(payload) {
                console.log("Do something when the dashboard fails loading");
            }
            function embedDashboard() {
                var containerDiv = document.getElementById("embeddingContainer");
                var options = {
                    // replace this dummy url with the one generated via embedding API
                    url: "https://us-east-1.quicksight.aws.amazon.com/sn/dashboards/dashboardId?isauthcode=true&identityprovider=quicksight&code=authcode",
                    container: containerDiv,
                    parameters: {
                        country: "United States"
                    },
                    scrolling: "no",
                    height: "700px",
                    width: "1000px",
                    locale: "en-US",
                    footerPaddingEnabled: true
                };
                dashboard = QuickSightEmbedding.embedDashboard(options);
                dashboard.on("error", onError);
                dashboard.on("load", onDashboardLoad);
            }
            function onCountryChange(obj) {
                dashboard.setParameters({country: obj.value});
            }
        </script>
    </head>
    <body onload="embedDashboard()">
        <span>
            <label for="country">Country</label>
            <select id="country" name="country" onchange="onCountryChange(this)">
                <option value="United States">United States</option>
                <option value="Mexico">Mexico</option>
                <option value="Canada">Canada</option>
            </select>
        </span>
        <div id="embeddingContainer"></div>
    </body>
</html>
```
For this example to work, make sure to use the Amazon Quick Sight Embedding SDK to load the embedded dashboard on your website using JavaScript. To get your copy, do one of the following:

- 
                    Download the [Amazon Quick Sight Embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk#step-3-create-the-quicksight-session-object)from GitHub. This repository is maintained by a group of Amazon Quick Sight developers.
- 
                    Download the latest embedding SDK version from [https://www.npmjs.com/package/amazon-quicksight-embedding-sdk](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk).
- 
                    If you use `npm`for JavaScript dependencies, download and install it by running the following command.`npm install amazon-quicksight-embedding-sdk`