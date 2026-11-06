# Creating a dataset using Amazon S3 files - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-s3.html](https://docs.aws.amazon.com/quick/latest/userguide/create-a-data-set-s3.html)

---

To create a dataset using one or more text files (.csv, .tsv, .clf, or .elf) from
            Amazon S3, create a manifest for Quick Sight. Quick Sight uses this manifest to identify
            the files that you want to use and to the upload settings needed to import them. When
            you create a dataset using Amazon S3, the file data is automatically imported into [SPICE](./spice.html).

You must grant Quick Sight access to any Amazon S3 buckets that you want to read files
            from. For information about granting Quick Sight access to AWS resources, see [Configuring Amazon Quick Sight access to AWS data sources](./access-to-aws-resources.html).