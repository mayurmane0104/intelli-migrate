# Prerequisites for Quick Flows - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/prerequisites-for-quick-flows.html](https://docs.aws.amazon.com/quick/latest/userguide/prerequisites-for-quick-flows.html)

---

Before you can create and use Amazon Quick Flows, you need to ensure that your Amazon Quick administrator has completed the following prerequisites.

## Administrator setup requirements

	  
    Your Quick administrator must complete the following tasks before you can create and use Quick Flows:

- 
        Set up and configure Quick for your organization. For more information, see [Setting up and signing into Amazon Quick](./setting-up.html).
- 
        (Optional) Restrict access to flows for specific users using custom permissions. 

For browser and region requirements, see [Supported browsers](./supported-browsers.html).

## Required permissions

    
    Permissions to create, run, share, and govern flows are determined by user subscriptions and any configured custom permissions. For more information, see [Managing Quick subscriptions](./managing-subscriptions.html) and [Managing user access inside Amazon Quick](./managing-users.html).

## Amazon Bedrock model access

    
    Quick Flows uses Amazon Bedrock models for AI reasoning in the General knowledge step. Your administrator must enable access in custom permissions for output refinement in flows using Bedrock models. For more information, see [General knowledge](./ai-response-steps.html#general-knowledge-step).

## Next steps

    
    After ensuring that all prerequisites are met, you can:

- 
        Learn about key concepts in Quick Flows. See [Terminology and key concepts](./terminology-and-key-concepts.html).
- 
        Create your first flow. See [Creating flows](./creating-flows.html).