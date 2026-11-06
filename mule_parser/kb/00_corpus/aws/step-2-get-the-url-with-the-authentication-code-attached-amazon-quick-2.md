# Step 2: Get the URL with the authentication code attached - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get-step-2.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get-step-2.html)

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

In the following section, you can find out how to authenticate your user and get the embeddable console session URL on your application server.

When a user accesses your app, the app assumes the IAM role on the user's behalf. Then it adds the user to Amazon Quick Sight, if that user doesn't already exist. Next, it passes an identifier as the unique role session ID.

Performing the described steps ensures that each viewer of the console session is uniquely provisioned in Amazon Quick Sight. It also enforces per-user settings, such as the row-level security and dynamic defaults for parameters.

The following examples perform the IAM authentication on the user's behalf. This code runs on your app server.

```
import com.amazonaws.auth.AWSCredentials;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.regions.Regions;
import com.amazonaws.services.quicksight.AmazonQuickSight;
import com.amazonaws.services.quicksight.AmazonQuickSightClientBuilder;
import com.amazonaws.services.quicksight.model.GetSessionEmbedUrlRequest;
import com.amazonaws.services.quicksight.model.GetSessionEmbedUrlResult;
/**
 * Class to call QuickSight AWS SDK to get url for session embedding.
 */
public class GetSessionEmbedUrlQSAuth {
    private final AmazonQuickSight quickSightClient;
    public GetSessionEmbedUrlQSAuth() {
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
            final String accountId, // YOUR AWS ACCOUNT ID
            final String userArn // REGISTERED USER ARN TO USE FOR EMBEDDING. REFER TO GETEMBEDURL SECTION IN DEV PORTAL TO FIND OUT HOW TO GET USER ARN FOR A QUICKSIGHT USER
    ) throws Exception {
        GetSessionEmbedUrlRequest getSessionEmbedUrlRequest = new GetSessionEmbedUrlRequest()
                .withAwsAccountId(accountId)
                .withEntryPoint("/start")
                .withUserArn(userArn);
        GetSessionEmbedUrlResult sessionEmbedUrl = quickSightClient.getSessionEmbedUrl(getSessionEmbedUrlRequest);
        return sessionEmbedUrl.getEmbedUrl();
    }
}
```