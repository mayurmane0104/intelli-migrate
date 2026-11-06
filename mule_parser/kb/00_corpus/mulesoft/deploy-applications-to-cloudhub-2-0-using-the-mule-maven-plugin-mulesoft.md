# Deploy Applications to CloudHub 2.0 Using the Mule Maven Plugin | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/deploy-to-cloudhub-2](https://docs.mulesoft.com/mule-runtime/latest/deploy-to-cloudhub-2)

---

```
  <distributionManagement>
    <repository>
      <id>Repository</id>
      <name>Corporate Repository</name>
      <url>https://maven.anypoint.mulesoft.com/api/v3/organizations/ORGANIZATION_ID/maven</url>
      <layout>default</layout>
    </repository>
  </distributionManagement>
```
xml# Deploy Applications to CloudHub 2.0 Using the Mule Maven Plugin

| Mule Maven plugin versions 3.0.0, 3.1.0, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5, 3.1.6, 3.1.7, and 3.8.3 are deprecated. | 

| Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. | 

In addition to using Anypoint Runtime Manager, to deploy applications to CloudHub 2.0, you can also deploy applications by using the Mule Maven plugin. To do so, you must meet certain prerequisites, and configure your CloudHub 2.0 deployment strategy in your project’s `pom.xml` file.

## Before You Begin

