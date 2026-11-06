# Step 2. Design an API Spec | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/api-led-design](https://docs.mulesoft.com/general/api-led-design)

---

- 
Option A: Use MuleSoft Vibes 
- 
Option B: Create Manually 

- 
Open MuleSoft Vibes from the toolbar or from the **Build Your Ecosystem with AI**card in the canvas.
- 
Type this prompt in the chat: `Create an OAS 3.0 API spec called "hello-world-api" with a GET endpoint at /greeting that accepts a required query parameter called "name" and returns a JSON response with a message field containing a personalized greeting.`text
- 
Press Enter to send. MuleSoft Vibes generates your API spec in about 10 seconds. You’ll see the generated spec in the chat response. 
- 
Click **Create Project**in the MuleSoft Vibes response.
- 
Select your home directory as the project location. Anypoint Code Builder creates the project and opens `hello-world-api.yaml`in the editor.

- 
Click **Design an API**.
- 
Complete the **API Specification**form:- 
**Project Name**, enter`hello-world-api`.
- 
**Project Location**, select your home directory.
- 
**API Type**, select**REST API**.
- 
**API Specification Language**, select**OAS 3.0 (YAML)**.
- 
Optionally, select a business group. ![The form to create a new API spec with values filled in](_images/api-tutorial-create-project-acb.png) 
 
- 
- 
Click **Create Project**.Anypoint Code Builder creates the project and opens `hello-world-api.yaml`in the editor with a basic template.
- 
Replace the template content with this API spec: `openapi: 3.0.0 info: title: hello-world-api version: 1.0.0 paths: /greeting: get: parameters: - name: name in: query required: true schema: type: string description: The name to greet responses: '200': description: Success content: application/json: schema: type: object properties: message: type: string example: "Hello, World!"`yaml
- 
Save the file ( **File > Save**or Cmd+S/Ctrl+S).