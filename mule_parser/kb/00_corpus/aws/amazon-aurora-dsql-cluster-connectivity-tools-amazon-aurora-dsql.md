# Amazon Aurora DSQL cluster connectivity tools - Amazon Aurora DSQL

**Source:** [https://docs.aws.amazon.com/aurora-dsql/latest/userguide/aws-sdks.html](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/aws-sdks.html)

---

Aurora DSQL is compatible with many third-party database drivers and ORM libraries. AWS provides two types of tools to simplify working with Aurora DSQL:

- 
                [Connectors](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_connectors.html)
- 
                **Adapters and dialects**– Extensions for specific ORM frameworks that provide IAM authentication and improved Aurora DSQL compatibility. Use adapters when working with a supported ORM framework.

## Aurora DSQL adapters and dialects

                The following table shows the available adapters and dialects for Aurora DSQL.

| Programming language | ORM/Framework | Repository link | 
|---|---|---|
| Java | Hibernate | [https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate](https://github.com/awslabs/aurora-dsql-orms/tree/main/java/hibernate) | 
| Python | Django | [https://github.com/awslabs/aurora-dsql-orms/tree/main/python/django](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/django) | 
| Python | SQLAlchemy | [https://github.com/awslabs/aurora-dsql-orms/tree/main/python/sqlalchemy](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/sqlalchemy) | 
| Python | Tortoise ORM | [https://github.com/awslabs/aurora-dsql-orms/tree/main/python/tortoise-orm](https://github.com/awslabs/aurora-dsql-orms/tree/main/python/tortoise-orm) | 

## Database driver samples

                The following table shows sample code for connecting to Aurora DSQL using third-party database drivers.

## ORM and framework samples

                The following table shows sample code for using third-party ORM libraries and frameworks with Aurora DSQL.