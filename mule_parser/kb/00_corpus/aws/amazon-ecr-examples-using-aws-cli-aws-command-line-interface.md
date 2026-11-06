# Amazon ECR examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_ecr_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_ecr_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon ECR.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-check-layer-availability`.

- **AWS CLI**
- 
            
                    **To check the availability of a layer**The following `batch-check-layer-availability`example checks the availability of a layer with the digest`sha256:6171c7451a50945f8ddd72f7732cc04d7a0d1f48138a426b2e64387fdeb834ed`in the`cluster-autoscaler`repository.`aws ecr batch-check-layer-availability \ --repository-name``cluster-autoscaler`\ --layer-digests`sha256:6171c7451a50945f8ddd72f7732cc04d7a0d1f48138a426b2e64387fdeb834ed`Output: `{ "layers": [ { "layerDigest": "sha256:6171c7451a50945f8ddd72f7732cc04d7a0d1f48138a426b2e64387fdeb834ed", "layerAvailability": "AVAILABLE", "layerSize": 2777, "mediaType": "application/vnd.docker.container.image.v1+json" } ], "failures": [] }`- 
                    For API details, see [BatchCheckLayerAvailability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/batch-check-layer-availability.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-delete-image`.

- **AWS CLI**
- 
            
                    **Example 1: To delete an image**The following `batch-delete-image`example deletes an image with the tag`precise`in the specified repository in the default registry for an account.`aws ecr batch-delete-image \ --repository-name``ubuntu`\ --image-ids`imageTag=precise`Output: `{ "failures": [], "imageIds": [ { "imageTag": "precise", "imageDigest": "sha256:19665f1e6d1e504117a1743c0a3d3753086354a38375961f2e665416ef4b1b2f" } ] }`**Example 2: To delete multiple images**The following `batch-delete-image`example deletes all images tagged with`prod`and`team1`in the specified repository.`aws ecr batch-delete-image \ --repository-name``MyRepository`\ --image-ids`imageTag=prod``imageTag=team1`Output: `{ "imageIds": [ { "imageDigest": "sha256:123456789012", "imageTag": "prod" }, { "imageDigest": "sha256:567890121234", "imageTag": "team1" } ], "failures": [] }`For more information, see [Deleting an Image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/delete_image.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [BatchDeleteImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/batch-delete-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-image`.

- **AWS CLI**
- 
            
                    **Example 1: To get an image**The following `batch-get-image`example gets an image with the tag`v1.13.6`in a repository called`cluster-autoscaler`in the default registry for an account.`aws ecr batch-get-image \ --repository-name``cluster-autoscaler`\ --image-ids`imageTag=v1.13.6`Output: `{ "images": [ { "registryId": "012345678910", "repositoryName": "cluster-autoscaler", "imageId": { "imageDigest": "sha256:4a1c6567c38904384ebc64e35b7eeddd8451110c299e3368d2210066487d97e5", "imageTag": "v1.13.6" }, "imageManifest": "{\n \"schemaVersion\": 2,\n \"mediaType\": \"application/vnd.docker.distribution.manifest.v2+json\",\n \"config\": {\n \"mediaType\": \"application/vnd.docker.container.image.v1+json\",\n \"size\": 2777,\n \"digest\": \"sha256:6171c7451a50945f8ddd72f7732cc04d7a0d1f48138a426b2e64387fdeb834ed\"\n },\n \"layers\": [\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 17743696,\n \"digest\": \"sha256:39fafc05754f195f134ca11ecdb1c9a691ab0848c697fffeb5a85f900caaf6e1\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 2565026,\n \"digest\": \"sha256:8c8a779d3a537b767ae1091fe6e00c2590afd16767aa6096d1b318d75494819f\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 28005981,\n \"digest\": \"sha256:c44ba47496991c9982ee493b47fd25c252caabf2b4ae7dd679c9a27b6a3c8fb7\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 775,\n \"digest\": \"sha256:e2c388b44226544363ca007be7b896bcce1baebea04da23cbd165eac30be650f\"\n }\n ]\n}" } ], "failures": [] }`**Example 2: To get multiple images**The following `batch-get-image`example displays details of all images tagged with`prod`and`team1`in the specified repository.`aws ecr batch-get-image \ --repository-name``MyRepository`\ --image-ids`imageTag=prod``imageTag=team1`Output: `{ "images": [ { "registryId": "123456789012", "repositoryName": "MyRepository", "imageId": { "imageDigest": "sha256:123456789012", "imageTag": "prod" }, "imageManifest": "manifestExample1" }, { "registryId": "567890121234", "repositoryName": "MyRepository", "imageId": { "imageDigest": "sha256:123456789012", "imageTag": "team1" }, "imageManifest": "manifestExample2" } ], "failures": [] }`For more information, see [Images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/images.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [BatchGetImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/batch-get-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `complete-layer-upload`.

- **AWS CLI**
- 
            
                    **To complete an image layer upload**The following `complete-layer-upload`example completes an image layer upload to the`layer-test`repository.`aws ecr complete-layer-upload \ --repository-name``layer-test`\ --upload-id`6cb64b8a-9378-0e33-2ab1-b780fab8a9e9`\ --layer-digests`6cb64b8a-9378-0e33-2ab1-b780fab8a9e9:48074e6d3a68b39aad8ccc002cdad912d4148c0f92b3729323e`Output: `{ "uploadId": "6cb64b8a-9378-0e33-2ab1-b780fab8a9e9", "layerDigest": "sha256:9a77f85878aa1906f2020a0ecdf7a7e962d57e882250acd773383224b3fe9a02", "repositoryName": "layer-test", "registryId": "130757420319" }`- 
                    For API details, see [CompleteLayerUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/complete-layer-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-repository`.

- **AWS CLI**
- 
            
                    **Example 1: To create a repository**The following `create-repository`example creates a repository inside the specified namespace in the default registry for an account.`aws ecr create-repository \ --repository-name``project-a/sample-repo`Output: `{ "repository": { "registryId": "123456789012", "repositoryName": "project-a/sample-repo", "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo" } }`For more information, see [Creating a Repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html)in the*Amazon ECR User Guide*.**Example 2: To create a repository configured with image tag immutability**The following `create-repository`example creates a repository configured for tag immutability in the default registry for an account.`aws ecr create-repository \ --repository-name``project-a/sample-repo`\ --image-tag-mutability`IMMUTABLE`Output: `{ "repository": { "registryId": "123456789012", "repositoryName": "project-a/sample-repo", "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo", "imageTagMutability": "IMMUTABLE" } }`For more information, see [Image Tag Mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html)in the*Amazon ECR User Guide*.**Example 3: To create a repository configured with a scanning configuration**The following `create-repository`example creates a repository configured to perform a vulnerability scan on image push in the default registry for an account.`aws ecr create-repository \ --repository-name``project-a/sample-repo`\ --image-scanning-configuration`scanOnPush=true`Output: `{ "repository": { "registryId": "123456789012", "repositoryName": "project-a/sample-repo", "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/project-a/sample-repo", "imageScanningConfiguration": { "scanOnPush": true } } }`For more information, see [Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [CreateRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/create-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-lifecycle-policy`.

- **AWS CLI**
- 
            
                    **To delete the lifecycle policy for a repository**The following `delete-lifecycle-policy`example deletes the lifecycle policy for the`hello-world`repository.`aws ecr delete-lifecycle-policy \ --repository-name``hello-world`Output: `{ "registryId": "012345678910", "repositoryName": "hello-world", "lifecyclePolicyText": "{\"rules\":[{\"rulePriority\":1,\"description\":\"Remove untagged images.\",\"selection\":{\"tagStatus\":\"untagged\",\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":10},\"action\":{\"type\":\"expire\"}}]}", "lastEvaluatedAt": 0.0 }`- 
                    For API details, see [DeleteLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-lifecycle-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-repository-policy`.

- **AWS CLI**
- 
            
                    **To delete the repository policy for a repository**The following `delete-repository-policy`example deletes the repository policy for the`cluster-autoscaler`repository.`aws ecr delete-repository-policy \ --repository-name``cluster-autoscaler`Output: `{ "registryId": "012345678910", "repositoryName": "cluster-autoscaler", "policyText": "{\n \"Version\" : \"2008-10-17\",\n \"Statement\" : [ {\n \"Sid\" : \"allow public pull\",\n \"Effect\" : \"Allow\",\n \"Principal\" : \"*\",\n \"Action\" : [ \"ecr:BatchCheckLayerAvailability\", \"ecr:BatchGetImage\", \"ecr:GetDownloadUrlForLayer\" ]\n } ]\n}" }`- 
                    For API details, see [DeleteRepositoryPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-repository`.

- **AWS CLI**
- 
            
                    **To delete a repository**The following `delete-repository`example command force deletes the specified repository in the default registry for an account. The`--force`flag is required if the repository contains images.`aws ecr delete-repository \ --repository-name``ubuntu`\ --forceOutput: `{ "repository": { "registryId": "123456789012", "repositoryName": "ubuntu", "repositoryArn": "arn:aws:ecr:us-west-2:123456789012:repository/ubuntu" } }`For more information, see [Deleting a Repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-delete.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [DeleteRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/delete-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-image-scan-findings`.

- **AWS CLI**
- 
            
                    **To describe the scan findings for an image**The following `describe-image-scan-findings`example returns the image scan findings for an image using the image digest in the specified repository in the default registry for an account.`aws ecr describe-image-scan-findings \ --repository-name``sample-repo`\ --image-id`imageDigest=sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6`Output: `{ "imageScanFindings": { "findings": [ { "name": "CVE-2019-5188", "description": "A code execution vulnerability exists in the directory rehashing functionality of E2fsprogs e2fsck 1.45.4. A specially crafted ext4 directory can cause an out-of-bounds write on the stack, resulting in code execution. An attacker can corrupt a partition to trigger this vulnerability.", "uri": "http://people.ubuntu.com/~ubuntu-security/cve/CVE-2019-5188", "severity": "MEDIUM", "attributes": [ { "key": "package_version", "value": "1.44.1-1ubuntu1.1" }, { "key": "package_name", "value": "e2fsprogs" }, { "key": "CVSS2_VECTOR", "value": "AV:L/AC:L/Au:N/C:P/I:P/A:P" }, { "key": "CVSS2_SCORE", "value": "4.6" } ] } ], "imageScanCompletedAt": 1579839105.0, "vulnerabilitySourceUpdatedAt": 1579811117.0, "findingSeverityCounts": { "MEDIUM": 1 } }, "registryId": "123456789012", "repositoryName": "sample-repo", "imageId": { "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6" }, "imageScanStatus": { "status": "COMPLETE", "description": "The scan was completed successfully." } }`For more information, see [Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [DescribeImageScanFindings](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-image-scan-findings.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-images`.

- **AWS CLI**
- 
            
                    **To describe an image in a repository**The following `describe-images`example displays details about an image in the`cluster-autoscaler`repository with the tag`v1.13.6`.`aws ecr describe-images \ --repository-name``cluster-autoscaler`\ --image-ids`imageTag=v1.13.6`Output: `{ "imageDetails": [ { "registryId": "012345678910", "repositoryName": "cluster-autoscaler", "imageDigest": "sha256:4a1c6567c38904384ebc64e35b7eeddd8451110c299e3368d2210066487d97e5", "imageTags": [ "v1.13.6" ], "imageSizeInBytes": 48318255, "imagePushedAt": 1565128275.0 } ] }`- 
                    For API details, see [DescribeImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-repositories`.

- **AWS CLI**
- 
            
                    **To describe the repositories in a registry**This example describes the repositories in the default registry for an account. Command: `aws ecr describe-repositories`Output: `{ "repositories": [ { "registryId": "012345678910", "repositoryName": "ubuntu", "repositoryArn": "arn:aws:ecr:us-west-2:012345678910:repository/ubuntu" }, { "registryId": "012345678910", "repositoryName": "test", "repositoryArn": "arn:aws:ecr:us-west-2:012345678910:repository/test" } ] }`- 
                    For API details, see [DescribeRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/describe-repositories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-authorization-token`.

- **AWS CLI**
- 
            
                    **To get an authorization token for your default registry**The following `get-authorization-token`example command gets an authorization token for your default registry.`aws ecr get-authorization-token`Output: `{ "authorizationData": [ { "authorizationToken": "QVdTOkN...", "expiresAt": 1448875853.241, "proxyEndpoint": "https://123456789012.dkr.ecr.us-west-2.amazonaws.com" } ] }`- 
                    For API details, see [GetAuthorizationToken](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-authorization-token.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-download-url-for-layer`.

- **AWS CLI**
- 
            
                    **To get the download URL of a layer**The following `get-download-url-for-layer`example displays the download URL of a layer with the digest`sha256:6171c7451a50945f8ddd72f7732cc04d7a0d1f48138a426b2e64387fdeb834ed`in the`cluster-autoscaler`repository.`aws ecr get-download-url-for-layer \ --repository-name``cluster-autoscaler`\ --layer-digest`sha256:6171c7451a50945f8ddd72f7732cc04d7a0d1f48138a426b2e64387fdeb834ed`Output: `{ "downloadUrl": "https://prod-us-west-2-starport-layer-bucket.s3.us-west-2.amazonaws.com/e501-012345678910-9cb60dc0-7284-5643-3987-da6dac0465f0/04620aac-66a5-4167-8232-55ee7ef6d565?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20190814T220617Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3600&X-Amz-Credential=AKIA32P3D2JDNMVAJLGF%2F20190814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=9161345894947a1672467a0da7a1550f2f7157318312fe4941b59976239c3337", "layerDigest": "sha256:6171c7451a50945f8ddd72f7732cc04d7a0d1f48138a426b2e64387fdeb834ed" }`- 
                    For API details, see [GetDownloadUrlForLayer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-download-url-for-layer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-lifecycle-policy-preview`.

- **AWS CLI**
- 
            
                    **To retrieve details for a lifecycle policy preview**The following `get-lifecycle-policy-preview`example retrieves the result of a lifecycle policy preview for the specified repository in the default registry for an account.Command: `aws ecr get-lifecycle-policy-preview \ --repository-name``"project-a/amazon-ecs-sample"`Output: `{ "registryId": "012345678910", "repositoryName": "project-a/amazon-ecs-sample", "lifecyclePolicyText": "{\n \"rules\": [\n {\n \"rulePriority\": 1,\n \"description\": \"Expire images older than 14 days\",\n \"selection\": {\n \"tagStatus\": \"untagged\",\n \"countType\": \"sinceImagePushed\",\n \"countUnit\": \"days\",\n \"countNumber\": 14\n },\n \"action\": {\n \"type\": \"expire\"\n }\n }\n ]\n}\n", "status": "COMPLETE", "previewResults": [], "summary": { "expiringImageTotalCount": 0 } }`For more information, see [Lifecycle Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [GetLifecyclePolicyPreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-lifecycle-policy-preview.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-lifecycle-policy`.

- **AWS CLI**
- 
            
                    **To retrieve a lifecycle policy**The following `get-lifecycle-policy`example displays details of the lifecycle policy for the specified repository in the default registry for the account.`aws ecr get-lifecycle-policy \ --repository-name``"project-a/amazon-ecs-sample"`Output: `{ "registryId": "123456789012", "repositoryName": "project-a/amazon-ecs-sample", "lifecyclePolicyText": "{\"rules\":[{\"rulePriority\":1,\"description\":\"Expire images older than 14 days\",\"selection\":{\"tagStatus\":\"untagged\",\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":14},\"action\":{\"type\":\"expire\"}}]}", "lastEvaluatedAt": 1504295007.0 }`For more information, see [Lifecycle Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [GetLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-lifecycle-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-login-password`.

- **AWS CLI**
- 
            
                    **To retrieve a password to authenticate to a registry**The following `get-login-password`displays a password that you can use with a container client of your choice to authenticate to any Amazon ECR registry that your IAM principal has access to.`aws ecr get-login-password`Output: `<password>`To use with the Docker CLI, pipe the output of the `get-login-password`command to the`docker login`command. When retrieving the password, ensure that you specify the same Region that your Amazon ECR registry exists in.`aws ecr get-login-password \ --region``<region>`\`|``docker``login`\ --username`AWS`\ --password-stdin`<aws_account_id>.dkr.ecr.<region>.amazonaws.com`For more information, see [Registry Authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Registries#registry_auth)in the*Amazon ECR User Guide*.- 
                    For API details, see [GetLoginPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-login-password.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-login`.

- **AWS CLI**
- 
            
                    **To retrieve a Docker login command to your default registry**This example prints a command that you can use to log in to your default Amazon ECR registry. Command: `aws ecr get-login`Output: `docker login -u AWS -p <password> -e none https://<aws_account_id>.dkr.ecr.<region>.amazonaws.com`**To log in to another account's registry**This example prints one or more commands that you can use to log in to Amazon ECR registries associated with other accounts. Command: `aws ecr get-login --registry-ids``012345678910``023456789012`Output: `docker login -u <username> -p <token-1> -e none <endpoint-1> docker login -u <username> -p <token-2> -e none <endpoint-2>`- 
                    For API details, see [GetLogin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-login.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-repository-policy`.

- **AWS CLI**
- 
            
                    **To retrieve the repository policy for a repository**The following `get-repository-policy`example displays details about the repository policy for the`cluster-autoscaler`repository.`aws ecr get-repository-policy \ --repository-name``cluster-autoscaler`Output: `{ "registryId": "012345678910", "repositoryName": "cluster-autoscaler", "policyText": "{\n \"Version\" : \"2008-10-17\",\n \"Statement\" : [ {\n \"Sid\" : \"allow public pull\",\n \"Effect\" : \"Allow\",\n \"Principal\" : \"*\",\n \"Action\" : [ \"ecr:BatchCheckLayerAvailability\", \"ecr:BatchGetImage\", \"ecr:GetDownloadUrlForLayer\" ]\n } ]\n}" }`- 
                    For API details, see [GetRepositoryPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-repository-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `initiate-layer-upload`.

- **AWS CLI**
- 
            
                    **To initiate an image layer upload**The following `initiate-layer-upload`example initiates an image layer upload to the`layer-test`repository.`aws ecr initiate-layer-upload \ --repository-name``layer-test`Output: `{ "partSize": 10485760, "uploadId": "6cb64b8a-9378-0e33-2ab1-b780fab8a9e9" }`- 
                    For API details, see [InitiateLayerUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/initiate-layer-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-images`.

- **AWS CLI**
- 
            
                    **To list the images in a repository**The following `list-images`example displays a list of the images in the`cluster-autoscaler`repository.`aws ecr list-images \ --repository-name``cluster-autoscaler`Output: `{ "imageIds": [ { "imageDigest": "sha256:99c6fb4377e9a420a1eb3b410a951c9f464eff3b7dbc76c65e434e39b94b6570", "imageTag": "v1.13.8" }, { "imageDigest": "sha256:99c6fb4377e9a420a1eb3b410a951c9f464eff3b7dbc76c65e434e39b94b6570", "imageTag": "v1.13.7" }, { "imageDigest": "sha256:4a1c6567c38904384ebc64e35b7eeddd8451110c299e3368d2210066487d97e5", "imageTag": "v1.13.6" } ] }`- 
                    For API details, see [ListImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags for repository**The following `list-tags-for-resource`example displays a list of the tags associated with the`hello-world`repository.`aws ecr list-tags-for-resource \ --resource-arn``arn:aws:ecr:us-west-2:012345678910:repository/hello-world`Output: `{ "tags": [ { "Key": "Stage", "Value": "Integ" } ] }`- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-image-scanning-configuration`.

- **AWS CLI**
- 
            
                    **To update the image scanning configuration for a repository**The following `put-image-scanning-configuration`example updates the image scanning configuration for the specified repository.`aws ecr put-image-scanning-configuration \ --repository-name``sample-repo`\ --image-scanning-configuration`scanOnPush=true`Output: `{ "registryId": "012345678910", "repositoryName": "sample-repo", "imageScanningConfiguration": { "scanOnPush": true } }`For more information, see [Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [PutImageScanningConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-image-scanning-configuration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-image-tag-mutability`.

- **AWS CLI**
- 
            
                    **To update the image tag mutability setting for a repository**The following `put-image-tag-mutability`example configures the specified repository for tag immutability. This prevents all image tags within the repository from being overwritten.`aws ecr put-image-tag-mutability \ --repository-name``hello-repository`\ --image-tag-mutability`IMMUTABLE`Output: `{ "registryId": "012345678910", "repositoryName": "sample-repo", "imageTagMutability": "IMMUTABLE" }`For more information, see [Image Tag Mutability](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-tag-mutability.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [PutImageTagMutability](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-image-tag-mutability.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-image`.

- **AWS CLI**
- 
            
                    **To retag an image with its manifest**The following `put-image`example creates a new tag in the`hello-world`repository with an existing image manifest.`aws ecr put-image \ --repository-name``hello-world`\ --image-tag`2019.08`\ --image-manifest`file://hello-world.manifest.json`Contents of `hello-world.manifest.json`:`{ "schemaVersion": 2, "mediaType": "application/vnd.docker.distribution.manifest.v2+json", "config": { "mediaType": "application/vnd.docker.container.image.v1+json", "size": 5695, "digest": "sha256:cea5fe7701b7db3dd1c372f3cea6f43cdda444fcc488f530829145e426d8b980" }, "layers": [ { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 39096921, "digest": "sha256:d8868e50ac4c7104d2200d42f432b661b2da8c1e417ccfae217e6a1e04bb9295" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 57938, "digest": "sha256:83251ac64627fc331584f6c498b3aba5badc01574e2c70b2499af3af16630eed" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 423, "digest": "sha256:589bba2f1b36ae56f0152c246e2541c5aa604b058febfcf2be32e9a304fec610" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 680, "digest": "sha256:d62ecaceda3964b735cdd2af613d6bb136a52c1da0838b2ff4b4dab4212bcb1c" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 162, "digest": "sha256:6d93b41cfc6bf0d2522b7cf61588de4cd045065b36c52bd3aec2ba0622b2b22b" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 28268840, "digest": "sha256:6986b4d4c07932c680b3587f2eac8b0e013568c003cc23b04044628a5c5e599f" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 35369152, "digest": "sha256:8c5ec60f10102dc8da0649d866c7c2f706e459d0bdc25c83ad2de86f4996c276" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 155, "digest": "sha256:cde50b1c594539c5f67cbede9aef95c9ae321ccfb857f7b251b45b84198adc85" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 28737, "digest": "sha256:2e102807ab72a73fc9abf53e8c50e421bdc337a0a8afcb242176edeec65977e4" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 190, "digest": "sha256:fc379bbd5ed37808772bef016553a297356c59b8f134659e6ee4ecb563c2f5a7" }, { "mediaType": "application/vnd.docker.image.rootfs.diff.tar.gzip", "size": 28748, "digest": "sha256:021db240dfccf5a1aff19507d17c0177e5888e518acf295b52204b1825e8b7ee" } ] }`Output: `{ "image": { "registryId": "130757420319", "repositoryName": "hello-world", "imageId": { "imageDigest": "sha256:8ece96b74f87652876199d83bd107d0435a196133af383ac54cb82b6cc5283ae", "imageTag": "2019.08" }, "imageManifest": "{\n \"schemaVersion\": 2,\n \"mediaType\": \"application/vnd.docker.distribution.manifest.v2+json\",\n \"config\": {\n \"mediaType\": \"application/vnd.docker.container.image.v1+json\",\n \"size\": 5695,\n \"digest\": \"sha256:cea5fe7701b7db3dd1c372f3cea6f43cdda444fcc488f530829145e426d8b980\"\n },\n \"layers\": [\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 39096921,\n \"digest\": \"sha256:d8868e50ac4c7104d2200d42f432b661b2da8c1e417ccfae217e6a1e04bb9295\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 57938,\n \"digest\": \"sha256:83251ac64627fc331584f6c498b3aba5badc01574e2c70b2499af3af16630eed\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 423,\n \"digest\": \"sha256:589bba2f1b36ae56f0152c246e2541c5aa604b058febfcf2be32e9a304fec610\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 680,\n \"digest\": \"sha256:d62ecaceda3964b735cdd2af613d6bb136a52c1da0838b2ff4b4dab4212bcb1c\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 162,\n \"digest\": \"sha256:6d93b41cfc6bf0d2522b7cf61588de4cd045065b36c52bd3aec2ba0622b2b22b\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 28268840,\n \"digest\": \"sha256:6986b4d4c07932c680b3587f2eac8b0e013568c003cc23b04044628a5c5e599f\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 35369152,\n \"digest\": \"sha256:8c5ec60f10102dc8da0649d866c7c2f706e459d0bdc25c83ad2de86f4996c276\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 155,\n \"digest\": \"sha256:cde50b1c594539c5f67cbede9aef95c9ae321ccfb857f7b251b45b84198adc85\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 28737,\n \"digest\": \"sha256:2e102807ab72a73fc9abf53e8c50e421bdc337a0a8afcb242176edeec65977e4\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 190,\n \"digest\": \"sha256:fc379bbd5ed37808772bef016553a297356c59b8f134659e6ee4ecb563c2f5a7\"\n },\n {\n \"mediaType\": \"application/vnd.docker.image.rootfs.diff.tar.gzip\",\n \"size\": 28748,\n \"digest\": \"sha256:021db240dfccf5a1aff19507d17c0177e5888e518acf295b52204b1825e8b7ee\"\n }\n ]\n}\n" } }`- 
                    For API details, see [PutImage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-image.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-lifecycle-policy`.

- **AWS CLI**
- 
            
                    **To create a lifecycle policy**The following `put-lifecycle-policy`example creates a lifecycle policy for the specified repository in the default registry for an account.`aws ecr put-lifecycle-policy \ --repository-name``"project-a/amazon-ecs-sample"`\ --lifecycle-policy-text`"file://policy.json"`Contents of `policy.json`:`{ "rules": [ { "rulePriority": 1, "description": "Expire images older than 14 days", "selection": { "tagStatus": "untagged", "countType": "sinceImagePushed", "countUnit": "days", "countNumber": 14 }, "action": { "type": "expire" } } ] }`Output: `{ "registryId": "<aws_account_id>", "repositoryName": "project-a/amazon-ecs-sample", "lifecyclePolicyText": "{\"rules\":[{\"rulePriority\":1,\"description\":\"Expire images older than 14 days\",\"selection\":{\"tagStatus\":\"untagged\",\"countType\":\"sinceImagePushed\",\"countUnit\":\"days\",\"countNumber\":14},\"action\":{\"type\":\"expire\"}}]}" }`For more information, see [Lifecycle Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [PutLifeCyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/put-life-cycle-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `set-repository-policy`.

- **AWS CLI**
- 
            
                    **To set the repository policy for a repository**The following `set-repository-policy`example attaches a repository policy contained in a file to the`cluster-autoscaler`repository.`aws ecr set-repository-policy \ --repository-name``cluster-autoscaler`\ --policy-text`file://my-policy.json`Contents of `my-policy.json`:`{ "Version":"2012-10-17", "Statement" : [ { "Sid" : "allow public pull", "Effect" : "Allow", "Principal" : "*", "Action" : [ "ecr:BatchCheckLayerAvailability", "ecr:BatchGetImage", "ecr:GetDownloadUrlForLayer" ] } ] }`Output: `{ "registryId": "012345678910", "repositoryName": "cluster-autoscaler", "policyText": "{\n \"Version\" : \"2008-10-17\",\n \"Statement\" : [ {\n \"Sid\" : \"allow public pull\",\n \"Effect\" : \"Allow\",\n \"Principal\" : \"*\",\n \"Action\" : [ \"ecr:BatchCheckLayerAvailability\", \"ecr:BatchGetImage\", \"ecr:GetDownloadUrlForLayer\" ]\n } ]\n}" }`- 
                    For API details, see [SetRepositoryPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/set-repository-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-image-scan`.

- **AWS CLI**
- 
            
                    **To start an image vulnerability scan**The following `start-image-scan`example starts an image scan for and specified by the image digest in the specified repository.`aws ecr start-image-scan \ --repository-name``sample-repo`\ --image-id`imageDigest=sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6`Output: `{ "registryId": "012345678910", "repositoryName": "sample-repo", "imageId": { "imageDigest": "sha256:74b2c688c700ec95a93e478cdb959737c148df3fbf5ea706abe0318726e885e6" }, "imageScanStatus": { "status": "IN_PROGRESS" } }`For more information, see [Image Scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html)in the*Amazon ECR User Guide*.- 
                    For API details, see [StartImageScan](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/start-image-scan.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-lifecycle-policy-preview`.

- **AWS CLI**
- 
            
                    **To create a lifecycle policy preview**The following `start-lifecycle-policy-preview`example creates a lifecycle policy preview defined by a JSON file for the specified repository.`aws ecr start-lifecycle-policy-preview \ --repository-name``"project-a/amazon-ecs-sample"`\ --lifecycle-policy-text`"file://policy.json"`Contents of `policy.json`:`{ "rules": [ { "rulePriority": 1, "description": "Expire images older than 14 days", "selection": { "tagStatus": "untagged", "countType": "sinceImagePushed", "countUnit": "days", "countNumber": 14 }, "action": { "type": "expire" } } ] }`Output: `{ "registryId": "012345678910", "repositoryName": "project-a/amazon-ecs-sample", "lifecyclePolicyText": "{\n \"rules\": [\n {\n \"rulePriority\": 1,\n \"description\": \"Expire images older than 14 days\",\n \"selection\": {\n \"tagStatus\": \"untagged\",\n \"countType\": \"sinceImagePushed\",\n \"countUnit\": \"days\",\n \"countNumber\": 14\n },\n \"action\": {\n \"type\": \"expire\"\n }\n }\n ]\n}\n", "status": "IN_PROGRESS" }`- 
                    For API details, see [StartLifecyclePolicyPreview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/start-lifecycle-policy-preview.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a repository**The following `tag-resource`example sets a tag with key`Stage`and value`Integ`on the`hello-world`repository.`aws ecr tag-resource \ --resource-arn``arn:aws:ecr:us-west-2:012345678910:repository/hello-world`\ --tags`Key=Stage,Value=Integ`This command produces no output. - 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To untag a repository**The following `untag-resource`example removes the tag with the key`Stage`from the`hello-world`repository.`aws ecr untag-resource \ --resource-arn``arn:aws:ecr:us-west-2:012345678910:repository/hello-world`\ --tag-keys`Stage`This command produces no output. - 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-layer-part`.

- **AWS CLI**
- 
            
                    **To upload a layer part**This following `upload-layer-part`uploads an image layer part to the`layer-test`repository.`aws ecr upload-layer-part \ --repository-name``layer-test`\ --upload-id`6cb64b8a-9378-0e33-2ab1-b780fab8a9e9`\ --part-first-byte`0`\ --part-last-byte`8323314`\ --layer-part-blob`file:///var/lib/docker/image/overlay2/layerdb/sha256/ff986b10a018b48074e6d3a68b39aad8ccc002cdad912d4148c0f92b3729323e/layer.b64`Output: `{ "uploadId": "6cb64b8a-9378-0e33-2ab1-b780fab8a9e9", "registryId": "012345678910", "lastByteReceived": 8323314, "repositoryName": "layer-test" }`- 
                    For API details, see [UploadLayerPart](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/upload-layer-part.html)in*AWS CLI Command Reference*.
 
-