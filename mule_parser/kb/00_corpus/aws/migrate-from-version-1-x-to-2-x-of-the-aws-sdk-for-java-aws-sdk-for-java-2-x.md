# Migrate from version 1.x to 2.x of the AWS SDK for Java - AWS SDK for Java 2.x

**Source:** [https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration.html)

---

The AWS SDK for Java 2.x is a major rewrite of the 1.x code base built on top of Java 8+. It includes many updates, such as improved consistency, ease of use, and strongly enforced immutability. This section describes the major features that are new in version 2.x, and provides guidance on how to migrate your code to version 2.x from 1.x.

###### Topics

## What’s new in version 2

      - 
            You can configure your own HTTP clients. See [HTTP transport configuration](./http-configuration.html).
- 
            Async clients feature non-blocking I/O support and return `CompletableFuture`objects. See[Asynchronous programming](./asynchronous.html).
- 
            Operations that return multiple pages have autopaginated responses. This way, you can focus your code on what to do with the response, without the need to check for and get subsequent pages. See [Pagination](./pagination.html).
- 
            SDK start time performance for AWS Lambda functions is improved. See [SDK start time performance improvements](./lambda-optimize-starttime.html).
- 
            Version 2.x supports a new shorthand method for creating requests. ###### Example`dynamoDbClient.putItem(request -> request.tableName(TABLE))`

For more details about the new features and to see specific code examples, refer to the other sections of this guide.