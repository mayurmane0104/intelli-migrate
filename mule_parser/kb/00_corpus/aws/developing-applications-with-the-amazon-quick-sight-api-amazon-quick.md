# Developing applications with the Amazon Quick Sight API - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/quicksight-sdks.html](https://docs.aws.amazon.com/quick/latest/userguide/quicksight-sdks.html)

---

You can manage most aspects of your deployment by using the AWS SDKs to access an API
		that's tailored to the programming language or platform that you're using. For more
		information, see [AWS SDKs](http://aws.amazon.com/tools/#SDKs). 

For more information on the API operations, see [Amazon Quick Sight API
			Reference](https://docs.aws.amazon.com/quicksight/index.html?id=docs_gateway). 

Before you can call the Amazon Quick Sight API operations, you need the
				`quicksight:` permission in a
		policy attached to your IAM identity. For example, to call `operation-name``list-users`, you need
		the permission `quicksight:ListUsers`. The same pattern applies to all
		operations.

If you're not sure what the necessary permission is, you can attempt to make a call. The
		client then tells you what the missing permission is. You can use asterisk (`*`)
		in the Resource field of your permission policy instead of specifying explicit resources.
		However, we recommended that you restrict each permission as much as possible. You can
		restrict user access by specifying or excluding resources in the policy, using their
		Amazon Quick Sight Amazon Resource Name (ARN) identifier. 

For more information, see the following:

To retrieve the ARN of a user or a group, use the `Describe` operation on the
		relevant resource. You can also add conditions in IAM to further restrict access to an API
		in some scenarios. For instance, when adding `User1` to `Group1`, the
		main resource is `Group1`, so you can allow or deny access to certain groups, but
		you can also add a condition by using the IAM Amazon Quick Sight key
			`quicksight:UserName` to allow or prevent certain users from being added to
		that group. 

Following is an example policy. It means that the caller with this policy attached, is
		able to invoke the `CreateGroupMembership` operation on any group, provided that
		the user name they are adding to the group is not `user1`. 

`{ "Effect": "Allow", "Action": "quicksight:CreateGroupMembership", "Resource": "arn:aws:quicksight:us-east-1:``aws-account-id`:group/default/*", "Condition": { "StringNotEquals": { "quicksight:UserName": "user1" } } }

The following procedure explains how to interact with Amazon Quick Sight API operations through the AWS CLI. The following instructions have been tested in Bash but should be identical or similar in other command-line environments.

- 
						Install AWS SDK in your environment. Instructions on how to do that are located here: [AWS Command line Interface](https://aws.amazon.com/cli/).
- 
						Set up your AWS CLI identity and region using the following command and follow-up instructions. Use the credentials for an IAM identity or role that has the proper permissions. `aws configure`
- 
						Look at the Amazon Quick Sight SDK help by issuing the following command: `aws quicksight help`
- 
						To get detailed instructions on how to use an API, enter its name followed by help, like so: `aws quicksight list-users help`
- 
						Now you can call an Amazon Quick Sight API operation. This example returns a list of Amazon Quick Sight users in your account. `aws quicksight list-users --aws-account-id``aws-account-id`--namespace default --region us-east-1