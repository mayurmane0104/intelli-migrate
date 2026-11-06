# Set up CodeCatalyst projects with blueprints - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/blueprints](https://docs.aws.amazon.com/codecatalyst/latest/userguide/blueprints)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

Blueprints are arbitrary code generators that represent an architectural component of a CodeCatalyst project. The component can consist of anything from a workflow in a single file to the entire project complete with sample code. Blueprints take an arbitrary set of options and use those to generate an arbitrary set of output code that gets forwarded into a project. As the blueprint gets updated with the latest best practices or new options, it can regenerate the relevant parts of your codebase in projects containing that blueprint.

You can use an Amazon CodeCatalyst blueprint to create a full project with a source repository, sample source code, CI/CD workflows, build and test 
    reports, and integrated issue tracking tools. A CodeCatalyst blueprint generates resources and source code based on configuration parameters set. When 
    using a CodeCatalyst-managed blueprint, the blueprint you choose determines which resources are added to your project, as well as the tools that CodeCatalyst 
    creates or configures, so you can track and use your project resources. As a blueprint user, you can create a project with a blueprint or add them 
    to an existing CodeCatalyst project. You can add multiple blueprints in your project, and each can be applied as an independent component. For example, 
    you can have project that was created with a web application blueprint, and then you add a security blueprint at a later time. When one of the 
    blueprints are updated, you can incorporate the changes or fixes in your project through lifecycle management. For more information, see 
    [Creating a comprehensive project with CodeCatalyst blueprints](./project-blueprints.html) and [Working with lifecycle management as a blueprint user](./lifecycle-management-user.html).

As a blueprint author, you can also create and publish custom blueprints for your CodeCatalyst space members to use your project resources. The custom 
    blueprints can be developed to meet specified needs for your space's projects. After adding a custom blueprint to your space's blueprints catalog, you 
    can manage the blueprint and continue to make updates so your space's projects stay up to date with the latest best practices. For 
    more information, see [Standardizing projects with custom blueprints in CodeCatalyst](./custom-blueprints.html). To view the blueprints SDK and sample blueprints, see the 
    [open-source GitHub repository](https://github.com/aws/codecatalyst-blueprints).

You may already have standardization and best practices in place. Instead of creating and developing a custom blueprint from scratch, you can
    choose to convert an existing source repository with source code into a custom blueprint. For more information, see 
    [Converting source repositories to custom blueprints](./convert-bp.html).