# API Gateway examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_api-gateway_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_api-gateway_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with API Gateway.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-api-key`.

- **AWS CLI**
- 
            
                    **To create an API key that is enabled for an existing API and Stage**Command: `aws apigateway create-api-key --name '``Dev API Key`' --description '`Used for development`' --enabled --stage-keys restApiId='a1b2c3d4e5',stageName='dev'- 
                    For API details, see [CreateApiKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-api-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-authorizer`.

- **AWS CLI**
- 
            
                    **Example 1: To create a token-based API Gateway Custom Authorizer for the API**The following `create-authorizer`example creates a token-based authorizer.`aws apigateway create-authorizer \ --rest-api-id``1234123412`\ --name '`First_Token_Custom_Authorizer`' \ --type`TOKEN`\ --authorizer-uri '`arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:customAuthFunction/invocations`' \ --identity-source '`method.request.header.Authorization`' \ --authorizer-result-ttl-in-seconds`300`Output: `{ "authType": "custom", "name": "First_Token_Custom_Authorizer", "authorizerUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:customAuthFunction/invocations", "authorizerResultTtlInSeconds": 300, "identitySource": "method.request.header.Authorization", "type": "TOKEN", "id": "z40xj0" }`**Example 2: To create a Cognito User Pools based API Gateway Custom Authorizer for the API**The following `create-authorizer`example creates a Cognito User Pools based API Gateway Custom Authorizer.`aws apigateway create-authorizer \ --rest-api-id``1234123412`\ --name '`First_Cognito_Custom_Authorizer`' \ --type`COGNITO_USER_POOLS`\ --provider-arns '`arn:aws:cognito-idp:us-east-1:123412341234:userpool/us-east-1_aWcZeQbuD`' \ --identity-source '`method.request.header.Authorization`'Output: `{ "authType": "cognito_user_pools", "identitySource": "method.request.header.Authorization", "name": "First_Cognito_Custom_Authorizer", "providerARNs": [ "arn:aws:cognito-idp:us-east-1:342398297714:userpool/us-east-1_qWbZzQhzE" ], "type": "COGNITO_USER_POOLS", "id": "5yid1t" }`**Example 3: To create a request-based API Gateway Custom Authorizer for the API**The following `create-authorizer`example creates a request-based authorizer.`aws apigateway create-authorizer \ --rest-api-id``1234123412`\ --name '`First_Request_Custom_Authorizer`' \ --type`REQUEST`\ --authorizer-uri '`arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:customAuthFunction/invocations`' \ --identity-source '`method.request.header.Authorization,context.accountId`' \ --authorizer-result-ttl-in-seconds`300`Output: `{ "id": "z40xj0", "name": "First_Request_Custom_Authorizer", "type": "REQUEST", "authType": "custom", "authorizerUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:customAuthFunction/invocations", "identitySource": "method.request.header.Authorization,context.accountId", "authorizerResultTtlInSeconds": 300 }`- 
                    For API details, see [CreateAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-base-path-mapping`.

- **AWS CLI**
- 
            
                    **To create the base path mapping for a custom domain name**Command: `aws apigateway create-base-path-mapping --domain-name``subdomain.domain.tld`--rest-api-id`1234123412`--stage`prod`--base-path`v1`- 
                    For API details, see [CreateBasePathMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-base-path-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-deployment`.

- **AWS CLI**
- 
            
                    **To deploy the configured resources for an API to a new Stage**Command: `aws apigateway create-deployment --rest-api-id``1234123412`--stage-name`dev`--stage-description '`Development Stage`' --description '`First deployment to the dev stage`'**To deploy the configured resources for an API to an existing stage**Command: `aws apigateway create-deployment --rest-api-id``1234123412`--stage-name`dev`--description '`Second deployment to the dev stage`'**To deploy the configured resources for an API to an existing stage with Stage Variables**aws apigateway create-deployment --rest-api-id 1234123412 --stage-name dev --description 'Third deployment to the dev stage' --variables key='value',otherKey='otherValue' - 
                    For API details, see [CreateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-domain-name-access-association`.

- **AWS CLI**
- 
            
                    **To create a domain name access association**The following `create-domain-name-access-association`example creates a domain name access association between a private custom domain name and VPC endpoint.`aws apigateway create-domain-name-access-association \ --domain-name-arn``arn:aws:apigateway:us-west-2:111122223333:/domainnames/my.private.domain.tld+abcd1234`\ --access-association-source`vpce-abcd1234efg`\ --access-association-source-type`VPCE`Output: `{ "domainNameAccessAssociationArn": "arn:aws:apigateway:us-west-2:012345678910:/domainnameaccessassociations/domainname/my.private.domain.tld/vpcesource/vpce-abcd1234efg "accessAssociationSource": "vpce-abcd1234efg", "accessAssociationSourceType": "VPCE", "domainNameArn" : "arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+abcd1234" }`For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateDomainNameAccessAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-domain-name-access-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-domain-name`.

- **AWS CLI**
- 
            
                    **Example 1: To create a public custom domain name**The following `create-domain-name`example creates a public custom domain name.`aws apigateway create-domain-name \ --domain-name '``my.domain.tld`' \ --certificate-name '`my.domain.tld cert`'\ --certificate-arn '`arn:aws:acm:us-east-1:012345678910:certificate/fb1b9770-a305-495d-aefb-27e5e101ff3`'Output: `{ "domainName": "my.domain.tld", "certificateName": "my.domain.tld cert", "certificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/fb1b9770-a305-495d-aefb-27e5e101ff3", "certificateUploadDate": "2024-10-08T11:29:49-07:00", "distributionDomainName": "abcd1234.cloudfront.net", "distributionHostedZoneId": "Z2FDTNDATAQYW2", "endpointConfiguration": { "types": [ "EDGE" ] }, "domainNameStatus": "AVAILABLE", "securityPolicy": "TLS_1_2" }`For more information, see [Custom domain name for public REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)in the*Amazon API Gateway Developer Guide*.**Example 2: To create a private custom domain name**The following `create-domain-name`example creates a private custom domain name.`aws apigateway create-domain-name \ --domain-name '``my.private.domain.tld`' \ --certificate-name '`my.domain.tld cert`' \ --certificate-arn '`arn:aws:acm:us-east-1:012345678910:certificate/fb1b9770-a305-495d-aefb-27e5e101ff3`' \ --endpoint-configuration '`{"types": ["PRIVATE"]}`' \ --security-policy '`TLS_1_2`' \ --policy`file://policy.json`Contents of `policy.json`:`{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": "*", "Action": "execute-api:Invoke", "Resource": [ "execute-api:/*" ] }, { "Effect": "Deny", "Principal": "*", "Action": "execute-api:Invoke", "Resource": [ "execute-api:/*" ], "Condition" : { "StringNotEquals": { "aws:SourceVpce": "vpce-abcd1234efg" } } } ] }`Output: `{ "domainName": "my.private.domain.tld", "domainNameId": "abcd1234", "domainNameArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234", "certificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/fb1b9770-a305-495d-aefb-27e5e101ff3", "certificateUploadDate": "2024-09-10T10:31:20-07:00", "endpointConfiguration": { "types": [ "PRIVATE" ] }, "domainNameStatus": "AVAILABLE", "securityPolicy": "TLS_1_2", "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"execute-api:Invoke\",\"Resource\":\"arn:aws:execute-api:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234\"},{\"Effect\":\"Deny\",\"Principal\":\"*\",\"Action\":\"execute-api:Invoke\",\"Resource\":\"arn:aws:execute-api:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234\",\"Condition\":{\"StringNotEquals\":{\"aws:SourceVpc\":\"vpc-1a2b3c4d\"}}}]}" }`For more information, see [Custom domain name for public REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [CreateDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-model`.

- **AWS CLI**
- 
            
                    **To create a model for an API**Command: `aws apigateway create-model --rest-api-id``1234123412`--name '`firstModel`' --description '`The First Model`' --content-type '`application/json`' --schema '`{ "$schema": "http://json-schema.org/draft-04/schema#", "title": "firstModel", "type": "object", "properties": { "firstProperty" : { "type": "object", "properties": { "key": { "type": "string" } } } } }`'Output: `{ "contentType": "application/json", "description": "The First Model", "name": "firstModel", "id": "2rzg0l", "schema": "{ \"$schema\": \"http://json-schema.org/draft-04/schema#\", \"title\": \"firstModel\", \"type\": \"object\", \"properties\": { \"firstProperty\" : { \"type\": \"object\", \"properties\": { \"key\": { \"type\": \"string\" } } } } }" }`- 
                    For API details, see [CreateModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-resource`.

- **AWS CLI**
- 
            
                    **To create a resource in an API**Command: `aws apigateway create-resource --rest-api-id``1234123412`--parent-id`a1b2c3`--path-part '`new-resource`'- 
                    For API details, see [CreateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-rest-api`.

- **AWS CLI**
- 
            
                    **To create an API**Command: `aws apigateway create-rest-api --name '``My First API`' --description '`This is my first API`'**To create a duplicate API from an existing API**Command: `aws apigateway create-rest-api --name '``Copy of My First API`' --description '`This is a copy of my first API`' --clone-from`1234123412`- 
                    For API details, see [CreateRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-rest-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-stage`.

- **AWS CLI**
- 
            
                    **To create a stage in an API which will contain an existing deployment**Command: `aws apigateway create-stage --rest-api-id``1234123412`--stage-name '`dev`' --description '`Development stage`' --deployment-id`a1b2c3`**To create a stage in an API which will contain an existing deployment and custom Stage Variables**Command: `aws apigateway create-stage --rest-api-id``1234123412`--stage-name '`dev`' --description '`Development stage`' --deployment-id`a1b2c3`--variables key='value',otherKey='otherValue'- 
                    For API details, see [CreateStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-usage-plan-key`.

- **AWS CLI**
- 
            
                    **Associate an existing API key with a Usage Plan**Command: `aws apigateway create-usage-plan-key --usage-plan-id``a1b2c3`--key-type`"API_KEY"`--key-id`4vq3yryqm5`- 
                    For API details, see [CreateUsagePlanKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-usage-plan`.

- **AWS CLI**
- 
            
                    **To create a usage plan with throttle and quota limits that resets at the beginning of the month**Command: `aws apigateway create-usage-plan --name``"New Usage Plan"`--description`"A new usage plan"`--throttle`burstLimit=10,rateLimit=5`--quota`limit=500,offset=0,period=MONTH`- 
                    For API details, see [CreateUsagePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-api-key`.

- **AWS CLI**
- 
            
                    **To delete an API key**Command: `aws apigateway delete-api-key --api-key``8bklk8bl1k3sB38D9B3l0enyWT8c09B30lkq0blk`- 
                    For API details, see [DeleteApiKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-api-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-authorizer`.

- **AWS CLI**
- 
            
                    **To delete a Custom Authorizer in an API**Command: `aws apigateway delete-authorizer --rest-api-id``1234123412`--authorizer-id`7gkfbo`- 
                    For API details, see [DeleteAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-base-path-mapping`.

- **AWS CLI**
- 
            
                    **To delete a base path mapping for a custom domain name**Command: `aws apigateway delete-base-path-mapping --domain-name '``api.domain.tld`' --base-path '`dev`'- 
                    For API details, see [DeleteBasePathMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-base-path-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-client-certificate`.

- **AWS CLI**
- 
            
                    **To delete a client certificate**Command: `aws apigateway delete-client-certificate --client-certificate-id``a1b2c3`- 
                    For API details, see [DeleteClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-client-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-deployment`.

- **AWS CLI**
- 
            
                    **To delete a deployment in an API**Command: `aws apigateway delete-deployment --rest-api-id``1234123412`--deployment-id`a1b2c3`- 
                    For API details, see [DeleteDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain-name-access-association`.

- **AWS CLI**
- 
            
                    **To delete a domain name access association**The following `delete-domain-name-access-association`example deletes a domain name access association between a private custom domain name and VPC endpoint.`aws apigateway delete-domain-name-access-association \ --domain-name-access-association-arn``arn:aws:apigateway:us-west-2:012345678910:/domainnameaccessassociations/domainname/my.private.domain.tld/vpcesource/vpce-abcd1234efg`This command produces no output. For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [DeleteDomainNameAccessAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-domain-name-access-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain-name`.

- **AWS CLI**
- 
            
                    **To delete a custom domain name**Command: `aws apigateway delete-domain-name --domain-name '``api.domain.tld`'- 
                    For API details, see [DeleteDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-integration-response`.

- **AWS CLI**
- 
            
                    **To delete an integration response for a given resource, method, and status code in an API**Command: `aws apigateway delete-integration-response --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--status-code`200`- 
                    For API details, see [DeleteIntegrationResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-integration-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-integration`.

- **AWS CLI**
- 
            
                    **To delete an integration for a given resource and method in an API**Command: `aws apigateway delete-integration --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`- 
                    For API details, see [DeleteIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-method-response`.

- **AWS CLI**
- 
            
                    **To delete a method response for the given resource, method, and status code in an API**Command: `aws apigateway delete-method-response --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--status-code`200`- 
                    For API details, see [DeleteMethodResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-method-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-method`.

- **AWS CLI**
- 
            
                    **To delete a method for the given resource in an API**Command: `aws apigateway delete-method --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`- 
                    For API details, see [DeleteMethod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-method.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-model`.

- **AWS CLI**
- 
            
                    **To delete a model in the given API**Command: `aws apigateway delete-model --rest-api-id``1234123412`--model-name '`customModel`'- 
                    For API details, see [DeleteModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource`.

- **AWS CLI**
- 
            
                    **To delete a resource in an API**Command: `aws apigateway delete-resource --rest-api-id``1234123412`--resource-id`a1b2c3`- 
                    For API details, see [DeleteResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-rest-api`.

- **AWS CLI**
- 
            
                    **To delete an API**Command: `aws apigateway delete-rest-api --rest-api-id``1234123412`- 
                    For API details, see [DeleteRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-rest-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-stage`.

- **AWS CLI**
- 
            
                    **To delete a stage in an API**Command: `aws apigateway delete-stage --rest-api-id``1234123412`--stage-name '`dev`'- 
                    For API details, see [DeleteStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-usage-plan-key`.

- **AWS CLI**
- 
            
                    **To remove an API key from a Usage Plan**Command: `aws apigateway delete-usage-plan-key --usage-plan-id``a1b2c3`--key-id`1NbjQzMReAkeEQPNAW8r3dXsU2rDD7fc7f2Sipnu`- 
                    For API details, see [DeleteUsagePlanKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-usage-plan-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-usage-plan`.

- **AWS CLI**
- 
            
                    **To delete a Usage Plan**Command: `aws apigateway delete-usage-plan --usage-plan-id``a1b2c3`- 
                    For API details, see [DeleteUsagePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/delete-usage-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `flush-stage-authorizers-cache`.

- **AWS CLI**
- 
            
                    **To flush all authorizer cache entries on a stage**Command: `aws apigateway flush-stage-authorizers-cache --rest-api-id``1234123412`--stage-name`dev`- 
                    For API details, see [FlushStageAuthorizersCache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/flush-stage-authorizers-cache.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `flush-stage-cache`.

- **AWS CLI**
- 
            
                    **To flush the cache for an API's stage**The following `flush-stage-cache`example flushes the cache of a stage.`aws apigateway flush-stage-cache \ --rest-api-id``1234123412`\ --stage-name`dev`This command produces no output. For more information, see [Flush the API stage cache in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html#flush-api-caching)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [FlushStageCache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/flush-stage-cache.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `generate-client-certificate`.

- **AWS CLI**
- 
            
                    **To create a Client-Side SSL Certificate**Command: `aws apigateway generate-client-certificate --description '``My First Client Certificate`'- 
                    For API details, see [GenerateClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/generate-client-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-account`.

- **AWS CLI**
- 
            
                    **To get API Gateway account settings**Command: `aws apigateway get-account`Output: `{ "cloudwatchRoleArn": "arn:aws:iam::123412341234:role/APIGatewayToCloudWatchLogsRole", "throttleSettings": { "rateLimit": 500.0, "burstLimit": 1000 } }`- 
                    For API details, see [GetAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-api-key`.

- **AWS CLI**
- 
            
                    **To get the information about a specific API key**Command: `aws apigateway get-api-key --api-key``8bklk8bl1k3sB38D9B3l0enyWT8c09B30lkq0blk`Output: `{ "description": "My first key", "enabled": true, "stageKeys": [ "a1b2c3d4e5/dev", "e5d4c3b2a1/dev" ], "lastUpdatedDate": 1456184515, "createdDate": 1456184452, "id": "8bklk8bl1k3sB38D9B3l0enyWT8c09B30lkq0blk", "name": "My key" }`- 
                    For API details, see [GetApiKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-api-keys`.

- **AWS CLI**
- 
            
                    **To get the list of API keys**Command: `aws apigateway get-api-keys`Output: `{ "items": [ { "description": "My first key", "enabled": true, "stageKeys": [ "a1b2c3d4e5/dev", "e5d4c3b2a1/dev" ], "lastUpdatedDate": 1456184515, "createdDate": 1456184452, "id": "8bklk8bl1k3sB38D9B3l0enyWT8c09B30lkq0blk", "name": "My key" } ] }`- 
                    For API details, see [GetApiKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-api-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-authorizer`.

- **AWS CLI**
- 
            
                    **To get the API Gateway per-API Authorizer settings**Command: `aws apigateway get-authorizer --rest-api-id``1234123412`--authorizer-id`gfi4n3`Output: `{ "authorizerResultTtlInSeconds": 300, "name": "MyAuthorizer", "type": "TOKEN", "identitySource": "method.request.header.Authorization", "authorizerUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:authorizer_function/invocations", "id": "gfi4n3" }`- 
                    For API details, see [GetAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-authorizers`.

- **AWS CLI**
- 
            
                    **To get the list of authorizers for a REST API**Command: `aws apigateway get-authorizers --rest-api-id``1234123412`Output: `{ "items": [ { "name": "MyAuthorizer", "authorizerUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:My_Authorizer_Function/invocations", "authorizerResultTtlInSeconds": 300, "identitySource": "method.request.header.Authorization", "type": "TOKEN", "id": "gfi4n3" } ] }`- 
                    For API details, see [GetAuthorizers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-authorizers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-base-path-mapping`.

- **AWS CLI**
- 
            
                    **To get the base path mapping for a custom domain name**Command: `aws apigateway get-base-path-mapping --domain-name``subdomain.domain.tld`--base-path`v1`Output: `{ "basePath": "v1", "restApiId": "1234w4321e", "stage": "api" }`- 
                    For API details, see [GetBasePathMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-base-path-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-base-path-mappings`.

- **AWS CLI**
- 
            
                    **To get the base path mappings for a custom domain name**Command: `aws apigateway get-base-path-mappings --domain-name``subdomain.domain.tld`Output: `{ "items": [ { "basePath": "(none)", "restApiId": "1234w4321e", "stage": "dev" }, { "basePath": "v1", "restApiId": "1234w4321e", "stage": "api" } ] }`- 
                    For API details, see [GetBasePathMappings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-base-path-mappings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-client-certificate`.

- **AWS CLI**
- 
            
                    **To get a client certificate**Command: `aws apigateway get-client-certificate --client-certificate-id``a1b2c3`- 
                    For API details, see [GetClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-client-certificates`.

- **AWS CLI**
- 
            
                    **To get a list of client certificates**Command: `aws apigateway get-client-certificates`Output: `{ "items": [ { "pemEncodedCertificate": "-----BEGIN CERTIFICATE----- <certificate content> -----END CERTIFICATE-----", "clientCertificateId": "a1b2c3", "expirationDate": 1483556561, "description": "My Client Certificate", "createdDate": 1452020561 } ] }`- 
                    For API details, see [GetClientCertificates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-client-certificates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployment`.

- **AWS CLI**
- 
            
                    **To get information about a deployment**Command: `aws apigateway get-deployment --rest-api-id``1234123412`--deployment-id`ztt4m2`Output: `{ "description": "myDeployment", "id": "ztt4m2", "createdDate": 1455218022 }`- 
                    For API details, see [GetDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-deployments`.

- **AWS CLI**
- 
            
                    **To get a list of deployments for a REST API**Command: `aws apigateway get-deployments --rest-api-id``1234123412`Output: `{ "items": [ { "createdDate": 1453797217, "id": "0a2b4c", "description": "Deployed my API for the first time" } ] }`- 
                    For API details, see [GetDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-deployments.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-name-access-associations`.

- **AWS CLI**
- 
            
                    **Example 1: To list all domain name access associations**The following `get-domain-name-access-associations`example lists all domain name access associations.`aws apigateway get-domain-name-access-associations`Output: `{ "items": [ { "domainNameAccessAssociationArn": "arn:aws:apigateway:us-west-2:012345678910:/domainnameaccessassociations/domainname/my.private.domain.tld/vpcesource/vpce-abcd1234efg "accessAssociationSource": "vpce-abcd1234efg", "accessAssociationSourceType": "VPCE", "domainNameArn" : "arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+abcd1234" } ] }`For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.**Example 2: To list all domain name access associations owned by this AWS account**The following `get-domain-name-access-associations`example lists all the domain name access associations owned by the current AWS account.`aws apigateway get-domain-name-access-associations \ --resource-owner``SELF`Output: `{ "items": [ { "domainNameAccessAssociationArn": "arn:aws:apigateway:us-west-2:012345678910:/domainnameaccessassociations/domainname/my.private.domain.tld/vpcesource/vpce-abcd1234efg "accessAssociationSource": "vpce-abcd1234efg", "accessAssociationSourceType": "VPCE", "domainNameArn" : "arn:aws:apigateway:us-west-2:111122223333:/domainnames/private.example.com+abcd1234" } ] }`For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetDomainNameAccessAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-name-access-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-name`.

- **AWS CLI**
- 
            
                    **Example 1: To get information about a public custom domain name**The following `get-domain-name`example gets information about a public custom domain name.`aws apigateway get-domain-name \ --domain-name``api.domain.tld`Output: `{ "domainName": "api.domain.tld", "distributionDomainName": "d1a2f3a4c5o6d.cloudfront.net", "certificateName": "uploadedCertificate", "certificateUploadDate": 1462565487 }`For more information, see [Custom domain name for public REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)in the*Amazon API Gateway Developer Guide*.**Example 2: To get information about a private custom domain name**The following `get-domain-name`example gets information about a private custom domain name.`aws apigateway get-domain-name \ --domain-name``api.private.domain.tld`\ --domain-name-id`abcd1234`Output: `{ "domainName": "my.private.domain.tld", "domainNameId": "abcd1234", "domainNameArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234", "certificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/fb1b9770-a305-495d-aefb-27e5e101ff3", "certificateUploadDate": "2024-09-10T10:31:20-07:00", "endpointConfiguration": { "types": [ "PRIVATE" ] }, "domainNameStatus": "AVAILABLE", "securityPolicy": "TLS_1_2", "policy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"execute-api:Invoke\",\"Resource\":\"arn:aws:execute-api:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234\"},{\"Effect\":\"Deny\",\"Principal\":\"*\",\"Action\":\"execute-api:Invoke\",\"Resource\":\"arn:aws:execute-api:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234\",\"Condition\":{\"StringNotEquals\":{\"aws:SourceVpc\":\"vpc-1a2b3c4d\"}}}]}" }`For more information, see [Custom domain name for public REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-names`.

- **AWS CLI**
- 
            
                    **Example 1: To get a list of custom domain names**The following `get-domain-names`command gets a list of domain names.`aws apigateway get-domain-names`Output: `{ "items": [ { "distributionDomainName": "d9511k3l09bkd.cloudfront.net", "certificateUploadDate": 1452812505, "certificateName": "my_custom_domain-certificate", "domainName": "subdomain.domain.tld" } ] }`For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.**Example 2: To get a list of custom domain names owned by this AWS account**The following `get-domain-names`command gets a list of domain names owned by this AWS account.`aws apigateway get-domain-names \ --resource-owner``SELF`Output: `{ "items": [ { "domainName": "my.domain.tld", "domainNameArn": "arn:aws:apigateway:us-east-1::/domainnames/my.private.domain.tld", "certificateUploadDate": "2024-08-15T17:02:55-07:00", "regionalDomainName": "d-abcd1234.execute-api.us-east-1.amazonaws.com", "regionalHostedZoneId": "Z1UJRXOUMOOFQ8", "regionalCertificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/fb1b9770-a305-495d-aefb-27e5e101ff3", "endpointConfiguration": { "types": [ "REGIONAL" ] }, "domainNameStatus": "AVAILABLE", "securityPolicy": "TLS_1_2" }, { "domainName": "my.private.domain.tld", "domainNameId": "abcd1234", "domainNameArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234", "certificateArn": "arn:aws:acm:us-east-1:012345678910:certificate/fb1b9770-a305-495d-aefb-27e5e101ff3", "certificateUploadDate": "2024-11-26T11:44:40-08:00", "endpointConfiguration": { "types": [ "PRIVATE" ] }, "domainNameStatus": "AVAILABLE", "securityPolicy": "TLS_1_2" } ] }`For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.**Example 3: To get a list of custom domain names owned by other AWS accounts that you can create a domain name access association with.**The following `get-domain-names`command gets a list of domain names owned by other AWS accounts that you have access to create a domain name access association with.`aws apigateway get-domain-names \ --resource-owner``OTHER_ACCOUNTS`Output: `{ "items": [ { "domainName": "my.private.domain.tld", "domainNameId": "abcd1234", "domainNameArn": "arn:aws:apigateway:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234" } ] }`For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [GetDomainNames](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-domain-names.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-export`.

- **AWS CLI**
- 
            
                    **To get the JSON Swagger template for a stage**Command: `aws apigateway get-export --rest-api-id``a1b2c3d4e5`--stage-name`dev`--export-type`swagger``/path/to/filename.json`**To get the JSON Swagger template + API Gateway Extensions for a stage**Command: `aws apigateway get-export --parameters extensions='integrations' --rest-api-id``a1b2c3d4e5`--stage-name`dev`--export-type`swagger``/path/to/filename.json`**To get the JSON Swagger template + Postman Extensions for a stage**Command: `aws apigateway get-export --parameters extensions='postman' --rest-api-id``a1b2c3d4e5`--stage-name`dev`--export-type`swagger``/path/to/filename.json`- 
                    For API details, see [GetExport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-export.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-integration-response`.

- **AWS CLI**
- 
            
                    **To get the integration response configuration for a HTTP method defined under a REST API's resource**Command: `aws apigateway get-integration-response --rest-api-id``1234123412`--resource-id`y9h6rt`--http-method`GET`--status-code`200`Output: `{ "statusCode": "200", "responseTemplates": { "application/json": null } }`- 
                    For API details, see [GetIntegrationResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-integration-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-integration`.

- **AWS CLI**
- 
            
                    **To get the integration configuration for a HTTP method defined under a REST API's resource**Command: `aws apigateway get-integration --rest-api-id``1234123412`--resource-id`y9h6rt`--http-method`GET`Output: `{ "httpMethod": "POST", "integrationResponses": { "200": { "responseTemplates": { "application/json": null }, "statusCode": "200" } }, "cacheKeyParameters": [], "type": "AWS", "uri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:My_Function/invocations", "cacheNamespace": "y9h6rt" }`- 
                    For API details, see [GetIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-method-response`.

- **AWS CLI**
- 
            
                    **To get the method response resource configuration for a HTTP method defined under a REST API's resource**Command: `aws apigateway get-method-response --rest-api-id``1234123412`--resource-id`y9h6rt`--http-method`GET`--status-code`200`Output: `{ "responseModels": { "application/json": "Empty" }, "statusCode": "200" }`- 
                    For API details, see [GetMethodResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-method-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-method`.

- **AWS CLI**
- 
            
                    **To get the method resource configuration for a HTTP method defined under a REST API's resource**Command: `aws apigateway get-method --rest-api-id``1234123412`--resource-id`y9h6rt`--http-method`GET`Output: `{ "apiKeyRequired": false, "httpMethod": "GET", "methodIntegration": { "integrationResponses": { "200": { "responseTemplates": { "application/json": null }, "statusCode": "200" } }, "cacheKeyParameters": [], "uri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:My_Function/invocations", "httpMethod": "POST", "cacheNamespace": "y9h6rt", "type": "AWS" }, "requestParameters": {}, "methodResponses": { "200": { "responseModels": { "application/json": "Empty" }, "statusCode": "200" } }, "authorizationType": "NONE" }`- 
                    For API details, see [GetMethod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-method.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-model-template`.

- **AWS CLI**
- 
            
                    **To get the mapping template for a model defined under a REST API**Command: `aws apigateway get-model-template --rest-api-id``1234123412`--model-name`Empty`Output: `{ "value": "#set($inputRoot = $input.path('$'))\n{ }" }`- 
                    For API details, see [GetModelTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-model-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-model`.

- **AWS CLI**
- 
            
                    **To get the configuration for a model defined under a REST API**Command: `aws apigateway get-model --rest-api-id``1234123412`--model-name`Empty`Output: `{ "contentType": "application/json", "description": "This is a default empty schema model", "name": "Empty", "id": "etd5w5", "schema": "{\n \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n \"title\" : \"Empty Schema\",\n \"type\" : \"object\"\n}" }`- 
                    For API details, see [GetModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-models`.

- **AWS CLI**
- 
            
                    **To get a list of models for a REST API**Command: `aws apigateway get-models --rest-api-id``1234123412`Output: `{ "items": [ { "description": "This is a default error schema model", "schema": "{\n \"$schema\" : \"http://json-schema.org/draft-04/schema#\",\n \"title\" : \"Error Schema\",\n \"type\" : \"object\",\n \"properties\" : {\n \"message\" : { \"type\" : \"string\" }\n }\n}", "contentType": "application/json", "id": "7tpbze", "name": "Error" }, { "description": "This is a default empty schema model", "schema": "{\n \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n \"title\" : \"Empty Schema\",\n \"type\" : \"object\"\n}", "contentType": "application/json", "id": "etd5w5", "name": "Empty" } ] }`- 
                    For API details, see [GetModels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-models.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resource`.

- **AWS CLI**
- 
            
                    **To get information about a resource**Command: `aws apigateway get-resource --rest-api-id``1234123412`--resource-id`zwo0y3`Output: `{ "path": "/path", "pathPart": "path", "id": "zwo0y3", "parentId": "uyokt6ij2g" }`- 
                    For API details, see [GetResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-resources`.

- **AWS CLI**
- 
            
                    **To get a list of resources for a REST API**Command: `aws apigateway get-resources --rest-api-id``1234123412`Output: `{ "items": [ { "path": "/resource/subresource", "resourceMethods": { "POST": {} }, "id": "024ace", "pathPart": "subresource", "parentId": "ai5b02" } ] }`- 
                    For API details, see [GetResources](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-resources.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-rest-api`.

- **AWS CLI**
- 
            
                    **To get information about an API**Command: `aws apigateway get-rest-api --rest-api-id``1234123412`Output: `{ "name": "myAPI", "id": "o1y243m4f5", "createdDate": 1453416433 }`- 
                    For API details, see [GetRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-rest-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-rest-apis`.

- **AWS CLI**
- 
            
                    **To get a list of REST APIs**Command: `aws apigateway get-rest-apis`Output: `{ "items": [ { "createdDate": 1438884790, "id": "12s44z21rb", "name": "My First API" } ] }`- 
                    For API details, see [GetRestApis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-rest-apis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sdk`.

- **AWS CLI**
- 
            
                    **To get the Android SDK for a REST API stage**Command: `aws apigateway get-sdk --rest-api-id``1234123412`--stage-name`dev`--sdk-type`android`--parameters groupId='com.mycompany',invokerPackage='com.mycompany.clientsdk',artifactId='Mycompany-client',artifactVersion='1.0.0'`/path/to/android_sdk.zip`Output: `{ "contentType": "application/octet-stream", "contentDisposition": "attachment; filename=\"android_2016-02-22_23-52Z.zip\"" }`**To get the IOS SDK for a REST API stage**Command: `aws apigateway get-sdk --rest-api-id``1234123412`--stage-name`dev`--sdk-type`objectivec`--parameters classPrefix='myprefix'`/path/to/iOS_sdk.zip`Output: `{ "contentType": "application/octet-stream", "contentDisposition": "attachment; filename=\"objectivec_2016-02-22_23-52Z.zip\"" }`**To get the Javascript SDK for a REST API stage**Command: `aws apigateway get-sdk --rest-api-id``1234123412`--stage-name`dev`--sdk-type`javascript``/path/to/javascript_sdk.zip`Output: `{ "contentType": "application/octet-stream", "contentDisposition": "attachment; filename=\"javascript_2016-02-22_23-52Z.zip\"" }`- 
                    For API details, see [GetSdk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-sdk.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stage`.

- **AWS CLI**
- 
            
                    **To get information about an API's stage**Command: `aws apigateway get-stage --rest-api-id``1234123412`--stage-name`dev`Output: `{ "stageName": "dev", "cacheClusterSize": "0.5", "cacheClusterEnabled": false, "cacheClusterStatus": "NOT_AVAILABLE", "deploymentId": "rbh1fj", "lastUpdatedDate": 1466802961, "createdDate": 1460682074, "methodSettings": { "*/*": { "cacheTtlInSeconds": 300, "loggingLevel": "INFO", "dataTraceEnabled": false, "metricsEnabled": true, "unauthorizedCacheControlHeaderStrategy": "SUCCEED_WITH_RESPONSE_HEADER", "throttlingRateLimit": 500.0, "cacheDataEncrypted": false, "cachingEnabled": false, "throttlingBurstLimit": 1000, "requireAuthorizationForCacheControl": true }, "~1resource/GET": { "cacheTtlInSeconds": 300, "loggingLevel": "INFO", "dataTraceEnabled": false, "metricsEnabled": true, "unauthorizedCacheControlHeaderStrategy": "SUCCEED_WITH_RESPONSE_HEADER", "throttlingRateLimit": 500.0, "cacheDataEncrypted": false, "cachingEnabled": false, "throttlingBurstLimit": 1000, "requireAuthorizationForCacheControl": true } } }`- 
                    For API details, see [GetStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-stages`.

- **AWS CLI**
- 
            
                    **To get the list of stages for a REST API**Command: `aws apigateway get-stages --rest-api-id``1234123412`Output: `{ "item": [ { "stageName": "dev", "cacheClusterSize": "0.5", "cacheClusterEnabled": true, "cacheClusterStatus": "AVAILABLE", "deploymentId": "123h64", "lastUpdatedDate": 1456185138, "createdDate": 1453589092, "methodSettings": { "~1resource~1subresource/POST": { "cacheTtlInSeconds": 300, "loggingLevel": "INFO", "dataTraceEnabled": true, "metricsEnabled": true, "throttlingRateLimit": 500.0, "cacheDataEncrypted": false, "cachingEnabled": false, "throttlingBurstLimit": 1000 } } } ] }`- 
                    For API details, see [GetStages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-stages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-usage-plan-key`.

- **AWS CLI**
- 
            
                    **To get the details of an API key associated with a Usage Plan**Command: `aws apigateway get-usage-plan-key --usage-plan-id``a1b2c3`--key-id`1NbjQzMReAkeEQPNAW8r3dXsU2rDD7fc7f2Sipnu`- 
                    For API details, see [GetUsagePlanKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-usage-plan-keys`.

- **AWS CLI**
- 
            
                    **To get the list of API keys associated with a Usage Plan**Command: `aws apigateway get-usage-plan-keys --usage-plan-id``a1b2c3`- 
                    For API details, see [GetUsagePlanKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-usage-plan`.

- **AWS CLI**
- 
            
                    **To get the details of a Usage Plan**Command: `aws apigateway get-usage-plan --usage-plan-id``a1b2c3`- 
                    For API details, see [GetUsagePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-usage-plans`.

- **AWS CLI**
- 
            
                    **To get the details of all Usage Plans**Command: `aws apigateway get-usage-plans`- 
                    For API details, see [GetUsagePlans](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plans.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-usage`.

- **AWS CLI**
- 
            
                    **To get the usage details for a Usage Plan**Command: `aws apigateway get-usage --usage-plan-id``a1b2c3`--start-date`"2016-08-16"`--end-date`"2016-08-17"`- 
                    For API details, see [GetUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-rest-api`.

- **AWS CLI**
- 
            
                    **To import a Swagger template and create an API**Command: `aws apigateway import-rest-api --body '``file:///path/to/API_Swagger_template.json`'- 
                    For API details, see [ImportRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/import-rest-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-integration-response`.

- **AWS CLI**
- 
            
                    **To create an integration response as the default response with a mapping template defined**Command: `aws apigateway put-integration-response --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--status-code`200`--selection-pattern "" --response-templates '`{"application/json": "{\"json\": \"template\"}"}`'**To create an integration response with a regex of 400 and a statically defined header value**Command: `aws apigateway put-integration-response --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--status-code`400`--selection-pattern`400`--response-parameters '{"method.response.header.custom-header": "'"'"'custom-value'"'"'"}'- 
                    For API details, see [PutIntegrationResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-integration`.

- **AWS CLI**
- 
            
                    **To create a MOCK integration request**Command: `aws apigateway put-integration --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--type`MOCK`--request-templates '`{ "application/json": "{\"statusCode\": 200}" }`'**To create a HTTP integration request**Command: `aws apigateway put-integration --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--type`HTTP`--integration-http-method`GET`--uri '`https://domain.tld/path`'**To create an AWS integration request with a Lambda Function endpoint**Command: `aws apigateway put-integration --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--type`AWS`--integration-http-method`POST`--uri '`arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:function_name/invocations`'- 
                    For API details, see [PutIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-method-response`.

- **AWS CLI**
- 
            
                    **To create a method response under the specified status code with a custom method response header**Command: `aws apigateway put-method-response --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--status-code`400`--response-parameters`"method.response.header.custom-header=false"`- 
                    For API details, see [PutMethodResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-method`.

- **AWS CLI**
- 
            
                    **To create a method for a resource in an API with no authorization, no API key, and a custom method request header**Command: `aws apigateway put-method --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`PUT`--authorization-type`"NONE"`--no-api-key-required --request-parameters`"method.request.header.custom-header=false"`- 
                    For API details, see [PutMethod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-method.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-rest-api`.

- **AWS CLI**
- 
            
                    **To overwrite an existing API using a Swagger template**Command: `aws apigateway put-rest-api --rest-api-id``1234123412`--mode`overwrite`--body '`fileb:///path/to/API_Swagger_template.json`'**To merge a Swagger template into an existing API**Command: `aws apigateway put-rest-api --rest-api-id``1234123412`--mode`merge`--body '`fileb:///path/to/API_Swagger_template.json`'- 
                    For API details, see [PutRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/put-rest-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `reject-domain-name-access-association`.

- **AWS CLI**
- 
            
                    **To reject a domain name access association**The following `reject-domain-name-access-association`example rejects a domain name access association between a private custom domain name and VPC endpoint.`aws apigateway reject-domain-name-access-association \ --domain-name-access-association-arn``arn:aws:apigateway:us-west-2:012345678910:/domainnameaccessassociations/domainname/my.private.domain.tld/vpcesource/vpce-abcd1234efg`\ --domain-name-arn`arn:aws:apigateway:us-east-1:012345678910:/domainnames/my.private.domain.tld+abcd1234`This command produces no output. For more information, see [Custom domain names for private APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-private-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [RejectDomainNameAccessAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/reject-domain-name-access-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-invoke-authorizer`.

- **AWS CLI**
- 
            
                    **To test invoke a request to a Custom Authorizer including the required header and value**Command: `aws apigateway test-invoke-authorizer --rest-api-id``1234123412`--authorizer-id`5yid1t`--headers Authorization='Value'- 
                    For API details, see [TestInvokeAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/test-invoke-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-invoke-method`.

- **AWS CLI**
- 
            
                    **To test invoke the root resource in an API by making a GET request**Command: `aws apigateway test-invoke-method --rest-api-id``1234123412`--resource-id`avl5sg8fw8`--http-method`GET`--path-with-query-string '`/`'**To test invoke a sub-resource in an API by making a GET request with a path parameter value specified**Command: `aws apigateway test-invoke-method --rest-api-id``1234123412`--resource-id`3gapai`--http-method`GET`--path-with-query-string '`/pets/1`'- 
                    For API details, see [TestInvokeMethod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/test-invoke-method.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-account`.

- **AWS CLI**
- 
            
                    **To change the IAM Role ARN for logging to CloudWatch Logs**Command: `aws apigateway update-account --patch-operations op='replace',path='/cloudwatchRoleArn',value='arn:aws:iam::123412341234:role/APIGatewayToCloudWatchLogs'`Output: `{ "cloudwatchRoleArn": "arn:aws:iam::123412341234:role/APIGatewayToCloudWatchLogs", "throttleSettings": { "rateLimit": 1000.0, "burstLimit": 2000 } }`- 
                    For API details, see [UpdateAccount](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-account.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-api-key`.

- **AWS CLI**
- 
            
                    **To change the name for an API Key**Command: `aws apigateway update-api-key --api-key``sNvjQDMReA1eEQPNAW8r37XsU2rDD7fc7m2SiMnu`--patch-operations op='replace',path='/name',value='newName'Output: `{ "description": "currentDescription", "enabled": true, "stageKeys": [ "41t2j324r5/dev" ], "lastUpdatedDate": 1470086052, "createdDate": 1445460347, "id": "sNvjQDMReA1vEQPNzW8r3dXsU2rrD7fcjm2SiMnu", "name": "newName" }`**To disable the API Key**Command: `aws apigateway update-api-key --api-key``sNvjQDMReA1eEQPNAW8r37XsU2rDD7fc7m2SiMnu`--patch-operations op='replace',path='/enabled',value='false'Output: `{ "description": "currentDescription", "enabled": false, "stageKeys": [ "41t2j324r5/dev" ], "lastUpdatedDate": 1470086052, "createdDate": 1445460347, "id": "sNvjQDMReA1vEQPNzW8r3dXsU2rrD7fcjm2SiMnu", "name": "newName" }`- 
                    For API details, see [UpdateApiKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-api-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-authorizer`.

- **AWS CLI**
- 
            
                    **To change the name of the Custom Authorizer**Command: `aws apigateway update-authorizer --rest-api-id``1234123412`--authorizer-id`gfi4n3`--patch-operations op='replace',path='/name',value='testAuthorizer'Output: `{ "authType": "custom", "name": "testAuthorizer", "authorizerUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:customAuthorizer/invocations", "authorizerResultTtlInSeconds": 300, "identitySource": "method.request.header.Authorization", "type": "TOKEN", "id": "gfi4n3" }`**To change the Lambda Function that is invoked by the Custom Authorizer**Command: `aws apigateway update-authorizer --rest-api-id``1234123412`--authorizer-id`gfi4n3`--patch-operations op='replace',path='/authorizerUri',value='arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:newAuthorizer/invocations'Output: `{ "authType": "custom", "name": "testAuthorizer", "authorizerUri": "arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:123412341234:function:newAuthorizer/invocations", "authorizerResultTtlInSeconds": 300, "identitySource": "method.request.header.Authorization", "type": "TOKEN", "id": "gfi4n3" }`- 
                    For API details, see [UpdateAuthorizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-authorizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-base-path-mapping`.

- **AWS CLI**
- 
            
                    **To change the base path for a custom domain name**Command: `aws apigateway update-base-path-mapping --domain-name``api.domain.tld`--base-path`prod`--patch-operations op='replace',path='/basePath',value='v1'Output: `{ "basePath": "v1", "restApiId": "1234123412", "stage": "api" }`- 
                    For API details, see [UpdateBasePathMapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-base-path-mapping.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-client-certificate`.

- **AWS CLI**
- 
            
                    **To update the description of a client certificate**Command: `aws apigateway update-client-certificate --client-certificate-id``a1b2c3`--patch-operations op='replace',path='/description',value='My new description'- 
                    For API details, see [UpdateClientCertificate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-client-certificate.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-deployment`.

- **AWS CLI**
- 
            
                    **To change the description of a deployment**Command: `aws apigateway update-deployment --rest-api-id``1234123412`--deployment-id`ztt4m2`--patch-operations op='replace',path='/description',value='newDescription'Output: `{ "description": "newDescription", "id": "ztt4m2", "createdDate": 1455218022 }`- 
                    For API details, see [UpdateDeployment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-deployment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-domain-name`.

- **AWS CLI**
- 
            
                    **To change the certificate name for a custom domain name**The following `update-domain-name`example changes the certificate name for a custom domain.`aws apigateway update-domain-name \ --domain-name``api.domain.tld`\ --patch-operations op='replace',path='/certificateArn',value='arn:aws:acm:us-west-2:111122223333:certificate/CERTEXAMPLE123EXAMPLE'Output: `{ "domainName": "api.domain.tld", "distributionDomainName": "d123456789012.cloudfront.net", "certificateArn": "arn:aws:acm:us-west-2:111122223333:certificate/CERTEXAMPLE123EXAMPLE", "certificateUploadDate": 1462565487 }`For more information, see [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateDomainName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-domain-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-integration-response`.

- **AWS CLI**
- 
            
                    **To change an integration response header to have a static mapping of '*'**Command: `aws apigateway update-integration-response --rest-api-id``1234123412`--resource-id`3gapai`--http-method`GET`--status-code`200`--patch-operations op='replace',path='/responseParameters/method.response.header.Access-Control-Allow-Origin',value='"'"'*'"'"'Output: `{ "statusCode": "200", "responseParameters": { "method.response.header.Access-Control-Allow-Origin": "'*'" } }`**To remove an integration response header**Command: `aws apigateway update-integration-response --rest-api-id``1234123412`--resource-id`3gapai`--http-method`GET`--status-code`200`--patch-operations op='remove',path='/responseParameters/method.response.header.Access-Control-Allow-Origin'- 
                    For API details, see [UpdateIntegrationResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-integration-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-integration`.

- **AWS CLI**
- 
            
                    **To add the 'Content-Type: application/json' Mapping Template configured with Input Passthrough**Command: `aws apigateway update-integration \ --rest-api-id``a1b2c3d4e5`\ --resource-id`a1b2c3`\ --http-method`POST`\ --patch-operations`"op='add',path='/requestTemplates/application~1json'"`**To update (replace) the 'Content-Type: application/json' Mapping Template configured with a custom template**Command: `aws apigateway update-integration \ --rest-api-id``a1b2c3d4e5`\ --resource-id`a1b2c3`\ --http-method`POST`\ --patch-operations "op='replace',path='/requestTemplates/application~1json',value='{"example": "json"}'"**To update (replace) a custom template associated with 'Content-Type: application/json' with Input Passthrough**Command: `aws apigateway update-integration \ --rest-api-id``a1b2c3d4e5`\ --resource-id`a1b2c3`\ --http-method`POST`\ --patch-operations`"op='replace',path='requestTemplates/application~1json'"`**To remove the 'Content-Type: application/json' Mapping Template**Command: `aws apigateway update-integration \ --rest-api-id``a1b2c3d4e5`\ --resource-id`a1b2c3`\ --http-method`POST`\ --patch-operations`"op='remove',path='/requestTemplates/application~1json'"`- 
                    For API details, see [UpdateIntegration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-integration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-method-response`.

- **AWS CLI**
- 
            
                    **To create a new method response header for the 200 response in a method and define it as not required (default)**Command: `aws apigateway update-method-response --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--status-code`200`--patch-operations op="add",path="/responseParameters/method.response.header.custom-header",value="false"**To delete a response model for the 200 response in a method**Command: `aws apigateway update-method-response --rest-api-id``1234123412`--resource-id`a1b2c3`--http-method`GET`--status-code`200`--patch-operations op="remove",path="/responseModels/application~1json"- 
                    For API details, see [UpdateMethodResponse](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-method-response.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-method`.

- **AWS CLI**
- 
            
                    **Example 1: To modify a method to require an API key**The following `update-method`example modifies the method to require an API key.`aws apigateway update-method \ --rest-api-id``1234123412`\ --resource-id`a1b2c3`\ --http-method`GET`\ --patch-operations op="replace",path="/apiKeyRequired",value="true"Output: `{ "httpMethod": "GET", "authorizationType": "NONE", "apiKeyRequired": true, "methodResponses": { "200": { "statusCode": "200", "responseModels": {} } }, "methodIntegration": { "type": "AWS", "httpMethod": "POST", "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789111:function:hello-world/invocations", "passthroughBehavior": "WHEN_NO_MATCH", "contentHandling": "CONVERT_TO_TEXT", "timeoutInMillis": 29000, "cacheNamespace": "h7i8j9", "cacheKeyParameters": [], "integrationResponses": { "200": { "statusCode": "200", "responseTemplates": {} } } } }`**Example 2: To modify a method to require IAM authorization**The following `update-method`example modifies the method to require IAM authorization.`aws apigateway update-method \ --rest-api-id``1234123412`\ --resource-id`a1b2c3`\ --http-method`GET`\ --patch-operations op="replace",path="/authorizationType",value="AWS_IAM"Output: `{ "httpMethod": "GET", "authorizationType": "AWS_IAM", "apiKeyRequired": false, "methodResponses": { "200": { "statusCode": "200", "responseModels": {} } }, "methodIntegration": { "type": "AWS", "httpMethod": "POST", "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789111:function:hello-world/invocations", "passthroughBehavior": "WHEN_NO_MATCH", "contentHandling": "CONVERT_TO_TEXT", "timeoutInMillis": 29000, "cacheNamespace": "h7i8j9", "cacheKeyParameters": [], "integrationResponses": { "200": { "statusCode": "200", "responseTemplates": {} } } } }`**Example 3: To modify a method to require Lambda authorization**The following `update-method`example modifies the method to required Lambda authorization.`aws apigateway update-method --rest-api-id``1234123412`\ --resource-id`a1b2c3`\ --http-method`GET`\ --patch-operations op="replace",path="/authorizationType",value="CUSTOM" op="replace",path="/authorizerId",value="e4f5g6"Output: `{ "httpMethod": "GET", "authorizationType": "CUSTOM", "authorizerId" : "e4f5g6", "apiKeyRequired": false, "methodResponses": { "200": { "statusCode": "200", "responseModels": {} } }, "methodIntegration": { "type": "AWS", "httpMethod": "POST", "uri": "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:123456789111:function:hello-world/invocations", "passthroughBehavior": "WHEN_NO_MATCH", "contentHandling": "CONVERT_TO_TEXT", "timeoutInMillis": 29000, "cacheNamespace": "h7i8j9", "cacheKeyParameters": [], "integrationResponses": { "200": { "statusCode": "200", "responseTemplates": {} } } } }`For more information, see [Create, configure, and test usage plans using the API Gateway CLI and REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-rest-api.html)and[Controlling and managing access to a REST API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-to-api.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateMethod](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-method.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-model`.

- **AWS CLI**
- 
            
                    **To change the description of a model in an API**Command: `aws apigateway update-model --rest-api-id``1234123412`--model-name '`Empty`' --patch-operations op=replace,path=/description,value='New Description'**To change the schema of a model in an API**Command: `aws apigateway update-model --rest-api-id``1234123412`--model-name '`Empty`' --patch-operations op=replace,path=/schema,value='"{ \"$schema\": \"http://json-schema.org/draft-04/schema#\", \"title\" : \"Empty Schema\", \"type\" : \"object\" }"'- 
                    For API details, see [UpdateModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-resource`.

- **AWS CLI**
- 
            
                    **To move a resource and place it under a different parent resource in an API**Command: `aws apigateway update-resource --rest-api-id``1234123412`--resource-id`1a2b3c`--patch-operations op=replace,path=/parentId,value='3c2b1a'Output: `{ "path": "/resource", "pathPart": "resource", "id": "1a2b3c", "parentId": "3c2b1a" }`**To rename a resource (pathPart) in an API**Command: `aws apigateway update-resource --rest-api-id``1234123412`--resource-id`1a2b3c`--patch-operations`op=replace,path=/pathPart,value=newresourcename`Output: `{ "path": "/newresourcename", "pathPart": "newresourcename", "id": "1a2b3c", "parentId": "3c2b1a" }`- 
                    For API details, see [UpdateResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-rest-api`.

- **AWS CLI**
- 
            
                    **To change the name of an API**Command: `aws apigateway update-rest-api --rest-api-id``1234123412`--patch-operations op=replace,path=/name,value='New Name'**To change the description of an API**Command: `aws apigateway update-rest-api --rest-api-id``1234123412`--patch-operations op=replace,path=/description,value='New Description'- 
                    For API details, see [UpdateRestApi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-rest-api.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-stage`.

- **AWS CLI**
- 
            
                    **Example 1: To override the stage settings for a resource and method**The following `update-stage`example overrides the stage settings and turns off full request/response logging for a specific resource and method.`aws apigateway update-stage \ --rest-api-id``1234123412`\ --stage-name '`dev`' \ --patch-operations`op=replace,path=/~1resourceName/GET/logging/dataTrace,value=false`Output: `{ "deploymentId": "5ubd17", "stageName": "dev", "cacheClusterEnabled": false, "cacheClusterStatus": "NOT_AVAILABLE", "methodSettings": { "~1resourceName/GET": { "metricsEnabled": false, "dataTraceEnabled": false, "throttlingBurstLimit": 5000, "throttlingRateLimit": 10000.0, "cachingEnabled": false, "cacheTtlInSeconds": 300, "cacheDataEncrypted": false, "requireAuthorizationForCacheControl": true, "unauthorizedCacheControlHeaderStrategy": "SUCCEED_WITH_RESPONSE_HEADER" } }, "tracingEnabled": false, "createdDate": "2022-07-18T10:11:18-07:00", "lastUpdatedDate": "2022-07-18T10:19:04-07:00" }`For more information, see [Setting up a stage for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html)in the*Amazon API Gateway Developer Guide*.**Example 2: To update the stage settings for all resources and methods of an API stage**The following `update-stage`example turns on full request/response logging for all resources and methods of an API stage.`aws apigateway update-stage \ --rest-api-id``1234123412`\ --stage-name '`dev`' \ --patch-operations '`op=replace,path=/*/*/logging/dataTrace,value=true`'Output: `{ "deploymentId": "5ubd17", "stageName": "dev", "cacheClusterEnabled": false, "cacheClusterStatus": "NOT_AVAILABLE", "methodSettings": { "*/*": { "metricsEnabled": false, "dataTraceEnabled": true, "throttlingBurstLimit": 5000, "throttlingRateLimit": 10000.0, "cachingEnabled": false, "cacheTtlInSeconds": 300, "cacheDataEncrypted": false, "requireAuthorizationForCacheControl": true, "unauthorizedCacheControlHeaderStrategy": "SUCCEED_WITH_RESPONSE_HEADER" } }, "tracingEnabled": false, "createdDate": "2022-07-18T10:11:18-07:00", "lastUpdatedDate": "2022-07-18T10:31:04-07:00" }`For more information, see [Setting up a stage for a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-stages.html)in the*Amazon API Gateway Developer Guide*.- 
                    For API details, see [UpdateStage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-stage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-usage-plan`.

- **AWS CLI**
- 
            
                    **To change the period defined in a Usage Plan**Command: `aws apigateway update-usage-plan --usage-plan-id``a1b2c3`--patch-operations op="replace",path="/quota/period",value="MONTH"**To change the quota limit defined in a Usage Plan**Command: `aws apigateway update-usage-plan --usage-plan-id``a1b2c3`--patch-operations op="replace",path="/quota/limit",value="500"**To change the throttle rate limit defined in a Usage Plan**Command: `aws apigateway update-usage-plan --usage-plan-id``a1b2c3`--patch-operations op="replace",path="/throttle/rateLimit",value="10"**To change the throttle burst limit defined in a Usage Plan**Command: `aws apigateway update-usage-plan --usage-plan-id``a1b2c3`--patch-operations op="replace",path="/throttle/burstLimit",value="20"- 
                    For API details, see [UpdateUsagePlan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-usage-plan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-usage`.

- **AWS CLI**
- 
            
                    **To temporarily modify the quota on an API key for the current period defined in the Usage Plan**Command: `aws apigateway update-usage --usage-plan-id``a1b2c3`--key-id`1NbjQzMReAkeEQPNAW8r3dXsU2rDD7fc7f2Sipnu`--patch-operations op="replace",path="/remaining",value="50"- 
                    For API details, see [UpdateUsage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-usage.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-vpc-link`.

- **AWS CLI**
- 
            
                    **Example 1: To update an existing VPC link name**The following `update-vpc-link`example updates the name of the specified VPC link.`aws apigateway update-vpc-link \ --vpc-link-id``ab3de6`\ --patch-operations`op=replace,path=/name,value=my-vpc-link`Output: `{ "id": "ab3de6", "name": "my-vpc-link", "targetArns": [ "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/my-lb/12a456s89aaa12345" ], "status": "AVAILABLE", "statusMessage": "Your vpc link is ready for use", "tags": {} }`For more information, see [Updating existing VPC link](https://docs.aws.amazon.com/cli/latest/reference/apigateway/update-vpc-link.html)in the*AWS CLI Command Reference*.**Example 2: To update an existing VPC link name and description**The following `update-vpc-link`example updates name of the specified VPC link.`aws apigateway update-vpc-link \ --vpc-link-id``ab3de6`\ --patch-operations`op=replace,path=/name,value=my-vpc-link`op=replace,path=/description,value="My custom description"Output: `{ "id": "ab3de6", "name": "my-vpc-link", "description": "My custom description", "targetArns": [ "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/my-lb/12a456s89aaa12345" ], "status": "AVAILABLE", "statusMessage": "Your vpc link is ready for use", "tags": {} }`For more information, see [Updating existing VPC link](https://docs.aws.amazon.com/cli/latest/reference/apigateway/update-vpc-link.html)in the*AWS CLI Command Reference*.- 
                    For API details, see [UpdateVpcLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-vpc-link.html)in*AWS CLI Command Reference*.
 
-