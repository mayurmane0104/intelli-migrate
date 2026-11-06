# Publish and share software packages in CodeCatalyst - Amazon CodeCatalyst

**Source:** [https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages](https://docs.aws.amazon.com/codecatalyst/latest/userguide/packages)

---

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](./migration.html).

Amazon CodeCatalyst contains a fully managed package repository service that makes it easy for your development team to securely store and share software packages used for application development. These packages are stored in package repositories, which are created and organized within projects in CodeCatalyst.

A single package repository can store packages of every supported package type. CodeCatalyst supports the following package formats:

- npm 
- Maven 
- NuGet 
- Python 

Packages in a package repository can be discovered and shared between members of the project that contains the repository.

To publish packages to, and consume packages from a repository, configure a package manager to use the repository endpoint (URL). You can then use the package manager to publish packages to the repository. You can use package managers such as Maven, Gradle, npm, yarn, nuget, dotnet, pip, and twine.

You can also configure CodeCatalyst workflows to use CodeCatalyst package repositories. For more 
    information about using packages in workflows, see [Connecting package repositories to workflows](./workflows-packages.html).

You can make packages in one package repository available to another repository in the same project by 
    adding it as an upstream repository. All package versions available to the upstream repository are also available to the downstream 
    repository. For more information, see [Configuring and using upstream repositories](./packages-upstream-repositories.html).

You can make open-source packages available to your CodeCatalyst repository by creating a special type of repository called a **gateway**. 
    Upstreaming to a gateway repository allows you to consume packages from popular public repositories such as npmjs.com and pypi.org, and automatically 
    cache them in your CodeCatalyst repository. For more information, see [Connecting to public external repositories](./packages-connect-external.html).