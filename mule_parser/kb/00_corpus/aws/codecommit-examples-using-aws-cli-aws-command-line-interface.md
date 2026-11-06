# CodeCommit examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_codecommit_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_codecommit_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with CodeCommit.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-approval-rule-template-with-repository`.

- **AWS CLI**
- 
            
                    **To associate an approval rule template with a repository**The following `associate-approval-rule-template-with-repository`example associates the specified approval rule template with a repository named`MyDemoRepo`.`aws codecommit associate-approval-rule-template-with-repository \ --repository-name``MyDemoRepo`\ --approval-rule-template-name`2-approver-rule-for-main`This command produces no output. For more information, see [Associate an Approval Rule Template with a Repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-associate-template.html#associate-template-repository)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [AssociateApprovalRuleTemplateWithRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/associate-approval-rule-template-with-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-associate-approval-rule-template-with-repositories`.

- **AWS CLI**
- 
            
                    **To associate an approval rule template with multiple repositories in a single operation**The following `batch-associate-approval-rule-template-with-repositories`example associates the specified approval rule template with repositories named`MyDemoRepo`and`MyOtherDemoRepo`.Note: Approval rule templates are specific to the AWS Region where they are created. They can only be associated with repositories in that AWS Region. `aws codecommit batch-associate-approval-rule-template-with-repositories \ --repository-names``MyDemoRepo,``MyOtherDemoRepo`\ --approval-rule-template-name`2-approver-rule-for-main`Output: `{ "associatedRepositoryNames": [ "MyDemoRepo", "MyOtherDemoRepo" ], "errors": [] }`For more information, see [Associate an Approval Rule Template with a Repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-associate-template.html#batch-associate-template-repositories)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [BatchAssociateApprovalRuleTemplateWithRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-associate-approval-rule-template-with-repositories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-describe-merge-conflicts`.

- **AWS CLI**
- 
            
                    **To get information about merge conflicts in all files or a subset of files in a merge between two commit specifiers**The following `batch-describe-merge-conflicts`example determines the merge conflicts for merging a source branch named`feature-randomizationfeature`with a destination branch named`main`using the`THREE_WAY_MERGE`strategy in a repository named`MyDemoRepo`.`aws codecommit batch-describe-merge-conflicts \ --source-commit-specifier``feature-randomizationfeature`\ --destination-commit-specifier`main`\ --merge-option`THREE_WAY_MERGE`\ --repository-name`MyDemoRepo`Output: `{ "conflicts": [ { "conflictMetadata": { "filePath": "readme.md", "fileSizes": { "source": 139, "destination": 230, "base": 85 }, "fileModes": { "source": "NORMAL", "destination": "NORMAL", "base": "NORMAL" }, "objectTypes": { "source": "FILE", "destination": "FILE", "base": "FILE" }, "numberOfConflicts": 1, "isBinaryFile": { "source": false, "destination": false, "base": false }, "contentConflict": true, "fileModeConflict": false, "objectTypeConflict": false, "mergeOperations": { "source": "M", "destination": "M" } }, "mergeHunks": [ { "isConflict": true, "source": { "startLine": 0, "endLine": 3, "hunkContent": "VGhpcyBpEXAMPLE==" }, "destination": { "startLine": 0, "endLine": 1, "hunkContent": "VXNlIHRoEXAMPLE=" } } ] } ], "errors": [], "destinationCommitId": "86958e0aEXAMPLE", "sourceCommitId": "6ccd57fdEXAMPLE", "baseCommitId": "767b6958EXAMPLE" }`For more information, see [Resolve Conflicts in a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-resolve-conflict-pull-request.html#batch-describe-merge-conflicts)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [BatchDescribeMergeConflicts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-describe-merge-conflicts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-disassociate-approval-rule-template-from-repositories`.

- **AWS CLI**
- 
            
                    **To disassociate an approval rule template from multiple repositories in a single operation**The following `batch-disassociate-approval-rule-template-from-repositories`example disassociates the specified approval rule template from repositories named`MyDemoRepo`and`MyOtherDemoRepo`.`aws codecommit batch-disassociate-approval-rule-template-from-repositories \ --repository-names``MyDemoRepo,``MyOtherDemoRepo`\ --approval-rule-template-name`1-approval-rule-for-all``pull``requests`Output: `{ "disassociatedRepositoryNames": [ "MyDemoRepo", "MyOtherDemoRepo" ], "errors": [] }`For more information, see [Disassociate an Approval Rule Template](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-disassociate-template.html#batch-disassociate-template)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [BatchDisassociateApprovalRuleTemplateFromRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-disassociate-approval-rule-template-from-repositories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-commits`.

- **AWS CLI**
- 
            
                    **To view information about multiple commits**The following `batch-get-commits`example displays details about the specified commits.`aws codecommit batch-get-commits \ --repository-name``MyDemoRepo`\ --commit-ids`317f8570EXAMPLE``4c925148EXAMPLE`Output: `{ "commits": [ { "additionalData": "", "committer": { "date": "1508280564 -0800", "name": "Mary Major", "email": "mary_major@example.com" }, "author": { "date": "1508280564 -0800", "name": "Mary Major", "email": "mary_major@example.com" }, "commitId": "317f8570EXAMPLE", "treeId": "1f330709EXAMPLE", "parents": [ "6e147360EXAMPLE" ], "message": "Change variable name and add new response element" }, { "additionalData": "", "committer": { "date": "1508280542 -0800", "name": "Li Juan", "email": "li_juan@example.com" }, "author": { "date": "1508280542 -0800", "name": "Li Juan", "email": "li_juan@example.com" }, "commitId": "4c925148EXAMPLE", "treeId": "1f330709EXAMPLE", "parents": [ "317f8570EXAMPLE" ], "message": "Added new class" } }`For more information, see [View Commit Details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-commit-details.html#how-to-view-commit-details-cli-batch-get-commits)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [BatchGetCommits](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-get-commits.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-get-repositories`.

- **AWS CLI**
- 
            
                    **To view details about multiple repositories**This example shows details about multiple AWS CodeCommit repositories. `aws codecommit batch-get-repositories \ --repository-names``MyDemoRepo``MyOtherDemoRepo`Output: `{ "repositoriesNotFound": [], "repositories": [ { "creationDate": 1429203623.625, "defaultBranch": "main", "repositoryName": "MyDemoRepo", "cloneUrlSsh": "ssh://git-codecommit.us-east-2.amazonaws.com/v1/repos/MyDemoRepo", "lastModifiedDate": 1430783812.0869999, "repositoryDescription": "My demonstration repository", "cloneUrlHttp": "https://codecommit.us-east-2.amazonaws.com/v1/repos/MyDemoRepo", "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE", "Arn": "arn:aws:codecommit:us-east-2:111111111111:MyDemoRepo" "accountId": "111111111111" }, { "creationDate": 1429203623.627, "defaultBranch": "main", "repositoryName": "MyOtherDemoRepo", "cloneUrlSsh": "ssh://git-codecommit.us-east-2.amazonaws.com/v1/repos/MyOtherDemoRepo", "lastModifiedDate": 1430783812.0889999, "repositoryDescription": "My other demonstration repository", "cloneUrlHttp": "https://codecommit.us-east-2.amazonaws.com/v1/repos/MyOtherDemoRepo", "repositoryId": "cfc29ac4-b0cb-44dc-9990-f6f51EXAMPLE", "Arn": "arn:aws:codecommit:us-east-2:111111111111:MyOtherDemoRepo" "accountId": "111111111111" } ], "repositoriesNotFound": [] }`- 
                    For API details, see [BatchGetRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-get-repositories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-approval-rule-template`.

- **AWS CLI**
- 
            
                    **To create an approval rule template**The following `create-approval-rule-template`example creates an approval rule template named`2-approver-rule-for-main ``. The template requires two users who assume the role of ``CodeCommitReview`to approve any pull request before it can be merged to the`main`branch.`aws codecommit create-approval-rule-template \ --approval-rule-template-name``2-approver-rule-for-main`\ --approval-rule-template-description`"Requires two developers from the team to approve the pull request if the destination branch is main"`\ --approval-rule-template-content "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}"Output: `{ "approvalRuleTemplate": { "approvalRuleTemplateName": "2-approver-rule-for-main", "creationDate": 1571356106.936, "approvalRuleTemplateId": "dd8b17fe-EXAMPLE", "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "approvalRuleTemplateDescription": "Requires two developers from the team to approve the pull request if the destination branch is main", "lastModifiedDate": 1571356106.936, "ruleContentSha256": "4711b576EXAMPLE" } }`For more information, see [Create an Approval Rule Template](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-template.html#create-template-cli)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [CreateApprovalRuleTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-approval-rule-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-branch`.

- **AWS CLI**
- 
            
                    **To create a branch**This example creates a branch in an AWS CodeCommit repository. This command produces output only if there are errors. Command: `aws codecommit create-branch --repository-name``MyDemoRepo`--branch-name`MyNewBranch`--commit-id`317f8570EXAMPLE`Output: `None.`- 
                    For API details, see [CreateBranch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-branch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-commit`.

- **AWS CLI**
- 
            
                    **To create a commit**The following `create-commit`example demonstrates how to create an initial commit for a repository that adds a`readme.md`file to a repository named`MyDemoRepo`in the`main`branch.`aws codecommit create-commit \ --repository-name``MyDemoRepo`\ --branch-name`main`\ --put-files`"filePath=readme.md,fileContent='Welcome to our team repository.'"`Output: `{ "filesAdded": [ { "blobId": "5e1c309d-EXAMPLE", "absolutePath": "readme.md", "fileMode": "NORMAL" } ], "commitId": "4df8b524-EXAMPLE", "treeId": "55b57003-EXAMPLE", "filesDeleted": [], "filesUpdated": [] }`For more information, see [Create a Commit in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-commit.html#how-to-create-commit-cli)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [CreateCommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-commit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-pull-request-approval-rule`.

- **AWS CLI**
- 
            
                    **To create an approval rule for a pull request**The following `create-pull-request-approval-rule`example creates an approval rule named`Require two approved approvers`for the specified pull request. The rule specifies that two approvals are required from an approval pool. The pool includes all users who access CodeCommit by assuming the role of`CodeCommitReview`in the`123456789012`AWS account. It also includes either an IAM user or federated user named`Nikhil_Jayashankar`from the same AWS account.`aws codecommit create-pull-request-approval-rule \ --pull-request-id``42`--approval-rule-name`"Require two approved approvers"`\ --approval-rule-content "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"CodeCommitApprovers:123456789012:Nikhil_Jayashankar\", \"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}"Output: `{ "approvalRule": { "approvalRuleName": "Require two approved approvers", "lastModifiedDate": 1570752871.932, "ruleContentSha256": "7c44e6ebEXAMPLE", "creationDate": 1570752871.932, "approvalRuleId": "aac33506-EXAMPLE", "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"CodeCommitApprovers:123456789012:Nikhil_Jayashankar\", \"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major" } }`For more information, see [Create an Approval Rule](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-pull-request-approval-rule.html#how-to-create-pull-request-approval-rule-cli)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [CreatePullRequestApprovalRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request-approval-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-pull-request`.

- **AWS CLI**
- 
            
                    **To create a pull request**The following `create-pull-request`example creates a pull request named 'Pronunciation difficulty analyzer' with a description of 'Please review these changes by Tuesday' that targets the 'jane-branch' source branch and is to be merged to the default branch 'main' in an AWS CodeCommit repository named 'MyDemoRepo'.`aws codecommit create-pull-request \ --title``"My Pull Request"`\ --description`"Please review these changes by Tuesday"`\ --client-request-token`123Example`\ --targets`repositoryName=MyDemoRepo,sourceReference=MyNewBranch`Output: `{ "pullRequest": { "approvalRules": [ { "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleId": "dd8b17fe-EXAMPLE", "approvalRuleName": "2-approver-rule-for-main", "creationDate": 1571356106.936, "lastModifiedDate": 571356106.936, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "originApprovalRuleTemplate": { "approvalRuleTemplateId": "dd3d22fe-EXAMPLE", "approvalRuleTemplateName": "2-approver-rule-for-main" }, "ruleContentSha256": "4711b576EXAMPLE" } ], "authorArn": "arn:aws:iam::111111111111:user/Jane_Doe", "description": "Please review these changes by Tuesday", "title": "Pronunciation difficulty analyzer", "pullRequestTargets": [ { "destinationCommit": "5d036259EXAMPLE", "destinationReference": "refs/heads/main", "repositoryName": "MyDemoRepo", "sourceCommit": "317f8570EXAMPLE", "sourceReference": "refs/heads/jane-branch", "mergeMetadata": { "isMerged": false } } ], "lastActivityDate": 1508962823.285, "pullRequestId": "42", "clientRequestToken": "123Example", "pullRequestStatus": "OPEN", "creationDate": 1508962823.285 } }`- 
                    For API details, see [CreatePullRequest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-pull-request.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-repository`.

- **AWS CLI**
- 
            
                    **To create a repository**This example creates a repository and associates it with the user's AWS account. Command: `aws codecommit create-repository --repository-name``MyDemoRepo`--repository-description`"My demonstration repository"`Output: `{ "repositoryMetadata": { "repositoryName": "MyDemoRepo", "cloneUrlSsh": "ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo", "lastModifiedDate": 1444766838.027, "repositoryDescription": "My demonstration repository", "cloneUrlHttp": "https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo", "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE", "Arn": "arn:aws:codecommit:us-east-1:111111111111EXAMPLE:MyDemoRepo", "accountId": "111111111111" } }`- 
                    For API details, see [CreateRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-unreferenced-merge-commit`.

- **AWS CLI**
- 
            
                    **To create an unreferenced commit that represents the result of merging two commit specifiers**The following `create-unreferenced-merge-commit`example creates a commit that represents the results of a merge between a source branch named`bugfix-1234`with a destination branch named`main`using the THREE_WAY_MERGE strategy in a repository named`MyDemoRepo`.`aws codecommit create-unreferenced-merge-commit \ --source-commit-specifier``bugfix-1234`\ --destination-commit-specifier`main`\ --merge-option`THREE_WAY_MERGE`\ --repository-name`MyDemoRepo`\ --name`"Maria Garcia"`\ --email`"maria_garcia@example.com"`\ --commit-message`"Testing the results of this merge."`Output: `{ "commitId": "4f178133EXAMPLE", "treeId": "389765daEXAMPLE" }`For more information, see [Resolve Conflicts in a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-resolve-conflict-pull-request.html#batch-describe-merge-conflicts)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [CreateUnreferencedMergeCommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-unreferenced-merge-commit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `credential-helper`.

- **AWS CLI**
- 
            
                    **To set up the credential helper included in the AWS CLI with AWS CodeCommit**The `credential-helper`utility is not designed to be called directly from the AWS CLI. Instead it is intended to be used as a parameter with the`git config`command to set up your local computer. It enables Git to use HTTPS and a cryptographically signed version of your IAM user credentials or Amazon EC2 instance role whenever Git needs to authenticate with AWS to interact with CodeCommit repositories.`git config --global credential.helper '!aws codecommit credential-helper $@' git config --global credential.UseHttpPath true`Output: `[credential] helper = !aws codecommit credential-helper $@ UseHttpPath = true`For more information, see Setting up for AWS CodeCommit Using Other Methods in the *AWS CodeCommit User Guide*. Review the content carefully, and then follow the procedures in one of the following topics: For HTTPS Connections on Linux, macOS, or Unix or For HTTPS Connections on Windows in the*AWS CodeCommit User Guide*.- 
                    For API details, see [CredentialHelper](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/credential-helper.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-approval-rule-template`.

- **AWS CLI**
- 
            
                    **To delete an approval rule template**The following `delete-approval-rule-template`example deletes the specified approval rule template.`aws codecommit delete-approval-rule-template \ --approval-rule-template-name``1-approver-for-all-pull-requests`Output: `{ "approvalRuleTemplateId": "41de97b7-EXAMPLE" }`For more information, see [Delete an Approval Rule Template](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-template.html#delete-template)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [DeleteApprovalRuleTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-approval-rule-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-branch`.

- **AWS CLI**
- 
            
                    **To delete a branch**This example shows how to delete a branch in an AWS CodeCommit repository. Command: `aws codecommit delete-branch --repository-name``MyDemoRepo`--branch-name`MyNewBranch`Output: `{ "branch": { "commitId": "317f8570EXAMPLE", "branchName": "MyNewBranch" } }`- 
                    For API details, see [DeleteBranch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-branch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-comment-content`.

- **AWS CLI**
- 
            
                    **To delete the content of a comment**You can only delete the content of a comment if you created the comment. This example demonstrates how to delete the content of a comment with the system-generated ID of `ff30b348EXAMPLEb9aa670f`.`aws codecommit delete-comment-content \ --comment-id``ff30b348EXAMPLEb9aa670f`Output: `{ "comment": { "creationDate": 1508369768.142, "deleted": true, "lastModifiedDate": 1508369842.278, "clientRequestToken": "123Example", "commentId": "ff30b348EXAMPLEb9aa670f", "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "callerReactions": [], "reactionCounts": { "CLAP" : 1 } } }`- 
                    For API details, see [DeleteCommentContent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-comment-content.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-file`.

- **AWS CLI**
- 
            
                    **To delete a file**The following `delete-file`example demonstrates how to delete a file named`README.md`from a branch named`main`with a most recent commit ID of`c5709475EXAMPLE`in a repository named`MyDemoRepo`.`aws codecommit delete-file \ --repository-name``MyDemoRepo`\ --branch-name`main`\ --file-path`README.md`\ --parent-commit-id`c5709475EXAMPLE`Output: `{ "blobId":"559b44fEXAMPLE", "commitId":"353cf655EXAMPLE", "filePath":"README.md", "treeId":"6bc824cEXAMPLE" }`For more information, see [Edit or Delete a File in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-edit-file.html?shortFooter=true#how-to-edit-file-cli)in the*AWS CodeCommit API Reference*guide.- 
                    For API details, see [DeleteFile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-file.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-pull-request-approval-rule`.

- **AWS CLI**
- 
            
                    **To delete an approval rule for a pull request**The following `delete-pull-request-approval-rule`example deletes the approval rule named`My Approval Rule`for the specified pull request.`aws codecommit delete-pull-request-approval-rule \ --approval-rule-name``"My Approval Rule"`\ --pull-request-id`15`Output: `{ "approvalRuleId": "077d8e8a8-EXAMPLE" }`For more information, see [Edit or Delete an Approval Rule](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-edit-delete-pull-request-approval-rule.html#delete-pull-request-approval-rule)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [DeletePullRequestApprovalRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-pull-request-approval-rule.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-repository`.

- **AWS CLI**
- 
            
                    **To delete a repository**This example shows how to delete an AWS CodeCommit repository. Command: `aws codecommit delete-repository --repository-name``MyDemoRepo`Output: `{ "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE" }`- 
                    For API details, see [DeleteRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-merge-conflicts`.

- **AWS CLI**
- 
            
                    **To get detailed information about merge conflicts**The following `describe-merge-conflicts`example determines the merge conflicts for a file named`readme.md`in the specified source branch and destination branch using the THREE_WAY_MERGE strategy.`aws codecommit describe-merge-conflicts \ --source-commit-specifier``feature-randomizationfeature`\ --destination-commit-specifier`main`\ --merge-option`THREE_WAY_MERGE`\ --file-path`readme.md`\ --repository-name`MyDemoRepo`Output: `{ "conflictMetadata": { "filePath": "readme.md", "fileSizes": { "source": 139, "destination": 230, "base": 85 }, "fileModes": { "source": "NORMAL", "destination": "NORMAL", "base": "NORMAL" }, "objectTypes": { "source": "FILE", "destination": "FILE", "base": "FILE" }, "numberOfConflicts": 1, "isBinaryFile": { "source": false, "destination": false, "base": false }, "contentConflict": true, "fileModeConflict": false, "objectTypeConflict": false, "mergeOperations": { "source": "M", "destination": "M" } }, "mergeHunks": [ { "isConflict": true, "source": { "startLine": 0, "endLine": 3, "hunkContent": "VGhpcyBpEXAMPLE=" }, "destination": { "startLine": 0, "endLine": 1, "hunkContent": "VXNlIHRoEXAMPLE=" } } ], "destinationCommitId": "86958e0aEXAMPLE", "sourceCommitId": "6ccd57fdEXAMPLE", "baseCommitId": "767b69580EXAMPLE" }`For more information, see [Resolve Conflicts in a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-resolve-conflict-pull-request.html#describe-merge-conflicts)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [DescribeMergeConflicts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/describe-merge-conflicts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-pull-request-events`.

- **AWS CLI**
- 
            
                    **To view events in a pull request**The following `describe-pull-request-events`example retrieves the events for a pull request with the ID of '8'.`aws codecommit describe-pull-request-events --pull-request-id``8`Output: `{ "pullRequestEvents": [ { "pullRequestId": "8", "pullRequestEventType": "PULL_REQUEST_CREATED", "eventDate": 1510341779.53, "actor": "arn:aws:iam::111111111111:user/Zhang_Wei" }, { "pullRequestStatusChangedEventMetadata": { "pullRequestStatus": "CLOSED" }, "pullRequestId": "8", "pullRequestEventType": "PULL_REQUEST_STATUS_CHANGED", "eventDate": 1510341930.72, "actor": "arn:aws:iam::111111111111:user/Jane_Doe" } ] }`- 
                    For API details, see [DescribePullRequestEvents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/describe-pull-request-events.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-approval-rule-template-from-repository`.

- **AWS CLI**
- 
            
                    **To disassociate an approval rule template from a repository**The following `disassociate-approval-rule-template-from-repository`example disassociates the specified approval rule template from a repository named`MyDemoRepo`.`aws codecommit disassociate-approval-rule-template-from-repository \ --repository-name``MyDemoRepo`\ --approval-rule-template-name`1-approver-rule-for-all-pull-requests`This command produces no output. For more information, see [Disassociate an Approval Rule Template](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-disassociate-template.html#disassociate-template)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [DisassociateApprovalRuleTemplateFromRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/disassociate-approval-rule-template-from-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `evaluate-pull-request-approval-rules`.

- **AWS CLI**
- 
            
                    **To evaluate whether a pull request has all of its approval rules satisfied**The following `evaluate-pull-request-approval-rules`example evaluates the state of approval rules on the specified pull request. In this example, an approval rule has not been satisfied for the pull request, so the output of the command shows an`approved`value of`false`.`aws codecommit evaluate-pull-request-approval-rules \ --pull-request-id``27`\ --revision-id`9f29d167EXAMPLE`Output: `{ "evaluation": { "approved": false, "approvalRulesNotSatisfied": [ "Require two approved approvers" ], "overridden": false, "approvalRulesSatisfied": [] } }`For more information, see [Merge a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-merge-pull-request.html#evaluate-pull-request-approval-rules)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [EvaluatePullRequestApprovalRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/evaluate-pull-request-approval-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-approval-rule-template`.

- **AWS CLI**
- 
            
                    **To get the content of an approval rule template**The following `get-approval-rule-template`example gets the content of an approval rule template named`1-approver-rule-for-all-pull-requests`.`aws codecommit get-approval-rule-template \ --approval-rule-template-name``1-approver-rule-for-all-pull-requests`Output: `{ "approvalRuleTemplate": { "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 1,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "ruleContentSha256": "621181bbEXAMPLE", "lastModifiedDate": 1571356106.936, "creationDate": 1571356106.936, "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests", "lastModifiedUser": "arn:aws:iam::123456789012:user/Li_Juan", "approvalRuleTemplateId": "a29abb15-EXAMPLE", "approvalRuleTemplateDescription": "All pull requests must be approved by one developer on the team." } }`For more information, see [Manage Approval Rule Templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html#get-template)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [GetApprovalRuleTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-approval-rule-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-blob`.

- **AWS CLI**
- 
            
                    **To view information about a Git blob object**The following `get-blob`example retrieves information about a Git blob with the ID of '2eb4af3bEXAMPLE' in an AWS CodeCommit repository named 'MyDemoRepo'.`aws codecommit get-blob --repository-name``MyDemoRepo`--blob-id`2eb4af3bEXAMPLE`Output: `{ "content": "QSBCaW5hcnkgTGFyToEXAMPLE=" }`- 
                    For API details, see [GetBlob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-blob.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-branch`.

- **AWS CLI**
- 
            
                    **To get information about a branch**This example gets information about a branch in an AWS CodeCommit repository. Command: `aws codecommit get-branch --repository-name``MyDemoRepo`--branch-name`MyNewBranch`Output: `{ "BranchInfo": { "commitID": "317f8570EXAMPLE", "branchName": "MyNewBranch" } }`- 
                    For API details, see [GetBranch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-branch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-comment-reactions`.

- **AWS CLI**
- 
            
                    **To view emoji reactions to a comment**The following `get-comment-reactions`example lists all emoji reactions to a comment with the ID of`abcd1234EXAMPLEb5678efgh`. If the font for your shell supports displaying Emoji Version 1.0, then in the output for`emoji`the emoji is displayed.`aws codecommit get-comment-reactions \ --comment-id``abcd1234EXAMPLEb5678efgh`Output: `{ "reactionsForComment": { [ { "reaction": { "emoji:"??", "shortCode": "thumbsup", "unicode": "U+1F44D" }, "users": [ "arn:aws:iam::123456789012:user/Li_Juan", "arn:aws:iam::123456789012:user/Mary_Major", "arn:aws:iam::123456789012:user/Jorge_Souza" ] }, { "reaction": { "emoji": "??", "shortCode": "thumbsdown", "unicode": "U+1F44E" }, "users": [ "arn:aws:iam::123456789012:user/Nikhil_Jayashankar" ] }, { "reaction": { "emoji": "??", "shortCode": "confused", "unicode": "U+1F615" }, "users": [ "arn:aws:iam::123456789012:user/Saanvi_Sarkar" ] } ] } }`For more information, see [Comment on a commit in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-commit-comment.html#how-to-commit-comment-cli-commit-emoji-view)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [GetCommentReactions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comment-reactions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-comment`.

- **AWS CLI**
- 
            
                    **To view details of a comment**This example demonstrates how to view details of a comment with the system-generated comment ID of `ff30b348EXAMPLEb9aa670f`.`aws codecommit get-comment \ --comment-id``ff30b348EXAMPLEb9aa670f`Output: `{ "comment": { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "123Example", "commentId": "ff30b348EXAMPLEb9aa670f", "content": "Whoops - I meant to add this comment to the line, but I don't see how to delete it.", "creationDate": 1508369768.142, "deleted": false, "commentId": "", "lastModifiedDate": 1508369842.278, "callerReactions": [], "reactionCounts": { "SMILE" : 6, "THUMBSUP" : 1 } } }`- 
                    For API details, see [GetComment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-comments-for-compared-commit`.

- **AWS CLI**
- 
            
                    **To view comments on a commit**This example demonstrates how to view view comments made on the comparison between two commits in a repository named `MyDemoRepo`.`aws codecommit get-comments-for-compared-commit \ --repository-name``MyDemoRepo`\ --before-commit-ID`6e147360EXAMPLE`\ --after-commit-id`317f8570EXAMPLE`Output: `{ "commentsForComparedCommitData": [ { "afterBlobId": "1f330709EXAMPLE", "afterCommitId": "317f8570EXAMPLE", "beforeBlobId": "80906a4cEXAMPLE", "beforeCommitId": "6e147360EXAMPLE", "comments": [ { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "123Example", "commentId": "ff30b348EXAMPLEb9aa670f", "content": "Whoops - I meant to add this comment to the line, not the file, but I don't see how to delete it.", "creationDate": 1508369768.142, "deleted": false, "CommentId": "123abc-EXAMPLE", "lastModifiedDate": 1508369842.278, "callerReactions": [], "reactionCounts": { "SMILE" : 6, "THUMBSUP" : 1 } }, { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "123Example", "commentId": "553b509bEXAMPLE56198325", "content": "Can you add a test case for this?", "creationDate": 1508369612.240, "deleted": false, "commentId": "456def-EXAMPLE", "lastModifiedDate": 1508369612.240, "callerReactions": [], "reactionCounts": { "THUMBSUP" : 2 } } ], "location": { "filePath": "cl_sample.js", "filePosition": 1232, "relativeFileVersion": "after" }, "repositoryName": "MyDemoRepo" } ], "nextToken": "exampleToken" }`- 
                    For API details, see [GetCommentsForComparedCommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comments-for-compared-commit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-comments-for-pull-request`.

- **AWS CLI**
- 
            
                    **To view comments for a pull request**This example demonstrates how to view comments for a pull request in a repository named `MyDemoRepo`.`aws codecommit get-comments-for-pull-request \ --repository-name``MyDemoRepo`\ --pull-request-id`42`--before-commit-ID`317f8570EXAMPLE`\ --after-commit-id`5d036259EXAMPLE`Output: `{ "commentsForPullRequestData": [ { "afterBlobId": "1f330709EXAMPLE", "afterCommitId": "5d036259EXAMPLE", "beforeBlobId": "80906a4cEXAMPLE", "beforeCommitId": "317f8570EXAMPLE", "comments": [ { "authorArn": "arn:aws:iam::111111111111:user/Saanvi_Sarkar", "clientRequestToken": "", "commentId": "abcd1234EXAMPLEb5678efgh", "content": "These don't appear to be used anywhere. Can we remove them?", "creationDate": 1508369622.123, "deleted": false, "lastModifiedDate": 1508369622.123, "callerReactions": [], "reactionCounts": { "THUMBSUP" : 6, "CONFUSED" : 1 } }, { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "", "commentId": "442b498bEXAMPLE5756813", "content": "Good catch. I'll remove them.", "creationDate": 1508369829.104, "deleted": false, "lastModifiedDate": 150836912.273, "callerReactions": ["THUMBSUP"] "reactionCounts": { "THUMBSUP" : 14 } } ], "location": { "filePath": "ahs_count.py", "filePosition": 367, "relativeFileVersion": "AFTER" }, "repositoryName": "MyDemoRepo", "pullRequestId": "42" } ], "nextToken": "exampleToken" }`- 
                    For API details, see [GetCommentsForPullRequest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-comments-for-pull-request.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-commit`.

- **AWS CLI**
- 
            
                    **To view information about a commit in a repository**This example shows details about a commit with the system-generated ID of '7e9fd3091thisisanexamplethisisanexample1' in an AWS CodeCommit repository named 'MyDemoRepo'. Command: `aws codecommit get-commit --repository-name``MyDemoRepo`--commit-id`7e9fd3091thisisanexamplethisisanexample1`Output: `{ "commit": { "additionalData": "", "committer": { "date": "1484167798 -0800", "name": "Mary Major", "email": "mary_major@example.com" }, "author": { "date": "1484167798 -0800", "name": "Mary Major", "email": "mary_major@example.com" }, "treeId": "347a3408thisisanexampletreeidexample", "parents": [ "7aa87a031thisisanexamplethisisanexample1" ], "message": "Fix incorrect variable name" } }`- 
                    For API details, see [GetCommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-commit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-differences`.

- **AWS CLI**
- 
            
                    **To get information about differences for a commit specifier in a repository**This example shows view metadata information about changes between two commit specifiers (branch, tag, HEAD, or other fully qualified references, such as commit IDs) in a renamed folder in AWS CodeCommit repository named MyDemoRepo. The example includes several options that are not required, including --before-commit-specifier, --before-path, and --after-path, in order to more fully illustrate how you can use these options to limit the results. The response includes file mode permissions. Command: `aws codecommit get-differences --repository-name``MyDemoRepo`--before-commit-specifier`955bba12thisisanexamplethisisanexample`--after-commit-specifier`14a95463thisisanexamplethisisanexample`--before-path`tmp/example-folder`--after-path`tmp/renamed-folder`Output: `{ "differences": [ { "afterBlob": { "path": "blob.txt", "blobId": "2eb4af3b1thisisanexamplethisisanexample1", "mode": "100644" }, "changeType": "M", "beforeBlob": { "path": "blob.txt", "blobId": "bf7fcf281thisisanexamplethisisanexample1", "mode": "100644" } } ] }`- 
                    For API details, see [GetDifferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-differences.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-file`.

- **AWS CLI**
- 
            
                    **To get the base-64 encoded contents of a file in an AWS CodeCommit repository**The following `get-file`example demonstrates how to get the base-64 encoded contents of a file named`README.md`from a branch named`main`in a repository named`MyDemoRepo`.`aws codecommit get-file \ --repository-name``MyDemoRepo`\ --commit-specifier`main`\ --file-path`README.md`Output: `{ "blobId":"559b44fEXAMPLE", "commitId":"c5709475EXAMPLE", "fileContent":"IyBQaHVzEXAMPLE", "filePath":"README.md", "fileMode":"NORMAL", "fileSize":1563 }`For more information, see [GetFile](https://docs.aws.amazon.com/codecommit/latest/APIReference/API_GetFile.html)in the*AWS CodeCommit API Reference*guide.- 
                    For API details, see [GetFile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-file.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-folder`.

- **AWS CLI**
- 
            
                    **To get the contents of a folder in an AWS CodeCommit repository**The following `get-folder`example demonstrates how to get the contents of a top-level folder from a repository named`MyDemoRepo`.`aws codecommit get-folder --repository-name``MyDemoRepo`--folder-path ""Output: `{ "commitId":"c5709475EXAMPLE", "files":[ { "absolutePath":".gitignore", "blobId":"74094e8bEXAMPLE", "fileMode":"NORMAL", "relativePath":".gitignore" }, { "absolutePath":"Gemfile", "blobId":"9ceb72f6EXAMPLE", "fileMode":"NORMAL", "relativePath":"Gemfile" }, { "absolutePath":"Gemfile.lock", "blobId":"795c4a2aEXAMPLE", "fileMode":"NORMAL", "relativePath":"Gemfile.lock" }, { "absolutePath":"LICENSE.txt", "blobId":"0c7932c8EXAMPLE", "fileMode":"NORMAL", "relativePath":"LICENSE.txt" }, { "absolutePath":"README.md", "blobId":"559b44feEXAMPLE", "fileMode":"NORMAL", "relativePath":"README.md" } ], "folderPath":"", "subFolders":[ { "absolutePath":"public", "relativePath":"public", "treeId":"d5e92ae3aEXAMPLE" }, { "absolutePath":"tmp", "relativePath":"tmp", "treeId":"d564d0bcEXAMPLE" } ], "subModules":[], "symbolicLinks":[], "treeId":"7b3c4dadEXAMPLE" }`For more information, see GetFolder in the *AWS CodeCommit API Reference*guide.- 
                    For API details, see [GetFolder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-folder.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-merge-commit`.

- **AWS CLI**
- 
            
                    **To get detailed information about a merge commit**The following `get-merge-commit`example displays details about a merge commit for the source branch named`bugfix-bug1234`with a destination branch named`main`in a repository named`MyDemoRepo`.`aws codecommit get-merge-commit \ --source-commit-specifier``bugfix-bug1234`\ --destination-commit-specifier`main`\ --repository-name`MyDemoRepo`Output: `{ "sourceCommitId": "c5709475EXAMPLE", "destinationCommitId": "317f8570EXAMPLE", "baseCommitId": "fb12a539EXAMPLE", "mergeCommitId": "ffc4d608eEXAMPLE" }`For more information, see [View Commit Details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-commit-details.html#how-to-view-commit-details-cli-merge-commit)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [GetMergeCommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-merge-commit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-merge-conflicts`.

- **AWS CLI**
- 
            
                    **To view whether there are any merge conflicts for a pull request**The following `get-merge-conflicts`example displays whether there are any merge conflicts between the tip of a source branch named`feature-randomizationfeature`and a destination branch named 'main' in a repository named`MyDemoRepo`.`aws codecommit get-merge-conflicts \ --repository-name``MyDemoRepo`\ --source-commit-specifier`feature-randomizationfeature`\ --destination-commit-specifier`main`\ --merge-option`THREE_WAY_MERGE`Output: `{ "mergeable": false, "destinationCommitId": "86958e0aEXAMPLE", "sourceCommitId": "6ccd57fdEXAMPLE", "baseCommitId": "767b6958EXAMPLE", "conflictMetadataList": [ { "filePath": "readme.md", "fileSizes": { "source": 139, "destination": 230, "base": 85 }, "fileModes": { "source": "NORMAL", "destination": "NORMAL", "base": "NORMAL" }, "objectTypes": { "source": "FILE", "destination": "FILE", "base": "FILE" }, "numberOfConflicts": 1, "isBinaryFile": { "source": false, "destination": false, "base": false }, "contentConflict": true, "fileModeConflict": false, "objectTypeConflict": false, "mergeOperations": { "source": "M", "destination": "M" } } ] }`- 
                    For API details, see [GetMergeConflicts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-merge-conflicts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-merge-options`.

- **AWS CLI**
- 
            
                    **To get information about the merge options available for merging two specified branches**The following `get-merge-options`example determines the merge options available for merging a source branch named`bugfix-bug1234`with a destination branch named`main`in a repository named`MyDemoRepo`.`aws codecommit get-merge-options \ --source-commit-specifier``bugfix-bug1234`\ --destination-commit-specifier`main`\ --repository-name`MyDemoRepo`Output: `{ "mergeOptions": [ "FAST_FORWARD_MERGE", "SQUASH_MERGE", "THREE_WAY_MERGE" ], "sourceCommitId": "18059494EXAMPLE", "destinationCommitId": "ffd3311dEXAMPLE", "baseCommitId": "ffd3311dEXAMPLE" }`For more information, see [Resolve Conflicts in a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-resolve-conflict-pull-request.html#get-merge-options)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [GetMergeOptions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-merge-options.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-pull-request-approval-states`.

- **AWS CLI**
- 
            
                    **To view approvals on a pull request**The following `get-pull-request-approval-states`example returns approvals for the specified pull request.`aws codecommit get-pull-request-approval-states \ --pull-request-id``8`\ --revision-id`9f29d167EXAMPLE`Output: `{ "approvals": [ { "userArn": "arn:aws:iam::123456789012:user/Mary_Major", "approvalState": "APPROVE" } ] }`For more information, see [View Pull Requests](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-pull-request.html#get-pull-request-approval-state)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [GetPullRequestApprovalStates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request-approval-states.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-pull-request-override-state`.

- **AWS CLI**
- 
            
                    **To get information about the override status of a pull request**The following `get-pull-request-override-state`example returns the override state for the specified pull request. In this example, the approval rules for the pull request were overridden by a user named Mary Major, so the output returns a value of`true`.:`aws codecommit get-pull-request-override-state \ --pull-request-id``34`\ --revision-id`9f29d167EXAMPLE`Output: `{ "overridden": true, "overrider": "arn:aws:iam::123456789012:user/Mary_Major" }`For more information, see [Override Approval Rules on a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-override-approval-rules.html#get-override-status)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [GetPullRequestOverrideState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request-override-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-pull-request`.

- **AWS CLI**
- 
            
                    **To view details of a pull request**This example demonstrates how to view information about a pull request with the ID of `27`.`aws codecommit get-pull-request \ --pull-request-id``27`Output: `{ "pullRequest": { "approvalRules": [ { "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleId": "dd8b17fe-EXAMPLE", "approvalRuleName": "2-approver-rule-for-main", "creationDate": 1571356106.936, "lastModifiedDate": 571356106.936, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "ruleContentSha256": "4711b576EXAMPLE" } ], "lastActivityDate": 1562619583.565, "pullRequestTargets": [ { "sourceCommit": "ca45e279EXAMPLE", "sourceReference": "refs/heads/bugfix-1234", "mergeBase": "a99f5ddbEXAMPLE", "destinationReference": "refs/heads/main", "mergeMetadata": { "isMerged": false }, "destinationCommit": "2abfc6beEXAMPLE", "repositoryName": "MyDemoRepo" } ], "revisionId": "e47def21EXAMPLE", "title": "Quick fix for bug 1234", "authorArn": "arn:aws:iam::123456789012:user/Nikhil_Jayashankar", "clientRequestToken": "d8d7612e-EXAMPLE", "creationDate": 1562619583.565, "pullRequestId": "27", "pullRequestStatus": "OPEN" } }`- 
                    For API details, see [GetPullRequest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-pull-request.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-repository-triggers`.

- **AWS CLI**
- 
            
                    **To get information about triggers in a repository**This example shows details about triggers configured for an AWS CodeCommit repository named `MyDemoRepo`.`aws codecommit get-repository-triggers \ --repository-name``MyDemoRepo`Output: `{ "configurationId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE", "triggers": [ { "destinationArn": "arn:aws:sns:us-east-1:111111111111:MyCodeCommitTopic", "branches": [ "main", "preprod" ], "name": "MyFirstTrigger", "customData": "", "events": [ "all" ] }, { "destinationArn": "arn:aws:lambda:us-east-1:111111111111:function:MyCodeCommitPythonFunction", "branches": [], "name": "MySecondTrigger", "customData": "EXAMPLE", "events": [ "all" ] } ] }`- 
                    For API details, see [GetRepositoryTriggers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository-triggers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-repository`.

- **AWS CLI**
- 
            
                    **To get information about a repository**This example shows details about an AWS CodeCommit repository. `aws codecommit get-repository \ --repository-name``MyDemoRepo`Output: `{ "repositoryMetadata": { "creationDate": 1429203623.625, "defaultBranch": "main", "repositoryName": "MyDemoRepo", "cloneUrlSsh": "ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/v1/repos/MyDemoRepo", "lastModifiedDate": 1430783812.0869999, "repositoryDescription": "My demonstration repository", "cloneUrlHttp": "https://codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo", "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE", "Arn": "arn:aws:codecommit:us-east-1:80398EXAMPLE:MyDemoRepo "accountId": "111111111111" } }`- 
                    For API details, see [GetRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-approval-rule-templates`.

- **AWS CLI**
- 
            
                    **To list all approval rule templates in an AWS Region**The following `list-approval-rule-templates`example lists all approval rule templates in the specified Region. If no AWS Region is specified as a parameter, the command returns approval rule templates for the region specified in the AWS CLI profile used to run the command.`aws codecommit list-approval-rule-templates \ --region``us-east-2`Output: `{ "approvalRuleTemplateNames": [ "2-approver-rule-for-main", "1-approver-rule-for-all-pull-requests" ] }`For more information, see [Manage Approval Rule Templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html#list-templates)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [ListApprovalRuleTemplates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-approval-rule-templates.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-associated-approval-rule-templates-for-repository`.

- **AWS CLI**
- 
            
                    **To list all templates associated with a repository**The following `list-associated-approval-rule-templates-for-repository`example lists all approval rule templates associated with a repository named`MyDemoRepo`.`aws codecommit list-associated-approval-rule-templates-for-repository \ --repository-name``MyDemoRepo`Output: `{ "approvalRuleTemplateNames": [ "2-approver-rule-for-main", "1-approver-rule-for-all-pull-requests" ] }`For more information, see [Manage Approval Rule Templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html#list-associated-templates)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [ListAssociatedApprovalRuleTemplatesForRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-associated-approval-rule-templates-for-repository.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-branches`.

- **AWS CLI**
- 
            
                    **To view a list of branch names**This example lists all branch names in an AWS CodeCommit repository. `aws codecommit list-branches \ --repository-name``MyDemoRepo`Output: `{ "branches": [ "MyNewBranch", "main" ] }`- 
                    For API details, see [ListBranches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-branches.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-pull-requests`.

- **AWS CLI**
- 
            
                    **To view a list of pull requests in a repository**This example demonstrates how to list pull requests created by an IAM user with the ARN 'arn:aws:iam::111111111111:user/Li_Juan' and the status of 'CLOSED' in an AWS CodeCommit repository named 'MyDemoRepo': `aws codecommit list-pull-requests --author-arn``arn:aws:iam::111111111111:user/Li_Juan`--pull-request-status`CLOSED`--repository-name`MyDemoRepo`Output: `{ "nextToken": "", "pullRequestIds": ["2","12","16","22","23","35","30","39","47"] }`- 
                    For API details, see [ListPullRequests](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-pull-requests.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-repositories-for-approval-rule-template`.

- **AWS CLI**
- 
            
                    **To list all repositories associated with a template**The following `list-repositories-for-approval-rule-template`example lists all repositories associated with the specified approval rule template.`aws codecommit list-repositories-for-approval-rule-template \ --approval-rule-template-name``2-approver-rule-for-main`Output: `{ "repositoryNames": [ "MyDemoRepo", "MyClonedRepo" ] }`For more information, see [Manage Approval Rule Templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html#list-associated-repositories)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [ListRepositoriesForApprovalRuleTemplate](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-repositories-for-approval-rule-template.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-repositories`.

- **AWS CLI**
- 
            
                    **To view a list of repositories**This example lists all AWS CodeCommit repositories associated with the user's AWS account. Command: `aws codecommit list-repositories`Output: `{ "repositories": [ { "repositoryName": "MyDemoRepo" "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE", }, { "repositoryName": "MyOtherDemoRepo" "repositoryId": "cfc29ac4-b0cb-44dc-9990-f6f51EXAMPLE" } ] }`- 
                    For API details, see [ListRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-repositories.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To view the AWS tags for a repository**The following `list-tags-for-resource`example lists tag keys and tag values for the specified repository.`aws codecommit list-tags-for-resource \ --resource-arn``arn:aws:codecommit:us-west-2:111111111111:MyDemoRepo`Output: `{ "tags": { "Status": "Secret", "Team": "Saanvi" } }`For more information, see [View Tags for a Repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository-list.html#how-to-tag-repository-list-cli)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `merge-branches-by-fast-forward`.

- **AWS CLI**
- 
            
                    **To merge two branches using the fast-forward merge strategy**The following `merge-branches-by-fast-forward`example merges the specified source branch with the specified destination branch in a repository named`MyDemoRepo`.`aws codecommit merge-branches-by-fast-forward \ --source-commit-specifier``bugfix-bug1234`\ --destination-commit-specifier`bugfix-bug1233`\ --repository-name`MyDemoRepo`Output: `{ "commitId": "4f178133EXAMPLE", "treeId": "389765daEXAMPLE" }`For more information, see [Compare and Merge Branches](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-compare-branches.html#merge-branches-by-fast-forward)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [MergeBranchesByFastForward](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-branches-by-fast-forward.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `merge-branches-by-squash`.

- **AWS CLI**
- 
            
                    **To merge two branches using the squash merge strategy**The following `merge-branches-by-squash`example merges the specified source branch with the specified destination branch in a repository named`MyDemoRepo`.`aws codecommit merge-branches-by-squash \ --source-commit-specifier``bugfix-bug1234`\ --destination-commit-specifier`bugfix-bug1233`\ --author-name`"Maria Garcia"`\ --email`"maria_garcia@example.com"`\ --commit-message`"Merging two fix branches to prepare for a general patch."`\ --repository-name`MyDemoRepo`Output: `{ "commitId": "4f178133EXAMPLE", "treeId": "389765daEXAMPLE" }`For more information, see [Compare and Merge Branches](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-compare-branches.html#merge-branches-by-squash)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [MergeBranchesBySquash](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-branches-by-squash.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `merge-branches-by-three-way`.

- **AWS CLI**
- 
            
                    **To merge two branches using the three-way merge strategy**The following `merge-branches-by-three-way`example merges the specified source branch with the specified destination branch in a repository named`MyDemoRepo`.`aws codecommit merge-branches-by-three-way \ --source-commit-specifier``main`\ --destination-commit-specifier`bugfix-bug1234`\ --author-name`"Jorge Souza"`--email`"jorge_souza@example.com"`\ --commit-message`"Merging changes from main to bugfix branch before additional testing."`\ --repository-name`MyDemoRepo`Output: `{ "commitId": "4f178133EXAMPLE", "treeId": "389765daEXAMPLE" }`For more information, see [Compare and Merge Branches](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-compare-branches.html#merge-branches-by-three-way)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [MergeBranchesByThreeWay](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-branches-by-three-way.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `merge-pull-request-by-fast-forward`.

- **AWS CLI**
- 
            
                    **To merge and close a pull request**This example demonstrates how to merge and close a pull request with the ID of '47' and a source commit ID of '99132ab0EXAMPLE' in a repository named `MyDemoRepo`.`aws codecommit merge-pull-request-by-fast-forward \ --pull-request-id``47`\ --source-commit-id`99132ab0EXAMPLE`\ --repository-name`MyDemoRepo`Output: `{ "pullRequest": { "approvalRules": [ { "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 1,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleId": "dd8b17fe-EXAMPLE", "approvalRuleName": "I want one approver for this pull request", "creationDate": 1571356106.936, "lastModifiedDate": 571356106.936, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "ruleContentSha256": "4711b576EXAMPLE" } ], "authorArn": "arn:aws:iam::123456789012:user/Li_Juan", "clientRequestToken": "", "creationDate": 1508530823.142, "description": "Review the latest changes and updates to the global variables", "lastActivityDate": 1508887223.155, "pullRequestId": "47", "pullRequestStatus": "CLOSED", "pullRequestTargets": [ { "destinationCommit": "9f31c968EXAMPLE", "destinationReference": "refs/heads/main", "mergeMetadata": { "isMerged": true, "mergedBy": "arn:aws:iam::123456789012:user/Mary_Major" }, "repositoryName": "MyDemoRepo", "sourceCommit": "99132ab0EXAMPLE", "sourceReference": "refs/heads/variables-branch" } ], "title": "Consolidation of global variables" } }`For more information, see [Merge a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-merge-pull-request.html#merge-pull-request-by-fast-forward)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [MergePullRequestByFastForward](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-pull-request-by-fast-forward.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `merge-pull-request-by-squash`.

- **AWS CLI**
- 
            
                    **To merge a pull request using the squash merge strategy**The following `merge-pull-request-by-squash`example merges and closes the specified pull request using the conflict resolution strategy of ACCEPT_SOURCE in a repository named`MyDemoRepo`.`aws codecommit merge-pull-request-by-squash \ --pull-request-id``47`\ --source-commit-id`99132ab0EXAMPLE`\ --repository-name`MyDemoRepo`\ --conflict-detail-level`LINE_LEVEL`\ --conflict-resolution-strategy`ACCEPT_SOURCE`\ --name`"Jorge Souza"`--email`"jorge_souza@example.com"`\ --commit-message`"Merging pull request 47 by squash and accepting source in merge conflicts"`Output: `{ "pullRequest": { "approvalRules": [ { "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleId": "dd8b17fe-EXAMPLE", "approvalRuleName": "2-approver-rule-for-main", "creationDate": 1571356106.936, "lastModifiedDate": 571356106.936, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "originApprovalRuleTemplate": { "approvalRuleTemplateId": "dd8b17fe-EXAMPLE", "approvalRuleTemplateName": "2-approver-rule-for-main" }, "ruleContentSha256": "4711b576EXAMPLE" } ], "authorArn": "arn:aws:iam::123456789012:user/Li_Juan", "clientRequestToken": "", "creationDate": 1508530823.142, "description": "Review the latest changes and updates to the global variables", "lastActivityDate": 1508887223.155, "pullRequestId": "47", "pullRequestStatus": "CLOSED", "pullRequestTargets": [ { "destinationCommit": "9f31c968EXAMPLE", "destinationReference": "refs/heads/main", "mergeMetadata": { "isMerged": true, "mergedBy": "arn:aws:iam::123456789012:user/Mary_Major" }, "repositoryName": "MyDemoRepo", "sourceCommit": "99132ab0EXAMPLE", "sourceReference": "refs/heads/variables-branch" } ], "title": "Consolidation of global variables" } }`For more information, see [Merge a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-merge-pull-request.html#merge-pull-request-by-squash)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [MergePullRequestBySquash](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-pull-request-by-squash.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `merge-pull-request-by-three-way`.

- **AWS CLI**
- 
            
                    **To merge a pull request using the three-way merge strategy**The following `merge-pull-request-by-three-way`example merges and closes the specified pull request using the default options for conflict detail and conflict resolution strategy in a repository named`MyDemoRepo`.`aws codecommit merge-pull-request-by-three-way \ --pull-request-id``47`\ --source-commit-id`99132ab0EXAMPLE`\ --repository-name`MyDemoRepo`\ --name`"Maria Garcia"`\ --email`"maria_garcia@example.com"`\ --commit-message`"Merging pull request 47 by three-way with default options"`Output: `{ "pullRequest": { "approvalRules": [ { "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleId": "dd8b17fe-EXAMPLE", "approvalRuleName": "2-approver-rule-for-main", "creationDate": 1571356106.936, "lastModifiedDate": 571356106.936, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "originApprovalRuleTemplate": { "approvalRuleTemplateId": "dd8b17fe-EXAMPLE", "approvalRuleTemplateName": "2-approver-rule-for-main" }, "ruleContentSha256": "4711b576EXAMPLE" } ], "authorArn": "arn:aws:iam::123456789012:user/Li_Juan", "clientRequestToken": "", "creationDate": 1508530823.142, "description": "Review the latest changes and updates to the global variables", "lastActivityDate": 1508887223.155, "pullRequestId": "47", "pullRequestStatus": "CLOSED", "pullRequestTargets": [ { "destinationCommit": "9f31c968EXAMPLE", "destinationReference": "refs/heads/main", "mergeMetadata": { "isMerged": true, "mergedBy": "arn:aws:iam::123456789012:user/Mary_Major" }, "repositoryName": "MyDemoRepo", "sourceCommit": "99132ab0EXAMPLE", "sourceReference": "refs/heads/variables-branch" } ], "title": "Consolidation of global variables" } }`For more information, see [Merge a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-merge-pull-request.html#merge-pull-request-by-three-way)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [MergePullRequestByThreeWay](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/merge-pull-request-by-three-way.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `override-pull-request-approval-rules`.

- **AWS CLI**
- 
            
                    **To override approval rule requirements on a pull request**The following `override-pull-request-approval-rules`example overrides approval rules on the specified pull request. To revoke an override instead, set the`--override-status`parameter value to`REVOKE`.`aws codecommit override-pull-request-approval-rules \ --pull-request-id``34`\ --revision-id`927df8d8EXAMPLE`\ --override-status`OVERRIDE`This command produces no output. For more information, see [Override Approval Rules on a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-override-approval-rules.html#override-approval-rules)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [OverridePullRequestApprovalRules](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/override-pull-request-approval-rules.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `post-comment-for-compared-commit`.

- **AWS CLI**
- 
            
                    **To create a comment on a commit**This example demonstrates how to add the comment `"Can you add a test case for this?"`on the change to the`cl_sample.js`file in the comparison between two commits in a repository named`MyDemoRepo`.`aws codecommit post-comment-for-compared-commit \ --repository-name``MyDemoRepo`\ --before-commit-id`317f8570EXAMPLE`\ --after-commit-id`5d036259EXAMPLE`\ --client-request-token`123Example`\ --content`"Can you add a test case for this?"`\ --location`filePath=cl_sample.js,filePosition=1232,relativeFileVersion=AFTER`Output: `{ "afterBlobId": "1f330709EXAMPLE", "afterCommitId": "317f8570EXAMPLE", "beforeBlobId": "80906a4cEXAMPLE", "beforeCommitId": "6e147360EXAMPLE", "comment": { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "", "commentId": "553b509bEXAMPLE56198325", "content": "Can you add a test case for this?", "creationDate": 1508369612.203, "deleted": false, "commentId": "abc123-EXAMPLE", "lastModifiedDate": 1508369612.203, "callerReactions": [], "reactionCounts": [] }, "location": { "filePath": "cl_sample.js", "filePosition": 1232, "relativeFileVersion": "AFTER" , "repositoryName": "MyDemoRepo" } }`- 
                    For API details, see [PostCommentForComparedCommit](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-for-compared-commit.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `post-comment-for-pull-request`.

- **AWS CLI**
- 
            
                    **To add a comment to a pull request**The following `post-comment-for-pull-request`example adds the comment "These don't appear to be used anywhere. Can we remove them?" on the change to the`ahs_count.py`file in a pull request with the ID of`47`in a repository named`MyDemoRepo`.`aws codecommit post-comment-for-pull-request \ --pull-request-id``"47"`\ --repository-name`MyDemoRepo`\ --before-commit-id`317f8570EXAMPLE`\ --after-commit-id`5d036259EXAMPLE`\ --client-request-token`123Example`\ --content`"These don't appear to be used anywhere. Can we remove them?"`\ --location`filePath=ahs_count.py,filePosition=367,relativeFileVersion=AFTER`Output: `{ "afterBlobId": "1f330709EXAMPLE", "afterCommitId": "5d036259EXAMPLE", "beforeBlobId": "80906a4cEXAMPLE", "beforeCommitId": "317f8570EXAMPLE", "comment": { "authorArn": "arn:aws:iam::111111111111:user/Saanvi_Sarkar", "clientRequestToken": "123Example", "commentId": "abcd1234EXAMPLEb5678efgh", "content": "These don't appear to be used anywhere. Can we remove them?", "creationDate": 1508369622.123, "deleted": false, "CommentId": "", "lastModifiedDate": 1508369622.123, "callerReactions": [], "reactionCounts": [] }, "location": { "filePath": "ahs_count.py", "filePosition": 367, "relativeFileVersion": "AFTER" }, "repositoryName": "MyDemoRepo", "pullRequestId": "47" }`- 
                    For API details, see [PostCommentForPullRequest](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-for-pull-request.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `post-comment-reply`.

- **AWS CLI**
- 
            
                    **To reply to a comment on a commit or in a pull request**This example demonstrates how to add the reply `"Good catch. I'll remove them."`to the comment with the system-generated ID of`abcd1234EXAMPLEb5678efgh`.`aws codecommit post-comment-reply \ --in-reply-to``abcd1234EXAMPLEb5678efgh`\ --content`"Good catch. I'll remove them."`\ --client-request-token`123Example`Output: `{ "comment": { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "123Example", "commentId": "442b498bEXAMPLE5756813", "content": "Good catch. I'll remove them.", "creationDate": 1508369829.136, "deleted": false, "CommentId": "abcd1234EXAMPLEb5678efgh", "lastModifiedDate": 150836912.221, "callerReactions": [], "reactionCounts": [] } }`- 
                    For API details, see [PostCommentReply](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/post-comment-reply.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-comment-reaction`.

- **AWS CLI**
- 
            
                    **To reply to a comment on a commit with an emoji**The following `put-comment-reaction`example replies to a comment with the ID of`abcd1234EXAMPLEb5678efgh`with an emoji reaction value of`:thumbsup:`.`aws codecommit put-comment-reaction \ --comment-id``abcd1234EXAMPLEb5678efgh`\ --reaction-value`:thumbsup:`This command produces no output. For more information, see [Comment on a commit in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-commit-comment.html#how-to-commit-comment-cli-commit-reply-emoji)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [PutCommentReaction](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-comment-reaction.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-file`.

- **AWS CLI**
- 
            
                    **To add a file to a repository**The following `put-file`example adds a file named 'ExampleSolution.py' to a repository named 'MyDemoRepo' to a branch named 'feature-randomizationfeature' whose most recent commit has an ID of '4c925148EXAMPLE'.`aws codecommit put-file \ --repository-name``MyDemoRepo`\ --branch-name`feature-randomizationfeature`\ --file-content`file://MyDirectory/ExampleSolution.py`\ --file-path`/solutions/ExampleSolution.py`\ --parent-commit-id`4c925148EXAMPLE`\ --name`"Maria Garcia"`\ --email`"maria_garcia@example.com"`\ --commit-message`"I added a third randomization routine."`Output: `{ "blobId": "2eb4af3bEXAMPLE", "commitId": "317f8570EXAMPLE", "treeId": "347a3408EXAMPLE" }`- 
                    For API details, see [PutFile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-file.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-repository-triggers`.

- **AWS CLI**
- 
            
                    **To add or update a trigger in a repository**This example demonstrates how to update triggers named 'MyFirstTrigger' and 'MySecondTrigger' using an already-created JSON file (here named MyTriggers.json) that contains the structure of all the triggers for a repository named MyDemoRepo. To learn how to get the JSON for existing triggers, see the get-repository-triggers command. `aws codecommit put-repository-triggers \ --repository-name``MyDemoRepo`--triggers`file://MyTriggers.json`Contents of `MyTriggers.json`:`{ "repositoryName": "MyDemoRepo", "triggers": [ { "destinationArn": "arn:aws:sns:us-east-1:80398EXAMPLE:MyCodeCommitTopic", "branches": [ "main", "preprod" ], "name": "MyFirstTrigger", "customData": "", "events": [ "all" ] }, { "destinationArn": "arn:aws:lambda:us-east-1:111111111111:function:MyCodeCommitPythonFunction", "branches": [], "name": "MySecondTrigger", "customData": "EXAMPLE", "events": [ "all" ] } ] }`Output: `{ "configurationId": "6fa51cd8-35c1-EXAMPLE" }`- 
                    For API details, see [PutRepositoryTriggers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/put-repository-triggers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add AWS tags to an existing repository**The following `tag-resource`example tags the specified repository with two tags.`aws codecommit tag-resource \ --resource-arn``arn:aws:codecommit:us-west-2:111111111111:MyDemoRepo`\ --tags`Status=Secret,Team=Saanvi`This command produces no output. For more information, see [Add a Tag to a Repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository-add.html#how-to-tag-repository-add-cli)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `test-repository-triggers`.

- **AWS CLI**
- 
            
                    **To test triggers in a repository**This example demonstrates how to test a trigger named 'MyFirstTrigger' in an AWS CodeCommit repository named MyDemoRepo. In this example, events in the repository trigger notifications from an Amazon Simple Notification Service (Amazon SNS) topic. Command: `aws codecommit test-repository-triggers --repository-name``MyDemoRepo`--triggers`name=MyFirstTrigger,destinationArn=arn:aws:sns:us-east-1:111111111111:MyCodeCommitTopic,branches=mainline,preprod,events=all`Output: `{ "successfulExecutions": [ "MyFirstTrigger" ], "failedExecutions": [] }`- 
                    For API details, see [TestRepositoryTriggers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/test-repository-triggers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove AWS tags from a repository**The following `untag-resource`example removes the tag with the specified key from the repository named`MyDemoRepo`.`aws codecommit untag-resource \ --resource-arn``arn:aws:codecommit:us-west-2:111111111111:MyDemoRepo`\ --tag-keys`Status`This command produces no output. For more information, see [Remove a Tag from a Repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-tag-repository-delete.html#how-to-tag-repository-delete-cli)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-approval-rule-template-content`.

- **AWS CLI**
- 
            
                    **To update the content of an approval rule template**The following `update-approval-rule-template-content`example changes the content of the specified approval rule template to redefine the approval pool to users who assume the role of`CodeCommitReview`.`aws codecommit update-approval-rule-template-content \ --approval-rule-template-name``1-approver-rule`\ --new-rule-content "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}"Output: `{ "approvalRuleTemplate": { "creationDate": 1571352720.773, "approvalRuleTemplateDescription": "Requires 1 approval for all pull requests from the CodeCommitReview pool", "lastModifiedDate": 1571358728.41, "approvalRuleTemplateId": "41de97b7-EXAMPLE", "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 1,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests", "ruleContentSha256": "2f6c21a5EXAMPLE", "lastModifiedUser": "arn:aws:iam::123456789012:user/Li_Juan" } }`For more information, see [Manage Approval Rule Templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html#update-template-content)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [UpdateApprovalRuleTemplateContent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-content.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-approval-rule-template-description`.

- **AWS CLI**
- 
            
                    **To update the description of an approval rule template**The following `update-approval-rule-template-description`example changes the description of the specified approval rule template to`Requires 1 approval for all pull requests from the CodeCommitReview pool`.:`aws codecommit update-approval-rule-template-description \ --approval-rule-template-name``1-approver-rule-for-all-pull-requests`\ --approval-rule-template-description`"Requires 1 approval for all pull requests from the CodeCommitReview pool"`Output: `{ "approvalRuleTemplate": { "creationDate": 1571352720.773, "approvalRuleTemplateDescription": "Requires 1 approval for all pull requests from the CodeCommitReview pool", "lastModifiedDate": 1571358728.41, "approvalRuleTemplateId": "41de97b7-EXAMPLE", "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 1,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests", "ruleContentSha256": "2f6c21a5EXAMPLE", "lastModifiedUser": "arn:aws:iam::123456789012:user/Li_Juan" } }`For more information, see [Manage Approval Rule Templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html#update-template-description)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [UpdateApprovalRuleTemplateDescription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-description.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-approval-rule-template-name`.

- **AWS CLI**
- 
            
                    **To update the name of an approval rule template**The following `update-approval-rule-template-name`example changes the name of an approval rule template from`1-approver-rule`to 1-approver-rule-for-all-pull-requests`.`aws codecommit update-approval-rule-template-name \ --old-approval-rule-template-name``1-approver-rule`\ --new-approval-rule-template-name`1-approver-rule-for-all-pull-requests`Output: `{ "approvalRuleTemplate": { "approvalRuleTemplateName": "1-approver-rule-for-all-pull-requests", "lastModifiedDate": 1571358241.619, "approvalRuleTemplateId": "41de97b7-EXAMPLE", "approvalRuleTemplateContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 1,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "creationDate": 1571352720.773, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "approvalRuleTemplateDescription": "All pull requests must be approved by one developer on the team.", "ruleContentSha256": "2f6c21a5cEXAMPLE" } }`For more information, see [Manage Approval Rule Templates](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-manage-templates.html#update-template-description)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [UpdateApprovalRuleTemplateName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-approval-rule-template-name.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-comment`.

- **AWS CLI**
- 
            
                    **To update a comment on a commit**This example demonstrates how to add the content `"Fixed as requested. I'll update the pull request."`to a comment with an ID of`442b498bEXAMPLE5756813`.`aws codecommit update-comment \ --comment-id``442b498bEXAMPLE5756813`\ --content`"Fixed as requested. I'll update the pull request."`Output: `{ "comment": { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "", "commentId": "442b498bEXAMPLE5756813", "content": "Fixed as requested. I'll update the pull request.", "creationDate": 1508369929.783, "deleted": false, "lastModifiedDate": 1508369929.287, "callerReactions": [], "reactionCounts": { "THUMBSUP" : 2 } } }`- 
                    For API details, see [UpdateComment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-comment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-default-branch`.

- **AWS CLI**
- 
            
                    **To change the default branch for a repository**This example changes the default branch for an AWS CodeCommit repository. This command produces output only if there are errors. Command: `aws codecommit update-default-branch --repository-name``MyDemoRepo`--default-branch-name`MyNewBranch`Output: `None.`- 
                    For API details, see [UpdateDefaultBranch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-default-branch.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-pull-request-approval-rule-content`.

- **AWS CLI**
- 
            
                    **To edit an approval rule for a pull request**The following `update-pull-request-approval-rule-content`example updates she specified approval rule to require one user approval from an approval pool that includes any IAM user in the`123456789012`AWS account.`aws codecommit update-pull-request-approval-rule-content \ --pull-request-id``27`\ --approval-rule-name`"Require two approved approvers"`\ --new-rule-content "{Version: 2018-11-08, Statements: [{Type: \"Approvers\", NumberOfApprovalsNeeded: 1, ApprovalPoolMembers:[\"CodeCommitApprovers:123456789012:user/*\"]}]}}"Output: `{ "approvalRule": { "approvalRuleContent": "{Version: 2018-11-08, Statements: [{Type: \"Approvers\", NumberOfApprovalsNeeded: 1, ApprovalPoolMembers:[\"CodeCommitApprovers:123456789012:user/*\"]}]}}", "approvalRuleId": "aac33506-EXAMPLE", "originApprovalRuleTemplate": {}, "creationDate": 1570752871.932, "lastModifiedDate": 1570754058.333, "approvalRuleName": Require two approved approvers", "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "ruleContentSha256": "cd93921cEXAMPLE", } }`For more information, see [Edit or Delete an Approval Rule](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-edit-delete-pull-request-approval-rule.html#update-pull-request-approval-rule-content)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [UpdatePullRequestApprovalRuleContent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-rule-content.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-pull-request-approval-state`.

- **AWS CLI**
- 
            
                    **To approve or revoke approval for a pull request**The following `update-pull-request-approval-state`example approves a pull request with the ID of`27`and a revision ID of`9f29d167EXAMPLE`. If you wanted to revoke approval instead, then set the`--approval-state`parameter value to`REVOKE`.`aws codecommit update-pull-request-approval-state \ --pull-request-id``27`\ --revision-id`9f29d167EXAMPLE`\ --approval-state`"APPROVE"`This command produces no output. For more information, see [Review a Pull Request](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-review-pull-request.html#update-pull-request-approval-state)in the*AWS CodeCommit User Guide*.- 
                    For API details, see [UpdatePullRequestApprovalState](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-approval-state.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-pull-request-description`.

- **AWS CLI**
- 
            
                    **To change the description of a pull request**This example demonstrates how to change the description of a pull request with the ID of `47`.`aws codecommit update-pull-request-description \ --pull-request-id``47`\ --description`"Updated the pull request to remove unused global variable."`Output: `{ "pullRequest": { "authorArn": "arn:aws:iam::111111111111:user/Li_Juan", "clientRequestToken": "", "creationDate": 1508530823.155, "description": "Updated the pull request to remove unused global variable.", "lastActivityDate": 1508372423.204, "pullRequestId": "47", "pullRequestStatus": "OPEN", "pullRequestTargets": [ { "destinationCommit": "9f31c968EXAMPLE", "destinationReference": "refs/heads/main", "mergeMetadata": { "isMerged": false, }, "repositoryName": "MyDemoRepo", "sourceCommit": "99132ab0EXAMPLE", "sourceReference": "refs/heads/variables-branch" } ], "title": "Consolidation of global variables" } }`- 
                    For API details, see [UpdatePullRequestDescription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-description.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-pull-request-status`.

- **AWS CLI**
- 
            
                    **To change the status of a pull request**This example demonstrates how to to change the status of a pull request with the ID of `42`to a status of`CLOSED`in an AWS CodeCommit repository named`MyDemoRepo`.`aws codecommit update-pull-request-status \ --pull-request-id``42`\ --pull-request-status`CLOSED`Output: `{ "pullRequest": { "approvalRules": [ { "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleId": "dd8b17fe-EXAMPLE", "approvalRuleName": "2-approvers-needed-for-this-change", "creationDate": 1571356106.936, "lastModifiedDate": 571356106.936, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "ruleContentSha256": "4711b576EXAMPLE" } ], "authorArn": "arn:aws:iam::123456789012:user/Li_Juan", "clientRequestToken": "", "creationDate": 1508530823.165, "description": "Updated the pull request to remove unused global variable.", "lastActivityDate": 1508372423.12, "pullRequestId": "47", "pullRequestStatus": "CLOSED", "pullRequestTargets": [ { "destinationCommit": "9f31c968EXAMPLE", "destinationReference": "refs/heads/main", "mergeMetadata": { "isMerged": false, }, "repositoryName": "MyDemoRepo", "sourceCommit": "99132ab0EXAMPLE", "sourceReference": "refs/heads/variables-branch" } ], "title": "Consolidation of global variables" } }`- 
                    For API details, see [UpdatePullRequestStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-status.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-pull-request-title`.

- **AWS CLI**
- 
            
                    **To change the title of a pull request**This example demonstrates how to change the title of a pull request with the ID of `47`.`aws codecommit update-pull-request-title \ --pull-request-id``47`\ --title`"Consolidation of global variables - updated review"`Output: `{ "pullRequest": { "approvalRules": [ { "approvalRuleContent": "{\"Version\": \"2018-11-08\",\"DestinationReferences\": [\"refs/heads/main\"],\"Statements\": [{\"Type\": \"Approvers\",\"NumberOfApprovalsNeeded\": 2,\"ApprovalPoolMembers\": [\"arn:aws:sts::123456789012:assumed-role/CodeCommitReview/*\"]}]}", "approvalRuleId": "dd8b17fe-EXAMPLE", "approvalRuleName": "2-approver-rule-for-main", "creationDate": 1571356106.936, "lastModifiedDate": 571356106.936, "lastModifiedUser": "arn:aws:iam::123456789012:user/Mary_Major", "originApprovalRuleTemplate": { "approvalRuleTemplateId": "dd8b26gr-EXAMPLE", "approvalRuleTemplateName": "2-approver-rule-for-main" }, "ruleContentSha256": "4711b576EXAMPLE" } ], "authorArn": "arn:aws:iam::123456789012:user/Li_Juan", "clientRequestToken": "", "creationDate": 1508530823.12, "description": "Review the latest changes and updates to the global variables. I have updated this request with some changes, including removing some unused variables.", "lastActivityDate": 1508372657.188, "pullRequestId": "47", "pullRequestStatus": "OPEN", "pullRequestTargets": [ { "destinationCommit": "9f31c968EXAMPLE", "destinationReference": "refs/heads/main", "mergeMetadata": { "isMerged": false, }, "repositoryName": "MyDemoRepo", "sourceCommit": "99132ab0EXAMPLE", "sourceReference": "refs/heads/variables-branch" } ], "title": "Consolidation of global variables - updated review" } }`- 
                    For API details, see [UpdatePullRequestTitle](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-pull-request-title.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-repository-description`.

- **AWS CLI**
- 
            
                    **To change the description for a repository**This example changes the description for an AWS CodeCommit repository. This command produces output only if there are errors. Command: `aws codecommit update-repository-description --repository-name``MyDemoRepo`--repository-description`"This description was changed"`Output: `None.`- 
                    For API details, see [UpdateRepositoryDescription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-description.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-repository-name`.

- **AWS CLI**
- 
            
                    **To change the name of a repository**This example changes the name of an AWS CodeCommit repository. This command produces output only if there are errors. Changing the name of the AWS CodeCommit repository will change the SSH and HTTPS URLs that users need to connect to the repository. Users will not be able to connect to this repository until they update their connection settings. Also, because the repository's ARN will change, changing the repository name will invalidate any IAM user policies that rely on this repository's ARN. Command: `aws codecommit update-repository-name --old-name``MyDemoRepo`--new-name`MyRenamedDemoRepo`Output: `None.`- 
                    For API details, see [UpdateRepositoryName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-name.html)in*AWS CLI Command Reference*.
 
-