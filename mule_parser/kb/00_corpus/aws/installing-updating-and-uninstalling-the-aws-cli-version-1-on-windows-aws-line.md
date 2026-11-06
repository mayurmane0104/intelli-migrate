# Installing, Updating, and Uninstalling the AWS CLI version 1 on Windows - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/v1/userguide/install-windows.html](https://docs.aws.amazon.com/cli/v1/userguide/install-windows.html)

---

**This documentation is for Version 1 of the AWS CLI only.**

We announced the upcoming end-of-support for the AWS CLI version 1. We recommend that you migrate to the AWS CLI version 2. For dates, additional details, and information on how to migrate, see the [announcement](https://aws.amazon.com/blogs/developer/cli-v1-maintenance-mode-announcement/). For documentation related to Version 2 of the AWS CLI, see the 

[Version 2 User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

You can install version 1 of the AWS Command Line Interface (AWS CLI) on Windows by using a standalone
        installer (recommended) or `pip`, which is a package manager for Python.

Don't include the prompt symbol (`C:\>`) when you type a command. These are
        included in program listings to differentiate commands that you type from output returned by
        the AWS CLI. The rest of this guide uses the generic prompt symbol (`$`), except in
        cases where a command is Windows-specific.

###### Topics

## Install, update, and uninstall the AWS CLI version 1 using the MSI installer

        The AWS CLI version 1 is supported on Windows XP or later. For Windows users, the MSI installation package offers a familiar and convenient way to install the AWS CLI version 1 without installing any other prerequisites.

### Install and update the AWS CLI version 1 using the MSI installer

Check the [Releases](https://github.com/aws/aws-cli/releases)
                page on GitHub to see when the latest version was released. When updates are
                released, you must repeat the installation process to get the latest version of the
                AWS CLI version 1. 

- 
                    Download the appropriate MSI installer: - 
                            AWS CLI MSI installer for Windows (64-bit): [https://s3.amazonaws.com/aws-cli/AWSCLI64PY3.msi](https://s3.amazonaws.com/aws-cli/AWSCLI64PY3.msi)
- 
                            AWS CLI MSI installer for Windows (32-bit): [https://s3.amazonaws.com/aws-cli/AWSCLI32PY3.msi](https://s3.amazonaws.com/aws-cli/AWSCLI32PY3.msi)
- 
                            AWS CLI combined setup file for Windows: [https://s3.amazonaws.com/aws-cli/AWSCLISetup.exe](https://s3.amazonaws.com/aws-cli/AWSCLISetup.exe)(includes both the 32-bit and 64-bit MSI installers, and automatically installs the correct version)
 
- 
                            
- 
                    Run the downloaded MSI installer or the setup file. 
- 
                    Follow the on-screen instructions. By default, the AWS CLI version 1 installs to `C:\Program Files\Amazon\AWSCLI`(64-bit version) or`C:\Program Files (x86)\Amazon\AWSCLI`(32-bit version).
- 
                    To confirm the installation, use the `aws --version`command at a command prompt (open the**Start**menu and search for`cmd`to start a command prompt).`C:\>``aws --version``aws-cli/1.40.41 Python/3.11.6 Windows/10 botocore/1.18.6`If Windows is unable to find the program, you might need to close and reopen the command prompt to refresh the path, or [add the installation directory to your PATH](#awscli-install-windows-path)environment variable manually.

### Uninstall the AWS CLI version 1

To use the following uninstall instructions, you need to have installed the AWS CLI version 1 with the MSI installer or setup file.

- 
                    Open **Programs and Features**by doing one of the following:- 
                            Open the **Control Panel**, and then choose**Programs and Features**.
- 
                            Open a command prompt and enter the following command. `C:\>``appwiz.cpl`
 
- 
                            
- 
                    Select the entry named **AWS Command Line Interface**, and then choose**Uninstall**to launch the uninstaller.
- 
                    Confirm that you want to uninstall the AWS CLI. 
- 
                    **(Optional)**Remove the shared AWS SDK and AWS CLI settings information in the`.aws`folder.###### WarningThese configuration and credentials settings are shared across all AWS SDKs and the AWS CLI. If you remove this folder, they cannot be accessed by any AWS SDKs that are still on your system. The default location of the `.aws`folder differs between platforms, by default the folder is located in`%UserProfile%\.aws`.`$``rmdir``%UserProfile%\.aws`

## Install, update, and uninstall the AWS CLI version 1 using Python and pip on Windows

        The Python Software Foundation provides installers for Windows that include
                `pip`.

### Prerequisites

You must have Python 3.8 or later installed. For installation instructions, see the
                    [Downloading
                    Python](https://wiki.python.org/moin/BeginnersGuide/Download) page in Python's 

*Beginner Guide*.

### Install and update the AWS CLI version 1 using pip

- 
                    To Install the AWS CLI version 1, use the `pip3`command (if you use Python version 3 or later) or the`pip`command.**For the latest version of the AWS CLI,**use the following command block:`C:\>``pip3 install awscli --upgrade --user`**For a specific version of the AWS CLI,**append a less-than symbol`<`and the version number to the filename. For this example the filename for version`1.16.312`would be`<1.16.312`resulting in the following command:`C:\>``pip3 install awscli<``1.16.312`--upgrade --user
- 
                    Verify that the AWS CLI version 1 is installed correctly. If there is no response, see the [Add the AWS CLI version 1 executable to your command line path](#awscli-install-windows-path)section.`C:\>``aws --version``aws-cli/1.40.41 Python/3.11.6 Windows/10 botocore/1.18.6`

### Uninstall the AWS CLI version 1 using pip

- 
                    If you installed the AWS CLI version 1 using `pip`, you must also uninstall using`pip`.`C:\>``pip uninstall awscli`If you are using version Python 2 or 3, you might need to use the `pip2`or`pip3`command. Use the`aws --version`command to determine the Python version associated with your installed AWS CLI version 1.`C:\>``pip3 uninstall awscli`You might need to restart your command prompt window or your computer to remove all files. 
- 
                    **(Optional)**Remove the shared AWS SDK and AWS CLI settings information in the`.aws`folder.###### WarningThese configuration and credentials settings are shared across all AWS SDKs and the AWS CLI. If you remove this folder, they cannot be accessed by any AWS SDKs that are still on your system. The default location of the `.aws`folder differs between platforms, by default the folder is located in`%UserProfile%\.aws`.`$``rmdir``%UserProfile%\.aws`

## Add the AWS CLI version 1 executable to your command line path

        After installing the AWS CLI version 1 with `pip`, add the `aws` program
            to your operating system's `PATH` environment variable. With an MSI
            installation, this should happen automatically. But if the `aws` command
            doesn't run after you install it, you might need to set it manually.

- 
                Use the `where`command to find the`aws`file location. By default, the`where`command shows where a specified program is found in the system's`PATH`.`C:\>``where aws`The paths that show up depend on your platform and which method you used to install the AWS CLI. Folder names that include version numbers can vary. These examples reflect the use of Python version 3.7. Replace the version with the version number you're using, as needed. Typical paths include the following: - 
                        Python 3 and `pip3`–`C:\Program Files\Python37\Scripts\`
- 
                        Python 3 and `pip3`--user option on earlier versions of Windows –`%USERPROFILE%\AppData\Local\Programs\Python\Python37\Scripts`
- 
                        Python 3 and `pip3`--user option on Windows 10 –`%USERPROFILE%\AppData\Roaming\Python\Python37\Scripts`
- 
                        MSI installer (64-bit) – `C:\Program Files\Amazon\AWSCLI\bin`
- 
                        MSI installer (32-bit) – `C:\Program Files (x86)\Amazon\AWSCLI\bin`
 Use the following steps based on whether a file path is returned. `C:\>``where aws``C:\Program Files\Amazon\AWSCLI\bin\aws.exe`You can find where the `aws`program is installed by running the following command.`C:\>``where c:\ aws``C:\Program Files\Python37\Scripts\aws`
- 
                        
- 
                Press the Windows key and enter `environment variables`.
- 
                Choose **Edit environment variables for your account**.
- 
                Choose **PATH**, and then choose**Edit**.
- 
                Add the path you found into the **Variable value**field, for example,`C:\Program Files\Amazon\AWSCLI\bin\aws.exe`
- 
                Choose **OK**twice to apply the new settings.
- 
                Close any running command prompts and reopen the command prompt window. 

## Troubleshooting AWS CLI install and uninstall errors

        If you come across issues after installing or uninstalling the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for troubleshooting steps. For the most
            relevant troubleshooting steps, see [Command not found errors](./cli-chap-troubleshooting.html#tshoot-install-not-found), [The "aws --version" command returns a different version than you installed](./cli-chap-troubleshooting.html#tshoot-install-wrong-version), and [The "aws --version" command returns a version after uninstalling the AWS CLI](./cli-chap-troubleshooting.html#tshoot-uninstall-1).