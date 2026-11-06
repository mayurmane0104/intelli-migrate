# Amazon Comprehend examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_comprehend_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_comprehend_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Comprehend.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `batch-detect-dominant-language`.

- **AWS CLI**
- 
            
                    **To detect the dominant language of multiple input texts**The following `batch-detect-dominant-language`example analyzes multiple input texts and returns the dominant language of each. The pre-trained models confidence score is also output for each prediction.`aws comprehend batch-detect-dominant-language \ --text-list``"Physics is the natural science that involves the study of matter and its motion and behavior through space and time, along with related concepts such as energy and force."`Output: `{ "ResultList": [ { "Index": 0, "Languages": [ { "LanguageCode": "en", "Score": 0.9986501932144165 } ] } ], "ErrorList": [] }`For more information, see [Dominant Language](https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [BatchDetectDominantLanguage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/batch-detect-dominant-language.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-detect-entities`.

- **AWS CLI**
- 
            
                    **To detect entities from multiple input texts**The following `batch-detect-entities`example analyzes multiple input texts and returns the named entities of each. The pre-trained model's confidence score is also output for each prediction.`aws compreh``en`d batch-detect-entities \ --language-code en \ --text-list`"Dear Jane, Your AnyCompany Financial Services LLC credit card account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st."``"Please send customer feedback to Sunshine Spa, 123 Main St, Anywhere or to Alice at AnySpa@example.com."`Output: `{ "ResultList": [ { "Index": 0, "Entities": [ { "Score": 0.9985517859458923, "Type": "PERSON", "Text": "Jane", "BeginOffset": 5, "EndOffset": 9 }, { "Score": 0.9767839312553406, "Type": "ORGANIZATION", "Text": "AnyCompany Financial Services, LLC", "BeginOffset": 16, "EndOffset": 50 }, { "Score": 0.9856694936752319, "Type": "OTHER", "Text": "1111-XXXX-1111-XXXX", "BeginOffset": 71, "EndOffset": 90 }, { "Score": 0.9652159810066223, "Type": "QUANTITY", "Text": ".53", "BeginOffset": 116, "EndOffset": 119 }, { "Score": 0.9986667037010193, "Type": "DATE", "Text": "July 31st", "BeginOffset": 135, "EndOffset": 144 } ] }, { "Index": 1, "Entities": [ { "Score": 0.720084547996521, "Type": "ORGANIZATION", "Text": "Sunshine Spa", "BeginOffset": 33, "EndOffset": 45 }, { "Score": 0.9865870475769043, "Type": "LOCATION", "Text": "123 Main St", "BeginOffset": 47, "EndOffset": 58 }, { "Score": 0.5895616412162781, "Type": "LOCATION", "Text": "Anywhere", "BeginOffset": 60, "EndOffset": 68 }, { "Score": 0.6809214353561401, "Type": "PERSON", "Text": "Alice", "BeginOffset": 75, "EndOffset": 80 }, { "Score": 0.9979087114334106, "Type": "OTHER", "Text": "AnySpa@example.com", "BeginOffset": 84, "EndOffset": 99 } ] } ], "ErrorList": [] }`For more information, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [BatchDetectEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/batch-detect-entities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-detect-key-phrases`.

- **AWS CLI**
- 
            
                    **To detect key phrases of multiple text inputs**The following `batch-detect-key-phrases`example analyzes multiple input texts and returns the key noun phrases of each. The pre-trained model's confidence score for each prediction is also output.`aws compreh``en`d batch-detect-key-phrases \ --language-code en \ --text-list`"Hello Zhang Wei, I am John, writing to you about the trip for next Saturday."``"Dear Jane, Your AnyCompany Financial Services LLC credit card account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st."``"Please send customer feedback to Sunshine Spa, 123 Main St, Anywhere or to Alice at AnySpa@example.com."`Output: `{ "ResultList": [ { "Index": 0, "KeyPhrases": [ { "Score": 0.99700927734375, "Text": "Zhang Wei", "BeginOffset": 6, "EndOffset": 15 }, { "Score": 0.9929308891296387, "Text": "John", "BeginOffset": 22, "EndOffset": 26 }, { "Score": 0.9997230172157288, "Text": "the trip", "BeginOffset": 49, "EndOffset": 57 }, { "Score": 0.9999470114707947, "Text": "next Saturday", "BeginOffset": 62, "EndOffset": 75 } ] }, { "Index": 1, "KeyPhrases": [ { "Score": 0.8358274102210999, "Text": "Dear Jane", "BeginOffset": 0, "EndOffset": 9 }, { "Score": 0.989359974861145, "Text": "Your AnyCompany Financial Services", "BeginOffset": 11, "EndOffset": 45 }, { "Score": 0.8812323808670044, "Text": "LLC credit card account 1111-XXXX-1111-XXXX", "BeginOffset": 47, "EndOffset": 90 }, { "Score": 0.9999381899833679, "Text": "a minimum payment", "BeginOffset": 95, "EndOffset": 112 }, { "Score": 0.9997439980506897, "Text": ".53", "BeginOffset": 116, "EndOffset": 119 }, { "Score": 0.996875524520874, "Text": "July 31st", "BeginOffset": 135, "EndOffset": 144 } ] }, { "Index": 2, "KeyPhrases": [ { "Score": 0.9990295767784119, "Text": "customer feedback", "BeginOffset": 12, "EndOffset": 29 }, { "Score": 0.9994127750396729, "Text": "Sunshine Spa", "BeginOffset": 33, "EndOffset": 45 }, { "Score": 0.9892991185188293, "Text": "123 Main St", "BeginOffset": 47, "EndOffset": 58 }, { "Score": 0.9969810843467712, "Text": "Alice", "BeginOffset": 75, "EndOffset": 80 }, { "Score": 0.9703696370124817, "Text": "AnySpa@example.com", "BeginOffset": 84, "EndOffset": 99 } ] } ], "ErrorList": [] }`For more information, see [Key Phrases](https://docs.aws.amazon.com/comprehend/latest/dg/how-key-phrases.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [BatchDetectKeyPhrases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/batch-detect-key-phrases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-detect-sentiment`.

- **AWS CLI**
- 
            
                    **To detect the prevailing sentiment of multiple input texts**The following `batch-detect-sentiment`example analyzes multiple input texts and returns the prevailing sentiment (`POSITIVE`,`NEUTRAL`,`MIXED`, or`NEGATIVE`, of each one).`aws comprehend batch-detect-sentiment \ --text-list``"That movie was very boring, I can't believe it was over four hours long."``"It is a beautiful day for hiking today."``"My meal was okay, I'm excited to try other restaurants."`\ --language-code`en`Output: `{ "ResultList": [ { "Index": 0, "Sentiment": "NEGATIVE", "SentimentScore": { "Positive": 0.00011316669406369328, "Negative": 0.9995445609092712, "Neutral": 0.00014722718333359808, "Mixed": 0.00019498742767609656 } }, { "Index": 1, "Sentiment": "POSITIVE", "SentimentScore": { "Positive": 0.9981263279914856, "Negative": 0.00015240783977787942, "Neutral": 0.0013876151060685515, "Mixed": 0.00033366199932061136 } }, { "Index": 2, "Sentiment": "MIXED", "SentimentScore": { "Positive": 0.15930435061454773, "Negative": 0.11471917480230331, "Neutral": 0.26897063851356506, "Mixed": 0.45700588822364807 } } ], "ErrorList": [] }`For more information, see [Sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [BatchDetectSentiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/batch-detect-sentiment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-detect-syntax`.

- **AWS CLI**
- 
            
                    **To inspect the syntax and parts of speech of words in multiple input texts**The following `batch-detect-syntax`example analyzes the syntax of multiple input texts and returns the different parts of speech. The pre-trained model's confidence score is also output for each prediction.`aws comprehend batch-detect-syntax \ --text-list``"It is a beautiful day."``"Can you please pass the salt?"``"Please pay the bill before the 31st."`\ --language-code`en`Output: `{ "ResultList": [ { "Index": 0, "SyntaxTokens": [ { "TokenId": 1, "Text": "It", "BeginOffset": 0, "EndOffset": 2, "PartOfSpeech": { "Tag": "PRON", "Score": 0.9999740719795227 } }, { "TokenId": 2, "Text": "is", "BeginOffset": 3, "EndOffset": 5, "PartOfSpeech": { "Tag": "VERB", "Score": 0.999937117099762 } }, { "TokenId": 3, "Text": "a", "BeginOffset": 6, "EndOffset": 7, "PartOfSpeech": { "Tag": "DET", "Score": 0.9999926686286926 } }, { "TokenId": 4, "Text": "beautiful", "BeginOffset": 8, "EndOffset": 17, "PartOfSpeech": { "Tag": "ADJ", "Score": 0.9987891912460327 } }, { "TokenId": 5, "Text": "day", "BeginOffset": 18, "EndOffset": 21, "PartOfSpeech": { "Tag": "NOUN", "Score": 0.9999778866767883 } }, { "TokenId": 6, "Text": ".", "BeginOffset": 21, "EndOffset": 22, "PartOfSpeech": { "Tag": "PUNCT", "Score": 0.9999974966049194 } } ] }, { "Index": 1, "SyntaxTokens": [ { "TokenId": 1, "Text": "Can", "BeginOffset": 0, "EndOffset": 3, "PartOfSpeech": { "Tag": "AUX", "Score": 0.9999770522117615 } }, { "TokenId": 2, "Text": "you", "BeginOffset": 4, "EndOffset": 7, "PartOfSpeech": { "Tag": "PRON", "Score": 0.9999986886978149 } }, { "TokenId": 3, "Text": "please", "BeginOffset": 8, "EndOffset": 14, "PartOfSpeech": { "Tag": "INTJ", "Score": 0.9681622385978699 } }, { "TokenId": 4, "Text": "pass", "BeginOffset": 15, "EndOffset": 19, "PartOfSpeech": { "Tag": "VERB", "Score": 0.9999874830245972 } }, { "TokenId": 5, "Text": "the", "BeginOffset": 20, "EndOffset": 23, "PartOfSpeech": { "Tag": "DET", "Score": 0.9999827146530151 } }, { "TokenId": 6, "Text": "salt", "BeginOffset": 24, "EndOffset": 28, "PartOfSpeech": { "Tag": "NOUN", "Score": 0.9995040893554688 } }, { "TokenId": 7, "Text": "?", "BeginOffset": 28, "EndOffset": 29, "PartOfSpeech": { "Tag": "PUNCT", "Score": 0.999998152256012 } } ] }, { "Index": 2, "SyntaxTokens": [ { "TokenId": 1, "Text": "Please", "BeginOffset": 0, "EndOffset": 6, "PartOfSpeech": { "Tag": "INTJ", "Score": 0.9997857809066772 } }, { "TokenId": 2, "Text": "pay", "BeginOffset": 7, "EndOffset": 10, "PartOfSpeech": { "Tag": "VERB", "Score": 0.9999252557754517 } }, { "TokenId": 3, "Text": "the", "BeginOffset": 11, "EndOffset": 14, "PartOfSpeech": { "Tag": "DET", "Score": 0.9999842643737793 } }, { "TokenId": 4, "Text": "bill", "BeginOffset": 15, "EndOffset": 19, "PartOfSpeech": { "Tag": "NOUN", "Score": 0.9999588131904602 } }, { "TokenId": 5, "Text": "before", "BeginOffset": 20, "EndOffset": 26, "PartOfSpeech": { "Tag": "ADP", "Score": 0.9958304762840271 } }, { "TokenId": 6, "Text": "the", "BeginOffset": 27, "EndOffset": 30, "PartOfSpeech": { "Tag": "DET", "Score": 0.9999947547912598 } }, { "TokenId": 7, "Text": "31st", "BeginOffset": 31, "EndOffset": 35, "PartOfSpeech": { "Tag": "NOUN", "Score": 0.9924124479293823 } }, { "TokenId": 8, "Text": ".", "BeginOffset": 35, "EndOffset": 36, "PartOfSpeech": { "Tag": "PUNCT", "Score": 0.9999955892562866 } } ] } ], "ErrorList": [] }`For more information, see [Syntax Analysis](https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [BatchDetectSyntax](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/batch-detect-syntax.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-detect-targeted-sentiment`.

- **AWS CLI**
- 
            
                    **To detect the sentiment and each named entity for multiple input texts**The following `batch-detect-targeted-sentiment`example analyzes multiple input texts and returns the named entities along with the prevailing sentiment attached to each entity. The pre-trained model's confidence score is also output for each prediction.`aws compreh``en`d batch-detect-targeted-sentiment \ --language-code en \ --text-list`"That movie was really boring, the original was way more entertaining"``"The trail is extra beautiful today."``"My meal was just okay."`Output: `{ "ResultList": [ { "Index": 0, "Entities": [ { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9999009966850281, "GroupScore": 1.0, "Text": "movie", "Type": "MOVIE", "MentionSentiment": { "Sentiment": "NEGATIVE", "SentimentScore": { "Positive": 0.13887299597263336, "Negative": 0.8057460188865662, "Neutral": 0.05525200068950653, "Mixed": 0.00012799999967683107 } }, "BeginOffset": 5, "EndOffset": 10 } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9921110272407532, "GroupScore": 1.0, "Text": "original", "Type": "MOVIE", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Positive": 0.9999989867210388, "Negative": 9.999999974752427e-07, "Neutral": 0.0, "Mixed": 0.0 } }, "BeginOffset": 34, "EndOffset": 42 } ] } ] }, { "Index": 1, "Entities": [ { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.7545599937438965, "GroupScore": 1.0, "Text": "trail", "Type": "OTHER", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Positive": 1.0, "Negative": 0.0, "Neutral": 0.0, "Mixed": 0.0 } }, "BeginOffset": 4, "EndOffset": 9 } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9999960064888, "GroupScore": 1.0, "Text": "today", "Type": "DATE", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Positive": 9.000000318337698e-06, "Negative": 1.9999999949504854e-06, "Neutral": 0.9999859929084778, "Mixed": 3.999999989900971e-06 } }, "BeginOffset": 29, "EndOffset": 34 } ] } ] }, { "Index": 2, "Entities": [ { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9999880194664001, "GroupScore": 1.0, "Text": "My", "Type": "PERSON", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Positive": 0.0, "Negative": 0.0, "Neutral": 1.0, "Mixed": 0.0 } }, "BeginOffset": 0, "EndOffset": 2 } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9995260238647461, "GroupScore": 1.0, "Text": "meal", "Type": "OTHER", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Positive": 0.04695599898695946, "Negative": 0.003226999891921878, "Neutral": 0.6091709733009338, "Mixed": 0.34064599871635437 } }, "BeginOffset": 3, "EndOffset": 7 } ] } ] } ], "ErrorList": [] }`For more information, see [Targeted Sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [BatchDetectTargetedSentiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/batch-detect-targeted-sentiment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `classify-document`.

- **AWS CLI**
- 
            
                    **To classify document with model-specific endpoint**The following `classify-document`example classifies a document with an endpoint of a custom model. The model in this example was trained on a dataset containing sms messages labeled as spam or non-spam, or, "ham".`aws comprehend classify-document \ --endpoint-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint`\ --text`"CONGRATULATIONS! TXT 1235550100 to win $5000"`Output: `{ "Classes": [ { "Name": "spam", "Score": 0.9998599290847778 }, { "Name": "ham", "Score": 0.00014001205272506922 } ] }`For more information, see [Custom Classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ClassifyDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/classify-document.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `contains-pii-entities`.

- **AWS CLI**
- 
            
                    **To analyze the input text for the presence of PII information**The following `contains-pii-entities`example analyzes the input text for the presence of personally identifiable information (PII) and returns the labels of identified PII entity types such as name, address, bank account number, or phone number.`aws compreh``en`d contains-pii-entities \ --language-code en \ --text`"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. Customer feedback for Sunshine Spa, 100 Main St, Anywhere. Send comments to Alice at AnySpa@example.com."`Output: `{ "Labels": [ { "Name": "NAME", "Score": 1.0 }, { "Name": "EMAIL", "Score": 1.0 }, { "Name": "BANK_ACCOUNT_NUMBER", "Score": 0.9995794296264648 }, { "Name": "BANK_ROUTING", "Score": 0.9173126816749573 }, { "Name": "CREDIT_DEBIT_NUMBER", "Score": 1.0 } }`For more information, see [Personally Identifiable Information (PII)](https://docs.aws.amazon.com/comprehend/latest/dg/pii.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ContainsPiiEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/contains-pii-entities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-dataset`.

- **AWS CLI**
- 
            
                    **To create a flywheel dataset**The following `create-dataset`example creates a dataset for a flywheel. This dataset will be used as additional training data as specified by the`--dataset-type`tag.`aws comprehend create-dataset \ --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity`\ --dataset-name`example-dataset`\ --dataset-type`"TRAIN"`\ --input-data-config`file://inputConfig.json`Contents of `file://inputConfig.json`:`{ "DataFormat": "COMPREHEND_CSV", "DocumentClassifierInputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/training-data.csv" } }`Output: `{ "DatasetArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity/dataset/example-dataset" }`For more information, see [Flywheel Overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in*Amazon Comprehend Developer Guide*.- 
                    For API details, see [CreateDataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-dataset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-document-classifier`.

- **AWS CLI**
- 
            
                    **To create a document classifier to categorize documents**The following `create-document-classifier`example begins the training process for a document classifier model. The training data file,`training.csv`, is located at the`--input-data-config`tag.`training.csv`is a two column document where the labels, or, classifications are provided in the first column and the documents are provided in the second column.`aws comprehend create-document-classifier \ --document-classifier-name``example-classifier`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/"`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/"`\ --language-code`en`Output: `{ "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier" }`For more information, see [Custom Classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [CreateDocumentClassifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-document-classifier.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-endpoint`.

- **AWS CLI**
- 
            
                    **To create an endpoint for a custom model**The following `create-endpoint`example creates an endpoint for synchronous inference for a previously trained custom model.`aws comprehend create-endpoint \ --endpoint-name``example-classifier-endpoint-1`\ --model-arn`arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier`\ --desired-inference-units`1`Output: `{ "EndpointArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint-1" }`For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [CreateEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-entity-recognizer`.

- **AWS CLI**
- 
            
                    **To create a custom entity recognizer**The following `create-entity-recognizer`example begins the training process for a custom entity recognizer model. This example uses a CSV file containing training documents,`raw_text.csv`, and a CSV entity list,`entity_list.csv`to train the model.`entity-list.csv`contains the following columns: text and type.`aws comprehend create-entity-recognizer \ --recognizer-name``example-entity-recognizer`--data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --input-data-config`"EntityTypes=[{Type=DEVICE}],Documents={S3Uri=s3://amzn-s3-demo-bucket/trainingdata/raw_text.csv},EntityList={S3Uri=s3://amzn-s3-demo-bucket/trainingdata/entity_list.csv}"`--language-code`en`Output: `{ "EntityRecognizerArn": "arn:aws:comprehend:us-west-2:111122223333:example-entity-recognizer/entityrecognizer1" }`For more information, see [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [CreateEntityRecognizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-entity-recognizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-flywheel`.

- **AWS CLI**
- 
            
                    **To create a flywheel**The following `create-flywheel`example creates a flywheel to orchestrate the ongoing training of either a document classification or entity recognition model. The flywheel in this example is created to manage an existing trained model specified by the`--active-model-arn`tag. When the flywheel is created, a data lake is created at the`--input-data-lake`tag.`aws comprehend create-flywheel \ --flywheel-name``example-flywheel`\ --active-model-arn`arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-model/version/1`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --data-lake-s3-uri`"s3://amzn-s3-demo-bucket"`Output: `{ "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel" }`For more information, see [Flywheel Overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in*Amazon Comprehend Developer Guide*.- 
                    For API details, see [CreateFlywheel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/create-flywheel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-document-classifier`.

- **AWS CLI**
- 
            
                    **To delete a custom document classifier**The following `delete-document-classifier`example deletes a custom document classifier model.`aws comprehend delete-document-classifier \ --document-classifier-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier-1`This command produces no output. For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DeleteDocumentClassifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-document-classifier.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-endpoint`.

- **AWS CLI**
- 
            
                    **To delete an endpoint for a custom model**The following `delete-endpoint`example deletes a model-specific endpoint. All endpoints must be deleted in order for the model to be deleted.`aws comprehend delete-endpoint \ --endpoint-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint-1`This command produces no output. For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DeleteEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-entity-recognizer`.

- **AWS CLI**
- 
            
                    **To delete a custom entity recognizer model**The following `delete-entity-recognizer`example deletes a custom entity recognizer model.`aws comprehend delete-entity-recognizer \ --entity-recognizer-arn``arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/example-entity-recognizer-1`This command produces no output. For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DeleteEntityRecognizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-entity-recognizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-flywheel`.

- **AWS CLI**
- 
            
                    **To delete a flywheel**The following `delete-flywheel`example deletes a flywheel. The data lake or the model associated with the flywheel is not deleted.`aws comprehend delete-flywheel \ --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel-1`This command produces no output. For more information, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DeleteFlywheel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-flywheel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-resource-policy`.

- **AWS CLI**
- 
            
                    **To delete a resource-based policy**The following `delete-resource-policy`example deletes a resource-based policy from an Amazon Comprehend resource.`aws comprehend delete-resource-policy \ --resource-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier-1/version/1`This command produces no output. For more information, see [Copying custom models between AWS accounts](https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DeleteResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/delete-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-dataset`.

- **AWS CLI**
- 
            
                    **To describe a flywheel dataset**The following `describe-dataset`example gets the properties of a flywheel dataset.`aws comprehend describe-dataset \ --dataset-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity/dataset/example-dataset`Output: `{ "DatasetProperties": { "DatasetArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity/dataset/example-dataset", "DatasetName": "example-dataset", "DatasetType": "TRAIN", "DatasetS3Uri": "s3://amzn-s3-demo-bucket/flywheel-entity/schemaVersion=1/12345678A123456Z/datasets/example-dataset/20230616T203710Z/", "Status": "CREATING", "CreationTime": "2023-06-16T20:37:10.400000+00:00" } }`For more information, see [Flywheel Overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeDataset](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-dataset.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-document-classification-job`.

- **AWS CLI**
- 
            
                    **To describe a document classification job**The following `describe-document-classification-job`example gets the properties of an asynchronous document classification job.`aws comprehend describe-document-classification-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "DocumentClassificationJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:document-classification-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "exampleclassificationjob", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-14T17:09:51.788000+00:00", "EndTime": "2023-06-14T17:15:58.582000+00:00", "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/mymodel/version/1", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/jobdata/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-CLN-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-servicerole" } }`For more information, see [Custom Classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeDocumentClassificationJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-document-classification-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-document-classifier`.

- **AWS CLI**
- 
            
                    **To describe a document classifier**The following `describe-document-classifier`example gets the properties of a custom document classifier model.`aws comprehend describe-document-classifier \ --document-classifier-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier-1`Output: `{ "DocumentClassifierProperties": { "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier-1", "LanguageCode": "en", "Status": "TRAINED", "SubmitTime": "2023-06-13T19:04:15.735000+00:00", "EndTime": "2023-06-13T19:42:31.752000+00:00", "TrainingStartTime": "2023-06-13T19:08:20.114000+00:00", "TrainingEndTime": "2023-06-13T19:41:35.080000+00:00", "InputDataConfig": { "DataFormat": "COMPREHEND_CSV", "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata" }, "OutputDataConfig": {}, "ClassifierMetadata": { "NumberOfLabels": 3, "NumberOfTrainedDocuments": 5016, "NumberOfTestDocuments": 557, "EvaluationMetrics": { "Accuracy": 0.9856, "Precision": 0.9919, "Recall": 0.9459, "F1Score": 0.9673, "MicroPrecision": 0.9856, "MicroRecall": 0.9856, "MicroF1Score": 0.9856, "HammingLoss": 0.0144 } }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role", "Mode": "MULTI_CLASS" } }`For more information, see [Creating and managing custom models](https://docs.aws.amazon.com/comprehend/latest/dg/manage-models.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeDocumentClassifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-document-classifier.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-dominant-language-detection-job`.

- **AWS CLI**
- 
            
                    **To describe a dominant language detection detection job.**The following `describe-dominant-language-detection-job`example gets the properties of an asynchronous dominant language detection job.`aws comprehend describe-dominant-language-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "DominantLanguageDetectionJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "languageanalysis1", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-09T18:10:38.037000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-LANGUAGE-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeDominantLanguageDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-dominant-language-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-endpoint`.

- **AWS CLI**
- 
            
                    **To describe a specific endpoint**The following `describe-endpoint`example gets the properties of a model-specific endpoint.`aws comprehend describe-endpoint \ --endpoint-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint`Output: `{ "EndpointProperties": { "EndpointArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint, "Status": "IN_SERVICE", "ModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier1", "DesiredModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier1", "DesiredInferenceUnits": 1, "CurrentInferenceUnits": 1, "CreationTime": "2023-06-13T20:32:54.526000+00:00", "LastModifiedTime": "2023-06-13T20:32:54.526000+00:00" } }`For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-entities-detection-job`.

- **AWS CLI**
- 
            
                    **To describe an entities detection job**The following `describe-entities-detection-job`example gets the properties of an asynchronous entities detection job.`aws comprehend describe-entities-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "EntitiesDetectionJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "example-entity-detector", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-08T21:30:15.323000+00:00", "EndTime": "2023-06-08T21:40:23.509000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/thefolder/111122223333-NER-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::12345678012:role/service-role/AmazonComprehendServiceRole-example-role" } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeEntitiesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-entities-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-entity-recognizer`.

- **AWS CLI**
- 
            
                    **To describe an entity recognizer**The following `describe-entity-recognizer`example gets the properties of a custom entity recognizer model.`aws comprehend describe-entity-recognizer \ --entity-recognizer-arn``arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/business-recongizer-1/version/1`Output: `{ "EntityRecognizerProperties": { "EntityRecognizerArn": "arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/business-recongizer-1/version/1", "LanguageCode": "en", "Status": "TRAINED", "SubmitTime": "2023-06-14T20:44:59.631000+00:00", "EndTime": "2023-06-14T20:59:19.532000+00:00", "TrainingStartTime": "2023-06-14T20:48:52.811000+00:00", "TrainingEndTime": "2023-06-14T20:58:11.473000+00:00", "InputDataConfig": { "DataFormat": "COMPREHEND_CSV", "EntityTypes": [ { "Type": "BUSINESS" } ], "Documents": { "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/dataset/", "InputFormat": "ONE_DOC_PER_LINE" }, "EntityList": { "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/entity.csv" } }, "RecognizerMetadata": { "NumberOfTrainedDocuments": 1814, "NumberOfTestDocuments": 486, "EvaluationMetrics": { "Precision": 100.0, "Recall": 100.0, "F1Score": 100.0 }, "EntityTypes": [ { "Type": "BUSINESS", "EvaluationMetrics": { "Precision": 100.0, "Recall": 100.0, "F1Score": 100.0 }, "NumberOfTrainMentions": 1520 } ] }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role", "VersionName": "1" } }`For more information, see [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeEntityRecognizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-entity-recognizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-events-detection-job`.

- **AWS CLI**
- 
            
                    **To describe an events detection job.**The following `describe-events-detection-job`example gets the properties of an asynchronous events detection job.`aws comprehend describe-events-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "EventsDetectionJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:events-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "events_job_1", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-12T18:45:56.054000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/EventsData", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-EVENTS-123456abcdeb0e11022f22a11EXAMPLE/output/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role", "TargetEventTypes": [ "BANKRUPTCY", "EMPLOYMENT", "CORPORATE_ACQUISITION", "CORPORATE_MERGER", "INVESTMENT_GENERAL" ] } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeEventsDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-events-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-flywheel-iteration`.

- **AWS CLI**
- 
            
                    **To describe a flywheel iteration**The following `describe-flywheel-iteration`example gets the properties of a flywheel iteration.`aws comprehend describe-flywheel-iteration \ --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel`\ --flywheel-iteration-id`20232222AEXAMPLE`Output: `{ "FlywheelIterationProperties": { "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity", "FlywheelIterationId": "20232222AEXAMPLE", "CreationTime": "2023-06-16T21:10:26.385000+00:00", "EndTime": "2023-06-16T23:33:16.827000+00:00", "Status": "COMPLETED", "Message": "FULL_ITERATION: Flywheel iteration performed all functions successfully.", "EvaluatedModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1", "EvaluatedModelMetrics": { "AverageF1Score": 0.7742663922375772, "AveragePrecision": 0.8287636394041166, "AverageRecall": 0.7427084833645399, "AverageAccuracy": 0.8795394154118689 }, "TrainedModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/Comprehend-Generated-v1-bb52d585", "TrainedModelMetrics": { "AverageF1Score": 0.9767700253081214, "AveragePrecision": 0.9767700253081214, "AverageRecall": 0.9767700253081214, "AverageAccuracy": 0.9858281665190434 }, "EvaluationManifestS3Prefix": "s3://amzn-s3-demo-destination-bucket/flywheel-entity/schemaVersion=1/20230616T200543Z/evaluation/20230616T211026Z/" } }`For more information, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeFlywheelIteration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-flywheel-iteration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-flywheel`.

- **AWS CLI**
- 
            
                    **To describe a flywheel**The following `describe-flywheel`example gets the properties of a flywheel. In this example, the model associated with the flywheel is a custom classifier model that is trained to classify documents as either spam or nonspam, or, "ham".`aws comprehend describe-flywheel \ --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel`Output: `{ "FlywheelProperties": { "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel", "ActiveModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-model/version/1", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role", "TaskConfig": { "LanguageCode": "en", "DocumentClassificationConfig": { "Mode": "MULTI_CLASS", "Labels": [ "ham", "spam" ] } }, "DataLakeS3Uri": "s3://amzn-s3-demo-bucket/example-flywheel/schemaVersion=1/20230616T200543Z/", "DataSecurityConfig": {}, "Status": "ACTIVE", "ModelType": "DOCUMENT_CLASSIFIER", "CreationTime": "2023-06-16T20:05:43.242000+00:00", "LastModifiedTime": "2023-06-16T20:21:43.567000+00:00" } }`For more information, see [Flywheel Overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeFlywheel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-flywheel.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-key-phrases-detection-job`.

- **AWS CLI**
- 
            
                    **To describe a key phrases detection job**The following `describe-key-phrases-detection-job`example gets the properties of an asynchronous key phrases detection job.`aws comprehend describe-key-phrases-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "KeyPhrasesDetectionJobProperties": { "JobId": "69aa080c00fc68934a6a98f10EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/69aa080c00fc68934a6a98f10EXAMPLE", "JobName": "example-key-phrases-detection-job", "JobStatus": "COMPLETED", "SubmitTime": 1686606439.177, "EndTime": 1686606806.157, "InputDataConfig": { "S3Uri": "s3://dereksbucket1001/EventsData/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://dereksbucket1002/testfolder/111122223333-KP-69aa080c00fc68934a6a98f10EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-testrole" } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeKeyPhrasesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-key-phrases-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-pii-entities-detection-job`.

- **AWS CLI**
- 
            
                    **To describe a PII entities detection job**The following `describe-pii-entities-detection-job`example gets the properties of an asynchronous pii entities detection job.`aws comprehend describe-pii-entities-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "PiiEntitiesDetectionJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "example-pii-entities-job", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-08T21:30:15.323000+00:00", "EndTime": "2023-06-08T21:40:23.509000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/thefolder/111122223333-NER-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::12345678012:role/service-role/AmazonComprehendServiceRole-example-role" } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribePiiEntitiesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-pii-entities-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-resource-policy`.

- **AWS CLI**
- 
            
                    **To describe a resource policy attached to a model**The following `describe-resource-policy`example gets the properties of a resource-based policy attached to a model.`aws comprehend describe-resource-policy \ --resource-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1`Output: `{ "ResourcePolicy": "{\"Version\":\"2012-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::444455556666:root\"},\"Action\":\"comprehend:ImportModel\",\"Resource\":\"*\"}]}", "CreationTime": "2023-06-19T18:44:26.028000+00:00", "LastModifiedTime": "2023-06-19T18:53:02.002000+00:00", "PolicyRevisionId": "baa675d069d07afaa2aa3106ae280f61" }`For more information, see [Copying custom models between AWS accounts](https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-sentiment-detection-job`.

- **AWS CLI**
- 
            
                    **To describe a sentiment detection job**The following `describe-sentiment-detection-job`example gets the properties of an asynchronous sentiment detection job.`aws comprehend describe-sentiment-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "SentimentDetectionJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "movie_review_analysis", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-09T23:16:15.956000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/MovieData", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TS-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-servicerole" } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeSentimentDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-sentiment-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-targeted-sentiment-detection-job`.

- **AWS CLI**
- 
            
                    **To describe a targeted sentiment detection job**The following `describe-targeted-sentiment-detection-job`example gets the properties of an asynchronous targeted sentiment detection job.`aws comprehend describe-targeted-sentiment-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "TargetedSentimentDetectionJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "movie_review_analysis", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-09T23:16:15.956000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/MovieData", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TS-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-servicerole" } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeTargetedSentimentDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-targeted-sentiment-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `describe-topics-detection-job`.

- **AWS CLI**
- 
            
                    **To describe a topics detection job**The following `describe-topics-detection-job`example gets the properties of an asynchronous topics detection job.`aws comprehend describe-topics-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "TopicsDetectionJobProperties": { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:topics-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "example_topics_detection", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-09T18:44:43.414000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TOPICS-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "NumberOfTopics": 10, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-examplerole" } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DescribeTopicsDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/describe-topics-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-dominant-language`.

- **AWS CLI**
- 
            
                    **To detect the dominant language of input text**The following `detect-dominant-language`analyzes the input text and identifies the dominant language. The pre-trained model's confidence score is also output.`aws comprehend detect-dominant-language \ --text``"It is a beautiful day in Seattle."`Output: `{ "Languages": [ { "LanguageCode": "en", "Score": 0.9877256155014038 } ] }`For more information, see [Dominant Language](https://docs.aws.amazon.com/comprehend/latest/dg/how-languages.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DetectDominantLanguage](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-dominant-language.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-entities`.

- **AWS CLI**
- 
            
                    **To detect named entities in input text**The following `detect-entities`example analyzes the input text and returns the named entities. The pre-trained model's confidence score is also output for each prediction.`aws compreh``en`d detect-entities \ --language-code en \ --text`"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card \ account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, \ we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. \ Customer feedback for Sunshine Spa, 123 Main St, Anywhere. Send comments to Alice at AnySpa@example.com."`Output: `{ "Entities": [ { "Score": 0.9994556307792664, "Type": "PERSON", "Text": "Zhang Wei", "BeginOffset": 6, "EndOffset": 15 }, { "Score": 0.9981022477149963, "Type": "PERSON", "Text": "John", "BeginOffset": 22, "EndOffset": 26 }, { "Score": 0.9986887574195862, "Type": "ORGANIZATION", "Text": "AnyCompany Financial Services, LLC", "BeginOffset": 33, "EndOffset": 67 }, { "Score": 0.9959119558334351, "Type": "OTHER", "Text": "1111-XXXX-1111-XXXX", "BeginOffset": 88, "EndOffset": 107 }, { "Score": 0.9708039164543152, "Type": "QUANTITY", "Text": ".53", "BeginOffset": 133, "EndOffset": 136 }, { "Score": 0.9987268447875977, "Type": "DATE", "Text": "July 31st", "BeginOffset": 152, "EndOffset": 161 }, { "Score": 0.9858865737915039, "Type": "OTHER", "Text": "XXXXXX1111", "BeginOffset": 271, "EndOffset": 281 }, { "Score": 0.9700471758842468, "Type": "OTHER", "Text": "XXXXX0000", "BeginOffset": 306, "EndOffset": 315 }, { "Score": 0.9591118693351746, "Type": "ORGANIZATION", "Text": "Sunshine Spa", "BeginOffset": 340, "EndOffset": 352 }, { "Score": 0.9797496795654297, "Type": "LOCATION", "Text": "123 Main St", "BeginOffset": 354, "EndOffset": 365 }, { "Score": 0.994929313659668, "Type": "PERSON", "Text": "Alice", "BeginOffset": 394, "EndOffset": 399 }, { "Score": 0.9949769377708435, "Type": "OTHER", "Text": "AnySpa@example.com", "BeginOffset": 403, "EndOffset": 418 } ] }`For more information, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DetectEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-entities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-key-phrases`.

- **AWS CLI**
- 
            
                    **To detect key phrases in input text**The following `detect-key-phrases`example analyzes the input text and identifies the key noun phrases. The pre-trained model's confidence score is also output for each prediction.`aws compreh``en`d detect-key-phrases \ --language-code en \ --text`"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card \ account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, \ we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. \ Customer feedback for Sunshine Spa, 123 Main St, Anywhere. Send comments to Alice at AnySpa@example.com."`Output: `{ "KeyPhrases": [ { "Score": 0.8996376395225525, "Text": "Zhang Wei", "BeginOffset": 6, "EndOffset": 15 }, { "Score": 0.9992469549179077, "Text": "John", "BeginOffset": 22, "EndOffset": 26 }, { "Score": 0.988385021686554, "Text": "Your AnyCompany Financial Services", "BeginOffset": 28, "EndOffset": 62 }, { "Score": 0.8740853071212769, "Text": "LLC credit card account 1111-XXXX-1111-XXXX", "BeginOffset": 64, "EndOffset": 107 }, { "Score": 0.9999437928199768, "Text": "a minimum payment", "BeginOffset": 112, "EndOffset": 129 }, { "Score": 0.9998900890350342, "Text": ".53", "BeginOffset": 133, "EndOffset": 136 }, { "Score": 0.9979453086853027, "Text": "July 31st", "BeginOffset": 152, "EndOffset": 161 }, { "Score": 0.9983011484146118, "Text": "your autopay settings", "BeginOffset": 172, "EndOffset": 193 }, { "Score": 0.9996572136878967, "Text": "your payment", "BeginOffset": 211, "EndOffset": 223 }, { "Score": 0.9995037317276001, "Text": "the due date", "BeginOffset": 227, "EndOffset": 239 }, { "Score": 0.9702621698379517, "Text": "your bank account number XXXXXX1111", "BeginOffset": 245, "EndOffset": 280 }, { "Score": 0.9179925918579102, "Text": "the routing number XXXXX0000.Customer feedback", "BeginOffset": 286, "EndOffset": 332 }, { "Score": 0.9978160858154297, "Text": "Sunshine Spa", "BeginOffset": 337, "EndOffset": 349 }, { "Score": 0.9706913232803345, "Text": "123 Main St", "BeginOffset": 351, "EndOffset": 362 }, { "Score": 0.9941995143890381, "Text": "comments", "BeginOffset": 379, "EndOffset": 387 }, { "Score": 0.9759287238121033, "Text": "Alice", "BeginOffset": 391, "EndOffset": 396 }, { "Score": 0.8376792669296265, "Text": "AnySpa@example.com", "BeginOffset": 400, "EndOffset": 415 } ] }`For more information, see [Key Phrases](https://docs.aws.amazon.com/comprehend/latest/dg/how-key-phrases.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DetectKeyPhrases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-key-phrases.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-pii-entities`.

- **AWS CLI**
- 
            
                    **To detect pii entities in input text**The following `detect-pii-entities`example analyzes the input text and identifies entities that contain personally identifiable information (PII). The pre-trained model's confidence score is also output for each prediction.`aws compreh``en`d detect-pii-entities \ --language-code en \ --text`"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card \ account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st. Based on your autopay settings, \ we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. \ Customer feedback for Sunshine Spa, 123 Main St, Anywhere. Send comments to Alice at AnySpa@example.com."`Output: `{ "Entities": [ { "Score": 0.9998322129249573, "Type": "NAME", "BeginOffset": 6, "EndOffset": 15 }, { "Score": 0.9998878240585327, "Type": "NAME", "BeginOffset": 22, "EndOffset": 26 }, { "Score": 0.9994089603424072, "Type": "CREDIT_DEBIT_NUMBER", "BeginOffset": 88, "EndOffset": 107 }, { "Score": 0.9999760985374451, "Type": "DATE_TIME", "BeginOffset": 152, "EndOffset": 161 }, { "Score": 0.9999449253082275, "Type": "BANK_ACCOUNT_NUMBER", "BeginOffset": 271, "EndOffset": 281 }, { "Score": 0.9999847412109375, "Type": "BANK_ROUTING", "BeginOffset": 306, "EndOffset": 315 }, { "Score": 0.999925434589386, "Type": "ADDRESS", "BeginOffset": 354, "EndOffset": 365 }, { "Score": 0.9989161491394043, "Type": "NAME", "BeginOffset": 394, "EndOffset": 399 }, { "Score": 0.9994171857833862, "Type": "EMAIL", "BeginOffset": 403, "EndOffset": 418 } ] }`For more information, see [Personally Identifiable Information (PII)](https://docs.aws.amazon.com/comprehend/latest/dg/pii.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DetectPiiEntities](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-pii-entities.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-sentiment`.

- **AWS CLI**
- 
            
                    **To detect the sentiment of an input text**The following `detect-sentiment`example analyzes the input text and returns an inference of the prevailing sentiment (`POSITIVE`,`NEUTRAL`,`MIXED`, or`NEGATIVE`).`aws compreh``en`d detect-sentiment \ --language-code en \ --text`"It is a beautiful day in Seattle"`Output: `{ "Sentiment": "POSITIVE", "SentimentScore": { "Positive": 0.9976957440376282, "Negative": 9.653854067437351e-05, "Neutral": 0.002169104292988777, "Mixed": 3.857641786453314e-05 } }`For more information, see [Sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-sentiment.html)in the*Amazon Comprehend Developer Guide*- 
                    For API details, see [DetectSentiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-sentiment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-syntax`.

- **AWS CLI**
- 
            
                    **To detect the parts of speech in an input text**The following `detect-syntax`example analyzes the syntax of the input text and returns the different parts of speech. The pre-trained model's confidence score is also output for each prediction.`aws compreh``en`d detect-syntax \ --language-code en \ --text`"It is a beautiful day in Seattle."`Output: `{ "SyntaxTokens": [ { "TokenId": 1, "Text": "It", "BeginOffset": 0, "EndOffset": 2, "PartOfSpeech": { "Tag": "PRON", "Score": 0.9999740719795227 } }, { "TokenId": 2, "Text": "is", "BeginOffset": 3, "EndOffset": 5, "PartOfSpeech": { "Tag": "VERB", "Score": 0.999901294708252 } }, { "TokenId": 3, "Text": "a", "BeginOffset": 6, "EndOffset": 7, "PartOfSpeech": { "Tag": "DET", "Score": 0.9999938607215881 } }, { "TokenId": 4, "Text": "beautiful", "BeginOffset": 8, "EndOffset": 17, "PartOfSpeech": { "Tag": "ADJ", "Score": 0.9987351894378662 } }, { "TokenId": 5, "Text": "day", "BeginOffset": 18, "EndOffset": 21, "PartOfSpeech": { "Tag": "NOUN", "Score": 0.9999796748161316 } }, { "TokenId": 6, "Text": "in", "BeginOffset": 22, "EndOffset": 24, "PartOfSpeech": { "Tag": "ADP", "Score": 0.9998047947883606 } }, { "TokenId": 7, "Text": "Seattle", "BeginOffset": 25, "EndOffset": 32, "PartOfSpeech": { "Tag": "PROPN", "Score": 0.9940530061721802 } } ] }`For more information, see [Syntax Analysis](https://docs.aws.amazon.com/comprehend/latest/dg/how-syntax.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DetectSyntax](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-syntax.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `detect-targeted-sentiment`.

- **AWS CLI**
- 
            
                    **To detect the targeted sentiment of named entities in an input text**The following `detect-targeted-sentiment`example analyzes the input text and returns the named entities in addition to the targeted sentiment associated with each entity. The pre-trained models confidence score for each prediction is also output.`aws compreh``en`d detect-targeted-sentiment \ --language-code en \ --text`"I do not enjoy January because it is too cold but August is the perfect temperature"`Output: `{ "Entities": [ { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9999979734420776, "GroupScore": 1.0, "Text": "I", "Type": "PERSON", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Positive": 0.0, "Negative": 0.0, "Neutral": 1.0, "Mixed": 0.0 } }, "BeginOffset": 0, "EndOffset": 1 } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9638869762420654, "GroupScore": 1.0, "Text": "January", "Type": "DATE", "MentionSentiment": { "Sentiment": "NEGATIVE", "SentimentScore": { "Positive": 0.0031610000878572464, "Negative": 0.9967250227928162, "Neutral": 0.00011100000119768083, "Mixed": 1.9999999949504854e-06 } }, "BeginOffset": 15, "EndOffset": 22 } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { { "Score": 0.9664419889450073, "GroupScore": 1.0, "Text": "August", "Type": "DATE", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Positive": 0.9999549984931946, "Negative": 3.999999989900971e-06, "Neutral": 4.099999932805076e-05, "Mixed": 0.0 } }, "BeginOffset": 50, "EndOffset": 56 } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "Score": 0.9803199768066406, "GroupScore": 1.0, "Text": "temperature", "Type": "ATTRIBUTE", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Positive": 1.0, "Negative": 0.0, "Neutral": 0.0, "Mixed": 0.0 } }, "BeginOffset": 77, "EndOffset": 88 } ] } ] }`For more information, see [Targeted Sentiment](https://docs.aws.amazon.com/comprehend/latest/dg/how-targeted-sentiment.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [DetectTargetedSentiment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/detect-targeted-sentiment.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `import-model`.

- **AWS CLI**
- 
            
                    **To import a model**The following `import-model`example imports a model from a different AWS account. The document classifier model in account`444455556666`has a resource-based policy allowing account`111122223333`to import the model.`aws comprehend import-model \ --source-model-arn``arn:aws:comprehend:us-west-2:444455556666:document-classifier/example-classifier`Output: `{ "ModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier" }`For more information, see [Copying custom models between AWS accounts](https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ImportModel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/import-model.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-datasets`.

- **AWS CLI**
- 
            
                    **To list all flywheel datasets**The following `list-datasets`example lists all datasets associated with a flywheel.`aws comprehend list-datasets \ --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity`Output: `{ "DatasetPropertiesList": [ { "DatasetArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity/dataset/example-dataset-1", "DatasetName": "example-dataset-1", "DatasetType": "TRAIN", "DatasetS3Uri": "s3://amzn-s3-demo-bucket/flywheel-entity/schemaVersion=1/20230616T200543Z/datasets/example-dataset-1/20230616T203710Z/", "Status": "CREATING", "CreationTime": "2023-06-16T20:37:10.400000+00:00" }, { "DatasetArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity/dataset/example-dataset-2", "DatasetName": "example-dataset-2", "DatasetType": "TRAIN", "DatasetS3Uri": "s3://amzn-s3-demo-bucket/flywheel-entity/schemaVersion=1/20230616T200543Z/datasets/example-dataset-2/20230616T200607Z/", "Description": "TRAIN Dataset created by Flywheel creation.", "Status": "COMPLETED", "NumberOfDocuments": 5572, "CreationTime": "2023-06-16T20:06:07.722000+00:00" } ] }`For more information, see [Flywheel Overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListDatasets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-datasets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-document-classification-jobs`.

- **AWS CLI**
- 
            
                    **To list of all document classification jobs**The following `list-document-classification-jobs`example lists all document classification jobs.`aws comprehend list-document-classification-jobs`Output: `{ "DocumentClassificationJobPropertiesList": [ { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:1234567890101:document-classification-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "exampleclassificationjob", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-14T17:09:51.788000+00:00", "EndTime": "2023-06-14T17:15:58.582000+00:00", "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:1234567890101:document-classifier/mymodel/version/12", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/jobdata/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/1234567890101-CLN-e758dd56b824aa717ceab551f11749fb/output/output.tar.gz" }, "DataAccessRoleArn": "arn:aws:iam::1234567890101:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "123456abcdeb0e11022f22a1EXAMPLE2", "JobArn": "arn:aws:comprehend:us-west-2:1234567890101:document-classification-job/123456abcdeb0e11022f22a1EXAMPLE2", "JobName": "exampleclassificationjob2", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-14T17:22:39.829000+00:00", "EndTime": "2023-06-14T17:28:46.107000+00:00", "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:1234567890101:document-classifier/mymodel/version/12", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/jobdata/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/1234567890101-CLN-123456abcdeb0e11022f22a1EXAMPLE2/output/output.tar.gz" }, "DataAccessRoleArn": "arn:aws:iam::1234567890101:role/service-role/AmazonComprehendServiceRole-example-role" } ] }`For more information, see [Custom Classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListDocumentClassificationJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-document-classification-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-document-classifier-summaries`.

- **AWS CLI**
- 
            
                    **To list the summaries of all created document classifiers**The following `list-document-classifier-summaries`example lists all created document classifier summaries.`aws comprehend list-document-classifier-summaries`Output: `{ "DocumentClassifierSummariesList": [ { "DocumentClassifierName": "example-classifier-1", "NumberOfVersions": 1, "LatestVersionCreatedAt": "2023-06-13T22:07:59.825000+00:00", "LatestVersionName": "1", "LatestVersionStatus": "TRAINED" }, { "DocumentClassifierName": "example-classifier-2", "NumberOfVersions": 2, "LatestVersionCreatedAt": "2023-06-13T21:54:59.589000+00:00", "LatestVersionName": "2", "LatestVersionStatus": "TRAINED" } ] }`For more information, see [Creating and managing custom models](https://docs.aws.amazon.com/comprehend/latest/dg/manage-models.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListDocumentClassifierSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-document-classifier-summaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-document-classifiers`.

- **AWS CLI**
- 
            
                    **To list of all document classifiers**The following `list-document-classifiers`example lists all trained and in-training document classifier models.`aws comprehend list-document-classifiers`Output: `{ "DocumentClassifierPropertiesList": [ { "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier1", "LanguageCode": "en", "Status": "TRAINED", "SubmitTime": "2023-06-13T19:04:15.735000+00:00", "EndTime": "2023-06-13T19:42:31.752000+00:00", "TrainingStartTime": "2023-06-13T19:08:20.114000+00:00", "TrainingEndTime": "2023-06-13T19:41:35.080000+00:00", "InputDataConfig": { "DataFormat": "COMPREHEND_CSV", "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata" }, "OutputDataConfig": {}, "ClassifierMetadata": { "NumberOfLabels": 3, "NumberOfTrainedDocuments": 5016, "NumberOfTestDocuments": 557, "EvaluationMetrics": { "Accuracy": 0.9856, "Precision": 0.9919, "Recall": 0.9459, "F1Score": 0.9673, "MicroPrecision": 0.9856, "MicroRecall": 0.9856, "MicroF1Score": 0.9856, "HammingLoss": 0.0144 } }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-testorle", "Mode": "MULTI_CLASS" }, { "DocumentClassifierArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier2", "LanguageCode": "en", "Status": "TRAINING", "SubmitTime": "2023-06-13T21:20:28.690000+00:00", "InputDataConfig": { "DataFormat": "COMPREHEND_CSV", "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata" }, "OutputDataConfig": {}, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-testorle", "Mode": "MULTI_CLASS" } ] }`For more information, see [Creating and managing custom models](https://docs.aws.amazon.com/comprehend/latest/dg/manage-models.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListDocumentClassifiers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-document-classifiers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-dominant-language-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all dominant language detection jobs**The following `list-dominant-language-detection-jobs`example lists all in-progress and completed asynchronous dominant language detection jobs.`aws comprehend list-dominant-language-detection-jobs`Output: `{ "DominantLanguageDetectionJobPropertiesList": [ { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "languageanalysis1", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-09T18:10:38.037000+00:00", "EndTime": "2023-06-09T18:18:45.498000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-LANGUAGE-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "languageanalysis2", "JobStatus": "STOPPED", "SubmitTime": "2023-06-09T18:16:33.690000+00:00", "EndTime": "2023-06-09T18:24:40.608000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-LANGUAGE-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" } ] }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListDominantLanguageDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-dominant-language-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-endpoints`.

- **AWS CLI**
- 
            
                    **To list of all endpoints**The following `list-endpoints`example lists all active model-specific endpoints.`aws comprehend list-endpoints`Output: `{ "EndpointPropertiesList": [ { "EndpointArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/ExampleClassifierEndpoint", "Status": "IN_SERVICE", "ModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier1", "DesiredModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier1", "DesiredInferenceUnits": 1, "CurrentInferenceUnits": 1, "CreationTime": "2023-06-13T20:32:54.526000+00:00", "LastModifiedTime": "2023-06-13T20:32:54.526000+00:00" }, { "EndpointArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/ExampleClassifierEndpoint2", "Status": "IN_SERVICE", "ModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier2", "DesiredModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier2", "DesiredInferenceUnits": 1, "CurrentInferenceUnits": 1, "CreationTime": "2023-06-13T20:32:54.526000+00:00", "LastModifiedTime": "2023-06-13T20:32:54.526000+00:00" } ] }`For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListEndpoints](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-endpoints.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-entities-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all entities detection jobs**The following `list-entities-detection-jobs`example lists all asynchronous entities detection jobs.`aws comprehend list-entities-detection-jobs`Output: `{ "EntitiesDetectionJobPropertiesList": [ { "JobId": "468af39c28ab45b83eb0c4ab9EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/468af39c28ab45b83eb0c4ab9EXAMPLE", "JobName": "example-entities-detection", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-08T20:57:46.476000+00:00", "EndTime": "2023-06-08T21:05:53.718000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/111122223333-NER-468af39c28ab45b83eb0c4ab9EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "809691caeaab0e71406f80a28EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/809691caeaab0e71406f80a28EXAMPLE", "JobName": "example-entities-detection-2", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-08T21:30:15.323000+00:00", "EndTime": "2023-06-08T21:40:23.509000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/111122223333-NER-809691caeaab0e71406f80a28EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "e00597c36b448b91d70dea165EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/e00597c36b448b91d70dea165EXAMPLE", "JobName": "example-entities-detection-3", "JobStatus": "STOPPED", "SubmitTime": "2023-06-08T22:19:28.528000+00:00", "EndTime": "2023-06-08T22:27:33.991000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/111122223333-NER-e00597c36b448b91d70dea165EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" } ] }`For more information, see [Entities](https://docs.aws.amazon.com/comprehend/latest/dg/how-entities.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListEntitiesDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-entities-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-entity-recognizer-summaries`.

- **AWS CLI**
- 
            
                    **To list of summaries for all created entity recognizers**The following `list-entity-recognizer-summaries`example lists all entity recognizer summaries.`aws comprehend list-entity-recognizer-summaries`Output: `{ "EntityRecognizerSummariesList": [ { "RecognizerName": "entity-recognizer-3", "NumberOfVersions": 2, "LatestVersionCreatedAt": "2023-06-15T23:15:07.621000+00:00", "LatestVersionName": "2", "LatestVersionStatus": "STOP_REQUESTED" }, { "RecognizerName": "entity-recognizer-2", "NumberOfVersions": 1, "LatestVersionCreatedAt": "2023-06-14T22:55:27.805000+00:00", "LatestVersionName": "2" "LatestVersionStatus": "TRAINED" }, { "RecognizerName": "entity-recognizer-1", "NumberOfVersions": 1, "LatestVersionCreatedAt": "2023-06-14T20:44:59.631000+00:00", "LatestVersionName": "1", "LatestVersionStatus": "TRAINED" } ] }`For more information, see [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListEntityRecognizerSummaries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-entity-recognizer-summaries.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-entity-recognizers`.

- **AWS CLI**
- 
            
                    **To list of all custom entity recognizers**The following `list-entity-recognizers`example lists all created custom entity recognizers.`aws comprehend list-entity-recognizers`Output: `{ "EntityRecognizerPropertiesList": [ { "EntityRecognizerArn": "arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/EntityRecognizer/version/1", "LanguageCode": "en", "Status": "TRAINED", "SubmitTime": "2023-06-14T20:44:59.631000+00:00", "EndTime": "2023-06-14T20:59:19.532000+00:00", "TrainingStartTime": "2023-06-14T20:48:52.811000+00:00", "TrainingEndTime": "2023-06-14T20:58:11.473000+00:00", "InputDataConfig": { "DataFormat": "COMPREHEND_CSV", "EntityTypes": [ { "Type": "BUSINESS" } ], "Documents": { "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/dataset/", "InputFormat": "ONE_DOC_PER_LINE" }, "EntityList": { "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/entity.csv" } }, "RecognizerMetadata": { "NumberOfTrainedDocuments": 1814, "NumberOfTestDocuments": 486, "EvaluationMetrics": { "Precision": 100.0, "Recall": 100.0, "F1Score": 100.0 }, "EntityTypes": [ { "Type": "BUSINESS", "EvaluationMetrics": { "Precision": 100.0, "Recall": 100.0, "F1Score": 100.0 }, "NumberOfTrainMentions": 1520 } ] }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-servicerole", "VersionName": "1" }, { "EntityRecognizerArn": "arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/entityrecognizer3", "LanguageCode": "en", "Status": "TRAINED", "SubmitTime": "2023-06-14T22:57:51.056000+00:00", "EndTime": "2023-06-14T23:14:13.894000+00:00", "TrainingStartTime": "2023-06-14T23:01:33.984000+00:00", "TrainingEndTime": "2023-06-14T23:13:02.984000+00:00", "InputDataConfig": { "DataFormat": "COMPREHEND_CSV", "EntityTypes": [ { "Type": "DEVICE" } ], "Documents": { "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/raw_txt.csv", "InputFormat": "ONE_DOC_PER_LINE" }, "EntityList": { "S3Uri": "s3://amzn-s3-demo-bucket/trainingdata/entity_list.csv" } }, "RecognizerMetadata": { "NumberOfTrainedDocuments": 4616, "NumberOfTestDocuments": 3489, "EvaluationMetrics": { "Precision": 98.54227405247813, "Recall": 100.0, "F1Score": 99.26578560939794 }, "EntityTypes": [ { "Type": "DEVICE", "EvaluationMetrics": { "Precision": 98.54227405247813, "Recall": 100.0, "F1Score": 99.26578560939794 }, "NumberOfTrainMentions": 2764 } ] }, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-servicerole" } ] }`For more information, see [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListEntityRecognizers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-entity-recognizers.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-events-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all events detection jobs**The following `list-events-detection-jobs`example lists all asynchronous events detection jobs.`aws comprehend list-events-detection-jobs`Output: `{ "EventsDetectionJobPropertiesList": [ { "JobId": "aa9593f9203e84f3ef032ce18EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:1111222233333:events-detection-job/aa9593f9203e84f3ef032ce18EXAMPLE", "JobName": "events_job_1", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-12T19:14:57.751000+00:00", "EndTime": "2023-06-12T19:21:04.962000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-source-bucket/EventsData/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/1111222233333-EVENTS-aa9593f9203e84f3ef032ce18EXAMPLE/output/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::1111222233333:role/service-role/AmazonComprehendServiceRole-example-role", "TargetEventTypes": [ "BANKRUPTCY", "EMPLOYMENT", "CORPORATE_ACQUISITION", "CORPORATE_MERGER", "INVESTMENT_GENERAL" ] }, { "JobId": "4a990a2f7e82adfca6e171135EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:1111222233333:events-detection-job/4a990a2f7e82adfca6e171135EXAMPLE", "JobName": "events_job_2", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-12T19:55:43.702000+00:00", "EndTime": "2023-06-12T20:03:49.893000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-source-bucket/EventsData/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/1111222233333-EVENTS-4a990a2f7e82adfca6e171135EXAMPLE/output/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::1111222233333:role/service-role/AmazonComprehendServiceRole-example-role", "TargetEventTypes": [ "BANKRUPTCY", "EMPLOYMENT", "CORPORATE_ACQUISITION", "CORPORATE_MERGER", "INVESTMENT_GENERAL" ] } ] }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListEventsDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-events-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-flywheel-iteration-history`.

- **AWS CLI**
- 
            
                    **To list all flywheel iteration history**The following `list-flywheel-iteration-history`example lists all iterations of a flywheel.`aws comprehend list-flywheel-iteration-history --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel`Output: `{ "FlywheelIterationPropertiesList": [ { "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel", "FlywheelIterationId": "20230619TEXAMPLE", "CreationTime": "2023-06-19T04:00:32.594000+00:00", "EndTime": "2023-06-19T04:00:49.248000+00:00", "Status": "COMPLETED", "Message": "FULL_ITERATION: Flywheel iteration performed all functions successfully.", "EvaluatedModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1", "EvaluatedModelMetrics": { "AverageF1Score": 0.7742663922375772, "AverageF1Score": 0.9876464664646313, "AveragePrecision": 0.9800000253081214, "AverageRecall": 0.9445600253081214, "AverageAccuracy": 0.9997281665190434 }, "EvaluationManifestS3Prefix": "s3://amzn-s3-demo-bucket/example-flywheel/schemaVersion=1/20230619TEXAMPLE/evaluation/20230619TEXAMPLE/" }, { "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel-2", "FlywheelIterationId": "20230616TEXAMPLE", "CreationTime": "2023-06-16T21:10:26.385000+00:00", "EndTime": "2023-06-16T23:33:16.827000+00:00", "Status": "COMPLETED", "Message": "FULL_ITERATION: Flywheel iteration performed all functions successfully.", "EvaluatedModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/spamvshamclassify/version/1", "EvaluatedModelMetrics": { "AverageF1Score": 0.7742663922375772, "AverageF1Score": 0.9767700253081214, "AveragePrecision": 0.9767700253081214, "AverageRecall": 0.9767700253081214, "AverageAccuracy": 0.9858281665190434 }, "EvaluationManifestS3Prefix": "s3://amzn-s3-demo-bucket/example-flywheel-2/schemaVersion=1/20230616TEXAMPLE/evaluation/20230616TEXAMPLE/" } ] }`For more information, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListFlywheelIterationHistory](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-flywheel-iteration-history.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-flywheels`.

- **AWS CLI**
- 
            
                    **To list all flywheels**The following `list-flywheels`example lists all created flywheels.`aws comprehend list-flywheels`Output: `{ "FlywheelSummaryList": [ { "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel-1", "ActiveModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier/version/1", "DataLakeS3Uri": "s3://amzn-s3-demo-bucket/example-flywheel-1/schemaVersion=1/20230616T200543Z/", "Status": "ACTIVE", "ModelType": "DOCUMENT_CLASSIFIER", "CreationTime": "2023-06-16T20:05:43.242000+00:00", "LastModifiedTime": "2023-06-19T04:00:43.027000+00:00", "LatestFlywheelIteration": "20230619T040032Z" }, { "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel-2", "ActiveModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/exampleclassifier2/version/1", "DataLakeS3Uri": "s3://amzn-s3-demo-bucket/example-flywheel-2/schemaVersion=1/20220616T200543Z/", "Status": "ACTIVE", "ModelType": "DOCUMENT_CLASSIFIER", "CreationTime": "2022-06-16T20:05:43.242000+00:00", "LastModifiedTime": "2022-06-19T04:00:43.027000+00:00", "LatestFlywheelIteration": "20220619T040032Z" } ] }`For more information, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListFlywheels](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-flywheels.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-key-phrases-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all key phrases detection jobs**The following `list-key-phrases-detection-jobs`example lists all in-progress and completed asynchronous key phrases detection jobs.`aws comprehend list-key-phrases-detection-jobs`Output: `{ "KeyPhrasesDetectionJobPropertiesList": [ { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "keyphrasesanalysis1", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-08T22:31:43.767000+00:00", "EndTime": "2023-06-08T22:39:52.565000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-source-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-KP-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "123456abcdeb0e11022f22a33EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/123456abcdeb0e11022f22a33EXAMPLE", "JobName": "keyphrasesanalysis2", "JobStatus": "STOPPED", "SubmitTime": "2023-06-08T22:57:52.154000+00:00", "EndTime": "2023-06-08T23:05:48.385000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-KP-123456abcdeb0e11022f22a33EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "123456abcdeb0e11022f22a44EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/123456abcdeb0e11022f22a44EXAMPLE", "JobName": "keyphrasesanalysis3", "JobStatus": "FAILED", "Message": "NO_READ_ACCESS_TO_INPUT: The provided data access role does not have proper access to the input data.", "SubmitTime": "2023-06-09T16:47:04.029000+00:00", "EndTime": "2023-06-09T16:47:18.413000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-KP-123456abcdeb0e11022f22a44EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" } ] }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListKeyPhrasesDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-key-phrases-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-pii-entities-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all pii entities detection jobs**The following `list-pii-entities-detection-jobs`example lists all in-progress and completed asynchronous pii detection jobs.`aws comprehend list-pii-entities-detection-jobs`Output: `{ "PiiEntitiesDetectionJobPropertiesList": [ { "JobId": "6f9db0c42d0c810e814670ee4EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/6f9db0c42d0c810e814670ee4EXAMPLE", "JobName": "example-pii-detection-job", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-09T21:02:46.241000+00:00", "EndTime": "2023-06-09T21:12:52.602000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-source-bucket/111122223333-PII-6f9db0c42d0c810e814670ee4EXAMPLE/output/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role", "Mode": "ONLY_OFFSETS" }, { "JobId": "d927562638cfa739331a99b3cEXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/d927562638cfa739331a99b3cEXAMPLE", "JobName": "example-pii-detection-job-2", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-09T21:20:58.211000+00:00", "EndTime": "2023-06-09T21:31:06.027000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/AsyncBatchJobs/", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/111122223333-PII-d927562638cfa739331a99b3cEXAMPLE/output/" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role", "Mode": "ONLY_OFFSETS" } ] }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListPiiEntitiesDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-pii-entities-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-sentiment-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all sentiment detection jobs**The following `list-sentiment-detection-jobs`example lists all in-progress and completed asynchronous sentiment detection jobs.`aws comprehend list-sentiment-detection-jobs`Output: `{ "SentimentDetectionJobPropertiesList": [ { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "example-sentiment-detection-job", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-09T22:42:20.545000+00:00", "EndTime": "2023-06-09T22:52:27.416000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/MovieData", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TS-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "123456abcdeb0e11022f22a1EXAMPLE2", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/123456abcdeb0e11022f22a1EXAMPLE2", "JobName": "example-sentiment-detection-job-2", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-09T23:16:15.956000+00:00", "EndTime": "2023-06-09T23:26:00.168000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/MovieData2", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TS-123456abcdeb0e11022f22a1EXAMPLE2/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" } ] }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListSentimentDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-sentiment-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To list tags for resource**The following `list-tags-for-resource`example lists the tags for an Amazon Comprehend resource.`aws comprehend list-tags-for-resource \ --resource-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1`Output: `{ "ResourceArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1", "Tags": [ { "Key": "Department", "Value": "Finance" }, { "Key": "location", "Value": "Seattle" } ] }`For more information, see [Tagging your resources](https://docs.aws.amazon.com/comprehend/latest/dg/tagging.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-targeted-sentiment-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all targeted sentiment detection jobs**The following `list-targeted-sentiment-detection-jobs`example lists all in-progress and completed asynchronous targeted sentiment detection jobs.`aws comprehend list-targeted-sentiment-detection-jobs`Output: `{ "TargetedSentimentDetectionJobPropertiesList": [ { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName": "example-targeted-sentiment-detection-job", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-09T22:42:20.545000+00:00", "EndTime": "2023-06-09T22:52:27.416000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/MovieData", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TS-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-IOrole" }, { "JobId": "123456abcdeb0e11022f22a1EXAMPLE2", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/123456abcdeb0e11022f22a1EXAMPLE2", "JobName": "example-targeted-sentiment-detection-job-2", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-09T23:16:15.956000+00:00", "EndTime": "2023-06-09T23:26:00.168000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket/MovieData2", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/testfolder/111122223333-TS-123456abcdeb0e11022f22a1EXAMPLE2/output/output.tar.gz" }, "LanguageCode": "en", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" } ] }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListTargetedSentimentDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-targeted-sentiment-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-topics-detection-jobs`.

- **AWS CLI**
- 
            
                    **To list all topic detection jobs**The following `list-topics-detection-jobs`example lists all in-progress and completed asynchronous topics detection jobs.`aws comprehend list-topics-detection-jobs`Output: `{ "TopicsDetectionJobPropertiesList": [ { "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:topics-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobName" "topic-analysis-1" "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-09T18:40:35.384000+00:00", "EndTime": "2023-06-09T18:46:41.936000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/111122223333-TOPICS-123456abcdeb0e11022f22a11EXAMPLE/output/output.tar.gz" }, "NumberOfTopics": 10, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "123456abcdeb0e11022f22a1EXAMPLE2", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:topics-detection-job/123456abcdeb0e11022f22a1EXAMPLE2", "JobName": "topic-analysis-2", "JobStatus": "COMPLETED", "SubmitTime": "2023-06-09T18:44:43.414000+00:00", "EndTime": "2023-06-09T18:50:50.872000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/111122223333-TOPICS-123456abcdeb0e11022f22a1EXAMPLE2/output/output.tar.gz" }, "NumberOfTopics": 10, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" }, { "JobId": "123456abcdeb0e11022f22a1EXAMPLE3", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:topics-detection-job/123456abcdeb0e11022f22a1EXAMPLE3", "JobName": "topic-analysis-2", "JobStatus": "IN_PROGRESS", "SubmitTime": "2023-06-09T18:50:56.737000+00:00", "InputDataConfig": { "S3Uri": "s3://amzn-s3-demo-bucket", "InputFormat": "ONE_DOC_PER_LINE" }, "OutputDataConfig": { "S3Uri": "s3://amzn-s3-demo-destination-bucket/thefolder/111122223333-TOPICS-123456abcdeb0e11022f22a1EXAMPLE3/output/output.tar.gz" }, "NumberOfTopics": 10, "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role" } ] }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [ListTopicsDetectionJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/list-topics-detection-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-resource-policy`.

- **AWS CLI**
- 
            
                    **To attach a resource-based policy**The following `put-resource-policy`example attaches a resource-based policy to a model so that can be imported by another AWS account. The policy is attached to the model in account`111122223333`and allows account`444455556666`import the model.`aws comprehend put-resource-policy \ --resource-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1`\ --resource-policy '`{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"comprehend:ImportModel","Resource":"*","Principal":{"AWS":["arn:aws:iam::444455556666:root"]}}]}`'Output: `{ "PolicyRevisionId": "aaa111d069d07afaa2aa3106aEXAMPLE" }`For more information, see [Copying custom models between AWS accounts](https://docs.aws.amazon.com/comprehend/latest/dg/custom-copy.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [PutResourcePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/put-resource-policy.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-document-classification-job`.

- **AWS CLI**
- 
            
                    **To start document classification job**The following `start-document-classification-job`example starts a document classification job with a custom model on all of the files at the address specified by the`--input-data-config`tag. In this example, the input S3 bucket contains`SampleSMStext1.txt`,`SampleSMStext2.txt`, and`SampleSMStext3.txt`. The model was previously trained on document classifications of spam and non-spam, or, "ham", SMS messages. When the job is complete,`output.tar.gz`is put at the location specified by the`--output-data-config`tag.`output.tar.gz`contains`predictions.jsonl`which lists the classification of each document. The Json output is printed on one line per file, but is formatted here for readability.`aws comprehend start-document-classification-job \ --job-name``exampleclassificationjob`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket-INPUT/jobdata/"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --document-classifier-arn`arn:aws:comprehend:us-west-2:111122223333:document-classifier/mymodel/version/12`Contents of `SampleSMStext1.txt`:`"CONGRATULATIONS! TXT 2155550100 to win $5000"`Contents of `SampleSMStext2.txt`:`"Hi, when do you want me to pick you up from practice?"`Contents of `SampleSMStext3.txt`:`"Plz send bank account # to 2155550100 to claim prize!!"`Output: `{ "JobId": "e758dd56b824aa717ceab551fEXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:document-classification-job/e758dd56b824aa717ceab551fEXAMPLE", "JobStatus": "SUBMITTED" }`Contents of `predictions.jsonl`:`{"File": "SampleSMSText1.txt", "Line": "0", "Classes": [{"Name": "spam", "Score": 0.9999}, {"Name": "ham", "Score": 0.0001}]} {"File": "SampleSMStext2.txt", "Line": "0", "Classes": [{"Name": "ham", "Score": 0.9994}, {"Name": "spam", "Score": 0.0006}]} {"File": "SampleSMSText3.txt", "Line": "0", "Classes": [{"Name": "spam", "Score": 0.9999}, {"Name": "ham", "Score": 0.0001}]}`For more information, see [Custom Classification](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartDocumentClassificationJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-document-classification-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-dominant-language-detection-job`.

- **AWS CLI**
- 
            
                    **To start an asynchronous language detection job**The following `start-dominant-language-detection-job`example starts an asynchronous language detection job for all of the files located at the address specified by the`--input-data-config`tag. The S3 bucket in this example contains`Sampletext1.txt`. When the job is complete, the folder,`output`, is placed in the location specified by the`--output-data-config`tag. The folder contains`output.txt`which contains the dominant language of each of the text files as well as the pre-trained model's confidence score for each prediction.`aws comprehend start-dominant-language-detection-job \ --job-name``example_language_analysis_job`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --language-code`en`Contents of Sampletext1.txt: `"Physics is the natural science that involves the study of matter and its motion and behavior through space and time, along with related concepts such as energy and force."`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:dominant-language-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobStatus": "SUBMITTED" }`Contents of `output.txt`:`{"File": "Sampletext1.txt", "Languages": [{"LanguageCode": "en", "Score": 0.9913753867149353}], "Line": 0}`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartDominantLanguageDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-dominant-language-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-entities-detection-job`.

- **AWS CLI**
- 
            
                    **Example 1: To start a standard entity detection job using the pre-trained model**The following `start-entities-detection-job`example starts an asynchronous entities detection job for all files located at the address specified by the`--input-data-config`tag. The S3 bucket in this example contains`Sampletext1.txt`,`Sampletext2.txt`, and`Sampletext3.txt`. When the job is complete, the folder,`output`, is placed in the location specified by the`--output-data-config`tag. The folder contains`output.txt`which lists all of the named entities detected within each text file as well as the pre-trained model's confidence score for each prediction. The Json output is printed on one line per input file, but is formatted here for readability.`aws comprehend start-entities-detection-job \ --job-name``entitiestest`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --language-code`en`Contents of `Sampletext1.txt`:`"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st."`Contents of `Sampletext2.txt`:`"Dear Max, based on your autopay settings for your account example1.org account, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. "`Contents of `Sampletext3.txt`:`"Jane, please submit any customer feedback from this weekend to AnySpa, 123 Main St, Anywhere and send comments to Alice at AnySpa@example.com."`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobStatus": "SUBMITTED" }`Contents of `output.txt`with line indents for readability:`{ "Entities": [ { "BeginOffset": 6, "EndOffset": 15, "Score": 0.9994006636420306, "Text": "Zhang Wei", "Type": "PERSON" }, { "BeginOffset": 22, "EndOffset": 26, "Score": 0.9976647915128143, "Text": "John", "Type": "PERSON" }, { "BeginOffset": 33, "EndOffset": 67, "Score": 0.9984608700836206, "Text": "AnyCompany Financial Services, LLC", "Type": "ORGANIZATION" }, { "BeginOffset": 88, "EndOffset": 107, "Score": 0.9868521019555556, "Text": "1111-XXXX-1111-XXXX", "Type": "OTHER" }, { "BeginOffset": 133, "EndOffset": 139, "Score": 0.998242565709204, "Text": "$24.53", "Type": "QUANTITY" }, { "BeginOffset": 155, "EndOffset": 164, "Score": 0.9993039263159287, "Text": "July 31st", "Type": "DATE" } ], "File": "SampleText1.txt", "Line": 0 } { "Entities": [ { "BeginOffset": 5, "EndOffset": 8, "Score": 0.9866232147545232, "Text": "Max", "Type": "PERSON" }, { "BeginOffset": 156, "EndOffset": 166, "Score": 0.9797723450933329, "Text": "XXXXXX1111", "Type": "OTHER" }, { "BeginOffset": 191, "EndOffset": 200, "Score": 0.9247838572396843, "Text": "XXXXX0000", "Type": "OTHER" } ], "File": "SampleText2.txt", "Line": 0 } { "Entities": [ { "Score": 0.9990532994270325, "Type": "PERSON", "Text": "Jane", "BeginOffset": 0, "EndOffset": 4 }, { "Score": 0.9519651532173157, "Type": "DATE", "Text": "this weekend", "BeginOffset": 47, "EndOffset": 59 }, { "Score": 0.5566426515579224, "Type": "ORGANIZATION", "Text": "AnySpa", "BeginOffset": 63, "EndOffset": 69 }, { "Score": 0.8059805631637573, "Type": "LOCATION", "Text": "123 Main St, Anywhere", "BeginOffset": 71, "EndOffset": 92 }, { "Score": 0.998830258846283, "Type": "PERSON", "Text": "Alice", "BeginOffset": 114, "EndOffset": 119 }, { "Score": 0.997818112373352, "Type": "OTHER", "Text": "AnySpa@example.com", "BeginOffset": 123, "EndOffset": 138 } ], "File": "SampleText3.txt", "Line": 0 }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.**Example 2: To start a custom entity detection job**The following `start-entities-detection-job`example starts an asynchronous custom entities detection job for all files located at the address specified by the`--input-data-config`tag. In this example, the S3 bucket in this example contains`SampleFeedback1.txt`,`SampleFeedback2.txt`, and`SampleFeedback3.txt`. The entity recognizer model was trained on customer support Feedbacks to recognize device names. When the job is complete, an the folder,`output`, is put at the location specified by the`--output-data-config`tag. The folder contains`output.txt`, which lists all of the named entities detected within each text file as well as the pre-trained model's confidence score for each prediction. The Json output is printed on one line per file, but is formatted here for readability.`aws comprehend start-entities-detection-job \ --job-name``customentitiestest`\ --entity-recognizer-arn`"arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/entityrecognizer"`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/jobdata/"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`"arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-IOrole"`Contents of `SampleFeedback1.txt`:`"I've been on the AnyPhone app have had issues for 24 hours when trying to pay bill. Cannot make payment. Sigh. | Oh man! Lets get that app up and running. DM me, and we can get to work!"`Contents of `SampleFeedback2.txt`:`"Hi, I have a discrepancy with my new bill. Could we get it sorted out? A rep added stuff I didn't sign up for when I did my AnyPhone 10 upgrade. | We can absolutely get this sorted!"`Contents of `SampleFeedback3.txt`:`"Is the by 1 get 1 free AnySmartPhone promo still going on? | Hi Christian! It ended yesterday, send us a DM if you have any questions and we can take a look at your options!"`Output: `{ "JobId": "019ea9edac758806850fa8a79ff83021", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:entities-detection-job/019ea9edac758806850fa8a79ff83021", "JobStatus": "SUBMITTED" }`Contents of `output.txt`with line indents for readability:`{ "Entities": [ { "BeginOffset": 17, "EndOffset": 25, "Score": 0.9999728210205924, "Text": "AnyPhone", "Type": "DEVICE" } ], "File": "SampleFeedback1.txt", "Line": 0 } { "Entities": [ { "BeginOffset": 123, "EndOffset": 133, "Score": 0.9999892116761524, "Text": "AnyPhone 10", "Type": "DEVICE" } ], "File": "SampleFeedback2.txt", "Line": 0 } { "Entities": [ { "BeginOffset": 23, "EndOffset": 35, "Score": 0.9999971389852362, "Text": "AnySmartPhone", "Type": "DEVICE" } ], "File": "SampleFeedback3.txt", "Line": 0 }`For more information, see [Custom entity recognition](https://docs.aws.amazon.com/comprehend/latest/dg/custom-entity-recognition.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartEntitiesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-entities-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-events-detection-job`.

- **AWS CLI**
- 
            
                    **To start an asynchronous events detection job**The following `start-events-detection-job`example starts an asynchronous events detection job for all files located at the address specified by the`--input-data-config`tag. Possible target event types include`BANKRUPCTY`,`EMPLOYMENT`,`CORPORATE_ACQUISITION`,`INVESTMENT_GENERAL`,`CORPORATE_MERGER`,`IPO`,`RIGHTS_ISSUE`,`SECONDARY_OFFERING`,`SHELF_OFFERING`,`TENDER_OFFERING`, and`STOCK_SPLIT`. The S3 bucket in this example contains`SampleText1.txt`,`SampleText2.txt`, and`SampleText3.txt`. When the job is complete, the folder,`output`, is placed in the location specified by the`--output-data-config`tag. The folder contains`SampleText1.txt.out`,`SampleText2.txt.out`, and`SampleText3.txt.out`. The JSON output is printed on one line per file, but is formatted here for readability.`aws comprehend start-events-detection-job \ --job-name``events-detection-1`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/EventsData"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-servicerole`\ --language-code`en`\ --target-event-types`"BANKRUPTCY"``"EMPLOYMENT"``"CORPORATE_ACQUISITION"``"CORPORATE_MERGER"``"INVESTMENT_GENERAL"`Contents of `SampleText1.txt`:`"Company AnyCompany grew by increasing sales and through acquisitions. After purchasing competing firms in 2020, AnyBusiness, a part of the AnyBusinessGroup, gave Jane Does firm a going rate of one cent a gallon or forty-two cents a barrel."`Contents of `SampleText2.txt`:`"In 2021, AnyCompany officially purchased AnyBusiness for 100 billion dollars, surprising and exciting the shareholders."`Contents of `SampleText3.txt`:`"In 2022, AnyCompany stock crashed 50. Eventually later that year they filed for bankruptcy."`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:events-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobStatus": "SUBMITTED" }`Contents of `SampleText1.txt.out`with line indents for readability:`{ "Entities": [ { "Mentions": [ { "BeginOffset": 8, "EndOffset": 18, "Score": 0.99977, "Text": "AnyCompany", "Type": "ORGANIZATION", "GroupScore": 1 }, { "BeginOffset": 112, "EndOffset": 123, "Score": 0.999747, "Text": "AnyBusiness", "Type": "ORGANIZATION", "GroupScore": 0.979826 }, { "BeginOffset": 171, "EndOffset": 175, "Score": 0.999615, "Text": "firm", "Type": "ORGANIZATION", "GroupScore": 0.871647 } ] }, { "Mentions": [ { "BeginOffset": 97, "EndOffset": 102, "Score": 0.987687, "Text": "firms", "Type": "ORGANIZATION", "GroupScore": 1 } ] }, { "Mentions": [ { "BeginOffset": 103, "EndOffset": 110, "Score": 0.999458, "Text": "in 2020", "Type": "DATE", "GroupScore": 1 } ] }, { "Mentions": [ { "BeginOffset": 160, "EndOffset": 168, "Score": 0.999649, "Text": "John Doe", "Type": "PERSON", "GroupScore": 1 } ] } ], "Events": [ { "Type": "CORPORATE_ACQUISITION", "Arguments": [ { "EntityIndex": 0, "Role": "INVESTOR", "Score": 0.99977 } ], "Triggers": [ { "BeginOffset": 56, "EndOffset": 68, "Score": 0.999967, "Text": "acquisitions", "Type": "CORPORATE_ACQUISITION", "GroupScore": 1 } ] }, { "Type": "CORPORATE_ACQUISITION", "Arguments": [ { "EntityIndex": 1, "Role": "INVESTEE", "Score": 0.987687 }, { "EntityIndex": 2, "Role": "DATE", "Score": 0.999458 }, { "EntityIndex": 3, "Role": "INVESTOR", "Score": 0.999649 } ], "Triggers": [ { "BeginOffset": 76, "EndOffset": 86, "Score": 0.999973, "Text": "purchasing", "Type": "CORPORATE_ACQUISITION", "GroupScore": 1 } ] } ], "File": "SampleText1.txt", "Line": 0 }`Contents of `SampleText2.txt.out`:`{ "Entities": [ { "Mentions": [ { "BeginOffset": 0, "EndOffset": 7, "Score": 0.999473, "Text": "In 2021", "Type": "DATE", "GroupScore": 1 } ] }, { "Mentions": [ { "BeginOffset": 9, "EndOffset": 19, "Score": 0.999636, "Text": "AnyCompany", "Type": "ORGANIZATION", "GroupScore": 1 } ] }, { "Mentions": [ { "BeginOffset": 45, "EndOffset": 56, "Score": 0.999712, "Text": "AnyBusiness", "Type": "ORGANIZATION", "GroupScore": 1 } ] }, { "Mentions": [ { "BeginOffset": 61, "EndOffset": 80, "Score": 0.998886, "Text": "100 billion dollars", "Type": "MONETARY_VALUE", "GroupScore": 1 } ] } ], "Events": [ { "Type": "CORPORATE_ACQUISITION", "Arguments": [ { "EntityIndex": 3, "Role": "AMOUNT", "Score": 0.998886 }, { "EntityIndex": 2, "Role": "INVESTEE", "Score": 0.999712 }, { "EntityIndex": 0, "Role": "DATE", "Score": 0.999473 }, { "EntityIndex": 1, "Role": "INVESTOR", "Score": 0.999636 } ], "Triggers": [ { "BeginOffset": 31, "EndOffset": 40, "Score": 0.99995, "Text": "purchased", "Type": "CORPORATE_ACQUISITION", "GroupScore": 1 } ] } ], "File": "SampleText2.txt", "Line": 0 }`Contents of `SampleText3.txt.out`:`{ "Entities": [ { "Mentions": [ { "BeginOffset": 9, "EndOffset": 19, "Score": 0.999774, "Text": "AnyCompany", "Type": "ORGANIZATION", "GroupScore": 1 }, { "BeginOffset": 66, "EndOffset": 70, "Score": 0.995717, "Text": "they", "Type": "ORGANIZATION", "GroupScore": 0.997626 } ] }, { "Mentions": [ { "BeginOffset": 50, "EndOffset": 65, "Score": 0.999656, "Text": "later that year", "Type": "DATE", "GroupScore": 1 } ] } ], "Events": [ { "Type": "BANKRUPTCY", "Arguments": [ { "EntityIndex": 1, "Role": "DATE", "Score": 0.999656 }, { "EntityIndex": 0, "Role": "FILER", "Score": 0.995717 } ], "Triggers": [ { "BeginOffset": 81, "EndOffset": 91, "Score": 0.999936, "Text": "bankruptcy", "Type": "BANKRUPTCY", "GroupScore": 1 } ] } ], "File": "SampleText3.txt", "Line": 0 }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartEventsDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-events-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-flywheel-iteration`.

- **AWS CLI**
- 
            
                    **To start a flywheel iteration**The following `start-flywheel-iteration`example starts a flywheel iteration. This operation uses any new datasets in the flywheel to train a new model version.`aws comprehend start-flywheel-iteration \ --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel`Output: `{ "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel", "FlywheelIterationId": "12345123TEXAMPLE" }`For more information, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartFlywheelIteration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-flywheel-iteration.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-key-phrases-detection-job`.

- **AWS CLI**
- 
            
                    **To start a key phrases detection job**The following `start-key-phrases-detection-job`example starts an asynchronous key phrases detection job for all files located at the address specified by the`--input-data-config`tag. The S3 bucket in this example contains`Sampletext1.txt`,`Sampletext2.txt`, and`Sampletext3.txt`. When the job is completed, the folder,`output`, is placed in the location specified by the`--output-data-config`tag. The folder contains the file`output.txt`which contains all the key phrases detected within each text file and the pre-trained model's confidence score for each prediction. The Json output is printed on one line per file, but is formatted here for readability.`aws comprehend start-key-phrases-detection-job \ --job-name``keyphrasesanalysistest1`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`"arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role"`\ --language-code`en`Contents of `Sampletext1.txt`:`"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st."`Contents of `Sampletext2.txt`:`"Dear Max, based on your autopay settings for your account Internet.org account, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. "`Contents of `Sampletext3.txt`:`"Jane, please submit any customer feedback from this weekend to Sunshine Spa, 123 Main St, Anywhere and send comments to Alice at AnySpa@example.com."`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobStatus": "SUBMITTED" }`Contents of `output.txt`with line indents for readability:`{ "File": "SampleText1.txt", "KeyPhrases": [ { "BeginOffset": 6, "EndOffset": 15, "Score": 0.9748965572679326, "Text": "Zhang Wei" }, { "BeginOffset": 22, "EndOffset": 26, "Score": 0.9997344722354619, "Text": "John" }, { "BeginOffset": 28, "EndOffset": 62, "Score": 0.9843791074032948, "Text": "Your AnyCompany Financial Services" }, { "BeginOffset": 64, "EndOffset": 107, "Score": 0.8976122401721824, "Text": "LLC credit card account 1111-XXXX-1111-XXXX" }, { "BeginOffset": 112, "EndOffset": 129, "Score": 0.9999612982629748, "Text": "a minimum payment" }, { "BeginOffset": 133, "EndOffset": 139, "Score": 0.99975728947036, "Text": "$24.53" }, { "BeginOffset": 155, "EndOffset": 164, "Score": 0.9940866241449973, "Text": "July 31st" } ], "Line": 0 } { "File": "SampleText2.txt", "KeyPhrases": [ { "BeginOffset": 0, "EndOffset": 8, "Score": 0.9974021100118472, "Text": "Dear Max" }, { "BeginOffset": 19, "EndOffset": 40, "Score": 0.9961120519515884, "Text": "your autopay settings" }, { "BeginOffset": 45, "EndOffset": 78, "Score": 0.9980620070116009, "Text": "your account Internet.org account" }, { "BeginOffset": 97, "EndOffset": 109, "Score": 0.999919660140754, "Text": "your payment" }, { "BeginOffset": 113, "EndOffset": 125, "Score": 0.9998370719754205, "Text": "the due date" }, { "BeginOffset": 131, "EndOffset": 166, "Score": 0.9955068678502509, "Text": "your bank account number XXXXXX1111" }, { "BeginOffset": 172, "EndOffset": 200, "Score": 0.8653433315829526, "Text": "the routing number XXXXX0000" } ], "Line": 0 } { "File": "SampleText3.txt", "KeyPhrases": [ { "BeginOffset": 0, "EndOffset": 4, "Score": 0.9142947833681668, "Text": "Jane" }, { "BeginOffset": 20, "EndOffset": 41, "Score": 0.9984325676596763, "Text": "any customer feedback" }, { "BeginOffset": 47, "EndOffset": 59, "Score": 0.9998782448150636, "Text": "this weekend" }, { "BeginOffset": 63, "EndOffset": 75, "Score": 0.99866741830757, "Text": "Sunshine Spa" }, { "BeginOffset": 77, "EndOffset": 88, "Score": 0.9695803485466054, "Text": "123 Main St" }, { "BeginOffset": 108, "EndOffset": 116, "Score": 0.9997065928550928, "Text": "comments" }, { "BeginOffset": 120, "EndOffset": 125, "Score": 0.9993466833825161, "Text": "Alice" }, { "BeginOffset": 129, "EndOffset": 144, "Score": 0.9654563612885667, "Text": "AnySpa@example.com" } ], "Line": 0 }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartKeyPhrasesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-key-phrases-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-pii-entities-detection-job`.

- **AWS CLI**
- 
            
                    **To start an asynchronous PII detection job**The following `start-pii-entities-detection-job`example starts an asynchronous personal identifiable information (PII) entities detection job for all files located at the address specified by the`--input-data-config`tag. The S3 bucket in this example contains`Sampletext1.txt`,`Sampletext2.txt`, and`Sampletext3.txt`. When the job is complete, the folder,`output`, is placed in the location specified by the`--output-data-config`tag. The folder contains`SampleText1.txt.out`,`SampleText2.txt.out`, and`SampleText3.txt.out`which list the named entities within each text file. The Json output is printed on one line per file, but is formatted here for readability.`aws comprehend start-pii-entities-detection-job \ --job-name``entities_test`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --language-code`en`\ --mode`ONLY_OFFSETS`Contents of `Sampletext1.txt`:`"Hello Zhang Wei, I am John. Your AnyCompany Financial Services, LLC credit card account 1111-XXXX-1111-XXXX has a minimum payment of $24.53 that is due by July 31st."`Contents of `Sampletext2.txt`:`"Dear Max, based on your autopay settings for your account Internet.org account, we will withdraw your payment on the due date from your bank account number XXXXXX1111 with the routing number XXXXX0000. "`Contents of `Sampletext3.txt`:`"Jane, please submit any customer feedback from this weekend to Sunshine Spa, 123 Main St, Anywhere and send comments to Alice at AnySpa@example.com."`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:pii-entities-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobStatus": "SUBMITTED" }`Contents of `SampleText1.txt.out`with line indents for readability:`{ "Entities": [ { "BeginOffset": 6, "EndOffset": 15, "Type": "NAME", "Score": 0.9998490510222595 }, { "BeginOffset": 22, "EndOffset": 26, "Type": "NAME", "Score": 0.9998937958019426 }, { "BeginOffset": 88, "EndOffset": 107, "Type": "CREDIT_DEBIT_NUMBER", "Score": 0.9554297245278491 }, { "BeginOffset": 155, "EndOffset": 164, "Type": "DATE_TIME", "Score": 0.9999720462925257 } ], "File": "SampleText1.txt", "Line": 0 }`Contents of `SampleText2.txt.out`with line indents for readability:`{ "Entities": [ { "BeginOffset": 5, "EndOffset": 8, "Type": "NAME", "Score": 0.9994390774924007 }, { "BeginOffset": 58, "EndOffset": 70, "Type": "URL", "Score": 0.9999958276922101 }, { "BeginOffset": 156, "EndOffset": 166, "Type": "BANK_ACCOUNT_NUMBER", "Score": 0.9999721058045592 }, { "BeginOffset": 191, "EndOffset": 200, "Type": "BANK_ROUTING", "Score": 0.9998968945989909 } ], "File": "SampleText2.txt", "Line": 0 }`Contents of `SampleText3.txt.out`with line indents for readability:`{ "Entities": [ { "BeginOffset": 0, "EndOffset": 4, "Type": "NAME", "Score": 0.999949934606805 }, { "BeginOffset": 77, "EndOffset": 88, "Type": "ADDRESS", "Score": 0.9999035300466904 }, { "BeginOffset": 120, "EndOffset": 125, "Type": "NAME", "Score": 0.9998203838716296 }, { "BeginOffset": 129, "EndOffset": 144, "Type": "EMAIL", "Score": 0.9998313473105228 } ], "File": "SampleText3.txt", "Line": 0 }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartPiiEntitiesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-pii-entities-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-sentiment-detection-job`.

- **AWS CLI**
- 
            
                    **To start an asynchronous sentiment analysis job**The following `start-sentiment-detection-job`example starts an asynchronous sentiment analysis detection job for all files located at the address specified by the`--input-data-config`tag. The S3 bucket folder in this example contains`SampleMovieReview1.txt`,`SampleMovieReview2.txt`, and`SampleMovieReview3.txt`. When the job is complete, the folder,`output`, is placed at the location specified by the`--output-data-config`tag. The folder contains the file,`output.txt`, which contains the prevailing sentiments for each text file and the pre-trained model's confidence score for each prediction. The Json output is printed on one line per file, but is formatted here for readability.`aws comprehend start-sentiment-detection-job \ --job-name``example-sentiment-detection-job`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/MovieData"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`Contents of `SampleMovieReview1.txt`:`"The film, AnyMovie2, is fairly predictable and just okay."`Contents of `SampleMovieReview2.txt`:`"AnyMovie2 is the essential sci-fi film that I grew up watching when I was a kid. I highly recommend this movie."`Contents of `SampleMovieReview3.txt`:`"Don't get fooled by the 'awards' for AnyMovie2. All parts of the film were poorly stolen from other modern directors."`Output: `{ "JobId": "0b5001e25f62ebb40631a9a1a7fde7b3", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:sentiment-detection-job/0b5001e25f62ebb40631a9a1a7fde7b3", "JobStatus": "SUBMITTED" }`Contents of `output.txt`with line of indents for readability:`{ "File": "SampleMovieReview1.txt", "Line": 0, "Sentiment": "MIXED", "SentimentScore": { "Mixed": 0.6591159105300903, "Negative": 0.26492202281951904, "Neutral": 0.035430654883384705, "Positive": 0.04053137078881264 } } { "File": "SampleMovieReview2.txt", "Line": 0, "Sentiment": "POSITIVE", "SentimentScore": { "Mixed": 0.000008718466233403888, "Negative": 0.00006134175055194646, "Neutral": 0.0002941041602753103, "Positive": 0.9996358156204224 } } { "File": "SampleMovieReview3.txt", "Line": 0, "Sentiment": "NEGATIVE", "SentimentScore": { "Mixed": 0.004146667663007975, "Negative": 0.9645107984542847, "Neutral": 0.016559595242142677, "Positive": 0.014782938174903393 } } }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartSentimentDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-sentiment-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-targeted-sentiment-detection-job`.

- **AWS CLI**
- 
            
                    **To start an asynchronous targeted sentiment analysis job**The following `start-targeted-sentiment-detection-job`example starts an asynchronous targeted sentiment analysis detection job for all files located at the address specified by the`--input-data-config`tag. The S3 bucket folder in this example contains`SampleMovieReview1.txt`,`SampleMovieReview2.txt`, and`SampleMovieReview3.txt`. When the job is complete,`output.tar.gz`is placed at the location specified by the`--output-data-config`tag.`output.tar.gz`contains the files`SampleMovieReview1.txt.out`,`SampleMovieReview2.txt.out`, and`SampleMovieReview3.txt.out`, which each contain all of the named entities and associated sentiments for a single input text file.`aws comprehend start-targeted-sentiment-detection-job \ --job-name``targeted_movie_review_analysis1`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/MovieData"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`Contents of `SampleMovieReview1.txt`:`"The film, AnyMovie, is fairly predictable and just okay."`Contents of `SampleMovieReview2.txt`:`"AnyMovie is the essential sci-fi film that I grew up watching when I was a kid. I highly recommend this movie."`Contents of `SampleMovieReview3.txt`:`"Don't get fooled by the 'awards' for AnyMovie. All parts of the film were poorly stolen from other modern directors."`Output: `{ "JobId": "0b5001e25f62ebb40631a9a1a7fde7b3", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:targeted-sentiment-detection-job/0b5001e25f62ebb40631a9a1a7fde7b3", "JobStatus": "SUBMITTED" }`Contents of `SampleMovieReview1.txt.out`with line indents for readability:`{ "Entities": [ { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "BeginOffset": 4, "EndOffset": 8, "Score": 0.994972, "GroupScore": 1, "Text": "film", "Type": "MOVIE", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 1, "Positive": 0 } } } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "BeginOffset": 10, "EndOffset": 18, "Score": 0.631368, "GroupScore": 1, "Text": "AnyMovie", "Type": "ORGANIZATION", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Mixed": 0.001729, "Negative": 0.000001, "Neutral": 0.000318, "Positive": 0.997952 } } } ] } ], "File": "SampleMovieReview1.txt", "Line": 0 }`Contents of `SampleMovieReview2.txt.out`line indents for readability:`{ "Entities": [ { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "BeginOffset": 0, "EndOffset": 8, "Score": 0.854024, "GroupScore": 1, "Text": "AnyMovie", "Type": "MOVIE", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 0.000007, "Positive": 0.999993 } } }, { "BeginOffset": 104, "EndOffset": 109, "Score": 0.999129, "GroupScore": 0.502937, "Text": "movie", "Type": "MOVIE", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 0, "Positive": 1 } } }, { "BeginOffset": 33, "EndOffset": 37, "Score": 0.999823, "GroupScore": 0.999252, "Text": "film", "Type": "MOVIE", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 0.000001, "Positive": 0.999999 } } } ] }, { "DescriptiveMentionIndex": [ 0, 1, 2 ], "Mentions": [ { "BeginOffset": 43, "EndOffset": 44, "Score": 0.999997, "GroupScore": 1, "Text": "I", "Type": "PERSON", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 1, "Positive": 0 } } }, { "BeginOffset": 80, "EndOffset": 81, "Score": 0.999996, "GroupScore": 0.52523, "Text": "I", "Type": "PERSON", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 1, "Positive": 0 } } }, { "BeginOffset": 67, "EndOffset": 68, "Score": 0.999994, "GroupScore": 0.999499, "Text": "I", "Type": "PERSON", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 1, "Positive": 0 } } } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "BeginOffset": 75, "EndOffset": 78, "Score": 0.999978, "GroupScore": 1, "Text": "kid", "Type": "PERSON", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 1, "Positive": 0 } } } ] } ], "File": "SampleMovieReview2.txt", "Line": 0 }`Contents of `SampleMovieReview3.txt.out`with line indents for readability:`{ "Entities": [ { "DescriptiveMentionIndex": [ 1 ], "Mentions": [ { "BeginOffset": 64, "EndOffset": 68, "Score": 0.992953, "GroupScore": 0.999814, "Text": "film", "Type": "MOVIE", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0.000004, "Negative": 0.010425, "Neutral": 0.989543, "Positive": 0.000027 } } }, { "BeginOffset": 37, "EndOffset": 45, "Score": 0.999782, "GroupScore": 1, "Text": "AnyMovie", "Type": "ORGANIZATION", "MentionSentiment": { "Sentiment": "POSITIVE", "SentimentScore": { "Mixed": 0.000095, "Negative": 0.039847, "Neutral": 0.000673, "Positive": 0.959384 } } } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "BeginOffset": 47, "EndOffset": 50, "Score": 0.999991, "GroupScore": 1, "Text": "All", "Type": "QUANTITY", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0.000001, "Negative": 0.000001, "Neutral": 0.999998, "Positive": 0 } } } ] }, { "DescriptiveMentionIndex": [ 0 ], "Mentions": [ { "BeginOffset": 106, "EndOffset": 115, "Score": 0.542083, "GroupScore": 1, "Text": "directors", "Type": "PERSON", "MentionSentiment": { "Sentiment": "NEUTRAL", "SentimentScore": { "Mixed": 0, "Negative": 0, "Neutral": 1, "Positive": 0 } } } ] } ], "File": "SampleMovieReview3.txt", "Line": 0 }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartTargetedSentimentDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-targeted-sentiment-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-topics-detection-job`.

- **AWS CLI**
- 
            
                    **To start a topics detection analysis job**The following `start-topics-detection-job`example starts an asynchronous topics detection job for all files located at the address specified by the`--input-data-config`tag. When the job is complete, the folder,`output`, is placed at the location specified by the`--ouput-data-config`tag.`output`contains topic-terms.csv and doc-topics.csv. The first output file, topic-terms.csv, is a list of topics in the collection. For each topic, the list includes, by default, the top terms by topic according to their weight. The second file,`doc-topics.csv`, lists the documents associated with a topic and the proportion of the document that is concerned with the topic.`aws comprehend start-topics-detection-job \ --job-name``example_topics_detection_job`\ --language-code`en`\ --input-data-config`"S3Uri=s3://amzn-s3-demo-bucket/"`\ --output-data-config`"S3Uri=s3://amzn-s3-demo-destination-bucket/testfolder/"`\ --data-access-role-arn`arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role`\ --language-code`en`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE", "JobArn": "arn:aws:comprehend:us-west-2:111122223333:key-phrases-detection-job/123456abcdeb0e11022f22a11EXAMPLE", "JobStatus": "SUBMITTED" }`For more information, see [Topic Modeling](https://docs.aws.amazon.com/comprehend/latest/dg/topic-modeling.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StartTopicsDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/start-topics-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-dominant-language-detection-job`.

- **AWS CLI**
- 
            
                    **To stop an asynchronous dominant language detection job**The following `stop-dominant-language-detection-job`example stops an in-progress, asynchronous dominant language detection job. If the current job state is`IN_PROGRESS`the job is marked for termination and put into the`STOP_REQUESTED`state. If the job completes before it can be stopped, it is put into the`COMPLETED`state.`aws comprehend stop-dominant-language-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE, "JobStatus": "STOP_REQUESTED" }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopDominantLanguageDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-dominant-language-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-entities-detection-job`.

- **AWS CLI**
- 
            
                    **To stop an asynchronous entities detection job**The following `stop-entities-detection-job`example stops an in-progress, asynchronous entities detection job. If the current job state is`IN_PROGRESS`the job is marked for termination and put into the`STOP_REQUESTED`state. If the job completes before it can be stopped, it is put into the`COMPLETED`state.`aws comprehend stop-entities-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE, "JobStatus": "STOP_REQUESTED" }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopEntitiesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-entities-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-events-detection-job`.

- **AWS CLI**
- 
            
                    **To stop an asynchronous events detection job**The following `stop-events-detection-job`example stops an in-progress, asynchronous events detection job. If the current job state is`IN_PROGRESS`the job is marked for termination and put into the`STOP_REQUESTED`state. If the job completes before it can be stopped, it is put into the`COMPLETED`state.`aws comprehend stop-events-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE, "JobStatus": "STOP_REQUESTED" }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopEventsDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-events-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-key-phrases-detection-job`.

- **AWS CLI**
- 
            
                    **To stop an asynchronous key phrases detection job**The following `stop-key-phrases-detection-job`example stops an in-progress, asynchronous key phrases detection job. If the current job state is`IN_PROGRESS`the job is marked for termination and put into the`STOP_REQUESTED`state. If the job completes before it can be stopped, it is put into the`COMPLETED`state.`aws comprehend stop-key-phrases-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE, "JobStatus": "STOP_REQUESTED" }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopKeyPhrasesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-key-phrases-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-pii-entities-detection-job`.

- **AWS CLI**
- 
            
                    **To stop an asynchronous pii entities detection job**The following `stop-pii-entities-detection-job`example stops an in-progress, asynchronous pii entities detection job. If the current job state is`IN_PROGRESS`the job is marked for termination and put into the`STOP_REQUESTED`state. If the job completes before it can be stopped, it is put into the`COMPLETED`state.`aws comprehend stop-pii-entities-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE, "JobStatus": "STOP_REQUESTED" }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopPiiEntitiesDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-pii-entities-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-sentiment-detection-job`.

- **AWS CLI**
- 
            
                    **To stop an asynchronous sentiment detection job**The following `stop-sentiment-detection-job`example stops an in-progress, asynchronous sentiment detection job. If the current job state is`IN_PROGRESS`the job is marked for termination and put into the`STOP_REQUESTED`state. If the job completes before it can be stopped, it is put into the`COMPLETED`state.`aws comprehend stop-sentiment-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE, "JobStatus": "STOP_REQUESTED" }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopSentimentDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-sentiment-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-targeted-sentiment-detection-job`.

- **AWS CLI**
- 
            
                    **To stop an asynchronous targeted sentiment detection job**The following `stop-targeted-sentiment-detection-job`example stops an in-progress, asynchronous targeted sentiment detection job. If the current job state is`IN_PROGRESS`the job is marked for termination and put into the`STOP_REQUESTED`state. If the job completes before it can be stopped, it is put into the`COMPLETED`state.`aws comprehend stop-targeted-sentiment-detection-job \ --job-id``123456abcdeb0e11022f22a11EXAMPLE`Output: `{ "JobId": "123456abcdeb0e11022f22a11EXAMPLE, "JobStatus": "STOP_REQUESTED" }`For more information, see [Async analysis for Amazon Comprehend insights](https://docs.aws.amazon.com/comprehend/latest/dg/api-async-insights.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopTargetedSentimentDetectionJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-targeted-sentiment-detection-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-training-document-classifier`.

- **AWS CLI**
- 
            
                    **To stop the training of a document classifier model**The following `stop-training-document-classifier`example stops the training of a document classifier model while in-progress.`aws comprehend stop-training-document-classifier --document-classifier-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier`This command produces no output. For more information, see [Creating and managing custom models](https://docs.aws.amazon.com/comprehend/latest/dg/manage-models.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopTrainingDocumentClassifier](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-training-document-classifier.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `stop-training-entity-recognizer`.

- **AWS CLI**
- 
            
                    **To stop the training of an entity recognizer model**The following `stop-training-entity-recognizer`example stops the training of an entity recognizer model while in-progress.`aws comprehend stop-training-entity-recognizer --entity-recognizer-arn``"arn:aws:comprehend:us-west-2:111122223333:entity-recognizer/examplerecognizer1"`This command produces no output. For more information, see [Creating and managing custom models](https://docs.aws.amazon.com/comprehend/latest/dg/manage-models.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [StopTrainingEntityRecognizer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/stop-training-entity-recognizer.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To tag a resource**The following `tag-resource`example adds a single tag to an Amazon Comprehend resource.`aws comprehend tag-resource \ --resource-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1`\ --tags`Key=Location,Value=Seattle`This command has no output. For more information, see [Tagging your resources](https://docs.aws.amazon.com/comprehend/latest/dg/tagging.html)in the*Amazon Comprehend Developer Guide*.**Example 2: To add multiple tags to a resource**The following `tag-resource`example adds multiple tags to an Amazon Comprehend resource.`aws comprehend tag-resource \ --resource-arn``"arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1"`\ --tags`Key=location,Value=Seattle``Key=Department,Value=Finance`This command has no output. For more information, see [Tagging your resources](https://docs.aws.amazon.com/comprehend/latest/dg/tagging.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To remove a single tag from a resource**The following `untag-resource`example removes a single tag from an Amazon Comprehend resource.`aws comprehend untag-resource \ --resource-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1`--tag-keys`Location`This command produces no output. For more information, see [Tagging your resources](https://docs.aws.amazon.com/comprehend/latest/dg/tagging.html)in the*Amazon Comprehend Developer Guide*.**Example 2: To remove multiple tags from a resource**The following `untag-resource`example removes multiple tags from an Amazon Comprehend resource.`aws comprehend untag-resource \ --resource-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/1`--tag-keys`Location``Department`This command produces no output. For more information, see [Tagging your resources](https://docs.aws.amazon.com/comprehend/latest/dg/tagging.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-endpoint`.

- **AWS CLI**
- 
            
                    **Example 1: To update an endpoint's inference units**The following `update-endpoint`example updates information about an endpoint. In this example, the number of inference units is increased.`aws comprehend update-endpoint \ --endpoint-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint`--desired-inference-units`2`This command produces no output. For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.**Example 2: To update an endpoint's actie model**The following `update-endpoint`example updates information about an endpoint. In this example, the active model is changed.`aws comprehend update-endpoint \ --endpoint-arn``arn:aws:comprehend:us-west-2:111122223333:document-classifier-endpoint/example-classifier-endpoint`--active-model-arn`arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier-new`This command produces no output. For more information, see [Managing Amazon Comprehend endpoints](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [UpdateEndpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/update-endpoint.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-flywheel`.

- **AWS CLI**
- 
            
                    **To update a flywheel configuration**The following `update-flywheel`example updates a flywheel configuration. In this example, the active model for the flywheel is updated.`aws comprehend update-flywheel \ --flywheel-arn``arn:aws:comprehend:us-west-2:111122223333:flywheel/example-flywheel-1`\ --active-model-arn`arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/new-example-classifier-model`Output: `{ "FlywheelProperties": { "FlywheelArn": "arn:aws:comprehend:us-west-2:111122223333:flywheel/flywheel-entity", "ActiveModelArn": "arn:aws:comprehend:us-west-2:111122223333:document-classifier/example-classifier/version/new-example-classifier-model", "DataAccessRoleArn": "arn:aws:iam::111122223333:role/service-role/AmazonComprehendServiceRole-example-role", "TaskConfig": { "LanguageCode": "en", "DocumentClassificationConfig": { "Mode": "MULTI_CLASS" } }, "DataLakeS3Uri": "s3://amzn-s3-demo-bucket/flywheel-entity/schemaVersion=1/20230616T200543Z/", "DataSecurityConfig": {}, "Status": "ACTIVE", "ModelType": "DOCUMENT_CLASSIFIER", "CreationTime": "2023-06-16T20:05:43.242000+00:00", "LastModifiedTime": "2023-06-19T04:00:43.027000+00:00", "LatestFlywheelIteration": "20230619T040032Z" } }`For more information, see [Flywheel overview](https://docs.aws.amazon.com/comprehend/latest/dg/flywheels-about.html)in the*Amazon Comprehend Developer Guide*.- 
                    For API details, see [UpdateFlywheel](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/comprehend/update-flywheel.html)in*AWS CLI Command Reference*.
 
-