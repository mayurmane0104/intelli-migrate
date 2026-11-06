# Download, Install, Configure, and Upgrade Mule | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/runtime-installation-task](https://docs.mulesoft.com/mule-runtime/latest/runtime-installation-task)

---

```
$ java -version
openjdk version "17.0.13" 2024-10-15
OpenJDK Runtime Environment Temurin-17.0.13+11 (build 17.0.13+11)
OpenJDK 64-Bit Server VM Temurin-17.0.13+11 (build 17.0.13+11, mixed mode, sharing)
```
# Download, Install, Configure, and Upgrade Mule

Before downloading and installing Mule, verify that you have a [supported JDK](../../general/java-support#mule-runtime-java-support) installed.
This example uses [Eclipse Temurin 17](https://adoptium.net/temurin/releases/?version=17), which is recommended for Mule 4.9.

AdoptOpenJDK moved to the Eclipse Foundation and changed its name to the Eclipse Adoptium project. The name of the JDK changed to Temurin.

## Download Mule

- 
Download the Mule 4 binary file from the following link and unzip it: [https://www.mulesoft.com/lp/dl/anypoint-mule-studio](https://www.mulesoft.com/lp/dl/anypoint-mule-studio)
- 
Set an environment variable called `MULE_HOME`for the`mule`directory inside your extracted folder.Example for version 4.9.0 in the `Downloads`directory:- 
In Windows environments: `$ env:MULE_HOME="C:\Downloads\mule-enterprise-standalone-4.9.0"`
- 
In Linux or Unix environments: `$ export MULE_HOME=~/Downloads/mule-enterprise-standalone-4.9.0`
 
- 

The procedure for making the `MULE_HOME` setting permanent depends on your operating system.

### Test Your Mule Instance

After downloading Mule, test to confirm that it runs in your system without errors by executing the following commands:

- 
In Windows environments: `%MULE_HOME%\bin\mule.bat`powershell
- 
In Linux or Unix environments: `$ $MULE_HOME/bin/mule`

These commands run Mule in foreground mode, and the startup script displays information on the terminal’s standard output. You can’t issue further commands on the terminal as long as Mule is running.

To stop Mule, press `CTRL-C` in the terminal in which the script is running.

## Install Mule

You can install Mule as a Windows service or as a Linux or Unix daemon by executing the corresponding command:

- 
In Windows environments: `$ $MULE_HOME\bin\mule.bat install`powershell
- 
In Linux or Unix environments: `$ $MULE_HOME/bin/mule install`

## Configure Properties in the wrapper.conf File

After installing Mule as a service or as a daemon, you can modify the properties defined in the `wrapper.conf` file.

For details about what you can do with the configuration file, see [Configuration Property Overview](https://wrapper.tanukisoftware.com/doc/english/properties.html).

After modifying the `wrapper.conf` file, restart your Mule instance to enable the changes.

| When you add new properties, ensure that no other properties already use the same sequence number (don’t worry about the ones in  Don’t modify the  | 

## Configure CPU Affinity

Many operating systems provide a mechanism to bind a process to one or more central processing units (CPUs) so that the process executes only on the assigned CPUs. You can configure CPU affinity in your environment to run Mule in a nonvirtualized multicore server and comply with the number of cores included in your subscription.

### Considerations When Using CPU Affinity

- 
CPUs have groups of cores that share a cache to improve thread communication and migration performance. To avoid such performance issues, check with your infrastructure team to identify which cores share this cache before setting up this feature. 
- 
Check with your infrastructure team to ensure that no existing resource allocation policy that can interfere with your CPU affinity configuration. 
- 
Ensure that the number of cores you plan to configure through CPU affinity does not exceed the number of cores included in your MuleSoft subscription plan. 

## Remove the Mule Service or Daemon

You can remove Mule as a Windows service or as a Unix daemon by executing the corresponding command:

- 
In Windows environments: `$ $MULE_HOME\bin\mule.bat remove`powershell
- 
In Linux or Unix environments: `$ $MULE_HOME/bin/mule remove MULE_HOME is set to /Applications/mule-enterprise-standalone-4.9.0 MULE_BASE is set to /Applications/mule-enterprise-standalone-4.9.0 Detected Mac OSX: Mule Enterprise Edition is not running. Removing Mule Enterprise Edition daemon...`

## Install Anypoint Monitoring

You can [install Anypoint Monitoring](../../monitoring/am-installing) for cloud-managed supported versions of on-premises runtime instances to monitor applications running on that server.

## Update, Upgrade, or Migrate Mule Versions

MuleSoft releases new major, minor, and patch release versions of Mule, as well as monthly updates to patch releases of Mule that incorporate the latest bug fixes and security enhancements.

- 
To update a patch version of Mule, see [Update Patches to Mule Runtime Engine](../../release-notes/mule-runtime/patching-mule-versions)
- 
To upgrade to a later version of Mule 4, see [Upgrading Mule Runtime Engine (Versions 4.x to 4.n)](../../release-notes/mule-runtime/updating-mule-4-versions)