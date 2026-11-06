# Test Your GraphQL Project | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/tut-graphql-test-first-implementation](https://docs.mulesoft.com/anypoint-code-builder/tut-graphql-test-first-implementation)

---

`curl --request POST \ --location 'http://localhost:8081/graphql' \ --header 'Content-Type: application/json' \ --data '{ "query": "query bookById($id: ID) {bookById(id: $id){ id name pageCount author{ id firstName lastName}}}", "variables": { "id": 1 } }'`curl

# Test Your GraphQL Project

Before making changes to your GraphQL project, run the application locally within the IDE to test the endpoints.

## Before You Begin

Complete [Implement a GraphQL API](tut-graphql-implement-api).

## Run Your Application

To deploy your Mule Application locally, within the IDE, run a debug session in Anypoint Code Builder:

- 
In Anypoint Code Builder, open the **Books Implementation**project.
- 
Click the ![](_images/icon-run-debug.png) ( (**Run and Debug**) icon in the activity bar, then click the**Start Debugging (F5)**icon.
- 
From your IDE, open the Terminal window in the console: - 
In the desktop IDE, select **View**>**Terminal**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**Terminal**>**New Terminal**.
- 
For either IDE: Press Ctrl and then press the backtick key (`). 
 
- 
- 
In the terminal, open a new command prompt by clicking the plus ( **+**) icon, for example:![Opening command prompt from Terminal](_images/open-command-prompt.png) Alternatively, select a command shell, such as **bash**, by clicking the**v**menu (inverted caret), located beside the plus (**+**) icon, and selecting the shell to use.![Opening bash prompt from Terminal](_images/open-command-prompt-bash.png) 
- 
Run the following `curl`command from the shell’s prompt to trigger the**bookById**flow:If you receive the error `curl: (7) Failed to connect to localhost port 8081 after 0 ms: Couldn’t connect to server`, stop and rerun the application in debug mode. For guidance with stopping the application, see[Debugging Mule Applications](int-debug-mule-apps).Tools such as Postman provide a way to build GraphQL queries. For example, in Postman, you can place your query in the **Body**tab and copy the example`curl`request. The resulting command includes newline (`\\n`) and tab (`\\t`) characters that you can delete from the`curl`command’s`--data`value. For more information, see[Make an HTTP call with GraphQL](https://learning.postman.com/docs/sending-requests/graphql/graphql-http/)in the Postman documentation.Anypoint Code Builder returns the following output in the terminal (manually reformatted to enhance readability): `{ "data": { "bookById": { "id":"#myID", "name":"This is some example data", "pageCount":100, "author": { "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "firstName":"This is some example data", "lastName":"Hello World!" } } } }`GraphQLThe mock data in the output comes from strings in the Set Payload component that is part of the **Query.bookById**flow (`<flow name="Query.bookById"/>`):`<set-payload value="{
 "id": "some-id",
 "name": "This is some example data",
 "pageCount": -2,
 "author": {
 "id": "urn:uuid:123e4567-e89b-12d3-a456-426655440000",
 "firstName": "This is some example data",
 "lastName": "This is some example data"
 }
}" mimeType="application/json"/>`xml
- 
Optionally, try queries for other endpoints: - 
Query the `books`endpoint with the following`curl`command:`curl --location 'http://localhost:8081/graphql' \ --header 'Content-Type: application/json' \ --data '{"query":"query books { books{ id name pageCount author{ id firstName lastName } }}","variables":{}}'`commandThis command returns the following result (manually reformatted to enhance readability): `{ "data": { "books": [{ "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "name":"This is some example data", "pageCount":1, "author": { "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "firstName":"This is some example data", "lastName":"Hello World!" } }] } }`For your reference, the `books`endpoint has the following structure:`query books { books{ id name pageCount author{ id firstName lastName } } }`GraphQL
- 
Query `bestSellers`:`curl --location 'http://localhost:8081/graphql' \ --header 'Content-Type: application/json' \ --data '{"query":"query bestsellers { bestsellers{ books{ id name pageCount author{ id firstName lastName } } authors{ id firstName lastName } } }","variables":{}}'`commandThis command returns the following result (manually reformatted to enhance readability): `{ "data" : { "bestsellers": { "books": [{ "id":"#myID", "name":"This is some example data", "pageCount":1, "author": { "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "firstName":"This is some example data", "lastName":"Hello World!" } }, { "id":"some-id", "name":"Goodbye", "pageCount":100, "author": { "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "firstName":"This is some example data", "lastName":"Hello World!" } }, { "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "name":"Hello World!", "pageCount":-10, "author": { "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "firstName":"This is some example data", "lastName":"Hello World!" } }], "authors": [{ "id":"urn:uuid:123e4567-e89b-12d3-a456-426655440000", "firstName":"Hello World!", "lastName":"Hello World!" }, { "id":"#myID", "firstName":"Goodbye", "lastName":"Goodbye" }] } } }`For your reference, the `bestsellers`endpoint has the following structure:`query bestsellers { bestsellers{ books{ id name pageCount author{ id firstName lastName } } authors{ id firstName lastName } } }`GraphQL
 
- 
- 
Proceed to [Configure Responses for Your GraphQL Implementation](tut-graphql-configure-flow-responses)to populate each flow with a custom response for each query.

[Implement a GraphQL API](tut-graphql-implement-api)

[Configure Responses for Your GraphQL Implementation](tut-graphql-configure-flow-responses)