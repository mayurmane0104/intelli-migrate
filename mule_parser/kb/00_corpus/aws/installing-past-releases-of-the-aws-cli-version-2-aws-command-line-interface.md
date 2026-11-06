# Installing past releases of the AWS CLI version 2 - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-version.html)

---

This topic describes how to install the past releases of the AWS Command Line Interface version 2 (AWS CLI) on
    supported operating systems. For information on the AWS CLI version 2 releases, see the [AWS CLI version 2 Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst)
    on GitHub.

AWS CLI version 2 installation instructions:

### Installation requirements

- 
            You know which release of the AWS CLI version 2 you'd like to install. For a list of versions, see the [AWS CLI version 2 Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst)on*GitHub*.
- 
            You must be able to extract or "unzip" the downloaded package. If your operating system doesn't have the built-in `unzip`command, use an equivalent.
- 
            The AWS CLI version 2 uses `glibc`,`groff`, and`less`. These are included by default in most major distributions of Linux.
- 
            We support the AWS CLI version 2 on 64-bit versions of recent distributions of CentOS, Fedora, Ubuntu, Amazon Linux 1, Amazon Linux 2 and Linux ARM. 
- 
            Because AWS doesn't maintain third-party repositories, we can’t guarantee that they contain the latest version of the AWS CLI. 

### Installation instructions

Follow these steps from the command line to install the AWS CLI on Linux.

We provide the steps in one easy to copy and paste group based on whether you use 64-bit Linux or Linux ARM. See the descriptions of each line in the steps that follow.

- 
            Download the installation file in one of the following ways: 
