# Installing, updating, and uninstalling the AWS CLI version 1 on Linux - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html](https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html)

---

**This documentation is for Version 1 of the AWS CLI only.**

We announced the upcoming end-of-support for the AWS CLI version 1. We recommend that you migrate to the AWS CLI version 2. For dates, additional details, and information on how to migrate, see the [announcement](https://aws.amazon.com/blogs/developer/cli-v1-maintenance-mode-announcement/). For documentation related to Version 2 of the AWS CLI, see the 

[Version 2 User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).

You can install the AWS Command Line Interface (AWS CLI) version 1 and its dependencies on most Linux
    distributions by using the `pip` package manager or the bundled installer.

Although the `awscli` package is available in repositories for other package
    managers such as `apt` and `yum`, these are not produced, managed, or
    supported by AWS. We recommend that you install the AWS CLI from only the official AWS
    distribution points, as documented in this guide.

###### Sections

## Prerequisites

    You must have Python 3.8 or later installed. For installation instructions, see the [Downloading Python](https://wiki.python.org/moin/BeginnersGuide/Download) page
      in Python's 

*Beginner Guide*.

**Python version support matrix**

| AWS CLI version | Supported Python version | 
|---|---|
| 1.39.0 – current | Python 3.9+ | 
| 1.32.0 – 1.38.38 | Python 3.8+ | 
| 1.27.0 – 1.31.x | Python 3.7+ | 
| 1.20.0 – 1.26.x | Python 3.6+ | 
| 1.19.0 – 1.19.x | Python 2.7+, Python 3.6+ | 
| 1.17 – 1.18.x | Python 2.7+, Python 3.4+ | 
| 1.0 – 1.16.x | Python 2.6 and older, Python 3.3 and older | 

## Install and uninstall the AWS CLI version 1 on Linux using the bundled installer

    On Linux or macOS, you can use the bundled installer to install version 1 of the AWS CLI. The bundled installer includes all dependencies and can be used offline.

###### Note

The bundled installer doesn't support installing to paths that contain spaces.

###### Topics

### Install the AWS CLI version 1 using the bundled installer with `sudo`

      The following steps enable you to install the AWS CLI version 1 from the command line on any build of Linux or macOS.

The following is a summary of the installation commands explained below that you can cut and paste to run as a single set of commands.

**For the latest version of the AWS CLI,** use the following
        command block:

`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" unzip awscli-bundle.zip sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws`

**For a specific version of the AWS CLI,** append a hyphen
        and the version number to the filename. For this example the filename for version
          `1.16.312` would be
          `awscli-bundle-1.16.312.zip` resulting in the following command:

`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle-``1.16.312`.zip" -o "awscli-bundle.zip" unzip awscli-bundle.zip sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

Follow these steps from the command line to install the AWS CLI version 1 using the bundled installer.

###### To install the AWS CLI version 1 using the bundled installer

- 
          Download the AWS CLI version 1 bundled installer using one of the the following methods. - 
              Download using the `curl`command.**For the latest version of the AWS CLI,**use the following command block:`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"`**For a specific version of the AWS CLI,**append a hyphen and the version number to the filename. For this example the filename for version`1.16.312`would be`awscli-bundle-1.16.312.zip`resulting in the following command:`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle-``1.16.312`.zip" -o "awscli-bundle.zip"
- 
              Download using the direct link. **For the latest version of the AWS CLI:**[https://s3.amazonaws.com/aws-cli/awscli-bundle.zip](https://s3.amazonaws.com/aws-cli/awscli-bundle.zip)**For a specific version of the AWS CLI,**append a hyphen and the version number to the filename. For this example the filename for version`1.16.312`would be`awscli-bundle-`resulting in the following url`1.16.312`.zip[https://s3.amazonaws.com/aws-cli/awscli-bundle-1.16.312.zip](https://s3.amazonaws.com/aws-cli/awscli-bundle-1.16.312.zip)
 
- 
              
- 
          Extract the files from the package. If you don't have `unzip`to extract the files, use your Linux distribution's built-in package manager to install it.`$``unzip awscli-bundle.zip`
- 
          Run the install program. The installer installs the AWS CLI at `/usr/local/aws`and creates the symlink`aws`at the`/usr/local/bin`directory. Using the`-b`option to create a symlink eliminates the need to specify the install directory in the user's`$PATH`variable. This should enable all users to call the AWS CLI by entering`aws`from any directory.`$``sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws`By default, the install script runs under the system default version of Python. If you have installed an alternative version of Python and want to use that version to install the AWS CLI, run the install script with that version by absolute path to the Python executable, as follows. `$``sudo``/usr/local/bin/python3.7`awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws
- 
          Verify that the AWS CLI installed correctly. `$``aws --version``aws-cli/1.40.41 Python/3.11.6 Linux/5.10.205-195.807.amzn2.x86_64 botocore/1.18.6`If you get an error, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

### Install the AWS CLI version 1 using the bundled installer without `sudo`

      If you don't have `sudo` permissions or want to install the AWS CLI only for
        the current user, you can use a modified version of the previous commands. The first two
        commands are the same. 

**For the latest version of the AWS CLI,** use the following
        command block:

`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" unzip awscli-bundle.zip ./awscli-bundle/install -b ~/bin/aws`

**For a specific version of the AWS CLI,** append a hyphen
        and the version number to the filename. For this example the filename for version
          `1.16.312` would be
          `awscli-bundle-1.16.312.zip` resulting in the following command:

`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle-``1.16.312`.zip" -o "awscli-bundle.zip" unzip awscli-bundle.zip ./awscli-bundle/install -b ~/bin/aws

###### To install the AWS CLI version 1 for current user

- 
          Download the AWS CLI version 1 bundled installer in one of the following ways. - 
              Download using the `curl`command.**For the latest version of the AWS CLI,**use the following command block:`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"`**For a specific version of the AWS CLI,**append a hyphen and the version number to the filename. For this example the filename for version`1.16.312`would be`awscli-bundle-1.16.312.zip`resulting in the following command:`$``curl "https://s3.amazonaws.com/aws-cli/awscli-bundle-``1.16.312`.zip" -o "awscli-bundle.zip"
- 
              Download using the direct link. **For the latest version of the AWS CLI:**[https://s3.amazonaws.com/aws-cli/awscli-bundle.zip](https://s3.amazonaws.com/aws-cli/awscli-bundle.zip)**For a specific version of the AWS CLI,**append a hyphen and the version number to the filename. For this example the filename for version`1.16.312`would be`awscli-bundle-`resulting in the following url`1.16.312`.zip[https://s3.amazonaws.com/aws-cli/awscli-bundle-1.16.312.zip](https://s3.amazonaws.com/aws-cli/awscli-bundle-1.16.312.zip)
 
- 
              
- 
          Extract the files from the package by using `unzip`. If you don't have`unzip`, use your Linux distribution's built-in package manager to install it.`$``unzip awscli-bundle.zip`
- 
          Run the install program. The installer installs the AWS CLI at `/usr/local/aws`and creates the symlink`aws`at the`/usr/local/bin`directory. The command uses the`-b`parameter to specify the directory where the installer places the`aws`symlink file. You must have write permissions to the specified folder.`$``./awscli-bundle/install -b ~/bin/aws`This installs the AWS CLI to the default location ( `~/.local/lib/aws`) and creates a symbolic link (symlink) at`~/bin/aws`. Make sure that`~/bin`is in your`PATH`environment variable for the symlink to work.`$``echo $PATH | grep ~/bin`// See if $PATH contains ~/bin (output will be empty if it doesn't)`$``export PATH=~/bin:$PATH`// Add ~/bin to $PATH if necessary
- 
          Ensure the directory that the AWS CLI version 1 is part of your `PATH`variable.- 
              Find your shell's profile script in your user folder. If you're not sure which shell you have, run `echo $SHELL`.`$``ls -a ~``. .. .bash_logout .bash_profile .bashrc Desktop Documents Downloads`- 
                  Bash – `.bash_profile`,`.profile`, or`.bash_login`
- 
                  Zsh – `.zshrc`
- 
                  Tcsh – `.tcshrc`,`.cshrc`or`.login`
 
- 
                  
- 
              Add an export command at the end of your profile script that's similar to the following example. `export PATH=``~/.local/bin`:$PATHThis command inserts the path, `~/.local/bin`in this example, at the front of the existing`PATH`variable.
- 
              Reload the profile into your current session to put those changes into effect. `$``source ~/``.bash_profile`
 
- 
              
- 
          Verify that the AWS CLI installed correctly. `$``aws --version``aws-cli/1.40.41 Python/3.11.6 Linux/5.10.205-195.807.amzn2.x86_64 botocore/1.18.6`If you get an error, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

### Uninstall the AWS CLI version 1 bundled installer

- 
          If you installed the AWS CLI using the bundled installer, follow these instructions. The bundled installer doesn't put anything outside of the installation directory except the optional symlink, so uninstalling is as simple as deleting those two items. `$``sudo rm -rf /usr/local/aws``$``sudo rm -rf /usr/local/bin/aws`
- 
          **(Optional)**Remove the shared AWS SDK and AWS CLI settings information in the`.aws`folder.###### WarningThese configuration and credentials settings are shared across all AWS SDKs and the AWS CLI. If you remove this folder, they cannot be accessed by any AWS SDKs that are still on your system. The default location of the `.aws`folder differs between platforms, by default the folder is located in`~/.aws/`. If your user has write permission to this directory, you don't need to use`sudo`.`$``sudo rm -r``~/.aws/`

## Install and uninstall the AWS CLI version 1 using pip

    
     
      ### Install pip

If you don't already have `pip` installed, you can install it by using the
        script that the *Python Packaging Authority* provides. Run
          `pip --version` to see if your version of Linux already includes Python and
          `pip`. We recommend that if you have Python version 3 or later installed, you
        use the `pip3` command.

- 
          Use the `curl`command to download the installation script. The following command uses the`-O`(uppercase "O")parameter to specify that the downloaded file is to be stored in the current directory using the same name it has on the remote host.`$``curl -O https://bootstrap.pypa.io/get-pip.py`
- 
          Run the script with the `python`or`python3`command to download and install the latest version of`pip`and other required support packages. When you include the`--user`switch, the script installs`pip`to the path`~/.local/bin`.`$``python3 get-pip.py --user`
- 
          Ensure the directory that contains `pip`is part of your`PATH`variable.- 
              Find your shell's profile script in your user folder. If you're not sure which shell you have, run `echo $SHELL`.`$``ls -a ~``. .. .bash_logout .bash_profile .bashrc Desktop Documents Downloads`- 
                  Bash – `.bash_profile`,`.profile`, or`.bash_login`
- 
                  Zsh – `.zshrc`
- 
                  Tcsh – `.tcshrc`,`.cshrc`or`.login`
 
- 
                  
- 
              Add an export command at the end of your profile script that's similar to the following example. `export PATH=``~/.local/bin`:$PATHThis command inserts the path, `~/.local/bin`in this example, at the front of the existing`PATH`variable.
- 
              Reload the profile into your current session to put those changes into effect. `$``source ~/``.bash_profile`
 
- 
              
- 
          To verify that `pip`or`pip3`is installed correctly, run the following command.`$``pip3 --version``pip 24.0 from ~/.local/lib/python3.7/site-packages (python 3.7)`

### Install and update the AWS CLI version 1 using pip

- 
          Use the `pip`or`pip3`command to install or update the AWS CLI. We recommend that if you use Python version 3 or later that you use the`pip3`command. The`--user`switch,`pip`installs the AWS CLI to`~/.local/bin`.**For the latest version of the AWS CLI,**use the following command block:`$``pip3 install awscli --upgrade --user`**For a specific version of the AWS CLI,**append two equals signs`=`and the version number to the filename. For this example the filename for version`1.16.312`would be`==1.16.312`resulting in the following command:`$``pip3 install awscli==``1.16.312`--upgrade --user###### NoteUse appropriate quoting rules for your terminal. In order to use the `=`character, you might need to use single or double quotes to escape properly. The following example escapes using single quotes:`$``pip3 install 'awscli==``1.16.312`' --upgrade --user
- 
          Verify that the AWS CLI installed correctly. `$``aws --version``aws-cli/1.40.41 Python/3.11.6 Linux/5.10.205-195.807.amzn2.x86_64 botocore/1.18.6`If you get an error, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

### Uninstall the AWS CLI using pip

- 
          If you installed the AWS CLI version 1 using `pip`, you must also uninstall using`pip`.`$``pip uninstall awscli`If you are using version Python 2 or 3, you might need to use the `pip2`or`pip3`command. Use the`aws --version`command to determine the Python version associated with your installed AWS CLI version 1.`$``pip3 uninstall awscli`You might need to restart your command prompt window or your computer to remove all files. 
- 
          **(Optional)**Remove the shared AWS SDK and AWS CLI settings information in the`.aws`folder.###### WarningThese configuration and credentials settings are shared across all AWS SDKs and the AWS CLI. If you remove this folder, they cannot be accessed by any AWS SDKs that are still on your system. The default location of the `.aws`folder differs between platforms, by default the folder is located in`~/.aws/`. If your user has write permission to this directory, you don't need to use`sudo`.`$``sudo rm -r``~/.aws/`

## Install and uninstall the AWS CLI version 1 using Snapcraft

    ###### Topics

### Install snap

If you don't already have `snap` installed, you can install it by using the
        instructions *Canonical Snapcraft* provides. Run ```
snap
          version
```
 to see if your version of Linux already includes `snap`.

- 
          Install Snapcraft on your platform. For information on installing Snapcraft, see [Installing the daemon](https://snapcraft.io/docs/installing-snapd)in the*Snap documentation*.
- 
          Restart your system so that your `PATH`variables are updated correctly. If you are having installation issues, follow steps in[Fix common issues](https://snapcraft.io/docs/fix-common-issues)in the*Snap documentation*.
- 
          To verify that `snap`is installed correctly, run the following command.`$``snap version`

### Install and update the AWS CLI version 1 using snap

- 
          Run the following `snap install`command for the AWS CLI version 1.`$``snap install aws-cli --channel=v1/stable --classic`Depending on your permissions, you may need to add `sudo`to your command.`$``sudo snap install aws-cli --channel=v1/stable --classic`
- 
          Verify that the AWS CLI installed correctly. `$``aws --version``aws-cli/1.40.41 Python/3.11.6 Linux/5.10.205-195.807.amzn2.x86_64 botocore/1.18.6`If you get an error, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

### Uninstall the AWS CLI using snap

- 
          If you installed the AWS CLI version 1 using `snap`, you must also uninstall using`snap`.`$``snap remove aws-cli`You might need to restart your command prompt window or your computer to remove all files. 
- 
          **(Optional)**Remove the shared AWS SDK and AWS CLI settings information in the`.aws`folder.###### WarningThese configuration and credentials settings are shared across all AWS SDKs and the AWS CLI. If you remove this folder, they cannot be accessed by any AWS SDKs that are still on your system. The default location of the `.aws`folder differs between platforms, by default the folder is located in`~/.aws/`. If you have write permissions to this directory, you don't need to use`sudo`.`$``sudo rm -r``~/.aws/`

## Add the AWS CLI version 1 executable to your command line path

    After installing with `pip` or `snap`, you might need to add the
        `aws` executable to your operating system' `PATH` environment
      variable.

You can verify which folder `pip` installed the AWS CLI in by running the
      following command.

`$``which aws``/home/``username`/.local/bin/aws

You can reference this as `~/.local/bin/` because
        `/home/username` corresponds to `~` in Linux.

If you omitted the `--user` switch and so didn't install in user mode, the
      executable might be in the `bin` folder of your Python installation. If you
      don't know where Python is installed, run this command.

`$``which python``/usr/local/bin/python`

The output might be the path to a symlink, not to the actual executable. Run ```
ls
        -al
```
 to see where it points.

`$``ls -al /usr/local/bin/python``/usr/local/bin/python -> ~/.local/Python/3.6/bin/python3.6`

`pip` installs programs in the same folder that contains the Python
      application. Add this folder to your `PATH` variable.

###### To modify your `PATH` variable

- 
    Find your shell's profile script in your user directory. If you're not sure which shell you have, run `echo $SHELL`.`$``ls -a ~``. .. .bash_logout .bash_profile .bashrc Desktop Documents Downloads`- 
        Bash – `.bash_profile`,`.profile`, or`.bash_login`
- 
        Zsh – `.zshrc`
- 
        Tcsh – `.tcshrc`,`.cshrc`, or`.login`
 
- 
        
- 
    Add an export command to your profile script. `export PATH=``~/.local/bin`:$PATHThis command adds a path, `~/.local/bin`in this example, to the current`PATH`variable.
- 
    Load the updated profile into your current session. `$``source ~/``.bash_profile`

## Troubleshooting AWS CLI install and uninstall errors

    If you come across issues after installing or uninstalling the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for troubleshooting steps. For the most relevant
      troubleshooting steps, see [Command not found errors](./cli-chap-troubleshooting.html#tshoot-install-not-found), [The "aws --version" command returns a different version than you installed](./cli-chap-troubleshooting.html#tshoot-install-wrong-version), and [The "aws --version" command returns a version after uninstalling the AWS CLI](./cli-chap-troubleshooting.html#tshoot-uninstall-1).