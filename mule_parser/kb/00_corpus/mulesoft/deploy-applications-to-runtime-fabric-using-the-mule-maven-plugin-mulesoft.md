# Deploy Applications to Runtime Fabric Using the Mule Maven Plugin | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/deploy-to-rtf](https://docs.mulesoft.com/mule-runtime/latest/deploy-to-rtf)

---

```
<plugin>
  <groupId>org.mule.tools.maven</groupId>
  <artifactId>mule-maven-plugin</artifactId>
  <version>3.7.1</version>
  <extensions>true</extensions>
  <configuration>
    <runtimeFabricDeployment>
      <uri>https://anypoint.mulesoft.com</uri>
      <muleVersion>4.3.0</muleVersion>
      <username>user</username>
      <password>pass</password>
      <applicationName>newapp</applicationName>
      <target>rtf</target>
      <environment>Sandbox</environment>
      <provider>MC</provider>
      <replicas>1</replicas>
      <properties>
        <key>value</key>
      </properties>
      <deploymentSettings>
        <enforceDeployingReplicasAcrossNodes>false</enforceDeployingReplicasAcrossNodes>
        <updateStrategy>recreate</updateStrategy>
        <clustered>false</clustered>
        <forwardSslSession>false</forwardSslSession>
        <lastMileSecurity>false</lastMileSecurity>
        <resources>
          <cpu>
            <reserved>20m</reserved>
            <limit>1500m</limit>
          </cpu>
          <memory>
            <reserved>700Mi</reserved>
          </memory>
        </resources>
        <http>
          <inbound>
            <publicUrl>url</publicUrl>
          </inbound>
        </http>
      </deploymentSettings>
    </runtimeFabricDeployment>
  </configuration>
</plugin>
```
xml# Deploy Applications to Runtime Fabric Using the Mule Maven Plugin

| Mule Maven plugin versions 3.0.0, 3.1.0, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5, 3.1.6, 3.1.7, and 3.8.3 are deprecated. | 

| Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain terms to avoid any effect on customer implementations. | 

In addition to using Anypoint Runtime Manager, to deploy applications to Anypoint Runtime Fabric, you can also deploy applications by using the Mule Maven plugin. To do so, you must meet certain prerequisites, and configure your Runtime Fabric deployment strategy in your project’s `pom.xml` file.

If you want to deploy applications to Runtime Fabric using a different method, see:

## Prerequisites

- 
Ensure that the Mule Maven Plugin is added to your project See [Add the Mule Maven Plugin to a Mule Project](mmp-concept#add-mmp)for instructions.
- 
You understand and have available the number of resources required to deploy to Runtime Fabric 
 See[Allocating Resources for Application Deployment on Runtime Fabric](../../runtime-fabric/latest/deploy-resource-allocation-self-managed)for more information.
- 
The application is already published in Exchange 
 See[Publish and Deploy Exchange Assets Using Maven](../../exchange/to-publish-assets-maven).

## Configure the Runtime Fabric Deployment Strategy

Inside the `plugin` element, add a configuration for your Runtime Fabric deployment, replacing the following placeholder values with your Runtime Fabric information:

## Deploy to Runtime Fabric

From the command line in your project’s folder, package the application and execute the deploy goal:

`mvn clean deploy -DmuleDeploy`bash

### Exchange Snapshot Assets

You can also deploy Exchange snapshot assets into Runtime Fabric.

By using `SNAPSHOT` version assets in Anypoint Exchange during the development and testing phase, you can avoid incrementing your application’s version number for small changes. After your `SNAPSHOT` version application has been overwritten in Anypoint Exchange, you can redeploy your `SNAPSHOT` version application to Runtime Fabric via the Mule Maven plugin to deploy the latest changes.

To learn more about publishing snapshot assets to Anypoint Exchange, see [Asset Lifecycle State](../../exchange/to-publish-assets-maven#asset-lifecycle-state).

| Each time you update your application’s snapshot, redeploy the application to refresh it with the latest snapshot binaries. Because snapshot assets can change after deployment, avoid deploying them into your production environment. | 

## Redeploy to Runtime Fabric

To redeploy the application, run the same command as you did to deploy.

Runtime Fabric rewrites the application you had deployed.

## Authentication Methods

When you deploy applications using Mule Maven plugin, you can use different methods to provide your credentials to authenticate against the deployment platform. Depending on the authentication method you use, the parameters to set in the deployment configuration differ:

| Authentication Method | Description | Configuration Parameters | 
|---|---|---|
| Username and password | Use a Runtime Fabric username and password to authenticate. | 
 | 
| Server | Use credentials stored in a Maven server, configured inside the Maven  | 
 | 
| Authorization Token | Use an authorization token to access the platform. | 
 | 
| Connected Apps | Use a Connected App to perform the authentication programmatically by communicating with Anypoint Platform. | 
 | 

For a detailed description of the configuration parameters, see the [Runtime Fabric Deployment Parameters Reference](#rtf-deploy-reference).

## Runtime Fabric Deployment Parameters Reference

| Parameter | Description | Required | 
|---|---|---|
| 
 | Top-Level Element | Yes | 
| 
 | Your Anypoint Platform URI. | No | 
| 
 | The Mule runtime engine version to run in your Runtime Fabric instance.  | No | 
| 
 | Set the name of the release channel used to select the Mule image. Supported values are  | No | 
| 
 | Set the Java version used in the deploy. Supported values are  | No | 
| 
 | Your Anypoint Platform username | Only when using Anypoint Platform credentials to login. | 
| 
 | Your Anypoint Platform password | Only when using Anypoint Platform credentials to login. | 
| 
 | The application name displayed in Runtime Manager after the app deploys. | Yes | 
| 
 | The Runtime Fabric target name where to deploy the app. | Yes | 
| 
 | Provider MC (MuleSoft Control Plane) indicates that the deployment is managed through Anypoint Runtime Manager. Set to  | Yes | 
| 
 | Target Anypoint Platform environment.  | Yes | 
| 
 | Specifies the number of replicas, or instances, of the Mule application to deploy. The maximum number of replicas per application is 16. | Only when  | 
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
 | Top-Level element For example:  | No | 
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
 | Any of the parameters documented in  | No | 

### deploymentSettings Parameters Reference

| Parameter | Description | ||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
| 
 | Enforces the deployment of replicas across different nodes. The default value is  Configuration example:  | ||||||||||
| 
 | 
 The default value is  Configuration example:  | ||||||||||
| 
 | Enables clustering across two or more replicas of the application. The default value is  Configuration example:  | ||||||||||
| 
 | 
 Configuration example:  | ||||||||||
| 
 | 
 Configuration example using wildcard URL: Configuration example for path-based routing:  | ||||||||||
| 
 | Configures the Mule application to use a persistent object store. By default, it is set to  | ||||||||||
| 
 | 
 Configuration example:  | ||||||||||
| 
 | Not applicable for Runtime Fabric BYOK. By default, it is set to  | ||||||||||
| 
 | Disables the application-level log forwarding to Anypoint Monitoring. By default, it is set to  | ||||||||||
| 
 | Provides CPU based horizontal autoscaling configuration for deployment and redeployment operations. If autoscaling is disabled and the fields   | 

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
In your configuration deployment, reference the credentials injecting the server ID configured in your `settings.xml`file:`<plugin> ... <configuration> ... <runtimeFabricDeployment> ... <server>my.anypoint.credentials</server> ... </runtimeFabricDeployment> ... </configuration> ... <plugin>`xmlMake sure that the username and password are not set in the deployment configuration, or they will overwrite the defined server ID.