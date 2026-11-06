# Building and installing the AWS CLI from source - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/getting-started-source-install.html](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-source-install.html)

---

This topic describes how to install or update from source to the latest release of the AWS Command Line Interface (AWS CLI) on supported operating systems.

For information on the latest releases of AWS CLI, see the [AWS CLI version 2 Changelog](https://raw.githubusercontent.com/aws/aws-cli/v2/CHANGELOG.rst)
    on GitHub.

###### Important

AWS CLI versions 1 and 2 use the same `aws` command name. If you previously
      installed AWS CLI version 1, see [Migration guide for the AWS CLI version 2](./cliv2-migration.html).

###### Topics

## Why build from source?

    The AWS CLI is [available as pre-built
        installers](./getting-started-install.html) for most platforms and environments as well as a Docker image. 

Generally, these installers provide coverage for most use-cases. The instructions for installing from source are to help with the use-cases our installers do not cover. Some of these use-cases include the following:

- 
        The pre-built installers do not support your environment. For example, ARM 32-bit is not supported by the pre-built installers. 
- 
        The pre-built installers have dependencies your environment lacks. For example, Alpine Linux uses `musl``glibc`causing the pre-built installers to not immediately work.
- 
        The pre-built installers require resources your environment restricts access to. For example, security hardened systems might not give permissions to shared memory. This is needed for the frozen `aws`installer.
- 
        The pre-built installers are often blockers for maintainers in package managers, as full control over the building process for code and packages is preferred. Building from source enables distribution maintainers a more streamlined process to keep the AWS CLI updated. Enabling maintainers provides customers more up-to-date versions of the AWS CLI when installing from a 3rd party package manager such as `brew`,`yum`, and`apt`.
- 
        Customers that patch AWS CLI functionality require building and installing the AWS CLI from source. This is especially important for community members that want to test changes they've made to the source prior to contributing the change to the AWS CLI GitHub repository. 

## Quicksteps

    ###### Note

All code examples are assumed to run from the root of the source directory.

To build and install the AWS CLI from source, follow the steps in this section. The AWS CLI
      leverages [GNU
        Autotools](https://www.gnu.org/software/automake/faq/autotools-faq.html) to install from source. In the simplest case, the AWS CLI can be installed
      from source by running the default example commands from the root of the AWS CLI GitHub
      repository.

- 
        [Setup all requirements for your environment.](#source-getting-started-install-reqs)This includes being able to run[GNU Autotools](https://www.gnu.org/software/automake/faq/autotools-faq.html)generated files and Python 3.8 or later is installed.
- 
        In your terminal, navigate to the top level of the AWS CLI source folder and run the `./configure`command. This command checks the system for all required dependencies and generates a`Makefile`for building and installing the AWS CLI based on detected and specified configurations.The following `./configure`command example sets the build configuration for the AWS CLI using default settings.`$``./configure`For details, available configuration options, and default setting information, see the [Step 2: Configuring the AWS CLI source installation](#source-getting-started-install-config)section.
- 
        Run the `make`command. This command builds the AWS CLI according to your configuration settings.The following `make`command example builds with default options using your existing`./configure`settings.`$``make`For details and available build options, see the [Step 3: Building the AWS CLI](#source-getting-started-install-build)section.
- 
        Run the `make install`command. This command installs your built AWS CLI to the configured location on your system.The following `make install`command example installs your built AWS CLI and creates symlinks in your configured locations using default command settings.`$``make install`For details and available install options, see the [Step 4: Installing the AWS CLI](#source-getting-started-install-instructions)section.
- 
        Confirm the AWS CLI successfully installed using the following command: `$``aws --version``aws-cli/2.27.41 Python/3.11.6 Windows/10 exe/AMD64 prompt/off`For troubleshooting steps for install errors see the [Troubleshooting AWS CLI install and uninstall errors](#source-install-tshoot)section.

## Step 1: Setup all requirements

    To build the AWS CLI from source you need the following completed beforehand:

###### Note

All code examples are assumed to run from the root of the source directory.

- Download the AWS CLI source by either forking the AWS CLI GitHub repository or downloading the source tarball. The instructions is one of the following: - 
            Fork and clone the [AWS CLI repository](https://github.com/aws/aws-cli)from*GitHub*. For more information, see[Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo)in the*GitHub Docs*.
- 
            Download the latest source tarball at [https://awscli.amazonaws.com/awscli.tar.gz](https://awscli.amazonaws.com/awscli.tar.gz)extract the contents using the following commands:`$``curl "https://awscli.amazonaws.com/awscli.tar.gz" -o "awscli.tar.gz"``$``tar -xzf awscli.tar.gz`###### NoteTo download a specific version, use the following link format: [https://awscli.amazonaws.com/awscli-](https://awscli.amazonaws.com/awscli.tar.gz)`versionnumber`.tar.gzFor example, for version 2.10.0 the link is the following: [https://awscli.amazonaws.com/awscli-](https://awscli.amazonaws.com/awscli.tar.gz)`2.10.0`.tar.gzSource versions are available starting with version **2.10.0**of the AWS CLI.**(Optional) Verifying the integrity of your downloaded zip file by completing the following steps:**- 
                You can use the following steps to verify the signatures by using the `GnuPG`tool.The AWS CLI installer package `.zip`files are cryptographically signed using PGP signatures. If there is any damage or alteration of the files, this verification fails and you should not proceed with installation.
- 
                Download and install the `gpg`command using your package manager. For more information about`GnuPG`, see the[GnuPG website](https://www.gnupg.org/).
- 
                To create the public key file, create a text file and paste in the following text. `-----BEGIN PGP PUBLIC KEY BLOCK----- mQINBF2Cr7UBEADJZHcgusOJl7ENSyumXh85z0TRV0xJorM2B/JL0kHOyigQluUG ZMLhENaG0bYatdrKP+3H91lvK050pXwnO/R7fB/FSTouki4ciIx5OuLlnJZIxSzx PqGl0mkxImLNbGWoi6Lto0LYxqHN2iQtzlwTVmq9733zd3XfcXrZ3+LblHAgEt5G TfNxEKJ8soPLyWmwDH6HWCnjZ/aIQRBTIQ05uVeEoYxSh6wOai7ss/KveoSNBbYz gbdzoqI2Y8cgH2nbfgp3DSasaLZEdCSsIsK1u05CinE7k2qZ7KgKAUIcT/cR/grk C6VwsnDU0OUCideXcQ8WeHutqvgZH1JgKDbznoIzeQHJD238GEu+eKhRHcz8/jeG 94zkcgJOz3KbZGYMiTh277Fvj9zzvZsbMBCedV1BTg3TqgvdX4bdkhf5cH+7NtWO lrFj6UwAsGukBTAOxC0l/dnSmZhJ7Z1KmEWilro/gOrjtOxqRQutlIqG22TaqoPG fYVN+en3Zwbt97kcgZDwqbuykNt64oZWc4XKCa3mprEGC3IbJTBFqglXmZ7l9ywG EEUJYOlb2XrSuPWml39beWdKM8kzr1OjnlOm6+lpTRCBfo0wa9F8YZRhHPAkwKkX XDeOGpWRj4ohOx0d2GWkyV5xyN14p2tQOCdOODmz80yUTgRpPVQUtOEhXQARAQAB tCFBV1MgQ0xJIFRlYW0gPGF3cy1jbGlAYW1hem9uLmNvbT6JAlQEEwEIAD4CGwMF CwkIBwIGFQoJCAsCBBYCAwECHgECF4AWIQT7Xbd/1cEYuAURraimMQrMRnJHXAUC aGveYQUJDMpiLAAKCRCmMQrMRnJHXKBYD/9Ab0qQdGiO5hObchG8xh8Rpb4Mjyf6 0JrVo6m8GNjNj6BHkSc8fuTQJ/FaEhaQxj3pjZ3GXPrXjIIVChmICLlFuRXYzrXc Pw0lniybypsZEVai5kO0tCNBCCFuMN9RsmmRG8mf7lC4FSTbUDmxG/QlYK+0IV/l uJkzxWa+rySkdpm0JdqumjegNRgObdXHAQDWlubWQHWyZyIQ2B4U7AxqSpcdJp6I S4Zds4wVLd1WE5pquYQ8vS2cNlDm4QNg8wTj58e3lKN47hXHMIb6CHxRnb947oJa pg189LLPR5koh+EorNkA1wu5mAJtJvy5YMsppy2y/kIjp3lyY6AmPT1posgGk70Z CmToEZ5rbd7ARExtlh76A0cabMDFlEHDIK8RNUOSRr7L64+KxOUegKBfQHb9dADY qqiKqpCbKgvtWlds909Ms74JBgr2KwZCSY1HaOxnIr4CY43QRqAq5YHOay/mU+6w hhmdF18vpyK0vfkvvGresWtSXbag7Hkt3XjaEw76BzxQH21EBDqU8WJVjHgU6ru+ DJTs+SxgJbaT3hb/vyjlw0lK+hFfhWKRwgOXH8vqducF95NRSUxtS4fpqxWVaw3Q V2OWSjbne99A5EPEySzryFTKbMGwaTlAwMCwYevt4YT6eb7NmFhTx0Fis4TalUs+ j+c7Kg92pDx2uQ== =OBAt -----END PGP PUBLIC KEY BLOCK-----`For reference, the following are the details of the public key. `Key ID: A6310ACC4672 Type: RSA Size: 4096/4096 Created: 2019-09-18 Expires: 2026-07-07 User ID: AWS CLI Team <aws-cli@amazon.com> Key fingerprint: FB5D B77F D5C1 18B8 0511 ADA8 A631 0ACC 4672 475C`
- 
                Import the AWS CLI public key with the following command, substituting `public-key-file-name`with the file name of the public key you created.`$``gpg --import``public-key-file-name``gpg: /home/``username`/.gnupg/trustdb.gpg: trustdb created gpg: key A6310ACC4672475C: public key "AWS CLI Team <aws-cli@amazon.com>" imported gpg: Total number processed: 1 gpg: imported: 1
- 
                Download the AWS CLI signature file for the package you downloaded at [https://awscli.amazonaws.com/awscli.tar.gz.sig](https://awscli.amazonaws.com/awscli.tar.gz.sig). It has the same path and name as the tarball file it corresponds to, but has the extension`.sig`. Save it in the same path as the tarball file. Or use the following command block:`$``curl awscliv2.sig https://awscli.amazonaws.com/ -o awscli.tar.gz.sig`
- 
                Verify the signature, passing both the downloaded `.sig`and`.zip`file names as parameters to the`gpg`command.`$``gpg --verify awscliv2.sig awscli.tar.gz`The output should look similar to the following. `gpg: Signature made Mon Nov 4 19:00:01 2019 PST gpg: using RSA key FB5D B77F D5C1 18B8 0511 ADA8 A631 0ACC 4672 475C gpg: Good signature from "AWS CLI Team <aws-cli@amazon.com>" [unknown] gpg: WARNING: This key is not certified with a trusted signature! gpg: There is no indication that the signature belongs to the owner. Primary key fingerprint: FB5D B77F D5C1 18B8 0511 ADA8 A631 0ACC 4672 475C`###### ImportantThe warning in the output is expected and doesn't indicate a problem. It occurs because there isn't a chain of trust between your personal PGP key (if you have one) and the AWS CLI PGP key. For more information, see [Web of trust](https://wikipedia.org/wiki/Web_of_trust).
 
- 
                
 
- 
            
- 
        You have an environment that can run [GNU Autotools](https://www.gnu.org/software/automake/faq/autotools-faq.html)generated files such as`configure`and`Makefile`. These files are widely portable across POSIX platforms.If Autotools is not already installed in your environment or you need to update them, then follow the installation instructions found in [How do I install the Autotools (as user)?](https://www.gnu.org/software/automake/faq/autotools-faq.html#How-do-I-install-the-Autotools-_0028as-user_0029_003f)or[Basic Installation](https://www.gnu.org/savannah-checkouts/gnu/automake/manual/automake.html#Basic-Installation)in the*GNU documentation*.
- 
        A Python 3.8 or later interpreter is installed. The minimum Python version required follows the same timelines as the official [Python support policy for AWS SDKs and Tools](https://aws.amazon.com/blogs/developer/python-support-policy-updates-for-aws-sdks-and-tools/). An interpreter is only supported 6 months after its end-of-support date.
- 
        
        
        **(Optional)**Install all build and runtime Python library dependencies of the AWS CLI. The`./configure`command informs you if you are missing any dependencies and how to install them.You can automatically install and use these dependencies through configuration, see [Downloading dependencies](#source-getting-started-install-config-dependencies)for more information.

## Step 2: Configuring the AWS CLI source installation

    Configuration for building and installing the AWS CLI is specified using the
        `configure` script. For the documentation of all configuration options, run the
        `configure` script with the `--help` option:

`$``./configure --help`

###### The most important options are the following:

### Install location

The source installation of the AWS CLI uses two configurable directories to install the AWS CLI:

- 
          `libdir`- Parent directory where the AWS CLI will be installed. The path to the AWS CLI installation is`<libdir-value>`/aws-cli`libdir`value for Linux and macOS is`/usr/local/lib`making the default installation directory`/usr/local/lib`/aws-cli
- 
          `bindir`- Directory where the AWS CLI executables are installed. The default location is`/usr/local/bin`.

The following `configure` options control the directories used:

- 
          `--prefix`- Sets the directory prefix to use for the installation. The default value for Linux and macOS is`/usr/local`.
- 
          `--libdir`- Sets the`libdir`to use for installing the AWS CLI. The default value is`<prefix-value>/lib`. If both`--libdir`and`--prefix`are not specified, the default for Linux and macOS is`/usr/local/lib/`.
- 
          `--bindir`- Sets the`bindir`to use for installing the AWS CLI`aws`and`aws_completer`executables. The default value is`<prefix-value>/bin`. If both`bindir`and`--prefix`are not specified, the default for Linux and macOS is`/usr/local/bin/`.

The following command example uses the `--prefix` option to do a local
              user install of the AWS CLI. This command installs the AWS CLI in
                `$HOME/.local/lib/aws-cli` and the executables in
                `$HOME/.local/bin`:

`$``./configure``--prefix=$HOME/.local`

The following command example uses the `--libdir` option to install the
              AWS CLI as an add-on application in the `/opt` directory. This command
              installs the AWS CLI at `/opt/aws-cli` and the executables at their default
              location of `/usr/local/bin`.

`$``./configure``--libdir=/opt`

### Python interpreter

###### Note

It is highly recommended to specify the Python interpreter when installing for Windows.

The `./configure` script automatically selects an installed
        Python 3.8 or later interpreter to use in building and running the AWS CLI using the [ AM_PATH_PYTHON](https://www.gnu.org/software/automake/manual/html_node/Python.html) Autoconf macro.

The Python interpreter to use can be explicitly set using the `PYTHON`
        environment variable when running the `configure` script:

`$``PYTHON=``/path/to/python`./configure

### Downloading dependencies

By default, it is required that all build and runtime dependencies of the AWS CLI are
        already installed on the system. This includes any Python library dependencies. All
        dependencies are checked when the `configure` script is run, and if the system is
        missing any Python dependencies, the `configure` script errors out. 

The following code example errors out when your system is missing dependencies:

`$``./configure``checking for a Python interpreter with version >= 3.8... python checking for python... /Users/username/.envs/env3.11/bin/python checking for python version... 3.11 checking for python platform... darwin checking for GNU default python prefix... ${prefix} checking for GNU default python exec_prefix... ${exec_prefix} checking for python script directory (pythondir)... ${PYTHON_PREFIX}/lib/python3.11/site-packages checking for python extension module directory (pyexecdir)... ${PYTHON_EXEC_PREFIX}/lib/python3.11/site-packages checking for --with-install-type... system-sandbox checking for --with-download-deps... Traceback (most recent call last): File "<frozen runpy>", line 198, in _run_module_as_main File "<frozen runpy>", line 88, in _run_code File "/Users/username/aws-code/aws-cli/./backends/build_system/__main__.py", line 125, in <module> main() File "/Users/username/aws-code/aws-cli/./backends/build_system/__main__.py", line 121, in main parsed_args.func(parsed_args) File "/Users/username/aws-code/aws-cli/./backends/build_system/__main__.py", line 49, in validate validate_env(parsed_args.artifact) File "/Users/username/aws-code/aws-cli/./backends/build_system/validate_env.py", line 68, in validate_env raise UnmetDependenciesException(unmet_deps, in_venv) validate_env.UnmetDependenciesException: Environment requires following Python dependencies: awscrt (required: ('>=0.12.4', '<0.17.0')) (version installed: None) We recommend using --with-download-deps flag to automatically create a virtualenv and download the dependencies. If you want to manage the dependencies yourself instead, run the following pip command: /Users/username/.envs/env3.11/bin/python -m pip install --prefer-binary 'awscrt>=0.12.4,<0.17.0' configure: error: "Python dependencies not met."`

To automatically install the required Python dependencies, use the
          `--with-download-deps` option. When using this flag, the build process does the
        following:

- 
          Skips the Python library dependencies check. 
- 
          Configures the settings to download all required Python dependencies and use **only**the downloaded dependencies to build the AWS CLI during the`make`build.

The following configure command example uses the `--with-download-deps`
        option to download and use the Python dependencies:

`$``./configure``--with-download-deps`

### Install type

The source install process supports the following installation types:

- 
          `system-sandbox`-**(Default)**Creates an isolated Python virtual environment, installs the AWS CLI into the virtual environment, and symlinks to the`aws`and`aws_completer`executable in the virtual environment. This install of the AWS CLI depends directly on the selected Python interpreter for its runtime.This is a lightweight install mechanism to get the AWS CLI installed on a system and follows best Python practices by sandboxing the installation in a virtual environment. This installation is intended for customers that want to install the AWS CLI from source in the most frictionless way possible with the installation coupled to your installation of Python. 
- 
          `portable-exe`- Freezes the AWS CLI into a standalone executable that can be distributed to environments of similar architectures. This is the same process used to generate the official pre-built executables of the AWS CLI. The`portable-exe`freezes in a copy of the Python interpreter chosen in the`configure`step to use for the runtime of the AWS CLI. This allows it to be moved to other machines that may not have a Python interpreter.This type of builds is useful because you can ensure your AWS CLI installation isn't coupled to the environment's installed Python version and you can distribute a build to other system that may not already have Python installed. This enables you to control the dependencies and security on the AWS CLI executables you use. 

To configure the installation type, use the `--with-install-type` option and
        specify a value of `portable-exe` or `system-sandbox`. 

The following `./configure` command example specifies a value of
          `portable-exe`:

`$``./configure``--with-install-type=portable-exe`

## Step 3: Building the AWS CLI

    Use the `make` command to build the AWS CLI using your configuration
      settings:

`$``make`

###### Note

###### When using the `make` command, the following steps are completed behind the scenes:

- 
            A virtual environment is created in the build directory using the Python `venv`[version of pip that is vendored in the Python standard library](https://docs.python.org/3/library/ensurepip.html).
- 
            Copies Python library dependencies. Depending on if the `--with-download-deps`flag is specified in the`configure`command, this step does one of the following:- 
                The `--with-download-deps`**is**specified. Python dependencies are pip installed. This includes`wheel`,`setuptools`, and all AWS CLI runtime dependencies. If you are building the`portable-exe`,`pyinstaller`is installed. These requirements are all specified in lock files generated from`pip-compile`
- 
                The `--with-download-deps`**is not**specified. Python libraries from the Python interpreter's site package plus any scripts (e.g.`pyinstaller`) are copied into the virtual environment being used for the build.
 
- 
                
- 
            Runs `pip install`directly on the AWS CLI codebase to do an offline, in-tree build and install of the AWS CLI into the build virtual environment. This install uses the pip flags[--no-build-isolation](https://pip.pypa.io/en/stable/cli/pip_install/#cmdoption-no-build-isolation),[--use-feature=in-tree-build](https://pip.pypa.io/en/stable/cli/pip_install/#local-project-installs),[--no-cache-dir](https://pip.pypa.io/en/stable/cli/pip_install/#caching), and`--no-index`
- 
            **(Optional)**If the`--install-type`is set to`portable-exe`in the`configure`command, builds a standalone executable using`pyinstaller`

## Step 4: Installing the AWS CLI

    The `make install` command installs your built AWS CLI to the configured location
      on the system. 

The following command example installs the AWS CLI using your configuration and build settings:

`$``make install`

The `make install` rule supports the [ DESTDIR](https://www.gnu.org/software/make/manual/html_node/DESTDIR.html#DESTDIR) variable. When specified, this variable prefixes the
      specified path to the already configured installation path when installing the AWS CLI. By
      default, no value is set for this variable. 

The following code example uses a `--prefix=/usr/local` flag for
            configuring an install location, and then alters that destination using
                `DESTDIR=` for the `/tmp/stage````
make
              install
```
 command. These commands result in the AWS CLI being installed at
                `/tmp/stage/`usr/local/lib/aws-cli`/tmp/stage/`usr/local/bin

`$``./configure --prefix=/usr/local``$``make``$``make DESTDIR=/tmp/stage install`

###### Note

###### When running `make install`, the following steps are completed behind the scenes

- 
            Moves one of the following to the configured install directory: - 
                If the install type is `system-sandbox`, moves your built virtual environment.
- 
                If the install type is a `portable-exe`, moves your built standalone executable.
 
- 
                
- 
            Creates symlinks for both the `aws`and`aws_completer`executables in your configured bin directory.

## Step 5: Verifying the AWS CLI installation

    Confirm the AWS CLI successfully installed by using the following command:

`$``aws --version``aws-cli/2.27.41 Python/3.11.6 Windows/10 exe/AMD64 prompt/off`

If the `aws` command is not recognized, you may need to restart your terminal
      for new symlinks to update. If you come across additional issues after installing or
      uninstalling the AWS CLI, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for common
      troubleshooting steps

## Workflow examples

    This section provides some basic workflow examples for installing from source.

### Basic Linux and macOS install

The following example is a basic installation workflow where the AWS CLI is installed in
        the default location of `/usr/local/lib/aws-cli`. 

`$``cd``path/to/cli/respository/``$``./configure``$``make``$``make install`

### Automated Windows install

###### Note

You must run PowerShell as an Administrator to use this workflow.

MSYS2 can be used in an automated fashion in a CI setting, see [Using MSYS2 in CI](https://www.msys2.org/docs/ci/) in the 

*MSYS2 Documentation*.

Download the `awscli.tar.gz` file, extract, and
              install the AWS CLI. When using the following commands, replace the following
              paths:

- 
                `C:\msys64\usr\bin\bash`with the location of your MSYS2 path.
- 
                `.\awscli-2.x.x\`with the extracted`awscli.tar.gz`folder name.
- 
                `PYTHON='C:\path\to\python.exe'`with your local Python path.

The following code example automates building and installing the AWS CLI from PowerShell using MSYS2, and specifies which local install of Python to use:

`PS C:\>``curl "https://awscli.amazonaws.com/awscli.tar.gz" -o "awscliv2.zip"``# Download the awscli.tar.gz file in the current working directory``PS C:\>``tar -xvzf .\awscli.tar.gz``# Extract awscli.tar.gz file``PS C:\>``cd``.\awscli-2.x.x\``# Navigate to the root of the extracted files``PS C:\>``$env:CHERE_INVOKING = 'yes'``# Preserve the current working directory``PS C:\>``C:\msys64\usr\bin\bash`-lc " PYTHON='`C:\path\to`\python.exe' ./configure --prefix='C:\Program Files\AWSCLI' --with-download-deps "`PS C:\>``C:\msys64\usr\bin\bash -lc "make"``PS C:\>``C:\msys64\usr\bin\bash -lc "make install"``PS C:\>``$Env:PATH +=";C:\Program Files\AWSCLI\bin\"``PS C:\>``aws --version``aws-cli/2.27.41 Python/3.11.6 Windows/10 source-sandbox/AMD64`

### Alpine Linux container

Below is an example Dockerfile that can be used to get a working installation of the
        AWS CLI in an Alpine Linux container as an [alternative to pre-built binaries for
          Alpine](https://github.com/aws/aws-cli/issues/4685). When using this example, replace 

`AWSCLI_VERSION`
        with you desired AWS CLI version number:```
FROM python:3.8-alpine AS builder
ENV AWSCLI_VERSION=2.10.1
RUN apk add --no-cache \
    curl \
    make \
    cmake \
    gcc \
    g++ \
    libc-dev \
    libffi-dev \
    openssl-dev \
    && curl https://awscli.amazonaws.com/awscli-${AWSCLI_VERSION}.tar.gz | tar -xz \
    && cd awscli-${AWSCLI_VERSION} \
    && ./configure --prefix=/opt/aws-cli/ --with-download-deps \
    && make \
    && make install
FROM python:3.8-alpine
RUN apk --no-cache add groff
COPY --from=builder /opt/aws-cli/ /opt/aws-cli/
ENTRYPOINT ["/opt/aws-cli/bin/aws"]
```
This image is built and the AWS CLI invoked from a container similar to the one that is built on Amazon Linux 2:

`$``docker build --tag awscli-alpine .``$``docker run --rm -it awscli-alpine --version``aws-cli/2.2.1 Python/3.8.11 Linux/5.10.25-linuxkit source-sandbox/x86_64.alpine.3 prompt/off`

The final size of this image is smaller than the size of the official AWS CLI Docker
        image. For information on the official Docker image, see [Running the official Amazon ECR Public or Docker images for the AWS CLI](./getting-started-docker.html).

## Troubleshooting AWS CLI install and uninstall errors

    For troubleshooting steps for install errors, see [Troubleshooting errors for the AWS CLI](./cli-chap-troubleshooting.html) for common troubleshooting steps. For the most relevant troubleshooting steps, see [Command not found errors](./cli-chap-troubleshooting.html#tshoot-install-not-found), [The "aws --version" command returns a different version than you installed](./cli-chap-troubleshooting.html#tshoot-install-wrong-version), and
        [The "aws --version" command returns a version after uninstalling the AWS CLI](./cli-chap-troubleshooting.html#tshoot-uninstall-1).

For any issues not covered in the troubleshooting guides, search the issues with the
        `source-distribution` label in the [AWS CLI Repository](https://github.com/aws/aws-cli/labels/source-distribution) on
        

*GitHub*. If no existing issues cover your errors,

[create a new issue](https://github.com/aws/aws-cli/issues/new?assignees=&labels=source-distribution%2Cneeds-triage&template=source-distribution.yml&title=%28short+issue+description%29)to receive help from the AWS CLI maintainers.

## Next steps

    After installing the AWS CLI, you should perform a [Setting up the AWS CLI](./getting-started-quickstart.html).