# Safeguard your Amazon Bedrock app with a guardrail - Amazon SageMaker Unified Studio

**Source:** [https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/guardrails.html](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/guardrails.html)

---

Guardrails for Amazon Bedrock lets you implement safeguards for your Amazon Bedrock in SageMaker Unified Studio app based on your use cases and responsible AI policies. You can create multiple guardrails tailored to different use cases and apply them across multiple foundation models, providing a consistent user experience and standardizing safety controls across generative AI apps. You can configure denied topics to disallow undesirable topics and content filters to block harmful content in the prompts you send to a model and to the responses you get from a model. You can use guardrails with text-only foundation models. For more information, see Safeguard your Amazon Bedrock app with a guardrail.

You can use guardrails with Amazon Bedrock in SageMaker Unified Studio chat agent app and with flow apps. 
  With a chat agent app you can create guardrail component when
  you [create the chat agent app](./create-chat-app-with-components.html#chat-app-add-guardrail) or you can add a guardrail component 
  that you have previously created. For more
  information, see [Create an Amazon Bedrock guardrail component](./creating-a-guardrail-component.html).

With a flow app, you can add a guardrail to prompt nodes and to knowledge base nodes.

###### Topics

## Guardrail policies

  
  A guardrail consists of the following policies to avoid content that falls into undesirable or harmful categories.

- 
    Content filters – Adjust filter strengths to filter input prompts or model responses containing harmful content. 
- 
    Denied topics – You can define a set of topics that are undesirable in the context of your app. These topics will be blocked if detected in user queries or model responses. 

### Content filters

Guardrails in Amazon Bedrock in SageMaker Unified Studio support the following content filters to detect and filter harmful user inputs and FM-generated outputs.

- 
     **Hate**– Describes language or a statement that discriminates, criticizes, insults, denounces, or dehumanizes a person or group on the basis of an identity (such as race, ethnicity, gender, religion, sexual orientation, ability, and national origin).
- 
     **Insults**– Describes language or a statement that includes demeaning, humiliating, mocking, insulting, or belittling language. This type of language is also labeled as bullying.
- 
     **Sexual**– Describes language or a statement that indicates sexual interest, activity, or arousal using direct or indirect references to body parts, physical traits, or sex.
- 
     **Violence**– Describes language or a statement that includes glorification of or threats to inflict physical pain, hurt, or injury toward a person, group or thing.

Content filtering depends on the confidence classification of user inputs and FM
    responses across each of the four harmful categories. All input and output statements are
    classified into one of four confidence levels (NONE, LOW, MEDIUM, HIGH) for each
    harmful category. For example, if a statement is classified as
    *Hate* with HIGH confidence, the likelihood of the statement
    representing hateful content is high. A single statement can be classified across
    multiple categories with varying confidence levels. For example, a single statement
    can be classified as *Hate* with HIGH confidence, *Insults* with LOW confidence, *Sexual* with NONE confidence, and *Violence* with MEDIUM confidence.

For each of the harmful categories, you can configure the strength of the filters. The filter strength determines the degree of filtering harmful content. As you increase the filter strength, the likelihood of filtering harmful content increases and the probability of seeing harmful content in your app reduces. The following table shows the degree of content that each filter strength blocks and allows.

| Filter strength | Blocked content confidence | Allowed content confidence | 
|---|---|---|
| None | No filtering | None, Low, Medium, High | 
| Low | High | None, Low, Medium | 
| Medium | High, Medium | None, Low | 
| High | High, Medium, Low | None | 

### Denied topics

Guardrails can be configured with a set of denied topics that are undesirable in the context of your generative AI app. For example, a bank may want their online assistant to avoid any conversation related to investment advice or engage in conversations related to fraudulent activities such as money laundering.

You can define up to five denied topics. Input prompts and model completions will be evaluated against each of these topics. If one of the topics is detected, the blocked message configured as part of the guardrail will be returned to the user.

Denied topics can be defined by providing a natural language definition of the topic along with a few optional example phrases of the topic. The definition and example phrases are used to detect if an input prompt or a model completion belongs to the topic.

Denied topics are defined with the following parameters.

- 
     Name – The name of the topic. The name should be a noun phrase. Don't describe the topic in the name. For example: - 
       `Investment Advice`
 
- 
       
- 
     Definition – Up to 200 characters summarizing the topic content. The description should describe the content of the topic and its subtopics. ###### NoteFor best results, adhere to the following principles: - 
        Don't include examples or instructions in the description. 
- 
        Don't use negative language (such as "don't talk about investment" or "no content about investment"). 
 The following is an example topic description that you can provide: - 
       `Investment advice refers to inquires, guidance or recommendations regarding the management or allocation of funds or assets with the goal of generating returns or achieving specific financial objectives.`
 
- 
        
- 
     Sample phrases – A list of up to five sample phrases that refer to the topic. Each phrase can be up to 1,000 characters. An sample is a prompt or continuation that shows what kind of content should be filtered out. For example: - 
       `Is investing in the stocks better than bonds?`
- 
       `Should I invest in gold?`
 
-