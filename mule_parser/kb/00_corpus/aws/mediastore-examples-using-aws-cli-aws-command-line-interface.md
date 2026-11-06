# MediaStore examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_mediastore_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediastore_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaStore.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `create-container`.

- **AWS CLI**
- 
            
                    **To create a container**The following `create-container`example creates a new, empty container.`aws mediastore create-container --container-name``ExampleContainer`Output: `{ "Container": { "AccessLoggingEnabled": false, "CreationTime": 1563557265, "Name": "ExampleContainer", "Status": "CREATING", "ARN": "arn:aws:mediastore:us-west-2:111122223333:container/ExampleContainer" } }`For more information, see [Creating a Container](https://docs.aws.amazon.com/mediastore/latest/ug/containers-create.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [CreateContainer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/create-container.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-container-policy`.

- **AWS CLI**
- 
            
                    **To delete a container policy**The following `delete-container-policy`example deletes the policy that is assigned to the specified container. When the policy is deleted, AWS Elemental MediaStore automatically assigns the default policy to the container.`aws mediastore delete-container-policy \ --container-name``LiveEvents`This command produces no output. For more information, see [DeleteContainerPolicy](https://docs.aws.amazon.com/mediastore/latest/apireference/API_DeleteContainerPolicy.html)in the*AWS Elemental MediaStore API reference*.- 
                    For API details, see [DeleteContainerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-container`.

- **AWS CLI**
- 
            
                    **To delete a container**The following `delete-container`example deletes the specified container. You can delete a container only if it has no objects.`aws mediastore delete-container \ --container-name=ExampleLiveDemo`This command produces no output. For more information, see [Deleting a Container](https://docs.aws.amazon.com/mediastore/latest/ug/containers-delete.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [DeleteContainer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-container.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-cors-policy`.

- **AWS CLI**
- 
            
                    **To delete a CORS policy**The following `delete-cors-policy`example deletes the cross-origin resource sharing (CORS) policy that is assigned to the specified container.`aws mediastore delete-cors-policy \ --container-name``ExampleContainer`This command produces no output. For more information, see [Deleting a CORS Policy](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy-deleting.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [DeleteCorsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-cors-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-lifecycle-policy`.

- **AWS CLI**
- 
            
                    **To delete an object lifecycle policy**The following `delete-lifecycle-policy`example deletes the object lifecycle policy attached to the specified container. This change can take up to 20 minutes to take effect.`aws mediastore delete-lifecycle-policy \ --container-name``LiveEvents`This command produces no output. For more information, see [Deleting an Object Lifecycle Policy](https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-delete.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [DeleteLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/delete-lifecycle-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-container`.

- **AWS CLI**
- 
            
                    **To view the details of a container**The following `describe-container`example displays the details of the specified container.`aws mediastore describe-container \ --container-name``ExampleContainer`Output: `{ "Container": { "CreationTime": 1563558086, "AccessLoggingEnabled": false, "ARN": "arn:aws:mediastore:us-west-2:111122223333:container/ExampleContainer", "Status": "ACTIVE", "Name": "ExampleContainer", "Endpoint": "https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com" } }`For more information, see [Viewing the Details for a Container](https://docs.aws.amazon.com/mediastore/latest/ug/containers-view-details.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [DescribeContainer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/describe-container.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-object`.

- **AWS CLI**
- 
            
                    **To view a list of objects and folders in a specific container**The following `describe-object`example displays items (objects and folders) stored in a specific container.`aws mediastore-data describe-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --path`/folder_name/file1234.jpg`Output: `{ "ContentType": "image/jpeg", "LastModified": "Fri, 19 Jul 2019 21:32:20 GMT", "ContentLength": "2307346", "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3" }`For more information, see [Viewing the Details of an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-view-details.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [DescribeObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/describe-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-container-policy`.

- **AWS CLI**
- 
            
                    **To view a container policy**The following `get-container-policy`example displays the resource-based policy of the specified container.`aws mediastore get-container-policy \ --container-name``ExampleLiveDemo`Output: `{ "Policy": { "Version":"2012-10-17", "Statement": [ { "Sid": "PublicReadOverHttps", "Effect": "Allow", "Principal": { "AWS": "arn:aws:iam::111122223333:root" }, "Action": [ "mediastore:GetObject", "mediastore:DescribeObject" ], "Resource": "arn:aws:mediastore:us-west-2:111122223333:container/ExampleLiveDemo/", "Condition": { "Bool": { "aws:SecureTransport": "true" } } } ] } }`For more information, see [Viewing a Container Policy](https://docs.aws.amazon.com/mediastore/latest/ug/policies-view.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [GetContainerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-container-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-cors-policy`.

- **AWS CLI**
- 
            
                    **To view a CORS policy**The following `get-cors-policy`example displays the cross-origin resource sharing (CORS) policy that is assigned to the specified container.`aws mediastore get-cors-policy \ --container-name``ExampleContainer`\ --region`us-west-2`Output: `{ "CorsPolicy": [ { "AllowedMethods": [ "GET", "HEAD" ], "MaxAgeSeconds": 3000, "AllowedOrigins": [ "" ], "AllowedHeaders": [ "" ] } ] }`For more information, see [Viewing a CORS Policy](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy-viewing.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [GetCorsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-cors-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-lifecycle-policy`.

- **AWS CLI**
- 
            
                    **To view an object lifecycle policy**The following `get-lifecycle-policy`example displays the object lifecycle policy attached to the specified container.`aws mediastore get-lifecycle-policy \ --container-name``LiveEvents`Output: `{ "LifecyclePolicy": { "rules": [ { "definition": { "path": [ { "prefix": "Football/" }, { "prefix": "Baseball/" } ], "days_since_create": [ { "numeric": [ ">", 28 ] } ] }, "action": "EXPIRE" } ] } }`For more information, see [Viewing an Object Lifecycle Policy](https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-view.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [GetLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-lifecycle-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object`.

- **AWS CLI**
- 
            
                    **To download an object**The following `get-object`example download an object to the specified endpoint.`aws mediastore-data get-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --path=/folder_name/`README.md`README.mdOutput: `{ "ContentLength": "2307346", "ContentType": "image/jpeg", "LastModified": "Fri, 19 Jul 2019 21:32:20 GMT", "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3", "StatusCode": 200 }`**To download part of an object**The following `get-object`example downloads a portion an object to the specified endpoint.`aws mediastore-data get-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --path`/folder_name/README.md`\ --range="bytes=0-100"`README2.md`Output: `{ "StatusCode": 206, "ContentRange": "bytes 0-100/2307346", "ContentLength": "101", "LastModified": "Fri, 19 Jul 2019 21:32:20 GMT", "ContentType": "image/jpeg", "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3" }`For more information, see [Downloading an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-download.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [GetObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/get-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-containers`.

- **AWS CLI**
- 
            
                    **To view a list of containers**The following `list-containers`example displays a list of all containers that are associated with your account.`aws mediastore list-containers`Output: `{ "Containers": [ { "CreationTime": 1505317931, "Endpoint": "https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com", "Status": "ACTIVE", "ARN": "arn:aws:mediastore:us-west-2:111122223333:container/ExampleLiveDemo", "AccessLoggingEnabled": false, "Name": "ExampleLiveDemo" }, { "CreationTime": 1506528818, "Endpoint": "https://fffggghhhiiijj.data.mediastore.us-west-2.amazonaws.com", "Status": "ACTIVE", "ARN": "arn:aws:mediastore:us-west-2:111122223333:container/ExampleContainer", "AccessLoggingEnabled": false, "Name": "ExampleContainer" } ] }`For more information, see [Viewing a List of Containers](https://docs.aws.amazon.com/mediastore/latest/ug/containers-view-list.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [ListContainers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/list-containers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-items`.

- **AWS CLI**
- 
            
                    **Example 1: To view a list of objects and folders in a specific container**The following `list-items`example displays items (objects and folders) stored in the specified container.`aws mediastore-data list-items \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`Output: `{ "Items": [ { "ContentType": "image/jpeg", "LastModified": 1563571859.379, "Name": "filename.jpg", "Type": "OBJECT", "ETag": "543ab21abcd1a234ab123456a1a2b12345ab12abc12a1234abc1a2bc12345a12", "ContentLength": 3784 }, { "Type": "FOLDER", "Name": "ExampleLiveDemo" } ] }`**Example 2: To view a list of objects and folders in a specific folder**The following `list-items`example displays items (objects and folders) stored in a specific folder.`aws mediastore-data list-items \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`Output: `{ "Items": [ { "ContentType": "image/jpeg", "LastModified": 1563571859.379, "Name": "filename.jpg", "Type": "OBJECT", "ETag": "543ab21abcd1a234ab123456a1a2b12345ab12abc12a1234abc1a2bc12345a12", "ContentLength": 3784 }, { "Type": "FOLDER", "Name": "ExampleLiveDemo" } ] }`For more information, see [Viewing a List of Objects](https://docs.aws.amazon.com/mediastore/latest/ug/objects-view-list.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [ListItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/list-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for a container**The following `list-tags-for-resource`example displays the tag keys and values assigned to the specified container.`aws mediastore list-tags-for-resource \ --resource``arn:aws:mediastore:us-west-2:1213456789012:container/ExampleContainer`Output: `{ "Tags": [ { "Value": "Test", "Key": "Environment" }, { "Value": "West", "Key": "Region" } ] }`For more information, see [ListTagsForResource](https://docs.aws.amazon.com/mediastore/latest/apireference/API_ListTagsForResource.html)in the*AWS Elemental MediaStore API Reference*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-container-policy`.

- **AWS CLI**
- 
            
                    **To edit a container policy**The following `put-container-policy`example assigns a different policy to the specified container. In this example, the updated policy is defined in a file named`LiveEventsContainerPolicy.json`.`aws mediastore put-container-policy \ --container-name``LiveEvents`\ --policy`file://LiveEventsContainerPolicy.json`This command produces no output. For more information, see [Editing a Container Policy](https://docs.aws.amazon.com/mediastore/latest/ug/policies-edit.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [PutContainerPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-container-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-cors-policy`.

- **AWS CLI**
- 
            
                    **Example 1: To add a CORS policy**The following `put-cors-policy`example adds a cross-origin resource sharing (CORS) policy to the specified container. The contents of the CORS policy are in the file named`corsPolicy.json`.`aws mediastore put-cors-policy \ --container-name``ExampleContainer`\ --cors-policy`file://corsPolicy.json`This command produces no output. For more information, see [Adding a CORS Policy to a Container](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy-adding.html)in the*AWS Elemental MediaStore User Guide*.**Example 2: To edit a CORS policy**The following `put-cors-policy`example updates the cross-origin resource sharing (CORS) policy that is assigned to the specified container. The contents of the updated CORS policy are in the file named`corsPolicy2.json`.For more information, see [Editing a CORS Policy](https://docs.aws.amazon.com/mediastore/latest/ug/cors-policy-editing.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [PutCorsPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-cors-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-lifecycle-policy`.

- **AWS CLI**
- 
            
                    **To create an object lifecycle policy**The following `put-lifecycle-policy`example attaches an object lifecycle policy to the specified container. This enables you to specify how long the service should store objects in your container. MediaStore deletes objects in the container once they reach their expiration date, as indicated in the policy, which is in the file named`LiveEventsLifecyclePolicy.json`.`aws mediastore put-lifecycle-policy \ --container-name``ExampleContainer`\ --lifecycle-policy`file://ExampleLifecyclePolicy.json`This command produces no output. For more information, see [Adding an Object Lifecycle Policy to a Container](https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle-add.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [PutLifecyclePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-lifecycle-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object`.

- **AWS CLI**
- 
            
                    **To upload an object**The following `put-object`example uploads an object to the specified container. You can specify a folder path where the object will be saved within the container. If the folder already exists, AWS Elemental MediaStore stores the object in the folder. If the folder doesn't exist, the service creates it, and then stores the object in the folder.`aws mediastore-data put-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --body`README.md`\ --path`/folder_name/README.md`\ --cache-control`"max-age=6, public"`\ --content-type`binary/octet-stream`Output: `{ "ContentSHA256": "74b5fdb517f423ed750ef214c44adfe2be36e37d861eafe9c842cbe1bf387a9d", "StorageClass": "TEMPORAL", "ETag": "af3e4731af032167a106015d1f2fe934e68b32ed1aa297a9e325f5c64979277b" }`For more information, see [Uploading an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-upload.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [PutObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/put-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-access-logging`.

- **AWS CLI**
- 
            
                    **To enable access logging on a container**The following `start-access-logging`example enable access logging on the specified container.`aws mediastore start-access-logging \ --container-name``LiveEvents`This command produces no output. For more information, see [Enabling Access Logging for a Container](https://docs.aws.amazon.com/mediastore/latest/ug/monitoring-cloudwatch-logs-enable.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [StartAccessLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/start-access-logging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-access-logging`.

- **AWS CLI**
- 
            
                    **To disable access logging on a container**The following `stop-access-logging`example disables access logging on the specified container.`aws mediastore stop-access-logging \ --container-name``LiveEvents`This command produces no output. For more information, see [Disabling Access Logging for a Container](https://docs.aws.amazon.com/mediastore/latest/ug/monitoring-cloudwatch-logs-disable.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [StopAccessLogging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/stop-access-logging.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To add tags to a container**The following `tag-resource`example adds tag keys and values to the specified container.`aws mediastore tag-resource \ --resource``arn:aws:mediastore:us-west-2:123456789012:container/ExampleContainer`\ --tags '`[{"Key": "Region", "Value": "West"}, {"Key": "Environment", "Value": "Test"}]`'This command produces no output. For more information, see [TagResource](https://docs.aws.amazon.com/mediastore/latest/apireference/API_TagResource.html)in the*AWS Elemental MediaStore API Reference*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove tags from a container**The following `untag-resource`example removes the specified tag key and its associated value from a container.`aws mediastore untag-resource \ --resource``arn:aws:mediastore:us-west-2:123456789012:container/ExampleContainer`\ --tag-keys`Region`This command produces no output. For more information, see [UntagResource](https://docs.aws.amazon.com/mediastore/latest/apireference/API_UntagResource.html)in the*AWS Elemental MediaStore API Reference.*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore/untag-resource.html)in*AWS CLI Command Reference*.
 
-