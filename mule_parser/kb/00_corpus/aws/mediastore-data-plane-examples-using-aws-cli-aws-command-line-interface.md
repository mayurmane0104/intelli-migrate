# MediaStore Data Plane examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_mediastore-data_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_mediastore-data_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with MediaStore Data Plane.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-object`.

- **AWS CLI**
- 
            
                    **To delete an object**The following `delete-object`example deletes the specified object.`aws mediastore-data delete-object \ --endpoint=https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com \ --path=/folder_name/README.md`This command produces no output. For more information, see [Deleting an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-delete.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [DeleteObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/delete-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-object`.

- **AWS CLI**
- 
            
                    **To view the headers for an object**The following `describe-object`example displays the headers for an object at the specified path.`aws mediastore-data describe-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --path`events/baseball/setup.jpg`Output: `{ "LastModified": "Fri, 19 Jul 2019 21:50:31 GMT", "ContentType": "image/jpeg", "ContentLength": "3860266", "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3" }`For more information, see [Viewing the Details of an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-view-details.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [DescribeObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/describe-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-object`.

- **AWS CLI**
- 
            
                    **Example 1: To download an entire object**The following `get-object`example downloads the specified object.`aws mediastore-data get-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --path`events/baseball/setup.jpg``setup.jpg`Output: `{ "ContentType": "image/jpeg", "StatusCode": 200, "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3", "ContentLength": "3860266", "LastModified": "Fri, 19 Jul 2019 21:50:31 GMT" }`**Example 2: To download part of an object**The following `get-object`example downloads the specified part of an object.`aws mediastore-data get-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --path`events/baseball/setup.jpg``setup.jpg`\ --range`"bytes=0-100"`Output: `{ "StatusCode": 206, "LastModified": "Fri, 19 Jul 2019 21:50:31 GMT", "ContentType": "image/jpeg", "ContentRange": "bytes 0-100/3860266", "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3", "ContentLength": "101" }`For more information, see [Downloading an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-download.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [GetObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/get-object.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-items`.

- **AWS CLI**
- 
            
                    **Example 1: To view a list of items (objects and folders) stored in a container**The following `list-items`example displays a list of items (objects and folders) stored in the specified container.`aws mediastore-data list-items \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`Output: `{ "Items": [ { "Type": "OBJECT", "ContentLength": 3784, "Name": "setup.jpg", "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3", "ContentType": "image/jpeg", "LastModified": 1563571859.379 }, { "Type": "FOLDER", "Name": "events" } ] }`**Example 2: To view a list of items (objects and folders) stored in a folder**The following `list-items`example displays a list of items (objects and folders) stored in the specified folder.`aws mediastore-data list-items \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --path`events/baseball`Output: `{ "Items": [ { "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3", "ContentType": "image/jpeg", "Type": "OBJECT", "ContentLength": 3860266, "LastModified": 1563573031.872, "Name": "setup.jpg" } ] }`For more information, see [Viewing a List of Objects](https://docs.aws.amazon.com/mediastore/latest/ug/objects-view-list.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [ListItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/list-items.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-object`.

- **AWS CLI**
- 
            
                    **Example 1: To upload an object to a container**The following `put-object`example upload an object to the specified container.`aws mediastore-data put-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --body`ReadMe.md`\ --path`ReadMe.md`\ --cache-control`"max-age=6, public"`\ --content-type`binary/octet-stream`Output: `{ "ContentSHA256": "f29bc64a9d3732b4b9035125fdb3285f5b6455778edca72414671e0ca3b2e0de", "StorageClass": "TEMPORAL", "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3" }`**Example 2: To upload an object to a folder within a container**The following `put-object`example upload an object to the specified folder within a container.`aws mediastore-data put-object \ --endpoint``https://aaabbbcccdddee.data.mediastore.us-west-2.amazonaws.com`\ --body`ReadMe.md`\ --path`/september-events/ReadMe.md`\ --cache-control`"max-age=6, public"`\ --content-type`binary/octet-stream`Output: `{ "ETag": "2aa333bbcc8d8d22d777e999c88d4aa9eeeeee4dd89ff7f555555555555da6d3", "ContentSHA256": "f29bc64a9d3732b4b9035125fdb3285f5b6455778edca72414671e0ca3b2e0de", "StorageClass": "TEMPORAL" }`For more information, see [Uploading an Object](https://docs.aws.amazon.com/mediastore/latest/ug/objects-upload.html)in the*AWS Elemental MediaStore User Guide*.- 
                    For API details, see [PutObject](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediastore-data/put-object.html)in*AWS CLI Command Reference*.
 
-