- 
            **(Optional) Verifying the integrity of your downloaded zip file**If you chose to manually download the AWS CLI installer package `.zip`in the above steps, you can use the following steps to verify the signatures by using the`GnuPG`tool.The AWS CLI installer package `.zip`files are cryptographically signed using PGP signatures. If there is any damage or alteration of the files, this verification fails and you should not proceed with installation.- 
                Download and install the `gpg`command using your package manager. For more information about`GnuPG`, see the[GnuPG website](https://www.gnupg.org/).
- 
                To create the public key file, create a text file and paste in the following text. `-----BEGIN PGP PUBLIC KEY BLOCK----- mQINBF2Cr7UBEADJZHcgusOJl7ENSyumXh85z0TRV0xJorM2B/JL0kHOyigQluUG ZMLhENaG0bYatdrKP+3H91lvK050pXwnO/R7fB/FSTouki4ciIx5OuLlnJZIxSzx PqGl0mkxImLNbGWoi6Lto0LYxqHN2iQtzlwTVmq9733zd3XfcXrZ3+LblHAgEt5G TfNxEKJ8soPLyWmwDH6HWCnjZ/aIQRBTIQ05uVeEoYxSh6wOai7ss/KveoSNBbYz gbdzoqI2Y8cgH2nbfgp3DSasaLZEdCSsIsK1u05CinE7k2qZ7KgKAUIcT/cR/grk C6VwsnDU0OUCideXcQ8WeHutqvgZH1JgKDbznoIzeQHJD238GEu+eKhRHcz8/jeG 94zkcgJOz3KbZGYMiTh277Fvj9zzvZsbMBCedV1BTg3TqgvdX4bdkhf5cH+7NtWO lrFj6UwAsGukBTAOxC0l/dnSmZhJ7Z1KmEWilro/gOrjtOxqRQutlIqG22TaqoPG fYVN+en3Zwbt97kcgZDwqbuykNt64oZWc4XKCa3mprEGC3IbJTBFqglXmZ7l9ywG EEUJYOlb2XrSuPWml39beWdKM8kzr1OjnlOm6+lpTRCBfo0wa9F8YZRhHPAkwKkX XDeOGpWRj4ohOx0d2GWkyV5xyN14p2tQOCdOODmz80yUTgRpPVQUtOEhXQARAQAB tCFBV1MgQ0xJIFRlYW0gPGF3cy1jbGlAYW1hem9uLmNvbT6JAlQEEwEIAD4CGwMF CwkIBwIGFQoJCAsCBBYCAwECHgECF4AWIQT7Xbd/1cEYuAURraimMQrMRnJHXAUC aGveYQUJDMpiLAAKCRCmMQrMRnJHXKBYD/9Ab0qQdGiO5hObchG8xh8Rpb4Mjyf6 0JrVo6m8GNjNj6BHkSc8fuTQJ/FaEhaQxj3pjZ3GXPrXjIIVChmICLlFuRXYzrXc Pw0lniybypsZEVai5kO0tCNBCCFuMN9RsmmRG8mf7lC4FSTbUDmxG/QlYK+0IV/l uJkzxWa+rySkdpm0JdqumjegNRgObdXHAQDWlubWQHWyZyIQ2B4U7AxqSpcdJp6I S4Zds4wVLd1WE5pquYQ8vS2cNlDm4QNg8wTj58e3lKN47hXHMIb6CHxRnb947oJa pg189LLPR5koh+EorNkA1wu5mAJtJvy5YMsppy2y/kIjp3lyY6AmPT1posgGk70Z CmToEZ5rbd7ARExtlh76A0cabMDFlEHDIK8RNUOSRr7L64+KxOUegKBfQHb9dADY qqiKqpCbKgvtWlds909Ms74JBgr2KwZCSY1HaOxnIr4CY43QRqAq5YHOay/mU+6w hhmdF18vpyK0vfkvvGresWtSXbag7Hkt3XjaEw76BzxQH21EBDqU8WJVjHgU6ru+ DJTs+SxgJbaT3hb/vyjlw0lK+hFfhWKRwgOXH8vqducF95NRSUxtS4fpqxWVaw3Q V2OWSjbne99A5EPEySzryFTKbMGwaTlAwMCwYevt4YT6eb7NmFhTx0Fis4TalUs+ j+c7Kg92pDx2uQ== =OBAt -----END PGP PUBLIC KEY BLOCK-----`For reference, the following are the details of the public key. `Key ID: A6310ACC4672 Type: RSA Size: 4096/4096 Created: 2019-09-18 Expires: 2026-07-07 User ID: AWS CLI Team <aws-cli@amazon.com> Key fingerprint: FB5D B77F D5C1 18B8 0511 ADA8 A631 0ACC 4672 475C`
- 
                Import the AWS CLI public key with the following command, substituting `public-key-file-name`with the file name of the public key you created.`$``gpg --import``public-key-file-name``gpg: /home/``username`/.gnupg/trustdb.gpg: trustdb created gpg: key A6310ACC4672475C: public key "AWS CLI Team <aws-cli@amazon.com>" imported gpg: Total number processed: 1 gpg: imported: 1
- 
                Download the AWS CLI signature file for the package you downloaded. It has the same path and name as the `.zip`file it corresponds to, but has the extension`.sig`. In the following examples, we save it to the current directory as a file named`awscliv2.sig`.
- 
                Verify the signature, passing both the downloaded `.sig`and`.zip`file names as parameters to the`gpg`command.`$``gpg --verify awscliv2.sig awscliv2.zip`The output should look similar to the following. `gpg: Signature made Mon Nov 4 19:00:01 2019 PST gpg: using RSA key FB5D B77F D5C1 18B8 0511 ADA8 A631 0ACC 4672 475C gpg: Good signature from "AWS CLI Team <aws-cli@amazon.com>" [unknown] gpg: WARNING: This key is not certified with a trusted signature! gpg: There is no indication that the signature belongs to the owner. Primary key fingerprint: FB5D B77F D5C1 18B8 0511 ADA8 A631 0ACC 4672 475C`###### ImportantThe warning in the output is expected and doesn't indicate a problem. It occurs because there isn't a chain of trust between your personal PGP key (if you have one) and the AWS CLI PGP key. For more information, see [Web of trust](https://en.wikipedia.org/wiki/Web_of_trust).
 
- 
                
- 
            Unzip the installer. If your Linux distribution doesn't have a built-in `unzip`command, use an equivalent to unzip it. The following example command unzips the package and creates a directory named`aws`under the current directory.`$``unzip awscliv2.zip`
- 
            Run the install program. The installation command uses a file named `install`in the newly unzipped`aws`directory. By default, the files are all installed to`/usr/local/aws-cli`, and a symbolic link is created in`/usr/local/bin`. The command includes`sudo`to grant write permissions to those directories.`$``sudo ./aws/install`You can install without `sudo`if you specify directories that you already have write permissions to. Use the following instructions for the`install`command to specify the installation location:- 
                Ensure that the paths you provide to the `-i`and`-b`parameters contain no volume name or directory names that contain any space characters or other white space characters. If there is a space, the installation fails.
- 
                `--install-dir`or`-i`– This option specifies the directory to copy all of the files to.The default value is `/usr/local/aws-cli`.
- 
                `--bin-dir`or`-b`– This option specifies that the main`aws`program in the install directory is symbolically linked to the file`aws`in the specified path. You must have write permissions to the specified directory. Creating a symlink to a directory that is already in your path eliminates the need to add the install directory to the user's`$PATH`variable.The default value is `/usr/local/bin`.
 `$``./aws/install -i``/usr/local/aws-cli`-b`/usr/local/bin`###### NoteTo update your current installation of the AWS CLI version 2 to a newer version, add your existing symlink and installer information to construct the `install`command with the`--update`parameter.`$``sudo ./aws/install --bin-dir``/usr/local/bin`--install-dir`/usr/local/aws-cli`--updateTo locate the existing symlink and installation directory, use the following steps: - 
                  Use the `which`command to find your symlink. This gives you the path to use with the`--bin-dir`parameter.`$``which aws``/usr/local/bin`/aws
- 
                  Use the `ls`command to find the directory that your symlink points to. This gives you the path to use with the`--install-dir`parameter.`$``ls -l /usr/local/bin/aws``lrwxrwxrwx 1 ec2-user ec2-user 49 Oct 22 09:49 /usr/local/bin/aws ->``/usr/local/aws-cli`/v2/current/bin/aws
 
- 
                
- 
            Confirm the installation with the following command. `$``aws --version``aws-cli/2.27.41 Python/3.11.6 Linux/5.10.205-195.807.amzn2.x86_64`If the `aws`command cannot be found, you might need to restart your terminal or follow the troubleshooting in[Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

### Installation requirements

- 
            You know which release of the AWS CLI version 2 you'd like to install. For a list of versions, see the [AWS CLI version 2 Changelog](https://github.com/aws/aws-cli/blob/v2/CHANGELOG.rst?plain=1)on*GitHub*.
- 
            We support the AWS CLI version 2 on Apple-supported versions of 64-bit macOS. 
- 
            Because AWS doesn't maintain third-party repositories, we can’t guarantee that they contain the latest version of the AWS CLI. 

### Installation instructions

You can install the AWS CLI version 2 on macOS in the following ways.

### Installation requirements

- 
            You know which release of the AWS CLI version 2 you'd like to install. For a list of versions, see the [AWS CLI version 2 Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst)on*GitHub*.
- 
            We support the AWS CLI on Microsoft-supported versions of 64-bit Windows. 
- 
            Admin rights to install software 

### Installation instructions

To update your current installation of AWS CLI version 2 on Windows, download a new installer
          each time you update to overwrite previous versions. AWS CLI is updated regularly. To see
          when the latest version was released, see the [AWS CLI version 2
            Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst) on 

*GitHub*.

- 
            Download and run the AWS CLI MSI installer for Windows (64-bit) in one of the following ways: - 
                **Downloading and running the MSI installer:**To create your download link for a specific version of the AWS CLI, append a hyphen and the version number to the filename.`https://awscli.amazonaws.com/AWSCLIV2-``version.number`.msiFor this example the filename for version `2.0.30`would be`AWSCLIV2-2.0.30.msi`resulting in the following link:[https://awscli.amazonaws.com/AWSCLIV2-2.0.30.msi](https://awscli.amazonaws.com/AWSCLIV2-2.0.30.msi).
- 
                **Using the msiexec command:**Alternatively, you can use the MSI installer by adding the link to the`msiexec`command. For a specific version of the AWS CLI, append a hyphen and the version number to the filename.`C:\>``msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2-``version.number`.msiFor this example the filename for version `2.0.30`would be`AWSCLIV2-2.0.30.msi`resulting in the following link[https://awscli.amazonaws.com/AWSCLIV2-2.0.30.msi](https://awscli.amazonaws.com/AWSCLIV2-2.0.30.msi).`C:\>``msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2-2.0.30.msi`For various parameters that can be used with `msiexec`, see[msiexec](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec)on the*Microsoft Docs*website.
 For a list of versions, see the [AWS CLI version 2 Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst)on*GitHub*.
- 
                
- 
            To confirm the installation, open the **Start**menu, search for`cmd`to open a command prompt window, and at the command prompt use the`aws --version`command.`C:\>``aws --version``aws-cli/2.27.41 Python/3.11.6 Windows/10 exe/AMD64 prompt/off`If Windows is unable to find the program, you might need to close and reopen the command prompt window to refresh the path, or follow the troubleshooting in [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html).

## Troubleshooting AWS CLI install and uninstall errors

    If you come across issues after installing or uninstalling the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for troubleshooting steps. For the most relevant
      troubleshooting steps, see [Command not found errors](./cli-chap-troubleshooting.html#tshoot-install-not-found), [The "aws --version" command returns a different version than you installed](./cli-chap-troubleshooting.html#tshoot-install-wrong-version), and [The "aws --version" command returns a version after uninstalling the AWS CLI](./cli-chap-troubleshooting.html#tshoot-uninstall-1).

## Next steps

    After completing the steps in [Prerequisites to use the AWS CLI version 2](./getting-started-prereqs.html) and installing the
      AWS CLI, you should perform a [Setting up the AWS CLI](./getting-started-quickstart.html).