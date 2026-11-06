# Storage Gateway examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_storage-gateway_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_storage-gateway_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Storage Gateway.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `describe-gateway-information`.

- **AWS CLI**
- 
            
                    **To describe a gateway**The following `describe-gateway-information`command returns metadata about the specified gateway. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in the command.This examples specifies a gateway with the id `sgw-12A3456B`in account`123456789012`:`aws storagegateway describe-gateway-information --gateway-arn``"arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B"`This command outputs a JSON block that contains metadata about about the gateway such as its name, network interfaces, configured time zone, and the state (whether the gateway is running or not). - 
                    For API details, see [DescribeGatewayInformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-gateway-information.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-file-shares`.

- **AWS CLI**
- 
            
                    **To list file shares**The following `command-name`example lists the available widgets in your AWS account.`aws storagegateway list-file-shares \ --gateway-arn``arn:aws:storagegateway:us-east-1:209870788375:gateway/sgw-FB02E292`Output: `{ "FileShareInfoList": [ { "FileShareType": "NFS", "FileShareARN": "arn:aws:storagegateway:us-east-1:111122223333:share/share-2FA12345", "FileShareId": "share-2FA12345", "FileShareStatus": "AVAILABLE", "GatewayARN": "arn:aws:storagegateway:us-east-1:111122223333:gateway/sgw-FB0AAAAA" } ], "Marker": null }`For more information, see [ListFileShares](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ListFileShares.html)in the*AWS Storage Gateway Service API Reference*.- 
                    For API details, see [ListFileShares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-file-shares.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-gateways`.

- **AWS CLI**
- 
            
                    **To list gateways for an account**The following `list-gateways`command lists all the gateways defined for an account:`aws storagegateway list-gateways`This command outputs a JSON block that contains a list of gateway Amazon Resource Names (ARNs). - 
                    For API details, see [ListGateways](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-gateways.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-volumes`.

- **AWS CLI**
- 
            
                    **To list the volumes configured for a gateway**The following `list-volumes`command returns a list of volumes configured for the specified gateway. To specify which gateway to describe, use the Amazon Resource Name (ARN) of the gateway in the command.This examples specifies a gateway with the id `sgw-12A3456B`in account`123456789012`:`aws storagegateway list-volumes --gateway-arn``"arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B"`This command outputs a JSON block that a list of volumes that includes the type and ARN for each volume. - 
                    For API details, see [ListVolumes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/list-volumes.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `refresh-cache`.

- **AWS CLI**
- 
            
                    **To refresh the file share cache**The following `refresh-cache`example refreshes the cache for the specified file share.`aws storagegateway refresh-cache \ --file-share-arn``arn:aws:storagegateway:us-east-1:111122223333:share/share-2FA12345`Output: `{ "FileShareARN": "arn:aws:storagegateway:us-east-1:111122223333:share/share-2FA12345", "NotificationId": "4954d4b1-abcd-ef01-1234-97950a7d3483" }`For more information, see [ListFileShares](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_RefreshCache.html)in the*AWS Storage Gateway Service API Reference*.- 
                    For API details, see [RefreshCache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/refresh-cache.html)in*AWS CLI Command Reference*.
 
-