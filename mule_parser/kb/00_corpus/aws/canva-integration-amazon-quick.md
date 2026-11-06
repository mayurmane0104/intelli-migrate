# Canva integration - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/canva-integration.html](https://docs.aws.amazon.com/quick/latest/userguide/canva-integration.html)

---

With Canva integration in Amazon Quick, you can create, edit, and manage designs and visual content through MCP server connectivity. This integration provides action capabilities for design operations and content creation.

## What you can do

        
        Canva integration provides action connector capabilities through MCP server connectivity:

- 
                Create new designs from templates 
- 
                Edit existing designs and presentations 
- 
                Manage design assets and media 
- 
                Export designs in various formats 
- 
                Share designs and collaborate with team members 

## Available tools

        
        The Canva MCP server typically provides these tools:

- 
                `comment-on-design`- Add a comment on a Canva design. You need to provide the design ID and the message text. The comment will be added to the design and visible to all users with access to the design.
- 
                `create-design-from-candidate`- Create a new Canva design from a generation job candidate ID. This converts an AI-generated design candidate into an editable Canva design. If successful, returns a design summary containing a design ID that can be used with the editing_transaction_tools. To make changes to the design, first call this tool with the candidate_id from generate-design results, then use the returned design_id with start-editing-transaction and subsequent editing tools.
- 
                `create-folder`- Create a new folder in Canva. You can create it at the root level or inside another folder.
- 
                `export-design`- Export a Canva design, doc, presentation, whiteboard, videos and other Canva content types to various formats (PDF, JPG, PNG, PPTX, GIF, MP4). You should use the get-export-formats tool first to check which export formats are supported for the design. This tool provides a download URL for the exported file that you can share with users. Always display this download URL to users so they can access their exported content.
- 
                `generate-design`- Generate designs with AI. Use the 'query' parameter to tell AI what you want to create.
- 
                `get-design`- Get detailed information about a Canva design, such as a doc, presentation, whiteboard, video, or sheet. This includes design owner information, title, URLs for editing and viewing, thumbnail, created/updated time, and page count. This tool doesn't work on folders or images. You must provide the design ID, which you can find by using the search-designs or list-folder-items tools.
- 
                `get-design-content`- Get the text content of a doc, presentation, whiteboard, social media post, sheet, and other designs in Canva. Use this when you only need to read text content without making changes. IMPORTANT: If the user wants to edit, update, change, translate, or fix content, use start-editing-transaction instead as it shows content AND enables editing. You must provide the design ID, which you can find with the search-designs tool. When given a URL to a Canva design, you can extract the design ID from the URL. Do not use web search to get the content of a design as the content is not accessible to the public. Example URL: https://www.canva.com/design/{design_id}.
- 
                `get-design-pages`- Get a list of pages in a Canva design, such as a presentation. Each page includes its index and thumbnail. This tool doesn't work on designs that don't have pages (e.g. Canva docs). You must provide the design ID, which you can find using tools like search-designs or list-folder-items. You can use 'offset' and 'limit' to paginate through the pages. Use get-design to find out the total number of pages, if needed.
- 
                `get-export-formats`- Get the available export formats for a Canva design. This tool lists the formats (PDF, JPG, PNG, PPTX, GIF, MP4) that are supported for exporting the design. Use this tool before calling export-design to ensure the format you want is supported.
- 
                `import-design-from-url`- Import a file from a URL as a new Canva design
- 
                `list-comments`- Get a list of comments for a particular Canva design. Comments are discussions attached to designs that help teams collaborate. Each comment can contain replies, mentions, and can be marked as resolved or unresolved. You need to provide the design ID, which you can find using the search-designs tool. Use the continuation token to get the next page of results, if needed. You can filter comments by their resolution status (resolved or unresolved) using the comment_resolution parameter.
- 
                `list-folder-items`- List items in a Canva folder. An item can be a design, folder, or image. You can filter by item type and sort the results. Use the continuation token to get the next page of results if needed.
- 
                `list-replies`- Get a list of replies for a specific comment on a Canva design. Comments can contain multiple replies from different users. These replies help teams collaborate by allowing discussion on a specific comment. You need to provide the design ID and comment ID. You can find the design ID using the search-designs tool and the comment ID using the list-comments tool. Use the continuation token to get the next page of results, if needed.
- 
                `move-item-to-folder`- Move items (designs, folders, images) to a specified Canva folder
- 
                `reply-to-comment`- Reply to an existing comment on a Canva design. You need to provide the design ID, comment ID, and your reply message. The reply will be added to the specified comment and visible to all users with access to the design.
- 
                `resize-design`- Resize a Canva design to a preset or custom size. The tool will provide a summary of the new resized design, including its metadata.
- 
                `search-designs`- Search docs, presentations, videos, whiteboards, sheets, and other designs in Canva. Use 'query' parameter to search by title or content. If 'query' is used, 'sortBy' must be set to 'relevance'. Filter by 'any' ownership unless specified. Sort by relevance unless specified. Use the continuation token to get the next page of results, if needed.
- 
                `search-folders`- Search the user's folders and folders shared with the user based on folder names and tags. Returns a list of matching folders with pagination support.
- 
                `upload-asset-from-url`- Upload an asset (e.g. an image, a video) from a URL into Canva If the API call returns "Missing scopes: [asset:write]", you should ask the user to disconnect and reconnect their connector. This will generate a new access token with the required scope for this tool.

## Setting up Canva integration

        
        Canva integration uses MCP server connectivity to provide action capabilities. For detailed setup instructions, see [Model Context Protocol (MCP) integration](./mcp-integration.html).

You'll need:

- 
                Canva account with appropriate permissions 

## Compatibility

        
        Canva integration supports:

- 
                **Chat Agents:**Yes
- 
                **Flows:**Yes
- 
                **Knowledge Base:**No