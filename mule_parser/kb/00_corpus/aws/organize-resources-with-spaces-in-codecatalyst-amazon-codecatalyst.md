# Organize resources with spaces in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces](https://docs.aws.amazon.com/codecatalyst/latest/userguide/spaces)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

You create a space that represents you, your company, department, or group, and provides a place where your development teams can manage projects. You must create a space to add projects, members, and the associated cloud resources you create in Amazon CodeCatalyst.

###### Note

Space names must be unique across CodeCatalyst. You cannot reuse names of deleted spaces.

When you create a space, you are automatically assigned the
      **Space administrator** role. You can add this role to other users in the
    space. 

With the **Space administrator** role, you can manage the space as
    follows:

- 
      Add other space administrators to the space 
- 
      Change member roles and permissions 
- 
      Edit or delete the space 
- 
      Create projects and invite members to the project 
- 
      View a list of all projects in the space 
- 
      View the activity feed for all projects in the space 

When you create a space, you are automatically added to the space with two roles:
    the **Space administrator** role, and the **Project administrator** role for the project you created as part of creating the
    space. Additional users are added as members to the space automatically when they
    accept invitations to projects. This membership in the space does not grant any permissions
    in the space. What users can do in a space is determined by the role the user has in a
    specific project.

For more information about roles, see [Granting access with user roles](./ipa-roles.html).

![Diagram showing how spaces share members and resources across projects while all projects return activity data to the space level](/images/codecatalyst/latest/userguide/images/spaces/spaces-flow.png) 

     
    
    
  The following are additional considerations for added accounts:

- 
      AWS accounts added to a CodeCatalyst space can be used in any project in that space. 
- 
      While each environment can support multiple AWS accounts, you can only use one account per environment in an action. 
- 
      Billing is configured at the space level. Multiple accounts can be configured for billing, but only one can be active in a CodeCatalyst space. An AWS account can be used as a billing account for more than one space in CodeCatalyst. The AWS account that is specified as the billing account for your CodeCatalyst space has different quotas from other account connections for a space. For more information, see [Quotas for CodeCatalyst](./quotas.html).
- 
      After you create a connection, you must add AWS IAM roles to your connection if your workflow must access those IAM roles with your CodeCatalyst environment. For more information about how environments are used, see [Deploying into AWS accounts and VPCs](./deploy-environments.html).