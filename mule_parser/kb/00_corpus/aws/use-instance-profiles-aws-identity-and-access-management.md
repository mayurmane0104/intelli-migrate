# Use instance profiles - AWS Identity and Access Management

**Source:** [https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html)

---

Use an instance profile to pass an IAM role to an EC2 instance. For more information, see
      [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the
      *Amazon EC2 User Guide*.

## Managing instance profiles (console)

    If you use the AWS Management Console to create a role for Amazon EC2, the console automatically creates an instance profile and gives it the same name as the role. When you then use the Amazon EC2 console to launch an instance with an IAM role, you can select a role to associate with the instance. In the console, the list that's displayed is actually a list of instance profile names. The console does not create an instance profile for a role that is not associated with Amazon EC2.

You can use the AWS Management Console to delete IAM roles and instance profiles for Amazon EC2 if the
      role and the instance profile have the same name. To learn more about deleting instance
      profiles, see [Delete roles or instance profiles](./id_roles_manage_delete.html).

###### Note

To update permissions for an instance, replace its instance profile. We do not recommend removing a role from an instance profile, because there is a delay of up to one hour before this change takes effect.

## Managing instance profiles (AWS CLI or AWS API)

    If you manage your roles from the AWS CLI or the AWS API, you create roles and instance profiles as separate actions. Because roles and instance profiles can have different names, you must know the names of your instance profiles as well as the names of roles they contain. That way you can choose the correct instance profile when you launch an EC2 instance.

You can attach tags to your IAM resources, including instance profiles, to identify, organize, and control access to them. You can tag instance profiles only when you use the AWS CLI or AWS API.

###### Note

An instance profile can contain only one IAM role, although a role can be included in
        multiple instance profiles. This limit of one role per instance profile cannot be increased.
        You can remove the existing role and then add a different role to an instance profile. You
        must then wait for the change to appear across all of AWS because of [eventual consistency](https://en.wikipedia.org/wiki/Eventual_consistency). To
        force the change, you must 

[disassociate the instance profile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.html)and then

[associate the instance profile](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.html), or you can stop your instance and then restart it.

### Managing instance profiles (AWS CLI)

You can use the following AWS CLI commands to work with instance profiles in an AWS account.

- 
          Create an instance profile: `aws iam create-instance-profile`
- 
          Tag an instance profile: `aws iam tag-instance-profile`
- 
          List tags for an instance profile: `aws iam list-instance-profile-tags`
- 
          Untag an instance profile: `aws iam untag-instance-profile`
- 
          Add a role to an instance profile: `aws iam add-role-to-instance-profile`
- 
          List instance profiles: `aws iam list-instance-profiles``aws iam list-instance-profiles-for-role`
- 
          Get information about an instance profile: `aws iam get-instance-profile`
- 
          Remove a role from an instance profile: `aws iam remove-role-from-instance-profile`
- 
          Delete an instance profile: `aws iam delete-instance-profile`

You can also attach a role to an already running EC2 instance by using the following
        commands. For more information, see [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role).

- 
          Attach an instance profile with a role to a stopped or running EC2 instance: `aws ec2 associate-iam-instance-profile`
- 
          Get information about an instance profile attached to an EC2 instance: `aws ec2 describe-iam-instance-profile-associations`
- 
          Detach an instance profile with a role from a stopped or running EC2 instance: `aws ec2 disassociate-iam-instance-profile`

### Managing instance profiles (AWS API)

You can call the following AWS API operations to work with instance profiles in an AWS account.

- 
          Create an instance profile: `CreateInstanceProfile`
- 
          Tag an instance profile: `TagInstanceProfile`
- 
          List tags on an instance profile: `ListInstanceProfileTags`
- 
          Untag an instance profile: `UntagInstanceProfile`
- 
          Add a role to an instance profile: `AddRoleToInstanceProfile`
- 
          List instance profiles: `ListInstanceProfiles``ListInstanceProfilesForRole`
- 
          Get information about an instance profile: `GetInstanceProfile`
- 
          Remove a role from an instance profile: `RemoveRoleFromInstanceProfile`
- 
          Delete an instance profile: `DeleteInstanceProfile`

You can also attach a role to an already running EC2 instance by calling the following
        operations. For more information, see [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#attach-iam-role).

- 
          Attach an instance profile with a role to a stopped or running EC2 instance: `AssociateIamInstanceProfile`
- 
          Get information about an instance profile attached to an EC2 instance: `DescribeIamInstanceProfileAssociations`
- 
          Detach an instance profile with a role from a stopped or running EC2 instance: `DisassociateIamInstanceProfile`