# Setting Up the Desktop IDE | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/start-acb-desktop](https://docs.mulesoft.com/anypoint-code-builder/start-acb-desktop)

---

![Setting an extension to auto-update](_images/start-extensions-auto-update.png) 

# Setting Up the Desktop IDE

The desktop-based IDE extensions in Anypoint Extension Pack are available from the Visual Studio Marketplace.

## Before You Begin Desktop IDE Setup

Before installing the desktop extensions to VS Code, make sure you have an Anypoint Platform account with the required permissions:

- 
An administrator with an Anypoint Platform organization account must provide you with the necessary permissions. See [Configuring Permissions](start-configure-permissions).
- 
The cloud IDE requires a non-trial Enterprise license of Mule runtime engine. See [Upgrade Your Account](../access-management/managing-your-account#upgrade-account)and[Install an Enterprise License](../mule-runtime/latest/installing-an-enterprise-license).
- 
Anypoint Platform requires a user account. You can use an existing account or create one from Anypoint Platform (see supported [Cloud Hosts](./#us-eu-clouds)).

For information about OS and system compatibility, see [Anypoint Code Builder Release Notes](acb-release-notes#compatibility).

## Hardware and Storage Requirements

Anypoint Code Builder for Desktop relies on Visual Studio Code (VS Code), Java, Node.js, Maven, and local build artifacts. To avoid timeouts, slow dependency resolution, and poor IDE responsiveness, your environment must meet the following minimum specifications. Recommended values improve performance for larger workspaces and frequent local runs.

For supported operating systems and extension compatibility, see [Anypoint Code Builder Release Notes](acb-release-notes#compatibility).

### Hardware Requirements

| Component | Minimum | Recommended | 
|---|---|---|
| CPU | 8 cores or 8 vCPUs | More cores for parallel builds and multiple large projects | 
| RAM | 32 GB | Additional memory for multiple VS Code windows and heavy local testing | 
| Primary storage type | NVMe SSD (PCIe 3.0 or higher) | Same; avoid network-only or heavily virtualized disks for the OS, user profile, and project roots | 
| Free disk space | 50 GB | 100 GB | 
| Network | 1 Gbps | 10 Gbps (for large dependency downloads and corporate artifact repositories) | 

### Storage Performance

Local disks that can’t sustain the following metrics often show slow indexing, Maven repository access, and Mule application startup.

Confirm values with your storage vendor or disk benchmark tooling on the volume that hosts your user profile, local Maven repository, VS Code data, and project directories. Consider input/output operations per second (IOPS) as well; higher IOPS generally improve responsiveness for random small-file access.

Antivirus, endpoint detection, and real-time scanning can reduce effective IOPS below these targets. Apply the exclusions in [Configure Antivirus and Endpoint Protection Exclusions](#antivirus-exclusions).

| Metric | Minimum Requirement | 
|---|---|
| Random read IOPS (4 KB) | 10,000 IOPS | 
| Random write IOPS (4 KB) | 8,000 IOPS | 
| Sequential read | 1,250 MB/s | 
| Sequential write | 1,000 MB/s | 

### Configure Antivirus and Endpoint Protection Exclusions

On managed devices, add exclusions for the processes and directories that Anypoint Code Builder and its toolchain use most intensively. Exclusions reduce file locking, false positives, and severe I/O latency during builds. They also reduce the scan surface for specific paths and processes, but your organization’s security policy decides whether exclusions are allowed and how they’re deployed.

Use the checklist with your security team. Adjust paths for your environment.

**Processes (executables)**

- 
Windows: `java.exe`or`javaw.exe`— Java runtime used by Mule and tooling
- 
macOS: `java`— same as on Windows, using the resolved path from your JDK install
- 
Windows: `node.exe`— Node.js used by VS Code extensions and scripts
- 
macOS: `node`— same as on Windows
- 
Windows: `Code.exe`— Visual Studio Code
- 
macOS: Visual Studio Code application bundle — for example, `Visual Studio Code.app`

**Directories**

- 
User profile Anypoint Code Builder data: 
 Windows:`%USERPROFILE%\AnypointCodeBuilder`
 macOS:`~/AnypointCodeBuilder`
- 
VS Code user data: 
 Windows:`%USERPROFILE%\.vscode`
 macOS:`~/.vscode`
- 
Local Maven repository: 
 Windows:`%USERPROFILE%\.m2`
 macOS:`~/.m2`
- 
System temporary directory used by the IDE and build tools: 
 Windows:`%USERPROFILE%\AppData\Local\Temp`
 macOS:`$TMPDIR`(or`/tmp`when that is your temp location)
- 
**Projects directory**— the root folder where you clone or store Mule and API projects (your`ProjectsDirectory`); exclude the entire tree, not single files

### Power Settings

Power management can throttle CPU and disk performance during long builds or local runs.

- 
Windows: Prefer a **High performance**or**Balanced**power plan while you work; avoid battery saver or aggressive power saving when the machine is on AC power.
- 
macOS: On notebooks, reduce battery-focused throttling where your org allows it—for example, adjust **System Settings**under**Battery**or**Energy**when plugged in.

For more information about hardware and storage requirements, see [Hardware and Storage Requirements](ref-hardware-storage-requirements).

## Install, Update, or Uninstall Anypoint Extension Pack

Use of Anypoint Code Builder in VS Code on your computer requires the Anypoint Extension Pack.

### Install Anypoint Extension Pack

To install the Anypoint Extension Pack into the desktop IDE:

- 
Open VS Code. 
- 
Find **Anypoint Extension Pack**from the desktop IDE or from[Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=salesforce.mule-dx-extension-pack).To avoid installation errors:Do not install the individual Anypoint Code Builder extensions that are also available separately from Anypoint Extension Pack in Visual Studio Marketplace. - 
To install from the desktop IDE, launch the Extensions menu by clicking the Extensions icon from the activity bar or pressing Cmd+Shift+x (Mac) or Ctrl+Shift+x (Windows), and search for the extension pack. Select **Install Release Version**.
- 
To install from the Visual Studio Marketplace website, find the extension pack, and install: Select **Install Release Version**.For additional guidance, see the [Visual Studio Code website](https://code.visualstudio.com/learn/get-started/extensions).
 
- 
- 
Open the Extensions menu, and review the extensions in Anypoint Extension Pack: Anypoint Extension Pack contains these extensions: - 
Anypoint Code Builder - API Extension 
- 
Anypoint Code Builder - APIkit Extension 
- 
Anypoint Code Builder - DataWeave Extension 
- 
Anypoint Code Builder - Dependencies Extension 
- 
Anypoint Code Builder - Integration Extension 
- 
Anypoint Code Builder - MUnit Extension 
- 
Anypoint Code Builder - Platform Extension For versioning information about extensions in Anypoint Extension Pack, see the [Change Log](https://marketplace.visualstudio.com/items/salesforce.mule-dx-extension-pack/changelog).
 
- 
- 
Recommended: Ensure that the Anypoint extensions update automatically by right-clicking each extension to see if **Auto Update All (From Publisher)**is checked. If it’s not, select**Auto Update**for each extension, for example:![Setting an extension to auto-update](_images/start-extensions-auto-update.png)  Ensure this option is checked. 
- 
Click the MuleSoft icon in the activity bar to access and use Anypoint Code Builder features. 
- 
Check that the IDE loads the [Anypoint Code Builder menu](#acb-menu).
- 
If you have an Anypoint Platform account running in the EU cloud, change the **Mule: Control Plane**setting to**EU cloud**.For guidance, see [Set the Desktop IDE to the EU or US Cloud](start-acb#change-clouds).
- 
Follow the steps in [Log in to Anypoint Platform from the IDE](start-acb#login-ide).

### Update Anypoint Extension Pack

If Anypoint Extension Pack is installed on your desktop IDE, update to the latest version of the extension pack by following VS Code instructions in [Update an extension manually](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace#_update-an-extension-manually).

### Uninstall Anypoint Extension Pack

Typically, it is unnecessary to uninstall the extension pack or individual Anypoint Code Builder extensions from VS Code. For example, you can update to a new version without uninstalling first.

If you decide to uninstall Anypoint Extension Pack, follow the same procedure that you use for other VS Code extensions. Uninstalling the extension pack also uninstalls the individual Anypoint Code Builder extensions that are bundled within the extension pack, such as the DataWeave and APIkit extensions.

To uninstall:

- 
Open VS Code. 
- 
From the activity bar, open the Extensions panel. 
- 
Find and select Anypoint Extension Pack. 
- 
In the Anypoint Extension Pack tab that opens, click **Uninstall**.
- 
To remove the Anypoint Code Builder extensions from the Extensions panel, click **Reload**on one of the extensions.

For additional guidance, see the VS Code documentation, [Manage extensions](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace#_manage-extensions).

You can reinstall at any time.