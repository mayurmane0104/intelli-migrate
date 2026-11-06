# CodeBuild examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_codebuild_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_codebuild_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CodeBuild.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-delete-builds`.

- **AWS CLI**
- 
            
                    **To delete builds in AWS CodeBuild.**The following `batch-delete-builds`example deletes builds in CodeBuild with the specified IDs.`aws codebuild batch-delete-builds --ids``my-build-project-one:a1b2c3d4-5678-9012-abcd-11111EXAMPLE``my-build-project-two:a1b2c3d4-5678-9012-abcd-22222EXAMPLE`Output: `{ "buildsNotDeleted": [ { "id": "arn:aws:codebuild:us-west-2:123456789012:build/my-build-project-one:a1b2c3d4-5678-9012-abcd-11111EXAMPLE", "statusCode": "BUILD_IN_PROGRESS" } ], "buildsDeleted": [ "arn:aws:codebuild:us-west-2:123456789012:build/my-build-project-two:a1b2c3d4-5678-9012-abcd-22222EXAMPLE" ] }`For more information, see [Delete Builds (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/delete-builds.html#delete-builds-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [BatchDeleteBuilds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-delete-builds.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-build-batches`.

- **AWS CLI**
- 
            
                    **To view details of builds in AWS CodeBuild.**The following `batch-get-build-batches`example gets information about build batches in CodeBuild with the specified IDs.`aws codebuild batch-get-build-batches \ --ids``codebuild-demo-project:e9c4f4df-3f43-41d2-ab3a-60fe2EXAMPLE`Output: `{ "buildBatches": [ { "id": "codebuild-demo-project:e9c4f4df-3f43-41d2-ab3a-60fe2EXAMPLE", "arn": "arn:aws:codebuild:us-west-2:123456789012:build-batch/codebuild-demo-project:e9c4f4df-3f43-41d2-ab3a-60fe2EXAMPLE", "startTime": "2020-11-03T21:52:20.775000+00:00", "endTime": "2020-11-03T21:56:59.784000+00:00", "currentPhase": "SUCCEEDED", "buildBatchStatus": "SUCCEEDED", "resolvedSourceVersion": "0a6546f68309560d08a310daac92314c4d378f6b", "projectName": "codebuild-demo-project", "phases": [ { "phaseType": "SUBMITTED", "phaseStatus": "SUCCEEDED", "startTime": "2020-11-03T21:52:20.775000+00:00", "endTime": "2020-11-03T21:52:20.976000+00:00", "durationInSeconds": 0 }, { "phaseType": "DOWNLOAD_BATCHSPEC", "phaseStatus": "SUCCEEDED", "startTime": "2020-11-03T21:52:20.976000+00:00", "endTime": "2020-11-03T21:52:57.401000+00:00", "durationInSeconds": 36 }, { "phaseType": "IN_PROGRESS", "phaseStatus": "SUCCEEDED", "startTime": "2020-11-03T21:52:57.401000+00:00", "endTime": "2020-11-03T21:56:59.751000+00:00", "durationInSeconds": 242 }, { "phaseType": "COMBINE_ARTIFACTS", "phaseStatus": "SUCCEEDED", "startTime": "2020-11-03T21:56:59.751000+00:00", "endTime": "2020-11-03T21:56:59.784000+00:00", "durationInSeconds": 0 }, { "phaseType": "SUCCEEDED", "startTime": "2020-11-03T21:56:59.784000+00:00" } ], "source": { "type": "GITHUB", "location": "https://github.com/my-repo/codebuild-demo-project.git", "gitCloneDepth": 1, "gitSubmodulesConfig": { "fetchSubmodules": false }, "reportBuildStatus": false, "insecureSsl": false }, "secondarySources": [], "secondarySourceVersions": [], "artifacts": { "location": "" }, "secondaryArtifacts": [], "cache": { "type": "NO_CACHE" }, "environment": { "type": "LINUX_CONTAINER", "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0", "computeType": "BUILD_GENERAL1_SMALL", "environmentVariables": [], "privilegedMode": false, "imagePullCredentialsType": "CODEBUILD" }, "logConfig": { "cloudWatchLogs": { "status": "ENABLED" }, "s3Logs": { "status": "DISABLED", "encryptionDisabled": false } }, "buildTimeoutInMinutes": 60, "queuedTimeoutInMinutes": 480, "complete": true, "initiator": "Strohm", "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "buildBatchNumber": 6, "buildBatchConfig": { "serviceRole": "arn:aws:iam::123456789012:role/service-role/codebuild-demo-project", "restrictions": { "maximumBuildsAllowed": 100 }, "timeoutInMins": 480 }, "buildGroups": [ { "identifier": "DOWNLOAD_SOURCE", "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:us-west-2:123456789012:build/codebuild-demo-project:379737d8-bc35-48ec-97fd-776d27545315", "requestedOn": "2020-11-03T21:52:21.394000+00:00", "buildStatus": "SUCCEEDED", "primaryArtifact": { "type": "no_artifacts", "identifier": "DOWNLOAD_SOURCE" }, "secondaryArtifacts": [] } }, { "identifier": "linux_small", "dependsOn": [], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:us-west-2:123456789012:build/codebuild-demo-project:dd785171-ed84-4bb6-8ede-ceeb86e54bdb", "requestedOn": "2020-11-03T21:52:57.604000+00:00", "buildStatus": "SUCCEEDED", "primaryArtifact": { "type": "no_artifacts", "identifier": "linux_small" }, "secondaryArtifacts": [] } }, { "identifier": "linux_medium", "dependsOn": [ "linux_small" ], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:us-west-2:123456789012:build/codebuild-demo-project:97cf7bd4-5313-4786-8243-4aef350a1267", "requestedOn": "2020-11-03T21:54:18.474000+00:00", "buildStatus": "SUCCEEDED", "primaryArtifact": { "type": "no_artifacts", "identifier": "linux_medium" }, "secondaryArtifacts": [] } }, { "identifier": "linux_large", "dependsOn": [ "linux_medium" ], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:us-west-2:123456789012:build/codebuild-demo-project:60a194cd-0d03-4337-9db1-d41476a17d27", "requestedOn": "2020-11-03T21:55:39.203000+00:00", "buildStatus": "SUCCEEDED", "primaryArtifact": { "type": "no_artifacts", "identifier": "linux_large" }, "secondaryArtifacts": [] } } ] } ], "buildBatchesNotFound": [] }`For more information, see Batch builds in AWS CodeBuild <https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html>)__ in the *AWS CodeBuild User Guide*.- 
                    For API details, see [BatchGetBuildBatches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-get-build-batches.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-builds`.

- **AWS CLI**
- 
            
                    **To view details of builds in AWS CodeBuild.**The following `batch-get-builds`example gets information about builds in CodeBuild with the specified IDs.`aws codebuild batch-get-builds --ids``codebuild-demo-project:e9c4f4df-3f43-41d2-ab3a-60fe2EXAMPLE``codebuild-demo-project:815e755f-bade-4a7e-80f0-efe51EXAMPLE`Output: `{ "buildsNotFound": [], "builds": [ { "artifacts": { "md5sum": "0e95edf915048a0c22efe6d139fff837", "location": "arn:aws:s3:::codepipeline-us-west-2-820783811474/CodeBuild-Python-Pip/BuildArtif/6DJsqQa", "encryptionDisabled": false, "sha256sum": "cfa0df33a090966a737f64ae4fe498969fdc842a0c9aec540bf93c37ac0d05a2" }, "logs": { "cloudWatchLogs": { "status": "ENABLED" }, "s3Logs": { "status": "DISABLED" }, "streamName": "46472baf-8f6b-43c2-9255-b3b963af2732", "groupName": "/aws/codebuild/codebuild-demo-project", "deepLink": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/codebuild-demo-project;stream=46472baf-8f6b-43c2-9255-b3b963af2732" }, "timeoutInMinutes": 60, "environment": { "privilegedMode": false, "computeType": "BUILD_GENERAL1_MEDIUM", "image": "aws/codebuild/windows-base:1.0", "environmentVariables": [], "type": "WINDOWS_CONTAINER" }, "projectName": "codebuild-demo-project", "buildComplete": true, "source": { "gitCloneDepth": 1, "insecureSsl": false, "type": "CODEPIPELINE" }, "buildStatus": "SUCCEEDED", "secondaryArtifacts": [], "phases": [ { "durationInSeconds": 0, "startTime": 1548717462.122, "phaseType": "SUBMITTED", "endTime": 1548717462.484, "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 0, "startTime": 1548717462.484, "phaseType": "QUEUED", "endTime": 1548717462.775, "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 34, "endTime": 1548717496.909, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717462.775, "phaseType": "PROVISIONING", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 15, "endTime": 1548717512.555, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717496.909, "phaseType": "DOWNLOAD_SOURCE", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 0, "endTime": 1548717512.734, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717512.555, "phaseType": "INSTALL", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 0, "endTime": 1548717512.924, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717512.734, "phaseType": "PRE_BUILD", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 9, "endTime": 1548717522.254, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717512.924, "phaseType": "BUILD", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 3, "endTime": 1548717525.498, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717522.254, "phaseType": "POST_BUILD", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 9, "endTime": 1548717534.646, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717525.498, "phaseType": "UPLOAD_ARTIFACTS", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 2, "endTime": 1548717536.846, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548717534.646, "phaseType": "FINALIZING", "phaseStatus": "SUCCEEDED" }, { "startTime": 1548717536.846, "phaseType": "COMPLETED" } ], "startTime": 1548717462.122, "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "initiator": "codepipeline/CodeBuild-Pipeline", "secondarySources": [], "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role", "currentPhase": "COMPLETED", "id": "codebuild-demo-project:e9c4f4df-3f43-41d2-ab3a-60fe2EXAMPLE", "cache": { "type": "NO_CACHE" }, "sourceVersion": "arn:aws:s3:::codepipeline-us-west-2-820783811474/CodeBuild-Python-Pip/SourceArti/1TspnN3.zip", "endTime": 1548717536.846, "arn": "arn:aws:codebuild:us-west-2:123456789012:build/codebuild-demo-project:e9c4f4df-3f43-41d2-ab3a-60fe2EXAMPLE", "queuedTimeoutInMinutes": 480, "resolvedSourceVersion": "f2194c1757bbdcb0f8f229254a4b3c8b27d43e0b" }, { "artifacts": { "md5sum": "", "overrideArtifactName": false, "location": "arn:aws:s3:::my-artifacts/codebuild-demo-project", "encryptionDisabled": false, "sha256sum": "" }, "logs": { "cloudWatchLogs": { "status": "ENABLED" }, "s3Logs": { "status": "DISABLED" }, "streamName": "4dea3ca4-20ec-4898-b22a-a9eb9292775d", "groupName": "/aws/codebuild/codebuild-demo-project", "deepLink": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/codebuild-demo-project;stream=4dea3ca4-20ec-4898-b22a-a9eb9292775d" }, "timeoutInMinutes": 60, "environment": { "privilegedMode": false, "computeType": "BUILD_GENERAL1_MEDIUM", "image": "aws/codebuild/windows-base:1.0", "environmentVariables": [], "type": "WINDOWS_CONTAINER" }, "projectName": "codebuild-demo-project", "buildComplete": true, "source": { "gitCloneDepth": 1, "location": "https://github.com/my-repo/codebuild-demo-project.git", "insecureSsl": false, "reportBuildStatus": false, "type": "GITHUB" }, "buildStatus": "SUCCEEDED", "secondaryArtifacts": [], "phases": [ { "durationInSeconds": 0, "startTime": 1548716241.89, "phaseType": "SUBMITTED", "endTime": 1548716242.241, "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 0, "startTime": 1548716242.241, "phaseType": "QUEUED", "endTime": 1548716242.536, "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 33, "endTime": 1548716276.171, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716242.536, "phaseType": "PROVISIONING", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 15, "endTime": 1548716291.809, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716276.171, "phaseType": "DOWNLOAD_SOURCE", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 0, "endTime": 1548716291.993, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716291.809, "phaseType": "INSTALL", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 0, "endTime": 1548716292.191, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716291.993, "phaseType": "PRE_BUILD", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 9, "endTime": 1548716301.622, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716292.191, "phaseType": "BUILD", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 3, "endTime": 1548716304.783, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716301.622, "phaseType": "POST_BUILD", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 8, "endTime": 1548716313.775, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716304.783, "phaseType": "UPLOAD_ARTIFACTS", "phaseStatus": "SUCCEEDED" }, { "durationInSeconds": 2, "endTime": 1548716315.935, "contexts": [ { "statusCode": "", "message": "" } ], "startTime": 1548716313.775, "phaseType": "FINALIZING", "phaseStatus": "SUCCEEDED" }, { "startTime": 1548716315.935, "phaseType": "COMPLETED" } ], "startTime": 1548716241.89, "secondarySourceVersions": [], "initiator": "my-codebuild-project", "arn": "arn:aws:codebuild:us-west-2:123456789012:build/codebuild-demo-project:815e755f-bade-4a7e-80f0-efe51EXAMPLE", "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role", "currentPhase": "COMPLETED", "id": "codebuild-demo-project:815e755f-bade-4a7e-80f0-efe51EXAMPLE", "cache": { "type": "NO_CACHE" }, "endTime": 1548716315.935, "secondarySources": [], "queuedTimeoutInMinutes": 480, "resolvedSourceVersion": "f2194c1757bbdcb0f8f229254a4b3c8b27d43e0b" } ] }`For more information, see [View Build Details (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-details.html#view-build-details-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [BatchGetBuilds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-get-builds.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-projects`.

- **AWS CLI**
- 
            
                    **To get a list of AWS CodeBuild build project names.**The following `batch-get-projects`example gets a list of CodeBuild build projects specified by name.`aws codebuild batch-get-projects --names``codebuild-demo-project``codebuild-demo-project2``my-other-demo-project`In the following output, the `projectsNotFound`array lists any build project names that were specified, but not found. The`projects`array lists details for each build project where information was found.`{ "projectsNotFound": [], "projects": [ { "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "name": "codebuild-demo-project2", "queuedTimeoutInMinutes": 480, "timeoutInMinutes": 60, "source": { "buildspec": "version: 0.2\n\n#env:\n #variables:\n # key: \"value\"\n # key: \"value\"\n #parameter-store:\n # key: \"value\"\n # key:\"value\"\n\nphases:\n #install:\n #commands:\n # - command\n # - command\n #pre_build:\n #commands:\n # - command\n # - command\n build:\n commands:\n # - command\n # - command\n #post_build:\n #commands:\n # - command\n # - command\n#artifacts:\n #files:\n # - location\n # - location\n #name: $(date +%Y-%m-%d)\n #discard-paths: yes\n #base-directory: location\n#cache:\n #paths:\n # - paths", "type": "NO_SOURCE", "insecureSsl": false, "gitCloneDepth": 1 }, "artifacts": { "type": "NO_ARTIFACTS" }, "badge": { "badgeEnabled": false }, "lastModified": 1540588091.108, "created": 1540588091.108, "arn": "arn:aws:codebuild:us-west-2:123456789012:project/test-for-sample", "secondarySources": [], "secondaryArtifacts": [], "cache": { "type": "NO_CACHE" }, "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-test-role", "environment": { "image": "aws/codebuild/java:openjdk-8", "privilegedMode": true, "type": "LINUX_CONTAINER", "computeType": "BUILD_GENERAL1_SMALL", "environmentVariables": [] }, "tags": [] }, { "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "name": "my-other-demo-project", "queuedTimeoutInMinutes": 480, "timeoutInMinutes": 60, "source": { "location": "https://github.com/iversonic/codedeploy-sample.git", "reportBuildStatus": false, "buildspec": "buildspec.yml", "insecureSsl": false, "gitCloneDepth": 1, "type": "GITHUB", "auth": { "type": "OAUTH" } }, "artifacts": { "type": "NO_ARTIFACTS" }, "badge": { "badgeEnabled": false }, "lastModified": 1523401711.73, "created": 1523401711.73, "arn": "arn:aws:codebuild:us-west-2:123456789012:project/Project2", "cache": { "type": "NO_CACHE" }, "serviceRole": "arn:aws:iam::123456789012:role/service-role/codebuild-Project2-service-role", "environment": { "image": "aws/codebuild/nodejs:4.4.7", "privilegedMode": false, "type": "LINUX_CONTAINER", "computeType": "BUILD_GENERAL1_SMALL", "environmentVariables": [] }, "tags": [] } ] }`For more information, see [View a Build Project's Details (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/view-project-details.html#view-project-details-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [BatchGetProjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-get-projects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-report-groups`.

- **AWS CLI**
- 
            
                    **To get information about one or more report groups in AWS CodeBuild.**The following `batch-get-report-groups`example retrieves information about the report group with the specified ARN.`aws codebuild batch-get-report-groups \ --report-group-arns``arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>`Output: `{ "reportGroups": [ { "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>", "name": "report-group-name", "type": "TEST", "exportConfig": { "exportConfigType": "NO_EXPORT" }, "created": "2020-10-01T18:04:08.466000+00:00", "lastModified": "2020-10-01T18:04:08.466000+00:00", "tags": [] } ], "reportGroupsNotFound": [] }`For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [BatchGetReportGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-get-report-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-reports`.

- **AWS CLI**
- 
            
                    **To get information about one or more reports in AWS CodeBuild.**The following `batch-get-reports`example retrieves information about the reports with the specified ARNs.`aws codebuild batch-get-reports \ --report-arns``arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report``1``ID>``arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report``2``ID>`Output: `{ "reports": [ { "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report 1 ID>", "type": "TEST", "name": "<report-group-name>", "reportGroupArn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>", "executionId": "arn:aws:codebuild:<region-ID>:<user-ID>:build/test-reports:<ID>", "status": "FAILED", "created": "2020-10-01T11:25:22.531000-07:00", "expired": "2020-10-31T11:25:22-07:00", "exportConfig": { "exportConfigType": "NO_EXPORT" }, "truncated": false, "testSummary": { "total": 28, "statusCounts": { "ERROR": 5, "FAILED": 1, "SKIPPED": 4, "SUCCEEDED": 18, "UNKNOWN": 0 }, "durationInNanoSeconds": 94000000 } }, { "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report 2 ID>", "type": "TEST", "name": "<report-group-name>", "reportGroupArn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>", "executionId": "arn:aws:codebuild:<region-ID>:<user-ID>:build/test-reports:<ID>", "status": "FAILED", "created": "2020-10-01T11:13:05.816000-07:00", "expired": "2020-10-31T11:13:05-07:00", "exportConfig": { "exportConfigType": "NO_EXPORT" }, "truncated": false, "testSummary": { "total": 28, "statusCounts": { "ERROR": 5, "FAILED": 1, "SKIPPED": 4, "SUCCEEDED": 18, "UNKNOWN": 0 }, "durationInNanoSeconds": 94000000 } } ], "reportsNotFound": [] }`For more information, see [Working with reports](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [BatchGetReports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/batch-get-reports.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-project`.

- **AWS CLI**
- 
            
                    **Example 1: To create an AWS CodeBuild build project**The following `create-project`example creates a CodeBuild build project using source files from an S3 bucket`aws codebuild create-project \ --name``"my-demo-project"`\ --source "{\"type\": \"S3\",\"location\": \"codebuild-us-west-2-123456789012-input-bucket/my-source.zip\"}" \ --artifacts {"\"type\": \"S3\",\"location\": \"codebuild-us-west-2-123456789012-output-bucket\""} \ --environment "{\"type\": \"LINUX_CONTAINER\",\"image\": \"aws/codebuild/standard:1.0\",\"computeType\": \"BUILD_GENERAL1_SMALL\"}" \ --service-role`"arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role"`Output: `{ "project": { "arn": "arn:aws:codebuild:us-west-2:123456789012:project/my-demo-project", "name": "my-cli-demo-project", "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role", "lastModified": 1556839783.274, "badge": { "badgeEnabled": false }, "queuedTimeoutInMinutes": 480, "environment": { "image": "aws/codebuild/standard:1.0", "computeType": "BUILD_GENERAL1_SMALL", "type": "LINUX_CONTAINER", "imagePullCredentialsType": "CODEBUILD", "privilegedMode": false, "environmentVariables": [] }, "artifacts": { "location": "codebuild-us-west-2-123456789012-output-bucket", "name": "my-cli-demo-project", "namespaceType": "NONE", "type": "S3", "packaging": "NONE", "encryptionDisabled": false }, "source": { "type": "S3", "location": "codebuild-us-west-2-123456789012-input-bucket/my-source.zip", "insecureSsl": false }, "timeoutInMinutes": 60, "cache": { "type": "NO_CACHE" }, "created": 1556839783.274 } }`**Example 2: To create an AWS CodeBuild build project using a JSON input file for the parameters**The following `create-project`example creates a CodeBuild build project by passing all of the required parameters in a JSON input file. Create the input file template by running the command with only the`--generate-cli-skeleton parameter`.`aws codebuild create-project --cli-input-json``file://create-project.json`The input JSON file `create-project.json`contains the following content:`{ "name": "codebuild-demo-project", "source": { "type": "S3", "location": "codebuild-region-ID-account-ID-input-bucket/MessageUtil.zip" }, "artifacts": { "type": "S3", "location": "codebuild-region-ID-account-ID-output-bucket" }, "environment": { "type": "LINUX_CONTAINER", "image": "aws/codebuild/standard:1.0", "computeType": "BUILD_GENERAL1_SMALL" }, "serviceRole": "serviceIAMRole" }`Output: `{ "project": { "name": "codebuild-demo-project", "serviceRole": "serviceIAMRole", "tags": [], "artifacts": { "packaging": "NONE", "type": "S3", "location": "codebuild-region-ID-account-ID-output-bucket", "name": "message-util.zip" }, "lastModified": 1472661575.244, "timeoutInMinutes": 60, "created": 1472661575.244, "environment": { "computeType": "BUILD_GENERAL1_SMALL", "image": "aws/codebuild/standard:1.0", "type": "LINUX_CONTAINER", "environmentVariables": [] }, "source": { "type": "S3", "location": "codebuild-region-ID-account-ID-input-bucket/MessageUtil.zip" }, "encryptionKey": "arn:aws:kms:region-ID:account-ID:alias/aws/s3", "arn": "arn:aws:codebuild:region-ID:account-ID:project/codebuild-demo-project" } }`For more information, see [Create a Build Project (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project.html#create-project-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [CreateProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/create-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-report-group`.

- **AWS CLI**
- 
            
                    **To create a report group in AWS CodeBuild.**The following `create-report-group`example creates a new report group.`aws codebuild create-report-group \ --cli-input-json``file://create-report-group-source.json`Contents of create-report-group-source.json: `{ "name": "cli-created-report-group", "type": "TEST", "exportConfig": { "exportConfigType": "S3", "s3Destination": { "bucket": "amzn-s3-demo-bucket", "path": "", "packaging": "ZIP", "encryptionDisabled": true } } }`Output: `{ "reportGroup": { "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/cli-created-report-group", "name": "cli-created-report-group", "type": "TEST", "exportConfig": { "exportConfigType": "S3", "s3Destination": { "bucket": "amzn-s3-demo-bucket", "path": "", "packaging": "ZIP", "encryptionDisabled": true } }, "created": 1602020026.775, "lastModified": 1602020026.775 } }`For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [CreateReportGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/create-report-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-webhook`.

- **AWS CLI**
- 
            
                    **To create webhook filters for an AWS CodeBuild project**The following `create-webhook`example creates a webhook for a CodeBuild project named`my-project`that has two filter groups. The first filter group specifies pull requests that are created, updated, or reopened on branches with Git reference names that match the regular expression`^refs/heads/master$`and head references that match`^refs/heads/myBranch$`. The second filter group specifies push requests on branches with Git reference names that do not match the regular expression`^refs/heads/myBranch$`.`aws codebuild create-webhook \ --project-name``my-project`\ --filter-groups "[[{\"type\":\"EVENT\",\"pattern\":\"PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_REOPENED\"},{\"type\":\"HEAD_REF\",\"pattern\":\"^refs/heads/myBranch$\",\"excludeMatchedPattern\":true},{\"type\":\"BASE_REF\",\"pattern\":\"^refs/heads/master$\",\"excludeMatchedPattern\":true}],[{\"type\":\"EVENT\",\"pattern\":\"PUSH\"},{\"type\":\"HEAD_REF\",\"pattern\":\"^refs/heads/myBranch$\",\"excludeMatchedPattern\":true}]]"Output: `{ "webhook": { "payloadUrl": "https://codebuild.us-west-2.amazonaws.com/webhooks?t=eyJlbmNyeXB0ZWREYXRhIjoiVVl5MGtoeGRwSzZFRXl2Wnh4bld1Z0tKZ291TVpQNEtFamQ3RDlDYWpRaGIreVFrdm9EQktIVk1NeHJEWEpmUDUrVUNOMUIyRHJRc1VxcHJ6QlNDSnljPSIsIml2UGFyYW1ldGVyU3BlYyI6InN4Tm1SeUt5MUhaUVRWbGciLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&v=1", "url": "https://api.github.com/repos/iversonic/codedeploy-sample/hooks/105190656", "lastModifiedSecret": 1556311319.069, "filterGroups": [ [ { "type": "EVENT", "pattern": "PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_REOPENED", "excludeMatchedPattern": false }, { "type": "HEAD_REF", "pattern": "refs/heads/myBranch$", "excludeMatchedPattern": true }, { "type": "BASE_REF", "pattern": "refs/heads/master$", "excludeMatchedPattern": true } ], [ { "type": "EVENT", "pattern": "PUSH", "excludeMatchedPattern": false }, { "type": "HEAD_REF", "pattern": "refs/heads/myBranch$", "excludeMatchedPattern": true } ] ] } }`For more information, see [Filter GitHub Webhook Events (SDK)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-github-pull-request.html#sample-github-pull-request-filter-webhook-events-sdk)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [CreateWebhook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/create-webhook.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-build-batch`.

- **AWS CLI**
- 
            
                    **To delete a batch build in AWS CodeBuild.**The following `delete-build-batch`example deletes the specified batch build.`aws codebuild delete-build-batch \ --id``<project-name>:<batch-ID>`Output: `{ "statusCode": "BATCH_DELETED", "buildsDeleted": [ "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>" ], "buildsNotDeleted": [] }`For more information, see [Batch builds in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DeleteBuildBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-build-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-project`.

- **AWS CLI**
- 
            
                    **To delete an AWS CodeBuild build project**The following `delete-project`example deletes the specified CodeBuild build project.`aws codebuild delete-project --name``my-project`This command produces no output. For more information, see [Delete a Build Project (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/delete-project.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DeleteProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-report-group`.

- **AWS CLI**
- 
            
                    **To delete a report groups in AWS CodeBuild.**The following `delete-report-group`example deletes the report group with the specified ARN.`aws codebuild delete-report-group \ --arn``arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>`This command produces no output. For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DeleteReportGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-report-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-report`.

- **AWS CLI**
- 
            
                    **To delete a report in AWS CodeBuild.**The following `delete-report`example deletes the specified report.`aws codebuild delete-report \ --arn``arn:aws:codebuild:<region-ID>:<account-ID>:report/<report-group-name>:<report-ID>`This command produces no output. For more information, see [Working with reports](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DeleteReport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-report.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-source-credentials`.

- **AWS CLI**
- 
            
                    **To disconnect from a source provider and remove its access tokens.**The following `delete-source-credentials`example disconnects from a source provider and removes its tokens. The ARN of source credentials used to connect to the source provider determines which source credentials.`aws codebuild delete-source-credentials --arn``arn-of-your-credentials`Output: `{ "arn": "arn:aws:codebuild:your-region:your-account-id:token/your-server-type" }`For more information, see [Connect Source Providers with Access Tokens (CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-access-tokens.html#sample-access-tokens-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DeleteSourceCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-source-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-webhook`.

- **AWS CLI**
- 
            
                    **To delete a webhook filter from an AWS CodeBuild project**The following `delete-webhook`example deletes a webhook from the specified CodeBuild project.`aws codebuild delete-webhook --project-name``my-project`This command produces no output. For more information, see [Stop Running Builds Automatically (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build.html#run-build-cli-auto-stop)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DeleteWebhook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/delete-webhook.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-code-coverages`.

- **AWS CLI**
- 
            
                    **To get detailed information about code coverage test results in AWS CodeBuild.**The following `describe-code-coverages`example gets information about the code coverage test results in the specified report.`aws codebuild describe-code-coverages \ --report-arn``arn:aws:codebuild:<region-ID>:<account-ID>:report/<report-group-name>:<report-ID>`Output: `{ "codeCoverages": [ { "id": "20a0adcc-db13-4b66-804b-ecaf9f852855", "reportARN": "arn:aws:codebuild:<region-ID>:972506530580:report/<report-group-name>:<report-ID>", "filePath": "<source-file-1-path>", "lineCoveragePercentage": 83.33, "linesCovered": 5, "linesMissed": 1, "branchCoveragePercentage": 50.0, "branchesCovered": 1, "branchesMissed": 1, "expired": "2020-11-20T21:22:45+00:00" }, { "id": "0887162d-bf57-4cf1-a164-e432373d1a83", "reportARN": "arn:aws:codebuild:<region-ID>:972506530580:report/<report-group-name>:<report-ID>", "filePath": "<source-file-2-path>", "lineCoveragePercentage": 90.9, "linesCovered": 10, "linesMissed": 1, "branchCoveragePercentage": 50.0, "branchesCovered": 1, "branchesMissed": 1, "expired": "2020-11-20T21:22:45+00:00" } ] }`For more information, see [Code coverage reports](https://docs.aws.amazon.com/codebuild/latest/userguide/code-coverage-report.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DescribeCodeCoverages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/describe-code-coverages.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-test-cases`.

- **AWS CLI**
- 
            
                    **To get detailed information about test cases in AWS CodeBuild.**The following `describe-test-cases`example gets information about the test cases in the specified report.`aws codebuild describe-test-cases \ --report-arn``arn:aws:codebuild:<region-ID>:<account-ID>:report/<report-group-name>:<report-ID>`Output: `{ "testCases": [ { "reportArn": "arn:aws:codebuild:<region-ID>:<account-ID>:report/<report-group-name>:<report-ID>", "testRawDataPath": "<test-report-path>", "prefix": "NUnit.Tests.Assemblies.MockTestFixture", "name": "NUnit.Tests.Assemblies.MockTestFixture.NotRunnableTest", "status": "ERROR", "durationInNanoSeconds": 0, "message": "No arguments were provided\n", "expired": "2020-11-20T17:52:10+00:00" }, { "reportArn": "arn:aws:codebuild:<region-ID>:<account-ID>:report/<report-group-name>:<report-ID>", "testRawDataPath": "<test-report-path>", "prefix": "NUnit.Tests.Assemblies.MockTestFixture", "name": "NUnit.Tests.Assemblies.MockTestFixture.TestWithException", "status": "ERROR", "durationInNanoSeconds": 0, "message": "System.ApplicationException : Intentional Exception\nat NUnit.Tests.Assemblies.MockTestFixture.MethodThrowsException()\nat NUnit.Tests.Assemblies.MockTestFixture.TestWithException()\n\n", "expired": "2020-11-20T17:52:10+00:00" } ] }`For more information, see [Working with test reporting in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/test-reporting.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [DescribeTestCases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/describe-test-cases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-source-credentials`.

- **AWS CLI**
- 
            
                    **Connect an AWS CodeBuild user to a source provider by importing credentials for the source provider.**The following `import-source-credentials`example imports a token for a Bitbucket repository that uses BASIC_AUTH for its authentication type.`aws codebuild import-source-credentials --server-type``BITBUCKET`--auth-type`BASIC_AUTH`--token`my-Bitbucket-password`--username`my-Bitbucket-username`Output: `{ "arn": "arn:aws:codebuild:us-west-2:123456789012:token/bitbucket" }`For more information, see [Connect Source Providers with Access Tokens (CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-access-tokens.html#sample-access-tokens-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ImportSourceCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/import-source-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `invalidate-project-cache`.

- **AWS CLI**
- 
            
                    **To reset the cache for an AWS CodeBuild build project.**The following `invalidate-project-cache`example resets the cache for the specified CodeBuild project.`aws codebuild invalidate-project-cache --project-name``my-project`This command produces no output. For more information, see [Build Caching in CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-caching.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [InvalidateProjectCache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/invalidate-project-cache.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-build-batches-for-project`.

- **AWS CLI**
- 
            
                    **To list batch builds for a specific build project in AWS CodeBuild.**The following `list-build-batches-for-project`example lists the CodeBuild batch builds for the specified project.`aws codebuild list-build-batches-for-project \ --project-name``"<project-name>"`Output: `{ "ids": [ "<project-name>:<batch-ID>", "<project-name>:<batch-ID>" ] }`For more information, see [Batch builds in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListBuildBatchesForProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-build-batches-for-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-build-batches`.

- **AWS CLI**
- 
            
                    **To list batch builds in AWS CodeBuild.**The following `list-build-batches`example lists the CodeBuild batch builds for the current account.`aws codebuild list-build-batches`Output: `{ "ids": [ "<project-name>:<batch-ID>", "<project-name>:<batch-ID>" ] }`For more information, see Batch builds in AWS CodeBuild <https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html>)__ in the *AWS CodeBuild User Guide*.- 
                    For API details, see [ListBuildBatches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-build-batches.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-builds-for-project`.

- **AWS CLI**
- 
            
                    **To view a list of builds for an AWS CodeBuild build project.**The following `list-builds-for-project`example lists the build IDs in descending order for the specified CodeBuild build project.`aws codebuild list-builds-for-project --project-name``codebuild-demo-project`--sort-order`DESCENDING`Output: `{ "ids": [ "codebuild-demo-project:1a2b3c4d-5678-90ab-cdef-11111example", "codebuild-demo-project:1a2b3c4d-5678-90ab-cdef-22222example", "codebuild-demo-project:1a2b3c4d-5678-90ab-cdef-33333example", "codebuild-demo-project:1a2b3c4d-5678-90ab-cdef-44444example", "codebuild-demo-project:1a2b3c4d-5678-90ab-cdef-55555example" ] }`For more information, see [View a List of Build IDs for a Build Project (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/view-builds-for-project.html#view-builds-for-project-cli)in the*AWS CodeBuild User Guide*- 
                    For API details, see [ListBuildsForProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-builds-for-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-builds`.

- **AWS CLI**
- 
            
                    **To get a list of AWS CodeBuild builds IDs.**The following `list-builds`example gets a list of CodeBuild IDs sorted in ascending order.`aws codebuild list-builds --sort-order``ASCENDING`The output includes a `nextToken`value which indicates that there is more output available.`{ "nextToken": "4AEA6u7J...The full token has been omitted for brevity...MzY2OA==", "ids": [ "codebuild-demo-project:815e755f-bade-4a7e-80f0-efe51EXAMPLE" "codebuild-demo-project:84a7f3d1-d40e-4956-b4cf-7a9d4EXAMPLE" ... The full list of build IDs has been omitted for brevity ... "codebuild-demo-project:931d0b72-bf6f-4040-a472-5c707EXAMPLE" ] }`Run this command again and provide the `nextToken`value in the previous response as a parameter to get the next part of the output. Repeat until you don't receive a`nextToken`value in the response.`aws codebuild list-builds --sort-order``ASCENDING`--next-token`4AEA6u7J...The``full``token``has``been``omitted``for``brevity...MzY2OA==`Next part of the output: `{ "ids": [ "codebuild-demo-project:49015049-21cf-4b50-9708-df115EXAMPLE", "codebuild-demo-project:543e7206-68a3-46d6-a4da-759abEXAMPLE", ... The full list of build IDs has been omitted for brevity ... "codebuild-demo-project:c282f198-4582-4b38-bdc0-26f96EXAMPLE" ] }`For more information, see [View a List of Build IDs (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/view-build-list.html)in the*AWS CodeBuild User Guide*- 
                    For API details, see [ListBuilds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-builds.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-curated-environment-images`.

- **AWS CLI**
- 
            
                    **To get a list of Docker images managed by AWS CodeBuild that you can use for your builds.**The following `list-curated-environment-images`example lists the Docker images managed by CodeBuild that can be used for builds.:`aws codebuild list-curated-environment-images`Output: `{ "platforms": [ { "platform": "AMAZON_LINUX", "languages": [ { "language": "JAVA", "images": [ { "description": "AWS ElasticBeanstalk - Java 7 Running on Amazon Linux 64bit v2.1.3", "name": "aws/codebuild/eb-java-7-amazonlinux-64:2.1.3", "versions": [ "aws/codebuild/eb-java-7-amazonlinux-64:2.1.3-1.0.0" ] }, { "description": "AWS ElasticBeanstalk - Java 8 Running on Amazon Linux 64bit v2.1.3", "name": "aws/codebuild/eb-java-8-amazonlinux-64:2.1.3", "versions": [ "aws/codebuild/eb-java-8-amazonlinux-64:2.1.3-1.0.0" ] }, ... LIST TRUNCATED FOR BREVITY ... ] } ] } ] }`For more information, see [Docker Images Provided by CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-available.html)in the*AWS CodeBuild User Guide*- 
                    For API details, see [ListCuratedEnvironmentImages](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-curated-environment-images.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-projects`.

- **AWS CLI**
- 
            
                    **To get a list of AWS CodeBuild build project names.**The following `list-projects`example gets a list of CodeBuild build projects sorted by name in ascending order.`aws codebuild list-projects --sort-by``NAME`--sort-order`ASCENDING`The output includes a `nextToken`value which indicates that there is more output available.`{ "nextToken": "Ci33ACF6...The full token has been omitted for brevity...U+AkMx8=", "projects": [ "codebuild-demo-project", "codebuild-demo-project2", ... The full list of build project names has been omitted for brevity ... "codebuild-demo-project99" ] }`Run this command again and provide the `nextToken`value from the previous response as a parameter to get the next part of the output. Repeat until you don't receive a`nextToken`value in the response.`aws codebuild list-projects --sort-by``NAME`--sort-order`ASCENDING`--next-token`Ci33ACF6...The``full``token``has``been``omitted``for``brevity...U+AkMx8=``{`"projects":`[`"codebuild-demo-project100", "codebuild-demo-project101",`...``The``full``list``of``build``project``names``has``been``omitted``for``brevity``...``"codebuild-demo-project122"``]``}`For more information, see [View a List of Build Project Names (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/view-project-list.html#view-project-list-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListProjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-projects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-report-groups`.

- **AWS CLI**
- 
            
                    **To get a list of the report group ARNs in AWS CodeBuild.**The following `list-report-groups`example retrieves the report group ARNs for the account in the region.`aws codebuild list-report-groups`Output: `{ "reportGroups": [ "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/report-group-1", "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/report-group-2", "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/report-group-3" ] }`For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListReportGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-report-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-reports-for-report-group`.

- **AWS CLI**
- 
            
                    **To get a list of the reports in a report group in AWS CodeBuild.**The following `list-report-for-report-groups`example retrieves the reports in the specified report group for the account in the region.`aws codebuild list-reports-for-report-group \ --report-group-arn``arn:aws:codebuild:<region-ID>:<user-ID>:report-group/<report-group-name>`Output: `{ "reports": [ "arn:aws:codebuild:<region-ID>:<user-ID>:report/report-1", "arn:aws:codebuild:<region-ID>:<user-ID>:report/report-2", "arn:aws:codebuild:<region-ID>:<user-ID>:report/report-3" ] }`For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListReportsForReportGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-reports-for-report-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-reports`.

- **AWS CLI**
- 
            
                    **To get a list of the reports for the current account in AWS CodeBuild.**The following `list-reports`example retrieves the ARNs of the reports for the current account.`aws codebuild list-reports`Output: `{ "reports": [ "arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report ID>", "arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report ID>", "arn:aws:codebuild:<region-ID>:<user-ID>:report/<report-group-name>:<report ID>" ] }`For more information, see [Working with reports](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListReports](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-reports.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-shared-projects`.

- **AWS CLI**
- 
            
                    **To list the shared project in AWS CodeBuild.**The following `list-shared-projects`example lists the CodeBuild shared projects that are available to the current account.`aws codebuild list-shared-projects`Output: `{ "projects": [ "arn:aws:codebuild:<region-ID>:<account-ID>:project/<shared-project-name-1>", "arn:aws:codebuild:<region-ID>:<account-ID>:project/<shared-project-name-2>" ] }`For more information, see [Working with shared projects](https://docs.aws.amazon.com/codebuild/latest/userguide/project-sharing.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListSharedProjects](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-shared-projects.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-shared-report-groups`.

- **AWS CLI**
- 
            
                    **To get a list of the shared report group ARNs in AWS CodeBuild.**The following `list-shared-report-groups`example retrieves the report group ARNs for the account in the region.`aws codebuild list-shared-report-groups`Output: `{ "reportGroups": [ "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/report-group-1", "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/report-group-2", "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/report-group-3" ] }`For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListSharedReportGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-shared-report-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-source-credentials`.

- **AWS CLI**
- 
            
                    **To view a list of sourceCredentialsObjects**The following `list-source-credentials`example lists tokens for an AWS account connected to one Bitbucket account and one GitHub account. Each`sourceCredentialsInfos`object in the response contains connected source credentials information.`aws codebuild list-source-credentials`Output: `{ "sourceCredentialsInfos": [ { "serverType": "BITBUCKET", "arn": "arn:aws:codebuild:us-west-2:123456789012:token/bitbucket", "authType": "BASIC_AUTH" }, { "serverType": "GITHUB", "arn": "arn:aws:codebuild:us-west-2:123456789012:token/github", "authType": "OAUTH" } ] }`For more information, see [Connect Source Providers with Access Tokens (CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-access-tokens.html#sample-access-tokens-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [ListSourceCredentials](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-source-credentials.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `retry-build-batch`.

- **AWS CLI**
- 
            
                    **To retry a failed batch build in AWS CodeBuild.**The following `retry-build-batch`example restarts the specified batch build.`aws codebuild retry-build-batch \ --id``<project-name>:<batch-ID>`Output: `{ "buildBatch": { "id": "<project-name>:<batch-ID>", "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build-batch/<project-name>:<batch-ID>", "startTime": "2020-10-21T17:26:23.099000+00:00", "currentPhase": "SUBMITTED", "buildBatchStatus": "IN_PROGRESS", "resolvedSourceVersion": "3a9e11cb419e8fff14b03883dc4e64f6155aaa7e", "projectName": "<project-name>", "phases": [ { "phaseType": "SUBMITTED", "phaseStatus": "SUCCEEDED", "startTime": "2020-10-21T17:26:23.099000+00:00", "endTime": "2020-10-21T17:26:23.457000+00:00", "durationInSeconds": 0 }, { "phaseType": "DOWNLOAD_BATCHSPEC", "phaseStatus": "SUCCEEDED", "startTime": "2020-10-21T17:26:23.457000+00:00", "endTime": "2020-10-21T17:26:54.902000+00:00", "durationInSeconds": 31 }, { "phaseType": "IN_PROGRESS", "phaseStatus": "CLIENT_ERROR", "startTime": "2020-10-21T17:26:54.902000+00:00", "endTime": "2020-10-21T17:28:16.060000+00:00", "durationInSeconds": 81 }, { "phaseType": "FAILED", "phaseStatus": "RETRY", "startTime": "2020-10-21T17:28:16.060000+00:00", "endTime": "2020-10-21T17:29:39.709000+00:00", "durationInSeconds": 83 }, { "phaseType": "SUBMITTED", "startTime": "2020-10-21T17:29:39.709000+00:00" } ], "source": { "type": "GITHUB", "location": "https://github.com/strohm-a/<project-name>-graph.git", "gitCloneDepth": 1, "gitSubmodulesConfig": { "fetchSubmodules": false }, "reportBuildStatus": false, "insecureSsl": false }, "secondarySources": [], "secondarySourceVersions": [], "artifacts": { "location": "" }, "secondaryArtifacts": [], "cache": { "type": "NO_CACHE" }, "environment": { "type": "LINUX_CONTAINER", "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0", "computeType": "BUILD_GENERAL1_SMALL", "environmentVariables": [], "privilegedMode": false, "imagePullCredentialsType": "CODEBUILD" }, "logConfig": { "cloudWatchLogs": { "status": "ENABLED" }, "s3Logs": { "status": "DISABLED", "encryptionDisabled": false } }, "buildTimeoutInMinutes": 60, "queuedTimeoutInMinutes": 480, "complete": false, "initiator": "<username>", "encryptionKey": "arn:aws:kms:<region-ID>:<account-ID>:alias/aws/s3", "buildBatchNumber": 4, "buildBatchConfig": { "serviceRole": "arn:aws:iam::<account-ID>:role/service-role/<project-name>", "restrictions": { "maximumBuildsAllowed": 100 }, "timeoutInMins": 480 }, "buildGroups": [ { "identifier": "DOWNLOAD_SOURCE", "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T17:26:23.889000+00:00", "buildStatus": "SUCCEEDED", "primaryArtifact": { "type": "no_artifacts", "identifier": "DOWNLOAD_SOURCE" }, "secondaryArtifacts": [] } }, { "identifier": "linux_small", "dependsOn": [], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T17:26:55.115000+00:00", "buildStatus": "FAILED", "primaryArtifact": { "type": "no_artifacts", "identifier": "linux_small" }, "secondaryArtifacts": [] } }, { "identifier": "linux_medium", "dependsOn": [ "linux_small" ], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T17:26:54.594000+00:00", "buildStatus": "STOPPED" } }, { "identifier": "linux_large", "dependsOn": [ "linux_medium" ], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T17:26:54.701000+00:00", "buildStatus": "STOPPED" } } ] } }`For more information, see [Batch builds in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [RetryBuildBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/retry-build-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `retry-build`.

- **AWS CLI**
- 
            
                    **To retry a failed build in AWS CodeBuild.**The following `retry-build`example restarts the specified build.`aws codebuild retry-build \ --id``<project-name>:<build-ID>`Output: `{ "build": { "id": "<project-name>:<build-ID>", "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "buildNumber": 9, "startTime": "2020-10-21T17:51:38.161000+00:00", "currentPhase": "QUEUED", "buildStatus": "IN_PROGRESS", "projectName": "<project-name>", "phases": [ { "phaseType": "SUBMITTED", "phaseStatus": "SUCCEEDED", "startTime": "2020-10-21T17:51:38.161000+00:00", "endTime": "2020-10-21T17:51:38.210000+00:00", "durationInSeconds": 0 }, { "phaseType": "QUEUED", "startTime": "2020-10-21T17:51:38.210000+00:00" } ], "source": { "type": "GITHUB", "location": "<GitHub-repo-URL>", "gitCloneDepth": 1, "gitSubmodulesConfig": { "fetchSubmodules": false }, "reportBuildStatus": false, "insecureSsl": false }, "secondarySources": [], "secondarySourceVersions": [], "artifacts": { "location": "" }, "secondaryArtifacts": [], "cache": { "type": "NO_CACHE" }, "environment": { "type": "LINUX_CONTAINER", "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0", "computeType": "BUILD_GENERAL1_SMALL", "environmentVariables": [], "privilegedMode": false, "imagePullCredentialsType": "CODEBUILD" }, "serviceRole": "arn:aws:iam::<account-ID>:role/service-role/<service-role-name>", "logs": { "deepLink": "https://console.aws.amazon.com/cloudwatch/home?region=<region-ID>#logEvent:group=null;stream=null", "cloudWatchLogsArn": "arn:aws:logs:<region-ID>:<account-ID>:log-group:null:log-stream:null", "cloudWatchLogs": { "status": "ENABLED" }, "s3Logs": { "status": "DISABLED", "encryptionDisabled": false } }, "timeoutInMinutes": 60, "queuedTimeoutInMinutes": 480, "buildComplete": false, "initiator": "<username>", "encryptionKey": "arn:aws:kms:<region-ID>:<account-ID>:alias/aws/s3" } }`For more information, see [Batch builds in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [RetryBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/retry-build.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-build-batch`.

- **AWS CLI**
- 
            
                    **To start a batch build in AWS CodeBuild.**The following `start-build-batch`example starts a batch build of the specified project.`aws codebuild start-build-batch \ --project-name``<project-name>`Output: `{ "buildBatch": { "id": "<project-name>:<batch-ID>", "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build-batch/<project-name>:<batch-ID>", "startTime": "2020-10-21T16:54:24.740000+00:00", "currentPhase": "SUBMITTED", "buildBatchStatus": "IN_PROGRESS", "projectName": "<project-name>", "source": { "type": "GITHUB", "location": "<GitHub-repo-URL>", "gitCloneDepth": 1, "gitSubmodulesConfig": { "fetchSubmodules": false }, "reportBuildStatus": false, "insecureSsl": false }, "secondarySources": [], "secondarySourceVersions": [], "artifacts": { "location": "" }, "secondaryArtifacts": [], "cache": { "type": "NO_CACHE" }, "environment": { "type": "LINUX_CONTAINER", "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0", "computeType": "BUILD_GENERAL1_SMALL", "environmentVariables": [], "privilegedMode": false, "imagePullCredentialsType": "CODEBUILD" }, "logConfig": { "cloudWatchLogs": { "status": "ENABLED" }, "s3Logs": { "status": "DISABLED", "encryptionDisabled": false } }, "buildTimeoutInMinutes": 60, "queuedTimeoutInMinutes": 480, "complete": false, "initiator": "<username>", "encryptionKey": "arn:aws:kms:<region-ID>:<account-ID>:alias/aws/s3", "buildBatchNumber": 3, "buildBatchConfig": { "serviceRole": "arn:aws:iam::<account-ID>:role/service-role/<service-role-name>", "restrictions": { "maximumBuildsAllowed": 100 }, "timeoutInMins": 480 } } }`For more information, see [Batch builds in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [StartBuildBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-build-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-build`.

- **AWS CLI**
- 
            
                    **To start running a build of an AWS CodeBuild build project.**The following `start-build`example starts a build for the specified CodeBuild project. The build overrides both the project's setting for the number of minutes the build is allowed to be queued before it times out and the project's artifact settings.`aws codebuild start-build \ --project-name``"my-demo-project"`\ --queued-timeout-in-minutes-override`5`\ --artifacts-override {"\"type\": \"S3\",\"location\": \"arn:aws:s3:::artifacts-override\",\"overrideArtifactName\":true"}Output: `{ "build": { "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role", "buildStatus": "IN_PROGRESS", "buildComplete": false, "projectName": "my-demo-project", "timeoutInMinutes": 60, "source": { "insecureSsl": false, "type": "S3", "location": "codebuild-us-west-2-123456789012-input-bucket/my-source.zip" }, "queuedTimeoutInMinutes": 5, "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "currentPhase": "QUEUED", "startTime": 1556905683.568, "environment": { "computeType": "BUILD_GENERAL1_MEDIUM", "environmentVariables": [], "type": "LINUX_CONTAINER", "privilegedMode": false, "image": "aws/codebuild/standard:1.0", "imagePullCredentialsType": "CODEBUILD" }, "phases": [ { "phaseStatus": "SUCCEEDED", "startTime": 1556905683.568, "phaseType": "SUBMITTED", "durationInSeconds": 0, "endTime": 1556905684.524 }, { "startTime": 1556905684.524, "phaseType": "QUEUED" } ], "logs": { "deepLink": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=null;stream=null" }, "artifacts": { "encryptionDisabled": false, "location": "arn:aws:s3:::artifacts-override/my-demo-project", "overrideArtifactName": true }, "cache": { "type": "NO_CACHE" }, "id": "my-demo-project::12345678-a1b2-c3d4-e5f6-11111EXAMPLE", "initiator": "my-aws-account-name", "arn": "arn:aws:codebuild:us-west-2:123456789012:build/my-demo-project::12345678-a1b2-c3d4-e5f6-11111EXAMPLE" } }`For more information, see [Run a Build (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/run-build.html#run-build-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [StartBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/start-build.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-build-batch`.

- **AWS CLI**
- 
            
                    **To stop an in-progress batch build in AWS CodeBuild.**The following `stop-build-batch`example stops the specified batch build.`aws codebuild stop-build-batch \ --id``<project-name>:<batch-ID>`Output: `{ "buildBatch": { "id": "<project-name>:<batch-ID>", "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build-batch/<project-name>:<batch-ID>", "startTime": "2020-10-21T16:54:24.740000+00:00", "endTime": "2020-10-21T16:56:05.152000+00:00", "currentPhase": "STOPPED", "buildBatchStatus": "STOPPED", "resolvedSourceVersion": "aef7744ed069c51098e15c360f4102cd2cd1ad64", "projectName": "<project-name>", "phases": [ { "phaseType": "SUBMITTED", "phaseStatus": "SUCCEEDED", "startTime": "2020-10-21T16:54:24.740000+00:00", "endTime": "2020-10-21T16:54:25.039000+00:00", "durationInSeconds": 0 }, { "phaseType": "DOWNLOAD_BATCHSPEC", "phaseStatus": "SUCCEEDED", "startTime": "2020-10-21T16:54:25.039000+00:00", "endTime": "2020-10-21T16:54:56.583000+00:00", "durationInSeconds": 31 }, { "phaseType": "IN_PROGRESS", "phaseStatus": "STOPPED", "startTime": "2020-10-21T16:54:56.583000+00:00", "endTime": "2020-10-21T16:56:05.152000+00:00", "durationInSeconds": 68 }, { "phaseType": "STOPPED", "startTime": "2020-10-21T16:56:05.152000+00:00" } ], "source": { "type": "GITHUB", "location": "<GitHub-repo-URL>", "gitCloneDepth": 1, "gitSubmodulesConfig": { "fetchSubmodules": false }, "reportBuildStatus": false, "insecureSsl": false }, "secondarySources": [], "secondarySourceVersions": [], "artifacts": { "location": "" }, "secondaryArtifacts": [], "cache": { "type": "NO_CACHE" }, "environment": { "type": "LINUX_CONTAINER", "image": "aws/codebuild/amazonlinux2-x86_64-standard:3.0", "computeType": "BUILD_GENERAL1_SMALL", "environmentVariables": [], "privilegedMode": false, "imagePullCredentialsType": "CODEBUILD" }, "logConfig": { "cloudWatchLogs": { "status": "ENABLED" }, "s3Logs": { "status": "DISABLED", "encryptionDisabled": false } }, "buildTimeoutInMinutes": 60, "queuedTimeoutInMinutes": 480, "complete": true, "initiator": "Strohm", "encryptionKey": "arn:aws:kms:<region-ID>:<account-ID>:alias/aws/s3", "buildBatchNumber": 3, "buildBatchConfig": { "serviceRole": "arn:aws:iam::<account-ID>:role/service-role/<project-name>", "restrictions": { "maximumBuildsAllowed": 100 }, "timeoutInMins": 480 }, "buildGroups": [ { "identifier": "DOWNLOAD_SOURCE", "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T16:54:25.468000+00:00", "buildStatus": "SUCCEEDED", "primaryArtifact": { "type": "no_artifacts", "identifier": "DOWNLOAD_SOURCE" }, "secondaryArtifacts": [] } }, { "identifier": "linux_small", "dependsOn": [], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T16:54:56.833000+00:00", "buildStatus": "IN_PROGRESS" } }, { "identifier": "linux_medium", "dependsOn": [ "linux_small" ], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T16:54:56.211000+00:00", "buildStatus": "PENDING" } }, { "identifier": "linux_large", "dependsOn": [ "linux_medium" ], "ignoreFailure": false, "currentBuildSummary": { "arn": "arn:aws:codebuild:<region-ID>:<account-ID>:build/<project-name>:<build-ID>", "requestedOn": "2020-10-21T16:54:56.330000+00:00", "buildStatus": "PENDING" } } ] } }`For more information, see [Batch builds in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/batch-build.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [StopBuildBatch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/stop-build-batch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-build`.

- **AWS CLI**
- 
            
                    **To stop a build of an AWS CodeBuild build project.**The following `stop-build`example stops the specified CodeBuild build.`aws codebuild stop-build --id``my-demo-project:12345678-a1b2-c3d4-e5f6-11111EXAMPLE`Output: `{ "build": { "startTime": 1556906956.318, "initiator": "my-aws-account-name", "projectName": "my-demo-project", "currentPhase": "COMPLETED", "cache": { "type": "NO_CACHE" }, "source": { "insecureSsl": false, "location": "codebuild-us-west-2-123456789012-input-bucket/my-source.zip", "type": "S3" }, "id": "my-demo-project:1a2b3c4d-5678-90ab-cdef-11111EXAMPLE", "endTime": 1556906974.781, "phases": [ { "durationInSeconds": 0, "phaseType": "SUBMITTED", "endTime": 1556906956.935, "phaseStatus": "SUCCEEDED", "startTime": 1556906956.318 }, { "durationInSeconds": 1, "phaseType": "QUEUED", "endTime": 1556906958.272, "phaseStatus": "SUCCEEDED", "startTime": 1556906956.935 }, { "phaseType": "PROVISIONING", "phaseStatus": "SUCCEEDED", "durationInSeconds": 14, "contexts": [ { "message": "", "statusCode": "" } ], "endTime": 1556906972.847, "startTime": 1556906958.272 }, { "phaseType": "DOWNLOAD_SOURCE", "phaseStatus": "SUCCEEDED", "durationInSeconds": 0, "contexts": [ { "message": "", "statusCode": "" } ], "endTime": 1556906973.552, "startTime": 1556906972.847 }, { "phaseType": "INSTALL", "phaseStatus": "SUCCEEDED", "durationInSeconds": 0, "contexts": [ { "message": "", "statusCode": "" } ], "endTime": 1556906973.75, "startTime": 1556906973.552 }, { "phaseType": "PRE_BUILD", "phaseStatus": "SUCCEEDED", "durationInSeconds": 0, "contexts": [ { "message": "", "statusCode": "" } ], "endTime": 1556906973.937, "startTime": 1556906973.75 }, { "durationInSeconds": 0, "phaseType": "BUILD", "endTime": 1556906974.781, "phaseStatus": "STOPPED", "startTime": 1556906973.937 }, { "phaseType": "COMPLETED", "startTime": 1556906974.781 } ], "artifacts": { "location": "arn:aws:s3:::artifacts-override/my-demo-project", "encryptionDisabled": false, "overrideArtifactName": true }, "buildComplete": true, "buildStatus": "STOPPED", "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role", "queuedTimeoutInMinutes": 5, "timeoutInMinutes": 60, "environment": { "type": "LINUX_CONTAINER", "environmentVariables": [], "computeType": "BUILD_GENERAL1_MEDIUM", "privilegedMode": false, "image": "aws/codebuild/standard:1.0", "imagePullCredentialsType": "CODEBUILD" }, "logs": { "streamName": "1a2b3c4d-5678-90ab-cdef-11111EXAMPLE", "deepLink": "https://console.aws.amazon.com/cloudwatch/home?region=us-west-2#logEvent:group=/aws/codebuild/my-demo-project;stream=1a2b3c4d-5678-90ab-cdef-11111EXAMPLE", "groupName": "/aws/codebuild/my-demo-project" }, "arn": "arn:aws:codebuild:us-west-2:123456789012:build/my-demo-project:1a2b3c4d-5678-90ab-cdef-11111EXAMPLE" } }`For more information, see [Stop a Build (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/stop-build.html#stop-build-cli)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [StopBuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/stop-build.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-project`.

- **AWS CLI**
- 
            
                    **To change an AWS CodeBuild build project's settings.**The following `update-project`example changes the settings of the specified CodeBuild build project named my-demo-project.`aws codebuild update-project --name``"my-demo-project"`\ --description`"This project is updated"`\ --source "{\"type\": \"S3\",\"location\": \"codebuild-us-west-2-123456789012-input-bucket/my-source-2.zip\"}" \ --artifacts {"\"type\": \"S3\",\"location\": \"codebuild-us-west-2-123456789012-output-bucket-2\""} \ --environment "{\"type\": \"LINUX_CONTAINER\",\"image\": \"aws/codebuild/standard:1.0\",\"computeType\": \"BUILD_GENERAL1_MEDIUM\"}" \ --service-role`"arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role"`The output displays the updated settings. `{ "project": { "arn": "arn:aws:codebuild:us-west-2:123456789012:project/my-demo-project", "environment": { "privilegedMode": false, "environmentVariables": [], "type": "LINUX_CONTAINER", "image": "aws/codebuild/standard:1.0", "computeType": "BUILD_GENERAL1_MEDIUM", "imagePullCredentialsType": "CODEBUILD" }, "queuedTimeoutInMinutes": 480, "description": "This project is updated", "artifacts": { "packaging": "NONE", "name": "my-demo-project", "type": "S3", "namespaceType": "NONE", "encryptionDisabled": false, "location": "codebuild-us-west-2-123456789012-output-bucket-2" }, "encryptionKey": "arn:aws:kms:us-west-2:123456789012:alias/aws/s3", "badge": { "badgeEnabled": false }, "serviceRole": "arn:aws:iam::123456789012:role/service-role/my-codebuild-service-role", "lastModified": 1556840545.967, "tags": [], "timeoutInMinutes": 60, "created": 1556839783.274, "name": "my-demo-project", "cache": { "type": "NO_CACHE" }, "source": { "type": "S3", "insecureSsl": false, "location": "codebuild-us-west-2-123456789012-input-bucket/my-source-2.zip" } } }`For more information, see [Change a Build Project's Settings (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-cli)in the*AWS CodeBuild User Guide*- 
                    For API details, see [UpdateProject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-project.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-report-group`.

- **AWS CLI**
- 
            
                    **To update a report group in AWS CodeBuild.**The following `update-report-group`example changes the export type of the report group to "NO_EXPORT".`aws codebuild update-report-group \ --arn``arn:aws:codebuild:<region-ID>:<user-ID>:report-group/cli-created-report-group`\ --export-config="exportConfigType=NO_EXPORT"Output: `{ "reportGroup": { "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/cli-created-report-group", "name": "cli-created-report-group", "type": "TEST", "exportConfig": { "exportConfigType": "NO_EXPORT" }, "created": 1602020686.009, "lastModified": 1602021033.454, "tags": [] } }`For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html)in the*AWS CodeBuild User Guide*.- 
                    For API details, see [UpdateReportGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-report-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-webhook`.

- **AWS CLI**
- 
            
                    **To update the webhook for an AWS CodeBuild project**The following `update-webhook`example updates a webhook for the specified CodeBuild project with two filter groups. The`--rotate-secret`parameter specifies that GitHub rotate the project's secret key every time a code change triggers a build. The first filter group specifies pull requests that are created, updated, or reopened on branches with Git reference names that match the regular expression`^refs/heads/master$`and head references that match`^refs/heads/myBranch$`. The second filter group specifies push requests on branches with Git reference names that do not match the regular expression`^refs/heads/myBranch$`.`aws codebuild update-webhook \ --project-name``Project2`\ --rotate-secret \ --filter-groups "[[{\"type\":\"EVENT\",\"pattern\":\"PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_REOPENED\"},{\"type\":\"HEAD_REF\",\"pattern\":\"^refs/heads/myBranch$\",\"excludeMatchedPattern\":true},{\"type\":\"BASE_REF\",\"pattern\":\"^refs/heads/master$\",\"excludeMatchedPattern\":true}],[{\"type\":\"EVENT\",\"pattern\":\"PUSH\"},{\"type\":\"HEAD_REF\",\"pattern\":\"^refs/heads/myBranch$\",\"excludeMatchedPattern\":true}]]"Output: `{ "webhook": { "filterGroups": [ [ { "pattern": "PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED, PULL_REQUEST_REOPENED", "type": "EVENT" }, { "excludeMatchedPattern": true, "pattern": "refs/heads/myBranch$", "type": "HEAD_REF" }, { "excludeMatchedPattern": true, "pattern": "refs/heads/master$", "type": "BASE_REF" } ], [ { "pattern": "PUSH", "type": "EVENT" }, { "excludeMatchedPattern": true, "pattern": "refs/heads/myBranch$", "type": "HEAD_REF" } ] ], "lastModifiedSecret": 1556312220.133 } }`For more information, see [Change a Build Project's Settings (AWS CLI)](https://docs.aws.amazon.com/codebuild/latest/userguide/change-project.html#change-project-cli)in the*AWS CodeBuild User Guide*- 
                    For API details, see [UpdateWebhook](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-webhook.html)in*AWS CLI Command Reference*.
 
-