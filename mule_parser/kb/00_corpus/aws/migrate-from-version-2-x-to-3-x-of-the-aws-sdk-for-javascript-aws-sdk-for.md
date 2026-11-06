# Migrate from version 2.x to 3.x of the AWS SDK for JavaScript - AWS SDK for JavaScript

**Source:** [https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrating.html](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/migrating.html)

---

The [AWS SDK for JavaScript V3 API
            Reference Guide](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/) describes in detail all the API operations for the AWS SDK for JavaScript
         version 3 (V3). 

The AWS SDK for JavaScript version 3 is a major rewrite of version 2. The section describes the differences between the two versions and explains how to migrate from version 2 to version 3 of the SDK for JavaScript.

## Migrate your code to SDK for JavaScript v3 using codemod

          
          AWS SDK for JavaScript version 3 (v3) comes with modernized interfaces for client configurations and
                  utilities, which include credentials, Amazon S3 multipart upload, DynamoDB document client,
                  waiters, and more. You can find what changed in v2 and the v3 equivalents for
                  each change in the [migration
                      guide on the AWS SDK for JavaScript GitHub repo](https://github.com/aws/aws-sdk-js-v3/blob/main/UPGRADING.md). 

To take full advantage of the AWS SDK for JavaScript v3, we recommend using the codemod scripts described below.

### Use codemod to migrate existing v2 code

The collection of codemod scripts in [aws-sdk-js-codemod](https://www.npmjs.com/package/aws-sdk-js-codemod) helps migrate your existing AWS SDK for JavaScript (v2) application to use v3 APIs. You can run the transform as follows.

`$ npx aws-sdk-js-codemod -t v2-to-v3 PATH...`

For example, consider you have the following code, which creates a Amazon DynamoDB client from v2 and calls `listTables` operation.

```
// example.ts
import AWS from "aws-sdk";
const region = "us-west-2";
const client = new AWS.DynamoDB({ region });
await client.listTables({}).promise()
  .then(console.log)
  .catch(console.error);
```
You can run our `v2-to-v3` transform on `example.ts` as follows.

`$ npx aws-sdk-js-codemod -t v2-to-v3 example.ts`

The transform will convert the DynamoDB import to v3, create v3 client and call the `listTables` operation as follows.

```
// example.ts
import { DynamoDB } from "@aws-sdk/client-dynamodb";
const region = "us-west-2";
const client = new DynamoDB({ region });
await client.listTables({})
  .then(console.log)
  .catch(console.error);
```
We’ve implemented transforms for common use cases. If your code doesn’t transform
                  correctly, please create a [bug report](https://github.com/awslabs/aws-sdk-js-codemod/issues/new?assignees=&labels=bug%2Ctriage&template=bug_report.yml&title=%5BBug%3F%5D%3A+) or 

[feature request](https://github.com/awslabs/aws-sdk-js-codemod/issues/new?assignees=&labels=enhancement&template=feature_request.yml&title=%5BFeature%5D%3A+)with example input code and observed/expected output code. If your specific use case is already reported in

[an existing issue](https://github.com/awslabs/aws-sdk-js-codemod/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc), show your support by an upvote.

## What's new in Version 3

        Version 3 of the SDK for JavaScript (v3) contains the following new features.

- Modularized packages
- 
              Users can now use a separate package for each service. 
- New middleware stack
- 
              Users can now use a middleware stack to control the lifecycle of an operation call. 

In addition, the SDK is written in TypeScript, which has many advantages, such as static typing.

###### Important

The code examples for v3 in this guide are written in ECMAScript 6 (ES6). ES6
          brings new syntax and new features to make your code more modern and readable, and do more.
          ES6 requires you use Node.js version 13.x or higher. To download and install the latest
          version of Node.js, see [Node.js downloads](https://nodejs.org/en/download/). For more information, see 

[JavaScript ES6/CommonJS syntax](./sdk-example-javascript-syntax.html).

## Modularized packages

        Version 2 of the SDK for JavaScript (v2) required you to use the entire AWS SDK, as follows.

`var AWS = require("aws-sdk");`Loading the entire SDK isn’t an issue if your application is using many AWS services. However, if you need to use only a few AWS services, it means increasing the size of your application with code you don't need or use.

In v3, you can load and use only the individual AWS Services you need. This is shown in the following example, which gives you access to Amazon DynamoDB (DynamoDB).

`import { DynamoDB } from "@aws-sdk/client-dynamodb";`Not only can you load and use individual AWS services, but you can also load and use only
          the service commands you need. This is shown in the following examples, which gives you
          access to DynamoDB client and the `ListTablesCommand` command.

```
import {
  DynamoDBClient,
  ListTablesCommand
} from "@aws-sdk/client-dynamodb";
```
###### Important

You should not import submodules into modules. For example, the following code might result in errors.

`import { CognitoIdentity } from "@aws-sdk/client-cognito-identity/CognitoIdentity";`The following is the correct code.

`import { CognitoIdentity } from "@aws-sdk/client-cognito-identity";`### Comparing code size

In Version 2 (v2), a simple code example that lists all of your Amazon DynamoDB
            tables in the `us-west-2` Region might look like the following.

```
var AWS = require("aws-sdk");
// Set the Region
AWS.config.update({ region: "us-west-2" });
// Create DynamoDB service object
var ddb = new AWS.DynamoDB({ apiVersion: "2012-08-10" });
// Call DynamoDB to retrieve the list of tables
ddb.listTables({ Limit: 10 }, function (err, data) {
  if (err) {
    console.log("Error", err.code);
  } else {
    console.log("Tables names are ", data.TableNames);
  }
});
```
v3 looks like the following.

```
import {
  DynamoDBClient,
  ListTablesCommand
} from "@aws-sdk/client-dynamodb";
const dbclient = new DynamoDBClient({ region: "us-west-2" });
try {
  const results = await dbclient.send(new ListTablesCommand);
  
  for (const item of results.TableNames) {
    console.log(item);
  }
} catch (err) {
  console.error(err)
}
```
The `aws-sdk` package adds about 40 MB to your application.
              Replacing `var AWS = require("aws-sdk")` with ```
import {DynamoDB} from
              "@aws-sdk/client-dynamodb"
```
 reduces that overhead to about 3 MB. Restricting the
            import to just the DynamoDB client and `ListTablesCommand` command reduces the
            overhead to less than 100 KB.

```
// Load the DynamoDB client and ListTablesCommand command for Node.js
import {
  DynamoDBClient,
  ListTablesCommand
} from "@aws-sdk/client-dynamodb";
const dbclient = new DynamoDBClient({});
```
### Calling commands in v3

You can perform operations in v3 using either v2 or v3 commands. To use v3 commands
          you import the commands and the required AWS Services package clients, and run the command
          using the `.send` method using the async/await pattern.

To use v2 commands you import the required AWS Services packages, and run the v2 command directly in the package using either a callback or async/await pattern.

#### Using v3 commands

v3 provides a set of commands for each AWS Service package to enable
            you to perform operations for that AWS Service. After you install an
            AWS Service, you can browse the available commands in your project's
                `node-modules/@aws-sdk/client-`
          `PACKAGE_NAME`/commands
              folder.

You must import the commands you want to use. For example, the following code loads
            the DynamoDB service, and the `CreateTableCommand` command. 

`import { DynamoDB, CreateTableCommand } from "@aws-sdk/client-dynamodb";`To call these commands in the recommended async/await pattern, use the following syntax.

`CLIENT`.send(new `XXX`Command);For example, the following example creates a DynamoDB table using the recommended async/await pattern.

```
import { DynamoDB, CreateTableCommand } from "@aws-sdk/client-dynamodb";
const dynamodb = new DynamoDB({ region: "us-west-2" });
const tableParams = {
  TableName: 
```
`TABLE_NAME`
};
try {
  const data = await dynamodb.send(new CreateTableCommand(tableParams));
  console.log("Success", data);
} catch (err) {
  console.log("Error", err);
};#### Using v2 commands

To use v2 commands in the SDK for JavaScript, you import the full AWS Service packages, as demonstrated in the following code.

`const { DynamoDB } = require('@aws-sdk/client-dynamodb');`To call v2 commands in the recommended async/await pattern, use the following syntax.

`client`.`command`(`parameters`);

The following example uses the v2 `createTable` command to create a DynamoDB
              table using the recommended async/await pattern.

```
const { DynamoDB } = require('@aws-sdk/client-dynamodb');
const dynamoDB = new DynamoDB({ region: 'us-west-2' });
var tableParams = {
  TableName: 
```
`TABLE_NAME`
};
async function run() => {
  try {
    const data = await dynamoDB.createTable(tableParams);
    console.log("Success", data);
  }
  catch (err) {
    console.log("Error", err);
  }
};
run();The following example uses the v2 `createBucket` command to create an Amazon S3
              bucket using the callback pattern.

```
const { S3 } = require('@aws-sdk/client-s3');
const s3 = new S3({ region: 'us-west-2' });
var bucketParams = {
  Bucket : 
```
`BUCKET_NAME`
};
function run() {
  s3.createBucket(bucketParams, function (err, data) {
    if (err) {
      console.log("Error", err);
    } else {
      console.log("Success", data.Location);
    }
  })
};
run();## New middleware stack

        v2 of the SDK enabled you to modify a request throughout the multiple stages of its lifecycle by attaching event listeners to the request. This approach can make it difficult to debug what went wrong during a request’s lifecycle.

In v3, you can use a new middleware stack to control the lifecycle of an operation call. This approach provides a couple of benefits. Each middleware stage in the stack calls the next middleware stage after making any changes to the request object. This also makes debugging issues in the stack much easier, because you can see exactly which middleware stages were called leading up to the error.

The following example adds a custom header to a Amazon DynamoDB client (which we created and showed earlier) using middleware. The first argument is a function that
            accepts `next`, which is the next middleware stage in the stack to call, and
            `context`, which is an object that contains some information about the
          operation being called. The function returns a function that accepts `args`,
          which is an object that contains the parameters passed to the operation and the request. It
          returns the result from calling the next middleware with `args`.

```
dbclient.middlewareStack.add(
  (next, context) => args => {
    args.request.headers["Custom-Header"] = "value";
    return next(args);
  },
  {
    name: "my-middleware",
    override: true,
    step: "build"
  }
);
dbclient.send(new PutObjectCommand(params));
```