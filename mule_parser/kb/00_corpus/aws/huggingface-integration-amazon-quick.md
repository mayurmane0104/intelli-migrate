# HuggingFace integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/huggingface-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/huggingface-integration.html)

---

With HuggingFace integration in Amazon Quick, you can access machine learning models, datasets, and spaces through MCP server connectivity. This integration provides action capabilities for ML workflow operations and model management.

## What you can do

        
        HuggingFace integration provides action connector capabilities through MCP server connectivity:

- 
                Browse and download models from HuggingFace Hub 
- 
                Access and manage datasets 
- 
                Interact with HuggingFace Spaces 
- 
                Upload and manage your own models 
- 
                Run inference on hosted models 
- 
                Manage model repositories and versions 

## Available tools

        
        The HuggingFace MCP server typically provides these tools:

- 
                `search_models`- Search for models on HuggingFace Hub
- 
                `get_model_info`- Get detailed model information
- 
                `download_model`- Download models locally
- 
                `list_datasets`- List available datasets
- 
                `get_dataset_info`- Get dataset information
- 
                `run_inference`- Run inference on hosted models
- 
                `upload_model`- Upload models to Hub
- 
                `list_spaces`- List HuggingFace Spaces

###### Note

The specific tools and capabilities available through this MCP server may change over time. For the most current information about supported tools, features, and implementation details, check the official HuggingFace documentation and MCP server repository.

## Setting up HuggingFace integration

        
        HuggingFace integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](./mcp-integration.html).

You'll need:

- 
                HuggingFace account with appropriate permissions 
- 
                HuggingFace API token for authentication 

## Compatibility

        
        HuggingFace integration supports:

- 
                **Chat Agents:**Yes
- 
                **Flows:**Yes
- 
                **Knowledge Base:**No