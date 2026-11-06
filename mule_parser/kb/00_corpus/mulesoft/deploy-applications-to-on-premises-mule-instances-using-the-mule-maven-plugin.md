# Deploy Applications to On-Premises Mule Instances Using the Mule Maven Plugin | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/deploy-on-premises](https://docs.mulesoft.com/mule-runtime/latest/deploy-on-premises)

---

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <standaloneDeployment>
      <muleHome>${mule.home.test}</muleHome>
      <muleVersion>${app.runtime}</muleVersion>
    </standaloneDeployment>
  </configuration>
</plugin>
```
xml# Deploy Applications to On-Premises Mule Instances Using the Mule Maven Plugin

| Mule Maven plugin versions 3.0.0, 3.1.0, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5, 3.1.6, 3.1.7, and 3.8.3 are deprecated. | 

| Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. | 

In addition to using Anypoint Studio, Anypoint Runtime Manager, or the Anypoint Platform CLI to deploy applications on-premises, you can also deploy Mule applications by using the Mule Maven plugin. To do so, you must meet certain prerequisites, and configure the desired deployment strategy in your project’s `pom.xml` file.

If you want to deploy applications on-premises using a different method, see:

## On-premises Deployment Strategies

When you deploy applications on-premises using the Mule Maven plugin, you can select three different methods for deployment:

- 
Standalone deployment 
 By using this method you perform a manual deployment of your Mule application to your on-premises Mule instance.
- 
Runtime Manager REST API deployment 
 This method enables you to deploy an application using the Runtime Manager REST API, which links your on-premises Mule instance with your Anypoint Runtime Manager account, where you can do further management and monitoring of your deployed application.
- 
Runtime Manager Agent deployment 
 This method enables you to deploy an application using the Runtime Manager agent, which exposes a local API that you can call to manage and monitor your deployed application.

The Mule Maven plugin also supports deploying domains when using the standalone deployment strategy, or the Runtime Manager agent deployment strategy.

Additional operations enable you to deploy applications in parallel and update applications at runtime.

## Prerequisites

- 
Add the Mule Maven Plugin to your project See [Add the Mule Maven Plugin to a Mule Project](mmp-concept#add-mmp)for instructions.

## Deploy a Mule Application to a Standalone Mule Runtime Engine

Inside the `plugin` element, add a configuration for your standalone deployment, replacing the placeholder values with your local Mule runtime engine information:

From the command line in your project’s folder, package the application and execute the deploy goal:

`mvn clean deploy -DmuleDeploy`### Standalone Deployment Parameters Reference

| Parameter | Description | Required | 
|---|---|---|
| 
 | Top-Level Element. | Yes | 
| 
 | Specifies the application name to use during deployment. | Yes | 
| 
 | The Mule version running in your local machine instance. The Mule Maven Plugin does not download a Mule runtime engine if these values don’t match. | Yes | 
| 
 | The location of the Mule instance in your local machine. | Yes | 
| 
 | The allowed elapsed time, in milliseconds, between the start of the deployment process and the confirmation that the artifact has been deployed The default value is  | No | 
| 
 | When set to  | No | 

## Deploy a Mule Application Using the Runtime Manager REST API

Mule Maven plugin enables you to deploy a Mule Application to a local Mule instance using the Runtime Manager REST API.

### Prerequisites

- 
You need a server, server group or cluster created in Runtime Manager. - 
To create a server, see [Add Servers](../../runtime-manager/servers-create).
- 
To create a server group, see [Create Server Groups](../../runtime-manager/server-group-create).
- 
To create a cluster, see [Create Clusters](../../runtime-manager/cluster-create).
 
- 

### Deploying Using the Runtime Manager REST API

Inside the `plugin` element, add a configuration for your Runtime Manager deployment, replacing the placeholder values with your Runtime Manager information:

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <armDeployment>
      <muleVersion>${app.runtime}</muleVersion>
      <uri>https://anypoint.mulesoft.com</uri>
      <target>${target}</target>
      <targetType>${target.type}</targetType>
      <username>${username}</username>
      <password>${password}</password>
      <environment>${environment}</environment>
      <properties>
        <key>value</key>
      </properties>
    </armDeployment>
  </configuration>
</plugin>
```
xmlFrom the command line in your project’s folder, package the application and execute the deploy goal:

`mvn clean deploy -DmuleDeploy`### Authentication Methods

When you deploy applications using Mule Maven plugin, you can use different methods to provide your credentials to authenticate against the deployment platform. Depending on the authentication method you use, the parameters to set in the deployment configuration differ:

| Authentication Method | Description | Configuration Parameters | 
|---|---|---|
| Username and password | Authenticate with the username and password for the server where your Mule instances are installed. | 
 | 
