# Store and collaborate on code with source repositories in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/source](https://docs.aws.amazon.com/codecatalyst/latest/userguide/source)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

CodeCatalyst source repositories are Git repositories hosted in Amazon CodeCatalyst. You can use source repositories in CodeCatalyst to securely store, version, and manage assets for a project.

Assets in a CodeCatalyst repository can include:

- documents 
- source code 
- binary files 

CodeCatalyst also uses the source repository for a project to store configuration information for your project, such as workflow configuration files.

You can have more than one source repository in a CodeCatalyst project. For example, you might want to have separate source repositories for front-end source code, back-end source code, utilities, and documentation.

Here is one possible workflow for working with code in source repositories, pull requests, and Dev Environments in CodeCatalyst:

Mary Major creates a web application project in CodeCatalyst using a blueprint,
    which creates a source repository with sample code in it. She invites her friends
    Li Juan, Saanvi Sarkar, and Jorge Souza to work on the project with her.
    Li Juan looks at the sample code in the source repository and decides to make some
    quick changes to add a test to the code. Li creates a Dev Environment, chooses AWS Cloud9 as the IDE, and specifies a new branch,
      `test-code`. The Dev Environment
    opens. Li quickly adds the code, then commits and pushes the branch with the changes to the
    source repository in CodeCatalyst. Li then creates a pull request. As part of creating that pull
    request, Li adds Jorge Souza and Saanvi Sarkar as reviewers to ensure that the code is
    reviewed.

While reviewing the code, Jorge Souza remembers that he has his own project repository on GitHub that contains a prototype of the app they're working on. He asks Mary Major to install and configure the extension that will allow him to link the GitHub repository to the project as an additional source repository. Mary reviews the repository on GitHub and works with Jorge to configure the GitHub extension so that he can link the GitHub repository as an additional source repository for the project.

CodeCatalyst source repositories support the standard functionality of Git and work with your
    existing Git-based tools. You can create and use personal access tokens (PATs) as an
    application-specific password when cloning and working with source repositories from a Git
    client or integrated development environments (IDEs). These PATs are associated with your CodeCatalyst
    user identity. For more information, see [Grant users repository access with personal access tokens](./ipa-tokens-keys.html).

CodeCatalyst source repositories support pull requests. This is a simple way for you and other project members to review and comment on code changes before you merge them from one branch to another. You can view the changes in the CodeCatalyst console and comment on lines of code.

Pushes to branches in a CodeCatalyst source repository can automatically start a run in a
    workflow, where changes can be built, tested, and deployed. If your source repository was
    created as part of a project using a project template, one or more workflows are configured for
    you as part of the project. You can add additional workflows for repositories at any time.  The
    YAML configuration files for workflows in a project are stored in the source repositories
    configured in the source action for those workflows. For more information, see [Getting started with workflows](./workflows-getting-started.html). 

###### Topics

- [Getting started with CodeCatalyst source repositories and the Single-page application blueprint](./source-getting-started.html)
- [Storing source code in repositories for a project in CodeCatalyst](./source-repositories.html)
- [Organizing your source code work with branches in Amazon CodeCatalyst](./source-branches.html)
- [Understanding changes in source code with commits in Amazon CodeCatalyst](./source-commits.html)