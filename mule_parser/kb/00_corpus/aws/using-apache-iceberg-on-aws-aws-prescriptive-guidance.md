# Using Apache Iceberg on AWS - AWS Prescriptive Guidance

**Source:** [https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/apache-iceberg-on-aws/introduction.html)

---

*Amazon Web Services* ([contributors](./contributors.html))

*November 2025* ([document
        history](./doc-history.html))

Apache Iceberg is an open-source table format that simplifies table management while improving performance. AWS analytics services such as Amazon EMR, AWS Glue, Amazon Athena, and Amazon Redshift include native support for Iceberg, so you can easily build transactional data lakes on top of Amazon Simple Storage Service (Amazon S3) on AWS.

In addition, the next generation of Amazon SageMaker is built on an [open lakehouse architecture](https://aws.amazon.com/sagemaker/lakehouse/) that unifies data access
        across AWS data lakes, data warehouses, and third-party and federated sources. The
        lakehouse is fully compatible with Iceberg and gives you the flexibility to access
        and query data in place by using the Iceberg REST API.

This technical guide provides guidance on getting started with Iceberg on different AWS services, and includes best practices and recommendations for running Iceberg on AWS at scale while optimizing cost and performance.

Whether you're just starting out with Iceberg or you're an experienced user looking to optimize your existing Iceberg workloads on AWS, this guide offers valuable insights for every stage of your project

In this guide: