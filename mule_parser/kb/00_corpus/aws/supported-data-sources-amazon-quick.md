# Supported data sources - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/supported-data-sources.html](https://docs.aws.amazon.com/quick/latest/userguide/supported-data-sources.html)

---

Amazon Quick Sight supports a variety of data sources that you can use to provide data for analyses. The following data sources are supported.

## Connecting to relational data

			You can use any of the following relational data stores as data sources for Amazon Quick Sight:

- 
					Amazon Athena 
- 
					Amazon Aurora 
- 
					AWS Glue Data Catalog can be accessed using AWS Glue data catalog compatible services, such as Athena or Redshift Spectrum 
- 
					Amazon OpenSearch Service 
- 
					Amazon Redshift 
- 
					Amazon Redshift Spectrum 
- 
					Amazon S3 
- 
					Amazon S3 Analytics 
- 
					Amazon S3 Tables 
- 
					Apache Impala 
- 
					Apache Spark 2.0 or later 
- 
					AWS IoT Analytics 
- 
					Databricks (E2 Platform only) on Spark 1.6 or later, up to version 3.0 
- 
					Exasol 7.1.2 or later 
- 
					Google BigQuery 
- 
					MariaDB 10.0 or later 
- 
					Microsoft SQL Server 2012 or later 
- 
					MySQL 5.7 or later ###### NoteEffective October 2023, the MySQL community has deprecated support for MySQL version 5.7. This means that Amazon Quick Sight will no longer support new features, enhancements, bug fixes, or security patches for MySQL 5.7. Support for existing query workload will take place at a best effort basis. Quick Sight customers can still use MySQL 5.7 datasets with Quick Sight, but we encourage customers to upgrade their MySQL databases (DB) to major version 8.0 or higher. To see the statement provided by Amazon RDS, see [Amazon RDS Extended Support opt-in behavior is changing. Upgrade your Amazon RDS for MySQL 5.7 database instances before February 29, 2024 to avoid potential increase in charges](https://repost.aws/articles/ARHdQg4IelQS2uyXkNrINw-A/announcement-amazon-rds-extended-support-opt-in-behavior-is-changing-upgrade-your-amazon-rds-for-mysql-5-7-database-instances-before-february-29-2024-to-avoid-potential-increase-in-charges).Amazon RDS has updated their security settings for Amazon RDS MySQL 8.3. Any connections from Quick Sight to Amazon RDS MySQL 8.3 are SSL-enabled by default. This is the only option available for MySQL 8.3. connections. TLS 1.2 for MySQL connections requires MySQL version 5.7.28 or higher. For MySQL versions below 5.7.28, Quick Sight falls back to TLS 1.1. If your security requirements mandate TLS 1.2, ensure your MySQL or Aurora MySQL database is running version 5.7.28 or higher. 
- 
					Oracle 12c or later 
- 
					PostgreSQL 9.3.1 or later ###### NoteSCRAM based authentication to PostgreSQL from Amazon Quick Sight is supported for the following connectors: RDS hosted PostgreSQL, Aurora PostgreSQL, and Vanilla PostgreSQL. If the appropriate PostgreSQL engine version is used, and the correct configurations in PostgreSQL for SCRAM are set up, no additional configurations are needed in Quick Sight. If you are still experiencing issues establishing a SCRAM authentication to PostgreSQL from Quick Sight, please create a support ticket. 
- 
					Presto 0.167 or later 
- 
					Snowflake 
- 
					Starburst 
- 
					Trino 
- 
					Teradata 14.0 or later 
- 
					Timestream 

###### Note

You can access additional data sources not listed here by linking or importing them through supported data sources.

Amazon Redshift clusters, Amazon Athena databases, and Amazon RDS instances must be in AWS. Other database instances must be in one of the following environments to be accessible from Amazon Quick Sight:

- 
					Amazon EC2 
- 
					Local (on-premises) databases 
- 
					Data in a data center or some other internet-accessible environment 

For more information, see [Infrastructure security in Amazon Quick](./infrastructure-and-network-access.html).

## Importing file data

			You can use files in Amazon S3 or on your local (on-premises) network as data sources. Quick Sight supports files in the following formats:

- 
					CSV and TSV – Comma-delimited and tab-delimited text files 
- 
					ELF and CLF – Extended and common log format files 
- 
					JSON – Flat or semistructured data files 
- 
					XLSX – Microsoft Excel files 

Quick Sight supports UTF-8 file encoding, but not UTF-8 (with BOM).

Files in Amazon S3 that have been compressed with zip, or gzip ([www.gzip.org](http://www.gzip.org)), can be imported as-is. If you
				used another compression program for files in Amazon S3, or if the files are on your
				local network, remove compression before importing them.

### JSON data

Amazon Quick Sight natively supports JSON flat files and JSON semistructured data files.

You can either upload a JSON file or connect to your Amazon S3 bucket that contains JSON data. Amazon Quick Sight automatically performs schema and type inference on JSON files and embedded JSON objects. Then it flattens the JSON, so you can analyze and visualize application-generated data.

Basic support for JSON flat-file data includes the following:

- 
						Inferring the schema 
- 
						Determining data types 
- 
						Flattening the data 
- 
						Parsing JSON (JSON embedded objects) from flat files 

Support for JSON file structures (.json) includes the following:

- 
						JSON records with structures 
- 
						JSON records with root elements as arrays 

You can also use the `parseJson` function to extract values from
					JSON objects in a text file. For example, if your CSV
					file has a JSON object embedded in one of the fields, you can extract a value
					from a specified key-value pair (KVP). For more information on how to do this,
					see [parseJson](./parseJson-function.html).

The following JSON features aren't supported:

- 
						Reading JSON with a structure containing a list of records 
- 
						List attributes and list objects within a JSON record; these are skipped during import 
- 
						Customizing upload or configuration settings 
- 
						parseJSON functions for SQL and analyses 
- 
						Error messaging for invalid JSON 
- 
						Extracting a JSON object from a JSON structure 
- 
						Reading delimited JSON records 

You can use the `parseJson` function to parse flat files during
					data preparation. This function extracts elements from valid JSON structures and
					lists.

The following JSON values are supported:

- 
						JSON object 
- 
						String (double quoted) 
- 
						Number (integer and float) 
- 
						Boolean 
- 
						NULL 

## Software as a service (SaaS) data

			Quick Sight can connect to a variety of Software as a Service (SaaS) data sources either by connecting directly or by using Open Authorization (OAuth).

SaaS sources that support direct connection include the following:

- 
					Jira 
- 
					ServiceNow 

SaaS sources that use OAuth require that you authorize the connection on the SaaS website. For this to work, Quick Sight must be able to access the SaaS data source over the network. These sources include the following:

- 
					Adobe Analytics 
- 
					GitHub 
- 
					Salesforce You can use reports or objects in the following editions of Salesforce as data sources for Amazon Quick Sight: - 
							Enterprise Edition 
- 
							Unlimited Edition 
- 
							Developer Edition 
 
- 
							

## Local data sources

			To connect to on premises data sources, you need to add your data sources and a Quick-specific network interface to Amazon Virtual Private Cloud (Amazon VPC). When configured properly, a VPC based on Amazon VPC resembles a traditional network that you operate in your own data center. It enables you to secure and isolate traffic between resources. You define and control the network elements to suit your requirements, while still getting the benefit of cloud networking and the scalable infrastructure of AWS.

For detailed information, see [Infrastructure security in Amazon Quick](./infrastructure-and-network-access.html).