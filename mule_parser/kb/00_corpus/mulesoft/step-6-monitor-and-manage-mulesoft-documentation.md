# Step 6. Monitor and Manage | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/api-led-operate](https://docs.mulesoft.com/general/api-led-operate)

---

`INFO [hello-world-impl].get:\greeting Received greeting request for name: World`text

# Step 6. Monitor and Manage

In this final step, you’ll learn how to monitor your deployed API using Runtime Manager, your operations dashboard for CloudHub applications.

## Step 6.1: Access Runtime Manager

- 
From Anypoint Platform, navigate to [Runtime Manager](https://anypoint.mulesoft.com/cloudhub/#/console/home/applications).
- 
Make sure you’re viewing the **Sandbox**environment.
- 
Select your **hello-world-impl**application.The dashboard opens. 

## Step 6.2: View Application Health

The dashboard shows real-time metrics:

- **Status**
- 
Running (green) means your API is healthy. 
- **Replicas**
- 
Shows **1/1**(1 running replica out of 1 expected).
- **Last Updated**
- 
The last time the application was updated. 
- **Mule Messages**
- 
The number of Mule messages the application has processed. Send a few test requests from Postman and watch the **Mule Messages**graph update.
- **Average Response Time**
- 
The average response time of the application. 
- **Errors**
- 
The number of errors the application has encountered. 

## Step 6.3: View Application Logs

Logs help you troubleshoot and understand what your application is doing.

- 
In Runtime Manager, click **Logs**in the left menu.
- 
You’ll see recent log entries. 
- 
Send a request to your API from Postman. 
- 
Refresh the logs to see your Logger message: 
- 
Use log filters: - **Log Level**
- 
Filter by INFO, WARN, or ERROR. 
- **Search**
- 
Find specific text. 
- **Time Range**
- 
View logs from the last 30 days. Logs show every request, error, and Logger message from your application. 
 

## Step 6.4: Understand Your Application URL

Your application URL has this structure:

`https://hello-world-impl-jsmith.<space-domain>.cloudhub.io/api/greeting`text

- 
`hello-world-impl-jsmith`: Your unique application name
- 
`<space-domain>`: Your Shared Space’s domain
- 
`/api/greeting`: Your API endpoint path

This URL is publicly accessible and automatically includes:

- 
HTTPS/TLS encryption 
- 
Load balancing across replicas 
- 
Distributed Denial-of-Service (DDoS) protection 
- 
Automatic scaling 

## Step 6.5: Test from Anywhere

Your API is now accessible from any device:

- 
Test the API from your phone’s browser. 
- 
Share the URL with teammates. 
- 
Call the API from other applications. 
- 
Use the API in front-end web apps. 

Try it! Open a browser on any device and visit:

`https://your-app-url.cloudhub.io/api/greeting?name=World`text

You’ll see your greeting in the browser.

## What You Learned

Congratulations! You’ve completed the full API development lifecycle:

- 
Designed an API spec with Anypoint Code Builder 
- 
Developed the API implementation in Anypoint Code Builder 
- 
Tested the API locally with debugging tools 
- 
Deployed the API to CloudHub 2.0 
- 
Verified and monitored the API in Runtime Manager 

## Clean Up (Optional)

To remove your tutorial application and free up resources:

- 
In Runtime Manager, click your application. 
- 
Click **Settings**>**Delete Application**.
- 
Confirm deletion. 

Your application is stopped and removed from CloudHub 2.0.

## Learn More

Ready to build more complex APIs? Explore:

- 
[API-Led Connectivity Patterns](https://www.salesforce.com/blog/api-led-connectivity/?bc=OTH)

[Step 5. Deploy the API to CloudHub 2.0](api-led-deploy)