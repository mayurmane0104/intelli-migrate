# Hardware and Software Requirements | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/mule-runtime/latest/hardware-and-software-requirements](https://docs.mulesoft.com/mule-runtime/latest/hardware-and-software-requirements)

---

JDK

# Hardware and Software Requirements

If you plan to install Mule and run it on-premises, review these minimum hardware and software requirements before you install.

## Minimum Hardware Requirements

- 
2 GHz CPU or 1 virtual CPU in virtualized environments. 
- 
1 GB of RAM. 
- 
4 GB of storage. 

Adjust RAM to match your latency requirements and the size and number of simultaneous messages that applications process.

Mule supports the x86 and x64 architectures.

## Required Software

Verify that you use a supported version of Java before you install Mule.

| Software | Version | 
|---|---|
| JDK 17 | 

| Though you can run a different JDK of choice, MuleSoft doesn’t support or take action to fix issues if they’re traced back to the JDK. | 

## Supported Software

Mule is supported on any operating system that runs a Java Runtime Environment (JRE) from a supported JDK.

### Tested Software

Mule runtime engine passed functional testing against these software and operating systems:

| Software | Version | 
|---|---|
| OS | MacOS 10.15, Windows Server 2019, Windows 10, Red Hat Enterprise Linux 9.4, Ubuntu Server 20.04 | 
| JDK | Adoptium OpenJDK distribution | 

This version of Mule runtime engine is bundled with the Runtime Manager agent plugin version 2.7.14. For Runtime Manager Agent compatibility, see [Runtime Manager Agent Release Notes](../../release-notes/runtime-manager-agent/runtime-manager-agent-release-notes).