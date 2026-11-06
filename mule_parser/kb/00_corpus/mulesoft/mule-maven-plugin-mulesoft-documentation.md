# Mule Maven Plugin | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/mmp-concept](https://docs.mulesoft.com/mule-runtime/latest/mmp-concept)

---

`onlyMuleSources`

# Mule Maven Plugin

| Mule Maven plugin versions 3.0.0, 3.1.0, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5, 3.1.6, 3.1.7, and 3.8.3 are deprecated. | 

The Mule Maven plugin enables you to integrate the packaging and deployment of your Mule applications with your Maven lifecycle.

See [Package a Mule Application](package-a-mule-application) for packaging instructions.

The Mule Maven plugin is compatible with Mule runtime engine (Enterprise Edition) and with Mule Kernel (Community Edition).

Using the Mule Maven plugin, you can automate your Mule application deployment to CloudHub, to CloudHub 2.0, to Anypoint Runtime Fabric, or on-premises, using any of the following deployment strategies:

- 
CloudHub deployment 
 Deploys your Mule application to CloudHub.
 See[Deploy Applications to CloudHub](deploy-to-cloudhub)for instructions.
- 
CloudHub 2.0 deployment 
 Deploys your Mule application to CloudHub 2.0.
 See[Deploy Applications to CloudHub 2.0](deploy-to-cloudhub-2)for instructions.
- 
Runtime Fabric deployment 
 Deploys your Mule application to Anypoint Runtime Fabric.
 See[Deploy Applications to Anypoint Runtime Fabric](deploy-to-rtf)for instructions.
