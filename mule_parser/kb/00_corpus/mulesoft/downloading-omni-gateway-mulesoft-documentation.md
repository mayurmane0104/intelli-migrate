# Downloading Omni Gateway | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/gateway/latest/flex-install](https://docs.mulesoft.com/gateway/latest/flex-install)

---

![20%](_images/install-linux-logo.png)


# Downloading Omni Gateway

Download and install Omni Gateway as a Linux service, or download the Omni Gateway image from the container registry. Downloading is a prerequisite to registering and running a gateway as a Linux service or in a container, Kubernetes cluster, or OpenShift cluster.

To run Omni Gateway inside a virtual machine (VM), download and install it as a Linux service. To run Omni Gateway in a container, Kubernetes cluster, or OpenShift cluster, download the Omni Gateway image.

| 
 | 
 | 
 | |

See [Requirements and Limits for Omni Gateway](flex-review-prerequisites) for details about hardware and software requirements.

## Download and Install as a Linux Service

You can download and install Omni Gateway as a service in one of the following Linux environments:

![2%](_images/install-ubuntu-logo.png) Ubuntu

 Ubuntu

## Download and install Omni Gateway as an Ubuntu service

##### Software Requirements

Omni Gateway runs on the following Long Term Support (LTS) versions of Ubuntu:

- 
Ubuntu Jammy 

##### Before You Begin

Before getting started, ensure that you have installed the following:

