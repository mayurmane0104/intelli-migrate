# Write and modify code with Dev Environments in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment](https://docs.aws.amazon.com/codecatalyst/latest/userguide/devenvironment)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

Dev Environments are cloud-based development environments. In Amazon CodeCatalyst, you use Dev Environments to work on the code stored in the source repositories of your project. When creating a Dev Environments, you have several options:

- 
      Create a project-specific Dev Environment in CodeCatalyst to work on code with a supported integrated development environment (IDE). 
- 
      Create an empty Dev Environment, clone code into it from a source repository, and work on that code with a supported IDE. 
- 
      Create a Dev Environment in an IDE and clone a source repository into the Dev Environment 

A *devfile* is an open standard
    YAML file that standardizes your Dev Environments. In other words, this file codifies the required
    development tools for your Dev Environment. As a result, you can quickly set up a Dev Environment,
    switch between projects, and replicate the Dev Environment configuration across team members. 
    Dev Environments minimize the time that you spend creating and maintaining a local
    development environment, because they use a devfile that configures all of
    the tools you need to code, test, and debug for a given project. 

###### Important

Dev Environments can run scripts via devfiles that have access to your CodeCatalyst credentials. Please inspect the repository before opening untrusted resources.

The project tools and application libraries included in your Dev Environment are defined by the
    devfile in the source repository of your project. If you don't have a devfile in your source
    repository, CodeCatalyst automatically applies a default devfile. This default devfile includes tools
    for the most frequently used programming languages and frameworks. If your project was created
    using a blueprint, a devfile is automatically created by CodeCatalyst. For more information about
    the devfile, see [https://devfile.io](https://devfile.io).

After you've created a Dev Environment, only you can access it. In your Dev Environment, you can view and work on your source repository's code in a supported IDE.

By default, a Dev Environment is configured to have a 2-core processor, 4 GB of RAM, and 16 GB of persistent storage. If you have Space administrator permissions, you can change the billing tier for your space to use different Dev Environment configuration options and manage compute and storage limits.