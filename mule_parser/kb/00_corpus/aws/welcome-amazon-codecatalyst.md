# Welcome - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/APIReference/index.html](https://docs.aws.amazon.com/codecatalyst/latest/APIReference/index.html)

---

###### Important

Amazon CodeCatalyst is no longer open to new customers. For more information, see [How to migrate from Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/migration.html).

Welcome to the Amazon CodeCatalyst API reference. This reference provides descriptions of operations and data types for Amazon CodeCatalyst. You can use the Amazon CodeCatalyst API to work with the following objects.

Spaces, by calling the following:

- 
         [DeleteSpace](./API_DeleteSpace.html), which deletes a space.
- 
         [GetSpace](./API_GetSpace.html), which returns information about a space.
- 
         [GetSubscription](./API_GetSubscription.html), which returns information about the AWS account used for billing purposes and the billing plan for the space.
- 
         [ListSpaces](./API_ListSpaces.html), which retrieves a list of spaces.
- 
         [UpdateSpace](./API_UpdateSpace.html), which changes one or more values for a space.

Projects, by calling the following:

- 
         [CreateProject](./API_CreateProject.html)which creates a project in a specified space.
- 
         [GetProject](./API_GetProject.html), which returns information about a project.
- 
         [ListProjects](./API_ListProjects.html), which retrieves a list of projects in a space.

Users, by calling the following:

- 
         [GetUserDetails](./API_GetUserDetails.html), which returns information about a user in Amazon CodeCatalyst.

Source repositories, by calling the following:

- 
         [CreateSourceRepository](./API_CreateSourceRepository.html), which creates an empty Git-based source repository in a specified project.
- 
         [CreateSourceRepositoryBranch](./API_CreateSourceRepositoryBranch.html), which creates a branch in a specified repository where you can work on code.
- 
         [DeleteSourceRepository](./API_DeleteSourceRepository.html), which deletes a source repository.
- 
         [GetSourceRepository](./API_GetSourceRepository.html), which returns information about a source repository.
- 
         [GetSourceRepositoryCloneUrls](./API_GetSourceRepositoryCloneUrls.html), which returns information about the URLs that can be used with a Git client to clone a source repository.
- 
         [ListSourceRepositories](./API_ListSourceRepositories.html), which retrieves a list of source repositories in a project.
- 
         [ListSourceRepositoryBranches](./API_ListSourceRepositoryBranches.html), which retrieves a list of branches in a source repository.

Dev Environments and the AWS Toolkits, by calling the following:

- 
         [CreateDevEnvironment](./API_CreateDevEnvironment.html), which creates a Dev Environment, where you can quickly work on the code stored in the source repositories of your project.
- 
         [DeleteDevEnvironment](./API_DeleteDevEnvironment.html), which deletes a Dev Environment.
- 
         [GetDevEnvironment](./API_GetDevEnvironment.html), which returns information about a Dev Environment.
- 
         [ListDevEnvironments](./API_ListDevEnvironments.html), which retrieves a list of Dev Environments in a project.
- 
         [ListDevEnvironmentSessions](./API_ListDevEnvironmentSessions.html), which retrieves a list of active Dev Environment sessions in a project.
- 
         [StartDevEnvironment](./API_StartDevEnvironment.html), which starts a specified Dev Environment and puts it into an active state.
- 
         [StartDevEnvironmentSession](./API_StartDevEnvironmentSession.html), which starts a session to a specified Dev Environment.
- 
         [StopDevEnvironment](./API_StopDevEnvironment.html), which stops a specified Dev Environment and puts it into an stopped state.
- 
         [StopDevEnvironmentSession](./API_StopDevEnvironmentSession.html), which stops a session for a specified Dev Environment.
- 
         [UpdateDevEnvironment](./API_UpdateDevEnvironment.html), which changes one or more values for a Dev Environment.

Workflows, by calling the following:

- 
         [GetWorkflow](./API_GetWorkflow.html), which returns information about a workflow.
- 
         [GetWorkflowRun](./API_GetWorkflowRun.html), which returns information about a specified run of a workflow.
- 
         [ListWorkflowRuns](./API_ListWorkflowRuns.html), which retrieves a list of runs of a specified workflow.
- 
         [ListWorkflows](./API_ListWorkflows.html), which retrieves a list of workflows in a specified project.
- 
         [StartWorkflowRun](./API_StartWorkflowRun.html), which starts a run of a specified workflow.

Security, activity, and resource management in Amazon CodeCatalyst, by calling the following:

- 
         [CreateAccessToken](./API_CreateAccessToken.html), which creates a personal access token (PAT) for the current user.
- 
         [DeleteAccessToken](./API_DeleteAccessToken.html), which deletes a specified personal access token (PAT).
- 
         [ListAccessTokens](./API_ListAccessTokens.html), which lists all personal access tokens (PATs) associated with a user.
- 
         [ListEventLogs](./API_ListEventLogs.html), which retrieves a list of events that occurred during a specified time period in a space.
- 
         [VerifySession](./API_VerifySession.html), which verifies whether the calling user has a valid Amazon CodeCatalyst login and session.

###### Note

If you are using the Amazon CodeCatalyst APIs with an SDK or the AWS CLI, you must
        configure your computer to work with Amazon CodeCatalyst and single sign-on (SSO). For more information,
        see [Setting
          up to use the AWS CLI with Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/set-up-cli.html) and the SSO documentation for your
        SDK.

This document was last published on June 14, 2026.