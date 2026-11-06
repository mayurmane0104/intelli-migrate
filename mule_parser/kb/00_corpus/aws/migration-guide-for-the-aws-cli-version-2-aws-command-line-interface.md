# Migration guide for the AWS CLI version 2 - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration.html](https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration.html)

---

This section contains instructions for updating the AWS CLI version 1 to AWS CLI version 2. The AWS CLI version 2 builds on AWS CLI version 1 and includes features and enhancements based on community feedback. The AWS CLI version 2 is the most recent major version of the AWS CLI and supports all of the latest features. Some features that were introduced in version 2 are not backported to version 1 and you must upgrade to access those features.

To prevent unexpected issues, before you migrate to version 2, [learn about the differences between the
            versions](./cliv2-migration-changes.html). The AWS CLI version 2 includes new features and changes that might require you to
        update your scripts or commands for backwards compatibility.

AWS CLI versions 1 and 2 use the same `aws` command name. If you have both
        versions installed, your computer uses the first one found in your search path. This could
        result in your `aws` command name calling your old AWS CLI version, even when you
        have the new one installed.

To update to the AWS CLI version 2, follow one of the below instructions:

- 
    If you previously installed AWS CLI version 1, follow the instructions in [Installing AWS CLI version 2 from AWS CLI version 1](./cliv2-migration-instructions.html).
- 
        If you have not previously installed AWS CLI version 1, follow the instructions in [Getting started with the AWS CLI](./cli-chap-getting-started.html).

## Using AWS CLI Migration Tools to Mitigate Breakage

    There are changes in behavior between AWS CLI version 1 and AWS CLI version 2 that might require you to update your scripts or commands. Upgrading to AWS CLI version 2 without verifying that your existing scripts are safely migrated risks encountering unexpected effects when running the scripts with AWS CLI version 2, such as making unintended changes to the resources on your AWS accounts.

There are two AWS-owned tools that you can use to guide your migration. Regardless of which tool 
      you use, we recommend that you reference 
      [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking) in 
      the [New features and changes in the AWS CLI version 2](./cliv2-migration-changes.html) guide.

### Upgrade Debug Mode

Upgrade debug mode is a feature in AWS CLI version 1 that is available in versions `1.44.0` 
          and higher. When this feature is enabled, each AWS CLI command that you execute is checked to determine 
          if it is likely to have different behavior in AWS CLI version 2, assuming the execution environment 
          stays the same. If an executed command would have different behavior in AWS CLI version 2, a warning will 
          be shown alongside the command output with suggested actions that can be taken to preserve AWS CLI version 
          1 behavior in AWS CLI version 2.

The main reason to use upgrade debug mode to guide your migration is that it has high coverage for detecting 
          whether commands will face a change of behavior. In total, 15 out of the 16 breaking changes described in 
          [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking) can be 
          detected with upgrade debug mode—see 
          [Limitations](./cli-upgrade-debug-mode.html#upgrade-mode-limitations) in 
          [Using upgrade debug mode to upgrade AWS CLI version 1 to AWS CLI version 2](./cli-upgrade-debug-mode.html) for the limitations of this 
          feature. On the other hand, the main downside of using upgrade debug mode is that its output is only relevant 
          within its execution environment; if any AWS CLI configuration settings change in the environment after 
          migrating to AWS CLI version 2, breaking changes may still occur, and you should re-verify using upgrade debug 
          mode in the updated environment.

### AWS CLI v1-to-v2 Migration Tool

The AWS CLI v1-to-v2 Migration Tool is a standalone tool that can be used with Python 3.9 and higher. This tool is a static linter that runs independently of the AWS CLI. It lints bash scripts containing AWS CLI version 1 commands that may have different behavior in AWS CLI version 2. For most commands that it detects as likely to have different behavior in AWS CLI version 2, it can automatically update the command within the script to preserve AWS CLI version 1 behavior in AWS CLI version 2.

The main reason to use the AWS CLI v1-to-v2 Migration Tool to guide your migration is that it can automatically update your scripts to preserve AWS CLI version 1 behavior in AWS CLI version 2, saving you time and effort in making the updates yourself. On the other hand, the main downside to using the migration tool is that it has lower coverage for detecting whether commands will face a change of behavior. Being a static tool, it does not check for changes in behavior that is determined at runtime.

## Choosing Between Upgrade Debug Mode and AWS CLI v1-to-v2 Migration Tool

    The following table highlights the main differences between upgrade debug mode and the AWS CLI v1-to-v2 Migration Tool, and can be used to help guide you to choosing the right tool for your use case.

| Upgrade debug mode | AWS CLI v1-to-v2 Migration Tool | 
|---|---|
| Detects 15 out of the 16 breaking changes between AWS CLI version 1 and AWS CLI version 2. | Detects 7 out of the 16 breaking changes between AWS CLI version 1 and AWS CLI version 2. | 
| Compatible with any terminal program that can run the AWS CLI. | Only supports linting bash scripts. | 
| Requires AWS CLI version 1, version `1.44.0`or higher. | Runs independently of the AWS CLI; it does not require the AWS CLI to be installed. | 
| Manual fixes must be made to preserve AWS CLI version 1 behavior in AWS CLI version 2. | Automatically fixes most AWS CLI version 1 commands that it detects as likely to have different behavior in AWS CLI version 2. | 
| Detections and suggested fixes are only relevant to the execution environment (i.e. AWS CLI configuration) that it is executed in. | Detections and suggested fixes are independent of the environment. | 
| Requires executing each AWS CLI command under test for change of behavior. | Does not require executing any AWS CLI commands. Only needs to be executed once per bash script. | 
| Has exactly 5 known cases where it will output false positive detections. | Has exactly 3 known cases where it will output false positive detections. | 

The following table shows which of the 
      [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking) are 
      supported in each of the two migration tools.