# Knowledge bases - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/knowledge-base-integrations.html](https://docs.aws.amazon.com/quick/latest/userguide/knowledge-base-integrations.html)

---

A knowledge base is an organized, indexed collection of documents or content from data sources optimized for generative AI-powered retrieval and question answering. Whether your team stores documentation in Confluence, collaborates through SharePoint, or manages files in cloud storage, you can bring all this information into one unified search experience by creating knowledge bases.

The built-in integrations can be set up with just a few clicks to sync your data in Quick and make it effortless to tap into your organization's knowledge across Google Drive, OneDrive, Confluence, SharePoint, S3, and Web Crawler. Whether your team stores documentation in Confluence, collaborates through SharePoint, or manages files in cloud storage, you can bring all this information into one unified search experience with the help of knowledge bases.

## How knowledge bases work

        Knowledge base is an indexed collection of documents or content from data sources such
            as Google Drive, optimized for generative AI-powered retrieval and question answering.
            Multiple knowledge bases can be created from the same source, and all can reside within
            a shared Quick Index. For example, if you sync two folders from Google Drive and create
            two knowledge bases — one for “Policy Documents” to answer queries such as *“What’s our refund policy”* and one for “Customer feedback”
            to answer queries such as *“What are the common customer
                complaints”* — both can be part of the same index. Quick distinguishes
            between them using the knowledge base id, so queries can be filtered to retrieve only
            the relevant documents from the desired knowledge base. This allows users to organize,
            secure, and retrieve information relevant to different domains or use cases, even though
            the underlying data is indexed together.

Your knowledge bases can be used individually or shared with team members through Amazon Quick spaces. Our coarse-grained access control enables security at the knowledge base level, ensuring that users only receive information from knowledge bases they're authorized to access.

### Creation process

You can create knowledge bases while setting up a new data access integration and use existing integrations to create additional knowledge bases:

- 
                    **Data access integration setup**- Connect to your external data source
- 
                    **Content selection**- Choose which content to include through filters and scope settings
- 
                    **Indexing**- Amazon Quick processes and indexes the selected content
- 
                    **Availability**- The knowledge base becomes available for use in spaces and by AI agents

### Capabilities

Each knowledge base provides the following capabilities:

- 
                    **Content indexing**- Processes text, documents, and structured data from external sources
- 
                    **Semantic search**- Enables AI-powered search across indexed content
- 
                    **Automatic synchronization**- Keeps content up-to-date with configurable sync schedules
- 
                    **Coarse-grained access control**- Ensures that users only receive information from knowledge bases they're authorized to access.
- 
                    **Multi-space usage**- Can be used across multiple spaces and by different AI agents

## General workflow

        
        The typical workflow for working with knowledge bases follows these steps:

- 
                **Set up data source integration**- Connect to your external application (such as SharePoint, Google Drive, or Confluence) with appropriate authentication. For more information, see[Integration-specific guides](./integration-guides.html).
- 
                **Create a knowledge base**- You can create a knowledge base while configuring your new integration. Configure your content filters by setting up include filters, file type restrictions, and folder selections to focus on relevant content.
- 
                **Set sync schedule**- Data refresh frequency is set to daily by default. You can edit the sync frequency to configure how often the knowledge base should be updated with new content from the source.
- 
                **Monitor and manage**- Review sync status, manage access permissions.

## Common configuration settings

        
        Knowledge bases share common configuration patterns across different data source integrations. Understanding these settings helps you optimize content indexing and manage sync behavior effectively.

###### Note

While these configuration options are available across most integrations, specific settings and available options may vary depending on your chosen data source integration.

### Service principal for knowledge base operations

If you use a customer-managed key (CMK) as your default CMK and Q data key (see
                    [Encrypting your Amazon Quick data with AWS Key Management Service customer-managed keys](./customer-managed-keys.html)), Amazon Quick accesses your AWS KMS key
                using the `qbusiness.amazonaws.com` and
                `quicksight.amazonaws.com` service principals during knowledge base sync
                operations.

###### Note

Ensure that any policies governing access to your CMK permit both the
                        `qbusiness.amazonaws.com` and
                        `quicksight.amazonaws.com` service principals.

### File size and content limits

Configure file size limits to optimize processing performance and manage storage costs. The specific limits vary by content type and are displayed in the console when you configure your knowledge base.

- **Standard text documents**
- 
                        Applies to documents like PDFs, Word files, and text files. File size limit is 500 MB. 
- **Video files**
- 
                        Available when video processing is enabled. Supported formats include `.mp4`,`.mov`,`.m4v`. File size limit is 10 GB (10240 MB). Quick Index supports up to**10 video files per GB of storage**. If your use case requires higher video volumes, please open a ticket with AWS support to extend this limit.
- **Audio files**
- 
                        Available when audio processing is enabled. Supported formats include `.mp3`,`.wav`,`.m4a`,`.flac`, and`.ogg`. Limit is 2 GB (2048 MB) for audio files.###### NoteFiles with extracted text that exceeds the 30 MB system limit are not indexed, regardless of the original file size. The maximum amount of text that can be extracted from a single document is 30 MB. 
- **Images**
- 
                        Quick Index applies the following limits for images: - 
                                **Per-document limit**: 500 images per document
- 
                                **Per-GB limit**: 10K images per GB of index storage
- 
                                **Per-index limit**: 2M images per index
 If your use case requires higher image volumes, please open a ticket with AWS support to extend these limits. 
- 
                                

### Sync schedule and safeguards

Configure how often your knowledge base updates and protect against unintended content deletion:

#### Sync frequency

Data refresh frequency is set to daily by default. You can edit the sync frequency to configure how often the knowledge base should update with new content from the source

#### Document deletion safeguard

Protect your indexed content from accidental mass deletion by setting a maximum deletion percentage threshold. If a sync job would delete more documents than your threshold allows, the deletion phase is skipped, preserving your existing indexed content.

This safeguard protects against temporary network issues, permission changes, or source system problems that might make content temporarily unavailable.

#### Maximum sync duration

Each sync run has a maximum runtime of 14 days. If a sync run is still in
                    progress after 14 days, Amazon Quick ends the run with a status of
                        **FAILED** and the following error
                    message:

If your sync run reaches this limit, edit your knowledge base to narrow the sync scope. For example, apply include or exclude filters, restrict the file types or folders being crawled, or split the content across multiple knowledge bases. For web crawler data sources, consider using the Web Search feature instead when your goal is to chat with large public websites.