| Server | Use credentials stored in a Maven server, configured inside the Maven  | 
 | 
| Authorization Token | Use an authorization token to access the platform. | 
 | 
| Connected Apps | Use a Connected App to perform the authentication programmatically by communicating with Anypoint Platform. | 
 | 

For a detailed description of the configuration parameters, see the [Runtime Manager REST API Deployment Parameters Reference](#arm-deploy-reference).

### Runtime Manager REST API Deployment Parameters Reference

| Parameter | Description | Required | 
|---|---|---|
| 
 | Top-Level Element. | Yes | 
| 
 | Specifies the application name to use during deployment. | Yes | 
| 
 | The Mule version required for your application to run in your deployment target. The Mule Maven Plugin does not download a Mule runtime engine if these values don’t match. | Yes | 
| 
 | The Anypoint Platform URI. If you are using Anypoint Platform PCE, specify this parameter with your Anypoint Platform installation URI. | No | 
| 
 | The server name for the server where your Mule instances are installed. | Yes | 
| 
 | The type of target to which you are deploying. Valid values are: 
 | Yes | 
| 
 | Your username for the server where your Mule instances are installed. | Only when using Anypoint Platform credentials to login. | 
| 
 | Your password for the server where your Mule instances are installed. | Only when using Anypoint Platform credentials to login. | 
| 
 | The environment name for the server where your Mule instances are installed. This value must match any environment configured in your Runtime Manager account.  | Yes | 
| 
 | The Business group path of the deployment This value is omitted if  | No | 
| 
 | The Business group ID of the deployment | No | 
| 
 | The allowed elapsed time, in milliseconds, between the start of the deployment process and the confirmation that the artifact has been deployed The default value is  | No | 
| 
 | Maven server with Anypoint Platform credentials | No | 
| 
 | Top-Level element For example:  | No | 
| 
 | Top-level element | No | 
| 
 | When set to  | No | 
| 
 | When set to  | No | 
| 
 | Specifies the authorization token to access the platform. You can use this authentication method instead of setting username and password. | Only when using an Authorization token to login. | 
| 
 | Specifies the Connected App  | Only when using Connected Apps credentials to login. | 
| 
 | Specifies the Connected App secret key. | Only when using Connected Apps credentials to login. | 
| 
 | Specifies the only supported connection type:  | Only when using Connected Apps credentials to login. | 

### Encrypt Credentials

To use encrypted credentials when deploying, you need to set up your Maven master encrypted password and your `settings-security.xml` file.

- 
Create a master password for your Maven configuration. mvn --encrypt-master-password <yourMasterPassword> Maven returns your master password encrypted: `{l9vZ2uM5SdgHy+H12z4pX7LEOZn3Kbnqmt3kIquLjnQ=}`
- 
Create a `settings-security.xml`file in your ~/.m2 repository and add your encrypted master password:`<settingsSecurity> <master>{l9vZ2uM5SdgHy+H12z4pX7LEOZn3Kbnqmt3kIquLjnQ=}</master> </settingsSecurity>`xml
- 
Encrypt your Anypoint platform password: mvn --encrypt-password <yourAnypointPlatformPassword> Maven returns your Anypoint platform password encrypted: `{HTWFGH5BG9QmvJ1B=}`
- 
Add your encrypted Anypoint Platform password to your `settings.xml`file in the <server> section:`<settings> ... <servers> ... <server> <id>my.anypoint.credentials</id> <username>my.anypoint.username</username> <password>{HTWFGH5BG9QmvJ1B=}</password> </server> ... </servers> ... </settings>`xml
- 
In your configuration deployment, reference the credentials injecting the server ID configured in your `settings.xml`file:`<plugin> ... <configuration> ... <armDeployment> ... <server>my.anypoint.credentials</server> ... </armDeployment> ... </configuration> ... <plugin>`xmlMake sure that the username and password are not set in the deployment configuration, or they will overwrite the defined server ID. 

### Troubleshoot TLS Errors in Anypoint Private Cloud Edition

When trying to connect to an instance of Runtime Manager that’s on an [Anypoint Platform Private Cloud Edition](../../private-cloud/latest/) installation, the plugin validates certificates for that server. If you haven’t installed the server certificates in your truststore, an SSL error occurs. To avoid this problem, you can run the plugin in an insecure mode, which skips the security validations. You can use the **armInsecure** tag or the **arm.insecure** system property.

| Enabling an insecure connection is a dangerous practice. Don’t use this unless you know what you are doing and your On-Premises installation is isolated in a local network. | 

See the configuration example below:

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <armDeployment>
        <target>${target}</target>
        <targetType>${target.type}</targetType>
        <username>${username}</username>
        <password>${password}</password>
        <environment>${environment}</environment>
        <armInsecure>true</armInsecure>
    </armDeployment>
  </configuration>
</plugin>
```
xml## Deploy a Mule Application Using the Runtime Manager Agent

Inside the `plugin` element, add a configuration for your Runtime Manager agent deployment, replacing the URI value with your remote server information:

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <agentDeployment>
      <uri>http://localhost:9999/</uri>
    </agentDeployment>
  </configuration>
</plugin>
```
xmlFrom the command line in your project’s folder, package the application and execute the deploy goal:

`mvn clean deploy -DmuleDeploy`### Runtime Manager Agent Deployment Parameters Reference

| Parameter | Description | Required | 
|---|---|---|
| 
 | Top-Level Element. | Yes | 
| 
 | Specifies the application name to use during deployment. | Yes | 
| 
 | The Mule version required for your application to run in your deployment target. The Mule Maven Plugin does not download a Mule runtime engine if these values don’t match. | Yes | 
| 
 | The server URI where your Mule instances are installed. | Yes | 
| 
 | The allowed elapsed time, in milliseconds, between the start of the deployment process and the confirmation that the artifact has been deployed The default value is  | No | 
| 
 | When set to  | No | 

## Deploy a Domain

The Mule Maven plugin supports deploying domains only when using the standalone deployment strategy, or the Runtime Manager agent deployment strategy.

To deploy a domain, use the same configuration and deployment steps you use when deploying an application. For example, to deploy a domain to a standalone instance:

- 
Inside the `plugin`element, add a configuration for your standalone deployment, replacing the placeholder values with your local Mule runtime engine information:`<plugin> <groupId>org.mule.tools.maven</groupId> <artifactId>mule-maven-plugin</artifactId> <version>3.7.1</version> <extensions>true</extensions> <configuration> <standaloneDeployment> <muleHome>${mule.home.test}</muleHome> <muleVersion>${app.runtime}</muleVersion> </standaloneDeployment> </configuration> </plugin>`xml
- 
From the command line in your project’s folder, package the domain and execute the deploy goal: `mvn clean deploy -DmuleDeploy`

## Deploy Applications in Parallel

You can deploy applications in parallel to on-premises Mule instances. Deploying applications in parallel reduces the startup time when you deploy a large number of apps. To prevent deployment failure, ensure that applications are not dependent on each other because a particular start order cannot be guaranteed.

Parallelism is fixed at 20.

To enable parallel deployment:

- 
Package or export your Mule applications to the `/apps`directory of your Mule runtime engine instance.
- 
Start Mule using the `-M-Dmule.deployment.parallel`option:`mule -M-Dmule.deployment.parallel`

After performing these steps, Mule deploys in parallel all applications in the `/apps` directory.

## Undeploy Applications

You can undeploy Mule applications by deleting an app’s anchor file only instead of deleting the application folder directly.

Deleting only the app’s anchor file:

- 
Prevents any interference from the hot-deployment layer and leaves no room for concurrent conflicting actions. 
- 
Avoids potential application JAR file locking issues on some operation systems and allows for clean shutdown and undeployment. 

For example, if the `stockTrader` app is running (app folder is there as well as the `$MULE_HOME/apps/stockTrader-anchor.txt` file), just delete the anchor file to have the app removed from the Mule instance at runtime. Application folder is removed after the app terminates.

| After undeploying a Mule application, there is a timeout of 15 seconds until `LoggerContext`stops. Log files for an application only release after this timeout expires. This information is important in Windows, where you can’t remove files that are in use by other processes.
After undeploying a Mule application, there is a timeout of 15 seconds until LoggerContext stops. Log files for an application only release after this timeout expires. This information is important in Windows, where you can’t remove files that are in use by other processes. | 

## Update Applications at Runtime

Updating a Mule application at runtime can be a complex change involving class modifications, endpoint modifications (for example, changing ports), and reconfiguring flows. An application update first performs a graceful app shutdown and then reconfigures itself in the background within seconds. This process is transparent for the users.

There are two ways you can update an application:

- 
By adding the modifications over an existing unpacked app folder and touching the main configuration file ( `mule-config.xml`located in the app’s root directory by default).
 For this option to be valid, start the runtime with the system property`-M-Dmule.deployment.forceParseConfigXmls=true`.
- 
By adding a new `jar`with an updated version of the app into the`$MULE_HOME/apps`directory. Mule detects the`jar`as an updated version of an existing application and ensures the update by a clean redeployment of the app.
 Note that Mule discards any modifications to the old application folder. The new app folder is a clean unpacked application from a`jar`.

Either method integrates well with existing build tools.