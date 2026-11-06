# Amazon Translate examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_translate_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_translate_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon Translate.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `import-terminology`.

- **AWS CLI**
- 
            
                    **To import a custom terminology from a file**The following `import-terminology`example creates a terminology called`MyTestTerminology`from the`test-terminology.csv`file:`aws translate import-terminology \ --name``MyTestTerminology`\ --description`"Creating a test terminology in AWS Translate"`\ --merge-strategy`OVERWRITE`\ --data-file`fileb://test-terminology.csv`\ --terminology-data`Format=CSV`Contents of `test-terminology.csv`:en,fr,es,zh Hello world!,Bonjour tout le monde!,Hola Mundo!,???? Amazon,Amazon,Amazon,Amazon Output: `{ "TerminologyProperties": { "SourceLanguageCode": "en", "Name": "MyTestTerminology", "TargetLanguageCodes": [ "fr", "es", "zh" ], "SizeBytes": 97, "LastUpdatedAt": 1571089500.851, "CreatedAt": 1571089500.851, "TermCount": 6, "Arn": "arn:aws:translate:us-west-2:123456789012:terminology/MyTestTerminology/LATEST", "Description": "Creating a test terminology in AWS Translate" } }`- 
                    For API details, see [ImportTerminology](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/translate/import-terminology.html)in*AWS CLI Command Reference*.
 
-