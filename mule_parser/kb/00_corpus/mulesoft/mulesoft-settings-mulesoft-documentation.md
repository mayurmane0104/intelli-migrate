# MuleSoft Settings | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/ref-mule-settings](https://docs.mulesoft.com/anypoint-code-builder/ref-mule-settings)

---

- 
From the Anypoint Code Builder panel, click the ![](_images/icon-settings-gear.png) (gear) icon. (gear) icon.
- 
From the activity bar, click the ![](_images/icon-settings-gear.png) (gear) icon, select (gear) icon, select**Settings**, and search for`mule`in the**Settings**tab.
- 
Provide the command `MuleSoft: Open ACB Settings`in the[Command Palette](start-use-command-palette).

# MuleSoft Settings

Anypoint Code Builder provides configurable settings that apply at the IDE level, across all your Anypoint Code Builder projects. Many of the default settings are suitable for most users. However, if you use the EU cloud, it is important to change the default US cloud setting. Some settings are configurable in the desktop IDE only.

To open the settings:

- 
If an API specification is open in the Explorer panel of the IDE, close the project to avoid a synchronization error when you switch clouds. - 
In the desktop IDE, click **File**>**Close Folder**.
 
- 
- 
Open the **Settings**tab in the desktop IDE:![Selecting the EU cloud from the desktop IDE](_images/acb-activity-bar-select-cloud.png) ## Show me how

For information about specific Mule settings, see the sections that follow.

## Mule › Application: Default Mule Runtime And Java Versions

Set a default Mule runtime engine and Java version for new Mule projects (integrations and implementations) by clicking the link **Edit defaults through command palette**.

## Mule › Application: Group ID

Set the Maven group ID value for the IDE to use when you create a Mule integration or implementation project. This setting populates the `pom.xml` file for each Mule project. The default is `com.mycompany`, for example, `<groupId>com.mycompany</groupId>` in the `pom.xml`. You can change the setting within your project, as needed.

For information about Maven group IDs, see [Introduction to the POM](https://maven.apache.org/guides/introduction/introduction-to-the-pom.html) in the Apache Maven Project documentation.

## Mule > Logging: Level

Set the verbosity of logs that appear in the Anypoint Code Builder extension, Mule DX Server, and Mule DX Server: Scaffolding logs. Verbosity options are progressive:

- 
Off: No issues 
- 
Fatal: Fatal issues only 
- 
Error: Fatal and Error issues 
- 
Warn (default): Fatal, Error, and Warn issues 
- 
Info: Fatal, Error, Warn, and Info issues 
- 
Debug: Fatal, Error, Warn, Info, and Debug issues 
- 
Trace: Fatal, Error, Warn, Info, Debug, and Trace issues 

## Mule › Lsp › Trace: Server

You can enable and control the verbosity of `LogTrace` notifications to VS Code from the `muleLanguageServerProtocol` service.

Available settings:

- 
**off**(default)
- 
**messages**
- 
**verbose**

## Mule › Runtime: Default Arguments

Set default command-line arguments to use when starting Mule Runtime engine (Mule). Mule starts when you run a Mule application in an integration or implementation project.

Common uses of this setting are to append an encryption key value (such as `-M-Dencryption.key=my-key`) that is used when running a local deployment that incorporates secure configuration properties, or for a variable (such as `-M-Denv=dev`) that Mule uses when selecting a configuration properties file by its file name. For more information about these uses, see [Defining and Securing Properties for a Mule Application](int-create-secure-configs).

## Mule › Runtime: Default Metaspace Size

Metaspace is an area for non-heap memory used to store class metadata, constant pool information, and method bytecode.

Typically, the default of **1g** (1 GB) is sufficient. However, you can change the metaspace size when installing Mule Runtime engine (Mule).

If you are using the cloud IDE, be aware of the memory available to the container before changing this value.

## Mule: Control Plane

Select a control plane for your desktop IDE:

- 
**US Cloud**(default)
- 
**EU Cloud**

In the cloud IDE, this setting is not configurable because it is set automatically based on the region where your Anypoint Platform account resides.

For more information, see [US and EU Cloud Hosts](./#us-eu-clouds).

## Mule > Telemetry

You can enable or disable telemetry services in the US cloud. By default, this setting is disabled and not used for the EU cloud. When telemetry services are enabled, the IDE sends anonymous usage data to the MuleSoft team. The data helps identify important usage trends.

## Mule: Home Directory

Set a home directory for downloaded assets, which include Mule runtime (`runtime/`) and Java (`java/`) versions for your implementations and integrations.

## Mule > Editor > Auto-completion: Enablement

Enable auto-completion suggestions in the API design editor in Anypoint Code Builder. This setting prevents the need to press Ctrl+Space to activate a list of suggestions and is disabled by default. See also [Mule > Editor > Auto-completion: Trigger Delay](#setting-auto-complete-debouncer).

## Mule > Editor > Auto-completion: Trigger Delay

Set the time in milliseconds to wait before displaying auto-completion options. This setting defaults to 1500 milliseconds. See also [Mule > Editor > Auto-completion: Enablement](#setting-auto-complete).

Avoid setting a long delay. If you activate the auto-completion menu but initiate other actions in your project before the delay period ends, the IDE automatically returns focus to the editor and opens the menu where you activated auto-completion. Such actions include opening the command palette or using the command terminal after activating the menu.

If you move your cursor to a new location or use the up or down arrow keys in the editor before the trigger delay expires, the request to open the auto-completion menu is cancelled.