# Upgrading Java for Custom Connectors (Customers) | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/general/customer-connector-upgrade](https://docs.mulesoft.com/general/customer-connector-upgrade)

---

```
<properties>
 <muleJavaEeBomVersion>4.6.0</muleJavaEeBomVersion>
</properties>
<dependencyManagement>
 <dependencies>
   <dependency>
     <groupId>org.mule</groupId>
     <artifactId>mule-javaee-runtime-bom</artifactId>
     <version>${muleJavaEeBomVersion}</version>
     <type>pom</type>
     <scope>import</scope>
   </dependency>
 </dependencies>
</dependencyManagement>
```
java# Upgrading Java for Custom Connectors (Customers)

| This guide applies to MuleSoft customers only. If you are a MuleSoft partner, see [Upgrading Java for Custom Connectors (Partners)](partner-connector-upgrade). | 

Upgrade, test, and release your custom connectors for Java 17 to ensure compatibility within the MuleSoft ecosystem. Ensuring this compatibility is crucial because running an incompatible connector can lead to runtime failures, decreased performance, and security vulnerabilities that could impact your app’s stability.

## Before You Begin

Before upgrading and testing your custom connector for Java 17, you must be familiar with the following considerations:

- 
Target compilation level In Mule 4.9.0 and later, you can compile any Mule project for Java 17 or lower. Additional dependencies must be compiled for Java 17 or lower. If you compile for Java 17, upgrade the `mule-modules-parent`to version 1.9.0 or later. The connector’s minimum Mule version will also be 4.9.0, ensuring compatibility only with Mule 4.9.0 or later. Verify that`minMuleVersion`in`META-INF/mule-artifact/mule-artifact.json`is 4.9.0 or later. See[Specify Java Compatibility](../mule-sdk/latest/java-version-support#specify-java-compatibility).If the `mule-modules-parent`version is earlier than 1.9.0, the bytecode level for the connector and its additional dependencies must be for Java 8. You can’t use language features from Java 11 or Java 17.
- 
Unsupported directives Don’t set `--add-opens`,`--add-exports`, or`--add-modules`directives. These directives are not allowed in CloudHub, Runtime Fabric, or on-premises. These directives also require managing them for each connector across all environments, and introduce a backward compatibility burden, complicating future Java upgrades and potentially enabling security vulnerabilities. If these directives are used, they are not covered under Support.
- 
Minimum Mule version If your custom connector is running on Mule 4.5.x or earlier, you can’t run Java 17 tests that extend the `MuleArtifactFunctionalTestCase`, but you can still run Java 8 tests.To decouple the minimum Mule version when running tests, add the `-Dmunit.jvm`parameter to use Java 17 as described in[Test Your Custom Connector with MUnit](#test-your-custom-connector-with-munit).

## Upgrade Your Custom Mule SDK Connectors

Upgrade your custom Mule SDK (Java SDK and XML SDK) connectors to Java 17.

### Upgrade Third-Party Libraries

Your custom connector likely relies on third-party libraries, so it’s important to ensure they are compatible with Java 17 as well. Even if your custom connector passes tests, it is still important to deliver secure and reliable software. If a critical bug or vulnerability is found, you must upgrade to a fixed version. Using up-to-date libraries that explicitly support Java 17 makes this process easier and more reliable, as the vendor has already tested them on Java 17.

Upgrade the third-party libraries of your custom connector to be compatible with Java 17:

- 
Java EE libraries Mule 4.6.x exposes Java EE libraries differently than earlier Mule versions. You must add the BOM dependency to your custom connector and, if applicable, exclude the provided conflicting library. You can also add the libraries in the BOM dependency separately. For more information, see [Java EE Libraries](../mule-sdk/latest/java-ee-libraries).
- 
External libraries Upgrade external libraries, which are third-party libraries that are not bundled with your custom connector. Some examples include a JDBC driver, JMS broker client, or Groovy runtime. The following example shows a JDBC driver external library configuration: `@ExternalLib(name = "MySQL JDBC Driver", description = "A JDBC driver that supports connection to the MySQL Database", nameRegexpMatcher = "(.*)\\.jar", requiredClassName = "com.mysql.jdbc.Driver", coordinates = "mysql:mysql-connector-java:5.1.44") public class MySqlConnectionProvider implements ConnectionProvider<Connection> { // }`javaYou must update your external libraries to a version that is compatible with Java 17. 

### Review Your Code

After you compile your custom connector, ensure you can run your custom connector with Java 17. Reviewing your code is important because some restrictions are flagged as warnings in Java 11 but are flagged as failures and can’t be disabled in Java 17. For example, reflection is more restricted in Java 17, so you must review your code to ensure there are no illegal actions.

To help you review your code, learn more about the different changes in Java 17:

- 
JDK Migration Guide See the [Oracle JDK Migration Guide](https://docs.oracle.com/en/java/javase/17/migrate/getting-started.html#GUID-C25E2B1D-6C24-4403-8540-CFEA875B994A)for a full list of the changes made from Java 8 to Java 17. Use the guide to assess the impact to your code.
- 
Mule runtime engine See [Mule runtime](java-support#mule-runtime)to learn more about the Java 17 changes made in Mule runtime engine.- 
Reflection on Java classes To ensure compatibility with Java 17, review and update any code that uses reflection to access Java classes or set parameter values. Java 17 imposes stricter access controls, so avoid introspecting JDK internals. Have a robust test suite that runs with Java 17. Pay special attention to the `setAccessible(true)`method because these access changes are not allowed in Java 17.
- 
Serialization Update your serialization code to accommodate the restrictions of Java 17. If your code uses libraries like Gson for serializing classes, switch to using Data Transfer Objects (DTOs) where reflective access to JDK classes is involved. Ensure that serialization libraries are updated and adjust your code to minimize reliance on reflection. For more information, refer to [Configure Custom Serializers](../mule-runtime/latest/configure-custom-serializers).
- 
Library upgrades Upgrade your libraries to versions compatible with Java 17. This includes updating ByteBuddy to version 1.14.0, Jacoco to 0.8.10, and SLF4J to version 2.x. Replace CGLib with ByteBuddy and check for updates to other libraries like Groovy and JRuby. Verify that all dependencies are compatible with Java 17 to avoid runtime issues. 
- 
Changes with running the test suite Adapt your testing approach for Java 17. If you use Mockito, be aware that Mockito can’t mock JVM classes. Consider custom implementations for mocking and switch from PowerMock to newer Mockito versions. Update your tests to handle the changes in Java 17 and avoid deprecated methods. 
- 
Java Platform Module System (JPMS) JPMS was introduced in Java 9. This feature introduces stricter encapsulation, impacting how Mule modules interact with JDK classes. As Mule upgrades to Java 17 and JPMS, these changes are necessary: - 
Refactor Split Packages: Resolve issues with internal and API package splits by reorganizing and refactoring packages to conform with JPMS modularization standards. 
- 
Address `ResourceBundle`Loading: Implement solutions for issues related to resource bundle loading, such as using`ResourceBundleProvider`or alternative methods.
- 
Analyze the third-party libraries' changelogs to understand Java 17 compatibility and changes related to JPMS. 
 
- 
 
- 

### Add Missing Code

Because reflection is more restricted in Java 17, API objects now require setters. Previously with Java 8, it was enough for API objects to only have default constructors and getters for all DataWeave accessible properties. Now, API objects must also have setters so DataWeave can write those properties without using reflection.

Constructors and setters are required if your class is instantiated by DataWeave, and getters are required if your class is read. If your class is returned and not instantiated, only getters are required. However, using both getters and setters simplifies the validation and certification process.

## Upgrade Your Custom REST Connect Connectors

Upgrade your custom REST Connect connectors to Java 17.

REST Connect now supports Java 17. REST Connect connectors are generated from an API specification using REST Connect. To make the connector Java 17-compatible, republish the API specification to Exchange. See [REST Connect Connector Generator](../exchange/to-deploy-using-rest-connect).

| REST Connect now adds support for TLS. To save time, enable TLS at the same time you update your generated connector for Java 17 so that you need to generate the connector and test your apps only once. | 

## Upgrade Your Custom Configuration Properties Providers

To upgrade your custom configuration properties provider to be compatible with Java 17, switch to use [Java SDK](../mule-sdk/latest/getting-started) and use the `@JavaVersionSupport` annotation as explained in [Release Your Custom Connector](#release-your-custom-connector). You must also perform all the steps described in [Upgrading Java for Custom Connectors (Customers)](customer-connector-upgrade), just like with any custom connector. The example custom configuration properties provider mentioned in [Example: Mule SDK Module](../mule-runtime/latest/custom-configuration-properties-provider#example-mule-sdk-module) is updated to support Java 17. Refer to that example to update your custom configuration properties provider. For more details about what the changed code looks like (including migrating tests to MUnit), refer to this [changeset](https://github.com/mulesoft/mule-custom-properties-providers-module-example/commit/410ee26d8b3c44adacb077e099f32886f99eb6be).

Alternatively, if switching to using [Java SDK](../mule-sdk/latest/getting-started) involves too many changes for you, add a declaration using `ExtensionDeclarer` inside `ExtensionLoadingDelegate` in your custom configuration properties provider. For more details about what the changed code looks like, refer to this [changeset](https://github.com/mulesoft/mule-custom-properties-providers-module-example/commit/19d9d45cd52b0695f7b9c2b9019bae88f45fb228).

## Test Your Custom Connector with MUnit

Run your MUnit tests to test compatibility of your connector against Java 17. Ensure your local JDK version is 17.

- 
Open the pom.xml file of your Mule app. 
- 
Replace the `mule-maven-plugin`version with the`${mule.maven.plugin.version}`parameter.
- 
If you haven’t already, add the `munit-maven-plugin`. Replace the version with the`${munit.version}`parameter and replace`runtimeVersion`with the`${app.runtime}`parameter.`<plugin> <groupId>com.mulesoft.munit.tools</groupId> <artifactId>munit-maven-plugin</artifactId> <version>${munit.version}</version> <executions> <execution> <id>test</id> <phase>test</phase> <goals> <goal>test</goal> <goal>coverage-report</goal> </goals> </execution> </executions> <configuration> <coverage> <runCoverage>true</runCoverage> <formats> <format>html</format> </formats> </coverage> <runtimeVersion>${app.runtime}</runtimeVersion> <dynamicPorts> <dynamicPort>http.port</dynamicPort> </dynamicPorts> </configuration> </plugin>`xmlMUnit 3.1 is compatible only with Mule runtime 4.3.0 and later. If your connector is compatible with Mule runtime 4.2.0 and earlier, you must create a legacy profile that overrides the MUnit version. 
- 
If you have MUnit dependencies, such as `munit-runner`and`munit-tools`, replace the version for each dependency with the`${munit-version}`parameter.
- 
Replace the version for each connector dependency with the Java 17 compatible version of the connector. 
- 
Open a terminal window in the root of your Mule project and run the following command. This command displays the earliest versions of Mule runtime, MUnit, and the Mule Maven plugin that are compatible with Java 17. `mvn -f pom.xml -s ~/.m2/settings.xml -Dapp.runtime=4.6.0 -Dmunit.version=3.1.0 -Dmule.maven.plugin.version=4.1.0 -fae test`bash

You can now see if your connector is compatible with Java 17. For more information about running MUnit tests, refer to [MUnit](../munit/latest/).

The Mule runtime version you use determines the version of the mule-modules-parent. For example, if you use Mule runtime 4.6.0, you must use mule-modules-parent 1.6.0. Minor versions maintain a correspondence, such as Mule runtime 4.1.0 with mule-modules parent 1.1.0, Mule runtime 4.2.0 with mule-modules-parent 1.2.0, and so forth.

Java 17 is supported with Mule runtime 4.6.0 and later. However, a connector can be compatible with both Mule 4.3.0 and Java 17 simultaneously. If your connector must be compatible with Mule 4.3.0, its mule-modules-parent version cannot exceed 1.3.0. You don’t necessarily need to use mule-modules-parent 1.6.0 for your connector to be compatible with Java 17. Using mule-modules-parent 1.6.0 is specifically required to leverage other features from the Mule runtime 4.6.0 in the connector.

## Release Your Custom Connector

After you update your code and your tests are green, you are ready to release a new Java 17-compatible version of your custom connector.

- 
To communicate Java 17 compatibility, generate metadata for Java compatibility of your custom connector by adding or upgrading the custom connector `mule-sdk-api`dependency to the latest version:`<dependency> <groupId>org.mule.sdk</groupId> <artifactId>mule-sdk-api</artifactId> <version>0.10.1</version> </dependency>`xml
- 
For Java SDK, add the `@JavaVersionSupport`annotation in the same class as the`@Extension`annotation and include the`JAVA_17`value, for example:You don’t need to add any annotations for XML SDK because XML SDK modules are Java 17 compatible and inherit the property automatically. `@Extension(name = "Database") @Operations(...) @JavaVersionSupport({JAVA_8, JAVA_11, JAVA_17}) public class DatabaseConnector { .. }`java

In Mule 4.5.0 and later, custom connectors that don’t specify the `@JavaVersionSupport` annotation are assumed to be compatible with Java 8 and Java 11.

You can mark your custom connector as compatible with Java 17 only; however, you must ensure that no adoption or backward compatibility issues exist.

When you deploy a Mule app, Mule verifies that all modules in the Mule app are compatible with the Java version. If Mule finds an incompatibility, Mule throws an error and the application does not deploy.

| If you receive an error message specific to an XML SDK based connector, such as `Extension 'module-error-handler-plugin' does not support Java 17. Supported versions are: [1.8, 11]`, this means that your Mule app still contains some connectors that are not compatible with Java 17. To resolve this error, upgrade all connectors in your Mule app to be compatible with Java 17. | 

If your code is compatible with Java 17 but you don’t declare Java 17 compatibility, you can still get a successful test run.

To run a quick check on your custom connector or if all dependencies are not ready, pass the following argument to skip hard checks on the Java support declaration:

`-M-Dmule.jvm.version.extension.enforcement=LOOSE`bash

For more information, see [Java Version Support](../mule-sdk/latest/java-version-support).