# Embedding Amazon Quick Sight dashboards for anonymous (unregistered) users - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-dashboards-for-everyone.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-dashboards-for-everyone.html)

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

In the following sections, you can find detailed information about how to set up embedded Amazon Quick Sight dashboards for anonymous (unregistered) users.

###### Topics

## Step 1: Set up permissions

            | Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

In the following section, you can find out how to set up permissions for the backend application or web server. This task requires administrative access to IAM.

Each user who accesses a dashboard assumes a role that gives them Amazon Quick Sight access and permissions to the dashboard. To make this possible, create an IAM role in your AWS account. Associate an IAM policy with the role to provide permissions to any user who assumes it.

You can create a condition in your IAM policy that limits the domains that
                developers can list in the `AllowedDomains` parameter of a
                    `GenerateEmbedUrlForAnonymousUser` API operation. The
                    `AllowedDomains` parameter is an optional parameter. It grants you as
                a developer the option to override the static domains that are configured in the
                    **Manage Amazon Quick Sight** menu. Instead, you can list up to
                three domains or subdomains that can access a generated URL. This URL is then
                embedded in the website that you create. Only the domains that are listed in the
                parameter can access the embedded dashboard. Without this condition, you can list
                any domain on the internet in the `AllowedDomains` parameter. 

To limit the domains that developers can use with this parameter, add an
                    `AllowedEmbeddingDomains` condition to your IAM policy. For more
                information about the `AllowedDomains` parameter, see [GenerateEmbedUrlForAnonymousUser](https://docs.aws.amazon.com//quicksight/latest/APIReference/API_GenerateEmbedUrlForAnonymousUser.html) in the *Amazon Quick Sight API Reference*.

###### Security best practice for IAM condition operators

Improperly configured IAM condition operators can allow unauthorized access to your embedded Quick resources through URL variations. When using the `quicksight:AllowedEmbeddingDomains` condition key in your IAM policies, use condition operators that either allow specific domains or deny all domains that are not specifically allowed. For more information about IAM condition operators, see [IAM JSON policy elements: Condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html) in the IAM User Guide.

Many different URL variations can point to the same resource. For example, the following URLs all resolve to the same content:

- `https://example.com`
- `https://example.com/`
- `https://Example.com`

If your policy uses operators that do not account for these URL variations, an attacker can bypass your restrictions by providing equivalent URL variations.

You must validate that your IAM policy uses appropriate condition operators to prevent bypass vulnerabilities and ensure that only your intended domains can access your embedded resources.

The following sample policy provides these permissions for use with
                    `GenerateEmbedUrlForAnonymousUser`. For this approach to work, you
                also need a session pack, or session capacity pricing, for your AWS account.
                Otherwise, when a user tries to access the dashboard, the error
                    `UnsupportedPricingPlanException` is returned. 

Your application's IAM identity must have a trust policy associated with it to allow access to the role that you just created. This means that when a user accesses your application, your application can assume the role on the user's behalf to open the dashboard. The following example shows a sample trust policy.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Sid": "AllowLambdaFunctionsToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "lambda.amazonaws.com" }, "Action": "sts:AssumeRole" }, { "Sid": "AllowEC2InstancesToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }`

For more information regarding trust policies, see [Temporary security credentials in
                    IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*.

## Step 2: Generate the URL with the authentication code attached

            | Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

In the following section, you can find how to authenticate on behalf of the anonymous visitor and get the embeddable dashboard URL on your application server.

When a user accesses your app, the app assumes the IAM role on the user's behalf. Then it adds the user to Amazon Quick Sight, if that user doesn't already exist. Next, it passes an identifier as the unique role session ID.

The following examples perform the IAM authentication on the user's behalf. It passes an identifier as the unique role session ID. This code runs on your app server.

```
import java.util.List;
    import com.amazonaws.auth.AWSCredentials;
    import com.amazonaws.auth.AWSCredentialsProvider;
    import com.amazonaws.auth.BasicAWSCredentials;
    import com.amazonaws.regions.Regions;
    import com.amazonaws.services.quicksight.AmazonQuickSight;
    import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
    import com.amazonaws.services.quicksight.model.RegisteredUserDashboardEmbeddingConfiguration;
    import com.amazonaws.services.quicksight.model.AnonymousUserEmbeddingExperienceConfiguration;
    import com.amazonaws.services.quicksight.model.GenerateEmbedUrlForAnonymousUserRequest;
    import com.amazonaws.services.quicksight.model.GenerateEmbedUrlForAnonymousUserResult;
    import com.amazonaws.services.quicksight.model.SessionTag;
    /**
    * Class to call QuickSight AWS SDK to generate embed url for anonymous user.
    */
    public class GenerateEmbedUrlForAnonymousUserExample {
        private final AmazonQuickSight quickSightClient;
        public GenerateEmbedUrlForAnonymousUserExample() {
            quickSightClient = AmazonQuickSightClientBuilder
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
        public String GenerateEmbedUrlForAnonymousUser(
            final String accountId, // YOUR AWS ACCOUNT ID
            final String initialDashboardId, // DASHBOARD ID TO WHICH THE CONSTRUCTED URL POINTS.
            final String namespace, // ANONYMOUS EMBEDDING REQUIRES SPECIFYING A VALID NAMESPACE FOR WHICH YOU WANT THE EMBEDDING URL
            final List<String> authorizedResourceArns, // DASHBOARD ARN LIST TO EMBED
            final List<String> allowedDomains, // RUNTIME ALLOWED DOMAINS FOR EMBEDDING
            final List<SessionTag> sessionTags // SESSION TAGS USED FOR ROW-LEVEL SECURITY
        ) throws Exception {
            AnonymousUserEmbeddingExperienceConfiguration experienceConfiguration = new AnonymousUserEmbeddingExperienceConfiguration();
            AnonymousUserDashboardEmbeddingConfiguration dashboardConfiguration = new AnonymousUserDashboardEmbeddingConfiguration();
            dashboardConfiguration.setInitialDashboardId(initialDashboardId);
            experienceConfiguration.setDashboard(dashboardConfiguration);
            GenerateEmbedUrlForAnonymousUserRequest generateEmbedUrlForAnonymousUserRequest = new GenerateEmbedUrlForAnonymousUserRequest()
                .withAwsAccountId(accountId)
                .withNamespace(namespace)
                .withAuthorizedResourceArns(authorizedResourceArns)
                .withExperienceConfiguration(experienceConfiguration)
                .withSessionTags(sessionTags)
                .withSessionLifetimeInMinutes(600L); // OPTIONAL: VALUE CAN BE [15-600]. DEFAULT: 600
                .withAllowedDomains(allowedDomains);
            GenerateEmbedUrlForAnonymousUserResult dashboardEmbedUrl = quickSightClient.generateEmbedUrlForAnonymousUser(generateEmbedUrlForAnonymousUserRequest);
            return dashboardEmbedUrl.getEmbedUrl();
        }
    }
```
```
global.fetch = require('node-fetch');
const AWS = require('aws-sdk');
function generateEmbedUrlForAnonymousUser(
accountId, // YOUR AWS ACCOUNT ID
initialDashboardId, // DASHBOARD ID TO WHICH THE CONSTRUCTED URL POINTS
quicksightNamespace, // VALID NAMESPACE WHERE YOU WANT TO DO NOAUTH EMBEDDING
authorizedResourceArns, // DASHBOARD ARN LIST TO EMBED
allowedDomains, // RUNTIME ALLOWED DOMAINS FOR EMBEDDING
sessionTags, // SESSION TAGS USED FOR ROW-LEVEL SECURITY
generateEmbedUrlForAnonymousUserCallback, // GENERATEEMBEDURLFORANONYMOUSUSER SUCCESS CALLBACK METHOD
errorCallback // GENERATEEMBEDURLFORANONYMOUSUSER ERROR CALLBACK METHOD
) {
const experienceConfiguration = {
    "DashboardVisual": {
        "InitialDashboardVisualId": {
            "DashboardId": "dashboard_id",
            "SheetId": "sheet_id",
            "VisualId": "visual_id"
        }
    }
};
const generateEmbedUrlForAnonymousUserParams = {
    "AwsAccountId": accountId,
    "Namespace": quicksightNamespace,
    "AuthorizedResourceArns": authorizedResourceArns,
    "AllowedDomains": allowedDomains,
    "ExperienceConfiguration": experienceConfiguration,
    "SessionTags": sessionTags,
    "SessionLifetimeInMinutes": 600
};
const quicksightClient = new AWS.QuickSight({
    region: process.env.AWS_REGION,
    credentials: {
        accessKeyId: AccessKeyId,
        secretAccessKey: SecretAccessKey,
        sessionToken: SessionToken,
        expiration: Expiration
    }
});
quicksightClient.generateEmbedUrlForAnonymousUser(generateEmbedUrlForAnonymousUserParams, function(err, data) {
    if (err) {
        console.log(err, err.stack);
        errorCallback(err);
    } else {
        const result = {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*", // USE YOUR WEBSITE DOMAIN TO SECURE ACCESS TO THIS API
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": JSON.stringify(data),
            "isBase64Encoded": false
        }
        generateEmbedUrlForAnonymousUserCallback(result);
    }
});
}
```
```
import json
import boto3
from botocore.exceptions import ClientError
import time
# Create QuickSight and STS clients
quicksightClient = boto3.client('quicksight',region_name='us-west-2')
sts = boto3.client('sts')
# Function to generate embedded URL for anonymous user
# accountId: YOUR AWS ACCOUNT ID
# quicksightNamespace: VALID NAMESPACE WHERE YOU WANT TO DO NOAUTH EMBEDDING
# authorizedResourceArns: DASHBOARD ARN LIST TO EMBED
# allowedDomains: RUNTIME ALLOWED DOMAINS FOR EMBEDDING
# dashboardId: DASHBOARD ID TO WHICH THE CONSTRUCTED URL POINTS
# sessionTags: SESSION TAGS USED FOR ROW-LEVEL SECURITY
def generateEmbedUrlForAnonymousUser(accountId, quicksightNamespace, authorizedResourceArns, allowedDomains, dashboardId, sessionTags):
try:
    response = quicksightClient.generate_embed_url_for_anonymous_user(
        AwsAccountId = accountId,
        Namespace = quicksightNamespace,
        AuthorizedResourceArns = authorizedResourceArns,
        AllowedDomains = allowedDomains,
            ExperienceConfiguration = {
                "Dashboard": {
                    "InitialDashboardId": dashboardId
                }
            },
        SessionTags = sessionTags,
        SessionLifetimeInMinutes = 600
    )
        
    return {
        'statusCode': 200,
        'headers': {"Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type"},
        'body': json.dumps(response),
        'isBase64Encoded':  bool('false')
    }
except ClientError as e:
    print(e)
    return "Error generating embeddedURL: " + str(e)
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
    quicksightClient.generateEmbedUrlForAnonymousUser({
        'AwsAccountId': '111122223333',
        'Namespace' : 'default',
        'AuthorizedResourceArns': authorizedResourceArns,
        'AllowedDomains': allowedDomains,
        'ExperienceConfiguration': experienceConfiguration,
        'SessionTags': sessionTags,
        'SessionLifetimeInMinutes': 600
    }, function(err, data) {
        console.log('Errors: ');
        console.log(err);
        console.log('Response: ');
        console.log(data);
    });
```
###### Example

`//The URL returned is over 900 characters. For this example, we've shortened the string for //readability and added ellipsis to indicate that it's incomplete. { Status: 200, EmbedUrl: 'https://``quicksightdomain`/embed/12345/dashboards/67890..', RequestId: '7bee030e-f191-45c4-97fe-d9faf0e03713' }

The following example shows the .NET/C# code that you can use on the app server to generate the URL for the embedded dashboard. You can use this URL in your website or app to display the dashboard.

###### Example

```
using System;
    using Amazon.QuickSight;
    using Amazon.QuickSight.Model;
    var quicksightClient = new AmazonQuickSightClient(
        AccessKey,
        SecretAccessKey,
        sessionToken,
        Amazon.RegionEndpoint.USEast1);
        
    try
    {
        Console.WriteLine(
            quicksightClient.GenerateEmbedUrlForAnonymousUserAsync(new GenerateEmbedUrlForAnonymousUserRequest
            {
                AwsAccountId = "111122223333",
                Namespace = default,
                AuthorizedResourceArns = authorizedResourceArns,
                AllowedDomains = allowedDomains,
                ExperienceConfiguration = experienceConfiguration,
                SessionTags = sessionTags,
                SessionLifetimeInMinutes = 600,
            }).Result.EmbedUrl
        );
    } catch (Exception ex) {
        Console.WriteLine(ex.Message);
    }
```
To assume the role, choose one of the following AWS Security Token Service (AWS STS) API operations:

- 
                            [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html)– Use this operation when you're using an IAM identity to assume the role.
- 
                            [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html)– Use this operation when you're using a web identity provider to authenticate your user.
- 
                            [AssumeRoleWithSaml](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithSAML.html)– Use this operation when you're using Security Assertion Markup Language (SAML) to authenticate your users.

The following example shows the CLI command to set the IAM role. The
                        role needs to have permissions enabled for
                            `quicksight:GenerateEmbedUrlForAnonymousUser`. 

`aws sts assume-role \ --role-arn "``arn:aws:iam::11112222333:role/QuickSightEmbeddingAnonymousPolicy`" \ --role-session-name`anonymous caller`

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
                            `embedding_quicksight_dashboard_role/QuickSightEmbeddingAnonymousPolicy`.
                        The role session ID is made up of the role name from `role-arn`
                        and the `role-session-name` value. Using the unique role session
                        ID for each user ensures that appropriate permissions are set for each
                        visiting user. It also keeps each session separate and distinct. If you're
                        using an array of web servers, for example for load balancing, and a session
                        is reconnected to a different server, a new session begins.

To get a signed URL for the dashboard, call
                            `generate-embed-url-for-anynymous-user` from the app server.
                        This returns the embeddable dashboard URL. The following example shows how
                        to generate the URL for an embedded dashboard using a server-side call for
                        users who are making anonymous visits to your web portal or app.

`aws quicksight generate-embed-url-for-anonymous-user \ --aws-account-id``111122223333`\ --namespace`default-or-something-else`\ --session-lifetime-in-minutes 15 \ --authorized-resource-arns '["`dashboard-arn-1`","`dashboard-arn-2`"]' \ --allowed-domains '["`domain1`","`domain2`"]' \ --session-tags '["Key":`tag-key-1`,"Value":`tag-value-1`,{"Key":`tag-key-1`,"Value":`tag-value-1`}]' \ --experience-configuration 'DashboardVisual={InitialDashboardVisualId={DashboardId=`dashboard_id`,SheetId=`sheet_id`,VisualId=`visual_id`}}'

For more information about using this operation, see [GenerateEmbedUrlForAnonymousUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForAnonymousUser.html). You can
                        use this and other API operations in your own code. 

## Step 3: Embed the dashboard URL

            | Applies
                    to:Enterprise Edition | 

| Intended audience: Amazon Quick developers | 

In the following section, you can find out how you can use the [Amazon Quick Sight Embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) (JavaScript) to embed the dashboard URL
                from step 2 in your website or application page. With the SDK, you can do the
                following: 

- 
                    Place the dashboard on an HTML page. 
- 
                    Pass parameters into the dashboard. 
- 
                    Handle error states with messages that are customized to your application. 

Call the `GenerateEmbedUrlForAnynymousUser` API operation to generate
                the URL that you can embed in your app. This URL is valid for 5 minutes, and the
                resulting session is valid for 10 hours. The API operation provides the URL with an
                    `auth_code` that enables a single-sign on session. 

The following shows an example response from
                    `generate-embed-url-for-anynymous-user`.

`//The URL returned is over 900 characters. For this example, we've shortened the string for //readability and added ellipsis to indicate that it's incomplete. { "Status": "200", "EmbedUrl": "https://``quicksightdomain`/embed/12345/dashboards/67890..", "RequestId": "7bee030e-f191-45c4-97fe-d9faf0e03713" }

Embed this dashboard in your web page by using the [Amazon Quick Sight Embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) or by adding this URL into an iframe.
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

The following example shows how to use the generated URL. This code resides on your app server.

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
                    Download the latest Amazon Quick Sight Embedding SDK version from [https://www.npmjs.com/package/amazon-quicksight-embedding-sdk](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk).
- 
                    If you use `npm`for JavaScript dependencies, download and install it by running the following command.`npm install amazon-quicksight-embedding-sdk`