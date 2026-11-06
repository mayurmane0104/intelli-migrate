# Migrating Mule Projects from Anypoint Studio to Anypoint Code Builder | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/int-migrate-studio-to-acb](https://docs.mulesoft.com/anypoint-code-builder/int-migrate-studio-to-acb)

---

- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
Select **View**>**Command Palette**.

# Migrating Mule Projects from Anypoint Studio to Anypoint Code Builder

Migrate your Mule project from Anypoint Studio to Anypoint Code Builder by creating a deployable Mule application archive (JAR file). With Anypoint Code Builder, you unlock a modern development experience with advantages like faster startup times, streamlined collaboration, and the integration of MuleSoft for Agentforce: Topic Center to enable API specifications for topics and agents.

## Export Your Mule Project to a Sharable JAR File in Anypoint Studio

- 
Open the project to export in Anypoint Studio. 
- 
Select **Export**from the**File**menu.
- 
Click to expand the Mule folder. 
- 
Select **Anypoint Studio Project to Mule Deployable Archive (includes Studio metadata)**and click**Next**.
- 
Select the project to export and click **Next**.
- 
In the **JAR file**menu, click the ellipses (…) button to explore your local drive, and select the folder to which you want to export your deployable JAR file.
- 
Click **Finish**.

### Exporting Considerations

- 
Select **Attach Project Sources**to include the project metadata if you plan to:- 
Reimport the deployable file as an open Mule project into your workspace 
- 
Import the JAR file into Anypoint Code Builder 
- 
Import the JAR file back into the same Studio workspace 
 
- 

| Selecting Attach Project Sourcesflags the`-DattachMuleSources`parameter as if you would pack your Mule project with Mule Maven Plugin. | 

- 
Select **Include project module and dependencies**if you plan to deploy your exported Mule project to CloudHub.

## Import a Mule Project from a Sharable JAR File in Anypoint Code Builder

Import a shareable JAR file for a snapshot of a Mule project into the desktop IDE.

To create a shareable JAR, see [Export Mule Project](int-export-mule-project#export-mule-project).

To import a shareable JAR file in your desktop IDE:

- 
Make sure that no project is open in the IDE. 
- 
Open the Command Palette. ## Show me how
- 
Provide the following command: `MuleSoft: Import a Mule Project`command
- 
Navigate to the shareable JAR file to import, and click **Select jar file to import**.
- 
Navigate to a folder to which to unpack the JAR file, such as your home directory or any folder *outside*of a Mule project folder.
- 
Click **Select project folder**.The IDE unpacks the shareable JAR file for your project into the selected folder. 
- 
If your Mule project folder is closed, [open a workspace](int-import-mule-project#open-a-project-folder-from-the-desktop-or-cloud-ide)for the project at the project’s*root*directory.In addition to loading the graphical canvas, the IDE also loads dependencies defined in the `pom.xml`for the project. If a Mule runtime or Java configuration is missing, set the versions to use from the canvas.Libraries load to the `target/repositories`directory within the project folder.
- 
Test your project: - 
In the open project, check for errors and make sure that the canvas and code editor load correctly, which indicates that component dependencies resolved. 
- 
Check for any configurations to modify, such as ports or file paths in the configuration XML. 
- 
Run and debug your project: For guidance, see [Run Your Application in Debug Mode](int-debug-mule-apps#run-debug-mode).
 
-