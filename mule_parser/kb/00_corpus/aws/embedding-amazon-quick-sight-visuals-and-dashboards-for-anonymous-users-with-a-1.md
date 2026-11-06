# Embedding Amazon Quick Sight visuals and dashboards for anonymous users with a 1-click embed code - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-1-click-public.html](https://docs.aws.amazon.com/quick/latest/userguide/embedded-analytics-1-click-public.html)

---

| Applies
                    to:Enterprise Edition | 

You can embed a visual or dashboard in public sites using the embed code that you get when you share the visual or dashboard in Amazon Quick Sight. You can also turn on public sharing by using the Amazon Quick Sight console and automatically grant access to a shared visual or dashboard to anyone on the internet.

Following, you can find how to turn on public sharing for a visual or dashboard and embed the visual or dashboard for anyone on the internet to see. In both cases, you do this by using the 1-click embed code.

## Before you start

                Before you get started, make sure of the following:

- 
                        Your internet browser settings contain one of the following to allow communication between the popup and the iframe that sharing uses: - 
                                Native support for the Mozilla Broadcast Channel API. For more information, see [Broadcast Channel API](https://developer.mozilla.org/en-US/docs/Web/API/Broadcast_Channel_API)in the Mozilla documentation.
- 
                                IndexedDB support. 
- 
                                LocalStorage support. 
 
- 
                                
- 
                        Your internet browser's "block all cookies" settings is turned off. 

## Step 1: Turn on public access for the dashboard

                For anyone on the internet to access your embedded visual or dashboard, first
                    turn on public access for the dashboard. Visual permissions are determined at
                    the dashboard level. To grant access to embedded visuals, grant access to the
                    dashboard that the visual belongs to. For more information, see [Granting anyone on the internet access to an Amazon Quick Sight dashboard](./share-a-dashboard-grant-access-anyone.html).

## Step 2: Put the domain where you want to embed the visual or dashboard on your allow list

                To embed visuals and dashboards in a public application, wiki, or portal, make sure that the domain where you're embedding it is on the allow list for your Amazon Quick Sight account.

## Step 3: Get the embed code

                Use the following procedure to get the visual or dashboard embed code.

###### To get the dashboard embed code

- 
                        Open the published dashboard in Amazon Quick Sight and choose **Share**at upper right. Then choose**Share dashboard**.
- 
                        In the **Share dashboard**page that opens, choose**Copy embed code**at upper left.The embed code is copied to your clipboard and is similar to the following. The `quicksightdomain``<iframe width="960" height="720" src="https://``quicksightdomain`/sn/ embed/share/accounts/`accountid`/dashboards/`dashboardid`"> </iframe>

###### To get the visual embed code

- 
                        Open the published dashboard in Amazon Quick Sight and choose the visual that you want to embed. Then open the on-visual menu in the top right corner of the visual and choose **Embed visual**.
- 
                        In the **Embed visual**pane that opens, choose**Copy code**.The embed code is copied to your clipboard and is similar to the following. The `quicksightdomain``<iframe width="600" height="400" src="https://``quicksightdomain`/sn/embed/share/accounts/`111122223333`/dashboards/`DASHBOARDID`/sheets/`SHEETID`>/visuals/`VISUALID`"> </iframe>

## Step 4: Paste the embed code into an HTML page, wiki page, or portal

                Use the following procedure to paste the embed code into an HTML page, wiki page, or portal.

###### To paste the embed code

- 
                        Open the HTML code for the location where you want to embed the visual or dashboard, and paste the embed code in. The following example shows what this might look like for an embedded dashboard. The `quicksightdomain``<!DOCTYPE html> <html> <body> <h2>Example.com - Employee Portal</h2> <h3>Current shipment stats</h3> <iframe width="960" height="720" src="https://``quicksightdomain`/sn/ embed/share/accounts/`accountid`/dashboards/`dashboardid`"> </iframe> </body> </html>The following example shows what this might look like for an embedded visual. The `quicksightdomain``<!DOCTYPE html> <html> <body> <h2>Example.com - Employee Portal</h2> <h3>Current shipment stats</h3> <iframe width="600" height="400" src="https://``quicksightdomain`/sn/embed/share/accounts/`111122223333`/dashboards/`DASHBOARDID`/sheets/`SHEETID`>/visuals/`VISUALID`"> </iframe> </body> </html>

If your public-facing applications are built on Google Sites, open the page on Google Sites and then paste the embed code using the embed widget.

Make sure that the following domains in Amazon Quick Sight are on your allow list when you embed in Google Sites:

- 
                        `https://googleusercontent.com`(turns on subdomains)
- 
                        `https://www.gstatic.com`
- 
                        `https://sites.google.com`

After you embed the visual or dashboard in your application, anyone who can
                    access your application can access the embedded visual or dashboard. To update a
                    dashboard that's shared with the public, see [Updating a publicly shared dashboard](./share-a-dashboard-grant-access-anyone-update.html). To turn off
                    public sharing, see [Turning off public sharing settings](./share-a-dashboard-grant-access-anyone-no-share.html). 

When you turn off public sharing, no one from the internet can access a dashboard or dashboards that you have embedded on a public application or shared with a link. The next time anyone tries to view such a dashboard from the internet, they receive a message that they don't have access to view it.