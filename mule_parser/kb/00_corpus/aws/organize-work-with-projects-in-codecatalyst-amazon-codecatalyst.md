# Organize work with projects in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects](https://docs.aws.amazon.com/codecatalyst/latest/userguide/projects)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

You use projects in Amazon CodeCatalyst to establish a collaboration space where development teams can conduct development tasks with shared continuous integration/continuous delivery (CI/CD) workflows and repositories. When you create a project, you can add, update, or remove resources. You can also monitor the progress of your team's work. You can have multiple projects within a space.

Spaces in CodeCatalyst are made up of projects. You can see every project within your space, but you can only use the projects of which you are a member. When you create a project, default roles for your project are generated, which you assign to users that you invite to your project.

- 
      Anyone assigned to the project with a project role, such as the **Contributor role**, can access project resources, such as a source repository.
- 
      Anyone with the **Space administrator**or**Project administrator**role can send invitations to join a project.
- 
      Users with the **Project administrator**role can track activity, status, and other settings across shared resources.
- 
      Users with the **Limited access**role can manage project assignments for features, code fixes, and tests as part of CI/CD workflows.Workflows are used to build, test, and release or update applications as a CI/CD pipeline. You can assemble workflows by adding actions that transfer and work on your source artifacts. When you run actions, your project cloud resources are used to provide on-demand compute ability for your workflow actions. You might configure more CI/CD workflows based on the activity and output you want to set up. For example, you might create a workflow for build and test actions only, where you can view test results and complete the workflow without a deployment while you fix bugs. Then, you might create another workflow to build and deploy your application to a staging environment. 

When you create a project, you can use a blueprint to create a project that contains sample code and creates resources, or you can start with an empty project. If you create a project using a blueprint, the blueprint you choose determines which resources are added to your project and the tools that CodeCatalyst creates or configures so you can track and use your project resources. You can manually add or remove resources after you have created a project.

Each project tracks project activity as a list of events by user, such as when a project is
    created or a resource is modified. Project activity is monitored and aggregated at the
    space level. For more information about working with activity data, see [Viewing all projects in a space](./projects-view-overview.html).

If your project uses AWS resources, you can connect your CodeCatalyst account to an AWS account where you have administrative permissions to integrate resources for your project.

You can add source repositories, issues, and other resources to your project after you
    create it. You must have the **Space administrator** role to create
    projects.