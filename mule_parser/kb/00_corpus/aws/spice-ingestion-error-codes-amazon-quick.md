# SPICE ingestion error codes - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/errors-spice-ingestion.html](https://docs.aws.amazon.com/quick/latest/userguide/errors-spice-ingestion.html)

---

The following list of errors codes and descriptions can help you understand and troubleshoot issues with data ingestion into SPICE.

## Error codes for skipped rows

			The following list of errors codes and descriptions can help you understand and troubleshoot issues with skipped rows.

**ARITHMETIC_EXCEPTION** – An arithmetic exception
				occurred while processing a value.

**ENCODING_EXCEPTION**
				– An unknown exception occurred while converting and encoding data to
					SPICE.

**OPENSEARCH_CURSOR_NOT_ENABLED** – The OpenSearch
				domain doesn't have SQL cursors enabled (```
"opendistro.sql.cursor.enabled" :
					"true"
```
). For more information, see [Authorizing connections to Amazon OpenSearch Service](./opensearch.html).

**INCORRECT_FIELD_COUNT** – One or more rows have too
				many fields. Make sure that the number of fields in each row matches the number of
				fields defined in the schema.

**INCORRECT_SAGEMAKER_OUTPUT_FIELD_COUNT** – The
				SageMaker AI output has an unexpected number of fields.

**INDEX_OUT_OF_BOUNDS** – The system requested an index
				that isn't valid for the array or list being processed.

**MALFORMED_DATE**
				– A value in a field can't be transformed to a valid date. For example, if
				you try to convert a field that contains a value like `"sale date"` or
					`"month-1"`, the action generates a malformed date error. To fix this
				error, remove nondate values from your data source. Check that you aren't importing
				a file with a column header mixed into the data. If your string contains a date or
				time that doesn't convert, see [Using unsupported or custom dates](./using-unsupported-dates.html).

**MISSING_SAGEMAKER_OUTPUT_FIELD** – A field in the
				SageMaker AI output is unexpectedly empty.

**NUMBER_BITWIDTH_TOO_LARGE** – A numeric value exceeds
				the length supported in SPICE. For example, your numeric value has
				more than 19 digits, which is the length of a `bigint` data type. For a
				long numeric sequence that isn't a mathematical value, use a `string`
				data type.

**NUMBER_PARSE_FAILURE** – A value in a numeric field is
				not a number. For example, a field with a data type of `int` contains a
				string or a float.

**SAGEMAKER_OUTPUT_COLUMN_TYPE_MISMATCH** – The data
				type defined in the SageMaker AI schema doesn't match the data type received from SageMaker AI. 

**STRING_TRUNCATION**
				– A string is being truncated by SPICE. Strings are truncated
				where the length of the string exceeds the SPICE quota. For more
				information about SPICE, see [Importing data into SPICE](./spice.html). For more information about quotas, see [Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html). 

**UNDEFINED** –
				An unknown error occurred while ingesting data.

**UNSUPPORTED_DATE_VALUE** – A date field contains a
				date that is in a supported format but is not in the supported range of dates, for
				example "12/31/1399" or "01/01/10000". For more information, see
					[Using unsupported or custom dates](./using-unsupported-dates.html). 

## Error codes during data import

			For imports and data refresh jobs that fail, Quick Sight provides an error code indicating what caused the failure. The following list of errors codes and descriptions can help you understand and troubleshoot issues with data ingestion into SPICE.

**ACCOUNT_CAPACITY_LIMIT_EXCEEDED** – This data
				exceeds your current SPICE capacity. Purchase more
					SPICE capacity or clean up existing SPICE data and
				then retry this ingestion.

**CONNECTION_FAILURE**
				– Amazon Quick Sight can't connect to your data source. Check the data source
				connection settings and try again.

**CUSTOMER_ERROR**
				– There was a problem parsing the data. If this persists, contact Amazon Quick Sight
				technical support.

**DATA_SET_DELETED**
				– The data source or dataset was deleted or became unavailable during
				ingestion.

**DATA_SET_SIZE_LIMIT_EXCEEDED** – This dataset
				exceeds the maximum allowable SPICE dataset size. Use filters to
				reduce the dataset size and try again. For information on SPICE
				quotas, see [Data source quotas](./data-source-limits.html).

**DATA_SOURCE_AUTH_FAILED** – Data source authentication
				failed. Check your credentials and use the **Edit data source**
				option to replace expired credentials.

**DATA_SOURCE_CONNECTION_FAILED** – Data source
				connection failed. Check the URL and try again. If this error persists, contact your
				data source administrator for assistance.

**DATA_SOURCE_NOT_FOUND** – No data source found. Check
				your Amazon Quick Sight data sources.

**DATA_TOLERANCE_EXCEPTION** – There are too many
				invalid rows. Amazon Quick Sight has reached the quota of rows that it can skip and still
				continue ingesting. Check your data and try again.

**FAILURE_TO_ASSUME_ROLE** – Amazon Quick Sight couldn't assume the
				correct AWS Identity and Access Management (IAM) role. Verify the policies for
					`Amazon Quick Sight-service-role` in the IAM console.

**FAILURE_TO_PROCESS_JSON_FILE** – Amazon Quick Sight
				couldn't parse a manifest file as valid JSON.

**IAM_ROLE_NOT_AVAILABLE** – Amazon Quick Sight doesn't have
				permission to access the data source. To manage Amazon Quick Sight permissions on AWS
				resources, go to the **Security and Permissions** page under the
					**Manage Amazon Quick Sight** option as an administrator.

**INGESTION_CANCELED**
				– The ingestion was canceled by the user.

**INGESTION_SUPERSEDED** – This ingestion has been
				superseded by another workflow. This happens when a new ingestion is created while
				another one is still in progress. Avoid manually editing the dataset multiple times
				in a short period, because each manual edit creates a new ingestion which will
				supersede and end the previous ingestion.

**INTERNAL_SERVICE_ERROR** – An internal service error
				occurred.

**INVALID_DATA_SOURCE_CONFIG** – Invalid values appeared
				in connection settings. Check your connection details and try again.

**INVALID_DATAPREP_SYNTAX** – Your calculated field
				expression contains invalid syntax. Correct the syntax and try again.

**INVALID_DATE_FORMAT** – An invalid date format
				appeared.

**IOT_DATA_SET_FILE_EMPTY** – No AWS IoT Analytics data
				was found. Check your account and try again.

**IOT_FILE_NOT_FOUND**
				– An indicated AWS IoT Analytics file wasn't found. Check your account and
				try again.

**OAUTH_TOKEN_FAILURE** – Credentials to the data source
				have expired. Renew your credentials and retry this ingestion.

**PASSWORD_AUTHENTICATION_FAILURE** – Incorrect
				credentials appeared for a data source. Update your data source credentials and
				retry this ingestion.

**PERMISSION_DENIED**
				– Access to the requested resources was denied by the data source. Request
				permissions from your database administrator or ensure proper permission has been
				granted to Amazon Quick Sight before retrying.

**QUERY_TIMEOUT**
				– A query to the data source timed out waiting for a response. Check your
				data source logs and try again.

**ROW_SIZE_LIMIT_EXCEEDED** – The row size quota
				exceeded the maximum.

**S3_FILE_INACCESSIBLE** – Couldn't connect to an S3
				bucket. Make sure that you grant Amazon Quick Sight and users necessary permissions before you
				connect to the S3 bucket.

**S3_MANIFEST_ERROR**
				– Couldn't connect to S3 data. Make sure that your S3 manifest file is valid.
				Also verify access to the S3 data. Both Amazon Quick Sight and the Amazon Quick Sight user need
				permissions to connect to the S3 data.

**S3_UPLOADED_FILE_DELETED** – The file or files for the
				ingestion were deleted (between ingestions). Check your S3 bucket and try
				again.

**SOURCE_API_LIMIT_EXCEEDED_FAILURE** – This
				ingestion exceeds the API quota for this data source. Contact your data source
				administrator for assistance.

**SOURCE_RESOURCE_LIMIT_EXCEEDED** – A SQL query
				exceeds the resource quota of the data source. Examples of resources involved can
				include the concurrent query quota, the connection quota, and physical server
				resources. Contact your data source administrator for assistance.

**SPICE_TABLE_NOT_FOUND** – An Amazon Quick Sight data source or
				dataset was deleted or became unavailable during ingestion. Check your dataset in
				Amazon Quick Sight and try again. For more information, see [Troubleshooting skipped row errors](./troubleshooting-skipped-rows.html).

**SQL_EXCEPTION**
				– A general SQL error occurred. This error can be caused by query timeouts,
				resource constraints, unexpected data definition language (DDL) changes before or
				during a query, and other database errors. Check your database settings and your
				query, and try again.

**SQL_INVALID_PARAMETER_VALUE** – An invalid SQL
				parameter appeared. Check your SQL and try again.

**SQL_NUMERIC_OVERFLOW** – Amazon Quick Sight encountered an
				out-of-range numeric exception. Check related values and calculated columns for
				overflows, and try again.

**SQL_SCHEMA_MISMATCH_ERROR** – The data source schema
				doesn't match the Amazon Quick Sight dataset. Update your Amazon Quick Sight dataset definition.

**SQL_TABLE_NOT_FOUND** – Amazon Quick Sight can't find the
				table in the data source. Verify the table specified in the dataset or custom SQL
				and try again.

**SSL_CERTIFICATE_VALIDATION_FAILURE** – Amazon Quick Sight
				can't validate the Secure Sockets Layer (SSL) certificate on your database
				server. Check the SSL status on that server with your database administrator and try
				again.

**UNRESOLVABLE_HOST**
				– Amazon Quick Sight can't resolve the host name of the data source. Verify the
				host name of the data source and try again.

**UNROUTABLE_HOST**
				– Amazon Quick Sight can't reach your data source because it's inside a
				private network. Ensure that your private VPC connection is configured correctly in
				Enterprise Edition, or allow Amazon Quick Sight IP address ranges to allow connectivity for
				Standard Edition.