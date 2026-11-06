# Using AWS CLI v1-to-v2 Migration Tool to upgrade AWS CLI version 1 to AWS CLI version 2 - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli-migration-tool.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-migration-tool.html)

---

This topic describes the AWS CLI v1-to-v2 Migration Tool.

We recommend that users of AWS CLI version 1 upgrade to AWS CLI version 2 to access new features and enhanced performance. There are changes in behavior between AWS CLI version 1 and AWS CLI version 2 that might require you to update your scripts or commands to get the same behavior. The AWS CLI v1-to-v2 Migration Tool analyzes bash scripts containing AWS CLI version 1 commands and detects usage of features that have been updated with breaking changes in AWS CLI version 2. Additionally, the tool can automatically modify your scripts to fix most issues that it detects. This tool improves the upgrade experience by automatically detecting and modifying AWS CLI version 1 commands in bash scripts to prevent unexpected issues when upgrading to version 2.

Compared to Upgrade Debug Mode, the AWS CLI v1-to-v2 Migration Tool is a standalone tool and does not 
    require executing AWS CLI commands. For a thorough comparison between the Upgrade Debug Mode and the AWS 
    CLI v1-to-v2 Migration Tool see 
    [Using AWS CLI Migration Tools to Mitigate Breakage](./cliv2-migration.html#using-migration-tools) in 
    [Migration guide for the AWS CLI version 2](./cliv2-migration.html).

For more details, see [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking) 
    in [New features and changes in the AWS CLI version 2](./cliv2-migration-changes.html).

## How it Works

    The AWS CLI v1-to-v2 Migration Tool is a Python package capable of linting bash scripts that use AWS CLI version 1. Being a static linter, it does not depend on the version of AWS CLI version 1 that you may have installed on your machine. The linter is invoked through the command line, where the local file path to the bash script is supplied as a parameter.

The migration tool can also automatically produce a modified bash script that resolves most findings that it detects by modifying the AWS CLI version 1 commands used in the script. The migration tool modifies commands so that they are compatible with AWS version 2 and retains the behavior of version 1.

For some findings, the AWS CLI v1-to-v2 Migration Tool can detect them but not offer an automatic fix. In these cases, the migration tool flags them as detections that require manual review.

See [Limitations](#migration-tool-limitations) for an 
      exhaustive list of breaking changes and automatic fixes that the AWS CLI v1-to-v2 Migration Tool supports.

## Prerequisites

       
        ### Python

To use this tool, you must have Python 3.9 or later installed.

To verify that you have a correct Python version installed, run the following command in a terminal and confirm the output shows a Python version of at least 3.9.

`$`python3 --version

If you have an older version of Python, or do not have Python installed, you can download 
          a compatible version from the 
          [official Python download page](https://www.python.org/downloads/).

### pip

In addition to having a compatible version of Python installed, you must have 
          `pip` installed.

To verify that `pip` is installed, run the following command:

`$`python3 -m pip --version

If you have `pip` installed, you will see an output similar to the following:

`pip 25.0.1 from ~/.local/lib/python3.13/site-packages (python 3.13)`If you do not have `pip` installed, see 
        [Install pip](https://docs.aws.amazon.com/cli/v1/userguide/install-linux.html#install-linux-pip-pip).

## Installation

          Install the AWS CLI v1-to-v2 Migration Tool in a new virtual environment:

`$ `python3 -m venv .venv
`$ `source .venv/bin/activate
`$ `python3 -m pip install aws-cli-migrate## Usage

       
        ### Dry-run Mode (default)

With dry-run mode, you can automatically detect AWS CLI version 1 commands that are subject to breaking changes without modifying the input script:

`$`migrate-aws-cli --script upload_s3_files.sh

### Auto-fix Mode

With auto-fix mode, you can automatically detect and update AWS CLI version 1 commands in the input script to mitigate breakage from changes introduced in AWS CLI version 2, where possible:

`$`migrate-aws-cli --script upload_s3_files.sh --fix

Optionally, you can supply an output path via the `--output` parameter to write the updated script, 
          rather than updating the input script:

`$`migrate-aws-cli --script upload_s3_files.sh --output upload_s3_files_v2.sh --fix

### Interactive Mode

With interactive mode, you can automatically detect AWS CLI version 1 commands that are subject to breaking changes. Most findings will show a 
          suggested fix to mitigate breakage in AWS CLI version 2. You can review the suggested fixes and decide whether to apply them. Optionally, 
          supply an output path via the `--output` parameter to control where to write the updated script:

`$`migrate-aws-cli --script upload_s3_files.sh --interactive \ --output upload_s3_files_v2.sh

The following output snippet is an example finding in interactive mode:

```
14 14│ 
15 15│ aws s3 ls s3://mybucket
16 16│ 
17   │-aws s3 cp s3://amzn-demo-bucket s3://amzn-demo-bucket2 --recursive
   17│+aws s3 cp s3://amzn-demo-bucket s3://amzn-demo-bucket2 --recursive --copy-props none
18 18│ 
19 19│ TEMPLATE_KEY="cloudformation/$(basename "$TEMPLATE_FILE")"
20 20│ 
examples/upload_s3_files.sh:17 [s3-copy] In AWS CLI v2, object properties will be copied 
from the source in multipart copies between S3 buckets. If a copy is or becomes multipart 
after upgrading to AWS CLI v2, extra API calls will be made. See 
https://docs.aws.amazon.com/cli/latest/userguide/cliv2-migration-changes.html#cliv2-migration-s3-copy-metadata.
Apply this fix? [y] yes, [n] no, [a] accept all of type, [r] reject all of type, [u] update all, 
[s] save and exit, [q] quit: 
```
The suggested fix is shown in a format similar to a Git diff. The migration tool suggests the removal of lines 
        starting with a `-`, and suggests adding lines starting with a `+`. In the previous example, 
        the suggestion can be interpreted as adding the `--copy-props none` parameter to the AWS CLI version 1 command 
        that executes an Amazon S3 copy.

For each suggested fix, you can enter any of the following controls:

- 
                Enter `y`to accept the suggested fix.
- 
                Enter `n`to reject the current fix.
- 
                Enter `a`to accept all fixes with the same type.
- 
                Enter `r`to reject all fixes with the same type.
- 
                Enter `u`to accept all remaining fixes.
- 
                Enter `s`to save and exit.
- 
                Enter `q`to quit without saving.

Some findings may be flagged for manual review without a suggested fix. You should review these findings and verify whether you are impacted by the referenced breaking changes. If you are impacted by these findings, you should follow the guidance specified in the finding description to make the necessary changes to avoid or prepare for the breaking changes introduced in AWS CLI version 2.

## Limitations

    The AWS CLI v1-to-v2 Migration Tool does not currently support every breaking change introduced with AWS CLI version 2, and has false positive cases where it outputs detections for commands even if no breaking changes would actually be faced.

We strongly recommend customers understand [Breaking changes between AWS CLI version 1 and AWS CLI version 2](./cliv2-migration-changes.html#cliv2-migration-changes-breaking) 
      published in [New features and changes in the AWS CLI version 2](./cliv2-migration-changes.html).

### Text-based Analysis

The migration tool analyzes your script without running it. This limits how it detects AWS CLI commands for breaking changes. The migration tool can only examine the text of an AWS CLI command. It cannot detect issues that arise at runtime, such as storing deprecated parameters in a variable instead of passing them directly to the AWS CLI.

### Unsupported Breaking Change Detection

The extent of support for breaking changes in the migration tool is summarized in the following table.