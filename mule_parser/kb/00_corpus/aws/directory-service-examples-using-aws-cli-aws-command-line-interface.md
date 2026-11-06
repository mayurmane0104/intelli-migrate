# Directory Service examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_directory-service_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_directory-service_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Directory Service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `describe-directories`.

- **AWS CLI**
- 
            
                    **To get details about your directories**The following `describe-directories`example displays details about the specified directory.`aws ds describe-directories \ --directory-id``d-a1b2c3d4e5`Output: `{ "DirectoryDescriptions": [ { "DirectoryId": "d-a1b2c3d4e5", "Name": "mydirectory.example.com", "ShortName": "mydirectory", "Size": "Small", "Edition": "Standard", "Alias": "d-a1b2c3d4e5", "AccessUrl": "d-a1b2c3d4e5.awsapps.com", "Stage": "Active", "ShareStatus": "Shared", "ShareMethod": "HANDSHAKE", "ShareNotes": "These are my share notes", "LaunchTime": "2019-07-08T15:33:46.327000-07:00", "StageLastUpdatedDateTime": "2019-07-08T15:59:12.307000-07:00", "Type": "SharedMicrosoftAD", "SsoEnabled": false, "DesiredNumberOfDomainControllers": 0, "OwnerDirectoryDescription": { "DirectoryId": "d-b2c3d4e5f6", "AccountId": "123456789111", "DnsIpAddrs": [ "203.113.0.248", "203.113.0.253" ], "VpcSettings": { "VpcId": "vpc-a1b2c3d4", "SubnetIds": [ "subnet-a1b2c3d4", "subnet-d4c3b2a1" ], "AvailabilityZones": [ "us-west-2a", "us-west-2c" ] } } } ] }`- 
                    For API details, see [DescribeDirectories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-trusts`.

- **AWS CLI**
- 
            
                    **To get details about your trust relationships**The following `describe-trusts`example displays details about the trust relationships for the specified directory.`aws ds describe-trusts \ --directory-id``d-a1b2c3d4e5`Output: `{ "Trusts": [ { "DirectoryId": "d-a1b2c3d4e5", "TrustId": "t-9a8b7c6d5e", "RemoteDomainName": "other.example.com", "TrustType": "Forest", "TrustDirection": "Two-Way", "TrustState": "Verified", "CreatedDateTime": "2017-06-20T18:08:45.614000-07:00", "LastUpdatedDateTime": "2019-06-04T10:52:12.410000-07:00", "StateLastUpdatedDateTime": "2019-06-04T10:52:12.410000-07:00", "SelectiveAuth": "Disabled" } ] }`- 
                    For API details, see [DescribeTrusts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-trusts.html)in*AWS CLI Command Reference*.
 
-