- 
Ensure that the Mule Maven Plugin is added to your project See [Add the Mule Maven Plugin to a Mule Project](mmp-concept#add-mmp)for instructions.
- 
The application is already published in Exchange 
- 
The Mule Maven Facade API (v3) is added as a repository in the distribution management section of your project’s POM file. For example: See [The Mule Maven Facade API documentation](https://anypoint.mulesoft.com/exchange/portals/anypoint-platform/f1e97bc6-315a-4490-82a7-23abe036327a.anypoint-platform/exchange-maven-facade-api-http/)for more information.

## Configure the CloudHub 2.0 Deployment Strategy

Inside the `plugin` element, add a configuration for your CloudHub 2.0 deployment, replacing the following placeholder values with your CloudHub 2.0 information:

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <cloudhub2Deployment>
      <uri>https://anypoint.mulesoft.com</uri>
      <provider>MC</provider>
      <environment>${environment}</environment>
      <target>${targetName}</target>
      <muleVersion>${muleVersion}</muleVersion>
      <username>${user}</username>
      <password>${pass}</password>
      <applicationName>${appName}</applicationName>
      <replicas>1</replicas>
      <vCores>1</vCores>
      <deploymentSettings>
        <http>
          <inbound>
            <publicUrl>${publicURL}</publicUrl>
            <forwardSslSession>true</forwardSslSession>
            <lastMileSecurity>true</lastMileSecurity>
          </inbound>
        </http>
      </deploymentSettings>
    </cloudhub2Deployment>
  </configuration>
</plugin>
```
xml## Deploy to CloudHub 2.0

From the command line in your project’s folder, package the application and execute the deploy goal:

`mvn clean deploy -DmuleDeploy`bash

To deploy the artifact without rebuilding it, run:

`mvn mule:deploy`bash

### Exchange Snapshot Assets

You can also deploy Exchange snapshot assets into CloudHub 2.0.

By using `SNAPSHOT` version assets in Anypoint Exchange during the development and testing phase, you can avoid incrementing your application’s version number for small changes. After your `SNAPSHOT` version application has been overwritten in Anypoint Exchange, you can redeploy your `SNAPSHOT` version application to CloudHub 2.0 via the Mule Maven plugin to deploy the latest changes.

To learn more about publishing snapshot assets to Anypoint Exchange, see [Asset Lifecycle State](../../exchange/to-publish-assets-maven#asset-lifecycle-state).

| Each time you update your application’s snapshot, redeploy the application to refresh it with the latest snapshot binaries. Because snapshot assets can change after deployment, avoid deploying them into your production environment. | 

## Redeploy to CloudHub 2.0

To redeploy the application, run the same command as you did to deploy.

CloudHub 2.0 rewrites the application you had deployed.

## Authentication Methods

When you deploy applications using Mule Maven plugin, you can use different methods to provide your credentials to authenticate against the deployment platform. Depending on the authentication method you use, the parameters to set in the deployment configuration differ:

| Authentication Method | Description | Configuration Parameters | 
|---|---|---|
| Username and password | Use a CloudHub 2.0 username and password to authenticate. | 
 | 
| Server | Use credentials stored in a Maven server, configured inside the Maven  | 
 | 
| Authorization Token | Use an authorization token to access the platform. | 
 | 
| Connected Apps | Use a Connected App to perform the authentication programmatically by communicating with Anypoint Platform. | 
 | 

For a detailed description of the configuration parameters, see the [CloudHub 2.0 Deployment Parameters Reference](#cloudhub2-deploy-reference).

## CloudHub 2.0 Deployment Parameters Reference

| Parameter | Description | Required | |||||
|---|---|---|---|---|---|---|---|
| 
 | Top-Level Element | Yes | |||||
| 
 | Your Anypoint Platform URI. | No | |||||
| 
 | The Mule runtime engine version to run in your CloudHub 2.0 instance.  | No | |||||
| 
 | Set the name of the release channel used to select the Mule image. Supported values are  | No | |||||
| 
 | Set the Java version used in the deploy. Supported values are  | No | |||||
| 
 | Your Anypoint Platform username | Only when using Anypoint Platform credentials to login. | |||||
| 
 | Your Anypoint Platform password | Only when using Anypoint Platform credentials to login. | |||||
| 
 | The application name displayed in Runtime Manager after the app deploys. | Yes | |||||
| 
 | 
 Configuration example:  | No | |||||
| 
 | The CloudHub 2.0 target name to deploy the app to. | Yes | |||||
| 
 | Provider MC (MuleSoft Control Plane) indicates that the deployment is managed through Anypoint Runtime Manager. Set to  | Yes | |||||
| 
 | Target Anypoint Platform environment.  | Yes | |||||
| 
 | Specifies the number of replicas, or instances, of the Mule application to deploy. | Only when  | |||||
| 
 | The size of each replica specified in vCores. Accepted values:  | Yes (Only when  | |||||
| 
 | The Business group path of the deployment This value is omitted if  | No | |||||
| 
 | The Business group ID of the deployment | No | |||||
| 
 | The allowed elapsed time, in milliseconds, between the start of the deployment process and the confirmation that the artifact has been deployed The default value is  | No | |||||
| 
 | Maven server with Anypoint Platform credentials | No | |||||
| 
 | Top-Level element For example: If you redeploy the application and the  | No | |||||
| 
 | Top-level element | No | |||||
| 
 | Top-Level element For example:  | No | |||||
| 
 | When set to  | No | |||||
| 
 | When set to  | No | |||||
| 
 | Specifies the authorization token to access the platform. You can use this authentication method instead of setting username and password. | Only when using an Authorization token to login. | |||||
| 
 | Specifies the Connected App  | Only when using Connected Apps credentials to login. | |||||
| 
 | Specifies the Connected App secret key. | Only when using Connected Apps credentials to login. | |||||
| 
 | Specifies the only supported connection type:  | Only when using Connected Apps credentials to login. | |||||
| 
 | Any of the parameters documented in  | No | |||||
| 
 | 
 Configuration example:  | No | 

### deploymentSettings Parameters Reference

| Parameter | Description | |||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 
 | Enforces the deployment of replicas across different nodes. The default value is  Configuration example:  | |||||||||||
| 
 | 
 The default value is  Configuration example:  | |||||||||||
| 
 | Enables clustering across two or more replicas of the application. The default value is  Configuration example:  | |||||||||||
| 
 | 
 
 Configuration example: Example using   | |||||||||||
| 
 | When set to  | |||||||||||
| 
 | Disables the application-level log forwarding to Anypoint Monitoring. The default value is  | |||||||||||
| 
 | Exposes tracing information in OpenTelemetry standard from Mule runtime into all APM solutions. See  | |||||||||||
| 
 | Provides CPU based horizontal autoscaling configuration for deployment and redeployment operations. If autoscaling is disabled and the fields   | |||||||||||
| 
 | Configures the Mule application to use a persistent object store. By default, it’s set to  | |||||||||||
| 
 | Specifies the capacity of the replica for application deployment. This flag is available only for organizations using a usage-based pricing (UBP) package. Non-UBP organizations use the  | 

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
In your configuration deployment, reference the credentials injecting the server ID configured in your `settings.xml`file:`<plugin> ... <configuration> ... <cloudhub2Deployment> ... <server>my.anypoint.credentials</server> ... </cloudhub2Deployment> ... </configuration> ... <plugin>`xmlMake sure that the username and password aren’t set in the deployment configuration, or they will overwrite the defined server ID.