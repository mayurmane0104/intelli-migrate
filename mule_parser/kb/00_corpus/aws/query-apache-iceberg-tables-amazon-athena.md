# Query Apache Iceberg tables - Amazon Athena

**Source:** [https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)

---

[Browser SSO OIDC credentials](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-browser-sso-oidc.html)

*5 June 2026*

We use essential cookies and similar tools that are necessary to provide our site and services. We use performance cookies to collect anonymous statistics, so we can understand how customers use our site and make improvements. Essential cookies cannot be deactivated, but you can choose “Customize” or “Decline” to decline performance cookies. 

 If you agree, AWS and approved third parties will also use cookies to provide useful site features, remember your preferences, and display relevant content, including relevant advertising. To accept or decline all non-essential cookies, choose “Accept” or “Decline.” To make more detailed choices, choose “Customize.”

Essential cookies are necessary to provide our site and services and cannot be deactivated. They are usually set in response to your actions on the site, such as setting your privacy preferences, signing in, or filling in forms.

Performance cookies provide anonymous statistics about how customers navigate our site so we can improve site experience and performance. Approved third parties may perform analytics on our behalf, but they cannot use the data for their own purposes.

Functional cookies help us provide useful site features, remember your preferences, and display relevant content. Approved third parties may set these cookies to provide certain site features. If you do not allow these cookies, then some or all of these services may not function properly.

Advertising cookies may be set through our site by us or our advertising partners and help us deliver relevant marketing content. If you do not allow these cookies, you will experience less relevant advertising.

