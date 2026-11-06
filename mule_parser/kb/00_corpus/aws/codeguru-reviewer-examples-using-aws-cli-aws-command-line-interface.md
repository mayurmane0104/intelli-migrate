# CodeGuru Reviewer examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_codeguru-reviewer_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_codeguru-reviewer_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CodeGuru Reviewer.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-repository`.

- **AWS CLI**
- 
            
                    **Example 1: To create a Bitbucket repository association**The following `associate-repository`example creates a repository association using an existing Bitbucket repository.`aws codeguru-reviewer associate-repository \ --repository '``Bitbucket={Owner=sample-owner, Name=mySampleRepo, ConnectionArn=arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 }`'Output: `{ "RepositoryAssociation": { "ProviderType": "Bitbucket", "Name": "mySampleRepo", "LastUpdatedTimeStamp": 1596216896.979, "AssociationId": "association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "CreatedTimeStamp": 1596216896.979, "ConnectionArn": "arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "State": "Associating", "StateReason": "Pending Repository Association", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Owner": "sample-owner" } }`For more information, see [Create a Bitbucket repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-bitbucket-association.html)in the*Amazon CodeGuru Reviewer User Guide*.**Example 2: To create a GitHub Enterprise repository association**The following `associate-repository`example creates a repository association using an existing GitHub Enterprise repository.`aws codeguru-reviewer associate-repository \ --repository '``GitHubEnterpriseServer={Owner=sample-owner, Name=mySampleRepo, ConnectionArn=arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 }`'Output: `{ "RepositoryAssociation": { "ProviderType": "GitHubEnterpriseServer", "Name": "mySampleRepo", "LastUpdatedTimeStamp": 1596216896.979, "AssociationId": "association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "CreatedTimeStamp": 1596216896.979, "ConnectionArn": "arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "State": "Associating", "StateReason": "Pending Repository Association", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Owner": "sample-owner" } }`For more information, see [Create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html)in the*Amazon Codeguru Reviewer User Guide*.**Example 3: To create an AWS CodeCommit repository association**The following `associate-repository`example creates a repository association using an existing AWS CodeCommit repository.`aws codeguru-reviewer associate-repository \ --repository``CodeCommit={Name=mySampleRepo}`Output: `{ "RepositoryAssociation": { "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "My-ecs-beta-repo", "LastUpdatedTimeStamp": 1595634764.029, "ProviderType": "CodeCommit", "CreatedTimeStamp": 1595634764.029, "Owner": "544120495673", "State": "Associating", "StateReason": "Pending Repository Association", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:544120495673:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [Create an AWS CodeCommit repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-codecommit-association.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [AssociateRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/associate-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-code-review`.

- **AWS CLI**
- 
            
                    **To create a code review.**The following `create-code-review`creates a review of code in the`mainline`branch of an AWS CodeCommit repository that is named`my-repository-name`.`aws codeguru-reviewer create-code-review \ --name``my-code-review`\ --repository-association-arn`arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --type '`{"RepositoryAnalysis": {"RepositoryHead": {"BranchName": "mainline"}}}`'Output: `{ "CodeReview": { "Name": "my-code-review", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222:code-review:RepositoryAnalysis-my-code-review", "RepositoryName": "my-repository-name", "Owner": "123456789012", "ProviderType": "CodeCommit", "State": "Pending", "StateReason": "CodeGuru Reviewer has received the request, and a code review is scheduled.", "CreatedTimeStamp": 1618873489.195, "LastUpdatedTimeStamp": 1618873489.195, "Type": "RepositoryAnalysis", "SourceCodeType": { "RepositoryHead": { "BranchName": "mainline" } }, "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [Create code reviews in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-code-reviews.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [CreateCodeReview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/create-code-review.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-code-review`.

- **AWS CLI**
- 
            
                    **List details about a code review.**The following `describe-code-review`lists information about a review of code in the "mainline" branch of an AWS CodeCommit repository that is named "my-repo-name".`aws codeguru-reviewer put-recommendation-feedback \ --code-review-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111:code-review:RepositoryAnalysis-my-repository-name-branch-abcdefgh12345678`\ --recommendation-id`3be1b2e5d7ef6e298a06499379ee290c9c596cf688fdcadb08285ddb0dd390eb`\ --reactions`ThumbsUp`Output `{ "CodeReview": { "Name": "My-ecs-beta-repo-master-xs6di4kfd4j269dz", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222:code-review:RepositoryAnalysis-my-repo-name", "RepositoryName": "My-ecs-beta-repo", "Owner": "123456789012", "ProviderType": "CodeCommit", "State": "Pending", "StateReason": "CodeGuru Reviewer is reviewing the source code.", "CreatedTimeStamp": 1618874226.226, "LastUpdatedTimeStamp": 1618874233.689, "Type": "RepositoryAnalysis", "SourceCodeType": { "RepositoryHead": { "BranchName": "mainline" } }, "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [View code review details](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/view-code-review-details.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [DescribeCodeReview](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-code-review.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-recommendation-feedback`.

- **AWS CLI**
- 
            
                    **To view information about feedback on a recommendation**The following `describe-recommendation-feedback`displays information about feedback on a recommendation. This recommendation has one`ThumbsUp`reaction.`aws codeguru-reviewer describe-recommendation-feedback \ --code-review-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111:code-review:RepositoryAnalysis-my-repository-name-branch-abcdefgh12345678`\ --recommendation-id`3be1b2e5d7ef6e298a06499379ee290c9c596cf688fdcadb08285ddb0dd390eb`Output: `{ "RecommendationFeedback": { "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111:code-review:RepositoryAnalysis-my-repository-name-branch-abcdefgh12345678", "RecommendationId": "3be1b2e5d7ef6e298a06499379ee290c9c596cf688fdcadb08285ddb0dd390eb", "Reactions": [ "ThumbsUp" ], "UserId": "aws-user-id", "CreatedTimeStamp": 1618877070.313, "LastUpdatedTimeStamp": 1618877948.881 } }`For more information, see [View recommendations and provide feedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/give-feedback-from-code-review-details.html)and[Step 4: Provide feedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/provide-feedback.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [DescribeRecommendationFeedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-recommendation-feedback.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-repository-association`.

- **AWS CLI**
- 
            
                    **Example 1: To return information about a GitHub repository association**The following `describe-repository-association`example returns information about a repository association that uses a GitHub Enterprise repository and is in the`Associated`state.`aws codeguru-reviewer describe-repository-association \ --association-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RepositoryAssociation": { "AssociationId": "b822717e-0711-4e8a-bada-0e738289c75e", "Name": "mySampleRepo", "LastUpdatedTimeStamp": 1588102637.649, "ProviderType": "GitHub", "CreatedTimeStamp": 1588102615.636, "Owner": "sample-owner", "State": "Associated", "StateReason": "Pull Request Notification configuration successful", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111" } }`For more information, see [Create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html)in the*Amazon CodeGuru Reviewer User Guide*.**Example 2: To return information about a failed repository association**The following `describe-repository-association`example returns information about a repository association that uses a GitHub Enterprise repository and is in the`Failed`state.`aws codeguru-reviewer describe-repository-association \ --association-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RepositoryAssociation": { "ProviderType": "GitHubEnterpriseServer", "Name": "mySampleRepo", "LastUpdatedTimeStamp": 1596217036.892, "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "CreatedTimeStamp": 1596216896.979, "ConnectionArn": "arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "State": "Failed", "StateReason": "Failed, Please retry.", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "Owner": "sample-owner" } }`For more information, see [Create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html)in the*Amazon CodeGuru Reviewer User Guide*.**Example 3: To return information about a disassociating repository association**The following `describe-repository-association`example returns information about a repository association that uses a GitHub Enterprise repository and is in the`Disassociating`state.`aws codeguru-reviewer describe-repository-association \ --association-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RepositoryAssociation": { "ProviderType": "GitHubEnterpriseServer", "Name": "mySampleRepo", "LastUpdatedTimeStamp": 1596217036.892, "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "CreatedTimeStamp": 1596216896.979, "ConnectionArn": "arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "State": "Disassociating", "StateReason": "Source code access removal in progress", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "Owner": "sample-owner" } }`For more information, see [Create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [DescribeRepositoryAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-repository-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-repository`.

- **AWS CLI**
- 
            
                    **To disassociate a repository association**The following `disassociate-repository`disassociates a repository association that is using an AWS CodeCommit repository.`aws codeguru-reviewer disassociate-repository \ --association-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RepositoryAssociation": { "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Name": "my-repository", "Owner": "123456789012", "ProviderType": "CodeCommit", "State": "Disassociating", "LastUpdatedTimeStamp": 1618939174.759, "CreatedTimeStamp": 1595636947.096 }, "Tags": { "Status": "Secret", "Team": "Saanvi" } }`For more information, see [Disassociate a repository in CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/disassociate-repository-association.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [DisassociateRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/disassociate-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-code-reviews`.

- **AWS CLI**
- 
            
                    **To list code reviews created in your AWS account in the last 90 days.**The following `list-code-reviews`example lists the code reviews created in the last 90 days using pull requests.`aws codeguru-reviewer list-code-reviews \ --type``PullRequest`Output: `{ "CodeReviewSummaries": [ { "LastUpdatedTimeStamp": 1588897288.054, "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProviderType": "GitHub", "PullRequestId": "5", "MetricsSummary": { "MeteredLinesOfCodeCount": 24, "FindingsCount": 1 }, "CreatedTimeStamp": 1588897068.512, "State": "Completed", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Owner": "sample-owner", "RepositoryName": "sample-repository-name", "Type": "PullRequest" }, { "LastUpdatedTimeStamp": 1588869793.263, "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "ProviderType": "GitHub", "PullRequestId": "4", "MetricsSummary": { "MeteredLinesOfCodeCount": 29, "FindingsCount": 0 }, "CreatedTimeStamp": 1588869575.949, "State": "Completed", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Owner": "sample-owner", "RepositoryName": "sample-repository-name", "Type": "PullRequest" }, { "LastUpdatedTimeStamp": 1588870511.211, "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "ProviderType": "GitHub", "PullRequestId": "4", "MetricsSummary": { "MeteredLinesOfCodeCount": 2, "FindingsCount": 0 }, "CreatedTimeStamp": 1588870292.425, "State": "Completed", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "Owner": "sample-owner", "RepositoryName": "sample-repository-name", "Type": "PullRequest" }, { "LastUpdatedTimeStamp": 1588118522.452, "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444", "ProviderType": "GitHub", "PullRequestId": "3", "MetricsSummary": { "MeteredLinesOfCodeCount": 29, "FindingsCount": 0 }, "CreatedTimeStamp": 1588118301.131, "State": "Completed", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE44444", "Owner": "sample-owner", "RepositoryName": "sample-repository-name", "Type": "PullRequest" }, { "LastUpdatedTimeStamp": 1588112205.207, "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555", "ProviderType": "GitHub", "PullRequestId": "2", "MetricsSummary": { "MeteredLinesOfCodeCount": 25, "FindingsCount": 0 }, "CreatedTimeStamp": 1588111987.443, "State": "Completed", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE55555", "Owner": "sample-owner", "RepositoryName": "sample-repository-name", "Type": "PullRequest" }, { "LastUpdatedTimeStamp": 1588104489.981, "Name": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666", "ProviderType": "GitHub", "PullRequestId": "1", "MetricsSummary": { "MeteredLinesOfCodeCount": 25, "FindingsCount": 0 }, "CreatedTimeStamp": 1588104270.223, "State": "Completed", "CodeReviewArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE66666", "Owner": "sample-owner", "RepositoryName": "sample-repository-name", "Type": "PullRequest" } ] }`For more information, see [View all code reviews](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/view-all-code-reviews.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [ListCodeReviews](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-code-reviews.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-recommendation-feedback`.

- **AWS CLI**
- 
            
                    **To list customer recommendation feedback for a recommendation on an associated repository**The following `list-recommendation-feedback`Lists customer feedback on all recommendations on a code review. This code review has one piece of feedback, a "ThumbsUp", from a customer.`aws codeguru-reviewer list-recommendation-feedback \ --code-review-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111:code-review:RepositoryAnalysis-my-repository-name-branch-abcdefgh12345678`Output: `{ "RecommendationFeedbackSummaries": [ { "RecommendationId": "3be1b2e5d7ef6e298a06499379ee290c9c596cf688fdcadb08285ddb0dd390eb", "Reactions": [ "ThumbsUp" ], "UserId": "aws-user-id" } ] }`For more information, see [Step 4: Provide feedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/provide-feedback.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [ListRecommendationFeedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-recommendation-feedback.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-recommendations`.

- **AWS CLI**
- 
            
                    **To list the recommendations for a completed code review**The following `list-recommendations`example lists the recommendations for a completed code review. This code review has one recommendations.`aws codeguru-reviewer list-recommendations \ --code-review-arn``arn:aws:codeguru-reviewer:us-west-2:544120495673:code-review:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "RecommendationSummaries": [ { "Description": "\n\n**Problem** \n You are using a `ConcurrentHashMap`, but your usage of `containsKey()` and `get()` may not be thread-safe at lines: **63 and 64**. In between the check and the `get()` another thread can remove the key and the `get()` will return `null`. The remove that can remove the key is at line: **59**.\n\n**Fix** \n Consider calling `get()`, checking instead of your current check if the returned object is `null`, and then using that object only, without calling `get()` again.\n\n**More info** \n [View an example on GitHub](https://github.com/apache/hadoop/blob/f16cf877e565084c66bc63605659b157c4394dc8/hadoop-tools/hadoop-aws/src/main/java/org/apache/hadoop/fs/s3a/s3guard/S3Guard.java#L302-L304) (external link).", "RecommendationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "StartLine": 63, "EndLine": 64, "FilePath": "src/main/java/com/company/sample/application/CreateOrderThread.java" } ] }`For more information, see [Step 4: Provide feedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/provide-feedback.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [ListRecommendations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-recommendations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-repository-associations`.

- **AWS CLI**
- 
            
                    **To list the repository associations in your AWS account**The following `list-repository-associations`example returns a list of repository association summary objects in your account. You can filter the returned list by`ProviderType`,`Name`,`State`, and`Owner`.`aws codeguru-reviewer list-repository-associations`Output: `{ "RepositoryAssociationSummaries": [ { "LastUpdatedTimeStamp": 1595886609.616, "Name": "test", "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "Owner": "sample-owner", "State": "Associated", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111", "ProviderType": "Bitbucket" }, { "LastUpdatedTimeStamp": 1595636969.035, "Name": "CodeDeploy-CodePipeline-ECS-Tutorial", "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "Owner": "123456789012", "State": "Associated", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222", "ProviderType": "CodeCommit" }, { "LastUpdatedTimeStamp": 1595634785.983, "Name": "My-ecs-beta-repo", "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "Owner": "123456789012", "State": "Associated", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333", "ProviderType": "CodeCommit" }, { "LastUpdatedTimeStamp": 1590712811.77, "Name": "MyTestCodeCommit", "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE44444", "Owner": "123456789012", "State": "Associated", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE44444", "ProviderType": "CodeCommit" }, { "LastUpdatedTimeStamp": 1588102637.649, "Name": "aws-codeguru-profiler-sample-application", "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE55555", "Owner": "sample-owner", "State": "Associated", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE55555", "ProviderType": "GitHub" }, { "LastUpdatedTimeStamp": 1588028233.995, "Name": "codeguru-profiler-demo-app", "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE66666", "Owner": "sample-owner", "State": "Associated", "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE66666", "ProviderType": "GitHub" } ] }`For more information, see [View all repository associations in CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/repository-association-view-all.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [ListRepositoryAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-repository-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list the tags on an associated repository**The following `list-tags-for-resource`lists the tags on an associated repository. This associated repository has two tags.`aws codeguru-reviewer list-tags-for-resource \ --resource-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`Output: `{ "Tags": { "Status": "Secret", "Team": "Saanvi" } }`For more information, see [View tags for a CodeGuru Reviewer associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-view-cli.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-recommendation-feedback`.

- **AWS CLI**
- 
            
                    **To add a recommendation to a code review**The following `put-recommendation-feedback`puts a`ThumbsUp`recommendation on a code review.`aws codeguru-reviewer put-recommendation-feedback \ --code-review-arn \``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111:code-review:RepositoryAnalysis-my-repository-name-branch-abcdefgh12345678`\ --recommendation-id`3be1b2e5d7ef6e298a06499379ee290c9c596cf688fdcadb08285ddb0dd390eb`\ --reactions`ThumbsUp`This command produces no output. For more information, see [Step 4: Provide feedback](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/provide-feedback.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [PutRecommendationFeedback](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/put-recommendation-feedback.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add a tag to an associated repository**The following `tag-resource`adds two tags to an associated repository`aws codeguru-reviewer tag-resource \ --resource-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --tags`Status=Secret,Team=Saanvi`This command produces no output. For more information, see [Add a tag to a CodeGuru Reviewer associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-add-cli.html)and[Add or update tags for a CodeGuru Reviewer associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-update-cli.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To untag an associated repository**The following `untag-resource`removes two tags with keys "Secret" and "Team" from an associated repository.`aws codeguru-reviewer untag-resource \ --resource-arn``arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`\ --tag-keys`Status``Team`This command produces no output. For more information, see [Remove tags from a CodeGuru Reviewer associated repository (AWS CLI)](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-remove-cli.html)in the*Amazon CodeGuru Reviewer User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/untag-resource.html)in*AWS CLI Command Reference*.
 
-