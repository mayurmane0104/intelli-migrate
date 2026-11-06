# AppRegistry examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_service-catalog-appregistry_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_service-catalog-appregistry_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AppRegistry.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `associate-attribute-group`.

- **AWS CLI**
- 
            
                    **To associate an attribute group**The following `associate-attribute-group`example associates a specific attribute group in your AWS account to a specific application in your AWS account.`aws servicecatalog-appregistry associate-attribute-group \ --application``"ExampleApplication"`\ --attribute-group`"ExampleAttributeGroup"`Output: `{ "applicationArn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/0ars38r6btoohvpvd9gqrptt9l", "attributeGroupArn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/01sj5xdwhbw54kejwnt09fnpcl" }`For more information, see [Associating and disassociating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attr-groups.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [AssociateAttributeGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/associate-attribute-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-application`.

- **AWS CLI**
- 
            
                    **To create an application**The following `create-application`example creates a new application in your AWS account.`aws servicecatalog-appregistry create-application \ --name``"ExampleApplication"`Output: `{ "application": { "id": "0ars38r6btoohvpvd9gqrptt9l", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/0ars38r6btoohvpvd9gqrptt9l", "name": "ExampleApplication", "creationTime": "2023-02-28T21:10:10.820000+00:00", "lastUpdateTime": "2023-02-28T21:10:10.820000+00:00", "tags": {} } }`For more information, see [Creating applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-apps.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [CreateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/create-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-attribute-group`.

- **AWS CLI**
- 
            
                    **To create an attribute group**The following `create-attribute-group`example creates a new attribute group in your AWS account.`aws servicecatalog-appregistry create-attribute-group \ --name``"ExampleAttributeGroup"`\ --attributes '`{"SomeKey1":"SomeValue1","SomeKey2":"SomeValue2"}`'Output: `{ "attributeGroup": { "id": "01sj5xdwhbw54kejwnt09fnpcl", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/01sj5xdwhbw54kejwnt09fnpcl", "name": "ExampleAttributeGroup", "creationTime": "2023-02-28T20:38:01.389000+00:00", "lastUpdateTime": "2023-02-28T20:38:01.389000+00:00", "tags": {} } }`For more information, see [Creating attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/create-attr-groups.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [CreateAttributeGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/create-attribute-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-application`.

- **AWS CLI**
- 
            
                    **To delete an application**The following `delete-application`example deletes a specific application in your AWS account.`aws servicecatalog-appregistry delete-application \ --application``"ExampleApplication3"`Output: `{ "application": { "id": "055gw7aynr1i5mbv7kjwzx5945", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/055gw7aynr1i5mbv7kjwzx5945", "name": "ExampleApplication3", "creationTime": "2023-02-28T22:06:28.228000+00:00", "lastUpdateTime": "2023-02-28T22:06:28.228000+00:00" } }`For more information, see [Deleting applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/delete-app-details.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [DeleteApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/delete-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-attribute-group`.

- **AWS CLI**
- 
            
                    **Example 8: To delete an attribute group**The following `delete-attribute-group`example deletes a specific attribute group in your AWS account.`aws servicecatalog-appregistry delete-attribute-group \ --attribute-group``"ExampleAttributeGroup3"`Output: `{ "attributeGroup": { "id": "011ge6y3emyjijt8dw8jn6r0hv", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/011ge6y3emyjijt8dw8jn6r0hv", "name": "ExampleAttributeGroup3", "creationTime": "2023-02-28T22:05:35.224000+00:00", "lastUpdateTime": "2023-02-28T22:05:35.224000+00:00" } }`For more information, see [Deleting attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/delete-attr-group.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [DeleteAttributeGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/delete-attribute-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-application`.

- **AWS CLI**
- 
            
                    **To get an application**The following `get-application`example retrieves metadata information about a specific application in your AWS account.`aws servicecatalog-appregistry get-application \ --application``"ExampleApplication"`Output: `{ "id": "0ars38r6btoohvpvd9gqrptt9l", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/0ars38r6btoohvpvd9gqrptt9l", "name": "ExampleApplication", "creationTime": "2023-02-28T21:10:10.820000+00:00", "lastUpdateTime": "2023-02-28T21:10:10.820000+00:00", "associatedResourceCount": 0, "tags": { "aws:servicecatalog:applicationName": "ExampleApplication" }, "integrations": { "resourceGroup": { "state": "CREATE_COMPLETE", "arn": "arn:aws:resource-groups:us-west-2:813737243517:group/AWS_AppRegistry_Application-ExampleApplication" } } }`For more information, see [Using Application details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/access-app-details.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [GetApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-attribute-group`.

- **AWS CLI**
- 
            
                    **To get an attribute group**The following `get-attribute-group`example retrieves a specific attribute group in your AWS account.`aws servicecatalog-appregistry get-attribute-group \ --attribute-group``"ExampleAttributeGroup"`Output: `{ "id": "01sj5xdwhbw54kejwnt09fnpcl", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/01sj5xdwhbw54kejwnt09fnpcl", "name": "ExampleAttributeGroup", "attributes": "{\"SomeKey1\":\"SomeValue1\",\"SomeKey2\":\"SomeValue2\"}", "creationTime": "2023-02-28T20:38:01.389000+00:00", "lastUpdateTime": "2023-02-28T20:38:01.389000+00:00", "tags": { "aws:servicecatalog:attributeGroupName": "ExampleAttributeGroup" } }`For more information, see [Managing metadata for attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/manage-metatdata.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [GetAttributeGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/get-attribute-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-applications`.

- **AWS CLI**
- 
            
                    **To list applications**The following `list-applications`example retrieves a list of all the applications in your AWS account.`aws servicecatalog-appregistry list-applications`Output: `{ "applications": [ { "id": "03axw94pjfj3uan00tcgbrxnkw", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/03axw94pjfj3uan00tcgbrxnkw", "name": "ExampleApplication2", "creationTime": "2023-02-28T21:59:34.094000+00:00", "lastUpdateTime": "2023-02-28T21:59:34.094000+00:00" }, { "id": "055gw7aynr1i5mbv7kjwzx5945", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/055gw7aynr1i5mbv7kjwzx5945", "name": "ExampleApplication3", "creationTime": "2023-02-28T22:06:28.228000+00:00", "lastUpdateTime": "2023-02-28T22:06:28.228000+00:00" }, { "id": "0ars38r6btoohvpvd9gqrptt9l", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/0ars38r6btoohvpvd9gqrptt9l", "name": "ExampleApplication", "description": "This is an example application", "creationTime": "2023-02-28T21:10:10.820000+00:00", "lastUpdateTime": "2023-02-28T21:24:19.729000+00:00" } ] }`For more information, see [Viewing application details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/view-app-details.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [ListApplications](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/list-applications.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-associated-attribute-groups`.

- **AWS CLI**
- 
            
                    **To list associated attribute groups**The following `list-associated-attribute-groups`example retrieves a list of all attribute groups in your AWS account that are associated with a specific application in your AWS account.`aws servicecatalog-appregistry list-associated-attribute-groups \ --application``"ExampleApplication"`Output: `{ "attributeGroups": [ "01sj5xdwhbw54kejwnt09fnpcl" ] }`For more information, see [Associating and disassociating attribute groups](https://https://docs.aws.amazon.com/servicecatalog/latest/arguide/associate-attr-groups.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [ListAssociatedAttributeGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/list-associated-attribute-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attribute-groups-for-application`.

- **AWS CLI**
- 
            
                    **To list attribute groups for an application**The following `list-attribute-groups-for-application`example lists the details of all attribute groups in your AWS account that are associated with a specific application in your AWS account.`aws servicecatalog-appregistry list-attribute-groups-for-application \ --application``"ExampleApplication"`Output: `{ "attributeGroupsDetails": [ { "id": "01sj5xdwhbw54kejwnt09fnpcl", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/01sj5xdwhbw54kejwnt09fnpcl", "name": "ExampleAttributeGroup" } ] }`For more information, see [Viewing attribute group details](https://servicecatalog/latest/arguide/view-attr-group.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [ListAttributeGroupsForApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/list-attribute-groups-for-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-attribute-groups`.

- **AWS CLI**
- 
            
                    **To list attribute groups**The following `list-attribute-groups`example retrieves a list of all attribute groups in your AWS account.`aws servicecatalog-appregistry list-attribute-groups`Output: `{ "attributeGroups": [ { "id": "011ge6y3emyjijt8dw8jn6r0hv", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/011ge6y3emyjijt8dw8jn6r0hv", "name": "ExampleAttributeGroup3", "creationTime": "2023-02-28T22:05:35.224000+00:00", "lastUpdateTime": "2023-02-28T22:05:35.224000+00:00" }, { "id": "01sj5xdwhbw54kejwnt09fnpcl", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/01sj5xdwhbw54kejwnt09fnpcl", "name": "ExampleAttributeGroup", "description": "This is an example attribute group", "creationTime": "2023-02-28T20:38:01.389000+00:00", "lastUpdateTime": "2023-02-28T21:02:04.559000+00:00" }, { "id": "03n1yffgq6d18vwrzxf0c70nm3", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/03n1yffgq6d18vwrzxf0c70nm3", "name": "ExampleAttributeGroup2", "creationTime": "2023-02-28T21:57:30.687000+00:00", "lastUpdateTime": "2023-02-28T21:57:30.687000+00:00" } ] }`For more information, see [Viewing attribute group details](https://docs.aws.amazon.com/servicecatalog/latest/arguide/view-attr-group.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [ListAttributeGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/list-attribute-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-application`.

- **AWS CLI**
- 
            
                    **To update an application**The following `update-application`example updates a specific application in your AWS account to include a description.`aws servicecatalog-appregistry update-application \ --application``"ExampleApplication"`\ --description`"This is an example application"`Output: `{ "application": { "id": "0ars38r6btoohvpvd9gqrptt9l", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/applications/0ars38r6btoohvpvd9gqrptt9l", "name": "ExampleApplication", "description": "This is an example application", "creationTime": "2023-02-28T21:10:10.820000+00:00", "lastUpdateTime": "2023-02-28T21:24:19.729000+00:00", "tags": { "aws:servicecatalog:applicationName": "ExampleApplication" } } }`For more information, see [Editing applications](https://docs.aws.amazon.com/servicecatalog/latest/arguide/edit-apps.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [UpdateApplication](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/update-application.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-attribute-group`.

- **AWS CLI**
- 
            
                    **To update an attribute group**The following `update-attribute-group`example updates a specific attribute group in your AWS account to include a description.`aws servicecatalog-appregistry update-attribute-group \ --attribute-group``"ExampleAttributeGroup"`\ --description`"This is an example attribute group"`Output: `{ "attributeGroup": { "id": "01sj5xdwhbw54kejwnt09fnpcl", "arn": "arn:aws:servicecatalog:us-west-2:813737243517:/attribute-groups/01sj5xdwhbw54kejwnt09fnpcl", "name": "ExampleAttributeGroup", "description": "This is an example attribute group", "creationTime": "2023-02-28T20:38:01.389000+00:00", "lastUpdateTime": "2023-02-28T21:02:04.559000+00:00", "tags": { "aws:servicecatalog:attributeGroupName": "ExampleAttributeGroup" } } }`For more information, see [Editing attribute groups](https://docs.aws.amazon.com/servicecatalog/latest/arguide/edit-attr-group.html)in the*AWS Service Catalog AppRegistry Administrator Guide*.- 
                    For API details, see [UpdateAttributeGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/servicecatalog-appregistry/update-attribute-group.html)in*AWS CLI Command Reference*.
 
-