Blocking some types of cookies may impact your experience of our sites. You may review and change your choices at any time by selecting Cookie preferences in the footer of this site. We and selected third-parties use cookies or similar technologies as specified in the [AWS Cookie Notice](https://aws.amazon.com/legal/cookies/).

We will only store essential cookies at this time, because we were unable to save your cookie preferences.

If you want to change your cookie preferences, try again later using the link in the AWS console footer, or contact support if the problem persists.

You can use Athena to perform read, time travel, write, and DDL queries on Apache Iceberg tables.

[Apache Iceberg](https://iceberg.apache.org/) is an open table format
        for very large analytic datasets. Iceberg manages large collections of files as tables, and
        it supports modern analytical data lake operations such as record-level insert, update,
        delete, and time travel queries. The Iceberg specification allows seamless table evolution
        such as schema and partition evolution and is designed for optimized usage on Amazon S3. Iceberg
        also helps guarantee data correctness under concurrent write scenarios.

For more information about Apache Iceberg, see [https://iceberg.apache.org/](https://iceberg.apache.org/).

Athena support for Iceberg tables has the following considerations and limitations:

Iceberg version support – Athena supports Apache Iceberg version 1.4.2.

Tables registered with Lake Formation – Athena does not currently support DDL operations on Iceberg tables that are registered with Lake Formation.

Queries against information schema – When querying the information schema of Iceberg tables, Athena uses S3 metadata as the source of truth for column metadata. This means that column information is derived from the underlying S3 files rather than from the catalog metadata. This behavior differs from other table formats where catalog metadata might be the primary source for column information.

Tables with AWS Glue catalog only – Only
                    Iceberg tables created against the AWS Glue catalog based on specifications defined
                    by the [open source glue catalog implementation](https://iceberg.apache.org/docs/latest/aws/#glue-catalog) are supported from
                    Athena.

Table locking support by AWS Glue only – Unlike the open source Glue catalog implementation, which supports plug-in custom locking, Athena supports AWS Glue optimistic locking only. Using Athena to modify an Iceberg table with any other lock implementation will cause potential data loss and break transactions.

Supported file formats – Athena engine version 3 supports the following Iceberg file formats.

Parquet

ORC

Avro

Iceberg restricted metadata – Lake Formation does
                    not evaluate the Iceberg metadata tables. Hence, the Iceberg metadata tables are
                    restricted if there are any Lake Formation row or cell filters present on the base table
                    or if you do not have permissions to view all columns in the base table. For
                    such cases, when you query the `$partitions`, `$files`,
                        `$manifests`, and `$snapshots` Iceberg metadata
                    tables, it fails and you get an `AccessDeniedException` error.
                    Additionally, the metadata column `$path` has the same Lake Formation
                    restrictions and fails when selected by the query. All other metadata tables can
                    be queried regardless of the Lake Formation filters. For more information, see [Metadata tables](https://trino.io/docs/current/connector/iceberg.html#metadata-tables).

Iceberg v2 tables – Athena only creates
                    and operates on Iceberg v2 tables. For the difference between v1 and v2 tables,
                    see [Format version changes](https://iceberg.apache.org/spec/#appendix-e-format-version-changes) in the Apache Iceberg documentation.

Display of time types without time zone – The time and timestamp without time zone types are displayed in UTC. If the time zone is unspecified in a filter expression on a time column, UTC is used.

Timestamp related data precision – Although Iceberg supports microsecond precision for the timestamp data type, Athena supports only millisecond precision for timestamps in both reads and writes. For data in time related columns that is rewritten during manual compaction operations, Athena retains only millisecond precision.

Unsupported operations – The following Athena operations are not supported for Iceberg tables.

Views – Use `CREATE VIEW` to
                    create Athena views as described in [Work with views](./views.html). If you are interested in using the [Iceberg view specification](https://github.com/apache/iceberg/blob/master/format/view-spec.md) to create views, contact 

TTF management commands not supported in
                        AWS Lake Formation – Although you can use Lake Formation to manage read access
                    permissions for TransactionTable Formats (TTFs) like Apache Iceberg, Apache
                    Hudi, and Linux Foundation Delta Lake, you cannot use Lake Formation to manage permissions
                    for operations like `VACUUM`, `MERGE`, `UPDATE`
                    or `OPTIMIZE` with these table formats. For more information about
                    Lake Formation integration with Athena, see [Using AWS Lake Formation with
                        Amazon Athena](https://docs.aws.amazon.com/lake-formation/latest/dg/athena-lf.html) in the *AWS Lake Formation Developer Guide*.

Partitioning by nested fields –
                    Partitioning by nested fields is not supported. Attempting to do so produces the
                    message ```
NOT_SUPPORTED: Partitioning by nested field is
                        unsupported:
```
`column_name`.`nested_field_name`.

Skipping Amazon Glacier objects not supported  –
                    If objects in the Apache Iceberg table are in an Amazon Glacier storage class, setting the
                        `read_restored_glacier_objects` table property to
                        `false` has no effect.

For example, suppose you issue the following command:

`ALTER TABLE ``table_name` SET TBLPROPERTIES ('read_restored_glacier_objects' = 'false')For Iceberg and Delta Lake tables, the command produces the error
                        ** Unsupported table property key:
                        read_restored_glacier_objects**. For Hudi tables, the 

```
ALTER
                        TABLE
```
 command does not produce an error, but Amazon Glacier objects are still
                    not skipped. Running `SELECT` queries after the ```
ALTER
                        TABLE
```
 command continues to return all objects.If you would like Athena to support a particular feature, send feedback to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

Athena engine version 3 queries Delta Lake tables via AWS Glue, supporting file-skipping predicates and Lake Formation permissions.

EMR fine-grained access control supports Iceberg, Hudi, Delta Lake row, column, cell-level permissions via Lake Formation.

Athena queries S3 data via SQL, runs Apache Spark analytics serverless, scales parallel for fast results.

Athena engine version 3 upgrade introduces breaking changes: timestamp precision serialization errors, deprecated Iceberg time travel clauses, CHAR VARCHAR coercion workarounds.

Tutorial covers querying data, creating tables, S3 bucket setup, named queries, keyboard shortcuts, typeahead, data sources.