# UI agents - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/ui-agents.html](https://docs.aws.amazon.com/quick/latest/userguide/ui-agents.html)

---

UI agent is a native agent that understands natural language instructions to perform complex browser actions. It can autonomously navigate websites, click, type, read data, and produce structured outputs optimized for downstream automation steps. Example use cases include summarizing products on a webpage or fetching data by navigating websites.

## Properties

        
        - Title
- Name of the step/UI agent 
- Instructions
- 
                    In this field you write the prompt for the agent in natural language. Best practices while writing the prompt: - Be clear and explicit about what you want. 
- Structure the prompt. Start with mentioning the 'Task' or 'Role' first and then 'Instructions' to achieve the task with numbered steps 
- Add constraints (e.g., only review the products section) and specify when to stop/end (e.g., stop when you find the relevant info) 
- Provide positive and negative (don't do this) examples 
- Specify length requirements (e.g., less that 100 words) or output format (e.g., date in MM/DD/YY format) clearly 
 Wrap the text in triple quotes (""") to write multiline prompts. For example: `"""Task: Locate the company's latest annual report. * Visit the provided URL. * Look for the annual report. The report may be titled 'Annual Report', 'Financial Report', 'Year in Review', or similar variations..."""`
- Structured Output (optional)
- Agent Response: Name of the variable to assign the output of this operation 

## How to configure structured output fields

        
        **Adding fields**

- Click Add field to create a new output field 
- Enter the Output name - this becomes the JSON property name 
- Select the Type from the dropdown 
- Check Required if the field must always be present 
- Add a Description to guide the AI agent 

**Field types**

- *String*- Text values (Names, descriptions, summaries)
- *Number*- Numeric values (Counts, scores, percentages)
- *Boolean*- True/false values (Status flags, yes/no questions)
- *Object*- Nested structure (Complex data groupings)
- *Array*- List of items (Tags, categories, multiple values)
- *File*- File references (Document attachments, images)
- *Data table*- Tabular data (Structured datasets, reports)

**Working with complex types**

Objects and Arrays can contain nested fields:

- Click the expand arrow (▶) next to Object or Array fields 
- Use Add field within the nested structure 
- Keep nesting to 2-3 levels maximum for optimal performance 

**Example configuration**

Here's a simple configuration for summarizing customer feedback:

```
{
  "orderId": "12345",
  "numberOfOrders": 3,
  "hasShipped": true,
  "orderDetails": {
    "quantity": 2,
    "productName": "ABC",
  },
  "tags": ["electronics", "urgent"]
}
```
This structure would be configured as:

- orderId (String, required) 
- numberOfOrders (Number, required) 
- hasShipped (Boolean, required) 
- orderDetails (Object, required) - quantity (Number, required) 
- productName (String, required) 
 
- tags (Array of Strings, Optional) 

**Best practices**

- Use descriptive field names - Help the AI understand what data to extract 
- Add clear descriptions - Provide context for complex fields 
- Mark critical fields as required - Ensure essential data is always present 
- Limit nesting depth - Keep structures simple for better performance 
- Test your configuration - Verify the output matches your expectations by running the agent step and verifying the response. 

**Important notes**

- JSON Knowledge: Unfamiliar with JSON? Learn the basics at json.org 
- No validation: Currently, the system doesn't validate output structure - ensure your automation handles missing or malformed data