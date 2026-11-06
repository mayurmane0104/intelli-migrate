# Maven Settings in Anypoint Code Builder | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/ref-acb-maven](https://docs.mulesoft.com/anypoint-code-builder/ref-acb-maven)

---

# Maven Settings in Anypoint Code Builder

Anypoint Code Builder uses Apache Maven to build and manage your Mule projects (implementation and integration projects) and API specifications in design projects. All Maven configurations, such as custom repositories, proxies, and server credentials, are managed through a central `settings.xml` file.

For information about the Maven file `settings.xml`, see the [Maven documentation](https://maven.apache.org/settings.html).

## Maven Settings File in Anypoint Code Builder

Use the Apache Maven file `settings.xml` to configure the Maven settings, such as repositories, proxy settings, and credentials. For detailed information, see [Settings Reference](https://maven.apache.org/settings.html) in the Apache Maven documentation.

If `settings.xml` isn’t found in that path, the IDE creates an empty `settings.xml` file in the default location, `${user.home}/.m2/repository`.

## User and Internal Maven Settings in Anypoint Code Builder

Anypoint Code Builder reads its configuration from your Maven `settings.xml` file. To configure Maven, for example, to add repositories, proxies, or credentials, edit your `settings.xml` file, usually located in your `~/.m2/` directory.

If you troubleshoot a project in Anypoint Code Builder, export the file with any sensitive information, such as passwords, obfuscated. See [Export Troubleshooting Information](troubleshooting#export-troubleshooting-info) for instructions.