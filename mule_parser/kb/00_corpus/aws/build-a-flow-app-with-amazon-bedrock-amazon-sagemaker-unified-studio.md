# Build a flow app with Amazon Bedrock - Amazon SageMaker Unified Studio

**Source:** [https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-flows-app.html](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/create-flows-app.html)

---

A flow app let you link prompts, supported foundational models, and other units of work, such as an Amazon Bedrock knowledge base, together and create generative AI workflows for end-to-end solutions. For example, you could create flow apps to do the following.

- 
   **Create a playlist of music**– Create a flow connecting a prompt node and knowledge base node. Provide the following prompt to generate a playlist:`Create a playlist`. After processing the prompt, the flow queries a knowledge base to look up information about local bands, such as the length of songs and genre of music. The flow then generates a playlist based the information in the knowledge base.
- 
   **Troubleshoot using the error message and the ID of the resource that is causing the error**– The flow looks up the possible causes of the error from a documentation knowledge base, pulls system logs and other relevant information about the resource, and updates the faulty configurations and values for the resource.

In this section you create a flow app that generates a playlist of music from a knowledge base of songs by fictional local bands.

To create a flow app, you use the  *flow
   builder* which is a tool in
   Amazon Bedrock in SageMaker Unified Studio to build and edit flow apps through a visual interface. You use the visual
   interface to drag and drop nodes onto the interface and configure inputs and outputs for these
   nodes to define your flow. 

![Example Amazon Bedrock in SageMaker Unified Studio flow.](/images/sagemaker-unified-studio/latest/userguide/images/bedrock/create-flow-kb-prompt-out.png) 

     
     
   In your flow you can apply logical conditions to direct the output from a node to different destinations. You can then run the flow within Amazon Bedrock in SageMaker Unified Studio and view the output.

The following list introduces you to the basic elements of a flow.

- 
    **Flow**– A flow is a construct consisting of a name, description, permissions, a collection of nodes, and connections between nodes. When you run a flow, the input to the flow is sent through each node of the flow until the flow emits the final output from an output node.
- 
    **Node**– A node is a step inside a flow. For each node, you configure its name, description, input, output, and any additional configurations. The configuration of a node differs based on its type.For information about the types of nodes that Amazon Bedrock in SageMaker Unified Studio supports, see [Flow nodes available in Amazon Bedrock](./nodes.html).
- 
    **Connection**– There are two types of connections used in flow apps:- 
      A **data connection**is drawn between the output of one node (the*source node*) and the input of another node (the*target node*) and sends data from an upstream node to a downstream node. In the flow builder, data connections are solid lines.
- 
      A **conditional connection**is drawn between a condition in a condition node and a downstream node and sends data from the node that precedes the condition node to a downstream node if the condition is fulfilled. In the flow builder, conditional connections are dotted lines.
 
- 
      
- 
    **Expressions**– An expression defines how to extract an input from the whole input entering a node. To learn how to write expressions, see[Define inputs with expressions](./flows-expressions.html).

If you want to use your flow app outside of Amazon SageMaker Unified Studio, you can export and deploy
  the app to an AWS account. For more information, see [Use your app outside of Amazon SageMaker Unified Studio](./app-export.html).

###### Warning

Generative AI may give inaccurate responses. Avoid sharing sensitive information. Chats may be visible to others in your organization.