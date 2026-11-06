# Configure identity, permissions, and access in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa](https://docs.aws.amazon.com/codecatalyst/latest/userguide/ipa)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

When you sign in to Amazon CodeCatalyst for the first time, you create an AWS Builder ID. AWS Builder IDs do not exist in AWS Identity and Access Management. The user name that you choose during your first sign-in becomes your unique user ID for your identity.

In CodeCatalyst, you can sign in for the first time in one of two ways:

- 
      As part of creating a space. 
- 
      As part of accepting an invitation to a project or space in CodeCatalyst. 

The *role* or roles associated with your identity determine the actions
    you can perform in CodeCatalyst. Project roles, such as **Project administrator** and
      **Contributor**, are specific to a project, so you can have one role
    in one project and a different role in another project. If you create a space, CodeCatalyst
    automatically assigns you the **Space administrator** role. When users accept
    invitations to a project, CodeCatalyst adds those identities to the space and assigns them the
      **Limited access** role. When you invite users to projects, you choose the
    role you want them to have in the project, which determines what actions they can and cannot
    take within the project. Most users working on a project only need the
      **Contributor** role to perform their tasks. For more information, see
      [Granting access with user roles](./ipa-roles.html).

In addition to a project role, users in a project need a personal access token (PAT) to access source repositories for a project when using Git clients or integrated development environments (IDEs). Project members can use this PAT with third-party applications as an application-specific password associated with their CodeCatalyst identity. For example, when you clone a source repository to a local computer, you must provide a PAT as well as your CodeCatalyst user name.

You can configure access between CodeCatalyst and AWS resources by using a [service role](./ipa-iam-roles.html#ipa-iam-roles-service-role) to perform actions such as
    accessing AWS CloudFormation stacks and resources when you deploy actions in workflows. You must configure access 
    between CodeCatalyst and AWS resources for the workflow actions that
    are included with the project templates to run.