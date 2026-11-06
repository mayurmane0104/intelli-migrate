# Edge and LTS Releases for Mule | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/release-notes/mule-runtime/lts-edge-release-cadence](https://docs.mulesoft.com/release-notes/mule-runtime/lts-edge-release-cadence)

---

Edge

# Edge and LTS Releases for Mule

Starting with Mule 4.5, MuleSoft introduces two new release channels, Edge and Long-Term Support (LTS). Both release channels are available in all our deployment models: Anypoint Runtime Fabric, CloudHub, CloudHub 2.0, and Hybrid Standalone.

Release cadence refers to new Mule runtime versions. Patch updates for supported versions continue to follow the monthly patch update schedule.

Consider these factors to determine the approach that best suits your requirements ahead of the Mule 4.4 End of Standard Support.

| Channel Type | Release Cadence | Differentiators | Support Coverage | 
|---|---|---|---|
| Up to three times per year | 
 | For versions 4.9 and later: 
 For version 4.8: 
 For versions 4.5 to 4.7: 
 | |
| LTS | Periodic (Scheduled for February) | 
 | For version 4.6 and later: 
 | 

If an LTS version is released in February, both Edge and LTS share the same underlying version, including the same minor Mule runtime version and new features.

To review the new support policy that aligns with the new release periods and types of releases, see [MuleSoft Support Policy](https://www.salesforce.com/en-us/wp-content/uploads/sites/4/documents/legal/Agreements/versioning-back-support-policy.pdf).

| For information about the monthly patch update process, see [Update Patches to Mule](patching-mule-versions). | 

## Edge Channel

Starting with Mule 4.5, MuleSoft releases Edge versions up to three times a year. Use the Edge channel if you want to stay on top of the latest features and feel comfortable with a more frequent release cycle and auto-app upgrade cycle. The Edge channel includes the latest features and innovations available on the MuleSoft platform.

## LTS Channel

Starting with Mule 4.6, MuleSoft releases Long-Term Support (LTS) versions periodically, scheduled for February. If you’re on Mule 4.4, you aren’t required to upgrade to Mule 4.6. However, because Mule 4.5 was released in October 2023, Standard Support for Mule 4.4 ends in October 2024, followed by the end of Extended Support in October 2025. For CloudHub and CloudHub 2.0 customers, once Standard Support for Mule 4.4 ends, if you want to deploy new apps, you must do so on Mule 4.6 LTS or Mule 4.8 Edge. Use the LTS channel if you want to avoid maintaining new versions frequently. The LTS channel adopts new capabilities after they have been introduced via Edge releases.

## Switch from an Edge Version to an LTS Version

You can switch from an Edge version to an LTS version and vice versa. However, when moving from Edge to LTS, you must choose a later LTS version. For example, if you choose Mule 4.6 LTS and you want to implement a specific new feature released on Mule 4.7 Edge, you can opt into that Edge release, then merge into Mule 4.9 LTS once it is available. MuleSoft does not support apps that are switched from Edge to an older LTS version. For example, switching an app from Mule 4.7 Edge to Mule 4.6 LTS might result in losing some of the new features in the older LTS version.

## Mule Runtime Release Cadence Support

This table shows the Mule runtime release cadence support for each channel:

| Mule Version | Release Date | Java Version | End of Standard Support | End of Extended Support | 
|---|---|---|---|---|
| 4.12 Edge | June 2026 | 17 | November 2026 | February 2027 | 
| 4.11 Edge | February 2026 | 17 | July 2026 | October 2026 | 
| 4.10 Edge | October 2025 | 17 | March 2026 | June 2026 | 
| 4.9 LTS | February 2025 | 17 | August 2027 | February 2028 | 
| 4.9 Edge | February 2025 | 17 | November 2025 | February 2026 | 
| 4.8 Edge | October 2024 | 8, 11, and 17 | March 2025 | June 2025 | 
| 4.7 Edge | June 2024 | 8, 11, and 17 | October 2024 | February 2025 | 
| 4.6 LTS | February 2024 | 8, 11, and 17 | August 2026 | February 2027 | 
| 4.6 Edge | February 2024 | 8, 11, and 17 | June 2024 | October 2024 | 
| 4.5 Edge | October 2023 | 8 and 11 | February 2024 | June 2024 | 

| MuleSoft provides an extended support window for version 4.6 LTS due to its compatibility with Java 8, 11, and 17. | 

## Deployment Models and Application Lifecycle Management

Application lifecycle management depends on the deployment model.

| Action | CloudHub and CloudHub 2.0 | Runtime Fabric | Hybrid Standalone | 
|---|---|---|---|
| Deploy net new apps | Deploy to the latest minor-patch version available under Standard Support of each channel. | Deploy to any patch version of Mule runtime available under Standard or Extended Support. By default, the latest version of Mule runtime is selected. | Deploy while versions are in support period. | 
| Auto-upgrade | Patches: Monthly auto-patching upgrade when a new patch version is available, as long as the app’s TLS version is compatible with the new patch version. See patching schedule for  Runtime version compatibility: Apps running Mule runtime 4.9 or earlier aren’t auto-upgraded to Mule runtime 4.10 or later. Mule 4.10 removes support for TLS 1.0 and 1.1, which can cause compatibility issues and break existing applications if upgraded automatically. Apps on earlier versions (for example, 4.6) are auto-upgraded to the latest available patch version in the 4.9 release line. To use Mule runtime 4.10 or later, upgrade your application manually. Channels: All apps are auto-upgraded to the latest minor version within their respective channels (Edge or LTS) during the monthly patching schedule of the month when previous version goes out of Standard Support. 
 | Applications aren’t auto-upgraded by MuleSoft without customer-initiated actions. | No auto-upgrade capabilities | 
| Self-upgrade | The auto-upgrade takes place during a fixed patching schedule after the version’s standard support ends. See patching schedule for  
 | Always available | Using the  | 
| Rollback | Available to the previously used version | Available to the previously used version | Available to the previous used version using the  | 
| Restart apps | Always | Always | Always while the version is within the support period | 
| Keep running applications | Until End of Extended Support | Always | Always | 
| End of Extended Support | Shutdown running apps. | Cannot deploy new apps | Can deploy new apps | 
| Retirement | Mule apps don’t reach End of Life because they’re always auto-upgraded. | When Mule apps reach End of Life, you can still restart or redeploy them using the same runtime version the apps are currently running on. | When Mule apps reach End of Life, MuleSoft reserves the right to close the connection of the Mule runtime server to Anypoint Platform. | 
| Supportability | All Mule apps are under Standard Support. | Supported while Mule apps are within the assigned support period. | Supported while Mule apps are within the assigned support period. | 
| Redeployment / Applying changes / Upgrades | Supported until End of Extended Support. | Supported when a build tag is provided. If a build tag isn’t provided, the application defaults to the latest patch of the minor version being used. If a wrong, invalid, or unsupported build tag is provided, the deployment fails. | Supported under Hybrid Stansalone. | 

## Mule Runtime Version Naming Changes

The version naming convention depends on the deployment model you’re using. A version increments:

- 
MAJOR when a release includes features that introduce breaking changes and backward incompatibility. 
- 
MINOR when a release includes all new features keeping backward compatibility with previous minors. 
- 
PATCH when a release includes bug fixes and security updates that include upgrades to libraries with reported vulnerabilities. We build a new runtime and do a full validation test. 
- 
BUILD when a release includes changes related to Image/AMI, including OS changes, OS security updates, and changes in products outside the runtime. It doesn’t include any runtime changes. 

### Cloudhub, Cloudhub 2.0, and Runtime Fabric

The Mule runtime versioning schema for the new release channels is:

*Major[numeric] . Minor[numeric] . Patch[numeric] : Build[numeric] Channel[e for edge, nothing for LTS]*

Each February, MuleSoft releases both an Edge and an LTS release with the same *Major.Minor* version. To distinguish the versions, they’re represented as:

- 
Edge: 4.6.0:1e 
- 
LTS: 4.6.0:1 

Unlike the Hybrid Standalone customer profile, CloudHub, CloudHub 2.0, and Runtime Fabric require regular OS updates, hence the addition of the build enumeration in the full runtime version schema.

Here are examples of the version numbers:

- 
Edge: 4.5.0:1e 
- 
Edge: 4.6.0:1e 
- 
LTS: 4.6.0:1 

### Hybrid Standalone

The Mule runtime versioning changes from date-based, for example, `4.4.0-20230317` to semVer as:

*Major.Minor.Patch*

Here are examples of the version numbers:

- 
4.5.1 
- 
4.5.2 
- 
4.5.3 

Mule runtime does not introduce a semVer increment if there is a month with no fixes.

Here is an example of the versioning schema using different patch and builds:

| Hybrid Standalone | CloudHub - AMI / CloudHub 2.0 / Runtime Fabric - Docker image | ||||
|---|---|---|---|---|---|
| Case | Release Date | Description | Patch/Build | Mule Runtime | Runtime Manager/Maven/API Tag for New Deployment | 
| 1 | Oct 3, 2023 | First release of 4.5.0 | 0th patch and 1st build | 4.5.0 | 4.5.0:1e | 
| 2 | Nov 7, 2023 | Second release of 4.5 | 1st patch and 1st build | 4.5.1 | 4.5.1:1e | 
| 3 | Nov 7, 2023 | Another build on same day for CloudHub, CloudHub 2.0, and Runtime Fabric | 1st patch and 2nd build | Not Available | 4.5.1:2e | 
| 4 | Nov 7, 2023 | OS updates only for CloudHub, CloudHub 2.0, and Runtime Fabric | 1st patch and 3rd build | Not Available | 4.5.1:3e | 
| 5 | Dec 5, 2023 | Second patch version of 4.5 | 2nd patch and 1st build | 4.5.2 | 4.5.2:1e | 
| 6 | Jan 2, 2024 | Hot fix for a Mule runtime regression | 3rd patch & 1st build | 4.5.3 | 4.5.3:1e | 
| 7 | Feb 6, 2024 | Release of new minor | 0th patch and 1st build | 4.6.0 | 4.6.0:1e (Edge) / 4.6.0:1 (LTS) | 

The Mule runtime versioning schema uses these conventions:

- 
Patch number in schema - 
In the schema `4.5.X:2e`, the patch number is the X.
- 
The patch number starts from `0`, introducing a new minor version.
- 
The patch number increments when the release introduces new code changes, including hotfixes to regressions or other bug fixes. 
 
- 
- 
Build number in schema - 
In the schema `4.5.1:Ye`, the build number is Y.
- 
The build number starts from `1`, introducing the first AMI or Docker image build of the patch.
- 
The build number increments whenever the release introduces a new build of the AMI or Docker image for the same Mule runtime version. This increment does not indicate code changes to Mule runtime. 
 
-