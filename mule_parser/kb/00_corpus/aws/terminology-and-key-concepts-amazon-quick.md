# Terminology and key concepts - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/terminology-and-key-concepts.html](https://docs.aws.amazon.com/quick/latest/userguide/terminology-and-key-concepts.html)

---

Understanding the core terminology and concepts helps you effectively create, run, share, and maintain flows within your organization.

## Steps and @ references

            A flow is made up of steps that each perform a specific function, such as calling an action, querying your data, or searching the web. Most steps are controlled through a natural language prompt.

Steps pass data to each other using @ references. When you write a prompt inside a step, type @ to see a menu of previous steps. Select one to include that step's output as context in your prompt. For example, if Step 1 collects a customer's issue and Step 3 needs to classify it, Step 3's prompt might say: "Classify the issue in @Customer Issue by severity (low, medium, high)."

The available step types are organized into the following groups:

- AI responses
- 
                        - **Chat agent**— Gets a response from a custom agent and can take actions in connected applications.
- **Research**— Invokes Amazon Quick Research to generate research reports as part of your workflow.
- **Web Search**— Generates responses using internet search results.
- **General knowledge**— Gets a response directly from Amazon Bedrock models, with configurable response preferences for speed or versatility.
- **UI Agent**— Navigates public websites that do not require a login and performs tasks like scrolling to find information or filling forms.
- **Create Image**— Generates AI images from text inputs.
 
- Flow logic
- 
                        - **Reasoning Group**— Groups related steps together with natural language instructions that define conditions, loops, validation, and execution order.
 
- Data insights
- 
                        - **Quick data**— Retrieves responses from spaces and knowledge bases.
- **Dashboards and topics**— Gets insights from Amazon Quick Sight dashboards and topics.
 
- Actions
- 
                        - **Application actions**— Performs read or write operations in connected third-party applications through pre-built connectors.
 
- User input
- 
                        - **Text**— Collects free-form text input from users.
- **Files**— Accepts file uploads from users for document processing.
 

## Editor and Run mode

            Editor mode is where you build your flow. You see all the steps laid out and can select each one to change its configuration. Run mode is where you test and execute your flow, with a chat panel where you can ask follow-up questions or refine the output.