# CodeConnections examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_codestar-connections_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_codestar-connections_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CodeConnections.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-connection`.

- **AWS CLI**
- 
            
                    **To create a connection**The following `create-connection`example shows how to create a connection to a third-party repository. This example creates a connection where the third-party provider is Bitbucket.A connection created through the AWS CLI or AWS CloudFormation is in Pending status by default. After you create a connection with the CLI or AWS CloudFormation, use the console to edit the connection to make its status Available. `aws codestar-connections create-connection \ --provider-type``Bitbucket`\ --connection-name`MyConnection`Output: `{ "ConnectionArn": "arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f" }`For more information, see [Create a connection](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-create.html)in the*Developer Tools console User Guide*.- 
                    For API details, see [CreateConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-host`.

- **AWS CLI**
- 
            
                    **To create a host**The following `create-host`example shows how to create a host to represent the endpoint for the infrastructure where your third-party provider is installed. This example creates a host where the third-party installed provider is GitHub Enterprise Server.A host created through the AWS CLI is in Pending status by default. After you create a host with the CLI, use the console or the CLI to set up the host to make its status Available. `aws codestar-connections create-host \ --name``MyHost`\ --provider-type`GitHubEnterpriseServer`\ --provider-endpoint`"https://my-instance.dev"`Output: `{ "HostArn": "arn:aws:codestar-connections:us-east-1:123456789012:host/My-Host-28aef605" }`For more information, see [Create a host (CLI)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-create.html)in the*Developer Tools console User Guide*.- 
                    For API details, see [CreateHost](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/create-host.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-connection`.

- **AWS CLI**
- 
            
                    **To delete a connection**The following `delete-connection`example shows how to delete a connection.`aws codestar-connections delete-connection \ --connection-arn``arn:aws:codestar-connections:us-west-2:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f`This command produces no output. For more information, see [Delete a connection (CLI)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-delete.html#connections-delete-cli)in the*Developer Tools console User Guide*.- 
                    For API details, see [DeleteConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-host`.

- **AWS CLI**
- 
            
                    **To delete a host**The following `delete-host`example shows how to delete a host. Before you can delete a host, you must delete all connections associated with the host.`aws codestar-connections delete-host \ --host-arn``"arn:aws:codestar-connections:us-east-1 :123456789012:host/My-Host-28aef605"`This command produces no output. For more information, see [Delete a host (CLI)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-delete.html#connections-host-delete-cli)in the*Developer Tools console User Guide*.- 
                    For API details, see [DeleteHost](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/delete-host.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-connection`.

- **AWS CLI**
- 
            
                    **To get information about a connection**The following `get-connection`example shows details about a connection.`aws codestar-connections get-connection \ --connection-arn``arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f`Output: `{ "Connection": { "ConnectionName": "MyConnection", "ConnectionArn": "arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f", "ProviderType": "Bitbucket", "OwnerAccountId": "123456789012", "ConnectionStatus": "AVAILABLE" } }`For more information, see [View connection details](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-view-details.html)in the*Developer Tools console User Guide*.- 
                    For API details, see [GetConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-host`.

- **AWS CLI**
- 
            
                    **To get information about a host**The following `get-host`example shows details about a host:`aws codestar-connections get-host \ --host-arn``arn:aws:codestar-connections:us-east-1:123456789012:host/MyHost-28aef605`Output: `{ "Name": "MyHost", "Status": "AVAILABLE", "ProviderType": "GitHubEnterpriseServer", "ProviderEndpoint": "https://test-instance-1.dev/" }`For more information, see [View host details (CLI)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-view.html#connections-host-view-cli)in the*Developer Tools console User Guide*.- 
                    For API details, see [GetHost](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/get-host.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-connections`.

- **AWS CLI**
- 
            
                    **To list connections**The following `list-connections`example retrieves a list of all connections in your account for the Bitbucket provider type.:`aws codestar-connections list-connections \ --provider-type``Bitbucket`\ --max-results`5`\ --`next-token`: next-tokenOutput: `{ "Connections": [ { "ConnectionName": "my-connection", "ProviderType": "Bitbucket", "Status": "PENDING", "ARN": "arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f", "OwnerAccountId": "123456789012" }, { "ConnectionName": "my-other-connection", "ProviderType": "Bitbucket", "Status": "AVAILABLE", "ARN": "arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f", "OwnerAccountId": "123456789012" }, ], "NextToken": "next-token" }`For more information, see [List connections (CLI)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-list.html#connections-list-cli)in the*Developer Tools console User Guide*.- 
                    For API details, see [ListConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-connections.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-hosts`.

- **AWS CLI**
- 
            
                    **To list hosts**The following `list-hosts`example retrieves a list of all hosts in your account.`aws codestar-connections list-hosts`Output: `{ "Hosts": [ { "Name": "My-Host", "HostArn": "arn:aws:codestar-connections:us-east-1:123456789012:host/My-Host-28aef605", "ProviderType": "GitHubEnterpriseServer", "ProviderEndpoint": "https://my-instance.test.dev", "Status": "AVAILABLE" } ] }`For more information, see [List hosts (CLI)](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-host-list.html)in the*Developer Tools console User Guide*.- 
                    For API details, see [ListHosts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-hosts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags**The following `list-tags-for-resource`example retrieves a list of all tags attached to the specified connections resource.`aws codestar-connections list-tags-for-resource \ --resource-arn``arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f`Output: `{ "Tags": [ { "Key": "Project", "Value": "ProjectA" }, { "Key": "ReadOnly", "Value": "true" } ] }`For more information, see [View tags for a connections resource](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-tag.html#connections-tag-view)in the*Developer Tools console User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example associates a set of provided tags with a connection. Use this command to add or edit tags.`aws codestar-connections tag-resource \ --resource-arn``arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f`\ --tags`Key=Project,Value=ProjectA``Key=IscontainerBased,Value=true`This command produces no output. For more information, see [Add tags to a connections resource](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-tag.html#connections-tag-add)in the*Developer Tools console User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove AWS tags from a connections resource**The following `untag-resource`removes a tag from the specified resource.`aws codestar-connections untag-resource \ --resource-arn``arn:aws:codestar-connections:us-east-1:123456789012:connection/aEXAMPLE-8aad-4d5d-8878-dfcab0bc441f`\ --tag-keys`Project``ReadOnly`Output: `{ "Tags": [] }`For more information, see [Remove tags from a connections resource](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections-tag.html#connections-tag-delete)in the*Developer Tools console User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar-connections/untag-resource.html)in*AWS CLI Command Reference*.
 
-