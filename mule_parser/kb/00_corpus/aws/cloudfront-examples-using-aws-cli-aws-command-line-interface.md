# CloudFront examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudfront_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudfront_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CloudFront.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-distribution-tenant-web-acl`.

- **AWS CLI**
- 
            
                    **To associate a web ACL with a CloudFront distribution tenant**The following `associate-distribution-tenant-web-acl`example associates a web ACL with a CloudFront distribution with ETag`E13V1IB3VIYABC`.`aws cloudfront associate-distribution-tenant-web-acl \ --id``dt_2wjDZi3hD1ivOXf6rpZJO1AB`\ --if-match`E13V1IB3VIYABC`\ --web-acl-arn`arn:aws:wafv2:us-east-1:123456789012:global/webacl/web-global-example/626900da-5f64-418b-ba9b-743f37123ABC`Output: `{ "ETag": "E1VC38T7YXBABC", "Id": "dt_2wjDZi3hD1ivOXf6rpZJO1AB", "WebACLArn": "arn:aws:wafv2:us-east-1:123456789012:global/webacl/web-global-example/626900da-5f64-418b-ba9b-743f37123ABC" }`For more information, see [Use AWS WAF protections](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [AssociateDistributionTenantWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/associate-distribution-tenant-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-distribution-web-acl`.

- **AWS CLI**
- 
            
                    **To associate a web ACL with a CloudFront distribution**The following `associate-distribution-web-acl`example associates a web ACL with a CloudFront distribution.`aws cloudfront associate-distribution-web-acl \ --id``E1XNX8R2GOAABC`\ --if-match`E2YWS1C2J3OABC`\ --web-acl-arn`arn:aws:wafv2:us-east-1:123456789012:global/webacl/web-global-example/626900da-5f64-418b-ba9b-743f3746cABC`Output: `{ "ETag": "E3QE7ED60U0ABC", "Id": "E1XNX8R2GOAABC", "WebACLArn": "arn:aws:wafv2:us-east-1:123456789012:global/webacl/web-global-example/626900da-5f64-418b-ba9b-743f3746cABC" }`For more information, see [Use AWS WAF protections](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-awswaf.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [AssociateDistributionWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/associate-distribution-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-cloud-front-origin-access-identity`.

- **AWS CLI**
- 
            
                    **To create a CloudFront origin access identity**The following example creates a CloudFront origin access identity (OAI) by providing the OAI configuration as a command line argument: `aws cloudfront create-cloud-front-origin-access-identity \ --cloud-front-origin-access-identity-config \ CallerReference="cli-example",Comment="Example OAI"`You can accomplish the same thing by providing the OAI configuration in a JSON file, as shown in the following example: `aws cloudfront create-cloud-front-origin-access-identity \ --cloud-front-origin-access-identity-config``file://OAI-config.json`The file `OAI-config.json`is a JSON document in the current directory that contains the following:`{ "CallerReference": "cli-example", "Comment": "Example OAI" }`Whether you provide the OAI configuration with a command line argument or a JSON file, the output is the same: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/origin-access-identity/cloudfront/E74FTE3AEXAMPLE", "ETag": "E2QWRUHEXAMPLE", "CloudFrontOriginAccessIdentity": { "Id": "E74FTE3AEXAMPLE", "S3CanonicalUserId": "cd13868f797c227fbea2830611a26fe0a21ba1b826ab4bed9b7771c9aEXAMPLE", "CloudFrontOriginAccessIdentityConfig": { "CallerReference": "cli-example", "Comment": "Example OAI" } } }`- 
                    For API details, see [CreateCloudFrontOriginAccessIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-cloud-front-origin-access-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-connection-group`.

- **AWS CLI**
- 
            
                    **To create a connection group in CloudFront**The following `create-connection-group`example creates an enabled connection group, specifies an Anycast static IP list, and disables IPv6.`aws cloudfront create-connection-group \ --name``cg-with-anycast-ip-list`\ --no-ipv6-enabled \ --enabled \ --anycast-ip-list-id`aip_CCkW6gKrDiBD4n78123ABC`\ --tags`"Items=[{Key=abc,Value=123}]"`Output: `{ "ETag": "E23ZP02F085ABC", "ConnectionGroup": { "Id": "cg_2yb6uj74B4PCbfhT31WFdiSABC", "Name": "cg-with-anycast-ip-list", "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_2yb6uj74B4PCbfhT31WFdiSABC", "CreatedTime": "2025-06-16T16:25:50.061000+00:00", "LastModifiedTime": "2025-06-16T16:25:50.061000+00:00", "Tags": { "Items": [ { "Key": "abc", "Value": "123" } ] }, "Ipv6Enabled": false, "RoutingEndpoint": "dj6xusxq65abc.cloudfront.net", "AnycastIpListId": "aip_CCkW6gKrDiBD4n78123ABC", "Status": "InProgress", "Enabled": true, "IsDefault": false } }`For more information, see [Create custom connection group (optional)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [CreateConnectionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-connection-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-distribution-tenant`.

- **AWS CLI**
- 
            
                    **Example 1: To create a CloudFront distribution tenant that uses a custom certificate**The following `create-distribution-tenant`example creates a CloudFront distribution tenant that specifies customizations to disable WAF, add geo-restrictions, and uses another TLS certificate.`aws cloudfront create-distribution-tenant \ --cli-input-json``file://tenant.json`Contents of `tenant.json`:`{ "DistributionId": "E1XNX8R2GOAABC", "Domains": [ { "Domain": "example.com" } ], "Parameters": [ { "Name": "testParam", "Value": "defaultValue" } ], "ConnectionGroupId": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "Enabled": false, "Tags": { "Items": [ { "Key": "tag", "Value": "tagValue" } ] }, "Name": "new-tenant-customizations", "Customizations": { "GeoRestrictions": { "Locations": ["DE"], "RestrictionType": "whitelist" }, "WebAcl": { "Action": "disable" }, "Certificate": { "Arn": "arn:aws:acm:us-east-1:123456789012:certificate/ec53f564-ea5a-4e4a-a0a2-e3c989449abc" } } }`Output: `{ "ETag": "E23ZP02F085ABC", "DistributionTenant": { "Id": "dt_2yN5tYwVbPKr7m2IB69M1yp1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "new-tenant-customizations", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2yN5tYwVbPKr7m2IB69M1yp1AB", "Domains": [ { "Domain": "example.com", "Status": "active" } ], "Tags": { "Items": [ { "Key": "tag", "Value": "tagValue" } ] }, "Customizations": { "WebAcl": { "Action": "disable" }, "Certificate": { "Arn": "arn:aws:acm:us-east-1:123456789012:certificate/ec53f564-ea5a-4e4a-a0a2-e3c989449abc" }, "GeoRestrictions": { "RestrictionType": "whitelist", "Locations": [ "DE" ] } }, "Parameters": [ { "Name": "testParam", "Value": "defaultValue" } ], "ConnectionGroupId": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "CreatedTime": "2025-06-11T17:20:06.432000+00:00", "LastModifiedTime": "2025-06-11T17:20:06.432000+00:00", "Enabled": false, "Status": "InProgress" } }`**Example 2: To create a distribution tenant with an inherited certificate**The following `create-distribution-tenant`example creates a distribution tenant and specifies an inherited TLS certificate from the multi-tenant distribution.`aws cloudfront create-distribution-tenant \ --cli-input-json``file://tenant.json`Contents of `tenant.json`:`{ "DistributionId": "E1HVIAU7U12ABC", "Domains": [ { "Domain": "example.com" } ], "Parameters": [ { "Name": "tenantName", "Value": "first-tenant" } ], "Enabled": true, "Name": "new-tenant-no-cert" }`Output: `{ "ETag": "E23ZP02F0ABC", "DistributionTenant": { "Id": "dt_2zhRB0vBe0B72LZCVy1mgzI1AB", "DistributionId": "E1HVIAU7U12ABC", "Name": "new-tenant-no-cert", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2zhRB0vBe0B72LZCVy1mgzI1AB", "Domains": [ { "Domain": "example.com", "Status": "active" } ], "Parameters": [ { "Name": "tenantName", "Value": "first-tenant" } ], "ConnectionGroupId": "cg_2yQEwpipGFN0hhA0ZemPabOABC", "CreatedTime": "2025-07-10T20:59:38.414000+00:00", "LastModifiedTime": "2025-07-10T20:59:38.414000+00:00", "Enabled": true, "Status": "InProgress" } }`**Example 3: To create a CloudFront distribution tenant using a CloudFront-hosted validation token**The following `create-distribution-tenant`example creates a distribution tenant and uses a CloudFront-hosted validation token for your domain name.`aws cloudfront create-distribution-tenant \ --cli-input-json``file://tenant.json`Contents of `tenant.json`:`{ "DistributionId": "E2GJ5J9QN12ABC", "Domains": [ { "Domain": "example.com" } ], "Parameters": [ { "Name": "tenantName", "Value": "first-tenant" } ], "ConnectionGroupId": "cg_2yQEwpipGFN0hhA0ZemPabOABC", "Enabled": true, "Name": "new-tenant-cf-hosted", "ManagedCertificateRequest": { "ValidationTokenHost": "cloudfront" } }`**Important:**To successfully run this command, you must configure a CNAME DNS record that points your new domain (example.com) to the routing endpoint of the connection group that is associated with the distribution tenant. This CNAME record must also be propagated before CloudFront can successfully complete this request.Output: `{ "ETag": "E23ZP02F0ABC", "DistributionTenant": { "Id": "dt_2zhStKrA524GvvTWJX92Ozl1AB", "DistributionId": "E2GJ5J9QN12ABC", "Name": "new-tenant-cf-hosted", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2zhStKrA524GvvTWJX92Ozl1AB", "Domains": [ { "Domain": "example.com", "Status": "inactive" } ], "Parameters": [ { "Name": "tenantName", "Value": "first-tenant" } ], "ConnectionGroupId": "cg_2zhSaGatwwXjTjE42nneZzqABC", "CreatedTime": "2025-07-10T21:13:46.416000+00:00", "LastModifiedTime": "2025-07-10T21:13:46.416000+00:00", "Enabled": true, "Status": "InProgress" } }`**Example 4: To create a CloudFront distribution tenant using a self-hosted validation token**The following `create-distribution-tenant`example creates a CloudFront distribution tenant and uses a self-hosted validation token.`aws cloudfront create-distribution-tenant \ --cli-input-json``file://tenant.json`Contents of `tenant.json`:`{ "DistributionId": "E2GJ5J9QN12ABC", "Domains": [ { "Domain": "example.com" } ], "Parameters": [ { "Name": "tenantName", "Value": "first-tenant" } ], "Enabled": true, "Name": "new-tenant-self-hosted", "ManagedCertificateRequest": { "ValidationTokenHost": "self-hosted" } }`Output: `{ "ETag": "E23ZP02F0ABC", "DistributionTenant": { "Id": "dt_2zhTFBV93OfFJJ3YMdNM5BC1AB", "DistributionId": "E2GJ5J9QN12ABC", "Name": "new-tenant-self-hosted", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2zhTFBV93OfFJJ3YMdNM5BC1AB", "Domains": [ { "Domain": "example.com", "Status": "inactive" } ], "Parameters": [ { "Name": "tenantName", "Value": "first-tenant" } ], "ConnectionGroupId": "cg_2yQEwpipGFN0hhA0ZemPabOABC", "CreatedTime": "2025-07-10T21:16:39.828000+00:00", "LastModifiedTime": "2025-07-10T21:16:39.828000+00:00", "Enabled": true, "Status": "InProgress" } }`**Important:**After you run this command, the distribution tenant will be created without validation. To validate the managed certificate request and configure the DNS when you're ready to start receiving traffic, see[Complete domain setup](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managed-cloudfront-certificates.html#complete-domain-ownership)in the*Amazon CloudFront Developer Guide*.For more information about creating distribution tenants, see [Create a distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-creating-console.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [CreateDistributionTenant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-distribution-tenant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-distribution-with-tags`.

- **AWS CLI**
- 
            
                    **To create a CloudFront distribution with tags**The following `create-distribution-with-tags`example creates a distribution with two tags by providing the distribution configuration and tags in a JSON file named`dist-config-with-tags.json`.`aws cloudfront create-distribution-with-tags \ --distribution-config-with-tags``file://dist-config-with-tags.json`The file `dist-config-with-tags.json`is a JSON document in the current folder. Note the`Tags`object at the top of the file, which contains two tags:`Name = ExampleDistribution``Project = ExampleProject`Contents of `dist-config-with-tags.json`:`{ "Tags": { "Items": [ { "Key": "Name", "Value": "ExampleDistribution" }, { "Key": "Project", "Value": "ExampleProject" } ] }, "DistributionConfig": { "CallerReference": "cli-example", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true } }`Output: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/distribution/EDFDVBD6EXAMPLE", "ETag": "E2QWRUHEXAMPLE", "Distribution": { "Id": "EDFDVBD6EXAMPLE", "ARN": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE", "Status": "InProgress", "LastModifiedTime": "2019-12-04T23:35:41.433Z", "InProgressInvalidationBatches": 0, "DomainName": "d111111abcdef8.cloudfront.net", "ActiveTrustedSigners": { "Enabled": false, "Quantity": 0 }, "DistributionConfig": { "CallerReference": "cli-example", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true } } }`- 
                    For API details, see [CreateDistributionWithTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-distribution-with-tags.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-distribution`.

- **AWS CLI**
- 
            
                    **Example 1: To create a CloudFront distribution**The following `create-distribution`example creates a distribution for an S3 bucket named`amzn-s3-demo-bucket`, and also specifies`index.html`as the default root object, using command line arguments.`aws cloudfront create-distribution \ --origin-domain-name``amzn-s3-demo-bucket.s3.amazonaws.com`\ --default-root-object`index.html`Output: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/distribution/EMLARXS9EXAMPLE", "ETag": "E9LHASXEXAMPLE", "Distribution": { "Id": "EMLARXS9EXAMPLE", "ARN": "arn:aws:cloudfront::123456789012:distribution/EMLARXS9EXAMPLE", "Status": "InProgress", "LastModifiedTime": "2019-11-22T00:55:15.705Z", "InProgressInvalidationBatches": 0, "DomainName": "d111111abcdef8.cloudfront.net", "ActiveTrustedSigners": { "Enabled": false, "Quantity": 0 }, "DistributionConfig": { "CallerReference": "cli-example", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true } } }`**Example 2: To create a CloudFront distribution using a JSON file**The following `create-distribution`example creates a distribution for an S3 bucket named`amzn-s3-demo-bucket`, and also specifies`index.html`as the default root object, using a JSON file.`aws cloudfront create-distribution \ --distribution-config``file://dist-config.json`Contents of `dist-config.json`:`{ "CallerReference": "cli-example", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true }`See Example 1 for sample output. **Example 3: To create a CloudFront multi-tenant distribution with a certificate**The following `create-distribution`example creates a CloudFront distribution with multi-tenant support and a specifies a TLS certificate.`aws cloudfront create-distribution \ --distribution-config``file://dist-config.json`Contents of `dist-config.json`:`{ "CallerReference": "cli-example-with-cert", "Comment": "CLI example distribution", "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "DomainName": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "OriginPath": "/{{tenantName}}", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e5ABC", "ViewerProtocolPolicy": "allow-all", "AllowedMethods": { "Quantity": 2, "Items": ["HEAD", "GET"], "CachedMethods": { "Quantity": 2, "Items": ["HEAD", "GET"] } } }, "Enabled": true, "ViewerCertificate": { "ACMCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/191306a1-db01-49ca-90ef-fc414ee5dabc", "SSLSupportMethod": "sni-only" }, "HttpVersion": "http2", "ConnectionMode": "tenant-only", "TenantConfig": { "ParameterDefinitions": [ { "Name": "tenantName", "Definition": { "StringSchema": { "Comment": "tenantName parameter", "DefaultValue": "root", "Required": false } } } ] } }`Output: `{ "Location": "https://cloudfront.amazonaws.com/2020-05-31/distribution/E1HVIAU7UABC", "ETag": "E20LT7R1BABC", "Distribution": { "Id": "E1HVIAU7U12ABC", "ARN": "arn:aws:cloudfront::123456789012:distribution/E1HVIAU7U12ABC", "Status": "InProgress", "LastModifiedTime": "2025-07-10T20:33:31.117000+00:00", "InProgressInvalidationBatches": 0, "DomainName": "example.com", "ActiveTrustedSigners": { "Enabled": false, "Quantity": 0 }, "ActiveTrustedKeyGroups": { "Enabled": false, "Quantity": 0 }, "DistributionConfig": { "CallerReference": "cli-example-with-cert", "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "DomainName": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "OriginPath": "/{{tenantName}}", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" }, "ConnectionAttempts": 3, "ConnectionTimeout": 10, "OriginShield": { "Enabled": false }, "OriginAccessControlId": "" } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "TrustedKeyGroups": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "AllowedMethods": { "Quantity": 2, "Items": ["HEAD", "GET"], "CachedMethods": { "Quantity": 2, "Items": ["HEAD", "GET"] } }, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "", "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e5ABC", "GrpcConfig": { "Enabled": false } }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "CLI example distribution", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": false, "ACMCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/1954f095-11b6-4daf-9952-0c308a00abc", "SSLSupportMethod": "sni-only", "MinimumProtocolVersion": "TLSv1.2_2021", "Certificate": "arn:aws:acm:us-east-1:123456789012:certificate/1954f095-11b6-4daf-9952-0c308a00abc", "CertificateSource": "acm" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "TenantConfig": { "ParameterDefinitions": [ { "Name": "tenantName", "Definition": { "StringSchema": { "Comment": "tenantName parameter", "DefaultValue": "root", "Required": false } } } ] }, "ConnectionMode": "tenant-only" } } }`For more information, see [Working with distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html)in the*Amazon CloudFront Developer Guide*.**Example 4: To create a CloudFront multi-tenant distribution without a certificate**The following `create-distribution`example creates a CloudFront distribution with multi-tenant support but without a TLS certificate.`aws cloudfront create-distribution \ --distribution-config``file://dist-config.json`Contents of `dist-config.json`:`{ "CallerReference": "cli-example", "Comment": "CLI example distribution", "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "DomainName": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "OriginPath": "/{{tenantName}}", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e5ABC", "ViewerProtocolPolicy": "allow-all", "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } } }, "Enabled": true, "HttpVersion": "http2", "ConnectionMode": "tenant-only", "TenantConfig": { "ParameterDefinitions": [ { "Name": "tenantName", "Definition": { "StringSchema": { "Comment": "tenantName parameter", "DefaultValue": "root", "Required": false } } } ] } }`Output: `{ "Location": "https://cloudfront.amazonaws.com/2020-05-31/distribution/E2GJ5J9QN12ABC", "ETag": "E37YLVVQIABC", "Distribution": { "Id": "E2GJ5J9QNABC", "ARN": "arn:aws:cloudfront::123456789012:distribution/E2GJ5J9QN12ABC", "Status": "InProgress", "LastModifiedTime": "2025-07-10T20:35:20.565000+00:00", "InProgressInvalidationBatches": 0, "DomainName": "example.com", "ActiveTrustedSigners": { "Enabled": false, "Quantity": 0 }, "ActiveTrustedKeyGroups": { "Enabled": false, "Quantity": 0 }, "DistributionConfig": { "CallerReference": "cli-example-no-cert", "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "DomainName": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "OriginPath": "/{{tenantName}}", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" }, "ConnectionAttempts": 3, "ConnectionTimeout": 10, "OriginShield": { "Enabled": false }, "OriginAccessControlId": "" } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "TrustedKeyGroups": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "", "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e5ABC", "GrpcConfig": { "Enabled": false } }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "CLI example distribution", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "SSLSupportMethod": "sni-only", "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "TenantConfig": { "ParameterDefinitions": [ { "Name": "tenantName", "Definition": { "StringSchema": { "Comment": "tenantName parameter", "DefaultValue": "root", "Required": false } } } ] }, "ConnectionMode": "tenant-only" } } }`For more information, see [Configure distributions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-working-with.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [CreateDistribution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-distribution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-field-level-encryption-config`.

- **AWS CLI**
- 
            
                    **To create a CloudFront field-level encryption configuration**The following example creates a field-level encryption configuration by providing the configuration parameters in a JSON file named `fle-config.json`. Before you can create a field-level encryption configuration, you must have a field-level encryption profile. To create a profile, see the create-field-level-encryption-profile command.For more information about CloudFront field-level encryption, see [Using Field-Level Encryption to Help Protect Sensitive Data](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html)in the*Amazon CloudFront Developer Guide*.`aws cloudfront create-field-level-encryption-config \ --field-level-encryption-config``file://fle-config.json`The file `fle-config.json`is a JSON document in the current folder that contains the following:`{ "CallerReference": "cli-example", "Comment": "Example FLE configuration", "QueryArgProfileConfig": { "ForwardWhenQueryArgProfileIsUnknown": true, "QueryArgProfiles": { "Quantity": 0 } }, "ContentTypeProfileConfig": { "ForwardWhenContentTypeIsUnknown": true, "ContentTypeProfiles": { "Quantity": 1, "Items": [ { "Format": "URLEncoded", "ProfileId": "P280MFCLSYOCVU", "ContentType": "application/x-www-form-urlencoded" } ] } } }`Output: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/field-level-encryption/C3KM2WVD605UAY", "ETag": "E2P4Z4VU7TY5SG", "FieldLevelEncryption": { "Id": "C3KM2WVD605UAY", "LastModifiedTime": "2019-12-10T21:30:18.974Z", "FieldLevelEncryptionConfig": { "CallerReference": "cli-example", "Comment": "Example FLE configuration", "QueryArgProfileConfig": { "ForwardWhenQueryArgProfileIsUnknown": true, "QueryArgProfiles": { "Quantity": 0, "Items": [] } }, "ContentTypeProfileConfig": { "ForwardWhenContentTypeIsUnknown": true, "ContentTypeProfiles": { "Quantity": 1, "Items": [ { "Format": "URLEncoded", "ProfileId": "P280MFCLSYOCVU", "ContentType": "application/x-www-form-urlencoded" } ] } } } } }`- 
                    For API details, see [CreateFieldLevelEncryptionConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-field-level-encryption-profile`.

- **AWS CLI**
- 
            
                    **To create a CloudFront field-level encryption profile**The following example creates a field-level encryption profile by providing the parameters in a JSON file named `fle-profile-config.json`. Before you can create a field-level encryption profile, you must have a CloudFront public key. To create a CloudFront public key, see the create-public-key command.For more information about CloudFront field-level encryption, see [Using Field-Level Encryption to Help Protect Sensitive Data](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html)in the*Amazon CloudFront Developer Guide*.`aws cloudfront create-field-level-encryption-profile \ --field-level-encryption-profile-config``file://fle-profile-config.json`The file `fle-profile-config.json`is a JSON document in the current folder that contains the following:`{ "Name": "ExampleFLEProfile", "CallerReference": "cli-example", "Comment": "FLE profile for AWS CLI example", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2K8NC4HVFE3M0", "ProviderId": "ExampleFLEProvider", "FieldPatterns": { "Quantity": 1, "Items": [ "ExampleSensitiveField" ] } } ] } }`Output: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/field-level-encryption-profile/PPK0UOSIF5WSV", "ETag": "E2QWRUHEXAMPLE", "FieldLevelEncryptionProfile": { "Id": "PPK0UOSIF5WSV", "LastModifiedTime": "2019-12-10T01:03:16.537Z", "FieldLevelEncryptionProfileConfig": { "Name": "ExampleFLEProfile", "CallerReference": "cli-example", "Comment": "FLE profile for AWS CLI example", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2K8NC4HVFE3M0", "ProviderId": "ExampleFLEProvider", "FieldPatterns": { "Quantity": 1, "Items": [ "ExampleSensitiveField" ] } } ] } } } }`- 
                    For API details, see [CreateFieldLevelEncryptionProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-field-level-encryption-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-invalidation-for-distribution-tenant`.

- **AWS CLI**
- 
            
                    **To create a CloudFront invalidation for a distribution tenant**The following `create-invalidation-for-distribution-tenant`example creates an invalidation for all files in a CloudFront distribution tenant.`aws cloudfront create-invalidation-for-distribution-tenant \ --id``dt_2wjDZi3hD1ivOXf6rpZJO1AB`\ --invalidation-batch '`{"Paths": {"Quantity": 1, "Items": ["/*"]}, "CallerReference": "invalidation-$(date +%s)"}`'Output: `{ "Location": "https://cloudfront.amazonaws.com/2020-05-31/distribution-tenant/dt_2wjDZi3hD1ivOXf6rpZJO1AB/invalidation/I2JGL2F1ZAA426PGG0YLLKABC", "Invalidation": { "Id": "I2JGL2F1ZAA426PGG0YLLKABC", "Status": "InProgress", "CreateTime": "2025-05-07T16:59:25.947000+00:00", "InvalidationBatch": { "Paths": { "Quantity": 1, "Items": [ "/*" ] }, "CallerReference": "invalidation-$(date +%s)" } } }`For more information, see [Invalidate files to remove content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [CreateInvalidationForDistributionTenant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-invalidation-for-distribution-tenant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-invalidation`.

- **AWS CLI**
- 
            
                    **To create an invalidation for a CloudFront distribution**The following `create-invalidation`example creates an invalidation for the specified files in the specified CloudFront distribution:`aws cloudfront create-invalidation \ --distribution-id``EDFDVBD6EXAMPLE`\ --paths`"/example-path/example-file.jpg"``"/example-path/example-file2.png"`Output: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/distribution/EDFDVBD6EXAMPLE/invalidation/I1JLWSDAP8FU89", "Invalidation": { "Id": "I1JLWSDAP8FU89", "Status": "InProgress", "CreateTime": "2019-12-05T18:24:51.407Z", "InvalidationBatch": { "Paths": { "Quantity": 2, "Items": [ "/example-path/example-file2.png", "/example-path/example-file.jpg" ] }, "CallerReference": "cli-1575570291-670203" } } }`In the previous example, the AWS CLI automatically generated a random `CallerReference`. To specify your own`CallerReference`, or to avoid passing the invalidation parameters as command line arguments, you can use a JSON file. The following example creates an invalidation for two files, by providing the invalidation parameters in a JSON file named`inv-batch.json`:`aws cloudfront create-invalidation \ --distribution-id``EDFDVBD6EXAMPLE`\ --invalidation-batch`file://inv-batch.json`Contents of `inv-batch.json`:`{ "Paths": { "Quantity": 2, "Items": [ "/example-path/example-file.jpg", "/example-path/example-file2.png" ] }, "CallerReference": "cli-example" }`Output: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/distribution/EDFDVBD6EXAMPLE/invalidation/I2J0I21PCUYOIK", "Invalidation": { "Id": "I2J0I21PCUYOIK", "Status": "InProgress", "CreateTime": "2019-12-05T18:40:49.413Z", "InvalidationBatch": { "Paths": { "Quantity": 2, "Items": [ "/example-path/example-file.jpg", "/example-path/example-file2.png" ] }, "CallerReference": "cli-example" } } }`- 
                    For API details, see [CreateInvalidation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-invalidation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-public-key`.

- **AWS CLI**
- 
            
                    **To create a CloudFront public key**The following example creates a CloudFront public key by providing the parameters in a JSON file named `pub-key-config.json`. Before you can use this command, you must have a PEM-encoded public key. For more information, see[Create an RSA Key Pair](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.html#field-level-encryption-setting-up-step1)in the*Amazon CloudFront Developer Guide*.`aws cloudfront create-public-key \ --public-key-config``file://pub-key-config.json`The file `pub-key-config.json`is a JSON document in the current folder that contains the following. Note that the public key is encoded in PEM format.`{ "CallerReference": "cli-example", "Name": "ExampleKey", "EncodedKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxPMbCA2Ks0lnd7IR+3pw\nwd3H/7jPGwj8bLUmore7bX+oeGpZ6QmLAe/1UOWcmZX2u70dYcSIzB1ofZtcn4cJ\nenHBAzO3ohBY/L1tQGJfS2A+omnN6H16VZE1JCK8XSJyfze7MDLcUyHZETdxuvRb\nA9X343/vMAuQPnhinFJ8Wdy8YBXSPpy7r95ylUQd9LfYTBzVZYG2tSesplcOkjM3\n2Uu+oMWxQAw1NINnSLPinMVsutJy6ZqlV3McWNWe4T+STGtWhrPNqJEn45sIcCx4\nq+kGZ2NQ0FyIyT2eiLKOX5Rgb/a36E/aMk4VoDsaenBQgG7WLTnstb9sr7MIhS6A\nrwIDAQAB\n-----END PUBLIC KEY-----\n", "Comment": "example public key" }`Output: `{ "Location": "https://cloudfront.amazonaws.com/2019-03-26/public-key/KDFB19YGCR002", "ETag": "E2QWRUHEXAMPLE", "PublicKey": { "Id": "KDFB19YGCR002", "CreatedTime": "2019-12-05T18:51:43.781Z", "PublicKeyConfig": { "CallerReference": "cli-example", "Name": "ExampleKey", "EncodedKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxPMbCA2Ks0lnd7IR+3pw\nwd3H/7jPGwj8bLUmore7bX+oeGpZ6QmLAe/1UOWcmZX2u70dYcSIzB1ofZtcn4cJ\nenHBAzO3ohBY/L1tQGJfS2A+omnN6H16VZE1JCK8XSJyfze7MDLcUyHZETdxuvRb\nA9X343/vMAuQPnhinFJ8Wdy8YBXSPpy7r95ylUQd9LfYTBzVZYG2tSesplcOkjM3\n2Uu+oMWxQAw1NINnSLPinMVsutJy6ZqlV3McWNWe4T+STGtWhrPNqJEn45sIcCx4\nq+kGZ2NQ0FyIyT2eiLKOX5Rgb/a36E/aMk4VoDsaenBQgG7WLTnstb9sr7MIhS6A\nrwIDAQAB\n-----END PUBLIC KEY-----\n", "Comment": "example public key" } } }`- 
                    For API details, see [CreatePublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cloud-front-origin-access-identity`.

- **AWS CLI**
- 
            
                    **To delete a CloudFront origin access identity**The following example deletes the origin access identity (OAI) with the ID `E74FTE3AEXAMPLE`. To delete an OAI, you must have the OAI's ID and`ETag`. The OAI ID is returned in the output of the create-cloud-front-origin-access-identity and list-cloud-front-origin-access-identities commands. To get the`ETag`, use the get-cloud-front-origin-access-identity or get-cloud-front-origin-access-identity-config command. Use the`--if-match`option to provide the OAI's`ETag`.`aws cloudfront delete-cloud-front-origin-access-identity \ --id``E74FTE3AEXAMPLE`\ --if-match`E2QWRUHEXAMPLE`When successful, this command has no output. - 
                    For API details, see [DeleteCloudFrontOriginAccessIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-cloud-front-origin-access-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-connection-group`.

- **AWS CLI**
- 
            
                    **To delete a connection group**The following `delete-connection-group`example deletes a connection group. The connection group must be disabled and can't be associated with any CloudFront resources.`aws cloudfront delete-connection-group \ --id``cg_2wjLpjbHkLUdhWAjHllcOeABC`\ --if-match`ETVPDKIKX0DABC`When successful, this command has no output. For more information about managing connection groups, see [Create custom connection group (optional)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [DeleteConnectionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-connection-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-distribution-tenant`.

- **AWS CLI**
- 
            
                    **To delete a distribution tenant**The following `delete-distribution-tenant`example deletes a distribution tenant with ETag`ETVPDKIKX0DABC`. The distribution tenant must be disabled and can't be associated with any CloudFront resources.`aws cloudfront delete-distribution-tenant \ --id``dt_2wjMUbg3NHZEQ7OfoalP5zi1AB`\ --if-match`ETVPDKIKX0DABC`When successful, this command has no output. For more information, see [Delete a distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [DeleteDistributionTenant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-distribution-tenant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-distribution`.

- **AWS CLI**
- 
            
                    **To delete a CloudFront distribution**The following example deletes the CloudFront distribution with the ID `EDFDVBD6EXAMPLE`. Before you can delete a distribution, you must disable it. To disable a distribution, use the update-distribution command. For more information, see the update-distribution examples.When a distribution is disabled, you can delete it. To delete a distribution, you must use the `--if-match`option to provide the distribution's`ETag`. To get the`ETag`, use the get-distribution or get-distribution-config command.`aws cloudfront delete-distribution \ --id``EDFDVBD6EXAMPLE`\ --if-match`E2QWRUHEXAMPLE`When successful, this command has no output. - 
                    For API details, see [DeleteDistribution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-distribution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-field-level-encryption-config`.

- **AWS CLI**
- 
            
                    **To delete a CloudFront field-level encryption configuration**The following example deletes the CloudFront field-level encryption configuration with the ID `C3KM2WVD605UAY`. To delete a field-level encryption configuration, you must have its ID and`ETag`. The ID is returned in the output of the create-field-level-encryption-config and list-field-level-encryption-configs commands. To get the`ETag`, use the get-field-level-encryption or get-field-level-encryption-config command. Use the`--if-match`option to provide the configuration's`ETag`.`aws cloudfront delete-field-level-encryption-config \ --id``C3KM2WVD605UAY`\ --if-match`E26M4BIAV81ZF6`When successful, this command has no output. - 
                    For API details, see [DeleteFieldLevelEncryptionConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-field-level-encryption-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-field-level-encryption-profile`.

- **AWS CLI**
- 
            
                    **To delete a CloudFront field-level encryption profile**The following example deletes the CloudFront field-level encryption profile with the ID `PPK0UOSIF5WSV`. To delete a field-level encryption profile, you must have its ID and`ETag`. The ID is returned in the output of the create-field-level-encryption-profile and list-field-level-encryption-profiles commands. To get the`ETag`, use the get-field-level-encryption-profile or get-field-level-encryption-profile-config command. Use the`--if-match`option to provide the profile's`ETag`.`aws cloudfront delete-field-level-encryption-profile \ --id``PPK0UOSIF5WSV`\ --if-match`EJETYFJ9CL66D`When successful, this command has no output. - 
                    For API details, see [DeleteFieldLevelEncryptionProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-field-level-encryption-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-public-key`.

- **AWS CLI**
- 
            
                    **To delete a CloudFront public key**The following example deletes the CloudFront public key with the ID `KDFB19YGCR002`. To delete a public key, you must have its ID and`ETag`. The ID is returned in the output of the create-public-key and list-public-keys commands. To get the`ETag`, use the get-public-key or get-public-key-config command. Use the`--if-match`option to provide the public key's`ETag`.`aws cloudfront delete-public-key \ --id``KDFB19YGCR002`\ --if-match`E2QWRUHEXAMPLE`When successful, this command has no output. - 
                    For API details, see [DeletePublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/delete-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-distribution-tenant-web-acl`.

- **AWS CLI**
- 
            
                    **To disassociate a web ACL from a distribution tenant**The following `disassociate-distribution-tenant-web-acl`example disassociates a web ACL from a distribution tenant with ETag`E1PA6795UKMABC`.`aws cloudfront disassociate-distribution-tenant-web-acl \ --id``dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB`\ --if-match`E1PA6795UKMABC`Output: `{ "ETag": "E13V1IB3VIYABC", "Id": "dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB" }`For more information, see [Disable AWS WAF security protections](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/disable-waf.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [DisassociateDistributionTenantWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/disassociate-distribution-tenant-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-distribution-web-acl`.

- **AWS CLI**
- 
            
                    **To disassociate a web ACL from a CloudFront distribution**The following `disassociate-distribution-web-acl`example removes the association between a web ACL and a CloudFront distribution with ETag`E13V1IB3VIYABC`.`aws cloudfront disassociate-distribution-web-acl \ --id``E1XNX8R2GOAABC`\ --if-match`EEZQ9Z24VM1ABC`Output: `{ "ETag": "E2YWS1C2J3OABC", "Id": "E1XNX8R2GOAABC" }`For more information, see [Disable AWS WAF security protections](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/disable-waf.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [DisassociateDistributionWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/disassociate-distribution-web-acl.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-cloud-front-origin-access-identity-config`.

- **AWS CLI**
- 
            
                    **To get a CloudFront origin access identity configuration**The following example gets metadata about the CloudFront origin access identity (OAI) with the ID `E74FTE3AEXAMPLE`, including its`ETag`. The OAI ID is returned in the output of the create-cloud-front-origin-access-identity and list-cloud-front-origin-access-identities commands.`aws cloudfront get-cloud-front-origin-access-identity-config --id``E74FTE3AEXAMPLE`Output: `{ "ETag": "E2QWRUHEXAMPLE", "CloudFrontOriginAccessIdentityConfig": { "CallerReference": "cli-example", "Comment": "Example OAI" } }`- 
                    For API details, see [GetCloudFrontOriginAccessIdentityConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-cloud-front-origin-access-identity`.

- **AWS CLI**
- 
            
                    **To get a CloudFront origin access identity**The following example gets the CloudFront origin access identity (OAI) with the ID `E74FTE3AEXAMPLE`, including its`ETag`and the associated S3 canonical ID. The OAI ID is returned in the output of the create-cloud-front-origin-access-identity and list-cloud-front-origin-access-identities commands.`aws cloudfront get-cloud-front-origin-access-identity --id``E74FTE3AEXAMPLE`Output: `{ "ETag": "E2QWRUHEXAMPLE", "CloudFrontOriginAccessIdentity": { "Id": "E74FTE3AEXAMPLE", "S3CanonicalUserId": "cd13868f797c227fbea2830611a26fe0a21ba1b826ab4bed9b7771c9aEXAMPLE", "CloudFrontOriginAccessIdentityConfig": { "CallerReference": "cli-example", "Comment": "Example OAI" } } }`- 
                    For API details, see [GetCloudFrontOriginAccessIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-cloud-front-origin-access-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-connection-group-by-routing-endpoint`.

- **AWS CLI**
- 
            
                    **To get a connection group by routing endpoint**The following `get-connection-group-by-routing-endpoint`example retrieves information about a connection group using its routing endpoint.`aws cloudfront get-connection-group-by-routing-endpoint \ --routing-endpoint``dvdg9gprgabc.cloudfront.net`Output: `{ "ETag": "E23ZP02F085ABC", "ConnectionGroup": { "Id": "cg_2wjDWTBKTlRB87cAaUQFaakABC", "Name": "connection-group-2", "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_2wjDWTBKTlRB87cAaUQFaakABC", "CreatedTime": "2025-05-06T15:42:00.790000+00:00", "LastModifiedTime": "2025-05-06T15:42:00.790000+00:00", "Ipv6Enabled": true, "RoutingEndpoint": "dvdg9gprgabc.cloudfront.net", "Status": "Deployed", "Enabled": true, "IsDefault": false } }`For more information, see [Create custom connection group (optional)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [GetConnectionGroupByRoutingEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-connection-group-by-routing-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-connection-group`.

- **AWS CLI**
- 
            
                    **To get a CloudFront connection group**The following `get-connection-group`example retrieves information about a CloudFront connection group.`aws cloudfront get-connection-group \ --identifier``cg_2wjDWTBKTlRB87cAaUQFaakABC`Output: `{ "ETag": "E23ZP02F085ABC", "ConnectionGroup": { "Id": "cg_2wjDWTBKTlRB87cAaUQFaakABC", "Name": "connection-group-2", "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_2wjDWTBKTlRB87cAaUQFaakABC", "CreatedTime": "2025-05-06T15:42:00.790000+00:00", "LastModifiedTime": "2025-05-06T15:42:00.790000+00:00", "Ipv6Enabled": true, "RoutingEndpoint": "dvdg9gprgabc.cloudfront.net", "Status": "Deployed", "Enabled": true, "IsDefault": false } }`For more information, see [Create custom connection group (optional)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [GetConnectionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-connection-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-distribution-config`.

- **AWS CLI**
- 
            
                    **To get a CloudFront distribution configuration**The following example gets metadata about the CloudFront distribution with the ID `EDFDVBD6EXAMPLE`, including its`ETag`. The distribution ID is returned in the create-distribution and list-distributions commands.`aws cloudfront get-distribution-config \ --id``EDFDVBD6EXAMPLE`Output: `{ "ETag": "E2QWRUHEXAMPLE", "DistributionConfig": { "CallerReference": "cli-example", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true } }`- 
                    For API details, see [GetDistributionConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-distribution-tenant-by-domain`.

- **AWS CLI**
- 
            
                    **To get distribution tenant information by domain**The following `get-distribution-tenant-by-domain`example retrieves information about a distribution tenant using the specified domain.`aws cloudfront get-distribution-tenant-by-domain \ --domain``example.com`Output: `{ "ETag": "E23ZP02F085ABC", "DistributionTenant": { "Id": "dt_2xVInRKCfUzQHgxosDs9hiLk1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "example-tenant-4", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2xVInRKCfUzQHgxosDs9hiLk1AB", "Domains": [ { "Domain": "example.com", "Status": "active" } ], "Parameters": [ { "Name": "testParam", "Value": "defaultValue" } ], "ConnectionGroupId": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "CreatedTime": "2025-05-23T16:16:20.871000+00:00", "LastModifiedTime": "2025-05-23T16:16:20.871000+00:00", "Enabled": false, "Status": "Deployed" } }`For more information, see [Understand how multi-tenant distributions work](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [GetDistributionTenantByDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution-tenant-by-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-distribution-tenant`.

- **AWS CLI**
- 
            
                    **To get details about a CloudFront distribution tenant**The following `get-distribution-tenant`example retrieves information about a CloudFront distribution tenant.`aws cloudfront get-distribution-tenant \ --id``dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB`Output: `{ "ETag": "E23ZP02F085ABC", "DistributionTenant": { "Id": "dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "example-tenant-2", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB", "Domains": [ { "Domain": "example.com", "Status": "inactive" } ], "ConnectionGroupId": "cg_2wjDWTBKTlRB87cAaUQFaakABC", "CreatedTime": "2025-05-06T15:42:28.542000+00:00", "LastModifiedTime": "2025-05-06T15:42:37.724000+00:00", "Enabled": true, "Status": "InProgress" } }`For more information, see [Understand how multi-tenant distributions work](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [GetDistributionTenant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution-tenant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-distribution`.

- **AWS CLI**
- 
            
                    **To get a CloudFront distribution**The following `get-distribution`example gets the CloudFront distribution with the ID`EDFDVBD6EXAMPLE`, including its`ETag`. The distribution ID is returned in the create-distribution and list-distributions commands.`aws cloudfront get-distribution \ --id``EDFDVBD6EXAMPLE`Output: `{ "ETag": "E2QWRUHEXAMPLE", "Distribution": { "Id": "EDFDVBD6EXAMPLE", "ARN": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE", "Status": "Deployed", "LastModifiedTime": "2019-12-04T23:35:41.433Z", "InProgressInvalidationBatches": 0, "DomainName": "d111111abcdef8.cloudfront.net", "ActiveTrustedSigners": { "Enabled": false, "Quantity": 0 }, "DistributionConfig": { "CallerReference": "cli-example", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-cli-example", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true } } }`- 
                    For API details, see [GetDistribution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-distribution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-field-level-encryption-config`.

- **AWS CLI**
- 
            
                    **To get metadata about a CloudFront field-level encryption configuration**The following example gets metadata about the CloudFront field-level encryption configuration with the ID `C3KM2WVD605UAY`, including its`ETag`:`aws cloudfront get-field-level-encryption-config --id``C3KM2WVD605UAY`Output: `{ "ETag": "E2P4Z4VU7TY5SG", "FieldLevelEncryptionConfig": { "CallerReference": "cli-example", "Comment": "Example FLE configuration", "QueryArgProfileConfig": { "ForwardWhenQueryArgProfileIsUnknown": true, "QueryArgProfiles": { "Quantity": 0, "Items": [] } }, "ContentTypeProfileConfig": { "ForwardWhenContentTypeIsUnknown": true, "ContentTypeProfiles": { "Quantity": 1, "Items": [ { "Format": "URLEncoded", "ProfileId": "P280MFCLSYOCVU", "ContentType": "application/x-www-form-urlencoded" } ] } } } }`- 
                    For API details, see [GetFieldLevelEncryptionConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-field-level-encryption-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-field-level-encryption-profile-config`.

- **AWS CLI**
- 
            
                    **To get a CloudFront field-level encryption profile configuration**The following example gets metadata about the CloudFront field-level encryption profile with ID `PPK0UOSIF5WSV`, including its`ETag`:`aws cloudfront get-field-level-encryption-profile-config --id``PPK0UOSIF5WSV`Output: `{ "ETag": "E1QQG65FS2L2GC", "FieldLevelEncryptionProfileConfig": { "Name": "ExampleFLEProfile", "CallerReference": "cli-example", "Comment": "FLE profile for AWS CLI example", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2K8NC4HVFE3M0", "ProviderId": "ExampleFLEProvider", "FieldPatterns": { "Quantity": 1, "Items": [ "ExampleSensitiveField" ] } } ] } } }`- 
                    For API details, see [GetFieldLevelEncryptionProfileConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-field-level-encryption-profile-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-field-level-encryption-profile`.

- **AWS CLI**
- 
            
                    **To get a CloudFront field-level encryption profile**The following example gets the CloudFront field-level encryption profile with ID `PPK0UOSIF5WSV`, including its`ETag`:`aws cloudfront get-field-level-encryption-profile --id``PPK0UOSIF5WSV`Output: `{ "ETag": "E1QQG65FS2L2GC", "FieldLevelEncryptionProfile": { "Id": "PPK0UOSIF5WSV", "LastModifiedTime": "2019-12-10T01:03:16.537Z", "FieldLevelEncryptionProfileConfig": { "Name": "ExampleFLEProfile", "CallerReference": "cli-example", "Comment": "FLE profile for AWS CLI example", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2K8NC4HVFE3M0", "ProviderId": "ExampleFLEProvider", "FieldPatterns": { "Quantity": 1, "Items": [ "ExampleSensitiveField" ] } } ] } } } }`- 
                    For API details, see [GetFieldLevelEncryptionProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-field-level-encryption-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-field-level-encryption`.

- **AWS CLI**
- 
            
                    **To get a CloudFront field-level encryption configuration**The following example gets the CloudFront field-level encryption configuration with the ID `C3KM2WVD605UAY`, including its`ETag`:`aws cloudfront get-field-level-encryption --id``C3KM2WVD605UAY`Output: `{ "ETag": "E2P4Z4VU7TY5SG", "FieldLevelEncryption": { "Id": "C3KM2WVD605UAY", "LastModifiedTime": "2019-12-10T21:30:18.974Z", "FieldLevelEncryptionConfig": { "CallerReference": "cli-example", "Comment": "Example FLE configuration", "QueryArgProfileConfig": { "ForwardWhenQueryArgProfileIsUnknown": true, "QueryArgProfiles": { "Quantity": 0, "Items": [] } }, "ContentTypeProfileConfig": { "ForwardWhenContentTypeIsUnknown": true, "ContentTypeProfiles": { "Quantity": 1, "Items": [ { "Format": "URLEncoded", "ProfileId": "P280MFCLSYOCVU", "ContentType": "application/x-www-form-urlencoded" } ] } } } } }`- 
                    For API details, see [GetFieldLevelEncryption](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-field-level-encryption.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-invalidation-for-distribution-tenant`.

- **AWS CLI**
- 
            
                    **To get an invalidation for a distribution tenant**The following `get-invalidation-for-distribution-tenant`example gets information about an invalidation for a distribution tenant.`aws cloudfront get-invalidation-for-distribution-tenant \ --distribution-tenant-id``dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB`\ --id`I4CU23QAPKMUDUU06F9OFGFABC`Output: `{ "Invalidation": { "Id": "I4CU23QAPKMUDUU06F9OFGFABC", "Status": "Completed", "CreateTime": "2025-05-06T15:46:12.824000+00:00", "InvalidationBatch": { "Paths": { "Quantity": 2, "Items": [ "/example/invalidation", "/more/invalidations" ] }, "CallerReference": "007ee5a6-d0a0-42be-bb61-e7b915969b48" } } }`For more information, see [Invalidate files to remove content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [GetInvalidationForDistributionTenant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-invalidation-for-distribution-tenant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-invalidation`.

- **AWS CLI**
- 
            
                    **To get a CloudFront invalidation**The following example gets the invalidation with the ID `I2J0I21PCUYOIK`for the CloudFront distribution with the ID`EDFDVBD6EXAMPLE`:`aws cloudfront get-invalidation --id``I2J0I21PCUYOIK`--distribution-id`EDFDVBD6EXAMPLE`Output: `{ "Invalidation": { "Status": "Completed", "InvalidationBatch": { "Paths": { "Items": [ "/example-path/example-file.jpg", "/example-path/example-file-2.jpg" ], "Quantity": 2 }, "CallerReference": "cli-example" }, "Id": "I2J0I21PCUYOIK", "CreateTime": "2019-12-05T18:40:49.413Z" } }`- 
                    For API details, see [GetInvalidation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-invalidation.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-managed-certificate-details`.

- **AWS CLI**
- 
            
                    **To get managed certificate details**The following `get-managed-certificate-details`example retrieves the details of a CloudFront managed ACM certificate.`aws cloudfront get-managed-certificate-details \ --identifier``dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB`Output: `{ "ManagedCertificateDetails": { "CertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/655dc1fe-6d37-451d-a013-c2db3a034abc", "CertificateStatus": "pending-validation", "ValidationTokenHost": "self-hosted", "ValidationTokenDetails": [ { "Domain": "example.com", "RedirectTo": "validation.us-east-1.acm-validations.aws/123456789012/.well-known/pki-validation/b315c9ae21284e7918bb9f3f422ab1c7.txt", "RedirectFrom": "example.com/.well-known/pki-validation/b315c9ae21284e7918bb9f3f422ac3c7.txt" } ] } }`For more information, see [Request certificates for your CloudFront distribution tenant](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/managed-cloudfront-certificates.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [GetManagedCertificateDetails](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-managed-certificate-details.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-public-key-config`.

- **AWS CLI**
- 
            
                    **To get a CloudFront public key configuration**The following example gets metadata about the CloudFront public key with the ID `KDFB19YGCR002`, including its`ETag`. The public key ID is returned in the create-public-key and list-public-keys commands.`aws cloudfront get-public-key-config --id``KDFB19YGCR002`Output: `{ "ETag": "E2QWRUHEXAMPLE", "PublicKeyConfig": { "CallerReference": "cli-example", "Name": "ExampleKey", "EncodedKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxPMbCA2Ks0lnd7IR+3pw\nwd3H/7jPGwj8bLUmore7bX+oeGpZ6QmLAe/1UOWcmZX2u70dYcSIzB1ofZtcn4cJ\nenHBAzO3ohBY/L1tQGJfS2A+omnN6H16VZE1JCK8XSJyfze7MDLcUyHZETdxuvRb\nA9X343/vMAuQPnhinFJ8Wdy8YBXSPpy7r95ylUQd9LfYTBzVZYG2tSesplcOkjM3\n2Uu+oMWxQAw1NINnSLPinMVsutJy6ZqlV3McWNWe4T+STGtWhrPNqJEn45sIcCx4\nq+kGZ2NQ0FyIyT2eiLKOX5Rgb/a36E/aMk4VoDsaenBQgG7WLTnstb9sr7MIhS6A\nrwIDAQAB\n-----END PUBLIC KEY-----\n", "Comment": "example public key" } }`- 
                    For API details, see [GetPublicKeyConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-public-key-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-public-key`.

- **AWS CLI**
- 
            
                    **To get a CloudFront public key**The following example gets the CloudFront public key with the ID `KDFB19YGCR002`, including its`ETag`. The public key ID is returned in the create-public-key and list-public-keys commands.`aws cloudfront get-public-key --id``KDFB19YGCR002`Output: `{ "ETag": "E2QWRUHEXAMPLE", "PublicKey": { "Id": "KDFB19YGCR002", "CreatedTime": "2019-12-05T18:51:43.781Z", "PublicKeyConfig": { "CallerReference": "cli-example", "Name": "ExampleKey", "EncodedKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxPMbCA2Ks0lnd7IR+3pw\nwd3H/7jPGwj8bLUmore7bX+oeGpZ6QmLAe/1UOWcmZX2u70dYcSIzB1ofZtcn4cJ\nenHBAzO3ohBY/L1tQGJfS2A+omnN6H16VZE1JCK8XSJyfze7MDLcUyHZETdxuvRb\nA9X343/vMAuQPnhinFJ8Wdy8YBXSPpy7r95ylUQd9LfYTBzVZYG2tSesplcOkjM3\n2Uu+oMWxQAw1NINnSLPinMVsutJy6ZqlV3McWNWe4T+STGtWhrPNqJEn45sIcCx4\nq+kGZ2NQ0FyIyT2eiLKOX5Rgb/a36E/aMk4VoDsaenBQgG7WLTnstb9sr7MIhS6A\nrwIDAQAB\n-----END PUBLIC KEY-----\n", "Comment": "example public key" } } }`- 
                    For API details, see [GetPublicKey](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-public-key.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-cloud-front-origin-access-identities`.

- **AWS CLI**
- 
            
                    **To list CloudFront origin access identities**The following example gets a list of the CloudFront origin access identities (OAIs) in your AWS account: `aws cloudfront list-cloud-front-origin-access-identities`Output: `{ "CloudFrontOriginAccessIdentityList": { "Items": [ { "Id": "E74FTE3AEXAMPLE", "S3CanonicalUserId": "cd13868f797c227fbea2830611a26fe0a21ba1b826ab4bed9b7771c9aEXAMPLE", "Comment": "Example OAI" }, { "Id": "EH1HDMBEXAMPLE", "S3CanonicalUserId": "1489f6f2e6faacaae7ff64c4c3e6956c24f78788abfc1718c3527c263bf7a17EXAMPLE", "Comment": "Test OAI" }, { "Id": "E2X2C9TEXAMPLE", "S3CanonicalUserId": "cbfeebb915a64749f9be546a45b3fcfd3a31c779673c13c4dd460911ae402c2EXAMPLE", "Comment": "Example OAI #2" } ] } }`- 
                    For API details, see [ListCloudFrontOriginAccessIdentities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-cloud-front-origin-access-identities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-connection-groups`.

- **AWS CLI**
- 
            
                    **To list connection groups**The following `list-connection-groups`example lists the available connection groups in your AWS account.`aws cloudfront list-connection-groups`Output: `{ "ConnectionGroups": [ { "Id": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "Name": "CreatedByCloudFront-cg_2whCJoXMYCjHcxaLGrkllvyABC", "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_2whCJoXMYCjHcxaLGrkllvyABC", "RoutingEndpoint": "d3sx0pso7m5abc.cloudfront.net", "CreatedTime": "2025-05-05T22:32:29.630000+00:00", "LastModifiedTime": "2025-05-05T22:32:29.630000+00:00", "ETag": "E23ZP02F085ABC", "Enabled": true, "Status": "Deployed", "IsDefault": true }, { "Id": "cg_2wjDWTBKTlRB87cAaUQFaakABC", "Name": "connection-group-2", "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_2wjDWTBKTlRB87cAaUQFaakABC", "RoutingEndpoint": "dvdg9gprgabc.cloudfront.net", "CreatedTime": "2025-05-06T15:42:00.790000+00:00", "LastModifiedTime": "2025-05-06T15:42:00.790000+00:00", "ETag": "E23ZP02F085ABC", "Enabled": true, "Status": "Deployed", "IsDefault": false } ] }`For more information, see [Create custom connection group (optional)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [ListConnectionGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-connection-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-distribution-tenants-by-customization`.

- **AWS CLI**
- 
            
                    **To list distribution tenants by customization**The following `list-distribution-tenants-by-customization`example lists distribution tenants that use the specified web ACL.`aws cloudfront list-distribution-tenants-by-customization \ --web-acl-arn``arn:aws:wafv2:us-east-1:123456789012:global/webacl/CreatedByCloudFront-0273cd2f/a3c19bce-42b5-48a1-a8d4-b2bb2f28eabc`Output: `{ "DistributionTenantList": [ { "Id": "dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "example-tenant-2", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB", "Domains": [ { "Domain": "example.com", "Status": "inactive" } ], "ConnectionGroupId": "cg_2wjDWTBKTlRB87cAaUQFaakABC", "Customizations": { "WebAcl": { "Action": "override", "Arn": "arn:aws:wafv2:us-east-1:123456789012:global/webacl/CreatedByCloudFront-0273cd2f/a3c19bce-42b5-48a1-a8d4-b2bb2f28eabc" }, "GeoRestrictions": { "RestrictionType": "whitelist", "Locations": [ "AL" ] } }, "CreatedTime": "2025-05-06T15:42:28.542000+00:00", "LastModifiedTime": "2025-05-06T16:14:08.710000+00:00", "ETag": "E1F83G8C2ARABC", "Enabled": true, "Status": "Deployed" } ] }`For more information, see [Distribution tenant customizations](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tenant-customization.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [ListDistributionTenantsByCustomization](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distribution-tenants-by-customization.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-distribution-tenants`.

- **AWS CLI**
- 
            
                    **To list CloudFront distribution tenants**The following `list-distribution-tenants`example lists 3 CloudFront distribution tenants in your AWS account by the associated connection group.`aws cloudfront list-distribution-tenants \ --association-filter``ConnectionGroupId=cg_2whCJoXMYCjHcxaLGrkllvyABC`\ --max-items`3`Output: `{ "DistributionTenantList": [ { "Id": "dt_2yMvQgam3QkJo2z54FDl91dk1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "new-tenant-customizations", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2yMvQgam3QkJo2z54FDl91dk1AB", "Domains": [ { "Domain": "example.com", "Status": "active" } ], "ConnectionGroupId": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "Customizations": { "WebAcl": { "Action": "disable" }, "GeoRestrictions": { "RestrictionType": "whitelist", "Locations": [ "DE" ] } }, "CreatedTime": "2025-06-11T15:54:02.142000+00:00", "LastModifiedTime": "2025-06-11T15:54:02.142000+00:00", "ETag": "E23ZP02F085ABC", "Enabled": false, "Status": "Deployed" }, { "Id": "dt_2yMuV7NJuBcAB0cwwxMCBZQ1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "new-tenant", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2yMuV7NJuBcAB0cwwxMCBZQ1AB", "Domains": [ { "Domain": "1.example.com", "Status": "active" } ], "ConnectionGroupId": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "Customizations": { "GeoRestrictions": { "RestrictionType": "whitelist", "Locations": [ "DE" ] } }, "CreatedTime": "2025-06-11T15:46:23.466000+00:00", "LastModifiedTime": "2025-06-11T15:46:23.466000+00:00", "ETag": "E23ZP02F085ABC", "Enabled": false, "Status": "Deployed" }, { "Id": "dt_2xVInRKCfUzQHgxosDs9hiLk1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "new-tenant-2", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2xVInRKCfUzQHgxosDs9hiLk1AB", "Domains": [ { "Domain": "2.example.com", "Status": "active" } ], "ConnectionGroupId": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "CreatedTime": "2025-05-23T16:16:20.871000+00:00", "LastModifiedTime": "2025-05-23T16:16:20.871000+00:00", "ETag": "E23ZP02F085ABC", "Enabled": false, "Status": "Deployed" } ], "NextToken": "eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAzfQ==" }`For more information, see [Understand how multi-tenant distributions work](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-config-options.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [ListDistributionTenants](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distribution-tenants.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-distributions-by-connection-mode`.

- **AWS CLI**
- 
            
                    **To list CloudFront distributions by connection mode**The following `list-distributions-by-connection-mode`example lists CloudFront distributions with the specified connection mode.`aws cloudfront list-distributions-by-connection-mode \ --connection-mode``tenant-only`Output: `{ "DistributionList": { "Items": [ { "Id": "E1XNX8R2GOAABC", "ARN": "arn:aws:cloudfront::123456789012:distribution/E1XNX8R2GOAABC", "ETag": "EPT4JPJQDY1ABC", "Status": "Deployed", "LastModifiedTime": "2025-05-23T16:16:15.691000+00:00", "DomainName": "-", "Aliases": { "Quantity": 0 }, "Origins": { "Quantity": 1, "Items": [ { "Id": "example-cfn-simple-distribution123", "DomainName": "example.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" }, "ConnectionAttempts": 3, "ConnectionTimeout": 10, "OriginShield": { "Enabled": false }, "OriginAccessControlId": "E2CJRMB5LKEABC" } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "example-cfn-simple-distribution123", "TrustedKeyGroups": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "Compress": true, "LambdaFunctionAssociations": { "Quantity": 0 }, "FunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "", "CachePolicyId": "658327ea-f89d-4fab-a63d-7e88639e5abc", "GrpcConfig": { "Enabled": false } }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": false, "ACMCertificateArn": "arn:aws:acm:us-east-1:123456789012:certificate/ec53f564-ea5a-4e4a-a0a2-e3c989449abc", "SSLSupportMethod": "sni-only", "MinimumProtocolVersion": "TLSv1.2_2021", "Certificate": "arn:aws:acm:us-east-1:123456789012:certificate/ec53f564-ea5a-4e4a-a0a2-e3c989449abc", "CertificateSource": "acm" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "arn:aws:wafv2:us-east-1:123456789012:global/webacl/web-global-example/626900da-5f64-418b-ba9b-743f3746cabc", "HttpVersion": "http2", "IsIPV6Enabled": false, "Staging": false, "ConnectionMode": "tenant-only" } ] } }`For more information, see [Create custom connection group (optional)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [ListDistributionsByConnectionMode](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distributions-by-connection-mode.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-distributions`.

- **AWS CLI**
- 
            
                    **To list CloudFront distributions**The following example gets a list of the CloudFront distributions in your AWS account. `aws cloudfront list-distributions`Output: `{ "DistributionList": { "Items": [ { "Id": "E23YS8OEXAMPLE", "ARN": "arn:aws:cloudfront::123456789012:distribution/E23YS8OEXAMPLE", "Status": "Deployed", "LastModifiedTime": "2024-08-05T18:23:40.375000+00:00", "DomainName": "abcdefgh12ijk.cloudfront.net", "Aliases": { "Quantity": 0 }, "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "DomainName": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" }, "ConnectionAttempts": 3, "ConnectionTimeout": 10, "OriginShield": { "Enabled": false }, "OriginAccessControlId": "EIAP8PEXAMPLE" } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.us-east-1.amazonaws.com", "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "TrustedKeyGroups": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "Compress": true, "LambdaFunctionAssociations": { "Quantity": 0 }, "FunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "", "CachePolicyId": "658327ea-f89d-4fab-a63d-7e886EXAMPLE" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "SSLSupportMethod": "vip", "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "HTTP2", "IsIPV6Enabled": true, "Staging": false } ] } }`- 
                    For API details, see [ListDistributions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-distributions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-domain-conflicts`.

- **AWS CLI**
- 
            
                    **To list domain conflicts for a CloudFront distribution**The following `list-domain-conflicts`example lists domain conflicts for a CloudFront distribution.`aws cloudfront list-domain-conflicts \ --domain``example.com`\ --domain-control-validation-resource`"DistributionTenantId=dt_2x9GhoK0TZRsohWzv1b9It8J1AB"`Output: `{ "DomainConflicts": [ { "Domain": "example.com", "ResourceType": "distribution-tenant", "ResourceId": "***************ohWzv1b9It8J1AB", "AccountId": "123456789012" } ] }`For more information, see [Move an alternate domain name to a different distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/alternate-domain-names-move.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [ListDomainConflicts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-domain-conflicts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-field-level-encryption-configs`.

- **AWS CLI**
- 
            
                    **To list CloudFront field-level encryption configurations**The following example gets a list of the CloudFront field-level encryption configurations in your AWS account: `aws cloudfront list-field-level-encryption-configs`Output: `{ "FieldLevelEncryptionList": { "MaxItems": 100, "Quantity": 1, "Items": [ { "Id": "C3KM2WVD605UAY", "LastModifiedTime": "2019-12-10T21:30:18.974Z", "Comment": "Example FLE configuration", "QueryArgProfileConfig": { "ForwardWhenQueryArgProfileIsUnknown": true, "QueryArgProfiles": { "Quantity": 0, "Items": [] } }, "ContentTypeProfileConfig": { "ForwardWhenContentTypeIsUnknown": true, "ContentTypeProfiles": { "Quantity": 1, "Items": [ { "Format": "URLEncoded", "ProfileId": "P280MFCLSYOCVU", "ContentType": "application/x-www-form-urlencoded" } ] } } } ] } }`- 
                    For API details, see [ListFieldLevelEncryptionConfigs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-field-level-encryption-configs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-field-level-encryption-profiles`.

- **AWS CLI**
- 
            
                    **To list CloudFront field-level encryption profiles**The following example gets a list of the CloudFront field-level encryption profiles in your AWS account: `aws cloudfront list-field-level-encryption-profiles`Output: `{ "FieldLevelEncryptionProfileList": { "MaxItems": 100, "Quantity": 2, "Items": [ { "Id": "P280MFCLSYOCVU", "LastModifiedTime": "2019-12-05T01:05:39.896Z", "Name": "ExampleFLEProfile", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2K8NC4HVFE3M0", "ProviderId": "ExampleFLEProvider", "FieldPatterns": { "Quantity": 1, "Items": [ "ExampleSensitiveField" ] } } ] }, "Comment": "FLE profile for AWS CLI example" }, { "Id": "PPK0UOSIF5WSV", "LastModifiedTime": "2019-12-10T01:03:16.537Z", "Name": "ExampleFLEProfile2", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2ABC10EXAMPLE", "ProviderId": "ExampleFLEProvider2", "FieldPatterns": { "Quantity": 1, "Items": [ "ExampleSensitiveField2" ] } } ] }, "Comment": "FLE profile #2 for AWS CLI example" } ] } }`- 
                    For API details, see [ListFieldLevelEncryptionProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-field-level-encryption-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-invalidations-for-distribution-tenant`.

- **AWS CLI**
- 
            
                    **To list invalidations for a CloudFront distribution tenant**The following `list-invalidations-for-distribution-tenant`example lists the invalidations for a CloudFront distribution tenant.`aws cloudfront list-invalidations-for-distribution-tenant \ --id``dt_2wjDZi3hD1ivOXf6rpZJOSNE1AB`Output: `{ "InvalidationList": { "Items": [ { "Id": "I4CU23QAPKMUDUU06F9OFGFABC", "CreateTime": "2025-05-06T15:46:12.824000+00:00", "Status": "Completed" } ] } }`For more information, see [Invalidate files to remove content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [ListInvalidationsForDistributionTenant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-invalidations-for-distribution-tenant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-invalidations`.

- **AWS CLI**
- 
            
                    **To list CloudFront invalidations**The following example gets a list of the invalidations for the CloudFront distribution with the ID `EDFDVBD6EXAMPLE`:`aws cloudfront list-invalidations --distribution-id``EDFDVBD6EXAMPLE`Output: `{ "InvalidationList": { "Marker": "", "Items": [ { "Status": "Completed", "Id": "YNY2LI2BVJ4NJU", "CreateTime": "2019-08-31T21:15:52.042Z" } ], "IsTruncated": false, "MaxItems": 100, "Quantity": 1 } }`- 
                    For API details, see [ListInvalidations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-invalidations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-public-keys`.

- **AWS CLI**
- 
            
                    **To list CloudFront public keys**The following example gets a list of the CloudFront public keys in your AWS account: `aws cloudfront list-public-keys`Output: `{ "PublicKeyList": { "MaxItems": 100, "Quantity": 2, "Items": [ { "Id": "K2K8NC4HVFE3M0", "Name": "ExampleKey", "CreatedTime": "2019-12-05T01:04:28.818Z", "EncodedKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxPMbCA2Ks0lnd7IR+3pw\nwd3H/7jPGwj8bLUmore7bX+oeGpZ6QmLAe/1UOWcmZX2u70dYcSIzB1ofZtcn4cJ\nenHBAzO3ohBY/L1tQGJfS2A+omnN6H16VZE1JCK8XSJyfze7MDLcUyHZETdxuvRb\nA9X343/vMAuQPnhinFJ8Wdy8YBXSPpy7r95ylUQd9LfYTBzVZYG2tSesplcOkjM3\n2Uu+oMWxQAw1NINnSLPinMVsutJy6ZqlV3McWNWe4T+STGtWhrPNqJEn45sIcCx4\nq+kGZ2NQ0FyIyT2eiLKOX5Rgb/a36E/aMk4VoDsaenBQgG7WLTnstb9sr7MIhS6A\nrwIDAQAB\n-----END PUBLIC KEY-----\n", "Comment": "example public key" }, { "Id": "K1S0LWQ2L5HTBU", "Name": "ExampleKey2", "CreatedTime": "2019-12-09T23:28:11.110Z", "EncodedKey": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApOCAg88A8+f4dujn9Izt\n26LxtgAkn2opGgo/NKpMiaisyw5qlg3f1gol7FV6pYNl78iJg3EO8JBbwtlH+cR9\nLGSf60NDeVhm76Oc39Np/vWgOdsGQcRbi9WmKZeSODqjQGzVZWqPmito3FzWVk6b\nfVY5N36U/RdbVAJm95Km+qaMYlbIdF40t72bi3IkKYV5hlB2XoDjlQ9F6ajQKyTB\nMHa3SN8q+3ZjQ4sJJ7D1V6r4wR8jDcFVD5NckWJmmgIVnkOQM37NYeoDnkaOuTpu\nha/+3b8tOb2z3LBVHPkp85zJRAOXacSwf5rZtPYKBNFsixTa2n55k2r218mOkMC4\nUwIDAQAB\n-----END PUBLIC KEY-----", "Comment": "example public key #2" } ] } }`- 
                    For API details, see [ListPublicKeys](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-public-keys.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a CloudFront distribution**The following example gets a list of the tags for a CloudFront distribution: `aws cloudfront list-tags-for-resource \ --resource``arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE`Output: `{ "Tags": { "Items": [ { "Key": "DateCreated", "Value": "2019-12-04" }, { "Key": "Name", "Value": "Example name" }, { "Key": "Project", "Value": "Example project" } ] } }`- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `sign`.

- **AWS CLI**
- 
            
                    **To sign a CloudFront URL**The following example signs a CloudFront URL. To sign a URL, you need the key pair ID (called the **Access Key ID**in the AWS Management Console) and the private key of the trusted signer's CloudFront key pair. For more information about signed URLs, see[Serving Private Content with Signed URLs and Signed Cookies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/PrivateContent.html)in the*Amazon CloudFront Developer Guide*.`aws cloudfront sign \ --url``https://d111111abcdef8.cloudfront.net/private-content/private-file.html`\ --key-pair-id`APKAEIBAERJR2EXAMPLE`\ --private-key`file://cf-signer-priv-key.pem`\ --date-less-than`2020-01-01`Output: `https://d111111abcdef8.cloudfront.net/private-content/private-file.html?Expires=1577836800&Signature=nEXK7Kby47XKeZQKVc6pwkif6oZc-JWSpDkH0UH7EBGGqvgurkecCbgL5VfUAXyLQuJxFwRQWscz-owcq9KpmewCXrXQbPaJZNi9XSNwf4YKurPDQYaRQawKoeenH0GFteRf9ELK-Bs3nljTLjtbgzIUt7QJNKXcWr8AuUYikzGdJ4-qzx6WnxXfH~fxg4-GGl6l2kgCpXUB6Jx6K~Y3kpVOdzUPOIqFLHAnJojbhxqrVejomZZ2XrquDvNUCCIbePGnR3d24UPaLXG4FKOqNEaWDIBXu7jUUPwOyQCvpt-GNvjRJxqWf93uMobeMOiVYahb-e0KItiQewGcm0eLZQ__&Key-Pair-Id=APKAEIBAERJR2EXAMPLE`- 
                    For API details, see [Sign](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/sign.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a CloudFront distribution**The following `tag-resource`example adds two tags to the specified CloudFront distribution.`aws cloudfront tag-resource \ --resource``arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE`\ --tags '`Items=[{Key=Name,Value="Example name"},{Key=Project,Value="Example project"}]`'Instead of using command line arguments, you can provide the tags in a JSON file, as shown in the following example: `aws cloudfront tag-resource \ --resource``arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE`\ --tags`file://tags.json`Contents of `tags.json`:`{ "Items": [ { "Key": "Name", "Value": "Example name" }, { "Key": "Project", "Value": "Example project" } ] }`This command produces no output. - 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a CloudFront distribution**The following example removes two tags from a CloudFront distribution by using command line arguments: `aws cloudfront untag-resource \ --resource``arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE`\ --tag-keys`Items=Name,Project`Instead of using command line arguments, you can provide the tag keys in a JSON file, as shown in the following example: `aws cloudfront untag-resource \ --resource``arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE`\ --tag-keys`file://tag-keys.json`The file `tag-keys.json`is a JSON document in the current folder that contains the following:`{ "Items": [ "Name", "Project" ] }`When successful, this command has no output. - 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-cloud-front-origin-access-identity`.

- **AWS CLI**
- 
            
                    **To update a CloudFront origin access identity**The following example updates the origin access identity (OAI) with the ID `E74FTE3AEXAMPLE`. The only field that you can update is the OAI's`Comment`.To update an OAI, you must have the OAI's ID and `ETag`. The OAI ID is returned in the output of the create-cloud-front-origin-access-identity and list-cloud-front-origin-access-identities commands. To get the`ETag`, use the get-cloud-front-origin-access-identity or get-cloud-front-origin-access-identity-config command. Use the`--if-match`option to provide the OAI's`ETag`.`aws cloudfront update-cloud-front-origin-access-identity \ --id``E74FTE3AEXAMPLE`\ --if-match`E2QWRUHEXAMPLE`\ --cloud-front-origin-access-identity-config \ CallerReference=cli-example,Comment="Example OAI Updated"You can accomplish the same thing by providing the OAI configuration in a JSON file, as shown in the following example: `aws cloudfront update-cloud-front-origin-access-identity \ --id``E74FTE3AEXAMPLE`\ --if-match`E2QWRUHEXAMPLE`\ --cloud-front-origin-access-identity-config`file://OAI-config.json`The file `OAI-config.json`is a JSON document in the current directory that contains the following:`{ "CallerReference": "cli-example", "Comment": "Example OAI Updated" }`Whether you provide the OAI configuration with a command line argument or a JSON file, the output is the same: `{ "ETag": "E9LHASXEXAMPLE", "CloudFrontOriginAccessIdentity": { "Id": "E74FTE3AEXAMPLE", "S3CanonicalUserId": "cd13868f797c227fbea2830611a26fe0a21ba1b826ab4bed9b7771c9aEXAMPLE", "CloudFrontOriginAccessIdentityConfig": { "CallerReference": "cli-example", "Comment": "Example OAI Updated" } } }`- 
                    For API details, see [UpdateCloudFrontOriginAccessIdentity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-cloud-front-origin-access-identity.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-connection-group`.

- **AWS CLI**
- 
            
                    **To update a CloudFront connection group**The following `update-connection-group`example disables a CloudFront connection group and disables IPv6.`aws cloudfront update-connection-group \ --id``cg_2yHsDkcPKeUlVkk3aEgLKcjABC`\ --no-ipv6-enabled \ --no-enabled \ --if-match`E3UN6WX5RRO2ABC`Output: `{ "ETag": "E1F83G8C2ARABC", "ConnectionGroup": { "Id": "cg_2yHsDkcPKeUlVkk3aEgLKcjABC", "Name": "cg-example", "Arn": "arn:aws:cloudfront::123456789012:connection-group/cg_2yHsDkcPKeUlVkk3aEgLKcjABC", "CreatedTime": "2025-06-09T20:58:35.481000+00:00", "LastModifiedTime": "2025-06-11T16:25:54.280000+00:00", "Ipv6Enabled": false, "RoutingEndpoint": "du9xp1elo1abc.cloudfront.net", "Status": "InProgress", "Enabled": false, "IsDefault": false } }`For more information, see [Create custom connection group (optional)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-connection-group.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [UpdateConnectionGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-connection-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-distribution-tenant`.

- **AWS CLI**
- 
            
                    **To update a CloudFront distribution tenant**The following `update-distribution-tenant`example updates a CloudFront distribution tenant with a new parameter value and adds a country to the geo-restrictions.`aws cloudfront update-distribution-tenant \ --cli-input-json``file://update-tenant.json`Contents of `update-tenant.json`:`{ "Id": "dt_2yMvQgam3QkJo2z54FDl91dk1AB", "IfMatch": "E1F83G8C2ARABC", "Parameters": [ { "Name": "testParam", "Value": "newParameterValue" } ], "Customizations": { "WebAcl": { "Action": "disable" }, "GeoRestrictions": { "RestrictionType": "whitelist", "Locations": [ "DE", "GB", "ES" ] } } }`Output: `{ "ETag": "E1PA6795UKMABC", "DistributionTenant": { "Id": "dt_2yMvQgam3QkJo2z54FDl91dk1AB", "DistributionId": "E1XNX8R2GOAABC", "Name": "new-tenant-customizations", "Arn": "arn:aws:cloudfront::123456789012:distribution-tenant/dt_2yMvQgam3QkJo2z54FDl91dk1AB", "Domains": [ { "Domain": "example.com", "Status": "active" } ], "Customizations": { "WebAcl": { "Action": "disable" }, "GeoRestrictions": { "RestrictionType": "whitelist", "Locations": [ "DE", "ES", "GB" ] } }, "Parameters": [ { "Name": "testParam", "Value": "newParameterValue" } ], "ConnectionGroupId": "cg_2whCJoXMYCjHcxaLGrkllvyABC", "CreatedTime": "2025-06-11T15:54:02.142000+00:00", "LastModifiedTime": "2025-06-11T16:42:45.531000+00:00", "Enabled": false, "Status": "InProgress" } }`For more information, see [Distribution tenant customizations](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/tenant-customization.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [UpdateDistributionTenant](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-distribution-tenant.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-distribution`.

- **AWS CLI**
- 
            
                    **Example 1: To update a CloudFront distribution's default root object**The following example updates the default root object to `index.html`for the CloudFront distribution with the ID`EDFDVBD6EXAMPLE`.`aws cloudfront update-distribution \ --id``EDFDVBD6EXAMPLE`\ --default-root-object`index.html`Output: `{ "ETag": "E2QWRUHEXAMPLE", "Distribution": { "Id": "EDFDVBD6EXAMPLE", "ARN": "arn:aws:cloudfront::123456789012:distribution/EDFDVBD6EXAMPLE", "Status": "InProgress", "LastModifiedTime": "2019-12-06T18:55:39.870Z", "InProgressInvalidationBatches": 0, "DomainName": "d111111abcdef8.cloudfront.net", "ActiveTrustedSigners": { "Enabled": false, "Quantity": 0 }, "DistributionConfig": { "CallerReference": "6b10378d-49be-4c4b-a642-419ccaf8f3b5", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "example-website", "DomainName": "www.example.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "CustomOriginConfig": { "HTTPPort": 80, "HTTPSPort": 443, "OriginProtocolPolicy": "match-viewer", "OriginSslProtocols": { "Quantity": 2, "Items": [ "SSLv3", "TLSv1" ] }, "OriginReadTimeout": 30, "OriginKeepaliveTimeout": 5 } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "example-website", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 1, "Items": [ "*" ] }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": true, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http1.1", "IsIPV6Enabled": true } } }`**Example 2: To update a CloudFront distribution**The following example disables the CloudFront distribution with the ID `EMLARXS9EXAMPLE`by providing the distribution configuration in a JSON file named`dist-config-disable.json`. To update a distribution, you must use the`--if-match`option to provide the distribution's`ETag`. To get the`ETag`, use the get-distribution or get-distribution-config command. Note that the`Enabled`field is set to`false`in the JSON file.After you use the following example to disable a distribution, you can use the delete-distribution command to delete it. `aws cloudfront update-distribution \ --id``EMLARXS9EXAMPLE`\ --if-match`E2QWRUHEXAMPLE`\ --distribution-config`file://dist-config-disable.json`Contents of `dist-config-disable.json`:`{ "CallerReference": "cli-1574382155-496510", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-1574382155-273939", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-1574382155-273939", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": false, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true }`Output: `{ "ETag": "E9LHASXEXAMPLE", "Distribution": { "Id": "EMLARXS9EXAMPLE", "ARN": "arn:aws:cloudfront::123456789012:distribution/EMLARXS9EXAMPLE", "Status": "InProgress", "LastModifiedTime": "2019-12-06T18:32:35.553Z", "InProgressInvalidationBatches": 0, "DomainName": "d111111abcdef8.cloudfront.net", "ActiveTrustedSigners": { "Enabled": false, "Quantity": 0 }, "DistributionConfig": { "CallerReference": "cli-1574382155-496510", "Aliases": { "Quantity": 0 }, "DefaultRootObject": "index.html", "Origins": { "Quantity": 1, "Items": [ { "Id": "amzn-s3-demo-bucket.s3.amazonaws.com-1574382155-273939", "DomainName": "amzn-s3-demo-bucket.s3.amazonaws.com", "OriginPath": "", "CustomHeaders": { "Quantity": 0 }, "S3OriginConfig": { "OriginAccessIdentity": "" } } ] }, "OriginGroups": { "Quantity": 0 }, "DefaultCacheBehavior": { "TargetOriginId": "amzn-s3-demo-bucket.s3.amazonaws.com-1574382155-273939", "ForwardedValues": { "QueryString": false, "Cookies": { "Forward": "none" }, "Headers": { "Quantity": 0 }, "QueryStringCacheKeys": { "Quantity": 0 } }, "TrustedSigners": { "Enabled": false, "Quantity": 0 }, "ViewerProtocolPolicy": "allow-all", "MinTTL": 0, "AllowedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ], "CachedMethods": { "Quantity": 2, "Items": [ "HEAD", "GET" ] } }, "SmoothStreaming": false, "DefaultTTL": 86400, "MaxTTL": 31536000, "Compress": false, "LambdaFunctionAssociations": { "Quantity": 0 }, "FieldLevelEncryptionId": "" }, "CacheBehaviors": { "Quantity": 0 }, "CustomErrorResponses": { "Quantity": 0 }, "Comment": "", "Logging": { "Enabled": false, "IncludeCookies": false, "Bucket": "", "Prefix": "" }, "PriceClass": "PriceClass_All", "Enabled": false, "ViewerCertificate": { "CloudFrontDefaultCertificate": true, "MinimumProtocolVersion": "TLSv1", "CertificateSource": "cloudfront" }, "Restrictions": { "GeoRestriction": { "RestrictionType": "none", "Quantity": 0 } }, "WebACLId": "", "HttpVersion": "http2", "IsIPV6Enabled": true } } }`- 
                    For API details, see [UpdateDistribution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-distribution.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-domain-association`.

- **AWS CLI**
- 
            
                    **To update a domain association**The following `update-domain-association`example updates a domain association for a distribution tenant with ETag`E23ZP02F085ABC`.`aws cloudfront update-domain-association \ --domain``example.com`\ --target-resource`DistributionTenantId=dt_2x9GhoK0TZRsohWzv1b9It8J1AB`\ --if-match`E23ZP02F085ABC`Output: `{ "ETag": "ETVPDKIKX0ABC", "Domain": "example.com", "ResourceId": "dt_2x9GhoK0TZRsohWzv1b9It8J1AB" }`For more information, see [Move an alternate domain name to a different distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/alternate-domain-names-move.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [UpdateDomainAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-domain-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-field-level-encryption-config`.

- **AWS CLI**
- 
            
                    **To update a CloudFront field-level encryption configuration**The following example updates the `Comment`field of the field-level encryption configuration with the ID`C3KM2WVD605UAY`by providing the parameters in a JSON file.To update a field-level encryption configuration, you must have the configuration's ID and `ETag`. The ID is returned in the output of the create-field-level-encryption-config and list-field-level-encryption-configs commands. To get the`ETag`, use the get-field-level-encryption or get-field-level-encryption-config command. Use the`--if-match`option to provide the configuration's`ETag`.`aws cloudfront update-field-level-encryption-config \ --id``C3KM2WVD605UAY`\ --if-match`E2P4Z4VU7TY5SG`\ --field-level-encryption-config`file://fle-config.json`The file `fle-config.json`is a JSON document in the current directory that contains the following:`{ "CallerReference": "cli-example", "Comment": "Updated example FLE configuration", "QueryArgProfileConfig": { "ForwardWhenQueryArgProfileIsUnknown": true, "QueryArgProfiles": { "Quantity": 0 } }, "ContentTypeProfileConfig": { "ForwardWhenContentTypeIsUnknown": true, "ContentTypeProfiles": { "Quantity": 1, "Items": [ { "Format": "URLEncoded", "ProfileId": "P280MFCLSYOCVU", "ContentType": "application/x-www-form-urlencoded" } ] } } }`Output: `{ "ETag": "E26M4BIAV81ZF6", "FieldLevelEncryption": { "Id": "C3KM2WVD605UAY", "LastModifiedTime": "2019-12-10T22:26:26.170Z", "FieldLevelEncryptionConfig": { "CallerReference": "cli-example", "Comment": "Updated example FLE configuration", "QueryArgProfileConfig": { "ForwardWhenQueryArgProfileIsUnknown": true, "QueryArgProfiles": { "Quantity": 0, "Items": [] } }, "ContentTypeProfileConfig": { "ForwardWhenContentTypeIsUnknown": true, "ContentTypeProfiles": { "Quantity": 1, "Items": [ { "Format": "URLEncoded", "ProfileId": "P280MFCLSYOCVU", "ContentType": "application/x-www-form-urlencoded" } ] } } } } }`- 
                    For API details, see [UpdateFieldLevelEncryptionConfig](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-field-level-encryption-config.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-field-level-encryption-profile`.

- **AWS CLI**
- 
            
                    **To update a CloudFront field-level encryption profile**The following example updates the field-level encryption profile with the ID `PPK0UOSIF5WSV`. This example updates the profile's`Name`and`Comment`, and adds a second`FieldPatterns`item, by providing the parameters in a JSON file.To update a field-level encryption profile, you must have the profile's ID and `ETag`. The ID is returned in the output of the create-field-level-encryption-profile and list-field-level-encryption-profiles commands. To get the`ETag`, use the get-field-level-encryption-profile or get-field-level-encryption-profile-config command. Use the`--if-match`option to provide the profile's`ETag`.`aws cloudfront update-field-level-encryption-profile \ --id``PPK0UOSIF5WSV`\ --if-match`E1QQG65FS2L2GC`\ --field-level-encryption-profile-config`file://fle-profile-config.json`The file `fle-profile-config.json`is a JSON document in the current directory that contains the following:`{ "Name": "ExampleFLEProfileUpdated", "CallerReference": "cli-example", "Comment": "Updated FLE profile for AWS CLI example", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2K8NC4HVFE3M0", "ProviderId": "ExampleFLEProvider", "FieldPatterns": { "Quantity": 2, "Items": [ "ExampleSensitiveField", "SecondExampleSensitiveField" ] } } ] } }`Output: `{ "ETag": "EJETYFJ9CL66D", "FieldLevelEncryptionProfile": { "Id": "PPK0UOSIF5WSV", "LastModifiedTime": "2019-12-10T19:05:58.296Z", "FieldLevelEncryptionProfileConfig": { "Name": "ExampleFLEProfileUpdated", "CallerReference": "cli-example", "Comment": "Updated FLE profile for AWS CLI example", "EncryptionEntities": { "Quantity": 1, "Items": [ { "PublicKeyId": "K2K8NC4HVFE3M0", "ProviderId": "ExampleFLEProvider", "FieldPatterns": { "Quantity": 2, "Items": [ "ExampleSensitiveField", "SecondExampleSensitiveField" ] } } ] } } } }`- 
                    For API details, see [UpdateFieldLevelEncryptionProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-field-level-encryption-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `verify-dns-configuration`.

- **AWS CLI**
- 
            
                    **To verify DNS configuration for a domain**The following `verify-dns-configuration`example verifies the DNS configuration for a domain.`aws cloudfront verify-dns-configuration \ --domain``example.com`\ --identifier`dt_2x9GhoK0TZRsohWzv1b9It8J1AB`Output: `{ "DnsConfigurationList": [ { "Domain": "example.com", "Status": "valid-configuration" } ] }`For more information, see [Move an alternate domain name to a different distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/alternate-domain-names-move.html)in the*Amazon CloudFront Developer Guide*.- 
                    For API details, see [VerifyDnsConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/verify-dns-configuration.html)in*AWS CLI Command Reference*.
 
-