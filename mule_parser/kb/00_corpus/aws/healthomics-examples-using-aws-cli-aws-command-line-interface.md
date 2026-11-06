# HealthOmics examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_omics_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_omics_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with HealthOmics.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `abort-multipart-read-set-upload`.

- **AWS CLI**
- 
            
                    **To stop a multipart read set upload**The following `abort-multipart-read-set-upload`example stops a multipart read set upload into your HealthOmics sequence store.`aws omics abort-multipart-read-set-upload \ --sequence-store-id``0123456789`\ --upload-id`1122334455`This command produces no output. For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [AbortMultipartReadSetUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/abort-multipart-read-set-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `accept-share`.

- **AWS CLI**
- 
            
                    **To accept a share of analytics store data**The following `accept-share`example accepts a share of HealthOmics analytics store data.`aws omics accept-share \ --share-id``"495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a"`Output: `{ "status": "ACTIVATING" }`For more information, see [Cross-account sharing](https://docs.aws.amazon.com/omics/latest/dev/cross-account-sharing.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [AcceptShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/accept-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `batch-delete-read-set`.

- **AWS CLI**
- 
            
                    **To delete multiple read sets**The following `batch-delete-read-set`example deletes two read sets.`aws omics batch-delete-read-set \ --sequence-store-id``1234567890`\ --ids`1234567890``0123456789`If there is an error deleting any of the specified read sets, the service returns an error list. `{ "errors": [ { "code": "", "id": "0123456789", "message": "The specified readset does not exist." } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [BatchDeleteReadSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/batch-delete-read-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-annotation-import-job`.

- **AWS CLI**
- 
            
                    **To cancel an annotation import job**The following `cancel-annotation-import-job`example cancels an annotation import job with ID`04f57618-xmpl-4fd0-9349-e5a85aefb997`.`aws omics cancel-annotation-import-job \ --job-id``04f57618-xmpl-4fd0-9349-e5a85aefb997`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [CancelAnnotationImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/cancel-annotation-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-run`.

- **AWS CLI**
- 
            
                    **To cancel a run**The following `cancel-run`example cancels a run with ID`1234567`.`aws omics cancel-run \ --id``1234567`For more information, see [Run lifecycle in a workflow](https://docs.aws.amazon.com/omics/latest/dev/monitoring-runs.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [CancelRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/cancel-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `cancel-variant-import-job`.

- **AWS CLI**
- 
            
                    **To cancel a variant import job**The following `cancel-variant-import-job`example cancels a variant import job with ID`69cb65d6-xmpl-4a4a-9025-4565794b684e`.`aws omics cancel-variant-import-job \ --job-id``69cb65d6-xmpl-4a4a-9025-4565794b684e`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [CancelVariantImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/cancel-variant-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `complete-multipart-read-set-upload`.

- **AWS CLI**
- 
            
                    **To conclude a multipart upload once you have uploaded all of the components.**The following `complete-multipart-read-set-upload`example concludes a multipart upload into a sequence store once all of the components have been uploaded.`aws omics complete-multipart-read-set-upload \ --sequence-store-id``0123456789`\ --upload-id`1122334455`\ --parts '`[{"checksum":"gaCBQMe+rpCFZxLpoP6gydBoXaKKDA/Vobh5zBDb4W4=","partNumber":1,"partSource":"SOURCE1"}]`'Output: `{ "readSetId": "0000000001" "readSetId": "0000000002" "readSetId": "0000000003" }`For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [CompleteMultipartReadSetUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/complete-multipart-read-set-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-annotation-store-version`.

- **AWS CLI**
- 
            
                    **To create a new version of an annotation store**The following `create-annotation-store-version`example creates a new version of an annotation store.`aws omics create-annotation-store-version \ --name``my_annotation_store`\ --version-name`my_version`Output: `{ "creationTime": "2023-07-21T17:15:49.251040+00:00", "id": "3b93cdef69d2", "name": "my_annotation_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:555555555555:referenceStore/6505293348/reference/5987565360" }, "status": "CREATING", "versionName": "my_version" }`For more information, see [Creating new versions of annotation stores](https://docs.aws.amazon.com/omics/latest/dev/annotation-store-versioning.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [CreateAnnotationStoreVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-annotation-store-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-annotation-store`.

- **AWS CLI**
- 
            
                    **Example 1: To create a VCF annotation store**The following `create-annotation-store`example creates a VCF format annotation store.`aws omics create-annotation-store \ --name``my_ann_store`\ --store-format`VCF`\ --reference`referenceArn=arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890`Output: `{ "creationTime": "2022-11-23T22:48:39.226492Z", "id": "0a91xmplc71f", "name": "my_ann_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "CREATING", "storeFormat": "VCF" }`**Example 2: To create a TSV annotation store**The following `create-annotation-store`example creates a TSV format annotation store.`aws omics create-annotation-store \ --name``tsv_ann_store`\ --store-format`TSV`\ --reference`referenceArn=arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890`\ --store-options`file://tsv-store-options.json``tsv-store-options.json`configures format options for annotations.`{ "tsvStoreOptions": { "annotationType": "CHR_START_END_ZERO_BASE", "formatToHeader": { "CHR": "chromosome", "START": "start", "END": "end" }, "schema": [ { "chromosome": "STRING" }, { "start": "LONG" }, { "end": "LONG" }, { "name": "STRING" } ] } }`Output: `{ "creationTime": "2022-11-30T01:28:08.525586Z", "id": "861cxmpl96b0", "name": "tsv_ann_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "CREATING", "storeFormat": "TSV", "storeOptions": { "tsvStoreOptions": { "annotationType": "CHR_START_END_ZERO_BASE", "formatToHeader": { "CHR": "chromosome", "END": "end", "START": "start" }, "schema": [ { "chromosome": "STRING" }, { "start": "LONG" }, { "end": "LONG" }, { "name": "STRING" } ] } } }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the Amazon Omics Developer Guide.- 
                    For API details, see [CreateAnnotationStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-annotation-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-multipart-read-set-upload`.

- **AWS CLI**
- 
            
                    **To begin a multipart read set upload.**The following `create-multipart-read-set-upload`example initiates a multipart read set upload.`aws omics create-multipart-read-set-upload \ --sequence-store-id``0123456789`\ --name`HG00146`\ --source-file-type`FASTQ`\ --subject-id`mySubject`\ --sample-id`mySample`\ --description`"FASTQ for HG00146"`\ --generated-from`"1000 Genomes"`Output: `{ "creationTime": "2022-07-13T23:25:20Z", "description": "FASTQ for HG00146", "generatedFrom": "1000 Genomes", "name": "HG00146", "sampleId": "mySample", "sequenceStoreId": "0123456789", "sourceFileType": "FASTQ", "subjectId": "mySubject", "uploadId": "1122334455" }`For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [CreateMultipartReadSetUpload](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-multipart-read-set-upload.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-reference-store`.

- **AWS CLI**
- 
            
                    **To create a reference store**The following `create-reference-store`example creates a reference store`my-ref-store`.`aws omics create-reference-store \ --name``my-ref-store`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890", "creationTime": "2022-11-22T22:13:25.947Z", "id": "1234567890", "name": "my-ref-store" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [CreateReferenceStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-reference-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-run-group`.

- **AWS CLI**
- 
            
                    **To create a run group**The following `create-run-group`example creates a run group named`cram-converter`.`aws omics create-run-group \ --name``cram-converter`\ --max-cpus`20`\ --max-gpus`10`\ --max-duration`600`\ --max-runs`5`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:runGroup/1234567", "id": "1234567", "tags": {} }`For more information, see [Creating run groups](https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [CreateRunGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-run-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-sequence-store`.

- **AWS CLI**
- 
            
                    **To create a sequence store**The following `create-sequence-store`example creates a sequence store.`aws omics create-sequence-store \ --name``my-seq-store`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:sequenceStore/1234567890", "creationTime": "2022-11-23T01:24:33.629Z", "id": "1234567890", "name": "my-seq-store" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [CreateSequenceStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-sequence-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-share`.

- **AWS CLI**
- 
            
                    **To create a share of a HealthOmics analytics store**The following `create-share`example shows how to create a share of a HealthOmics analytics store that can be accepted by a subscriber outside the account.`aws omics create-share \ --resource-arn``"arn:aws:omics:us-west-2:555555555555:variantStore/omics_dev_var_store"`\ --principal-subscriber`"123456789012"`\ --name`"my_Share-123"`Output: `{ "shareId": "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a", "name": "my_Share-123", "status": "PENDING" }`For more information, see [Cross-acount sharing](https://docs.aws.amazon.com/omics/latest/dev/cross-account-sharing.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [CreateShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-variant-store`.

- **AWS CLI**
- 
            
                    **To create a variant store**The following `create-variant-store`example creates a variant store named`my_var_store`.`aws omics create-variant-store \ --name``my_var_store`\ --reference`referenceArn=arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890`Output: `{ "creationTime": "2022-11-23T22:09:07.534499Z", "id": "02dexmplcfdd", "name": "my_var_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "CREATING" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [CreateVariantStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-variant-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-workflow`.

- **AWS CLI**
- 
            
                    **To create a workflow**The following `create-workflow`example creates a WDL workflow.`aws omics create-workflow \ --name``cram-converter`\ --engine`WDL`\ --definition-zip`fileb://workflow-crambam.zip`\ --parameter-template`file://workflow-params.json``workflow-crambam.zip`is a ZIP archive containing a workflow definition.`workflow-params.json`defines runtime parameters for the workflow.`{ "ref_fasta" : { "description": "Reference genome fasta file", "optional": false }, "ref_fasta_index" : { "description": "Index of the reference genome fasta file", "optional": false }, "ref_dict" : { "description": "dictionary file for 'ref_fasta'", "optional": false }, "input_cram" : { "description": "The Cram file to convert to BAM", "optional": false }, "sample_name" : { "description": "The name of the input sample, used to name the output BAM", "optional": false } }`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:workflow/1234567", "id": "1234567", "status": "CREATING", "tags": {} }`For more information, see [Creating private workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows-setup.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [CreateWorkflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-workflow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-annotation-store-versions`.

- **AWS CLI**
- 
            
                    **To delete an annotation store version**The following `delete-annotation-store-versions`example deletes an annotation store version.`aws omics delete-annotation-store-versions \ --name``my_annotation_store`\ --versions`my_version`Output: `{ "errors": [] }`For more information, see [Creating new versions of annotation stores](https://docs.aws.amazon.com/omics/latest/dev/annotation-store-versioning.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [DeleteAnnotationStoreVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-annotation-store-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-annotation-store`.

- **AWS CLI**
- 
            
                    **To delete an annotation store**The following `delete-annotation-store`example deletes an annotation store named`my_vcf_store`.`aws omics delete-annotation-store \ --name``my_vcf_store`Output: `{ "status": "DELETING" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [DeleteAnnotationStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-annotation-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-reference-store`.

- **AWS CLI**
- 
            
                    **To delete a reference store**The following `delete-reference-store`example deletes a reference store with ID`1234567890`.`aws omics delete-reference-store \ --id``1234567890`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [DeleteReferenceStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-reference-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-reference`.

- **AWS CLI**
- 
            
                    **To delete a reference**The following `delete-reference`example deletes a reference.`aws omics delete-reference \ --reference-store-id``1234567890`\ --id`1234567890`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [DeleteReference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-reference.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-run-group`.

- **AWS CLI**
- 
            
                    **To delete a run group**The following `delete-run-group`example deletes a run group with ID`1234567`.`aws omics delete-run-group \ --id``1234567`For more information, see [Deleting runs and run groups](https://docs.aws.amazon.com/omics/latest/dev/deleting-workflows-and-runs.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [DeleteRunGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-run-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-run`.

- **AWS CLI**
- 
            
                    **To delete a workflow run**The following `delete-run`example deletes a run with ID`1234567`.`aws omics delete-run \ --id``1234567`For more information, see [Deleting runs and run groups](https://docs.aws.amazon.com/omics/latest/dev/deleting-workflows-and-runs.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [DeleteRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-sequence-store`.

- **AWS CLI**
- 
            
                    **To delete a sequence store**The following `delete-sequence-store`example deletes a sequence store with ID`1234567890`.`aws omics delete-sequence-store \ --id``1234567890`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [DeleteSequenceStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-sequence-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-share`.

- **AWS CLI**
- 
            
                    **To delete a share of HealthOmics analytics data**The following `delete-share`example deletes a cross-account share of analytics data.`aws omics delete-share \ --share-id``"495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a"`Output: `{ "status": "DELETING" }`For more information, see [Cross-account sharing](https://docs.aws.amazon.com/omics/latest/dev/cross-account-sharing.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [DeleteShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-variant-store`.

- **AWS CLI**
- 
            
                    **To delete a variant store**The following `delete-variant-store`example deletes a variant store named`my_var_store`.`aws omics delete-variant-store \ --name``my_var_store`Output: `{ "status": "DELETING" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [DeleteVariantStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-variant-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-workflow`.

- **AWS CLI**
- 
            
                    **To delete a workflow**The following `delete-workflow`example deletes a workflow with ID`1234567`.`aws omics delete-workflow \ --id``1234567`For more information, see [Delete a private workflow](https://docs.aws.amazon.com/omics/latest/dev/delete-private-workflow.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [DeleteWorkflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/delete-workflow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-annotation-import-job`.

- **AWS CLI**
- 
            
                    **To view an annotation import job**The following `get-annotation-import-job`example gets details about an annotation import job.`aws omics get-annotation-import-job \ --job-id``984162c7-xmpl-4d23-ab47-286f7950bfbf`Output: `{ "creationTime": "2022-11-30T01:40:11.017746Z", "destinationName": "tsv_ann_store", "id": "984162c7-xmpl-4d23-ab47-286f7950bfbf", "items": [ { "jobStatus": "COMPLETED", "source": "s3://omics-artifacts-01d6xmpl4e72dd32/targetedregions.bed.gz" } ], "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "runLeftNormalization": false, "status": "COMPLETED", "updateTime": "2022-11-30T01:42:39.134009Z" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetAnnotationImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-annotation-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-annotation-store-version`.

- **AWS CLI**
- 
            
                    **To retrieve the metadata for an annotation store version**The following `get-annotation-store-version`example retrieves the metadata for the requested annotation store version.`aws omics get-annotation-store-version \ --name``my_annotation_store`\ --version-name`my_version`Output: `{ "storeId": "4934045d1c6d", "id": "2a3f4a44aa7b", "status": "ACTIVE", "versionArn": "arn:aws:omics:us-west-2:555555555555:annotationStore/my_annotation_store/version/my_version", "name": "my_annotation_store", "versionName": "my_version", "creationTime": "2023-07-21T17:15:49.251040+00:00", "updateTime": "2023-07-21T17:15:56.434223+00:00", "statusMessage": "", "versionSizeBytes": 0 }`For more information, see [Creating new versions of annotation stores](https://docs.aws.amazon.com/omics/latest/dev/annotation-store-versioning.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [GetAnnotationStoreVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-annotation-store-version.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-annotation-store`.

- **AWS CLI**
- 
            
                    **To view an annotation store**The following `get-annotation-store`example gets details about an annotation store named`my_ann_store`.`aws omics get-annotation-store \ --name``my_ann_store`Output: `{ "creationTime": "2022-11-23T22:48:39.226492Z", "id": "0a91xmplc71f", "name": "my_ann_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "CREATING", "storeArn": "arn:aws:omics:us-west-2:123456789012:annotationStore/my_ann_store", "storeFormat": "VCF", "storeSizeBytes": 0, "tags": {} }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetAnnotationStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-annotation-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-read-set-activation-job`.

- **AWS CLI**
- 
            
                    **To view a read set activation job**The following `get-read-set-activation-job`example gets details about a read set activation job.`aws omics get-read-set-activation-job \ --sequence-store-id``1234567890`\ --id`1234567890`Output: `{ "completionTime": "2022-12-06T22:33:42.828Z", "creationTime": "2022-12-06T22:32:45.213Z", "id": "1234567890", "sequenceStoreId": "1234567890", "sources": [ { "readSetId": "1234567890", "status": "FINISHED", "statusMessage": "No activation needed as read set is already in ACTIVATING or ACTIVE state." } ], "status": "COMPLETED", "statusMessage": "The job completed successfully." }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReadSetActivationJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-read-set-activation-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-read-set-export-job`.

- **AWS CLI**
- 
            
                    **To view a read set export job**The following `get-read-set-export-job`example gets details about a read set export job.`aws omics get-read-set-export-job \ --sequence-store-id``1234567890`\ --id`1234567890`Output: `{ "completionTime": "2022-12-06T22:39:14.491Z", "creationTime": "2022-12-06T22:37:18.612Z", "destination": "s3://omics-artifacts-01d6xmpl4e72dd32/read-set-export/", "id": "1234567890", "sequenceStoreId": "1234567890", "status": "COMPLETED", "statusMessage": "The job is submitted and will start soon." }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReadSetExportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-read-set-export-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-read-set-import-job`.

- **AWS CLI**
- 
            
                    **To view a read set import job**The following `get-read-set-import-job`example gets details about a read set import job.`aws omics get-read-set-import-job \ --sequence-store-id``1234567890`\ --id`1234567890`Output: `{ "creationTime": "2022-11-23T01:36:38.158Z", "id": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "sequenceStoreId": "1234567890", "sources": [ { "name": "HG00100", "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "sampleId": "bam-sample", "sourceFileType": "BAM", "sourceFiles": { "source1": "s3://omics-artifacts-01d6xmpl4e72dd32/HG00100.chrom20.ILLUMINA.bwa.GBR.low_coverage.20101123.bam", "source2": "" }, "status": "IN_PROGRESS", "statusMessage": "The source job is currently in progress.", "subjectId": "bam-subject", "tags": { "aws:omics:sampleId": "bam-sample", "aws:omics:subjectId": "bam-subject" } }, { "name": "HG00146", "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "sampleId": "fastq-sample", "sourceFileType": "FASTQ", "sourceFiles": { "source1": "s3://omics-artifacts-01d6xmpl4e72dd32/SRR233106_1.filt.fastq.gz", "source2": "s3://omics-artifacts-01d6xmpl4e72dd32/SRR233106_2.filt.fastq.gz" }, "status": "IN_PROGRESS", "statusMessage": "The source job is currently in progress.", "subjectId": "fastq-subject", "tags": { "aws:omics:sampleId": "fastq-sample", "aws:omics:subjectId": "fastq-subject" } }, { "name": "HG00096", "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "sampleId": "cram-sample", "sourceFileType": "CRAM", "sourceFiles": { "source1": "s3://omics-artifacts-01d6xmpl4e72dd32/HG00096.alt_bwamem_GRCh38DH.20150718.GBR.low_coverage.cram", "source2": "" }, "status": "IN_PROGRESS", "statusMessage": "The source job is currently in progress.", "subjectId": "cram-subject", "tags": { "aws:omics:sampleId": "cram-sample", "aws:omics:subjectId": "cram-subject" } } ], "status": "IN_PROGRESS", "statusMessage": "The job is currently in progress." }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReadSetImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-read-set-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-read-set-metadata`.

- **AWS CLI**
- 
            
                    **To view a read set**The following `get-read-set-metadata`example gets details about a read set's files.`aws omics get-read-set-metadata \ --sequence-store-id``1234567890`\ --id`1234567890`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:sequenceStore/1234567890/readSet/1234567890", "creationTime": "2022-11-23T21:55:00.515Z", "fileType": "FASTQ", "files": { "source1": { "contentLength": 310054739, "partSize": 104857600, "totalParts": 3 }, "source2": { "contentLength": 307846621, "partSize": 104857600, "totalParts": 3 } }, "id": "1234567890", "name": "HG00146", "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "sampleId": "fastq-sample", "sequenceInformation": { "alignment": "UNALIGNED", "totalBaseCount": 677717384, "totalReadCount": 8917334 }, "sequenceStoreId": "1234567890", "status": "ACTIVE", "subjectId": "fastq-subject" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReadSetMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-read-set-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-read-set`.

- **AWS CLI**
- 
            
                    **To download a read set**The following `get-read-set`example downloads part 3 of a read set as`1234567890.3.bam`.`aws omics get-read-set \ --sequence-store-id``1234567890`\ --id`1234567890`\ --part-number`3``1234567890.3.bam`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReadSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-read-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reference-import-job`.

- **AWS CLI**
- 
            
                    **To view a reference import job**The following `get-reference-import-job`example example gets details about a reference import job.`aws omics get-reference-import-job \ --reference-store-id``1234567890`\ --id`1234567890`Output: `{ "creationTime": "2022-11-22T22:25:41.124Z", "id": "1234567890", "referenceStoreId": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "sources": [ { "name": "assembly-38", "sourceFile": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta", "status": "IN_PROGRESS", "statusMessage": "The source job is currently in progress." } ], "status": "IN_PROGRESS", "statusMessage": "The job is currently in progress." }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReferenceImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-reference-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reference-metadata`.

- **AWS CLI**
- 
            
                    **To view a reference**The following `get-reference-metadata`example gets details about a reference.`aws omics get-reference-metadata \ --reference-store-id``1234567890`\ --id`1234567890`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "creationTime": "2022-11-22T22:27:09.033Z", "files": { "index": { "contentLength": 160928, "partSize": 104857600, "totalParts": 1 }, "source": { "contentLength": 3249912778, "partSize": 104857600, "totalParts": 31 } }, "id": "1234567890", "md5": "7ff134953dcca8c8997453bbb80b6b5e", "name": "assembly-38", "referenceStoreId": "1234567890", "status": "ACTIVE", "updateTime": "2022-11-22T22:27:09.033Z" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReferenceMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-reference-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reference-store`.

- **AWS CLI**
- 
            
                    **To view a reference store**The following `get-reference-store`example gets details about a reference store.`aws omics get-reference-store \ --id``1234567890`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890", "creationTime": "2022-09-23T23:27:20.364Z", "id": "1234567890", "name": "my-rstore-0" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReferenceStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-reference-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-reference`.

- **AWS CLI**
- 
            
                    **To download a genome reference**The following `get-reference`example downloads part 1 of a genome as`hg38.1.fa`.`aws omics get-reference \ --reference-store-id``1234567890`\ --id`1234567890`\ --part-number`1``hg38.1.fa`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetReference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-reference.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-run-group`.

- **AWS CLI**
- 
            
                    **To view a run group**The following `get-run-group`example gets details about a run group.`aws omics get-run-group \ --id``1234567`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:runGroup/1234567", "creationTime": "2022-12-01T00:58:42.915219Z", "id": "1234567", "maxCpus": 20, "maxDuration": 600, "name": "cram-convert", "tags": {} }`For more information, see [Creating run groups](https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [GetRunGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-run-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-run-task`.

- **AWS CLI**
- 
            
                    **To view a task**The following `get-run-task`example gets details about a workflow task.`aws omics get-run-task \ --id``1234567`\ --task-id`1234567`Output: `{ "cpus": 1, "creationTime": "2022-11-30T23:13:00.718651Z", "logStream": "arn:aws:logs:us-west-2:123456789012:log-group:/aws/omics/WorkflowLog:log-stream:run/1234567/task/1234567", "memory": 15, "name": "CramToBamTask", "startTime": "2022-11-30T23:17:47.016Z", "status": "COMPLETED", "stopTime": "2022-11-30T23:18:21.503Z", "taskId": "1234567" }`For more information, see [Task lifecycle in a HealthOmics run](https://docs.aws.amazon.com/omics/latest/dev/workflow-run-tasks.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [GetRunTask](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-run-task.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-run`.

- **AWS CLI**
- 
            
                    **To view a workflow run**The following `get-run`example gets details about a workflow run.`aws omics get-run \ --id``1234567`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567", "creationTime": "2022-11-30T22:58:22.615865Z", "digest": "sha256:c54bxmpl742dcc26f7fa1f10e37550ddd8f251f418277c0a58e895b801ed28cf", "id": "1234567", "name": "cram-to-bam", "outputUri": "s3://omics-artifacts-01d6xmpl4e72dd32/workflow-output/", "parameters": { "ref_dict": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict", "ref_fasta_index": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta.fai", "ref_fasta": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta", "sample_name": "NA12878", "input_cram": "s3://omics-artifacts-01d6xmpl4e72dd32/NA12878.cram" }, "resourceDigests": { "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta.fai": "etag:f76371b113734a56cde236bc0372de0a", "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict": "etag:3884c62eb0e53fa92459ed9bff133ae6", "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta": "etag:e307d81c605fb91b7720a08f00276842-388", "s3://omics-artifacts-01d6xmpl4e72dd32/NA12878.cram": "etag:a9f52976381286c6143b5cc681671ec6" }, "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "startedBy": "arn:aws:iam::123456789012:user/laptop-2020", "status": "STARTING", "tags": {}, "workflowId": "1234567", "workflowType": "PRIVATE" }`For more information, see [Run lifecycle in a workflow](https://docs.aws.amazon.com/omics/latest/dev/monitoring-runs.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [GetRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-sequence-store`.

- **AWS CLI**
- 
            
                    **To view a sequence store**The following `get-sequence-store`example gets details about a sequence store with ID`1234567890`.`aws omics get-sequence-store \ --id``1234567890`Output: `{ "arn": "arn:aws:omics:us-east-1:123456789012:sequenceStore/1234567890", "creationTime": "2022-11-23T19:55:48.376Z", "id": "1234567890", "name": "my-seq-store" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetSequenceStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-sequence-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-share`.

- **AWS CLI**
- 
            
                    **To retrieves the metadata about a share of a HealthOmics analytics data**The following `get-share`example retrieves the metadata for a cross-account share of analytics data.`aws omics get-share \ --share-id``"495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a"`Output: `{ "share": { "shareId": "495c21bedc889d07d0ab69d710a6841e-dd75ab7a1a9c384fa848b5bd8e5a7e0a", "name": "my_Share-123", "resourceArn": "arn:aws:omics:us-west-2:555555555555:variantStore/omics_dev_var_store", "principalSubscriber": "123456789012", "ownerId": "555555555555", "status": "PENDING" } }`For more information, see [Cross-account sharing](https://docs.aws.amazon.com/omics/latest/dev/cross-account-sharing.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [GetShare](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-share.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-variant-import-job`.

- **AWS CLI**
- 
            
                    **To view a variant import job**The following `get-variant-import-job`example gets details about a variant import job.`aws omics get-variant-import-job \ --job-id``edd7b8ce-xmpl-47e2-bc99-258cac95a508`Output: `{ "creationTime": "2022-11-23T22:42:50.037812Z", "destinationName": "my_var_store", "id": "edd7b8ce-xmpl-47e2-bc99-258cac95a508", "items": [ { "jobStatus": "IN_PROGRESS", "source": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.known_indels.vcf.gz" } ], "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "runLeftNormalization": false, "status": "IN_PROGRESS", "updateTime": "2022-11-23T22:43:05.898309Z" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetVariantImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-variant-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-variant-store`.

- **AWS CLI**
- 
            
                    **To view a variant store**The following `get-variant-store`example gets details about a variant store.`aws omics get-variant-store \ --name``my_var_store`Output: `{ "creationTime": "2022-11-23T22:09:07.534499Z", "id": "02dexmplcfdd", "name": "my_var_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "CREATING", "storeArn": "arn:aws:omics:us-west-2:123456789012:variantStore/my_var_store", "storeSizeBytes": 0, "tags": {}, "updateTime": "2022-11-23T22:09:24.931711Z" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [GetVariantStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-variant-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-workflow`.

- **AWS CLI**
- 
            
                    **To view a workflow**The following `get-workflow`example gets details about a workflow with ID`1234567`.`aws omics get-workflow \ --id``1234567`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:workflow/1234567", "creationTime": "2022-11-30T22:33:16.225368Z", "digest": "sha256:c54bxmpl742dcc26f7fa1f10e37550ddd8f251f418277c0a58e895b801ed28cf", "engine": "WDL", "id": "1234567", "main": "workflow-crambam.wdl", "name": "cram-converter", "parameterTemplate": { "ref_dict": { "description": "dictionary file for 'ref_fasta'" }, "ref_fasta_index": { "description": "Index of the reference genome fasta file" }, "ref_fasta": { "description": "Reference genome fasta file" }, "input_cram": { "description": "The Cram file to convert to BAM" }, "sample_name": { "description": "The name of the input sample, used to name the output BAM" } }, "status": "ACTIVE", "statusMessage": "workflow-crambam.wdl\n workflow CramToBamFlow\n call CramToBamTask\n call ValidateSamFile\n task CramToBamTask\n task ValidateSamFile\n", "tags": {}, "type": "PRIVATE" }`For more information, see [Creating private workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows-setup.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [GetWorkflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-workflow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-annotation-import-jobs`.

- **AWS CLI**
- 
            
                    **To get a list of annotation import jobs**The following `list-annotation-import-jobs`gets a list of annotation import jobs.`aws omics list-annotation-import-jobs`Output: `{ "annotationImportJobs": [ { "creationTime": "2022-11-30T01:39:41.478294Z", "destinationName": "gff_ann_store", "id": "18a9e792-xmpl-4869-a105-e5b602900444", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "runLeftNormalization": false, "status": "COMPLETED", "updateTime": "2022-11-30T01:47:09.145178Z" }, { "creationTime": "2022-11-30T00:45:58.007838Z", "destinationName": "my_ann_store", "id": "4e9eafc8-xmpl-431e-a0b2-3bda27cb600a", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "runLeftNormalization": false, "status": "FAILED", "updateTime": "2022-11-30T00:47:01.706325Z" } ] }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListAnnotationImportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-annotation-import-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-annotation-store-versions`.

- **AWS CLI**
- 
            
                    **To list all the versions of an annotation store.**The following `list-annotation-store-versions`example lists all versions that exist of an annotation store.`aws omics list-annotation-store-versions \ --name``my_annotation_store`Output: `{ "annotationStoreVersions": [ { "storeId": "4934045d1c6d", "id": "2a3f4a44aa7b", "status": "CREATING", "versionArn": "arn:aws:omics:us-west-2:555555555555:annotationStore/my_annotation_store/version/my_version_2", "name": "my_annotation_store", "versionName": "my_version_2", "creation Time": "2023-07-21T17:20:59.380043+00:00", "versionSizeBytes": 0 }, { "storeId": "4934045d1c6d", "id": "4934045d1c6d", "status": "ACTIVE", "versionArn": "arn:aws:omics:us-west-2:555555555555:annotationStore/my_annotation_store/version/my_version_1", "name": "my_annotation_store", "versionName": "my_version_1", "creationTime": "2023-07-21T17:15:49.251040+00:00", "updateTime": "2023-07-21T17:15:56.434223+00:00", "statusMessage": "", "versionSizeBytes": 0 } }`For more information, see [Creating new versions of annotation stores](https://docs.aws.amazon.com/omics/latest/dev/annotation-store-versioning.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListAnnotationStoreVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-annotation-store-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-annotation-stores`.

- **AWS CLI**
- 
            
                    **To get a list of annotation stores**The following `list-annotation-stores`example gets a list of annotation stores.`aws omics list-annotation-stores`Output: `{ "annotationStores": [ { "creationTime": "2022-11-23T22:48:39.226492Z", "id": "0a91xmplc71f", "name": "my_ann_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "ACTIVE", "statusMessage": "", "storeArn": "arn:aws:omics:us-west-2:123456789012:annotationStore/my_ann_store", "storeFormat": "VCF", "storeSizeBytes": 0, "updateTime": "2022-11-23T22:53:27.372840Z" } ] }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListAnnotationStores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-annotation-stores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-multipart-read-set-uploads`.

- **AWS CLI**
- 
            
                    **To list all multipart read set uploads and their statuses.**The following `list-multipart-read-set-uploads`example lists all multipart read set uploads and their statuses.`aws omics list-multipart-read-set-uploads \ --sequence-store-id``0123456789`Output: `{ "uploads": [ { "sequenceStoreId": "0123456789", "uploadId": "8749584421", "sourceFileType": "FASTQ", "subjectId": "mySubject", "sampleId": "mySample", "generatedFrom": "1000 Genomes", "name": "HG00146", "description": "FASTQ for HG00146", "creationTime": "2023-11-29T19:22:51.349298+00:00" }, { "sequenceStoreId": "0123456789", "uploadId": "5290538638", "sourceFileType": "BAM", "subjectId": "mySubject", "sampleId": "mySample", "generatedFrom": "1000 Genomes", "referenceArn": "arn:aws:omics:us-west-2:845448930428:referenceStore/8168613728/reference/2190697383", "name": "HG00146", "description": "BAM for HG00146", "creationTime": "2023-11-29T19:23:33.116516+00:00" }, { "sequenceStoreId": "0123456789", "uploadId": "4174220862", "sourceFileType": "BAM", "subjectId": "mySubject", "sampleId": "mySample", "generatedFrom": "1000 Genomes", "referenceArn": "arn:aws:omics:us-west-2:845448930428:referenceStore/8168613728/reference/2190697383", "name": "HG00147", "description": "BAM for HG00147", "creationTime": "2023-11-29T19:23:47.007866+00:00" } ] }`For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListMultipartReadSetUploads](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-multipart-read-set-uploads.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-read-set-activation-jobs`.

- **AWS CLI**
- 
            
                    **To get a list of read set activation jobs**The following `list-read-set-activation-jobs`example gets a list of activation jobs for a sequence store with id`1234567890`.`aws omics list-read-set-activation-jobs \ --sequence-store-id``1234567890`Output: `{ "activationJobs": [ { "completionTime": "2022-12-06T22:33:42.828Z", "creationTime": "2022-12-06T22:32:45.213Z", "id": "1234567890", "sequenceStoreId": "1234567890", "status": "COMPLETED" }, { "creationTime": "2022-12-06T22:35:10.100Z", "id": "1234567890", "sequenceStoreId": "1234567890", "status": "IN_PROGRESS" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListReadSetActivationJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-read-set-activation-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-read-set-export-jobs`.

- **AWS CLI**
- 
            
                    **To gets a list of read set export jobs**The following `list-read-set-export-jobs`example gets a list of export jobs for a sequence store with id`1234567890`.`aws omics list-read-set-export-jobs \ --sequence-store-id``1234567890`Output: `{ "exportJobs": [ { "completionTime": "2022-12-06T22:39:14.491Z", "creationTime": "2022-12-06T22:37:18.612Z", "destination": "s3://omics-artifacts-01d6xmpl4e72dd32/read-set-export/", "id": "1234567890", "sequenceStoreId": "1234567890", "status": "COMPLETED" }, { "creationTime": "2022-12-06T22:38:04.871Z", "destination": "s3://omics-artifacts-01d6xmpl4e72dd32/read-set-export/", "id": "1234567890", "sequenceStoreId": "1234567890", "status": "IN_PROGRESS" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListReadSetExportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-read-set-export-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-read-set-import-jobs`.

- **AWS CLI**
- 
            
                    **To get a list of read set import jobs**The following `list-read-set-import-jobs`example gets a list of import jobs for a sequence store with id`1234567890`.`aws omics list-read-set-import-jobs \ --sequence-store-id``1234567890`Output: `{ "importJobs": [ { "completionTime": "2022-11-29T18:17:49.244Z", "creationTime": "2022-11-29T17:32:47.700Z", "id": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "sequenceStoreId": "1234567890", "status": "COMPLETED" }, { "completionTime": "2022-11-23T22:01:34.090Z", "creationTime": "2022-11-23T21:52:43.289Z", "id": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "sequenceStoreId": "1234567890", "status": "COMPLETED_WITH_FAILURES" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListReadSetImportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-read-set-import-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-read-set-upload-parts`.

- **AWS CLI**
- 
            
                    **To list all parts in a requested multipart upload for a sequence store.**The following `list-read-set-upload-parts`example list all parts in a requested multipart upload for a sequence store.`aws omics list-read-set-upload-parts \ --sequence-store-id``0123456789`\ --upload-id`1122334455`\ --part-source`SOURCE1`Output: `{ "parts": [ { "partNumber": 1, "partSize": 94371840, "file": "SOURCE1", "checksum": "984979b9928ae8d8622286c4a9cd8e99d964a22d59ed0f5722e1733eb280e635", "lastUpdatedTime": "2023-02-02T20:14:47.533000+00:00" } { "partNumber": 2, "partSize": 10471840, "file": "SOURCE1", "checksum": "984979b9928ae8d8622286c4a9cd8e99d964a22d59ed0f5722e1733eb280e635", "lastUpdatedTime": "2023-02-02T20:14:47.533000+00:00" } ] }`For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListReadSetUploadParts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-read-set-upload-parts.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-read-sets`.

- **AWS CLI**
- 
            
                    **To get a list of read sets**The following `list-read-sets`example gets a list of read sets for a sequence store with id`1234567890`.`aws omics list-read-sets \ --sequence-store-id``1234567890`Output: `{ "readSets": [ { "arn": "arn:aws:omics:us-west-2:123456789012:sequenceStore/1234567890/readSet/1234567890", "creationTime": "2022-11-23T21:55:00.515Z", "fileType": "FASTQ", "id": "1234567890", "name": "HG00146", "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "sampleId": "fastq-sample", "sequenceStoreId": "1234567890", "status": "ACTIVE", "subjectId": "fastq-subject" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListReadSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-read-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-reference-import-jobs`.

- **AWS CLI**
- 
            
                    **To get a list of reference import jobs**The following `list-reference-import-jobs`example gets a list of reference import jobs for a reference store with id`1234567890`.`aws omics list-reference-import-jobs \ --reference-store-id``1234567890`Output: `{ "importJobs": [ { "completionTime": "2022-11-23T19:54:58.204Z", "creationTime": "2022-11-23T19:53:20.729Z", "id": "1234567890", "referenceStoreId": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "status": "COMPLETED" }, { "creationTime": "2022-11-23T20:34:03.250Z", "id": "1234567890", "referenceStoreId": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "status": "IN_PROGRESS" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListReferenceImportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-reference-import-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-reference-stores`.

- **AWS CLI**
- 
            
                    **To get a list of reference stores**The following `list-reference-stores`example gets a list of reference stores.`aws omics list-reference-stores`Output: `{ "referenceStores": [ { "arn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890", "creationTime": "2022-11-22T22:13:25.947Z", "id": "1234567890", "name": "my-ref-store" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListReferenceStores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-reference-stores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-references`.

- **AWS CLI**
- 
            
                    **To get a list of references**The following `list-references`example gets a list of genome references for a reference store with id`1234567890`.`aws omics list-references \ --reference-store-id``1234567890`Output: `{ "references": [ { "arn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "creationTime": "2022-11-22T22:27:09.033Z", "id": "1234567890", "md5": "7ff134953dcca8c8997453bbb80b6b5e", "name": "assembly-38", "referenceStoreId": "1234567890", "status": "ACTIVE", "updateTime": "2022-11-22T22:27:09.033Z" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListReferences](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-references.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-run-groups`.

- **AWS CLI**
- 
            
                    **To get a list of run groups**The following `list-run-groups`example gets a list of run groups.`aws omics list-run-groups`Output: `{ "items": [ { "arn": "arn:aws:omics:us-west-2:123456789012:runGroup/1234567", "creationTime": "2022-12-01T00:58:42.915219Z", "id": "1234567", "maxCpus": 20, "maxDuration": 600, "name": "cram-convert" } ] }`For more information, see [Creating run groups](https://docs.aws.amazon.com/omics/latest/dev/creating-run-groups.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListRunGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-run-groups.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-run-tasks`.

- **AWS CLI**
- 
            
                    **To get a list of tasks**The following `list-run-tasks`example gets a list of tasks for a workflow run.`aws omics list-run-tasks \ --id``1234567`Output: `{ "items": [ { "cpus": 1, "creationTime": "2022-11-30T23:13:00.718651Z", "memory": 15, "name": "CramToBamTask", "startTime": "2022-11-30T23:17:47.016Z", "status": "COMPLETED", "stopTime": "2022-11-30T23:18:21.503Z", "taskId": "1234567" }, { "cpus": 1, "creationTime": "2022-11-30T23:18:32.315606Z", "memory": 4, "name": "ValidateSamFile", "startTime": "2022-11-30T23:23:40.165Z", "status": "COMPLETED", "stopTime": "2022-11-30T23:24:14.766Z", "taskId": "1234567" } ] }`For more information, see [Task lifecycle in a HealthOmics run](https://docs.aws.amazon.com/omics/latest/dev/workflow-run-tasks.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListRunTasks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-run-tasks.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-runs`.

- **AWS CLI**
- 
            
                    **To get a list of workflow runs**The following `list-runs`example gets a list of workflow runs.`aws omics list-runs`Output: `{ "items": [ { "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567", "creationTime": "2022-12-02T23:20:01.202074Z", "id": "1234567", "name": "cram-to-bam", "priority": 1, "startTime": "2022-12-02T23:29:18.115Z", "status": "COMPLETED", "stopTime": "2022-12-02T23:57:54.428812Z", "storageCapacity": 10, "workflowId": "1234567" }, { "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567", "creationTime": "2022-12-03T00:16:57.180066Z", "id": "1234567", "name": "cram-to-bam", "priority": 1, "startTime": "2022-12-03T00:26:50.233Z", "status": "FAILED", "stopTime": "2022-12-03T00:37:21.451340Z", "storageCapacity": 10, "workflowId": "1234567" }, { "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567", "creationTime": "2022-12-05T17:57:08.444817Z", "id": "1234567", "name": "cram-to-bam", "status": "STARTING", "workflowId": "1234567" } ] }`For more information, see [Run lifecycle in a workflow](https://docs.aws.amazon.com/omics/latest/dev/monitoring-runs.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListRuns](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-runs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-sequence-stores`.

- **AWS CLI**
- 
            
                    **To get a list of sequence stores**The following `list-sequence-stores`example gets a list of sequence stores.`aws omics list-sequence-stores`Output: `{ "sequenceStores": [ { "arn": "arn:aws:omics:us-west-2:123456789012:sequenceStore/1234567890", "creationTime": "2022-11-23T01:24:33.629Z", "id": "1234567890", "name": "my-seq-store" } ] }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListSequenceStores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-sequence-stores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-shares`.

- **AWS CLI**
- 
            
                    **To list the available shares of a HealthOmics analytics data**The following `list-shares`example lists all shares that have been created for a resource-owner.`aws omics list-shares \ --resource-owner``SELF`Output: `{ "shares": [ { "shareId": "595c1cbd-a008-4eca-a887-954d30c91c6e", "name": "myShare", "resourceArn": "arn:aws:omics:us-west-2:555555555555:variantStore/store_1", "principalSubscriber": "123456789012", "ownerId": "555555555555", "status": "PENDING" } { "shareId": "39b65d0d-4368-4a19-9814-b0e31d73c10a", "name": "myShare3456", "resourceArn": "arn:aws:omics:us-west-2:555555555555:variantStore/store_2", "principalSubscriber": "123456789012", "ownerId": "555555555555", "status": "ACTIVE" }, { "shareId": "203152f5-eef9-459d-a4e0-a691668d44ef", "name": "myShare4", "resourceArn": "arn:aws:omics:us-west-2:555555555555:variantStore/store_3", "principalSubscriber": "123456789012", "ownerId": "555555555555", "status": "ACTIVE" } ] }`For more information, see [Cross-account sharing](https://docs.aws.amazon.com/omics/latest/dev/cross-account-sharing.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListShares](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-shares.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **To get a list of tags**The following `list-tags-for-resource`example gets a list of tags for a workflow with id`1234567`.`aws omics list-tags-for-resource \ --resource-arn``arn:aws:omics:us-west-2:123456789012:workflow/1234567`Output: `{ "tags": { "department": "analytics" } }`For more information, see [Tagging resources in Amazon Omics](https://docs.aws.amazon.com/omics/latest/dev/workflows.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-variant-import-jobs`.

- **AWS CLI**
- 
            
                    **To get a list of variant import jobs**The following `list-variant-import-jobs`example gets a list of variant import jobs.`aws omics list-variant-import-jobs`Output: `{ "variantImportJobs": [ { "creationTime": "2022-11-23T22:47:02.514002Z", "destinationName": "my_var_store", "id": "69cb65d6-xmpl-4a4a-9025-4565794b684e", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "runLeftNormalization": false, "status": "COMPLETED", "updateTime": "2022-11-23T22:49:17.976597Z" }, { "creationTime": "2022-11-23T22:42:50.037812Z", "destinationName": "my_var_store", "id": "edd7b8ce-xmpl-47e2-bc99-258cac95a508", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "runLeftNormalization": false, "status": "COMPLETED", "updateTime": "2022-11-23T22:45:26.009880Z" } ] }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListVariantImportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-variant-import-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-variant-stores`.

- **AWS CLI**
- 
            
                    **To get a list of variant stores**The following `list-variant-stores`example gets a list of variant stores.`aws omics list-variant-stores`Output: `{ "variantStores": [ { "creationTime": "2022-11-23T22:09:07.534499Z", "id": "02dexmplcfdd", "name": "my_var_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "CREATING", "storeArn": "arn:aws:omics:us-west-2:123456789012:variantStore/my_var_store", "storeSizeBytes": 0, "updateTime": "2022-11-23T22:09:24.931711Z" }, { "creationTime": "2022-09-23T23:00:09.140265Z", "id": "8777xmpl1a24", "name": "myvstore0", "status": "ACTIVE", "storeArn": "arn:aws:omics:us-west-2:123456789012:variantStore/myvstore0", "storeSizeBytes": 0, "updateTime": "2022-09-23T23:03:26.013220Z" } ] }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [ListVariantStores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-variant-stores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-workflows`.

- **AWS CLI**
- 
            
                    **To get a list of workflows**The following `list-workflows`example gets a list of workflows.`aws omics list-workflows`Output: `{ "items": [ { "arn": "arn:aws:omics:us-west-2:123456789012:workflow/1234567", "creationTime": "2022-09-23T23:08:22.041227Z", "digest": "nSCNo/qMWFxmplXpUdokXJnwgneOaxyyc2YOxVxrJTE=", "id": "1234567", "name": "my-wkflow-0", "status": "ACTIVE", "type": "PRIVATE" }, { "arn": "arn:aws:omics:us-west-2:123456789012:workflow/1234567", "creationTime": "2022-11-30T22:33:16.225368Z", "digest": "sha256:c54bxmpl742dcc26f7fa1f10e37550ddd8f251f418277c0a58e895b801ed28cf", "id": "1234567", "name": "cram-converter", "status": "ACTIVE", "type": "PRIVATE" } ] }`For more information, see [Creating private workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows-setup.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [ListWorkflows](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/list-workflows.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-annotation-import-job`.

- **AWS CLI**
- 
            
                    **To import annotations**The following `start-annotation-import-job`example imports annotations from Amazon S3.`aws omics start-annotation-import-job \ --destination-name``tsv_ann_store`\ --no-run-left-normalization \ --role-arn`arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ`\ --items`source=s3://omics-artifacts-01d6xmpl4e72dd32/targetedregions.bed.gz`Output: `{ "jobId": "984162c7-xmpl-4d23-ab47-286f7950bfbf" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [StartAnnotationImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-annotation-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-read-set-activation-job`.

- **AWS CLI**
- 
            
                    **To activate an archived read set**The following `start-read-set-activation-job`example activates two read sets.`aws omics start-read-set-activation-job \ --sequence-store-id``1234567890`\ --sources`readSetId=1234567890``readSetId=1234567890`Output: `{ "creationTime": "2022-12-06T22:35:10.100Z", "id": "1234567890", "sequenceStoreId": "1234567890", "status": "SUBMITTED" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [StartReadSetActivationJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-read-set-activation-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-read-set-export-job`.

- **AWS CLI**
- 
            
                    **To export a read set**The following `start-read-set-export-job`example exports two read sets to Amazon S3.`aws omics start-read-set-export-job \ --sequence-store-id 1234567890 \ --sources readSetId=1234567890 readSetId=1234567890 \ --role-arn arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ \ --destination s3://omics-artifacts-01d6xmpl4e72dd32/read-set-export/`Output: `{ "creationTime": "2022-12-06T22:37:18.612Z", "destination": "s3://omics-artifacts-01d6xmpl4e72dd32/read-set-export/", "id": "1234567890", "sequenceStoreId": "1234567890", "status": "SUBMITTED" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [StartReadSetExportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-read-set-export-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-read-set-import-job`.

- **AWS CLI**
- 
            
                    **To import a read set**The following `start-read-set-import-job`example imports a read set.`aws omics start-read-set-import-job \ --sequence-store-id``1234567890`\ --role-arn`arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ`\ --sources`file://readset-sources.json`readset-sources.json is a JSON document with the following content. `[ { "sourceFiles": { "source1": "s3://omics-artifacts-01d6xmpl4e72dd32/HG00100.chrom20.ILLUMINA.bwa.GBR.low_coverage.20101123.bam" }, "sourceFileType": "BAM", "subjectId": "bam-subject", "sampleId": "bam-sample", "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890", "name": "HG00100" } ]`Output: `{ "creationTime": "2022-11-23T01:36:38.158Z", "id": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "sequenceStoreId": "1234567890", "status": "SUBMITTED" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [StartReadSetImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-read-set-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-reference-import-job`.

- **AWS CLI**
- 
            
                    **To import a reference genome**The following `start-reference-import-job`example imports a reference genome from Amazon S3.`aws omics start-reference-import-job \ --reference-store-id``1234567890`\ --role-arn`arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ`\ --sources`sourceFile=s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta,name=assembly-38`Output: `{ "creationTime": "2022-11-22T22:25:41.124Z", "id": "1234567890", "referenceStoreId": "1234567890", "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ", "status": "SUBMITTED" }`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/sequence-stores.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [StartReferenceImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-reference-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-run`.

- **AWS CLI**
- 
            
                    **To run a workflow**The following `start-run`example runs a workflow with ID`1234567`.`aws omics start-run \ --workflow-id``1234567`\ --role-arn`arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ`\ --name '`cram-to-bam`' \ --output-uri`s3://omics-artifacts-01d6xmpl4e72dd32/workflow-output/`\ --run-group-id`1234567`\ --priority`1`\ --storage-capacity`10`\ --log-level`ALL`\ --parameters`file://workflow-inputs.json`workflow-inputs.json is a JSON document with the following content. `{ "sample_name": "NA12878", "input_cram": "s3://omics-artifacts-01d6xmpl4e72dd32/NA12878.cram", "ref_dict": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict", "ref_fasta": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta", "ref_fasta_index": "omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta.fai" }`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567", "id": "1234567", "status": "PENDING", "tags": {} }`For more information, see [Starting a run](https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html)in the*AWS HealthOmics User Guide*.**To load source files from Amazon Omics**You can also load source files from Amazon Omics storage, by using service-specific URIs. The following example workflow-inputs.json file uses Amazon Omics URIs for read set and reference genome sources. `{ "sample_name": "NA12878", "input_cram": "omics://123456789012.storage.us-west-2.amazonaws.com/1234567890/readSet/1234567890/source1", "ref_dict": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict", "ref_fasta": "omics://123456789012.storage.us-west-2.amazonaws.com/1234567890/reference/1234567890", "ref_fasta_index": "omics://123456789012.storage.us-west-2.amazonaws.com/1234567890/reference/1234567890/index" }`- 
                    For API details, see [StartRun](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-run.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-variant-import-job`.

- **AWS CLI**
- 
            
                    **To import a variant file**The following `start-variant-import-job`example imports a VCF format variant file.`aws omics start-variant-import-job \ --destination-name``my_var_store`\ --no-run-left-normalization \ --role-arn`arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ`\ --items`source=s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.known_indels.vcf.gz`Output: `{ "jobId": "edd7b8ce-xmpl-47e2-bc99-258cac95a508" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [StartVariantImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-variant-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **To tag a resource**The following `tag-resource`example adds a`department`tag to a workflow with id`1234567`.`aws omics tag-resource \ --resource-arn``arn:aws:omics:us-west-2:123456789012:workflow/1234567`\ --tags`department=analytics`For more information, see [Tagging resources in Amazon Omics](https://docs.aws.amazon.com/omics/latest/dev/workflows.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **To remove a tag from a resource**The following `untag-resource`example removes the`department`tag from a workflow.`aws omics untag-resource \ --resource-arn``arn:aws:omics:us-west-2:123456789012:workflow/1234567`\ --tag-keys`department`For more information, see [Omics Storage](https://docs.aws.amazon.com/omics/latest/dev/tagging.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-annotation-store`.

- **AWS CLI**
- 
            
                    **To update an annotation store**The following `update-annotation-store`example updates the description of an annotation store named`my_vcf_store`.`aws omics update-annotation-store \ --name``my_vcf_store`\ --description`"VCF annotation store"`Output: `{ "creationTime": "2022-12-05T18:00:56.101860Z", "description": "VCF annotation store", "id": "bd6axmpl2444", "name": "my_vcf_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "ACTIVE", "storeFormat": "VCF", "updateTime": "2022-12-05T18:13:16.100051Z" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [UpdateAnnotationStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/update-annotation-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-run-group`.

- **AWS CLI**
- 
            
                    **To update a run group**The following `update-run-group`example updates the settings of a run group with id`1234567`.`aws omics update-run-group \ --id``1234567`\ --max-cpus`10`Output: `{ "arn": "arn:aws:omics:us-west-2:123456789012:runGroup/1234567", "creationTime": "2022-12-01T00:58:42.915219Z", "id": "1234567", "maxCpus": 10, "maxDuration": 600, "name": "cram-convert", "tags": {} }`For more information, see [Omics Workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [UpdateRunGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/update-run-group.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-variant-store`.

- **AWS CLI**
- 
            
                    **To update a variant store**The following `update-variant-store`example updates the description of a variant store named`my_var_store`.`aws omics update-variant-store \ --name``my_var_store`\ --description`"variant store"`Output: `{ "creationTime": "2022-11-23T22:09:07.534499Z", "description": "variant store", "id": "02dexmplcfdd", "name": "my_var_store", "reference": { "referenceArn": "arn:aws:omics:us-west-2:123456789012:referenceStore/1234567890/reference/1234567890" }, "status": "ACTIVE", "updateTime": "2022-12-05T18:23:37.686402Z" }`For more information, see [Omics Analytics](https://docs.aws.amazon.com/omics/latest/dev/omics-analytics.html)in the*Amazon Omics Developer Guide*.- 
                    For API details, see [UpdateVariantStore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/update-variant-store.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-workflow`.

- **AWS CLI**
- 
            
                    **To update a workflow**The following `update-workflow`example updates the description of a workflow with ID`1234567`.`aws omics update-workflow \ --id``1234567`\ --description`"copy workflow"`For more information, see [Creating or updating a workflow](https://docs.aws.amazon.com/omics/latest/dev/creating-private-workflows.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [UpdateWorkflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/update-workflow.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `upload-read-set-part`.

- **AWS CLI**
- 
            
                    **To upload a read set part.**The following `upload-read-set-part`example uploads a specified part of a read set.`aws omics upload-read-set-part \ --sequence-store-id``0123456789`\ --upload-id`1122334455`\ --part-source`SOURCE1`\ --part-number`1`\ --payload`/path/to/file/read_1_part_1.fastq.gz`Output: `{ "checksum": "984979b9928ae8d8622286c4a9cd8e99d964a22d59ed0f5722e1733eb280e635" }`For more information, see [Direct upload to a sequence store](https://docs.aws.amazon.com/omics/latest/dev/synchronous-uploads.html)in the*AWS HealthOmics User Guide*.- 
                    For API details, see [UploadReadSetPart](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/upload-read-set-part.html)in*AWS CLI Command Reference*.
 
-