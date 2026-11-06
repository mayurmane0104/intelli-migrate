# Supported formats for Amazon S3 manifest files - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/supported-manifest-file-format.html](https://docs.aws.amazon.com/quick/latest/userguide/supported-manifest-file-format.html)

---

You use JSON manifest files to specify files in Amazon S3 to import into Quick Sight.
                These JSON manifest files can use either the Quick Sight format described following
                or the Amazon Redshift format described in [Using a manifest to
                    specify data files](https://docs.aws.amazon.com/redshift/latest/dg/loading-data-files-using-manifest.html) in the *Amazon Redshift Database Developer Guide*. You don't
                have to use Amazon Redshift to use the Amazon Redshift manifest file format. 

If you use an Quick Sight manifest file, it must have a .json extension, for
                example `my_manifest.json`. If you use an Amazon Redshift manifest file, it
                can have any extension. 

If you use an Amazon Redshift manifest file, Quick Sight processes the optional
                    `mandatory` option as Amazon Redshift does. If the associated file isn't
                found, Quick Sight ends the import process and returns an error. 

Files that you select for import must be delimited text (for example, .csv or
                .tsv), log (.clf), or extended log (.elf) format, or JSON (.json). All files
                identified in one manifest file must use the same file format. Plus, they must have
                the same number and type of columns. Quick Sight supports UTF-8 file encoding, but
                not UTF-8 with byte-order mark (BOM). If you are importing JSON files, then for
                    `globalUploadSettings` specify `format`, but not
                    `delimiter`, `textqualifier`, or
                    `containsHeader`.

Make sure that any files that you specify are in Amazon S3 buckets that you have
                granted Quick Sight access to. For information about granting Quick Sight access
                to AWS resources, see [Configuring Amazon Quick Sight access to AWS data sources](./access-to-aws-resources.html).

## Manifest file format for Quick Sight

                Quick Sight manifest files use the following JSON format.

`{ "fileLocations": [ { "URIs": [ "uri1", "uri2", "uri3" ] }, { "URIPrefixes": [ "prefix1", "prefix2", "prefix3" ] } ], "globalUploadSettings": { "format": "JSON", "delimiter": ",", "textqualifier": "'", "containsHeader": "true" } }`

Use the fields in the `fileLocations` element to specify the files
                    to import, and the fields in the `globalUploadSettings` element to
                    specify import settings for those files, such as field delimiters. 

The manifest file elements are described following:

- 
                        **fileLocations**– Use this element to specify the files to import. You can use either or both of the`URIs`and`URIPrefixes`arrays to do this. You must specify at least one value in one or the other of them.- 
                                **URIs**– Use this array to list URIs for specific files to import.Quick Sight can access Amazon S3 files that are in any AWS Region. However, you must use a URI format that identifies the AWS Region of the Amazon S3 bucket if it's different from that used by your Quick account. URIs in the following formats are supported. URI format Example Comments https://s3.amazonaws.com/< *bucket name*>/<*file name*>https://s3.amazonaws.com/amzn-s3-demo-bucket/data.csv s3://< *bucket name*>/<*file name*>s3://amzn-s3-demo-bucket/data.csv https://< *bucket name*>.s3.amazonaws.com/<*file name*>https:// `amzn-s3-demo-bucket`.s3.amazonaws.com/`data.csv`https://s3-< *region name*>.amazonaws.com/<*bucket name*>/<*file name*>https:// `s3-us-east-1.amazonaws.com`/`amzn-s3-demo-bucket`/`data.csv`This URI type identifies the AWS Region for the Amazon S3 bucket. https://< *bucket name*>.s3-<*region name*>.amazonaws.com/<*file name*>https:// `amzn-s3-demo-bucket`.`s3-us-east-1`.`amazonaws`.`com`/`data.csv`This URI type identifies the AWS Region for the Amazon S3 bucket. 
- 
                                **URIPrefixes**– Use this array to list URI prefixes for S3 buckets and folders. All files in a specified bucket or folder are imported. Quick Sight recursively retrieves files from child folders.Quick Sight can access Amazon S3 buckets or folders that are in any AWS Region. Make sure to use a URI prefix format that identifies the S3 bucket's AWS Region if it's different from that used by your Quick account. URI prefixes in the following formats are supported. URI prefix format Example Comments https://s3.amazonaws.com/< *bucket name*>/https://s3.amazonaws.com/amzn-s3-demo-bucket/ https://s3.amazonaws.com/< *bucket name*>/<*folder name1*>/(<*folder name2>/etc.)*https://s3.amazonaws.com/amzn-s3-demo-bucket/folder1/ s3://< *bucket name*>s3://amzn-s3-demo-bucket/ s3://< *bucket name*>/<*folder name1*>/(<*folder name2>/etc.)*s3://amzn-s3-demo-bucket/folder1/ https://< `bucket name``s3`.`amazonaws.com`https:// `amzn-s3-demo-bucket`.`s3`.`amazonaws.com`https://s3-< *region name*>.amazonaws.com/<*bucket name*>/https://s3- `your-region-for-example-us-east-2`.`amazonaws.com`/`amzn-s3-demo-bucket`/This `URIPrefix`type identifies the AWS Region for the Amazon S3 bucket.https://s3-< *region name*>.amazonaws.com/<*bucket name*>/<*folder name1*>/(<*folder name2>/etc.)*https:// `s3-us-east-1.amazonaws.com`/`amzn-s3-demo-bucket`/`folder1`/This `URIPrefix`type identifies the AWS Region for the Amazon S3 bucket.https://< *bucket name*>.s3-<*region name*>.amazonaws.comhttps:// `amzn-s3-demo-bucket`.`s3-us-east-1.amazonaws`.`com`This `URIPrefix`type identifies the AWS Region for the Amazon S3 bucket.
 
- 
                                
- 
                        **globalUploadSettings**– (Optional) Use this element to specify import settings for the Amazon S3 files, such as field delimiters. If this element is not specified, Quick Sight uses the default values for the fields in this section.###### ImportantFor log (.clf) and extended log (.elf) files, only the **format**field in this section is applicable, so you can skip the other fields. If you choose to include them, their values are ignored.- 
                                **format**– (Optional) Specify the format of the files to be imported. Valid formats are`CSV`,`TSV`,`CLF`,`ELF`, and`JSON`. The default value is`CSV`.
- 
                                **delimiter**– (Optional) Specify the file field delimiter. This must map to the file type specified in the`format`field. Valid formats are commas (`,`) for .csv files and tabs (`\t`) for .tsv files. The default value is comma (`,`).
- 
                                **textqualifier**– (Optional) Specify the file text qualifier. Valid formats are single quote (`'`), double quotes (`\"`). The leading backslash is a required escape character for a double quote in JSON. The default value is double quotes (`\"`). If your text doesn't need a text qualifier, don't include this property.
- 
                                **containsHeader**– (Optional) Specify whether the file has a header row. Valid formats are`true`or`false`. The default value is`true`.
 
- 
                                

### Manifest file examples for Quick Sight

The following are some examples of completed Quick Sight manifest files.

The following example shows a manifest file that identifies two specific
                        .csv files for import. These files use double quotes for text qualifiers.
                        The `format`, `delimiter`, and
                            `containsHeader` fields are skipped because the default
                        values are acceptable.

`{ "fileLocations": [ { "URIs": [ "https://``yourBucket`.`s3`.`amazonaws.com`/`data-file.csv`", "https://`yourBucket`.`s3`.`amazonaws.com`/`data-file-2.csv`" ] } ], "globalUploadSettings": { "textqualifier": "\"" } }

The following example shows a manifest file that identifies one specific
                        .tsv file for import. This file also includes a bucket in another AWS
                        Region that contains additional .tsv files for import. The
                            `textqualifier` and `containsHeader` fields are
                        skipped because the default values are acceptable.

`{ "fileLocations": [ { "URIs": [ "https://``s3`.`amazonaws.com/``amzn-s3-demo-bucket`/`data.tsv`" ] }, { "URIPrefixes": [ "https://`s3-us-east-1.amazonaws.com`/`amzn-s3-demo-bucket`/" ] } ], "globalUploadSettings": { "format": "TSV", "delimiter": "\t" } }

The following example identifies two buckets that contain .clf files for
                        import. One is in the same AWS Region as the Quick account,
                        and one in a different AWS Region. The `delimiter`,
                            `textqualifier`, and `containsHeader` fields are
                        skipped because they are not applicable to log files.

`{ "fileLocations": [ { "URIPrefixes": [ "https://``amzn-s3-demo-bucket1`.`your-s3-url`.com", "s3://amzn-s3-demo-bucket2/" ] } ], "globalUploadSettings": { "format": "CLF" } }

The following example uses the Amazon Redshift format to identify a .csv file for import.

`{ "entries": [ { "url": "https://``amzn-s3-demo-bucket`.`your-s3-url`.com/myalias-test/file-to-import.csv", "mandatory": true } ] }

The following example uses the Amazon Redshift format to identify two JSON files for import.

`{ "fileLocations": [ { "URIs": [ "https://``yourBucket`.`s3`.`amazonaws.com`/`data-file.json`", "https://`yourBucket`.`s3`.`amazonaws.com`/`data-file-2.json`" ] } ], "globalUploadSettings": { "format": "JSON" } }