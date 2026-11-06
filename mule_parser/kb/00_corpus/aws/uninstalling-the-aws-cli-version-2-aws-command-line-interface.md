# Uninstalling the AWS CLI version 2 - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/uninstall.html](https://docs.aws.amazon.com/cli/latest/userguide/uninstall.html)

---

This topic describes how to uninstall the AWS Command Line Interface version 2 (AWS CLI version 2).

AWS CLI version 2 uninstallation instructions:

To uninstall, follow the same method you used to install the AWS CLI.

To uninstall the AWS CLI version 2, run the following commands, substituting the paths you used to install. The example commands use the default installation paths.

- 
                    Find the folder that contains the symlinks to the main program and the completer. `$``which aws``/usr/local/bin`/aws
- 
                    Using that information, run the following command to find the installation folder that the symlinks point to. `$``ls -l /usr/local/bin/aws``lrwxrwxrwx 1 ec2-user ec2-user 49 Oct 22 09:49 /usr/local/bin/aws ->``/usr/local/aws-cli`/aws
- 
                    Delete the two symlinks in the first folder. If your user already has write permission to these folders, you don't need to use `sudo`.`$``sudo rm``/usr/local/bin`/aws`$``sudo rm``/usr/local/bin`/aws_completer
- 
                    Delete the main installation folder. Use `sudo`to gain write access to the`/usr/local`folder.`$``sudo rm -rf``/usr/local/aws-cli`
- 
                    **(Optional)**Remove the shared AWS SDK and AWS CLI settings information in the`.aws`folder.###### WarningThese configuration and credentials settings are shared across all AWS SDKs and the AWS CLI. If you remove this folder, they cannot be accessed by any AWS SDKs that are still on your system. The default location of the `.aws`folder differs between platforms, by default the folder is located in`~/.aws/`. If your user has write permission to this directory, you don't need to use`sudo`.`$``sudo rm -rf``~/.aws/`

- 
                    Open **Programs and Features**by doing one of the following:- 
                            Open the **Control Panel**, and then choose**Programs and Features**.
- 
                            Open a command prompt, and then enter the following command. `C:\>``appwiz.cpl`
 
- 
                            
- 
                    Select the entry named **AWS Command Line Interface**, and then choose**Uninstall**to launch the uninstaller.
- 
                    Confirm that you want to uninstall the AWS CLI. 
- 
                    **(Optional)**Remove the shared AWS SDK and AWS CLI settings information in the`.aws`folder.###### WarningThese configuration and credentials settings are shared across all AWS SDKs and the AWS CLI. If you remove this folder, they cannot be accessed by any AWS SDKs that are still on your system. The default location of the `.aws`folder differs between platforms, by default the folder is located in`%UserProfile%\.aws`.`$``rmdir``%UserProfile%\.aws`

## Troubleshooting AWS CLI install and uninstall errors

        If you come across issues after installing or uninstalling the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for troubleshooting steps. For the most
            relevant troubleshooting steps, see [Command not found errors](./cli-chap-troubleshooting.html#tshoot-install-not-found), [The "aws --version" command returns a different version than you installed](./cli-chap-troubleshooting.html#tshoot-install-wrong-version), and [The "aws --version" command returns a version after uninstalling the AWS CLI](./cli-chap-troubleshooting.html#tshoot-uninstall-1).