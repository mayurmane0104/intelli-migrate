# Setting granular access to AWS services through IAM - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/scoping-policies-iam-interface.html](https://docs.aws.amazon.com/quick/latest/userguide/scoping-policies-iam-interface.html)

---

| Applies
                    to:Enterprise Edition | 

| Intended audience: System administrators and Amazon Quick administrators | 

In Enterprise edition, Amazon Quick provides a way for you to set up detailed access to resources in AWS services. Like every other AWS service, Quick uses IAM policies to control access for users and groups.

Before you begin, ask an administrator to set up the necessary IAM policies ahead of
            time. If these are set up, you can select them as part of the procedure in this section.
            For information about creating IAM policies to use with Quick, see [Identity and access
                management in Quick](https://docs.aws.amazon.com/quicksight/latest/user/identity.html).

###### To assign an IAM policy to a user or group

- 
                Sign in to Quick at [https://quicksight.aws.amazon.com/](https://quicksight.aws.amazon.com/).
- 
                At upper left, choose your user name, and then choose **Manage QuickSight**.
- 
                Choose **Security & permissions**.
- 
                Under **Resource access for individual users and groups**, choose**IAM policy assignments**.The remaining steps at this point involve choosing an IAM policy to assign to the user or group. You can assign multiple IAM policies to one Amazon Quick user or group. To determine permissions, Amazon Quick performs a union and an intersection with the AWS account–level policies. If you already have active IAM policy assignments, they are listed on this page. You can search for existing assignments by using the search box. If you have drafts that aren't active yet, they are listed under **Assignment drafts**.
- 
                Choose one of the following: - 
                        To create an IAM policy assignment, choose **Add new assignment**.
- 
                        To edit an existing assignment, choose the **Edit assignment**icon for that assignment.
- 
                        To enable or disable a policy, select the check box for that policy, and then choose **Enable**or**Disable**. You can select multiple policy assignments at a time.
- 
                        To delete an existing assignment, choose the **Remove assignment**icon near the name of the assignment. To confirm your choice, choose**Delete**on the confirmation screen. Or choose**Back**to cancel deletion.
 If you are creating or editing an assignment, continue to the next step. Otherwise, skip to the end of this procedure. 
- 
                        
- 
                On the next screen, you perform the policy assignment process, which is divided into steps. As you work through the steps, you can go forward or backward to make changes. When you exit the screen, your changes from all of the steps are saved. - 
                        Step 1: Name assignment – If this is a new assignment, enter a name for the assignment, and then choose **Next**to continue. If you want to change the name, choose**Step 1**at left.
- 
                        Step 2: Select an IAM policy – Choose an IAM policy that you want to use. From this screen, you can interact with the policies as follows: - 
                                Choose a policy that you want to use. 
- 
                                Search for a policy name. 
- 
                                Filter the list to see all IAM policies, AWS-managed policies, or customer-managed policies. 
- 
                                View a policy, by choosing **View policy**.
 To choose a policy, choose the button beside it, and then choose **Next**to continue.
- 
                                
- 
                        Step 3: Assign users and groups – Choose specific users or groups. Or choose to use the selected IAM policy for all users and groups. Choose one of the following. - 
                                For **Assign to all users and groups**, select the check box to assign the IAM policy to all Amazon Quick users and groups. Choosing this option assigns the policy to all current and future users and groups.
- 
                                Choose the users and groups you want to assign to this IAM policy. You can search for them by name, email address, or group name. 
 When you are finished selecting users and groups, choose **Next**to continue.
- 
                                
- 
                        Step 4: Review and enable changes – Save your changes. Choose one of the following. - 
                                To edit any of your choices, choose that step to edit it. 
- 
                                To save this policy assignment as a draft, choose **Save as draft**. You can enable the draft later.
- 
                                To immediately enable this policy, choose **Save and enable**. This option overwrites any existing policy assignment with the same name.
 
- 
                                
 
-