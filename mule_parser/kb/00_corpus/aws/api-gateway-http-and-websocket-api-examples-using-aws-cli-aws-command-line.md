# API Gateway HTTP and WebSocket API examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_apigatewayv2_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_apigatewayv2_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with API Gateway HTTP and WebSocket API.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-api-mapping`.

- **AWS CLI**
- 
            
                    **To create an API mapping for an API**The following `create-api-mapping`example maps the`test`stage of an API to the`/myApi`path of the`regional.example.com`custom domain name.`aws apigatewayv2 create-api-mapping \ --domain-name``regional.example.com`\ --api-mapping-key`myApi`\ --api-id`a1b2c3d4`\ --stage`test`Output: `{ "ApiId": "a1b2c3d4", "ApiMappingId": "0qzs2sy7bh", "ApiMappingKey": "myApi" "Stage": "test" }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateApiMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-api`.

- **AWS CLI**
- 
            
                    **To create an HTTP API**The following `create-api`example creates an HTTP API by using quick create. You can use quick create to create an API with an AWS Lambda or HTTP integration, a default catch-all route, and a default stage that is configured to automatically deploy changes. The following command uses quick create to create an HTTP API that integrates with a Lambda function.`aws apigatewayv2 create-api \ --name``my-http-api`\ --protocol-type`HTTP`\ --target`arn:aws:lambda:us-west-2:123456789012:function:my-lambda-function`Output: `{ "ApiEndpoint": "https://a1b2c3d4.execute-api.us-west-2.amazonaws.com", "ApiId": "a1b2c3d4", "ApiKeySelectionExpression": "$request.header.x-api-key", "CreatedDate": "2020-04-08T19:05:45+00:00", "Name": "my-http-api", "ProtocolType": "HTTP", "RouteSelectionExpression": "$request.method $request.path" }`For more information, see [Developing an HTTP API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html)in the*Amazon API Gateway Developer Guide*.**To create a WebSocket API**The following `create-api`example creates a WebSocket API with the specified name.`aws apigatewayv2 create-api \ --name``"myWebSocketApi"`\ --protocol-type`WEBSOCKET`\ --route-selection-expression '`$request.body.action`'Output: `{ "ApiKeySelectionExpression": "$request.header.x-api-key", "Name": "myWebSocketApi", "CreatedDate": "2018-11-15T06:23:51Z", "ProtocolType": "WEBSOCKET", "RouteSelectionExpression": "'$request.body.action'", "ApiId": "aabbccddee" }`For more information, see [Create a WebSocket API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-create-empty-api.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-authorizer`.

- **AWS CLI**
- 
            
                    **To create a JWT authorizer for an HTTP API**The following `create-authorizer`example creates a JWT authorizer that uses Amazon Cognito as an identity provider.`aws apigatewayv2 create-authorizer \ --name``my-jwt-authorizer`\ --api-id`a1b2c3d4`\ --authorizer-type`JWT`\ --identity-source '`$request.header.Authorization`' \ --jwt-configuration`Audience=123456abc,Issuer=https://cognito-idp.us-west-2.amazonaws.com/us-west-2_abc123`Output: `{ "AuthorizerId": "a1b2c3", "AuthorizerType": "JWT", "IdentitySource": [ "$request.header.Authorization" ], "JwtConfiguration": { "Audience": [ "123456abc" ], "Issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_abc123" }, "Name": "my-jwt-authorizer" }`For more information, see [Controlling access to HTTP APIs with JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-deployment`.

- **AWS CLI**
- 
            
                    **To create a deployment for an API**The following `create-deployment`example creates a deployment for an API and associates that deployment with the`dev`stage of the API.`aws apigatewayv2 create-deployment \ --api-id``a1b2c3d4`\ --stage-name`dev`Output: `{ "AutoDeployed": false, "CreatedDate": "2020-04-06T23:38:08Z", "DeploymentId": "53lz9l", "DeploymentStatus": "DEPLOYED" }`For more information, see [API deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html#apigateway-definition-api-deployment)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-domain-name`.

- **AWS CLI**
- 
            
                    **To create a custom domain name**The following `create-domain-name`example creates a regional custom domain name for an API.`aws apigatewayv2 create-domain-name \ --domain-name``regional.example.com`\ --domain-name-configurations`CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678`Output: `{ "ApiMappingSelectionExpression": "$request.basepath", "DomainName": "regional.example.com", "DomainNameConfigurations": [ { "ApiGatewayDomainName": "d-id.execute-api.us-west-2.amazonaws.com", "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678", "EndpointType": "REGIONAL", "HostedZoneId": "123456789111", "SecurityPolicy": "TLS_1_2", "DomainNameStatus": "AVAILABLE" } ] }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-integration`.

- **AWS CLI**
- 
            
                    **To create a WebSocket API integration**The following `create-integration`example creates a mock integration for a WebSocket API.`aws apigatewayv2 create-integration \ --api-id``aabbccddee`\ --passthrough-behavior`WHEN_NO_MATCH`\ --timeout-in-millis`29000`\ --connection-type`INTERNET`\ --integration-type`MOCK`Output: `{ "ConnectionType": "INTERNET", "IntegrationId": "0abcdef", "IntegrationResponseSelectionExpression": "${integration.response.statuscode}", "IntegrationType": "MOCK", "PassthroughBehavior": "WHEN_NO_MATCH", "PayloadFormatVersion": "1.0", "TimeoutInMillis": 29000 }`For more information, see [Set up a WebSocket API integration request in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-requests.html)in the*Amazon API Gateway Developer Guide*.**To create an HTTP API integration**The following `create-integration`example creates an AWS Lambda integration for an HTTP API.`aws apigatewayv2 create-integration \ --api-id``a1b2c3d4`\ --integration-type`AWS_PROXY`\ --integration-uri`arn:aws:lambda:us-west-2:123456789012:function:my-function`\ --payload-format-version`2.0`Output: `{ "ConnectionType": "INTERNET", "IntegrationId": "0abcdef", "IntegrationMethod": "POST", "IntegrationType": "AWS_PROXY", "IntegrationUri": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "PayloadFormatVersion": "2.0", "TimeoutInMillis": 30000 }`For more information, see [Configuring integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-route`.

- **AWS CLI**
- 
            
                    **To create a $default route for a WebSocket or HTTP API**The following `create-route`example creates a`$default`route for a WebSocket or HTTP API.`aws apigatewayv2 create-route \ --api-id``aabbccddee`\ --route-key '`$default`'Output: `{ "ApiKeyRequired": false, "AuthorizationType": "NONE", "RouteKey": "$default", "RouteId": "1122334" }`For more information, see [Working with routes for WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-add-route.html)in the*Amazon API Gateway Developer Guide***To create a route for an HTTP API**The following `create-route`example creates a route named`signup`that accepts POST requests.`aws apigatewayv2 create-route \ --api-id``aabbccddee`\ --route-key '`POST /signup`'Output: `{ "ApiKeyRequired": false, "AuthorizationType": "NONE", "RouteKey": "POST /signup", "RouteId": "1122334" }`For more information, see [Working with routes for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html)in the*Amazon API Gateway Developer Guide*- 
                    For API details, see [CreateRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-routing-rule`.

- **AWS CLI**
- 
            
                    **To create a routing rule**The following `create-routing-rule`example creates a routing rule with a priority of`50`.`aws apigatewayv2 create-routing-rule \ --domain-name '``regional.example.com`' \ --priority`50`\ --conditions '`[ \ { \ "MatchBasePaths": { \ "AnyOf": [ \ "PetStoreShopper" \ ] \ } \ } \ ]`' \ --actions '`[ \ { \ "InvokeApi": { \ "ApiId": "abcd1234", \ "Stage": "prod" \ } \ } \ ]`'Output: `{ "Actions": [ { "InvokeApi": { "ApiId": "abcd1234", "Stage": "prod", "StripBasePath": false } } ], "Conditions": [ { "MatchBasePaths": { "AnyOf": [ "PetStoreShopper" ] } } ], "Priority": 50, "RoutingRuleArn": "arn:aws:apigateway:us-east-2:123456789012:/domainnames/regional.example.com/routingrules/aaa111", "RoutingRuleId": "aaa111" }`For more information, see [Routing rules to connect API stages to a custom domain name for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateRoutingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-routing-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stage`.

- **AWS CLI**
- 
            
                    **To create a stage**The following `create-stage`example creates a stage named dev for an API.`aws apigatewayv2 create-stage \ --api-id``a1b2c3d4`\ --stage-name`dev`Output: `{ "CreatedDate": "2020-04-06T23:23:46Z", "DefaultRouteSettings": { "DetailedMetricsEnabled": false }, "LastUpdatedDate": "2020-04-06T23:23:46Z", "RouteSettings": {}, "StageName": "dev", "StageVariables": {}, "Tags": {} }`For more information, see [Working with stages for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-vpc-link`.

- **AWS CLI**
- 
            
                    **To create a VPC link for an HTTP API**The following `create-vpc-link`example creates a VPC link for HTTP APIs.`aws apigatewayv2 create-vpc-link \ --name``MyVpcLink`\ --subnet-ids`subnet-aaaa``subnet-bbbb`\ --security-group-ids`sg1234``sg5678`Output: `{ "CreatedDate": "2020-04-07T00:11:46Z", "Name": "MyVpcLink", "SecurityGroupIds": [ "sg1234", "sg5678" ], "SubnetIds": [ "subnet-aaaa", "subnet-bbbb" ], "Tags": {}, "VpcLinkId": "abcd123", "VpcLinkStatus": "PENDING", "VpcLinkStatusMessage": "VPC link is provisioning ENIs", "VpcLinkVersion": "V2" }`For more information, see [Working with VPC links for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateVpcLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/create-vpc-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-access-log-settings`.

- **AWS CLI**
- 
            
                    **To disable access logging for an API**The following `delete-access-log-settings`example deletes the access log settings for the`$default`stage of an API. To disable access logging for a stage, delete its access log settings.`aws apigatewayv2 delete-access-log-settings \ --api-id``a1b2c3d4`\ --stage-name '`$default`'This command produces no output. For more information, see [Configuring logging for an HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-logging.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteAccessLogSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-access-log-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-api-mapping`.

- **AWS CLI**
- 
            
                    **To delete an API mapping**The following `delete-api-mapping`example deletes an API mapping for the`api.example.com`custom domain name.`aws apigatewayv2 delete-api-mapping \ --api-mapping-id``a1b2c3`\ --domain-name`api.example.com`This command produces no output. For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteApiMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-api`.

- **AWS CLI**
- 
            
                    **To delete an API**The following `delete-api`example deletes an API.`aws apigatewayv2 delete-api \ --api-id``a1b2c3d4`This command produces no output. For more information, see [Working with HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)and[Working with WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-authorizer`.

- **AWS CLI**
- 
            
                    **To delete an authorizer**The following `delete-authorizer`example deletes an authorizer.`aws apigatewayv2 delete-authorizer \ --api-id``a1b2c3d4`\ --authorizer-id`a1b2c3`This command produces no output. For more information, see [Controlling access to HTTP APIs with JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cors-configuration`.

- **AWS CLI**
- 
            
                    **To delete the CORS configuration for an HTTP API**The following `delete-cors-configuration`example disables CORS for an HTTP API by deleting its CORS configuration.`aws apigatewayv2 delete-cors-configuration \ --api-id``a1b2c3d4`This command produces no output. For more information, see [Configuring CORS for an HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteCorsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-cors-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-deployment`.

- **AWS CLI**
- 
            
                    **To delete a deployment**The following `delete-deployment`example deletes a deployment of an API.`aws apigatewayv2 delete-deployment \ --api-id``a1b2c3d4`\ --deployment-id`a1b2c3`This command produces no output. For more information, see [API deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html#apigateway-definition-api-deployment)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain-name`.

- **AWS CLI**
- 
            
                    **To delete a custom domain name**The following `delete-domain-name`example deletes a custom domain name.`aws apigatewayv2 delete-domain-name \ --domain-name``api.example.com`This command produces no output. For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-integration`.

- **AWS CLI**
- 
            
                    **To delete an integration**The following `delete-integration`example deletes an API integration.`aws apigatewayv2 delete-integration \ --api-id``a1b2c3d4`\ --integration-id`a1b2c3`This command produces no output. For more information, see [Configuring integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)and[Setting up WebSocket API integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integrations.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-route-settings`.

- **AWS CLI**
- 
            
                    **To delete route settings**The following `delete-route-settings`example deletes the route settings for the specified route.`aws apigatewayv2 delete-route-settings \ --api-id``a1b2c3d4`\ --stage-name`dev`\ --route-key '`GET /pets`'This command produces no output. For more information, see [Working with routes for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteRouteSettings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route-settings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-route`.

- **AWS CLI**
- 
            
                    **To delete a route**The following `delete-route`example deletes an API route.`aws apigatewayv2 delete-route \ --api-id``a1b2c3d4`\ --route-id`a1b2c3`This command produces no output. For more information, see [Working with routes for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-routing-rule`.

- **AWS CLI**
- 
            
                    **To delete a routing rule**The following `delete-routing-rule`example deletes a routing rule for a custom domain name.`aws apigatewayv2 delete-routing-rule \ --domain-name '``regional.example.com`' \ --routing-rule-id`aaa111`This command produces no output. For more information, see [Routing rules to connect API stages to a custom domain name for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteRoutingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-routing-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stage`.

- **AWS CLI**
- 
            
                    **To delete a stage**The following `delete-stage`example deletes the`test`stage of an API.`aws apigatewayv2 delete-stage \ --api-id``a1b2c3d4`\ --stage-name`test`This command produces no output. For more information, see [Working with stages for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-vpc-link`.

- **AWS CLI**
- 
            
                    **To delete a VPC link for an HTTP API**The following `delete-vpc-link`example deletes a VPC link.`aws apigatewayv2 delete-vpc-link \ --vpc-link-id``abcd123`This command produces no output. For more information, see [Working with VPC links for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteVpcLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/delete-vpc-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `export-api`.

- **AWS CLI**
- 
            
                    **To export an OpenAPI definition of an HTTP API**The following `export-api`example exports an OpenAPI 3.0 definition of an API stage named`prod`to a YAML file named`stage-definition.yaml`. The exported definition file includes API Gateway extensions by default.`aws apigatewayv2 export-api \ --api-id``a1b2c3d4`\ --output-type`YAML`\ --specification`OAS30`\ --stage-name`prod`\`stage-definition.yaml`This command produces no output. For more information, see [Exporting an HTTP API from API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-export.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [ExportApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/export-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-api-mapping`.

- **AWS CLI**
- 
            
                    **To get information about an API mapping for a custom domain name**The following `get-api-mapping`example displays information about an API mapping for the`api.example.com`custom domain name.`aws apigatewayv2 get-api-mapping \ --api-mapping-id``a1b2c3`\ --domain-name`api.example.com`Output: `{ "ApiId": "a1b2c3d4", "ApiMappingId": "a1b2c3d5", "ApiMappingKey": "myTestApi" "Stage": "test" }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetApiMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-api-mappings`.

- **AWS CLI**
- 
            
                    **To get API mappings for a custom domain name**The following `get-api-mappings`example displays a list of all of the API mappings for the`api.example.com`custom domain name.`aws apigatewayv2 get-api-mappings \ --domain-name``api.example.com`Output: `{ "Items": [ { "ApiId": "a1b2c3d4", "ApiMappingId": "a1b2c3d5", "ApiMappingKey": "myTestApi" "Stage": "test" }, { "ApiId": "a5b6c7d8", "ApiMappingId": "a1b2c3d6", "ApiMappingKey": "myDevApi" "Stage": "dev" }, ] }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetApiMappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api-mappings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-api`.

- **AWS CLI**
- 
            
                    **To retrieve information about an API**The following `get-api`example displays information about an API.`aws apigatewayv2 get-api \ --api-id``a1b2c3d4`Output: `{ "ApiEndpoint": "https://a1b2c3d4.execute-api.us-west-2.amazonaws.com", "ApiId": "a1b2c3d4", "ApiKeySelectionExpression": "$request.header.x-api-key", "CreatedDate": "2020-03-28T00:32:37Z", "Name": "my-api", "ProtocolType": "HTTP", "RouteSelectionExpression": "$request.method $request.path", "Tags": { "department": "finance" } }`- 
                    For API details, see [GetApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-apis`.

- **AWS CLI**
- 
            
                    **To retrieve a list of APIs**The following `get-apis`example lists all of the APIs for the current user.`aws apigatewayv2 get-apis`Output: `{ "Items": [ { "ApiEndpoint": "wss://a1b2c3d4.execute-api.us-west-2.amazonaws.com", "ApiId": "a1b2c3d4", "ApiKeySelectionExpression": "$request.header.x-api-key", "CreatedDate": "2020-04-07T20:21:59Z", "Name": "my-websocket-api", "ProtocolType": "WEBSOCKET", "RouteSelectionExpression": "$request.body.message", "Tags": {} }, { "ApiEndpoint": "https://a1b2c3d5.execute-api.us-west-2.amazonaws.com", "ApiId": "a1b2c3d5", "ApiKeySelectionExpression": "$request.header.x-api-key", "CreatedDate": "2020-04-07T20:23:50Z", "Name": "my-http-api", "ProtocolType": "HTTP", "RouteSelectionExpression": "$request.method $request.path", "Tags": {} } ] }`For more information, see [Working with HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html)and[Working with WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetApis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-apis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-authorizer`.

- **AWS CLI**
- 
            
                    **To retrieve information about an authorizer**The following `get-authorizer`example displays information about an authorizer.`aws apigatewayv2 get-authorizer \ --api-id``a1b2c3d4`\ --authorizer-id`a1b2c3`Output: `{ "AuthorizerId": "a1b2c3", "AuthorizerType": "JWT", "IdentitySource": [ "$request.header.Authorization" ], "JwtConfiguration": { "Audience": [ "123456abc" ], "Issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_abc123" }, "Name": "my-jwt-authorizer" }`For more information, see [Controlling access to HTTP APIs with JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-authorizers`.

- **AWS CLI**
- 
            
                    **To retrieve a list of authorizers for an API**The following `get-authorizers`example displays a list of all of the authorizers for an API.`aws apigatewayv2 get-authorizers \ --api-id``a1b2c3d4`Output: `{ "Items": [ { "AuthorizerId": "a1b2c3", "AuthorizerType": "JWT", "IdentitySource": [ "$request.header.Authorization" ], "JwtConfiguration": { "Audience": [ "123456abc" ], "Issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_abc123" }, "Name": "my-jwt-authorizer" }, { "AuthorizerId": "a1b2c4", "AuthorizerType": "JWT", "IdentitySource": [ "$request.header.Authorization" ], "JwtConfiguration": { "Audience": [ "6789abcde" ], "Issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_abc234" }, "Name": "new-jwt-authorizer" } ] }`For more information, see [Controlling access to HTTP APIs with JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetAuthorizers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-authorizers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment`.

- **AWS CLI**
- 
            
                    **To retrieve information about a deployment**The following `get-deployment`example displays information about a deployment.`aws apigatewayv2 get-deployment \ --api-id``a1b2c3d4`\ --deployment-id`abcdef`Output: `{ "AutoDeployed": true, "CreatedDate": "2020-04-07T23:58:40Z", "DeploymentId": "abcdef", "DeploymentStatus": "DEPLOYED", "Description": "Automatic deployment triggered by changes to the Api configuration" }`For more information, see [API deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html#apigateway-definition-api-deployment)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployments`.

- **AWS CLI**
- 
            
                    **To retrieve a list of deployments**The following `get-deployments`example displays a list of all of an API's deployments.`aws apigatewayv2 get-deployments \ --api-id``a1b2c3d4`Output: `{ "Items": [ { "AutoDeployed": true, "CreatedDate": "2020-04-07T23:58:40Z", "DeploymentId": "abcdef", "DeploymentStatus": "DEPLOYED", "Description": "Automatic deployment triggered by changes to the Api configuration" }, { "AutoDeployed": true, "CreatedDate": "2020-04-06T00:33:00Z", "DeploymentId": "bcdefg", "DeploymentStatus": "DEPLOYED", "Description": "Automatic deployment triggered by changes to the Api configuration" } ] }`For more information, see [API deployment](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-basic-concept.html#apigateway-definition-api-deployment)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-name`.

- **AWS CLI**
- 
            
                    **To retrieve information about a custom domain name**The following `get-domain-name`example displays information about a custom domain name.`aws apigatewayv2 get-domain-name \ --domain-name``api.example.com`Output: `{ "ApiMappingSelectionExpression": "$request.basepath", "DomainName": "api.example.com", "DomainNameConfigurations": [ { "ApiGatewayDomainName": "d-1234.execute-api.us-west-2.amazonaws.com", "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678", "EndpointType": "REGIONAL", "HostedZoneId": "123456789111", "SecurityPolicy": "TLS_1_2", "DomainNameStatus": "AVAILABLE" } ], "Tags": {} }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-names`.

- **AWS CLI**
- 
            
                    **To retrieve a list of custom domain names**The following `get-domain-names`example displays a list of all of the custom domain names for the current user.`aws apigatewayv2 get-domain-names`Output: `{ "Items": [ { "ApiMappingSelectionExpression": "$request.basepath", "DomainName": "api.example.com", "DomainNameConfigurations": [ { "ApiGatewayDomainName": "d-1234.execute-api.us-west-2.amazonaws.com", "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678", "EndpointType": "REGIONAL", "HostedZoneId": "123456789111", "SecurityPolicy": "TLS_1_2", "DomainNameStatus": "AVAILABLE" } ] }, { "ApiMappingSelectionExpression": "$request.basepath", "DomainName": "newApi.example.com", "DomainNameConfigurations": [ { "ApiGatewayDomainName": "d-5678.execute-api.us-west-2.amazonaws.com", "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678", "EndpointType": "REGIONAL", "HostedZoneId": "123456789222", "SecurityPolicy": "TLS_1_2", "DomainNameStatus": "AVAILABLE" } ] } ] }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetDomainNames](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-domain-names.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-integration`.

- **AWS CLI**
- 
            
                    **To retrieve information about an integration**The following `get-integration`example displays information about an integration.`aws apigatewayv2 get-integration \ --api-id``a1b2c3d4`\ --integration-id`a1b2c3`Output: `{ "ApiGatewayManaged": true, "ConnectionType": "INTERNET", "IntegrationId": "a1b2c3", "IntegrationMethod": "POST", "IntegrationType": "AWS_PROXY", "IntegrationUri": "arn:aws:lambda:us-west-2:12356789012:function:hello12", "PayloadFormatVersion": "2.0", "TimeoutInMillis": 30000 }`For more information, see [Configuring integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)and[Setting up WebSocket API integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integrations.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-integrations`.

- **AWS CLI**
- 
            
                    **To retrieve a list of integrations**The following `get-integrations`example displays a list of all of an API's integrations.`aws apigatewayv2 get-integrations \ --api-id``a1b2c3d4`Output: `{ "Items": [ { "ApiGatewayManaged": true, "ConnectionType": "INTERNET", "IntegrationId": "a1b2c3", "IntegrationMethod": "POST", "IntegrationType": "AWS_PROXY", "IntegrationUri": "arn:aws:lambda:us-west-2:123456789012:function:my-function", "PayloadFormatVersion": "2.0", "TimeoutInMillis": 30000 }, { "ConnectionType": "INTERNET", "IntegrationId": "a1b2c4", "IntegrationMethod": "ANY", "IntegrationType": "HTTP_PROXY", "IntegrationUri": "https://www.example.com", "PayloadFormatVersion": "1.0", "TimeoutInMillis": 30000 } ] }`For more information, see [Configuring integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)and[Setting up WebSocket API integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integrations.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetIntegrations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-integrations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-route`.

- **AWS CLI**
- 
            
                    **To retrieve information about a route**The following `get-route`example displays information about a route.`aws apigatewayv2 get-route \ --api-id``a1b2c3d4`\ --route-id`72jz1wk`Output: `{ "ApiKeyRequired": false, "AuthorizationType": "NONE", "RouteId": "72jz1wk", "RouteKey": "ANY /pets", "Target": "integrations/a1b2c3" }`For more information, see [Working with routes for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html)in the*Amazon API Gateway Developer Guide*- 
                    For API details, see [GetRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-routes`.

- **AWS CLI**
- 
            
                    **To retrieve a list of routes**The following `get-routes`example displays a list of all of an API's routes.`aws apigatewayv2 get-routes \ --api-id``a1b2c3d4`Output: `{ "Items": [ { "ApiKeyRequired": false, "AuthorizationType": "NONE", "RouteId": "72jz1wk", "RouteKey": "ANY /admin", "Target": "integrations/a1b2c3" }, { "ApiGatewayManaged": true, "ApiKeyRequired": false, "AuthorizationType": "NONE", "RouteId": "go65gqi", "RouteKey": "$default", "Target": "integrations/a1b2c4" } ] }`For more information, see [Working with routes for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-routes.html)in the*Amazon API Gateway Developer Guide*- 
                    For API details, see [GetRoutes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-routes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-routing-rule`.

- **AWS CLI**
- 
            
                    **To get a routing rule**The following `get-routing-rule`example gets a routing rule for a domain name.`aws apigatewayv2 get-routing-rule \ --domain-name '``regional.example.com`' \ --routing-rule-id`aaa111`Output: `{ "Actions": [ { "InvokeApi": { "ApiId": "abcd1234", "Stage": "prod", "StripBasePath": false } } ], "Conditions": [ { "MatchBasePaths": { "AnyOf": [ "PetStoreShopper" ] } } ], "Priority": 50, "RoutingRuleArn": "arn:aws:apigateway:us-east-2:123456789012:/domainnames/regional.example.com/routingrules/aaa111", "RoutingRuleId": "aaa111" }`For more information, see [Routing rules to connect API stages to a custom domain name for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetRoutingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-routing-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stage`.

- **AWS CLI**
- 
            
                    **To retrieve information about a stage**The following `get-stage`example displays information about the`prod`stage of an API.`aws apigatewayv2 get-stage \ --api-id``a1b2c3d4`\ --stage-name`prod`Output: `{ "CreatedDate": "2020-04-08T00:36:05Z", "DefaultRouteSettings": { "DetailedMetricsEnabled": false }, "DeploymentId": "x1zwyv", "LastUpdatedDate": "2020-04-08T00:36:13Z", "RouteSettings": {}, "StageName": "prod", "StageVariables": { "function": "my-prod-function" }, "Tags": {} }`For more information, see [Working with stages for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stages`.

- **AWS CLI**
- 
            
                    **To retrieve a list of stages**The following `get-stages`example lists all of an API's stages.`aws apigatewayv2 get-stages \ --api-id``a1b2c3d4`Output: `{ "Items": [ { "ApiGatewayManaged": true, "AutoDeploy": true, "CreatedDate": "2020-04-08T00:08:44Z", "DefaultRouteSettings": { "DetailedMetricsEnabled": false }, "DeploymentId": "dty748", "LastDeploymentStatusMessage": "Successfully deployed stage with deployment ID 'dty748'", "LastUpdatedDate": "2020-04-08T00:09:49Z", "RouteSettings": {}, "StageName": "$default", "StageVariables": {}, "Tags": {} }, { "AutoDeploy": true, "CreatedDate": "2020-04-08T00:35:06Z", "DefaultRouteSettings": { "DetailedMetricsEnabled": false }, "LastUpdatedDate": "2020-04-08T00:35:48Z", "RouteSettings": {}, "StageName": "dev", "StageVariables": { "function": "my-dev-function" }, "Tags": {} }, { "CreatedDate": "2020-04-08T00:36:05Z", "DefaultRouteSettings": { "DetailedMetricsEnabled": false }, "DeploymentId": "x1zwyv", "LastUpdatedDate": "2020-04-08T00:36:13Z", "RouteSettings": {}, "StageName": "prod", "StageVariables": { "function": "my-prod-function" }, "Tags": {} } ] }`For more information, see [Working with stages for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetStages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-stages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-tags`.

- **AWS CLI**
- 
            
                    **To retrieve a list of tags for a resource**The following `get-tags`example lists all of an API's tags.`aws apigatewayv2 get-tags \ --resource-arn``arn:aws:apigateway:us-west-2::/apis/a1b2c3d4`Output: `{ "Tags": { "owner": "dev-team", "environment": "prod" } }`For more information, see [Tagging your API Gateway resources](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-vpc-link`.

- **AWS CLI**
- 
            
                    **To retrieve information about a VPC link**The following `get-vpc-link`example displays information about a VPC link.`aws apigatewayv2 get-vpc-link \ --vpc-link-id``abcd123`Output: `{ "CreatedDate": "2020-04-07T00:27:47Z", "Name": "MyVpcLink", "SecurityGroupIds": [ "sg1234", "sg5678" ], "SubnetIds": [ "subnet-aaaa", "subnet-bbbb" ], "Tags": {}, "VpcLinkId": "abcd123", "VpcLinkStatus": "AVAILABLE", "VpcLinkStatusMessage": "VPC link is ready to route traffic", "VpcLinkVersion": "V2" }`For more information, see [Working with VPC links for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetVpcLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-vpc-link.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-vpc-links`.

- **AWS CLI**
- 
            
                    **To retrieve a list of VPC links**The following `get-vpc-links`example displays a list of all of the VPC links for the current user.`aws apigatewayv2 get-vpc-links`Output: `{ "Items": [ { "CreatedDate": "2020-04-07T00:27:47Z", "Name": "MyVpcLink", "SecurityGroupIds": [ "sg1234", "sg5678" ], "SubnetIds": [ "subnet-aaaa", "subnet-bbbb" ], "Tags": {}, "VpcLinkId": "abcd123", "VpcLinkStatus": "AVAILABLE", "VpcLinkStatusMessage": "VPC link is ready to route traffic", "VpcLinkVersion": "V2" } { "CreatedDate": "2020-04-07T00:27:47Z", "Name": "MyOtherVpcLink", "SecurityGroupIds": [ "sg1234", "sg5678" ], "SubnetIds": [ "subnet-aaaa", "subnet-bbbb" ], "Tags": {}, "VpcLinkId": "abcd456", "VpcLinkStatus": "AVAILABLE", "VpcLinkStatusMessage": "VPC link is ready to route traffic", "VpcLinkVersion": "V2" } ] }`For more information, see [Working with VPC links for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetVpcLinks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/get-vpc-links.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-api`.

- **AWS CLI**
- 
            
                    **To import an HTTP API**The following `import-api`example creates an HTTP API from an OpenAPI 3.0 definition file named`api-definition.yaml`.`aws apigatewayv2 import-api \ --body``file://api-definition.yaml`Contents of `api-definition.yaml`:`openapi: 3.0.1 info: title: My Lambda API version: v1.0 paths: /hello: x-amazon-apigateway-any-method: x-amazon-apigateway-integration: payloadFormatVersion: 2.0 type: aws_proxy httpMethod: POST uri: arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:hello/invocations connectionType: INTERNET`Output: `{ "ApiEndpoint": "https://a1b2c3d4.execute-api.us-west-2.amazonaws.com", "ApiId": "a1b2c3d4", "ApiKeySelectionExpression": "$request.header.x-api-key", "CreatedDate": "2020-04-08T17:19:38+00:00", "Name": "My Lambda API", "ProtocolType": "HTTP", "RouteSelectionExpression": "$request.method $request.path", "Tags": {}, "Version": "v1.0" }`For more information, see [Working with OpenAPI definitions for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-open-api.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [ImportApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/import-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-routing-rules`.

- **AWS CLI**
- 
            
                    **To list routing rules**The following `list-routing-rules`example lists the routing rules for a domain name.`aws apigatewayv2 list-routing-rules \ --domain-name '``regional.example.com`'Output: `{ "RoutingRules": [ { "Actions": [ { "InvokeApi": { "ApiId": "abcd1234", "Stage": "prod", "StripBasePath": false } } ], "Conditions": [ { "MatchBasePaths": { "AnyOf": [ "PetStoreShopper" ] } } ], "Priority": 150, "RoutingRuleArn": "arn:aws:apigateway:us-east-1:123456789012:/domainnames/regional.example.com/routingrules/aaa111", "RoutingRuleId": "aaa111" } ] }`For more information, see [Routing rules to connect API stages to a custom domain name for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [ListRoutingRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/list-routing-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-routing-rule`.

- **AWS CLI**
- 
            
                    **To update a routing rule**The following `put-routing-rule`example updates the priority of a routing rule.`aws apigatewayv2 put-routing-rule \ --routing-rule-id '``aaa111`' \ --domain-name '`regional.example.com`' \ --priority`150`\ --conditions '`[ \ { \ "MatchBasePaths": { \ "AnyOf": [ \ "PetStoreShopper" \ ] \ } \ } \ ]`' \ --actions '`[ \ { \ "InvokeApi": { \ "ApiId": "abcd1234", \ "Stage": "prod" \ } \ } \ ]`'Output: `{ "Actions": [ { "InvokeApi": { "ApiId": "abcd1234", "Stage": "prod", "StripBasePath": false } } ], "Conditions": [ { "MatchBasePaths": { "AnyOf": [ "PetStoreShopper" ] } } ], "Priority": 150, "RoutingRuleArn": "arn:aws:apigateway:us-east-2:123456789012:/domainnames/regional.example.com/routingrules/aaa111", "RoutingRuleId": "aaa111" }`For more information, see [Routing rules to connect API stages to a custom domain name for REST APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/rest-api-routing-rules.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [PutRoutingRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/put-routing-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reimport-api`.

- **AWS CLI**
- 
            
                    **To reimport an HTTP API**The following `reimport-api`example updates an existing HTTP API to use the OpenAPI 3.0 definition specified in`api-definition.yaml`.`aws apigatewayv2 reimport-api \ --body``file://api-definition.yaml`\ --api-id`a1b2c3d4`Contents of `api-definition.yaml`:`openapi: 3.0.1 info: title: My Lambda API version: v1.0 paths: /hello: x-amazon-apigateway-any-method: x-amazon-apigateway-integration: payloadFormatVersion: 2.0 type: aws_proxy httpMethod: POST uri: arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:12356789012:function:hello/invocations connectionType: INTERNET`Output: `{ "ApiEndpoint": "https://a1b2c3d4.execute-api.us-west-2.amazonaws.com", "ApiId": "a1b2c3d4", "ApiKeySelectionExpression": "$request.header.x-api-key", "CreatedDate": "2020-04-08T17:19:38+00:00", "Name": "My Lambda API", "ProtocolType": "HTTP", "RouteSelectionExpression": "$request.method $request.path", "Tags": {}, "Version": "v1.0" }`For more information, see [Working with OpenAPI definitions for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-open-api.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [ReimportApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/reimport-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example adds a tag with the key name`Department`and a value of`Accounting`to the specified API.`aws apigatewayv2 tag-resource \ --resource-arn``arn:aws:apigateway:us-west-2::/apis/a1b2c3d4`\ --tags`Department=Accounting`This command produces no output. For more information, see [Tagging your API Gateway resources](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a resource**The following `untag-resource`example removes tags with the key names`Project`and`Owner`from the specified API.`aws apigatewayv2 untag-resource \ --resource-arn``arn:aws:apigateway:us-west-2::/apis/a1b2c3d4`\ --tag-keys`Project``Owner`This command produces no output. For more information, see [Tagging your API Gateway resources](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-tagging.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-api-mapping`.

- **AWS CLI**
- 
            
                    **To update an API mapping**The following `update-api-mapping`example changes an API mapping for a custom domain name. As a result, the base URL using the custom domain name for the specified API and stage becomes`https://api.example.com/dev`.`aws apigatewayv2 update-api-mapping \ --api-id``a1b2c3d4`\ --stage`dev`\ --domain-name`api.example.com`\ --api-mapping-id`0qzs2sy7bh`\ --api-mapping-key`dev`Output: `{ "ApiId": "a1b2c3d4", "ApiMappingId": "0qzs2sy7bh", "ApiMappingKey": "dev" "Stage": "dev" }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateApiMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-api`.

- **AWS CLI**
- 
            
                    **To enable CORS for an HTTP API**The following `update-api`example updates the specified API's CORS configuration to allow requests from`https://www.example.com`.`aws apigatewayv2 update-api \ --api-id``a1b2c3d4`\ --cors-configuration`AllowOrigins=https://www.example.com`Output: `{ "ApiEndpoint": "https://a1b2c3d4.execute-api.us-west-2.amazonaws.com", "ApiId": "a1b2c3d4", "ApiKeySelectionExpression": "$request.header.x-api-key", "CorsConfiguration": { "AllowCredentials": false, "AllowHeaders": [ "header1", "header2" ], "AllowMethods": [ "GET", "OPTIONS" ], "AllowOrigins": [ "https://www.example.com" ] }, "CreatedDate": "2020-04-08T18:39:37+00:00", "Name": "my-http-api", "ProtocolType": "HTTP", "RouteSelectionExpression": "$request.method $request.path", "Tags": {}, "Version": "v1.0" }`For more information, see [Configuring CORS for an HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-authorizer`.

- **AWS CLI**
- 
            
                    **To update an authorizer**The following `update-authorizer`example changes a JWT authorizer's identity source to a header named`Authorization`.`aws apigatewayv2 update-authorizer \ --api-id``a1b2c3d4`\ --authorizer-id`a1b2c3`\ --identity-source '`$request.header.Authorization`'Output: `{ "AuthorizerId": "a1b2c3", "AuthorizerType": "JWT", "IdentitySource": [ "$request.header.Authorization" ], "JwtConfiguration": { "Audience": [ "123456abc" ], "Issuer": "https://cognito-idp.us-west-2.amazonaws.com/us-west-2_abc123" }, "Name": "my-jwt-authorizer" }`For more information, see [Controlling access to HTTP APIs with JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-deployment`.

- **AWS CLI**
- 
            
                    **To change a deployment's description**The following `update-deployment`example updates a deployment's description.`aws apigatewayv2 update-deployment \ --api-id``a1b2c3d4`\ --deployment-id`abcdef`\ --description '`Manual deployment to fix integration test failures.`'Output: `{ "AutoDeployed": false, "CreatedDate": "2020-02-05T16:21:48+00:00", "DeploymentId": "abcdef", "DeploymentStatus": "DEPLOYED", "Description": "Manual deployment to fix integration test failures." }`For more information, see [Developing an HTTP API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-domain-name`.

- **AWS CLI**
- 
            
                    **To update a custom domain name**The following `update-domain-name`example specifies a new ACM certificate for the`api.example.com`custom domain name.`aws apigatewayv2 update-domain-name \ --domain-name``api.example.com`\ --domain-name-configurations`CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678`Output: `{ "ApiMappingSelectionExpression": "$request.basepath", "DomainName": "regional.example.com", "DomainNameConfigurations": [ { "ApiGatewayDomainName": "d-id.execute-api.us-west-2.amazonaws.com", "CertificateArn": "arn:aws:acm:us-west-2:123456789012:certificate/123456789012-1234-1234-1234-12345678", "EndpointType": "REGIONAL", "HostedZoneId": "123456789111", "SecurityPolicy": "TLS_1_2", "DomainNameStatus": "AVAILABLE" } ] }`For more information, see [Setting up a regional custom domain name in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-integration`.

- **AWS CLI**
- 
            
                    **To update a Lambda integration**The following `update-integration`example updates an existing AWS Lambda integration to use the specified Lambda function.`aws apigatewayv2 update-integration \ --api-id``a1b2c3d4`\ --integration-id`a1b2c3`\ --integration-uri`arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:my-new-function/invocations`Output: `{ "ConnectionType": "INTERNET", "IntegrationId": "a1b2c3", "IntegrationMethod": "POST", "IntegrationType": "AWS_PROXY", "IntegrationUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:my-new-function/invocations", "PayloadFormatVersion": "2.0", "TimeoutInMillis": 5000 }`For more information, see [Configuring integrations for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations.html)and[Setting up WebSocket API integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integrations.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-route`.

- **AWS CLI**
- 
            
                    **Example 1: To update the integration of a route**The following `update-route`example updates the integration of a specified route.`aws apigatewayv2 update-route \ --api-id``a1b2c3d4`\ --route-id`a1b2c3`\ --target`integrations/a1b2c6`Output: `{ "ApiKeyRequired": false, "AuthorizationType": "NONE", "RouteId": "a1b2c3", "RouteKey": "ANY /pets", "Target": "integrations/a1b2c6" }`**Example 2: To add an authorizer to a route**The following `update-route`example updates the specified route to use a JWT authorizer.`aws apigatewayv2 update-route \ --api-id``a1b2c3d4`\ --route-id`a1b2c3`\ --authorization-type`JWT`\ --authorizer-id`a1b2c5`\ --authorization-scopes`user.id``user.email`Output: `{ "ApiKeyRequired": false, "AuthorizationScopes": [ "user.id", "user.email" ], "AuthorizationType": "JWT", "AuthorizerId": "a1b2c5", "OperationName": "GET HTTP", "RequestParameters": {}, "RouteId": "a1b2c3", "RouteKey": "GET /pets", "Target": "integrations/a1b2c6" }`For more information, see [Controlling access to HTTP APIs with JWT authorizers](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-jwt-authorizer.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateRoute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-route.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-stage`.

- **AWS CLI**
- 
            
                    **To configure custom throttling**The following `update-stage`example configures custom throttling for the specified stage and route of an API.`aws apigatewayv2 update-stage \ --api-id``a1b2c3d4`\ --stage-name`dev`\ --route-settings '`{"GET /pets":{"ThrottlingBurstLimit":100,"ThrottlingRateLimit":2000}}`'Output: `{ "CreatedDate": "2020-04-05T16:21:16+00:00", "DefaultRouteSettings": { "DetailedMetricsEnabled": false }, "DeploymentId": "shktxb", "LastUpdatedDate": "2020-04-08T22:23:17+00:00", "RouteSettings": { "GET /pets": { "ThrottlingBurstLimit": 100, "ThrottlingRateLimit": 2000.0 } }, "StageName": "dev", "StageVariables": {}, "Tags": {} }`For more information, see [Protecting your HTTP API](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-protect.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-vpc-link`.

- **AWS CLI**
- 
            
                    **To update a VPC link**The following `update-vpc-link`example updates the name of a VPC link. After you've created a VPC link, you can't change its security groups or subnets.`aws apigatewayv2 update-vpc-link \ --vpc-link-id``abcd123`\ --name`MyUpdatedVpcLink`Output: `{ "CreatedDate": "2020-04-07T00:27:47Z", "Name": "MyUpdatedVpcLink", "SecurityGroupIds": [ "sg1234", "sg5678" ], "SubnetIds": [ "subnet-aaaa", "subnet-bbbb" ], "Tags": {}, "VpcLinkId": "abcd123", "VpcLinkStatus": "AVAILABLE", "VpcLinkStatusMessage": "VPC link is ready to route traffic", "VpcLinkVersion": "V2" }`For more information, see [Working with VPC links for HTTP APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateVpcLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigatewayv2/update-vpc-link.html)in*AWS CLI Command Reference*.
 
-