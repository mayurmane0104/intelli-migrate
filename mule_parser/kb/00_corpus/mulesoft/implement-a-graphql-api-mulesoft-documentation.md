# Implement a GraphQL API | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/tut-graphql-implement-api](https://docs.mulesoft.com/anypoint-code-builder/tut-graphql-implement-api)

---

`schema { query: Query } type Query { bookById(id: ID): Book books: [Book] bestsellers: Bestsellers } type Book { id: ID! name: String pageCount: Int author: Author } type Author { id: ID! firstName: String lastName: String } type Bestsellers { books: [Book] authors: [Author] }`graphql

# Implement a GraphQL API

Publish a GraphQL API schema to Anypoint Exchange. Then use Anypoint Code Builder to import and scaffold the schema into a Mule application. Run and implement the interface.

## Before You Begin

Complete these procedures:

- 
Set up your MuleSoft environment. See [Getting Started with Anypoint Code Builder](start-acb)for more information.
- 
Download the **Books API**GraphQL schemaAlternatively, create a file named`books-api.graphql`with the following content:

## Publish the GraphQL API to Exchange

To implement a GraphQL API, the API must first be manually published to Exchange:

- 
Navigate to Anypoint Exchange, and sign in. ## Show me how- 
US cloud (non-EU host): [Exchange (US)](https://anypoint.mulesoft.com/exchange/)
- 
EU cloud (EU host): [Exchange (EU)](https://eu1.anypoint.mulesoft.com/exchange/)
 
- 
- 
Click **Publish new asset**.
- 
For **Name**, type`books-api`.
- 
For **Asset types**, select**GraphQL API**.
- 
For **Method**, select**Upload a GraphQL API Schema**:![A form for publishing a GraphQL API asset](_images/upload-graphql-api-exchange-method-select.png)  
- 
For **File upload**, click**Choose file**and browse for your`books-api.graphql`schema file.
- 
For **Lifecycle state**, select**Stable**.
- 
Click **Publish**.

## Implement the GraphQL API Schema

Use Anypoint Code Builder to retrieve the schema from Anypoint Exchange and scaffold the schema into an interface that you can implement from the desktop or cloud IDE.

- 
Open Anypoint Code Builder. 
- 
Open the Command Palette. ## Show me how- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
In the desktop IDE, select **View**>**Command Palette**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Command Palette**.
 
- 
- 
Provide the following command: `MuleSoft: Implement an API Specification`command
- 
If prompted to sign in to Anypoint Platform, click **Allow**, and follow the prompts to sign in.
- 
Configure your project using the following values: ![A form for implementing a new API specification](_images/implement-api-configure-in-task.png)  - 
**Project Name**:`books-implementation`
- 
**Project Location**: click**Browse**, and then select your home directory.
- 
Search for your **books-api**specification in Exchange by typing`books`and pressing Return to display the results.
- 
In the search results, hover over **books-api**, and click the**Add Asset**button that appears:![A table of available API specifications with the Add Asset button highlighted](_images/select-books-graphql-api.png)  
- 
Provide **Mule runtime**and**Java**versions.
 
- 
- 
Click **Create Project**.
- 
If prompted, trust the authors of the API specification. Trusting is required before you can work on the project from the IDE. After you trust the authors, Anypoint Code Builder scaffolds your GraphQL API and creates a project with an empty flow for each type in your Books API GraphQL schema. GraphQL Schema Mule Flow `type Query { bookById(id: ID): Book books: [Book] bestsellers: Bestsellers } type Book { id: ID! name: String pageCount: Int author: Author } type Author { id: ID! firstName: String lastName: String } type Bestsellers { books: [Book] authors: [Author] }`GraphQL`<flow name="Query.bookById"/> <flow name="Query.books"/> <flow name="Query.bestsellers"/> <flow name="Book.author"/> <flow name="Bestsellers.books"/> <flow name="Bestsellers.authors"/>`XMLEach flow contains configurations for the elements `<graphql-router:data-fetcher/>`,`<set-payload/>`, and ` <graphql-router:serialize/>`. The`<graphql-router:data-fetcher>`element serves as a trigger for a flow. See[Mapping a GraphQL API to Your Data Sources](../apikit/latest/apikit-graphql-api-mapping)for more information about data fetchers.
- 
Proceed to [Test Your GraphQL Project](tut-graphql-test-first-implementation)to run your application in Anypoint Code Builder and post GraphQL queries to your endpoint.

[Test Your GraphQL Project](tut-graphql-test-first-implementation)