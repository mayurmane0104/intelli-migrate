# Deploy Applications to CloudHub Using the Mule Maven Plugin | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/deploy-to-cloudhub](https://docs.mulesoft.com/mule-runtime/latest/deploy-to-cloudhub)

---

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <cloudHubDeployment>
      <uri>https://anypoint.mulesoft.com</uri>
      <muleVersion>${app.runtime}</muleVersion>
      <username>${username}</username>
      <password>${password}</password>
      <applicationName>${cloudhub.application.name}</applicationName>
      <environment>${environment}</environment>
      <region>${region}</region>
      <workers>${workers}</workers>
      <workerType>${workerType}</workerType>
      <properties>
        <key>value</key>
      </properties>
    </cloudHubDeployment>
  </configuration>
</plugin>
```
xml# Deploy Applications to CloudHub Using the Mule Maven Plugin

| Mule Maven plugin versions 3.0.0, 3.1.0, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5, 3.1.6, 3.1.7, and 3.8.3 are deprecated. | 

| Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. | 

In addition to using Anypoint Studio, Anypoint Runtime Manager, or the Anypoint Platform CLI to deploy applications to CloudHub, you can also deploy, redeploy, or undeploy applications by using the Mule Maven plugin. To do so, you must meet certain prerequisites, and configure your CloudHub deployment strategy in your project’s `pom.xml` file.

If you want to deploy applications to CloudHub using a different method, see:

## Prerequisites

Before you can deploy to CloudHub using the Mule Maven plugin, you must complete the following tasks:

- 
Add the Mule Maven plugin to your project See [Add the Mule Maven Plugin to a Mule Project](mmp-concept#add-mmp)for instructions.
- 
If you are using the HTTP Listener as source for your flow, you need to set its host to **0.0.0.0**and its port to**${http.port}**
- 
Declare all external classes and resources in the `exportedPackages`and`exportedResources`fields on the`mule-artifact.json`file

## Configure the CloudHub Deployment Strategy

Configure the CloudHub deployment strategy in your project’s `pom.xml` file so you can deploy, redeploy and undeploy your Mule application using the Mule Maven plugin.

Inside the `plugin` element in your project’s `pom.xml` file, configure your CloudHub deployment, replacing the placeholder values with your CloudHub information:

## Deploy to CloudHub

From the command line in your project’s folder, package the app and execute the deploy goal:

`mvn clean deploy -DmuleDeploy`## Redeploy to CloudHub

To redeploy a Mule application using Mule Maven plugin, run `mvn clean deploy -DmuleDeploy` as you did to previously deploy the app. CloudHub rewrites the app you had deployed.

## Undeploy from CloudHub

To undeploy a Mule application using Mule Maven plugin, run the following command:

`mvn mule:undeploy`The undeploy command also deletes the app in Mule Maven plugin 3.3.0 and later versions.

## Authentication Methods

When you deploy applications using Mule Maven plugin, you can use different methods to provide your credentials to authenticate against the deployment platform. Depending on the authentication method you use, the parameters to set in the deployment configuration differ:

| Authentication Method | Description | Configuration Parameters | 
|---|---|---|
| Username and password | Use a CloudHub username and password to authenticate. | 
 | 
| Server | Use credentials stored in a Maven server, configured inside the Maven  | 
 | 
| Authorization Token | Use an authorization token to access the platform. | 
 | 
| Connected Apps | Use a Connected App to perform the authentication programmatically by communicating with Anypoint Platform. | 
 | 

For a detailed description of the configuration parameters, see the [CloudHub Deployment Reference](#cloudhub-deploy-reference).

## CloudHub Deployment Reference

The following table shows the available parameters to configure the CloudHub deployment strategy in your project’s `pom.xml` file.

| Parameter | Description | Required | 
|---|---|---|
| 
 | Top-level element | Yes | 
| 
 | Your Anypoint Platform URI | No | 
| 
 | The Mule runtime engine version to run in your CloudHub instance.  | Yes | 
| 
 | Set the name of the release channel to use for the selected Mule version. Supported values are  | No | 
| 
 | Set the name of the Java version to use for the selected Mule version. Supported values are  | No | 
| 
 | Your CloudHub username | Only when using Anypoint Platform credentials to login. | 
| 
 | Your CloudHub password | Only when using Anypoint Platform credentials to login. | 
| 
 | The name of your application in CloudHub | Yes | 
| 
 | The absolute path of the JAR file to be deployed | No | 
| 
 | The CloudHub environment to which you want to deploy  | Yes | 
| 
 | Top-Level element For example:  | No | 
| 
 | Top-level element | No | 
| 
 | The number of workers | No | 
| 
 | Size of each worker; one of the following values: 
 | No | 
| 
 | Region of worker clouds; one of the following values: 
 | No | 
| 
 | Enables Object Store V2 | No | 
| 
 | Enables persistent queues | No | 
| 
 | The Business group path of the deployment This value is omitted if  | No | 
| 
 | The Business group ID of the deployment | No | 
| 
 | The allowed elapsed time, in milliseconds, between the start of the deployment process and the confirmation that the artifact has been deployed The default value is  | No | 
| 
 | Maven server with Anypoint Platform credentials | No | 
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
| 
 | When set to  | No | 
| 
 | When set to  | No | 

## Encrypt Credentials

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
In your configuration deployment, reference the credentials injecting the server ID configured in your `settings.xml`file:`<plugin> ... <configuration> ... <cloudHubDeployment> ... <server>my.anypoint.credentials</server> ... </cloudHubDeployment> ... </configuration> ... <plugin>`xmlMake sure that the username and password are not set in the deployment configuration, or they will overwrite the defined server ID.