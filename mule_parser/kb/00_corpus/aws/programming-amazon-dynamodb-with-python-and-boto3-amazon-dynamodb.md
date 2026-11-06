# Programming Amazon DynamoDB with Python and Boto3 - Amazon DynamoDB

**Source:** [https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/programming-with-python.html)

---

This guide provides an orientation to programmers wanting to use Amazon DynamoDB with Python. Learn about the different abstraction layers, configuration management, error handling, controlling retry policies, managing keep-alive, and more.

###### Topics

## About Boto

        You can access DynamoDB from Python by using the official AWS SDK for Python, commonly
            referred to as **Boto3**. The name Boto (pronounced
            boh-toh) comes from a freshwater dolphin native to the Amazon River. The Boto3 library
            is the library’s third major version, first released in 2015. The Boto3 library is quite
            large, as it supports all AWS services, not just DynamoDB. This orientation targets only
            the parts of Boto3 relevant to DynamoDB.

Boto is maintained and published by AWS as open-source project hosted on GitHub.
            It’s split into two packages: [Botocore](https://github.com/boto/botocore) and 

[Boto3](https://github.com/boto/boto3).

- 
                **Botocore**provides the low-level functionality. In Botocore you’ll find the client, session, credentials, config, and exception classes.
- 
                **Boto3**builds on top of Botocore. It offers a higher-level, more Pythonic interface. Specifically, it exposes a DynamoDB table as a Resource and offers a simpler, more elegant interface compared to the lower-level, service-oriented client interface.

Because these projects are hosted on GitHub, you can view the source code, track open issues, or submit your own issues.

## Using the Boto documentation

        Get started with the Boto documentation with the following resources:

- 
                Begin with the [Quickstart section](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)that provides a solid starting point for the package installation. Go there for instructions on getting Boto3 installed if it’s not already (Boto3 is often automatically available within AWS services such as AWS Lambda).
- 
                After that, focus on the documentation’s [DynamoDB guide](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html). It shows you how to perform the basic DynamoDB activities: create and delete a table, manipulate items, run batch operations, run a query, and perform a scan. Its examples use the**resource**interface. When you see`boto3.resource('dynamodb')`that indicates you’re using the higher-level**resource**interface.
- 
                After the guide, you can review the [DynamoDB reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html). This landing page provides an exhaustive list of the classes and methods available to you. At the top, you’ll see the`DynamoDB.Client`class. This provides low-level access to all the control-plane and data-plane operations. At the bottom, look at the`DynamoDB.ServiceResource`class. This is the higher-level Pythonic interface. With it you can create a table, do batch operations across tables, or obtain a`DynamoDB.ServiceResource.Table`instance for table-specific actions.

## Understanding the client and resource abstraction layers

        The two interfaces you'll be working with are the **client** interface and the **resource**
            interface. 

- 
                The low-level **client**interface provides a 1-to-1 mapping to the underlying service API. Every API offered by DynamoDB is available through the client. This means the client interface can provide complete functionality, but it's often more verbose and complex to use.
- 
                The higher-level **resource**interface does not provide a 1-to-1 mapping of the underlying service API. However, it provides methods that make it more convenient for you to access the service such as`batch_writer`.

Here’s an example of inserting an item using the client interface. Notice how all values are passed as a map with the key indicating their type ('S' for string, 'N' for number) and their value as a string. This is known as DynamoDB JSON format.

```
import boto3
dynamodb = boto3.client('dynamodb')
dynamodb.put_item(
    TableName='YourTableName',
    Item={
        'pk': {'S': 'id#1'},
        'sk': {'S': 'cart#123'},
        'name': {'S': 'SomeName'},
        'inventory': {'N': '500'},
        # ... more attributes ...
    }
)
```
Here's the same `PutItem` operation using the resource interface. The data
            typing is implicit:

```
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')
table.put_item(
    Item={
        'pk': 'id#1',
        'sk': 'cart#123',
        'name': 'SomeName',
        'inventory': 500,
        # ... more attributes ...
    }
)
```
If needed, you can convert between regular JSON and DynamoDB JSON using the
                `TypeSerializer` and `TypeDeserializer` classes provided with
            boto3:

```
def dynamo_to_python(dynamo_object: dict) -> dict:
    deserializer = TypeDeserializer()
    return {
        k: deserializer.deserialize(v) 
        for k, v in dynamo_object.items()
    }  
  
def python_to_dynamo(python_object: dict) -> dict:
    serializer = TypeSerializer()
    return {
        k: serializer.serialize(v)
        for k, v in python_object.items()
    }
```
Here is how to perform a query using the client interface. It expresses the query as a
            JSON construct. It uses a `KeyConditionExpression` string which requires
            variable substitution to handle any potential keyword conflicts:

```
import boto3
client = boto3.client('dynamodb')
# Construct the query
response = client.query(
    TableName='YourTableName',
    KeyConditionExpression='pk = :pk_val AND begins_with(sk, :sk_val)',
    FilterExpression='#name = :name_val',
    ExpressionAttributeValues={
        ':pk_val': {'S': 'id#1'},
        ':sk_val': {'S': 'cart#'},
        ':name_val': {'S': 'SomeName'},
    },
    ExpressionAttributeNames={
        '#name': 'name',
    }
)
```
The same query operation using the resource interface can be shortened and simplified:

```
import boto3
from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')
response = table.query(
    KeyConditionExpression=Key('pk').eq('id#1') & Key('sk').begins_with('cart#'),
    FilterExpression=Attr('name').eq('SomeName')
)
```
As a final example, imagine you want to get the approximate size of a table (which is
            metadata kept on the table that is updated about every 6 hours). With the client
            interface, you do a `describe_table()` operation and pull the answer from the
            JSON structure returned:

```
import boto3
dynamodb = boto3.client('dynamodb')
response = dynamodb.describe_table(TableName='YourTableName')
size = response['Table']['TableSizeBytes']
```
With the resource interface, the table performs the describe operation implicitly and presents the data directly as an attribute:

```
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')
size = table.table_size_bytes
```
###### Note

When considering whether to develop using the client or resource interface, be
                aware that new features will not be added to the resource interface per the [resource documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html): “The AWS Python SDK team does not intend to
                add new features to the resources interface in boto3. Existing interfaces will
                continue to operate during boto3’s lifecycle. Customers can find access to newer
                service features through the client interface.”

## Using the table resource batch_writer

        One convenience available only with the higher-level table resource is the
                `batch_writer`. DynamoDB supports batch write operations allowing up to 25
            put or delete operations in one network request. Batching like this improves efficiency
            by minimizing network round trips.

With the low-level client library, you use the `client.batch_write_item()`
            operation to run batches. You must manually split your work into batches of 25. After
            each operation, you also have to request to receive a list of unprocessed items (some of
            the write operations may succeed while others could fail). You then have to pass those
            unprocessed items again into a later `batch_write_item()` operation. There's
            a significant amount of boilerplate code.

The [Table.batch_writer](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/table/batch_writer.html) method creates a context manager for writing objects in
            a batch. It presents an interface where it seems as if you're writing items one at a
            time, but internally it's buffering and sending the items in batches. It also handles
            unprocessed item retries implicitly.

```
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')
movies = # long list of movies in {'pk': 'val', 'sk': 'val', etc} format
with table.batch_writer() as writer:
    for movie in movies:
        writer.put_item(Item=movie)
```
## Additional code examples that explore the client and resource layers

        You can also refer to the following code sample repositories that explore usage of the various functions, using both client and resource:

## Understanding how the Client and Resource objects interact with sessions and threads

        The Resource object is not thread safe and should not be shared across threads or
            processes. Refer to the [guide on Resource](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html#multithreading-or-multiprocessing-with-resources) for more details.

The Client object, in contrast, is generally thread safe, except for specific advanced
            features. Refer to the [guide on Clients](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html#multithreading-or-multiprocessing-with-clients) for more details. 

The Session object is not thread safe. So, each time you make a Client or Resource in
            a multi-threaded environment you should create a new Session first and then make the
            Client or Resource from the Session. Refer to the [guide on Sessions](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html#multithreading-or-multiprocessing-with-sessions) for more details. 

When you call the `boto3.resource()`, you’re implicitly using the default
            Session. This is convenient for writing single-threaded code. When writing
            multi-threaded code, you’ll want to first construct a new Session for each thread and
            then retrieve the resource from that Session:

```
# Explicitly create a new Session for this thread 
session = boto3.Session()
dynamodb = session.resource('dynamodb')
```
## Customizing the Config object

        When constructing a Client or Resource object, you can pass optional named parameters
            to customize behavior. The parameter named `config` unlocks a variety of
            functionality. It’s an instance of `botocore.client.Config` and the [reference documentation for Config](https://botocore.amazonaws.com/v1/documentation/api/latest/reference/config.html) shows everything it exposes for you to
            control. The 

[guide to Configuration](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html)provides a good overview.

###### Note

You can modify many of these behavioral settings at the Session level, within the AWS configuration file, or as environment variables.

**Config for timeouts**

One use of a custom config is to adjust networking behaviors:

- 
                **connect_timeout (float or int)**– The time in seconds till a timeout exception is thrown when attempting to make a connection. The default is 60 seconds.
- 
                **read_timeout (float or int)**– The time in seconds till a timeout exception is thrown when attempting to read from a connection. The default is 60 seconds.

Timeouts of 60 seconds are excessive for DynamoDB. It means a transient network glitch will cause a minute’s delay for the client before it can try again. The following code shortens the timeouts to a second:

```
import boto3
from botocore.config import Config
my_config = Config(
   connect_timeout = 1.0,
   read_timeout = 1.0
)
dynamodb = boto3.resource('dynamodb', config=my_config)
```
For more discussion about timeouts, see [Tuning AWS Java SDK HTTP request settings for latency-aware DynamoDB
                applications](https://aws.amazon.com/blogs/database/tuning-aws-java-sdk-http-request-settings-for-latency-aware-amazon-dynamodb-applications/). Note the Java SDK has more timeout configurations than
            Python.

**Config for keep-alive**

If you're using botocore 1.27.84 or later, you can also control **TCP Keep-Alive**:

- 
                **tcp_keepalive**(bool) - Enables the TCP Keep-Alive socket option used when creating new connections if set to`True`( defaults to`False`). This is only available starting with botocore 1.27.84.

Setting TCP Keep-Alive to `True` can reduce average latencies. Here's
            sample code that conditionally sets TCP Keep-Alive to true when you have the right
            botocore version:

```
import botocore
import boto3
from botocore.config import Config
from distutils.version import LooseVersion
required_version = "1.27.84"
current_version = botocore.__version__
my_config = Config(
   connect_timeout = 0.5,
   read_timeout = 0.5
)
if LooseVersion(current_version) > LooseVersion(required_version):
    my_config = my_config.merge(Config(tcp_keepalive = True))
dynamodb = boto3.resource('dynamodb', config=my_config)
```
###### Note

TCP Keep-Alive is different than HTTP Keep-Alive. With TCP Keep-Alive, small packets are sent by the underlying operating system over the socket connection to keep the connection alive and immediately detect any drops. With HTTP Keep-Alive, the web connection built on the underlying socket gets reused. HTTP Keep-Alive is always enabled with boto3.

There's a limit to how long an idle connection can be kept alive. Consider sending periodic requests (say every minute) if you have an idle connection but want the next request to use an already-established connection.

**Config for retries**

The config also accepts a dictionary called **retries**
            where you can specify your desired retry behavior. Retries happen within the SDK when
            the SDK receives an error and the error is of a transient type. If an error is retried
            internally (and a retry eventually produces a successful response), there's no error
            seen from the calling code's perspective, just a slightly elevated latency. Here are the
            values you can specify:

- 
                **max_attempts**– An integer representing the maximum number of retry attempts that will be made on a single request. For example, setting this value to 2 will result in the request being retried at most two times after the initial request. Setting this value to 0 will result in no retries ever being attempted after the initial request.
- 
                **total_max_attempts**– An integer representing the maximum number of total attempts that will be made on a single request. This includes the initial request, so a value of 1 indicates that no requests will be retried. If`total_max_attempts`and`max_attempts`are both provided,`total_max_attempts`takes precedence.`total_max_attempts`is preferred over`max_attempts`because it maps to the`AWS_MAX_ATTEMPTS`environment variable and the`max_attempts`config file value.
- 
                **mode**– A string representing the type of retry mode botocore should use. Valid values are:- 
                        **legacy**– The default mode. Waits 50ms the first retry, then uses exponential backoff with a base factor of 2. For DynamoDB, it performs up to 10 total max attempts (unless overridden with the above).###### NoteWith exponential backoff, the last attempt will wait almost 13 seconds. 
- 
                        **standard**– Named standard because it’s more consistent with other AWS SDKs. Waits a random time from 0ms to 1,000ms for the first retry. If another retry is necessary, it picks another random time from 0ms to 1,000ms and multiplies it by 2. If an additional retry is necessary, it does the same random pick multiplied by 4, and so on. Each wait is capped at 20 seconds. This mode will perform retries on more detected failure conditions than the`legacy`mode. For DynamoDB, it performs up to 3 total max attempts (unless overridden with the above).
- 
                        **adaptive**- An experimental retry mode that includes all the functionality of standard mode but adds automatic client-side throttling. With adaptive rate limiting, SDKs can slow down the rate at which requests are sent to better accommodate the capacity of AWS services. This is a provisional mode whose behavior might change.
 
- 
                        

An expanded definition of these retry modes can be found in the [guide to retries](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html) as well as in the 

[Retry behavior topic in the SDK reference](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html).

Here’s an example that explicitly uses the `legacy` retry policy with a
            maximum of 3 total requests (2 retries):

```
import boto3
from botocore.config import Config
my_config = Config(
   connect_timeout = 1.0,
   read_timeout = 1.0,
   retries = {
     'mode': 'legacy',
     'total_max_attempts': 3
   }
)
dynamodb = boto3.resource('dynamodb', config=my_config)
```
Because DynamoDB is a highly-available, low-latency system, you may want to be more aggressive with the speed of retries than the built-in retry policies allow. You can implement your own retry policy by setting the max attempts to 0, catching the exceptions yourself, and retrying as appropriate from your own code instead of relying on boto3 to do implicit retries.

If you manage your own retry policy, you'll want to differentiate between throttles and errors:

- 
                A **throttle**(indicated by a`ProvisionedThroughputExceededException`or`ThrottlingException`) indicates a healthy service that's informing you that you've exceeded your read or write capacity on a DynamoDB table or partition. Every millisecond that passes, a bit more read or write capacity is made available, so you can retry quickly (such as every 50ms) to attempt to access that newly released capacity. With throttles, you don't especially need exponential backoff because throttles are lightweight for DynamoDB to return and incur no per-request charge to you. Exponential backoff assigns longer delays to client threads that have already waited the longest, which statistically extends the p50 and p99 outward.
- 
                An **error**(indicated by an`InternalServerError`or a`ServiceUnavailable`, among others) indicates a transient issue with the service. This can be for the whole table or possibly just the partition you're reading from or writing to. With errors, you can pause longer before retries (such as 250ms or 500ms) and use jitter to stagger the retries.

**Config for max pool connections**

Lastly, the config lets you control the connection pool size:

- 
                **max_pool_connections (int)**– The maximum number of connections to keep in a connection pool. If this value is not set, the default value of 10 is used.

This option controls the maximum number of HTTP connections to keep pooled for reuse. A different pool is kept per Session. If you anticipate more than 10 threads going against clients or resources built off the same Session, you should consider raising this, so threads don't have to wait on other threads using a pooled connection.

```
import boto3
from botocore.config import Config
my_config = Config(
   max_pool_connections = 20
)
# Setup a single session holding up to 20 pooled connections
session = boto3.Session(my_config)
# Create up to 20 resources against that session for handing to threads
# Notice the single-threaded access to the Session and each Resource
resource1 = session.resource('dynamodb')
resource2 = session.resource('dynamodb')
# etc
```
## Error handling

        AWS service exceptions aren’t all statically defined in Boto3. This is because
            errors and exceptions from AWS services vary widely and are subject to change. Boto3
            wraps all service exceptions as a `ClientError` and exposes the details as
            structured JSON. For example, an error response might be structured like this:

```
{
    'Error': {
        'Code': 'SomeServiceException',
        'Message': 'Details/context around the exception or error'
    },
    'ResponseMetadata': {
        'RequestId': '1234567890ABCDEF',
        'HostId': 'host ID data will appear here as a hash',
        'HTTPStatusCode': 400,
        'HTTPHeaders': {'header metadata key/values will appear here'},
        'RetryAttempts': 0
    }
}
```
The following code catches any `ClientError` exceptions and looks at the
            string value of the `Code` within the `Error` to determine what
            action to take:

```
import botocore
import boto3
dynamodb = boto3.client('dynamodb')
try:
    response = dynamodb.put_item(...)
except botocore.exceptions.ClientError as err:
    print('Error Code: {}'.format(err.response['Error']['Code']))
    print('Error Message: {}'.format(err.response['Error']['Message']))
    print('Http Code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
    print('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
    if err.response['Error']['Code'] in ('ProvisionedThroughputExceededException', 'ThrottlingException'):
        print("Received a throttle")
    elif err.response['Error']['Code'] == 'InternalServerError':
        print("Received a server error")
    else:
        raise err
```
Some (but not all) exception codes have been materialized as top-level classes. You can choose to handle these directly. When using the Client interface, these exceptions are dynamically populated on your client and you catch these exceptions using your client instance, like this:

`except ddb_client.exceptions.ProvisionedThroughputExceededException:`When using the Resource interface, you have to use `.meta.client` to
            traverse from the resource to the underlying Client to access the exceptions, like
            this:

`except ddb_resource.meta.client.exceptions.ProvisionedThroughputExceededException:`To review the list of materialized exception types, you can generate the list dynamically:

```
ddb = boto3.client("dynamodb")
print([e for e in dir(ddb.exceptions) if e.endswith('Exception') or e.endswith('Error')])
```
When doing a write operation with a condition expression, you can request that if the expression fails the value of the item should be returned in the error response.

```
try:
    response = table.put_item(
        Item=item,
        ConditionExpression='attribute_not_exists(pk)',
        ReturnValuesOnConditionCheckFailure='ALL_OLD'
    )
except table.meta.client.exceptions.ConditionalCheckFailedException as e:
    print('Item already exists:', e.response['Item'])
```
For further reading on error handling and exceptions:

- 
                The [boto3 guide on error handling](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/error-handling.html)has more information on error handling techniques.
- 
                The [DynamoDB developer guide section on programming errors](./Programming.Errors.html)lists what errors you might encounter.
- 
                The documentation on each API operation lists what errors that call might generate (for example [BatchWriteItem](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BatchWriteItem.html)).

## Logging

        The boto3 library integrates with Python's built-in logging module for tracking what happens during a session. To control logging levels, you can configure the logging module:

```
import logging
logging.basicConfig(level=logging.INFO)
```
This configures the root logger to log `INFO` and above level messages.
            Logging messages which are less severe than level will be ignored. Logging levels
            include `DEBUG`, `INFO`, `WARNING`, `ERROR`,
            and `CRITICAL`. The default is `WARNING`.

Loggers in boto3 are hierarchical. The library uses a few different loggers, each corresponding to different parts of the library. You can separately control the behavior of each:

- 
                **boto3**: The main logger for the boto3 module.
- 
                **botocore**: The main logger for the botocore package.
- 
                **botocore.auth**: Used for logging AWS signature creation for requests.
- 
                **botocore.credentials**: Used for logging the process of credential fetching and refresh.
- 
                **botocore.endpoint**: Used for logging request creation before it's sent over the network.
- 
                **botocore.hooks**: Used for logging events triggered in the library.
- 
                **botocore.loaders**: Used for logging when parts of AWS service models are loaded.
- 
                **botocore.parsers**: Used for logging AWS service responses before they're parsed.
- 
                **botocore.retryhandler**: Used for logging the processing of AWS service request retries (legacy mode).
- 
                **botocore.retries.standard**: Used for logging the processing of AWS service request retries (standard or adaptive mode).
- 
                **botocore.utils**: Used for logging miscellaneous activities in the library.
- 
                **botocore.waiter**: Used for logging the functionality of waiters, which poll an AWS service until a certain state is reached.

Other libraries log as well. Internally, boto3 uses the third party urllib3 for HTTP connection handling. When latency is important, you can watch its logs to ensure your pool is being well utilized by seeing when urllib3 establishes a new connection or closes an idle one down.

- 
                **urllib3.connectionpool:**Use for logging connection pool handling events.

The following code snippet sets most logging to `INFO` with
                `DEBUG` logging for endpoint and connection pool activity:

```
import logging
logging.getLogger('boto3').setLevel(logging.INFO)
logging.getLogger('botocore').setLevel(logging.INFO)
logging.getLogger('botocore.endpoint').setLevel(logging.DEBUG)
logging.getLogger('urllib3.connectionpool').setLevel(logging.DEBUG)
```
## Event hooks

        Botocore emits events during various parts of its execution. You can register handlers for these events so that whenever an event is emitted, your handler will be called. This lets you extend the behavior of botocore without having to modify the internals.

For instance, let's say you want to keep track of every time a `PutItem`
            operation is called on any DynamoDB table in your application. You might register on the
                `'provide-client-params.dynamodb.PutItem'` event to catch and log every
            time a `PutItem` operation is invoked on the associated Session. Here's an
            example:

```
import boto3
import botocore
import logging
def log_put_params(params, **kwargs):
    if 'TableName' in params and 'Item' in params:
        logging.info(f"PutItem on table {params['TableName']}: {params['Item']}")
logging.basicConfig(level=logging.INFO)
session = boto3.Session()
event_system = session.events
# Register our interest in hooking in when the parameters are provided to PutItem
event_system.register('provide-client-params.dynamodb.PutItem', log_put_params)
# Now, every time you use this session to put an item in DynamoDB,
# it will log the table name and item data.
dynamodb = session.resource('dynamodb')
table = dynamodb.Table('YourTableName')
table.put_item(
    Item={
        'pk': '123',
        'sk': 'cart#123',
        'item_data': 'YourItemData',
        # ... more attributes ...
    }
)
```
Within the handler, you can even manipulate the params programmatically to change behavior:

`params['TableName'] = "NewTableName"`For more information on events, see the [botocore documentation on events](https://botocore.amazonaws.com/v1/documentation/api/latest/topics/events.html) and the 

[boto3 documentation on events](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/events.html).

## Pagination and the Paginator

        Some requests, such as Query and Scan, limit the size of data returned on a single request and require you to make repeated requests to pull subsequent pages.

You can control the maximum number of items to be read for each page with the
                `limit` parameter. For example, if you want the last 10 items, you can
            use `limit` to retrieve only the last 10. Note the limit is how much should
            be read from the table before any filtering is applied. There's no way to specify you
            want exactly 10 after filtering; you can only control the pre-filtered count and check
            client-side when you've actually retrieved 10. Regardless of the limit, every response
            always has a maximum size of 1 MB.

If the response includes a `LastEvaluatedKey`, it indicates the response
            ended because it hit a count or size limit. The key is the last key evaluated for the
            response. You can retrieve this `LastEvaluatedKey` and pass it to a follow-up
            call as `ExclusiveStartKey` to read the next chunk from that starting point.
            When there's no `LastEvaluatedKey` returned that, means there are no more
            items matching the Query or Scan.

Here's a simple example (using the Resource interface, but the Client interface has the same pattern) that reads at most 100 items per page and loops until all items have been read.

```
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('YourTableName')
query_params = {
    'KeyConditionExpression': Key('pk').eq('123') & Key('sk').gt(1000),
    'Limit': 100
}
while True:
    response = table.query(**query_params)
    # Process the items however you like
    for item in response['Items']:
        print(item)
    # No LastEvaluatedKey means no more items to retrieve
    if 'LastEvaluatedKey' not in response:
        break
    # If there are possibly more items, update the start key for the next page
    query_params['ExclusiveStartKey'] = response['LastEvaluatedKey']
```
For convenience, boto3 can do this for you with Paginators. However, it only works with the Client interface. Here's the code rewritten to use Paginators:

```
import boto3
dynamodb = boto3.client('dynamodb')
paginator = dynamodb.get_paginator('query')
query_params = {
    'TableName': 'YourTableName',
    'KeyConditionExpression': 'pk = :pk_val AND sk > :sk_val',
    'ExpressionAttributeValues': {
        ':pk_val': {'S': '123'},
        ':sk_val': {'N': '1000'},
    },
    'Limit': 100
}
page_iterator = paginator.paginate(**query_params)
for page in page_iterator:
    # Process the items however you like
    for item in page['Items']:
        print(item)
```
For more information, see the [Guide on Paginators](https://botocore.amazonaws.com/v1/documentation/api/latest/topics/events.html) and the 

[API reference for DynamoDB.Paginator.Query](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/paginator/Query.html).

###### Note

Paginators also have their own configuration settings named `MaxItems`,
                    `StartingToken`, and `PageSize`. For paginating with
                DynamoDB, you should ignore these settings.

## Waiters

        Waiters provide the ability to wait for something to complete before proceeding. At present, they only support waiting for a table to be created or deleted. In the background, the waiter operation does a check for you every 20 seconds up to 25 times. You could do this yourself, but using a waiter is elegant when writing automation.

This code shows how to wait for a particular table to have been created:

```
# Create a table, wait until it exists, and print its ARN
response = client.create_table(...)
waiter = client.get_waiter('table_exists')
waiter.wait(TableName='YourTableName')
print('Table created:', response['TableDescription']['TableArn']
```
For more information, see the [Guide to Waiters](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html#waiters) and 

[Reference on Waiters](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#waiters).