# Network and database configuration requirements - Amazon Quick

**Source:** [https://docs.aws.amazon.com/quick/latest/userguide/configure-access.html](https://docs.aws.amazon.com/quick/latest/userguide/configure-access.html)

---

To serve as data sources, databases need to be configured so that Amazon Quick can access them. Use the following sections to make sure that your database is configured appropriately.

###### Important

Because a database instance on Amazon EC2 is administered by you rather than AWS, it must
            meet both the [Network configuration requirements](https://docs.aws.amazon.com/quicksuite/latest/userguide/configure-access.html#network-configuration-requirements) as well as the
                [Database configuration requirements for self-administered
                instances](https://docs.aws.amazon.com/quicksuite/latest/userguide/configure-access.html#database-configuration-requirements).

###### Topics

## Network configuration requirements

        | Intended audience: System administrators | 

For you to use your database server from Amazon Quick, your server must be accessible from the internet. It must also allow inbound traffic from Amazon Quick servers.

If the database is on AWS and in the same AWS Region as your Amazon Quick account,
            you can auto-discover the instance to make connecting to it easier. To do this, you must
            grant Amazon Quick permissions to access it. For more information, see [Accessing data sources](https://docs.aws.amazon.com/quicksight/latest/user/access-to-aws-resources.html).

###### Topics

### Network configuration for an AWS instance in a default VPC

In some cases, your database might be on an AWS cluster or instance that you created in a default VPC. Thus, it's publicly accessible (that is, you didn't choose to make it private). In such cases, your database is already appropriately configured to be accessible from the internet. However, you still need to enable access from Amazon Quick servers to your AWS cluster or instance. For further details on how to do this, choose the appropriate topic following:

### Network configuration for an AWS instance in a nondefault VPC

If you are configuring an AWS instance in a nondefault VPC, make sure that the instance is publicly accessible and that the VPC has the following:

- 
                    An internet gateway. 
- 
                    A public subnet. 
- 
                    A route in the route table between the internet gateway and the AWS instance. 
- 
                    Network access control lists (ACLs) in your VPC that allow traffic between the cluster or instance and Amazon Quick servers. These ACLs must do the following: - 
                            Allow inbound traffic from the appropriate Amazon Quick IP address range and all ports to the IP address and port that the database is listening on. 
- 
                            Allow outbound traffic from the database’s IP address and port to the appropriate Amazon Quick IP address range and all ports. 
 For more information about Amazon Quick IP address ranges, see [IP address ranges for Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/regions.html)following.For more information about configuring VPC ACLs, see [Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_ACLs.html).
- 
                            
- 
                    Security group rules that allow traffic between the cluster or instance and Amazon Quick servers. For further details on how to create appropriate security group rules, see [Authorizing connections to AWS data sources](https://docs.aws.amazon.com/quicksight/latest/user/enabling-access.html).

For more information about configuring a VPC in the Amazon VPC service, see [Networking in Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Networking.html).

### Network configuration for an AWS instance in a private VPC

If your database is on an AWS cluster or instance that you created in a private
                VPC, you can use it with Amazon Quick. For more information, see [Connecting to a Amazon VPC with Amazon Quick](https://docs.aws.amazon.com/quicksight/latest/user/working-with-aws-vpc.html).

For more information on Amazon VPC, see [Amazon VPC](https://aws.amazon.com/vpc/) and 

[Amazon VPC Documentation](https://docs.aws.amazon.com/vpc/).

### Network configuration for an AWS instance that is not in a VPC

If you are configuring an AWS instance that is not in a VPC, make sure that the instance is publicly accessible. Also, make sure that there is a security group rule that allows traffic between the cluster or instance and Amazon Quick servers. For further details on how to do this, choose the appropriate topic following:

### Network configuration for a database instance other than AWS

To use SSL to secure your connections to your database
                    (*recommended*), make sure that you have a certificate signed
                by a recognized certificate authority (CA). Amazon Quick doesn't accept certificates
                that are self-signed or issued from a nonpublic CA. For more information, see [Amazon Quick SSL and CA certificates](https://docs.aws.amazon.com/quicksuite/latest/userguide/configure-access.html#database-configuration-requirements).

If your database is on a server other than AWS, you must change that server's
                firewall configuration to accept traffic from the appropriate Amazon Quick IP
                address range. For more information about Amazon Quick IP address ranges, see [IP address
                    ranges for Amazon Quick](https://docs.aws.amazon.com/quicksuite/latest/userguide/regions.html). For any other steps that you need to take to
                enable internet connectivity, see your operating system documentation.

#### Amazon Quick SSL and CA certificates

We recommend that you use a public certificate issued by
                    [AWS
                    Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/). Amazon Quick supports the same
                    certificate authorities (CAs) as Mozilla, so if you don't use ACM, use a
                    certificate issued by a CA on the [Mozilla Included
                        CA Certificate List](https://wiki.mozilla.org/CA/Included_Certificates).

#### IP address ranges for Amazon Quick

For more information on the IP address ranges for Amazon Quick in supported
                    Regions, see [AWS Regions, websites, IP address ranges, and
                        endpoints](https://docs.aws.amazon.com/quicksight/latest/user/regions.html).

## Database configuration requirements for self-administered instances

        | Intended audience: System administrators and Amazon Quick administrators | 

For a database to be accessible to Amazon Quick, it must meet the following criteria:

- 
                It must be accessible from the internet. To enable internet connectivity, see your database management system documentation. 
- 
                It must be configured to accept connections and authenticate access using the user credentials that you provide as part of creating the data set. 
- 
                If you are connecting to MySQL or PostgreSQL, the database engine must be accessible from your host or IP range. This optional security limitation is specified in MySQL or PostgreSQL connection settings. If this limitation is in place, any attempt to connect from a nonspecified host or IP address is rejected, even if you have the correct username and password. 
- 
                In MySQL, the server accepts the connection only if the user and host are verified in the user table. For more information, see [Access Control, Stage 1: Connection Verification](https://dev.mysql.com/doc/refman/5.7/en/connection-access.html)in the MySQL documentation.
- 
                In PostgreSQL, you control client authentication by using the `pg_hba.conf`file in the database cluster's data directory. However, this file might be named and located differently on your system. For more information, see[Client Authentication](https://www.postgresql.org/docs/9.3/static/client-authentication.html)in the PostgreSQL documentation.