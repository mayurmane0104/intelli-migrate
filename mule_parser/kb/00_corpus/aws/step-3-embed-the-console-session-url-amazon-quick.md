# Step 3: Embed the console session URL - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get-step-3.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-full-console-for-authenticated-users-get-step-3.html)

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

In the following section, you can find out how you can use the [Amazon Quick Sight embedding SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) (JavaScript) to embed the console
                session URL from step 3 in your website or application page. With the SDK, you can
                do the following: 

- 
                    Place the console session on an HTML page. 
- 
                    Pass parameters into the console session. 
- 
                    Handle error states with messages that are customized to your application. 

Call the `GetSessionEmbedUrl` API operation to get the URL that you can
                embed in your app. This URL is valid for 5 minutes, and the resulting session is
                valid for 10 hours. The API operation provides the URL with an
                    `auth_code` that enables a single-sign on session. 

The following shows an example response from
                `get-dashboard-embed-url`.

```
//The URL returned is over 900 characters. For this example, we've shortened the string for
//readability and added ellipsis to indicate that it's incomplete.
{
     "Status": "200",
     "EmbedUrl": "https: //dashboards.example.com/embed/620bef10822743fab329fb3751187d2d...",
     "RequestId": "7bee030e-f191-45c4-97fe-d9faf0e03713"
}           
```
Embed this console session in your webpage by using the Amazon Quick Sight [Embedding
                    SDK](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk) or by adding this URL into an iframe. If you set a fixed height and
                width number (in pixels), Amazon Quick Sight uses those and doesn't change your
                visual as your window resizes. If you set a relative percent height and width,
                Amazon Quick Sight provides a responsive layout that is modified as your window size
                changes. By using the Amazon Quick Sight Embedding SDK, you can also control
                parameters within the console session and receive callbacks in terms of page load
                completion and errors. 

The following example shows how to use the generated URL. This code is generated on your app server.

```
<!DOCTYPE html>
<html>
<head>
    <title>Basic Embed</title>
    <script src="./quicksight-embedding-js-sdk.min.js"></script>
    <script type="text/javascript">
        var dashboard;
        function embedDashboard() {
            var containerDiv = document.getElementById("embeddingContainer");
            var options = {
                // replace this dummy url with the one generated via embedding API
                url: "https://
```
`us-east-1`.quicksight.aws.amazon.com/sn/dashboards/dashboardId?isauthcode=true&identityprovider=quicksight&code=authcode",  
                container: containerDiv,
                scrolling: "no",
                height: "700px",
                width: "1000px",
                footerPaddingEnabled: true
            };
            dashboard = QuickSightEmbedding.embedDashboard(options);
        }
    </script>
</head>
<body onload="embedDashboard()">
    <div id="embeddingContainer"></div>
</body>
</html>For this example to work, make sure to use the Amazon Quick Sight Embedding SDK to load the embedded console session on your website using JavaScript. To get your copy, do one of the following:

- 
                    Download the [Amazon Quick Sight embedding SDK](https://github.com/awslabs/amazon-quicksight-embedding-sdk#step-3-create-the-quicksight-session-object)from GitHub. This repository is maintained by a group of Amazon Quick Sight developers.
- 
                    Download the latest embedding SDK version from [https://www.npmjs.com/package/amazon-quicksight-embedding-sdk](https://www.npmjs.com/package/amazon-quicksight-embedding-sdk).
- 
                    If you use `npm`for JavaScript dependencies, download and install it by running the following command.`npm install amazon-quicksight-embedding-sdk`