# Step 2: Get the URL with the authentication code attached - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-dashboards-for-authenticated-users-get-step-2.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-dashboards-for-authenticated-users-get-step-2.html)

---

###### Important

Amazon Quick Sight has new APIs for embedding analytics:
                        `GenerateEmbedUrlForAnonymousUser` and
                        `GenerateEmbedUrlForRegisteredUser`.

You can still use the `GetDashboardEmbedUrl` and
                        `GetSessionEmbedUrl` APIs to embed dashboards and the
                    Amazon Quick Sight console, but they do not contain the latest embedding
                    capabilities. For the latest up-to-date embedding experience, see [Embedding Amazon Quick Sight analytics into your
                    applications](https://docs.aws.amazon.com/quicksight/latest/user/embedding-overview.html).

In the following section, you can find out how to authenticate your user and get the embeddable dashboard URL on your application server.

When a user accesses your app, the app assumes the IAM role on the user's behalf. Then it adds the user to Amazon Quick Sight, if that user doesn't already exist. Next, it passes an identifier as the unique role session ID.

Performing the described steps ensures that each viewer of the dashboard is uniquely provisioned in Amazon Quick Sight. It also enforces per-user settings, such as the row-level security and dynamic defaults for parameters.

The following examples perform the IAM authentication on the user's behalf. This code runs on your app server.

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicSessionCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.quicksight.AmazonQuickSight;
import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
import com.amazonaws.services.quicksight.model.GetDashboardEmbedUrlRequest;
import com.amazonaws.services.quicksight.model.GetDashboardEmbedUrlResult;
import com.amazonaws.services.securitytoken.AWSSecurityTokenService;
import com.amazonaws.services.securitytoken.model.AssumeRoleRequest;
import com.amazonaws.services.securitytoken.model.AssumeRoleResult;
/**
 * Class to call QuickSight AWS SDK to get url for dashboard embedding.
 */
public class GetQuicksightEmbedUrlIAMAuth {
    private static String IAM = "IAM";
    private final AmazonQuickSight quickSightClient;
    private final AWSSecurityTokenService awsSecurityTokenService;
    public GetQuicksightEmbedUrlIAMAuth(final AWSSecurityTokenService awsSecurityTokenService) {
        this.quickSightClient = AmazonQuickSightClientBuilder
                .standard()
                .withRegion(Regions.
```
`US_EAST_1`.getName())
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
        this.awsSecurityTokenService = awsSecurityTokenService;
    }
    public String getQuicksightEmbedUrl(
            final String accountId, // YOUR AWS ACCOUNT ID
            final String dashboardId, // YOUR DASHBOARD ID TO EMBED
            final String openIdToken, // TOKEN TO ASSUME ROLE WITH ROLEARN
            final String roleArn, // IAM USER ROLE TO USE FOR EMBEDDING
            final String sessionName, // SESSION NAME FOR THE ROLEARN ASSUME ROLE
            final boolean resetDisabled, // OPTIONAL PARAMETER TO ENABLE DISABLE RESET BUTTON IN EMBEDDED DASHBAORD
            final boolean undoRedoDisabled // OPTIONAL PARAMETER TO ENABLE DISABLE UNDO REDO BUTTONS IN EMBEDDED DASHBAORD
    ) throws Exception {
        AssumeRoleRequest request = new AssumeRoleRequest()
                .withRoleArn(roleArn)
                .withRoleSessionName(sessionName)
                .withTokenCode(openIdToken)
                .withDurationSeconds(3600);
        AssumeRoleResult assumeRoleResult = awsSecurityTokenService.assumeRole(request);
        AWSCredentials temporaryCredentials = new BasicSessionCredentials(
                assumeRoleResult.getCredentials().getAccessKeyId(),
                assumeRoleResult.getCredentials().getSecretAccessKey(),
                assumeRoleResult.getCredentials().getSessionToken());
        AWSStaticCredentialsProvider awsStaticCredentialsProvider = new AWSStaticCredentialsProvider(temporaryCredentials);
        GetDashboardEmbedUrlRequest getDashboardEmbedUrlRequest = new GetDashboardEmbedUrlRequest()
                .withDashboardId(dashboardId)
                .withAwsAccountId(accountId)
                .withIdentityType(IAM)
                .withResetDisabled(resetDisabled)
                .withUndoRedoDisabled(undoRedoDisabled)
                .withRequestCredentialsProvider(awsStaticCredentialsProvider);
        GetDashboardEmbedUrlResult dashboardEmbedUrl = quickSightClient.getDashboardEmbedUrl(getDashboardEmbedUrlRequest);
        return dashboardEmbedUrl.getEmbedUrl();
    }
}