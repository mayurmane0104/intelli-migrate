# Setting up service provider–initiated federation with Quick Enterprise edition - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/setup-quicksight-to-idp.html](https://docs.aws.amazon.com/quick/latest/userguide/setup-quicksight-to-idp.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators | 

###### Note

IAM identity federation doesn't support syncing identity provider groups with Amazon Quick.

After you have finished configuring your identity provider with AWS Identity and Access Management (IAM), you can set up service provider–initiated sign in through Amazon Quick Enterprise Edition. For Quick-initiated IAM federation to work, you need to authorize Quick to send the authentication request to your IdP. A Quick administrator can configure this by adding the following information provided by the IdP:

- 
                The IdP URL – Quick redirects users to this URL for authentication. 
- 
                The relay state parameter – This parameter relays the state that the browser session was in when it was redirected for authentication. The IdP redirects the user back to the original state after authentication. The state is provided as a URL. 

The following table shows the standard authentication URL and relay state parameter for redirecting the user to the Quick URL that you provide.

| Identity provider | Parameter | Authentication URL | 
|---|---|---|
| Auth0 | 
                                 | 
                                 | 
| Google accounts | 
                                 | 
                                 | 
| Microsoft Azure | 
                                 | 
                                 | 
| Okta | 
                                 | 
                                 | 
| PingFederate | 
                                 | 
                                 | 
| PingOne | 
                                 | 
                                 | 

Amazon Quick supports connecting to one IdP per AWS account. The configuration page
            in Amazon Quick provides you with test URLs based on your entries, so you can test the
            settings before you turn on the feature. To make the process even more seamless,
            Amazon Quick provides a parameter (`enable-sso=0`) to temporarily turn off
            Amazon Quick initiated IAM federation, in case you need to disable it
            temporarily.

## To set up Amazon Quick as a service provider that can initiate IAM federation for an existing IdP

            - 
                    Make sure that you already have IAM federation set up in your IdP, in IAM, and Amazon Quick. To test this setup, check if you can share a dashboard with another person in your company's domain. 
- 
                    Open Amazon Quick, and choose **Manage Amazon Quick**from your profile menu at upper right.To perform this procedure, you need to be a Amazon Quick administrator. If you aren't, you can't see **Manage Amazon Quick**under your profile menu.
- 
                    Choose **Single sign-on (IAM federation)**from the navigation pane.
- 
                    For **Configuration**,**IdP URL**, enter the URL that your IdP provides to authenticate users.
- 
                    For **IdP URL**, enter the parameter that your IdP provides to relay state, for example`RelayState`. The actual name of the parameter is provided by your IdP.
- 
                    
                    Test signing in: - 
                            To test signing in with your identity provider, use the custom URL provided in **Test starting with your IdP**. You should arrive at the start page for Amazon Quick, for example https://quicksight.aws.amazon.com/sn/start.
- 
                            To test signing in with Amazon Quick first, use the custom URL provided in **Test the end-to-end experience**. The`enable-sso`parameter is appended to the URL. If`enable-sso=1`, IAM federation attempts to authenticate.
 
- 
                            
- 
                    Choose **Save**to keep your settings.

## To enable service provider–initiated IAM federation IdP

            - 
                    Make sure your IAM federation settings are configured and tested. If you're not sure about the configuration, test the connection by using the URLs from the previous procedure. 
- 
                    Open Amazon Quick, and choose **Manage Amazon Quick**from your profile menu.
- 
                    Choose **Single sign-on (IAM federation)**from the navigation pane.
- 
                    For **Status**, choose**ON**.
- 
                    Verify that it's working by disconnecting from your IdP and opening Amazon Quick. 

## To disable service provider initiated IAM federation

            - 
                    Open Amazon Quick, and choose **Manage Amazon Quick**from your profile menu.
- 
                    Choose **Single sign-on (IAM federation)**from the navigation pane.
- 
                    For **Status**, choose**OFF**.