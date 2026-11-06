# Welcome - Amazon S3

**Source:** [https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

---

## Amazon S3

   Welcome to the *Amazon S3 API Reference*. This guide explains the Amazon Simple Storage Service (Amazon S3)
      application programming interface (API).

You can use any toolkit that supports HTTP to use the REST API. You can even use a browser to fetch objects, as long as they are anonymously readable.

The REST API uses the standard HTTP headers and status codes, so that standard browsers and toolkits work as expected. In some areas, we have added functionality to HTTP (for example, we added headers to support access control). In these cases, we have done our best to add the new functionality in a way that matched the style of standard HTTP usage.

The current version of the Amazon S3 API is `2006-03-01`.

Amazon S3 supports the REST API.

###### Note

Support for SOAP over HTTP is deprecated, but it is still available over HTTPS. However, new Amazon S3 features will not be supported for SOAP. We recommend that you use either this REST API or the AWS SDKs.

## Amazon S3 Control

   AWS S3 Control provides access to Amazon S3 control plane actions.

## Amazon S3 Files

   S3 Files makes S3 buckets accessible as high-performance file systems powered by EFS. This service enables file system interface access to S3 data with sub-millisecond latencies through mount targets, supporting AI/ML workloads, media processing, and hybrid storage workflows that require both file system and object storage access to the same data.

## Amazon S3 on Outposts

   Amazon S3 on Outposts provides access to S3 on Outposts operations.

## Amazon S3 Tables

   An Amazon S3 table represents a structured dataset consisting of tabular data in [Apache Parquet](https://parquet.apache.org/docs/) format and related metadata. This data is stored inside an S3 table as a subresource. All tables in a table bucket are stored in the 

[Apache Iceberg](https://iceberg.apache.org/docs/latest/)table format. Through integration with the

[AWS Glue Data Catalog](https://docs.aws.amazon.com/https:/docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)you can interact with your tables using AWS analytics services, such as

[Amazon Athena](https://docs.aws.amazon.com/https:/docs.aws.amazon.com/athena/)and

[Amazon Redshift](https://docs.aws.amazon.com/https:/docs.aws.amazon.com/redshift/). Amazon S3 manages maintenance of your tables through automatic file compaction and snapshot management. For more information, see

[Amazon S3 table buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-tables-buckets.html).

## Amazon S3 Vectors

   Amazon S3 vector buckets are a bucket type to store and search vectors with sub-second search times. They are designed to provide dedicated API operations for you to interact with vectors to do similarity search. Within a vector bucket, you use a vector index to organize and logically group your vector data. When you make a write or read request, you direct it to a single vector index. You store your vector data as vectors. A vector contains a key (a name that you assign), a multi-dimensional vector, and, optionally, metadata that describes a vector. The key uniquely identifies the vector in a vector index.