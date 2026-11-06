# Mulesoft Vibes Example Messages | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/vibes-prompt-examples](https://docs.mulesoft.com/anypoint-code-builder/vibes-prompt-examples)

---

`openapi: 3.0.0 info: title: Order Management API version: 1.0.0 description: API for managing orders in an e-commerce platform. servers: - url: https://api.ecommerce.com/v1 paths: /orders: post:`(1)summary: Create a new order operationId: createOrder requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/Order' responses: '201': description: Order created successfully '400': description: Bad request '401': description: Unauthorized '500': description: Internal server error security: - bearerAuth: [] get:(2)summary: Retrieve all orders operationId: getOrders responses: '200': description: A list of orders content: application/json: schema: type: array items: $ref: '#/components/schemas/Order' '401': description: Unauthorized '500': description: Internal server error security: - bearerAuth: [] /orders/{orderId}:(3)get: summary: Retrieve a specific order operationId: getOrder parameters: - name: orderId in: path required: true schema: type: string responses: '200': description: Order details '404': description: Order not found put: summary: Update an existing order operationId: updateOrder parameters: - name: orderId in: path required: true schema: type: string requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/Order' responses: '200': description: Order updated successfully '404': description: Order not found delete: summary: Delete an order operationId: deleteOrder parameters: - name: orderId in: path required: true schema: type: string responses: '204': description: Order deleted successfully '404': description: Order not found components: securitySchemes:(4)bearerAuth: type: http scheme: bearer bearerFormat: JWT schemas:(5)Order: type: object properties: id: type: string customerId: type: string items: type: array items: $ref: '#/components/schemas/OrderItem' totalAmount: type: number format: float status: type: string enum: [pending, processing, completed, cancelled] OrderItem: type: object properties: productId: type: string quantity: type: integer price: type: number format: floatxml

# Mulesoft Vibes Example Messages

Use these example messages to guide Mulesoft Vibes in completing common tasks. Customize the values to match your project or environment.

## Application Deployment and Projects

- 
**Task**: Deploy an app to CloudHub or Runtime Fabric.**Prompt**: Deploy the [application_name] app from Anypoint Exchange.
- 
**Task**: Create an integration project.**Prompt**: Create a Mule project that creates an order in NetSuite every time an opportunity in Salesforce is updated to the ‘Closed Won’ stage.
- 
**Task**: Deploy an integration application.**Prompt**: Deploy [application_name] app in the current project. Deploy it with high security, high availability, and performance optimized settings.
- 
**Task**: Modify an existing application.**Prompt**: Update [application_name] so that it meets [specific business requirements].
- 
**Task**: Generate an MCP server using Anypoint connectors.**Prompt**: Generate an MCP server that exposes three tools from the following operations: Workday - Absence Management - Get Time Off Plan Balances, Workday - Absence Management - Enter Time Off, and Google Calendar - Create Calendar Event.

## Exchange Asset Management

- 
**Task**: Create an asset in Exchange.**Prompt**: Publish [this asset type] in Exchange using this [name].
- 
**Task**: Search for an asset in Exchange.**Prompt**: Do I have any assets for order notifications in Exchange?
- 
**Task**: Search for an asset within a specific organization.**Prompt**: Find [asset name] in [organization name].

## API Instances

- 
**Task**: Create an app instance and apply a policy.**Prompt**: Create an instance for the [application_name] and apply the rate limiting policy to that instance.
- 
**Task**: View performance metrics for your APIs or apps.**Prompt**: Which apps generated the most errors this month?

## Custom Metadata

- 
**Task**: Set custom metadata that uses sample data.**Prompt**: Can you help me define custom metadata on the following component? This is how the sample data looks: [sample data].
- 
**Task**: Set custom metadata using a file.**Prompt**: Define custom metadata using the sample file below and attach it to [processor_name] @[path_to_file].

## Agent Network Operations

- 
**Task**: Create an Agent Network**Prompt**: Create an Agent Network for called "Employee Onboarding".
- 
**Task**: Publish an Agent Network.**Prompt**: Publish the "Employee Onboarding" Agent Network project to Exchange.
- 
**Task**: Deploy an instance of the "Employee Onboarding" Agent Network to staging.**Prompt**: Deploy this Agent Network project.

## Order Management

Your company manages a growing e-commerce platform and needs a way to streamline the handling of customer orders. You want to build an API specification that allows your backend systems to create, retrieve, update, and delete orders, ensuring consistent data models and robust error handling across all operations.

To generate a specification for this task, enter a message like:
`Generate an API specification for an order management system for an e-commerce platform. The API should include endpoints to create, retrieve, update, and delete orders, along with detailed definitions for request and response payloads, versioning details, and error handling mechanisms.`

This message generates an API specification using the same specification language as the file that was in focus:

| 1 | Creates a new order: The`POST /orders`operation accepts a JSON payload and returns a success or error response. | 
| 2 | Retrieves a list of all orders: The`GET /orders`operation returns an array of order objects. | 
| 3 | Handles operations for a specific order: Includes`GET`,`PUT`, and`DELETE`methods on`/orders/{orderId}`with path parameter validation. | 
| 4 | Uses bearer token authentication: The`bearerAuth`scheme is applied to secure all endpoints. | 
| 5 | Defines reusable data models: The`Order`and`OrderItem`schemas provide consistent structure for request and response payloads. | 

