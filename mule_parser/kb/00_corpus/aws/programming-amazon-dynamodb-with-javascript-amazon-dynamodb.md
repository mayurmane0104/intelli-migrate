# Programming Amazon DynamoDB with JavaScript - Amazon DynamoDB

**Source:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-javascript.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-javascript.html)

---

This guide provides an orientation to programmers wanting to use Amazon DynamoDB with JavaScript. Learn about the AWS SDK for JavaScript, abstraction layers available, configuring connections, handling errors, defining retry policies, managing keep-alive, and more.

###### Topics

## About AWS SDK for JavaScript

        The AWS SDK for JavaScript provides access to AWS services using either browser scripts or
            Node.js. This documentation focuses on the latest version of the SDK (V3). The AWS SDK for JavaScript
            V3 is maintained by AWS as an [open-source project hosted on GitHub](https://github.com/aws/aws-sdk-js-v3). Issues and feature requests are
            public and you can access them on the issues page for the GitHub repository.

JavaScript V2 is similar to V3, but contains syntax differences. V3 is more modular, making it easier to ship smaller dependencies, and has first-class TypeScript support. We recommend using the latest version of the SDK.

## Using the AWS SDK for JavaScript V3

        You can add the SDK to your Node.js application using the Node Package Manager. The examples below show how to add the most common SDK packages for working with DynamoDB.

- 
                `npm install @aws-sdk/client-dynamodb`
- 
                `npm install @aws-sdk/lib-dynamodb`
- 
                `npm install @aws-sdk/util-dynamodb`

Installing packages adds references to the dependency section of your package.json project file. You have the option to use the newer ECMAScript module syntax. For further details on these two approaches, see the Considerations section.

## Accessing JavaScript documentation

        Get started with JavaScript documentation with the following resources:

- 
                Access the [Developer guide](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/welcome.html)for core JavaScript documentation. Installation instructions are located in the**Setting up**section.
- 
                Access the [API reference](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/introduction/)documentation to explore all available classes and methods.
- 
                The SDK for JavaScript supports many AWS services other than DynamoDB. Use the following procedure to locate specific API coverage for DynamoDB: - 
                        From **Services**, choose**DynamoDB and Libraries**. This documents the low-level client.
- 
                        Choose **lib-dynamodb**. This documents the high-level client. The two clients represent two different abstraction layers that you have the choice to use. See the section below for more information about abstraction layers.
 
- 
                        

## Abstraction layers

        The SDK for JavaScript V3 has a low-level client (`DynamoDBClient`) and a
            high-level client (`DynamoDBDocumentClient`).

### Low-level client (`DynamoDBClient`)

            The low-level client provides no extra abstractions over the underlying wire protocol. It gives you full control over all aspects of communication, but because there are no abstractions, you must do things like provide item definitions using the DynamoDB JSON format.

As the example below shows, with this format data types must be stated explicitly.
                An *S* indicates a string value and an *N* indicates a number value. Numbers on the wire are
                always sent as strings tagged as number types to ensure no loss in precision. The
                low-level API calls have a naming pattern such as `PutItemCommand` and
                    `GetItemCommand`.

The following example is using low-level client with `Item` defined
                using DynamoDB JSON:

```
const { DynamoDBClient, PutItemCommand } = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient({});
async function addProduct() {
  const params = {
    TableName: "products",
    Item: {
      "id": { S: "Product01" },
      "description": { S: "Hiking Boots" },
      "category": { S: "footwear" },
      "sku": { S: "hiking-sku-01" },
      "size": { N: "9" }
    }
  };
  try {
    const data = await client.send(new PutItemCommand(params));
    console.log('result : ' + JSON.stringify(data));
  } catch (error) {
    console.error("Error:", error);
  }
}
addProduct();
```
### High-level client (`DynamoDBDocumentClient`)

            The high-level DynamoDB document client offers built-in convenience features, such as
                eliminating the need to manually marshal data and allowing for direct reads and
                writes using standard JavaScript objects. The [documentation for  lib-dynamodb](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-lib-dynamodb/) provides the list of
                advantages.

To instantiate the `DynamoDBDocumentClient`, construct a low-level
                    `DynamoDBClient` and then wrap it with a
                    `DynamoDBDocumentClient`. The function naming convention differs
                slightly between the two packages. For instance, the low-level uses
                    `PutItemCommand` while the high-level uses `PutCommand`.
                The distinct names allow both sets of functions to coexist in the same context,
                allowing you to mix both in the same script.

```
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, PutCommand } = require("@aws-sdk/lib-dynamodb");
const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);
async function addProduct() {
  const params = {
    TableName: "products",
    Item: {
      id: "Product01",
      description: "Hiking Boots",
      category: "footwear",
      sku: "hiking-sku-01",
      size: 9,
    },
  };
  try {
    const data = await docClient.send(new PutCommand(params));
    console.log('result : ' + JSON.stringify(data));
  } catch (error) {
    console.error("Error:", error);
  }
}
addProduct();
```
The pattern of usage is consistent when you're reading items using API operations
                such as `GetItem`, `Query`, or `Scan`.

## Using the marshall utility function

        You can use the low-level client and marshall or unmarshall the data types on your
            own. The utility package, [util-dynamodb](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/Package/-aws-sdk-util-dynamodb/), has a `marshall()` utility function that accepts
            JSON and produces DynamoDB JSON, as well as an `unmarshall()` function, that
            does the reverse. The following example uses the low-level client with data marshalling
            handled by the `marshall()` call.

```
const { DynamoDBClient, PutItemCommand } = require("@aws-sdk/client-dynamodb");
const { marshall } = require("@aws-sdk/util-dynamodb");
const client = new DynamoDBClient({});
async function addProduct() {
  const params = {
    TableName: "products",
    Item: marshall({
      id: "Product01",
      description: "Hiking Boots",
      category: "footwear",
      sku: "hiking-sku-01",
      size: 9,
    }),
  };
  try {
    const data = await client.send(new PutItemCommand(params));
  } catch (error) {
    console.error("Error:", error);
  }
}
addProduct();
```
## Reading items

        To read a single item from DynamoDB, you use the `GetItem` API operation.
            Similar to the `PutItem` command, you have the choice to use either the
            low-level client or the high-level Document client. The example below demonstrates using
            the high-level Document client to retrieve an item.

```
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, GetCommand } = require("@aws-sdk/lib-dynamodb");
const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);
async function getProduct() {
  const params = {
    TableName: "products",
    Key: {
      id: "Product01",
    },
  };
  try {
    const data = await docClient.send(new GetCommand(params));
    console.log('result : ' + JSON.stringify(data));
  } catch (error) {
    console.error("Error:", error);
  }
}
getProduct();
```
Use the `Query` API operation to read multiple items. You can use the
            low-level client or the Document client. The example below uses the high-level Document
            client.

```
const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const {
  DynamoDBDocumentClient,
  QueryCommand,
} = require("@aws-sdk/lib-dynamodb");
const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);
async function productSearch() {
  const params = {
    TableName: "products",
    IndexName: "GSI1",
    KeyConditionExpression: "#category = :category and begins_with(#sku, :sku)",
    ExpressionAttributeNames: {
      "#category": "category",
      "#sku": "sku",
    },
    ExpressionAttributeValues: {
      ":category": "footwear",
      ":sku": "hiking",
    },
  };
  try {
    const data = await docClient.send(new QueryCommand(params));
    console.log('result : ' + JSON.stringify(data));
  } catch (error) {
    console.error("Error:", error);
  }
}
productSearch();
```
## Conditional writes

        DynamoDB write operations can specify a logical condition expression that must evaluate to true for the write to proceed. If the condition does not evaluate to true, the write operation generates an exception. The condition expression can check if the item already exists or if its attributes match certain constraints.

```
ConditionExpression = "version = :ver AND size(VideoClip) < :maxsize"
            
```

When the conditional expression fails, you can use
                `ReturnValuesOnConditionCheckFailure` to request that the error response
            include the item that didn't satisfy the conditions to deduce what the problem was. For
            more details, see [Handle conditional write errors in high concurrency scenarios with
                Amazon DynamoDB](https://aws.amazon.com/blogs/database/handle-conditional-write-errors-in-high-concurrency-scenarios-with-amazon-dynamodb/).

```
try {
      const response = await client.send(new PutCommand({
          TableName: "YourTableName",
          Item: item,
          ConditionExpression: "attribute_not_exists(pk)",
          ReturnValuesOnConditionCheckFailure: "ALL_OLD"
      }));
  } catch (e) {
      if (e.name === 'ConditionalCheckFailedException') {
          console.log('Item already exists:', e.Item);
      } else {
          throw e;
      }
  }
```
Additional code examples showing other aspects of JavsScript SDK V3 usage are
            available in the [JavaScript SDK V3 Documentation](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/javascript_dynamodb_code_examples.html) and under the [DynamoDB-SDK-Examples GitHub repository](https://github.com/aws-samples/aws-dynamodb-examples/tree/master/examples/SDK/node.js).

## Pagination

        
        Read requests such as `Scan` or `Query` will likely return
            multiple items in a dataset. If you perform a `Scan` or `Query`
            with a `Limit` parameter, then once the system has read that many items, a
            partial response will be sent, and you'll need to paginate to retrieve additional
            items.

The system will only read a maximum of 1 megabyte of data per request. If you're
            including a `Filter` expression, the system will still read a megabyte, at
            maximum, of data from disk, but will return the items of that megabyte that match the
            filter. The filter operation could return 0 items for a page, but still require further
            pagination before the search is exhausted.

You should look for `LastEvaluatedKey` in the response and using it as the
                `ExclusiveStartKey` parameter in a subsequent request to continue data
            retrieval. This serves as a bookmark as noted in the following example.

###### Note

The sample passes a null `lastEvaluatedKey` as the
                    `ExclusiveStartKey` on the first iteration and this is
                allowed.

Example using the `LastEvaluatedKey`:

```
const { DynamoDBClient, ScanCommand } = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient({});
async function paginatedScan() {
  let lastEvaluatedKey;
  let pageCount = 0;
  do {
    const params = {
      TableName: "products",
      ExclusiveStartKey: lastEvaluatedKey,
    };
    const response = await client.send(new ScanCommand(params));
    pageCount++;
    console.log(`Page ${pageCount}, Items:`, response.Items);
    lastEvaluatedKey = response.LastEvaluatedKey;
  } while (lastEvaluatedKey);
}
paginatedScan().catch((err) => {
  console.error(err);
});
```
### Using the `paginateScan` convenience method

            
            
            The SDK provides convenience methods called `paginateScan` and
                    `paginateQuery` that do this work for you and makes the repeated
                requests behind the scenes. Specify the max number of items to read per request
                using the standard `Limit` parameter.

```
const { DynamoDBClient, paginateScan } = require("@aws-sdk/client-dynamodb");
const client = new DynamoDBClient({});
async function paginatedScanUsingPaginator() {
  const params = {
    TableName: "products",
    Limit: 100
  };
  const paginator = paginateScan({client}, params);
  let pageCount = 0;
  for await (const page of paginator) {
    pageCount++;
    console.log(`Page ${pageCount}, Items:`, page.Items);
  }
}
paginatedScanUsingPaginator().catch((err) => {
  console.error(err);
});
```
###### Note

Performing full table scans regularly is not a recommended access pattern unless the table is small.

## Specifying configuration

        
        When setting up the `DynamoDBClient`, you can specify various configuration
            overrides by passing a configuration object to the constructor. For example, you can
            specify the Region to connect to if it's not already known to the calling context or the
            endpoint URL to use. This is useful if you want to target a DynamoDB Local instance for
            development purposes.

```
const client = new DynamoDBClient({
  region: "eu-west-1",
  endpoint: "http://localhost:8000",
});
```
### Config for timeouts

DynamoDB uses HTTPS for client-server communication. You can control some aspects of
                the HTTP layer by providing a `NodeHttpHandler` object. For example, you
                can adjust the key timeout values `connectionTimeout` and
                    `requestTimeout`. The `connectionTimeout` is the maximum
                duration, in milliseconds, that the client will wait while trying to establish a
                connection before giving up.

The `requestTimeout` defines how long the client will wait for a
                response after a request has been sent, also in milliseconds. The defaults for both
                are zero, meaning the timeout is disabled and there's no limit on how long the
                client will wait if the response does not arrive. You should set the timeouts to
                something reasonable so in the event of a network issue the request will error out
                and a new request can be initiated. For example:

```
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { NodeHttpHandler } from "@smithy/node-http-handler";
const requestHandler = new NodeHttpHandler({
  connectionTimeout: 2000,
  requestTimeout: 2000,
});
const client = new DynamoDBClient({
  requestHandler
});
```
###### Note

The example provided uses the [Smithy](https://smithy.io/2.0/index.html) import. Smithy is a language for defining services and SDKs,
                    open-source and maintained by AWS.

In addition to configuring timeout values, you can set the maximum number of
                sockets, which allows for an increased number of concurrent connections per origin.
                The developer guide includes [details on configuring the  maxSockets parameter](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/node-configuring-maxsockets.html).

### Config for keep-alive

When using HTTPS, the first request always takes some back-and-forth communication to establish a secure connection. HTTP Keep-Alive allows subsequent requests to reuse the already-established connection, making the requests more efficient and lowering latency. HTTP Keep-Alive is enabled by default with JavaScript V3.

There's a limit to how long an idle connection can be kept alive. Consider sending periodic requests, maybe every minute, if you have an idle connection but want the next request to use an already-established connection.

###### Note

Note that in the older V2 of the SDK, keep-alive was off by default, meaning each connection would get closed immediately after use. If using V2, you can override this setting.

### Config for retries

When the SDK receives an error response and the error is resumable as determined by the SDK, such as a throttling exception or a temporary service exception, it will retry again. This happens invisibly to you as the caller, except that you might notice the request took longer to succeed.

The SDK for JavaScript V3 will make 3 total requests, by default, before giving up and passing the error into the calling context. You can adjust the number and frequency of these retries.

The `DynamoDBClient` constructor accepts a `maxAttempts`
                setting that limits how many attempts will happen. The below example raises the
                value from the default of 3 to a total of 5. If you set it to 0 or 1, that indicates
                you don't want any automatic retries and want to handle any resumable errors
                yourself within your catch block.

```
const client = new DynamoDBClient({
  maxAttempts: 5,
});
```
You can also control the timing of the retries with a custom retry strategy. To do
                this, import the `util-retry` utility package and create a custom backoff
                function that calculates the wait time between retries based on the current retry
                count.

The example below says to make a maximum of 5 attempts with delays of 15, 30, 90,
                and 360 milliseconds should the first attempt fail. The custom backoff function,
                    ` calculateRetryBackoff`, calculates the delays by accepting the
                retry attempt number (starts with 1 for the first retry) and returns how many
                milliseconds to wait for that request.

```
const { ConfiguredRetryStrategy } = require("@aws-sdk/util-retry");
const calculateRetryBackoff = (attempt) => {
  const backoffTimes = [15, 30, 90, 360];
  return backoffTimes[attempt - 1] || 0;
};
const client = new DynamoDBClient({
  retryStrategy: new ConfiguredRetryStrategy(
    5, // max attempts.
    calculateRetryBackoff // backoff function.
  ),
});
```
## Waiters

        The DynamoDB client includes two useful [waiter functions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/wait/index.html#cli-aws-dynamodb-wait) that can be used when creating, modifying, or deleting
            tables when you want your code to wait to proceed until the table modification has
            finished. For example, you can deploy a table, call the
                

`waitUntilTableExists` function, and the code will block until the table
            has been made **ACTIVE**. The waiter internally polls the DynamoDB service with a

`describe-table` every 20 seconds.```
import {waitUntilTableExists, waitUntilTableNotExists} from "@aws-sdk/client-dynamodb";
… <create table details>
const results = await waitUntilTableExists({client: client, maxWaitTime: 180}, {TableName: "products"});
if (results.state == 'SUCCESS') {
  return results.reason.Table
}
console.error(`${results.state} ${results.reason}`);
```
The `waitUntilTableExists` feature returns control only when it can perform
            a `describe-table` command that shows the table status
                **ACTIVE**. This ensures that you can use
                `waitUntilTableExists` to wait for the completion of creation, as well as
            modifications such as adding a GSI index, which may take some time to apply before the
            table returns to **ACTIVE** status.

## Error handling

        In the early examples here, we've caught all errors broadly. However, in practical applications, it's important to discern between various error types and implement more precise error handling.

DynamoDB error responses contain metadata, including the name of the error. You can catch
            errors then match against the possible string names of error conditions to determine how
            to proceed. For server-side errors, you can leverage the `instanceof`
            operator with the error types exported by the `@aws-sdk/client-dynamodb`
            package to manage error handling efficiently.

It's important to note that these errors only manifest after all retries have been exhausted. If an error is retried and is eventually followed by a successful call, from the code's perspective, there's no error just a slightly elevated latency. Retries will show up in Amazon CloudWatch charts as unsuccessful requests, such as throttle or error requests. If the client reaches the maximum retry count, it will give up and generate an exception. This is the client's way of saying it's not going to retry.

Below is a snippet to catch the error and take action based on the type of error that was returned.

```
import {
  ResourceNotFoundException
  ProvisionedThroughputExceededException,
  DynamoDBServiceException,
} from "@aws-sdk/client-dynamodb";
try {
  await client.send(someCommand);
} catch (e) {
    if (e instanceof ResourceNotFoundException) {
      // Handle ResourceNotFoundException
    } else if (e instanceof ProvisionedThroughputExceededException) {
      // Handle ProvisionedThroughputExceededException
    } else if (e instanceof DynamoDBServiceException) {
      // Handle DynamoDBServiceException
    } else {
      // Other errors such as those from the SDK
      if (e.name === "TimeoutError") {
        // Handle SDK TimeoutError.
      } else {
        // Handle other errors.
      }
    }
}
```
See [Error handling with DynamoDB](./Programming.Errors.html) for common error strings in the *DynamoDB Developer Guide*. The exact errors possible with
            any particular API call can be found in the documentation for that API call, such as the
                [Query API docs](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_Query.html).

The metadata of errors include additional properties, depending on the error. For
                a` TimeoutError`, the metadata includes the number of attempts that were
            made and the `totalRetryDelay`, as shown below.

```
{
  "name": "TimeoutError",
  "$metadata": {
    "attempts": 3,
    "totalRetryDelay": 199
  }
}
```
If you manage your own retry policy, you'll want to differentiate between throttles and errors:

- 
                A **throttle**(indicated by a`ProvisionedThroughputExceededException`or`ThrottlingException`) indicates a healthy service that's informing you that you've exceeded your read or write capacity on a DynamoDB table or partition. Every millisecond that passes, a bit more read or write capacity is made available, and so you can retry quickly, such as every 50ms, to attempt to access that newly released capacity.With throttles you don't especially need exponential backoff because throttles are lightweight for DynamoDB to return and incur no per-request charge to you. Exponential backoff assigns longer delays to client threads that have already waited the longest, which statistically extends the p50 and p99 outward. 
- 
                An **error**(indicated by an`InternalServerError`or a`ServiceUnavailable`, among others) indicates a transient issue with the service, possibly the whole table or just the partition you're reading from or writing to. With errors, you can pause longer before retries, such as 250ms or 500ms, and use jitter to stagger the retries.

## Logging

        Turn on logging to get more details about what the SDK is doing. You can set a
            parameter on the `DynamoDBClient` as shown in the example below. More log
            information will appear in the console and includes metadata such as the status code and
            the consumed capacity. If you run the code locally in a terminal window, the logs appear
            there. If you run the code in AWS Lambda, and you have Amazon CloudWatch logs set up, then the
            console output will be written there.

```
const client = new DynamoDBClient({
  logger: console
});
```
You can also hook into the internal SDK activities and perform custom logging as
            certain events happen. The example below uses the client's `middlewareStack`
            to intercept each request as it's being sent from the SDK and logs it as it's
            happening.

```
const client = new DynamoDBClient({});
client.middlewareStack.add(
  (next) => async (args) => {
    console.log("Sending request from AWS SDK", { request: args.request });
    return next(args);
  },
  {
    step: "build",
    name: "log-ddb-calls",
  }
);
```
The `MiddlewareStack` provides a powerful hook for observing and
            controlling SDK behavior. See the blog [Introducing Middleware Stack in Modular AWS SDK for JavaScript](https://aws.amazon.com/blogs/developer/middleware-stack-modular-aws-sdk-js/), for more
            information.

## Considerations

        When implementing the AWS SDK for JavaScript in your project, here are some further factors to consider.

- **Module systems**
- 
                    The SDK supports two module systems, CommonJS and ES (ECMAScript). CommonJS uses the `require`function, while ES uses the`import`keyword.- 
                            **Common JS**–`const { DynamoDBClient, PutItemCommand } = require("@aws-sdk/client-dynamodb");`
- 
                            **ES (ECMAScript**–`import { DynamoDBClient, PutItemCommand } from "@aws-sdk/client-dynamodb";`
 The project type dictates the module system to be used and is specified in the type section of your package.json file. The default is CommonJS. Use `"type": "module"`to indicate an ES project. If you have an existing Node.JS project that uses the CommonJS package format, you can still add functions with the more modern SDK V3 Import syntax by naming your function files with the .mjs extension. This will allow the code file to be treated as ES (ECMAScript).
- 
                            
- **Asynchronous operations**
- 
                    You'll see many code samples using callbacks and promises to handle the result of DynamoDB operations. With modern JavaScript this complexity is no longer needed and developers can take advantage of the more succinct and readable async/await syntax for asynchronous operations. 
- **Web browser runtime**
- 
                    Web and mobile developers building with React or React Native can use the SDK for JavaScript in their projects. With the earlier V2 of the SDK, web developers would have to load the full SDK into the browser, referencing an SDK image hosted at https://sdk.amazonaws.com/js/. With V3, it's possible to bundle just the required V3 client modules and all required JavaScript functions into a single JavaScript file using Webpack, and add it in a script tag in the `<head>`of your HTML pages, as explained in the[Getting started in a browser script](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/getting-started-browser.html)section of the SDK documentation.
- **DAX data plane operations**
- 
                    The Amazon DynamoDB Streams Accelerator (DAX) data plane operations are supported by the SDK for JavaScript V3.