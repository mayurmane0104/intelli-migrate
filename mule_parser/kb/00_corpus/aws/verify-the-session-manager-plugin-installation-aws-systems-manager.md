# Verify the Session Manager plugin installation - AWS Systems Manager

**Source:** [https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-verify.html](https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-verify.html)

---

Run the following commands to verify that the Session Manager plugin installed successfully.

`session-manager-plugin`

If the installation was successful, the following message is returned.

The Session Manager plugin is installed successfully. Use the AWS CLI to start a session.

You can also test the installation by running the [start-session](https://docs.aws.amazon.com/cli/latest/reference/ssm/start-session.html)
                    command in the the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI).
                    In the following command, replace 

`instance-id` with
                    your own information.`aws ssm start-session --target``instance-id`

This command will work only if you have installed and configured the AWS CLI, and if your Session Manager administrator has granted you the necessary IAM permissions to access the target managed node using Session Manager.