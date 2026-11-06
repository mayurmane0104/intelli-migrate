# MuleSoft Vectors Connector 1.1 | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mulesoft-vectors-connector/latest](https://docs.mulesoft.com/mulesoft-vectors-connector/latest)

---

# MuleSoft Vectors Connector 1.1

Anypoint Connector for MuleSoft Vectors (MuleSoft Vectors Connector) provides access to a broad number of external vector stores and databases. MuleSoft Vectors Connector can be used with other connectors (for example, MuleSoft Inference Connector or Einstein AI Connector) and provides seamless access to vector stores for implementing smarter search or Retrieval Augmented Generation (RAG) use cases.

For information about compatibility and fixed issues, see the MuleSoft Vectors Connector release notes.

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements and global elements in a Mule flow 
- 
How to create a Mule app using Anypoint Code Builder or Anypoint Studio 

Before creating an app, you must have:

- 
Java 17 (required for compilation and runtime) 
- 
Apache Maven 
- 
Credentials to access the MuleSoft Vectors Connector target resources 
- 
Anypoint Platform 
- 
The latest versions of Anypoint Code Builder or Anypoint Studio 

## Key Features

MuleSoft Vectors Connector provides:

- 
Accelerated AI-powered application development 
- 
Simplified vector database integration 
- 
Easy-to-build semantic search and RAG experiences without managing complex vector infrastructure 

| Data is processed in in-memory, so if you do parallel processing (such as running multiple flows in one go), you might encounter an out-of-memory issue. For example, if you process 1 MB files in three flows, around 3 MB files will be loaded in-memory. This is due to the nature of Apache Tika and LangChain4j libraries. | 

## Supported Vector Stores

MuleSoft Vectors Connector supports these vector stores:

- 
Azure AI Search (beta) 
- 
Chroma (beta) 
- 
Milvus (beta) 
- 
OpenSearch (beta) 
- 
PGVector (beta) PGVector is not FIPS-compliant. 
- 
Pinecone (beta) 
- 
Qdrant (beta) 
- 
MongoDB Atlas (beta) 
- 
Ephemeral File (beta) 

### Supported Operations by Vector Stores

This table provides a detailed view of operation support across all vector stores:

| Vector Store | Storing Metadata | Filtering by Metadata | Removing Embeddings | List All Embeddings | 
|---|---|---|---|---|
| 
 | Yes | Yes | Yes | Yes | 
| 
 | Yes | Yes | Yes | Yes | 
| 
 | Yes | Yes | Yes | Yes | 
| 
 | Yes | Yes | Yes | No | 
| 
 | Yes | Yes | Yes | Yes | 
| 
 | Yes | Yes | No | No | 
| 
 | Yes | Yes | Yes | Yes | 
| 
 | Yes | Yes | Yes | Yes | 
| 
 | Yes | Yes | Yes | Yes | 

## Supported Model Providers

MuleSoft Vectors Connector supports these model providers to generate embeddings:

- 
Azure OpenAI 
- 
Azure Vision AI (beta) 
- 
Einstein 
- 
Hugging Face (beta) 
- 
Mistral AI (beta) 
- 
Nomic (beta) 
- 
Ollama (beta) 
- 
OpenAI 

### Supported Embedding Types by Model Providers

This table provides a detailed view of embedding type support across all model providers:

| Model Provider | Text Embedding | Image Embedding | Video Embedding | 
|---|---|---|---|
| 
 | Yes | No | No | 
| 
 | Yes | No | No | 
| 
 | Yes | No | No | 
| 
 | Yes | No | No | 
| 
 | Yes | No | No | 
| 
 | Yes | No | No | 
| 
 | Yes | No | No | 
| 
 | Yes | No | No | 

| To keep pace with the rapidly evolving AI landscape, certain vector stores and LLMs are marked as beta. These are early-stage integrations that may change based on stability, demand, or provider updates. You can explore them but should do so with awareness that support might be limited and subject to change. | 

## Supported Storage Options

- 
**Local**: Load data from application local storage
- 
**Azure Blob Storage**
- 
**Amazon S3**

## Next Step

After you complete the prerequisites, you are ready to create an app and configure the connector using [Anypoint Studio](mulesoft-vectors-connector-studio) or [Anypoint Code Builder](mulesoft-vectors-connector-config-acb).

## See Also

- 
[Salesforce Help](https://help.salesforce.com)