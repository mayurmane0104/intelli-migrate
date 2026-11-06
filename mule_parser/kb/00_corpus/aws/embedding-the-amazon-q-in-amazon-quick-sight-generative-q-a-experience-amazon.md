# Embedding the Amazon Q in Amazon Quick Sight Generative Q&A experience - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedding-gen-bi.html](https://docs.aws.amazon.com/quick/latest/userguide/embedding-gen-bi.html)

---

| Intended audience: Amazon Quick developers | 

In the following sections, you can find detailed information about how to set up an embedded Generative Q&A experience that uses enhanced NLQ capabilties powered by LLMs. The Generative Q&A experience is the recommended replacement for the embedded Q Search Bar and provides an updated BI experience for users.

###### Topics

## Embedding the Amazon Q in Amazon Quick Sight Generative Q&A experience for registered users

        In the following sections, you can find detailed information about how to set up an embedded Generative Q&A experience for registered users of Amazon Quick Sight.

###### Topics

### Step 1: Set up permissions

In the following section, you can find how to set up permissions for your backend application or web server to embed the Generative Q&A experience. This task requires administrative access to AWS Identity and Access Management (IAM).

Each user who accesses a Generative Q&A experience assumes a role that gives them Amazon Quick Sight access and permissions. To make this possible, create an IAM role in your AWS account. Associate an IAM policy with the role to provide permissions to any user who assumes it. The IAM role needs to provide permissions to retrieve embedding URLs for a specific user pool.

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
                the embedded Generative Q&A experience. Without this condition, developers can list any domain on the
                internet in the `AllowedDomains` parameter. 

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

### Step 2: Generate the URL with the authentication code attached

In the following section, you can find how to authenticate your user and get the embeddable Q topic URL on your application server. If you plan to embed the Generative Q&A experience for IAM or Amazon Quick Sight identity types, share the Q topic with the users.

When a user accesses your app, the app assumes the IAM role on the user's behalf. Then the app adds the user to Amazon Quick Sight, if that user doesn't already exist. Next, it passes an identifier as the unique role session ID.

Performing the described steps ensures that each viewer of the Q topic is uniquely provisioned in Amazon Quick Sight. It also enforces per-user settings, such as the row-level security and dynamic defaults for parameters. Tag-based row-level security can be used for anonymous user embedding of the Q bar.

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
import com.amazonaws.services.quicksight.model.RegisteredUserGenerativeQnAEmbeddingConfiguration;
/**
 * Class to call QuickSight AWS SDK to get url for embedding Generative Q&A experience.
 */
