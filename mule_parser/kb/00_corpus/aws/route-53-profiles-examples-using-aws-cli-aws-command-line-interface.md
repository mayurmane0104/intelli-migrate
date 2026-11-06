# Route 53 Profiles examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_route53profiles_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_route53profiles_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Route 53 Profiles.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-profile`.

- **AWS CLI**
- 
            
                    **To associate a Profile**The following `associate-profile`example associates a Profile to a VPC.`aws route53profiles associate-profile \ --name``test-association`\ --profile-id`rp-4987774726example`\ --resource-id`vpc-0af3b96b3example`Output: `{ "ProfileAssociation": { "CreationTime": 1710851336.527, "Id": "rpassoc-489ce212fexample", "ModificationTime": 1710851336.527, "Name": "test-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceId": "vpc-0af3b96b3example", "Status": "CREATING", "StatusMessage": "Creating Profile Association" } }`For more information, see [Using Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profile-high-level-steps.html)in the*Amazon Route 53 Developer Guide*.- 
                    For API details, see [AssociateProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/associate-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `associate-resource-to-profile`.

- **AWS CLI**
- 
            
                    **To associate a resource to a Profile**The following `associate-resource-to-profile`example associates a DNS Firewall rule group with the priority of 102 to a Profile.`aws route53profiles associate-resource-to-profile \ --name``test-resource-association`\ --profile-id`rp-4987774726example`\ --resource-arn`arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example`\ --resource-properties "{\"priority\": 102}"Output: `{ "ProfileResourceAssociation": { "CreationTime": 1710851216.613, "Id": "rpr-001913120a7example", "ModificationTime": 1710851216.613, "Name": "test-resource-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example", "ResourceProperties": "{\"priority\":102}", "ResourceType": "FIREWALL_RULE_GROUP", "Status": "UPDATING", "StatusMessage": "Updating the Profile to DNS Firewall rule group association" } }`- 
                    For API details, see [AssociateResourceToProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/associate-resource-to-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-profile`.

- **AWS CLI**
- 
            
                    **To create a Profile**The following `create-profile`example creates a Profile.`aws route53profiles create-profile \ --name``test`Output: `{ "Profile": { "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-6ffe47d5example", "ClientToken": "2ca1a304-32b3-4f5f-bc4c-EXAMPLE11111", "CreationTime": 1710850903.578, "Id": "rp-6ffe47d5example", "ModificationTime": 1710850903.578, "Name": "test", "OwnerId": "123456789012", "ShareStatus": "NOT_SHARED", "Status": "COMPLETE", "StatusMessage": "Created Profile" } }`- 
                    For API details, see [CreateProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/create-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-profile`.

- **AWS CLI**
- 
            
                    **To delete a Profile**The following `delete-profile`example deletes a Profile.`aws route53profiles delete-profile \ --profile-id``rp-6ffe47d5example`Output: `{ "Profile": { "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-6ffe47d5example", "ClientToken": "0a15fec0-05d9-4f78-bec0-EXAMPLE11111", "CreationTime": 1710850903.578, "Id": "rp-6ffe47d5example", "ModificationTime": 1710850903.578, "Name": "test", "OwnerId": "123456789012", "ShareStatus": "NOT_SHARED", "Status": "DELETED", "StatusMessage": "Deleted Profile" } }`- 
                    For API details, see [DeleteProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/delete-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-profile`.

- **AWS CLI**
- 
            
                    **To disassociate a Profile**The following `disassociate-profile`example disassociates a Profile from a VPC.`aws route53profiles disassociate-profile \ --profile-id``rp-4987774726example`\ --resource-id`vpc-0af3b96b3example`Output: `{ "ProfileAssociation": { "CreationTime": 1710851336.527, "Id": "rpassoc-489ce212fexample", "ModificationTime": 1710851401.362, "Name": "test-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceId": "vpc-0af3b96b3example", "Status": "DELETING", "StatusMessage": "Deleting Profile Association" } }`- 
                    For API details, see [DisassociateProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/disassociate-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `disassociate-resource-from-profile`.

- **AWS CLI**
- 
            
                    **To disassociate a resource from Profile**The following `disassociate-resource-from-profile`example disassociates a DNS Firewall rule group from a Profile.`aws route53profiles disassociate-resource-from-profile \ --profile-id``rp-4987774726example`\ --resource-arn`arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example`Output: `{ "ProfileResourceAssociation": { "CreationTime": 1710851216.613, "Id": "rpr-001913120a7example", "ModificationTime": 1710852624.36, "Name": "test-resource-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example", "ResourceProperties": "{\"priority\":105}", "ResourceType": "FIREWALL_RULE_GROUP", "Status": "DELETING", "StatusMessage": "Deleting the Profile to DNS Firewall rule group association" } }`- 
                    For API details, see [DisassociateResourceFromProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/disassociate-resource-from-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-profile-association`.

- **AWS CLI**
- 
            
                    **To get information about a Profile association**The following `get-profile-association`returns information about the specified Profile association.`aws route53profiles get-profile-association \ --profile-association-id``rpassoc-489ce212fexample`Output: `{ "ProfileAssociation": { "CreationTime": 1709338817.148, "Id": "rrpassoc-489ce212fexample", "ModificationTime": 1709338974.772, "Name": "test-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceId": "vpc-0af3b96b3example", "Status": "COMPLETE", "StatusMessage": "Created Profile Association" } }`- 
                    For API details, see [GetProfileAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/get-profile-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-profile-resource-association`.

- **AWS CLI**
- 
            
                    **To get information about a resource associated to a Profile**The following `get-profile-resource-association`returns information about the specified resource association to a Profile.`aws route53profiles get-profile-resource-association \ --profile-resource-association-id``rpr-001913120a7example`Output: `{ "ProfileResourceAssociation": { "CreationTime": 1710851216.613, "Id": "rpr-001913120a7example", "ModificationTime": 1710852303.798, "Name": "test-resource-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example", "ResourceProperties": "{\"priority\":105}", "ResourceType": "FIREWALL_RULE_GROUP", "Status": "COMPLETE", "StatusMessage": "Completed creation of Profile to DNS Firewall rule group association" } }`- 
                    For API details, see [GetProfileResourceAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/get-profile-resource-association.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-profile`.

- **AWS CLI**
- 
            
                    **To get information about a Profile**The following `get-profile`returns information about the specified Profile.`aws route53profiles get-profile \ --profile-id``rp-4987774726example`Output: `{ "Profile": { "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-4987774726example", "ClientToken": "0cbc5ae7-4921-4204-bea9-EXAMPLE11111", "CreationTime": 1710851044.288, "Id": "rp-4987774726example", "ModificationTime": 1710851044.288, "Name": "test", "OwnerId": "123456789012", "ShareStatus": "NOT_SHARED", "Status": "COMPLETE", "StatusMessage": "Created Profile" } }`- 
                    For API details, see [GetProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/get-profile.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-profile-associations`.

- **AWS CLI**
- 
            
                    **To list Profile associations**The following `list-profile-associations`lists the Profile associations in your AWS account.`aws route53profiles list-profile-associations`Output: `{ "ProfileAssociations": [ { "CreationTime": 1709338817.148, "Id": "rpassoc-489ce212fexample", "ModificationTime": 1709338974.772, "Name": "test-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceId": "vpc-0af3b96b3example", "Status": "COMPLETE", "StatusMessage": "Created Profile Association" } ] }`- 
                    For API details, see [ListProfileAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/list-profile-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-profile-resource-associations`.

- **AWS CLI**
- 
            
                    **To list Profile resource associations**The following `list-profile-resource-associations`list the Profile resource associations for the specified Profile.`aws route53profiles list-profile-resource-associations \ --profile-id``rp-4987774726example`Output: `{ "ProfileResourceAssociations": [ { "CreationTime": 1710851216.613, "Id": "rpr-001913120a7example", "ModificationTime": 1710851216.613, "Name": "test-resource-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example", "ResourceProperties": "{\"priority\":102}", "ResourceType": "FIREWALL_RULE_GROUP", "Status": "COMPLETE", "StatusMessage": "Completed creation of Profile to DNS Firewall rule group association" } ] }`- 
                    For API details, see [ListProfileResourceAssociations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/list-profile-resource-associations.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-profiles`.

- **AWS CLI**
- 
            
                    **To list Profiles**The following `list-profiles`lists the Profiles in your AWS account and displays additional information about them.`aws route53profiles list-profiles`Output: `{ "ProfileSummaries": [ { "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-4987774726example", "Id": "rp-4987774726example", "Name": "test", "ShareStatus": "NOT_SHARED" } ] }`- 
                    For API details, see [ListProfiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/list-profiles.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a resource**The following `list-tags-for-resource`lists tags for the specified resource.`aws route53profiles list-tags-for-resource \ --resource-arn``arn:aws:route53profiles:us-east-1:123456789012:profile/rp-4987774726example`Output: `{ "Tags": { "my-key-2": "my-value-2", "my-key-1": "my-value-1" } }`- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-profile-resource-association`.

- **AWS CLI**
- 
            
                    **To update a resource associated to a Profile**The following `update-profile-resource-association`updates a priority of a DNS Firewall rule group that is associated to the Profile.`aws route53profiles update-profile-resource-association \ --profile-resource-association-id``rpr-001913120a7example`\ --resource-properties "{\"priority\": 105}"Output: `{ "ProfileResourceAssociation": { "CreationTime": 1710851216.613, "Id": "rpr-001913120a7example", "ModificationTime": 1710852303.798, "Name": "test-resource-association", "OwnerId": "123456789012", "ProfileId": "rp-4987774726example", "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example", "ResourceProperties": "{\"priority\":105}", "ResourceType": "FIREWALL_RULE_GROUP", "Status": "UPDATING", "StatusMessage": "Updating the Profile to DNS Firewall rule group association" } }`- 
                    For API details, see [UpdateProfileResourceAssociation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53profiles/update-profile-resource-association.html)in*AWS CLI Command Reference*.
 
-