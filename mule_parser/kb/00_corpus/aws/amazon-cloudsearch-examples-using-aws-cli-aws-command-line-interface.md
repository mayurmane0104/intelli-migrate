# Amazon CloudSearch examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudsearch-domain_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_cloudsearch-domain_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Amazon CloudSearch.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `upload-documents`.

- **AWS CLI**
- 
            
                    The following `upload-documents`command uploads a batch of JSON documents to an Amazon CloudSearch domain:`aws cloudsearchdomain upload-documents --endpoint-url``https://doc-my-domain.us-west-1.cloudsearch.amazonaws.com`--content-type`application/json`--documents`document-batch.json`Output: `{ "status": "success", "adds": 5000, "deletes": 0 }`- 
                    For API details, see [UploadDocuments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearchdomain/upload-documents.html)in*AWS CLI Command Reference*.
 
-