public class RegisteredUserGenerativeQnAEmbeddingSample {
    private final AmazonQuickSight quickSightClient;
    public RegisteredUserGenerativeQnAEmbeddingSample() {
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
                .withGenerativeQnA(new RegisteredUserGenerativeQnAEmbeddingConfiguration().withInitialTopicId(topicId));
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
###### Note

Embed URL generation APIs cannot be called from browsers directly. Refer to the Node.JS example instead.

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
                    'GenerativeQnA': {
                        'InitialTopicId': topicId
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
    region: 'us-east-1'
});
quicksightClient.generateEmbedUrlForRegisteredUser({
    'AwsAccountId': '111122223333',
    'ExperienceConfiguration': { 
        'GenerativeQnA': {
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
The following example shows the .NET/C# code that you can use on the app server to generate the URL for the embedded Q search bar. You can use this URL in your website or app to display the Q search bar.

###### Example

```
using System;
using Amazon.QuickSight;
using Amazon.QuickSight.Model;
namespace GenerateGenerativeQnAEmbedUrlForRegisteredUser
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
                RegisteredUserGenerativeQnAEmbeddingConfiguration registeredUserGenerativeQnAEmbeddingConfiguration
                    = new RegisteredUserGenerativeQnAEmbeddingConfiguration
                    {
                        InitialTopicId = "U4zJMVZ2n2stZflc8Ou3iKySEb3BEV6f"
                    };
                RegisteredUserEmbeddingExperienceConfiguration registeredUserEmbeddingExperienceConfiguration
                    = new RegisteredUserEmbeddingExperienceConfiguration
                    {
                        GenerativeQnA = registeredUserGenerativeQnAEmbeddingConfiguration
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

`aws sts assume-role \ --role-arn "arn:aws:iam::``111122223333`:role/embedding_quicksight_q_generative_qna_role" \ --role-session-name`john.doe@example.com`

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

The role session ID also becomes the user name in Amazon Quick Sight. You can use this pattern to provision your users in Amazon Quick Sight ahead of time, or to provision them the first time that they access the Generative Q&A experience.

The following example shows the CLI command that you can use to provision
                        a user. For more information about [RegisterUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisterUser.html), [DescribeUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DescribeUser.html), and other Amazon Quick Sight API operations, see
                        the [Amazon Quick Sight API reference](https://docs.aws.amazon.com/quicksight/latest/APIReference/Welcome.html).

`aws quicksight register-user \ --aws-account-id``111122223333`\ --namespace`default`\ --identity-type`IAM`\ --iam-arn "`arn:aws:iam::111122223333:role/embedding_quicksight_q_generative_qna_role`" \ --user-role`READER`\ --user-name`jhnd`\ --session-name "`john.doe@example.com`" \ --email`john.doe@example.com`\ --region`us-east-1`\ --custom-permissions-name`TeamA1`

If the user is authenticated through Microsoft AD, you don't need to use
                            `RegisterUser` to set them up. Instead, they should be
                        automatically subscribed the first time that they access Amazon Quick Sight.
                        For Microsoft AD users, you can use `DescribeUser` to get the
                        user Amazon Resource Name (ARN).

The first time a user accesses Amazon Quick Sight, you can also add this user to the group that the dashboard is shared with. The following example shows the CLI command to add a user to a group.

`aws quicksight create-group-membership \ --aws-account-id``111122223333`\ --namespace`default`\ --group-name`financeusers`\ --member-name "`embedding_quicksight_q_generative_qna_role/john.doe@example.com`"

You now have a user of your app who is also a user of Amazon Quick Sight, and who has access to the dashboard.

Finally, to get a signed URL for the dashboard, call
                            `generate-embed-url-for-registered-user` from the app server.
                        This returns the embeddable dashboard URL. The following example shows how
                        to generate the URL for an embedded dashboard using a server-side call for
                        users authenticated through AWS Managed Microsoft AD or single sign-on (IAM Identity Center).

`aws quicksight generate-embed-url-for-anonymous-user \ --aws-account-id``111122223333`\ --namespace`default-or-something-else`\ --authorized-resource-arns '["`topic-arn-topicId1`","`topic-arn-topicId2`"]' \ --allowed-domains '["`domain1`","`domain2`"]' \ --experience-configuration 'GenerativeQnA={InitialTopicId="`topicId1`"}' \ --session-tags '["Key":`tag-key-1`,"Value":`tag-value-1`,{"Key":`tag-key-1`,"Value":`tag-value-1`}]' \ --session-lifetime-in-minutes`15`

For more information about using this operation, see [GenerateEmbedUrlForRegisteredUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForRegisteredUser.html). You can
                        use this and other API operations in your own code.

### Step 3: Embed the Generative Q&A experience URL

In the following section, you can find how to embed the Generative Q&A experience URL in your website
                or application page. You do this with the [Amazon Quick Sight embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) (JavaScript). With the SDK, you can do
                the following: 

- 
                    Place the Generative Q&A experience on an HTML page. 
- 
                    Customize the layout and appearance of the embedded experience to fit your application needs. 
- 
                    Handle error states with messages that are customized to your application. 

To generate the URL that you can embed in your app, call the
                    `GenerateEmbedUrlForRegisteredUser` API operation. This URL is valid
                for 5 minutes, and the resulting session is valid for up to 10 hours. The API
                operation provides the URL with an `auth_code` value that enables a
                single-sign on session. 

The following shows an example response from
                    `generate-embed-url-for-registered-user`.

```
//The URL returned is over 900 characters. For this example, we've shortened the string for
//readability and added ellipsis to indicate that it's incomplete. 
{
 "Status": "200",
"EmbedUrl": "https://quicksightdomain/embedding/12345/q/search...",
"RequestId": "7bee030e-f191-45c4-97fe-d9faf0e03713"
}
```
Embed the Generative Q&A experience in your webpage by using the [Amazon Quick Sight embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) or by adding this URL into an iframe.
                If you set a fixed height and width number (in pixels), Amazon Quick Sight uses those
                and doesn't change your visual as your window resizes. If you set a relative
                percent height and width, Amazon Quick Sight provides a responsive layout that is
                modified as your window size changes. 

Make sure that the domain to host the embedded Generative Q&A experience is on the *allow list*, the list of approved domains for your
                Amazon Quick Sight subscription. This requirement protects your data by keeping
                unapproved domains from hosting embedded dashboards. For more information about
                adding domains for an embedded Generative Q&A experience, see [Managing domains](./manage-domains.html).

You can use the Amazon Quick Sight Embedding SDK to customize the layout and
                apperance of the embedded Generative Q&A experience to fit your application. Use the
                    `panelType` property to configure the landing state of the Generative Q&A experience when
                it renders in your application. Set the `panelType` property to
                    `'FULL'` to render the full Generative Q&A experience panel. This panel resembles the
                experience that Amazon Quick Sight users have in the Amazon Quick Sight console. The
                frame height of the panel is not changed based on user interaction and respects the
                value that you set in the `frameOptions.height` property. The image below
                shows the Generative Q&A experience panel that renders when you set the `panelType` value to
                    `'FULL'`.

Set the `panelType` property to `'SEARCH_BAR'` to render the
                Generative Q&A experience as a search bar. This search bar resembles the way that the Q Search Bar
                renders when it is embedded into an application. The Generative Q&A search bar
                expands to a larger panel that displays topic selection options, the question
                suggestion list, the answer panel or the pinboard.

The default minimum height of the Generative Q&A search bar is rendered when
                the embedded asset loads. It is recommended that you set the
                    `frameOptions.height` value to `"38px"` to optimize the
                search bar experience. Use the `focusedHeight` property to set the
                optimal size of the topic selection dropdown and the question suggestion list. Use
                the `expandedHeight` property to set the optimal size of the answer panel
                and pinboard. If you choose the `'SEARCH_BAR'` option, it is recommended
                that you style the parent container with position; absolute to avoid unwanted
                content shifting in your application. The image below shows the Generative Q&A experience search bar
                that renders when you set the `panelType` value to
                    `'SEARCH_BAR'`.

After you configure the `panelType` property, use the Amazon Quick Sight
                embedding SDK to customize the following properties of the Generative Q&A experience.

- 
                    The title of the Generative Q&A panel (Applies only to the `panelType: FULL`option).
- 
                    The search bar's placeholder text. 
- 
                    Whether topic selection is allowed. 
- 
                    Whether topic names are shown or hidden. 
- 
                    Whether the Amazon Q icon is shown or hidden (Applies only to the `panelType: FULL`option).
- 
                    Whether the pinboard is shown of hidden. 
- 
                    Whether users can maximize the Genertaive Q&A panel to fullscreen. 
- 
                    The theme of the Generative Q&A panel. A custom theme ARN can be passed in the SDK to change the appearance of the frame's content. Amazon Quick Sight starter themes are not supported for embedded Generative BI panels. To use a Amazon Quick Sight starter theme, save it as a custom theme in Amazon Quick Sight. 

When you use the Amazon Quick Sight Embedding SDK, the Generative Q&A experience on your page is dynamically resized based on the state. By using the Amazon Quick Sight Embedding SDK, you can also control parameters within the Generative Q&A experience and receive callbacks in terms of page load completion, state changes, and errors.

The following example shows how to use the generated URL. This code is generated on your app server.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Generative Q&A Embedding Example</title>
        <script src="https://unpkg.com/amazon-quicksight-embedding-sdk@2.7.0/dist/quicksight-embedding-js-sdk.min.js"></script>
        <script type="text/javascript">
            const embedGenerativeQnA = async() => {    
                const {createEmbeddingContext} = QuickSightEmbedding;
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
                    // Optional panel settings. Default behavior is equivalent to {panelType: 'FULL'}
                    panelOptions: {
                        panelType: 'FULL',
                        title: 'custom title', // Optional
                        showQIcon: false, // Optional, Default: true
                    },
                    // Use SEARCH_BAR panel type for the landing state to be similar to embedQSearchBar
                    // with generative capability enabled topics
                    /*
                    panelOptions: {
                        panelType: 'SEARCH_BAR',
                        focusedHeight: '250px',
                        expandedHeight: '500px',
                    },
                    */
                    showTopicName: false, // Optional, Default: true
                    showPinboard: false, // Optional, Default: true
                    allowTopicSelection: false, // Optional, Default: true
                    allowFullscreen: false, // Optional, Default: true
                    searchPlaceholderText: "custom search placeholder", // Optional
                    themeOptions: { // Optional
                        themeArn: 'arn:aws:quicksight:<Region>:<AWS-Account-ID>:theme/<Theme-ID>'
                    }
                    onMessage: async (messageEvent, experienceMetadata) => {
                        switch (messageEvent.eventName) {
                            case 'Q_SEARCH_OPENED': {
                                // called when pinboard is shown / visuals are rendered
                                console.log("Do something when SEARCH_BAR type panel is expanded");
                                break;
                            }
                            case 'Q_SEARCH_FOCUSED': {
                                // called when question suggestions or topic selection dropdown are shown
                                console.log("Do something when SEARCH_BAR type panel is focused");
                                break;
                            }
                            case 'Q_SEARCH_CLOSED': {
                                // called when shrinked to initial bar height
                                console.log("Do something when SEARCH_BAR type panel is collapsed");
                                break;
                            }
                            case 'Q_PANEL_ENTERED_FULLSCREEN': {
                                console.log("Do something when panel enters full screen mode");
                                break;
                            }
                            case 'Q_PANEL_EXITED_FULLSCREEN': {
                                console.log("Do something when panel exits full screen mode");
                                break;
                            }
                            case 'CONTENT_LOADED': {
                                console.log("Do something after experience is loaded");
                                break;
                            }
                            case 'ERROR_OCCURRED': {
                                console.log("Do something when experience fails to load");
                                break;
                            }
                        }
                    }
                };
                const embeddedGenerativeQnExperience = await embeddingContext.embedGenerativeQnA(frameOptions, contentOptions);
            };
        </script>
    </head>
    <body onload="embedGenerativeQnA()">
        <div id="experience-container"></div>
    </body>
</html>
```
For this example to work, make sure to use the Amazon Quick Sight Embedding SDK to load the embedded Generative Q&A experience on your website with JavaScript. To get your copy, do one of the following:

- 
                    Download the [Amazon Quick Sight embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk#step-3-create-the-quicksight-session-object)from GitHub. This repository is maintained by a group of Amazon Quick Sight developers.
- 
                    Download the latest embedding SDK version from [https://www.npmjs.com/package/amazon-quicksight-embedding-sdk](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk).
- 
                    If you use `npm`for JavaScript dependencies, download and install it by running the following command.`npm install amazon-quicksight-embedding-sdk`

### Optional embedded Generative Q&A experience functionalities

The following optional functionalities are available for the embedded Generative Q&A experience with the embedding SDK.

#### Invoke Generative Q&A search bar actions

- 
                        Set a question — This feature sends a question to the Generative Q&A experience and immediately queries the question. `embeddedGenerativeQnExperience.setQuestion('``show me monthly revenue`');
- 
                        Close the answer panel (applies to the Generative Q&A search bar option) — This feature closes the answer panel and returns the iframe to the original search bar state. `embeddedGenerativeQnExperience.close();`

For more information, see the [Amazon Quick Sight embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk).

## Embedding the Amazon Q in Quick Generative Q&A experience for anonymous (unregistered) users

        | Intended audience: Amazon Quick developers | 

In the following sections, you can find detailed information about how to set up an embedded Generative Q&A experience for anonymous (unregistered) users.

###### Topics

### Step 1: Set up permissions

In the following section, you can find how to set up permissions for your backend application or web server to embed the Generative Q&A experience. This task requires administrative access to AWS Identity and Access Management (IAM).

Each user who accesses a Generative Q&A experience assumes a role that gives them Amazon Quick Sight access and permissions. To make this possible, create an IAM role in your AWS account. Associate an IAM policy with the role to provide permissions to any user who assumes it. The IAM role needs to provide permissions to retrieve embedding URLs for a specific user pool.

With the help of the wildcard character ***, you can grant the
                permissions to generate a URL for all users in a specific namespace. Or you can
                grant permissions to generate a URL for a subset of users in specific namespaces.
                For this, you add `quicksight:GenerateEmbedUrlForAnonymousUser`.

You can create a condition in your IAM policy that limits the domains that
                developers can list in the `AllowedDomains` parameter of a
                    `GenerateEmbedUrlForAnonymousUser` API operation. The
                    `AllowedDomains` parameter is an optional parameter. It grants
                developers the option to override the static domains that are configured in the
                    **Manage Amazon Quick Sight** menu and instead list up to three
                domains or subdomains that can access a generated URL. This URL is then embedded in
                a developer's website. Only the domains that are listed in the parameter can access
                the embedded Q search bar. Without this condition, developers can list any domain on
                the internet in the `AllowedDomains` parameter. 

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

Your application's IAM identity must have a trust policy associated with it to allow access to the role that you just created. This means that when a user accesses your application, your application can assume the role on the user's behalf to load the Generative Q&A experience. The following example shows a sample trust policy.

- 
            
                
                `{ "Version":"2012-10-17", "Statement": [ { "Sid": "AllowLambdaFunctionsToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "lambda.amazonaws.com" }, "Action": "sts:AssumeRole" }, { "Sid": "AllowEC2InstancesToAssumeThisRole", "Effect": "Allow", "Principal": { "Service": "ec2.amazonaws.com" }, "Action": "sts:AssumeRole" } ] }`

For more information regarding trust policies, see [Temporary security credentials in
                    IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) in the *IAM User Guide*

### Step 2: Generate the URL with the authentication code attached

In the following section, you can find how to authenticate your user and get the embeddable Q topic URL on your application server.

When a user accesses your app, the app assumes the IAM role on the user's behalf. Then the app adds the user to Amazon Quick Sight, if that user doesn't already exist. Next, it passes an identifier as the unique role session ID.

```
import java.util.List;
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.quicksight.AmazonQuickSight;
import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
import com.amazonaws.services.quicksight.model.AnonymousUserGenerativeQnAEmbeddingConfiguration;
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
        final String initialTopicId, // Q TOPIC ID TO WHICH THE CONSTRUCTED URL POINTS AND EXPERIENCE PREPOPULATES INITIALLY
        final String namespace, // ANONYMOUS EMBEDDING REQUIRES SPECIFYING A VALID NAMESPACE FOR WHICH YOU WANT THE EMBEDDING URL
        final List<String> authorizedResourceArns, // Q TOPIC ARN LIST TO EMBED
        final List<String> allowedDomains, // RUNTIME ALLOWED DOMAINS FOR EMBEDDING
        final List<SessionTag> sessionTags // SESSION TAGS USED FOR ROW-LEVEL SECURITY
    ) throws Exception {
        AnonymousUserEmbeddingExperienceConfiguration experienceConfiguration = new AnonymousUserEmbeddingExperienceConfiguration();
        AnonymousUserGenerativeQnAEmbeddingConfiguration generativeQnAConfiguration = new AnonymousUserGenerativeQnAEmbeddingConfiguration();
        generativeQnAConfiguration.setInitialTopicId(initialTopicId);
        experienceConfiguration.setGenerativeQnA(generativeQnAConfiguration);
        GenerateEmbedUrlForAnonymousUserRequest generateEmbedUrlForAnonymousUserRequest = new GenerateEmbedUrlForAnonymousUserRequest()
            .withAwsAccountId(accountId)
            .withNamespace(namespace)
            .withAuthorizedResourceArns(authorizedResourceArns)
            .withExperienceConfiguration(experienceConfiguration)
            .withSessionTags(sessionTags)
            .withSessionLifetimeInMinutes(600L); // OPTIONAL: VALUE CAN BE [15-600]. DEFAULT: 600
            .withAllowedDomains(allowedDomains);
        GenerateEmbedUrlForAnonymousUserResult result = quickSightClient.generateEmbedUrlForAnonymousUser(generateEmbedUrlForAnonymousUserRequest);
        return result.getEmbedUrl();
    }
}
```
###### Note

Embed URL generation APIs cannot be called from browsers directly. Refer to the Node.JS example instead.

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
# topicId: Topic ID to embed
# quicksightNamespace: VALID NAMESPACE WHERE YOU WANT TO DO NOAUTH EMBEDDING
# authorizedResourceArns: TOPIC ARN LIST TO EMBED
# allowedDomains: RUNTIME ALLOWED DOMAINS FOR EMBEDDING
# sessionTags: SESSION TAGS USED FOR ROW-LEVEL SECURITY
def generateEmbedUrlForAnonymousUser(accountId, quicksightNamespace, authorizedResourceArns, allowedDomains, sessionTags):
    try:
        response = quicksightClient.generate_embed_url_for_anonymous_user(
            AwsAccountId = accountId,
            Namespace = quicksightNamespace,
            AuthorizedResourceArns = authorizedResourceArns,
            AllowedDomains = allowedDomains,
            ExperienceConfiguration = {
                'GenerativeQnA': {
                        'InitialTopicId': topicId
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
    region: 'us-east-1',
});
quicksightClient.generateEmbedUrlForAnonymousUser({
    'AwsAccountId': '111122223333',
    'Namespace': 'DEFAULT'
    'AuthorizedResourceArns': '["topic-arn-topicId1","topic-arn-topicId2"]',
    'AllowedDomains': allowedDomains,
    'ExperienceConfiguration': { 
        'GenerativeQnA': {
            'InitialTopicId': 'U4zJMVZ2n2stZflc8Ou3iKySEb3BEV6f'
        }
    },
    'SessionTags': '["Key": tag-key-1,"Value": tag-value-1,{"Key": tag-key-1,"Value": tag-value-1}]',
    'SessionLifetimeInMinutes': 15
}, function(err, data) {
    console.log('Errors: ');
    console.log(err);
    console.log('Response: ');
    console.log(data);
});
```
The following example shows the .NET/C# code that you can use on the app server to generate the URL for the embedded Q search bar. You can use this URL in your website or app to display the Q search bar.

###### Example

```
using System;
using Amazon.QuickSight;
using Amazon.QuickSight.Model;
namespace GenerateGenerativeQnAEmbedUrlForAnonymousUser
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
                AnonymousUserGenerativeQnAEmbeddingConfiguration anonymousUserGenerativeQnAEmbeddingConfiguration
                    = new AnonymousUserGenerativeQnAEmbeddingConfiguration
                    {
                        InitialTopicId = "U4zJMVZ2n2stZflc8Ou3iKySEb3BEV6f"
                    };
                AnonymousUserEmbeddingExperienceConfiguration anonymousUserEmbeddingExperienceConfiguration
                    = new AnonymousUserEmbeddingExperienceConfiguration
                    {
                        GenerativeQnA = anonymousUserGenerativeQnAEmbeddingConfiguration
                    }; 
                
                Console.WriteLine(
                    quicksightClient.GenerateEmbedUrlForAnonymousUserAsync(new GenerateEmbedUrlForAnonymousUserRequest
                    {
                        AwsAccountId = "111122223333",
                        Namespace = "DEFAULT",
                        AuthorizedResourceArns '["topic-arn-topicId1","topic-arn-topicId2"]',
                        AllowedDomains = allowedDomains,
                        ExperienceConfiguration = anonymousUserEmbeddingExperienceConfiguration,
                        SessionTags = '["Key": tag-key-1,"Value": tag-value-1,{"Key": tag-key-1,"Value": tag-value-1}]',
                        SessionLifetimeInMinutes = 15,
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

The following example shows the CLI command to set the IAM role. The role
                        needs to have permissions enabled for
                            `quicksight:GenerateEmbedUrlForAnonymousUser`.

`aws sts assume-role \ --role-arn "``arn:aws:iam::111122223333:role/embedding_quicksight_generative_qna_role`" \ --role-session-name`anonymous caller`

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
                            `embedding_quicksight_q_search_bar_role/QuickSightEmbeddingAnonymousPolicy`.
                        The role session ID is made up of the role name from `role-arn`
                        and the `role-session-name` value. Using the unique role session
                        ID for each user ensures that appropriate permissions are set for each user.
                        It also prevents any throttling of user access. *Throttling* is a security feature that prevents the same user
                        from accessing Amazon Quick Sight from multiple locations. In addition, it
                        keeps each session separate and distinct. If you're using an array of web
                        servers, for example for load balancing, and a session is reconnected to a
                        different server, a new session begins.

To get a signed URL for the dashboard, call
                            `generate-embed-url-for-anynymous-user` from the app server.
                        This returns the embeddable dashboard URL. The following example shows how
                        to generate the URL for an embedded dashboard using a server-side call for
                        users who are making anonymous visits to your web portal or app.

`aws quicksight generate-embed-url-for-anonymous-user \ --aws-account-id``111122223333`\ --namespace`default-or-something-else`\ --authorized-resource-arns '["`topic-arn-topicId`","`topic-arn-topicId2`"]' \ --allowed-domains '["`domain1`","`domain2`"]' \ --experience-configuration '`GenerativeQnA={InitialTopicId="topicId1"}`' \ --session-tags '`["Key": tag-key-1,"Value": tag-value-1,{"Key": tag-key-1,"Value": tag-value-1}]`' \ --session-lifetime-in-minutes`15`

For more information about using this operation, see [GenerateEmbedUrlForAnonymousUser](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_GenerateEmbedUrlForAnonymousUser.html). You can
                        use this and other API operations in your own code.

### Step 3: Embed the Generative Q&A experience URL

In the following section, you can find how to embed the Generative Q&A experience URL in your website
                or application page. You do this with the [Amazon Quick Sight embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) (JavaScript). With the SDK, you can do
                the following: 

- 
                    Place the Generative Q&A experience on an HTML page. 
- 
                    Customize the layout and appearance of the embedded experience to fit your application needs. 
- 
                    Handle error states with messages that are customized to your application. 

To generate the URL that you can embed in your app, call the
                    `GenerateEmbedUrlForAnonymousUser` API operation. This URL is valid
                for 5 minutes, and the resulting session is valid for up to 10 hours. The API
                operation provides the URL with an `auth_code` value that enables a
                single-sign on session. 

The following shows an example response from
                    `generate-embed-url-for-anonymous-user`.

```
//The URL returned is over 900 characters. For this example, we've shortened the string for
//readability and added ellipsis to indicate that it's incomplete.{
     "Status": "200",
     "EmbedUrl": "https://quicksightdomain/embedding/12345/q/search...",
     "RequestId": "7bee030e-f191-45c4-97fe-d9faf0e03713"
} 
```
Embed the Generative Q&A experience in your webpage with the [Amazon Quick Sight embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) or by adding this URL into an iframe.
                If you set a fixed height and width number (in pixels), Amazon Quick Sight uses those
                and doesn't change your visual as your window resizes. If you set a relative
                percent height and width, Amazon Quick Sight provides a responsive layout that is
                modified as your window size changes. 

Make sure that the domain to host the Generative Q&A experience is on the *allow list*, the list of approved domains for your Amazon Quick Sight
                subscription. This requirement protects your data by keeping unapproved domains from
                hosting embedded Generative Q&A experiences. For more information about adding domains for an embedded
                Generative Q&A experience, see [Managing domains](./manage-domains.html).

You can use the Amazon Quick Sight Embedding SDK to customize the layout and
                apperance of the embedded Generative Q&A experience to fit your application. Use the
                    `panelType` property to configure the landing state of the Generative Q&A experience when
                it renders in your application. Set the `panelType` property to
                    `'FULL'` to render the full Generative Q&A experience panel. This panel resembles the
                experience that Amazon Quick Sight users have in the Amazon Quick Sight console. The
                frame height of the panel is not changed based on user interaction and respects the
                value that you set in the `frameOptions.height` property. The image below
                shows the Generative Q&A experience panel that renders when you set the `panelType` value to
                    `'FULL'`.

Set the `panelType` property to `'SEARCH_BAR'` to render the
                Generative Q&A experience as a search bar. This search bar resembles the way that the Q Search Bar
                renders when it is embedded into an application. The Generative Q&A search bar
                expands to a larger panel that displays topic selection options, the question
                suggestion list, the answer panel or the pinboard.

The default minimum height of the Generative Q&A search bar is rendered when
                the embedded asset loads. It is recommended that you set the
                    `frameOptions.height` value to `"38px"` to optimize the
                search bar experience. Use the `focusedHeight` property to set the
                optimal size of the topic selection dropdown and the question suggestion list. Use
                the `expandedHeight` property to set the optimal size of the answer panel
                and pinboard. If you choose the `'SEARCH_BAR'` option, it is recommended
                that you style the parent container with position; absolute to avoid unwanted
                content shifting in your application. The image below shows the Generative Q&A experience search bar
                that renders when you set the `panelType` value to
                    `'SEARCH_BAR'`.

After you configure the `panelType` property, use the Amazon Quick Sight
                embedding SDK to customize the following properties of the Generative Q&A experience.

- 
                    The title of the Generative Q&A panel (Applies only to the `panelType: FULL`option).
- 
                    The search bar's placeholder text. 
- 
                    Whether topic selection is allowed. 
- 
                    Whether topic names are shown or hidden. 
- 
                    Whether the Amazon Q icon is shown or hidden (Applies only to the `panelType: FULL`option).
- 
                    Whether the pinboard is shown of hidden. 
- 
                    Whether users can maximize the Genertaive Q&A panel to fullscreen. 
- 
                    The theme of the Generative Q&A panel. A custom theme ARN can be passed in the SDK to change the appearance of the frame's content. Amazon Quick Sight starter themes are not supported for embedded Generative BI panels. To use a Amazon Quick Sight starter theme, save it as a custom theme in Amazon Quick Sight. 

When you use the Amazon Quick Sight Embedding SDK, the Generative Q&A experience on your page is dynamically resized based on the state. With the Amazon Quick Sight Embedding SDK, you can also control parameters within the Generative Q&A experience and receive callbacks in terms of page load completion, state changes, and errors.

The following example shows how to use the generated URL. This code is generated on your app server.

```
<!DOCTYPE html>
<html>
    <head>
        <title>Generative Q&A Embedding Example</title>
        <script src="https://unpkg.com/amazon-quicksight-embedding-sdk@2.7.0/dist/quicksight-embedding-js-sdk.min.js"></script>
        <script type="text/javascript">
            const embedGenerativeQnA = async() => {    
                const {createEmbeddingContext} = QuickSightEmbedding;
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
                    // Optional panel settings. Default behavior is equivalent to {panelType: 'FULL'}
                    panelOptions: {
                        panelType: 'FULL',
                        title: 'custom title', // Optional
                        showQIcon: false, // Optional, Default: true
                    },
                    // Use SEARCH_BAR panel type for the landing state to be similar to embedQSearchBar
                    // with generative capability enabled topics
                    /*
                    panelOptions: {
                        panelType: 'SEARCH_BAR',
                        focusedHeight: '250px',
                        expandedHeight: '500px',
                    },
                    */
                    showTopicName: false, // Optional, Default: true
                    showPinboard: false, // Optional, Default: true
                    allowTopicSelection: false, // Optional, Default: true
                    allowFullscreen: false, // Optional, Default: true
                    searchPlaceholderText: "custom search placeholder", // Optional
                    themeOptions: { // Optional
                        themeArn: 'arn:aws:quicksight:<Region>:<AWS-Account-ID>:theme/<Theme-ID>'
                    }
                    onMessage: async (messageEvent, experienceMetadata) => {
                        switch (messageEvent.eventName) {
                            case 'Q_SEARCH_OPENED': {
                                // called when pinboard is shown / visuals are rendered
                                console.log("Do something when SEARCH_BAR type panel is expanded");
                                break;
                            }
                            case 'Q_SEARCH_FOCUSED': {
                                // called when question suggestions or topic selection dropdown are shown
                                console.log("Do something when SEARCH_BAR type panel is focused");
                                break;
                            }
                            case 'Q_SEARCH_CLOSED': {
                                // called when shrinked to initial bar height
                                console.log("Do something when SEARCH_BAR type panel is collapsed");
                                break;
                            }
                            case 'Q_PANEL_ENTERED_FULLSCREEN': {
                                console.log("Do something when panel enters full screen mode");
                                break;
                            }
                            case 'Q_PANEL_EXITED_FULLSCREEN': {
                                console.log("Do something when panel exits full screen mode");
                                break;
                            }
                            case 'CONTENT_LOADED': {
                                console.log("Do something after experience is loaded");
                                break;
                            }
                            case 'ERROR_OCCURRED': {
                                console.log("Do something when experience fails to load");
                                break;
                            }
                        }
                    }
                };
                const embeddedGenerativeQnExperience = await embeddingContext.embedGenerativeQnA(frameOptions, contentOptions);
            };
        </script>
    </head>
    <body onload="embedGenerativeQnA()">
        <div id="experience-container"></div>
    </body>
</html>
```
For this example to work, make sure to use the Amazon Quick Sight Embedding SDK to load the embedded Generative Q&A experience on your website with JavaScript. To get your copy, do one of the following:

- 
                    Download the [Amazon Quick Sight embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk#step-3-create-the-quicksight-session-object)from GitHub. This repository is maintained by a group of Amazon Quick Sight developers.
- 
                    Download the latest embedding SDK version from [https://www.npmjs.com/package/amazon-quicksight-embedding-sdk](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk).
- 
                    If you use `npm`for JavaScript dependencies, download and install it by running the following command.`npm install amazon-quicksight-embedding-sdk`

### Optional embedded Generative Q&A experience functionalities

The following optional functionalities are available for the embedded Generative Q&A experience with the embedding SDK.

#### Invoke Generative Q&A search bar actions

- 
                        Set a question — This feature sends a question to the Generative Q&A experience and immediately queries the question. `embeddedGenerativeQnExperience.setQuestion('``show me monthly revenue`');
- 
                        Close the answer panel (applies to the Generative Q&A search bar option) — This feature closes the answer panel and returns the iframe to the original search bar state. `embeddedGenerativeQnExperience.close();`

For more information, see the [Amazon Quick Sight embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk).