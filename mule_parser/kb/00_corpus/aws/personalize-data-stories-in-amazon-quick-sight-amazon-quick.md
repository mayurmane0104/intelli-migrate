# Personalize data stories in Amazon Quick Sight - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/working-with-stories-personalize.html](https://docs.aws.amazon.com/quick/latest/userguide/working-with-stories-personalize.html)

---

User location and job-related information from your IAM Identity Center instance are leveraged to generate personalized data stories that are more relevant to authors and readers. For example, when an author in the US issues the prompt “Write a business strategy focusing on a plan on how to increase the revenue in my location", insights related to the US in the data story's narrative are automatically included. If the author wants the data story to focus on another country such as Canada, they can specify this in the prompt.

For personalization to work, you must add country and job title for users in the IAM Identity Center
            instance that is connected to your Quick account. For more information, see
                [Add
                users to your IAM Identity Center directory](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html) in the IAM Identity Center User Guide.

User data in your IAM Identity Center instance is connected to your application environment by
            default. This means that all data stories are personalized by default. You can choose to
                [opt out of personalization](https://docs.aws.amazon.com/quicksuite/latest/userguide/qs-q-manage-personalization) at any time in the Account settings menu in the
            QuickSight administration console.

###### Note

Personalization in data stories is currently available in the US East (N. Virginia) and US West (Oregon) AWS Regions.