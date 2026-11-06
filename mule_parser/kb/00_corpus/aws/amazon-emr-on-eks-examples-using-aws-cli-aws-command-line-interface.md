# Amazon EMR on EKS examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_emr-containers_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_emr-containers_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon EMR on EKS.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `update-role-trust-policy`.

- **AWS CLI**
- 
            
                    **To update the trust policy of an IAM Role to be used with Amazon EMR on EKS**This example command updates the trust policy of a role named **example_iam_role**such that it can be used with Amazon EMR on EKS with**example_namespace**namespace from an EKS cluster named**example_cluster**.Command: `aws emr-containers update-role-trust-policy \ --cluster example_cluster \ --namespace example_namespace \ --role-name example_iam_role`Output: `If the trust policy has already been updated, then the output will be: Trust policy statement already exists for role example_iam_role. No changes were made! If the trust policy has not been updated yet, then the output will be: Successfully updated trust policy of role example_iam_role.`- 
                    For API details, see [UpdateRoleTrustPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/update-role-trust-policy.html)in*AWS CLI Command Reference*.
 
-