- 
[gnupg2](https://gnupg.org/)
- 
[lsb_release](https://refspecs.linuxfoundation.org/LSB_3.0.0/LSB-PDA/LSB-PDA/lsbrelease.html)

##### Run Installation Commands

To download and install Omni Gateway as a Ubuntu service, run the command block that performs the following actions:

- 
Retrieves the public package keys and adds the package repository 
- 
Updates the package list 
- 
Updates `apt-get`
- 
Installs the Omni Gateway package 

`curl -XGET https://flex-packages.anypoint.mulesoft.com/ubuntu/pubkey.gpg | sudo apt-key add - echo "deb [arch=amd64] https://flex-packages.anypoint.mulesoft.com/ubuntu $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/mulesoft.list sudo apt update sudo apt install -y flex-gateway`ssh

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).
For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

![2%](_images/install-debian-logo.png) Debian

 Debian

## Download and install Omni Gateway as a Debian service

##### Software Requirements

Omni Gateway runs on the following Long Term Support (LTS) versions of Debian:

- 
Debian Bookworm 

##### Before You Begin

Before getting started, ensure that you have installed the following:

- 
[gnupg2](https://gnupg.org/)
- 
[lsb_release](https://refspecs.linuxfoundation.org/LSB_3.0.0/LSB-PDA/LSB-PDA/lsbrelease.html)

##### Run Installation Commands

To download and install Omni Gateway as a Debian service, run the command block that performs the following actions:

- 
Retrieves the public package keys and adds the package repository 
- 
Updates the package list 
- 
Updates `apt-get`
- 
Installs the Omni Gateway package 

`curl -XGET https://flex-packages.anypoint.mulesoft.com/debian/pubkey.gpg | sudo apt-key add - echo "deb [arch=amd64] https://flex-packages.anypoint.mulesoft.com/debian $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/mulesoft.list sudo apt update sudo apt install -y flex-gateway`ssh

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).
For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

![2%](_images/install-amazon-linux-logo.png) Amazon Linux

 Amazon Linux

## Download and install Omni Gateway as an Amazon Linux service

##### Software Requirements

Omni Gateway runs on the following Long Term Support (LTS) version of Amazon Linux:

- 
Amazon Linux 2023 

##### Before You Begin

Before getting started, ensure that you have installed the following:

- 
[gnupg2](https://gnupg.org/)

##### Run Installation Commands

To download and install Omni Gateway as an Amazon Linux service, run the command block that performs the following actions:

- 
Adds the Omni Gateway package repository with a reference to its public key 
- 
Installs the Omni Gateway package 

`sudo tee /etc/yum.repos.d/flex-gateway.repo <<\EOF [flex-gateway] name = Anypoint Flex Gateway baseurl = https://flex-packages.anypoint.mulesoft.com/amazonlinux/2023/main gpgcheck=1 gpgkey=https://flex-packages.anypoint.mulesoft.com/amazonlinux/pubkey.gpg repo_gpgcheck=1 enabled=1 EOF sudo yum install -y flex-gateway`ssh

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).
For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

![2%](_images/install-rhel-logo.png) Red Hat Enterprise Linux

 Red Hat Enterprise Linux

## Download and install Omni Gateway as a Red Hat Enterprise Linux service

##### Software Requirements

Omni Gateway runs on the following Long Term Support (LTS) versions of RHEL:

- 
Red Hat Enterprise Linux (9) 

##### Before You Begin

Before getting started, ensure that you have installed the following:

- 
[gnupg2](https://gnupg.org/)

##### Run Installation Commands

To download and install Omni Gateway as a Red Hat Enterprise Linux service, run the command block that performs the following actions:

- 
Adds the Omni Gateway package repository with a reference to its public key 
- 
Installs the Omni Gateway package 

`sudo tee /etc/yum.repos.d/flex-gateway.repo <<\EOF [flex-gateway] name = Anypoint Flex Gateway baseurl = https://flex-packages.anypoint.mulesoft.com/rhel/$releasever/main gpgcheck=1 gpgkey=https://flex-packages.anypoint.mulesoft.com/rhel/pubkey.gpg repo_gpgcheck=1 enabled=1 EOF sudo yum install -y flex-gateway`ssh

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).
For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

![6%](_images/install-rhel-ibm-logo.png) Red Hat Enterprise Linux on IBM Power

 Red Hat Enterprise Linux on IBM Power

## Download and install Omni Gateway as a Red Hat Enterprise Linux service on IBM Power

##### Software Requirements

Omni Gateway runs on the following Long Term Support (LTS) versions:

- 
Red Hat Enterprise Linux (9) on IBM Power (ppc64le) 

##### Before You Begin

Before getting started, ensure that you have installed the following:

- 
[gnupg2](https://gnupg.org/)

##### Run Installation Commands

To download and install Omni Gateway as a Red Hat Enterprise Linux service, run the command block that performs the following actions:

- 
Adds the Omni Gateway package repository with a reference to its public key 
- 
Installs the Omni Gateway package 

`sudo tee /etc/yum.repos.d/flex-gateway.repo <<\EOF [flex-gateway] name = Anypoint Flex Gateway baseurl = https://flex-packages.anypoint.mulesoft.com/rhel/$releasever/main gpgcheck=1 gpgkey=https://flex-packages.anypoint.mulesoft.com/rhel/pubkey.gpg repo_gpgcheck=1 enabled=1 EOF sudo yum install -y flex-gateway`ssh

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).
For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

![2%](_images/install-centos-logo.png) CentOS

 CentOS

## Download and install Omni Gateway as a CentOS service

##### Software Requirements

Omni Gateway runs on the following Long Term Support (LTS) version of CentOS:

- 
CentOS 8 

##### Before You Begin

Before getting started, ensure that you have installed the following:

- 
[gnupg2](https://gnupg.org/)

##### Run Installation Commands

To download and install Omni Gateway as an CentOS service, run the command block that performs the following actions:

- 
Adds the Omni Gateway package repository with a reference to its public key 
- 
Installs the Omni Gateway package 

`sudo tee /etc/yum.repos.d/flex-gateway.repo <<\EOF [flex-gateway] name = Anypoint Flex Gateway baseurl = https://flex-packages.anypoint.mulesoft.com/centos/$releasever/main gpgcheck=1 gpgkey=https://flex-packages.anypoint.mulesoft.com/centos/pubkey.gpg repo_gpgcheck=1 enabled=1 EOF sudo yum install -y flex-gateway`ssh

Due to issues with the CentOS package manager you might encounter the following error:

Error: Failed to download metadata for repo 'AppStream': Cannot prepare internal mirrorlist: No URLs in mirrorlist

If you encounter this error, run the following command:

`sudo sed -i -e "s|mirrorlist=|#mirrorlist=|g" -e "s|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g" /etc/yum.repos.d/CentOS-*`ssh

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).
For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

## Download Omni Gateway for Use in a Container

You can download and install Omni Gateway in one of the following containers:

![2%](_images/install-docker-logo.png) Docker

 Docker

## Download Omni Gateway for Use in a Docker Container

Download the Omni Gateway container image to prepare for registering and running a gateway in a Docker container:

- 
Download the Omni Gateway Docker image: `docker pull mulesoft/flex-gateway:latest`ssh
- 
Verify that the download succeeded: `docker images mulesoft/flex-gateway`sshWhen successful, the command lists the Omni Gateway container image, for example: `REPOSITORY TAG mulesoft/flex-gateway latest`text

For deployments using Docker images, add the Omni Gateway Docker image to your Docker registry to ensure the image is available in the event of a Dockerhub outage.

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

![2%](_images/install-podman-logo.png) Podman

 Podman

## Download Omni Gateway for Use in a Podman Container

Download the Omni Gateway container image to prepare for registering and running a gateway in a Podman container:

- 
Download the Omni Gateway container image: `podman pull docker.io/mulesoft/flex-gateway:latest`ssh
- 
Verify that the download succeeded: `podman images docker.io/mulesoft/flex-gateway`sshWhen successful, the command lists the Omni Gateway container image, for example: `REPOSITORY TAG mulesoft/flex-gateway latest`text

For deployments using Docker images, add the Omni Gateway Docker image to your Docker registry to ensure the image is available in the event of a Dockerhub outage.

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

For more detail, see [Connected Mode vs. Local Mode](./#connected-mode-vs-local-mode).

## Download Omni Gateway for Use in a Kubernetes Cluster

Download the Omni Gateway container image to prepare for registering and running a gateway in a Kubernetes cluster. You can use the following container runtimes:

**Docker**

- 
Download the Omni Gateway container image: `docker pull mulesoft/flex-gateway:latest`ssh
- 
Verify that the download succeeded: `docker images mulesoft/flex-gateway`sshWhen successful, the command lists the Omni Gateway container image, for example: `REPOSITORY TAG mulesoft/flex-gateway latest`text

For deployments using Docker images, add the Omni Gateway Docker image to your Docker registry to ensure the image is available in the event of a Dockerhub outage.

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

After downloading the image, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

**Podman**

- 
Download the Omni Gateway container image: `podman pull docker.io/mulesoft/flex-gateway:latest`ssh
- 
Verify that the download succeeded: `podman images docker.io/mulesoft/flex-gateway`sshWhen successful, the command lists the Omni Gateway container image, for example: `REPOSITORY TAG mulesoft/flex-gateway latest`text

For deployments using Docker images, add the Omni Gateway Docker image to your Docker registry to ensure the image is available in the event of a Dockerhub outage.

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

After downloading the image, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

## Download Omni Gateway for Use in an OpenShift Cluster

Download the Omni Gateway container image to prepare for registering and running a gateway in an OpenShift cluster. You can use the following container runtimes:

**Docker**

- 
Download the Omni Gateway container image: `docker pull mulesoft/flex-gateway:latest`ssh
- 
Verify that the download succeeded: `docker images mulesoft/flex-gateway`sshWhen successful, the command lists the Omni Gateway container image, for example: `REPOSITORY TAG mulesoft/flex-gateway latest`text

For deployments using Docker images, add the Omni Gateway Docker image to your Docker registry to ensure the image is available in the event of a Dockerhub outage.

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

After downloading the image, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

**Podman**

- 
Download the Omni Gateway container image: `podman pull docker.io/mulesoft/flex-gateway:latest`ssh
- 
Verify that the download succeeded: `podman images docker.io/mulesoft/flex-gateway`sshWhen successful, the command lists the Omni Gateway container image, for example: `REPOSITORY TAG mulesoft/flex-gateway latest`text

For deployments using Docker images, add the Omni Gateway Docker image to your Docker registry to ensure the image is available in the event of a Dockerhub outage.

After downloading and installing, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).

After downloading the image, register Omni Gateway in
[Connected](flex-conn-reg-run) or [Local Mode](flex-local-reg-run).