- 
Runtime Manager REST API deployment 
 Deploys your Mule application to your server, or server clusters using the Runtime Manager REST API.
 See[Deploy a Mule Application Using the Runtime Manager REST API](deploy-on-premises#mmp-deploy-arm)for instructions.
- 
Runtime Manager agent deployment 
 Deploy your Mule application using the Runtime Manager agent.
 This deployment strategy works only if all your Mule instances reside in one address space.
 See[Deploy a Mule Application Using the Runtime Manager Agent](deploy-on-premises#mmp-deploy-agent)for instructions.
- 
Standalone runtime deployment 
 Deploy your Mule application to a Mule instance running on your machine.
 See[Deploy a Mule Application to a Standalone Mule Runtime Engine](deploy-on-premises#mmp-deploy-standalone)for instructions.

## Compatibility

- 
Mule 4.x 
- 
Anypoint Studio 7.x 

## Mule Maven Plugin Goals

The Mule Maven plugin provides the following goals:

- 
`package`
 Generates the jar file for your project.
- 
`deploy`
 Automatically uploads and starts your application in any of the application deployment targets (CloudHub, Runtime Fabric, or On-Premises).
- 
`mule:deploy`
 Deploys an artifact from the specified location.
- 
`mule:undeploy`
 Automatically removes your application from any of the application deployment targets (CloudHub, Runtime Fabric, or On-Premises).

Each goal accepts parameters that are unique to the desired plugin behavior.
To provide a parameter from the command line, prepend `-D` to the parameter name.

### Package Goal

The `package` goal generates the application JAR file. This goal binds by default to the Maven lifecycle phase: `package`.

Optional Parameters

| Name | Type | Description | 
|---|---|---|
| boolean | Generates the application JAR file containing only the source code. This property is just for sharing purposes. | |
| 
 | boolean | Attaches the source code inside the generated JAR file. | 
| 
 | boolean | Doesn’t generate the repository with all the application dependencies inside the JAR file. This property is just for sharing purposes. | 

For example, to execute the `package` goal and set the `attachMuleSources` parameter, you run the following command:

`mvn package -DattachMuleSources`### Deploy Goal

This goal uploads and deploys the application JAR file to any of the application deployment targets. The deploy goal binds by default to the Maven lifecycle phase: `deploy`.

Optional Parameters

| Name | Type | Description | 
|---|---|---|
| 
 | String | Path to the application JAR file to be deployed. By default is set to the application  | 
| 
 | boolean | Instructs the plugin to deploy using the deployment strategy defined in the plugin configuration. If the  | 

For example, to execute the `deploy` goal and set the `muleDeploy` parameter, you run the following command:

`mvn deploy -DmuleDeploy`### mule:deploy Goal

This goal enables you to deploy an artifact without building it. To specify the artifact’s location, use the `mule.artifact` parameter.

For example:

`mvn mule:deploy -Dmule.artifact=myProject/myArtifact.jar`This property is valid for CloudHub, standalone, and on-premises deployments.

### mule:undeploy Goal

This goal removes an application from any of the application deployment targets. It uses the information from the plugin configuration to remove the application from the defined deployment target.

To execute the `undeploy` goal, run the following command:

`mvn mule:undeploy`The undeploy goal also deletes the app in Mule Maven plugin 3.3.0 and later versions.

## Add the Mule Maven Plugin to a Mule Project

Before you can perform any operations, you must add the Mule Maven plugin to your project.

To add the Mule Maven plugin, you need to add its maven dependency to the project:

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
</plugin>
```
xmlFrom this repository:

```
<pluginRepositories>
  <pluginRepository>
    <id>mule-public</id>
    <url>https://repository.mulesoft.org/nexus/content/repositories/releases</url>
  </pluginRepository>
</pluginRepositories>
```
xmlThis enables the Mule Maven plugin in your project.

| If `<extensions>true</extensions>`is not present, the plugin does not work. | 

## Skip Plugin Execution

You can skip the plugin execution by setting the `skip` parameter to true inside your deployment configuration:

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <standaloneDeployment>
      <muleHome>${mule.home.test}</muleHome>
      <skip>true</skip>
    </standaloneDeployment>
  </configuration>
</plugin>
```
xml## Skip Deployment Verification

You can skip the status verification of your deployed app by setting the `skipDeploymentVerification` parameter to true inside of any of the platform deployments (Cloudhub, Runtime Manager, and Runtime Fabric):

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <runtimeFabricDeployment>
      ...
      <skipDeploymentVerification>true</skipDeploymentVerification>
      ...
    </runtimeFabricDeployment>
  </configuration>
</plugin>
```
xmlIf the `skipDeploymentVerification` parameter is not present, the default value is false.

This feature is available in plugin version 3.2.5 and later.

## Configure Shared Libraries

Shared libraries enable you to configure a dependency in your application and make this dependency accessible to all the connectors in your application.

See [Shared Libraries](about-classloading-isolation#shared-libraries) for an in-depth explanation of this feature.

To configure a dependency as a shared library, add the following elements inside your Mule Maven plugin configuration in your project’s `pom.xml` file:

```
<sharedLibraries>
  <sharedLibrary>
    <groupId>${dependencyGroupID}</groupId>
    <artifactId>${dependencyArtifactID}</artifactId>
  </sharedLibrary>
</sharedLibraries>
```
xmlThe following example configures Anypoint Connector for Database (Database Connector) in a project, and also configures the MySQL driver as a shared library:

```
<build>
  <plugins>
    <!-- Mule Maven Plugin configuration -->
    <plugin>
    	<groupId>org.mule.tools.maven</groupId>
    	<artifactId>mule-maven-plugin</artifactId>
    	<version>${mule.maven.plugin.version}</version>
    	<extensions>true</extensions>
    	<configuration>
    	<sharedLibraries>
        <!-- MySQL driver dependency configured as a shared library -->
        <sharedLibrary>
          <groupId>mysql</groupId>
          <artifactId>mysql-connector-java</artifactId>
        </sharedLibrary>
      </sharedLibraries>
      </configuration>
    </plugin>
  </plugins>
</build>
<dependencies>
  <!--Database Connector dependency -->
  <dependency>
    <groupId>org.mule.connectors</groupId>
    <artifactId>mule-db-connector</artifactId>
    <version>1.5.0</version>
    <classifier>mule-plugin</classifier>
  </dependency>
  <!-- MySQL driver dependency -->
  <dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.33</version>
  </dependency>
</dependencies>
```
xml## Configure Additional Plugin Dependencies

Configuring additional plugin dependencies for a connector in your application makes those dependencies available for only that connector. Doing this  enables you to configure different dependencies, or even multiple versions of the same dependency, for different connectors.

See [Additional Plugin Dependencies](about-classloading-isolation#additional-plugin-dependencies) for an in-depth explanation of this feature.

To configure additional plugin dependencies, add the following elements inside your Mule Maven plugin configuration in your project’s `pom.xml` file:

```
<additionalPluginDependencies>
    <plugin>
        <groupId>${connectorGroupID}</groupId>
        <artifactId>${connectorArtifactID}</artifactId>
        <additionalDependencies>
            <dependency>
                <groupId>${dependencyGroupID}</groupId>
                <artifactId>${dependencyArtifactID}</artifactId>
                <version>${dependencyVersion}</version>
            </dependency>
        </additionalDependencies>
    </plugin>
</additionalPluginDependencies>
```
xmlThe following example configures the Derby driver as a dependency of Database Connector:

```
<plugin>
    <!-- Mule Maven Plugin configuration -->
    <groupId>org.mule.tools.maven</groupId>
    <artifactId>mule-maven-plugin</artifactId>
    <version>${mule.maven.plugin.version}</version>
    <configuration>
        <!-- Plugin dependencies configuration-->
        <additionalPluginDependencies>
            <!-- The connector for which the dependency is defined -->
            <plugin>
                <groupId>org.mule.connectors</groupId>
                <artifactId>mule-db-connector</artifactId>
                <!-- Dependencies definition for the connector -->
                <additionalDependencies>
                    <dependency>
                        <groupId>org.apache.derby</groupId>
                        <artifactId>derby</artifactId>
                        <version>10.11.1.1</version>
                    </dependency>
                </additionalDependencies>
            </plugin>
        </additionalPluginDependencies>
    </configuration>
</plugin>
```
xml## Mule Maven Plugin Reference

The following links contain the parameter reference of each deployment strategy: