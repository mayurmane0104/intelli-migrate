# Amazon Bedrock in SageMaker Unified Studio - Amazon SageMaker Unified Studio

**Source:** [https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/bedrock.html)

---

With Amazon Bedrock in SageMaker Unified Studio you can build generative AI apps that use Amazon Bedrock models and features, such as knowledge bases and guardrails, without needing to write any code.

To use Amazon Bedrock in SageMaker Unified Studio, you must be a member of an Amazon SageMaker Unified Studio domain. Your organization will provide you with login details. Contact your administrator if you don't have your login details.

Your organization's administrator determines which Amazon Bedrock models and features you have access to. Contact your organization's administrator if you need access to a model or feature that you don't currently have access to.

###### Note

If you are administrator and need information about managing Amazon Bedrock in SageMaker Unified Studio, see [Amazon Bedrock in SageMaker Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/amazon-bedrock-ide.html) in the *Amazon SageMaker Unified Studio admin guide*. 

## Discover Amazon Bedrock in SageMaker Unified Studio playgrounds

    Amazon Bedrock in SageMaker Unified Studio provides various options for discovering and experimenting with Amazon Bedrock models and apps.

With the model catalog you can find information about the Amazon Bedrock models that are available to you and decide which model is
      suitable for your use case. Different models have different capabilities and modalities. For more information, see [Find serverless models with the Amazon Bedrock model catalog](./model-catalog.html).

Amazon Bedrock in SageMaker Unified Studio offers two playgrounds for you to experiment with Amazon Bedrock models in: the [chat](./bedrock-explore-chat-playground.html) playground and the [image and video](./explore-image-playground.html) playground. With the chat playground, 
      you can generate text responses from a model by sending text and image prompts. You can also interact with chat agent apps that have been shared with you. 
      With the image and video playground, you can generate and edit images and videos by sending text and image prompts to a suitable model. For more information, see [Experiment with the Amazon Bedrock playgrounds](./bedrock-playgrounds.html).

## Build generative AI apps

    Within an Amazon SageMaker Unified Studio project, you can create two types of generative AI apps: a 
      [chat agent app](./create-chat-app.html) and a [flow app](./create-flows-app.html). You
      can use a chat agent app to chat with an Amazon Bedrock model through a conversational interface, typically by sending prompts (text or image) and
      receiving responses. You can use a flows ap to link prompts, supported Amazon Bedrock models, and other units of work, such as a knowledge base,
      together and create generative AI workflows.

Apps that you create with Amazon Bedrock in SageMaker Unified Studio can integrate the following Amazon Bedrock features.

- 
        [Data sources](./data-sources.html)
- 
        [Guardrails](./guardrails.html)
- 
        [Functions](./functions.html)
- 
        [Prompts](./prompt-mgmt.html)

Within a project, you can use the *asset gallery* to organize the
      prompts and components that you use for an app. A component is an Amazon Bedrock knowledge base,
      guardrail, or function.

A critical part of creating a generative AI app is deciding which model to use and which
      model settings to use. To help you decide, you can [evaluate](./evaluation.html)
      a model for different task types.

If you work on a team, you can collaborate by [sharing](./app-share.html) an
      app with other team members. You can also [export](./app-export.html) an app so
      that you can use the app in your own environment.

You can clone the repository that holds your Amazon SageMaker Unified Studio project files to your computer. However, we don't recommend making changes to your project's files on your local desktop, as this may break your project's apps and components.