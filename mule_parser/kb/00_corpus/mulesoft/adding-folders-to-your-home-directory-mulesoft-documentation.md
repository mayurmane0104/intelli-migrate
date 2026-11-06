# Adding Folders to Your Home Directory | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/anypoint-code-builder/start-add-folders](https://docs.mulesoft.com/anypoint-code-builder/start-add-folders)

---

- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
In the desktop IDE, select **View**>**Command Palette**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Command Palette**.

# Adding Folders to Your Home Directory

When you create a project, Anypoint Code Builder stores it in your home directory by default. You can create other folders for your projects in the IDE.

Don’t create the project within another project directory.

## Create Project Folders in the Cloud IDE

To a folder for storing your Mule projects under your home directory:

- 
Open the Command Palette. ## Show me how
- 
Select the following command: `File: Open Folder...`command![Finding the command in the Command Palette](_images/file-open-folder-command.png)  
- 
Select your Anypoint Code Builder home directory: ![Adding a home directory to the Open Folder field](_images/select-home-directory.png)  If prompted, trust the authors of the files in the directory: ![Trusting authors of the files in the folder](_images/trust-home-directory.png)  
- 
After Anypoint Code Builder loads your home directory, right-click your Explorer view, and select **New Folder**.![Selecting New Folder from the Explorer](_images/new-folder-home-directory.png)  
- 
Name your new directory and press Enter. 
- 
Close your home directory by clicking the ![](_images/icon-menu.png) (menu) icon and selecting (menu) icon and selecting**File**>**Close Folder**.![Closing the folder from the File menu](_images/close-working-directory.png)  

## Create a Project Folder in the Desktop IDE

To create a local folder for your projects from the desktop IDE:

- 
Open the Command Palette. ## Show me how- 
Use the keyboard shortcuts: - 
Mac: Cmd+Shift+p 
- 
Windows: Ctrl+Shift+p 
 
- 
- 
In the desktop IDE, select **View**>**Command Palette**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**View**>**Command Palette**.
 
- 
- 
Select the following command: `File: Open Folder...`command![Opening a folder from the Command Palette](_images/file-open-folder-command.png)  
- 
Use your local directory to create a new folder. 

## Create a Project Folder from the Desktop or Cloud IDE

Use the terminal in the IDE to create folders.

- 
Ensure that no projects are open. 
- 
From your IDE, open the Terminal window in the console: - 
In the desktop IDE, select **View**>**Terminal**.
- 
In the cloud IDE, click the ![](_images/icon-menu.png) (menu) icon, and select (menu) icon, and select**Terminal**>**New Terminal**.
- 
For either IDE: Press Ctrl and then press the backtick key (`). 
 
- 
- 
Provide this command to create a folder: `mkdir <name-of-your-folder>`Replace `<name-of-your-folder>`with a name of your choice for the directory.