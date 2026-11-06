# Set up kubectl and eksctl - Amazon EKS

**Source:** [https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html)

---

[Create a VPC and subnets for Amazon EKS local clusters on AWS Outposts configured with EC2 instance store](https://docs.aws.amazon.com/eks/latest/userguide/eks-outposts-instance-store-vpc-subnet-requirements.html)

*12 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

         **Help improve this page**
      

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

         **Help improve this page**
      

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

         [Register](https://aws-experience.com/emea/smb/events/series/get-hands-on-with-amazon-eks?trk=4a9b4147-2490-4c63-bc9f-f8a84b122c8c&sc_channel=el) for upcoming Amazon EKS workshops.

Once the AWS CLI is installed, there are two other tools you should install to create and manage your Kubernetes clusters:

            `kubectl`: The `kubectl` command line tool is the main tool you will use to manage resources within your Kubernetes cluster. This page describes how to download and set up the `kubectl` binary that matches the version of your Kubernetes cluster. See [Install or update kubectl](#kubectl-install-update).

            `eksctl`: The `eksctl` command line tool is made for creating EKS clusters in the AWS cloud or on-premises (with EKS Anywhere), as well as modifying and deleting those clusters. See [Install eksctl](#eksctl-install-update).

`kubectl`This topic helps you to download and install, or update, the `kubectl` binary on your device. The binary is identical to the [upstream community versions](https://kubernetes.io/docs/tasks/tools/#kubectl). The binary is not unique to Amazon EKS or AWS. Use the steps below to get the specific version of 

`kubectl` that you need, although many builders simply run `brew install kubectl` to install it.You must use a `kubectl` version that is within one minor version difference of your Amazon EKS cluster control plane. For example, a `1.35`
            `kubectl` client works with Kubernetes `1.34`, `1.35`, and `1.36` clusters.

You can also use `kubectl` directly from the EKS console via AWS CloudShell. Choose **Connect** on any cluster details page to get a pre-configured session. For more information, see [Connect kubectl to an EKS cluster by creating a kubeconfig file](./create-kubeconfig.html).

`kubectl` is installedDetermine whether you already have `kubectl` installed on your device.

`kubectl version --client`

If you have `kubectl` installed in the path of your device, the example output includes information similar to the following. If you want to update the version that you currently have installed with a later version, complete the next step, making sure to install the new version in the same location that your current version is in.

`Client Version: v1.31.X-eks-1234567`

If you receive no output, then you either don’t have `kubectl` installed, or it’s not installed in a location that’s in your device’s path.

`kubectl`Install or update `kubectl` on one of the following operating systems:

If downloads are slow to your AWS Region from the AWS Regions used in this section,
consider setting up CloudFront to front the content.
For further information, see [Get started with a basic CloudFront distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/GettingStartedSimpleDistributon.html).

Follow the steps below to install `kubectl` on macOS. The steps include:

Choosing and downloading the binary for the Kubernetes version you want.

Optionally checking the binary’s checksum.

Adding execute to the binary’s permissions.

Copying the binary to a folder in your PATH.

Optionally adding the binary’s directory to your PATH.

Procedure:

Download the binary for your cluster’s Kubernetes version from Amazon S3.

Kubernetes `1.35`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/darwin/amd64/kubectl`

Kubernetes `1.34`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/darwin/amd64/kubectl`

Kubernetes `1.33`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/darwin/amd64/kubectl`

Kubernetes `1.32`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/darwin/amd64/kubectl`

Kubernetes `1.31`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/darwin/amd64/kubectl`

Kubernetes `1.30`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/darwin/amd64/kubectl`

(Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.

Download the `SHA-256` checksum for your cluster’s Kubernetes version.

Kubernetes `1.35`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/darwin/amd64/kubectl.sha256`

Kubernetes `1.34`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/darwin/amd64/kubectl.sha256`

Kubernetes `1.33`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/darwin/amd64/kubectl.sha256`

Kubernetes `1.32`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/darwin/amd64/kubectl.sha256`

Kubernetes `1.31`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/darwin/amd64/kubectl.sha256`

Kubernetes `1.30`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/darwin/amd64/kubectl.sha256`

Check the `SHA-256` checksum for your downloaded binary.

`openssl sha1 -sha256 kubectl`

Make sure that the generated checksum in the output matches the checksum in the downloaded `kubectl.sha256` file.

Apply execute permissions to the binary.

`chmod +x ./kubectl`

Copy the binary to a folder in your `PATH`. If you have already installed a version of `kubectl`, then we recommend creating a `$HOME/bin/kubectl` and ensuring that `$HOME/bin` comes first in your `$PATH`.

`mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH`(Optional) Add the `$HOME/bin` path to your shell initialization file so that it is configured when you open a shell.

`echo 'export PATH=$HOME/bin:$PATH' >> ~/.bash_profile`Follow the steps below to install `kubectl` on Linux (amd64). The steps include:

Choosing and downloading the binary for the Kubernetes version you want.

Optionally checking the binary’s checksum.

Adding execute to the binary’s permissions.

Copying the binary to a folder in your PATH.

Optionally adding the binary’s directory to your PATH.

Procedure:

Download the `kubectl` binary for your cluster’s Kubernetes version from Amazon S3.

Kubernetes `1.35`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/linux/amd64/kubectl`

Kubernetes `1.34`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/linux/amd64/kubectl`

Kubernetes `1.33`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/linux/amd64/kubectl`

Kubernetes `1.32`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/linux/amd64/kubectl`

Kubernetes `1.31`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/linux/amd64/kubectl`

Kubernetes `1.30`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/linux/amd64/kubectl`

(Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.

Download the `SHA-256` checksum for your cluster’s Kubernetes version from Amazon S3 using the command for your device’s hardware platform.

Kubernetes `1.35`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/linux/amd64/kubectl.sha256`

Kubernetes `1.34`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/linux/amd64/kubectl.sha256`

Kubernetes `1.33`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/linux/amd64/kubectl.sha256`

Kubernetes `1.32`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/linux/amd64/kubectl.sha256`

Kubernetes `1.31`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/linux/amd64/kubectl.sha256`

Kubernetes `1.30`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/linux/amd64/kubectl.sha256`

Check the `SHA-256` checksum for your downloaded binary with one of the following commands.

`sha256sum -c kubectl.sha256`

or

`openssl sha1 -sha256 kubectl`

For the first, you should see `kubectl: OK`, for the second, you can check that the generated checksum in the output matches the checksum in the downloaded `kubectl.sha256` file.

Apply execute permissions to the binary.

`chmod +x ./kubectl`

Copy the binary to a folder in your `PATH`. If you have already installed a version of `kubectl`, then we recommend creating a `$HOME/bin/kubectl` and ensuring that `$HOME/bin` comes first in your `$PATH`.

`mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH`(Optional) Add the `$HOME/bin` path to your shell initialization file so that it is configured when you open a shell.

This step assumes you are using the Bash shell; if you are using another shell, change the command to use your specific shell initialization file.

`echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc`Follow the steps below to install `kubectl` on Linux (arm64). The steps include:

Choosing and downloading the binary for the Kubernetes version you want.

Optionally checking the binary’s checksum.

Adding execute to the binary’s permissions.

Copying the binary to a folder in your PATH.

Optionally adding the binary’s directory to your PATH.

Procedure:

Download the `kubectl` binary for your cluster’s Kubernetes version from Amazon S3.

Kubernetes `1.35`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/linux/arm64/kubectl`

Kubernetes `1.34`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/linux/arm64/kubectl`

Kubernetes `1.33`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/linux/arm64/kubectl`

Kubernetes `1.32`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/linux/arm64/kubectl`

Kubernetes `1.31`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/linux/arm64/kubectl`

Kubernetes `1.30`
                     

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/linux/arm64/kubectl`

(Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.

Download the `SHA-256` checksum for your cluster’s Kubernetes version from Amazon S3 using the command for your device’s hardware platform.

Kubernetes `1.35`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/linux/arm64/kubectl.sha256`

Kubernetes `1.34`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/linux/arm64/kubectl.sha256`

Kubernetes `1.33`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/linux/arm64/kubectl.sha256`

Kubernetes `1.32`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/linux/arm64/kubectl.sha256`

Kubernetes `1.31`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/linux/arm64/kubectl.sha256`

Kubernetes `1.30`
                           

`curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/linux/arm64/kubectl.sha256`

Check the `SHA-256` checksum for your downloaded binary with one of the following commands.

`sha256sum -c kubectl.sha256`

or

`openssl sha1 -sha256 kubectl`

For the first, you should see `kubectl: OK`, for the second, you can check that the generated checksum in the output matches the checksum in the downloaded `kubectl.sha256` file.

Apply execute permissions to the binary.

`chmod +x ./kubectl`

Copy the binary to a folder in your `PATH`. If you have already installed a version of `kubectl`, then we recommend creating a `$HOME/bin/kubectl` and ensuring that `$HOME/bin` comes first in your `$PATH`.

`mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH`(Optional) Add the `$HOME/bin` path to your shell initialization file so that it is configured when you open a shell.

This step assumes you are using the Bash shell; if you are using another shell, change the command to use your specific shell initialization file.

`echo 'export PATH=$HOME/bin:$PATH' >> ~/.bashrc`Follow the steps below to install `kubectl` on Windows. The steps include:

Choosing and downloading the binary for the Kubernetes version you want.

Optionally checking the binary’s checksum.

Copying the binary to a folder in your PATH.

Optionally adding the binary’s directory to your PATH.

Procedure:

Open a PowerShell terminal.

Download the `kubectl` binary for your cluster’s Kubernetes version from Amazon S3.

Kubernetes `1.35`
                     

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/windows/amd64/kubectl.exe`

Kubernetes `1.34`
                     

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/windows/amd64/kubectl.exe`

Kubernetes `1.33`
                     

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/windows/amd64/kubectl.exe`

Kubernetes `1.32`
                     

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/windows/amd64/kubectl.exe`

Kubernetes `1.31`
                     

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/windows/amd64/kubectl.exe`

Kubernetes `1.30`
                     

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/windows/amd64/kubectl.exe`

(Optional) Verify the downloaded binary with the `SHA-256` checksum for your binary.

Download the `SHA-256` checksum for your cluster’s Kubernetes version for Windows.

Kubernetes `1.35`
                           

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.35.3/2026-04-08/bin/windows/amd64/kubectl.exe.sha256`

Kubernetes `1.34`
                           

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.34.6/2026-04-08/bin/windows/amd64/kubectl.exe.sha256`

Kubernetes `1.33`
                           

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.10/2026-04-08/bin/windows/amd64/kubectl.exe.sha256`

Kubernetes `1.32`
                           

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.32.13/2026-04-08/bin/windows/amd64/kubectl.exe.sha256`

Kubernetes `1.31`
                           

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.31.14/2026-04-08/bin/windows/amd64/kubectl.exe.sha256`

Kubernetes `1.30`
                           

`curl.exe -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.30.14/2026-04-08/bin/windows/amd64/kubectl.exe.sha256`

Check the `SHA-256` checksum for your downloaded binary.

`Get-FileHash kubectl.exe`

Make sure that the generated checksum in the output matches the checksum in the downloaded `kubectl.sha256` file. The PowerShell output should be an uppercase equivalent string of characters.

Copy the binary to a folder in your `PATH`. If you have an existing directory in your `PATH` that you use for command line utilities, copy the binary to that directory. Otherwise, complete the following steps.

Create a new directory for your command line binaries, such as `C:\bin`.

Copy the `kubectl.exe` binary to your new directory.

Edit your user or system `PATH` environment variable to add the new directory to your `PATH`.

Close your PowerShell terminal and open a new one to pick up the new `PATH` variable.

After you install `kubectl`, you can verify its version.

`kubectl version --client`

When first installing `kubectl`, it isn’t yet configured to communicate with any server. We will cover this configuration as needed in other procedures. If you ever need to update the configuration to communicate with a particular cluster, you can run the following command. Replace `region-code` with the AWS Region that your cluster is in. Replace `my-cluster` with the name of your cluster.

`aws eks update-kubeconfig --region region-code --name my-cluster`

Consider configuring auto completion, which lets you use the tab key to complete `kubectl` subcommands after typing the first few letters. See [Kubectl autocomplete](https://kubernetes.io/docs/reference/kubectl/quick-reference/#kubectl-autocomplete) in the Kubernetes documentation for details.

`eksctl`The `eksctl` CLI is used to work with EKS clusters. It automates many individual tasks. See [Installation](https://eksctl.io/installation) in the 

`eksctl` documentation for instructions on installing `eksctl`. For Linux, use the UNIX instructions.When using `eksctl` the IAM security principal that you’re using must have permissions to work with Amazon EKS IAM roles, service linked roles, AWS CloudFormation, a VPC, and related resources. For more information, see [Actions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonelastickubernetesservice.html) and [Using service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) in the IAM User Guide. You must complete all steps in this guide as the same user. To check the current user, run the following command:

`aws sts get-caller-identity`

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

EKS supports Kubernetes versions 14 months standard, then 12 months extended at added cost before auto-upgrade.

Configure kubectl EKS access via kubeconfig file using AWS CLI authentication or CloudShell console connection.

IRSA associates IAM roles Kubernetes service accounts, enabling least privilege Pod credential isolation via OIDC JWT tokens.