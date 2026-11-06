# Version Settings for Mule, Java, and Connectors | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/int-versions](https://docs.mulesoft.com/anypoint-code-builder/int-versions)

---

- 
From the Anypoint Code Builder panel, click the ![](_images/icon-settings-gear.png) (gear) icon. (gear) icon.
- 
From the activity bar, click the ![](_images/icon-settings-gear.png) (gear) icon, select (gear) icon, select**Settings**, and search for`mule`in the**Settings**tab.
- 
Provide the command `MuleSoft: Open ACB Settings`in the[Command Palette](start-use-command-palette).

# Version Settings for Mule, Java, and Connectors

Anypoint Code Builder includes bundled Mule runtime versions that enable you to open and design projects instantly without mandatory Mule runtime downloads. The IDE uses these bundled Mule runtime versions for editing and DataSense. Exact Mule runtime versions are only required when you run or debug your applications.

- 
[Bundled runtimes](#bundled-runtimes): Learn about the Mule runtime versions included with Anypoint Code Builder.
- 
[Default versions](#default-versions): Set default Mule and Java versions to show in version dropdown menus.
- 
Project-level versions: Set versions to use in a specific project. - 
For Mule and Java versions, see [Select Mule and Java Versions for a Project](#project-version-mule-java).
- 
For connector versions, see [Select Connector Versions for a Project](#project-versions-connectors).
 
- 
- 
[Install additional runtimes](#install-additional-runtimes): Download specific Mule runtime versions when needed for run or debug operations.

## Bundled Mule Runtime Versions

Anypoint Code Builder includes two bundled Mule runtime versions that are available immediately after installation:

- 
**Mule 4.8 (Java 8 compatible)**: A minimal Mule runtime version bundle compatible with all Java 8-based Mule 4.4 and later projects. This Mule runtime version is used for design-time activities with Java 8 projects and serves as the default fallback for legacy applications. You can’t use this version to run Mule applications.
- 
**Latest Runtime (Java 17)**: The most recent supported Mule runtime version (Edge or LTS) bundled with Anypoint Code Builder at the time of release. For example, Mule 4.11. This Mule runtime version supports Java 17 and can be used for both designing and running applications. Projects configured for Mule 4.6, 4.9, and 4.10 are compatible with this bundled Mule runtime version.

The IDE automatically selects the appropriate bundled Mule runtime version based on your project’s Java version:

- 
Java 8 projects use the bundled 4.8 minimal Mule runtime version 
- 
Java 17 projects use the latest bundled Mule runtime version 

These bundled Mule runtime versions guarantee that the design service can always start and serve the canvas and design-time needs without requiring runtime downloads. Projects open instantly using these bundled Mule runtime versions. Download a specific Mule runtime version if you want to run or debug your application with an exact version that isn’t available locally.

## Select Default Mule and Java Versions

Select the default Mule and Java versions for new implementation and integration projects. The defaults appear in drop-down menus from which you select a version, for example, when creating a project.

The dropdown shows only locally available Mule runtime versions, including the bundled ones. Versions that don’t support a feature typically append a message, such as **AsyncAPI implementation unsupported** for Mule 4.4.

You can set a different version at the project level (see [Select Mule and Java Versions for a Project](#project-version-mule-java)).

To select the default Mule and Java versions from the **Settings** tab:

- 
Open the **Settings**tab for the IDE:## Show me how
- 
Find **Mule › Application: Default Mule Runtime And Java Versions**in the open tab.
- 
Click **Edit defaults through command palette**.Although it is also possible to set the versions as values to **muleRuntimeVersion**and**jdkVersion**items directly in the**Settings**tab, you must know the major, minor, and patch numbers, and in some cases, the timestamp. It is easier to set them after clicking**Edit defaults through command palette**.
- 
Select a Mule runtime version. 
- 
Select a Java version. 

## Select Mule and Java Versions for a Project

Set Mule or Java versions for a specific implementation or integration project from **Project Properties**. You can change versions at any time, but test your projects with the versions you intend to deploy.

The IDE uses bundled Mule runtime versions to open and edit projects immediately. The design service uses the latest Java-compatible Mule runtime version available locally. Anypoint Code Builder bundles the latest Mule runtime version (for example, 4.11) for Java 17 and a reduced Mule runtime version 4.8 for Java 8. This guarantees that the design service can always start and serve the canvas and design-time needs without requiring runtime downloads.

Because the bundled Mule runtime version is the latest one, you can open and edit any project regardless of its `minMuleVersion` property. The design service uses the latest Java-compatible Mule runtime version available locally for design-time activities. The `minMuleVersion` property in your project’s `mule-artifact.json` file is checked only at deployment time. The `minMuleVersion` property specifies the minimum Mule runtime version required to run or deploy the application.

Version settings are important in several scenarios:

- 
Updating a project to use more current versions 
- 
Switching to a supported version, for example, for a project that you import into Anypoint Code Builder that uses an unsupported version 
- 
Selecting versions of Mule or Java that are compatible with each other 
- 
Specifying exact Mule runtime versions for run and debug operations 

When you run or debug an application, the IDE checks if the exact Mule runtime version specified in your project is available locally. If not, you see a warning dialog that allows you to:

- 
Continue with the latest compatible local version 
- 
Open **Project Properties**to select or download the required Mule runtime version

| Changing the minimum Mule version ( `minMuleVersion`) manually can have serious implications. This requires a full test of your application so it works correctly with the target Mule runtime version. Newer Mule runtime versions turn on feature flags by default. See[Feature Flagging Mechanism](../mule-runtime/latest/feature-flagging). This can change behavior that was fixed in later versions. Your application can rely on behavior that was later corrected or on a previous issue. Prefer changing the Mule runtime version throughProject Properties, and always run full regression tests after any version change. | 

When a Mule or Java version isn’t set for a project, the IDE’s canvas and notifications provide a **Set version** button that opens the **Project Properties** tab. You can also navigate directly to the **Project Properties** tab.

To select Mule and Java versions for a project:

- 
Open your implementation or integration project 
- 
Run this command to open the **Project Properties**tab:`MuleSoft: Open Mule Project Properties`command
- 
In the Explorer, right-click a configuration XML file in your project directory, and select **Project Properties**from the menu.
- 
In **Project Properties**, select the versions to use in this project.![Mule and Java versions in Project Properties tab](_images/int-project-properties.png)  You can select from locally available Mule runtime and Java versions. The dropdown shows only the Mule runtime versions that are installed on your local disk, including bundled Mule runtime versions that are available immediately after installation. The IDE saves your version settings to the project’s `mule-artifact.json`file. Bundled Mule runtime versions enable instant project opening and design. To install additional Mule runtime versions, use the`MuleSoft: Install Runtime`command. For information about version support and automated Mule patch updates, see[Mule and Java version support](acb-release-notes#versions-mule-jdk).

## Select Connector Versions for a Project

Set connector versions for a specific implementation or integration project from **Project Properties** or when you add a component to the canvas. You can change versions at any time, but it is important to test your projects with the versions you intend to deploy.

To select connector versions for a project:

- 
Open your implementation or integration project. 
- 
Run this command to open the **Project Properties**tab:`MuleSoft: Open Mule Project Properties`command
- 
In the Explorer, right-click a configuration XML file in your project directory, and select **Project Properties**from the menu.
- 
Click **Connectors**from the**Project Properties**side bar.![Connector versions in Project Properties tab](_images/int-project-properties-connectors.png)  
- 
Select connector versions. You can update Exchange connector versions for compatibility with your project’s Mule runtime and Java versions. 

| Connector compatibility is checked against the selected Mule runtime and Java versions. Compatibility issues appear after you apply changes in  | 

## Install Additional Mule Runtime Versions

Bundled Mule runtime versions enable instant project opening and design. If you need specific Mule versions for running or debugging your applications, install these additional versions.

To install a specific Mule runtime version:

- 
Open **Command Palette**by pressing Cmd+Shift+P on Mac, or Ctrl+Shift+P on Windows.
- 
Run the command: `MuleSoft: Install Runtime`command
- 
Select the Mule runtime version to install. The IDE downloads the selected Mule runtime version to `${user.home}/AnypointCodeBuilder/runtimes`.

| The dropdown in project creation and  |