## Inventory Management

Your business needs to track and manage product stock across multiple warehouses and storefronts. To ensure accurate inventory levels and prevent overselling, you want to generate an API specification that supports creating, updating, deleting, and listing products. The specification should include clear data models, input validation rules, and proper security mechanisms.

To generate a specification for this task, enter a message like:
`Generate an API specification for an inventory management system. The API should expose endpoints to manage products and stock levels, support operations to add, update, delete, and list products, and include clear definitions for data models, input validation rules, and security considerations.`

`openapi: 3.0.0 info: title: Inventory Management API version: 1.0.0 description: API for managing products and stock levels. servers: - url: https://api.inventory.com/v1 paths: /products: post:`(1)summary: Add a new product operationId: addProduct requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/Product' responses: '201': description: Product added successfully '400': description: Invalid input security: - bearerAuth: [] get:(2)summary: List all products operationId: listProducts responses: '200': description: A list of products content: application/json: schema: type: array items: $ref: '#/components/schemas/Product' '500': description: Internal server error security: - bearerAuth: [] /products/{productId}:(3)get: summary: Get product details operationId: getProduct parameters: - name: productId in: path required: true schema: type: string responses: '200': description: Product data '404': description: Product not found put: summary: Update a product operationId: updateProduct parameters: - name: productId in: path required: true schema: type: string requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/Product' responses: '200': description: Product updated '400': description: Invalid input '404': description: Product not found delete: summary: Delete a product operationId: deleteProduct parameters: - name: productId in: path required: true schema: type: string responses: '204': description: Product deleted '404': description: Product not found components: securitySchemes:(4)bearerAuth: type: http scheme: bearer bearerFormat: JWT schemas:(5)Product: type: object required: [id, name, quantity, price] properties: id: type: string name: type: string description: type: string quantity: type: integer minimum: 0 price: type: number format: floatxml

| 1 | Creates a new product: The`POST /products`operation uses a JSON payload to define the product. | 
| 2 | Lists all products: The`GET /products`operation returns an array of products in stock. | 
| 3 | Manages individual products: Includes operations to retrieve, update, or delete a specific product using its ID. | 
| 4 | Secures endpoints with bearer authentication: The API uses`bearerAuth`to protect inventory operations. | 
| 5 | Includes a validated product schema: The Product schema enforces required fields and validation like minimum: 0 for quantity. | 

## User authentication and management

Your application requires secure and reliable user authentication to protect user data and manage access to services. To support this, you want to generate an API specification that handles user registration, login, token management, and password resets. The specification should include proper input validation, error responses, and security best practices.

To generate a specification for this task, enter a message like:

`Generate an API specification for a user authentication and management service. The API should support endpoints for user registration, login, token management, and password resets, including thorough details on input validation, error responses, and necessary security protocols.`

This message generates an API specification using the same specification language as the file that was in focus:

`openapi: 3.0.0 info: title: User Auth API version: 1.0.0 description: API for managing user authentication and credentials. servers: - url: https://api.example.com/v1 paths: /register:`(1)post: summary: Register a new user operationId: registerUser requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/RegisterRequest' responses: '201': description: User created '400': description: Invalid input /login:(2)post: summary: Authenticate a user operationId: loginUser requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/LoginRequest' responses: '200': description: Login successful '401': description: Unauthorized /token/refresh:(3)post: summary: Refresh an access token operationId: refreshToken requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/RefreshRequest' responses: '200': description: Token refreshed '401': description: Invalid refresh token /reset-password:(4)post: summary: Request password reset operationId: resetPassword requestBody: required: true content: application/json: schema: $ref: '#/components/schemas/ResetRequest' responses: '200': description: Password reset email sent '404': description: User not found components: securitySchemes:(5)bearerAuth: type: http scheme: bearer bearerFormat: JWT schemas:(6)RegisterRequest: type: object required: [email, password] properties: email: type: string format: email password: type: string minLength: 8 LoginRequest: type: object required: [email, password] properties: email: type: string password: type: string RefreshRequest: type: object required: [refreshToken] properties: refreshToken: type: string ResetRequest: type: object required: [email] properties: email: type: stringxml

| 1 | Registers a new user:`POST /register`validates input and creates a new user account. | 
| 2 | Logs in a user:`POST /login`checks credentials and returns a token on success. | 
| 3 | Refreshes token:`POST /token/refresh`issues a new access token using a refresh token. | 
| 4 | Initiates password reset:`POST /reset-password`sends a reset email if the user exists. | 
| 5 | Secures endpoints: All protected routes use JWT bearer authentication. | 
| 6 | Defines schemas:`UserRegistration`and`UserLogin`schemas include input validation like`minLength`and`format: email`. | 

## MUnit tests for Mule flows

Your Mule application exposes APIs and orchestrates calls to backend services. To improve reliability, create MUnit tests for a flow that processes requests, transforms payloads, and returns responses under different conditions.

To generate tests for this task, enter a message like:

`Create MUnit tests for the <flow-name> flow. Add one test for the happy path, one test for invalid input, and one test for a downstream service failure. Mock the external dependencies, use sample event payloads, and verify the expected response payload and status code in each case.`