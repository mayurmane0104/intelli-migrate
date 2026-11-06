# Chat agent context sources and best practices - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/agent-knowledge-sources-best-practices.html](https://docs.aws.amazon.com/quick/latest/userguide/agent-knowledge-sources-best-practices.html)

---

When creating custom chat agents in Amazon Quick, you have multiple options to influence chat agent behavior and frame chat agent workflows. The way you configure chat agent context and instructions significantly impacts how your chat agent performs and responds to user interactions. Understanding when to use instructions, reference documents, and spaces is crucial for creating effective chat agents that meet your specific business needs and deliver consistent, reliable results. The following sections outline how to best use chat agent context and knowledge for your use case.

###### Topics

## Types of agent context

            Amazon Quick provides three distinct methods for configuring chat agent behavior, each serving different purposes in chat agent development. Understanding how each method processes content and when to use them forms the foundation of effective chat chat agent configuration.

The three context types available in Amazon Quick are:

- 
                    **Persona instructions**– High-level guidance that Amazon Quick enhances using generative AI
- 
                    **Reference documents**– Documents that provide exact instructions and remain active in the chat agent's memory
- 
                    **Spaces**– Collections of searchable Amazon Quick resources and documents from which chat agents retrieve information to answer questions

The following section details what these are and the best practices of using them.

### Chat agent persona instructions

You provide chat agent persona instructions in the **Persona
                        instructions** field when you create your custom chat agent. These
                    persona instructions are refined using generative AI to ensure that it works
                    with all the chat features and the resources configured for the chat agent. This
                    approach is ideal when you want the system to build upon your foundational
                    direction. When you use persona instructions, Amazon Quick uses generative
                        AI to interpret and expand your persona instructions in the
                    backend, augment simple guidance with additional context and capabilities,
                    optimize the prompt for better chat agent performance, and enhance effectiveness
                    through AI-driven improvements.

**Use persona instructions to:**

- 
                        Provide high level guidance on behavior and goals, which are enhanced by Amazon Quick AI to customize agent responses 
- 
                        Instruct how to leverage reference documents for detailed interactions 
- 
                        Provide general guidance on use of spaces and action connectors in its responses 

This approach works best for general-purpose chat agents and exploratory use cases where you want to benefit from AI assistance in chat agent design.

###### Note

The AI enhancement process may modify your original wording and structure to improve chat agent performance. Critical guidelines that must remain unchanged should be placed in reference documents instead.

### Chat agent reference documents

Reference documents provide specific process and response templates that the chat agents need to follow. These reference documents are part of the chat agent's permanent context and go hand-in-hand with persona instructions and response style to inform its overall behavior.

Reference documents provide complete control over chat agent behavior by preserving your content exactly as written. This approach is essential when precision and consistency are paramount. When you upload reference documents, Amazon Quick preserves precise wording and specific instructions, maintains exact formatting and structure, provides direct control over chat agent behavior, and ensures consistency across all interactions.

**Use reference documents when you need:**

- 
                        Exact control where precise wording and specific instructions must be preserved 
- 
                        Brand consistency with specific tone, terminology, or response formats 
- 
                        Complex workflows with multi-step processes that must follow exact sequences 
- 
                        Predictable behavior with consistent responses across all interactions 

**Supported file formats:**

- 
                        `.pdf`,`.txt`,`.html`,`.md`– Instructions, templates, and guidelines
- 
                        `.csv`– Reference data, lookup tables, and examples
- 
                        `.doc`,`.docx`– Detailed process documentation

You can attach upto 10 files of total size 50 MB as reference documents. Amazon Quick extracts text from these documents and applies a 100K character limit after processing.

###### File prioritization and behavior

- 
                            Behavioral frameworks and reference data from files remain active even when users attach alternative content. 
- 
                            Response templates may be temporarily adjusted if users provide conflicting formatting instructions. 

Reference documents serve as the chat agent's operating manual, providing the behavioral framework that remains constant across all user interactions with the chat agent.

### Chat agents and spaces

Spaces provide dynamic, searchable knowledge repositories that chat agents query during conversations to retrieve specific information. When you link spaces to chat agents, Amazon Quick chat agents look for answers within the space to generate responses. Spaces excel at managing organizational knowledge that evolves over time, allowing multiple team members to contribute and update information while maintaining appropriate security boundaries through Amazon Quick's permission system.

Use spaces with chat agents for:

- 
                        Enabling chat agents to search and retrieve current business data 
- 
                        Providing chat agents access to organizational knowledge repositories 
- 
                        Allowing chat agents to respect existing permission boundaries 
- 
                        Connecting chat agents to collaborative document collections 
- 
                        Giving chat agents access to regularly updated information 
- 
                        Enabling chat agents to query live dashboards and datasets 

Spaces function as the chat agent's dynamic knowledge layer, enabling real-time access to organizational information while maintaining security boundaries and collaborative workflows.