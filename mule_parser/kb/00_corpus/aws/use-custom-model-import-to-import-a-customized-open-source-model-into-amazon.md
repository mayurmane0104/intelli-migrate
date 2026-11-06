# Use Custom model import to import a customized open-source model into Amazon Bedrock - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html)

---

[Gemma 4 E2B](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-google-gemma-4-e2b.html)

*12 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

You can create a custom model in Amazon Bedrock by using the Amazon Bedrock Custom Model Import feature to import Foundation Models that you have customized in other environments, such as Amazon SageMaker AI. For example, you might have a model that you have created in Amazon SageMaker AI that has proprietary model weights. You can now import that model into Amazon Bedrock and then use Amazon Bedrock features to make inference calls to the model.

You can use a model that you import with on demand throughput. Use the 
        [InvokeModel](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModel.html) or [InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html) operations to make inference calls to the model. For more information,
        see [Submit a single prompt with InvokeModel](./inference-invoke.html).

Custom model import is supported in the following regions:

eu-central-1

us-east-1

us-east-2

us-west-2

Make sure that your import and use of the models in Amazon Bedrock complies with the terms or licenses applicable to the models.

You can't use Custom Model Import with the following Amazon Bedrock features.

Batch inference

CloudFormation

With Custom Model Import you can create a custom model that supports the following patterns.

**Fine-tuned model**
                — You can customize the model weights using proprietary data, but retain the
                configuration of the base model. 

**Adaptation** You can customize the model
                to your domain for use cases where the model doesn't generalize well. Domain
                adaptation modifies a model to generalize for a target domain and
                deal with discrepancies across domains, such as a financial
                industry wanting to create a model which generalizes well on pricing. Another example is
                language adaptation. For example you could customize a model to generate responses
                in Portuguese or Tamil. Most often, this involves changes to the
                vocabulary of the model that you are using.

**Pretrained from scratch** — In addition to
                customizing the weights and vocabulary of the model, you can also change model
                configuration parameters such as the number of attention heads, hidden layers, or
                context length.

For information regarding pricing for custom model import, select the Custom Model Import tab in the Model pricing details section of [Amazon Bedrock pricing](https://aws.amazon.com/bedrock/pricing).

The model you import must be in one of the following architectures.

**Mistral** — A decoder-only Transformer
                    based architecture with Sliding Window Attention (SWA) and options for Grouped
                    Query Attention (GQA). For more information, see [Mistral](https://huggingface.co/docs/transformers/en/model_doc/mistral) 
                in the Hugging Face documentation. 

**Mixtral** — A decoder-only transformer model with sparse 
                Mixture of Experts (MoE) models. For more information, see [Mixtral](https://huggingface.co/docs/transformers/en/model_doc/mixtral) in the Hugging Face documentation. 

                **Flan ** — An
                enhanced version of the T5 architecture, an encoder-decoder based transformer model.
                For more information, see [Flan T5](https://huggingface.co/docs/transformers/model_doc/flan-t5) in the Hugging Face documentation. 

**Llama 2, Llama3, Llama3.1, Llama3.2, Llama 3.3, and Mllama** — An improved version of Llama
                with Grouped Query Attention (GQA). For more information, see [Llama 2](https://huggingface.co/blog/llama2), 

**GPTBigCode** — An optimized version of GPT-2 with Multi-Query action. 
                For more information, see [GPTBigCode](https://huggingface.co/docs/transformers/en/model_doc/gpt_bigcode) in the Hugging Face documentation.

**Qwen2, Qwen2.5, Qwen2-VL, Qwen2.5-VL, Qwen3** — An LLM family with comprehensive multimodal perception and high speed vision encoding.
                Any model using the Qwen2, Qwen2-VL, and Qwen2.5-VL architectures can be imported. For Qwen3 architecture, only Qwen3ForCausalLM and Qwen3MoeForCausalLM are supported. Converse is also not supported for Qwen3 models.
                For more information, see [Qwen2](https://huggingface.co/collections/Qwen/qwen2-6659360b33528ced941e557f), 

**GPT-OSS** — OpenAI based GPT-OSS
                architecture. Amazon Bedrock supports both 20B and 120B based custom models. GPT-OSS model architecture is only supported in the US East (N. Virginia) region.

The size of the imported model weights must be less than 100GB for multimodal models and 200GB for text models.

The maximum positional embeddings or the maximum context length supported by the model should be less than 128K.

Amazon Bedrock supports transformer version 4.51.3. Ensure that you are using transformer version 4.51.3 when you fine tune your model.

Custom Model Import does not support embedding models.

You import a model into Amazon Bedrock by creating a model import job in the Amazon Bedrock console or API. In the job you specify the Amazon S3 URI for the source of the model files. During model training, the import job automatically detects your model's architecture.

You need to supply the model files in the
                Hugging Face weights format. You can create the files by using the
            Hugging Face transformer library. To create model files for a Llama
            model, see [convert_llama_weights_to_hf.py](https://github.com/huggingface/transformers/blob/main/src/transformers/models/llama/convert_llama_weights_to_hf.py). To create the files for a Mistral AI model,
            see 

To import the model from Amazon S3, you minimally need the following files that the Hugging Face transformer library creates.

**.safetensor** — the model weights in
                *Safetensor* format. Safetensors is a format created by
                Hugging Face that stores a model weights as tensors. You must store the tensors
                for your model in a file with the extension `.safetensors`. For more
                information, see [Safetensors](https://huggingface.co/docs/safetensors/en/index). For information about converting model weights to
                Safetensor format, see 

**config.json** — For examples, 
            see [LlamaConfig](https://huggingface.co/docs/transformers/model_doc/llama2#transformers.LlamaConfig)
            and 

Amazon Bedrock overrides llama3 `rope_scaling` value with the following values:

`original_max_position_embeddings=8192`

`high_freq_factor=4`

`low_freq_factor=1`

`factor=8`

**tokenizer_config.json**  For an example,
                see [LlamaTokenizer](https://huggingface.co/docs/transformers/model_doc/llama2#transformers.LlamaTokenizer).

**tokenizer.json **

**tokenizer.model** 

Amazon Bedrock Custom Model Import supports the following tokenizers. You can use these tokenizers with any model.

T5Tokenizer

T5TokenizerFast

LlamaTokenizer

LlamaTokenizerFast

CodeLlamaTokenizer

CodeLlamaTokenizerFast

GPT2Tokenizer

GPT2TokenizerFast

GPTNeoXTokenizer

GPTNeoXTokenizerFast

PreTrainedTokenizer

PreTrainedTokenizerFast

Qwen2Tokenizer

Qwen2TokenizerFast

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.