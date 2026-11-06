# API Gateway Management API examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_apigatewaymanagementapi_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_apigatewaymanagementapi_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with API Gateway Management API.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-connection`.

- **AWS CLI**
- 
            
                    **To delete a WebSocket connection**The following `delete-connection`example disconnects a client from the specified WebSocket API.`aws apigatewaymanagementapi delete-connection \ --connection-id``L0SM9cOFvHcCIhw=`\ --endpoint-url`https://aabbccddee.execute-api.us-west-2.amazonaws.com/prod`This command produces no output. For more information, see [Use @connections commands in your backend service](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewaymanagementapi/delete-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-connection`.

- **AWS CLI**
- 
            
                    **To get information about a WebSocket connection**The following `get-connection`example describes a connection to the specified WebSocket API.`aws apigatewaymanagementapi get-connection \ --connection-id``L0SM9cOFvHcCIhw=`\ --endpoint-url`https://aabbccddee.execute-api.us-west-2.amazonaws.com/prod`Output: `{ "ConnectedAt": "2020-04-30T20:10:33.236Z", "Identity": { "SourceIp": "192.0.2.1" }, "LastActiveAt": "2020-04-30T20:10:42.997Z" }`For more information, see [Use @connections commands in your backend service](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewaymanagementapi/get-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `post-to-connection`.

- **AWS CLI**
- 
            
                    **To send data to a WebSocket connection**The following `post-to-connection`example sends a message to a client that's connected to the specified WebSocket API.`aws apigatewaymanagementapi post-to-connection \ --connection-id``L0SM9cOFvHcCIhw=`\ --data`"Hello from API Gateway!"`\ --endpoint-url`https://aabbccddee.execute-api.us-west-2.amazonaws.com/prod`This command produces no output. For more information, see [Use @connections commands in your backend service](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-how-to-call-websocket-api-connections.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [PostToConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewaymanagementapi/post-to-connection.html)in*AWS CLI Command Reference*.
 
-