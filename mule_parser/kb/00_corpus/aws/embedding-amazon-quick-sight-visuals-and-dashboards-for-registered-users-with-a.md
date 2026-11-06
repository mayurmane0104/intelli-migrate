# Embedding Amazon Quick Sight visuals and dashboards for registered users with a 1-click embed code - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-1-click.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-1-click.html)

---

| Applies
                    to:Enterprise Edition | 

You can embed a visual or dashboard in your internal application for registered
                users of your Amazon Quick Sight account. You do so using the embed code that you get
                when you share the dashboard or from the **Embed visual** menu in
                Amazon Quick Sight. You don't have to run the Amazon Quick Sight embedding API to
                generate the embed code. You can copy the embed code from Amazon Quick Sight and
                paste it in your internal application's HTML code.

When users and groups (or all users on your Amazon Quick Sight account) who have access to the dashboard that you want to embed or that holds the visual that you want to embed access your internal application, they're prompted to sign in to the Amazon Quick Sight account with their credentials. After they are authenticated, they can access the visual or dashboard on their internal page. If you have single sign-on enabled, users aren't prompted to sign in again.

Following, you can find descriptions about how to embed a visual or dashboard for registered users using the visual or dashboard embed code.

## Before you start

                Before you get started, make sure of the following:

- 
                        Your internet browser settings contain one of the following to allow communication between the popup and the iframe: - 
                                Native support for the Mozilla Broadcast Channel API. For more information, see [Broadcast Channel API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API)in the Mozilla documentation.
- 
                                IndexedDB support. 
- 
                                LocalStorage support. 
 
- 
                                
- 
                        Your internet browser's "block all cookies" settings is turned off. 

## Step 1: Grant access to the dashboard

                For users to access your embedded dashboard, grant them access to view it. You
                    can grant individual users and groups access to a dashboard, or you can grant
                    everyone in your account access. Visual permissions are determined at the
                    dashboard level. To grant access to embedded visuals, grant access to the
                    dashboard that the visual belongs to. For more information, see [Granting access to a dashboard](./share-a-dashboard.html).

## Step 2: Put the domain where you want to embed the visual or dashboard on your allow list

                To embed visuals and dashboards in your internal application, make sure that
                    the domain where you're embedding is allow-listed in your Amazon Quick Sight
                    account. For more information, see [Allow listing static domains](./manage-domains.html#embedding-static).

## Step 3: Get the embed code

                Use the following procedure to get the visual or dashboard embed code.

###### To get the dashboard embed code

- 
                        Open the published dashboard in Amazon Quick Sight and choose **Share**at upper right. Then choose**Share dashboard**.
- 
                        In the **Share dashboard**page that opens, choose**Copy embed code**at upper left.The embed code is copied to your clipboard and is similar to the following. The `quicksightdomain``<iframe width="960" height="720" src="https://``quicksightdomain`/sn/embed/share/accounts/`accountid`/dashboards/`dashboardid`?directory_alias=account_directory_alias"> </iframe>

###### To get the visual embed code

- 
                        Open the published dashboard in Amazon Quick Sight and choose the visual that you want to embed. Then open the on-visual menu at the upper right of the visual and choose **Embed visual**.
- 
                        In the **Embed visual**pane that opens, choose**Copy code**.The embed code is copied to your clipboard and is similar to the following. The `quicksightdomain``<iframe width="600" height="400" src="https://``quicksightdomain`/sn/embed/share/accounts/`111122223333`/dashboards/`DASHBOARDID`/sheets/`SHEETID`>/visuals/`VISUALID`"> </iframe>

## Step 4: Paste the code into your internal application's HTML page

                Use the following procedure to paste the embed code into your internal application's HTML page

###### To paste the code in your internal application's HTML page

- 
                        Open the HTML code for any page where you want to embed the dashboard and paste the embed code in. The following example shows what this might look like for an embedded dashboard. The `quicksightdomain``<!DOCTYPE html> <html> <body> <h2>Example.com - Employee Portal</h2> <h3>Current shipment stats</h3> <iframe width="960" height="720" src="https://``quicksightdomain`/sn/embed/share/accounts/`accountid`/dashboards/`dashboardid`?directory_alias=account_directory_alias"> </iframe> </body> </html>The following example shows what this might look like for an embedded visual. The `quicksightdomain``<!DOCTYPE html> <html> <body> <h2>Example.com - Employee Portal</h2> <h3>Current shipment stats</h3> <iframe width="600" height="400" src="https://``quicksightdomain`/sn/embed/share/accounts/`111122223333`/dashboards/`DASHBOARDID`/sheets/`SHEETID`>/visuals/`VISUALID`?directory_alias=account_directory_alias"> </iframe> </body> </html>

For example, let's say that you want to embed your visual or dashboard in an internal Google Sites page. You can open the page on Google Sites and paste the embed code in an embed widget.

If you want to embed your visual or dashboard in an internal Microsoft SharePoint site, you can create a new page and then paste the embed code in an Embed web part.