# Amazon Polly examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_polly_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_polly_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Polly.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `delete-lexicon`.

- **AWS CLI**
- 
            
                    **To delete a lexicon**The following `delete-lexicon`example deletes the specified lexicon.`aws polly delete-lexicon \ --name``w3c`This command produces no output. For more information, see [Using the DeleteLexicon operation](https://docs.aws.amazon.com/polly/latest/dg/gs-delete-lexicon.html)in the*Amazon Polly Developer Guide*.- 
                    For API details, see [DeleteLexicon](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/delete-lexicon.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-lexicon`.

- **AWS CLI**
- 
            
                    **To retrieve the content of a lexicon**The following `get-lexicon`example retrieves the content of the specified pronunciation lexicon.`aws polly get-lexicon \ --name``w3c`Output: `{ "Lexicon": { "Content": "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<lexicon version=\"1.0\" \n xmlns= \"http://www.w3.org/2005/01/pronunciation-lexicon\"\n xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" \n xsi:schemaLocation=\"http://www.w3.org/2005/01/pronunciation-lexicon \n http://www.w3.org/TR/2007/CR-pronunciation- lexicon-20071212/pls.xsd\"\n alphabet=\"ipa\" \n xml:lang=\"en-US\">\n <lexeme>\n <grapheme>W3C</grapheme>\n <alias>World Wide Web Consortium</alias>\n </lexeme>\n</lexicon>\n", "Name": "w3c" }, "LexiconAttributes": { "Alphabet": "ipa", "LanguageCode": "en-US", "LastModified": 1603908910.99, "LexiconArn": "arn:aws:polly:us-west-2:880185128111:lexicon/w3c", "LexemesCount": 1, "Size": 492 } }`For more information, see [Using the GetLexicon operation](https://docs.aws.amazon.com/polly/latest/dg/gs-get-lexicon.html)in the*Amazon Polly Developer Guide*.- 
                    For API details, see [GetLexicon](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-lexicon.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-speech-synthesis-task`.

- **AWS CLI**
- 
            
                    **To get information about a speech synthesis task**The following `get-speech-synthesis-task`example retrieves information about the specified speech synthesis task.`aws polly get-speech-synthesis-task \ --task-id``70b61c0f-57ce-4715-a247-cae8729dcce9`Output: `{ "SynthesisTask": { "TaskId": "70b61c0f-57ce-4715-a247-cae8729dcce9", "TaskStatus": "completed", "OutputUri": "https://s3.us-west-2.amazonaws.com/amzn-s3-demo-bucket/70b61c0f-57ce-4715-a247-cae8729dcce9.mp3", "CreationTime": 1603911042.689, "RequestCharacters": 1311, "OutputFormat": "mp3", "TextType": "text", "VoiceId": "Joanna" } }`For more information, see [Creating long audio files](https://docs.aws.amazon.com/polly/latest/dg/longer-cli.html)in the*Amazon Polly Developer Guide*.- 
                    For API details, see [GetSpeechSynthesisTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/get-speech-synthesis-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-lexicons`.

- **AWS CLI**
- 
            
                    **To list your lexicons**The following `list-lexicons`example lists your pronunciation lexicons.`aws polly list-lexicons`Output: `{ "Lexicons": [ { "Name": "w3c", "Attributes": { "Alphabet": "ipa", "LanguageCode": "en-US", "LastModified": 1603908910.99, "LexiconArn": "arn:aws:polly:us-east-2:123456789012:lexicon/w3c", "LexemesCount": 1, "Size": 492 } } ] }`For more information, see [Using the ListLexicons operation](https://docs.aws.amazon.com/polly/latest/dg/gs-list-lexicons.html)in the*Amazon Polly Developer Guide*.- 
                    For API details, see [ListLexicons](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-lexicons.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-speech-synthesis-tasks`.

- **AWS CLI**
- 
            
                    **To list your speech synthesis tasks**The following `list-speech-synthesis-tasks`example lists your speech synthesis tasks.`aws polly list-speech-synthesis-tasks`Output: `{ "SynthesisTasks": [ { "TaskId": "70b61c0f-57ce-4715-a247-cae8729dcce9", "TaskStatus": "completed", "OutputUri": "https://s3.us-west-2.amazonaws.com/amzn-s3-demo-bucket/70b61c0f-57ce-4715-a247-cae8729dcce9.mp3", "CreationTime": 1603911042.689, "RequestCharacters": 1311, "OutputFormat": "mp3", "TextType": "text", "VoiceId": "Joanna" } ] }`For more information, see [Creating long audio files](https://docs.aws.amazon.com/polly/latest/dg/longer-cli.html)in the*Amazon Polly Developer Guide*.- 
                    For API details, see [ListSpeechSynthesisTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/list-speech-synthesis-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `put-lexicon`.

- **AWS CLI**
- 
            
                    **To store a lexicon**The following `put-lexicon`example stores the specified pronunciation lexicon. The`example.pls`file specifies a W3C PLS-compliant lexicon.`aws polly put-lexicon \ --name``w3c`\ --content`file://example.pls`Contents of `example.pls``{ <?xml version="1.0" encoding="UTF-8"?> <lexicon version="1.0" xmlns="http://www.w3.org/2005/01/pronunciation-lexicon" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.w3.org/2005/01/pronunciation-lexicon http://www.w3.org/TR/2007/CR-pronunciation-lexicon-20071212/pls.xsd" alphabet="ipa" xml:lang="en-US"> <lexeme> <grapheme>W3C</grapheme> <alias>World Wide Web Consortium</alias> </lexeme> </lexicon> }`This command produces no output. For more information, see [Using the PutLexicon operation](https://docs.aws.amazon.com/polly/latest/dg/gs-put-lexicon.html)in the*Amazon Polly Developer Guide*.- 
                    For API details, see [PutLexicon](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/put-lexicon.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-speech-synthesis-task`.

- **AWS CLI**
- 
            
                    **To synthesize text**The following `start-speech-synthesis-task`example synthesizes the text in`text_file.txt`and stores the resulting MP3 file in the specified bucket.`aws polly start-speech-synthesis-task \ --output-format``mp3`\ --output-s3-bucket-name`amzn-s3-demo-bucket`\ --text`file://text_file.txt`\ --voice-id`Joanna`Output: `{ "SynthesisTask": { "TaskId": "70b61c0f-57ce-4715-a247-cae8729dcce9", "TaskStatus": "scheduled", "OutputUri": "https://s3.us-east-2.amazonaws.com/amzn-s3-demo-bucket/70b61c0f-57ce-4715-a247-cae8729dcce9.mp3", "CreationTime": 1603911042.689, "RequestCharacters": 1311, "OutputFormat": "mp3", "TextType": "text", "VoiceId": "Joanna" } }`For more information, see [Creating long audio files](https://docs.aws.amazon.com/polly/latest/dg/longer-cli.html)in the*Amazon Polly Developer Guide*.- 
                    For API details, see [StartSpeechSynthesisTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/polly/start-speech-synthesis-task.html)in*AWS CLI Command Reference*.
 
-