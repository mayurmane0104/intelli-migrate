# Create an Amazon Bedrock Knowledge Base component - Amazon SageMaker Unified Studio

**Source:** [https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/creating-a-knowledge-base-component.html](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/creating-a-knowledge-base-component.html)

---

You can create a knowledge base as a component in an Amazon Bedrock in SageMaker Unified Studio project. You then add
        the knowledge base to an chat agent app or flow app. Alternatively, you can create a
        knowledge base when you [design](./create-chat-app-with-components.html#chat-app-add-data-source) the app. When
        you create a knowledge base, you choose a data source, such as a local file or web crawler.

In this section you learn about the various data sources that you can use and how to create a knowledge base component.

###### Topics

You can create a Knowledge base as a component in an Amazon Bedrock in SageMaker Unified Studio project. If you are creating an app, you can also create a Knowledge Base when you configure the app. When you create a Knowledge Base, you choose your data source, an embeddings model for transforming your data into vectors, and a vector store to store and manage the vectors. You can also specify how the Knowledge Base should preprocess data from the data source, either through chunking or parsing. The following procedure demonstrates how to create a Knowledge Base in Amazon Bedrock in SageMaker Unified Studio.

###### To create a Knowledge Base

- 
    Navigate to the Amazon SageMaker Unified Studio landing page by using the URL from your administrator. 
- 
    Access Amazon SageMaker Unified Studio using your IAM or single sign-on (SSO) credentials. For more information, see [Access Amazon SageMaker Unified Studio](./getting-started-access-the-portal.html).
- 
    In the left navigation pane, under **Generative AI**, choose**AI apps**.
- From the project selector dropdown at the top of the page, choose the project that you want to use. 
- 
    In the left pane, choose **Asset gallery**.
- Choose - **My components**.
- 
            In the **Components**section, choose**Create component**and then**Knowledge Base**. The**Create Knowledge Base**pane is shown.
- 
            For **Name**, enter a name for the Knowledge Base.
- 
            For **Description**, enter a description for the Knowledge Base.
- 
            In **Add data sources**, do one of the following:- 
                    Use a document as a data source by doing the following: - 
                            Choose **Local file**.
- 
                            Choose **Click to upload**and upload the document that you want the Knowledge Base to use. Alternatively, add your source documents by dragging and dropping the document from your computer.
 For more information, see [Use a Local file as a data source](./data-source-document.html).
- 
                            
- 
                    Use a web crawler as a data source by doing the following: - 
                            Choose **Web crawler**.
- 
                            Provide the **Source URLs**of the URLs you want to crawl. You can add up to 9 additional URLs by selecting**Add Source URLs**. By providing a source URL, you are confirming that you are authorized to crawl its domain.
- 
                            (Optional) Choose **Specify web crawler configs**to make the following optional configuration changes:- 
                                    **Website domain range**. Set the domain that you want the Knowledge Base to crawl. For more information, see[Website domain range for crawling URLs](./data-source-document-web-crawler.html#ds-sync-scope).
- 
                                    **Maximum throttling of crawling speed**. Set the speed at which the Knowledge Base crawls through the source URLs. For more information, see[Throttle crawling speed](./data-source-document-web-crawler.html#ds-throttle-crawling).
- 
                                    **URL regex filter**. Set regex filters for including (**Include patterns**) or excluding**Exclude patterns**URLS from the web crawl. For more information, see[Use a URL regex filter to include or exclude URLs](./data-source-document-web-crawler.html#ds-inclusion-exclusion).
- Choose - **Back**to leave the web crawler configuration pane.
 
- 
                                    
 
- 
                            
 
- 
                    
- 
            In **Configurations**, under**Data storage and processing**, do the following:- For - **Embeddings model**, select a foundation model from the drop down to use for transforming your data into vector embeddings.
- For - **Embedding type**and- **Vector dimensions**, select an option from the dropdown to optimize accuracy, cost, and latency. Your options for embedding types and vector dimensions may be limited depending on the embeddings model that you chose.- ###### Note- Amazon OpenSearch Serverless is the only vector store that supports binary vector embeddings. Floating-point vector embeddings are supported by all available vector stores. 
- For - **Vector store**choose from one of the following options:- **Vector engine for Amazon OpenSearch Serverless**‐ Provides contextually relevant responses across billions of vectors in milliseconds. Supports searches combined with text-based keywords for hybrid requests.
- **Amazon S3 Vectors**‐ Optimizes cost-effectiveness, durability, and latency for storage of large, long-term vector data sets. Amazon S3 Vectors does not support web crawler data sources. Supports metadata for enhanced search and filtering capabilities.- ###### Note- Amazon S3 Vectors for Amazon Bedrock in SageMaker Unified Studio is available in all AWS Regions where both Amazon Bedrock and Amazon S3 Vectors are available. For information about regional availability of Amazon S3 Vectors, see - [Amazon S3 Vectors](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-vectors-regions-quotas.html)in the- *Amazon S3 User Guide*.
- **Amazon Neptune Analytics (GraphRAG)**‐ Provides high-performance graph analytics and graph-based Retrieval Augmented Generation (GraphRAG) solutions. You must have access to Claude 3 Haiku in order to use this vector store. Contact your administrator if you do not have the necessary permissions.
 - Once you select an option for your vector store, Amazon Bedrock in SageMaker Unified Studio will create the vector store on your behalf. 
- 
            For **Chunking strategy**, choose either**Default**,**Fixed sized**,**Hierarchical**,**Semantic**, or**None**. These options represent different methods for breaking down data into smaller segments before embedding.
- 
            For **Parsing strategy**, choose either**Bedrock default parser**or**Foundation model as a parser**. If you choose**Foundation model as a parser**, do the following:- 
                    For **Choose a foundation model for parsing**select your preferred foundation model. You can only choose models that your administrator has enabled for parsing. If you don't see a suitable model, contact your administrator.
- 
                    (Optional) Overwrite the **Instructions for the parser**to suit your specific needs.
 
- 
                    
 
- 
            Choose **Create**to create the Knowledge Base.
- 
            Use the Knowledge Base in an app, by doing one of the following: - 
                    If your app is a chat agent app, do [Add an Amazon Bedrock Knowledge Base component to a chat agent app](./add-kb-component-chat-app.html).
- 
                    If your app is a flow app, do [Add a Knowledge Base component to a flow app](./add-kb-component-prompt-flow-app.html).
 
-