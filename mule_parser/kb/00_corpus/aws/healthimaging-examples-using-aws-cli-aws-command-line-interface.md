# HealthImaging examples using AWS CLI - AWS Command Line Interface

**Source:** [https://docs.aws.amazon.com/cli/latest/userguide/cli_medical-imaging_code_examples.html](https://docs.aws.amazon.com/cli/latest/userguide/cli_medical-imaging_code_examples.html)

---

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with HealthImaging.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

###### Topics

## Actions

    The following code example shows how to use `copy-image-set`.

- **AWS CLI**
- 
            
                    **Example 1: To copy an image set without a destination.**The following `copy-image-set`example makes a duplicate copy of an image set without a destination.`aws medical-imaging copy-image-set \ --datastore-id``12345678901234567890123456789012`\ --source-image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\ --copy-image-set-information '`{"sourceImageSet": {"latestVersionId": "1" } }`'Output: `{ "destinationImageSetProperties": { "latestVersionId": "2", "imageSetWorkflowStatus": "COPYING", "updatedAt": 1680042357.432, "imageSetId": "b9a06fef182a5f992842f77f8e0868e5", "imageSetState": "LOCKED", "createdAt": 1680042357.432 }, "sourceImageSetProperties": { "latestVersionId": "1", "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS", "updatedAt": 1680042357.432, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "LOCKED", "createdAt": 1680027126.436 }, "datastoreId": "12345678901234567890123456789012" }`**Example 2: To copy an image set with a destination.**The following `copy-image-set`example makes a duplicate copy of an image set with a destination.`aws medical-imaging copy-image-set \ --datastore-id``12345678901234567890123456789012`\ --source-image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\ --copy-image-set-information '`{"sourceImageSet": {"latestVersionId": "1" }, "destinationImageSet": { "imageSetId": "b9a06fef182a5f992842f77f8e0868e5", "latestVersionId": "1"} }`'Output: `{ "destinationImageSetProperties": { "latestVersionId": "2", "imageSetWorkflowStatus": "COPYING", "updatedAt": 1680042505.135, "imageSetId": "b9a06fef182a5f992842f77f8e0868e5", "imageSetState": "LOCKED", "createdAt": 1680042357.432 }, "sourceImageSetProperties": { "latestVersionId": "1", "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS", "updatedAt": 1680042505.135, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "LOCKED", "createdAt": 1680027126.436 }, "datastoreId": "12345678901234567890123456789012" }`**Example 3: To copy a subset of instances from a source image set to a destination image set.**The following `copy-image-set`example copies one DICOM instance from the source image set to the destination image set. The force parameter is provided to override inconsistencies in the Patient, Study, and Series level attributes.`aws medical-imaging copy-image-set \ --datastore-id``12345678901234567890123456789012`\ --source-image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\ --copy-image-set-information '`{"sourceImageSet": {"latestVersionId": "1","DICOMCopies": {"copiableAttributes": "{\"SchemaVersion\":\"1.1\",\"Study\":{\"Series\":{\"1.3.6.1.4.1.5962.99.1.3673257865.2104868982.1369432891697.3666.0\":{\"Instances\":{\"1.3.6.1.4.1.5962.99.1.3673257865.2104868982.1369432891697.3669.0\":{}}}}}}"}},"destinationImageSet": {"imageSetId": "b9eb50d8ee682eb9fcf4acbf92f62bb7","latestVersionId": "1"}}`' \ --forceOutput: `{ "destinationImageSetProperties": { "latestVersionId": "2", "imageSetWorkflowStatus": "COPYING", "updatedAt": 1680042505.135, "imageSetId": "b9eb50d8ee682eb9fcf4acbf92f62bb7", "imageSetState": "LOCKED", "createdAt": 1680042357.432 }, "sourceImageSetProperties": { "latestVersionId": "1", "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS", "updatedAt": 1680042505.135, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "LOCKED", "createdAt": 1680027126.436 }, "datastoreId": "12345678901234567890123456789012" }`For more information, see [Copying an image set](https://docs.aws.amazon.com/healthimaging/latest/devguide/copy-image-set.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [CopyImageSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/copy-image-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `create-datastore`.

- **AWS CLI**
- 
            
                    **Example 1: To create a data store**The following `create-datastore`code example creates a data store with the name`my-datastore`. When you create a datastore without specifying a`--lossless-storage-format`, AWS HealthImaging defaults to HTJ2K (High Throughput JPEG 2000).`aws medical-imaging create-datastore \ --datastore-name``"my-datastore"`Output: `{ "datastoreId": "12345678901234567890123456789012", "datastoreStatus": "CREATING" }`**Example 2: To create a data store with JPEG 2000 Lossless storage format**A data store configured with JPEG 2000 Lossless storage format will transcode and persist lossless image frames in JPEG 2000 format. Image frames can then be retrieved in JPEG 2000 Lossless without transcoding. The following `create-datastore`code example creates a data store configured for JPEG 2000 Lossless storage format with the name`my-datastore`.`aws medical-imaging create-datastore \ --datastore-name``"my-datastore"`\ --lossless-storage-format`JPEG_2000_LOSSLESS`Output: `{ "datastoreId": "12345678901234567890123456789012", "datastoreStatus": "CREATING" }`For more information, see [Creating a data store](https://docs.aws.amazon.com/healthimaging/latest/devguide/create-data-store.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [CreateDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/create-datastore.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-datastore`.

- **AWS CLI**
- 
            
                    **To delete a data store**The following `delete-datastore`code example deletes a data store.`aws medical-imaging delete-datastore \ --datastore-id``"12345678901234567890123456789012"`Output: `{ "datastoreId": "12345678901234567890123456789012", "datastoreStatus": "DELETING" }`For more information, see [Deleting a data store](https://docs.aws.amazon.com/healthimaging/latest/devguide/delete-data-store.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [DeleteDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-datastore.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `delete-image-set`.

- **AWS CLI**
- 
            
                    **To delete an image set**The following `delete-image-set`code example deletes an image set.`aws medical-imaging delete-image-set \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`ea92b0d8838c72a3f25d00d13616f87e`Output: `{ "imageSetWorkflowStatus": "DELETING", "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "LOCKED", "datastoreId": "12345678901234567890123456789012" }`For more information, see [Deleting an image set](https://docs.aws.amazon.com/healthimaging/latest/devguide/delete-image-set.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [DeleteImageSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/delete-image-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-datastore`.

- **AWS CLI**
- 
            
                    **Example 1: To get a data store's properties**The following `get-datastore`code example gets a data store's properties.`aws medical-imaging get-datastore \ --datastore-id``12345678901234567890123456789012`Output: `{ "datastoreProperties": { "datastoreId": "12345678901234567890123456789012", "datastoreName": "TestDatastore123", "datastoreStatus": "ACTIVE", "losslessStorageFormat": "HTJ2K" "datastoreArn": "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012", "createdAt": "2022-11-15T23:33:09.643000+00:00", "updatedAt": "2022-11-15T23:33:09.643000+00:00" } }`**Example 2: To get data store's properties configured for JPEG2000**The following `get-datastore`code example gets a data store's properties for a data store configured for JPEG 2000 Lossless storage format.`aws medical-imaging get-datastore \ --datastore-id``12345678901234567890123456789012`Output: `{ "datastoreProperties": { "datastoreId": "12345678901234567890123456789012", "datastoreName": "TestDatastore123", "datastoreStatus": "ACTIVE", "losslessStorageFormat": "JPEG_2000_LOSSLESS", "datastoreArn": "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012", "createdAt": "2022-11-15T23:33:09.643000+00:00", "updatedAt": "2022-11-15T23:33:09.643000+00:00" } }`For more information, see [Getting data store properties](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-data-store.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [GetDatastore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-datastore.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-dicom-import-job`.

- **AWS CLI**
- 
            
                    **To get a dicom import job's properties**The following `get-dicom-import-job`code example gets a dicom import job's properties.`aws medical-imaging get-dicom-import-job \ --datastore-id``"12345678901234567890123456789012"`\ --job-id`"09876543210987654321098765432109"`Output: `{ "jobProperties": { "jobId": "09876543210987654321098765432109", "jobName": "my-job", "jobStatus": "COMPLETED", "datastoreId": "12345678901234567890123456789012", "dataAccessRoleArn": "arn:aws:iam::123456789012:role/ImportJobDataAccessRole", "endedAt": "2022-08-12T11:29:42.285000+00:00", "submittedAt": "2022-08-12T11:28:11.152000+00:00", "inputS3Uri": "s3://medical-imaging-dicom-input/dicom_input/", "outputS3Uri": "s3://medical-imaging-output/job_output/12345678901234567890123456789012-DicomImport-09876543210987654321098765432109/" } }`For more information, see [Getting import job properties](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-dicom-import-job.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [GetDICOMImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-dicom-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image-frame`.

- **AWS CLI**
- 
            
                    **To get image set pixel data**The following `get-image-frame`code example gets an image frame.`aws medical-imaging get-image-frame \ --datastore-id``"12345678901234567890123456789012"`\ --image-set-id`"98765412345612345678907890789012"`\ --image-frame-information`imageFrameId=3abf5d5d7ae72f80a0ec81b2c0de3ef4`\`imageframe.jph`Note: This code example does not include output because the GetImageFrame action returns a stream of pixel data to the imageframe.jph file. For information about decoding and viewing image frames, see HTJ2K decoding libraries. For more information, see [Getting image set pixel data](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-image-frame.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [GetImageFrame](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-frame.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image-set-metadata`.

- **AWS CLI**
- 
            
                    **Example 1: To get image set metadata without version**The following `get-image-set-metadata`code example gets metadata for an image set without specifying a version.Note: `outfile`is a required parameter`aws medical-imaging get-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\`studymetadata.json.gz`The returned metadata is compressed with gzip and stored in the studymetadata.json.gz file. To view the contents of the returned JSON object, you must first decompress it. Output: `{ "contentType": "application/json", "contentEncoding": "gzip" }`**Example 2: To get image set metadata with version**The following `get-image-set-metadata`code example gets metadata for an image set with a specified version.Note: `outfile`is a required parameter`aws medical-imaging get-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\ --version-id`1`\`studymetadata.json.gz`The returned metadata is compressed with gzip and stored in the studymetadata.json.gz file. To view the contents of the returned JSON object, you must first decompress it. Output: `{ "contentType": "application/json", "contentEncoding": "gzip" }`For more information, see [Getting image set metadata](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-image-set-metadata.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [GetImageSetMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-set-metadata.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `get-image-set`.

- **AWS CLI**
- 
            
                    **To get image set properties**The following `get-image-set`code example gets the properties for an image set.`aws medical-imaging get-image-set \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`18f88ac7870584f58d56256646b4d92b`\ --version-id`1`Output: `{ "versionId": "1", "imageSetWorkflowStatus": "COPIED", "updatedAt": 1680027253.471, "imageSetId": "18f88ac7870584f58d56256646b4d92b", "imageSetState": "ACTIVE", "createdAt": 1679592510.753, "datastoreId": "12345678901234567890123456789012" }`For more information, see [Getting image set properties](https://docs.aws.amazon.com/healthimaging/latest/devguide/get-image-set-properties.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [GetImageSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/get-image-set.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-datastores`.

- **AWS CLI**
- 
            
                    **To list data stores**The following `list-datastores`code example lists available data stores.`aws medical-imaging list-datastores`Output: `{ "datastoreSummaries": [ { "datastoreId": "12345678901234567890123456789012", "datastoreName": "TestDatastore123", "datastoreStatus": "ACTIVE", "datastoreArn": "arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012", "createdAt": "2022-11-15T23:33:09.643000+00:00", "updatedAt": "2022-11-15T23:33:09.643000+00:00" } ] }`For more information, see [Listing data stores](https://docs.aws.amazon.com/healthimaging/latest/devguide/list-data-stores.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [ListDatastores](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-datastores.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-dicom-import-jobs`.

- **AWS CLI**
- 
            
                    **To list dicom import jobs**The following `list-dicom-import-jobs`code example lists dicom import jobs.`aws medical-imaging list-dicom-import-jobs \ --datastore-id``"12345678901234567890123456789012"`Output: `{ "jobSummaries": [ { "jobId": "09876543210987654321098765432109", "jobName": "my-job", "jobStatus": "COMPLETED", "datastoreId": "12345678901234567890123456789012", "dataAccessRoleArn": "arn:aws:iam::123456789012:role/ImportJobDataAccessRole", "endedAt": "2022-08-12T11:21:56.504000+00:00", "submittedAt": "2022-08-12T11:20:21.734000+00:00" } ] }`For more information, see [Listing import jobs](https://docs.aws.amazon.com/healthimaging/latest/devguide/list-dicom-import-jobs.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [ListDICOMImportJobs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-dicom-import-jobs.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-image-set-versions`.

- **AWS CLI**
- 
            
                    **To list image set versions**The following `list-image-set-versions`code example lists the version history for an image set.`aws medical-imaging list-image-set-versions \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`ea92b0d8838c72a3f25d00d13616f87e`Output: `{ "imageSetPropertiesList": [ { "ImageSetWorkflowStatus": "UPDATED", "versionId": "4", "updatedAt": 1680029436.304, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "ACTIVE", "createdAt": 1680027126.436 }, { "ImageSetWorkflowStatus": "UPDATED", "versionId": "3", "updatedAt": 1680029163.325, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "ACTIVE", "createdAt": 1680027126.436 }, { "ImageSetWorkflowStatus": "COPY_FAILED", "versionId": "2", "updatedAt": 1680027455.944, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "ACTIVE", "message": "INVALID_REQUEST: Series of SourceImageSet and DestinationImageSet don't match.", "createdAt": 1680027126.436 }, { "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "ACTIVE", "versionId": "1", "ImageSetWorkflowStatus": "COPIED", "createdAt": 1680027126.436 } ] }`For more information, see [Listing image set versions](https://docs.aws.amazon.com/healthimaging/latest/devguide/list-image-set-versions.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [ListImageSetVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-image-set-versions.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `list-tags-for-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To list resource tags for a data store**The following `list-tags-for-resource`code example lists tags for a data store.`aws medical-imaging list-tags-for-resource \ --resource-arn``"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012"`Output: `{ "tags":{ "Deployment":"Development" } }`**Example 2: To list resource tags for an image set**The following `list-tags-for-resource`code example lists tags for an image set.`aws medical-imaging list-tags-for-resource \ --resource-arn``"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/18f88ac7870584f58d56256646b4d92b"`Output: `{ "tags":{ "Deployment":"Development" } }`For more information, see [Tagging resources with AWS HealthImaging](https://docs.aws.amazon.com/healthimaging/latest/devguide/tagging.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/list-tags-for-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `search-image-sets`.

- **AWS CLI**
- 
            
                    **Example 1: To search image sets with an EQUAL operator**The following `search-image-sets`code example uses the EQUAL operator to search image sets based on a specific value.`aws medical-imaging search-image-sets \ --datastore-id``12345678901234567890123456789012`\ --search-criteria`file://search-criteria.json`Contents of `search-criteria.json``{ "filters": [{ "values": [{"DICOMPatientId" : "SUBJECT08701"}], "operator": "EQUAL" }] }`Output: `{ "imageSetsMetadataSummaries": [{ "imageSetId": "09876543210987654321098765432109", "createdAt": "2022-12-06T21:40:59.429000+00:00", "version": 1, "DICOMTags": { "DICOMStudyId": "2011201407", "DICOMStudyDate": "19991122", "DICOMPatientSex": "F", "DICOMStudyInstanceUID": "1.2.840.99999999.84710745.943275268089", "DICOMPatientBirthDate": "19201120", "DICOMStudyDescription": "UNKNOWN", "DICOMPatientId": "SUBJECT08701", "DICOMPatientName": "Melissa844 Huel628", "DICOMNumberOfStudyRelatedInstances": 1, "DICOMStudyTime": "140728", "DICOMNumberOfStudyRelatedSeries": 1 }, "updatedAt": "2022-12-06T21:40:59.429000+00:00" }] }`**Example 2: To search image sets with a BETWEEN operator using DICOMStudyDate and DICOMStudyTime**The following `search-image-sets`code example searches for image sets with DICOM Studies generated between January 1, 1990 (12:00 AM) and January 1, 2023 (12:00 AM).Note: DICOMStudyTime is optional. If it is not present, 12:00 AM (start of the day) is the time value for the dates provided for filtering. `aws medical-imaging search-image-sets \ --datastore-id``12345678901234567890123456789012`\ --search-criteria`file://search-criteria.json`Contents of `search-criteria.json``{ "filters": [{ "values": [{ "DICOMStudyDateAndTime": { "DICOMStudyDate": "19900101", "DICOMStudyTime": "000000" } }, { "DICOMStudyDateAndTime": { "DICOMStudyDate": "20230101", "DICOMStudyTime": "000000" } }], "operator": "BETWEEN" }] }`Output: `{ "imageSetsMetadataSummaries": [{ "imageSetId": "09876543210987654321098765432109", "createdAt": "2022-12-06T21:40:59.429000+00:00", "version": 1, "DICOMTags": { "DICOMStudyId": "2011201407", "DICOMStudyDate": "19991122", "DICOMPatientSex": "F", "DICOMStudyInstanceUID": "1.2.840.99999999.84710745.943275268089", "DICOMPatientBirthDate": "19201120", "DICOMStudyDescription": "UNKNOWN", "DICOMPatientId": "SUBJECT08701", "DICOMPatientName": "Melissa844 Huel628", "DICOMNumberOfStudyRelatedInstances": 1, "DICOMStudyTime": "140728", "DICOMNumberOfStudyRelatedSeries": 1 }, "updatedAt": "2022-12-06T21:40:59.429000+00:00" }] }`**Example 3: To search image sets with a BETWEEN operator using createdAt (time studies were previously persisted)**The following `search-image-sets`code example searches for image sets with DICOM Studies persisted in HealthImaging between the time ranges in UTC time zone.Note: Provide createdAt in example format ("1985-04-12T23:20:50.52Z"). `aws medical-imaging search-image-sets \ --datastore-id``12345678901234567890123456789012`\ --search-criteria`file://search-criteria.json`Contents of `search-criteria.json``{ "filters": [{ "values": [{ "createdAt": "1985-04-12T23:20:50.52Z" }, { "createdAt": "2022-04-12T23:20:50.52Z" }], "operator": "BETWEEN" }] }`Output: `{ "imageSetsMetadataSummaries": [{ "imageSetId": "09876543210987654321098765432109", "createdAt": "2022-12-06T21:40:59.429000+00:00", "version": 1, "DICOMTags": { "DICOMStudyId": "2011201407", "DICOMStudyDate": "19991122", "DICOMPatientSex": "F", "DICOMStudyInstanceUID": "1.2.840.99999999.84710745.943275268089", "DICOMPatientBirthDate": "19201120", "DICOMStudyDescription": "UNKNOWN", "DICOMPatientId": "SUBJECT08701", "DICOMPatientName": "Melissa844 Huel628", "DICOMNumberOfStudyRelatedInstances": 1, "DICOMStudyTime": "140728", "DICOMNumberOfStudyRelatedSeries": 1 }, "lastUpdatedAt": "2022-12-06T21:40:59.429000+00:00" }] }`**Example 4: To search image sets with an EQUAL operator on DICOMSeriesInstanceUID and BETWEEN on updatedAt and sort response in ASC order on updatedAt field**The following `search-image-sets`code example searches for image sets with an EQUAL operator on DICOMSeriesInstanceUID and BETWEEN on updatedAt and sort response in ASC order on updatedAt field.Note: Provide updatedAt in example format ("1985-04-12T23:20:50.52Z"). `aws medical-imaging search-image-sets \ --datastore-id``12345678901234567890123456789012`\ --search-criteria`file://search-criteria.json`Contents of `search-criteria.json``{ "filters": [{ "values": [{ "updatedAt": "2024-03-11T15:00:05.074000-07:00" }, { "updatedAt": "2024-03-11T16:00:05.074000-07:00" }], "operator": "BETWEEN" }, { "values": [{ "DICOMSeriesInstanceUID": "1.2.840.99999999.84710745.943275268089" }], "operator": "EQUAL" }], "sort": { "sortField": "updatedAt", "sortOrder": "ASC" } }`Output: `{ "imageSetsMetadataSummaries": [{ "imageSetId": "09876543210987654321098765432109", "createdAt": "2022-12-06T21:40:59.429000+00:00", "version": 1, "DICOMTags": { "DICOMStudyId": "2011201407", "DICOMStudyDate": "19991122", "DICOMPatientSex": "F", "DICOMStudyInstanceUID": "1.2.840.99999999.84710745.943275268089", "DICOMPatientBirthDate": "19201120", "DICOMStudyDescription": "UNKNOWN", "DICOMPatientId": "SUBJECT08701", "DICOMPatientName": "Melissa844 Huel628", "DICOMNumberOfStudyRelatedInstances": 1, "DICOMStudyTime": "140728", "DICOMNumberOfStudyRelatedSeries": 1 }, "lastUpdatedAt": "2022-12-06T21:40:59.429000+00:00" }] }`For more information, see [Searching image sets](https://docs.aws.amazon.com/healthimaging/latest/devguide/search-image-sets.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [SearchImageSets](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/search-image-sets.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `start-dicom-import-job`.

- **AWS CLI**
- 
            
                    **To start a dicom import job**The following `start-dicom-import-job`code example starts a dicom import job.`aws medical-imaging start-dicom-import-job \ --job-name``"my-job"`\ --datastore-id`"12345678901234567890123456789012"`\ --input-s3-uri`"s3://medical-imaging-dicom-input/dicom_input/"`\ --output-s3-uri`"s3://medical-imaging-output/job_output/"`\ --data-access-role-arn`"arn:aws:iam::123456789012:role/ImportJobDataAccessRole"`Output: `{ "datastoreId": "12345678901234567890123456789012", "jobId": "09876543210987654321098765432109", "jobStatus": "SUBMITTED", "submittedAt": "2022-08-12T11:28:11.152000+00:00" }`For more information, see [Starting an import job](https://docs.aws.amazon.com/healthimaging/latest/devguide/start-dicom-import-job.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [StartDICOMImportJob](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/start-dicom-import-job.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `tag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To tag a data store**The following `tag-resource`code examples tags a data store.`aws medical-imaging tag-resource \ --resource-arn``"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012"`\ --tags '`{"Deployment":"Development"}`'This command produces no output. **Example 2: To tag an image set**The following `tag-resource`code examples tags an image set.`aws medical-imaging tag-resource \ --resource-arn``"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/18f88ac7870584f58d56256646b4d92b"`\ --tags '`{"Deployment":"Development"}`'This command produces no output. For more information, see [Tagging resources with AWS HealthImaging](https://docs.aws.amazon.com/healthimaging/latest/devguide/tagging.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [TagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/tag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `untag-resource`.

- **AWS CLI**
- 
            
                    **Example 1: To untag a data store**The following `untag-resource`code example untags a data store.`aws medical-imaging untag-resource \ --resource-arn``"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012"`\ --tag-keys '`["Deployment"]`'This command produces no output. **Example 2: To untag an image set**The following `untag-resource`code example untags an image set.`aws medical-imaging untag-resource \ --resource-arn``"arn:aws:medical-imaging:us-east-1:123456789012:datastore/12345678901234567890123456789012/imageset/18f88ac7870584f58d56256646b4d92b"`\ --tag-keys '`["Deployment"]`'This command produces no output. For more information, see [Tagging resources with AWS HealthImaging](https://docs.aws.amazon.com/healthimaging/latest/devguide/tagging.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [UntagResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/untag-resource.html)in*AWS CLI Command Reference*.
 
- 
                    

The following code example shows how to use `update-image-set-metadata`.

- **AWS CLI**
- 
            
                    **Example 1: To insert or update an attribute in image set metadata**The following `update-image-set-metadata`example inserts or updates an attribute in image set metadata.`aws medical-imaging update-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\ --latest-version-id`1`\ --cli-binary-format`raw-in-base64-out`\ --update-image-set-metadata-updates`file://metadata-updates.json`Contents of `metadata-updates.json``{ "DICOMUpdates": { "updatableAttributes": "{\"SchemaVersion\":1.1,\"Patient\":{\"DICOM\":{\"PatientName\":\"MX^MX\"}}}" } }`Output: `{ "latestVersionId": "2", "imageSetWorkflowStatus": "UPDATING", "updatedAt": 1680042257.908, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "LOCKED", "createdAt": 1680027126.436, "datastoreId": "12345678901234567890123456789012" }`**Example 2: To remove an attribute from image set metadata**The following `update-image-set-metadata`example removes an attribute from image set metadata.`aws medical-imaging update-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\ --latest-version-id`1`\ --cli-binary-format`raw-in-base64-out`\ --update-image-set-metadata-updates`file://metadata-updates.json`Contents of `metadata-updates.json``{ "DICOMUpdates": { "removableAttributes": "{\"SchemaVersion\":1.1,\"Study\":{\"DICOM\":{\"StudyDescription\":\"CHEST\"}}}" } }`Output: `{ "latestVersionId": "2", "imageSetWorkflowStatus": "UPDATING", "updatedAt": 1680042257.908, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "LOCKED", "createdAt": 1680027126.436, "datastoreId": "12345678901234567890123456789012" }`**Example 3: To remove an instance from image set metadata**The following `update-image-set-metadata`example removes an instance from image set metadata.`aws medical-imaging update-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`ea92b0d8838c72a3f25d00d13616f87e`\ --latest-version-id`1`\ --cli-binary-format`raw-in-base64-out`\ --update-image-set-metadata-updates`file://metadata-updates.json`\ --forceContents of `metadata-updates.json``{ "DICOMUpdates": { "removableAttributes": "{\"SchemaVersion\": 1.1,\"Study\": {\"Series\": {\"1.1.1.1.1.1.12345.123456789012.123.12345678901234.1\": {\"Instances\": {\"1.1.1.1.1.1.12345.123456789012.123.12345678901234.1\": {}}}}}}" } }`Output: `{ "latestVersionId": "2", "imageSetWorkflowStatus": "UPDATING", "updatedAt": 1680042257.908, "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e", "imageSetState": "LOCKED", "createdAt": 1680027126.436, "datastoreId": "12345678901234567890123456789012" }`**Example 4: To revert an image set to a previous version**The following `update-image-set-metadata`example shows how to revert an image set to a prior version. CopyImageSet and UpdateImageSetMetadata actions create new versions of image sets.`aws medical-imaging update-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`53d5fdb05ca4d46ac7ca64b06545c66e`\ --latest-version-id`3`\ --cli-binary-format`raw-in-base64-out`\ --update-image-set-metadata-updates '`{"revertToVersionId": "1"}`'Output: `{ "datastoreId": "12345678901234567890123456789012", "imageSetId": "53d5fdb05ca4d46ac7ca64b06545c66e", "latestVersionId": "4", "imageSetState": "LOCKED", "imageSetWorkflowStatus": "UPDATING", "createdAt": 1680027126.436, "updatedAt": 1680042257.908 }`**Example 5: To add a private DICOM data element to an instance**The following `update-image-set-metadata`example shows how to add a private element to a specified instance within an image set. The DICOM standard permits private data elements for communication of information that cannot be contained in standard data elements. You can create, update, and delete private data elements with the UpdateImageSetMetadata action.`aws medical-imaging update-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`53d5fdb05ca4d46ac7ca64b06545c66e`\ --latest-version-id`1`\ --cli-binary-format`raw-in-base64-out`\ --force \ --update-image-set-metadata-updates`file://metadata-updates.json`Contents of `metadata-updates.json``{ "DICOMUpdates": { "updatableAttributes": "{\"SchemaVersion\": 1.1,\"Study\": {\"Series\": {\"1.1.1.1.1.1.12345.123456789012.123.12345678901234.1\": {\"Instances\": {\"1.1.1.1.1.1.12345.123456789012.123.12345678901234.1\": {\"DICOM\": {\"001910F9\": \"97\"},\"DICOMVRs\": {\"001910F9\": \"DS\"}}}}}}}" } }`Output: `{ "latestVersionId": "2", "imageSetWorkflowStatus": "UPDATING", "updatedAt": 1680042257.908, "imageSetId": "53d5fdb05ca4d46ac7ca64b06545c66e", "imageSetState": "LOCKED", "createdAt": 1680027126.436, "datastoreId": "12345678901234567890123456789012" }`**Example 6: To update a private DICOM data element to an instance**The following `update-image-set-metadata`example shows how to update the value of a private data element belonging to an instance within an image set.`aws medical-imaging update-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`53d5fdb05ca4d46ac7ca64b06545c66e`\ --latest-version-id`1`\ --cli-binary-format`raw-in-base64-out`\ --force \ --update-image-set-metadata-updates`file://metadata-updates.json`Contents of `metadata-updates.json``{ "DICOMUpdates": { "updatableAttributes": "{\"SchemaVersion\": 1.1,\"Study\": {\"Series\": {\"1.1.1.1.1.1.12345.123456789012.123.12345678901234.1\": {\"Instances\": {\"1.1.1.1.1.1.12345.123456789012.123.12345678901234.1\": {\"DICOM\": {\"00091001\": \"GE_GENESIS_DD\"}}}}}}}" } }`Output: `{ "latestVersionId": "2", "imageSetWorkflowStatus": "UPDATING", "updatedAt": 1680042257.908, "imageSetId": "53d5fdb05ca4d46ac7ca64b06545c66e", "imageSetState": "LOCKED", "createdAt": 1680027126.436, "datastoreId": "12345678901234567890123456789012" }`**Example 7: To update a SOPInstanceUID with the force parameter**The following `update-image-set-metadata`example shows how to update a SOPInstanceUID, using the force parameter to override the DICOM metadata constraints.`aws medical-imaging update-image-set-metadata \ --datastore-id``12345678901234567890123456789012`\ --image-set-id`53d5fdb05ca4d46ac7ca64b06545c66e`\ --latest-version-id`1`\ --cli-binary-format`raw-in-base64-out`\ --force \ --update-image-set-metadata-updates`file://metadata-updates.json`Contents of `metadata-updates.json``{ "DICOMUpdates": { "updatableAttributes": "{\"SchemaVersion\":1.1,\"Study\":{\"Series\":{\"1.3.6.1.4.1.5962.99.1.3633258862.2104868982.1369432891697.3656.0\":{\"Instances\":{\"1.3.6.1.4.1.5962.99.1.3633258862.2104868982.1369432891697.3659.0\":{\"DICOM\":{\"SOPInstanceUID\":\"1.3.6.1.4.1.5962.99.1.3633258862.2104868982.1369432891697.3659.9\"}}}}}}}" } }`Output: `{ "latestVersionId": "2", "imageSetWorkflowStatus": "UPDATING", "updatedAt": 1680042257.908, "imageSetId": "53d5fdb05ca4d46ac7ca64b06545c66e", "imageSetState": "LOCKED", "createdAt": 1680027126.436, "datastoreId": "12345678901234567890123456789012" }`For more information, see [Updating image set metadata](https://docs.aws.amazon.com/healthimaging/latest/devguide/update-image-set-metadata.html)in the*AWS HealthImaging Developer Guide*.- 
                    For API details, see [UpdateImageSetMetadata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/update-image-set-metadata.html)in*AWS CLI Command Reference*.
 
-