# Deploy an Amazon Bedrock chat agent app - Amazon SageMaker Unified Studio

**Source:** [https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/app-deploy.html](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/app-deploy.html)

---

Deployment of a chat agent app happens for the following reasons:

- 
            You want to use a chat agent app as an [agent node](./flows-use-chat-agent.html)within a flow app. Before you can do so, you must first deploy the chat agent app.
- 
            You want to [share](./app-share.html)a chat agent app with other users. When you share the app, Amazon Bedrock deploys the chat agent app for you.

During deployment Amazon Bedrock creates, or reuses, an *alias* for the chat agent app
        and creates a new *version* of the chat agent app. 

**Aliases and versions**

An alias is associated with a specific version of a chat agent app. When you use a chat agent app as an agent node in a flow app, you configure the agent node in the flow app with the alias of the chat agent app. When you share an app, the recipient can access the version of the app that is associated with the alias. You can create up to 8 aliases for a chat agent app.

A version is a snapshot of a chat agent app at the time you deploy the app. Amazon Bedrock creates a new version of your chat agent app each time you deploy the app. Amazon Bedrock creates versions in numerical order, starting from 1.

With aliases, you can switch efficiently between [different versions](./app-change-alias-version.html) of a chat agent app, without having to update the
        flow apps that use the chat agent app. For example, if you discover an issue with the
        current version of your chat agent app, you can quickly update agent nodes that use the
        current version to a previous version. 

The following procedure shows you how to deploy a chat agent app. After deploying
            the app, you can then use the app as a [node
                agent](./flows-use-chat-agent.html) in a flow app. You don't need to deploy a chat agent app before
            sharing the app, as Amazon Bedrock deploys the app for you. For more information, see Deploy an Amazon Bedrock chat agent app.

###### To deploy a chat agent app

- 
    Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator. 
- 
    Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](./getting-started-access-the-portal.html).
- From the project selector dropdown at the top of the page, choose the project that you want to use. 
- In the left navigation pane, under - **Generative AI**, choose- **AI apps**.
- 
                Open the app that you want to deploy. 
- 
                Choose **Deploy**.
- 
                In **App description**enter a short description for the app. Make sure that that the description lets users understand the purpose of the app.
- 
                Assign an alias by doing one of the following: - 
                        Choose **Create a new alias**to create a new alias. Then enter an name and optional description for the alias.
- 
                        Choose **Select an existing alias**to use an existing alias. Then select the existing alias that you want to use.
 
- 
                        
- 
                Choose **Deploy**to deploy the app. It might take a few seconds to deploy the app.
- 
                To use the deployed app, select **Working draft**in the configuration pane and then select the name of the alias that you used to deploy the app.
- 
                Enter a prompt to try your deployed app.