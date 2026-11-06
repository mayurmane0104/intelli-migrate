# Retrieve data and generate AI responses with Amazon Bedrock Knowledge Bases - Amazon Bedrock

**Source:** [https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)

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

While foundation models have general knowledge, you can further improve their responses by using Retrieval Augmented Generation (RAG). RAG is a technique that uses information from data sources to improve the relevancy and accuracy of generated responses. With Amazon Bedrock Knowledge Bases, you can integrate proprietary information into your generative-AI applications. When a query is made, a knowledge base searches your data to find relevant information to answer the query. The retrieved information can then be used to improve generated responses. You can build your own RAG-based application by using the capabilities of Amazon Bedrock Knowledge Bases.

With Amazon Bedrock Knowledge Bases, you can:

Answer user queries by returning relevant information from data sources.

Use retrieved information from data sources to help generate an accurate and relevant response to user queries.

Augment your own prompts by feeding the returned relevant information into the prompt.

Include citations in the generated response so the original data source can be referenced and accuracy can be checked.

Include documents with copious visual resources, from which images can be extracted and retrieved in responses to queries. If you generate a response based on the retrieved data, the model can deliver additional insights based on these images.

Search using images as queries to find visually similar content, or combine text and images in queries for more precise results using multimodal embedding models.

Convert natural language into queries (such as SQL queries) that are customized for structured databases. These queries are used to retrieve data from structured data stores.

Update your data sources and ingest the changes into the knowledge base directly so they can be immediately accessed.

Use reranking models to influence the results that are retrieved from your data source.

Include the knowledge base in an [Amazon Bedrock Agents](./agents.html)
                workflow.

To set up a knowledge base, you must complete the following general steps:

(Optional) If you connect your knowledge base to an unstructured data source, set
                up your own [supported vector
                    store](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup.html) to index the vector embeddings representation of your data. You
                can skip this step if you plan to use the Amazon Bedrock console to create an Amazon OpenSearch Serverless vector
                store for you.

Connect your knowledge base to an unstructured or structured data source.

Sync your data source with your knowledge base.

Set up your application or agent to do the following:

Query the knowledge base and return relevant sources.

Query the knowledge base and generate natural language responses based on the retrieved results.

(If you query a knowledge base connected to a structured data store) Transform a query into a structured data language-specific query (such as an SQL query).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

RAG augments prompts using external data embeddings, enabling domain-specific tasks via JumpStart models.

Rerank API improves query relevance, reduces cost latency; supports Knowledge Bases RAG via Retrieve RetrieveAndGenerate operations.

Multimodal RAG systems leverage Titan embeddings and Bedrock Knowledge Bases, enabling Nova models query mixed text-image content efficiently.

Amazon Bedrock enables generative AI development, now featuring GPT-5 agentic coding, Claude Opus 4.7, IAM cost attribution.

Optimize LLM prompts via few-shot techniques, RAG, templates, conversational API calls reduce hallucinations.

Amazon Bedrock foundation model details, IDs, Regions, modalities, inference parameters consolidated models at glance.