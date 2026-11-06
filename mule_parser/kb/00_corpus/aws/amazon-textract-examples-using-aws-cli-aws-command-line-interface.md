# Amazon Textract examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_textract_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_textract_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Textract.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `analyze-document`.

- **AWS CLI**
- 
            
                    **To analyze text in a document**The following `analyze-document`example shows how to analyze text in a document.Linux/macOS: `aws textract analyze-document \ --document '``{"S3Object":{"Bucket":"bucket","Name":"document"}}`' \ --feature-types '`["TABLES","FORMS"]`'Windows: `aws textract analyze-document \ --document "{\"S3Object\":{\"Bucket\":\"bucket\",\"Name\":\"document\"}}" \ --feature-types "[\"TABLES\",\"FORMS\"]" \ --region``region-name`Output: `{ "Blocks": [ { "Geometry": { "BoundingBox": { "Width": 1.0, "Top": 0.0, "Left": 0.0, "Height": 1.0 }, "Polygon": [ { "Y": 0.0, "X": 0.0 }, { "Y": 0.0, "X": 1.0 }, { "Y": 1.0, "X": 1.0 }, { "Y": 1.0, "X": 0.0 } ] }, "Relationships": [ { "Type": "CHILD", "Ids": [ "87586964-d50d-43e2-ace5-8a890657b9a0", "a1e72126-21d9-44f4-a8d6-5c385f9002ba", "e889d012-8a6b-4d2e-b7cd-7a8b327d876a" ] } ], "BlockType": "PAGE", "Id": "c2227f12-b25d-4e1f-baea-1ee180d926b2" } ], "DocumentMetadata": { "Pages": 1 } }`For more information, see Analyzing Document Text with Amazon Textract in the *Amazon Textract Developers Guide*- 
                    For API details, see [AnalyzeDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/analyze-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-document-text`.

- **AWS CLI**
- 
            
                    **To detect text in a document**The following `detect-document-text`The following example shows how to detect text in a document.Linux/macOS: `aws textract detect-document-text \ --document '``{"S3Object":{"Bucket":"bucket","Name":"document"}}`'Windows: `aws textract detect-document-text \ --document "{\"S3Object\":{\"Bucket\":\"bucket\",\"Name\":\"document\"}}" \ --region``region-name`Output: `{ "Blocks": [ { "Geometry": { "BoundingBox": { "Width": 1.0, "Top": 0.0, "Left": 0.0, "Height": 1.0 }, "Polygon": [ { "Y": 0.0, "X": 0.0 }, { "Y": 0.0, "X": 1.0 }, { "Y": 1.0, "X": 1.0 }, { "Y": 1.0, "X": 0.0 } ] }, "Relationships": [ { "Type": "CHILD", "Ids": [ "896a9f10-9e70-4412-81ce-49ead73ed881", "0da18623-dc4c-463d-a3d1-9ac050e9e720", "167338d7-d38c-4760-91f1-79a8ec457bb2" ] } ], "BlockType": "PAGE", "Id": "21f0535e-60d5-4bc7-adf2-c05dd851fa25" }, { "Relationships": [ { "Type": "CHILD", "Ids": [ "62490c26-37ea-49fa-8034-7a9ff9369c9c", "1e4f3f21-05bd-4da9-ba10-15d01e66604c" ] } ], "Confidence": 89.11581420898438, "Geometry": { "BoundingBox": { "Width": 0.33642634749412537, "Top": 0.17169663310050964, "Left": 0.13885067403316498, "Height": 0.49159330129623413 }, "Polygon": [ { "Y": 0.17169663310050964, "X": 0.13885067403316498 }, { "Y": 0.17169663310050964, "X": 0.47527703642845154 }, { "Y": 0.6632899641990662, "X": 0.47527703642845154 }, { "Y": 0.6632899641990662, "X": 0.13885067403316498 } ] }, "Text": "He llo,", "BlockType": "LINE", "Id": "896a9f10-9e70-4412-81ce-49ead73ed881" }, { "Relationships": [ { "Type": "CHILD", "Ids": [ "19b28058-9516-4352-b929-64d7cef29daf" ] } ], "Confidence": 85.5694351196289, "Geometry": { "BoundingBox": { "Width": 0.33182239532470703, "Top": 0.23131252825260162, "Left": 0.5091826915740967, "Height": 0.3766750991344452 }, "Polygon": [ { "Y": 0.23131252825260162, "X": 0.5091826915740967 }, { "Y": 0.23131252825260162, "X": 0.8410050868988037 }, { "Y": 0.607987642288208, "X": 0.8410050868988037 }, { "Y": 0.607987642288208, "X": 0.5091826915740967 } ] }, "Text": "worlc", "BlockType": "LINE", "Id": "0da18623-dc4c-463d-a3d1-9ac050e9e720" } ], "DocumentMetadata": { "Pages": 1 } }`For more information, see Detecting Document Text with Amazon Textract in the *Amazon Textract Developers Guide*- 
                    For API details, see [DetectDocumentText](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/detect-document-text.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-document-analysis`.

- **AWS CLI**
- 
            
                    **To get the results of asynchronous text analysis of a multi-page document**The following `get-document-analysis`example shows how to get the results of asynchronous text analysis of a multi-page document.`aws textract get-document-analysis \ --job-id``df7cf32ebbd2a5de113535fcf4d921926a701b09b4e7d089f3aebadb41e0712b`\ --max-results`1000`Output: `{ "Blocks": [ { "Geometry": { "BoundingBox": { "Width": 1.0, "Top": 0.0, "Left": 0.0, "Height": 1.0 }, "Polygon": [ { "Y": 0.0, "X": 0.0 }, { "Y": 0.0, "X": 1.0 }, { "Y": 1.0, "X": 1.0 }, { "Y": 1.0, "X": 0.0 } ] }, "Relationships": [ { "Type": "CHILD", "Ids": [ "75966e64-81c2-4540-9649-d66ec341cd8f", "bb099c24-8282-464c-a179-8a9fa0a057f0", "5ebf522d-f9e4-4dc7-bfae-a288dc094595" ] } ], "BlockType": "PAGE", "Id": "247c28ee-b63d-4aeb-9af0-5f7ea8ba109e", "Page": 1 } ], "NextToken": "cY1W3eTFvoB0cH7YrKVudI4Gb0H8J0xAYLo8xI/JunCIPWCthaKQ+07n/ElyutsSy0+1VOImoTRmP1zw4P0RFtaeV9Bzhnfedpx1YqwB4xaGDA==", "DocumentMetadata": { "Pages": 1 }, "JobStatus": "SUCCEEDED" }`For more information, see Detecting and Analyzing Text in Multi-Page Documents in the *Amazon Textract Developers Guide*- 
                    For API details, see [GetDocumentAnalysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/get-document-analysis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-document-text-detection`.

- **AWS CLI**
- 
            
                    **To get the results of asynchronous text detection in a multi-page document**The following `get-document-text-detection`example shows how to get the results of asynchronous text detection in a multi-page document.`aws textract get-document-text-detection \ --job-id``57849a3dc627d4df74123dca269d69f7b89329c870c65bb16c9fd63409d200b9`\ --max-results`1000`Output `{ "Blocks": [ { "Geometry": { "BoundingBox": { "Width": 1.0, "Top": 0.0, "Left": 0.0, "Height": 1.0 }, "Polygon": [ { "Y": 0.0, "X": 0.0 }, { "Y": 0.0, "X": 1.0 }, { "Y": 1.0, "X": 1.0 }, { "Y": 1.0, "X": 0.0 } ] }, "Relationships": [ { "Type": "CHILD", "Ids": [ "1b926a34-0357-407b-ac8f-ec473160c6a9", "0c35dc17-3605-4c9d-af1a-d9451059df51", "dea3db8a-52c2-41c0-b50c-81f66f4aa758" ] } ], "BlockType": "PAGE", "Id": "84671a5e-8c99-43be-a9d1-6838965da33e", "Page": 1 } ], "NextToken": "GcqyoAJuZwujOT35EN4LCI3EUzMtiLq3nKyFFHvU5q1SaIdEBcSty+njNgoWwuMP/muqc96S4o5NzDqehhXvhkodMyVO5OJGyms5lsrCxibWJw==", "DocumentMetadata": { "Pages": 1 }, "JobStatus": "SUCCEEDED" }`For more information, see Detecting and Analyzing Text in Multi-Page Documents in the *Amazon Textract Developers Guide*- 
                    For API details, see [GetDocumentTextDetection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/get-document-text-detection.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-document-analysis`.

- **AWS CLI**
- 
            
                    **To start analyzing text in a multi-page document**The following `start-document-analysis`example shows how to start asynchronous analysis of text in a multi-page document.Linux/macOS: `aws textract start-document-analysis \ --document-location '``{"S3Object":{"Bucket":"bucket","Name":"document"}}`' \ --feature-types '`["TABLES","FORMS"]`' \ --notification-channel`"SNSTopicArn=arn:snsTopic,RoleArn=roleArn"`Windows: `aws textract start-document-analysis \ --document-location "{\"S3Object\":{\"Bucket\":\"bucket\",\"Name\":\"document\"}}" \ --feature-types "[\"TABLES\", \"FORMS\"]" \ --region``region-name`\ --notification-channel`"SNSTopicArn=arn:snsTopic,RoleArn=roleArn"`Output: `{ "JobId": "df7cf32ebbd2a5de113535fcf4d921926a701b09b4e7d089f3aebadb41e0712b" }`For more information, see Detecting and Analyzing Text in Multi-Page Documents in the *Amazon Textract Developers Guide*- 
                    For API details, see [StartDocumentAnalysis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-document-analysis.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-document-text-detection`.

- **AWS CLI**
- 
            
                    **To start detecting text in a multi-page document**The following `start-document-text-detection`example shows how to start asynchronous detection of text in a multi-page document.Linux/macOS: `aws textract start-document-text-detection \ --document-location '``{"S3Object":{"Bucket":"bucket","Name":"document"}}`' \ --notification-channel`"SNSTopicArn=arn:snsTopic,RoleArn=roleARN"`Windows: `aws textract start-document-text-detection \ --document-location "{\"S3Object\":{\"Bucket\":\"bucket\",\"Name\":\"document\"}}" \ --region``region-name`\ --notification-channel`"SNSTopicArn=arn:snsTopic,RoleArn=roleArn"`Output: `{ "JobId": "57849a3dc627d4df74123dca269d69f7b89329c870c65bb16c9fd63409d200b9" }`For more information, see Detecting and Analyzing Text in Multi-Page Documents in the *Amazon Textract Developers Guide*- 
                    For API details, see [StartDocumentTextDetection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/textract/start-document-text-detection.html)in*AWS CLI Command Reference*.
 
-