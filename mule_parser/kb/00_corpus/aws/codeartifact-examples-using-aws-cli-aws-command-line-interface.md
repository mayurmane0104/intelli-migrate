# CodeArtifact examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_codeartifact_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_codeartifact_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CodeArtifact.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-external-connection`.

- **AWS CLI**
- 
            
                    **To add an external connection to a repository**The following `associate-external-connection`example adds an external connection to npmjs.com to a repository named test-repo.`aws codeartifact associate-external-connection \ --repository``test-repo`\ --domain`test-domain`\ --external-connection`public:npmjs`Output: `{ "repository": { "name": "test-repo", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo", "upstreams": [], "externalConnections": [ { "externalConnectionName": "public:npmjs", "packageFormat": "npm", "status": "AVAILABLE" } ] } }`For more information, see [Add an external connection](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [AssociateExternalConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/associate-external-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `copy-package-versions`.

- **AWS CLI**
- 
            
                    **To copy package versions from one repository to another**The following `copy-package-versions`moves versions 4.0.0 and 5.0.0 of a package named test-package from my-repo to test-repo.`aws codeartifact copy-package-versions \ --domain``test-domain`\ --source-repository`my-repo`\ --destination-repository`test-repo`\ --format`npm`\ --package`test-package`\ --versions '`["4.0.0", "5.0.0"]`'Output: `{ "format": "npm", "package": "test-package", "versions": [ { "version": "5.0.0", "revision": "REVISION-1-SAMPLE-6C81EFF7DA55CC", "status": "Published" }, { "version": "4.0.0", "revision": "REVISION-2-SAMPLE-55C752BEE772FC", "status": "Published" } ] }`For more information, see [Copy packages between repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/copy-package.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [CopyPackageVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/copy-package-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-domain`.

- **AWS CLI**
- 
            
                    **To create a domain**The following `create-domain`example creates a domain named test-domain.`aws codeartifact create-domain \ --domain``test-domain`Output: `{ "domain": { "name": "test-domain", "owner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:domain/test-domain", "status": "Active", "createdTime": "2020-10-20T13:16:48.559000-04:00", "encryptionKey": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "repositoryCount": 0, "assetSizeBytes": 0 } }`For more information, see [Create a domain](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-create.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [CreateDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/create-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-repository`.

- **AWS CLI**
- 
            
                    **To create a repository**The following `create-repository`example creates a repository named test-repo inside a domain named test-domain.`aws codeartifact create-repository \ --domain``test-domain`\ --domain-owner`111122223333`\ --repository`test-repo`\ --description`"This is a test repository."`Output: `{ "repository": { "name": "test-repo", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo", "description": "This is a test repository.", "upstreams": [], "externalConnections": [] } }`For more information, see [Create a domain](https://docs.aws.amazon.com/codeartifact/latest/ug/create-repo.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [CreateRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/create-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain-permissions-policy`.

- **AWS CLI**
- 
            
                    **To delete the permissions policy document from a domain**The following `delete-domain-permissions-policy`example deletes the permission policy from a domain named test-domain.`aws codeartifact delete-domain-permissions-policy \ --domain``test-domain`Output: `{ "Version":"2012-10-17", "Statement": [ { "Sid": "BasicDomainPolicy", "Action": [ "codeartifact:GetDomainPermissionsPolicy", "codeartifact:ListRepositoriesInDomain", "codeartifact:GetAuthorizationToken", "codeartifact:CreateRepository" ], "Effect": "Allow", "Resource": "*", "Principal": { "AWS": "arn:aws:iam::111122223333:root" } } ] }`For more information, see [Delete a domain policy](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-policies.html#deleting-a-domain-policy)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DeleteDomainPermissionsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-domain-permissions-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-domain`.

- **AWS CLI**
- 
            
                    **To delete a domain**The following `delete-domain`example deletes a domain named`test-domain`.`aws codeartifact delete-domain \ --domain``test-domain`Output: `{ "domain": { "name": "test-domain", "owner": "417498243647", "arn": "arn:aws:codeartifact:us-west-2:417498243647:domain/test-domain", "status": "Deleted", "createdTime": "2020-10-20T13:16:48.559000-04:00", "encryptionKey": "arn:aws:kms:us-west-2:417498243647:key/c9fe2447-0795-4fda-afbe-8464574ae162", "repositoryCount": 0, "assetSizeBytes": 0 } }`For more information, see [Delete a domain](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-domain.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DeleteDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-package-versions`.

- **AWS CLI**
- 
            
                    **To delete package versions**The following `delete-package-versions`example deletes version 4.0.0 of a package named test-package.`aws codeartifact delete-package-versions \ --domain``test-domain`\ --repo`test-repo`\ --format`npm`\ --package`test-package`\ --versions`4.0.0`Output: `{ "successfulVersions": { "4.0.0": { "revision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=", "status": "Deleted" } }, "failedVersions": {} }`For more information, see [Delete a package version](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-package.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DeletePackageVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-package-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-repository-permissions-policy`.

- **AWS CLI**
- 
            
                    **To delete a permissions policy from a repository**The following `delete-repository-permissions-policy`example deletes the permission policy from a repository named test-repo.`aws codeartifact delete-repository-permissions-policy \ --domain``test-domain`\ --repository`test-repo`Output: `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::111122223333:root" }, "Action": [ "codeartifact:DescribePackageVersion", "codeartifact:DescribeRepository", "codeartifact:GetPackageVersionReadme", "codeartifact:GetRepositoryEndpoint", "codeartifact:ListPackages", "codeartifact:ListPackageVersions", "codeartifact:ListPackageVersionAssets", "codeartifact:ListPackageVersionDependencies", "codeartifact:ReadFromRepository" ], "Resource": "*" } ] }`For more information, see [Delete a policy](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html#deleting-a-policy)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DeleteRepositoryPermissionsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository-permissions-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-repository`.

- **AWS CLI**
- 
            
                    **To delete a repository**The following `delete-repository`example deletes a repository named`test-repo`in a domain named`test-domain`.`aws codeartifact delete-repository \ --domain``test-domain`\ --repository`test-repo`Output: `{ "repository": { "name": "test-repo", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo", "description": "This is a test repository", "upstreams": [], "externalConnections": [] } }`For more information, see [Delete a repository](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-repo.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DeleteRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-domain`.

- **AWS CLI**
- 
            
                    **To get information about a domain**The following `describe-domain`example returns a DomainDescription object for a domain named test-domain.`aws codeartifact describe-domain \ --domain``test-domain`Output: `{ "domain": { "name": "test-domain", "owner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:domain/test-domain", "status": "Active", "createdTime": "2020-10-20T13:16:48.559000-04:00", "encryptionKey": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "repositoryCount": 2, "assetSizeBytes": 0, "s3BucketArn": "arn:aws:s3:::assets-111122223333-us-west-2" } }`For more information, see [Domain overview](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-overview.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DescribeDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-repository`.

- **AWS CLI**
- 
            
                    **To get information about a repository**The following `describe-repository`example returns a RepositoryDescription object for a repository named test-repo.`aws codeartifact describe-repository \ --domain``test-domain`\ --repository`test-repo`Output: `{ "repository": { "name": "test-repo", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo", "description": "This is a test repository.", "upstreams": [], "externalConnections": [] } }`For more information, see [Create a domain](https://docs.aws.amazon.com/codeartifact/latest/ug/create-repo.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DescribeRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-external-connection`.

- **AWS CLI**
- 
            
                    **To remove an external connection from a repository**The following `disassociate-external-connection`example removes an external connection to npmjs.com from a repository named test-repo.`aws codeartifact disassociate-external-connection \ --repository``test-repo`\ --domain`test-domain`\ --external-connection`public:npmjs`Output: `{ "repository": { "name": "test-repo", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo", "upstreams": [], "externalConnections": [] } }`For more information, see [Remove an external connection](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html#removing-an-external-connection)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DisassociateExternalConnection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/disassociate-external-connection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `dispose-package-versions`.

- **AWS CLI**
- 
            
                    **To delete a package version's assets and set its status to Disposed**The following `dispose-package-versions`example deletes the assets of test-package version 4.0.0 and sets its status to Disposed.`aws codeartifact dispose-package-versions \ --domain``test-domain`\ --repo`test-repo`\ --format`npm`\ --package`test-package`\ --versions`4.0.0`Output: `{ "successfulVersions": { "4.0.0": { "revision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=", "status": "Disposed" } }, "failedVersions": {} }`For more information, see [Working with packages in CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/packages.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [DisposePackageVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/dispose-package-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-authorization-token`.

- **AWS CLI**
- 
            
                    **To get an authorization token**The following `get-authorization-token`example retrieves a CodeArtifact authorization token.`aws codeartifact get-authorization-token \ --domain``test-domain`\ --query`authorizationToken`\ --output`text`Output: `This command will return the authorization token. You can store the output in an environment variable when calling the command.`For more information, see [Configure pip without the login command](https://docs.aws.amazon.com/codeartifact/latest/ug/python-configure-without-pip.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [GetAuthorizationToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-authorization-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-domain-permissions-policy`.

- **AWS CLI**
- 
            
                    **To get the permissions policy document for a domain**The following `get-domain-permissions-policy`example gets the permission policy attached to a domain named test-domain.`aws codeartifact get-domain-permissions-policy \ --domain``test-domain`Output: `{ "Version":"2012-10-17", "Statement": [ { "Sid": "BasicDomainPolicy", "Action": [ "codeartifact:GetDomainPermissionsPolicy", "codeartifact:ListRepositoriesInDomain", "codeartifact:GetAuthorizationToken", "codeartifact:CreateRepository" ], "Effect": "Allow", "Resource": "*", "Principal": { "AWS": "arn:aws:iam::111122223333:root" } } ] }`For more information, see [Read a domain policy](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-policies.html#reading-a-domain-policy)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [GetDomainPermissionsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-domain-permissions-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-package-version-asset`.

- **AWS CLI**
- 
            
                    **To get an asset from a package version**The following `get-package-version-asset`example retrieves the`package.tgz`asset for version 4.0.0 of an npm package named test-package.`aws codeartifact get-package-version-asset \ --domain``test-domain`\ --repository`test-repo`\ --format`npm`\ --package`test-package`\ --package-version`4.0.0`\ --asset '`package.tgz`' \`outfileName`Output: `The output for this command will also store the raw asset in the file provided in place of outfileName. { "assetName": "package.tgz", "packageVersion": "4.0.0", "packageVersionRevision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=" }`For more information, see [List package version assets](https://docs.aws.amazon.com/codeartifact/latest/ug/list-assets.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [GetPackageVersionAsset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-package-version-asset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-package-version-readme`.

- **AWS CLI**
- 
            
                    **To get a package version's readme file**The following `get-package-version-readme`example retrieves the readme file for version 4.0.0 of an npm package named test-package.`aws codeartifact get-package-version-readme \ --domain``test-domain`\ --repo`test-repo`\ --format`npm`\ --package`test-package`\ --package-version`4.0.0`Output: `{ "format": "npm", "package": "test-package", "version": "4.0.0", "readme": "<div align=\"center\">\n <a href=\https://github.com/test-package/testpack\"> ... more content ... \n", "versionRevision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=" }`For more information, see [View package version readme file](https://docs.aws.amazon.com/codeartifact/latest/ug/describe-package-version.html#view-package-readme)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [GetPackageVersionReadme](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-package-version-readme.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-repository-endpoint`.

- **AWS CLI**
- 
            
                    **To get a repository's URL endpoint**The following `get-repository-endpoint`example returns the npm endpoint for the test-repo repository.`aws codeartifact get-repository-endpoint \ --domain``test-domain`\ --repository`test-repo`\ --format`npm`Output: `{ "repositoryEndpoint": "https://test-domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/npm/test-repo/" }`For more information, see [Connect to a repository](https://docs.aws.amazon.com/codeartifact/latest/ug/connect-repo.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [GetRepositoryEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-repository-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-repository-permissions-policy`.

- **AWS CLI**
- 
            
                    **To get the permissions policy document for a repository**The following `get-repository-permissions-policy`example gets the permission policy attached to a repository named test-repo.`aws codeartifact get-repository-permissions-policy \ --domain``test-domain`\ --repository`test-repo`Output: `{ "Version":"2012-10-17", "Statement": [ { "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::111122223333:root" }, "Action": [ "codeartifact:DescribePackageVersion", "codeartifact:DescribeRepository", "codeartifact:GetPackageVersionReadme", "codeartifact:GetRepositoryEndpoint", "codeartifact:ListPackages", "codeartifact:ListPackageVersions", "codeartifact:ListPackageVersionAssets", "codeartifact:ListPackageVersionDependencies", "codeartifact:ReadFromRepository" ], "Resource": "*" } ] }`For more information, see [Read a policy](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html#setting-a-policy)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [GetRepositoryPermissionsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-repository-permissions-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-domains`.

- **AWS CLI**
- 
            
                    **To list domains**The following `list-domains`example returns a summary of all domains owned by the AWS account that makes the call.`aws codeartifact list-domains`Output: `{ "domains": [ { "name": "my-domain", "owner": "111122223333", "status": "Active", "encryptionKey": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" }, { "name": "test-domain", "owner": "111122223333", "status": "Active", "encryptionKey": "arn:aws:kms:us-west-2:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222" } ] }`For more information, see [Working with domains in CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/domains.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [ListDomains](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-domains.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-package-version-assets`.

- **AWS CLI**
- 
            
                    **To view a package version's assets**The following `list-package-version-assets`example retrieves the assets for version 4.0.0 of an npm package named test-package.`aws codeartifact list-package-version-assets \ --domain``test-domain`\ --repo`test-repo`\ --format`npm`\ --package`test-package`\ --package-version`4.0.0`Output: `{ "format": "npm", "package": "test-package", "version": "4.0.0", "versionRevision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=", "assets": [ { "name": "package.tgz", "size": 316680, "hashes": { "MD5": "60078ec6d9e76b89fb55c860832742b2", "SHA-1": "b44a9b6297bcb698f1c51a3545a2b3b368d59c52", "SHA-256": "d2aa8c6afc3c8591765785a37d1c5acae482a8eb3ab9729ed28922692454f2e2", "SHA-512": "3e585d15c8a594e20d7de57b362ea81754c011acb2641a19f1b72c8531ea39825896bab344ae616a0a5a824cb9a381df0b3cddd534645cf305aba70a93dac698" } } ] }`For more information, see [List package version assets](https://docs.aws.amazon.com/codeartifact/latest/ug/list-assets.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [ListPackageVersionAssets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-version-assets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-package-version-dependencies`.

- **AWS CLI**
- 
            
                    **To view a package version's dependencies**The following `list-package-version-dependencies`example retrieves the dependencies for version 4.0.0 of an npm package named test-package.`aws codeartifact list-package-version-dependencies \ --domain``test-domain`\ --repo`test-repo`\ --format`npm`\ --package`test-package`\ --package-version`4.0.0`Output: `{ "format": "npm", "package": "test-package", "version": "4.0.0", "versionRevision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=", "dependencies": [ { "namespace": "testns", "package": "testdep1", "dependencyType": "regular", "versionRequirement": "1.8.5" }, { "namespace": "testns", "package": "testdep2", "dependencyType": "regular", "versionRequirement": "1.8.5" } ] }`For more information, see [View and update package version details and dependencies](https://docs.aws.amazon.com/codeartifact/latest/ug/describe-package-version.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [ListPackageVersionDependencies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-version-dependencies.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-package-versions`.

- **AWS CLI**
- 
            
                    **To list package versions for a package**The following `list-package-versions`example returns a list of package versions for a package named`kind-of`.`aws codeartifact list-package-versions \ --package``kind-of`\ --domain`test-domain`\ --repository`test-repo`\ --format`npm`Output: `{ "defaultDisplayVersion": "1.0.1", "format": "npm", "package": "kind-of", "versions": [ { "version": "1.0.1", "revision": "REVISION-SAMPLE-1-C7F4S5E9B772FC", "status": "Published" }, { "version": "1.0.0", "revision": "REVISION-SAMPLE-2-C752BEEF6D2CFC", "status": "Published" }, { "version": "0.1.2", "revision": "REVISION-SAMPLE-3-654S65A5C5E1FC", "status": "Published" }, { "version": "0.1.1", "revision": "REVISION-SAMPLE-1-C7F4S5E9B772FC"", "status": "Published" }, { "version": "0.1.0", "revision": "REVISION-SAMPLE-4-AF669139B772FC", "status": "Published" } ] }`For more information, see [List package versions](https://docs.aws.amazon.com/codeartifact/latest/ug/list-packages-versions.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [ListPackageVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-packages`.

- **AWS CLI**
- 
            
                    **To list packages in a repository**The following `list-packages`example list packages in a repository named`test-repo`in a domain named`test-domain`.`aws codeartifact list-packages \ --domain``test-domain`\ --repository`test-repo`Output: `{ "packages": [ { "format": "npm", "package": "lodash" } { "format": "python", "package": "test-package" } ] }`For more information, see [List package names](https://docs.aws.amazon.com/codeartifact/latest/ug/list-packages.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [ListPackages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-packages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-repositories-in-domain`.

- **AWS CLI**
- 
            
                    **To list repositories in a domain**The following `list-repositories-in-domain`example returns a summary of all repositories in the test-domain domain.`aws codeartifact list-repositories-in-domain \ --domain``test-domain`Output: `{ "repositories": [ { "name": "test-repo", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo", "description": "This is a test repository." }, { "name": "test-repo2", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo2", "description": "This is a test repository." } ] }`For more information, see [List repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/list-repos.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [ListRepositoriesInDomain](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-repositories-in-domain.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-repositories`.

- **AWS CLI**
- 
            
                    **To list repositories**The following `list-repositories`example returns a summary of all repositories in domain owned by the AWS account that makes the call.`aws codeartifact list-repositories`Output: `{ "repositories": [ { "name": "npm-store", "administratorAccount": "111122223333", "domainName": "my-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/my-domain/npm-store", "description": "Provides npm artifacts from npm, Inc." }, { "name": "target-repo", "administratorAccount": "111122223333", "domainName": "my-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/my-domain/target-repo", "description": "test target repo" }, { "name": "test-repo2", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo2", "description": "This is a test repository." } ] }`For more information, see [List repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/list-repos.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [ListRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-repositories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `login`.

- **AWS CLI**
- 
            
                    **To configure authentication to your repository with the login command**The following `login`example configures the npm package manager with a repository named test-repo in a domain named test-domain.`aws codeartifact login \ --domain``test-domain`\ --repository`test-repo`\ --tool`npm`Output: `Successfully configured npm to use AWS CodeArtifact repository https://test-domain-111122223333.d.codeartifact.us-west-2.amazonaws.com/npm/test-repo/ Login expires in 12 hours at 2020-11-12 01:53:16-05:00`For more information, see [Getting started with the AWS CLI](https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started-cli.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [Login](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/login.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-domain-permissions-policy`.

- **AWS CLI**
- 
            
                    **To attach a permissions policy to a domain**The following `put-domain-permissions-policy`example attaches a permission policy that is defined in the policy.json file to a domain named test-domain.`aws codeartifact put-domain-permissions-policy \ --domain``test-domain`\ --policy-document`file://PATH/TO/policy.json`Output: `{ "policy": { "resourceArn": "arn:aws:codeartifact:region-id:111122223333:domain/test-domain", "document": "{ ...policy document content...}", "revision": "MQlyyTQRASRU3HB58gBtSDHXG7Q3hvxxxxxxx=" } }`For more information, see [Set a domain policy](https://docs.aws.amazon.com/codeartifact/latest/ug/domain-policies.html#set-domain-policy)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [PutDomainPermissionsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-domain-permissions-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-repository-permissions-policy`.

- **AWS CLI**
- 
            
                    **To attach a permissions policy to a repository**The following `put-repository-permissions-policy`example attaches a permission policy that is defined in the policy.json file to a repository named test-repo.`aws codeartifact put-repository-permissions-policy \ --domain``test-domain`\ --repository`test-repo`\ --policy-document`file://PATH/TO/policy.json`Output: `{ "policy": { "resourceArn": "arn:aws:codeartifact:region-id:111122223333:repository/test-domain/test-repo", "document": "{ ...policy document content...}", "revision": "MQlyyTQRASRU3HB58gBtSDHXG7Q3hvxxxxxxx=" } }`For more information, see [Set a policy](https://docs.aws.amazon.com/codeartifact/latest/ug/repo-policies.html#setting-a-policy)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [PutRepositoryPermissionsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-repository-permissions-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-package-versions-status`.

- **AWS CLI**
- 
            
                    **To update package version status**The following `update-package-versions-status`example updates the status of version 4.0.0 of the test-package package to Archived.`aws codeartifact update-package-versions-status \ --domain``test-domain`\ --repo`test-repo`\ --format`npm`\ --package`test-package`\ --versions`4.0.0`\ --target-status`Archived`Output: `{ "successfulVersions": { "4.0.0": { "revision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=", "status": "Archived" } }, "failedVersions": {} }`For more information, see [Update package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/describe-package-version.html#update-package-version-status)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [UpdatePackageVersionsStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-package-versions-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-repository`.

- **AWS CLI**
- 
            
                    **To update a repository**The following `update-repository`example updates the description of a repo named test-repo in a domain named test-domain to "this is an updated description".`aws codeartifact update-repository \ --domain``test-domain`\ --repository`test-repo`\ --description`"this is an updated description"`Output: `{ "repository": { "name": "test-repo", "administratorAccount": "111122223333", "domainName": "test-domain", "domainOwner": "111122223333", "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo", "description": "this is an updated description", "upstreams": [], "externalConnections": [] } }`For more information, see [View or modify a repository configuration](https://docs.aws.amazon.com/codeartifact/latest/ug/config-repos.html)in the*AWS CodeArtifact User Guide*.- 
                    For API details, see [UpdateRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-repository.html)in*AWS CLI Command Reference*.
 
-