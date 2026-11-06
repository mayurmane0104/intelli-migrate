# Microsoft Windows PowerShell Connector | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/windows-powershell-connector/latest](https://docs.mulesoft.com/windows-powershell-connector/latest)

---

```
<dependency>
  <groupId>com.mulesoft.connectors</groupId>
  <artifactId>mule-powershell-connector</artifactId>
  <version>x.x.x</version>
  <classifier>mule-plugin</classifier>
</dependency>
```
xml# Microsoft Windows PowerShell Connector

Microsoft Windows PowerShell Connector Version 2.1

Anypoint Connector for Microsoft Windows PowerShell (PowerShell Connector) enables you to integrate Windows administration tasks into Mule applications. PowerShell Connector enables you to connect to any machine, local or remote, to execute script files and commands on those machines. You can use SSH to execute PowerShell scripts on a remote Windows or Linux (Ubuntu) machine and have the result processed within Mule runtime engine (Mule).

| The connector does not support executing a PowerShell script on a MacOS computer. | 

For information about compatibility and fixed issues, see [Microsoft Powershell Connector Release Notes](../../release-notes/connector/microsoft-powershell-connector-release-notes-mule-4).

## Before You Begin

To use this connector, you must be familiar with:

- 
Anypoint Connectors 
- 
Mule runtime engine (Mule) 
- 
Elements in a Mule flow 
- 
Global elements 
- 
How to create a Mule app using Anypoint Studio 

To work with PowerShell Connector, you must first install an SSH server on a Windows or Linux (Ubuntu) remote machine:

- 
Windows - 
Download [OpenSSH for Win32 or Win64](https://github.com/PowerShell/Win32-OpenSSH/releases).
- 
Follow the [OpenSSH installation steps](https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH).
 
- 
- 
Linux (Ubuntu) - 
Follow the [SSH installation steps](https://ubuntu.com/server/docs/).
- 
Follow [install PowerShell on Linux](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-core-on-linux?view=powershell-6)from Microsoft.
 
- 

## Add a POM File Dependency

Verify that the connector `version` corresponds to the one you are using.

To obtain the most up-to-date `pom.xml` file information:

- 
Go to [Anypoint Exchange](https://www.mulesoft.com/exchange/).
- 
In Exchange, click **Login**and supply your Anypoint Platform username and password.
- 
In Exchange, search for `hdfs`.
- 
Click **Dependency Snippets**.

## Add the Connector in Studio

Add PowerShell Connector to a Mule project to automatically populate the XML code with the connector’s namespace and schema location, as well as add the required dependencies to the project’s `pom.xml` file.

- 
In Anypoint Studio, from the main menu, select **File > New > Mule Project**.
- 
Enter a name for your Mule project, and click **Finish**.
- 
In the **Mule Palette**view, click**(X) Search in Exchange**.
- 
In **Add Modules to Project**, type`powershell`in the search field.
- 
Click the name of the connector in **Available modules**.
- 
Click **Add**.
- 
Click **Finish**.

Adding a connector to a Mule project in Studio does not make that same connector available to other projects in your Studio workspace.

### Configure a Global Element in Studio

- 
In Studio, click the **Global Elements**tab at the bottom of the canvas.
- 
In the **Global Configuration Elements**screen, click**Create**:![Choose Global Type window with list of configurations](_images/microsoft-powershell-config-global-wizard.png)  
- 
In the **Choose Global Type**wizard, expand**Connector Configuration**, select either**Windows Configuration**or**Linux Configuration**, and click**OK**.This selection enables you to connect remotely to the type of operating system that you choose. 
- 
Configure the parameters as follows: Parameter Description **Connection**Connection type: Windows or Linux **IP Address**IP address of the machine on which you want to execute the script file or command **Username**User associated with the Windows or Linux machine **Password**Password associated with the user name In the previous image, the placeholder values refer to a configuration file `mule-artifact.properties`placed in the`src/main/resources`folder of your project.
 You can enter your credentials in the global configuration properties, or you can reference a configuration file that contains those values.To simplify maintenance and improve project reusability, of your project, use a configuration file. Keeping these values in a separate file is useful if you need to deploy to different environments, such as production, development, and QA, where your access credentials differ. See [Anypoint Connector Configuration](../../connectors/introduction/intro-connector-configuration-overview)for more information.
- 
Keep the **Advanced**tab default values.
- 
Click **Test Connection**.
- 
Click **OK**.
- 
Your configuration should look like this: ![Global element properties window with Windows configuration](_images/microsoft-powershell-config.png)  

## Next Step

After you configure the PowerShell Connector, see the
[Examples](microsoft-powershell-connector-examples)
topic for more configuration information.

## See Also

- 
[Microsoft Windows PowerShell Connector](https://www.mulesoft.com/exchange/com.mulesoft.connectors/mule-powershell-connector/)
- 
[OpenSSH for Windows](https://github.com/PowerShell/Win32-OpenSSH/releases#)
- 
[OpenSSH installation steps](https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH)
- 
[Linux install SSH](https://documentation.ubuntu.com/server/)
- 
[Salesforce Help](https://help.salesforce.com)