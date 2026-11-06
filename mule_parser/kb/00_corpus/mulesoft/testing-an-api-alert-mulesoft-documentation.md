# Testing an API Alert | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/api-manager/latest/test-alert-task](https://docs.mulesoft.com/api-manager/latest/test-alert-task)

---

# Testing an API Alert

This procedure describes how to test a request count alert. This procedure requires the following preparation:

- 
Design an API. 
- 
Publish the API to Exchange. 
- 
In API Manager, manage the API from Exchange. 
- 
Deploy a proxy of the API instance to CloudHub. 
- 
Apply the Rate Limiting Policy to the API as follows: Request Count greater than 1 for at least 1 consecutive minute. 
- 
Add the alert described in the topic about how to add an alert. 
- 
Call the API. 
- 
Recall the API two more times (reload the page). Check that `API calls exceeded`appears if you called and recalled the API within the 1 minute period. Any additional page reload operations within the 1 minute period have no effect.
- 
Check that users, who you selected for email notification when you added the alert, actually receive email notifications. 
- 
Check that the alert was resolved.